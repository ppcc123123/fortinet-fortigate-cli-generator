# 系统：高可用 (HA) 与集群

> 来源: FortiOS-8.0.0-CLI_Reference.pdf
> 覆盖命令/章节: config system ha, config system ha-monitor, config system standalone-cluster, config system management-tunnel, config system auto-scale
> 本文件由 extract_pdf.py 从官方 PDF 自动提取，请勿手动编辑；
> 如需修正请修改 map.json 后重跑脚本。

---


<!-- 来源页 1507 -->
config system auto-scale
This command is available for model(s): FortiGate-VM64 Aliyun, FortiGate-VM64 AWS, FortiGate-VM64 Azure, FortiGate-VM64 GCP, FortiGate-VM64 OPC.
It is not available for: FortiGate 1000D, FortiGate 1000F, FortiGate 1001F, FortiGate 100F, FortiGate
101F Gen2, FortiGate 1100E, FortiGate 1101E, FortiGate 120G, FortiGate 121G, FortiGate 1800F,
FortiGate 1801F, FortiGate 2000E, FortiGate 200E, FortiGate 200F, FortiGate 200G, FortiGate 201E,
FortiGate 201F, FortiGate 201G, FortiGate 2200E, FortiGate 2201E, FortiGate 2500E, FortiGate
2600F, FortiGate 2601F, FortiGate 3000F, FortiGate 3001F, FortiGate 300E, FortiGate 301E,
FortiGate 30G, FortiGate 31G, FortiGate 3200F, FortiGate 3201F Gen2, FortiGate 3300E, FortiGate
3301E, FortiGate 3400E, FortiGate 3401E, FortiGate 3500F Gen2, FortiGate 3501F Gen2, FortiGate
3600E, FortiGate 3601E, FortiGate 3700F, FortiGate 3701F, FortiGate 3960E, FortiGate 3980E,
FortiGate 400E Bypass, FortiGate 400E, FortiGate 400F, FortiGate 401E, FortiGate 401F, FortiGate
40F 3G4G, FortiGate 40F, FortiGate 4200F, FortiGate 4201F Gen2, FortiGate 4400F, FortiGate
4401F Gen2, FortiGate 4800F, FortiGate 4801F, FortiGate 500E, FortiGate 501E, FortiGate 50G 5G,
FortiGate 50G DSL, FortiGate 50G SFP-POE, FortiGate 50G SFP, FortiGate 50G, FortiGate 51G 5G,
FortiGate 51G SFP-POE, FortiGate 51G, FortiGate 600E, FortiGate 600F, FortiGate 601E, FortiGate
601F, FortiGate 60F, FortiGate 61F, FortiGate 70F, FortiGate 70G-POE, FortiGate 70G, FortiGate 71F,
FortiGate 71G-POE, FortiGate 71G, FortiGate 800D, FortiGate 80F Bypass, FortiGate 80F DSL,
FortiGate 80F Gen2, FortiGate 80F-POE, FortiGate 81F Gen2, FortiGate 81F-POE, FortiGate 900D,
FortiGate 900G, FortiGate 901G, FortiGate 90G Gen2, FortiGate 90G, FortiGate 91G Gen2, FortiGate
91G, FortiGate-VM64, FortiGateRugged 50G 5G, FortiGateRugged 60F 3G4G, FortiGateRugged 60F
Gen2, FortiGateRugged 70F 3G4G, FortiGateRugged 70F, FortiGateRugged 70G 5G Dual,
FortiGateRugged 70G, FortiWiFi 30G, FortiWiFi 31G, FortiWiFi 40F 3G4G, FortiWiFi 40F, FortiWiFi
50G 5G, FortiWiFi 50G DSL, FortiWiFi 50G SFP, FortiWiFi 50G, FortiWiFi 51G, FortiWiFi 60F, FortiWiFi
61F, FortiWiFi 70G-POE, FortiWiFi 70G, FortiWiFi 71G, FortiWiFi 80F 2R 3G4G DSL, FortiWiFi 80F 2R,
FortiWiFi 81F 2R 3G4G DSL, FortiWiFi 81F 2R 3G4G-POE, FortiWiFi 81F 2R-POE, FortiWiFi 81F 2R.
Configure system auto-scaling.
config system auto-scale
Description: Configure system auto-scaling.
set callback-url {var-string}
set cloud-mode {string}
set hb-interval {integer}
set primary-ip {ipv4-address-any}
set psksecret {password-3}
set role [primary|secondary]
set status [enable|disable]
set sync-interface {string}
end
FortiOS 8.0.0 CLI Reference
1507
Fortinet Inc.

