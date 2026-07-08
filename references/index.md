# 配置参考索引
> 本索引由 extract_pdf.py 自动生成，按业务主题聚合官方 CLI。

| 文件 | 主题 | 内容 | 大小 |
|---|---|---|---|
| `00-cli-basics.md` | FortiOS CLI 基础与命令树 | 命令可用性说明、全局命令树结构，理解 config/edit/set/next/end 配置模式的基础 | 3685 |
| `01-system-interfaces.md` | 系统：接口 / Zone / 隧道 / VDOM | 物理/逻辑接口、Zone、聚合/软件交换机、虚拟线对、各类隧道(gre/ipip/ipv6/sit/geneve/vxlan/pppoe)、VDOM 与 VDOM 链路 | 145029 |
| `02-system-network.md` | 系统：DNS / DHCP / NTP / SNMP / SDWAN / 全局 | DNS、DHCP 服务、NTP、SNMP、NetFlow/sFlow、SDWAN、链路监测、全局与基础设置、会话、IPAM | 259078 |
| `03-system-admin.md` | 系统：管理 / AAA / 认证 / 消息 / 自动化 | 管理员与权限(accprofile)、API 用户、密码策略、SSO/SAML、集中管理(CSF/FortiManager)、FortiGuard、替换消息、邮件/SMS 服务器、自动化 stitch | 134046 |
| `04-system-ha.md` | 系统：高可用 (HA) 与集群 | HA 双机热备、HA 监控、独立集群(standalone-cluster)、管理隧道、自动扩缩容 | 34171 |
| `05-firewall-policy.md` | 防火墙：安全策略 / 地址 / 服务 / 调度 | IPv4/IPv6 安全策略、NGFW 安全策略、地址/地址组(含IPv6/wildcard-fqdn)、服务对象/组、调度、安全配置文件组与 ssl-ssh-profile、互联网服务、代理策略 | 263680 |
| `06-firewall-nat.md` | 防火墙：NAT (IP池 / 虚拟IP / 中心SNAT) | IP 池(ippool, 含IPv6)、虚拟 IP(vip/vipgrp, 含IPv6)、中心 NAT 映射(central-snat-map)、IP 转换、DNS 翻译 | 107656 |
| `07-firewall-advanced.md` | 防火墙：多播/接口策略/本地策略/DoS/限速/嗅探/反向代理 | 多播策略与地址、接口策略、本地入站策略(local-in)、DoS 策略、TTL 策略、流量整形(shaper/shaping-policy)、嗅探、访问代理(access-proxy)、SSL/SSH 设置、IP-MAC 绑定、认证门户 | 172548 |
| `08-router.md` | 路由 | 静态路由、默认路由、OSPF/OSPF6、BGP、RIP、ISIS、策略路由、路由映射(route-map)、BGP 社区、BFD、组播路由(PIM) | 209751 |
| `09-vpn.md` | VPN (IPsec / SSL / 拨号) | IPsec 阶段1/2、IKE、SSL VPN、拨号(拨号接口)、L2TP、GRE over IPsec、证书绑定 | 221078 |
| `10-user-auth.md` | 用户 / 认证 / 证书 | 本地用户与用户组、LDAP/RADIUS/TACACS+/FSSO 服务器、认证方案与规则、PKI 证书(CA/本地/证书远程)、guest 用户 | 138529 |
| `11-utm-antivirus-ips.md` | 威胁防护：防病毒 / IPS / 虚拟补丁 | 防病毒配置文件、IPS 传感器与规则、虚拟补丁(virtual-patch)防护 | 81685 |
| `12-utm-web-filter.md` | 内容安全：Web过滤/DNS过滤/邮件代理/文件过滤 | Web 过滤、DNS 过滤、Web 代理、FTP 代理、邮件过滤、文件过滤(文件类型阻断) | 134297 |
| `13-app-control.md` | 应用控制 | 应用识别列表、应用分组、自定义应用、应用控制列表与规则、分类设置 | 23377 |
| `14-voip-dlp.md` | VoIP / DLP / CASB / 其他协议过滤 | VoIP 配置、视频过滤、数据防泄漏(DLP)、CASB、Diameter/SCTP/SSH 协议过滤 | 104311 |
| `15-waf.md` | WAF (Web 应用防火墙) | WAF 配置文件、签名、约束(constraint)、方法(method)与规则 | 25618 |
| `16-log-report.md` | 日志 / 报表 / 监控 / 告警邮件 | 日志设置(磁盘/远程/FortiAnalyzer)、日志过滤、报表配置、监控设置、告警邮件(alertemail) | 287061 |
| `17-ztna.md` | 零信任网络访问 (ZTNA) | ZTNA 代理、ZTNA 规则、ZTNA 服务器与标签 | 67799 |
| `18-switch-wireless.md` | 交换机 / 无线 / 扩展控制器 | Switch Controller(托管交换机)、Wireless Controller(AP/SSID)、Extension Controller(扩展设备)、以太网 OAM | 566843 |
| `19-automation-cloud.md` | 自动化 / 云集成 / WAN优化 / 其他 | 自动化(automation 配置)、AWS/Azure/NSX-T 连接器、遥测控制器、WAN 优化、终端控制、ICAP、LLM、DPDK | 148745 |
| `20-execute.md` | 运维命令 (execute) | 备份/恢复/重启/出厂重置/配置事务/接口/路由/HA/更新/上传下载/Ping/Traceroute/抓包等运行时命令 | 254098 |
| `21-diagnose.md` | 诊断命令 (diagnose) | 故障排查命令：防火墙/路由/IP/IPv6/IPS/VPN/SNMP/NPU/LLDP/调试/嗅探/硬件/日志等 diagnose 子命令 | 1075346 |
