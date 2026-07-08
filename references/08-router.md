# 路由

> 来源: FortiOS-8.0.0-CLI_Reference.pdf
> 覆盖命令/章节: router
> 本文件由 extract_pdf.py 从官方 PDF 自动提取，请勿手动编辑；
> 如需修正请修改 map.json 后重跑脚本。

---


<!-- 来源页 1114 -->
router
This section includes syntax for the following commands:
l config router access-list on page 1114
l config router access-list6 on page 1116
l config router aspath-list on page 1117
l config router auth-path on page 1118
l config router bfd on page 1118
l config router bfd6 on page 1120
l config router bgp on page 1121
l config router community-list on page 1192
l config router extcommunity-list on page 1193
l config router isis on page 1194
l config router key-chain on page 1208
l config router multicast-flow on page 1228
l config router multicast on page 1209
l config router multicast6-flow on page 1227
l config router multicast6 on page 1220
l config router ospf on page 1229
l config router ospf6 on page 1245
l config router policy on page 1260
l config router policy6 on page 1263
l config router prefix-list on page 1266
l config router prefix-list6 on page 1267
l config router rip on page 1268
l config router ripng on page 1275
l config router route-map on page 1281
l config router setting on page 1287
l config router static on page 1288
l config router static6 on page 1291
config router access-list
Configure access lists.
config router access-list
Description: Configure access lists.
edit <name>
set comments {string}
FortiOS 8.0.0 CLI Reference
1114
Fortinet Inc.

<!-- 来源页 1115 -->
config rule
Description: Rule.
edit <id>
set action [permit|deny]
set exact-match [enable|disable]
set prefix {user}
set wildcard {user}
next
end
next
end
config router access-list
Parameter
Description
Type
Size
Default
comments
Comment.
string
Maximum length:
127
name
Name.
string
Maximum length: 35
config rule
Parameter
Description
Type
Size
Default
action
Permit or deny this IP address and netmask
prefix.
option
-permit
Option
Description
permit
Permit or allow this IP address and netmask prefix.
deny
Deny this IP address and netmask prefix.
exact-match
Enable/disable exact match.
option
-disable
Option
Description
enable
Enable exact match.
disable
Disable exact match.
id
Rule ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
prefix
IPv4 prefix to define regular filter criteria, such as
"any" or subnets.
user
Not Specified
wildcard
Wildcard to define Cisco-style wildcard filter
criteria.
user
Not Specified
FortiOS 8.0.0 CLI Reference
1115
Fortinet Inc.

<!-- 来源页 1116 -->
config router access-list6
Configure IPv6 access lists.
config router access-list6
Description: Configure IPv6 access lists.
edit <name>
set comments {string}
config rule
Description: Rule.
edit <id>
set action [permit|deny]
set exact-match [enable|disable]
set flags {integer}
set prefix6 {user}
next
end
next
end
config router access-list6
Parameter
Description
Type
Size
Default
comments
Comment.
string
Maximum length:
127
name
Name.
string
Maximum length: 35
config rule
Parameter
Description
Type
Size
Default
action
Permit or deny this IP address and netmask
prefix.
option
-permit
Option
Description
permit
Permit or allow this IP address and netmask prefix.
deny
Deny this IP address and netmask prefix.
exact-match
Enable/disable exact prefix match.
option
-disable
Option
Description
enable
Enable exact match.
disable
Disable exact match.
FortiOS 8.0.0 CLI Reference
1116
Fortinet Inc.

<!-- 来源页 1117 -->
Parameter
Description
Type
Size
Default
flags
Flags. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
id
Rule ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
prefix6
IPv6 prefix to define regular filter criteria, such as
"any" or subnets.
user
Not Specified
config router aspath-list
Configure Autonomous System (AS) path lists.
config router aspath-list
Description: Configure Autonomous System (AS) path lists.
edit <name>
config rule
Description: AS path list rule.
edit <id>
set action [deny|permit]
set regexp {string}
next
end
next
end
config router aspath-list
Parameter
Description
Type
Size
Default
name
AS path list name.
string
Maximum length:
35
config rule
Parameter
Description
Type
Size
Default
action
Permit or deny route-based operations, based
on the route's AS_PATH attribute.
option
-FortiOS 8.0.0 CLI Reference
1117
Fortinet Inc.

<!-- 来源页 1118 -->
Parameter
Description
Type
Size
Default
Option
Description
deny
Deny route-based operations.
permit
Permit route-based operations.
id
ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
regexp
Regular-expression to match the Border
Gateway Protocol (BGP) AS paths.
string
Maximum
length: 63
config router auth-path
Configure authentication based routing.
config router auth-path
Description: Configure authentication based routing.
edit <name>
set device {string}
set gateway {ipv4-address}
next
end
config router auth-path
Parameter
Description
Type
Size
Default
device
Outgoing interface.
string
Maximum
length: 35
gateway
Gateway IP address.
ipv4-address
Not
Specified
0.0.0.0
name
Name of the entry.
string
Maximum
length: 15
config router bfd
Configure BFD.
config router bfd
Description: Configure BFD.
FortiOS 8.0.0 CLI Reference
1118
Fortinet Inc.

<!-- 来源页 1119 -->
config multihop-template
Description: BFD multi-hop template table.
edit <id>
set auth-mode [none|md5]
set bfd-desired-min-tx {integer}
set bfd-detect-mult {integer}
set bfd-required-min-rx {integer}
set dst {ipv4-classnet}
set md5-key {password}
set src {ipv4-classnet}
next
end
config neighbor
Description: Neighbor.
edit <ip>
set interface {string}
next
end
end
config multihop-template
Parameter
Description
Type
Size
Default
auth-mode
Authentication mode.
option
-none
Option
Description
none
None.
md5
Meticulous MD5 mode.
bfd-desired-min-tx
BFD desired minimal transmit interval
(milliseconds).
integer
Minimum value:
100 Maximum
value: 30000
250
bfd-detect-mult
BFD detection multiplier.
integer
Minimum value:
3 Maximum
value: 50
3
bfd-required-min-rx
BFD required minimal receive interval
(milliseconds).
integer
Minimum value:
100 Maximum
value: 30000
250
dst
Destination prefix.
ipv4-classnet
Not Specified
0.0.0.0
0.0.0.0
id
ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
md5-key
MD5 key of key ID 1.
password
Not Specified
FortiOS 8.0.0 CLI Reference
1119
Fortinet Inc.

<!-- 来源页 1120 -->
Parameter
Description
Type
Size
Default
src
Source prefix.
ipv4-classnet
Not Specified
0.0.0.0
0.0.0.0
config neighbor
Parameter
Description
Type
Size
Default
interface
Interface name.
string
Maximum
length: 15
ip
IPv4 address of the BFD neighbor.
ipv4-address
Not
Specified
0.0.0.0
config router bfd6
Configure IPv6 BFD.
config router bfd6
Description: Configure IPv6 BFD.
config multihop-template
Description: BFD IPv6 multi-hop template table.
edit <id>
set auth-mode [none|md5]
set bfd-desired-min-tx {integer}
set bfd-detect-mult {integer}
set bfd-required-min-rx {integer}
set dst {ipv6-network}
set md5-key {password}
set src {ipv6-network}
next
end
config neighbor
Description: Configure neighbor of IPv6 BFD.
edit <ip6-address>
set interface {string}
next
end
end
config multihop-template
Parameter
Description
Type
Size
Default
auth-mode
Authentication mode.
option
-none
FortiOS 8.0.0 CLI Reference
1120
Fortinet Inc.

<!-- 来源页 1121 -->
Parameter
Description
Type
Size
Default
Option
Description
none
None.
md5
Meticulous MD5 mode.
bfd-desired-min-tx
BFD desired minimal transmit interval
(milliseconds).
integer
Minimum value:
100 Maximum
value: 30000
250
bfd-detect-mult
BFD detection multiplier.
integer
Minimum value:
3 Maximum
value: 50
3
bfd-required-min-rx
BFD required minimal receive interval
(milliseconds).
integer
Minimum value:
100 Maximum
value: 30000
250
dst
Destination prefix.
ipv6-network
Not Specified
::/0
id
ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
md5-key
MD5 key of key ID 1.
password
Not Specified
src
Source prefix.
ipv6-network
Not Specified
::/0
config neighbor
Parameter
Description
Type
Size
Default
interface
Interface to the BFD neighbor.
string
Maximum
length: 15
ip6-address
IPv6 address of the BFD neighbor.
ipv6-address
Not
Specified
::
config router bgp
Configure BGP.
config router bgp
Description: Configure BGP.
set additional-path [enable|disable]
set additional-path-select {integer}
set additional-path-select-vpnv4 {integer}
FortiOS 8.0.0 CLI Reference
1121
Fortinet Inc.

<!-- 来源页 1122 -->
set additional-path-select-vpnv6 {integer}
set additional-path-select6 {integer}
set additional-path-vpnv4 [enable|disable]
set additional-path-vpnv6 [enable|disable]
set additional-path6 [enable|disable]
config admin-distance
Description: Administrative distance modifications.
edit <id>
set distance {integer}
set neighbour-prefix {ipv4-classnet}
set route-list {string}
next
end
config aggregate-address
Description: BGP aggregate address table.
edit <id>
set as-set [enable|disable]
set prefix {ipv4-classnet-any}
set summary-only [enable|disable]
next
end
config aggregate-address6
Description: BGP IPv6 aggregate address table.
edit <id>
set as-set [enable|disable]
set prefix6 {ipv6-prefix}
set summary-only [enable|disable]
next
end
set always-compare-med [enable|disable]
set as {user}
set bestpath-as-path-ignore [enable|disable]
set bestpath-cmp-confed-aspath [enable|disable]
set bestpath-cmp-routerid [enable|disable]
set bestpath-med-confed [enable|disable]
set bestpath-med-missing-as-worst [enable|disable]
set client-to-client-reflection [enable|disable]
set cluster-id {ipv4-address-any}
set confederation-identifier {integer}
set confederation-peers <peer1>, <peer2>, ...
set cross-family-conditional-adv [enable|disable]
set dampening [enable|disable]
set dampening-max-suppress-time {integer}
set dampening-reachability-half-life {integer}
set dampening-reuse {integer}
set dampening-route-map {string}
set dampening-suppress {integer}
set dampening-unreachability-half-life {integer}
set dampening6 [enable|disable]
set dampening6-max-suppress-time {integer}
set dampening6-reachability-half-life {integer}
set dampening6-reuse {integer}
FortiOS 8.0.0 CLI Reference
1122
Fortinet Inc.

<!-- 来源页 1123 -->
set dampening6-route-map {string}
set dampening6-suppress {integer}
set dampening6-unreachability-half-life {integer}
set default-local-preference {integer}
set deterministic-med [enable|disable]
set display-options {integer}
set distance-external {integer}
set distance-internal {integer}
set distance-local {integer}
set ebgp-multipath [enable|disable]
set enforce-first-as [enable|disable]
set fast-external-failover [enable|disable]
set graceful-end-on-timer [enable|disable]
set graceful-restart [enable|disable]
set graceful-restart-time {integer}
set graceful-stalepath-time {integer}
set graceful-update-delay {integer}
set holdtime-timer {integer}
set ibgp-multipath [enable|disable]
set ignore-optional-capability [enable|disable]
set keepalive-timer {integer}
set log-neighbour-changes [enable|disable]
set multipath-recursive-distance [enable|disable]
config neighbor
Description: BGP neighbor table.
edit <ip>
set activate [enable|disable]
set activate-evpn [enable|disable]
set activate-vpnv4 [enable|disable]
set activate-vpnv6 [enable|disable]
set activate6 [enable|disable]
set additional-path [send|receive|...]
set additional-path-vpnv4 [send|receive|...]
set additional-path-vpnv6 [send|receive|...]
set additional-path6 [send|receive|...]
set adv-additional-path {integer}
set adv-additional-path-vpnv4 {integer}
set adv-additional-path-vpnv6 {integer}
set adv-additional-path6 {integer}
set adv-evpn-route {option1}, {option2}, ...
set advertisement-interval {integer}
set allowas-in {integer}
set allowas-in-enable [enable|disable]
set allowas-in-enable-evpn [enable|disable]
set allowas-in-enable-vpnv4 [enable|disable]
set allowas-in-enable-vpnv6 [enable|disable]
set allowas-in-enable6 [enable|disable]
set allowas-in-evpn {integer}
set allowas-in-vpnv4 {integer}
set allowas-in-vpnv6 {integer}
set allowas-in6 {integer}
set as-override [enable|disable]
FortiOS 8.0.0 CLI Reference
1123
Fortinet Inc.

<!-- 来源页 1124 -->
set as-override6 [enable|disable]
set attribute-unchanged {option1}, {option2}, ...
set attribute-unchanged-vpnv4 {option1}, {option2}, ...
set attribute-unchanged-vpnv6 {option1}, {option2}, ...
set attribute-unchanged6 {option1}, {option2}, ...
set auth-options {string}
set bfd [enable|disable]
set capability-default-originate [enable|disable]
set capability-default-originate6 [enable|disable]
set capability-dynamic [enable|disable]
set capability-graceful-restart [enable|disable]
set capability-graceful-restart-evpn [enable|disable]
set capability-graceful-restart-vpnv4 [enable|disable]
set capability-graceful-restart-vpnv6 [enable|disable]
set capability-graceful-restart6 [enable|disable]
set capability-orf [none|receive|...]
set capability-orf6 [none|receive|...]
set capability-route-refresh [enable|disable]
config conditional-advertise
Description: Conditional advertisement.
edit <advertise-routemap>
set condition-routemap <name1>, <name2>, ...
set condition-type [exist|non-exist]
next
end
config conditional-advertise6
Description: IPv6 conditional advertisement.
edit <advertise-routemap>
set condition-routemap <name1>, <name2>, ...
set condition-type [exist|non-exist]
next
end
set connect-timer {integer}
set default-originate-routemap {string}
set default-originate-routemap6 {string}
set description {string}
set display-options {integer}
set distribute-list-in {string}
set distribute-list-in-vpnv4 {string}
set distribute-list-in-vpnv6 {string}
set distribute-list-in6 {string}
set distribute-list-out {string}
set distribute-list-out-vpnv4 {string}
set distribute-list-out-vpnv6 {string}
set distribute-list-out6 {string}
set dont-capability-negotiate [enable|disable]
set ebgp-enforce-multihop [enable|disable]
set ebgp-multihop-ttl {integer}
set enforce-preferred-source [enable|disable]
set filter-list-in {string}
set filter-list-in-vpnv4 {string}
set filter-list-in-vpnv6 {string}
FortiOS 8.0.0 CLI Reference
1124
Fortinet Inc.

<!-- 来源页 1125 -->
set filter-list-in6 {string}
set filter-list-out {string}
set filter-list-out-vpnv4 {string}
set filter-list-out-vpnv6 {string}
set filter-list-out6 {string}
set graceful-shutdown-community {string}
set graceful-shutdown-delay {integer}
set graceful-shutdown-local-preference {integer}
set holdtime-timer {integer}
set interface {string}
set keep-alive-timer {integer}
set link-down-failover [enable|disable]
set local-as {user}
set local-as-no-prepend [enable|disable]
set local-as-replace-as [enable|disable]
set maximum-prefix {integer}
set maximum-prefix-evpn {integer}
set maximum-prefix-threshold {integer}
set maximum-prefix-threshold-evpn {integer}
set maximum-prefix-threshold-vpnv4 {integer}
set maximum-prefix-threshold-vpnv6 {integer}
set maximum-prefix-threshold6 {integer}
set maximum-prefix-vpnv4 {integer}
set maximum-prefix-vpnv6 {integer}
set maximum-prefix-warning-only [enable|disable]
set maximum-prefix-warning-only-evpn [enable|disable]
set maximum-prefix-warning-only-vpnv4 [enable|disable]
set maximum-prefix-warning-only-vpnv6 [enable|disable]
set maximum-prefix-warning-only6 [enable|disable]
set maximum-prefix6 {integer}
set name {var-string}
set next-hop-self [enable|disable]
set next-hop-self-rr [enable|disable]
set next-hop-self-rr-vpnv4 [enable|disable]
set next-hop-self-rr-vpnv6 [enable|disable]
set next-hop-self-rr6 [enable|disable]
set next-hop-self-vpnv4 [enable|disable]
set next-hop-self-vpnv6 [enable|disable]
set next-hop-self6 [enable|disable]
set override-capability [enable|disable]
set passive [enable|disable]
set password {password}
set prefix-list-in {string}
set prefix-list-in-vpnv4 {string}
set prefix-list-in-vpnv6 {string}
set prefix-list-in6 {string}
set prefix-list-out {string}
set prefix-list-out-vpnv4 {string}
set prefix-list-out-vpnv6 {string}
set prefix-list-out6 {string}
set remote-as {user}
set remove-private-as [enable|disable]
FortiOS 8.0.0 CLI Reference
1125
Fortinet Inc.

<!-- 来源页 1126 -->
set remove-private-as-evpn [enable|disable]
set remove-private-as-vpnv4 [enable|disable]
set remove-private-as-vpnv6 [enable|disable]
set remove-private-as6 [enable|disable]
set restart-time {integer}
set retain-stale-time {integer}
set route-map-in {string}
set route-map-in-evpn {string}
set route-map-in-vpnv4 {string}
set route-map-in-vpnv6 {string}
set route-map-in6 {string}
set route-map-out {string}
set route-map-out-evpn {string}
set route-map-out-preferable {string}
set route-map-out-vpnv4 {string}
set route-map-out-vpnv4-preferable {string}
set route-map-out-vpnv6 {string}
set route-map-out-vpnv6-preferable {string}
set route-map-out6 {string}
set route-map-out6-preferable {string}
set route-reflector-client [enable|disable]
set route-reflector-client-evpn [enable|disable]
set route-reflector-client-vpnv4 [enable|disable]
set route-reflector-client-vpnv6 [enable|disable]
set route-reflector-client6 [enable|disable]
set route-server-client [enable|disable]
set route-server-client-evpn [enable|disable]
set route-server-client-vpnv4 [enable|disable]
set route-server-client-vpnv6 [enable|disable]
set route-server-client6 [enable|disable]
set rr-attr-allow-change [enable|disable]
set rr-attr-allow-change-evpn [enable|disable]
set rr-attr-allow-change-vpnv4 [enable|disable]
set rr-attr-allow-change-vpnv6 [enable|disable]
set rr-attr-allow-change6 [enable|disable]
set send-community [standard|extended|...]
set send-community-evpn [standard|extended|...]
set send-community-vpnv4 [standard|extended|...]
set send-community-vpnv6 [standard|extended|...]
set send-community6 [standard|extended|...]
set shutdown [disable|enable|...]
set soft-reconfiguration [enable|disable]
set soft-reconfiguration-evpn [enable|disable]
set soft-reconfiguration-vpnv4 [enable|disable]
set soft-reconfiguration-vpnv6 [enable|disable]
set soft-reconfiguration6 [enable|disable]
set stale-route [enable|disable]
set strict-capability-match [enable|disable]
set unsuppress-map {string}
set unsuppress-map6 {string}
set update-source {string}
set use-sdwan [enable|disable]
FortiOS 8.0.0 CLI Reference
1126
Fortinet Inc.

<!-- 来源页 1127 -->
set weight {integer}
next
end
config neighbor-group
Description: BGP neighbor group table.
edit <name>
set activate [enable|disable]
set activate-evpn [enable|disable]
set activate-vpnv4 [enable|disable]
set activate-vpnv6 [enable|disable]
set activate6 [enable|disable]
set additional-path [send|receive|...]
set additional-path-vpnv4 [send|receive|...]
set additional-path-vpnv6 [send|receive|...]
set additional-path6 [send|receive|...]
set adv-additional-path {integer}
set adv-additional-path-vpnv4 {integer}
set adv-additional-path-vpnv6 {integer}
set adv-additional-path6 {integer}
set adv-evpn-route {option1}, {option2}, ...
set advertisement-interval {integer}
set allowas-in {integer}
set allowas-in-enable [enable|disable]
set allowas-in-enable-evpn [enable|disable]
set allowas-in-enable-vpnv4 [enable|disable]
set allowas-in-enable-vpnv6 [enable|disable]
set allowas-in-enable6 [enable|disable]
set allowas-in-evpn {integer}
set allowas-in-vpnv4 {integer}
set allowas-in-vpnv6 {integer}
set allowas-in6 {integer}
set as-override [enable|disable]
set as-override6 [enable|disable]
set attribute-unchanged {option1}, {option2}, ...
set attribute-unchanged-vpnv4 {option1}, {option2}, ...
set attribute-unchanged-vpnv6 {option1}, {option2}, ...
set attribute-unchanged6 {option1}, {option2}, ...
set auth-options {string}
set bfd [enable|disable]
set capability-default-originate [enable|disable]
set capability-default-originate6 [enable|disable]
set capability-dynamic [enable|disable]
set capability-graceful-restart [enable|disable]
set capability-graceful-restart-evpn [enable|disable]
set capability-graceful-restart-vpnv4 [enable|disable]
set capability-graceful-restart-vpnv6 [enable|disable]
set capability-graceful-restart6 [enable|disable]
set capability-orf [none|receive|...]
set capability-orf6 [none|receive|...]
set capability-route-refresh [enable|disable]
set connect-timer {integer}
set default-originate-routemap {string}
FortiOS 8.0.0 CLI Reference
1127
Fortinet Inc.

<!-- 来源页 1128 -->
set default-originate-routemap6 {string}
set description {string}
set display-options {integer}
set distribute-list-in {string}
set distribute-list-in-vpnv4 {string}
set distribute-list-in-vpnv6 {string}
set distribute-list-in6 {string}
set distribute-list-out {string}
set distribute-list-out-vpnv4 {string}
set distribute-list-out-vpnv6 {string}
set distribute-list-out6 {string}
set dont-capability-negotiate [enable|disable]
set ebgp-enforce-multihop [enable|disable]
set ebgp-multihop-ttl {integer}
set enforce-preferred-source [enable|disable]
set filter-list-in {string}
set filter-list-in-vpnv4 {string}
set filter-list-in-vpnv6 {string}
set filter-list-in6 {string}
set filter-list-out {string}
set filter-list-out-vpnv4 {string}
set filter-list-out-vpnv6 {string}
set filter-list-out6 {string}
set graceful-shutdown-community {string}
set graceful-shutdown-delay {integer}
set graceful-shutdown-local-preference {integer}
set holdtime-timer {integer}
set interface {string}
set keep-alive-timer {integer}
set link-down-failover [enable|disable]
set local-as {user}
set local-as-no-prepend [enable|disable]
set local-as-replace-as [enable|disable]
set maximum-prefix {integer}
set maximum-prefix-evpn {integer}
set maximum-prefix-threshold {integer}
set maximum-prefix-threshold-evpn {integer}
set maximum-prefix-threshold-vpnv4 {integer}
set maximum-prefix-threshold-vpnv6 {integer}
set maximum-prefix-threshold6 {integer}
set maximum-prefix-vpnv4 {integer}
set maximum-prefix-vpnv6 {integer}
set maximum-prefix-warning-only [enable|disable]
set maximum-prefix-warning-only-evpn [enable|disable]
set maximum-prefix-warning-only-vpnv4 [enable|disable]
set maximum-prefix-warning-only-vpnv6 [enable|disable]
set maximum-prefix-warning-only6 [enable|disable]
set maximum-prefix6 {integer}
set next-hop-self [enable|disable]
set next-hop-self-rr [enable|disable]
set next-hop-self-rr-vpnv4 [enable|disable]
set next-hop-self-rr-vpnv6 [enable|disable]
FortiOS 8.0.0 CLI Reference
1128
Fortinet Inc.

<!-- 来源页 1129 -->
set next-hop-self-rr6 [enable|disable]
set next-hop-self-vpnv4 [enable|disable]
set next-hop-self-vpnv6 [enable|disable]
set next-hop-self6 [enable|disable]
set override-capability [enable|disable]
set passive [enable|disable]
set password {password}
set prefix-list-in {string}
set prefix-list-in-vpnv4 {string}
set prefix-list-in-vpnv6 {string}
set prefix-list-in6 {string}
set prefix-list-out {string}
set prefix-list-out-vpnv4 {string}
set prefix-list-out-vpnv6 {string}
set prefix-list-out6 {string}
set remote-as {user}
set remote-as-filter {string}
set remove-private-as [enable|disable]
set remove-private-as-evpn [enable|disable]
set remove-private-as-vpnv4 [enable|disable]
set remove-private-as-vpnv6 [enable|disable]
set remove-private-as6 [enable|disable]
set restart-time {integer}
set retain-stale-time {integer}
set route-map-in {string}
set route-map-in-evpn {string}
set route-map-in-vpnv4 {string}
set route-map-in-vpnv6 {string}
set route-map-in6 {string}
set route-map-out {string}
set route-map-out-evpn {string}
set route-map-out-preferable {string}
set route-map-out-vpnv4 {string}
set route-map-out-vpnv4-preferable {string}
set route-map-out-vpnv6 {string}
set route-map-out-vpnv6-preferable {string}
set route-map-out6 {string}
set route-map-out6-preferable {string}
set route-reflector-client [enable|disable]
set route-reflector-client-evpn [enable|disable]
set route-reflector-client-vpnv4 [enable|disable]
set route-reflector-client-vpnv6 [enable|disable]
set route-reflector-client6 [enable|disable]
set route-server-client [enable|disable]
set route-server-client-evpn [enable|disable]
set route-server-client-vpnv4 [enable|disable]
set route-server-client-vpnv6 [enable|disable]
set route-server-client6 [enable|disable]
set rr-attr-allow-change [enable|disable]
set rr-attr-allow-change-evpn [enable|disable]
set rr-attr-allow-change-vpnv4 [enable|disable]
set rr-attr-allow-change-vpnv6 [enable|disable]
FortiOS 8.0.0 CLI Reference
1129
Fortinet Inc.