---


<!-- 来源页 1688 -->
Parameter
Description
Type
Size
Default
remote-gw
IP address of the remote gateway.
ipv4-address
Not Specified
0.0.0.0
remote-gw6
IPv6 address of the remote gateway.
ipv6-address
Not Specified
::
sequence-number-reception *
Enable/disable validating sequence numbers
in received GRE packets.
option
-disable
Option
Description
disable
Do not validate sequence number in received GRE packets.
enable
Validate sequence numbers in received GRE packets.
sequence-number-transmission *
Enable/disable including of sequence numbers
in transmitted GRE packets.
option
-disable
Option
Description
disable
Include sequence numbers in transmitted GRE packets.
enable
Do not include sequence numbers in transmitted GRE packets.
use-sdwan
Enable/disable use of SD-WAN to reach
remote gateway.
option
-disable
Option
Description
disable
Disable use of SD-WAN to reach remote gateway.
enable
Enable use of SD-WAN to reach remote gateway.
* This parameter may not exist in some models.
config system ha
Configure HA.
config system ha
Description: Configure HA.
set arps {integer}
set arps-interval {integer}
set authentication [enable|disable]
set auto-virtual-mac-interface <interface-name1>, <interface-name2>, ...
set backup-hbdev <name1>, <name2>, ...
set bounce-intf-upon-failover [enable|disable]
set check-secondary-dev-health [enable|disable]
set cpu-threshold {user}
FortiOS 8.0.0 CLI Reference
1688
Fortinet Inc.

<!-- 来源页 1689 -->
set encryption [enable|disable]
set evpn-ttl {integer}
set failover-hold-time {integer}
set ftp-proxy-threshold {user}
set gratuitous-arps [enable|disable]
set group-id {integer}
set group-name {string}
set ha-direct [enable|disable]
set ha-eth-type {string}
config ha-mgmt-interfaces
Description: Reserve interfaces to manage individual cluster units.
edit <id>
set dst {ipv4-classnet}
set dst6 {ipv6-prefix}
set gateway {ipv4-address}
set gateway6 {ipv6-address}
set interface {string}
next
end
set ha-mgmt-status [enable|disable]
set ha-uptime-diff-margin {integer}
set hb-interval {integer}
set hb-interval-in-milliseconds [100ms|10ms]
set hb-lost-threshold {integer}
set hbdev {user}
set hc-eth-type {string}
set hello-holddown {integer}
set http-proxy-threshold {user}
set imap-proxy-threshold {user}
set ipsec-phase2-proposal {option1}, {option2}, ...
set key {password}
set l2ep-eth-type {string}
set link-failed-signal [enable|disable]
config link-group
Description: Link group table.
edit <name>
set member <devname1>, <devname2>, ...
set min-members {integer}
next
end
set link-group-monitor {user}
set load-balance-all [enable|disable]
set logical-sn [enable|disable]
set memory-based-failover [enable|disable]
set memory-compatible-mode [enable|disable]
set memory-failover-flip-timeout {integer}
set memory-failover-monitor-period {integer}
set memory-failover-sample-rate {integer}
set memory-failover-threshold {integer}
set memory-threshold {user}
set mode [standalone|a-a|...]
set monitor {user}
FortiOS 8.0.0 CLI Reference
1689
Fortinet Inc.

<!-- 来源页 1690 -->
set multicast-ttl {integer}
set nntp-proxy-threshold {user}
set override [enable|disable]
set override-wait-time {integer}
set password {password}
set pingserver-failover-threshold {integer}
set pingserver-flip-timeout {integer}
set pingserver-monitor-interface {user}
set pingserver-secondary-force-reset [enable|disable]
set pop3-proxy-threshold {user}
set priority {integer}
set route-hold {integer}
set route-ttl {integer}
set route-wait {integer}
set schedule [none|leastconnection|...]
set session-pickup [enable|disable]
set session-pickup-connectionless [enable|disable]
set session-pickup-delay [enable|disable]
set session-pickup-expectation [enable|disable]
set session-pickup-nat [enable|disable]
set session-sync-dev {user}
set smtp-proxy-threshold {user}
set ssd-failover [enable|disable]
set standalone-config-sync [enable|disable]
set standalone-mgmt-vdom [enable|disable]
set sync-config [enable|disable]
set sync-packet-balance [enable|disable]
set unicast-gateway {ipv4-address}
set unicast-hb [enable|disable]
set unicast-hb-netmask {ipv4-netmask}
set unicast-hb-peerip {ipv4-address}
config unicast-peers
Description: Number of unicast peers.
edit <id>
set peer-ip {ipv4-address}
next
end
set unicast-status [enable|disable]
set uninterruptible-primary-wait {integer}
set upgrade-mode [simultaneous|uninterruptible|...]
config vcluster
Description: Virtual cluster table.
edit <vcluster-id>
set link-group-monitor {user}
set monitor {user}
set override [enable|disable]
set override-wait-time {integer}
set pingserver-failover-threshold {integer}
set pingserver-flip-timeout {integer}
set pingserver-monitor-interface {user}
set pingserver-secondary-force-reset [enable|disable]
set priority {integer}
FortiOS 8.0.0 CLI Reference
1690
Fortinet Inc.

