# 防火墙：NAT (IP池 / 虚拟IP / 中心SNAT)

> 来源: FortiOS-8.0.0-CLI_Reference.pdf
> 覆盖命令/章节: config firewall ippool, config firewall ippool6, config firewall vip, config firewall vip6, config firewall vipgrp, config firewall vipgrp6, config firewall central-snat-map, config firewall ip-translation, config firewall dnstranslation
> 本文件由 extract_pdf.py 从官方 PDF 自动提取，请勿手动编辑；
> 如需修正请修改 map.json 后重跑脚本。

---


<!-- 来源页 507 -->
Parameter
Description
Type
Size
Default
portal-addr6
IPv6 address (or FQDN) of authentication portal.
string
Maximum
length: 63
proxy-auth
Enable/disable authentication by proxy daemon
(default = disable).
option
-disable
Option
Description
enable
Users are authenticated by proxy daemon.
disable
Users are not authenticated by proxy daemon.
config firewall central-snat-map
Configure IPv4 and IPv6 central SNAT policies.
config firewall central-snat-map
Description: Configure IPv4 and IPv6 central SNAT policies.
edit <policyid>
set comments {var-string}
set custom-tags <name1>, <name2>, ...
set dst-addr <name1>, <name2>, ...
set dst-addr6 <name1>, <name2>, ...
set dst-port {user}
set dstintf <name1>, <name2>, ...
set nat [disable|enable]
set nat-ippool <name1>, <name2>, ...
set nat-ippool6 <name1>, <name2>, ...
set nat-port {user}
set nat46 [enable|disable]
set nat64 [enable|disable]
set orig-addr <name1>, <name2>, ...
set orig-addr6 <name1>, <name2>, ...
set orig-port {user}
set port-preserve [enable|disable]
set port-random [enable|disable]
set protocol {integer}
set srcintf <name1>, <name2>, ...
set status [enable|disable]
set type [ipv4|ipv6]
set uuid {uuid}
next
end
FortiOS 8.0.0 CLI Reference
507
Fortinet Inc.

<!-- 来源页 508 -->
config firewall central-snat-map
Parameter
Description
Type
Size
Default
comments
Comment.
var-string
Maximum
length: 1023
custom-tags
<name> *
Custom tags.
Names of custom tags used with this
policy.
string
Maximum
length: 35
dst-addr
<name>
IPv4 Destination address.
Address name.
string
Maximum
length: 79
dst-addr6
<name>
IPv6 Destination address.
Address name.
string
Maximum
length: 79
dst-port
Destination port or port range (1 to 65535,
0 means any port).
user
Not Specified
dstintf
<name>
Destination interface name from available
interfaces.
Interface name.
string
Maximum
length: 79
nat
Enable/disable source NAT.
option
-enable
Option
Description
disable
Disable source NAT.
enable
Enable source NAT.
nat-ippool
<name>
Name of the IP pools to be used to
translate addresses from available IP
Pools.
IP pool name.
string
Maximum
length: 79
nat-ippool6
<name>
IPv6 pools to be used for source NAT.
IPv6 pool name.
string
Maximum
length: 79
nat-port
Translated port or port range (1 to 65535,
0 means any port).
user
Not Specified
nat46
Enable/disable NAT46.
option
-disable
Option
Description
enable
Enable NAT46.
disable
Disable NAT46.
nat64
Enable/disable NAT64.
option
-disable
FortiOS 8.0.0 CLI Reference
508
Fortinet Inc.

<!-- 来源页 509 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable NAT64.
disable
Disable NAT64.
orig-addr
<name>
IPv4 Original address.
Address name.
string
Maximum
length: 79
orig-addr6
<name>
IPv6 Original address.
Address name.
string
Maximum
length: 79
orig-port
Original TCP port (1 to 65535, 0 means
any port).
user
Not Specified
policyid
Policy ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
port-preserve
Enable/disable preservation of the original
source port from source NAT if it has not
been used.
option
-enable
Option
Description
enable
Use the original source port if it has not been used.
disable
Source NAT always changes the source port.
port-random
Enable/disable random source port
selection for source NAT.
option
-disable
Option
Description
enable
Enable random source port selection for source NAT.
disable
Disable random source port selection for source NAT.
protocol
Integer value for the protocol type (0 -255).
integer
Minimum value:
0 Maximum
value: 255
0
srcintf
<name>
Source interface name from available
interfaces.
Interface name.
string
Maximum
length: 79
status
Enable/disable the active status of this
policy.
option
-enable
FortiOS 8.0.0 CLI Reference
509
Fortinet Inc.

---


<!-- 来源页 514 -->
config firewall decrypted-traffic-mirror
Configure decrypted traffic mirror.
config firewall decrypted-traffic-mirror
Description: Configure decrypted traffic mirror.
edit <name>
set dstmac {mac-address}
set interface <name1>, <name2>, ...
set traffic-source [client|server|...]
set traffic-type {option1}, {option2}, ...
next
end
config firewall decrypted-traffic-mirror
Parameter
Description
Type
Size
Default
dstmac
Set destination MAC address for mirrored
traffic.
mac-address
Not
Specified
ff:ff:ff:ff:ff:ff
interface
<name>
Decrypted traffic mirror interface.
Decrypted traffic mirror interface.
string
Maximum
length: 79
name
Name.
string
Maximum
length: 35
traffic-source
Source of decrypted traffic to be mirrored.
option
-client
Option
Description
client
Mirror client side decrypted traffic.
server
Mirror server side decrypted traffic.
both
Mirror both client and server side decrypted traffic.
traffic-type
Types of decrypted traffic to be mirrored.
option
-ssl
Option
Description
ssl
Mirror decrypted SSL traffic.
ssh
Mirror decrypted SSH traffic.
config firewall dnstranslation
Configure DNS translation.
FortiOS 8.0.0 CLI Reference
514
Fortinet Inc.

---


<!-- 来源页 550 -->
Parameter
Description
Type
Size
Default
seq-num
Entry number.
integer
Minimum value:
0 Maximum
value:
4294967295
0
status
Enable/disable this IP-mac binding
pair.
option
-disable
Option
Description
enable
Enable this IP-mac binding pair.
disable
Disable this IP-mac binding pair.
config firewall ippool
Configure IPv4 IP pools.
config firewall ippool
Description: Configure IPv4 IP pools.
edit <name>
set add-nat64-route [disable|enable]
set arp-intf {string}
set arp-reply [disable|enable]
set associated-interface {string}
set block-size {integer}
set cgn-block-size {integer}
set cgn-client-endip {var-string}
set cgn-client-ipv6shift {integer}
set cgn-client-startip {var-string}
set cgn-fixedalloc [disable|enable]
set cgn-overload [disable|enable]
set cgn-port-end {integer}
set cgn-port-start {integer}
set cgn-spa [disable|enable]
set client-prefix-length {integer}
set comments {var-string}
set endip {ipv4-address-any}
set endport {integer}
set exclude-ip <ip1>, <ip2>, ...
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set icmp-session-quota {integer}
set nat64 [disable|enable]
set num-blocks-per-user {integer}
set pba-interim-log {integer}
set pba-timeout {integer}
set permit-any-host [disable|enable]
FortiOS 8.0.0 CLI Reference
550
Fortinet Inc.

<!-- 来源页 551 -->
set port-per-user {integer}
set privileged-port-use-pba [disable|enable]
set source-endip {ipv4-address-any}
set source-prefix6 {ipv6-network}
set source-startip {ipv4-address-any}
set startip {ipv4-address-any}
set startport {integer}
set subnet-broadcast-in-ippool {option}
set tcp-session-quota {integer}
set type [overload|one-to-one|...]
set udp-session-quota {integer}
set utilization-alarm-clear {integer}
set utilization-alarm-raise {integer}
set uuid {uuid}
next
end
config firewall ippool
Parameter
Description
Type
Size
Default
add-nat64-route
Enable/disable adding NAT64 route.
option
-enable
Option
Description
disable
Disable adding NAT64 route.
enable
Enable adding NAT64 route.
arp-intf
Select an interface from available options that
will reply to ARP requests. (If blank, any is
selected).
string
Maximum
length: 15
arp-reply
Enable/disable replying to ARP requests when
an IP Pool is added to a policy (default =
enable).
option
-enable
Option
Description
disable
Disable ARP reply.
enable
Enable ARP reply.
associated-interface
Associated interface name.
string
Maximum
length: 15
FortiOS 8.0.0 CLI Reference
551
Fortinet Inc.

<!-- 来源页 552 -->
Parameter
Description
Type
Size
Default
block-size
Number of addresses in a block (64 - 4096,
default = 128).
integer
Minimum
value: 64
Maximum
value:
4096
128
cgn-block-size *
Number of ports in a block(64 to 4096 in unit
of 64, default = 128).
integer
Minimum
value: 64
Maximum
value:
4096
128
cgn-client-endip *
Final client IPv4 address (inclusive) (format
xxx.xxx.xxx.xxx, Default: 0.0.0.0).
var-string
Maximum
length: 255
cgn-client-ipv6shift *
IPv6 shift for fixed-allocation.(default 0)
integer
Minimum
value: 0
Maximum
value: 127
0
cgn-client-startip *
First client IPv4 address (inclusive) (format
xxx.xxx.xxx.xxx, Default: 0.0.0.0).
var-string
Maximum
length: 255
cgn-fixedalloc *
Enable/disable fixed-allocation mode.
option
-disable
Option
Description
disable
Disable fixed-allocation mode.
enable
Enable fixed-allocation mode.
cgn-overload
*
Enable/disable overload mode.
option
-disable
Option
Description
disable
Disable overload mode.
enable
Enable overload mode.
cgn-port-end
*
Ending public port can be allocated.
integer
Minimum
value: 1024
Maximum
value:
65535
65530
FortiOS 8.0.0 CLI Reference
552
Fortinet Inc.

<!-- 来源页 553 -->
Parameter
Description
Type
Size
Default
cgn-port-start *
Starting public port can be allocated.
integer
Minimum
value: 1024
Maximum
value:
65535
5117
cgn-spa *
Enable/disable single port allocation mode.
option
-disable
Option
Description
disable
Disable SPA mode.
enable
Enable SPA mode.
client-prefix-length
Subnet length of a single deterministic NAT64
client (1 - 128, default = 64).
integer
Minimum
value: 1
Maximum
value: 128
64
comments
Comment.
var-string
Maximum
length: 255
endip
Final IPv4 address (inclusive) in the range for
the address pool (format xxx.xxx.xxx.xxx,
Default: 0.0.0.0).
ipv4-address-any
Not
Specified
0.0.0.0
endport
Final port number (inclusive) in the range for
the address pool (1024 - 65535, Default:
65533).
integer
Minimum
value: 1024
Maximum
value:
65535
65533
exclude-ip
<ip> *
Exclude IPs x.x.x.x.
Exclude IPs (xxx.xxx.xxx.xxx)
string
Maximum
length: 79
fabric-force-sync *
Enable/disable forced synchronization of
configuration objects from the root FortiGate
unit to the downstream devices. Configuration
conflict check is skipped.
option
-disable
Option
Description
enable
Enable forced synchronization of configuration objects from the root
FortiGate unit to the downstream devices.
disable
Disable forced synchronization of configuration objects from the root
FortiGate unit to the downstream devices.
fabric-object
*
Security Fabric global object setting.
option
-disable
FortiOS 8.0.0 CLI Reference
553
Fortinet Inc.

<!-- 来源页 554 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Object is set as a security fabric-wide global object.
disable
Object is local to this security fabric member.
fabric-object-source *
Source of truth for fabric object.
option
-root
Option
Description
member
Source of truth for this object is a non-root member of fabric.
local
Source of truth for this object is this security fabric member.
root
Source of truth for this object is the root of the fabric.
icmp-session-quota
Maximum number of concurrent ICMP
sessions allowed per client (0 - 2097000,
default = 0 which means no limit).
integer
Minimum
value: 0
Maximum
value:
2097000
0
name
IP pool name.
string
Maximum
length: 79
nat64
Enable/disable NAT64.
option
-disable
Option
Description
disable
Disable DNAT64.
enable
Enable DNAT64.
num-blocks-per-user
Number of addresses blocks that can be used
by a user (1 to 128, default = 8).
integer
Minimum
value: 1
Maximum
value: 128
8
pba-interim-log
Port block allocation interim logging interval
(600 - 86400 seconds, default = 0 which
disables interim logging).
integer
Minimum
value: 600
Maximum
value:
86400
0
pba-timeout
Port block allocation timeout (seconds).
integer
Minimum
value: 3
Maximum
value:
86400
30
FortiOS 8.0.0 CLI Reference
554
Fortinet Inc.

<!-- 来源页 555 -->
Parameter
Description
Type
Size
Default
permit-any-host
Enable/disable fullcone NAT. Accept UDP
packets from any host.
option
-disable
Option
Description
disable
Disable full cone NAT.
enable
Enable full cone NAT.
port-per-user
Number of port for each user (32 - 60416,
default = 0, which is auto).
integer
Minimum
value: 32
Maximum
value:
60417
0
privileged-port-use-pba
Enable/disable selection of the external port
from the port block allocation for NAT'ing
privileged ports (deafult = disable).
option
-disable
Option
Description
disable
Select new nat port for privileged source ports from privileged range
512-1023.
enable
Select new nat port for privileged source ports from client's port block
source-endip
Final IPv4 address (inclusive) in the range of
the source addresses to be translated (format
xxx.xxx.xxx.xxx, Default: 0.0.0.0).
ipv4-address-any
Not
Specified
0.0.0.0
source-prefix6
Source IPv6 network to be translated (format
=
xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xxx,
default = ::/0).
ipv6-network
Not
Specified
::/0
source-startip
First IPv4 address (inclusive) in the range of
the source addresses to be translated (format
= xxx.xxx.xxx.xxx, default = 0.0.0.0).
ipv4-address-any
Not
Specified
0.0.0.0
startip
First IPv4 address (inclusive) in the range for
the address pool (format xxx.xxx.xxx.xxx,
Default: 0.0.0.0).
ipv4-address-any
Not
Specified
0.0.0.0
startport
First port number (inclusive) in the range for
the address pool (1024 - 65535, Default:
5117).
integer
Minimum
value: 1024
Maximum
value:
65535
5117
FortiOS 8.0.0 CLI Reference
555
Fortinet Inc.