<!-- 来源页 1130 -->
set rr-attr-allow-change6 [enable|disable]
set send-community [standard|extended|...]
set send-community-evpn [standard|extended|...]
set send-community-vpnv4 [standard|extended|...]
set send-community-vpnv6 [standard|extended|...]
set send-community6 [standard|extended|...]
set shutdown [disable|enable|...]
set soft-reconfiguration [enable|disable]
set soft-reconfiguration-evpn [enable|disable]
set soft-reconfiguration-vpnv4 [enable|disable]
set soft-reconfiguration-vpnv6 [enable|disable]
set soft-reconfiguration6 [enable|disable]
set stale-route [enable|disable]
set strict-capability-match [enable|disable]
set unsuppress-map {string}
set unsuppress-map6 {string}
set update-source {string}
set use-sdwan [enable|disable]
set weight {integer}
next
end
config neighbor-range
Description: BGP neighbor range table.
edit <id>
set max-neighbor-num {integer}
set neighbor-group {string}
set prefix {ipv4-classnet}
next
end
config neighbor-range6
Description: BGP IPv6 neighbor range table.
edit <id>
set max-neighbor-num {integer}
set neighbor-group {string}
set prefix6 {ipv6-network}
next
end
config network
Description: BGP network table.
edit <id>
set backdoor [enable|disable]
set internet-service-name {string}
set network-import-check [global|enable|...]
set prefix {ipv4-classnet}
set prefix-name {string}
set route-map {string}
next
end
set network-import-check [enable|disable]
config network6
Description: BGP IPv6 network table.
edit <id>
FortiOS 8.0.0 CLI Reference
1130
Fortinet Inc.

<!-- 来源页 1131 -->
set backdoor [enable|disable]
set network-import-check [global|enable|...]
set prefix6 {ipv6-network}
set route-map {string}
next
end
set recursive-inherit-priority [enable|disable]
set recursive-next-hop [enable|disable]
config redistribute
Description: BGP IPv4 redistribute table. Read-only.
edit <name>
set route-map {string}
set route-map-evpn {string}
set status [enable|disable]
set status-evpn [enable|disable]
next
end
config redistribute6
Description: BGP IPv6 redistribute table. Read-only.
edit <name>
set route-map {string}
set status [enable|disable]
next
end
set router-id {ipv4-address-any}
set scan-time {integer}
set synchronization [enable|disable]
set tag-resolve-mode [disable|preferred|...]
config vrf
Description: BGP VRF leaking table.
edit <vrf>
set export-rt <route-target1>, <route-target2>, ...
set import-route-map {string}
set import-rt <route-target1>, <route-target2>, ...
config leak-target
Description: Target VRF table.
edit <vrf>
set interface {string}
set route-map {string}
next
end
set rd {string}
set role [standalone|ce|...]
next
end
config vrf6
Description: BGP IPv6 VRF leaking table.
edit <vrf>
set export-rt <route-target1>, <route-target2>, ...
set import-route-map {string}
set import-rt <route-target1>, <route-target2>, ...
config leak-target
FortiOS 8.0.0 CLI Reference
1131
Fortinet Inc.

<!-- 来源页 1132 -->
Description: Target VRF table.
edit <vrf>
set interface {string}
set route-map {string}
next
end
set rd {string}
set role [standalone|ce|...]
next
end
end
config router bgp
Parameter
Description
Type
Size
Default
additional-path
Enable/disable selection of BGP IPv4
additional paths.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
additional-path-select
Number of additional paths to be selected
for each IPv4 NLRI.
integer
Minimum value:
2 Maximum
value: 255
2
additional-path-select-vpnv4
Number of additional paths to be selected
for each VPNv4 NLRI.
integer
Minimum value:
2 Maximum
value: 255
2
additional-path-select-vpnv6
Number of additional paths to be selected
for each VPNv6 NLRI.
integer
Minimum value:
2 Maximum
value: 255
2
additional-path-select6
Number of additional paths to be selected
for each IPv6 NLRI.
integer
Minimum value:
2 Maximum
value: 255
2
additional-path-vpnv4
Enable/disable selection of BGP VPNv4
additional paths.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
additional-path-vpnv6
Enable/disable selection of BGP VPNv6
additional paths.
option
-disable
FortiOS 8.0.0 CLI Reference
1132
Fortinet Inc.

<!-- 来源页 1133 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable setting.
disable
Disable setting.
additional-path6
Enable/disable selection of BGP IPv6
additional paths.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
always-compare-med
Enable/disable always compare MED.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
as
Router AS number, asplain/asdot/asdot+
format, 0 to disable BGP.
user
Not Specified
bestpath-as-path-ignore
Enable/disable ignore AS path.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
bestpath-cmp-confed-aspath
Enable/disable compare federation AS path
length.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
bestpath-cmp-routerid
Enable/disable compare router ID for
identical EBGP paths.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
1133
Fortinet Inc.

<!-- 来源页 1134 -->
Parameter
Description
Type
Size
Default
bestpath-med-confed
Enable/disable compare MED among
confederation paths.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
bestpath-med-missing-as-worst
Enable/disable treat missing MED as least
preferred.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
client-to-client-reflection
Enable/disable client-to-client route
reflection.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
cluster-id
Route reflector cluster ID.
ipv4-address-any
Not Specified
0.0.0.0
confederation-identifier
Confederation identifier.
integer
Minimum value:
1 Maximum
value:
4294967295
0
confederation-peers <peer>
Confederation peers.
Peer ID.
string
Maximum
length: 79
cross-family-conditional-adv
Enable/disable cross address family
conditional advertisement.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
dampening
Enable/disable route-flap dampening.
option
-disable
FortiOS 8.0.0 CLI Reference
1134
Fortinet Inc.

<!-- 来源页 1135 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable setting.
disable
Disable setting.
dampening-max-suppress-time
Maximum minutes a route can be
suppressed.
integer
Minimum value:
1 Maximum
value: 255
60
dampening-reachability-half-life
Reachability half-life time for penalty (min).
integer
Minimum value:
1 Maximum
value: 45
15
dampening-reuse
Threshold to reuse routes.
integer
Minimum value:
1 Maximum
value: 20000
750
dampening-route-map
Criteria for dampening.
string
Maximum
length: 35
dampening-suppress
Threshold to suppress routes.
integer
Minimum value:
1 Maximum
value: 20000
2000
dampening-unreachability-half-life
Unreachability half-life time for penalty
(min).
integer
Minimum value:
1 Maximum
value: 45
15
dampening6 *
Enable/disable IPv6 route-flap dampening.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
dampening6-max-suppress-time *
Maximum minutes an IPv6 route can be
suppressed.
integer
Minimum value:
1 Maximum
value: 255
60
dampening6-reachability-half-life *
IPv6 reachability half-life time for penalty
(min).
integer
Minimum value:
1 Maximum
value: 45
15
dampening6-reuse *
Threshold to reuse IPv6 routes.
integer
Minimum value:
1 Maximum
value: 20000
750
dampening6-route-map *
Criteria for IPv6 dampening.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
1135
Fortinet Inc.

<!-- 来源页 1136 -->
Parameter
Description
Type
Size
Default
dampening6-suppress *
Threshold to suppress IPv6 routes.
integer
Minimum value:
1 Maximum
value: 20000
2000
dampening6-unreachability-half-life *
IPv6 unreachability half-life time for penalty
(min).
integer
Minimum value:
1 Maximum
value: 45
15
default-local-preference
Default local preference.
integer
Minimum value:
0 Maximum
value:
4294967295
100
deterministic-med
Enable/disable enforce deterministic
comparison of MED.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
display-options *
Display options for Router AS number Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
distance-external
Distance for routes external to the AS.
integer
Minimum value:
1 Maximum
value: 255
20
distance-internal
Distance for routes internal to the AS.
integer
Minimum value:
1 Maximum
value: 255
200
distance-local
Distance for routes local to the AS.
integer
Minimum value:
1 Maximum
value: 255
200
ebgp-multipath
Enable/disable EBGP multi-path.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
enforce-first-as
Enable/disable enforce first AS for EBGP
routes.
option
-enable
FortiOS 8.0.0 CLI Reference
1136
Fortinet Inc.

<!-- 来源页 1137 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable setting.
disable
Disable setting.
fast-external-failover
Enable/disable reset peer BGP session if
link goes down.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
graceful-end-on-timer
Enable/disable to exit graceful restart on
timer only.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
graceful-restart
Enable/disable BGP graceful restart
capabilities.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
graceful-restart-time
Time needed for neighbors to restart (sec).
integer
Minimum value:
1 Maximum
value: 3600
120
graceful-stalepath-time
Time to hold stale paths of restarting
neighbor (sec).
integer
Minimum value:
1 Maximum
value: 3600
360
graceful-update-delay
Route advertisement/selection delay after
restart (sec).
integer
Minimum value:
1 Maximum
value: 3600
120
holdtime-timer
Number of seconds to mark peer as dead.
integer
Minimum value:
3 Maximum
value: 65535
180
ibgp-multipath
Enable/disable IBGP multi-path.
option
-disable
FortiOS 8.0.0 CLI Reference
1137
Fortinet Inc.

<!-- 来源页 1138 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable setting.
disable
Disable setting.
ignore-optional-capability
Do not send unknown optional capability
notification message.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
keepalive-timer
Frequency to send keep alive requests.
integer
Minimum value:
0 Maximum
value: 65535
60
log-neighbour-changes
Log BGP neighbor changes.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
multipath-recursive-distance
Enable/disable use of recursive distance to
select multipath.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
network-import-check
Enable/disable ensure BGP network route
exists in IGP.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
recursive-inherit-priority
Enable/disable priority inheritance for
recursive resolution.
option
-disable
FortiOS 8.0.0 CLI Reference
1138
Fortinet Inc.

<!-- 来源页 1139 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable setting.
disable
Disable setting.
recursive-next-hop
Enable/disable recursive resolution of next-hop using BGP route.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
router-id
Router ID.
ipv4-address-any
Not Specified
scan-time
Background scanner interval (sec), 0 to
disable it.
integer
Minimum value:
5 Maximum
value: 60
60
synchronization
Enable/disable only advertise routes from
iBGP if routes present in an IGP.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
tag-resolve-mode
Configure tag-match mode. Resolves BGP
routes with other routes containing the
same tag.
option
-disable
Option
Description
disable
Disable tag-match mode.
preferred
Use tag-match if a BGP route resolution with another route
containing the same tag is successful.
merge
Merge tag-match with best-match if they are using different routes.
The result will exclude the next hops of tag-match whose interfaces
or child interfaces have appeared in best-match.
merge-all
Merge tag-match with best-match if they are using different routes.
The result will exclude the next hops of tag-match whose interfaces
have appeared in best-match.
* This parameter may not exist in some models.
FortiOS 8.0.0 CLI Reference
1139
Fortinet Inc.

<!-- 来源页 1140 -->
config admin-distance
Parameter
Description
Type
Size
Default
distance
Administrative distance to apply (1 - 255).
integer
Minimum value:
1 Maximum
value: 255
0
id
ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
neighbour-prefix
Neighbor address prefix.
ipv4-classnet
Not Specified
0.0.0.0
0.0.0.0
route-list
Access list of routes to apply new distance to.
string
Maximum
length: 35
config aggregate-address
Parameter
Description
Type
Size
Default
as-set
Enable/disable generate AS set path
information.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
id
ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
prefix
Aggregate prefix.
ipv4-classnet-any
Not Specified
0.0.0.0
0.0.0.0
summary-only
Enable/disable filter more specific routes from
updates.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
1140
Fortinet Inc.

<!-- 来源页 1141 -->
config aggregate-address6
Parameter
Description
Type
Size
Default
as-set
Enable/disable generate AS set path information.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
id
ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
prefix6
Aggregate IPv6 prefix.
ipv6-prefix
Not Specified
::/0
summary-only
Enable/disable filter more specific routes from
updates.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
config neighbor
Parameter
Description
Type
Size
Default
activate
Enable/disable address family IPv4
for this neighbor.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
activate-evpn
Enable/disable address family L2VPN
EVPN for this neighbor.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
activate-vpnv4
Enable/disable address family VPNv4
for this neighbor.
option
-enable
FortiOS 8.0.0 CLI Reference
1141
Fortinet Inc.

<!-- 来源页 1142 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable setting.
disable
Disable setting.
activate-vpnv6
Enable/disable address family VPNv6
for this neighbor.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
activate6
Enable/disable address family IPv6
for this neighbor.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
additional-path
Enable/disable IPv4 additional-path
capability.
option
-disable
Option
Description
send
Enable sending additional paths.
receive
Enable receiving additional paths.
both
Enable sending and receiving additional paths.
disable
Disable additional paths.
additional-path-vpnv4
Enable/disable VPNv4 additional-path capability.
option
-disable
Option
Description
send
Enable sending additional paths.
receive
Enable receiving additional paths.
both
Enable sending and receiving additional paths.
disable
Disable additional paths.
additional-path-vpnv6
Enable/disable VPNv6 additional-path capability.
option
-disable
FortiOS 8.0.0 CLI Reference
1142
Fortinet Inc.

<!-- 来源页 1143 -->
Parameter
Description
Type
Size
Default
Option
Description
send
Enable sending additional paths.
receive
Enable receiving additional paths.
both
Enable sending and receiving additional paths.
disable
Disable additional paths.
additional-path6
Enable/disable IPv6 additional-path
capability.
option
-disable
Option
Description
send
Enable sending additional paths.
receive
Enable receiving additional paths.
both
Enable sending and receiving additional paths.
disable
Disable additional paths.
adv-additional-path
Number of IPv4 additional paths that
can be advertised to this neighbor.
integer
Minimum value:
2 Maximum
value: 255
2
adv-additional-path-vpnv4
Number of VPNv4 additional paths
that can be advertised to this
neighbor.
integer
Minimum value:
2 Maximum
value: 255
2
adv-additional-path-vpnv6
Number of VPNv6 additional paths
that can be advertised to this
neighbor.
integer
Minimum value:
2 Maximum
value: 255
2
adv-additional-path6
Number of IPv6 additional paths that
can be advertised to this neighbor.
integer
Minimum value:
2 Maximum
value: 255
2
adv-evpn-route *
Types of EVPN routes that can be
advertised to this neighbor as IPv4
routes.
option
-Option
Description
type2
Type 2 EVPN routes.
type5
Type 5 EVPN routes.
local
Local EVPN routes.
FortiOS 8.0.0 CLI Reference
1143
Fortinet Inc.

<!-- 来源页 1144 -->
Parameter
Description
Type
Size
Default
advertisement-interval
Minimum interval (sec) between
sending updates.
integer
Minimum value:
0 Maximum
value: 600
30
allowas-in
IPv4 The maximum number of
occurrence of my AS number
allowed.
integer
Minimum value:
1 Maximum
value: 10
3
allowas-in-enable
Enable/disable IPv4 to allow my AS in
AS path.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
allowas-in-enable-evpn
Enable/disable to allow my AS in AS
path for L2VPN EVPN route.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
allowas-in-enable-vpnv4
Enable/disable to allow my AS in AS
path for VPNv4 route.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
allowas-in-enable-vpnv6
Enable/disable to allow my AS in AS
path for VPNv6 route.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
allowas-in-enable6
Enable/disable IPv6 to allow my AS in
AS path.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
1144
Fortinet Inc.

<!-- 来源页 1145 -->
Parameter
Description
Type
Size
Default
allowas-in-evpn
The maximum number of occurrence
of my AS number allowed for L2VPN
EVPN route.
integer
Minimum value:
1 Maximum
value: 10
3
allowas-in-vpnv4
The maximum number of occurrence
of my AS number allowed for VPNv4
route.
integer
Minimum value:
1 Maximum
value: 10
3
allowas-in-vpnv6
The maximum number of occurrence
of my AS number allowed for VPNv6
route.
integer
Minimum value:
1 Maximum
value: 10
3
allowas-in6
IPv6 The maximum number of
occurrence of my AS number
allowed.
integer
Minimum value:
1 Maximum
value: 10
3
as-override
Enable/disable replace peer AS with
own AS for IPv4.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
as-override6
Enable/disable replace peer AS with
own AS for IPv6.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
attribute-unchanged
IPv4 List of attributes that should be
unchanged.
option
-Option
Description
as-path
AS path.
med
MED.
next-hop
Next hop.
attribute-unchanged-vpnv4
List of attributes that should be
unchanged for VPNv4 route.
option
-Option
Description
as-path
AS path.
FortiOS 8.0.0 CLI Reference
1145
Fortinet Inc.

<!-- 来源页 1146 -->
Parameter
Description
Type
Size
Default
Option
Description
med
MED.
next-hop
Next hop.
attribute-unchanged-vpnv6
List of attributes that should not be
changed for VPNv6 route.
option
-Option
Description
as-path
AS path.
med
MED.
next-hop
Next hop.
attribute-unchanged6
IPv6 List of attributes that should be
unchanged.
option
-Option
Description
as-path
AS path.
med
MED.
next-hop
Next hop.
auth-options
Key-chain name for TCP
authentication options.
string
Maximum
length: 35
bfd
Enable/disable BFD for this neighbor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
capability-default-originate
Enable/disable advertise default IPv4
route to this neighbor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
capability-default-originate6
Enable/disable advertise default IPv6
route to this neighbor.
option
-disable
FortiOS 8.0.0 CLI Reference
1146
Fortinet Inc.

<!-- 来源页 1147 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable setting.
disable
Disable setting.
capability-dynamic
Enable/disable advertise dynamic
capability to this neighbor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
capability-graceful-restart
Enable/disable advertise IPv4
graceful restart capability to this
neighbor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
capability-graceful-restart-evpn
Enable/disable advertisement of
L2VPN EVPN graceful restart
capability to this neighbor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
capability-graceful-restart-vpnv4
Enable/disable advertise VPNv4
graceful restart capability to this
neighbor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
capability-graceful-restart-vpnv6
Enable/disable advertisement of
VPNv6 graceful restart capability to
this neighbor.
option
-disable
FortiOS 8.0.0 CLI Reference
1147
Fortinet Inc.

<!-- 来源页 1148 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable setting.
disable
Disable setting.
capability-graceful-restart6
Enable/disable advertise IPv6
graceful restart capability to this
neighbor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
capability-orf
Accept/Send IPv4 ORF lists to/from
this neighbor.
option
-none
Option
Description
none
None.
receive
Receive ORF lists.
send
Send ORF list.
both
Send and receive ORF lists.
capability-orf6
Accept/Send IPv6 ORF lists to/from
this neighbor.
option
-none
Option
Description
none
None.
receive
Receive ORF lists.
send
Send ORF list.
both
Send and receive ORF lists.
capability-route-refresh
Enable/disable advertise route
refresh capability to this neighbor.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
1148
Fortinet Inc.

<!-- 来源页 1149 -->
Parameter
Description
Type
Size
Default
connect-timer
Interval (sec) for connect timer.
integer
Minimum value:
1 Maximum
value: 65535
4294967295
default-originate-routemap
Route map to specify criteria to
originate IPv4 default.
string
Maximum
length: 35
default-originate-routemap6
Route map to specify criteria to
originate IPv6 default.
string
Maximum
length: 35
description
Description.
string
Maximum
length: 63
display-options *
Display options for remote AS
number Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
distribute-list-in
Filter for IPv4 updates from this
neighbor.
string
Maximum
length: 35
distribute-list-in-vpnv4
Filter for VPNv4 updates from this
neighbor.
string
Maximum
length: 35
distribute-list-in-vpnv6
Filter for VPNv6 updates from this
neighbor.
string
Maximum
length: 35
distribute-list-in6
Filter for IPv6 updates from this
neighbor.
string
Maximum
length: 35
distribute-list-out
Filter for IPv4 updates to this
neighbor.
string
Maximum
length: 35
distribute-list-out-vpnv4
Filter for VPNv4 updates to this
neighbor.
string
Maximum
length: 35
distribute-list-out-vpnv6
Filter for VPNv6 updates to this
neighbor.
string
Maximum
length: 35
distribute-list-out6
Filter for IPv6 updates to this
neighbor.
string
Maximum
length: 35
dont-capability-negotiate
Do not negotiate capabilities with this
neighbor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
ebgp-enforce-multihop
Enable/disable allow multi-hop EBGP
neighbors.
option
-disable
FortiOS 8.0.0 CLI Reference
1149
Fortinet Inc.

<!-- 来源页 1150 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable setting.
disable
Disable setting.
ebgp-multihop-ttl
EBGP multihop TTL for this peer.
integer
Minimum value:
1 Maximum
value: 255
255
enforce-preferred-source *
Enable/disable enforce usage of the
update-source as preferred source
for IPv4 routes learned from this
neighbor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
filter-list-in
BGP filter for IPv4 inbound routes.
string
Maximum
length: 35
filter-list-in-vpnv4
BGP filter for VPNv4 inbound routes.
string
Maximum
length: 35
filter-list-in-vpnv6
BGP filter for VPNv6 inbound routes.
string
Maximum
length: 35
filter-list-in6
BGP filter for IPv6 inbound routes.
string
Maximum
length: 35
filter-list-out
BGP filter for IPv4 outbound routes.
string
Maximum
length: 35
filter-list-out-vpnv4
BGP filter for VPNv4 outbound
routes.
string
Maximum
length: 35
filter-list-out-vpnv6
BGP filter for VPNv6 outbound
routes.
string
Maximum
length: 35
filter-list-out6
BGP filter for IPv6 outbound routes.
string
Maximum
length: 35
graceful-shutdown-community *
Graceful shutdown community.
string
Maximum
length: 35
graceful-shutdown-delay *
Delay in seconds before graceful
shutdown ends.
integer
Minimum value:
60 Maximum
value: 36000
3600
FortiOS 8.0.0 CLI Reference
1150
Fortinet Inc.

<!-- 来源页 1151 -->
Parameter
Description
Type
Size
Default
graceful-shutdown-local-preference *
Graceful shutdown local preference.
integer
Minimum value:
0 Maximum
value:
4294967295
0
holdtime-timer
Interval (sec) before peer considered
dead.
integer
Minimum value:
0 Maximum
value:
4294967295
**
4294967295
interface
Specify outgoing interface for peer
connection. For IPv6 peer, the
interface should have link-local
address.
string
Maximum
length: 15
ip
IP/IPv6 address of neighbor.
string
Maximum
length: 45
keep-alive-timer
Keep alive timer interval (sec).
integer
Minimum value:
0 Maximum
value: 65535
4294967295
link-down-failover
Enable/disable failover upon link
down.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
local-as
Local AS number of neighbor.
user
Not Specified
local-as-no-prepend
Do not prepend local-as to incoming
updates.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
local-as-replace-as
Replace real AS with local-as in
outgoing updates.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
1151
Fortinet Inc.

<!-- 来源页 1152 -->
Parameter
Description
Type
Size
Default
maximum-prefix
Maximum number of IPv4 prefixes to
accept from this peer.
integer
Minimum value:
1 Maximum
value:
4294967295
0
maximum-prefix-evpn
Maximum number of L2VPN EVPN
prefixes to accept from this peer.
integer
Minimum value:
1 Maximum
value:
4294967295
0
maximum-prefix-threshold
Maximum IPv4 prefix threshold value
(1 - 100 percent).
integer
Minimum value:
1 Maximum
value: 100
75
maximum-prefix-threshold-evpn
Maximum L2VPN EVPN prefix
threshold value (1 - 100 percent).
integer
Minimum value:
1 Maximum
value: 100
75
maximum-prefix-threshold-vpnv4
Maximum VPNv4 prefix threshold
value (1 - 100 percent).
integer
Minimum value:
1 Maximum
value: 100
75
maximum-prefix-threshold-vpnv6
Maximum VPNv6 prefix threshold
value (1 - 100 percent).
integer
Minimum value:
1 Maximum
value: 100
75
maximum-prefix-threshold6
Maximum IPv6 prefix threshold value
(1 - 100 percent).
integer
Minimum value:
1 Maximum
value: 100
75
maximum-prefix-vpnv4
Maximum number of VPNv4 prefixes
to accept from this peer.
integer
Minimum value:
1 Maximum
value:
4294967295
0
maximum-prefix-vpnv6
Maximum number of VPNv6 prefixes
to accept from this peer.
integer
Minimum value:
1 Maximum
value:
4294967295
0
maximum-prefix-warning-only
Enable/disable IPv4 Only give
warning message when limit is
exceeded.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
1152
Fortinet Inc.

<!-- 来源页 1153 -->
Parameter
Description
Type
Size
Default
maximum-prefix-warning-only-evpn
Enable/disable only sending warning
message when exceeding limit of
L2VPN EVPN routes.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
maximum-prefix-warning-only-vpnv4
Enable/disable only giving warning
message when limit is exceeded for
VPNv4 routes.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
maximum-prefix-warning-only-vpnv6
Enable/disable warning message
when limit is exceeded for VPNv6
routes.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
maximum-prefix-warning-only6
Enable/disable IPv6 Only give
warning message when limit is
exceeded.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
maximum-prefix6
Maximum number of IPv6 prefixes to
accept from this peer.
integer
Minimum value:
1 Maximum
value:
4294967295
0
name *
Name of this neighbor.
var-string
Maximum
length: 255
next-hop-self
Enable/disable IPv4 next-hop
calculation for this neighbor.
option
-disable
FortiOS 8.0.0 CLI Reference
1153
Fortinet Inc.

