# FortiGate / FortiOS 防火墙配置 CLI 生成工具

[📖 English version: README_EN.md](README_EN.md)

> 一个基于官方《FortiOS 8.0.0 CLI Reference》自动生成的 **防火墙配置 CLI 生成 Skill**，
> 面向所有 AI Agent 通用。用自然语言描述需求即可输出可复制的 FortiGate 配置命令。

## 简介

本仓库将 Fortinet 官方《FortiOS 8.0.0 CLI Reference》（共 4268 页）按业务主题结构化提取为
一份「配置 CLI 生成 Skill」，帮助网络工程师通过自然语言快速生成 FortiGate 防火墙的配置命令，
覆盖安全策略、NAT、接口、路由、VPN、HA、用户认证、威胁防护、应用控制、日志等常见场景。

**特点**

- 📚 **权威来源**：所有命令提取自官方 CLI 手册，未做任何人工编造。
- 🧩 **多模块组合**：支持跨主题组合（如 接口 + 安全策略 + NAT + IPS + VPN + 路由 + HA）。
- 📋 **双格式输出**：每次同时给出「纯净可复制 CLI」与「带中文注释的 CLI 详解」。
- 🌐 **双语**：中文 / English 双版本说明。
- 🤖 **Agent 通用**：不依赖任何特定 Agent 平台，任何支持 Skill 机制的 AI Agent 均可加载使用。

## 配置主题覆盖

| 文件 | 主题 | 内容 |
|---|---|---|
| `00-cli-basics.md` | CLI 基础与命令树 | 命令可用性、全局命令树、config/edit/set 配置模式基础 |
| `01-system-interfaces.md` | 接口 / Zone / 隧道 / VDOM | 物理/逻辑接口、Zone、聚合/软件交换、各类隧道、VDOM |
| `02-system-network.md` | DNS / DHCP / NTP / SNMP / SDWAN | 域名解析、地址分配、时间同步、网管、SDWAN、链路监测 |
| `03-system-admin.md` | 管理 / AAA / 认证 / 消息 | 管理员与权限、API 用户、SSO/SAML、集中管理、替换消息、自动化 |
| `04-system-ha.md` | 高可用 (HA) 与集群 | 双机热备、HA 监控、独立集群 |
| `05-firewall-policy.md` | 安全策略 / 地址 / 服务 / 调度 | IPv4/IPv6/NGFW 策略、地址/地址组、服务对象/组、调度、安全配置文件 |
| `06-firewall-nat.md` | NAT (IP池 / 虚拟IP / 中心SNAT) | 源 NAT、IP 池、虚拟 IP、中心 NAT 映射 |
| `07-firewall-advanced.md` | 多播/接口策略/本地策略/DoS/限速/嗅探/反向代理 | 高级防火墙特性 |
| `08-router.md` | 路由 | 静态/OSPF/BGP/RIP/ISIS/策略路由/路由映射/BFD |
| `09-vpn.md` | VPN | IPsec / SSL VPN / 拨号 / IKE |
| `10-user-auth.md` | 用户 / 认证 / 证书 | 本地用户、LDAP/RADIUS/TACACS、证书/PKI |
| `11-utm-antivirus-ips.md` | 威胁防护 | 防病毒 / IPS / 虚拟补丁 |
| `12-utm-web-filter.md` | 内容安全 | Web 过滤 / DNS 过滤 / 邮件过滤 / 文件过滤 |
| `13-app-control.md` | 应用控制 | 应用识别与管控 |
| `14-voip-dlp.md` | VoIP / DLP / CASB | 音视频协议过滤、数据防泄漏、CASB |
| `15-waf.md` | WAF | Web 应用防火墙 |
| `16-log-report.md` | 日志 / 报表 / 监控 / 告警 | 日志与报表、监控、告警邮件 |
| `17-ztna.md` | 零信任 (ZTNA) | 零信任网络访问 |
| `18-switch-wireless.md` | 交换机 / 无线 / 扩展控制器 | 托管交换、无线 AP/SSID、扩展设备 |
| `19-automation-cloud.md` | 自动化 / 云集成 / WAN优化 | 自动化、AWS/Azure/NSX、WAN 优化 |
| `20-execute.md` | 运维命令 (execute) | 备份/恢复/重启/上传下载等运行时命令 |
| `21-diagnose.md` | 诊断命令 (diagnose) | 故障排查与调试命令 |

> 完整索引见 [`references/index.md`](references/index.md)。

## 目录结构

```
fortinet-fortigate-cli-generator/
├── SKILL.md                 # Skill 定义（触发词 + 路由表 + 工作流 + 双格式输出）
├── README.md                # 中文说明（本文件）
├── README_EN.md             # English 说明
├── references/              # 各业务主题的官方 CLI 提取（由脚本自动生成）
│   ├── index.md
│   ├── 00-cli-basics.md
│   ├── 01-system-interfaces.md
│   └── ...（共 22 个主题文件）
└── scripts/
    ├── extract_pdf.py       # 通用 PDF → reference 提取脚本
    └── map.json             # 主题分组映射（可修改后重跑提取）
```

## 工作原理

1. 用户用自然语言描述配置需求（例如"配置一条允许内网访问外网的安全策略并做源 NAT"）。
2. Skill 根据路由表判断涉及的配置主题，加载对应的 `references/*.md`。
3. 在 reference 中匹配最贴近的官方命令模板，进行参数化替换。
4. 输出**双格式**：纯净可复制 CLI + 带中文注释的详解表。

## 快速开始

将本仓库作为 Skill 加载到支持 Skill 机制的 Agent 中即可。例如：

```
帮我在 FortiGate 上配置：
接口 port2 接内网 192.168.1.0/24，port1 接外网；
允许内网访问外网并做源 NAT，同时开启防病毒与 IPS 检查。
```

Skill 会自动加载 `01-system-interfaces` + `05-firewall-policy` + `06-firewall-nat`
+ `11-utm-antivirus-ips` 并组合输出。

## 重新生成参考文件

所有 `references/*.md` 均由官方 PDF 自动提取，**请勿手动编辑**。如需重新生成或调整分组：

```bash
pip install PyMuPDF
python scripts/extract_pdf.py <FortiOS-CLI-Reference.pdf> \
    --map scripts/map.json --output references
```

修改 `scripts/map.json` 中的主题分组后重跑脚本即可。

## 免责声明

本仓库内容提取自 Fortinet 官方公开手册《FortiOS 8.0.0 CLI Reference》，仅供学习与研究使用。
如有侵权，请主动与我联系，随时删除。工作邮箱：jeffchenchen@foxmail.com

---

© 本工具为社区学习用途整理，FortiGate / FortiOS 为 Fortinet, Inc. 的商标。