<!-- 来源页 1691 -->
set vdom <name1>, <name2>, ...
next
end
set vcluster-status [enable|disable]
set weight {user}
end
config system ha
Parameter
Description
Type
Size
Default
arps
Number of gratuitous ARPs (1 - 60).
Lower to reduce traffic. Higher to
reduce failover time.
integer
Minimum
value: 1
Maximum
value: 60
5
arps-interval
Time between gratuitous ARPs (1 -20 sec). Lower to reduce failover
time. Higher to reduce traffic.
integer
Minimum
value: 1
Maximum
value: 20
8
authentication
Enable/disable heartbeat message
authentication.
option
-disable
Option
Description
enable
Enable heartbeat message authentication.
disable
Disable heartbeat message authentication.
auto-virtual-mac-interface
<interface-name>
The physical interface that will be
assigned an auto-generated virtual
MAC address.
Interface name.
string
Maximum
length: 15
backup-hbdev
<name>
Backup heartbeat interfaces. Must
be the same for all members.
Interface name.
string
Maximum
length: 79
bounce-intf-upon-failover
Enable/disable notification of kernel
to bring down and up all monitored
interfaces. The setting is used during
failovers if gratuitous ARPs do not
update the network.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
1691
Fortinet Inc.

<!-- 来源页 1692 -->
Parameter
Description
Type
Size
Default
check-secondary-dev-health
Enable/disable secondary dev health
check for session load-balance in HA
A-A mode.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
cpu-threshold
Dynamic weighted load balancing
CPU usage weight and high and low
thresholds.
user
Not Specified
encryption
Enable/disable heartbeat message
encryption.
option
-disable
Option
Description
enable
Enable heartbeat message encryption.
disable
Disable heartbeat message encryption.
evpn-ttl
HA EVPN FDB TTL on primary box (5
- 3600 sec).
integer
Minimum
value: 5
Maximum
value: 3600
60
failover-hold-time
Time to wait before failover (0 - 300
sec, default = 0), to avoid flip.
integer
Minimum
value: 0
Maximum
value: 300
0
ftp-proxy-threshold
Dynamic weighted load balancing
weight and high and low number of
FTP proxy sessions.
user
Not Specified
gratuitous-arps
Enable/disable gratuitous ARPs.
Recommended to disable if link-failed-signal is enabled.
option
-enable
Option
Description
enable
Enable gratuitous ARPs.
disable
Disable gratuitous ARPs.
group-id
HA group ID (0 - 1023; or 0 - 7 when
there are more than 2 vclusters).
Must be the same for all members.
integer
Minimum
value: 0
Maximum
value: 1023
0
FortiOS 8.0.0 CLI Reference
1692
Fortinet Inc.

<!-- 来源页 1693 -->
Parameter
Description
Type
Size
Default
group-name
Cluster group name. Must be the
same for all members.
string
Maximum
length: 32
ha-direct
Enable/disable using ha-mgmt
interface for syslog, remote
authentication (RADIUS),
FortiAnalyzer, FortiSandbox, sFlow,
and Netflow.
option
-disable
Option
Description
enable
Enable using ha-mgmt interface for syslog, remote authentication
(RADIUS), FortiAnalyzer, FortiSandbox, sFlow, and Netflow.
disable
Disable using ha-mgmt interface for syslog, remote authentication
(RADIUS), FortiAnalyzer, FortiSandbox, sFlow, and Netflow.
ha-eth-type
HA heartbeat packet Ethertype (4-digit hex).
string
Maximum
length: 4
8890
ha-mgmt-status
Enable to reserve interfaces to
manage individual cluster units.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
ha-uptime-diff-margin
Normally you would only reduce this
value for failover testing.
integer
Minimum
value: 1
Maximum
value: 65535
300
hb-interval
Time between sending heartbeat
packets (1 - 20). Increase to reduce
false positives.
integer
Minimum
value: 1
Maximum
value: 20
2
hb-interval-in-milliseconds
Units of heartbeat interval time
between sending heartbeat packets.
Default is 100ms.
option
-100ms
Option
Description
100ms
Each heartbeat interval is 100ms.
10ms
Each heartbeat interval is 10ms.
FortiOS 8.0.0 CLI Reference
1693
Fortinet Inc.