<!-- 来源页 556 -->
Parameter
Description
Type
Size
Default
subnet-broadcast-in-ippool
Enable/disable inclusion of the subnetwork
address and broadcast IP address in the
NAT64 IP pool.
option
-Option
Description
disable
Do not include the subnetwork address and broadcast IP address in the
NAT64 IP pool.
tcp-session-quota
Maximum number of concurrent TCP sessions
allowed per client (0 - 2097000, default = 0
which means no limit).
integer
Minimum
value: 0
Maximum
value:
2097000
0
type
IP pool type: overload, one-to-one, fixed-port-range, port-block-allocation, cgn-resource-allocation (hyperscale vdom only)
option
-overload
Option
Description
overload
IP addresses in the IP pool can be shared by clients.
one-to-one
One to one mapping.
fixed-port-range
Fixed port range.
port-block-allocation
Port block allocation.
cgn-resource-allocation
CGN NAT resource allocation
udp-session-quota
Maximum number of concurrent UDP sessions
allowed per client (0 - 2097000, default = 0
which means no limit).
integer
Minimum
value: 0
Maximum
value:
2097000
0
utilization-alarm-clear *
Pool utilization alarm clear threshold (40-100).
integer
Minimum
value: 40
Maximum
value: 100
80
utilization-alarm-raise *
Pool utilization alarm raise threshold (50-100).
integer
Minimum
value: 50
Maximum
value: 100
100
FortiOS 8.0.0 CLI Reference
556
Fortinet Inc.

---


<!-- 来源页 557 -->
Parameter
Description
Type
Size
Default
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be manually
reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
config firewall ippool6
Configure IPv6 IP pools.
config firewall ippool6
Description: Configure IPv6 IP pools.
edit <name>
set add-nat46-route [disable|enable]
set comments {var-string}
set endip {ipv6-address}
set external-prefix {ipv6-network}
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set internal-prefix {ipv6-network}
set nat46 [disable|enable]
set startip {ipv6-address}
set type [overload|nptv6]
set uuid {uuid}
next
end
config firewall ippool6
Parameter
Description
Type
Size
Default
add-nat46-route
Enable/disable adding NAT46 route.
option
-enable
Option
Description
disable
Disable adding NAT46 route.
enable
Enable adding NAT46 route.
comments
Comment.
var-string
Maximum
length: 255
FortiOS 8.0.0 CLI Reference
557
Fortinet Inc.

<!-- 来源页 558 -->
Parameter
Description
Type
Size
Default
endip
Final IPv6 address (inclusive) in the range for
the address pool (format =
xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx,
default = ::).
ipv6-address
Not
Specified
::
external-prefix
External NPTv6 prefix length (32 - 64).
ipv6-network
Not
Specified
::/0
fabric-force-sync *
Enable/disable forced synchronization of
configuration objects from the root FortiGate
unit to the downstream devices.
Configuration conflict check is skipped.
option
-disable
Option
Description
enable
Enable forced synchronization of configuration objects from the root
FortiGate unit to the downstream devices.
disable
Disable forced synchronization of configuration objects from the root
FortiGate unit to the downstream devices.
fabric-object
*
Security Fabric global object setting.
option
-disable
Option
Description
enable
Object is set as a security fabric-wide global object.
disable
Object is local to this security fabric member.
fabric-object-source *
Source of truth for fabric object.
option
-root
Option
Description
member
Source of truth for this object is a non-root member of fabric.
local
Source of truth for this object is this security fabric member.
root
Source of truth for this object is the root of the fabric.
internal-prefix
Internal NPTv6 prefix length (32 - 64).
ipv6-network
Not
Specified
::/0
name
IPv6 IP pool name.
string
Maximum
length: 79
nat46
Enable/disable NAT46.
option
-disable
FortiOS 8.0.0 CLI Reference
558
Fortinet Inc.

---


<!-- 来源页 561 -->
Parameter
Description
Type
Size
Default
routing
Enable/disable blocking packets with Routing
headers (default = enable).
option
-enable
Option
Description
enable
Block packets with Routing headers.
disable
Allow packets with Routing headers.
routing-type
Block specific Routing header types (max. 7 types,
each between 0 and 255, default = 0).
integer
Minimum
value: 0
Maximum
value: 255
0
config firewall ip-translation
Configure firewall IP-translation.
config firewall ip-translation
Description: Configure firewall IP-translation.
edit <transid>
set endip {ipv4-address-any}
set map-startip {ipv4-address-any}
set startip {ipv4-address-any}
set type {option}
next
end
config firewall ip-translation
Parameter
Description
Type
Size
Default
endip
Final IPv4 address (inclusive) in the range of the
addresses to be translated (format
xxx.xxx.xxx.xxx, default: 0.0.0.0).
ipv4-address-any
Not Specified
0.0.0.0
map-startip
Address to be used as the starting point for
translation in the range (format xxx.xxx.xxx.xxx,
default: 0.0.0.0).
ipv4-address-any
Not Specified
0.0.0.0
startip
First IPv4 address (inclusive) in the range of the
addresses to be translated (format
xxx.xxx.xxx.xxx, default: 0.0.0.0).
ipv4-address-any
Not Specified
0.0.0.0
FortiOS 8.0.0 CLI Reference
561
Fortinet Inc.

---


<!-- 来源页 758 -->
set obsolete {integer}
next
end
config firewall vendor-mac
Parameter
Description
Type
Size
Default
id
Vendor ID. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
mac-number
Total number of MAC addresses. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
name
Vendor name. Read-only.
string
Maximum
length: 63
obsolete
Indicates whether the Vendor ID can be used.
Read-only.
integer
Minimum value:
0 Maximum
value: 255
0
config firewall vip
Configure virtual IP for IPv4.
config firewall vip
Description: Configure virtual IP for IPv4.
edit <name>
set add-nat46-route [disable|enable]
set arp-reply [disable|enable]
set auth-portal [disable|enable]
set auth-virtual-host {string}
set client-cert [disable|enable]
set color {integer}
set comment {var-string}
set dns-mapping-ttl {integer}
set empty-cert-action [accept|block|...]
set extaddr <name1>, <name2>, ...
set extintf {string}
set extip {user}
set extport {user}
set gratuitous-arp-interval {integer}
set gslb-domain-name {string}
set gslb-hostname {string}
config gslb-public-ips
FortiOS 8.0.0 CLI Reference
758
Fortinet Inc.

<!-- 来源页 759 -->
Description: Publicly accessible IP addresses for the FortiGSLB service.
edit <index>
set ip {ipv4-address-any}
next
end
set h2-support [enable|disable]
set h3-support [enable|disable]
set http-cookie-age {integer}
set http-cookie-domain {string}
set http-cookie-domain-from-host [disable|enable]
set http-cookie-generation {integer}
set http-cookie-path {string}
set http-cookie-share [disable|same-ip]
set http-ip-header [enable|disable]
set http-ip-header-name {string}
set http-multiplex [enable|disable]
set http-multiplex-max-concurrent-request {integer}
set http-multiplex-max-request {integer}
set http-multiplex-ttl {integer}
set http-redirect [enable|disable]
set https-cookie-secure [disable|enable]
set id {integer}
set ipv6-mappedip {user}
set ipv6-mappedport {user}
set ldb-method [static|round-robin|...]
set log-blocked-traffic [enable|disable]
set mapped-addr {string}
set mappedip <range1>, <range2>, ...
set mappedport {user}
set max-embryonic-connections {integer}
set monitor <name1>, <name2>, ...
set nat-source-vip [disable|enable]
set nat44 [disable|enable]
set nat46 [disable|enable]
set one-click-gslb-server [disable|enable]
set outlook-web-access [disable|enable]
set persistence [none|http-cookie|...]
set portforward [disable|enable]
set portmapping-type [1-to-1|m-to-n]
set protocol [tcp|udp|...]
config quic
Description: QUIC setting.
set ack-delay-exponent {integer}
set active-connection-id-limit {integer}
set active-migration [enable|disable]
set grease-quic-bit [enable|disable]
set max-ack-delay {integer}
set max-datagram-frame-size {integer}
set max-idle-timeout {integer}
set max-udp-payload-size {integer}
end
config realservers
FortiOS 8.0.0 CLI Reference
759
Fortinet Inc.

<!-- 来源页 760 -->
Description: Select the real servers that this server load balancing VIP will
distribute traffic to.
edit <id>
set address {string}
set client-ip {user}
set healthcheck [disable|enable|...]
set holddown-interval {integer}
set http-host {string}
set ip {user}
set max-connections {integer}
set monitor <name1>, <name2>, ...
set port {integer}
set status [active|standby|...]
set translate-host [enable|disable]
set type [ip|address]
set verify-cert [enable|disable]
set weight {integer}
next
end
set server-type [http|https|...]
set service <name1>, <name2>, ...
set src-filter <range1>, <range2>, ...
set src-vip-filter [disable|enable]
set srcintf-filter <interface-name1>, <interface-name2>, ...
set ssl-accept-ffdhe-groups [enable|disable]
set ssl-algorithm [high|medium|...]
set ssl-certificate <name1>, <name2>, ...
config ssl-cipher-suites
Description: SSL/TLS cipher suites acceptable from a client, ordered by priority.
edit <priority>
set cipher [TLS-AES-128-GCM-SHA256|TLS-AES-256-GCM-SHA384|...]
set versions {option1}, {option2}, ...
next
end
set ssl-client-fallback [disable|enable]
set ssl-client-rekey-count {integer}
set ssl-client-renegotiation [allow|deny|...]
set ssl-client-session-state-max {integer}
set ssl-client-session-state-timeout {integer}
set ssl-client-session-state-type [disable|time|...]
set ssl-dh-bits [768|1024|...]
set ssl-hpkp [disable|enable|...]
set ssl-hpkp-age {integer}
set ssl-hpkp-backup {string}
set ssl-hpkp-include-subdomains [disable|enable]
set ssl-hpkp-primary {string}
set ssl-hpkp-report-uri {var-string}
set ssl-hsts [disable|enable]
set ssl-hsts-age {integer}
set ssl-hsts-include-subdomains [disable|enable]
set ssl-http-location-conversion [enable|disable]
set ssl-http-match-host [enable|disable]
FortiOS 8.0.0 CLI Reference
760
Fortinet Inc.

<!-- 来源页 761 -->
set ssl-http-strip-secure-cookies [enable|disable]
set ssl-max-version [ssl-3.0|tls-1.0|...]
set ssl-min-version [ssl-3.0|tls-1.0|...]
set ssl-mode [half|full]
set ssl-pfs [require|deny|...]
set ssl-send-empty-frags [enable|disable]
set ssl-server-algorithm [high|medium|...]
config ssl-server-cipher-suites
Description: SSL/TLS cipher suites to offer to a server, ordered by priority.
edit <priority>
set cipher [TLS-AES-128-GCM-SHA256|TLS-AES-256-GCM-SHA384|...]
set versions {option1}, {option2}, ...
next
end
set ssl-server-client-certificate {string}
set ssl-server-max-version [ssl-3.0|tls-1.0|...]
set ssl-server-min-version [ssl-3.0|tls-1.0|...]
set ssl-server-renegotiation [enable|disable]
set ssl-server-session-state-max {integer}
set ssl-server-session-state-timeout {integer}
set ssl-server-session-state-type [disable|time|...]
set ssl-upstream [enable|disable]
set status [disable|enable]
set type [static-nat|load-balance|...]
set user-agent-detect [disable|enable]
set uuid {uuid}
set weblogic-server [disable|enable]
set websphere-server [disable|enable]
next
end
config firewall vip
Parameter
Description
Type
Size
Default
add-nat46-route
Enable/disable adding NAT46 route.
option
-enable
Option
Description
disable
Disable adding NAT46 route.
enable
Enable adding NAT46 route.
arp-reply
Enable to respond to ARP requests for
this virtual IP address. Enabled by
default.
option
-enable
FortiOS 8.0.0 CLI Reference
761
Fortinet Inc.

<!-- 来源页 762 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable ARP reply.
enable
Enable ARP reply.
auth-portal *
Enable/disable authentication portal.
option
-enable
Option
Description
disable
Disable authentication portal.
enable
Enable authentication portal.
auth-virtual-host *
Virtual host for authentication portal.
string
Maximum
length: 79
client-cert
Enable/disable requesting client
certificate.
option
-enable
Option
Description
disable
Disable client certificate request.
enable
Enable client certificate request.
color
Color of icon on the GUI.
integer
Minimum value:
0 Maximum
value: 32
0
comment
Comment.
var-string
Maximum
length: 255
dns-mapping-ttl
DNS mapping TTL (Set to zero to use
TTL in DNS response, default = 0).
integer
Minimum value:
0 Maximum
value: 604800
0
empty-cert-action
Action for an empty client certificate.
option
-block
Option
Description
accept
Accept the SSL handshake if the client certificate is empty.
block
Block the SSL handshake if the client certificate is empty.
accept-unmanageable
Accept the SSL handshake only if the end-point is unmanageable.
extaddr <name>
External FQDN address name.
Address name.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
762
Fortinet Inc.

<!-- 来源页 763 -->
Parameter
Description
Type
Size
Default
extintf
Interface connected to the source
network that receives the packets
that will be forwarded to the
destination network.
string
Maximum
length: 35
extip
IP address or address range on the
external interface that you want to
map to an address or address range
on the destination network.
user
Not Specified
extport
Incoming port number range that you
want to map to a port number range
on the destination network.
user
Not Specified
gratuitous-arp-interval
Enable to have the VIP send
gratuitous ARPs. 0=disabled. Set from
5 up to 8640000 seconds to enable.
integer
Minimum value:
5 Maximum
value:
8640000
0
gslb-domain-name
Domain to use when integrating with
FortiGSLB.
string
Maximum
length: 255
gslb-hostname
Hostname to use within the
configured FortiGSLB domain.
string
Maximum
length: 35
h2-support
Enable/disable HTTP2 support
(default = enable).
option
-enable
Option
Description
enable
Enable HTTP2 support.
disable
Disable HTTP2 support.
h3-support
Enable/disable HTTP3/QUIC support
(default = disable).
option
-disable
Option
Description
enable
Enable HTTP3/QUIC support.
disable
Disable HTTP3/QUIC support.
http-cookie-age
Time in minutes that client web
browsers should keep a cookie.
Default is 60 minutes. 0 = no time
limit.
integer
Minimum value:
0 Maximum
value: 525600
60
http-cookie-domain
Domain that HTTP cookie persistence
should apply to.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
763
Fortinet Inc.

