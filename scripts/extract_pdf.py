#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
通用 PDF 配置手册提取脚本 (适配 FortiOS / 飞塔 等「按命令族组织」的手册)
============================================================================

将厂商配置手册 PDF 按 map.json 定义的主题分组，提取为 references/*.md 文件。

支持两种映射模式（可混用）：
  * sections 模式（推荐，适配 FortiOS）：按 TOC 节点的「标题/层级」匹配。
      - 每个 section: {"level": <TOC层级>, "title": "<标题或前缀>", "prefix": true/false}
      - prefix=true 时按标题前缀匹配（如 "config firewall address" 同时匹配 address6）
      - 适用于按 config <family> / execute / diagnose 命令族组织的手册
  * chapters 模式（兼容 StoneOS 等按章节号组织的手册）：按 L1 章节号聚合。
      - 每个 theme 含 "chapters": [num, ...]

用法:
    python3 extract_pdf.py <pdf_path> --map map.json --output <references_dir>

特性:
    - 基于 PDF 书签(TOC) 计算节点页码范围（含其所有子节点）
    - 自动清洗文本：安全重建被软连字符断开的词（保留连字符，仅去掉换行）
    - reference 内容以 PDF 为唯一真相，修正必须重跑本脚本（禁止手改）
"""

import argparse
import json
import os
import re
import sys

import fitz  # PyMuPDF


# --------------------------------------------------------------------------- #
# 文本清洗
# --------------------------------------------------------------------------- #
def clean_text(text):
    """清洗提取出的文本。

    关键：只处理「连字符紧跟换行」(软连字符断词) 的情况，保留连字符、仅去除换行，
    以同时正确还原散文词 (fabric-object) 与可能带连字符的命令 token (per-ip-shaper)。
    绝不盲目合并字母，避免破坏 CLI。
    """
    # 软连字符断词：连字符在行尾 -> 去掉换行但保留连字符
    text = re.sub(r'-\n', '-', text)
    # 去除行尾孤立的页码标记如 "- 395 -"
    text = re.sub(r'^\s*-\s*\d+\s*-\s*$', '', text, flags=re.MULTILINE)
    # 合并多余空行
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


# --------------------------------------------------------------------------- #
# TOC 解析
# --------------------------------------------------------------------------- #
def load_flat_toc(doc):
    """返回扁平 TOC: [(level, title, page), ...] 保持文档顺序。"""
    return [(item[0], item[1], item[2]) for item in doc.get_toc()]


def node_range(flat, i):
    """计算节点 i 的内容结束页：取其后第一个层级 <= 当前层级的节点的起始页 - 1。

    健壮性：若 TOC 页码乱序导致算出的结束页早于起始页（例如两个书签同页），
    则回退为起始页本身，保证该节点至少提取到自己的那一页，避免整段内容丢失。
    """
    level_i = flat[i][0]
    start = flat[i][2]
    for j in range(i + 1, len(flat)):
        if flat[j][0] <= level_i:
            end = flat[j][2] - 1
            return end if end >= start else start
    return None  # 直到文档末尾


def extract_range(doc, start_page, end_page, verbose=True):
    """提取 [start_page, end_page] 范围内的全部页文本。"""
    pages = []
    s = max(0, start_page - 1)
    e = min(doc.page_count - 1, end_page - 1) if end_page else doc.page_count - 1
    for pn in range(s, e + 1):
        txt = doc[pn].get_text()
        if txt.strip():
            pages.append("\n<!-- 来源页 %d -->\n" % (pn + 1) + clean_text(txt))
    if verbose:
        print("    提取 p%d-%d -> %d 页文本" % (start_page, end_page, len(pages)))
    return "\n".join(pages)


# --------------------------------------------------------------------------- #
# 两种映射模式
# --------------------------------------------------------------------------- #
def match_sections(flat, theme):
    """sections 模式：返回需要提取的 (节点下标集合, 匹配标题列表)。"""
    idxs = set()
    matched_titles = []
    for spec in theme.get("sections", []):
        lvl = spec.get("level")
        title = spec.get("title", "")
        prefix = spec.get("prefix", False)
        for i, (cl, ct, cp) in enumerate(flat):
            if cl != lvl:
                continue
            if ct == title or (prefix and ct.lower().startswith(title.lower())):
                idxs.add(i)
                matched_titles.append(ct)
    return idxs, matched_titles


def match_chapters(doc, flat, theme):
    """chapters 模式（兼容）：按 L1 章节号聚合，返回 (idxs, titles)。"""
    # 建立 L1 章节起始节点索引
    l1 = [(i, cl, ct, cp) for i, (cl, ct, cp) in enumerate(flat) if cl == 1]
    idxs = set()
    titles = []
    for cnum in theme.get("chapters", []):
        for i, cl, ct, cp in l1:
            m = re.match(r'^\s*(\d+)\s*(.*)$', ct)
            num = int(m.group(1)) if m else None
            if num == cnum:
                idxs.add(i)
                titles.append(ct)
                break
    return idxs, titles


# --------------------------------------------------------------------------- #
# 主流程
# --------------------------------------------------------------------------- #
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf", help="源 PDF 路径")
    ap.add_argument("--map", default="map.json", help="主题映射 JSON")
    ap.add_argument("--output", default="references", help="输出目录")
    args = ap.parse_args()

    if not os.path.exists(args.map):
        print("[ERROR] map 文件不存在: %s" % args.map, file=sys.stderr)
        sys.exit(1)

    with open(args.map, "r", encoding="utf-8") as f:
        cfg = json.load(f)

    os.makedirs(args.output, exist_ok=True)
    doc = fitz.open(args.pdf)
    print("PDF: %s  总页数=%d" % (args.pdf, doc.page_count))

    flat = load_flat_toc(doc)
    print("TOC 节点总数: %d" % len(flat))

    index_entries = []
    for theme in cfg["themes"]:
        key = theme["key"]
        title = theme["title"]
        out_path = os.path.join(args.output, "%s.md" % key)
        print("\n[提取] %s - %s" % (key, title))

        if theme.get("sections") is not None:
            idxs, matched = match_sections(flat, theme)
        elif theme.get("chapters") is not None:
            idxs, matched = match_chapters(doc, flat, theme)
        else:
            print("    [SKIP] 未定义 sections 或 chapters")
            continue

        if not idxs:
            print("    [WARN] 未匹配到任何 TOC 节点，跳过")
            continue

        collected = []
        # 按文档顺序提取，避免乱序
        for i in sorted(idxs):
            cl, ct, cp = flat[i]
            end = node_range(flat, i)
            collected.append(extract_range(doc, cp, end if end else doc.page_count))

        body = "\n\n---\n\n".join(collected)
        header = (
            "# %s\n\n" % title
            + "> 来源: %s\n" % cfg.get("source_pdf", "官方配置手册")
            + "> 覆盖命令/章节: %s\n" % ", ".join(matched)
            + "> 本文件由 extract_pdf.py 从官方 PDF 自动提取，请勿手动编辑；\n"
            + "> 如需修正请修改 map.json 后重跑脚本。\n\n---\n\n"
        )
        content = header + body + "\n"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content)
        size = len(content)
        print("    已保存 %s (%d 字符, %d 节点)" % (out_path, size, len(idxs)))
        index_entries.append((key, title, theme.get("desc", ""), size))

    doc.close()

    idx_path = os.path.join(args.output, "index.md")
    lines = ["# 配置参考索引\n",
             "> 本索引由 extract_pdf.py 自动生成，按业务主题聚合官方 CLI。\n\n",
             "| 文件 | 主题 | 内容 | 大小 |\n", "|---|---|---|---|\n"]
    for key, title, desc, size in index_entries:
        lines.append("| `%s.md` | %s | %s | %d |\n" % (key, title, desc, size))
    with open(idx_path, "w", encoding="utf-8") as f:
        f.write("".join(lines))
    print("\n[完成] 索引已生成: %s" % idx_path)
    print("[完成] 共提取 %d 个主题文件" % len(index_entries))


if __name__ == "__main__":
    main()
