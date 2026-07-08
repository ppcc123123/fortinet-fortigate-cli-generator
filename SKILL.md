---
name: fortinet-fortigate-cli-generator
description: >-
  Fortinet FortiGate / FortiOS 防火墙配置 CLI 生成工具。
  基于官方《FortiOS 8.0.0 CLI Reference》提取的权威 CLI 命令与配置模板。
  当用户需要进行 FortiGate / FortiOS 防火墙配置时使用，
  包括但不限于：安全策略配置（IPv4/IPv6/NGFW）、地址/地址组/服务对象、NAT（源NAT/IP池/虚拟IP/中心SNAT）、
  接口与 Zone 配置、路由配置（静态/OSPF/BGP/RIP/策略路由）、
  VPN 配置（IPsec/SSL VPN/IKE）、高可靠性配置（HA 双机热备）、
  用户与认证（本地用户/LDAP/RADIUS/TACACS/证书）、
  威胁防护（防病毒/IPS/虚拟补丁/WAF）、内容安全（Web过滤/DNS过滤/邮件过滤/文件过滤）、
  应用控制、VoIP/DLP/CASB、日志与报表、零信任（ZTNA）、
  交换机/无线控制器、自动化与云集成、以及 execute / diagnose 运维与诊断命令。
  支持自然语言描述需求（如"帮我配置一条允许内网 192.168.1.0/24 访问外网的安全策略并做源NAT"）
  和参数化输入。支持多模块组合配置（如 接口 + 安全策略 + NAT + IPS + VPN + 路由 + HA）。
  输出格式包含两部分：可直接复制的纯净 CLI 命令 + 带中文注释的 CLI 详解。
---

# FortiGate / FortiOS 防火墙配置助手

> 基于官方《FortiOS 8.0.0 CLI Reference》生成的配置 CLI 智能助手，
> 适用于 Fortinet FortiGate 全系列防火墙设备（FortiOS 8.0.0）。
> 所有命令均来自官方 CLI 手册，未经人工编造。

## 核心规则（铁律）

1. **以 PDF 为唯一真相**：所有 CLI 命令来源于官方 FortiOS CLI Reference，reference 文件由 `scripts/extract_pdf.py` 自动提取，**不可手动编造或修改命令**。
2. **先路由后加载**：先判断用户问题属于哪个配置主题，再加载对应 `references/<key>.md`，不要全量加载。
3. **双格式输出**：每次输出必须同时包含 (A) 纯净可复制 CLI 与 (B) 带中文注释的 CLI 详解表。
4. **参数化替换**：识别用户提供的 IP、端口、接口名、策略名、地址/服务对象名、Zone 名等参数并替换到模板。
5. **多模块组合**：当用户需求跨多个主题时，自动识别并合并多个 reference 文件，按依赖顺序输出、去重。
6. **中文优先**：所有解释与注释使用中文；命令本身保持英文原文。

## FortiOS 配置语法速记（非 reference，通用规则）

FortiOS 采用层级配置模式，基本范式：

```
config <table>            # 进入配置表
    edit <name|id>        # 新建/编辑某条目（id 为整数或 name 为字符串）
        set <option> <value>   # 设置参数
        ...
    next                  # 保存当前条目，准备下一条
end                       # 退出配置模式并保存
```

- 查看：`show <table>` / `show full-configuration <table>`；退出配置可用 `abort` 放弃未提交改动。
- 布尔选项通常为 `enable` / `disable`；很多功能需 `set utm-status enable` 后才出现安全配置项。
- 接口名称区分大小写，常用 `port1`/`port2` 或自定义名；策略方向由 `srcintf`/`dstintf` 决定。

## 工作流

```
1. 理解意图   → 解析用户自然语言/参数，识别配置目标与涉及的模块
2. 路由到文件 → 根据下方路由表，确定需要加载的 references/<key>.md（1~N 个）
3. 匹配模板   → 在 reference 文件中检索最匹配的配置模板/命令块
4. 参数替换   → 将用户提供的 IP/端口/接口/名称填入模板
5. 双格式输出 → 纯净 CLI + 带中文注释的 CLI 详解表
6. 验证命令   → 附上对应的 show/diagnose 验证命令（如 reference 中有）
```

## 多模块组合规则

当用户需求涉及多个主题（例如"配置 IPsec VPN 并做源 NAT 穿透 + 威胁防护 + HA"），必须：

1. **识别所有相关主题**：用路由表关键词匹配，加载全部相关 reference 文件。
2. **按依赖排序输出**：
   - 基础先行：接口/Zone 配置 → 地址/服务对象 → 路由 → 安全策略 → NAT → VPN → 威胁防护 → 日志/HA → 监控
   - 例如 VPN 依赖接口 IP 与路由；安全策略引用地址/服务对象；NAT 依赖接口与地址；威胁防护绑定到策略。
3. **去重**：相同命令（如进入某配置表）只出现一次，用注释标明其作用范围。
4. **分段标注**：每个模块用 `## 模块X：<主题名>` 分隔，段内给出纯净 CLI + 注释。

## 主题路由表