<!-- 来源页 1154 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable setting.
disable
Disable setting.
next-hop-self-rr
Enable/disable setting nexthop's
address to interface's IPv4 address
for route-reflector routes.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
next-hop-self-rr-vpnv4 *
Enable/disable setting of the
nexthop's address to interface's
address for route-reflector VPNv4
routes.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
next-hop-self-rr-vpnv6 *
Enable/disable setting of the
nexthop's address to interface's
address for route-reflector VPNv6
routes.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
next-hop-self-rr6
Enable/disable setting nexthop's
address to interface's IPv6 address
for route-reflector routes.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
next-hop-self-vpnv4
Enable/disable setting VPNv4 next-hop to interface's IP address for this
neighbor.
option
-disable
FortiOS 8.0.0 CLI Reference
1154
Fortinet Inc.

<!-- 来源页 1155 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable setting.
disable
Disable setting.
next-hop-self-vpnv6
Enable/disable use of outgoing
interface's IP address as VPNv6 next-hop for this neighbor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
next-hop-self6
Enable/disable IPv6 next-hop
calculation for this neighbor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
override-capability
Enable/disable override result of
capability negotiation.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
passive
Enable/disable initiation of the TCP
session for this neighbor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
password
Password used in MD5
authentication.
password
Not Specified
prefix-list-in
IPv4 Inbound filter for updates from
this neighbor.
string
Maximum
length: 35
prefix-list-in-vpnv4
Inbound filter for VPNv4 updates
from this neighbor.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
1155
Fortinet Inc.

<!-- 来源页 1156 -->
Parameter
Description
Type
Size
Default
prefix-list-in-vpnv6
Inbound filter for VPNv6 updates
from this neighbor.
string
Maximum
length: 35
prefix-list-in6
IPv6 Inbound filter for updates from
this neighbor.
string
Maximum
length: 35
prefix-list-out
IPv4 Outbound filter for updates to
this neighbor.
string
Maximum
length: 35
prefix-list-out-vpnv4
Outbound filter for VPNv4 updates to
this neighbor.
string
Maximum
length: 35
prefix-list-out-vpnv6
Outbound filter for VPNv6 updates to
this neighbor.
string
Maximum
length: 35
prefix-list-out6
IPv6 Outbound filter for updates to
this neighbor.
string
Maximum
length: 35
remote-as
AS number of neighbor.
user
Not Specified
remove-private-as
Enable/disable remove private AS
number from IPv4 outbound updates.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
remove-private-as-evpn
Enable/disable removing private AS
number from L2VPN EVPN outbound
updates.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
remove-private-as-vpnv4
Enable/disable remove private AS
number from VPNv4 outbound
updates.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
remove-private-as-vpnv6
Enable/disable to remove private AS
number from VPNv6 outbound
updates.
option
-disable
FortiOS 8.0.0 CLI Reference
1156
Fortinet Inc.

<!-- 来源页 1157 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable setting.
disable
Disable setting.
remove-private-as6
Enable/disable remove private AS
number from IPv6 outbound updates.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
restart-time
Graceful restart delay time (sec, 0 =
global default).
integer
Minimum value:
0 Maximum
value: 3600
0
retain-stale-time
Time to retain stale routes.
integer
Minimum value:
0 Maximum
value: 65535
0
route-map-in
IPv4 Inbound route map filter.
string
Maximum
length: 35
route-map-in-evpn
L2VPN EVPN inbound route map
filter.
string
Maximum
length: 35
route-map-in-vpnv4
VPNv4 inbound route map filter.
string
Maximum
length: 35
route-map-in-vpnv6
VPNv6 inbound route map filter.
string
Maximum
length: 35
route-map-in6
IPv6 Inbound route map filter.
string
Maximum
length: 35
route-map-out
IPv4 outbound route map filter.
string
Maximum
length: 35
route-map-out-evpn
L2VPN EVPN outbound route map
filter.
string
Maximum
length: 35
route-map-out-preferable
IPv4 outbound route map filter if the
peer is preferred.
string
Maximum
length: 35
route-map-out-vpnv4
VPNv4 outbound route map filter.
string
Maximum
length: 35
route-map-out-vpnv4-preferable
VPNv4 outbound route map filter if
the peer is preferred.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
1157
Fortinet Inc.

<!-- 来源页 1158 -->
Parameter
Description
Type
Size
Default
route-map-out-vpnv6
VPNv6 outbound route map filter.
string
Maximum
length: 35
route-map-out-vpnv6-preferable
VPNv6 outbound route map filter if
the peer is preferred.
string
Maximum
length: 35
route-map-out6
IPv6 Outbound route map filter.
string
Maximum
length: 35
route-map-out6-preferable
IPv6 outbound route map filter if the
peer is preferred.
string
Maximum
length: 35
route-reflector-client
Enable/disable IPv4 AS route
reflector client.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
route-reflector-client-evpn
Enable/disable L2VPN EVPN AS route
reflector client for this neighbor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
route-reflector-client-vpnv4
Enable/disable VPNv4 AS route
reflector client for this neighbor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
route-reflector-client-vpnv6
Enable/disable VPNv6 AS route
reflector client for this neighbor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
route-reflector-client6
Enable/disable IPv6 AS route
reflector client.
option
-disable
FortiOS 8.0.0 CLI Reference
1158
Fortinet Inc.

<!-- 来源页 1159 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable setting.
disable
Disable setting.
route-server-client
Enable/disable IPv4 AS route server
client.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
route-server-client-evpn
Enable/disable L2VPN EVPN AS route
server client for this neighbor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
route-server-client-vpnv4
Enable/disable VPNv4 AS route
server client for this neighbor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
route-server-client-vpnv6
Enable/disable VPNv6 AS route
server client for this neighbor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
route-server-client6
Enable/disable IPv6 AS route server
client.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
1159
Fortinet Inc.

<!-- 来源页 1160 -->
Parameter
Description
Type
Size
Default
rr-attr-allow-change
Enable/disable allowing change of
route attributes when advertising to
IPv4 route reflector clients.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
rr-attr-allow-change-evpn
Enable/disable allowing change of
route attributes when advertising to
L2VPN EVPN route reflector clients.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
rr-attr-allow-change-vpnv4
Enable/disable allowing change of
route attributes when advertising to
VPNv4 route reflector clients.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
rr-attr-allow-change-vpnv6
Enable/disable allowing change of
route attributes when advertising to
VPNv6 route reflector clients.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
rr-attr-allow-change6
Enable/disable allowing change of
route attributes when advertising to
IPv6 route reflector clients.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
send-community
IPv4 Send community attribute to
neighbor.
option
-both
FortiOS 8.0.0 CLI Reference
1160
Fortinet Inc.

<!-- 来源页 1161 -->
Parameter
Description
Type
Size
Default
Option
Description
standard
Standard.
extended
Extended.
both
Both.
disable
Disable
send-community-evpn
Enable/disable sending community
attribute to neighbor for L2VPN EVPN
address family.
option
-both
Option
Description
standard
Standard.
extended
Extended.
both
Both.
disable
Disable
send-community-vpnv4
Enable/disable sending community
attribute to this neighbor for VPNv4
address family.
option
-both
Option
Description
standard
Standard.
extended
Extended.
both
Both.
disable
Disable
send-community-vpnv6
Enable/disable sending community
attribute to this neighbor for VPNv6
address family.
option
-both
Option
Description
standard
Standard.
extended
Extended.
both
Both.
disable
Disable
send-community6
IPv6 Send community attribute to
neighbor.
option
-both
FortiOS 8.0.0 CLI Reference
1161
Fortinet Inc.

<!-- 来源页 1162 -->
Parameter
Description
Type
Size
Default
Option
Description
standard
Standard.
extended
Extended.
both
Both.
disable
Disable
shutdown
Enable/disable shutting down this
neighbor.
option
-disable
Option
Description
disable
Disable shut down of this neighbor.
enable
Enable shut down of this neighbor.
graceful
Shut down this neighbor gracefully.
graceful-soft
Enable GSHUT community for this neighbor.
soft-reconfiguration
Enable/disable allow IPv4 inbound
soft reconfiguration.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
soft-reconfiguration-evpn
Enable/disable L2VPN EVPN inbound
soft reconfiguration.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
soft-reconfiguration-vpnv4
Enable/disable allow VPNv4 inbound
soft reconfiguration.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
1162
Fortinet Inc.

<!-- 来源页 1163 -->
Parameter
Description
Type
Size
Default
soft-reconfiguration-vpnv6
Enable/disable VPNv6 inbound soft
reconfiguration.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
soft-reconfiguration6
Enable/disable allow IPv6 inbound
soft reconfiguration.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
stale-route
Enable/disable stale route after
neighbor down.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
strict-capability-match
Enable/disable strict capability
matching.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
unsuppress-map
IPv4 Route map to selectively
unsuppress suppressed routes.
string
Maximum
length: 35
unsuppress-map6
IPv6 Route map to selectively
unsuppress suppressed routes.
string
Maximum
length: 35
update-source
Interface to use as source IP/IPv6
address of TCP connections.
string
Maximum
length: 15
use-sdwan *
Use SDWAN rules for BGP
connection.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
1163
Fortinet Inc.

<!-- 来源页 1164 -->
Parameter
Description
Type
Size
Default
weight
Neighbor weight.
integer
Minimum value:
0 Maximum
value: 65535
4294967295
* This parameter may not exist in some models.
** Values may differ between models.
config conditional-advertise
Parameter
Description
Type
Size
Default
advertise-routemap
Name of advertising route map.
string
Maximum
length: 35
condition-routemap
<name>
List of conditional route maps.
Route map.
string
Maximum
length: 79
condition-type
Type of condition.
option
-exist
Option
Description
exist
True if condition route map is matched.
non-exist
True if condition route map is not matched.
config conditional-advertise6
Parameter
Description
Type
Size
Default
advertise-routemap
Name of advertising route map.
string
Maximum
length: 35
condition-routemap
<name>
List of conditional route maps.
Route map.
string
Maximum
length: 79
condition-type
Type of condition.
option
-exist
Option
Description
exist
True if condition route map is matched.
non-exist
True if condition route map is not matched.
FortiOS 8.0.0 CLI Reference
1164
Fortinet Inc.

<!-- 来源页 1165 -->
config neighbor-group
Parameter
Description
Type
Size
Default
activate
Enable/disable address family IPv4
for this neighbor.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
activate-evpn
Enable/disable address family L2VPN
EVPN for this neighbor.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
activate-vpnv4
Enable/disable address family VPNv4
for this neighbor.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
activate-vpnv6
Enable/disable address family VPNv6
for this neighbor.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
activate6
Enable/disable address family IPv6
for this neighbor.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
additional-path
Enable/disable IPv4 additional-path
capability.
option
-disable
FortiOS 8.0.0 CLI Reference
1165
Fortinet Inc.

<!-- 来源页 1166 -->
Parameter
Description
Type
Size
Default
Option
Description
send
Enable sending additional paths.
receive
Enable receiving additional paths.
both
Enable sending and receiving additional paths.
disable
Disable additional paths.
additional-path-vpnv4
Enable/disable VPNv4 additional-path capability.
option
-disable
Option
Description
send
Enable sending additional paths.
receive
Enable receiving additional paths.
both
Enable sending and receiving additional paths.
disable
Disable additional paths.
additional-path-vpnv6
Enable/disable VPNv6 additional-path capability.
option
-disable
Option
Description
send
Enable sending additional paths.
receive
Enable receiving additional paths.
both
Enable sending and receiving additional paths.
disable
Disable additional paths.
additional-path6
Enable/disable IPv6 additional-path
capability.
option
-disable
Option
Description
send
Enable sending additional paths.
receive
Enable receiving additional paths.
both
Enable sending and receiving additional paths.
disable
Disable additional paths.
adv-additional-path
Number of IPv4 additional paths that
can be advertised to this neighbor.
integer
Minimum value:
2 Maximum
value: 255
2
FortiOS 8.0.0 CLI Reference
1166
Fortinet Inc.

<!-- 来源页 1167 -->
Parameter
Description
Type
Size
Default
adv-additional-path-vpnv4
Number of VPNv4 additional paths
that can be advertised to this
neighbor.
integer
Minimum value:
2 Maximum
value: 255
2
adv-additional-path-vpnv6
Number of VPNv6 additional paths
that can be advertised to this
neighbor.
integer
Minimum value:
2 Maximum
value: 255
2
adv-additional-path6
Number of IPv6 additional paths that
can be advertised to this neighbor.
integer
Minimum value:
2 Maximum
value: 255
2
adv-evpn-route *
Types of EVPN routes that can be
advertised to this neighbor as IPv4
routes.
option
-Option
Description
type2
Type 2 EVPN routes.
type5
Type 5 EVPN routes.
local
Local EVPN routes.
advertisement-interval
Minimum interval (sec) between
sending updates.
integer
Minimum value:
0 Maximum
value: 600
30
allowas-in
IPv4 The maximum number of
occurrence of my AS number
allowed.
integer
Minimum value:
1 Maximum
value: 10
3
allowas-in-enable
Enable/disable IPv4 to allow my AS in
AS path.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
allowas-in-enable-evpn
Enable/disable to allow my AS in AS
path for L2VPN EVPN route.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
allowas-in-enable-vpnv4
Enable/disable to allow my AS in AS
path for VPNv4 route.
option
-disable
FortiOS 8.0.0 CLI Reference
1167
Fortinet Inc.

<!-- 来源页 1168 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable setting.
disable
Disable setting.
allowas-in-enable-vpnv6
Enable/disable to allow my AS in AS
path for VPNv6 route.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
allowas-in-enable6
Enable/disable IPv6 to allow my AS in
AS path.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
allowas-in-evpn
The maximum number of occurrence
of my AS number allowed for L2VPN
EVPN route.
integer
Minimum value:
1 Maximum
value: 10
3
allowas-in-vpnv4
The maximum number of occurrence
of my AS number allowed for VPNv4
route.
integer
Minimum value:
1 Maximum
value: 10
3
allowas-in-vpnv6
The maximum number of occurrence
of my AS number allowed for VPNv6
route.
integer
Minimum value:
1 Maximum
value: 10
3
allowas-in6
IPv6 The maximum number of
occurrence of my AS number
allowed.
integer
Minimum value:
1 Maximum
value: 10
3
as-override
Enable/disable replace peer AS with
own AS for IPv4.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
as-override6
Enable/disable replace peer AS with
own AS for IPv6.
option
-disable
FortiOS 8.0.0 CLI Reference
1168
Fortinet Inc.

<!-- 来源页 1169 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable setting.
disable
Disable setting.
attribute-unchanged
IPv4 List of attributes that should be
unchanged.
option
-Option
Description
as-path
AS path.
med
MED.
next-hop
Next hop.
attribute-unchanged-vpnv4
List of attributes that should be
unchanged for VPNv4 route.
option
-Option
Description
as-path
AS path.
med
MED.
next-hop
Next hop.
attribute-unchanged-vpnv6
List of attributes that should not be
changed for VPNv6 route.
option
-Option
Description
as-path
AS path.
med
MED.
next-hop
Next hop.
attribute-unchanged6
IPv6 List of attributes that should be
unchanged.
option
-Option
Description
as-path
AS path.
med
MED.
next-hop
Next hop.
auth-options
Key-chain name for TCP
authentication options.
string
Maximum
length: 35
bfd
Enable/disable BFD for this neighbor.
option
-disable
FortiOS 8.0.0 CLI Reference
1169
Fortinet Inc.

<!-- 来源页 1170 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable setting.
disable
Disable setting.
capability-default-originate
Enable/disable advertise default IPv4
route to this neighbor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
capability-default-originate6
Enable/disable advertise default IPv6
route to this neighbor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
capability-dynamic
Enable/disable advertise dynamic
capability to this neighbor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
capability-graceful-restart
Enable/disable advertise IPv4
graceful restart capability to this
neighbor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
capability-graceful-restart-evpn
Enable/disable advertisement of
L2VPN EVPN graceful restart
capability to this neighbor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
1170
Fortinet Inc.

<!-- 来源页 1171 -->
Parameter
Description
Type
Size
Default
capability-graceful-restart-vpnv4
Enable/disable advertise VPNv4
graceful restart capability to this
neighbor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
capability-graceful-restart-vpnv6
Enable/disable advertisement of
VPNv6 graceful restart capability to
this neighbor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
capability-graceful-restart6
Enable/disable advertise IPv6
graceful restart capability to this
neighbor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
capability-orf
Accept/Send IPv4 ORF lists to/from
this neighbor.
option
-none
Option
Description
none
None.
receive
Receive ORF lists.
send
Send ORF list.
both
Send and receive ORF lists.
capability-orf6
Accept/Send IPv6 ORF lists to/from
this neighbor.
option
-none
Option
Description
none
None.
receive
Receive ORF lists.
FortiOS 8.0.0 CLI Reference
1171
Fortinet Inc.

<!-- 来源页 1172 -->
Parameter
Description
Type
Size
Default
Option
Description
send
Send ORF list.
both
Send and receive ORF lists.
capability-route-refresh
Enable/disable advertise route
refresh capability to this neighbor.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
connect-timer
Interval (sec) for connect timer.
integer
Minimum value:
1 Maximum
value: 65535
4294967295
default-originate-routemap
Route map to specify criteria to
originate IPv4 default.
string
Maximum
length: 35
default-originate-routemap6
Route map to specify criteria to
originate IPv6 default.
string
Maximum
length: 35
description
Description.
string
Maximum
length: 63
display-options *
Display options for remote AS
number Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
distribute-list-in
Filter for IPv4 updates from this
neighbor.
string
Maximum
length: 35
distribute-list-in-vpnv4
Filter for VPNv4 updates from this
neighbor.
string
Maximum
length: 35
distribute-list-in-vpnv6
Filter for VPNv6 updates from this
neighbor.
string
Maximum
length: 35
distribute-list-in6
Filter for IPv6 updates from this
neighbor.
string
Maximum
length: 35
distribute-list-out
Filter for IPv4 updates to this
neighbor.
string
Maximum
length: 35
distribute-list-out-vpnv4
Filter for VPNv4 updates to this
neighbor.
string
Maximum
length: 35
distribute-list-out-vpnv6
Filter for VPNv6 updates to this
neighbor.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
1172
Fortinet Inc.

<!-- 来源页 1173 -->
Parameter
Description
Type
Size
Default
distribute-list-out6
Filter for IPv6 updates to this
neighbor.
string
Maximum
length: 35
dont-capability-negotiate
Do not negotiate capabilities with this
neighbor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
ebgp-enforce-multihop
Enable/disable allow multi-hop EBGP
neighbors.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
ebgp-multihop-ttl
EBGP multihop TTL for this peer.
integer
Minimum value:
1 Maximum
value: 255
255
enforce-preferred-source *
Enable/disable enforce usage of the
update-source as preferred source
for IPv4 routes learned from this
neighbor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
filter-list-in
BGP filter for IPv4 inbound routes.
string
Maximum
length: 35
filter-list-in-vpnv4
BGP filter for VPNv4 inbound routes.
string
Maximum
length: 35
filter-list-in-vpnv6
BGP filter for VPNv6 inbound routes.
string
Maximum
length: 35
filter-list-in6
BGP filter for IPv6 inbound routes.
string
Maximum
length: 35
filter-list-out
BGP filter for IPv4 outbound routes.
string
Maximum
length: 35
filter-list-out-vpnv4
BGP filter for VPNv4 outbound
routes.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
1173
Fortinet Inc.

<!-- 来源页 1174 -->
Parameter
Description
Type
Size
Default
filter-list-out-vpnv6
BGP filter for VPNv6 outbound
routes.
string
Maximum
length: 35
filter-list-out6
BGP filter for IPv6 outbound routes.
string
Maximum
length: 35
graceful-shutdown-community *
Graceful shutdown community.
string
Maximum
length: 35
graceful-shutdown-delay *
Delay in seconds before graceful
shutdown ends.
integer
Minimum value:
60 Maximum
value: 36000
3600
graceful-shutdown-local-preference *
Graceful shutdown local preference.
integer
Minimum value:
0 Maximum
value:
4294967295
0
holdtime-timer
Interval (sec) before peer considered
dead.
integer
Minimum value:
0 Maximum
value:
4294967295
**
4294967295
interface
Specify outgoing interface for peer
connection. For IPv6 peer, the
interface should have link-local
address.
string
Maximum
length: 15
keep-alive-timer
Keep alive timer interval (sec).
integer
Minimum value:
0 Maximum
value: 65535
4294967295
link-down-failover
Enable/disable failover upon link
down.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
local-as
Local AS number of neighbor.
user
Not Specified
local-as-no-prepend
Do not prepend local-as to incoming
updates.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
1174
Fortinet Inc.

<!-- 来源页 1175 -->
Parameter
Description
Type
Size
Default
local-as-replace-as
Replace real AS with local-as in
outgoing updates.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
maximum-prefix
Maximum number of IPv4 prefixes to
accept from this peer.
integer
Minimum value:
1 Maximum
value:
4294967295
0
maximum-prefix-evpn
Maximum number of L2VPN EVPN
prefixes to accept from this peer.
integer
Minimum value:
1 Maximum
value:
4294967295
0
maximum-prefix-threshold
Maximum IPv4 prefix threshold value
(1 - 100 percent).
integer
Minimum value:
1 Maximum
value: 100
75
maximum-prefix-threshold-evpn
Maximum L2VPN EVPN prefix
threshold value (1 - 100 percent).
integer
Minimum value:
1 Maximum
value: 100
75
maximum-prefix-threshold-vpnv4
Maximum VPNv4 prefix threshold
value (1 - 100 percent).
integer
Minimum value:
1 Maximum
value: 100
75
maximum-prefix-threshold-vpnv6
Maximum VPNv6 prefix threshold
value (1 - 100 percent).
integer
Minimum value:
1 Maximum
value: 100
75
maximum-prefix-threshold6
Maximum IPv6 prefix threshold value
(1 - 100 percent).
integer
Minimum value:
1 Maximum
value: 100
75
maximum-prefix-vpnv4
Maximum number of VPNv4 prefixes
to accept from this peer.
integer
Minimum value:
1 Maximum
value:
4294967295
0
maximum-prefix-vpnv6
Maximum number of VPNv6 prefixes
to accept from this peer.
integer
Minimum value:
1 Maximum
value:
4294967295
0
maximum-prefix-warning-only
Enable/disable IPv4 Only give
warning message when limit is
exceeded.
option
-disable
FortiOS 8.0.0 CLI Reference
1175
Fortinet Inc.

<!-- 来源页 1176 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable setting.
disable
Disable setting.
maximum-prefix-warning-only-evpn
Enable/disable only sending warning
message when exceeding limit of
L2VPN EVPN routes.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
maximum-prefix-warning-only-vpnv4
Enable/disable only giving warning
message when limit is exceeded for
VPNv4 routes.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
maximum-prefix-warning-only-vpnv6
Enable/disable warning message
when limit is exceeded for VPNv6
routes.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
maximum-prefix-warning-only6
Enable/disable IPv6 Only give
warning message when limit is
exceeded.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
maximum-prefix6
Maximum number of IPv6 prefixes to
accept from this peer.
integer
Minimum value:
1 Maximum
value:
4294967295
0
FortiOS 8.0.0 CLI Reference
1176
Fortinet Inc.

<!-- 来源页 1177 -->
Parameter
Description
Type
Size
Default
name
Neighbor group name.
string
Maximum
length: 45
next-hop-self
Enable/disable IPv4 next-hop
calculation for this neighbor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
next-hop-self-rr
Enable/disable setting nexthop's
address to interface's IPv4 address
for route-reflector routes.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
next-hop-self-rr-vpnv4 *
Enable/disable setting of the
nexthop's address to interface's
address for route-reflector VPNv4
routes.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
next-hop-self-rr-vpnv6 *
Enable/disable setting of the
nexthop's address to interface's
address for route-reflector VPNv6
routes.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
next-hop-self-rr6
Enable/disable setting nexthop's
address to interface's IPv6 address
for route-reflector routes.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
1177
Fortinet Inc.

<!-- 来源页 1178 -->
Parameter
Description
Type
Size
Default
next-hop-self-vpnv4
Enable/disable setting VPNv4 next-hop to interface's IP address for this
neighbor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
next-hop-self-vpnv6
Enable/disable use of outgoing
interface's IP address as VPNv6 next-hop for this neighbor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
next-hop-self6
Enable/disable IPv6 next-hop
calculation for this neighbor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
override-capability
Enable/disable override result of
capability negotiation.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
passive
Enable/disable initiation of the TCP
session for this neighbor.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
password
Password used in MD5
authentication.
password
Not Specified
prefix-list-in
IPv4 Inbound filter for updates from
this neighbor.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
1178
Fortinet Inc.

<!-- 来源页 1179 -->
Parameter
Description
Type
Size
Default
prefix-list-in-vpnv4
Inbound filter for VPNv4 updates
from this neighbor.
string
Maximum
length: 35
prefix-list-in-vpnv6
Inbound filter for VPNv6 updates
from this neighbor.
string
Maximum
length: 35
prefix-list-in6
IPv6 Inbound filter for updates from
this neighbor.
string
Maximum
length: 35
prefix-list-out
IPv4 Outbound filter for updates to
this neighbor.
string
Maximum
length: 35
prefix-list-out-vpnv4
Outbound filter for VPNv4 updates to
this neighbor.
string
Maximum
length: 35
prefix-list-out-vpnv6
Outbound filter for VPNv6 updates to
this neighbor.
string
Maximum
length: 35
prefix-list-out6
IPv6 Outbound filter for updates to
this neighbor.
string
Maximum
length: 35
remote-as
AS number of neighbor.
user
Not Specified
remote-as-filter
BGP filter for remote AS.
string
Maximum
length: 35
remove-private-as
Enable/disable remove private AS
number from IPv4 outbound updates.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
remove-private-as-evpn
Enable/disable removing private AS
number from L2VPN EVPN outbound
updates.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
remove-private-as-vpnv4
Enable/disable remove private AS
number from VPNv4 outbound
updates.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
1179
Fortinet Inc.