<!-- 来源页 1694 -->
Parameter
Description
Type
Size
Default
hb-lost-threshold
Number of lost heartbeats to signal a
failure (1 - 60). Increase to reduce
false positives.
integer
Minimum
value: 1
Maximum
value: 60
6 **
hbdev
Heartbeat interfaces. Must be the
same for all members. Enter
<interface> <priority> pairs to
specify the priority of each heartbeat
interface. Higher priority takes
precedence.
user
Not Specified
hc-eth-type
Transparent mode HA heartbeat
packet Ethertype (4-digit hex).
string
Maximum
length: 4
8891
hello-holddown
Time to wait before changing from
hello to work state (5 - 300 sec).
integer
Minimum
value: 5
Maximum
value: 300
20
http-proxy-threshold
Dynamic weighted load balancing
weight and high and low number of
HTTP proxy sessions.
user
Not Specified
imap-proxy-threshold
Dynamic weighted load balancing
weight and high and low number of
IMAP proxy sessions.
user
Not Specified
ipsec-phase2-proposal
IPsec phase2 proposal.
option
-Option
Description
aes128-sha1
aes128-sha1
aes128-sha256
aes128-sha256
aes128-sha384
aes128-sha384
aes128-sha512
aes128-sha512
aes192-sha1
aes192-sha1
aes192-sha256
aes192-sha256
aes192-sha384
aes192-sha384
aes192-sha512
aes192-sha512
aes256-sha1
aes256-sha1
aes256-sha256
aes256-sha256
FortiOS 8.0.0 CLI Reference
1694
Fortinet Inc.

<!-- 来源页 1695 -->
Parameter
Description
Type
Size
Default
Option
Description
aes256-sha384
aes256-sha384
aes256-sha512
aes256-sha512
aes128gcm
aes128gcm
aes256gcm
aes256gcm
chacha20poly1305
chacha20poly1305
key
Key.
password
Not Specified
l2ep-eth-type
Telnet session HA heartbeat packet
Ethertype (4-digit hex).
string
Maximum
length: 4
8893
link-failed-signal
Enable to shut down all interfaces for
1 sec after a failover. Use if
gratuitous ARPs do not update
network.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
link-group-monitor *
Link groups to check for port
monitoring.
user
Not Specified
load-balance-all
Enable to load balance TCP
sessions. Disable to load balance
proxy sessions only.
option
-disable
Option
Description
enable
Enable load balance.
disable
Disable load balance.
logical-sn *
Enable/disable usage of the logical
serial number.
option
-disable
Option
Description
enable
Enable usage of the logical serial number.
disable
Disable usage of the logical serial number.
memory-based-failover
Enable/disable memory based
failover.
option
-disable
FortiOS 8.0.0 CLI Reference
1695
Fortinet Inc.

<!-- 来源页 1696 -->
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
memory-compatible-mode
Enable/disable memory compatible
mode.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
memory-failover-flip-timeout
Time to wait between subsequent
memory based failovers in minutes
(6 - 2147483647, default = 6).
integer
Minimum
value: 6
Maximum
value:
2147483647
6
memory-failover-monitor-period
Duration of high memory usage
before memory based failover is
triggered in seconds (1 - 300, default
= 60).
integer
Minimum
value: 1
Maximum
value: 300
60
memory-failover-sample-rate
Rate at which memory usage is
sampled in order to measure
memory usage in seconds (1 - 60,
default = 1).
integer
Minimum
value: 1
Maximum
value: 60
1
memory-failover-threshold
Memory usage threshold to trigger
memory based failover (0 means
using conserve mode threshold in
system.global).
integer
Minimum
value: 0
Maximum
value: 95
0
memory-threshold
Dynamic weighted load balancing
memory usage weight and high and
low thresholds.
user
Not Specified
mode
HA mode. Must be the same for all
members.
option
-standalone
Option
Description
standalone
Standalone mode.
a-a
Active-active mode.
a-p
Active-passive mode.
FortiOS 8.0.0 CLI Reference
1696
Fortinet Inc.

