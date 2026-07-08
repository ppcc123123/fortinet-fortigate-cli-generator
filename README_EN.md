# FortiGate / FortiOS Firewall Configuration CLI Generator

[📖 中文版： README.md](README.md)

> A **firewall configuration CLI generator Skill** automatically built from the official
> *FortiOS 8.0.0 CLI Reference*, designed to be **agent-agnostic**. Describe your need in
> natural language and get copy-ready FortiGate configuration commands.

## Overview

This repository structures the official *FortiOS 8.0.0 CLI Reference* (4,268 pages) into a
**configuration CLI generation Skill**, helping network engineers produce FortiGate firewall
configuration commands from natural-language requests. It covers common scenarios such as
security policies, NAT, interfaces, routing, VPN, HA, user authentication, threat protection,
application control, and logging.

**Highlights**

- 📚 **Authoritative source**: every command is extracted from the official CLI reference — no hand-written commands.
- 🧩 **Multi-module composition**: combine across topics (e.g. interfaces + policy + NAT + IPS + VPN + routing + HA).
- 📋 **Dual-format output**: each response gives both *clean copy-ready CLI* and *annotated CLI with explanations*.
- 🌐 **Bilingual**: Chinese / English documentation.
- 🤖 **Agent-agnostic**: not tied to any specific agent platform; usable by any agent that supports the Skill mechanism.

## Covered Topics

| File | Topic | Contents |
|---|---|---|
| `00-cli-basics.md` | CLI basics & command tree | Command availability, global command tree, config/edit/set mode basics |
| `01-system-interfaces.md` | Interfaces / Zone / Tunnels / VDOM | Physical/logical interfaces, zones, aggregates, tunnels, VDOM |
| `02-system-network.md` | DNS / DHCP / NTP / SNMP / SDWAN | Name resolution, address assignment, time sync, NMS, SDWAN, link monitor |
| `03-system-admin.md` | Management / AAA / Auth / Messaging | Admins & permissions, API users, SSO/SAML, central management, replacement messages, automation |
| `04-system-ha.md` | High Availability (HA) & clustering | Active-active/passive failover, HA monitoring, standalone cluster |
| `05-firewall-policy.md` | Security policy / Address / Service / Schedule | IPv4/IPv6/NGFW policy, address/addrgrp, service objects/groups, schedule, security profiles |
| `06-firewall-nat.md` | NAT (IP pool / Virtual IP / Central SNAT) | Source NAT, IP pools, virtual IP, central SNAT mapping |
| `07-firewall-advanced.md` | Multicast / Interface policy / Local policy / DoS / Shaping / Sniffer / Reverse proxy | Advanced firewall features |
| `08-router.md` | Routing | Static / OSPF / BGP / RIP / ISIS / policy route / route-map / BFD |
| `09-vpn.md` | VPN | IPsec / SSL VPN / dialup / IKE |
| `10-user-auth.md` | User / Auth / Certificate | Local users, LDAP/RADIUS/TACACS, certificates/PKI |
| `11-utm-antivirus-ips.md` | Threat protection | Antivirus / IPS / virtual-patch |
| `12-utm-web-filter.md` | Content security | Web filter / DNS filter / email filter / file filter |
| `13-app-control.md` | Application control | Application identification & control |
| `14-voip-dlp.md` | VoIP / DLP / CASB | Voice/video protocol filters, DLP, CASB |
| `15-waf.md` | WAF | Web application firewall |
| `16-log-report.md` | Logging / Reports / Monitoring / Alert | Logs, reports, monitoring, alert email |
| `17-ztna.md` | Zero Trust (ZTNA) | Zero-trust network access |
| `18-switch-wireless.md` | Switch / Wireless / Extension controller | Managed switch, wireless AP/SSID, extension devices |
| `19-automation-cloud.md` | Automation / Cloud / WAN optimization | Automation, AWS/Azure/NSX, WAN optimization |
| `20-execute.md` | Operational commands (execute) | Backup/restore/reboot/upload/download and runtime commands |
| `21-diagnose.md` | Diagnostic commands (diagnose) | Troubleshooting and debugging commands |

> Full index in [`references/index.md`](references/index.md).

## Directory Layout

```
fortinet-fortigate-cli-generator/
├── SKILL.md                 # Skill definition (triggers + routing table + workflow + dual-format output)
├── README.md                # Chinese documentation
├── README_EN.md             # English documentation (this file)
├── references/              # Official CLI extracts per topic (auto-generated)
│   ├── index.md
│   ├── 00-cli-basics.md
│   ├── 01-system-interfaces.md
│   └── ... (22 topic files in total)
└── scripts/
    ├── extract_pdf.py       # Generic PDF -> reference extractor
    └── map.json             # Topic grouping map (edit then re-run to regenerate)
```

## How It Works

1. The user describes a configuration need in natural language.
2. The Skill routes to the relevant topic(s) and loads the corresponding `references/*.md`.
3. It matches the closest official command template and substitutes the user's parameters.
4. It outputs **dual format**: clean copy-ready CLI + annotated explanation table.

## Quick Start

Load this repository as a Skill into any agent that supports the Skill mechanism. Example:

```
On my FortiGate:
port2 = internal 192.168.1.0/24, port1 = external;
allow internal to access internet with source NAT, and enable antivirus + IPS inspection.
```

The Skill will automatically load `01-system-interfaces` + `05-firewall-policy` + `06-firewall-nat`
+ `11-utm-antivirus-ips` and compose the output.

## Regenerating Reference Files

All `references/*.md` are auto-extracted from the official PDF — **do not edit manually**.
To regenerate or adjust grouping:

```bash
pip install PyMuPDF
python scripts/extract_pdf.py <FortiOS-CLI-Reference.pdf> \
    --map scripts/map.json --output references
```

Edit `scripts/map.json` to change topic grouping, then re-run the script.

## Disclaimer

The content of this repository is extracted from the official public manual
*FortiOS 8.0.0 CLI Reference* by Fortinet, for learning and research purposes only.
If any content infringes copyright, please contact me and it will be removed promptly.
Work email: jeffchenchen@foxmail.com

---

© Compiled for community learning purposes. FortiGate / FortiOS are trademarks of Fortinet, Inc.