<!-- 来源页 1180 -->
Parameter
Description
Type
Size
Default
remove-private-as-vpnv6
Enable/disable to remove private AS
number from VPNv6 outbound
updates.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
remove-private-as6
Enable/disable remove private AS
number from IPv6 outbound updates.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
restart-time
Graceful restart delay time (sec, 0 =
global default).
integer
Minimum value:
0 Maximum
value: 3600
0
retain-stale-time
Time to retain stale routes.
integer
Minimum value:
0 Maximum
value: 65535
0
route-map-in
IPv4 Inbound route map filter.
string
Maximum
length: 35
route-map-in-evpn
L2VPN EVPN inbound route map
filter.
string
Maximum
length: 35
route-map-in-vpnv4
VPNv4 inbound route map filter.
string
Maximum
length: 35
route-map-in-vpnv6
VPNv6 inbound route map filter.
string
Maximum
length: 35
route-map-in6
IPv6 Inbound route map filter.
string
Maximum
length: 35
route-map-out
IPv4 outbound route map filter.
string
Maximum
length: 35
route-map-out-evpn
L2VPN EVPN outbound route map
filter.
string
Maximum
length: 35
route-map-out-preferable
IPv4 outbound route map filter if the
peer is preferred.
string
Maximum
length: 35
route-map-out-vpnv4
VPNv4 outbound route map filter.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
1180
Fortinet Inc.

<!-- 来源页 1181 -->
Parameter
Description
Type
Size
Default
route-map-out-vpnv4-preferable
VPNv4 outbound route map filter if
the peer is preferred.
string
Maximum
length: 35
route-map-out-vpnv6
VPNv6 outbound route map filter.
string
Maximum
length: 35
route-map-out-vpnv6-preferable
VPNv6 outbound route map filter if
the peer is preferred.
string
Maximum
length: 35
route-map-out6
IPv6 Outbound route map filter.
string
Maximum
length: 35
route-map-out6-preferable
IPv6 outbound route map filter if the
peer is preferred.
string
Maximum
length: 35
route-reflector-client
Enable/disable IPv4 AS route
reflector client.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
route-reflector-client-evpn
Enable/disable L2VPN EVPN AS route
reflector client for this neighbor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
route-reflector-client-vpnv4
Enable/disable VPNv4 AS route
reflector client for this neighbor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
route-reflector-client-vpnv6
Enable/disable VPNv6 AS route
reflector client for this neighbor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
route-reflector-client6
Enable/disable IPv6 AS route
reflector client.
option
-disable
FortiOS 8.0.0 CLI Reference
1181
Fortinet Inc.

<!-- 来源页 1182 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable setting.
disable
Disable setting.
route-server-client
Enable/disable IPv4 AS route server
client.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
route-server-client-evpn
Enable/disable L2VPN EVPN AS route
server client for this neighbor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
route-server-client-vpnv4
Enable/disable VPNv4 AS route
server client for this neighbor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
route-server-client-vpnv6
Enable/disable VPNv6 AS route
server client for this neighbor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
route-server-client6
Enable/disable IPv6 AS route server
client.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
1182
Fortinet Inc.

<!-- 来源页 1183 -->
Parameter
Description
Type
Size
Default
rr-attr-allow-change
Enable/disable allowing change of
route attributes when advertising to
IPv4 route reflector clients.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
rr-attr-allow-change-evpn
Enable/disable allowing change of
route attributes when advertising to
L2VPN EVPN route reflector clients.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
rr-attr-allow-change-vpnv4
Enable/disable allowing change of
route attributes when advertising to
VPNv4 route reflector clients.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
rr-attr-allow-change-vpnv6
Enable/disable allowing change of
route attributes when advertising to
VPNv6 route reflector clients.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
rr-attr-allow-change6
Enable/disable allowing change of
route attributes when advertising to
IPv6 route reflector clients.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
send-community
IPv4 Send community attribute to
neighbor.
option
-both
FortiOS 8.0.0 CLI Reference
1183
Fortinet Inc.

<!-- 来源页 1184 -->
Parameter
Description
Type
Size
Default
Option
Description
standard
Standard.
extended
Extended.
both
Both.
disable
Disable
send-community-evpn
Enable/disable sending community
attribute to neighbor for L2VPN EVPN
address family.
option
-both
Option
Description
standard
Standard.
extended
Extended.
both
Both.
disable
Disable
send-community-vpnv4
Enable/disable sending community
attribute to this neighbor for VPNv4
address family.
option
-both
Option
Description
standard
Standard.
extended
Extended.
both
Both.
disable
Disable
send-community-vpnv6
Enable/disable sending community
attribute to this neighbor for VPNv6
address family.
option
-both
Option
Description
standard
Standard.
extended
Extended.
both
Both.
disable
Disable
send-community6
IPv6 Send community attribute to
neighbor.
option
-both
FortiOS 8.0.0 CLI Reference
1184
Fortinet Inc.

<!-- 来源页 1185 -->
Parameter
Description
Type
Size
Default
Option
Description
standard
Standard.
extended
Extended.
both
Both.
disable
Disable
shutdown
Enable/disable shutting down this
neighbor.
option
-disable
Option
Description
disable
Disable shut down of this neighbor.
enable
Enable shut down of this neighbor.
graceful
Shut down this neighbor gracefully.
graceful-soft
Enable GSHUT community for this neighbor.
soft-reconfiguration
Enable/disable allow IPv4 inbound
soft reconfiguration.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
soft-reconfiguration-evpn
Enable/disable L2VPN EVPN inbound
soft reconfiguration.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
soft-reconfiguration-vpnv4
Enable/disable allow VPNv4 inbound
soft reconfiguration.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
1185
Fortinet Inc.

<!-- 来源页 1186 -->
Parameter
Description
Type
Size
Default
soft-reconfiguration-vpnv6
Enable/disable VPNv6 inbound soft
reconfiguration.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
soft-reconfiguration6
Enable/disable allow IPv6 inbound
soft reconfiguration.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
stale-route
Enable/disable stale route after
neighbor down.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
strict-capability-match
Enable/disable strict capability
matching.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
unsuppress-map
IPv4 Route map to selectively
unsuppress suppressed routes.
string
Maximum
length: 35
unsuppress-map6
IPv6 Route map to selectively
unsuppress suppressed routes.
string
Maximum
length: 35
update-source
Interface to use as source IP/IPv6
address of TCP connections.
string
Maximum
length: 15
use-sdwan *
Use SDWAN rules for BGP
connection.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
1186
Fortinet Inc.

<!-- 来源页 1187 -->
Parameter
Description
Type
Size
Default
weight
Neighbor weight.
integer
Minimum value:
0 Maximum
value: 65535
4294967295
* This parameter may not exist in some models.
** Values may differ between models.
config neighbor-range
Parameter
Description
Type
Size
Default
id
Neighbor range ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
max-neighbor-num
Maximum number of neighbors.
integer
Minimum value:
1 Maximum
value: 1000
0
neighbor-group
Neighbor group name.
string
Maximum
length: 63
prefix
Neighbor range prefix.
ipv4-classnet
Not Specified
0.0.0.0
0.0.0.0
config neighbor-range6
Parameter
Description
Type
Size
Default
id
IPv6 neighbor range ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
max-neighbor-num
Maximum number of neighbors.
integer
Minimum value:
1 Maximum
value: 1000
0
neighbor-group
Neighbor group name.
string
Maximum
length: 63
prefix6
IPv6 prefix.
ipv6-network
Not Specified
::/0
FortiOS 8.0.0 CLI Reference
1187
Fortinet Inc.

<!-- 来源页 1188 -->
config network
Parameter
Description
Type
Size
Default
backdoor
Enable/disable route as backdoor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
id
ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
internet-service-name
*
Name of internet service.
string
Maximum
length: 79
network-import-check
Configure insurance of BGP network route
existence in IGP.
option
-global
Option
Description
global
Use global network sync value.
enable
Enable network sync per prefix.
disable
Disable network sync per prefix.
prefix
Network prefix.
ipv4-classnet
Not Specified
0.0.0.0
0.0.0.0
prefix-name
Name of firewall address or address group.
string
Maximum
length: 79
route-map
Route map to modify generated route.
string
Maximum
length: 35
* This parameter may not exist in some models.
config network6
Parameter
Description
Type
Size
Default
backdoor
Enable/disable route as backdoor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
1188
Fortinet Inc.

<!-- 来源页 1189 -->
Parameter
Description
Type
Size
Default
id
ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
network-import-check
Configure insurance of BGP network route
existence in IGP.
option
-global
Option
Description
global
Use global network sync value.
enable
Enable network sync per prefix.
disable
Disable network sync per prefix.
prefix6
Network IPv6 prefix.
ipv6-network
Not Specified
::/0
route-map
Route map to modify generated route.
string
Maximum
length: 35
config redistribute
Parameter
Description
Type
Size
Default
name
Distribute list entry name.
string
Maximum
length: 35
route-map
Route map name.
string
Maximum
length: 35
route-map-evpn *
Route map name for EVPN redistribution.
string
Maximum
length: 35
status
Status.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
status-evpn *
EVPN redistribution status.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
* This parameter may not exist in some models.
FortiOS 8.0.0 CLI Reference
1189
Fortinet Inc.

<!-- 来源页 1190 -->
config redistribute6
Parameter
Description
Type
Size
Default
name
Distribute list entry name.
string
Maximum
length: 35
route-map
Route map name.
string
Maximum
length: 35
status
Status.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
config vrf
Parameter
Description
Type
Size
Default
export-rt
<route-target>
List of export route target.
Attribute: AA:NN|A.B.C.D:NN.
string
Maximum
length: 79
import-route-map
Import route map.
string
Maximum
length: 35
import-rt
<route-target>
List of import route target.
Attribute: AA:NN|A.B.C.D:NN
string
Maximum
length: 79
rd
Route Distinguisher: AA:NN|A.B.C.D:NN.
string
Maximum
length: 79
role
VRF role.
option
-standalone
Option
Description
standalone
Stand-alone VRF.
ce
CE VRF.
pe
PE VRF.
vrf
Origin VRF ID <0-511>.
string
Maximum
length: 7
FortiOS 8.0.0 CLI Reference
1190
Fortinet Inc.

<!-- 来源页 1191 -->
config leak-target
Parameter
Description
Type
Size
Default
interface
Interface which is used to leak routes to target VRF.
string
Maximum
length: 15
route-map
Route map of VRF leaking.
string
Maximum
length: 35
vrf
Target VRF ID <0-511>.
string
Maximum
length: 7
config vrf6
Parameter
Description
Type
Size
Default
export-rt
<route-target>
List of export route target.
Attribute: AA:NN|A.B.C.D:NN.
string
Maximum
length: 79
import-route-map
Import route map.
string
Maximum
length: 35
import-rt
<route-target>
List of import route target.
Attribute: AA:NN|A.B.C.D:NN
string
Maximum
length: 79
rd
Route Distinguisher: AA:NN|A.B.C.D:NN.
string
Maximum
length: 79
role
VRF role.
option
-standalone
Option
Description
standalone
Stand-alone VRF.
ce
CE VRF.
pe
PE VRF.
vrf
Origin VRF ID <0-511>.
string
Maximum
length: 7
config leak-target
Parameter
Description
Type
Size
Default
interface
Interface which is used to leak routes to target VRF.
string
Maximum
length: 15
route-map
Route map of VRF leaking.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
1191
Fortinet Inc.

<!-- 来源页 1192 -->
Parameter
Description
Type
Size
Default
vrf
Target VRF ID <0-511>.
string
Maximum
length: 7
config router community-list
Configure community lists.
config router community-list
Description: Configure community lists.
edit <name>
config rule
Description: Community list rule.
edit <id>
set action [deny|permit]
set match {string}
set regexp {string}
next
end
set type [standard|expanded]
next
end
config router community-list
Parameter
Description
Type
Size
Default
name
Community list name.
string
Maximum
length: 35
type
Community list type (standard or expanded).
option
-standard
Option
Description
standard
Standard community list type.
expanded
Expanded community list type.
config rule
Parameter
Description
Type
Size
Default
action
Permit or deny route-based operations, based
on the route's COMMUNITY attribute.
option
-FortiOS 8.0.0 CLI Reference
1192
Fortinet Inc.

<!-- 来源页 1193 -->
Parameter
Description
Type
Size
Default
Option
Description
deny
Deny route-based operations.
permit
Permit or allow route-based operations.
id
ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
match
Community specifications for matching a
reserved community.
string
Maximum
length: 255
regexp
Ordered list of COMMUNITY attributes as a
regular expression.
string
Maximum
length: 255
config router extcommunity-list
Configure extended community lists.
config router extcommunity-list
Description: Configure extended community lists.
edit <name>
config rule
Description: Extended community list rule.
edit <id>
set action [deny|permit]
set match {string}
set regexp {string}
set type [rt|soo]
next
end
set type [standard|expanded]
next
end
config router extcommunity-list
Parameter
Description
Type
Size
Default
name
Extended community list name.
string
Maximum
length: 35
type
Extended community list type (standard or
expanded).
option
-standard
FortiOS 8.0.0 CLI Reference
1193
Fortinet Inc.

<!-- 来源页 1194 -->
Parameter
Description
Type
Size
Default
Option
Description
standard
Standard extended community list type.
expanded
Expanded extended community list type.
config rule
Parameter
Description
Type
Size
Default
action
Permit or deny route-based operations, based
on the route's EXTENDED COMMUNITY
attribute.
option
-Option
Description
deny
Deny route-based operations.
permit
Permit or allow route-based operations.
id
ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
match
Extended community specifications for
matching a reserved extended community.
string
Maximum
length: 255
regexp
Ordered list of EXTENDED COMMUNITY
attributes as a regular expression.
string
Maximum
length: 255
type
Type of extended community.
option
-rt
Option
Description
rt
Route Target.
soo
Site of Origin.
config router isis
Configure IS-IS.
config router isis
Description: Configure IS-IS.
set adjacency-check [enable|disable]
set adjacency-check6 [enable|disable]
set adv-passive-only [enable|disable]
set adv-passive-only6 [enable|disable]
FortiOS 8.0.0 CLI Reference
1194
Fortinet Inc.

<!-- 来源页 1195 -->
set auth-keychain-l1 {string}
set auth-keychain-l2 {string}
set auth-mode-l1 [password|md5]
set auth-mode-l2 [password|md5]
set auth-password-l1 {password}
set auth-password-l2 {password}
set auth-sendonly-l1 [enable|disable]
set auth-sendonly-l2 [enable|disable]
set default-originate [enable|disable]
set default-originate6 [enable|disable]
set dynamic-hostname [enable|disable]
set ignore-lsp-errors [enable|disable]
set is-type [level-1-2|level-1|...]
config isis-interface
Description: IS-IS interface configuration.
edit <name>
set auth-keychain-l1 {string}
set auth-keychain-l2 {string}
set auth-mode-l1 [md5|password]
set auth-mode-l2 [md5|password]
set auth-password-l1 {password}
set auth-password-l2 {password}
set auth-send-only-l1 [enable|disable]
set auth-send-only-l2 [enable|disable]
set circuit-type [level-1-2|level-1|...]
set csnp-interval-l1 {integer}
set csnp-interval-l2 {integer}
set hello-interval-l1 {integer}
set hello-interval-l2 {integer}
set hello-multiplier-l1 {integer}
set hello-multiplier-l2 {integer}
set hello-padding [enable|disable]
set lsp-interval {integer}
set lsp-retransmit-interval {integer}
set mesh-group [enable|disable]
set mesh-group-id {integer}
set metric-l1 {integer}
set metric-l2 {integer}
set network-type [broadcast|point-to-point|...]
set priority-l1 {integer}
set priority-l2 {integer}
set status [enable|disable]
set status6 [enable|disable]
set wide-metric-l1 {integer}
set wide-metric-l2 {integer}
next
end
config isis-net
Description: IS-IS net configuration.
edit <id>
set net {user}
next
FortiOS 8.0.0 CLI Reference
1195
Fortinet Inc.

<!-- 来源页 1196 -->
end
set lsp-gen-interval-l1 {integer}
set lsp-gen-interval-l2 {integer}
set lsp-refresh-interval {integer}
set max-lsp-lifetime {integer}
set metric-style [narrow|wide|...]
set overload-bit [enable|disable]
set overload-bit-on-startup {integer}
set overload-bit-suppress {option1}, {option2}, ...
config redistribute
Description: IS-IS redistribute protocols. Read-only.
edit <protocol>
set level [level-1-2|level-1|...]
set metric {integer}
set metric-type [external|internal]
set routemap {string}
set status [enable|disable]
next
end
set redistribute-l1 [enable|disable]
set redistribute-l1-list {string}
set redistribute-l2 [enable|disable]
set redistribute-l2-list {string}
config redistribute6
Description: IS-IS IPv6 redistribution for routing protocols. Read-only.
edit <protocol>
set level [level-1-2|level-1|...]
set metric {integer}
set metric-type [external|internal]
set routemap {string}
set status [enable|disable]
next
end
set redistribute6-l1 [enable|disable]
set redistribute6-l1-list {string}
set redistribute6-l2 [enable|disable]
set redistribute6-l2-list {string}
set spf-interval-exp-l1 {user}
set spf-interval-exp-l2 {user}
config summary-address
Description: IS-IS summary addresses.
edit <id>
set level [level-1-2|level-1|...]
set prefix {ipv4-classnet-any}
next
end
config summary-address6
Description: IS-IS IPv6 summary addresses.
edit <id>
set level [level-1-2|level-1|...]
set prefix6 {ipv6-prefix}
next
FortiOS 8.0.0 CLI Reference
1196
Fortinet Inc.

<!-- 来源页 1197 -->
end
end
config router isis
Parameter
Description
Type
Size
Default
adjacency-check
Enable/disable adjacency check.
option
-disable
Option
Description
enable
Enable adjacency check.
disable
Disable adjacency check.
adjacency-check6
Enable/disable IPv6 adjacency check.
option
-disable
Option
Description
enable
Enable IPv6 adjacency check.
disable
Disable IPv6 adjacency check.
adv-passive-only
Enable/disable IS-IS advertisement of passive
interfaces only.
option
-disable
Option
Description
enable
Advertise passive interfaces only.
disable
Advertise all IS-IS enabled interfaces.
adv-passive-only6
Enable/disable IPv6 IS-IS advertisement of
passive interfaces only.
option
-disable
Option
Description
enable
Advertise passive interfaces only.
disable
Advertise all IS-IS enabled interfaces.
auth-keychain-l1
Authentication key-chain for level 1 PDUs.
string
Maximum
length: 35
auth-keychain-l2
Authentication key-chain for level 2 PDUs.
string
Maximum
length: 35
auth-mode-l1
Level 1 authentication mode.
option
-password
FortiOS 8.0.0 CLI Reference
1197
Fortinet Inc.

<!-- 来源页 1198 -->
Parameter
Description
Type
Size
Default
Option
Description
password
Password.
md5
MD5.
auth-mode-l2
Level 2 authentication mode.
option
-password
Option
Description
password
Password.
md5
MD5.
auth-password-l1
Authentication password for level 1 PDUs.
password
Not
Specified
auth-password-l2
Authentication password for level 2 PDUs.
password
Not
Specified
auth-sendonly-l1
Enable/disable level 1 authentication send-only.
option
-disable
Option
Description
enable
Enable level 1 authentication send-only.
disable
Disable level 1 authentication send-only.
auth-sendonly-l2
Enable/disable level 2 authentication send-only.
option
-disable
Option
Description
enable
Enable level 2 authentication send-only.
disable
Disable level 2 authentication send-only.
default-originate
Enable/disable distribution of default route
information.
option
-disable
Option
Description
enable
Enable distribution of default route information.
disable
Disable distribution of default route information.
default-originate6
Enable/disable distribution of default IPv6
route information.
option
-disable
FortiOS 8.0.0 CLI Reference
1198
Fortinet Inc.

<!-- 来源页 1199 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable distribution of default IPv6 route information.
disable
Disable distribution of default IPv6 route information.
dynamic-hostname
Enable/disable dynamic hostname.
option
-disable
Option
Description
enable
Enable dynamic hostname.
disable
Disable dynamic hostname.
ignore-lsp-errors
Enable/disable ignoring of LSP errors with bad
checksums.
option
-disable
Option
Description
enable
Enable ignoring of LSP errors with bad checksums.
disable
Disable ignoring of LSP errors with bad checksums.
is-type
IS type.
option
-level-1-2
Option
Description
level-1-2
Level 1 and 2.
level-1
Level 1 only.
level-2-only
Level 2 only.
lsp-gen-interval-l1
Minimum interval for level 1 LSP regenerating.
integer
Minimum
value: 1
Maximum
value: 120
30
lsp-gen-interval-l2
Minimum interval for level 2 LSP regenerating.
integer
Minimum
value: 1
Maximum
value: 120
30
lsp-refresh-interval
LSP refresh time in seconds.
integer
Minimum
value: 1
Maximum
value:
65535
900
FortiOS 8.0.0 CLI Reference
1199
Fortinet Inc.

<!-- 来源页 1200 -->
Parameter
Description
Type
Size
Default
max-lsp-lifetime
Maximum LSP lifetime in seconds.
integer
Minimum
value: 350
Maximum
value:
65535
1200
metric-style
Use old-style (ISO 10589) or new-style packet
formats.
option
-narrow
Option
Description
narrow
Use old style of TLVs with narrow metric.
wide
Use new style of TLVs to carry wider metric.
transition
Send and accept both styles of TLVs during transition.
narrow-transition
Narrow and accept both styles of TLVs during transition.
narrow-transition-l1
Narrow-transition level-1 only.
narrow-transition-l2
Narrow-transition level-2 only.
wide-l1
Wide level-1 only.
wide-l2
Wide level-2 only.
wide-transition
Wide and accept both styles of TLVs during transition.
wide-transition-l1
Wide-transition level-1 only.
wide-transition-l2
Wide-transition level-2 only.
transition-l1
Transition level-1 only.
transition-l2
Transition level-2 only.
overload-bit
Enable/disable signal other routers not to use
us in SPF.
option
-disable
Option
Description
enable
Enable overload bit.
disable
Disable overload bit.
FortiOS 8.0.0 CLI Reference
1200
Fortinet Inc.

<!-- 来源页 1201 -->
Parameter
Description
Type
Size
Default
overload-bit-on-startup
Overload-bit only temporarily after reboot.
integer
Minimum
value: 5
Maximum
value:
86400
0
overload-bit-suppress
Suppress overload-bit for the specific prefixes.
option
-Option
Description
external
External.
interlevel
Inter-level.
redistribute-l1
Enable/disable redistribution of level 1 routes
into level 2.
option
-disable
Option
Description
enable
Enable redistribution of level 1 routes into level 2.
disable
Disable redistribution of level 1 routes into level 2.
redistribute-l1-list
Access-list for route redistribution from l1 to l2.
string
Maximum
length: 35
redistribute-l2
Enable/disable redistribution of level 2 routes
into level 1.
option
-disable
Option
Description
enable
Enable redistribution of level 2 routes into level 1.
disable
Disable redistribution of level 2 routes into level 1.
redistribute-l2-list
Access-list for route redistribution from l2 to l1.
string
Maximum
length: 35
redistribute6-l1
Enable/disable redistribution of level 1 IPv6
routes into level 2.
option
-disable
Option
Description
enable
Enable redistribution of level 1 IPv6 routes into level 2.
disable
Disable redistribution of level 1 IPv6 routes into level 2.
redistribute6-l1-list
Access-list for IPv6 route redistribution from l1
to l2.
string
Maximum
length: 35
redistribute6-l2
Enable/disable redistribution of level 2 IPv6
routes into level 1.
option
-disable
FortiOS 8.0.0 CLI Reference
1201
Fortinet Inc.

<!-- 来源页 1202 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable redistribution of level 2 IPv6 routes into level 1.
disable
Disable redistribution of level 2 IPv6 routes into level 1.
redistribute6-l2-list
Access-list for IPv6 route redistribution from l2
to l1.
string
Maximum
length: 35
spf-interval-exp-l1
Level 1 SPF calculation delay.
user
Not
Specified
spf-interval-exp-l2
Level 2 SPF calculation delay.
user
Not
Specified
config isis-interface
Parameter
Description
Type
Size
Default
auth-keychain-l1
Authentication key-chain for level 1 PDUs.
string
Maximum
length: 35
auth-keychain-l2
Authentication key-chain for level 2 PDUs.
string
Maximum
length: 35
auth-mode-l1
Level 1 authentication mode.
option
-password
Option
Description
md5
MD5.
password
Password.
auth-mode-l2
Level 2 authentication mode.
option
-password
Option
Description
md5
MD5.
password
Password.
auth-password-l1
Authentication password for level 1 PDUs.
password
Not Specified
auth-password-l2
Authentication password for level 2 PDUs.
password
Not Specified
auth-send-only-l1
Enable/disable authentication send-only for
level 1 PDUs.
option
-disable
FortiOS 8.0.0 CLI Reference
1202
Fortinet Inc.