<!-- 来源页 1697 -->
Parameter
Description
Type
Size
Default
monitor
Interfaces to check for port
monitoring (or link failure).
user
Not Specified
multicast-ttl
HA multicast TTL on primary (5 -3600 sec).
integer
Minimum
value: 5
Maximum
value: 3600
600
nntp-proxy-threshold
Dynamic weighted load balancing
weight and high and low number of
NNTP proxy sessions.
user
Not Specified
override
Enable and increase the priority of
the unit that should always be
primary (master).
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
override-wait-time
Delay negotiating if override is
enabled (0 - 3600 sec). Reduces
how often the cluster negotiates.
integer
Minimum
value: 0
Maximum
value: 3600
0
password
Cluster password. It is mandatory
and must be the same for all
members
password
Not Specified
pingserver-failover-threshold
Remote IP monitoring failover
threshold (0 - 50).
integer
Minimum
value: 0
Maximum
value: 50
0
pingserver-flip-timeout
Time to wait in minutes before
renegotiating after a remote IP
monitoring failover.
integer
Minimum
value: 6
Maximum
value:
2147483647
60
pingserver-monitor-interface
Interfaces to check for remote IP
monitoring.
user
Not Specified
pingserver-secondary-force-reset
Enable to force the cluster to
negotiate after a remote IP
monitoring failover.
option
-enable
FortiOS 8.0.0 CLI Reference
1697
Fortinet Inc.

<!-- 来源页 1698 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable force reset of secondary member after PING server failure.
disable
Disable force reset of secondary member after PING server failure.
pop3-proxy-threshold
Dynamic weighted load balancing
weight and high and low number of
POP3 proxy sessions.
user
Not Specified
priority
Increase the priority to select the
primary unit (0 - 255).
integer
Minimum
value: 0
Maximum
value: 255
128
route-hold
Time to wait between routing table
updates to the cluster (0 - 3600
sec).
integer
Minimum
value: 0
Maximum
value: 3600
10
route-ttl
TTL for primary unit routes (5 - 3600
sec). Increase to maintain active
routes during failover.
integer
Minimum
value: 5
Maximum
value: 3600
10
route-wait
Time to wait before sending new
routes to the cluster (0 - 3600 sec).
integer
Minimum
value: 0
Maximum
value: 3600
0
schedule
Type of A-A load balancing. Use
none if you have external load
balancers.
option
-round-robin
Option
Description
none
None.
leastconnection
Least connection.
round-robin
Round robin.
weight-round-robin
Weight round robin.
random
Random.
ip
IP.
ipport
IP port.
session-pickup
Enable/disable session pickup.
Enabling it can reduce session down
time when fail over happens.
option
-disable
FortiOS 8.0.0 CLI Reference
1698
Fortinet Inc.

<!-- 来源页 1699 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable session pickup.
disable
Disable session pickup.
session-pickup-connectionless
Enable/disable UDP and ICMP
session sync.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
session-pickup-delay
Enable to sync sessions longer than
30 sec. Only longer lived sessions
need to be synced.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
session-pickup-expectation
Enable/disable session helper
expectation session sync for FGSP.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
session-pickup-nat
Enable/disable NAT session sync for
FGSP.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
session-sync-dev
Offload session-sync process to
kernel and sync sessions using
connected interface(s) directly.
user
Not Specified
smtp-proxy-threshold
Dynamic weighted load balancing
weight and high and low number of
SMTP proxy sessions.
user
Not Specified
ssd-failover *
Enable/disable automatic HA failover
on SSD disk failure.
option
-disable
FortiOS 8.0.0 CLI Reference
1699
Fortinet Inc.

<!-- 来源页 1700 -->
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
standalone-config-sync
Enable/disable FGSP configuration
synchronization.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
standalone-mgmt-vdom
Enable/disable standalone
management VDOM.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
sync-config
Enable/disable configuration
synchronization.
option
-enable
Option
Description
enable
Enable configuration synchronization.
disable
Disable configuration synchronization.
sync-packet-balance
Enable/disable HA packet
distribution to multiple CPUs.
option
-disable
Option
Description
enable
Enable HA packet distribution to multiple CPUs.
disable
Disable HA packet distribution to multiple CPUs.
unicast-gateway
*
Default route gateway for unicast
interface.
ipv4-address
Not Specified
0.0.0.0
unicast-hb *
Enable/disable unicast heartbeat.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
1700
Fortinet Inc.