<!-- 来源页 764 -->
Parameter
Description
Type
Size
Default
http-cookie-domain-from-host
Enable/disable use of HTTP cookie
domain from host field in HTTP.
option
-disable
Option
Description
disable
Disable use of HTTP cookie domain from host field in HTTP (use http-cooke-domain setting).
enable
Enable use of HTTP cookie domain from host field in HTTP.
http-cookie-generation
Generation of HTTP cookie to be
accepted. Changing invalidates all
existing cookies.
integer
Minimum value:
0 Maximum
value:
4294967295
0
http-cookie-path
Limit HTTP cookie persistence to the
specified path.
string
Maximum
length: 35
http-cookie-share
Control sharing of cookies across
virtual servers. Use of same-ip means
a cookie from one virtual server can
be used by another. Disable stops
cookie sharing.
option
-same-ip
Option
Description
disable
Only allow HTTP cookie to match this virtual server.
same-ip
Allow HTTP cookie to match any virtual server with same IP.
http-ip-header
For HTTP multiplexing, enable to add
the original client IP address in the X-Forwarded-For HTTP header.
option
-disable
Option
Description
enable
Enable adding HTTP header.
disable
Disable adding HTTP header.
http-ip-header-name
For HTTP multiplexing, enter a custom
HTTPS header name. The original
client IP address is added to this
header. If empty, X-Forwarded-For is
used.
string
Maximum
length: 35
http-multiplex
Enable/disable HTTP multiplexing.
option
-disable
FortiOS 8.0.0 CLI Reference
764
Fortinet Inc.

<!-- 来源页 765 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable HTTP session multiplexing.
disable
Disable HTTP session multiplexing.
http-multiplex-max-concurrent-request
Maximum number of concurrent
requests that a multiplex server can
handle (default = unlimited).
integer
Minimum value:
0 Maximum
value:
2147483647
0
http-multiplex-max-request
Maximum number of requests that a
multiplex server can handle before
disconnecting sessions (default =
unlimited).
integer
Minimum value:
0 Maximum
value:
2147483647
0
http-multiplex-ttl
Time-to-live for idle connections to
servers.
integer
Minimum value:
0 Maximum
value:
2147483647
15
http-redirect
Enable/disable redirection of HTTP to
HTTPS.
option
-disable
Option
Description
enable
Enable redirection of HTTP to HTTPS.
disable
Disable redirection of HTTP to HTTPS.
https-cookie-secure
Enable/disable verification that
inserted HTTPS cookies are secure.
option
-disable
Option
Description
disable
Do not mark cookie as secure, allow sharing between an HTTP and
HTTPS connection.
enable
Mark inserted cookie as secure, cookie can only be used for HTTPS a
connection.
id
Custom defined ID.
integer
Minimum value:
0 Maximum
value: 65535
0
ipv6-mappedip
Range of mapped IPv6 addresses.
Specify the start IPv6 address
followed by a space and the end IPv6
address.
user
Not Specified
FortiOS 8.0.0 CLI Reference
765
Fortinet Inc.

<!-- 来源页 766 -->
Parameter
Description
Type
Size
Default
ipv6-mappedport
IPv6 port number range on the
destination network to which the
external port number range is
mapped.
user
Not Specified
ldb-method
Method used to distribute sessions to
real servers.
option
-static
Option
Description
static
Distribute to server based on source IP.
round-robin
Distribute to server based round robin order.
weighted
Distribute to server based on weight.
least-session
Distribute to server with lowest session count.
least-rtt
Distribute to server with lowest Round-Trip-Time.
first-alive
Distribute to the first server that is alive.
http-host
Distribute to server based on host field in HTTP header.
log-blocked-traffic *
Enable/disable logging of blocked
traffic.
option
-enable
Option
Description
enable
Log all traffic denied by this access proxy.
disable
Do not log all traffic denied by this access proxy.
mapped-addr
Mapped FQDN address name.
string
Maximum
length: 79
mappedip
<range>
IP address or address range on the
destination network to which the
external IP address is mapped.
Mapped IP range.
string
Maximum
length: 79
mappedport
Port number range on the destination
network to which the external port
number range is mapped.
user
Not Specified
max-embryonic-connections
Maximum number of incomplete
connections.
integer
Minimum value:
0 Maximum
value: 100000
1000
monitor <name>
Name of the health check monitor to
use when polling to determine a virtual
server's connectivity status.
Health monitor name.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
766
Fortinet Inc.

<!-- 来源页 767 -->
Parameter
Description
Type
Size
Default
name
Virtual IP name.
string
Maximum
length: 79
nat-source-vip
Enable/disable forcing the source NAT
mapped IP to the external IP for all
traffic.
option
-disable
Option
Description
disable
Force only the source NAT mapped IP to the external IP for traffic
egressing the external interface of the VIP.
enable
Force the source NAT mapped IP to the external IP for all traffic.
nat44
Enable/disable NAT44.
option
-enable
Option
Description
disable
Disable NAT44.
enable
Enable NAT44.
nat46
Enable/disable NAT46.
option
-disable
Option
Description
disable
Disable NAT46.
enable
Enable NAT46.
one-click-gslb-server
Enable/disable one click GSLB server
integration with FortiGSLB.
option
-disable
Option
Description
disable
Disable integration with FortiGSLB.
enable
Enable integration with FortiGSLB.
outlook-web-access
Enable to add the Front-End-Https
header for Microsoft Outlook Web
Access.
option
-disable
Option
Description
disable
Disable Outlook Web Access support.
enable
Enable Outlook Web Access support.
persistence
Configure how to make sure that
clients connect to the same server
every time they make a request that is
part of the same session.
option
-none
FortiOS 8.0.0 CLI Reference
767
Fortinet Inc.

<!-- 来源页 768 -->
Parameter
Description
Type
Size
Default
Option
Description
none
None.
http-cookie
HTTP cookie.
ssl-session-id
SSL session ID.
portforward
Enable/disable port forwarding.
option
-disable
Option
Description
disable
Disable port forward.
enable
Enable port forward.
portmapping-type
Port mapping type.
option
-1-to-1
Option
Description
1-to-1
One to one.
m-to-n
Many to many.
protocol
Protocol to use when forwarding
packets.
option
-tcp
Option
Description
tcp
TCP.
udp
UDP.
sctp
SCTP.
icmp
ICMP.
server-type
Protocol to be load balanced by the
virtual server (also called the server
load balance virtual IP).
option
-Option
Description
http
HTTP.
https
HTTPS.
imaps
IMAPS.
pop3s
POP3S.
smtps
SMTPS.
FortiOS 8.0.0 CLI Reference
768
Fortinet Inc.

<!-- 来源页 769 -->
Parameter
Description
Type
Size
Default
Option
Description
ssl
SSL.
tcp
TCP.
udp
UDP.
ip
IP.
service <name>
Service name.
Service name.
string
Maximum
length: 79
src-filter
<range>
Source address filter. Each address
must be either an IP/subnet (x.x.x.x/n)
or a range (x.x.x.x-y.y.y.y). Separate
addresses with spaces.
Source-filter range.
string
Maximum
length: 79
src-vip-filter
Enable/disable use of 'src-filter' to
match destinations for the reverse
SNAT rule.
option
-disable
Option
Description
disable
Match any destination for the reverse SNAT rule.
enable
Match only destinations in 'src-filter' for the reverse SNAT rule.
srcintf-filter
<interface-name>
Interfaces to which the VIP applies.
Separate the names with spaces.
Interface name.
string
Maximum
length: 79
ssl-accept-ffdhe-groups
Enable/disable FFDHE cipher suite for
SSL key exchange.
option
-enable
Option
Description
enable
Accept FFDHE groups.
disable
Do not accept FFDHE groups.
ssl-algorithm
Permitted encryption algorithms for
SSL sessions according to encryption
strength.
option
-high
Option
Description
high
High encryption. Allow only AES and ChaCha.
medium
Medium encryption. Allow AES, ChaCha, 3DES, and RC4.
FortiOS 8.0.0 CLI Reference
769
Fortinet Inc.

<!-- 来源页 770 -->
Parameter
Description
Type
Size
Default
Option
Description
low
Low encryption. Allow AES, ChaCha, 3DES, RC4, and DES.
custom
Custom encryption. Use config ssl-cipher-suites to select the cipher
suites that are allowed.
ssl-certificate
<name>
Name of the certificate to use for SSL
handshake.
Certificate list.
string
Maximum
length: 79
ssl-client-fallback
Enable/disable support for preventing
Downgrade Attacks on client
connections (RFC 7507).
option
-enable
Option
Description
disable
Disable.
enable
Enable.
ssl-client-rekey-count
Maximum length of data in MB before
triggering a client rekey (0 = disable).
integer
Minimum value:
200 Maximum
value: 1048576
0
ssl-client-renegotiation
Allow, deny, or require secure
renegotiation of client sessions to
comply with RFC 5746.
option
-secure
Option
Description
allow
Allow a SSL client to renegotiate.
deny
Abort any client initiated SSL re-negotiation attempt.
secure
Abort any client initiated SSL re-negotiation attempt that does not use
RFC 5746 Secure Renegotiation.
ssl-client-session-state-max
Maximum number of client to
FortiGate SSL session states to keep.
integer
Minimum value:
1 Maximum
value: 10000
1000
ssl-client-session-state-timeout
Number of minutes to keep client to
FortiGate SSL session state.
integer
Minimum value:
1 Maximum
value: 14400
30
ssl-client-session-state-type
How to expire SSL sessions for the
segment of the SSL connection
between the client and the FortiGate.
option
-both
FortiOS 8.0.0 CLI Reference
770
Fortinet Inc.

<!-- 来源页 771 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Do not keep session states.
time
Expire session states after this many minutes.
count
Expire session states when this maximum is reached.
both
Expire session states based on time or count, whichever occurs first.
ssl-dh-bits
Number of bits to use in the Diffie-Hellman exchange for RSA encryption
of SSL sessions.
option
-2048
Option
Description
768
768-bit Diffie-Hellman prime.
1024
1024-bit Diffie-Hellman prime.
1536
1536-bit Diffie-Hellman prime.
2048
2048-bit Diffie-Hellman prime.
3072
3072-bit Diffie-Hellman prime.
4096
4096-bit Diffie-Hellman prime.
ssl-hpkp
Enable/disable including HPKP header
in response.
option
-disable
Option
Description
disable
Do not add a HPKP header to each HTTP response.
enable
Add a HPKP header to each a HTTP response.
report-only
Add a HPKP Report-Only header to each HTTP response.
ssl-hpkp-age
Number of seconds the client should
honor the HPKP setting.
integer
Minimum value:
60 Maximum
value:
157680000
5184000
ssl-hpkp-backup
Certificate to generate backup HPKP
pin from.
string
Maximum
length: 79
ssl-hpkp-include-subdomains
Indicate that HPKP header applies to
all subdomains.
option
-disable
FortiOS 8.0.0 CLI Reference
771
Fortinet Inc.

<!-- 来源页 772 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
HPKP header does not apply to subdomains.
enable
HPKP header applies to subdomains.
ssl-hpkp-primary
Certificate to generate primary HPKP
pin from.
string
Maximum
length: 79
ssl-hpkp-report-uri
URL to report HPKP violations to.
var-string
Maximum
length: 255
ssl-hsts
Enable/disable including HSTS header
in response.
option
-disable
Option
Description
disable
Do not add a HSTS header to each a HTTP response.
enable
Add a HSTS header to each HTTP response.
ssl-hsts-age
Number of seconds the client should
honor the HSTS setting.
integer
Minimum value:
60 Maximum
value:
157680000
5184000
ssl-hsts-include-subdomains
Indicate that HSTS header applies to
all subdomains.
option
-disable
Option
Description
disable
HSTS header does not apply to subdomains.
enable
HSTS header applies to subdomains.
ssl-http-location-conversion
Enable to convert HTTP/HTTPS in the
reply's Location HTTP header field.
option
-disable
Option
Description
enable
Enable HTTP location conversion.
disable
Disable HTTP location conversion.
ssl-http-match-host
Enable/disable HTTP host matching
for location conversion.
option
-enable
Option
Description
enable
Match HTTP host in response header.
FortiOS 8.0.0 CLI Reference
772
Fortinet Inc.

<!-- 来源页 773 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Do not match HTTP host.
ssl-http-strip-secure-cookies
*
Enable/disable removal of HTTPS-only directives in the reply's Set-Cookie HTTP header fields.
option
-disable
Option
Description
enable
Remove HTTPS-only directives in response Set-Cookie headers.
disable
Do not remove HTTPS-only directives.
ssl-max-version
Highest SSL/TLS version acceptable
from a client.
option
-tls-1.3
Option
Description
ssl-3.0
SSL 3.0.
tls-1.0
TLS 1.0.
tls-1.1
TLS 1.1.
tls-1.2
TLS 1.2.
tls-1.3
TLS 1.3.
ssl-min-version
Lowest SSL/TLS version acceptable
from a client.
option
-tls-1.1
Option
Description
ssl-3.0
SSL 3.0.
tls-1.0
TLS 1.0.
tls-1.1
TLS 1.1.
tls-1.2
TLS 1.2.
tls-1.3
TLS 1.3.
ssl-mode
Apply SSL offloading between the
client and the FortiGate (half) or from
the client to the FortiGate and from
the FortiGate to the server (full).
option
-half
Option
Description
half
Client to FortiGate SSL.
full
Client to FortiGate and FortiGate to Server SSL.
FortiOS 8.0.0 CLI Reference
773
Fortinet Inc.

<!-- 来源页 774 -->
Parameter
Description
Type
Size
Default
ssl-pfs
Select the cipher suites that can be
used for SSL perfect forward secrecy
(PFS). Applies to both client and
server sessions.
option
-require
Option
Description
require
Allow only Diffie-Hellman cipher-suites, so PFS is applied.
deny
Allow only non-Diffie-Hellman cipher-suites, so PFS is not applied.
allow
Allow use of any cipher suite so PFS may or may not be used
depending on the cipher suite selected.
ssl-send-empty-frags
Enable/disable sending empty
fragments to avoid CBC IV attacks
(SSL 3.0 & TLS 1.0 only). May need to
be disabled for compatibility with
older systems.
option
-enable
Option
Description
enable
Send empty fragments.
disable
Do not send empty fragments.
ssl-server-algorithm
Permitted encryption algorithms for
the server side of SSL sessions
according to encryption strength.
option
-client
Option
Description
high
High encryption. Allow only AES and ChaCha.
medium
Medium encryption. Allow AES, ChaCha, 3DES, and RC4.
low
Low encryption. Allow AES, ChaCha, 3DES, RC4, and DES.
custom
Custom encryption. Use ssl-server-cipher-suites to select the cipher
suites that are allowed.
client
Use the same encryption algorithms for both client and server
sessions.
ssl-server-client-certificate *
Name of the client certificate
presented to realserver during
SSL/TLS handshake if requested.
string
Maximum
length: 79
ssl-server-max-version
Highest SSL/TLS version acceptable
from a server. Use the client setting
by default.
option
-client
FortiOS 8.0.0 CLI Reference
774
Fortinet Inc.