<!-- 来源页 1203 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable authentication send-only for level 1 PDUs.
disable
Disable authentication send-only for level 1 PDUs.
auth-send-only-l2
Enable/disable authentication send-only for
level 2 PDUs.
option
-disable
Option
Description
enable
Enable authentication send-only for level 2 PDUs.
disable
Disable authentication send-only for level 2 PDUs.
circuit-type
IS-IS interface's circuit type.
option
-level-1-2
Option
Description
level-1-2
Level 1 and 2.
level-1
Level 1.
level-2
Level 2.
csnp-interval-l1
Level 1 CSNP interval.
integer
Minimum value:
1 Maximum
value: 65535
10
csnp-interval-l2
Level 2 CSNP interval.
integer
Minimum value:
1 Maximum
value: 65535
10
hello-interval-l1
Level 1 hello interval.
integer
Minimum value:
0 Maximum
value: 65535
10
hello-interval-l2
Level 2 hello interval.
integer
Minimum value:
0 Maximum
value: 65535
10
hello-multiplier-l1
Level 1 multiplier for Hello holding time.
integer
Minimum value:
2 Maximum
value: 100
3
hello-multiplier-l2
Level 2 multiplier for Hello holding time.
integer
Minimum value:
2 Maximum
value: 100
3
hello-padding
Enable/disable padding to IS-IS hello packets.
option
-enable
FortiOS 8.0.0 CLI Reference
1203
Fortinet Inc.

<!-- 来源页 1204 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable padding to IS-IS hello packets.
disable
Disable padding to IS-IS hello packets.
lsp-interval
LSP transmission interval (milliseconds).
integer
Minimum value:
1 Maximum
value:
4294967295
33
lsp-retransmit-interval
LSP retransmission interval (sec).
integer
Minimum value:
1 Maximum
value: 65535
5
mesh-group
Enable/disable IS-IS mesh group.
option
-disable
Option
Description
enable
Enable IS-IS mesh group.
disable
Disable IS-IS mesh group.
mesh-group-id
Mesh group ID <0-4294967295>, 0: mesh-group blocked.
integer
Minimum value:
0 Maximum
value:
4294967295
0
metric-l1
Level 1 metric for interface.
integer
Minimum value:
1 Maximum
value: 63
10
metric-l2
Level 2 metric for interface.
integer
Minimum value:
1 Maximum
value: 63
10
name
IS-IS interface name.
string
Maximum
length: 15
network-type
IS-IS interface's network type.
option
-Option
Description
broadcast
Broadcast.
point-to-point
Point-to-point.
loopback
Loopback.
priority-l1
Level 1 priority.
integer
Minimum value:
0 Maximum
value: 127
64
FortiOS 8.0.0 CLI Reference
1204
Fortinet Inc.

<!-- 来源页 1205 -->
Parameter
Description
Type
Size
Default
priority-l2
Level 2 priority.
integer
Minimum value:
0 Maximum
value: 127
64
status
Enable/disable interface for IS-IS.
option
-disable
Option
Description
enable
Enable interface for IS-IS.
disable
Disable interface for IS-IS.
status6
Enable/disable IPv6 interface for IS-IS.
option
-disable
Option
Description
enable
Enable IPv6 interface for IS-IS.
disable
Disable IPv6 interface for IS-IS.
wide-metric-l1
Level 1 wide metric for interface.
integer
Minimum value:
1 Maximum
value:
16777214
10
wide-metric-l2
Level 2 wide metric for interface.
integer
Minimum value:
1 Maximum
value:
16777214
10
config isis-net
Parameter
Description
Type
Size
Default
id
ISIS network ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
net
IS-IS networks (format = xx.xxxx. .xxxx.xx.).
user
Not Specified
config redistribute
Parameter
Description
Type
Size
Default
level
Level.
option
-level-2
Option
Description
level-1-2
Level 1 and 2.
FortiOS 8.0.0 CLI Reference
1205
Fortinet Inc.

<!-- 来源页 1206 -->
Parameter
Description
Type
Size
Default
Option
Description
level-1
Level 1.
level-2
Level 2.
metric
Metric.
integer
Minimum
value: 0
Maximum
value:
4261412864
0
metric-type
Metric type.
option
-internal
Option
Description
external
External.
internal
Internal.
protocol
Protocol name.
string
Maximum
length: 35
routemap
Route map name.
string
Maximum
length: 35
status
Status.
option
-disable
Option
Description
enable
Enable.
disable
Disable.
config redistribute6
Parameter
Description
Type
Size
Default
level
Level.
option
-level-2
Option
Description
level-1-2
Level 1 and 2.
level-1
Level 1.
level-2
Level 2.
FortiOS 8.0.0 CLI Reference
1206
Fortinet Inc.

<!-- 来源页 1207 -->
Parameter
Description
Type
Size
Default
metric
Metric.
integer
Minimum
value: 0
Maximum
value:
4261412864
0
metric-type
Metric type.
option
-internal
Option
Description
external
External metric type.
internal
Internal metric type.
protocol
Protocol name.
string
Maximum
length: 35
routemap
Route map name.
string
Maximum
length: 35
status
Enable/disable redistribution.
option
-disable
Option
Description
enable
Enable redistribution.
disable
Disable redistribution.
config summary-address
Parameter
Description
Type
Size
Default
id
Summary address entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
level
Level.
option
-level-2
Option
Description
level-1-2
Level 1 and 2.
level-1
Level 1.
level-2
Level 2.
prefix
Prefix.
ipv4-classnet-any
Not Specified
0.0.0.0
0.0.0.0
FortiOS 8.0.0 CLI Reference
1207
Fortinet Inc.

<!-- 来源页 1208 -->
config summary-address6
Parameter
Description
Type
Size
Default
id
Prefix entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
level
Level.
option
-level-2
Option
Description
level-1-2
Level 1 and 2.
level-1
Level 1.
level-2
Level 2.
prefix6
IPv6 prefix.
ipv6-prefix
Not Specified
::/0
config router key-chain
Configure key-chain.
config router key-chain
Description: Configure key-chain.
edit <name>
config key
Description: Configuration method to edit key settings.
edit <id>
set accept-lifetime {user}
set algorithm [md5|hmac-sha1|...]
set key-string {password}
set send-lifetime {user}
next
end
next
end
config router key-chain
Parameter
Description
Type
Size
Default
name
Key-chain name.
string
Maximum length:
35
FortiOS 8.0.0 CLI Reference
1208
Fortinet Inc.

<!-- 来源页 1209 -->
config key
Parameter
Description
Type
Size
Default
accept-lifetime
Lifetime of received authentication key.
user
Not
Specified
algorithm
Cryptographic algorithm.
option
-md5
Option
Description
md5
MD5.
hmac-sha1
HMAC-SHA1.
hmac-sha256
HMAC-SHA256.
hmac-sha384
HMAC-SHA384.
hmac-sha512
HMAC-SHA512.
cmac-aes128
CMAC-AES128.
id
Key ID (0 - 2147483647).
string
Maximum
length: 10
key-string
Password for the key (maximum = 64 characters).
password
Not
Specified
send-lifetime
Lifetime of sent authentication key.
user
Not
Specified
config router multicast
Configure router multicast.
config router multicast
Description: Configure router multicast.
config interface
Description: PIM interfaces.
edit <name>
set bfd [enable|disable]
set cisco-exclude-genid [enable|disable]
set dr-priority {integer}
set hello-holdtime {integer}
set hello-interval {integer}
config igmp
Description: IGMP configuration options.
set access-group {string}
set immediate-leave-group {string}
set last-member-query-count {integer}
set last-member-query-interval {integer}
set query-interval {integer}
FortiOS 8.0.0 CLI Reference
1209
Fortinet Inc.

<!-- 来源页 1210 -->
set query-max-response-time {integer}
set query-timeout {integer}
set router-alert-check [enable|disable]
set version [3|2|...]
end
config join-group
Description: Join multicast groups.
edit <address>
next
end
set multicast-flow {string}
set neighbour-filter {string}
set passive [enable|disable]
set pim-mode [sparse-mode|dense-mode]
set propagation-delay {integer}
set rp-candidate [enable|disable]
set rp-candidate-group {string}
set rp-candidate-interval {integer}
set rp-candidate-priority {integer}
set rpf-nbr-fail-back [enable|disable]
set rpf-nbr-fail-back-filter {string}
set state-refresh-interval {integer}
set static-group {string}
set ttl-threshold {integer}
next
end
set multicast-routing [enable|disable]
config pim-sm-global
Description: PIM sparse-mode global settings.
set accept-register-list {string}
set accept-source-list {string}
set bsr-allow-quick-refresh [enable|disable]
set bsr-candidate [enable|disable]
set bsr-hash {integer}
set bsr-interface {string}
set bsr-priority {integer}
set cisco-crp-prefix [enable|disable]
set cisco-ignore-rp-set-priority [enable|disable]
set cisco-register-checksum [enable|disable]
set cisco-register-checksum-group {string}
set join-prune-holdtime {integer}
set message-interval {integer}
set null-register-retries {integer}
set pim-use-sdwan [enable|disable]
set register-rate-limit {integer}
set register-rp-reachability [enable|disable]
set register-source [disable|interface|...]
set register-source-interface {string}
set register-source-ip {ipv4-address}
set register-supression {integer}
config rp-address
Description: Statically configure RP addresses.
FortiOS 8.0.0 CLI Reference
1210
Fortinet Inc.

<!-- 来源页 1211 -->
edit <id>
set group {string}
set ip-address {ipv4-address}
next
end
set rp-register-keepalive {integer}
set spt-threshold [enable|disable]
set spt-threshold-group {string}
set ssm [enable|disable]
set ssm-range {string}
end
config pim-sm-global-vrf
Description: per-VRF PIM sparse-mode global settings.
edit <vrf>
set bsr-allow-quick-refresh [enable|disable]
set bsr-candidate [enable|disable]
set bsr-hash {integer}
set bsr-interface {string}
set bsr-priority {integer}
set cisco-crp-prefix [enable|disable]
config rp-address
Description: Statically configure RP addresses.
edit <id>
set group {string}
set ip-address {ipv4-address}
next
end
next
end
set route-limit {integer}
set route-threshold {integer}
end
config router multicast
Parameter
Description
Type
Size
Default
multicast-routing
Enable/disable IP multicast routing.
option
-disable
Option
Description
enable
Enable IP multicast routing.
disable
Disable IP multicast routing.
FortiOS 8.0.0 CLI Reference
1211
Fortinet Inc.

<!-- 来源页 1212 -->
Parameter
Description
Type
Size
Default
route-limit
Maximum number of multicast routes.
integer
Minimum
value: 1
Maximum
value:
2147483647
2147483647
route-threshold
Generate warnings when the number of
multicast routes exceeds this number, must
not be greater than route-limit.
integer
Minimum
value: 1
Maximum
value:
2147483647
config interface
Parameter
Description
Type
Size
Default
bfd
Enable/disable Protocol Independent Multicast
(PIM) Bidirectional Forwarding Detection
(BFD).
option
-disable
Option
Description
enable
Enable Protocol Independent Multicast (PIM) Bidirectional Forwarding
Detection (BFD).
disable
Disable Protocol Independent Multicast (PIM) Bidirectional Forwarding
Detection (BFD).
cisco-exclude-genid
Exclude GenID from hello packets
(compatibility with old Cisco IOS).
option
-disable
Option
Description
enable
Do not send GenID.
disable
Send GenID according to standard.
dr-priority
DR election priority.
integer
Minimum value:
1 Maximum
value:
4294967295
1
hello-holdtime
Time before old neighbor information expires
(0 - 65535 sec, default = 105).
integer
Minimum value:
1 Maximum
value: 65535
105
hello-interval
Interval between sending PIM hello messages
(0 - 65535 sec, default = 30).
integer
Minimum value:
1 Maximum
value: 65535
30
FortiOS 8.0.0 CLI Reference
1212
Fortinet Inc.

<!-- 来源页 1213 -->
Parameter
Description
Type
Size
Default
multicast-flow
Acceptable source for multicast group.
string
Maximum
length: 35
name
Interface name.
string
Maximum
length: 15
neighbour-filter
Routers acknowledged as neighbor routers.
string
Maximum
length: 35
passive
Enable/disable listening to IGMP but not
participating in PIM.
option
-disable
Option
Description
enable
Listen only.
disable
Participate in PIM.
pim-mode
PIM operation mode.
option
-sparse-mode
Option
Description
sparse-mode
sparse-mode
dense-mode
dense-mode
propagation-delay
Delay flooding packets on this interface (100 -5000 msec, default = 500).
integer
Minimum value:
100 Maximum
value: 5000
500
rp-candidate
Enable/disable compete to become RP in
elections.
option
-disable
Option
Description
enable
Compete for RP elections.
disable
Do not compete for RP elections.
rp-candidate-group
Multicast groups managed by this RP.
string
Maximum
length: 35
rp-candidate-interval
RP candidate advertisement interval (1 - 16383
sec, default = 60).
integer
Minimum value:
1 Maximum
value: 16383
60
rp-candidate-priority
Router's priority as RP.
integer
Minimum value:
0 Maximum
value: 255
192
rpf-nbr-fail-back
Enable/disable fail back for RPF neighbor
query.
option
-disable
FortiOS 8.0.0 CLI Reference
1213
Fortinet Inc.

<!-- 来源页 1214 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable fail back for RPF neighbor query.
disable
Disable fail back for RPF neighbor query.
rpf-nbr-fail-back-filter
Filter for fail back RPF neighbors.
string
Maximum
length: 35
state-refresh-interval
Interval between sending state-refresh
packets (1 - 100 sec, default = 60).
integer
Minimum value:
1 Maximum
value: 100
60
static-group
Statically set multicast groups to forward out.
string
Maximum
length: 35
ttl-threshold
Minimum TTL of multicast packets that will be
forwarded (applied only to new multicast
routes) (1 - 255, default = 1).
integer
Minimum value:
1 Maximum
value: 255
1
config igmp
Parameter
Description
Type
Size
Default
access-group
Groups IGMP hosts are allowed to join.
string
Maximum
length: 35
immediate-leave-group
Groups to drop membership for immediately after
receiving IGMPv2 leave.
string
Maximum
length: 35
last-member-query-count
Number of group specific queries before removing
group (2 - 7, default = 2).
integer
Minimum
value: 2
Maximum
value: 7
2
last-member-query-interval
Timeout between IGMPv2 leave and removing
group (1 - 65535 msec, default = 1000).
integer
Minimum
value: 1
Maximum
value:
65535
1000
query-interval
Interval between queries to IGMP hosts (1 - 65535
sec, default = 125).
integer
Minimum
value: 1
Maximum
value:
65535
125
query-max-response-time
Maximum time to wait for a IGMP query response (1
- 25 sec, default = 10).
integer
Minimum
value: 1
Maximum
value: 25
10
FortiOS 8.0.0 CLI Reference
1214
Fortinet Inc.

<!-- 来源页 1215 -->
Parameter
Description
Type
Size
Default
query-timeout
Timeout between queries before becoming
querying unit for network (60 - 900, default = 255).
integer
Minimum
value: 60
Maximum
value: 900
255
router-alert-check
Enable/disable require IGMP packets contain router
alert option.
option
-disable
Option
Description
enable
Require Router Alert option in IGMP packets.
disable
don't require Router Alert option in IGMP packets
version
Maximum version of IGMP to support.
option
-3
Option
Description
3
Version 3 and lower.
2
Version 2 and lower.
1
Version 1.
config join-group
Parameter
Description
Type
Size
Default
address
Multicast group IP address.
ipv4-address-any
Not
Specified
0.0.0.0
config pim-sm-global
Parameter
Description
Type
Size
Default
accept-register-list
Sources allowed to register packets with this
Rendezvous Point (RP).
string
Maximum
length: 35
accept-source-list
Sources allowed to send multicast traffic.
string
Maximum
length: 35
bsr-allow-quick-refresh
Enable/disable accept BSR quick refresh packets
from neighbors.
option
-disable
Option
Description
enable
Allow quick refresh packets.
disable
Do not allow quick refresh packets.
FortiOS 8.0.0 CLI Reference
1215
Fortinet Inc.

<!-- 来源页 1216 -->
Parameter
Description
Type
Size
Default
bsr-candidate
Enable/disable allowing this router to become a
bootstrap router (BSR).
option
-disable
Option
Description
enable
Allow this router to function as a BSR.
disable
Do not allow this router to function as a BSR.
bsr-hash
BSR hash length (0 - 32, default = 10).
integer
Minimum
value: 0
Maximum
value: 32
10
bsr-interface
Interface to advertise as candidate BSR.
string
Maximum
length: 15
bsr-priority
BSR priority (0 - 255, default = 0).
integer
Minimum
value: 0
Maximum
value: 255
0
cisco-crp-prefix
Enable/disable making candidate RP compatible
with old Cisco IOS.
option
-disable
Option
Description
enable
Do not allow sending group prefix of zero.
disable
Allow sending group prefix of zero.
cisco-ignore-rp-set-priority
Use only hash for RP selection (compatibility with
old Cisco IOS).
option
-disable
Option
Description
enable
Ignore RP-SET priority value.
disable
Do not ignore RP-SET priority value.
cisco-register-checksum
Checksum entire register packet(for old Cisco IOS
compatibility).
option
-disable
Option
Description
enable
register checksum entire packet.
disable
Do not register checksum entire packet.
FortiOS 8.0.0 CLI Reference
1216
Fortinet Inc.

<!-- 来源页 1217 -->
Parameter
Description
Type
Size
Default
cisco-register-checksum-group
Cisco register checksum only these groups.
string
Maximum
length: 35
join-prune-holdtime
Join/prune holdtime (1 - 65535, default = 210).
integer
Minimum
value: 1
Maximum
value:
65535
210
message-interval
Period of time between sending periodic PIM
join/prune messages in seconds (1 - 65535, default
= 60).
integer
Minimum
value: 1
Maximum
value:
65535
60
null-register-retries
Maximum retries of null register (1 - 20, default =
1).
integer
Minimum
value: 1
Maximum
value: 20
1
pim-use-sdwan
Enable/disable use of SDWAN when checking RPF
neighbor and sending of REG packet.
option
-disable
Option
Description
enable
Enable use of SDWAN when checking RPF neighbor and sending of REG
packet.
disable
Disable use of SDWAN when checking RPF neighbor and sending of
REG packet.
register-rate-limit
Limit of packets/sec per source registered through
this RP (0 - 65535, default = 0 which means
unlimited).
integer
Minimum
value: 0
Maximum
value:
65535
0
register-rp-reachability
Enable/disable check RP is reachable before
registering packets.
option
-enable
Option
Description
enable
Check target RP is unicast reachable before registering.
disable
Do not check RP unicast reachability.
register-source
Override source address in register packets.
option
-disable
FortiOS 8.0.0 CLI Reference
1217
Fortinet Inc.

<!-- 来源页 1218 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Use source address of RPF interface.
interface
Use primary IP of an interface.
ip-address
Use a local IP address.
register-source-interface
Override with primary interface address.
string
Maximum
length: 15
register-source-ip
Override with local IP address.
ipv4-address
Not
Specified
0.0.0.0
register-supression
Period of time to honor register-stop message (1 -65535 sec, default = 60).
integer
Minimum
value: 1
Maximum
value:
65535
60
rp-register-keepalive
Timeout for RP receiving data on (S,G) tree (1 -65535 sec, default = 185).
integer
Minimum
value: 1
Maximum
value:
65535
185
spt-threshold
Enable/disable switching to source specific trees.
option
-enable
Option
Description
enable
Switch to Source tree when available.
disable
Do not switch to Source tree when available.
spt-threshold-group
Groups allowed to switch to source tree.
string
Maximum
length: 35
ssm
Enable/disable source specific multicast.
option
-disable
Option
Description
enable
Allow source specific multicast.
disable
Do not allow source specific multicast.
ssm-range
Groups allowed to source specific multicast.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
1218
Fortinet Inc.

<!-- 来源页 1219 -->
config rp-address
Parameter
Description
Type
Size
Default
group
Groups to use this RP.
string
Maximum
length: 35
id
ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
ip-address
RP router address.
ipv4-address
Not Specified
0.0.0.0
config pim-sm-global-vrf
Parameter
Description
Type
Size
Default
bsr-allow-quick-refresh
Enable/disable accept BSR quick refresh
packets from neighbors.
option
-disable
Option
Description
enable
Allow quick refresh packets.
disable
Do not allow quick refresh packets.
bsr-candidate
Enable/disable allowing this router to become a
bootstrap router (BSR).
option
-disable
Option
Description
enable
Allow this router to function as a BSR.
disable
Do not allow this router to function as a BSR.
bsr-hash
BSR hash length (0 - 32, default = 10).
integer
Minimum
value: 0
Maximum
value: 32
10
bsr-interface
Interface to advertise as candidate BSR.
string
Maximum
length: 15
bsr-priority
BSR priority (0 - 255, default = 0).
integer
Minimum
value: 0
Maximum
value: 255
0
cisco-crp-prefix
Enable/disable making candidate RP compatible
with old Cisco IOS.
option
-disable
FortiOS 8.0.0 CLI Reference
1219
Fortinet Inc.

<!-- 来源页 1220 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Do not allow sending group prefix of zero.
disable
Allow sending group prefix of zero.
vrf
VRF ID.
integer
Minimum
value: 1
Maximum
value: 511
1886221359
**
** Values may differ between models.
config rp-address
Parameter
Description
Type
Size
Default
group
Groups to use this RP.
string
Maximum
length: 35
id
ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
ip-address
RP router address.
ipv4-address
Not Specified
0.0.0.0
config router multicast6
Configure IPv6 multicast.
config router multicast6
Description: Configure IPv6 multicast.
config interface
Description: Protocol Independent Multicast (PIM) interfaces.
edit <name>
set hello-holdtime {integer}
set hello-interval {integer}
set rp-candidate [enable|disable]
set rp-candidate-group {string}
set rp-candidate-interval {integer}
set rp-candidate-priority {integer}
set static-group {string}
next
end
set multicast-pmtu [enable|disable]
set multicast-routing [enable|disable]
FortiOS 8.0.0 CLI Reference
1220
Fortinet Inc.

<!-- 来源页 1221 -->
config pim-sm-global
Description: PIM sparse-mode global settings.
set bsr-allow-quick-refresh [enable|disable]
set bsr-candidate [enable|disable]
set bsr-hash {integer}
set bsr-interface {string}
set bsr-priority {integer}
set cisco-crp-prefix [enable|disable]
set cisco-ignore-rp-set-priority [enable|disable]
set pim-use-sdwan [enable|disable]
set register-rate-limit {integer}
config rp-address
Description: Statically configured RP addresses.
edit <id>
set group {string}
set ip6-address {ipv6-address}
next
end
set spt-threshold [enable|disable]
set spt-threshold-group {string}
end
config pim-sm-global-vrf
Description: per-VRF PIM sparse-mode global settings.
edit <vrf>
set bsr-allow-quick-refresh [enable|disable]
set bsr-candidate [enable|disable]
set bsr-hash {integer}
set bsr-interface {string}
set bsr-priority {integer}
set cisco-crp-prefix [enable|disable]
config rp-address
Description: Statically configured RP addresses.
edit <id>
set group {string}
set ip6-address {ipv6-address}
next
end
next
end
end
config router multicast6
Parameter
Description
Type
Size
Default
multicast-pmtu
Enable/disable PMTU for IPv6 multicast.
option
-disable
FortiOS 8.0.0 CLI Reference
1221
Fortinet Inc.

<!-- 来源页 1222 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable PMTU for IPv6 multicast.
disable
Disable PMTU for IPv6 multicast.
multicast-routing
Enable/disable IPv6 multicast routing.
option
-disable
Option
Description
enable
Enable IPv6 multicast routing.
disable
Disable IPv6 multicast routing.
config interface
Parameter
Description
Type
Size
Default
hello-holdtime
Time before old neighbor information expires in
seconds (1 - 65535, default = 105).
integer
Minimum
value: 1
Maximum
value:
65535
hello-interval
Interval between sending PIM hello messages in
seconds (1 - 65535, default = 30).
integer
Minimum
value: 1
Maximum
value:
65535
30
name
Interface name.
string
Maximum
length: 15
rp-candidate
*
Enable/disable compete to become RP in elections.
option
-disable
Option
Description
enable
Compete for RP elections.
disable
Do not compete for RP elections.
rp-candidate-group *
Multicast groups managed by this RP.
string
Maximum
length: 35
rp-candidate-interval *
RP candidate advertisement interval (1 - 16383 sec,
default = 60).
integer
Minimum
value: 1
Maximum
value:
16383
60
FortiOS 8.0.0 CLI Reference
1222
Fortinet Inc.

<!-- 来源页 1223 -->
Parameter
Description
Type
Size
Default
rp-candidate-priority *
Router's priority as RP.
integer
Minimum
value: 0
Maximum
value: 255
192
static-group
*
Statically set IPv6 multicast groups to forward out.
string
Maximum
length: 35
* This parameter may not exist in some models.
config pim-sm-global
Parameter
Description
Type
Size
Default
bsr-allow-quick-refresh
*
Enable/disable accept BSR quick refresh packets
from neighbors.
option
-disable
Option
Description
enable
Allow BSR quick refresh packets.
disable
Do not BSR allow quick refresh packets.
bsr-candidate *
Enable/disable allowing this router to become a
bootstrap router (BSR).
option
-disable
Option
Description
enable
Allow this router to function as a BSR.
disable
Do not allow this router to function as a BSR.
bsr-hash *
BSR hash length (0 - 128, default = 126).
integer
Minimum
value: 0
Maximum
value: 128
126
bsr-interface
*
Interface to advertise as candidate BSR.
string
Maximum
length: 15
bsr-priority *
BSR priority (0 - 255, default = 0).
integer
Minimum
value: 0
Maximum
value: 255
0
cisco-crp-prefix *
Enable/disable making candidate RP compatible
with old Cisco IOS.
option
-disable
FortiOS 8.0.0 CLI Reference
1223
Fortinet Inc.