<!-- 来源页 1701 -->
Parameter
Description
Type
Size
Default
unicast-hb-netmask *
Unicast heartbeat netmask.
ipv4-netmask
Not Specified
0.0.0.0
unicast-hb-peerip *
Unicast heartbeat peer IP.
ipv4-address
Not Specified
0.0.0.0
unicast-status *
Enable/disable unicast connection.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
uninterruptible-primary-wait
Number of minutes the primary HA
unit waits before the secondary HA
unit is considered upgraded and the
system is started before starting its
own upgrade (15 - 300, default =
30).
integer
Minimum
value: 15
Maximum
value: 300
30
upgrade-mode
The mode to upgrade a cluster.
option
-uninterruptible
Option
Description
simultaneous
Upgrade all HA members at the same time.
uninterruptible
Upgrade HA cluster without blocking network traffic.
local-only
Upgrade local member only.
secondary-only
Upgrade secondary member only.
vcluster-status
Enable/disable virtual cluster for
virtual clustering.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
weight
Weight-round-robin weight for each
cluster unit. Syntax <priority>
<weight>.
user
Not Specified
0 40
* This parameter may not exist in some models.
** Values may differ between models.
FortiOS 8.0.0 CLI Reference
1701
Fortinet Inc.

<!-- 来源页 1702 -->
config ha-mgmt-interfaces
Parameter
Description
Type
Size
Default
dst
Default route destination for reserved HA
management interface.
ipv4-classnet
Not Specified
0.0.0.0
0.0.0.0
dst6
Default IPv6 destination for reserved HA
management interface.
ipv6-prefix
Not Specified
::/0
gateway
Default route gateway for reserved HA
management interface.
ipv4-address
Not Specified
0.0.0.0
gateway6
Default IPv6 gateway for reserved HA
management interface.
ipv6-address
Not Specified
::
id
Table ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
interface
Interface to reserve for HA management.
string
Maximum
length: 15
config link-group
Parameter
Description
Type
Size
Default
member
<devname>
Member interface in this link group.
Interface name.
string
Maximum
length: 15
min-members
Minimum number of members that must be up
before this link group is considered up.
integer
Minimum
value: 1
Maximum
value: 64
1
name
Name.
string
Maximum
length: 15
config unicast-peers
Parameter
Description
Type
Size
Default
id
Table ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
peer-ip
Unicast peer IP.
ipv4-address
Not Specified
0.0.0.0
FortiOS 8.0.0 CLI Reference
1702
Fortinet Inc.

<!-- 来源页 1703 -->
config vcluster
Parameter
Description
Type
Size
Default
link-group-monitor *
Link groups to check for port monitoring.
user
Not Specified
monitor
Interfaces to check for port monitoring (or link
failure).
user
Not Specified
override
Enable and increase the priority of the unit that
should always be primary (master).
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
override-wait-time
Delay negotiating if override is enabled (0 -3600 sec). Reduces how often the cluster
negotiates.
integer
Minimum
value: 0
Maximum
value: 3600
0
pingserver-failover-threshold
Remote IP monitoring failover threshold (0 - 50).
integer
Minimum
value: 0
Maximum
value: 50
0
pingserver-flip-timeout
Time to wait in minutes before renegotiating
after a remote IP monitoring failover.
integer
Minimum
value: 6
Maximum
value:
2147483647
60
pingserver-monitor-interface
Interfaces to check for remote IP monitoring.
user
Not Specified
pingserver-secondary-force-reset
Enable to force the cluster to negotiate after a
remote IP monitoring failover.
option
-enable
Option
Description
enable
Enable force reset of secondary member after PING server failure.
disable
Disable force reset of secondary member after PING server failure.
priority
Increase the priority to select the primary unit (0
- 255).
integer
Minimum
value: 0
Maximum
value: 255
128
FortiOS 8.0.0 CLI Reference
1703
Fortinet Inc.

---


<!-- 来源页 1704 -->
Parameter
Description
Type
Size
Default
vcluster-id
ID.
integer
Minimum
value: 1
Maximum
value: 30
1
vdom <name>
Virtual domain(s) in the virtual cluster.
Virtual domain name.
string
Maximum
length: 79
* This parameter may not exist in some models.
config system ha-monitor
Configure HA monitor.
config system ha-monitor
Description: Configure HA monitor.
set monitor-vlan [enable|disable]
set vlan-hb-interval {integer}
set vlan-hb-lost-threshold {integer}
end
config system ha-monitor
Parameter
Description
Type
Size
Default
monitor-vlan
Enable/disable monitor VLAN interfaces.
option
-disable
Option
Description
enable
Enable monitor VLAN interfaces.
disable
Disable monitor VLAN interfaces.
vlan-hb-interval
Configure heartbeat interval (seconds).
integer
Minimum
value: 1
Maximum
value: 30
5
vlan-hb-lost-threshold
VLAN lost heartbeat threshold (1 - 60).
integer
Minimum
value: 1
Maximum
value: 60
3
FortiOS 8.0.0 CLI Reference
1704
Fortinet Inc.