<!-- 来源页 775 -->
Parameter
Description
Type
Size
Default
Option
Description
ssl-3.0
SSL 3.0.
tls-1.0
TLS 1.0.
tls-1.1
TLS 1.1.
tls-1.2
TLS 1.2.
tls-1.3
TLS 1.3.
client
Use same value as client configuration.
ssl-server-min-version
Lowest SSL/TLS version acceptable
from a server. Use the client setting
by default.
option
-client
Option
Description
ssl-3.0
SSL 3.0.
tls-1.0
TLS 1.0.
tls-1.1
TLS 1.1.
tls-1.2
TLS 1.2.
tls-1.3
TLS 1.3.
client
Use same value as client configuration.
ssl-server-renegotiation
Enable/disable secure renegotiation
to comply with RFC 5746.
option
-enable
Option
Description
enable
Enable secure renegotiation.
disable
Disable secure renegotiation.
ssl-server-session-state-max
Maximum number of FortiGate to
Server SSL session states to keep.
integer
Minimum value:
1 Maximum
value: 10000
100
ssl-server-session-state-timeout
Number of minutes to keep FortiGate
to Server SSL session state.
integer
Minimum value:
1 Maximum
value: 14400
60
ssl-server-session-state-type
How to expire SSL sessions for the
segment of the SSL connection
between the server and the FortiGate.
option
-both
FortiOS 8.0.0 CLI Reference
775
Fortinet Inc.

<!-- 来源页 776 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Do not keep session states.
time
Expire session states after this many minutes.
count
Expire session states when this maximum is reached.
both
Expire session states based on time or count, whichever occurs first.
ssl-upstream *
Apply SSL encryption between the
FortiGate and the upstream server
(default = disable).
option
-disable
Option
Description
enable
Apply SSL encryption between the FortiGate and the upstream server.
disable
Do not apply SSL encryption between the FortiGate and the upstream
server. Use plain text.
status
Enable/disable VIP.
option
-enable
Option
Description
disable
Disable the VIP.
enable
Enable the VIP.
type
Configure a static NAT, load balance,
server load balance, access proxy,
DNS translation, or FQDN VIP.
option
-static-nat
Option
Description
static-nat
Static NAT.
load-balance
Load balance.
server-load-balance
Server load balance.
dns-translation
DNS translation.
fqdn
Fully qualified domain name.
access-proxy
Access proxy.
user-agent-detect
Enable/disable detecting device type
by HTTP user-agent if no client
certificate is provided.
option
-enable
FortiOS 8.0.0 CLI Reference
776
Fortinet Inc.

<!-- 来源页 777 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable detecting unknown devices by HTTP user-agent if no client
certificate is provided.
enable
Enable detecting unknown devices by HTTP user-agent if no client
certificate is provided.
uuid
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not Specified
00000000-0000-0000-0000-000000000000
weblogic-server
Enable to add an HTTP header to
indicate SSL offloading for a
WebLogic server.
option
-disable
Option
Description
disable
Do not add HTTP header indicating SSL offload for WebLogic server.
enable
Add HTTP header indicating SSL offload for WebLogic server.
websphere-server
Enable to add an HTTP header to
indicate SSL offloading for a
WebSphere server.
option
-disable
Option
Description
disable
Do not add HTTP header indicating SSL offload for WebSphere server.
enable
Add HTTP header indicating SSL offload for WebSphere server.
* This parameter may not exist in some models.
config gslb-public-ips
Parameter
Description
Type
Size
Default
index
Index of this public IP setting.
integer
Minimum value:
0 Maximum
value:
4294967295
0
ip
The publicly accessible IP address.
ipv4-address-any
Not Specified
0.0.0.0
FortiOS 8.0.0 CLI Reference
777
Fortinet Inc.

<!-- 来源页 778 -->
config quic
Parameter
Description
Type
Size
Default
ack-delay-exponent
ACK delay exponent (1 - 20, default = 3).
integer
Minimum
value: 1
Maximum
value: 20
3
active-connection-id-limit
Active connection ID limit (1 - 8, default = 2).
integer
Minimum
value: 1
Maximum
value: 8
2
active-migration
Enable/disable active migration (default = disable).
option
-disable
Option
Description
enable
Enable active migration.
disable
Disable active migration.
grease-quic-bit
Enable/disable grease QUIC bit (default = enable).
option
-enable
Option
Description
enable
Enable grease QUIC bit.
disable
Disable grease QUIC bit.
max-ack-delay
Maximum ACK delay in milliseconds (1 - 16383,
default = 25).
integer
Minimum
value: 1
Maximum
value:
16383
25
max-datagram-frame-size
Maximum datagram frame size in bytes (1 - 1500,
default = 1500).
integer
Minimum
value: 1
Maximum
value: 1500
1500
max-idle-timeout
Maximum idle timeout milliseconds (1 - 60000,
default = 30000).
integer
Minimum
value: 1
Maximum
value:
60000
30000
max-udp-payload-size
Maximum UDP payload size in bytes (1200 - 1500,
default = 1500).
integer
Minimum
value: 1200
Maximum
value: 1500
1500
FortiOS 8.0.0 CLI Reference
778
Fortinet Inc.

<!-- 来源页 779 -->
config realservers
Parameter
Description
Type
Size
Default
address
Dynamic address of the real server.
string
Maximum
length: 79
client-ip
Only clients in this IP range can connect to this
real server.
user
Not Specified
healthcheck
Enable to check the responsiveness of the real
server before forwarding traffic.
option
-vip
Option
Description
disable
Disable per server health check.
enable
Enable per server health check.
vip
Use health check defined in VIP.
holddown-interval
Time in seconds that the system waits before
re-activating a previously down active server in
the active-standby mode. This is to prevent
any flapping issues.
integer
Minimum value:
30 Maximum
value: 65535
300
http-host
HTTP server domain name in HTTP header.
string
Maximum
length: 63
id
Real server ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
ip
IP address of the real server.
user
Not Specified
max-connections
Max number of active connections that can be
directed to the real server. When reached,
sessions are sent to other real servers.
integer
Minimum value:
0 Maximum
value:
2147483647
0
monitor
<name>
Name of the health check monitor to use when
polling to determine a virtual server's
connectivity status.
Health monitor name.
string
Maximum
length: 79
port
Port for communicating with the real server.
Required if port forwarding is enabled.
integer
Minimum value:
1 Maximum
value: 65535
0
status
Set the status of the real server to active so
that it can accept traffic, or on standby or
disabled so no traffic is sent.
option
-active
FortiOS 8.0.0 CLI Reference
779
Fortinet Inc.

<!-- 来源页 780 -->
Parameter
Description
Type
Size
Default
Option
Description
active
Server status active.
standby
Server status standby.
disable
Server status disable.
translate-host
Enable/disable translation of hostname/IP from
virtual server to real server.
option
-enable
Option
Description
enable
Enable virtual hostname/IP translation.
disable
Disable virtual hostname/IP translation.
type
Type of address.
option
-ip
Option
Description
ip
Standard IPv4 address.
address
Dynamic address object.
verify-cert
Enable/disable certificate verification of the
real server.
option
-enable
Option
Description
enable
Enable certificate verification.
disable
Disable certificate verification.
weight
Weight of the real server. If weighted load
balancing is enabled, the server with the
highest weight gets more connections.
integer
Minimum value:
1 Maximum
value: 255
1
config ssl-cipher-suites
Parameter
Description
Type
Size
Default
cipher
Cipher suite name.
option
-Option
Description
TLS-AES-128-GCM-SHA256
Cipher suite TLS-AES-128-GCM-SHA256.
TLS-AES-256-GCM-SHA384
Cipher suite TLS-AES-256-GCM-SHA384.
FortiOS 8.0.0 CLI Reference
780
Fortinet Inc.

<!-- 来源页 781 -->
Parameter
Description
Type
Size
Default
Option
Description
TLS-CHACHA20-POLY1305-SHA256
Cipher suite TLS-CHACHA20-POLY1305-SHA256.
TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256
Cipher suite TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256.
TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256
Cipher suite TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256.
TLS-DHE-RSA-WITH-CHACHA20-POLY1305-SHA256
Cipher suite TLS-DHE-RSA-WITH-CHACHA20-POLY1305-SHA256.
TLS-DHE-RSA-WITH-AES-128-CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-AES-128-CBC-SHA.
TLS-DHE-RSA-WITH-AES-256-CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-AES-256-CBC-SHA.
TLS-DHE-RSA-WITH-AES-128-CBC-SHA256
Cipher suite TLS-DHE-RSA-WITH-AES-128-CBC-SHA256.
TLS-DHE-RSA-WITH-AES-128-GCM-SHA256
Cipher suite TLS-DHE-RSA-WITH-AES-128-GCM-SHA256.
TLS-DHE-RSA-WITH-AES-256-CBC-SHA256
Cipher suite TLS-DHE-RSA-WITH-AES-256-CBC-SHA256.
TLS-DHE-RSA-WITH-AES-256-GCM-SHA384
Cipher suite TLS-DHE-RSA-WITH-AES-256-GCM-SHA384.
FortiOS 8.0.0 CLI Reference
781
Fortinet Inc.

<!-- 来源页 782 -->
Parameter
Description
Type
Size
Default
Option
Description
TLS-DHE-DSS-WITH-AES-128-CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-AES-128-CBC-SHA.
TLS-DHE-DSS-WITH-AES-256-CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-AES-256-CBC-SHA.
TLS-DHE-DSS-WITH-AES-128-CBC-SHA256
Cipher suite TLS-DHE-DSS-WITH-AES-128-CBC-SHA256.
TLS-DHE-DSS-WITH-AES-128-GCM-SHA256
Cipher suite TLS-DHE-DSS-WITH-AES-128-GCM-SHA256.
TLS-DHE-DSS-WITH-AES-256-CBC-SHA256
Cipher suite TLS-DHE-DSS-WITH-AES-256-CBC-SHA256.
TLS-DHE-DSS-WITH-AES-256-GCM-SHA384
Cipher suite TLS-DHE-DSS-WITH-AES-256-GCM-SHA384.
TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA
Cipher suite TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA.
TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256
Cipher suite TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256.
TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256
Cipher suite TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256.
TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA
Cipher suite TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA.
FortiOS 8.0.0 CLI Reference
782
Fortinet Inc.

<!-- 来源页 783 -->
Parameter
Description
Type
Size
Default
Option
Description
TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384
Cipher suite TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384.
TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384
Cipher suite TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384.
TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA.
TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256.
TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256.
TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA.
TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384.
TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384.
TLS-RSA-WITH-AES-128-CBC-SHA
Cipher suite TLS-RSA-WITH-AES-128-CBC-SHA.
TLS-RSA-WITH-AES-256-CBC-SHA
Cipher suite TLS-RSA-WITH-AES-256-CBC-SHA.
FortiOS 8.0.0 CLI Reference
783
Fortinet Inc.

<!-- 来源页 784 -->
Parameter
Description
Type
Size
Default
Option
Description
TLS-RSA-WITH-AES-128-CBC-SHA256
Cipher suite TLS-RSA-WITH-AES-128-CBC-SHA256.
TLS-RSA-WITH-AES-128-GCM-SHA256
Cipher suite TLS-RSA-WITH-AES-128-GCM-SHA256.
TLS-RSA-WITH-AES-256-CBC-SHA256
Cipher suite TLS-RSA-WITH-AES-256-CBC-SHA256.
TLS-RSA-WITH-AES-256-GCM-SHA384
Cipher suite TLS-RSA-WITH-AES-256-GCM-SHA384.
TLS-RSA-WITH-CAMELLIA-128-CBC-SHA
Cipher suite TLS-RSA-WITH-CAMELLIA-128-CBC-SHA.
TLS-RSA-WITH-CAMELLIA-256-CBC-SHA
Cipher suite TLS-RSA-WITH-CAMELLIA-256-CBC-SHA.
TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256
Cipher suite TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256.
TLS-RSA-WITH-CAMELLIA-256-CBC-SHA256
Cipher suite TLS-RSA-WITH-CAMELLIA-256-CBC-SHA256.
TLS-DHE-RSA-WITH-3DES-EDE-CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-3DES-EDE-CBC-SHA.
TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA.
FortiOS 8.0.0 CLI Reference
784
Fortinet Inc.

<!-- 来源页 785 -->
Parameter
Description
Type
Size
Default
Option
Description
TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA
Cipher suite TLS-DSS-RSA-WITH-CAMELLIA-128-CBC-SHA.
TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA.
TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA.
TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256
Cipher suite TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256.
TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256
Cipher suite TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256.
TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256
Cipher suite TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256.
TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA256
Cipher suite TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA256.
TLS-DHE-RSA-WITH-SEED-CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-SEED-CBC-SHA.
TLS-DHE-DSS-WITH-SEED-CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-SEED-CBC-SHA.
FortiOS 8.0.0 CLI Reference
785
Fortinet Inc.

<!-- 来源页 786 -->
Parameter
Description
Type
Size
Default
Option
Description
TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256
Cipher suite TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256.
TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384
Cipher suite TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384.
TLS-DHE-DSS-WITH-ARIA-128-CBC-SHA256
Cipher suite TLS-DHE-DSS-WITH-ARIA-128-CBC-SHA256.
TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384
Cipher suite TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384.
TLS-RSA-WITH-SEED-CBC-SHA
Cipher suite TLS-RSA-WITH-SEED-CBC-SHA.
TLS-RSA-WITH-ARIA-128-CBC-SHA256
Cipher suite TLS-RSA-WITH-ARIA-128-CBC-SHA256.
TLS-RSA-WITH-ARIA-256-CBC-SHA384
Cipher suite TLS-RSA-WITH-ARIA-256-CBC-SHA384.
TLS-ECDHE-RSA-WITH-ARIA-128-CBC-SHA256
Cipher suite TLS-ECDHE-RSA-WITH-ARIA-128-CBC-SHA256.
TLS-ECDHE-RSA-WITH-ARIA-256-CBC-SHA384
Cipher suite TLS-ECDHE-RSA-WITH-ARIA-256-CBC-SHA384.
TLS-ECDHE-ECDSA-WITH-ARIA-128-CBC-SHA256
Cipher suite TLS-ECDHE-ECDSA-WITH-ARIA-128-CBC_SHA256.
FortiOS 8.0.0 CLI Reference
786
Fortinet Inc.