<!-- 来源页 1224 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Do not allow sending group prefix of zero.
disable
Allow sending group prefix of zero.
cisco-ignore-rp-set-priority *
Use only hash for RP selection (compatibility with
old Cisco IOS).
option
-disable
Option
Description
enable
Ignore RP-SET priority value.
disable
Do not ignore RP-SET priority value.
pim-use-sdwan
Enable/disable use of SDWAN when checking RPF
neighbor and sending of REG packet.
option
-disable
Option
Description
enable
Enable use of SDWAN when checking RPF neighbor and sending of REG
packet.
disable
Disable use of SDWAN when checking RPF neighbor and sending of REG
packet.
register-rate-limit
Limit of packets/sec per source registered through
this RP (0 means unlimited).
integer
Minimum
value: 0
Maximum
value:
65535
0
spt-threshold
*
Enable/disable switching to source specific trees.
option
-enable
Option
Description
enable
Switch to Source tree when available.
disable
Do not switch to Source tree when available.
spt-threshold-group *
Groups allowed to switch to source tree.
string
Maximum
length: 35
* This parameter may not exist in some models.
FortiOS 8.0.0 CLI Reference
1224
Fortinet Inc.

<!-- 来源页 1225 -->
config rp-address
Parameter
Description
Type
Size
Default
group *
Groups to use this RP.
string
Maximum
length: 35
id
ID of the entry.
integer
Minimum value:
0 Maximum
value:
4294967295
0
ip6-address
RP router IPv6 address.
ipv6-address
Not Specified
::
* This parameter may not exist in some models.
config pim-sm-global-vrf
Parameter
Description
Type
Size
Default
bsr-allow-quick-refresh
Enable/disable accept BSR quick refresh packets
from neighbors.
option
-disable
Option
Description
enable
Allow BSR quick refresh packets.
disable
Do not BSR allow quick refresh packets.
bsr-candidate
Enable/disable allowing this router to become a
bootstrap router (BSR).
option
-disable
Option
Description
enable
Allow this router to function as a BSR.
disable
Do not allow this router to function as a BSR.
bsr-hash
BSR hash length (0 - 128, default = 126).
integer
Minimum
value: 0
Maximum
value: 128
126
bsr-interface
Interface to advertise as candidate BSR.
string
Maximum
length: 15
bsr-priority
BSR priority (0 - 255, default = 0).
integer
Minimum
value: 0
Maximum
value: 255
0
FortiOS 8.0.0 CLI Reference
1225
Fortinet Inc.

<!-- 来源页 1226 -->
Parameter
Description
Type
Size
Default
cisco-crp-prefix
Enable/disable making candidate RP compatible
with old Cisco IOS.
option
-disable
Option
Description
enable
Do not allow sending group prefix of zero.
disable
Allow sending group prefix of zero.
vrf
VRF ID.
integer
Minimum
value: 1
Maximum
value: 511
442055907
**
** Values may differ between models.
config rp-address
Parameter
Description
Type
Size
Default
group
Groups to use this RP.
string
Maximum
length: 35
id
ID of the entry.
integer
Minimum value:
0 Maximum
value:
4294967295
0
ip6-address
RP router IPv6 address.
ipv6-address
Not Specified
::
FortiOS 8.0.0 CLI Reference
1226
Fortinet Inc.

<!-- 来源页 1227 -->
config router multicast6-flow
This command is available for model(s): FortiGate 1000D, FortiGate 1000F, FortiGate 1001F,
FortiGate 100F, FortiGate 101F Gen2, FortiGate 1100E, FortiGate 1101E, FortiGate 120G, FortiGate
121G, FortiGate 1800F, FortiGate 1801F, FortiGate 2000E, FortiGate 200E, FortiGate 200F, FortiGate
200G, FortiGate 201E, FortiGate 201F, FortiGate 201G, FortiGate 2200E, FortiGate 2201E, FortiGate
2500E, FortiGate 2600F, FortiGate 2601F, FortiGate 3000F, FortiGate 3001F, FortiGate 300E,
FortiGate 301E, FortiGate 30G, FortiGate 31G, FortiGate 3200F, FortiGate 3201F Gen2, FortiGate
3300E, FortiGate 3301E, FortiGate 3400E, FortiGate 3401E, FortiGate 3500F Gen2, FortiGate 3501F
Gen2, FortiGate 3600E, FortiGate 3601E, FortiGate 3700F, FortiGate 3701F, FortiGate 3960E,
FortiGate 3980E, FortiGate 400E Bypass, FortiGate 400E, FortiGate 400F, FortiGate 401E, FortiGate
401F, FortiGate 40F 3G4G, FortiGate 40F, FortiGate 4200F, FortiGate 4201F Gen2, FortiGate 4400F,
FortiGate 4401F Gen2, FortiGate 4800F, FortiGate 4801F, FortiGate 500E, FortiGate 501E, FortiGate
50G 5G, FortiGate 50G DSL, FortiGate 50G SFP-POE, FortiGate 50G SFP, FortiGate 50G, FortiGate
51G 5G, FortiGate 51G SFP-POE, FortiGate 51G, FortiGate 600E, FortiGate 600F, FortiGate 601E,
FortiGate 601F, FortiGate 60F, FortiGate 61F, FortiGate 70F, FortiGate 70G-POE, FortiGate 70G,
FortiGate 71F, FortiGate 71G-POE, FortiGate 71G, FortiGate 800D, FortiGate 80F Bypass, FortiGate
80F DSL, FortiGate 80F Gen2, FortiGate 80F-POE, FortiGate 81F Gen2, FortiGate 81F-POE, FortiGate
900D, FortiGate 900G, FortiGate 901G, FortiGate 90G Gen2, FortiGate 90G, FortiGate 91G Gen2,
FortiGate 91G, FortiGate-VM64 Aliyun, FortiGate-VM64 AWS, FortiGate-VM64 Azure, FortiGate-VM64 GCP, FortiGate-VM64 OPC, FortiGateRugged 50G 5G, FortiGateRugged 60F 3G4G,
FortiGateRugged 60F Gen2, FortiGateRugged 70F 3G4G, FortiGateRugged 70F, FortiGateRugged
70G 5G Dual, FortiGateRugged 70G, FortiWiFi 30G, FortiWiFi 31G, FortiWiFi 40F 3G4G, FortiWiFi 40F,
FortiWiFi 50G 5G, FortiWiFi 50G DSL, FortiWiFi 50G SFP, FortiWiFi 50G, FortiWiFi 51G, FortiWiFi 60F,
FortiWiFi 61F, FortiWiFi 70G-POE, FortiWiFi 70G, FortiWiFi 71G, FortiWiFi 80F 2R 3G4G DSL, FortiWiFi
80F 2R, FortiWiFi 81F 2R 3G4G DSL, FortiWiFi 81F 2R 3G4G-POE, FortiWiFi 81F 2R-POE, FortiWiFi 81F
2R.
It is not available for: FortiGate-VM64.
Configure IPv6 multicast-flow.
config router multicast6-flow
Description: Configure IPv6 multicast-flow.
edit <name>
set comments {string}
config flows
Description: IPv6 multicast-flow entries.
edit <id>
set group-addr {ipv6-address}
next
end
next
end
FortiOS 8.0.0 CLI Reference
1227
Fortinet Inc.

<!-- 来源页 1228 -->
config router multicast6-flow
Parameter
Description
Type
Size
Default
comments
Comment.
string
Maximum length:
127
name
Name.
string
Maximum length: 35
config flows
Parameter
Description
Type
Size
Default
group-addr
Multicast group IP address.
ipv6-address
Not Specified
::
id
Flow ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config router multicast-flow
Configure multicast-flow.
config router multicast-flow
Description: Configure multicast-flow.
edit <name>
set comments {string}
config flows
Description: Multicast-flow entries.
edit <id>
set group-addr {ipv4-address-any}
set source-addr {ipv4-address-any}
next
end
next
end
config router multicast-flow
Parameter
Description
Type
Size
Default
comments
Comment.
string
Maximum length:
127
name
Name.
string
Maximum length: 35
FortiOS 8.0.0 CLI Reference
1228
Fortinet Inc.

<!-- 来源页 1229 -->
config flows
Parameter
Description
Type
Size
Default
group-addr
Multicast group IP address.
ipv4-address-any
Not Specified
0.0.0.0
id
Flow ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
source-addr
Multicast source IP address.
ipv4-address-any
Not Specified
0.0.0.0
config router ospf
Configure OSPF.
config router ospf
Description: Configure OSPF.
set abr-type [cisco|ibm|...]
config area
Description: OSPF area configuration.
edit <id>
set authentication [none|text|...]
set comments {var-string}
set default-cost {integer}
config filter-list
Description: OSPF area filter-list configuration.
edit <id>
set direction [in|out]
set list {string}
next
end
set nssa-default-information-originate [enable|always|...]
set nssa-default-information-originate-metric {integer}
set nssa-default-information-originate-metric-type [1|2]
set nssa-redistribution [enable|disable]
set nssa-translator-role [candidate|never|...]
config range
Description: OSPF area range configuration.
edit <id>
set advertise [disable|enable]
set prefix {ipv4-classnet-any}
set substitute {ipv4-classnet-any}
set substitute-status [enable|disable]
next
FortiOS 8.0.0 CLI Reference
1229
Fortinet Inc.

<!-- 来源页 1230 -->
end
set shortcut [disable|enable|...]
set stub-type [no-summary|summary]
set type [regular|nssa|...]
config virtual-link
Description: OSPF virtual link configuration.
edit <name>
set authentication [none|text|...]
set authentication-key {password}
set dead-interval {integer}
set hello-interval {integer}
set keychain {string}
config md5-keys
Description: MD5 key.
edit <id>
set key-string {password}
next
end
set peer {ipv4-address-any}
set retransmit-interval {integer}
set transmit-delay {integer}
next
end
next
end
set auto-cost-ref-bandwidth {integer}
set bfd [enable|disable]
set database-overflow [enable|disable]
set database-overflow-max-lsas {integer}
set database-overflow-time-to-recover {integer}
set default-information-metric {integer}
set default-information-metric-type [1|2]
set default-information-originate [enable|always|...]
set default-information-route-map {string}
set default-metric {integer}
set distance {integer}
set distance-external {integer}
set distance-inter-area {integer}
set distance-intra-area {integer}
config distribute-list
Description: Distribute list configuration.
edit <id>
set access-list {string}
set protocol [connected|static|...]
next
end
set distribute-list-in {string}
set distribute-route-map-in {string}
set log-neighbour-changes [enable|disable]
set lsa-refresh-interval {integer}
config neighbor
Description: OSPF neighbor configuration are used when OSPF runs on non-broadcast media.
FortiOS 8.0.0 CLI Reference
1230
Fortinet Inc.

<!-- 来源页 1231 -->
edit <id>
set cost {integer}
set ip {ipv4-address}
set poll-interval {integer}
set priority {integer}
next
end
config network
Description: OSPF network configuration.
edit <id>
set area {ipv4-address-any}
set comments {var-string}
set prefix {ipv4-classnet}
next
end
config ospf-interface
Description: OSPF interface configuration.
edit <name>
set authentication [none|text|...]
set authentication-key {password}
set bfd [global|enable|...]
set comments {var-string}
set cost {integer}
set database-filter-out [enable|disable]
set dead-interval {integer}
set hello-interval {integer}
set hello-multiplier {integer}
set interface {string}
set ip {ipv4-address}
set keychain {string}
set linkdown-fast-failover [enable|disable]
config md5-keys
Description: MD5 key.
edit <id>
set key-string {password}
next
end
set mtu {integer}
set mtu-ignore [enable|disable]
set network-type [broadcast|non-broadcast|...]
set prefix-length {integer}
set priority {integer}
set resync-timeout {integer}
set retransmit-interval {integer}
set status [disable|enable]
set transmit-delay {integer}
next
end
set passive-interface <name1>, <name2>, ...
config redistribute
Description: Redistribute configuration. Read-only.
edit <name>
FortiOS 8.0.0 CLI Reference
1231
Fortinet Inc.

<!-- 来源页 1232 -->
set metric {integer}
set metric-type [1|2]
set routemap {string}
set status [enable|disable]
set tag {integer}
next
end
set restart-mode [none|lls|...]
set restart-on-topology-change [enable|disable]
set restart-period {integer}
set rfc1583-compatible [enable|disable]
set router-id {ipv4-address-any}
set spf-timers {user}
config summary-address
Description: IP address summary configuration.
edit <id>
set advertise [disable|enable]
set prefix {ipv4-classnet}
set tag {integer}
next
end
end
config router ospf
Parameter
Description
Type
Size
Default
abr-type
Area border router type.
option
-standard
Option
Description
cisco
Cisco.
ibm
IBM.
shortcut
Shortcut.
standard
Standard.
auto-cost-ref-bandwidth
Reference bandwidth in terms of megabits per
second.
integer
Minimum value:
1 Maximum
value: 1000000
1000
bfd
Bidirectional Forwarding Detection (BFD).
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
1232
Fortinet Inc.

<!-- 来源页 1233 -->
Parameter
Description
Type
Size
Default
database-overflow
Enable/disable database overflow.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
database-overflow-max-lsas
Database overflow maximum LSAs.
integer
Minimum value:
0 Maximum
value:
4294967295
10000
database-overflow-time-to-recover
Database overflow time to recover (sec).
integer
Minimum value:
0 Maximum
value: 65535
300
default-information-metric
Default information metric.
integer
Minimum value:
1 Maximum
value:
16777214
10
default-information-metric-type
Default information metric type.
option
-2
Option
Description
1
Type 1.
2
Type 2.
default-information-originate
Enable/disable generation of default route.
option
-disable
Option
Description
enable
Enable setting.
always
Always advertise the default route.
disable
Disable setting.
default-information-route-map
Default information route map.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
1233
Fortinet Inc.

<!-- 来源页 1234 -->
Parameter
Description
Type
Size
Default
default-metric
Default metric of redistribute routes.
integer
Minimum value:
1 Maximum
value:
16777214
10
distance
Distance of the route.
integer
Minimum value:
1 Maximum
value: 255
110
distance-external
Administrative external distance.
integer
Minimum value:
1 Maximum
value: 255
110
distance-inter-area
Administrative inter-area distance.
integer
Minimum value:
1 Maximum
value: 255
110
distance-intra-area
Administrative intra-area distance.
integer
Minimum value:
1 Maximum
value: 255
110
distribute-list-in
Filter incoming routes.
string
Maximum
length: 35
distribute-route-map-in
Filter incoming external routes by route-map.
string
Maximum
length: 35
log-neighbour-changes
Log of OSPF neighbor changes.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
lsa-refresh-interval
The minimal OSPF LSA update time interval.
integer
Minimum value:
0 Maximum
value: 5
5
passive-interface
<name>
Passive interface configuration.
Passive interface name.
string
Maximum
length: 79
restart-mode
OSPF restart mode (graceful or LLS).
option
-none
Option
Description
none
Hitless restart disabled.
lls
LLS mode.
FortiOS 8.0.0 CLI Reference
1234
Fortinet Inc.

<!-- 来源页 1235 -->
Parameter
Description
Type
Size
Default
Option
Description
graceful-restart
Graceful Restart Mode.
restart-on-topology-change
Enable/disable continuing graceful restart
upon topology change.
option
-disable
Option
Description
enable
Continue graceful restart upon topology change.
disable
Exit graceful restart upon topology change.
restart-period
Graceful restart period.
integer
Minimum value:
1 Maximum
value: 3600
120
rfc1583-compatible
Enable/disable RFC1583 compatibility.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
router-id
Router ID.
ipv4-address-any
Not Specified
0.0.0.0
spf-timers
SPF calculation frequency.
user
Not Specified
config area
Parameter
Description
Type
Size
Default
authentication
Authentication type.
option
-none
Option
Description
none
None.
text
Text.
message-digest
Message digest.
comments
Comment.
var-string
Maximum
length: 255
FortiOS 8.0.0 CLI Reference
1235
Fortinet Inc.

<!-- 来源页 1236 -->
Parameter
Description
Type
Size
Default
default-cost
Summary default cost of stub or NSSA
area.
integer
Minimum value:
0 Maximum
value:
4294967295
10
id
Area entry IP address.
ipv4-address-any
Not Specified
0.0.0.0
nssa-default-information-originate
Redistribute, advertise, or do not originate
Type-7 default route into NSSA area.
option
-disable
Option
Description
enable
Redistribute Type-7 default route from routing table.
always
Advertise a self-originated Type-7 default route.
disable
Do not advertise Type-7 default route.
nssa-default-information-originate-metric
OSPF default metric.
integer
Minimum value:
0 Maximum
value:
16777214
10
nssa-default-information-originate-metric-type
OSPF metric type for default routes.
option
-2
Option
Description
1
Type 1.
2
Type 2.
nssa-redistribution
Enable/disable redistribute into NSSA area.
option
-enable
Option
Description
enable
Enable redistribute into NSSA area.
disable
Disable redistribute into NSSA area.
nssa-translator-role
NSSA translator role type.
option
-candidate
FortiOS 8.0.0 CLI Reference
1236
Fortinet Inc.

<!-- 来源页 1237 -->
Parameter
Description
Type
Size
Default
Option
Description
candidate
Candidate.
never
Never.
always
Always.
shortcut
Enable/disable shortcut option.
option
-disable
Option
Description
disable
Disable shortcut option.
enable
Enable shortcut option.
default
Default shortcut option.
stub-type
Stub summary setting.
option
-summary
Option
Description
no-summary
No summary.
summary
Summary.
type
Area type setting.
option
-regular
Option
Description
regular
Regular.
nssa
NSSA.
stub
Stub.
config filter-list
Parameter
Description
Type
Size
Default
direction
Direction.
option
-out
Option
Description
in
In.
out
Out.
id
Filter list entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
list
Access-list or prefix-list name.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
1237
Fortinet Inc.

<!-- 来源页 1238 -->
config range
Parameter
Description
Type
Size
Default
advertise
Enable/disable advertise status.
option
-enable
Option
Description
disable
Disable advertise status.
enable
Enable advertise status.
id
Range entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
prefix
Prefix.
ipv4-classnet-any
Not Specified
0.0.0.0
0.0.0.0
substitute
Substitute prefix.
ipv4-classnet-any
Not Specified
0.0.0.0
0.0.0.0
substitute-status
Enable/disable substitute status.
option
-disable
Option
Description
enable
Enable substitute status.
disable
Disable substitute status.
config virtual-link
Parameter
Description
Type
Size
Default
authentication
Authentication type.
option
-none
Option
Description
none
None.
text
Text.
message-digest
Message digest.
authentication-key
Authentication key.
password
Not
Specified
FortiOS 8.0.0 CLI Reference
1238
Fortinet Inc.

<!-- 来源页 1239 -->
Parameter
Description
Type
Size
Default
dead-interval
Dead interval.
integer
Minimum
value: 1
Maximum
value:
65535
40
hello-interval
Hello interval.
integer
Minimum
value: 1
Maximum
value:
65535
10
keychain
Message-digest key-chain name.
string
Maximum
length: 35
name
Virtual link entry name.
string
Maximum
length: 35
peer
Peer IP.
ipv4-address-any
Not
Specified
0.0.0.0
retransmit-interval
Retransmit interval.
integer
Minimum
value: 1
Maximum
value:
65535
5
transmit-delay
Transmit delay.
integer
Minimum
value: 1
Maximum
value:
65535
1
config md5-keys
Parameter
Description
Type
Size
Default
id
Key ID (1 - 255).
integer
Minimum
value: 1
Maximum
value: 255
0
key-string
Password for the key.
password
Not
Specified
FortiOS 8.0.0 CLI Reference
1239
Fortinet Inc.

<!-- 来源页 1240 -->
config distribute-list
Parameter
Description
Type
Size
Default
access-list
Access list name.
string
Maximum
length: 35
id
Distribute list entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
protocol
Protocol type.
option
-connected
Option
Description
connected
Connected type.
static
Static type.
rip
RIP type.
config neighbor
Parameter
Description
Type
Size
Default
cost
Cost of the interface, value range from 0 to
65535, 0 means auto-cost.
integer
Minimum value:
0 Maximum
value: 65535
0
id
Neighbor entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
ip
Interface IP address of the neighbor.
ipv4-address
Not Specified
0.0.0.0
poll-interval
Poll interval time in seconds.
integer
Minimum value:
1 Maximum
value: 65535
10
priority
Priority.
integer
Minimum value:
0 Maximum
value: 255
1
FortiOS 8.0.0 CLI Reference
1240
Fortinet Inc.

<!-- 来源页 1241 -->
config network
Parameter
Description
Type
Size
Default
area
Attach the network to area.
ipv4-address-any
Not Specified
0.0.0.0
comments
Comment.
var-string
Maximum
length: 255
id
Network entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
prefix
Prefix.
ipv4-classnet
Not Specified
0.0.0.0
0.0.0.0
config ospf-interface
Parameter
Description
Type
Size
Default
authentication
Authentication type.
option
-none
Option
Description
none
None.
text
Text.
message-digest
Message digest.
authentication-key
Authentication key.
password
Not
Specified
bfd
Bidirectional Forwarding Detection (BFD).
option
-global
Option
Description
global
Follow global configuration.
enable
Enable BFD on this interface.
disable
Disable BFD on this interface.
comments
Comment.
var-string
Maximum
length: 255
FortiOS 8.0.0 CLI Reference
1241
Fortinet Inc.

<!-- 来源页 1242 -->
Parameter
Description
Type
Size
Default
cost
Cost of the interface, value range from 0 to
65535, 0 means auto-cost.
integer
Minimum
value: 0
Maximum
value:
65535
0
database-filter-out
Enable/disable control of flooding out LSAs.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
dead-interval
Dead interval.
integer
Minimum
value: 0
Maximum
value:
65535
0
hello-interval
Hello interval.
integer
Minimum
value: 0
Maximum
value:
65535
0
hello-multiplier
Number of hello packets within dead interval.
integer
Minimum
value: 3
Maximum
value: 10
0
interface
Configuration interface name.
string
Maximum
length: 15
ip
IP address.
ipv4-address
Not
Specified
0.0.0.0
keychain
Message-digest key-chain name.
string
Maximum
length: 35
linkdown-fast-failover
Enable/disable fast link failover.
option
-disable
Option
Description
enable
Enable fast failover for VLAN interfaces.
disable
Disable fast failover for VLAN interfaces.
FortiOS 8.0.0 CLI Reference
1242
Fortinet Inc.

<!-- 来源页 1243 -->
Parameter
Description
Type
Size
Default
mtu
MTU for database description packets.
integer
Minimum
value: 576
Maximum
value:
65535
0
mtu-ignore
Enable/disable ignore MTU.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
name
Interface entry name.
string
Maximum
length: 35
network-type
Network type.
option
-broadcast
Option
Description
broadcast
Broadcast.
non-broadcast
Non-broadcast.
point-to-point
Point-to-point.
point-to-multipoint
Point-to-multipoint.
point-to-multipoint-non-broadcast
Point-to-multipoint and non-broadcast.
prefix-length
Prefix length.
integer
Minimum
value: 0
Maximum
value: 32
0
priority
Priority.
integer
Minimum
value: 0
Maximum
value: 255
1
resync-timeout
Graceful restart neighbor resynchronization
timeout.
integer
Minimum
value: 1
Maximum
value: 3600
40
FortiOS 8.0.0 CLI Reference
1243
Fortinet Inc.

<!-- 来源页 1244 -->
Parameter
Description
Type
Size
Default
retransmit-interval
Retransmit interval.
integer
Minimum
value: 1
Maximum
value:
65535
5
status
Enable/disable status.
option
-enable
Option
Description
disable
Disable status.
enable
Enable status.
transmit-delay
Transmit delay.
integer
Minimum
value: 1
Maximum
value:
65535
1
config md5-keys
Parameter
Description
Type
Size
Default
id
Key ID (1 - 255).
integer
Minimum
value: 1
Maximum
value: 255
0
key-string
Password for the key.
password
Not
Specified
config redistribute
Parameter
Description
Type
Size
Default
metric
Redistribute metric setting.
integer
Minimum value:
0 Maximum
value:
16777214
0
metric-type
Metric type.
option
-2
Option
Description
1
Type 1.
2
Type 2.
FortiOS 8.0.0 CLI Reference
1244
Fortinet Inc.

<!-- 来源页 1245 -->
Parameter
Description
Type
Size
Default
name
Redistribute name.
string
Maximum
length: 35
routemap
Route map name.
string
Maximum
length: 35
status
Status.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
tag
Tag value.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config summary-address
Parameter
Description
Type
Size
Default
advertise
Enable/disable advertise status.
option
-enable
Option
Description
disable
Disable advertise status.
enable
Enable advertise status.
id
Summary address entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
prefix
Prefix.
ipv4-classnet
Not Specified
0.0.0.0
0.0.0.0
tag
Tag value.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config router ospf6
Configure IPv6 OSPF.
config router ospf6
Description: Configure IPv6 OSPF.
FortiOS 8.0.0 CLI Reference
1245
Fortinet Inc.

<!-- 来源页 1246 -->
set abr-type [cisco|ibm|...]
config area
Description: OSPF6 area configuration.
edit <id>
set authentication [none|ah|...]
set default-cost {integer}
set ipsec-auth-alg [md5|sha1|...]
set ipsec-enc-alg [null|des|...]
config ipsec-keys
Description: IPsec authentication and encryption keys.
edit <spi>
set auth-key {password}
set enc-key {password}
next
end
set key-rollover-interval {integer}
set nssa-default-information-originate [enable|disable]
set nssa-default-information-originate-metric {integer}
set nssa-default-information-originate-metric-type [1|2]
set nssa-redistribution [enable|disable]
set nssa-translator-role [candidate|never|...]
config range
Description: OSPF6 area range configuration.
edit <id>
set advertise [disable|enable]
set prefix6 {ipv6-network}
next
end
set stub-type [no-summary|summary]
set type [regular|nssa|...]
config virtual-link
Description: OSPF6 virtual link configuration.
edit <name>
set authentication [none|ah|...]
set dead-interval {integer}
set hello-interval {integer}
set ipsec-auth-alg [md5|sha1|...]
set ipsec-enc-alg [null|des|...]
config ipsec-keys
Description: IPsec authentication and encryption keys.
edit <spi>
set auth-key {password}
set enc-key {password}
next
end
set key-rollover-interval {integer}
set peer {ipv4-address-any}
set retransmit-interval {integer}
set transmit-delay {integer}
next
end
next
FortiOS 8.0.0 CLI Reference
1246
Fortinet Inc.