---


<!-- 来源页 1836 -->
next
end
config system mac-address-table
Parameter
Description
Type
Size
Default
interface
Interface name.
string
Maximum
length: 35
mac
MAC address.
mac-address
Not
Specified
00:00:00:00:00:00
reply-substitute
New MAC for reply traffic.
mac-address
Not
Specified
00:00:00:00:00:00
config system management-tunnel
Management tunnel configuration.
config system management-tunnel
Description: Management tunnel configuration.
set allow-collect-statistics [enable|disable]
set allow-config-restore [enable|disable]
set allow-push-configuration [enable|disable]
set allow-push-firmware [enable|disable]
set authorized-manager-only [enable|disable]
set serial-number {user}
set status [enable|disable]
end
config system management-tunnel
Parameter
Description
Type
Size
Default
allow-collect-statistics
Enable/disable collection of run time statistics.
option
-enable
Option
Description
enable
Enable collection of run time statistics.
disable
Disable collection of run time statistics.
allow-config-restore
Enable/disable allow config restore.
option
-enable
FortiOS 8.0.0 CLI Reference
1836
Fortinet Inc.

---


<!-- 来源页 2164 -->
Parameter
Description
Type
Size
Default
name
FortiCloud SSO admin name.
string
Maximum
length: 64
openai-api-key *
OpenAI API key.
password-3
Not
Specified
openai-api-key-part2 *
OpenAI API key part 2 for excess length.
password-3
Not
Specified
openai-model *
OpenAI model.
string
Maximum
length: 35
௭V௭J **
openai-org-id
*
OpenAI organization ID.
string
Maximum
length: 35
openai-project-id *
OpenAI project ID.
string
Maximum
length: 35
vdom <name>
Virtual domain(s) that the administrator can
access.
Virtual domain name.
string
Maximum
length: 79
* This parameter may not exist in some models.
** Values may differ between models.
config system standalone-cluster
Configure FortiGate Session Life Support Protocol (FGSP) cluster attributes.
config system standalone-cluster
Description: Configure FortiGate Session Life Support Protocol (FGSP) cluster attributes.
set asymmetric-traffic-control [cps-preferred|strict-anti-replay]
config cluster-peer
Description: Configure FortiGate Session Life Support Protocol (FGSP) session
synchronization.
edit <sync-id>
set down-intfs-before-sess-sync <name1>, <name2>, ...
set hb-interval {integer}
set hb-lost-threshold {integer}
set interface {string}
set ipsec-tunnel-sync [enable|disable]
set peerip {ipv4-address}
set peervd {string}
set secondary-add-ipsec-routes [enable|disable]
config session-sync-filter
Description: Add one or more filters if you only want to synchronize some
sessions. Use the filter to configure the types of sessions to synchronize.
config custom-service
Description: Only sessions using these custom services are synchronized. Use
FortiOS 8.0.0 CLI Reference
2164
Fortinet Inc.

<!-- 来源页 2165 -->
source and destination port ranges to define these custom services.
edit <id>
set dst-port-range {user}
set src-port-range {user}
next
end
set dstaddr {ipv4-classnet-any}
set dstaddr6 {ipv6-network}
set dstintf {string}
set srcaddr {ipv4-classnet-any}
set srcaddr6 {ipv6-network}
set srcintf {string}
end
set source-ip {ipv4-address}
set syncvd <name1>, <name2>, ...
next
end
set encryption [enable|disable]
set group-member-id {integer}
set helper-traffic-bounce [enable|disable]
set layer2-connection [available|unavailable]
set monitor-interface <name1>, <name2>, ...
config monitor-prefix
Description: Configure a list of routing prefixes to monitor.
edit <id>
set prefix {ipv4-classnet-any}
set vdom {string}
set vrf {integer}
next
end
set pingsvr-monitor-interface <name1>, <name2>, ...
set psksecret {password-3}
set session-sync [enable|disable]
set session-sync-dev {user}
set standalone-group-id {integer}
set utm-traffic-bounce [enable|disable]
end
config system standalone-cluster
Parameter
Description
Type
Size
Default
asymmetric-traffic-control
Asymmetric traffic control mode.
option
-cps-preferred
Option
Description
cps-preferred
Connection per second (CPS) preferred.
strict-anti-replay
Strict anti-replay check.
FortiOS 8.0.0 CLI Reference
2165
Fortinet Inc.