<!-- 来源页 787 -->
Parameter
Description
Type
Size
Default
Option
Description
TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC-SHA384
Cipher suite TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC_SHA384.
TLS-ECDHE-RSA-WITH-RC4-128-SHA
Cipher suite TLS-ECDHE-RSA-WITH-RC4-128-SHA.
TLS-ECDHE-RSA-WITH-3DES-EDE-CBC-SHA
Cipher suite TLS-ECDHE-RSA-WITH-3DES-EDE-CBC-SHA.
TLS-DHE-DSS-WITH-3DES-EDE-CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-3DES-EDE-CBC-SHA.
TLS-RSA-WITH-3DES-EDE-CBC-SHA
Cipher suite TLS-RSA-WITH-3DES-EDE-CBC-SHA.
TLS-RSA-WITH-RC4-128-MD5
Cipher suite TLS-RSA-WITH-RC4-128-MD5.
TLS-RSA-WITH-RC4-128-SHA
Cipher suite TLS-RSA-WITH-RC4-128-SHA.
TLS-DHE-RSA-WITH-DES-CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-DES-CBC-SHA.
TLS-DHE-DSS-WITH-DES-CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-DES-CBC-SHA.
TLS-RSA-WITH-DES-CBC-SHA
Cipher suite TLS-RSA-WITH-DES-CBC-SHA.
priority
SSL/TLS cipher suites priority.
integer
Minimum value:
0 Maximum
value:
4294967295
0
FortiOS 8.0.0 CLI Reference
787
Fortinet Inc.

<!-- 来源页 788 -->
Parameter
Description
Type
Size
Default
versions
SSL/TLS versions that the cipher suite can be
used with.
option
-tls-1.1 tls-1.2 tls-1.3
**
Option
Description
ssl-3.0
SSL 3.0.
tls-1.0
TLS 1.0.
tls-1.1
TLS 1.1.
tls-1.2
TLS 1.2.
tls-1.3
TLS 1.3.
** Values may differ between models.
config ssl-server-cipher-suites
Parameter
Description
Type
Size
Default
cipher
Cipher suite name.
option
-Option
Description
TLS-AES-128-GCM-SHA256
Cipher suite TLS-AES-128-GCM-SHA256.
TLS-AES-256-GCM-SHA384
Cipher suite TLS-AES-256-GCM-SHA384.
TLS-CHACHA20-POLY1305-SHA256
Cipher suite TLS-CHACHA20-POLY1305-SHA256.
TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256
Cipher suite TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256.
TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256
Cipher suite TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256.
FortiOS 8.0.0 CLI Reference
788
Fortinet Inc.

<!-- 来源页 789 -->
Parameter
Description
Type
Size
Default
Option
Description
TLS-DHE-RSA-WITH-CHACHA20-POLY1305-SHA256
Cipher suite TLS-DHE-RSA-WITH-CHACHA20-POLY1305-SHA256.
TLS-DHE-RSA-WITH-AES-128-CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-AES-128-CBC-SHA.
TLS-DHE-RSA-WITH-AES-256-CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-AES-256-CBC-SHA.
TLS-DHE-RSA-WITH-AES-128-CBC-SHA256
Cipher suite TLS-DHE-RSA-WITH-AES-128-CBC-SHA256.
TLS-DHE-RSA-WITH-AES-128-GCM-SHA256
Cipher suite TLS-DHE-RSA-WITH-AES-128-GCM-SHA256.
TLS-DHE-RSA-WITH-AES-256-CBC-SHA256
Cipher suite TLS-DHE-RSA-WITH-AES-256-CBC-SHA256.
TLS-DHE-RSA-WITH-AES-256-GCM-SHA384
Cipher suite TLS-DHE-RSA-WITH-AES-256-GCM-SHA384.
TLS-DHE-DSS-WITH-AES-128-CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-AES-128-CBC-SHA.
TLS-DHE-DSS-WITH-AES-256-CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-AES-256-CBC-SHA.
TLS-DHE-DSS-WITH-AES-128-CBC-SHA256
Cipher suite TLS-DHE-DSS-WITH-AES-128-CBC-SHA256.
TLS-DHE-DSS-WITH-AES-128-GCM-SHA256
Cipher suite TLS-DHE-DSS-WITH-AES-128-GCM-SHA256.
FortiOS 8.0.0 CLI Reference
789
Fortinet Inc.

<!-- 来源页 790 -->
Parameter
Description
Type
Size
Default
Option
Description
TLS-DHE-DSS-WITH-AES-256-CBC-SHA256
Cipher suite TLS-DHE-DSS-WITH-AES-256-CBC-SHA256.
TLS-DHE-DSS-WITH-AES-256-GCM-SHA384
Cipher suite TLS-DHE-DSS-WITH-AES-256-GCM-SHA384.
TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA
Cipher suite TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA.
TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256
Cipher suite TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256.
TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256
Cipher suite TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256.
TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA
Cipher suite TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA.
TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384
Cipher suite TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384.
TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384
Cipher suite TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384.
TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA.
FortiOS 8.0.0 CLI Reference
790
Fortinet Inc.

<!-- 来源页 791 -->
Parameter
Description
Type
Size
Default
Option
Description
TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256.
TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256.
TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA.
TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384.
TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384.
TLS-RSA-WITH-AES-128-CBC-SHA
Cipher suite TLS-RSA-WITH-AES-128-CBC-SHA.
TLS-RSA-WITH-AES-256-CBC-SHA
Cipher suite TLS-RSA-WITH-AES-256-CBC-SHA.
TLS-RSA-WITH-AES-128-CBC-SHA256
Cipher suite TLS-RSA-WITH-AES-128-CBC-SHA256.
TLS-RSA-WITH-AES-128-GCM-SHA256
Cipher suite TLS-RSA-WITH-AES-128-GCM-SHA256.
TLS-RSA-WITH-AES-256-CBC-SHA256
Cipher suite TLS-RSA-WITH-AES-256-CBC-SHA256.
FortiOS 8.0.0 CLI Reference
791
Fortinet Inc.

<!-- 来源页 792 -->
Parameter
Description
Type
Size
Default
Option
Description
TLS-RSA-WITH-AES-256-GCM-SHA384
Cipher suite TLS-RSA-WITH-AES-256-GCM-SHA384.
TLS-RSA-WITH-CAMELLIA-128-CBC-SHA
Cipher suite TLS-RSA-WITH-CAMELLIA-128-CBC-SHA.
TLS-RSA-WITH-CAMELLIA-256-CBC-SHA
Cipher suite TLS-RSA-WITH-CAMELLIA-256-CBC-SHA.
TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256
Cipher suite TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256.
TLS-RSA-WITH-CAMELLIA-256-CBC-SHA256
Cipher suite TLS-RSA-WITH-CAMELLIA-256-CBC-SHA256.
TLS-DHE-RSA-WITH-3DES-EDE-CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-3DES-EDE-CBC-SHA.
TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA.
TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA
Cipher suite TLS-DSS-RSA-WITH-CAMELLIA-128-CBC-SHA.
TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA.
FortiOS 8.0.0 CLI Reference
792
Fortinet Inc.

<!-- 来源页 793 -->
Parameter
Description
Type
Size
Default
Option
Description
TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA.
TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256
Cipher suite TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256.
TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256
Cipher suite TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256.
TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256
Cipher suite TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256.
TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA256
Cipher suite TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA256.
TLS-DHE-RSA-WITH-SEED-CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-SEED-CBC-SHA.
TLS-DHE-DSS-WITH-SEED-CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-SEED-CBC-SHA.
TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256
Cipher suite TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256.
TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384
Cipher suite TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384.
FortiOS 8.0.0 CLI Reference
793
Fortinet Inc.

<!-- 来源页 794 -->
Parameter
Description
Type
Size
Default
Option
Description
TLS-DHE-DSS-WITH-ARIA-128-CBC-SHA256
Cipher suite TLS-DHE-DSS-WITH-ARIA-128-CBC-SHA256.
TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384
Cipher suite TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384.
TLS-RSA-WITH-SEED-CBC-SHA
Cipher suite TLS-RSA-WITH-SEED-CBC-SHA.
TLS-RSA-WITH-ARIA-128-CBC-SHA256
Cipher suite TLS-RSA-WITH-ARIA-128-CBC-SHA256.
TLS-RSA-WITH-ARIA-256-CBC-SHA384
Cipher suite TLS-RSA-WITH-ARIA-256-CBC-SHA384.
TLS-ECDHE-RSA-WITH-ARIA-128-CBC-SHA256
Cipher suite TLS-ECDHE-RSA-WITH-ARIA-128-CBC-SHA256.
TLS-ECDHE-RSA-WITH-ARIA-256-CBC-SHA384
Cipher suite TLS-ECDHE-RSA-WITH-ARIA-256-CBC-SHA384.
TLS-ECDHE-ECDSA-WITH-ARIA-128-CBC-SHA256
Cipher suite TLS-ECDHE-ECDSA-WITH-ARIA-128-CBC_SHA256.
TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC-SHA384
Cipher suite TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC_SHA384.
TLS-ECDHE-RSA-WITH-RC4-128-SHA
Cipher suite TLS-ECDHE-RSA-WITH-RC4-128-SHA.
FortiOS 8.0.0 CLI Reference
794
Fortinet Inc.

<!-- 来源页 795 -->
Parameter
Description
Type
Size
Default
Option
Description
TLS-ECDHE-RSA-WITH-3DES-EDE-CBC-SHA
Cipher suite TLS-ECDHE-RSA-WITH-3DES-EDE-CBC-SHA.
TLS-DHE-DSS-WITH-3DES-EDE-CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-3DES-EDE-CBC-SHA.
TLS-RSA-WITH-3DES-EDE-CBC-SHA
Cipher suite TLS-RSA-WITH-3DES-EDE-CBC-SHA.
TLS-RSA-WITH-RC4-128-MD5
Cipher suite TLS-RSA-WITH-RC4-128-MD5.
TLS-RSA-WITH-RC4-128-SHA
Cipher suite TLS-RSA-WITH-RC4-128-SHA.
TLS-DHE-RSA-WITH-DES-CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-DES-CBC-SHA.
TLS-DHE-DSS-WITH-DES-CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-DES-CBC-SHA.
TLS-RSA-WITH-DES-CBC-SHA
Cipher suite TLS-RSA-WITH-DES-CBC-SHA.
priority
SSL/TLS cipher suites priority.
integer
Minimum value:
0 Maximum
value:
4294967295
0
versions
SSL/TLS versions that the cipher suite can be
used with.
option
-tls-1.1 tls-1.2 tls-1.3
**
Option
Description
ssl-3.0
SSL 3.0.
tls-1.0
TLS 1.0.
tls-1.1
TLS 1.1.
FortiOS 8.0.0 CLI Reference
795
Fortinet Inc.

---


<!-- 来源页 796 -->
Parameter
Description
Type
Size
Default
Option
Description
tls-1.2
TLS 1.2.
tls-1.3
TLS 1.3.
** Values may differ between models.
config firewall vip6
Configure virtual IP for IPv6.
config firewall vip6
Description: Configure virtual IP for IPv6.
edit <name>
set add-nat64-route [disable|enable]
set auth-virtual-host {string}
set client-cert [disable|enable]
set color {integer}
set comment {var-string}
set embedded-ipv4-address [disable|enable]
set empty-cert-action [accept|block|...]
set extip {user}
set extport {user}
set h2-support [enable|disable]
set h3-support [enable|disable]
set http-cookie-age {integer}
set http-cookie-domain {string}
set http-cookie-domain-from-host [disable|enable]
set http-cookie-generation {integer}
set http-cookie-path {string}
set http-cookie-share [disable|same-ip]
set http-ip-header [enable|disable]
set http-ip-header-name {string}
set http-multiplex [enable|disable]
set http-redirect [enable|disable]
set https-cookie-secure [disable|enable]
set id {integer}
set ipv4-mappedip {user}
set ipv4-mappedport {user}
set ldb-method [static|round-robin|...]
set mappedip {user}
set mappedport {user}
set max-embryonic-connections {integer}
set monitor <name1>, <name2>, ...
set nat-source-vip [disable|enable]
set nat64 [disable|enable]
set nat66 [disable|enable]
FortiOS 8.0.0 CLI Reference
796
Fortinet Inc.

<!-- 来源页 797 -->
set ndp-reply [disable|enable]
set outlook-web-access [disable|enable]
set persistence [none|http-cookie|...]
set portforward [disable|enable]
set protocol [tcp|udp|...]
config quic
Description: QUIC setting.
set ack-delay-exponent {integer}
set active-connection-id-limit {integer}
set active-migration [enable|disable]
set grease-quic-bit [enable|disable]
set max-ack-delay {integer}
set max-datagram-frame-size {integer}
set max-idle-timeout {integer}
set max-udp-payload-size {integer}
end
config realservers
Description: Select the real servers that this server load balancing VIP will
distribute traffic to.
edit <id>
set client-ip {user}
set healthcheck [disable|enable|...]
set holddown-interval {integer}
set http-host {string}
set ip {user}
set max-connections {integer}
set monitor <name1>, <name2>, ...
set port {integer}
set status [active|standby|...]
set translate-host [enable|disable]
set verify-cert [enable|disable]
set weight {integer}
next
end
set server-type [http|https|...]
set src-filter <range1>, <range2>, ...
set src-vip-filter [disable|enable]
set ssl-accept-ffdhe-groups [enable|disable]
set ssl-algorithm [high|medium|...]
set ssl-certificate <name1>, <name2>, ...
config ssl-cipher-suites
Description: SSL/TLS cipher suites acceptable from a client, ordered by priority.
edit <priority>
set cipher [TLS-AES-128-GCM-SHA256|TLS-AES-256-GCM-SHA384|...]
set versions {option1}, {option2}, ...
next
end
set ssl-client-fallback [disable|enable]
set ssl-client-rekey-count {integer}
set ssl-client-renegotiation [allow|deny|...]
set ssl-client-session-state-max {integer}
set ssl-client-session-state-timeout {integer}
FortiOS 8.0.0 CLI Reference
797
Fortinet Inc.