| 用户提及关键词 | reference 文件 | 主题 |
|---|---|---|
| CLI、命令树、配置模式、config/edit/set/end、可用性 | `00-cli-basics.md` | FortiOS CLI 基础与命令树 |
| 接口、interface、zone、聚合、隧道、gre、ipip、ipv6-tunnel、vxlan、geneve、pppoe、vdom、虚拟系统 | `01-system-interfaces.md` | 系统：接口/Zone/隧道/VDOM |
| DNS、DHCP、NTP、SNMP、netflow、sflow、sdwan、链路监测、全局设置、global、session、IPAM | `02-system-network.md` | 系统：DNS/DHCP/NTP/SNMP/SDWAN/全局 |
| 管理员、admin、权限、accprofile、API用户、密码策略、SSO、SAML、集中管理、FortiManager、替换消息、邮件服务器、自动化stitch | `03-system-admin.md` | 系统：管理/AAA/认证/消息/自动化 |
| HA、双机热备、高可靠、集群、standalone-cluster、会话同步 | `04-system-ha.md` | 系统：高可用(HA)与集群 |
| 安全策略、policy、security policy、地址、address、addrgrp、服务、service、调度、schedule、profile-group、ssl-ssh-profile、互联网服务、代理策略 | `05-firewall-policy.md` | 防火墙：安全策略/地址/服务/调度 |
| NAT、源NAT、ippool、IP池、虚拟IP、vip、vipgrp、中心SNAT、central-snat、IP转换 | `06-firewall-nat.md` | 防火墙：NAT(IP池/虚拟IP/中心SNAT) |
| 多播、multicast、接口策略、interface-policy、local-in、本地策略、DoS、限速、shaper、整形、嗅探、sniffer、反向代理、access-proxy、ssl setting | `07-firewall-advanced.md` | 防火墙：多播/接口策略/本地策略/DoS/限速/嗅探/反向代理 |
| 路由、静态路由、OSPF、BGP、RIP、ISIS、策略路由、route-map、路由映射、BFD | `08-router.md` | 路由 |
| VPN、IPsec、IKE、phase1、phase2、SSL VPN、拨号、L2TP | `09-vpn.md` | VPN(IPsec/SSL/拨号) |
| 用户、user、本地用户、用户组、LDAP、RADIUS、TACACS、FSSO、认证、authentication、证书、certificate、CA、PKI | `10-user-auth.md` | 用户/认证/证书 |
| 防病毒、antivirus、IPS、入侵防御、虚拟补丁、virtual-patch、威胁防护 | `11-utm-antivirus-ips.md` | 威胁防护：防病毒/IPS/虚拟补丁 |
| Web过滤、webfilter、DNS过滤、dnsfilter、Web代理、邮件过滤、文件过滤、内容安全 | `12-utm-web-filter.md` | 内容安全：Web/DNS/邮件/文件过滤 |
| 应用控制、application、应用识别、app control | `13-app-control.md` | 应用控制 |
| VoIP、视频过滤、videofilter、DLP、CASB、Diameter、SCTP、SSH过滤 | `14-voip-dlp.md` | VoIP/DLP/CASB/其他协议过滤 |
| WAF、Web应用防火墙 | `15-waf.md` | WAF |
| 日志、log、报表、report、监控、monitoring、告警邮件、alertemail、FortiAnalyzer | `16-log-report.md` | 日志/报表/监控/告警邮件 |
| 零信任、ZTNA、SDP | `17-ztna.md` | 零信任网络访问(ZTNA) |
| 交换机、switch-controller、无线、wireless-controller、AP、SSID、扩展控制器、OAM | `18-switch-wireless.md` | 交换机/无线/扩展控制器 |
| 自动化、automation、AWS、Azure、NSX、遥测、WAN优化、wanopt、终端控制、ICAP | `19-automation-cloud.md` | 自动化/云集成/WAN优化/其他 |
| 备份、恢复、重启、出厂重置、execute、配置事务、上传、下载、ping、traceroute | `20-execute.md` | 运维命令(execute) |
| 诊断、diagnose、排错、故障排查、debug、抓包、sniffer | `21-diagnose.md` | 诊断命令(diagnose) |

> 完整索引见 `references/index.md`。

## 输出格式

### 格式 A：纯净 CLI（可直接复制粘贴）

```
config firewall policy
    edit 1
        set name "allow-internal-out"
        set srcintf "port2"
        set dstintf "port1"
        set srcaddr "internal-net"
        set dstaddr "all"
        set action accept
        set schedule "always"
        set service "ALL"
        set nat enable
        set logtraffic all
    next
end
```

### 格式 B：带中文注释的 CLI 详解（表格：`命令 | 说明`）

| 命令 | 说明 |
|---|---|
| `config firewall policy` | 进入 IPv4 安全策略配置表 |
| `edit 1` | 新建/编辑编号为 1 的策略 |
| `set name "allow-internal-out"` | 策略名称 |
| `set srcintf "port2"` | 源接口（内网侧） |
| `set dstintf "port1"` | 目的接口（外网侧） |
| `set srcaddr "internal-net"` | 引用源地址对象（需先建地址） |
| `set dstaddr "all"` | 目的地址 |
| `set action accept` | 动作允许 |
| `set schedule "always"` | 生效时间表 |
| `set service "ALL"` | 服务对象 |
| `set nat enable` | 开启源 NAT（出向地址转换） |
| `set logtraffic all` | 记录全部流量日志 |
| `next` / `end` | 保存条目 / 退出并保存 |

> 注：带注释版本中的说明是辅助理解，**命令本身必须与官方手册一致**；如需变更命令参数，回到对应 reference 文件核实。

## 边缘情况

- **无法匹配**：当用户需求不在任何 reference 覆盖范围内，明确告知并建议最接近的模块，不得编造命令。
- **版本差异**：本 Skill 基于 FortiOS 8.0.0；其他版本命令可能略有差异，生成时注明版本来源。
- **跨主题组合**：主动加载多个 reference 并按依赖顺序合并输出，避免遗漏前置对象（如策略引用的地址/服务需先创建）。
- **依赖前置**：涉及安全策略引用地址/服务/安全配置文件时，先输出被引用对象的创建命令，再输出策略本身。