<!-- 来源页 1247 -->
end
set auto-cost-ref-bandwidth {integer}
set bfd [enable|disable]
set default-information-metric {integer}
set default-information-metric-type [1|2]
set default-information-originate [enable|always|...]
set default-information-route-map {string}
set default-metric {integer}
set log-neighbour-changes [enable|disable]
config ospf6-interface
Description: OSPF6 interface configuration.
edit <name>
set area-id {ipv4-address-any}
set authentication [none|ah|...]
set bfd [global|enable|...]
set cost {integer}
set dead-interval {integer}
set hello-interval {integer}
set interface {string}
set ipsec-auth-alg [md5|sha1|...]
set ipsec-enc-alg [null|des|...]
config ipsec-keys
Description: IPsec authentication and encryption keys.
edit <spi>
set auth-key {password}
set enc-key {password}
next
end
set key-rollover-interval {integer}
set mtu {integer}
set mtu-ignore [enable|disable]
config neighbor
Description: OSPFv3 neighbors are used when OSPFv3 runs on non-broadcast media.
edit <ip6>
set cost {integer}
set poll-interval {integer}
set priority {integer}
next
end
set network-type [broadcast|point-to-point|...]
set priority {integer}
set retransmit-interval {integer}
set status [disable|enable]
set transmit-delay {integer}
next
end
set passive-interface <name1>, <name2>, ...
config redistribute
Description: Redistribute configuration. Read-only.
edit <name>
set metric {integer}
set metric-type [1|2]
FortiOS 8.0.0 CLI Reference
1247
Fortinet Inc.

<!-- 来源页 1248 -->
set routemap {string}
set status [enable|disable]
next
end
set restart-mode [none|graceful-restart]
set restart-on-topology-change [enable|disable]
set restart-period {integer}
set router-id {ipv4-address-any}
set spf-timers {user}
config summary-address
Description: IPv6 address summary configuration.
edit <id>
set advertise [disable|enable]
set prefix6 {ipv6-network}
set tag {integer}
next
end
end
config router ospf6
Parameter
Description
Type
Size
Default
abr-type
Area border router type.
option
-standard
Option
Description
cisco
Cisco.
ibm
IBM.
standard
Standard.
auto-cost-ref-bandwidth
Reference bandwidth in terms of megabits per
second.
integer
Minimum
value: 1
Maximum
value:
1000000
1000
bfd
Enable/disable Bidirectional Forwarding Detection
(BFD).
option
-disable
Option
Description
enable
Enable Bidirectional Forwarding Detection (BFD).
disable
Disable Bidirectional Forwarding Detection (BFD).
FortiOS 8.0.0 CLI Reference
1248
Fortinet Inc.

<!-- 来源页 1249 -->
Parameter
Description
Type
Size
Default
default-information-metric
Default information metric.
integer
Minimum
value: 1
Maximum
value:
16777214
10
default-information-metric-type
Default information metric type.
option
-2
Option
Description
1
Type 1.
2
Type 2.
default-information-originate
Enable/disable generation of default route.
option
-disable
Option
Description
enable
Enable setting.
always
Always advertise the default route.
disable
Disable setting.
default-information-route-map
Default information route map.
string
Maximum
length: 35
default-metric
Default metric of redistribute routes.
integer
Minimum
value: 1
Maximum
value:
16777214
10
log-neighbour-changes
Log OSPFv3 neighbor changes.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
passive-interface
<name>
Passive interface configuration.
Passive interface name.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
1249
Fortinet Inc.

<!-- 来源页 1250 -->
Parameter
Description
Type
Size
Default
restart-mode
OSPFv3 restart mode (graceful or none).
option
-none
Option
Description
none
Disable hitless restart.
graceful-restart
Enable graceful restart mode.
restart-on-topology-change
Enable/disable continuing graceful restart upon
topology change.
option
-disable
Option
Description
enable
Continue graceful restart upon topology change.
disable
Exit graceful restart upon topology change.
restart-period
Graceful restart period in seconds.
integer
Minimum
value: 1
Maximum
value: 3600
120
router-id
A.B.C.D, in IPv4 address format.
ipv4-address-any
Not
Specified
0.0.0.0
spf-timers
SPF calculation frequency.
user
Not
Specified
config area
Parameter
Description
Type
Size
Default
authentication
Authentication mode.
option
-none
Option
Description
none
Disable authentication.
ah
Authentication Header.
esp
Encapsulating Security Payload.
default-cost
Summary default cost of stub or NSSA area.
integer
Minimum
value: 0
Maximum
value:
16777215
10
FortiOS 8.0.0 CLI Reference
1250
Fortinet Inc.

<!-- 来源页 1251 -->
Parameter
Description
Type
Size
Default
id
Area entry IP address.
ipv4-address-any
Not
Specified
0.0.0.0
ipsec-auth-alg
Authentication algorithm.
option
-md5
Option
Description
md5
MD5.
sha1
SHA1.
sha256
SHA256.
sha384
SHA384.
sha512
SHA512.
ipsec-enc-alg
Encryption algorithm.
option
-null
Option
Description
null
No encryption.
des
DES.
3des
3DES.
aes128
AES128.
aes192
AES192.
aes256
AES256.
key-rollover-interval
Key roll-over interval.
integer
Minimum
value: 300
Maximum
value:
216000
300
nssa-default-information-originate
Enable/disable originate type 7 default into
NSSA area.
option
-disable
Option
Description
enable
Enable originate type 7 default into NSSA area.
disable
Disable originate type 7 default into NSSA area.
nssa-default-information-originate-metric
OSPFv3 default metric.
integer
Minimum
value: 0
Maximum
value:
16777214
10
FortiOS 8.0.0 CLI Reference
1251
Fortinet Inc.

<!-- 来源页 1252 -->
Parameter
Description
Type
Size
Default
nssa-default-information-originate-metric-type
OSPFv3 metric type for default routes.
option
-2
Option
Description
1
Type 1.
2
Type 2.
nssa-redistribution
Enable/disable redistribute into NSSA area.
option
-enable
Option
Description
enable
Enable redistribute into NSSA area.
disable
Disable redistribute into NSSA area.
nssa-translator-role
NSSA translator role type.
option
-candidate
Option
Description
candidate
Candidate.
never
Never.
always
Always.
stub-type
Stub summary setting.
option
-summary
Option
Description
no-summary
No summary.
summary
Summary.
type
Area type setting.
option
-regular
Option
Description
regular
Regular.
nssa
NSSA.
stub
Stub.
FortiOS 8.0.0 CLI Reference
1252
Fortinet Inc.

<!-- 来源页 1253 -->
config ipsec-keys
Parameter
Description
Type
Size
Default
auth-key
Authentication key.
password
Not Specified
enc-key
Encryption key.
password
Not Specified
spi
Security Parameters Index.
integer
Minimum value:
256 Maximum
value:
4294967295
0
config range
Parameter
Description
Type
Size
Default
advertise
Enable/disable advertise status.
option
-enable
Option
Description
disable
disable
enable
enable
id
Range entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
prefix6
IPv6 prefix.
ipv6-network
Not Specified
::/0
config virtual-link
Parameter
Description
Type
Size
Default
authentication
Authentication mode.
option
-area
Option
Description
none
Disable authentication.
ah
Authentication Header.
esp
Encapsulating Security Payload.
area
Use the routing area's authentication configuration.
FortiOS 8.0.0 CLI Reference
1253
Fortinet Inc.

<!-- 来源页 1254 -->
Parameter
Description
Type
Size
Default
dead-interval
Dead interval.
integer
Minimum
value: 1
Maximum
value:
65535
40
hello-interval
Hello interval.
integer
Minimum
value: 1
Maximum
value:
65535
10
ipsec-auth-alg
Authentication algorithm.
option
-md5
Option
Description
md5
MD5.
sha1
SHA1.
sha256
SHA256.
sha384
SHA384.
sha512
SHA512.
ipsec-enc-alg
Encryption algorithm.
option
-null
Option
Description
null
No encryption.
des
DES.
3des
3DES.
aes128
AES128.
aes192
AES192.
aes256
AES256.
key-rollover-interval
Key roll-over interval.
integer
Minimum
value: 300
Maximum
value:
216000
300
name
Virtual link entry name.
string
Maximum
length: 35
peer
A.B.C.D, peer router ID.
ipv4-address-any
Not
Specified
0.0.0.0
FortiOS 8.0.0 CLI Reference
1254
Fortinet Inc.

<!-- 来源页 1255 -->
Parameter
Description
Type
Size
Default
retransmit-interval
Retransmit interval.
integer
Minimum
value: 1
Maximum
value:
65535
5
transmit-delay
Transmit delay.
integer
Minimum
value: 1
Maximum
value:
65535
1
config ipsec-keys
Parameter
Description
Type
Size
Default
auth-key
Authentication key.
password
Not Specified
enc-key
Encryption key.
password
Not Specified
spi
Security Parameters Index.
integer
Minimum value:
256 Maximum
value:
4294967295
0
config ospf6-interface
Parameter
Description
Type
Size
Default
area-id
A.B.C.D, in IPv4 address format.
ipv4-address-any
Not
Specified
0.0.0.0
authentication
Authentication mode.
option
-area
Option
Description
none
Disable authentication.
ah
Authentication Header.
esp
Encapsulating Security Payload.
area
Use the routing area's authentication configuration.
bfd
Enable/disable Bidirectional Forwarding
Detection (BFD).
option
-global
FortiOS 8.0.0 CLI Reference
1255
Fortinet Inc.

<!-- 来源页 1256 -->
Parameter
Description
Type
Size
Default
Option
Description
global
Use global configuration of Bidirectional Forwarding Detection (BFD).
enable
Enable Bidirectional Forwarding Detection (BFD) on this interface.
disable
Disable Bidirectional Forwarding Detection (BFD) on this interface.
cost
Cost of the interface, value range from 0 to
65535, 0 means auto-cost.
integer
Minimum
value: 0
Maximum
value:
65535
0
dead-interval
Dead interval.
integer
Minimum
value: 1
Maximum
value:
65535
0
hello-interval
Hello interval.
integer
Minimum
value: 1
Maximum
value:
65535
0
interface
Configuration interface name.
string
Maximum
length: 15
ipsec-auth-alg
Authentication algorithm.
option
-md5
Option
Description
md5
MD5.
sha1
SHA1.
sha256
SHA256.
sha384
SHA384.
sha512
SHA512.
ipsec-enc-alg
Encryption algorithm.
option
-null
Option
Description
null
No encryption.
des
DES.
3des
3DES.
aes128
AES128.
FortiOS 8.0.0 CLI Reference
1256
Fortinet Inc.

<!-- 来源页 1257 -->
Parameter
Description
Type
Size
Default
Option
Description
aes192
AES192.
aes256
AES256.
key-rollover-interval
Key roll-over interval.
integer
Minimum
value: 300
Maximum
value:
216000
300
mtu
MTU for OSPFv3 packets.
integer
Minimum
value: 576
Maximum
value:
65535
0
mtu-ignore
Enable/disable ignoring MTU field in DBD
packets.
option
-disable
Option
Description
enable
Ignore MTU field in DBD packets.
disable
Do not ignore MTU field in DBD packets.
name
Interface entry name.
string
Maximum
length: 35
network-type
Network type.
option
-broadcast
Option
Description
broadcast
broadcast
point-to-point
point-to-point
non-broadcast
non-broadcast
point-to-multipoint
point-to-multipoint
point-to-multipoint-non-broadcast
point-to-multipoint and non-broadcast.
priority
Priority.
integer
Minimum
value: 0
Maximum
value: 255
1
FortiOS 8.0.0 CLI Reference
1257
Fortinet Inc.

<!-- 来源页 1258 -->
Parameter
Description
Type
Size
Default
retransmit-interval
Retransmit interval.
integer
Minimum
value: 1
Maximum
value:
65535
5
status
Enable/disable OSPF6 routing on this
interface.
option
-enable
Option
Description
disable
Disable OSPF6 routing.
enable
Enable OSPF6 routing.
transmit-delay
Transmit delay.
integer
Minimum
value: 1
Maximum
value:
65535
1
config ipsec-keys
Parameter
Description
Type
Size
Default
auth-key
Authentication key.
password
Not Specified
enc-key
Encryption key.
password
Not Specified
spi
Security Parameters Index.
integer
Minimum value:
256 Maximum
value:
4294967295
0
config neighbor
Parameter
Description
Type
Size
Default
cost
Cost of the interface, value range from 0 to 65535,
0 means auto-cost.
integer
Minimum
value: 0
Maximum
value:
65535
0
ip6
IPv6 link local address of the neighbor.
ipv6-address
Not
Specified
::
FortiOS 8.0.0 CLI Reference
1258
Fortinet Inc.

<!-- 来源页 1259 -->
Parameter
Description
Type
Size
Default
poll-interval
Poll interval time in seconds.
integer
Minimum
value: 1
Maximum
value:
65535
10
priority
Priority.
integer
Minimum
value: 0
Maximum
value: 255
1
config redistribute
Parameter
Description
Type
Size
Default
metric
Redistribute metric setting.
integer
Minimum
value: 0
Maximum
value:
16777214
0
metric-type
Metric type.
option
-2
Option
Description
1
Type 1.
2
Type 2.
name
Redistribute name.
string
Maximum
length: 35
routemap
Route map name.
string
Maximum
length: 35
status
Status.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
config summary-address
Parameter
Description
Type
Size
Default
advertise
Enable/disable advertise status.
option
-enable
FortiOS 8.0.0 CLI Reference
1259
Fortinet Inc.

<!-- 来源页 1260 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
disable
enable
enable
id
Summary address entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
prefix6
IPv6 prefix.
ipv6-network
Not Specified
::/0
tag
Tag value.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config router policy
Configure IPv4 routing policies.
config router policy
Description: Configure IPv4 routing policies.
edit <seq-num>
set action [deny|permit]
set comments {var-string}
set dst <subnet1>, <subnet2>, ...
set dst-negate [enable|disable]
set dstaddr <name1>, <name2>, ...
set end-port {integer}
set end-source-port {integer}
set gateway {ipv4-address}
set groups <name1>, <name2>, ...
set input-device <name1>, <name2>, ...
set input-device-negate [enable|disable]
set internet-service-custom <name1>, <name2>, ...
set internet-service-fortiguard <name1>, <name2>, ...
set internet-service-id <id1>, <id2>, ...
set output-device {string}
set protocol {integer}
set src <subnet1>, <subnet2>, ...
set src-negate [enable|disable]
set srcaddr <name1>, <name2>, ...
set start-port {integer}
set start-source-port {integer}
set status [enable|disable]
set tos {user}
FortiOS 8.0.0 CLI Reference
1260
Fortinet Inc.

<!-- 来源页 1261 -->
set tos-mask {user}
set users <name1>, <name2>, ...
next
end
config router policy
Parameter
Description
Type
Size
Default
action
Action of the policy route.
option
-permit
Option
Description
deny
Do not search policy route table.
permit
Use this policy route for forwarding.
comments
Optional comments.
var-string
Maximum
length: 255
dst <subnet>
Destination IP and mask (x.x.x.x/x).
IP and mask.
string
Maximum
length: 79
dst-negate
Enable/disable negation of destination address
match.
option
-disable
Option
Description
enable
Enable destination address negation.
disable
Disable destination address negation.
dstaddr
<name>
Destination address name.
Address/group name.
string
Maximum
length: 79
end-port
End destination port number (0 - 65535).
integer
Minimum value:
0 Maximum
value: 65535
65535
end-source-port
End source port number (0 - 65535).
integer
Minimum value:
0 Maximum
value: 65535
65535
gateway
IP address of the gateway.
ipv4-address
Not Specified
0.0.0.0
groups
<name>
List of user groups.
Group name.
string
Maximum
length: 79
input-device
<name>
Incoming interface name.
Interface name.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
1261
Fortinet Inc.

<!-- 来源页 1262 -->
Parameter
Description
Type
Size
Default
input-device-negate
Enable/disable negation of input device match.
option
-disable
Option
Description
enable
Enable negation of input device match.
disable
Disable negation of input device match.
internet-service-custom
<name>
Custom Destination Internet Service name.
Custom Destination Internet Service name.
string
Maximum
length: 79
internet-service-fortiguard
<name>
FortiGuard Destination Internet Service name.
FortiGuard Destination Internet Service name.
string
Maximum
length: 79
internet-service-id
<id>
Destination Internet Service ID.
Destination Internet Service ID.
integer
Minimum value:
0 Maximum
value:
4294967295
output-device
Outgoing interface name.
string
Maximum
length: 35
protocol
Protocol number (0 - 255).
integer
Minimum value:
0 Maximum
value: 255
0
seq-num
Sequence number(1-65535).
integer
Minimum value:
1 Maximum
value: 65535
0
src <subnet>
Source IP and mask (x.x.x.x/x).
IP and mask.
string
Maximum
length: 79
src-negate
Enable/disable negation of source address
match.
option
-disable
Option
Description
enable
Enable source address negation.
disable
Disable source address negation.
srcaddr
<name>
Source address name.
Address/group name.
string
Maximum
length: 79
start-port
Start destination port number (0 - 65535).
integer
Minimum value:
0 Maximum
value: 65535
0
FortiOS 8.0.0 CLI Reference
1262
Fortinet Inc.

<!-- 来源页 1263 -->
Parameter
Description
Type
Size
Default
start-source-port
Start source port number (0 - 65535).
integer
Minimum value:
0 Maximum
value: 65535
0
status
Enable/disable this policy route.
option
-enable
Option
Description
enable
Enable this policy route.
disable
Disable this policy route.
tos
Type of service bit pattern.
user
Not Specified
tos-mask
Type of service evaluated bits.
user
Not Specified
users <name>
List of users.
User name.
string
Maximum
length: 79
config router policy6
Configure IPv6 routing policies.
config router policy6
Description: Configure IPv6 routing policies.
edit <seq-num>
set action [deny|permit]
set comments {var-string}
set dst <addr61>, <addr62>, ...
set dst-negate [enable|disable]
set dstaddr <name1>, <name2>, ...
set end-port {integer}
set end-source-port {integer}
set gateway {ipv6-address}
set groups <name1>, <name2>, ...
set input-device <name1>, <name2>, ...
set input-device-negate [enable|disable]
set internet-service-custom <name1>, <name2>, ...
set internet-service-fortiguard <name1>, <name2>, ...
set internet-service-id <id1>, <id2>, ...
set output-device {string}
set protocol {integer}
set src <addr61>, <addr62>, ...
set src-negate [enable|disable]
set srcaddr <name1>, <name2>, ...
set start-port {integer}
set start-source-port {integer}
set status [enable|disable]
set tos {user}
set tos-mask {user}
FortiOS 8.0.0 CLI Reference
1263
Fortinet Inc.

<!-- 来源页 1264 -->
set users <name1>, <name2>, ...
next
end
config router policy6
Parameter
Description
Type
Size
Default
action
Action of the policy route.
option
-permit
Option
Description
deny
Do not search policy route table.
permit
Use this policy route for forwarding.
comments
Optional comments.
var-string
Maximum
length: 255
dst <addr6>
Destination IPv6 prefix.
IPv6 address prefix.
string
Maximum
length: 79
dst-negate
Enable/disable negating destination address
match.
option
-disable
Option
Description
enable
Enable destination address negation.
disable
Disable destination address negation.
dstaddr
<name>
Destination address name.
Address/group name.
string
Maximum
length: 79
end-port
End destination port number (1 - 65535).
integer
Minimum value:
1 Maximum
value: 65535
65535
end-source-port
End source port number (1 - 65535).
integer
Minimum value:
1 Maximum
value: 65535
65535
gateway
IPv6 address of the gateway.
ipv6-address
Not Specified
::
groups
<name>
List of user groups.
Group name.
string
Maximum
length: 79
input-device
<name>
Incoming interface name.
Interface name.
string
Maximum
length: 79
input-device-negate
Enable/disable negation of input device match.
option
-disable
FortiOS 8.0.0 CLI Reference
1264
Fortinet Inc.

<!-- 来源页 1265 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable negation of input device match.
disable
Disable negation of input device match.
internet-service-custom
<name>
Custom Destination Internet Service name.
Custom Destination Internet Service name.
string
Maximum
length: 79
internet-service-fortiguard
<name>
FortiGuard Destination Internet Service name.
FortiGuard Destination Internet Service name.
string
Maximum
length: 79
internet-service-id
<id>
Destination Internet Service ID.
Destination Internet Service ID.
integer
Minimum value:
0 Maximum
value:
4294967295
output-device
Outgoing interface name.
string
Maximum
length: 35
protocol
Protocol number (0 - 255).
integer
Minimum value:
0 Maximum
value: 255
0
seq-num
Sequence number(1-65535).
integer
Minimum value:
1 Maximum
value: 65535
0
src <addr6>
Source IPv6 prefix.
IPv6 address prefix.
string
Maximum
length: 79
src-negate
Enable/disable negating source address match.
option
-disable
Option
Description
enable
Enable source address negation.
disable
Disable source address negation.
srcaddr
<name>
Source address name.
Address/group name.
string
Maximum
length: 79
start-port
Start destination port number (1 - 65535).
integer
Minimum value:
1 Maximum
value: 65535
1
start-source-port
Start source port number (1 - 65535).
integer
Minimum value:
1 Maximum
value: 65535
1
FortiOS 8.0.0 CLI Reference
1265
Fortinet Inc.

<!-- 来源页 1266 -->
Parameter
Description
Type
Size
Default
status
Enable/disable this policy route.
option
-enable
Option
Description
enable
Enable this policy route.
disable
Disable this policy route.
tos
Type of service bit pattern.
user
Not Specified
tos-mask
Type of service evaluated bits.
user
Not Specified
users <name>
List of users.
User name.
string
Maximum
length: 79
config router prefix-list
Configure IPv4 prefix lists.
config router prefix-list
Description: Configure IPv4 prefix lists.
edit <name>
set comments {string}
config rule
Description: IPv4 prefix list rule.
edit <id>
set action [permit|deny]
set ge {integer}
set le {integer}
set prefix {user}
next
end
next
end
config router prefix-list
Parameter
Description
Type
Size
Default
comments
Comment.
string
Maximum length:
127
name
Name.
string
Maximum length: 35
FortiOS 8.0.0 CLI Reference
1266
Fortinet Inc.

<!-- 来源页 1267 -->
config rule
Parameter
Description
Type
Size
Default
action
Permit or deny this IP address and netmask
prefix.
option
-permit
Option
Description
permit
Allow or permit packets that match this rule.
deny
Deny packets that match this rule.
ge
Minimum prefix length to be matched (0 - 32).
integer
Minimum value:
0 Maximum
value: 32
id
Rule ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
le
Maximum prefix length to be matched (0 - 32).
integer
Minimum value:
0 Maximum
value: 32
prefix
IPv4 prefix to define regular filter criteria, such as
"any" or subnets.
user
Not Specified
0.0.0.0
0.0.0.0
config router prefix-list6
Configure IPv6 prefix lists.
config router prefix-list6
Description: Configure IPv6 prefix lists.
edit <name>
set comments {string}
config rule
Description: IPv6 prefix list rule.
edit <id>
set action [permit|deny]
set flags {integer}
set ge {integer}
set le {integer}
set prefix6 {user}
next
end
next
end
FortiOS 8.0.0 CLI Reference
1267
Fortinet Inc.

<!-- 来源页 1268 -->
config router prefix-list6
Parameter
Description
Type
Size
Default
comments
Comment.
string
Maximum length:
127
name
Name.
string
Maximum length: 35
config rule
Parameter
Description
Type
Size
Default
action
Permit or deny packets that match this rule.
option
-permit
Option
Description
permit
Allow or permit packets that match this rule.
deny
Deny packets that match this rule.
flags
Flags. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
ge
Minimum prefix length to be matched (0 - 128).
integer
Minimum value:
0 Maximum
value: 128
id
Rule ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
le
Maximum prefix length to be matched (0 - 128).
integer
Minimum value:
0 Maximum
value: 128
prefix6
IPv6 prefix to define regular filter criteria, such as
"any" or subnets.
user
Not Specified
config router rip
Configure RIP.
config router rip
Description: Configure RIP.
set default-information-originate [enable|disable]
set default-metric {integer}
FortiOS 8.0.0 CLI Reference
1268
Fortinet Inc.

<!-- 来源页 1269 -->
config distance
Description: Distance.
edit <id>
set access-list {string}
set distance {integer}
set prefix {ipv4-classnet-any}
next
end
config distribute-list
Description: Distribute list.
edit <id>
set direction [in|out]
set interface {string}
set listname {string}
set status [enable|disable]
next
end
set garbage-timer {integer}
config interface
Description: RIP interface configuration.
edit <name>
set auth-keychain {string}
set auth-mode [none|text|...]
set auth-string {password}
set flags {integer}
set receive-version {option1}, {option2}, ...
set send-version {option1}, {option2}, ...
set send-version2-broadcast [disable|enable]
set split-horizon [poisoned|regular]
set split-horizon-status [enable|disable]
next
end
set max-out-metric {integer}
config neighbor
Description: Neighbor.
edit <id>
set ip {ipv4-address}
next
end
config network
Description: Network.
edit <id>
set prefix {ipv4-classnet}
next
end
config offset-list
Description: Offset list.
edit <id>
set access-list {string}
set direction [in|out]
set interface {string}
set offset {integer}
FortiOS 8.0.0 CLI Reference
1269
Fortinet Inc.