<!-- 来源页 798 -->
set ssl-client-session-state-type [disable|time|...]
set ssl-dh-bits [768|1024|...]
set ssl-hpkp [disable|enable|...]
set ssl-hpkp-age {integer}
set ssl-hpkp-backup {string}
set ssl-hpkp-include-subdomains [disable|enable]
set ssl-hpkp-primary {string}
set ssl-hpkp-report-uri {var-string}
set ssl-hsts [disable|enable]
set ssl-hsts-age {integer}
set ssl-hsts-include-subdomains [disable|enable]
set ssl-http-location-conversion [enable|disable]
set ssl-http-match-host [enable|disable]
set ssl-http-strip-secure-cookies [enable|disable]
set ssl-max-version [ssl-3.0|tls-1.0|...]
set ssl-min-version [ssl-3.0|tls-1.0|...]
set ssl-mode [half|full]
set ssl-pfs [require|deny|...]
set ssl-send-empty-frags [enable|disable]
set ssl-server-algorithm [high|medium|...]
config ssl-server-cipher-suites
Description: SSL/TLS cipher suites to offer to a server, ordered by priority.
edit <priority>
set cipher [TLS-AES-128-GCM-SHA256|TLS-AES-256-GCM-SHA384|...]
set versions {option1}, {option2}, ...
next
end
set ssl-server-client-certificate {string}
set ssl-server-max-version [ssl-3.0|tls-1.0|...]
set ssl-server-min-version [ssl-3.0|tls-1.0|...]
set ssl-server-renegotiation [enable|disable]
set ssl-server-session-state-max {integer}
set ssl-server-session-state-timeout {integer}
set ssl-server-session-state-type [disable|time|...]
set ssl-upstream [enable|disable]
set type [static-nat|server-load-balance|...]
set user-agent-detect [disable|enable]
set uuid {uuid}
set weblogic-server [disable|enable]
set websphere-server [disable|enable]
next
end
config firewall vip6
Parameter
Description
Type
Size
Default
add-nat64-route
Enable/disable adding NAT64 route.
option
-enable
FortiOS 8.0.0 CLI Reference
798
Fortinet Inc.

<!-- 来源页 799 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable adding NAT64 route.
enable
Enable adding NAT64 route.
auth-virtual-host *
Virtual host for authentication portal.
string
Maximum
length: 79
client-cert
Enable/disable requesting client
certificate.
option
-enable
Option
Description
disable
Disable client certificate request.
enable
Enable client certificate request.
color
Color of icon on the GUI.
integer
Minimum value:
0 Maximum
value: 32
0
comment
Comment.
var-string
Maximum
length: 255
embedded-ipv4-address
Enable/disable use of the lower 32 bits
of the external IPv6 address as
mapped IPv4 address.
option
-disable
Option
Description
disable
Disable use of the lower 32 bits of the external IPv6 address as
mapped IPv4 address.
enable
Enable use of the lower 32 bits of the external IPv6 address as mapped
IPv4 address.
empty-cert-action
Action for an empty client certificate.
option
-block
Option
Description
accept
Accept the SSL handshake if the client certificate is empty.
block
Block the SSL handshake if the client certificate is empty.
accept-unmanageable
Accept the SSL handshake only if the end-point is unmanageable.
FortiOS 8.0.0 CLI Reference
799
Fortinet Inc.

<!-- 来源页 800 -->
Parameter
Description
Type
Size
Default
extip
IPv6 address or address range on the
external interface that you want to
map to an address or address range
on the destination network.
user
Not Specified
extport
Incoming port number range that you
want to map to a port number range on
the destination network.
user
Not Specified
h2-support
Enable/disable HTTP2 support (default
= enable).
option
-enable
Option
Description
enable
Enable HTTP2 support.
disable
Disable HTTP2 support.
h3-support
Enable/disable HTTP3/QUIC support
(default = disable).
option
-disable
Option
Description
enable
Enable HTTP3/QUIC support.
disable
Disable HTTP3/QUIC support.
http-cookie-age
Time in minutes that client web
browsers should keep a cookie.
Default is 60 minutes. 0 = no time limit.
integer
Minimum value:
0 Maximum
value: 525600
60
http-cookie-domain
Domain that HTTP cookie persistence
should apply to.
string
Maximum
length: 35
http-cookie-domain-from-host
Enable/disable use of HTTP cookie
domain from host field in HTTP.
option
-disable
Option
Description
disable
Disable use of HTTP cookie domain from host field in HTTP (use http-cooke-domain setting).
enable
Enable use of HTTP cookie domain from host field in HTTP.
http-cookie-generation
Generation of HTTP cookie to be
accepted. Changing invalidates all
existing cookies.
integer
Minimum value:
0 Maximum
value:
4294967295
0
http-cookie-path
Limit HTTP cookie persistence to the
specified path.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
800
Fortinet Inc.

<!-- 来源页 801 -->
Parameter
Description
Type
Size
Default
http-cookie-share
Control sharing of cookies across
virtual servers. Use of same-ip means
a cookie from one virtual server can be
used by another. Disable stops cookie
sharing.
option
-same-ip
Option
Description
disable
Only allow HTTP cookie to match this virtual server.
same-ip
Allow HTTP cookie to match any virtual server with same IP.
http-ip-header
For HTTP multiplexing, enable to add
the original client IP address in the X-Forwarded-For HTTP header.
option
-disable
Option
Description
enable
Enable adding HTTP header.
disable
Disable adding HTTP header.
http-ip-header-name
For HTTP multiplexing, enter a custom
HTTPS header name. The original
client IP address is added to this
header. If empty, X-Forwarded-For is
used.
string
Maximum
length: 35
http-multiplex
Enable/disable HTTP multiplexing.
option
-disable
Option
Description
enable
Enable HTTP session multiplexing.
disable
Disable HTTP session multiplexing.
http-redirect
Enable/disable redirection of HTTP to
HTTPS.
option
-disable
Option
Description
enable
Enable redirection of HTTP to HTTPS.
disable
Disable redirection of HTTP to HTTPS.
https-cookie-secure
Enable/disable verification that
inserted HTTPS cookies are secure.
option
-disable
FortiOS 8.0.0 CLI Reference
801
Fortinet Inc.

<!-- 来源页 802 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Do not mark cookie as secure, allow sharing between an HTTP and
HTTPS connection.
enable
Mark inserted cookie as secure, cookie can only be used for HTTPS a
connection.
id
Custom defined ID.
integer
Minimum value:
0 Maximum
value: 65535
0
ipv4-mappedip
Range of mapped IP addresses.
Specify the start IP address followed
by a space and the end IP address.
user
Not Specified
ipv4-mappedport
IPv4 port number range on the
destination network to which the
external port number range is mapped.
user
Not Specified
ldb-method
Method used to distribute sessions to
real servers.
option
-static
Option
Description
static
Distribute sessions based on source IP.
round-robin
Distribute sessions based round robin order.
weighted
Distribute sessions based on weight.
least-session
Sends new sessions to the server with the lowest session count.
least-rtt
Distribute new sessions to the server with lowest Round-Trip-Time.
first-alive
Distribute sessions to the first server that is alive.
http-host
Distribute sessions to servers based on host field in HTTP header.
mappedip
Mapped IPv6 address range in the
format startIP-endIP.
user
Not Specified
mappedport
Port number range on the destination
network to which the external port
number range is mapped.
user
Not Specified
max-embryonic-connections
Maximum number of incomplete
connections.
integer
Minimum value:
0 Maximum
value: 100000
1000
monitor <name>
Name of the health check monitor to
use when polling to determine a virtual
server's connectivity status.
Health monitor name.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
802
Fortinet Inc.

<!-- 来源页 803 -->
Parameter
Description
Type
Size
Default
name
Virtual ip6 name.
string
Maximum
length: 79
nat-source-vip
Enable to perform SNAT on traffic from
mappedip to the extip for all egress
interfaces.
option
-disable
Option
Description
disable
Disable nat-source-vip.
enable
Perform SNAT on traffic from mappedip to the extip for all egress
interfaces.
nat64
Enable/disable DNAT64.
option
-disable
Option
Description
disable
Disable DNAT64.
enable
Enable DNAT64.
nat66
Enable/disable DNAT66.
option
-enable
Option
Description
disable
Disable DNAT66.
enable
Enable DNAT66.
ndp-reply
Enable/disable this FortiGate unit's
ability to respond to NDP requests for
this virtual IP address (default =
enable).
option
-enable
Option
Description
disable
Disable this FortiGate unit's ability to respond to NDP requests for this
virtual IP address.
enable
Enable this FortiGate unit's ability to respond to NDP requests for this
virtual IP address.
outlook-web-access
Enable to add the Front-End-Https
header for Microsoft Outlook Web
Access.
option
-disable
Option
Description
disable
Disable Outlook Web Access support.
enable
Enable Outlook Web Access support.
FortiOS 8.0.0 CLI Reference
803
Fortinet Inc.

<!-- 来源页 804 -->
Parameter
Description
Type
Size
Default
persistence
Configure how to make sure that
clients connect to the same server
every time they make a request that is
part of the same session.
option
-none
Option
Description
none
None.
http-cookie
HTTP cookie.
ssl-session-id
SSL session ID.
portforward
Enable port forwarding.
option
-disable
Option
Description
disable
Disable port forward.
enable
Enable/disable port forwarding.
protocol
Protocol to use when forwarding
packets.
option
-tcp
Option
Description
tcp
TCP.
udp
UDP.
sctp
SCTP.
server-type
Protocol to be load balanced by the
virtual server (also called the server
load balance virtual IP).
option
-Option
Description
http
HTTP.
https
HTTPS.
imaps
IMAPS.
pop3s
POP3S.
smtps
SMTPS.
ssl
SSL.
tcp
TCP.
udp
UDP.
ip
IP.
FortiOS 8.0.0 CLI Reference
804
Fortinet Inc.

<!-- 来源页 805 -->
Parameter
Description
Type
Size
Default
src-filter
<range>
Source IP6 filter (x:x:x:x:x:x:x:x/x).
Separate addresses with spaces.
Source-filter range.
string
Maximum
length: 79
src-vip-filter
Enable/disable use of 'src-filter' to
match destinations for the reverse
SNAT rule.
option
-disable
Option
Description
disable
Match any destination for the reverse SNAT rule.
enable
Match only destinations in 'src-filter' for the reverse SNAT rule.
ssl-accept-ffdhe-groups
Enable/disable FFDHE cipher suite for
SSL key exchange.
option
-enable
Option
Description
enable
Accept FFDHE groups.
disable
Do not accept FFDHE groups.
ssl-algorithm
Permitted encryption algorithms for
SSL sessions according to encryption
strength.
option
-high
Option
Description
high
Use AES.
medium
Use AES, 3DES, or RC4.
low
Use AES, 3DES, RC4, or DES.
custom
Use config ssl-cipher-suites to select the cipher suites that are
allowed.
ssl-certificate
<name>
Name of the certificate to use for SSL
handshake.
Certificate list.
string
Maximum
length: 79
ssl-client-fallback
Enable/disable support for preventing
Downgrade Attacks on client
connections (RFC 7507).
option
-enable
Option
Description
disable
Disable.
enable
Enable.
FortiOS 8.0.0 CLI Reference
805
Fortinet Inc.

<!-- 来源页 806 -->
Parameter
Description
Type
Size
Default
ssl-client-rekey-count
Maximum length of data in MB before
triggering a client rekey (0 = disable).
integer
Minimum value:
200 Maximum
value: 1048576
0
ssl-client-renegotiation
Allow, deny, or require secure
renegotiation of client sessions to
comply with RFC 5746.
option
-secure
Option
Description
allow
Allow a SSL client to renegotiate.
deny
Abort any SSL connection that attempts to renegotiate.
secure
Reject any SSL connection that does not offer a RFC 5746 Secure
Renegotiation Indication.
ssl-client-session-state-max
Maximum number of client to FortiGate
SSL session states to keep.
integer
Minimum value:
1 Maximum
value: 10000
1000
ssl-client-session-state-timeout
Number of minutes to keep client to
FortiGate SSL session state.
integer
Minimum value:
1 Maximum
value: 14400
30
ssl-client-session-state-type
How to expire SSL sessions for the
segment of the SSL connection
between the client and the FortiGate.
option
-both
Option
Description
disable
Do not keep session states.
time
Expire session states after this many minutes.
count
Expire session states when this maximum is reached.
both
Expire session states based on time or count, whichever occurs first.
ssl-dh-bits
Number of bits to use in the Diffie-Hellman exchange for RSA encryption
of SSL sessions.
option
-2048
Option
Description
768
768-bit Diffie-Hellman prime.
1024
1024-bit Diffie-Hellman prime.
1536
1536-bit Diffie-Hellman prime.
2048
2048-bit Diffie-Hellman prime.
3072
3072-bit Diffie-Hellman prime.
FortiOS 8.0.0 CLI Reference
806
Fortinet Inc.

<!-- 来源页 807 -->
Parameter
Description
Type
Size
Default
Option
Description
4096
4096-bit Diffie-Hellman prime.
ssl-hpkp
Enable/disable including HPKP header
in response.
option
-disable
Option
Description
disable
Do not add a HPKP header to each HTTP response.
enable
Add a HPKP header to each a HTTP response.
report-only
Add a HPKP Report-Only header to each HTTP response.
ssl-hpkp-age
Number of minutes the web browser
should keep HPKP.
integer
Minimum value:
60 Maximum
value:
157680000
5184000
ssl-hpkp-backup
Certificate to generate backup HPKP
pin from.
string
Maximum
length: 79
ssl-hpkp-include-subdomains
Indicate that HPKP header applies to
all subdomains.
option
-disable
Option
Description
disable
HPKP header does not apply to subdomains.
enable
HPKP header applies to subdomains.
ssl-hpkp-primary
Certificate to generate primary HPKP
pin from.
string
Maximum
length: 79
ssl-hpkp-report-uri
URL to report HPKP violations to.
var-string
Maximum
length: 255
ssl-hsts
Enable/disable including HSTS header
in response.
option
-disable
Option
Description
disable
Do not add a HSTS header to each a HTTP response.
enable
Add a HSTS header to each HTTP response.
ssl-hsts-age
Number of seconds the client should
honor the HSTS setting.
integer
Minimum value:
60 Maximum
value:
157680000
5184000
FortiOS 8.0.0 CLI Reference
807
Fortinet Inc.

<!-- 来源页 808 -->
Parameter
Description
Type
Size
Default
ssl-hsts-include-subdomains
Indicate that HSTS header applies to
all subdomains.
option
-disable
Option
Description
disable
HSTS header does not apply to subdomains.
enable
HSTS header applies to subdomains.
ssl-http-location-conversion
Enable to convert HTTP/HTTPS in the
reply's Location HTTP header field.
option
-disable
Option
Description
enable
Enable HTTP location conversion.
disable
Disable HTTP location conversion.
ssl-http-match-host
Enable/disable HTTP host matching
for location conversion.
option
-enable
Option
Description
enable
Match HTTP host in response header.
disable
Do not match HTTP host.
ssl-http-strip-secure-cookies
*
Enable/disable removal of HTTPS-only
directives in the reply's Set-Cookie
HTTP header fields.
option
-disable
Option
Description
enable
Remove HTTPS-only directives in response Set-Cookie headers.
disable
Do not remove HTTPS-only directives.
ssl-max-version
Highest SSL/TLS version acceptable
from a client.
option
-tls-1.3
Option
Description
ssl-3.0
SSL 3.0.
tls-1.0
TLS 1.0.
tls-1.1
TLS 1.1.
tls-1.2
TLS 1.2.
tls-1.3
TLS 1.3.
FortiOS 8.0.0 CLI Reference
808
Fortinet Inc.