<!-- 来源页 2166 -->
Parameter
Description
Type
Size
Default
encryption
Enable/disable encryption when
synchronizing sessions.
option
-disable
Option
Description
enable
Enable encryption when synchronizing sessions.
disable
Disable encryption when synchronizing sessions.
group-member-id
Cluster member ID (0 - 15).
integer
Minimum
value: 0
Maximum
value: 15
0
helper-traffic-bounce
Enable/disable helper related traffic bounce.
option
-enable
Option
Description
enable
Enable helper related traffic bounce.
disable
Disable helper related traffic bounce.
layer2-connection
Indicate whether layer 2 connections are
present among FGSP members.
option
-unavailable
Option
Description
available
There exist layer 2 connections among FGSP members.
unavailable
There does not exist layer 2 connection among FGSP members.
monitor-interface
<name>
Configure a list of interfaces on which to
monitor itself. Monitoring is performed on the
status of the interface.
Interface name.
string
Maximum
length: 79
pingsvr-monitor-interface
<name>
List of pingsvr monitor interface to check for
remote IP monitoring.
Interface name.
string
Maximum
length: 79
psksecret
Pre-shared secret for session
synchronization (ASCII string or hexadecimal
encoded with a leading 0x).
password-3
Not
Specified
session-sync *
Enable/disable session synchronization.
option
-enable
Option
Description
enable
Enable session synchronization.
disable
Disable session synchronization.
FortiOS 8.0.0 CLI Reference
2166
Fortinet Inc.

<!-- 来源页 2167 -->
Parameter
Description
Type
Size
Default
session-sync-dev
Offload session-sync process to kernel and
sync sessions using connected interface(s)
directly.
user
Not
Specified
standalone-group-id
Cluster group ID (0 - 255). Must be the same
for all members.
integer
Minimum
value: 0
Maximum
value: 255
0
utm-traffic-bounce
Enable/disable UTM related traffic bounce,
disable it may stop the asymmetric-traffic
UTM features from working.
option
-enable
Option
Description
enable
Enable UTM related traffic bounce.
disable
Disable UTM related traffic bounce.
* This parameter may not exist in some models.
config cluster-peer
Parameter
Description
Type
Size
Default
down-intfs-before-sess-sync <name>
List of interfaces to be turned down before
session synchronization is complete.
Interface name.
string
Maximum
length: 79
hb-interval
Heartbeat interval (1 - 20) (100*ms). Increase to
reduce false positives.
integer
Minimum value:
1 Maximum
value: 20
2
hb-lost-threshold
Lost heartbeat threshold (1 - 60). Increase to
reduce false positives.
integer
Minimum value:
1 Maximum
value: 60
10
interface *
Outgoing interface for peer connections.
string
Maximum
length: 15
ipsec-tunnel-sync
Enable/disable IPsec tunnel synchronization.
option
-enable
Option
Description
enable
Enable IPsec tunnel synchronization.
disable
Disable IPsec tunnel synchronization.
peerip
IP address of the interface on the peer unit that
is used for the session synchronization link.
ipv4-address
Not Specified
0.0.0.0
FortiOS 8.0.0 CLI Reference
2167
Fortinet Inc.

<!-- 来源页 2168 -->
Parameter
Description
Type
Size
Default
peervd
VDOM that contains the session synchronization
link interface on the peer unit. Usually both
peers would have the same peervd.
string
Maximum
length: 31
root
secondary-add-ipsec-routes
Enable/disable IKE route announcement on the
backup unit.
option
-enable
Option
Description
enable
Add IKE routes to the backup unit.
disable
Do not add IKE routes to the backup unit.
source-ip *
Source IP address to use for peer connections.
ipv4-address
Not Specified
0.0.0.0
sync-id
Sync ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
syncvd
<name>
Sessions from these VDOMs are synchronized
using this session synchronization
configuration.
VDOM name.
string
Maximum
length: 79
* This parameter may not exist in some models.
config session-sync-filter
Parameter
Description
Type
Size
Default
dstaddr
Only sessions to this IPv4 address are
synchronized.
ipv4-classnet-any
Not
Specified
0.0.0.0
0.0.0.0
dstaddr6
Only sessions to this IPv6 address are
synchronized.
ipv6-network
Not
Specified
::/0
dstintf
Only sessions to this interface are synchronized.
string
Maximum
length: 15
srcaddr
Only sessions from this IPv4 address are
synchronized.
ipv4-classnet-any
Not
Specified
0.0.0.0
0.0.0.0
srcaddr6
Only sessions from this IPv6 address are
synchronized.
ipv6-network
Not
Specified
::/0
srcintf
Only sessions from this interface are synchronized.
string
Maximum
length: 15
FortiOS 8.0.0 CLI Reference
2168
Fortinet Inc.