<!-- 来源页 1270 -->
set status [enable|disable]
next
end
set passive-interface <name1>, <name2>, ...
config redistribute
Description: Redistribute configuration. Read-only.
edit <name>
set metric {integer}
set routemap {string}
set status [enable|disable]
next
end
set timeout-timer {integer}
set update-timer {integer}
set version [1|2]
end
config router rip
Parameter
Description
Type
Size
Default
default-information-originate
Enable/disable generation of default route.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
default-metric
Default metric.
integer
Minimum
value: 1
Maximum
value: 16
1
garbage-timer
Garbage timer in seconds.
integer
Minimum
value: 5
Maximum
value:
2147483647
120
max-out-metric
Maximum metric allowed to output(0 means 'not
set').
integer
Minimum
value: 0
Maximum
value: 15
0
passive-interface
<name>
Passive interface configuration.
Passive interface name.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
1270
Fortinet Inc.

<!-- 来源页 1271 -->
Parameter
Description
Type
Size
Default
timeout-timer
Timeout timer in seconds.
integer
Minimum
value: 5
Maximum
value:
2147483647
180
update-timer
Update timer in seconds.
integer
Minimum
value: 1
Maximum
value:
2147483647
30
version
RIP version.
option
-2
Option
Description
1
Version 1.
2
Version 2.
config distance
Parameter
Description
Type
Size
Default
access-list
Access list for route destination.
string
Maximum
length: 35
distance
Distance (1 - 255).
integer
Minimum value:
1 Maximum
value: 255
0
id
Distance ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
prefix
Distance prefix.
ipv4-classnet-any
Not Specified
0.0.0.0
0.0.0.0
config distribute-list
Parameter
Description
Type
Size
Default
direction
Distribute list direction.
option
-out
Option
Description
in
Filter incoming packets.
FortiOS 8.0.0 CLI Reference
1271
Fortinet Inc.

<!-- 来源页 1272 -->
Parameter
Description
Type
Size
Default
Option
Description
out
Filter outgoing packets.
id
Distribute list ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
interface
Distribute list interface name.
string
Maximum
length: 15
listname
Distribute access/prefix list name.
string
Maximum
length: 35
status
Status.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
config interface
Parameter
Description
Type
Size
Default
auth-keychain
Authentication key-chain name.
string
Maximum
length: 35
auth-mode
Authentication mode.
option
-none
Option
Description
none
None.
text
Text.
md5
MD5.
auth-string
Authentication string/password.
password
Not
Specified
flags
Flags. Read-only.
integer
Minimum
value: 0
Maximum
value: 255
8
name
Interface name.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
1272
Fortinet Inc.

<!-- 来源页 1273 -->
Parameter
Description
Type
Size
Default
receive-version
Receive version.
option
-Option
Description
1
Version 1.
2
Version 2.
send-version
Send version.
option
-Option
Description
1
Version 1.
2
Version 2.
send-version2-broadcast
Enable/disable broadcast version 1 compatible
packets.
option
-disable
Option
Description
disable
Disable broadcasting.
enable
Enable broadcasting.
split-horizon
Enable/disable split horizon.
option
-poisoned
Option
Description
poisoned
Poisoned.
regular
Regular.
split-horizon-status
Enable/disable split horizon.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
config neighbor
Parameter
Description
Type
Size
Default
id
Neighbor entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
FortiOS 8.0.0 CLI Reference
1273
Fortinet Inc.

<!-- 来源页 1274 -->
Parameter
Description
Type
Size
Default
ip
IP address.
ipv4-address
Not Specified
0.0.0.0
config network
Parameter
Description
Type
Size
Default
id
Network entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
prefix
Network prefix.
ipv4-classnet
Not Specified
0.0.0.0
0.0.0.0
config offset-list
Parameter
Description
Type
Size
Default
access-list
Access list name.
string
Maximum
length: 35
direction
Offset list direction.
option
-out
Option
Description
in
Filter incoming packets.
out
Filter outgoing packets.
id
Offset-list ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
interface
Interface name.
string
Maximum
length: 15
offset
Offset.
integer
Minimum value:
1 Maximum
value: 16
0
status
Status.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
1274
Fortinet Inc.

<!-- 来源页 1275 -->
config redistribute
Parameter
Description
Type
Size
Default
metric
Redistribute metric setting.
integer
Minimum
value: 1
Maximum
value: 16
0
name
Redistribute name.
string
Maximum
length: 35
routemap
Route map name.
string
Maximum
length: 35
status
Status.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
config router ripng
Configure RIPng.
config router ripng
Description: Configure RIPng.
config aggregate-address
Description: Aggregate address.
edit <id>
set prefix6 {ipv6-prefix}
next
end
set default-information-originate [enable|disable]
set default-metric {integer}
config distance
Description: Distance.
edit <id>
set access-list6 {string}
set distance {integer}
set prefix6 {ipv6-prefix}
next
end
config distribute-list
Description: Distribute list.
edit <id>
set direction [in|out]
set interface {string}
set listname {string}
FortiOS 8.0.0 CLI Reference
1275
Fortinet Inc.

<!-- 来源页 1276 -->
set status [enable|disable]
next
end
set garbage-timer {integer}
config interface
Description: RIPng interface configuration.
edit <name>
set flags {integer}
set split-horizon [poisoned|regular]
set split-horizon-status [enable|disable]
next
end
set max-out-metric {integer}
config neighbor
Description: Neighbor.
edit <id>
set interface {string}
set ip6 {ipv6-address}
next
end
config network
Description: Network.
edit <id>
set prefix {ipv6-prefix}
next
end
config offset-list
Description: Offset list.
edit <id>
set access-list6 {string}
set direction [in|out]
set interface {string}
set offset {integer}
set status [enable|disable]
next
end
set passive-interface <name1>, <name2>, ...
config redistribute
Description: Redistribute configuration. Read-only.
edit <name>
set metric {integer}
set routemap {string}
set status [enable|disable]
next
end
set timeout-timer {integer}
set update-timer {integer}
end
FortiOS 8.0.0 CLI Reference
1276
Fortinet Inc.

<!-- 来源页 1277 -->
config router ripng
Parameter
Description
Type
Size
Default
default-information-originate
Enable/disable generation of default route.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
default-metric
Default metric.
integer
Minimum
value: 1
Maximum
value: 16
1
garbage-timer
Garbage timer in seconds.
integer
Minimum
value: 5
Maximum
value:
2147483647
120
max-out-metric
Maximum metric allowed to output(0 means 'not
set').
integer
Minimum
value: 0
Maximum
value: 15
0
passive-interface
<name>
Passive interface configuration.
Passive interface name.
string
Maximum
length: 79
timeout-timer
Timeout timer in seconds.
integer
Minimum
value: 5
Maximum
value:
2147483647
180
update-timer
Update timer in seconds.
integer
Minimum
value: 5
Maximum
value:
2147483647
30
FortiOS 8.0.0 CLI Reference
1277
Fortinet Inc.

<!-- 来源页 1278 -->
config aggregate-address
Parameter
Description
Type
Size
Default
id
Aggregate address entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
prefix6
Aggregate address prefix.
ipv6-prefix
Not Specified
::/0
config distance
Parameter
Description
Type
Size
Default
access-list6
Access list for route destination.
string
Maximum
length: 35
distance
Distance (1 - 255).
integer
Minimum value:
1 Maximum
value: 255
0
id
Distance ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
prefix6
Distance prefix6.
ipv6-prefix
Not Specified
::/0
config distribute-list
Parameter
Description
Type
Size
Default
direction
Distribute list direction.
option
-out
Option
Description
in
Filter incoming packets.
out
Filter outgoing packets.
id
Distribute list ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
interface
Distribute list interface name.
string
Maximum
length: 15
FortiOS 8.0.0 CLI Reference
1278
Fortinet Inc.

<!-- 来源页 1279 -->
Parameter
Description
Type
Size
Default
listname
Distribute access/prefix list name.
string
Maximum
length: 35
status
Status.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
config interface
Parameter
Description
Type
Size
Default
flags
Flags. Read-only.
integer
Minimum
value: 0
Maximum
value: 255
8
name
Interface name.
string
Maximum
length: 35
split-horizon
Enable/disable split horizon.
option
-poisoned
Option
Description
poisoned
Poisoned.
regular
Regular.
split-horizon-status
Enable/disable split horizon.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
config neighbor
Parameter
Description
Type
Size
Default
id
Neighbor entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
interface
Interface name.
string
Maximum
length: 15
FortiOS 8.0.0 CLI Reference
1279
Fortinet Inc.

<!-- 来源页 1280 -->
Parameter
Description
Type
Size
Default
ip6
IPv6 link-local address.
ipv6-address
Not Specified
::
config network
Parameter
Description
Type
Size
Default
id
Network entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
prefix
Network IPv6 link-local prefix.
ipv6-prefix
Not Specified
::/0
config offset-list
Parameter
Description
Type
Size
Default
access-list6
IPv6 access list name.
string
Maximum
length: 35
direction
Offset list direction.
option
-out
Option
Description
in
Filter incoming packets.
out
Filter outgoing packets.
id
Offset-list ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
interface
Interface name.
string
Maximum
length: 15
offset
Offset.
integer
Minimum value:
1 Maximum
value: 16
0
status
Status.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
1280
Fortinet Inc.

<!-- 来源页 1281 -->
config redistribute
Parameter
Description
Type
Size
Default
metric
Redistribute metric setting.
integer
Minimum
value: 1
Maximum
value: 16
0
name
Redistribute name.
string
Maximum
length: 35
routemap
Route map name.
string
Maximum
length: 35
status
Status.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
config router route-map
Configure route maps.
config router route-map
Description: Configure route maps.
edit <name>
set comments {string}
config rule
Description: Rule.
edit <id>
set action [permit|deny]
set match-as-path {string}
set match-community {string}
set match-community-exact [enable|disable]
set match-extcommunity {string}
set match-extcommunity-exact [enable|disable]
set match-interface {string}
set match-ip-address {string}
set match-ip-nexthop {string}
set match-ip6-address {string}
set match-ip6-nexthop {string}
set match-metric {integer}
set match-origin [none|egp|...]
set match-route-type [external-type1|external-type2|...]
set match-suppress [enable|disable]
set match-tag {integer}
set match-vrf {integer}
FortiOS 8.0.0 CLI Reference
1281
Fortinet Inc.

<!-- 来源页 1282 -->
set set-aggregator-as {integer}
set set-aggregator-ip {ipv4-address-any}
set set-aspath <as1>, <as2>, ...
set set-aspath-action [prepend|replace]
set set-atomic-aggregate [enable|disable]
set set-community <community1>, <community2>, ...
set set-community-additive [enable|disable]
set set-community-delete {string}
set set-dampening-max-suppress {integer}
set set-dampening-reachability-half-life {integer}
set set-dampening-reuse {integer}
set set-dampening-suppress {integer}
set set-dampening-unreachability-half-life {integer}
set set-extcommunity-rt <community1>, <community2>, ...
set set-extcommunity-soo <community1>, <community2>, ...
set set-ip-nexthop {ipv4-address}
set set-ip-prefsrc {ipv4-address}
set set-ip6-nexthop {ipv6-address}
set set-ip6-nexthop-local {ipv6-address}
set set-local-preference {integer}
set set-metric {integer}
set set-metric-type [external-type1|external-type2|...]
set set-origin [none|egp|...]
set set-originator-id {ipv4-address-any}
set set-priority {integer}
set set-route-tag {integer}
set set-tag {integer}
set set-vpnv4-nexthop {ipv4-address}
set set-vpnv6-nexthop {ipv6-address}
set set-vpnv6-nexthop-local {ipv6-address}
set set-weight {integer}
next
end
next
end
config router route-map
Parameter
Description
Type
Size
Default
comments
Optional comments.
string
Maximum
length: 127
name
Name.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
1282
Fortinet Inc.

<!-- 来源页 1283 -->
config rule
Parameter
Description
Type
Size
Default
action
Action.
option
-permit
Option
Description
permit
Permit.
deny
Deny.
id
Rule ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
match-as-path
Match BGP AS path list.
string
Maximum
length: 35
match-community
Match BGP community list.
string
Maximum
length: 35
match-community-exact
Enable/disable exact matching of
communities.
option
-disable
Option
Description
enable
Enable exact matching of communities.
disable
Disable exact matching of communities.
match-extcommunity
Match BGP extended community list.
string
Maximum
length: 35
match-extcommunity-exact
Enable/disable exact matching of extended
communities.
option
-disable
Option
Description
enable
Enable exact matching of extended communities.
disable
Disable exact matching of extended communities.
match-interface
Match interface configuration.
string
Maximum
length: 15
match-ip-address
Match IP address permitted by access-list
or prefix-list.
string
Maximum
length: 35
match-ip-nexthop
Match next hop IP address passed by
access-list or prefix-list.
string
Maximum
length: 35
match-ip6-address
Match IPv6 address permitted by access-list6 or prefix-list6.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
1283
Fortinet Inc.

<!-- 来源页 1284 -->
Parameter
Description
Type
Size
Default
match-ip6-nexthop
Match next hop IPv6 address passed by
access-list6 or prefix-list6.
string
Maximum
length: 35
match-metric
Match metric for redistribute routes.
integer
Minimum value:
0 Maximum
value:
4294967295
match-origin
Match BGP origin code.
option
-none
Option
Description
none
None.
egp
Remote EGP.
igp
Local IGP.
incomplete
Unknown heritage.
match-route-type
Match route type.
option
-Option
Description
external-type1
External type 1.
external-type2
External type 2.
none
No type specified.
match-suppress
Enable/disable matching of suppressed
original neighbor.
option
-disable
Option
Description
enable
Enable matching of suppressed original neighbor.
disable
Disable matching of suppressed original neighbor.
match-tag
Match tag.
integer
Minimum value:
0 Maximum
value:
4294967295
match-vrf
Match VRF ID.
integer
Minimum value:
0 Maximum
value: 511
set-aggregator-as
BGP aggregator AS.
integer
Minimum value:
0 Maximum
value:
4294967295
0
FortiOS 8.0.0 CLI Reference
1284
Fortinet Inc.

<!-- 来源页 1285 -->
Parameter
Description
Type
Size
Default
set-aggregator-ip
BGP aggregator IP.
ipv4-address-any
Not Specified
0.0.0.0
set-aspath <as>
Prepend BGP AS path attribute.
AS number (0 - 4294967295).
string
Maximum
length: 79
set-aspath-action
Specify preferred action of set-aspath.
option
-prepend
Option
Description
prepend
Prepend.
replace
Replace.
set-atomic-aggregate
Enable/disable BGP atomic aggregate
attribute.
option
-disable
Option
Description
enable
Enable BGP atomic aggregate attribute.
disable
Disable BGP atomic aggregate attribute.
set-community
<community>
BGP community attribute.
Attribute: AA|AA:NN|internet|local-AS|no-advertise|no-export|gshut.(exact match
required for well known communities).
string
Maximum
length: 79
set-community-additive
Enable/disable adding set-community to
existing community.
option
-disable
Option
Description
enable
Enable adding set-community to existing community.
disable
Disable adding set-community to existing community.
set-community-delete
Delete communities matching community
list.
string
Maximum
length: 35
set-dampening-max-suppress
Maximum duration to suppress a route (1 -255 min, 0 = unset).
integer
Minimum value:
0 Maximum
value: 255
0
set-dampening-reachability-half-life
Reachability half-life time for the penalty (1
- 45 min, 0 = unset).
integer
Minimum value:
0 Maximum
value: 45
0
FortiOS 8.0.0 CLI Reference
1285
Fortinet Inc.

<!-- 来源页 1286 -->
Parameter
Description
Type
Size
Default
set-dampening-reuse
Value to start reusing a route (1 - 20000, 0
= unset).
integer
Minimum value:
0 Maximum
value: 20000
0
set-dampening-suppress
Value to start suppressing a route (1 -20000, 0 = unset).
integer
Minimum value:
0 Maximum
value: 20000
0
set-dampening-unreachability-half-life
Unreachability Half-life time for the penalty
(1 - 45 min, 0 = unset).
integer
Minimum value:
0 Maximum
value: 45
0
set-extcommunity-rt
<community>
Route Target extended community.
AA:NN.
string
Maximum
length: 79
set-extcommunity-soo <community>
Site-of-Origin extended community.
Community (format = AA:NN).
string
Maximum
length: 79
set-ip-nexthop
IP address of next hop.
ipv4-address
Not Specified
set-ip-prefsrc
IP address of preferred source.
ipv4-address
Not Specified
set-ip6-nexthop
IPv6 global address of next hop.
ipv6-address
Not Specified
set-ip6-nexthop-local
IPv6 local address of next hop.
ipv6-address
Not Specified
set-local-preference
BGP local preference path attribute.
integer
Minimum value:
0 Maximum
value:
4294967295
set-metric
Metric value.
integer
Minimum value:
0 Maximum
value:
4294967295
set-metric-type
Metric type.
option
-Option
Description
external-type1
External type 1.
external-type2
External type 2.
none
No type specified.
set-origin
BGP origin code.
option
-none
FortiOS 8.0.0 CLI Reference
1286
Fortinet Inc.

<!-- 来源页 1287 -->
Parameter
Description
Type
Size
Default
Option
Description
none
None.
egp
Remote EGP.
igp
Local IGP.
incomplete
Unknown heritage.
set-originator-id
BGP originator ID attribute.
ipv4-address-any
Not Specified
set-priority
Priority for routing table.
integer
Minimum value:
1 Maximum
value: 65535
set-route-tag
Route tag for routing table.
integer
Minimum value:
0 Maximum
value:
4294967295
set-tag
Tag value.
integer
Minimum value:
0 Maximum
value:
4294967295
set-vpnv4-nexthop
IP address of VPNv4 next hop.
ipv4-address
Not Specified
set-vpnv6-nexthop
IPv6 global address of VPNv6 next hop.
ipv6-address
Not Specified
set-vpnv6-nexthop-local
IPv6 link-local address of VPNv6 next hop.
ipv6-address
Not Specified
set-weight
BGP weight for routing table.
integer
Minimum value:
0 Maximum
value:
4294967295
config router setting
Configure router settings.
config router setting
Description: Configure router settings.
set hostname {string}
set kernel-route-distance {integer}
FortiOS 8.0.0 CLI Reference
1287
Fortinet Inc.

<!-- 来源页 1288 -->
set show-filter {string}
end
config router setting
Parameter
Description
Type
Size
Default
hostname
Hostname for this virtual domain router.
string
Maximum
length: 14
kernel-route-distance
Administrative distance for routes learned from
kernel (0 - 255).
integer
Minimum
value: 0
Maximum
value: 255
255
show-filter
Prefix-list as filter for showing routes.
string
Maximum
length: 35
config router static
Configure IPv4 static routing tables.
config router static
Description: Configure IPv4 static routing tables.
edit <seq-num>
set bfd [enable|disable]
set blackhole [enable|disable]
set comment {var-string}
set device {string}
set distance {integer}
set dst {ipv4-classnet}
set dstaddr {string}
set dynamic-gateway [enable|disable]
set gateway {ipv4-address}
set internet-service {integer}
set internet-service-custom {string}
set internet-service-fortiguard {string}
set link-monitor-exempt [enable|disable]
set preferred-source {ipv4-address}
set priority {integer}
set sdwan-zone <name1>, <name2>, ...
set src {ipv4-classnet}
set status [enable|disable]
set tag {integer}
set vrf {integer}
set weight {integer}
next
end
FortiOS 8.0.0 CLI Reference
1288
Fortinet Inc.

<!-- 来源页 1289 -->
config router static
Parameter
Description
Type
Size
Default
bfd
Enable/disable Bidirectional Forwarding
Detection (BFD).
option
-disable
Option
Description
enable
Enable Bidirectional Forwarding Detection (BFD).
disable
Disable Bidirectional Forwarding Detection (BFD).
blackhole
Enable/disable black hole.
option
-disable
Option
Description
enable
Enable black hole.
disable
Disable black hole.
comment
Optional comments.
var-string
Maximum
length: 255
device
Gateway out interface or tunnel.
string
Maximum
length: 35
distance
Administrative distance (1 - 255).
integer
Minimum value:
1 Maximum
value: 255
10
dst
Destination IP and mask for this route.
ipv4-classnet
Not Specified
0.0.0.0
0.0.0.0
dstaddr
Name of firewall address or address group.
string
Maximum
length: 79
dynamic-gateway
Enable use of dynamic gateway retrieved
from a DHCP or PPP server.
option
-disable
Option
Description
enable
Enable dynamic gateway.
disable
Disable dynamic gateway.
gateway
Gateway IP for this route.
ipv4-address
Not Specified
0.0.0.0
internet-service
Application ID in the Internet Service
database.
integer
Minimum value:
0 Maximum
value:
4294967295
0
FortiOS 8.0.0 CLI Reference
1289
Fortinet Inc.

<!-- 来源页 1290 -->
Parameter
Description
Type
Size
Default
internet-service-custom
Application name in the Internet Service
custom database.
string
Maximum
length: 64
internet-service-fortiguard
Application name in the Internet Service
FortiGuard database.
string
Maximum
length: 64
link-monitor-exempt
Enable/disable withdrawal of this static route
when link monitor or health check is down.
option
-disable
Option
Description
enable
Keep this static route when link monitor or health check is down.
disable
Withdraw this static route when link monitor or health check is down.
(default)
preferred-source
Preferred source IP for this route.
ipv4-address
Not Specified
0.0.0.0
priority
Administrative priority (1 - 65535).
integer
Minimum value:
1 Maximum
value: 65535
1
sdwan-zone
<name>
Choose SD-WAN Zone.
SD-WAN zone name.
string
Maximum
length: 79
seq-num
Sequence number.
integer
Minimum value:
0 Maximum
value:
4294967295
0
src
Source prefix for this route.
ipv4-classnet
Not Specified
0.0.0.0
0.0.0.0
status
Enable/disable this static route.
option
-enable
Option
Description
enable
Enable static route.
disable
Disable static route.
tag
Route tag.
integer
Minimum value:
0 Maximum
value:
4294967295
0
vrf
Virtual Routing Forwarding ID.
integer
Minimum value:
0 Maximum
value: 511
unspecified
FortiOS 8.0.0 CLI Reference
1290
Fortinet Inc.

<!-- 来源页 1291 -->
Parameter
Description
Type
Size
Default
weight
Administrative weight (0 - 255).
integer
Minimum value:
0 Maximum
value: 255
0
config router static6
Configure IPv6 static routing tables.
config router static6
Description: Configure IPv6 static routing tables.
edit <seq-num>
set bfd [enable|disable]
set blackhole [enable|disable]
set comment {var-string}
set device {string}
set devindex {integer}
set distance {integer}
set dst {ipv6-network}
set dstaddr {string}
set dynamic-gateway [enable|disable]
set gateway {ipv6-address}
set link-monitor-exempt [enable|disable]
set priority {integer}
set sdwan-zone <name1>, <name2>, ...
set status [enable|disable]
set tag {integer}
set vrf {integer}
set weight {integer}
next
end
config router static6
Parameter
Description
Type
Size
Default
bfd
Enable/disable Bidirectional Forwarding
Detection (BFD).
option
-disable
Option
Description
enable
Enable Bidirectional Forwarding Detection (BFD).
disable
Disable Bidirectional Forwarding Detection (BFD).
blackhole
Enable/disable black hole.
option
-disable
FortiOS 8.0.0 CLI Reference
1291
Fortinet Inc.

<!-- 来源页 1292 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable black hole.
disable
Disable black hole.
comment
Optional comments.
var-string
Maximum
length: 255
device
Gateway out interface or tunnel.
string
Maximum
length: 35
devindex
Device index (0 - 4294967295).
integer
Minimum value:
0 Maximum
value:
4294967295
0
distance
Administrative distance (1 - 255).
integer
Minimum value:
1 Maximum
value: 255
10
dst
Destination IPv6 prefix.
ipv6-network
Not Specified
::/0
dstaddr
Name of firewall address or address group.
string
Maximum
length: 79
dynamic-gateway
Enable use of dynamic gateway retrieved
from Router Advertisement (RA).
option
-disable
Option
Description
enable
Enable dynamic gateway.
disable
Disable dynamic gateway.
gateway
IPv6 address of the gateway.
ipv6-address
Not Specified
::
link-monitor-exempt
Enable/disable withdrawal of this static route
when link monitor or health check is down.
option
-disable
Option
Description
enable
Keep this static route when link monitor or health check is down.
disable
Withdraw this static route when link monitor or health check is down.
(default)
priority
Administrative priority (1 - 65535).
integer
Minimum value:
1 Maximum
value: 65535
1024
FortiOS 8.0.0 CLI Reference
1292
Fortinet Inc.

<!-- 来源页 1293 -->
Parameter
Description
Type
Size
Default
sdwan-zone
<name>
Choose SD-WAN Zone.
SD-WAN zone name.
string
Maximum
length: 79
seq-num
Sequence number.
integer
Minimum value:
0 Maximum
value:
4294967295
0
status
Enable/disable this static route.
option
-enable
Option
Description
enable
Enable static route.
disable
Disable static route.
tag
Route tag.
integer
Minimum value:
0 Maximum
value:
4294967295
0
vrf
Virtual Routing Forwarding ID.
integer
Minimum value:
0 Maximum
value: 511
unspecified
weight
Administrative weight (0 - 255).
integer
Minimum value:
0 Maximum
value: 255
0
FortiOS 8.0.0 CLI Reference
1293
Fortinet Inc.