<!-- 来源页 809 -->
Parameter
Description
Type
Size
Default
ssl-min-version
Lowest SSL/TLS version acceptable
from a client.
option
-tls-1.1
Option
Description
ssl-3.0
SSL 3.0.
tls-1.0
TLS 1.0.
tls-1.1
TLS 1.1.
tls-1.2
TLS 1.2.
tls-1.3
TLS 1.3.
ssl-mode
Apply SSL offloading between the
client and the FortiGate (half) or from
the client to the FortiGate and from the
FortiGate to the server (full).
option
-half
Option
Description
half
Client to FortiGate SSL.
full
Client to FortiGate and FortiGate to Server SSL.
ssl-pfs
Select the cipher suites that can be
used for SSL perfect forward secrecy
(PFS). Applies to both client and server
sessions.
option
-require
Option
Description
require
Allow only Diffie-Hellman cipher-suites, so PFS is applied.
deny
Allow only non-Diffie-Hellman cipher-suites, so PFS is not applied.
allow
Allow use of any cipher suite so PFS may or may not be used
depending on the cipher suite selected.
ssl-send-empty-frags
Enable/disable sending empty
fragments to avoid CBC IV attacks
(SSL 3.0 & TLS 1.0 only). May need to
be disabled for compatibility with older
systems.
option
-enable
Option
Description
enable
Send empty fragments.
disable
Do not send empty fragments.
FortiOS 8.0.0 CLI Reference
809
Fortinet Inc.

<!-- 来源页 810 -->
Parameter
Description
Type
Size
Default
ssl-server-algorithm
Permitted encryption algorithms for
the server side of SSL sessions
according to encryption strength.
option
-client
Option
Description
high
Use AES.
medium
Use AES, 3DES, or RC4.
low
Use AES, 3DES, RC4, or DES.
custom
Use config ssl-server-cipher-suites to select the cipher suites that are
allowed.
client
Use the same encryption algorithms for client and server sessions.
ssl-server-client-certificate *
Name of the client certificate
presented to realserver during
SSL/TLS handshake if requested.
string
Maximum
length: 79
ssl-server-max-version
Highest SSL/TLS version acceptable
from a server. Use the client setting by
default.
option
-client
Option
Description
ssl-3.0
SSL 3.0.
tls-1.0
TLS 1.0.
tls-1.1
TLS 1.1.
tls-1.2
TLS 1.2.
tls-1.3
TLS 1.3.
client
Use same value as client configuration.
ssl-server-min-version
Lowest SSL/TLS version acceptable
from a server. Use the client setting by
default.
option
-client
Option
Description
ssl-3.0
SSL 3.0.
tls-1.0
TLS 1.0.
tls-1.1
TLS 1.1.
tls-1.2
TLS 1.2.
tls-1.3
TLS 1.3.
FortiOS 8.0.0 CLI Reference
810
Fortinet Inc.

<!-- 来源页 811 -->
Parameter
Description
Type
Size
Default
Option
Description
client
Use same value as client configuration.
ssl-server-renegotiation
Enable/disable secure renegotiation to
comply with RFC 5746.
option
-enable
Option
Description
enable
Enable secure renegotiation.
disable
Disable secure renegotiation.
ssl-server-session-state-max
Maximum number of FortiGate to
Server SSL session states to keep.
integer
Minimum value:
1 Maximum
value: 10000
100
ssl-server-session-state-timeout
Number of minutes to keep FortiGate
to Server SSL session state.
integer
Minimum value:
1 Maximum
value: 14400
60
ssl-server-session-state-type
How to expire SSL sessions for the
segment of the SSL connection
between the server and the FortiGate.
option
-both
Option
Description
disable
Do not keep session states.
time
Expire session states after this many minutes.
count
Expire session states when this maximum is reached.
both
Expire session states based on time or count, whichever occurs first.
ssl-upstream *
Apply SSL encryption between the
FortiGate and the upstream server
(default = disable).
option
-disable
Option
Description
enable
Apply SSL encryption between the FortiGate and the upstream server.
disable
Do not apply SSL encryption between the FortiGate and the upstream
server. Use plain text.
type
Configure a static NAT server load
balance VIP or access proxy.
option
-static-nat
Option
Description
static-nat
Static NAT.
FortiOS 8.0.0 CLI Reference
811
Fortinet Inc.

<!-- 来源页 812 -->
Parameter
Description
Type
Size
Default
Option
Description
server-load-balance
Server load balance.
access-proxy
Access proxy.
user-agent-detect
Enable/disable detecting device type
by HTTP user-agent if no client
certificate is provided.
option
-enable
Option
Description
disable
Disable detecting unknown devices by HTTP user-agent if no client
certificate is provided.
enable
Enable detecting unknown devices by HTTP user-agent if no client
certificate is provided.
uuid
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not Specified
00000000-0000-0000-0000-000000000000
weblogic-server
Enable to add an HTTP header to
indicate SSL offloading for a WebLogic
server.
option
-disable
Option
Description
disable
Do not add HTTP header indicating SSL offload for WebLogic server.
enable
Add HTTP header indicating SSL offload for WebLogic server.
websphere-server
Enable to add an HTTP header to
indicate SSL offloading for a
WebSphere server.
option
-disable
Option
Description
disable
Do not add HTTP header indicating SSL offload for WebSphere server.
enable
Add HTTP header indicating SSL offload for WebSphere server.
* This parameter may not exist in some models.
FortiOS 8.0.0 CLI Reference
812
Fortinet Inc.

<!-- 来源页 813 -->
config quic
Parameter
Description
Type
Size
Default
ack-delay-exponent
ACK delay exponent (1 - 20, default = 3).
integer
Minimum
value: 1
Maximum
value: 20
3
active-connection-id-limit
Active connection ID limit (1 - 8, default = 2).
integer
Minimum
value: 1
Maximum
value: 8
2
active-migration
Enable/disable active migration (default = disable).
option
-disable
Option
Description
enable
Enable active migration.
disable
Disable active migration.
grease-quic-bit
Enable/disable grease QUIC bit (default = enable).
option
-enable
Option
Description
enable
Enable grease QUIC bit.
disable
Disable grease QUIC bit.
max-ack-delay
Maximum ACK delay in milliseconds (1 - 16383,
default = 25).
integer
Minimum
value: 1
Maximum
value:
16383
25
max-datagram-frame-size
Maximum datagram frame size in bytes (1 - 1500,
default = 1500).
integer
Minimum
value: 1
Maximum
value: 1500
1500
max-idle-timeout
Maximum idle timeout milliseconds (1 - 60000,
default = 30000).
integer
Minimum
value: 1
Maximum
value:
60000
30000
max-udp-payload-size
Maximum UDP payload size in bytes (1200 - 1500,
default = 1500).
integer
Minimum
value: 1200
Maximum
value: 1500
1500
FortiOS 8.0.0 CLI Reference
813
Fortinet Inc.

<!-- 来源页 814 -->
config realservers
Parameter
Description
Type
Size
Default
client-ip
Only clients in this IP range can connect to this
real server.
user
Not Specified
healthcheck
Enable to check the responsiveness of the real
server before forwarding traffic.
option
-vip
Option
Description
disable
Disable per server health check.
enable
Enable per server health check.
vip
Use health check defined in VIP.
holddown-interval
Time in seconds that the system waits before
re-activating a previously down active server in
the active-standby mode. This is to prevent
any flapping issues.
integer
Minimum value:
30 Maximum
value: 65535
300
http-host
HTTP server domain name in HTTP header.
string
Maximum
length: 63
id
Real server ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
ip
IP address of the real server.
user
Not Specified
max-connections
Max number of active connections that can
directed to the real server. When reached,
sessions are sent to other real servers.
integer
Minimum value:
0 Maximum
value:
2147483647
0
monitor
<name>
Name of the health check monitor to use when
polling to determine a virtual server's
connectivity status.
Health monitor name.
string
Maximum
length: 79
port
Port for communicating with the real server.
Required if port forwarding is enabled.
integer
Minimum value:
1 Maximum
value: 65535
0
status
Set the status of the real server to active so
that it can accept traffic, or on standby or
disabled so no traffic is sent.
option
-active
Option
Description
active
Server status active.
FortiOS 8.0.0 CLI Reference
814
Fortinet Inc.

<!-- 来源页 815 -->
Parameter
Description
Type
Size
Default
Option
Description
standby
Server status standby.
disable
Server status disable.
translate-host
Enable/disable translation of hostname/IP from
virtual server to real server.
option
-enable
Option
Description
enable
Enable virtual hostname/IP translation.
disable
Disable virtual hostname/IP translation.
verify-cert
Enable/disable certificate verification of the
real server.
option
-enable
Option
Description
enable
Enable certificate verification.
disable
Disable certificate verification.
weight
Weight of the real server. If weighted load
balancing is enabled, the server with the
highest weight gets more connections.
integer
Minimum value:
1 Maximum
value: 255
1
config ssl-cipher-suites
Parameter
Description
Type
Size
Default
cipher
Cipher suite name.
option
-Option
Description
TLS-AES-128-GCM-SHA256
Cipher suite TLS-AES-128-GCM-SHA256.
TLS-AES-256-GCM-SHA384
Cipher suite TLS-AES-256-GCM-SHA384.
TLS-CHACHA20-POLY1305-SHA256
Cipher suite TLS-CHACHA20-POLY1305-SHA256.
FortiOS 8.0.0 CLI Reference
815
Fortinet Inc.

<!-- 来源页 816 -->
Parameter
Description
Type
Size
Default
Option
Description
TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256
Cipher suite TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256.
TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256
Cipher suite TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256.
TLS-DHE-RSA-WITH-CHACHA20-POLY1305-SHA256
Cipher suite TLS-DHE-RSA-WITH-CHACHA20-POLY1305-SHA256.
TLS-DHE-RSA-WITH-AES-128-CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-AES-128-CBC-SHA.
TLS-DHE-RSA-WITH-AES-256-CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-AES-256-CBC-SHA.
TLS-DHE-RSA-WITH-AES-128-CBC-SHA256
Cipher suite TLS-DHE-RSA-WITH-AES-128-CBC-SHA256.
TLS-DHE-RSA-WITH-AES-128-GCM-SHA256
Cipher suite TLS-DHE-RSA-WITH-AES-128-GCM-SHA256.
TLS-DHE-RSA-WITH-AES-256-CBC-SHA256
Cipher suite TLS-DHE-RSA-WITH-AES-256-CBC-SHA256.
TLS-DHE-RSA-WITH-AES-256-GCM-SHA384
Cipher suite TLS-DHE-RSA-WITH-AES-256-GCM-SHA384.
TLS-DHE-DSS-WITH-AES-128-CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-AES-128-CBC-SHA.
FortiOS 8.0.0 CLI Reference
816
Fortinet Inc.

<!-- 来源页 817 -->
Parameter
Description
Type
Size
Default
Option
Description
TLS-DHE-DSS-WITH-AES-256-CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-AES-256-CBC-SHA.
TLS-DHE-DSS-WITH-AES-128-CBC-SHA256
Cipher suite TLS-DHE-DSS-WITH-AES-128-CBC-SHA256.
TLS-DHE-DSS-WITH-AES-128-GCM-SHA256
Cipher suite TLS-DHE-DSS-WITH-AES-128-GCM-SHA256.
TLS-DHE-DSS-WITH-AES-256-CBC-SHA256
Cipher suite TLS-DHE-DSS-WITH-AES-256-CBC-SHA256.
TLS-DHE-DSS-WITH-AES-256-GCM-SHA384
Cipher suite TLS-DHE-DSS-WITH-AES-256-GCM-SHA384.
TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA
Cipher suite TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA.
TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256
Cipher suite TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256.
TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256
Cipher suite TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256.
TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA
Cipher suite TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA.
TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384
Cipher suite TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384.
FortiOS 8.0.0 CLI Reference
817
Fortinet Inc.

<!-- 来源页 818 -->
Parameter
Description
Type
Size
Default
Option
Description
TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384
Cipher suite TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384.
TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA.
TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256.
TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256.
TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA.
TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384.
TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384.
TLS-RSA-WITH-AES-128-CBC-SHA
Cipher suite TLS-RSA-WITH-AES-128-CBC-SHA.
TLS-RSA-WITH-AES-256-CBC-SHA
Cipher suite TLS-RSA-WITH-AES-256-CBC-SHA.
TLS-RSA-WITH-AES-128-CBC-SHA256
Cipher suite TLS-RSA-WITH-AES-128-CBC-SHA256.
FortiOS 8.0.0 CLI Reference
818
Fortinet Inc.

<!-- 来源页 819 -->
Parameter
Description
Type
Size
Default
Option
Description
TLS-RSA-WITH-AES-128-GCM-SHA256
Cipher suite TLS-RSA-WITH-AES-128-GCM-SHA256.
TLS-RSA-WITH-AES-256-CBC-SHA256
Cipher suite TLS-RSA-WITH-AES-256-CBC-SHA256.
TLS-RSA-WITH-AES-256-GCM-SHA384
Cipher suite TLS-RSA-WITH-AES-256-GCM-SHA384.
TLS-RSA-WITH-CAMELLIA-128-CBC-SHA
Cipher suite TLS-RSA-WITH-CAMELLIA-128-CBC-SHA.
TLS-RSA-WITH-CAMELLIA-256-CBC-SHA
Cipher suite TLS-RSA-WITH-CAMELLIA-256-CBC-SHA.
TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256
Cipher suite TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256.
TLS-RSA-WITH-CAMELLIA-256-CBC-SHA256
Cipher suite TLS-RSA-WITH-CAMELLIA-256-CBC-SHA256.
TLS-DHE-RSA-WITH-3DES-EDE-CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-3DES-EDE-CBC-SHA.
TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA.
TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA
Cipher suite TLS-DSS-RSA-WITH-CAMELLIA-128-CBC-SHA.
FortiOS 8.0.0 CLI Reference
819
Fortinet Inc.

<!-- 来源页 820 -->
Parameter
Description
Type
Size
Default
Option
Description
TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA.
TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA.
TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256
Cipher suite TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256.
TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256
Cipher suite TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256.
TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256
Cipher suite TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256.
TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA256
Cipher suite TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA256.
TLS-DHE-RSA-WITH-SEED-CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-SEED-CBC-SHA.
TLS-DHE-DSS-WITH-SEED-CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-SEED-CBC-SHA.
TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256
Cipher suite TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256.
FortiOS 8.0.0 CLI Reference
820
Fortinet Inc.

<!-- 来源页 821 -->
Parameter
Description
Type
Size
Default
Option
Description
TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384
Cipher suite TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384.
TLS-DHE-DSS-WITH-ARIA-128-CBC-SHA256
Cipher suite TLS-DHE-DSS-WITH-ARIA-128-CBC-SHA256.
TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384
Cipher suite TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384.
TLS-RSA-WITH-SEED-CBC-SHA
Cipher suite TLS-RSA-WITH-SEED-CBC-SHA.
TLS-RSA-WITH-ARIA-128-CBC-SHA256
Cipher suite TLS-RSA-WITH-ARIA-128-CBC-SHA256.
TLS-RSA-WITH-ARIA-256-CBC-SHA384
Cipher suite TLS-RSA-WITH-ARIA-256-CBC-SHA384.
TLS-ECDHE-RSA-WITH-ARIA-128-CBC-SHA256
Cipher suite TLS-ECDHE-RSA-WITH-ARIA-128-CBC-SHA256.
TLS-ECDHE-RSA-WITH-ARIA-256-CBC-SHA384
Cipher suite TLS-ECDHE-RSA-WITH-ARIA-256-CBC-SHA384.
TLS-ECDHE-ECDSA-WITH-ARIA-128-CBC-SHA256
Cipher suite TLS-ECDHE-ECDSA-WITH-ARIA-128-CBC_SHA256.
TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC-SHA384
Cipher suite TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC_SHA384.
FortiOS 8.0.0 CLI Reference
821
Fortinet Inc.

<!-- 来源页 822 -->
Parameter
Description
Type
Size
Default
Option
Description
TLS-ECDHE-RSA-WITH-RC4-128-SHA
Cipher suite TLS-ECDHE-RSA-WITH-RC4-128-SHA.
TLS-ECDHE-RSA-WITH-3DES-EDE-CBC-SHA
Cipher suite TLS-ECDHE-RSA-WITH-3DES-EDE-CBC-SHA.
TLS-DHE-DSS-WITH-3DES-EDE-CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-3DES-EDE-CBC-SHA.
TLS-RSA-WITH-3DES-EDE-CBC-SHA
Cipher suite TLS-RSA-WITH-3DES-EDE-CBC-SHA.
TLS-RSA-WITH-RC4-128-MD5
Cipher suite TLS-RSA-WITH-RC4-128-MD5.
TLS-RSA-WITH-RC4-128-SHA
Cipher suite TLS-RSA-WITH-RC4-128-SHA.
TLS-DHE-RSA-WITH-DES-CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-DES-CBC-SHA.
TLS-DHE-DSS-WITH-DES-CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-DES-CBC-SHA.
TLS-RSA-WITH-DES-CBC-SHA
Cipher suite TLS-RSA-WITH-DES-CBC-SHA.
priority
SSL/TLS cipher suites priority.
integer
Minimum value:
0 Maximum
value:
4294967295
0
versions
SSL/TLS versions that the cipher suite can be
used with.
option
-ssl-3.0 tls-1.0 tls-1.1
tls-1.2 tls-1.3
FortiOS 8.0.0 CLI Reference
822
Fortinet Inc.

<!-- 来源页 823 -->
Parameter
Description
Type
Size
Default
Option
Description
ssl-3.0
SSL 3.0.
tls-1.0
TLS 1.0.
tls-1.1
TLS 1.1.
tls-1.2
TLS 1.2.
tls-1.3
TLS 1.3.
config ssl-server-cipher-suites
Parameter
Description
Type
Size
Default
cipher
Cipher suite name.
option
-Option
Description
TLS-AES-128-GCM-SHA256
Cipher suite TLS-AES-128-GCM-SHA256.
TLS-AES-256-GCM-SHA384
Cipher suite TLS-AES-256-GCM-SHA384.
TLS-CHACHA20-POLY1305-SHA256
Cipher suite TLS-CHACHA20-POLY1305-SHA256.
TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256
Cipher suite TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256.
TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256
Cipher suite TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256.
TLS-DHE-RSA-WITH-CHACHA20-POLY1305-SHA256
Cipher suite TLS-DHE-RSA-WITH-CHACHA20-POLY1305-SHA256.
FortiOS 8.0.0 CLI Reference
823
Fortinet Inc.

<!-- 来源页 824 -->
Parameter
Description
Type
Size
Default
Option
Description
TLS-DHE-RSA-WITH-AES-128-CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-AES-128-CBC-SHA.
TLS-DHE-RSA-WITH-AES-256-CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-AES-256-CBC-SHA.
TLS-DHE-RSA-WITH-AES-128-CBC-SHA256
Cipher suite TLS-DHE-RSA-WITH-AES-128-CBC-SHA256.
TLS-DHE-RSA-WITH-AES-128-GCM-SHA256
Cipher suite TLS-DHE-RSA-WITH-AES-128-GCM-SHA256.
TLS-DHE-RSA-WITH-AES-256-CBC-SHA256
Cipher suite TLS-DHE-RSA-WITH-AES-256-CBC-SHA256.
TLS-DHE-RSA-WITH-AES-256-GCM-SHA384
Cipher suite TLS-DHE-RSA-WITH-AES-256-GCM-SHA384.
TLS-DHE-DSS-WITH-AES-128-CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-AES-128-CBC-SHA.
TLS-DHE-DSS-WITH-AES-256-CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-AES-256-CBC-SHA.
TLS-DHE-DSS-WITH-AES-128-CBC-SHA256
Cipher suite TLS-DHE-DSS-WITH-AES-128-CBC-SHA256.
TLS-DHE-DSS-WITH-AES-128-GCM-SHA256
Cipher suite TLS-DHE-DSS-WITH-AES-128-GCM-SHA256.
TLS-DHE-DSS-WITH-AES-256-CBC-SHA256
Cipher suite TLS-DHE-DSS-WITH-AES-256-CBC-SHA256.
FortiOS 8.0.0 CLI Reference
824
Fortinet Inc.

<!-- 来源页 825 -->
Parameter
Description
Type
Size
Default
Option
Description
TLS-DHE-DSS-WITH-AES-256-GCM-SHA384
Cipher suite TLS-DHE-DSS-WITH-AES-256-GCM-SHA384.
TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA
Cipher suite TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA.
TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256
Cipher suite TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256.
TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256
Cipher suite TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256.
TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA
Cipher suite TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA.
TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384
Cipher suite TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384.
TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384
Cipher suite TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384.
TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA.
TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256.
FortiOS 8.0.0 CLI Reference
825
Fortinet Inc.

<!-- 来源页 826 -->
Parameter
Description
Type
Size
Default
Option
Description
TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256.
TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA.
TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384.
TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384.
TLS-RSA-WITH-AES-128-CBC-SHA
Cipher suite TLS-RSA-WITH-AES-128-CBC-SHA.
TLS-RSA-WITH-AES-256-CBC-SHA
Cipher suite TLS-RSA-WITH-AES-256-CBC-SHA.
TLS-RSA-WITH-AES-128-CBC-SHA256
Cipher suite TLS-RSA-WITH-AES-128-CBC-SHA256.
TLS-RSA-WITH-AES-128-GCM-SHA256
Cipher suite TLS-RSA-WITH-AES-128-GCM-SHA256.
TLS-RSA-WITH-AES-256-CBC-SHA256
Cipher suite TLS-RSA-WITH-AES-256-CBC-SHA256.
TLS-RSA-WITH-AES-256-GCM-SHA384
Cipher suite TLS-RSA-WITH-AES-256-GCM-SHA384.
FortiOS 8.0.0 CLI Reference
826
Fortinet Inc.

<!-- 来源页 827 -->
Parameter
Description
Type
Size
Default
Option
Description
TLS-RSA-WITH-CAMELLIA-128-CBC-SHA
Cipher suite TLS-RSA-WITH-CAMELLIA-128-CBC-SHA.
TLS-RSA-WITH-CAMELLIA-256-CBC-SHA
Cipher suite TLS-RSA-WITH-CAMELLIA-256-CBC-SHA.
TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256
Cipher suite TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256.
TLS-RSA-WITH-CAMELLIA-256-CBC-SHA256
Cipher suite TLS-RSA-WITH-CAMELLIA-256-CBC-SHA256.
TLS-DHE-RSA-WITH-3DES-EDE-CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-3DES-EDE-CBC-SHA.
TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA.
TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA
Cipher suite TLS-DSS-RSA-WITH-CAMELLIA-128-CBC-SHA.
TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA.
TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA.
FortiOS 8.0.0 CLI Reference
827
Fortinet Inc.

<!-- 来源页 828 -->
Parameter
Description
Type
Size
Default
Option
Description
TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256
Cipher suite TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256.
TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256
Cipher suite TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256.
TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256
Cipher suite TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256.
TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA256
Cipher suite TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA256.
TLS-DHE-RSA-WITH-SEED-CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-SEED-CBC-SHA.
TLS-DHE-DSS-WITH-SEED-CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-SEED-CBC-SHA.
TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256
Cipher suite TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256.
TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384
Cipher suite TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384.
TLS-DHE-DSS-WITH-ARIA-128-CBC-SHA256
Cipher suite TLS-DHE-DSS-WITH-ARIA-128-CBC-SHA256.
FortiOS 8.0.0 CLI Reference
828
Fortinet Inc.

<!-- 来源页 829 -->
Parameter
Description
Type
Size
Default
Option
Description
TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384
Cipher suite TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384.
TLS-RSA-WITH-SEED-CBC-SHA
Cipher suite TLS-RSA-WITH-SEED-CBC-SHA.
TLS-RSA-WITH-ARIA-128-CBC-SHA256
Cipher suite TLS-RSA-WITH-ARIA-128-CBC-SHA256.
TLS-RSA-WITH-ARIA-256-CBC-SHA384
Cipher suite TLS-RSA-WITH-ARIA-256-CBC-SHA384.
TLS-ECDHE-RSA-WITH-ARIA-128-CBC-SHA256
Cipher suite TLS-ECDHE-RSA-WITH-ARIA-128-CBC-SHA256.
TLS-ECDHE-RSA-WITH-ARIA-256-CBC-SHA384
Cipher suite TLS-ECDHE-RSA-WITH-ARIA-256-CBC-SHA384.
TLS-ECDHE-ECDSA-WITH-ARIA-128-CBC-SHA256
Cipher suite TLS-ECDHE-ECDSA-WITH-ARIA-128-CBC_SHA256.
TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC-SHA384
Cipher suite TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC_SHA384.
TLS-ECDHE-RSA-WITH-RC4-128-SHA
Cipher suite TLS-ECDHE-RSA-WITH-RC4-128-SHA.
TLS-ECDHE-RSA-WITH-3DES-EDE-CBC-SHA
Cipher suite TLS-ECDHE-RSA-WITH-3DES-EDE-CBC-SHA.
FortiOS 8.0.0 CLI Reference
829
Fortinet Inc.

<!-- 来源页 830 -->
Parameter
Description
Type
Size
Default
Option
Description
TLS-DHE-DSS-WITH-3DES-EDE-CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-3DES-EDE-CBC-SHA.
TLS-RSA-WITH-3DES-EDE-CBC-SHA
Cipher suite TLS-RSA-WITH-3DES-EDE-CBC-SHA.
TLS-RSA-WITH-RC4-128-MD5
Cipher suite TLS-RSA-WITH-RC4-128-MD5.
TLS-RSA-WITH-RC4-128-SHA
Cipher suite TLS-RSA-WITH-RC4-128-SHA.
TLS-DHE-RSA-WITH-DES-CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-DES-CBC-SHA.
TLS-DHE-DSS-WITH-DES-CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-DES-CBC-SHA.
TLS-RSA-WITH-DES-CBC-SHA
Cipher suite TLS-RSA-WITH-DES-CBC-SHA.
priority
SSL/TLS cipher suites priority.
integer
Minimum value:
0 Maximum
value:
4294967295
0
versions
SSL/TLS versions that the cipher suite can be
used with.
option
-ssl-3.0 tls-1.0 tls-1.1
tls-1.2 tls-1.3
Option
Description
ssl-3.0
SSL 3.0.
tls-1.0
TLS 1.0.
tls-1.1
TLS 1.1.
tls-1.2
TLS 1.2.
tls-1.3
TLS 1.3.
FortiOS 8.0.0 CLI Reference
830
Fortinet Inc.

---


<!-- 来源页 831 -->
config firewall vipgrp
Configure IPv4 virtual IP groups.
config firewall vipgrp
Description: Configure IPv4 virtual IP groups.
edit <name>
set color {integer}
set comments {var-string}
set interface {string}
set member <name1>, <name2>, ...
set uuid {uuid}
next
end
config firewall vipgrp
Parameter
Description
Type
Size
Default
color
Integer value to determine the color of the
icon in the GUI (range 1 to 32, default = 0,
which sets the value to 1).
integer
Minimum
value: 0
Maximum
value: 32
0
comments
Comment.
var-string
Maximum
length: 255
interface
Interface.
string
Maximum
length: 35
member
<name>
Member VIP objects of the group (Separate
multiple objects with a space).
VIP name.
string
Maximum
length: 79
name
VIP group name.
string
Maximum
length: 79
uuid
Universally Unique Identifier (UUID;
automatically assigned but can be manually
reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
config firewall vipgrp6
Configure IPv6 virtual IP groups.
config firewall vipgrp6
Description: Configure IPv6 virtual IP groups.
edit <name>
FortiOS 8.0.0 CLI Reference
831
Fortinet Inc.

---


<!-- 来源页 831 -->
config firewall vipgrp
Configure IPv4 virtual IP groups.
config firewall vipgrp
Description: Configure IPv4 virtual IP groups.
edit <name>
set color {integer}
set comments {var-string}
set interface {string}
set member <name1>, <name2>, ...
set uuid {uuid}
next
end
config firewall vipgrp
Parameter
Description
Type
Size
Default
color
Integer value to determine the color of the
icon in the GUI (range 1 to 32, default = 0,
which sets the value to 1).
integer
Minimum
value: 0
Maximum
value: 32
0
comments
Comment.
var-string
Maximum
length: 255
interface
Interface.
string
Maximum
length: 35
member
<name>
Member VIP objects of the group (Separate
multiple objects with a space).
VIP name.
string
Maximum
length: 79
name
VIP group name.
string
Maximum
length: 79
uuid
Universally Unique Identifier (UUID;
automatically assigned but can be manually
reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
config firewall vipgrp6
Configure IPv6 virtual IP groups.
config firewall vipgrp6
Description: Configure IPv6 virtual IP groups.
edit <name>
FortiOS 8.0.0 CLI Reference
831
Fortinet Inc.
