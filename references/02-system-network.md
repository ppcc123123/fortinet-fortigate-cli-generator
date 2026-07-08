# 系统：DNS / DHCP / NTP / SNMP / SDWAN / 全局

> 来源: FortiOS-8.0.0-CLI_Reference.pdf
> 覆盖命令/章节: config system dns, config system dns64, config system dns-database, config system dns-server, config system dhcp server, config system dhcp template, config system dhcp6 server, config system ntp, config system snmp community, config system snmp user, config system snmp sysinfo, config system snmp mib-view, config system snmp rmon-stat, config system netflow, config system sflow, config system sdwan, config system link-monitor, config system global, config system settings, config system session-helper, config system session-ttl, config system ipam, config system arp-table, config system proxy-arp, config system probe-response
> 本文件由 extract_pdf.py 从官方 PDF 自动提取，请勿手动编辑；
> 如需修正请修改 map.json 后重跑脚本。

---


<!-- 来源页 1487 -->
Parameter
Description
Type
Size
Default
Option
Description
ipv4-trusthost
IPv4 trusthost.
ipv6-trusthost
IPv6 trusthost.
config system arp-table
Configure ARP table.
config system arp-table
Description: Configure ARP table.
edit <id>
set interface {string}
set ip {ipv4-address}
set mac {mac-address}
next
end
config system arp-table
Parameter
Description
Type
Size
Default
id
Unique integer ID of the entry.
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
ip
IP address.
ipv4-address
Not Specified
0.0.0.0
mac
MAC address.
mac-address
Not Specified
00:00:00:00:00:00
config system automation-action
Action for automation stitches.
config system automation-action
Description: Action for automation stitches.
edit <name>
set accprofile {string}
FortiOS 8.0.0 CLI Reference
1487
Fortinet Inc.

---


<!-- 来源页 1545 -->
Parameter
Description
Type
Size
Default
id
Device upgrade exemption ID (0 - 65535).
integer
Minimum
value: 0
Maximum
value:
65535
0
version
Highest version of Fortinet firmware to exempt
(format in Major.minor.patch, such as 7.6.4).
user
Not
Specified
config system dhcp server
Configure DHCP servers.
config system dhcp server
Description: Configure DHCP servers.
edit <id>
set auto-configuration [disable|enable]
set auto-managed-status [disable|enable]
set conflicted-ip-timeout {integer}
set ddns-auth [disable|tsig]
set ddns-key {password_aes256}
set ddns-keyname {string}
set ddns-server-ip {ipv4-address}
set ddns-ttl {integer}
set ddns-update [disable|enable]
set ddns-update-override [disable|enable]
set ddns-zone {string}
set default-gateway {ipv4-address}
set dhcp-settings-from-fortiipam [disable|enable]
set dns-server1 {ipv4-address}
set dns-server2 {ipv4-address}
set dns-server3 {ipv4-address}
set dns-server4 {ipv4-address}
set dns-service [local|default|...]
set domain {string}
config exclude-range
Description: Exclude one or more ranges of IP addresses from being assigned to
clients.
edit <id>
set end-ip {ipv4-address}
set lease-time {integer}
set oui-match [disable|enable]
set oui-string <oui-string1>, <oui-string2>, ...
set start-ip {ipv4-address}
set uci-match [disable|enable]
set uci-string <uci-string1>, <uci-string2>, ...
set vci-match [disable|enable]
set vci-string <vci-string1>, <vci-string2>, ...
FortiOS 8.0.0 CLI Reference
1545
Fortinet Inc.

<!-- 来源页 1546 -->
set vendor {string}
next
end
set filename {string}
set forticlient-on-net-status [disable|enable]
set interface {string}
set ip-mode [range|usrgrp]
config ip-range
Description: DHCP IP range configuration.
edit <id>
set end-ip {ipv4-address}
set lease-time {integer}
set oui-match [disable|enable]
set oui-string <oui-string1>, <oui-string2>, ...
set start-ip {ipv4-address}
set uci-match [disable|enable]
set uci-string <uci-string1>, <uci-string2>, ...
set vci-match [disable|enable]
set vci-string <vci-string1>, <vci-string2>, ...
set vendor {string}
next
end
set ipsec-lease-hold {integer}
set lease-time {integer}
set mac-acl-default-action [assign|block]
set netmask {ipv4-netmask}
set next-server {ipv4-address}
set ntp-server1 {ipv4-address}
set ntp-server2 {ipv4-address}
set ntp-server3 {ipv4-address}
set ntp-service [local|default|...]
config options
Description: DHCP options.
edit <id>
set code {integer}
set ip {user}
set type [hex|string|...]
set uci-match [disable|enable]
set uci-string <uci-string1>, <uci-string2>, ...
set value {string}
set vci-match [disable|enable]
set vci-string <vci-string1>, <vci-string2>, ...
next
end
set relay-agent {ipv4-address}
config reserved-address
Description: Options for the DHCP server to assign IP settings to specific MAC
addresses.
edit <id>
set action [assign|block|...]
set circuit-id {string}
set circuit-id-type [hex|string]
FortiOS 8.0.0 CLI Reference
1546
Fortinet Inc.

<!-- 来源页 1547 -->
set description {var-string}
set ip {ipv4-address}
set mac {mac-address}
set remote-id {string}
set remote-id-type [hex|string]
set type [mac|option82]
next
end
set server-type [regular|ipsec]
set shared-subnet [disable|enable]
set status [disable|enable]
set template {string}
set template-subnet {ipv4-classnet}
set template-subnet-from-interface [disable|enable]
set tftp-server <tftp-server1>, <tftp-server2>, ...
set timezone {string}
set timezone-option [disable|default|...]
set vci-match [disable|enable]
set vci-string <vci-string1>, <vci-string2>, ...
set wifi-ac-service [specify|local]
set wifi-ac1 {ipv4-address}
set wifi-ac2 {ipv4-address}
set wifi-ac3 {ipv4-address}
set wins-server1 {ipv4-address}
set wins-server2 {ipv4-address}
next
end
config system dhcp server
Parameter
Description
Type
Size
Default
auto-configuration
Enable/disable auto configuration.
option
-enable
Option
Description
disable
Disable auto configuration.
enable
Enable auto configuration.
auto-managed-status
Enable/disable use of this DHCP server once
this interface has been assigned an IP
address from FortiIPAM.
option
-enable
Option
Description
disable
Disable use of this DHCP server once this interface has been assigned
an IP address from FortiIPAM.
FortiOS 8.0.0 CLI Reference
1547
Fortinet Inc.

<!-- 来源页 1548 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable use of this DHCP server once this interface has been assigned
an IP address from FortiIPAM.
conflicted-ip-timeout
Time in seconds to wait after a conflicted IP
address is removed from the DHCP range
before it can be reused.
integer
Minimum value:
60 Maximum
value:
8640000
1800
ddns-auth
DDNS authentication mode.
option
-disable
Option
Description
disable
Disable DDNS authentication.
tsig
TSIG based on RFC2845.
ddns-key
DDNS update key (base 64 encoding).
password_
aes256
Not Specified
ddns-keyname
DDNS update key name.
string
Maximum
length: 64
ddns-server-ip
DDNS server IP.
ipv4-address
Not Specified
0.0.0.0
ddns-ttl
TTL.
integer
Minimum value:
60 Maximum
value: 86400
300
ddns-update
Enable/disable DDNS update for DHCP.
option
-disable
Option
Description
disable
Disable DDNS update for DHCP.
enable
Enable DDNS update for DHCP.
ddns-update-override
Enable/disable DDNS update override for
DHCP.
option
-disable
Option
Description
disable
Disable DDNS update override for DHCP.
enable
Enable DDNS update override for DHCP.
ddns-zone
Zone of your domain name (ex. DDNS.com).
string
Maximum
length: 64
default-gateway
Default gateway IP address assigned by the
DHCP server.
ipv4-address
Not Specified
0.0.0.0
FortiOS 8.0.0 CLI Reference
1548
Fortinet Inc.

<!-- 来源页 1549 -->
Parameter
Description
Type
Size
Default
dhcp-settings-from-fortiipam
Enable/disable populating of DHCP server
settings from FortiIPAM.
option
-disable
Option
Description
disable
Disable populating of DHCP server settings from FortiIPAM.
enable
Enable populating of DHCP server settings from FortiIPAM.
dns-server1
DNS server 1.
ipv4-address
Not Specified
0.0.0.0
dns-server2
DNS server 2.
ipv4-address
Not Specified
0.0.0.0
dns-server3
DNS server 3.
ipv4-address
Not Specified
0.0.0.0
dns-server4
DNS server 4.
ipv4-address
Not Specified
0.0.0.0
dns-service
Options for assigning DNS servers to DHCP
clients.
option
-specify
Option
Description
local
IP address of the interface the DHCP server is added to becomes the
client's DNS server IP address.
default
Clients are assigned the FortiGate's configured DNS servers.
specify
Specify up to 3 DNS servers in the DHCP server configuration.
domain
Domain name suffix for the IP addresses that
the DHCP server assigns to clients.
string
Maximum
length: 35
filename
Name of the boot file on the TFTP server.
string
Maximum
length: 127
forticlient-on-net-status
Enable/disable FortiClient-On-Net service
for this DHCP server.
option
-enable
Option
Description
disable
Disable FortiClient On-Net Status.
enable
Enable FortiClient On-Net Status.
id
ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
FortiOS 8.0.0 CLI Reference
1549
Fortinet Inc.

<!-- 来源页 1550 -->
Parameter
Description
Type
Size
Default
interface
DHCP server can assign IP configurations to
clients connected to this interface.
string
Maximum
length: 15
ip-mode
Method used to assign client IP.
option
-range
Option
Description
range
Use range defined by start-ip/end-ip to assign client IP.
usrgrp
Use user-group defined method to assign client IP.
ipsec-lease-hold
DHCP over IPsec leases expire this many
seconds after tunnel down (0 to disable
forced-expiry).
integer
Minimum value:
0 Maximum
value:
8640000
60
lease-time
Lease time in seconds, 0 means unlimited.
integer
Minimum value:
300 Maximum
value:
8640000
604800
mac-acl-default-action
MAC access control default action (allow or
block assigning IP settings).
option
-assign
Option
Description
assign
Allow the DHCP server to assign IP settings to clients on the MAC
access control list.
block
Block the DHCP server from assigning IP settings to clients on the
MAC access control list.
netmask
Netmask assigned by the DHCP server.
ipv4-netmask
Not Specified
0.0.0.0
next-server
IP address of a server, such as a TFTP
server, from which DHCP clients can
download a boot file.
ipv4-address
Not Specified
0.0.0.0
ntp-server1
NTP server 1.
ipv4-address
Not Specified
0.0.0.0
ntp-server2
NTP server 2.
ipv4-address
Not Specified
0.0.0.0
ntp-server3
NTP server 3.
ipv4-address
Not Specified
0.0.0.0
ntp-service
Options for assigning Network Time Protocol
(NTP) servers to DHCP clients.
option
-specify
FortiOS 8.0.0 CLI Reference
1550
Fortinet Inc.

<!-- 来源页 1551 -->
Parameter
Description
Type
Size
Default
Option
Description
local
IP address of the interface the DHCP server is added to becomes the
client's NTP server IP address.
default
Clients are assigned the FortiGate's configured NTP servers.
specify
Specify up to 3 NTP servers in the DHCP server configuration.
relay-agent
Relay agent IP.
ipv4-address
Not Specified
0.0.0.0
server-type
DHCP server can be a normal DHCP server or
an IPsec DHCP server.
option
-regular
Option
Description
regular
Regular DHCP service.
ipsec
DHCP over IPsec service.
shared-subnet
Enable/disable shared subnet.
option
-disable
Option
Description
disable
Disable shared subnet.
enable
Enable shared subnet.
status
Enable/disable this DHCP configuration.
option
-enable
Option
Description
disable
Do not use this DHCP server configuration.
enable
Use this DHCP server configuration.
template *
DHCP template associated with the server.
string
Maximum
length: 35
template-subnet *
Configure template subnet.
ipv4-classnet
Not Specified
0.0.0.0
0.0.0.0
template-subnet-from-interface *
Use interface subnet as DHCP template
subnet.
option
-disable
Option
Description
disable
Disable use of template subnet from interface.
enable
Enable use of template subnet from interface.
FortiOS 8.0.0 CLI Reference
1551
Fortinet Inc.

<!-- 来源页 1552 -->
Parameter
Description
Type
Size
Default
tftp-server
<tftp-server>
One or more hostnames or IP addresses of
the TFTP servers in quotes separated by
spaces.
TFTP server.
string
Maximum
length: 63
timezone
Select the time zone to be assigned to DHCP
clients.
string
Maximum
length: 63
timezone-option
Options for the DHCP server to set the
client's time zone.
option
-disable
Option
Description
disable
Do not set the client's time zone.
default
Clients are assigned the FortiGate's configured time zone.
specify
Specify the time zone to be assigned to DHCP clients.
vci-match
Enable/disable vendor class identifier (VCI)
matching. When enabled only DHCP
requests with a matching VCI are served.
option
-disable
Option
Description
disable
Disable VCI matching.
enable
Enable VCI matching.
vci-string
<vci-string>
One or more VCI strings in quotes separated
by spaces.
VCI strings.
string
Maximum
length: 255
wifi-ac-service
Options for assigning WiFi access controllers
to DHCP clients.
option
-specify
Option
Description
specify
Specify up to 3 WiFi Access Controllers in the DHCP server
configuration.
local
IP address of the interface the DHCP server is added to becomes the
client's WiFi Access Controller IP address.
wifi-ac1
WiFi Access Controller 1 IP address (DHCP
option 138, RFC 5417).
ipv4-address
Not Specified
0.0.0.0
wifi-ac2
WiFi Access Controller 2 IP address (DHCP
option 138, RFC 5417).
ipv4-address
Not Specified
0.0.0.0
wifi-ac3
WiFi Access Controller 3 IP address (DHCP
option 138, RFC 5417).
ipv4-address
Not Specified
0.0.0.0
FortiOS 8.0.0 CLI Reference
1552
Fortinet Inc.

<!-- 来源页 1553 -->
Parameter
Description
Type
Size
Default
wins-server1
WINS server 1.
ipv4-address
Not Specified
0.0.0.0
wins-server2
WINS server 2.
ipv4-address
Not Specified
0.0.0.0
* This parameter may not exist in some models.
config exclude-range
Parameter
Description
Type
Size
Default
end-ip
End of IP range.
ipv4-address
Not Specified
0.0.0.0
id
ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
lease-time
Lease time in seconds, 0 means default lease
time.
integer
Minimum value:
300 Maximum
value:
8640000
0
oui-match *
Enable/disable organizationally unique identifier
(OUI) matching. When enabled only DHCP
requests with a matching OUI are served with
this range.
option
-disable
Option
Description
disable
Disable OUI matching.
enable
Enable OUI matching.
oui-string
<oui-string> *
One or more OUI strings in quotes separated by
spaces (in format of xx:xx:xx).
MAC OUI strings.
string
Maximum
length: 17
start-ip
Start of IP range.
ipv4-address
Not Specified
0.0.0.0
uci-match
Enable/disable user class identifier (UCI)
matching. When enabled only DHCP requests
with a matching UCI are served with this range.
option
-disable
Option
Description
disable
Disable UCI matching.
enable
Enable UCI matching.
FortiOS 8.0.0 CLI Reference
1553
Fortinet Inc.

<!-- 来源页 1554 -->
Parameter
Description
Type
Size
Default
uci-string
<uci-string>
One or more UCI strings in quotes separated by
spaces.
UCI strings.
string
Maximum
length: 255
vci-match
Enable/disable vendor class identifier (VCI)
matching. When enabled only DHCP requests
with a matching VCI are served with this range.
option
-disable
Option
Description
disable
Disable VCI matching.
enable
Enable VCI matching.
vci-string
<vci-string>
One or more VCI strings in quotes separated by
spaces.
VCI strings.
string
Maximum
length: 255
vendor *
Vendor this ip-range will be assigned to.
string
Maximum
length: 255
* This parameter may not exist in some models.
config ip-range
Parameter
Description
Type
Size
Default
end-ip
End of IP range.
ipv4-address
Not Specified
0.0.0.0
id
ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
lease-time
Lease time in seconds, 0 means default lease
time.
integer
Minimum value:
300 Maximum
value:
8640000
0
oui-match *
Enable/disable organizationally unique identifier
(OUI) matching. When enabled only DHCP
requests with a matching OUI are served with
this range.
option
-disable
Option
Description
disable
Disable OUI matching.
enable
Enable OUI matching.
FortiOS 8.0.0 CLI Reference
1554
Fortinet Inc.

<!-- 来源页 1555 -->
Parameter
Description
Type
Size
Default
oui-string
<oui-string> *
One or more OUI strings in quotes separated by
spaces (in format of xx:xx:xx).
MAC OUI strings.
string
Maximum
length: 17
start-ip
Start of IP range.
ipv4-address
Not Specified
0.0.0.0
uci-match
Enable/disable user class identifier (UCI)
matching. When enabled only DHCP requests
with a matching UCI are served with this range.
option
-disable
Option
Description
disable
Disable UCI matching.
enable
Enable UCI matching.
uci-string
<uci-string>
One or more UCI strings in quotes separated by
spaces.
UCI strings.
string
Maximum
length: 255
vci-match
Enable/disable vendor class identifier (VCI)
matching. When enabled only DHCP requests
with a matching VCI are served with this range.
option
-disable
Option
Description
disable
Disable VCI matching.
enable
Enable VCI matching.
vci-string
<vci-string>
One or more VCI strings in quotes separated by
spaces.
VCI strings.
string
Maximum
length: 255
vendor *
Vendor this ip-range will be assigned to.
string
Maximum
length: 255
* This parameter may not exist in some models.
config options
Parameter
Description
Type
Size
Default
code
DHCP option code.
integer
Minimum value:
0 Maximum
value: 255
0
FortiOS 8.0.0 CLI Reference
1555
Fortinet Inc.

<!-- 来源页 1556 -->
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
ip
DHCP option IPs.
user
Not Specified
type
DHCP option type.
option
-hex
Option
Description
hex
DHCP option in hex.
string
DHCP option in string.
ip
DHCP option in IP.
fqdn
DHCP option in domain search option format.
uci-match
Enable/disable user class identifier (UCI)
matching. When enabled only DHCP requests
with a matching UCI are served with this option.
option
-disable
Option
Description
disable
Disable UCI matching.
enable
Enable UCI matching.
uci-string
<uci-string>
One or more UCI strings in quotes separated by
spaces.
UCI strings.
string
Maximum
length: 255
value
DHCP option value.
string
Maximum
length: 312
vci-match
Enable/disable vendor class identifier (VCI)
matching. When enabled only DHCP requests
with a matching VCI are served with this option.
option
-disable
Option
Description
disable
Disable VCI matching.
enable
Enable VCI matching.
vci-string
<vci-string>
One or more VCI strings in quotes separated by
spaces.
VCI strings.
string
Maximum
length: 255
FortiOS 8.0.0 CLI Reference
1556
Fortinet Inc.

<!-- 来源页 1557 -->
config reserved-address
Parameter
Description
Type
Size
Default
action
Options for the DHCP server to
configure the client with the reserved
MAC address.
option
-reserved
Option
Description
assign
Configure the client with this MAC address like any other client.
block
Block the DHCP server from assigning IP settings to the client with this
MAC address.
reserved
Assign the reserved IP address to the client with this MAC address.
circuit-id
Option 82 circuit-ID of the client that
will get the reserved IP address.
string
Maximum
length: 312
circuit-id-type
DHCP option type.
option
-string
Option
Description
hex
DHCP option in hex.
string
DHCP option in string.
description
Description.
var-string
Maximum
length: 255
id
ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
ip
IP address to be reserved for the
MAC address.
ipv4-address
Not Specified
0.0.0.0
mac
MAC address of the client that will get
the reserved IP address.
mac-address
Not Specified
00:00:00:00:00:00
remote-id
Option 82 remote-ID of the client that
will get the reserved IP address.
string
Maximum
length: 312
remote-id-type
DHCP option type.
option
-string
Option
Description
hex
DHCP option in hex.
string
DHCP option in string.
type
DHCP reserved-address type.
option
-mac
FortiOS 8.0.0 CLI Reference
1557
Fortinet Inc.

---


<!-- 来源页 1558 -->
Parameter
Description
Type
Size
Default
Option
Description
mac
Match with MAC address.
option82
Match with DHCP option 82.
config system dhcp template
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
Configure DHCP server templates.
config system dhcp template
Description: Configure DHCP server templates.
edit <name>
set auto-configuration [disable|enable]
set conflicted-ip-timeout {integer}
set ddns-auth [disable|tsig]
set ddns-key {password_aes256}
set ddns-keyname {string}
FortiOS 8.0.0 CLI Reference
1558
Fortinet Inc.

<!-- 来源页 1559 -->
set ddns-server-ip {ipv4-address}
set ddns-ttl {integer}
set ddns-update [disable|enable]
set ddns-update-override [disable|enable]
set ddns-zone {string}
set dns-server1 {ipv4-address}
set dns-server2 {ipv4-address}
set dns-server3 {ipv4-address}
set dns-server4 {ipv4-address}
set dns-service [local|default|...]
set domain {string}
config exclude-range
Description: Exclude one or more ranges of IP addresses from being assigned to
clients.
edit <id>
set ip-count {integer}
set lease-time {integer}
set oui-match [disable|enable]
set oui-string <oui-string1>, <oui-string2>, ...
set start-ip-index {integer}
set uci-match [disable|enable]
set uci-string <uci-string1>, <uci-string2>, ...
set vci-match [disable|enable]
set vci-string <vci-string1>, <vci-string2>, ...
set vendor {string}
next
end
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set filename {string}
set forticlient-on-net-status [disable|enable]
config ip-range
Description: DHCP IP range configuration.
edit <id>
set ip-count {integer}
set lease-time {integer}
set oui-match [disable|enable]
set oui-string <oui-string1>, <oui-string2>, ...
set reserve [disable|enable]
set uci-match [disable|enable]
set uci-string <uci-string1>, <uci-string2>, ...
set vci-match [disable|enable]
set vci-string <vci-string1>, <vci-string2>, ...
set vendor {string}
next
end
set ipsec-lease-hold {integer}
set lease-time {integer}
set mac-acl-default-action [assign|block]
set next-server {ipv4-address}
set ntp-server1 {ipv4-address}
FortiOS 8.0.0 CLI Reference
1559
Fortinet Inc.

<!-- 来源页 1560 -->
set ntp-server2 {ipv4-address}
set ntp-server3 {ipv4-address}
set ntp-service [local|default|...]
config options
Description: DHCP options.
edit <id>
set code {integer}
set ip {user}
set type [hex|string|...]
set uci-match [disable|enable]
set uci-string <uci-string1>, <uci-string2>, ...
set value {string}
set vci-match [disable|enable]
set vci-string <vci-string1>, <vci-string2>, ...
next
end
set relay-agent {ipv4-address}
set reserve-extra-addresses [disable|enable]
config reserved-address
Description: Options for the DHCP server to assign IP settings to specific MAC
addresses.
edit <id>
set action [assign|block|...]
set circuit-id {string}
set circuit-id-type [hex|string]
set description {var-string}
set ip-index {integer}
set mac {mac-address}
set remote-id {string}
set remote-id-type [hex|string]
set type [mac|option82]
next
end
set server-type [regular|ipsec]
set shared-subnet [disable|enable]
set tftp-server <tftp-server1>, <tftp-server2>, ...
set timezone {string}
set timezone-option [disable|default|...]
set uuid {uuid}
set vci-match [disable|enable]
set vci-string <vci-string1>, <vci-string2>, ...
set wifi-ac-service [specify|local]
set wifi-ac1 {ipv4-address}
set wifi-ac2 {ipv4-address}
set wifi-ac3 {ipv4-address}
set wins-server1 {ipv4-address}
set wins-server2 {ipv4-address}
next
end
FortiOS 8.0.0 CLI Reference
1560
Fortinet Inc.

<!-- 来源页 1561 -->
config system dhcp template
Parameter
Description
Type
Size
Default
auto-configuration
Enable/disable auto configuration.
option
-enable
Option
Description
disable
Disable auto configuration.
enable
Enable auto configuration.
conflicted-ip-timeout
Time in seconds to wait after a
conflicted IP address is removed from
the DHCP range before it can be reused.
integer
Minimum
value: 60
Maximum
value:
8640000
1800
ddns-auth
DDNS authentication mode.
option
-disable
Option
Description
disable
Disable DDNS authentication.
tsig
TSIG based on RFC2845.
ddns-key
DDNS update key (base 64 encoding).
password_
aes256
Not
Specified
ddns-keyname
DDNS update key name.
string
Maximum
length: 64
ddns-server-ip
DDNS server IP.
ipv4-address
Not
Specified
0.0.0.0
ddns-ttl
TTL.
integer
Minimum
value: 60
Maximum
value:
86400
300
ddns-update
Enable/disable DDNS update for DHCP.
option
-disable
Option
Description
disable
Disable DDNS update for DHCP.
enable
Enable DDNS update for DHCP.
ddns-update-override
Enable/disable DDNS update override
for DHCP.
option
-disable
FortiOS 8.0.0 CLI Reference
1561
Fortinet Inc.

<!-- 来源页 1562 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable DDNS update override for DHCP.
enable
Enable DDNS update override for DHCP.
ddns-zone
Zone of your domain name (ex.
DDNS.com).
string
Maximum
length: 64
dns-server1
DNS server 1.
ipv4-address
Not
Specified
0.0.0.0
dns-server2
DNS server 2.
ipv4-address
Not
Specified
0.0.0.0
dns-server3
DNS server 3.
ipv4-address
Not
Specified
0.0.0.0
dns-server4
DNS server 4.
ipv4-address
Not
Specified
0.0.0.0
dns-service
Options for assigning DNS servers to
DHCP clients.
option
-default
Option
Description
local
IP address of the interface the DHCP server is added to becomes the
client's DNS server IP address.
default
Clients are assigned the FortiGate's configured DNS servers.
specify
Specify up to 3 DNS servers in the DHCP server configuration.
domain
Domain name suffix for the IP addresses
that the DHCP server assigns to clients.
string
Maximum
length: 35
fabric-force-sync
Enable/disable forced synchronization
of configuration objects from the root
FortiGate unit to the downstream
devices. Configuration conflict check is
skipped.
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
Security Fabric global object setting.
option
-disable
FortiOS 8.0.0 CLI Reference
1562
Fortinet Inc.

<!-- 来源页 1563 -->
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
fabric-object-source
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
filename
Name of the boot file on the TFTP
server.
string
Maximum
length: 127
forticlient-on-net-status
Enable/disable FortiClient-On-Net
service for this DHCP server.
option
-enable
Option
Description
disable
Disable FortiClient On-Net Status.
enable
Enable FortiClient On-Net Status.
ipsec-lease-hold
DHCP over IPsec leases expire this many
seconds after tunnel down (0 to disable
forced-expiry).
integer
Minimum
value: 0
Maximum
value:
8640000
60
lease-time
Lease time in seconds, 0 means
unlimited.
integer
Minimum
value: 300
Maximum
value:
8640000
604800
mac-acl-default-action
MAC access control default action (allow
or block assigning IP settings).
option
-assign
Option
Description
assign
Allow the DHCP server to assign IP settings to clients on the MAC
access control list.
block
Block the DHCP server from assigning IP settings to clients on the
MAC access control list.
FortiOS 8.0.0 CLI Reference
1563
Fortinet Inc.

<!-- 来源页 1564 -->
Parameter
Description
Type
Size
Default
name
DHCP server template name.
string
Maximum
length: 35
next-server
IP address of a server, such as a TFTP
server, from which DHCP clients can
download a boot file.
ipv4-address
Not
Specified
0.0.0.0
ntp-server1
NTP server 1.
ipv4-address
Not
Specified
0.0.0.0
ntp-server2
NTP server 2.
ipv4-address
Not
Specified
0.0.0.0
ntp-server3
NTP server 3.
ipv4-address
Not
Specified
0.0.0.0
ntp-service
Options for assigning Network Time
Protocol (NTP) servers to DHCP clients.
option
-default
Option
Description
local
IP address of the interface the DHCP server is added to becomes the
client's NTP server IP address.
default
Clients are assigned the FortiGate's configured NTP servers.
specify
Specify up to 3 NTP servers in the DHCP server configuration.
relay-agent
Relay agent IP.
ipv4-address
Not
Specified
0.0.0.0
reserve-extra-addresses
Enable/disable reservation of the extra
IP addresses in the subnet.
option
-disable
Option
Description
disable
Disable reservation of the extra IP addresses in the subnet.
enable
Enable reservation of the extra IP addresses in the subnet.
server-type
DHCP server can be a normal DHCP
server or an IPsec DHCP server.
option
-regular
Option
Description
regular
Regular DHCP service.
ipsec
DHCP over IPsec service.
shared-subnet
Enable/disable shared subnet.
option
-disable
FortiOS 8.0.0 CLI Reference
1564
Fortinet Inc.

<!-- 来源页 1565 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable shared subnet.
enable
Enable shared subnet.
tftp-server
<tftp-server>
One or more hostnames or IP addresses
of the TFTP servers in quotes separated
by spaces.
TFTP server.
string
Maximum
length: 63
timezone
Select the time zone to be assigned to
DHCP clients.
string
Maximum
length: 63
timezone-option
Options for the DHCP server to set the
client's time zone.
option
-disable
Option
Description
disable
Do not set the client's time zone.
default
Clients are assigned the FortiGate's configured time zone.
specify
Specify the time zone to be assigned to DHCP clients.
uuid
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
vci-match
Enable/disable vendor class identifier
(VCI) matching. When enabled only
DHCP requests with a matching VCI are
served.
option
-disable
Option
Description
disable
Disable VCI matching.
enable
Enable VCI matching.
vci-string
<vci-string>
One or more VCI strings in quotes
separated by spaces.
VCI strings.
string
Maximum
length: 255
wifi-ac-service
Options for assigning WiFi access
controllers to DHCP clients.
option
-specify
Option
Description
specify
Specify up to 3 WiFi Access Controllers in the DHCP server
configuration.
FortiOS 8.0.0 CLI Reference
1565
Fortinet Inc.

<!-- 来源页 1566 -->
Parameter
Description
Type
Size
Default
Option
Description
local
IP address of the interface the DHCP server is added to becomes the
client's WiFi Access Controller IP address.
wifi-ac1
WiFi Access Controller 1 IP address
(DHCP option 138, RFC 5417).
ipv4-address
Not
Specified
0.0.0.0
wifi-ac2
WiFi Access Controller 2 IP address
(DHCP option 138, RFC 5417).
ipv4-address
Not
Specified
0.0.0.0
wifi-ac3
WiFi Access Controller 3 IP address
(DHCP option 138, RFC 5417).
ipv4-address
Not
Specified
0.0.0.0
wins-server1
WINS server 1.
ipv4-address
Not
Specified
0.0.0.0
wins-server2
WINS server 2.
ipv4-address
Not
Specified
0.0.0.0
config exclude-range
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
ip-count
Number of IP addresses to include in the range.
integer
Minimum value:
1 Maximum
value:
16777216
0
lease-time
Lease time in seconds, 0 means default lease
time.
integer
Minimum value:
300 Maximum
value:
8640000
0
oui-match
Enable/disable organizationally unique identifier
(OUI) matching. When enabled only DHCP
requests with a matching OUI are served with
this range.
option
-disable
Option
Description
disable
Disable OUI matching.
enable
Enable OUI matching.
FortiOS 8.0.0 CLI Reference
1566
Fortinet Inc.

<!-- 来源页 1567 -->
Parameter
Description
Type
Size
Default
oui-string
<oui-string>
One or more OUI strings in quotes separated by
spaces (in format of xx:xx:xx).
MAC OUI strings.
string
Maximum
length: 17
start-ip-index
Start of IP range.
integer
Minimum value:
1 Maximum
value:
16777216
0
uci-match
Enable/disable user class identifier (UCI)
matching. When enabled only DHCP requests
with a matching UCI are served with this range.
option
-disable
Option
Description
disable
Disable UCI matching.
enable
Enable UCI matching.
uci-string
<uci-string>
One or more UCI strings in quotes separated by
spaces.
UCI strings.
string
Maximum
length: 255
vci-match
Enable/disable vendor class identifier (VCI)
matching. When enabled only DHCP requests
with a matching VCI are served with this range.
option
-disable
Option
Description
disable
Disable VCI matching.
enable
Enable VCI matching.
vci-string
<vci-string>
One or more VCI strings in quotes separated by
spaces.
VCI strings.
string
Maximum
length: 255
vendor
Vendor this ip-range will be assigned to.
string
Maximum
length: 255
config ip-range
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
FortiOS 8.0.0 CLI Reference
1567
Fortinet Inc.

<!-- 来源页 1568 -->
Parameter
Description
Type
Size
Default
ip-count
Number of IP addresses to include in the range.
integer
Minimum value:
1 Maximum
value:
16777216
0
lease-time
Lease time in seconds, 0 means default lease
time.
integer
Minimum value:
300 Maximum
value:
8640000
0
oui-match
Enable/disable organizationally unique identifier
(OUI) matching. When enabled only DHCP
requests with a matching OUI are served with
this range.
option
-disable
Option
Description
disable
Disable OUI matching.
enable
Enable OUI matching.
oui-string
<oui-string>
One or more OUI strings in quotes separated by
spaces (in format of xx:xx:xx).
MAC OUI strings.
string
Maximum
length: 17
reserve
Enable/disable address reservation for use
without DHCP.
option
-disable
Option
Description
disable
Disable range reservation. Create an ip-range when applying the
template.
enable
Enable range reservation. Skip over these IPs when applying the
template.
uci-match
Enable/disable user class identifier (UCI)
matching. When enabled only DHCP requests
with a matching UCI are served with this range.
option
-disable
Option
Description
disable
Disable UCI matching.
enable
Enable UCI matching.
uci-string
<uci-string>
One or more UCI strings in quotes separated by
spaces.
UCI strings.
string
Maximum
length: 255
FortiOS 8.0.0 CLI Reference
1568
Fortinet Inc.

<!-- 来源页 1569 -->
Parameter
Description
Type
Size
Default
vci-match
Enable/disable vendor class identifier (VCI)
matching. When enabled only DHCP requests
with a matching VCI are served with this range.
option
-disable
Option
Description
disable
Disable VCI matching.
enable
Enable VCI matching.
vci-string
<vci-string>
One or more VCI strings in quotes separated by
spaces.
VCI strings.
string
Maximum
length: 255
vendor
Vendor this ip-range will be assigned to.
string
Maximum
length: 255
config options
Parameter
Description
Type
Size
Default
code
DHCP option code.
integer
Minimum value:
0 Maximum
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
ip
DHCP option IPs.
user
Not Specified
type
DHCP option type.
option
-hex
Option
Description
hex
DHCP option in hex.
string
DHCP option in string.
ip
DHCP option in IP.
fqdn
DHCP option in domain search option format.
uci-match
Enable/disable user class identifier (UCI)
matching. When enabled only DHCP requests
with a matching UCI are served with this option.
option
-disable
Option
Description
disable
Disable UCI matching.
enable
Enable UCI matching.
FortiOS 8.0.0 CLI Reference
1569
Fortinet Inc.

<!-- 来源页 1570 -->
Parameter
Description
Type
Size
Default
uci-string
<uci-string>
One or more UCI strings in quotes separated by
spaces.
UCI strings.
string
Maximum
length: 255
value
DHCP option value.
string
Maximum
length: 312
vci-match
Enable/disable vendor class identifier (VCI)
matching. When enabled only DHCP requests
with a matching VCI are served with this option.
option
-disable
Option
Description
disable
Disable VCI matching.
enable
Enable VCI matching.
vci-string
<vci-string>
One or more VCI strings in quotes separated by
spaces.
VCI strings.
string
Maximum
length: 255
config reserved-address
Parameter
Description
Type
Size
Default
action
Options for the DHCP server to
configure the client with the reserved
MAC address.
option
-reserved
Option
Description
assign
Configure the client with this MAC address like any other client.
block
Block the DHCP server from assigning IP settings to the client with this
MAC address.
reserved
Assign the reserved IP address to the client with this MAC address.
circuit-id
Option 82 circuit-ID of the client that
will get the reserved IP address.
string
Maximum
length: 312
circuit-id-type
DHCP option type.
option
-string
Option
Description
hex
DHCP option in hex.
string
DHCP option in string.
description
Description.
var-string
Maximum
length: 255
FortiOS 8.0.0 CLI Reference
1570
Fortinet Inc.

---


<!-- 来源页 1571 -->
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
ip-index
Index of IP address to be reserved for
the MAC address.
integer
Minimum value:
1 Maximum
value:
16777216
0
mac
MAC address of the client that will get
the reserved IP address.
mac-address
Not Specified
00:00:00:00:00:00
remote-id
Option 82 remote-ID of the client that
will get the reserved IP address.
string
Maximum
length: 312
remote-id-type
DHCP option type.
option
-string
Option
Description
hex
DHCP option in hex.
string
DHCP option in string.
type
DHCP reserved-address type.
option
-mac
Option
Description
mac
Match with MAC address.
option82
Match with DHCP option 82.
config system dhcp6 server
Configure DHCPv6 servers.
config system dhcp6 server
Description: Configure DHCPv6 servers.
edit <id>
set delegated-prefix-iaid {integer}
set delegated-prefix-route [disable|enable]
set dns-search-list [delegated|specify]
set dns-server1 {ipv6-address}
set dns-server2 {ipv6-address}
set dns-server3 {ipv6-address}
set dns-server4 {ipv6-address}
set dns-service [delegated|default|...]
set domain {string}
set interface {string}
FortiOS 8.0.0 CLI Reference
1571
Fortinet Inc.

<!-- 来源页 1572 -->
set ip-mode [range|delegated]
config ip-range
Description: DHCP IP range configuration.
edit <id>
set end-ip {ipv6-address}
set start-ip {ipv6-address}
set vci-match [disable|enable]
set vci-string <vci-string1>, <vci-string2>, ...
next
end
set lease-time {integer}
config options
Description: DHCPv6 options.
edit <id>
set code {integer}
set ip6 {user}
set type [hex|string|...]
set value {string}
set vci-match [disable|enable]
set vci-string <vci-string1>, <vci-string2>, ...
next
end
set prefix-mode [dhcp6|ra]
config prefix-range
Description: DHCP prefix configuration.
edit <id>
set end-prefix {ipv6-address}
set prefix-length {integer}
set start-prefix {ipv6-address}
next
end
set rapid-commit [disable|enable]
set status [disable|enable]
set subnet {ipv6-prefix}
set upstream-interface {string}
next
end
config system dhcp6 server
Parameter
Description
Type
Size
Default
delegated-prefix-iaid
IAID of obtained delegated-prefix from the
upstream interface.
integer
Minimum value:
0 Maximum
value:
4294967295
0
delegated-prefix-route
Enable/disable automatically adding of routing
for delegated prefix.
option
-disable
FortiOS 8.0.0 CLI Reference
1572
Fortinet Inc.

<!-- 来源页 1573 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable automatically adding of routing for delegated prefix.
enable
Enable automatically adding of routing for delegated prefix.
dns-search-list
DNS search list options.
option
-specify
Option
Description
delegated
Delegated the DNS search list.
specify
Specify the DNS search list.
dns-server1
DNS server 1.
ipv6-address
Not Specified
::
dns-server2
DNS server 2.
ipv6-address
Not Specified
::
dns-server3
DNS server 3.
ipv6-address
Not Specified
::
dns-server4
DNS server 4.
ipv6-address
Not Specified
::
dns-service
Options for assigning DNS servers to DHCPv6
clients.
option
-specify
Option
Description
delegated
Delegated DNS settings.
default
Clients are assigned the FortiGate's configured DNS servers.
specify
Specify up to 3 DNS servers in the DHCPv6 server configuration.
domain
Domain name suffix for the IP addresses that the
DHCP server assigns to clients.
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
interface
DHCP server can assign IP configurations to
clients connected to this interface.
string
Maximum
length: 15
ip-mode
Method used to assign client IP.
option
-range
FortiOS 8.0.0 CLI Reference
1573
Fortinet Inc.

<!-- 来源页 1574 -->
Parameter
Description
Type
Size
Default
Option
Description
range
Use range defined by start IP/end IP to assign client IP.
delegated
Use delegated prefix method to assign client IP.
lease-time
Lease time in seconds, 0 means unlimited.
integer
Minimum value:
300 Maximum
value:
8640000
604800
prefix-mode
Assigning a prefix from a DHCPv6 client or RA.
option
-dhcp6
Option
Description
dhcp6
Use delegated prefix from a DHCPv6 client.
ra
Use prefix from RA.
rapid-commit
Enable/disable allow/disallow rapid commit.
option
-disable
Option
Description
disable
Do not allow rapid commit.
enable
Allow rapid commit.
status
Enable/disable this DHCPv6 configuration.
option
-enable
Option
Description
disable
Enable this DHCPv6 server configuration.
enable
Disable this DHCPv6 server configuration.
subnet
Subnet or subnet-id if the IP mode is delegated.
ipv6-prefix
Not Specified
::/0
upstream-interface
Interface name from where delegated
information is provided.
string
Maximum
length: 15
config ip-range
Parameter
Description
Type
Size
Default
end-ip
End of IP range.
ipv6-address
Not Specified
::
id
ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
FortiOS 8.0.0 CLI Reference
1574
Fortinet Inc.

<!-- 来源页 1575 -->
Parameter
Description
Type
Size
Default
start-ip
Start of IP range.
ipv6-address
Not Specified
::
vci-match
Enable/disable vendor class option matching.
When enabled only DHCP requests with a
matching VC are served with this range.
option
-disable
Option
Description
disable
Disable VCI matching.
enable
Enable VCI matching.
vci-string
<vci-string>
One or more VCI strings in quotes separated by
spaces.
VCI strings.
string
Maximum
length: 255
config options
Parameter
Description
Type
Size
Default
code
DHCPv6 option code.
integer
Minimum value:
0 Maximum
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
ip6
DHCP option IP6s.
user
Not Specified
type
DHCPv6 option type.
option
-hex
Option
Description
hex
DHCPv6 option in hex.
string
DHCPv6 option in string.
ip6
DHCPv6 option in IP6.
fqdn
DHCPv6 option in domain search option format.
value
DHCPv6 option value (hexadecimal value must
be even).
string
Maximum
length: 312
vci-match
Enable/disable vendor class option matching.
When enabled only DHCP requests with a
matching VCI are served with this option.
option
-disable
FortiOS 8.0.0 CLI Reference
1575
Fortinet Inc.

<!-- 来源页 1576 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable VCI matching.
enable
Enable VCI matching.
vci-string
<vci-string>
One or more VCI strings in quotes separated by
spaces.
VCI strings.
string
Maximum
length: 255
config prefix-range
Parameter
Description
Type
Size
Default
end-prefix
End of prefix range.
ipv6-address
Not Specified
::
id
ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
prefix-length
Prefix length.
integer
Minimum value:
1 Maximum
value: 128
0
start-prefix
Start of prefix range.
ipv6-address
Not Specified
::
FortiOS 8.0.0 CLI Reference
1576
Fortinet Inc.

---


<!-- 来源页 1581 -->
Parameter
Description
Type
Size
Default
Option
Description
odd
Odd parity check.
even
Even parity check.
term-stopbits
Term Stop Bits.
integer
Minimum
value: 0
Maximum
value:
65535
1
config system dns
Configure DNS.
config system dns
Description: Configure DNS.
set alt-primary {ipv4-address}
set alt-secondary {ipv4-address}
set cache-notfound-responses [disable|enable]
set dns-cache-limit {integer}
set dns-cache-ttl {integer}
set domain <domain1>, <domain2>, ...
set fqdn-cache-ttl {integer}
set fqdn-max-refresh {integer}
set fqdn-min-refresh {integer}
set hostname-limit {integer}
set hostname-ttl {integer}
set interface {string}
set interface-select-method [auto|sdwan|...]
set ip6-primary {ipv6-address}
set ip6-secondary {ipv6-address}
set log [disable|error|...]
set primary {ipv4-address}
set protocol {option1}, {option2}, ...
set retry {integer}
set root-servers {user}
set secondary {ipv4-address}
set server-hostname <hostname1>, <hostname2>, ...
set server-select-method [least-rtt|failover]
set source-ip {ipv4-address}
set source-ip-interface {string}
set ssl-certificate {string}
set timeout {integer}
set vrf-select {integer}
end
FortiOS 8.0.0 CLI Reference
1581
Fortinet Inc.

<!-- 来源页 1582 -->
config system dns
Parameter
Description
Type
Size
Default
alt-primary
Alternate primary DNS server. This is not used
as a failover DNS server.
ipv4-address
Not Specified
0.0.0.0
alt-secondary
Alternate secondary DNS server. This is not
used as a failover DNS server.
ipv4-address
Not Specified
0.0.0.0
cache-notfound-responses
Enable/disable response from the DNS server
when a record is not in cache.
option
-disable
Option
Description
disable
Disable cache NOTFOUND responses from DNS server.
enable
Enable cache NOTFOUND responses from DNS server.
dns-cache-limit
Maximum number of records in the DNS cache.
integer
Minimum value:
0 Maximum
value:
4294967295
5000
dns-cache-ttl
Duration in seconds that the DNS cache retains
information.
integer
Minimum value:
60 Maximum
value: 86400
1800
domain
<domain>
Search suffix list for hostname lookup.
DNS search domain list separated by space
(maximum 8 domains).
string
Maximum
length: 127
fqdn-cache-ttl
FQDN cache time to live in seconds (0 - 86400,
default = 0).
integer
Minimum value:
0 Maximum
value: 86400
0
fqdn-max-refresh
FQDN cache maximum refresh time in seconds
(3600 - 86400, default = 3600).
integer
Minimum value:
3600 Maximum
value: 86400
3600
fqdn-min-refresh
FQDN cache minimum refresh time in seconds
(10 - 3600, default = 60).
integer
Minimum value:
10 Maximum
value: 3600
60
hostname-limit
Limit of the number of hostname table entries
(0 - 50000).
integer
Minimum value:
0 Maximum
value: 50000
5000
hostname-ttl
TTL of hostname table entries (60 - 86400).
integer
Minimum value:
60 Maximum
value: 86400
86400
interface
Specify outgoing interface to reach server.
string
Maximum
length: 15
FortiOS 8.0.0 CLI Reference
1582
Fortinet Inc.

<!-- 来源页 1583 -->
Parameter
Description
Type
Size
Default
interface-select-method
Specify how to select outgoing interface to
reach server.
option
-auto
Option
Description
auto
Set outgoing interface automatically.
sdwan
Set outgoing interface by SD-WAN or policy routing rules.
specify
Set outgoing interface manually.
ip6-primary
Primary DNS server IPv6 address.
ipv6-address
Not Specified
::
ip6-secondary
Secondary DNS server IPv6 address.
ipv6-address
Not Specified
::
log
Local DNS log setting.
option
-disable
Option
Description
disable
Disable.
error
Enable local DNS error log.
all
Enable local DNS log.
primary
Primary DNS server IP address.
ipv4-address
Not Specified
0.0.0.0
protocol
DNS transport protocols.
option
-cleartext
Option
Description
cleartext
DNS over UDP/53, DNS over TCP/53.
dot
DNS over TLS/853.
doh
DNS over HTTPS/443.
retry
Number of times to retry (0 - 5).
integer
Minimum value:
0 Maximum
value: 5
2
root-servers
Configure up to two preferred servers that
serve the DNS root zone (default uses all 13
root servers).
user
Not Specified
secondary
Secondary DNS server IP address.
ipv4-address
Not Specified
0.0.0.0
FortiOS 8.0.0 CLI Reference
1583
Fortinet Inc.

---


<!-- 来源页 1584 -->
Parameter
Description
Type
Size
Default
server-hostname
<hostname>
DNS server host name list.
DNS server host name list separated by space
(maximum 4 domains).
string
Maximum
length: 127
server-select-method
Specify how configured servers are prioritized.
option
-least-rtt
Option
Description
least-rtt
Select servers based on least round trip time.
failover
Select servers based on the order they are configured.
source-ip
IP address used by the DNS server as its source
IP.
ipv4-address
Not Specified
0.0.0.0
source-ip-interface
IP address of the specified interface as the
source IP address.
string
Maximum
length: 15
ssl-certificate
Name of local certificate for SSL connections.
string
Maximum
length: 35
Fortinet_
Factory
timeout
DNS query timeout interval in seconds (1 - 10).
integer
Minimum value:
1 Maximum
value: 10
5
vrf-select
VRF ID used for connection to server.
integer
Minimum value:
0 Maximum
value: 511
0
config system dns64
Configure DNS64.
config system dns64
Description: Configure DNS64.
set always-synthesize-aaaa-record [enable|disable]
set dns64-prefix {ipv6-prefix}
set status [enable|disable]
end
FortiOS 8.0.0 CLI Reference
1584
Fortinet Inc.

---


<!-- 来源页 1585 -->
config system dns64
Parameter
Description
Type
Size
Default
always-synthesize-aaaa-record
Enable/disable AAAA record synthesis (default =
enable).
option
-enable
Option
Description
enable
Enable AAAA record synthesis.
disable
Disable AAAA record synthesis.
dns64-prefix
DNS64 prefix must be ::/96 (default =
64:ff9b::/96).
ipv6-prefix
Not
Specified
64:ff9b::/96
status
Enable/disable DNS64 (default = disable).
option
-disable
Option
Description
enable
Enable DNS64.
disable
Disable DNS64.
config system dns-database
Configure DNS databases.
config system dns-database
Description: Configure DNS databases.
edit <name>
set allow-transfer {user}
set authoritative [enable|disable]
set contact {string}
config dns-entry
Description: DNS entry.
edit <id>
set canonical-name {string}
set hostname {string}
set ip {ipv4-address-any}
set ipv6 {ipv6-address}
set preference {integer}
set status [enable|disable]
set ttl {integer}
set type [A|NS|...]
next
end
set domain {string}
set forwarder {user}
set forwarder6 {ipv6-address}
FortiOS 8.0.0 CLI Reference
1585
Fortinet Inc.

<!-- 来源页 1586 -->
set interface {string}
set interface-select-method [auto|sdwan|...]
set ip-primary {ipv4-address-any}
set primary-name {string}
set rr-max {integer}
set source-ip {ipv4-address}
set source-ip-interface {string}
set source-ip6 {ipv6-address}
set status [enable|disable]
set ttl {integer}
set type [primary|secondary]
set view [shadow|public|...]
set vrf-select {integer}
next
end
config system dns-database
Parameter
Description
Type
Size
Default
allow-transfer
DNS zone transfer IP address list.
user
Not Specified
authoritative
Enable/disable authoritative zone.
option
-enable
Option
Description
enable
Enable authoritative zone.
disable
Disable authoritative zone.
contact
Email address of the administrator for this
zone. You can specify only the username, such
as admin or the full email address, such as
admin@test.com When using only a username,
the domain of the email will be this zone.
string
Maximum
length: 255
host
domain
Domain name.
string
Maximum
length: 255
forwarder
DNS zone forwarder IP address list.
user
Not Specified
forwarder6
Forwarder IPv6 address.
ipv6-address
Not Specified
::
interface
Specify outgoing interface to reach server.
string
Maximum
length: 15
interface-select-method
Specify how to select outgoing interface to
reach server.
option
-auto
FortiOS 8.0.0 CLI Reference
1586
Fortinet Inc.

<!-- 来源页 1587 -->
Parameter
Description
Type
Size
Default
Option
Description
auto
Set outgoing interface automatically.
sdwan
Set outgoing interface by SD-WAN or policy routing rules.
specify
Set outgoing interface manually.
ip-primary
IP address of primary DNS server. Entries in
this primary DNS server and imported into the
DNS zone.
ipv4-address-any
Not Specified
0.0.0.0
name
Zone name.
string
Maximum
length: 35
primary-name
Domain name of the default DNS server for
this zone.
string
Maximum
length: 255
dns
rr-max
Maximum number of resource records (10 -65536, 0 means infinite).
integer
Minimum
value: 10
Maximum
value: 65536
16384
source-ip
Source IP for forwarding to DNS server.
ipv4-address
Not Specified
0.0.0.0
source-ip-interface
IP address of the specified interface as the
source IP address.
string
Maximum
length: 15
source-ip6
IPv6 source IP address for forwarding to DNS
server.
ipv6-address
Not Specified
::
status
Enable/disable this DNS zone.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
ttl
Default time-to-live value for the entries of this
DNS zone (0 - 2147483647 sec, default =
86400).
integer
Minimum
value: 0
Maximum
value:
2147483647
86400
type
Zone type (primary to manage entries directly,
secondary to import entries from other zones).
option
-primary
Option
Description
primary
Primary DNS zone, to manage entries directly.
secondary
Secondary DNS zone, to import entries from other DNS zones.
FortiOS 8.0.0 CLI Reference
1587
Fortinet Inc.

<!-- 来源页 1588 -->
Parameter
Description
Type
Size
Default
view
Zone view (public to serve public clients,
shadow to serve internal clients).
option
-shadow
Option
Description
shadow
Shadow DNS zone to serve internal clients.
public
Public DNS zone to serve public clients.
shadow-ztna
implicit DNS zone for ztna dox tunnel.
proxy
Shadow DNS zone for internal proxy.
vrf-select
VRF ID used for connection to server.
integer
Minimum
value: 0
Maximum
value: 511
0
config dns-entry
Parameter
Description
Type
Size
Default
canonical-name
Canonical name of the host.
string
Maximum
length: 255
hostname
Name of the host.
string
Maximum
length: 255
id
DNS entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
ip
IPv4 address of the host.
ipv4-address-any
Not Specified
0.0.0.0
ipv6
IPv6 address of the host.
ipv6-address
Not Specified
::
preference
DNS entry preference (0 - 65535, highest
preference = 0, default = 10).
integer
Minimum value:
0 Maximum
value: 65535
10
status
Enable/disable resource record status.
option
-enable
Option
Description
enable
Enable resource record status.
disable
Disable resource record status.
FortiOS 8.0.0 CLI Reference
1588
Fortinet Inc.

---


<!-- 来源页 1589 -->
Parameter
Description
Type
Size
Default
ttl
Time-to-live for this entry (0 to 2147483647
sec, default = 0).
integer
Minimum value:
0 Maximum
value:
2147483647
0
type
Resource record type.
option
-A
Option
Description
A
Host type.
NS
Name server type.
CNAME
Canonical name type.
MX
Mail exchange type.
AAAA
IPv6 host type.
PTR
Pointer type.
PTR_V6
IPv6 pointer type.
config system dns-server
Configure DNS servers.
config system dns-server
Description: Configure DNS servers.
edit <name>
set dnsfilter-profile {string}
set doh [enable|disable]
set doh3 [enable|disable]
set doq [enable|disable]
set mode [recursive|non-recursive|...]
set ssl-cert {string}
next
end
config system dns-server
Parameter
Description
Type
Size
Default
dnsfilter-profile
DNS filter profile.
string
Maximum
length: 47
doh
Enable/disable DNS over HTTPS/443 (default =
disable).
option
-disable
FortiOS 8.0.0 CLI Reference
1589
Fortinet Inc.

---


<!-- 来源页 1634 -->
Parameter
Description
Type
Size
Default
id
ID of individual entry in the IPv6 range table.
integer
Minimum
value: 0
Maximum
value:
65535
0
start-ip
Starting IP address, inclusive, of the address range
(format: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx).
ipv6-address
Not
Specified
::
config system global
Configure global attributes.
config system global
Description: Configure global attributes.
set admin-ble-button [enable|disable]
set admin-concurrent [enable|disable]
set admin-console-timeout {integer}
set admin-forticloud-sso-default-profile {string}
set admin-forticloud-sso-login [enable|disable]
set admin-host {string}
set admin-hsts-max-age {integer}
set admin-http-rate-limit-exempt-auth [enable|disable]
set admin-http-rate-limit-max-requests {integer}
set admin-http-request-body-timeout {integer}
set admin-http-request-header-timeout {integer}
set admin-http-unauthenticated-request-body-timeout {integer}
set admin-https-pki-required [enable|disable]
set admin-https-redirect [enable|disable]
set admin-https-ssl-banned-ciphers {option1}, {option2}, ...
set admin-https-ssl-ciphersuites {option1}, {option2}, ...
set admin-https-ssl-versions {option1}, {option2}, ...
set admin-lockout-duration {integer}
set admin-lockout-threshold {integer}
set admin-login-max {integer}
set admin-port {integer}
set admin-reset-button [enable|disable]
set admin-restrict-local [all|non-console-only|...]
set admin-scp [enable|disable]
set admin-server-cert {string}
set admin-sport {integer}
set admin-ssh-grace-time {integer}
set admin-ssh-password [enable|disable]
set admin-ssh-port {integer}
set admin-ssh-v1 [enable|disable]
set admin-telnet [enable|disable]
set admin-telnet-port {integer}
set admintimeout {integer}
FortiOS 8.0.0 CLI Reference
1634
Fortinet Inc.

<!-- 来源页 1635 -->
set airplane-mode [enable|disable]
set alias {string}
set allow-traffic-redirect [enable|disable]
set anti-replay [disable|loose|...]
set application-bandwidth-tracking [disable|enable]
set arp-max-entry {integer}
set auth-cert {string}
set auth-http-port {integer}
set auth-https-port {integer}
set auth-ike-saml-port {integer}
set auth-keepalive [enable|disable]
set auth-session-auto-backup [enable|disable]
set auth-session-auto-backup-interval [1min|5min|...]
set auth-session-limit [block-new|logout-inactive]
set auto-auth-extension-device [enable|disable]
set autorun-log-fsck [enable|disable]
set av-affinity {string}
set av-failopen [pass|off|...]
set av-failopen-session [enable|disable]
set batch-cmdb [enable|disable]
set bfd-affinity {string}
set block-session-timer {integer}
set br-fdb-max-entry {integer}
set cert-chain-max {integer}
set cfg-revert-timeout {integer}
set cfg-save [automatic|manual|...]
set check-protocol-header [loose|strict]
set check-reset-range [strict|disable]
set cli-audit-log [enable|disable]
set cloud-communication [enable|disable]
set clt-cert-req [enable|disable]
set cmdbsvr-affinity {string}
set cpu-use-threshold {integer}
set csr-ca-attribute [enable|disable]
set daily-restart [enable|disable]
set default-service-source-port {user}
set delay-tcp-npu-session [enable|disable]
set device-idle-timeout {integer}
set dh-params [1024|1536|...]
set dhcp-lease-backup-interval {integer}
set dnsproxy-worker-count {integer}
set early-tcp-npu-session [enable|disable]
set edit-vdom-prompt [enable|disable]
set extender-controller-reserved-network {ipv4-classnet-host}
set failtime {integer}
set faz-disk-buffer-size {integer}
set fds-statistics [enable|disable]
set fds-statistics-period {integer}
set fgd-alert-subscription {option1}, {option2}, ...
set forticonverter-config-upload [once|disable]
set forticonverter-integration [enable|disable]
set fortiextender [disable|enable]
FortiOS 8.0.0 CLI Reference
1635
Fortinet Inc.

<!-- 来源页 1636 -->
set fortiextender-data-port {integer}
set fortiextender-discovery-lockdown [disable|enable]
set fortiextender-provision-on-authorization [enable|disable]
set fortiextender-vlan-mode [enable|disable]
set fortigslb-integration [disable|enable]
set fortiservice-port {integer}
set fortitoken-cloud [enable|disable]
set fortitoken-cloud-push-status [enable|disable]
set fortitoken-cloud-region {string}
set fortitoken-cloud-sync-interval {integer}
set geoip-full-db [enable|disable]
set gtpu-dynamic-source-port [enable|disable]
set gui-allow-incompatible-fabric-fgt [enable|disable]
set gui-app-detection-sdwan [enable|disable]
set gui-auto-upgrade-setup-warning [enable|disable]
set gui-cdn-domain-override {string}
set gui-cdn-usage [enable|disable]
set gui-certificates [enable|disable]
set gui-custom-language [enable|disable]
set gui-custom-theme {string}
set gui-date-format [yyyy/MM/dd|dd/MM/yyyy|...]
set gui-date-time-source [system|browser]
set gui-device-latitude {string}
set gui-device-longitude {string}
set gui-display-hostname [enable|disable]
set gui-firmware-upgrade-warning [enable|disable]
set gui-forticare-registration-setup-warning [enable|disable]
set gui-fortigate-cloud-sandbox [enable|disable]
set gui-ipv6 [enable|disable]
set gui-local-out [enable|disable]
set gui-login-request-rate-limit {integer}
set gui-replacement-message-groups [enable|disable]
set gui-rest-api-cache [enable|disable]
set gui-restrict-theme-change [enable|disable]
set gui-theme [jade|neutrino|...]
set gui-wireless-opensecurity [enable|disable]
set gui-workflow-management [enable|disable]
set ha-affinity {string}
set honor-df [enable|disable]
set hostname {string}
set http-request-limit {integer}
set http-unauthenticated-request-limit {integer}
set httpd-max-worker-count {integer}
set hyper-scale-vdom-num {integer}
set igmp-state-limit {integer}
set interface-subnet-usage [disable|enable]
set internet-service-database [mini|standard|...]
set internet-service-download-list <id1>, <id2>, ...
set interval {integer}
set ip-conflict-detection [enable|disable]
set ip-fragment-mem-thresholds {integer}
set ip-fragment-timeout {integer}
FortiOS 8.0.0 CLI Reference
1636
Fortinet Inc.

<!-- 来源页 1637 -->
set ip-src-port-range {user}
set ips-affinity {string}
set ipsec-asic-offload [enable|disable]
set ipsec-ha-seqjump-rate {integer}
set ipsec-hmac-offload [enable|disable]
set ipsec-qat-offload [enable|disable]
set ipv6-accept-dad {integer}
set ipv6-allow-anycast-probe [enable|disable]
set ipv6-allow-local-in-silent-drop [enable|disable]
set ipv6-allow-multicast-probe [enable|disable]
set ipv6-allow-traffic-redirect [enable|disable]
set ipv6-fragment-timeout {integer}
set ipv6-snat-route-change [enable|disable]
set irq-time-accounting [auto|force]
set language [english|french|...]
set ldapconntimeout {integer}
set legacy-poe-device-support [enable|disable]
set lldp-reception [enable|disable]
set lldp-transmission [enable|disable]
set log-daemon-cpu-threshold {integer}
set log-fsck-timeout {integer}
set log-single-cpu-high [enable|disable]
set log-ssl-connection [enable|disable]
set log-uuid-address [enable|disable]
set login-timestamp [enable|disable]
set long-vdom-name [enable|disable]
set management-ip {string}
set management-port {integer}
set management-port-use-admin-sport [enable|disable]
set management-vdom {string}
set max-route-cache-size {integer}
set memory-use-threshold-extreme {integer}
set memory-use-threshold-green {integer}
set memory-use-threshold-red {integer}
set miglog-affinity {string}
set miglogd-children {integer}
set multi-factor-authentication [optional|mandatory]
set ndp-max-entry {integer}
set npu-neighbor-update [enable|disable]
set per-user-bal [enable|disable]
set pmtu-discovery [enable|disable]
set policy-auth-concurrent {integer}
set post-login-banner [disable|enable]
set pre-login-banner [enable|disable]
set private-data-encryption [disable|enable]
set proxy-auth-lifetime [enable|disable]
set proxy-auth-lifetime-timeout {integer}
set proxy-auth-timeout {integer}
set proxy-cert-use-mgmt-vdom [enable|disable]
set proxy-hardware-acceleration [disable|enable]
set proxy-keep-alive-mode [session|traffic|...]
set proxy-re-authentication-time {integer}
FortiOS 8.0.0 CLI Reference
1637
Fortinet Inc.

<!-- 来源页 1638 -->
set proxy-resource-mode [enable|disable]
set proxy-worker-count {integer}
set purdue-level [1|1.5|...]
set quic-ack-thresold {integer}
set quic-congestion-control-algo [cubic|bbr|...]
set quic-max-datagram-size {integer}
set quic-pmtud [enable|disable]
set quic-tls-handshake-timeout {integer}
set quic-udp-payload-size-shaping-per-cid [enable|disable]
set radius-port {integer}
set reboot-upon-config-restore [enable|disable]
set refresh {integer}
set remoteauthtimeout {integer}
set reset-sessionless-tcp [enable|disable]
set rest-api-key-url-query [enable|disable]
set restart-time {user}
set revision-backup-on-logout [enable|disable]
set revision-image-auto-backup [enable|disable]
set router-affinity {string}
set scanunit-count {integer}
set scim-http-port {integer}
set scim-https-port {integer}
set scim-server-cert {string}
set send-pmtu-icmp [enable|disable]
set sflowd-max-children-num {integer}
set single-vdom-npuvlink [enable|disable]
set snat-route-change [enable|disable]
set special-file-23-support [disable|enable]
set speedtest-server [enable|disable]
set speedtestd-ctrl-port {integer}
set speedtestd-server-port {integer}
set split-port {string}
config split-port-mode
Description: Configure split port mode of ports.
edit <interface>
set split-mode [disable|4x10G|...]
next
end
set ssd-trim-date {integer}
set ssd-trim-freq [never|hourly|...]
set ssd-trim-hour {integer}
set ssd-trim-min {integer}
set ssd-trim-weekday [sunday|monday|...]
set ssl-min-proto-version [SSLv3|TLSv1|...]
set ssl-static-key-ciphers [enable|disable]
set sslvpn-affinity {string}
set sslvpn-max-worker-count {integer}
set sslvpn-web-mode [enable|disable]
set strict-dirty-session-check [enable|disable]
set strong-crypto [enable|disable]
set switch-controller [disable|enable]
set switch-controller-reserved-network {ipv4-classnet-host}
FortiOS 8.0.0 CLI Reference
1638
Fortinet Inc.

<!-- 来源页 1639 -->
set sys-perf-log-interval {integer}
set syslog-affinity {string}
set tcp-congestion-control [cubic|bbr]
set tcp-halfclose-timer {integer}
set tcp-halfopen-timer {integer}
set tcp-option [enable|disable]
set tcp-rst-timer {integer}
set tcp-timewait-timer {integer}
set telemetry-controller [enable|disable]
set telemetry-data-port {integer}
set tftp [enable|disable]
set timezone {string}
set tls-session-cache [enable|disable]
set traffic-priority [tos|dscp]
set traffic-priority-level [low|medium|...]
set two-factor-email-expiry {integer}
set two-factor-fac-expiry {integer}
set two-factor-ftk-expiry {integer}
set two-factor-ftm-expiry {integer}
set two-factor-sms-expiry {integer}
set udp-idle-timer {integer}
set upgrade-report [enable|disable]
set url-filter-affinity {string}
set url-filter-count {integer}
set user-device-store-max-device-mem {integer}
set user-device-store-max-devices {integer}
set user-device-store-max-unified-mem {integer}
set user-device-store-max-users {integer}
set user-history-password-threshold {integer}
set vdom-mode [no-vdom|multi-vdom]
set vip-arp-range [unlimited|restricted]
set virtual-switch-vlan [enable|disable]
set wad-affinity {string}
set wad-csvc-cs-count {integer}
set wad-csvc-db-count {integer}
set wad-memory-change-granularity {integer}
set wad-p2s-max-body-size {integer}
set wad-restart-end-time {user}
set wad-restart-mode [none|time|...]
set wad-restart-start-time {user}
set wad-source-affinity [disable|enable]
set wad-worker-count {integer}
set wad-worker-dev-cache {integer}
set wifi-ca-certificate {string}
set wifi-certificate {string}
set wimax-4g-usb [enable|disable]
set wireless-controller [enable|disable]
set wireless-controller-port {integer}
set wireless-mode [ac|client|...]
end
FortiOS 8.0.0 CLI Reference
1639
Fortinet Inc.

<!-- 来源页 1640 -->
config system global
Parameter
Description
Type
Size
Default
admin-ble-button *
press the BLE button can enable
BLE function
option
-enable
Option
Description
enable
Press the BLE button can enable BLE function
disable
Press the BLE button cannot enable BLE function
admin-concurrent
Enable/disable concurrent
administrator logins. Use policy-auth-concurrent for firewall
authenticated users.
option
-enable
Option
Description
enable
Enable admin concurrent login.
disable
Disable admin concurrent login.
admin-console-timeout
Console login timeout that
overrides the admin timeout value
(15 - 300 seconds, default = 0,
which disables the timeout).
integer
Minimum value:
15 Maximum
value: 300
0
admin-forticloud-sso-default-profile
Override access profile.
string
Maximum
length: 35
admin-forticloud-sso-login
Enable/disable FortiCloud admin
login via SSO.
option
-disable
Option
Description
enable
Enable FortiCloud admin login via SSO.
disable
Disable FortiCloud admin login via SSO.
admin-host
Administrative host for HTTP and
HTTPS. When set, will be used in
lieu of the client's Host header for
any redirection.
string
Maximum
length: 255
admin-hsts-max-age
HTTPS Strict-Transport-Security
header max-age in seconds. A
value of 0 will reset any HSTS
records in the browser.When
admin-https-redirect is disabled
the header max-age will be 0.
integer
Minimum value:
0 Maximum
value:
2147483647
63072000
FortiOS 8.0.0 CLI Reference
1640
Fortinet Inc.

<!-- 来源页 1641 -->
Parameter
Description
Type
Size
Default
admin-http-rate-limit-exempt-auth *
Enable/disable exemption of
authenticated administrator
sessions from rate limiting.
option
-disable
Option
Description
enable
Enable exemption of authenticated administrator sessions from
rate limiting.
disable
Disable exemption of authenticated administrator sessions from
rate limiting.
admin-http-rate-limit-max-requests *
Maximum number of HTTP requests
that are allowed to be made in a
second by a single client (0 will
disable rate limiting).
integer
Minimum value:
50 Maximum
value: 1000
100
admin-http-request-body-timeout *
Authenticated HTTP request body
timeout, in milliseconds (0 will
disable the timeout).
integer
Minimum value:
100 Maximum
value:
3600000
1800000
admin-http-request-header-timeout *
HTTP request header timeout, in
milliseconds (0 will disable the
timeout).
integer
Minimum value:
100 Maximum
value: 60000
10000
admin-http-unauthenticated-request-body-timeout *
Unauthenticated HTTP request
body timeout, in milliseconds,
before authentication (0 will disable
the timeout).
integer
Minimum value:
100 Maximum
value: 600000
1000
admin-https-pki-required
Enable/disable admin login method.
Enable to force administrators to
provide a valid certificate to log in if
PKI is enabled. Disable to allow
administrators to log in with a
certificate or password.
option
-disable
Option
Description
enable
Admin users must provide a valid certificate when PKI is enabled
for HTTPS admin access.
disable
Admin users can login by providing a valid certificate or password.
admin-https-redirect
Enable/disable redirection of HTTP
administration access to HTTPS.
option
-enable
FortiOS 8.0.0 CLI Reference
1641
Fortinet Inc.

<!-- 来源页 1642 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable redirecting HTTP administration access to HTTPS.
disable
Disable redirecting HTTP administration access to HTTPS.
admin-https-ssl-banned-ciphers
Select one or more cipher
technologies that cannot be used in
GUI HTTPS negotiations. Only
applies to TLS 1.2 and below.
option
-Option
Description
RSA
Ban the use of cipher suites using RSA key.
DHE
Ban the use of cipher suites using authenticated ephemeral DH
key agreement.
ECDHE
Ban the use of cipher suites using authenticated ephemeral ECDH
key agreement.
DSS
Ban the use of cipher suites using DSS authentication.
ECDSA
Ban the use of cipher suites using ECDSA authentication.
AES
Ban the use of cipher suites using either 128 or 256 bit AES.
AESGCM
Ban the use of cipher suites using AES in Galois Counter Mode
(GCM).
CAMELLIA
Ban the use of cipher suites using either 128 or 256 bit CAMELLIA.
3DES
Ban the use of cipher suites using triple DES.
SHA1
Ban the use of cipher suites using HMAC-SHA1.
SHA256
Ban the use of cipher suites using HMAC-SHA256.
SHA384
Ban the use of cipher suites using HMAC-SHA384.
STATIC
Ban the use of cipher suites using static keys.
CHACHA20
Ban the use of cipher suites using ChaCha20.
ARIA
Ban the use of cipher suites using ARIA.
AESCCM
Ban the use of cipher suites using AESCCM.
FortiOS 8.0.0 CLI Reference
1642
Fortinet Inc.

<!-- 来源页 1643 -->
Parameter
Description
Type
Size
Default
admin-https-ssl-ciphersuites
Select one or more TLS 1.3
ciphersuites to enable. Does not
affect ciphers in TLS 1.2 and below.
At least one must be enabled. To
disable all, remove TLS1.3 from
admin-https-ssl-versions.
option
-TLS-AES-128-GCM-SHA256
TLS-AES-256-GCM-SHA384
TLS-CHACHA20-POLY1305-SHA256
Option
Description
TLS-AES-128-GCM-SHA256
Enable TLS-AES-128-GCM-SHA256 in TLS 1.3.
TLS-AES-256-GCM-SHA384
Enable TLS-AES-256-GCM-SHA384 in TLS 1.3.
TLS-CHACHA20-POLY1305-SHA256
Enable TLS-CHACHA20-POLY1305-SHA256 in TLS 1.3.
TLS-AES-128-CCM-SHA256
Enable TLS-AES-128-CCM-SHA256 in TLS 1.3.
TLS-AES-128-CCM-8-SHA256
Enable TLS-AES-128-CCM-8-SHA256 in TLS 1.3.
admin-https-ssl-versions
Allowed TLS versions for web
administration.
option
-tlsv1-2 tlsv1-3
Option
Description
tlsv1-1
TLS 1.1.
tlsv1-2
TLS 1.2.
tlsv1-3
TLS 1.3.
admin-lockout-duration
Amount of time in seconds that an
administrator account is locked out
after reaching the admin-lockout-threshold for repeated failed login
attempts.
integer
Minimum value:
1 Maximum
value:
2147483647
60
admin-lockout-threshold
Number of failed login attempts
before an administrator account is
locked out for the admin-lockout-duration.
integer
Minimum value:
1 Maximum
value: 10
3
FortiOS 8.0.0 CLI Reference
1643
Fortinet Inc.

<!-- 来源页 1644 -->
Parameter
Description
Type
Size
Default
admin-login-max
Maximum number of administrators
who can be logged in at the same
time (1 - 100, default = 100).
integer
Minimum value:
1 Maximum
value: 100
100
admin-port
Administrative access port for
HTTP. (1 - 65535, default = 80).
integer
Minimum value:
1 Maximum
value: 65535
80
admin-reset-button *
Press the reset button can reset to
factory default.
option
-enable
Option
Description
enable
press the reset button can reset to factory default
disable
press the reset button cannot reset to factory default
admin-restrict-local
Enable/disable local admin
authentication restriction when
remote authenticator is up and
running (default = disable).
option
-disable
Option
Description
all
Enable local admin authentication restriction including console.
non-console-only
Enable local admin authentication restriction excluding console.
disable
Disable local admin authentication restriction.
admin-scp
Enable/disable SCP support for
system configuration backup,
restore, and firmware file upload.
option
-disable
Option
Description
enable
Enable SCP support for system configuration backup, restore, and
firmware file upload.
disable
Disable SCP support for system configuration backup, restore,
and firmware file upload.
admin-server-cert
Server certificate that the FortiGate
uses for HTTPS administrative
connections.
string
Maximum
length: 35
Fortinet_GUI_
Server
admin-sport
Administrative access port for
HTTPS. (1 - 65535, default = 443).
integer
Minimum value:
1 Maximum
value: 65535
443
FortiOS 8.0.0 CLI Reference
1644
Fortinet Inc.

<!-- 来源页 1645 -->
Parameter
Description
Type
Size
Default
admin-ssh-grace-time
Maximum time in seconds
permitted between making an SSH
connection to the FortiGate unit and
authenticating (10 - 3600 sec (1
hour), default 120).
integer
Minimum value:
10 Maximum
value: 3600
120
admin-ssh-password
Enable/disable password
authentication for SSH admin
access.
option
-enable
Option
Description
enable
Enable password authentication for SSH admin access.
disable
Disable password authentication for SSH admin access.
admin-ssh-port
Administrative access port for SSH.
(1 - 65535, default = 22).
integer
Minimum value:
1 Maximum
value: 65535
22
admin-ssh-v1
Enable/disable SSH v1
compatibility.
option
-disable
Option
Description
enable
Enable SSH v1 compatibility.
disable
Disable SSH v1 compatibility.
admin-telnet
Enable/disable TELNET service.
option
-enable
Option
Description
enable
Enable TELNET service.
disable
Disable TELNET service.
admin-telnet-port
Administrative access port for
TELNET. (1 - 65535, default = 23).
integer
Minimum value:
1 Maximum
value: 65535
23
admintimeout
Number of minutes before an idle
administrator session times out (1 -480 minutes (8 hours), default = 5).
A shorter idle timeout is more
secure.
integer
Minimum value:
1 Maximum
value: 480
5
airplane-mode *
Enable/disable airplane mode.
option
-disable
FortiOS 8.0.0 CLI Reference
1645
Fortinet Inc.

<!-- 来源页 1646 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Shutdown RF signal of internal MODEM and Bluetooth module.
disable
Enable RF signal of internal MODEM and Bluetooth module.
alias
Alias for your FortiGate unit.
string
Maximum
length: 35
allow-traffic-redirect
Disable to prevent traffic with same
local ingress and egress interface
from being forwarded without
policy check.
option
-disable
Option
Description
enable
Enable allow traffic redirect.
disable
Disable allow traffic redirect.
anti-replay
Level of checking for packet replay
and TCP sequence checking.
option
-strict
Option
Description
disable
Disable anti-replay check.
loose
Loose anti-replay check.
strict
Strict anti-replay check.
application-bandwidth-tracking
Enable/disable application
bandwidth tracking.
option
-disable
Option
Description
disable
Disable application bandwidth tracking.
enable
Enable application bandwidth tracking.
arp-max-entry
Maximum number of dynamically
learned MAC addresses that can be
added to the ARP table (131072 -2147483647, default = 131072).
integer
Minimum value:
131072
Maximum
value:
2147483647
131072
auth-cert
Server certificate that the FortiGate
uses for HTTPS firewall
authentication connections.
string
Maximum
length: 35
Fortinet_
Factory **
FortiOS 8.0.0 CLI Reference
1646
Fortinet Inc.

<!-- 来源页 1647 -->
Parameter
Description
Type
Size
Default
auth-http-port
User authentication HTTP port. (1 -65535, default = 1000).
integer
Minimum value:
1 Maximum
value: 65535
1000
auth-https-port
User authentication HTTPS port. (1
- 65535, default = 1003).
integer
Minimum value:
1 Maximum
value: 65535
1003
auth-ike-saml-port
User IKE SAML authentication port
(0 - 65535, default = 1001).
integer
Minimum value:
0 Maximum
value: 65535
1001
auth-keepalive
Enable to prevent user
authentication sessions from timing
out when idle.
option
-disable
Option
Description
enable
Enable use of keep alive to extend authentication.
disable
Disable use of keep alive to extend authentication.
auth-session-auto-backup
Enable/disable automatic and
periodic backup of authentication
sessions (default = disable).
Sessions are restored upon bootup.
option
-disable
Option
Description
enable
Enable periodic backup of authentication sessions.
disable
Disable periodic backup of authentication sessions.
auth-session-auto-backup-interval
Configure automatic authentication
session backup interval (default =
15min).
option
-15min
Option
Description
1min
One minute.
5min
Five minutes.
15min
Fifteen minutes.
30min
Thirty minutes.
1hr
One hour.
auth-session-limit
Action to take when the number of
allowed user authenticated
sessions is reached.
option
-block-new
FortiOS 8.0.0 CLI Reference
1647
Fortinet Inc.

<!-- 来源页 1648 -->
Parameter
Description
Type
Size
Default
Option
Description
block-new
Block new user authentication attempts.
logout-inactive
Logout the most inactive user authenticated sessions.
auto-auth-extension-device
Enable/disable automatic
authorization of dedicated Fortinet
extension devices.
option
-enable
Option
Description
enable
Enable automatic authorization of dedicated Fortinet extension
device globally.
disable
Disable automatic authorization of dedicated Fortinet extension
device globally.
autorun-log-fsck
Enable/disable automatic log
partition check after ungraceful
shutdown.
option
-disable
Option
Description
enable
Enable automatic log partition check after ungraceful shutdown.
disable
Disable automatic log partition check after ungraceful shutdown.
av-affinity *
Affinity setting for AV scanning
(hexadecimal value up to 256 bits in
the format of xxxxxxxxxxxxxxxx).
string
Maximum
length: 79
0
av-failopen
Set the action to take if the
FortiGate is running low on memory
or the proxy connection limit has
been reached.
option
-pass
Option
Description
pass
Bypass the antivirus system when memory is low. Antivirus
scanning resumes when the low memory condition is resolved.
off
Stop accepting new AV sessions when entering conserve mode,
but continue to process current active sessions.
one-shot
Bypass the antivirus system when memory is low.
FortiOS 8.0.0 CLI Reference
1648
Fortinet Inc.

<!-- 来源页 1649 -->
Parameter
Description
Type
Size
Default
av-failopen-session
When enabled and a proxy for a
protocol runs out of room in its
session table, that protocol goes
into failopen mode and enacts the
action specified by av-failopen.
option
-disable
Option
Description
enable
Enable AV fail open session option.
disable
Disable AV fail open session option.
batch-cmdb
Enable/disable batch mode,
allowing you to enter a series of CLI
commands that will execute as a
group once they are loaded.
option
-enable
Option
Description
enable
Enable batch mode to execute in CMDB server.
disable
Disable batch mode to execute in CMDB server.
bfd-affinity *
Affinity setting for BFD daemon
(hexadecimal value up to 256 bits in
the format of xxxxxxxxxxxxxxxx).
string
Maximum
length: 79
1
block-session-timer
Duration in seconds for blocked
sessions (1 - 300 sec (5 minutes),
default = 30).
integer
Minimum value:
1 Maximum
value: 300
30
br-fdb-max-entry
Maximum number of bridge
forwarding database (FDB) entries.
integer
Minimum value:
8192 Maximum
value:
2147483647
8192
cert-chain-max
Maximum number of certificates
that can be traversed in a
certificate chain.
integer
Minimum value:
1 Maximum
value:
2147483647
8
cfg-revert-timeout
Time-out for reverting to the last
saved configuration. (10 -4294967295 seconds, default =
600).
integer
Minimum value:
10 Maximum
value:
4294967295
600
cfg-save
Configuration file save mode for CLI
changes.
option
-automatic
FortiOS 8.0.0 CLI Reference
1649
Fortinet Inc.

<!-- 来源页 1650 -->
Parameter
Description
Type
Size
Default
Option
Description
automatic
Automatically save config.
manual
Manually save config.
revert
Manually save config and revert the config when timeout.
check-protocol-header
Level of checking performed on
protocol headers. Strict checking is
more thorough but may affect
performance. Loose checking is OK
in most cases.
option
-loose
Option
Description
loose
Check protocol header loosely.
strict
Check protocol header strictly.
check-reset-range
Configure ICMP error message
verification. You can either apply
strict RST range checking or disable
it.
option
-disable
Option
Description
strict
Check RST range strictly.
disable
Disable RST range check.
cli-audit-log
Enable/disable CLI audit log.
option
-disable
Option
Description
enable
Enable CLI audit log.
disable
Disable CLI audit log.
cloud-communication
Enable/disable all cloud
communication.
option
-enable
Option
Description
enable
Allow cloud communication.
disable
Disable all cloud-related settings.
clt-cert-req
Enable/disable requiring
administrators to have a client
certificate to log into the GUI using
HTTPS.
option
-disable
FortiOS 8.0.0 CLI Reference
1650
Fortinet Inc.

<!-- 来源页 1651 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable require client certificate for GUI login.
disable
Disable require client certificate for GUI login.
cmdbsvr-affinity
Affinity setting for cmdbsvr
(hexadecimal value up to 256 bits in
the format of xxxxxxxxxxxxxxxx).
string
Maximum
length: 79
0 **
cpu-use-threshold
Threshold at which CPU usage is
reported (% of total CPU, default =
90).
integer
Minimum value:
50 Maximum
value: 99
90
csr-ca-attribute
Enable/disable the CA attribute in
certificates. Some CA servers reject
CSRs that have the CA attribute.
option
-enable
Option
Description
enable
Enable CA attribute in CSR.
disable
Disable CA attribute in CSR.
daily-restart
Enable/disable daily restart of
FortiGate unit. Use the restart-time
option to set the time of day for the
restart.
option
-disable
Option
Description
enable
Enable daily reboot of the FortiGate.
disable
Disable daily reboot of the FortiGate.
default-service-source-port
Default service source port range
(default = 1 - 65535).
user
Not Specified
delay-tcp-npu-session *
Enable TCP NPU session delay to
guarantee packet order of 3-way
handshake.
option
-disable
Option
Description
enable
Enable TCP NPU session delay in order to guarantee packet order
of 3-way handshake.
disable
Disable TCP NPU session delay in order to guarantee packet
order of 3-way handshake.
FortiOS 8.0.0 CLI Reference
1651
Fortinet Inc.

<!-- 来源页 1652 -->
Parameter
Description
Type
Size
Default
device-idle-timeout
Time in seconds that a device must
be idle to automatically log the
device user out. (30 - 31536000
sec (30 sec to 1 year), default =
300).
integer
Minimum value:
30 Maximum
value:
31536000
300
dh-params
Number of bits to use in the Diffie-Hellman exchange for HTTPS/SSH
protocols.
option
-2048
Option
Description
1024
1024 bits.
1536
1536 bits.
2048
2048 bits.
3072
3072 bits.
4096
4096 bits.
6144
6144 bits.
8192
8192 bits.
dhcp-lease-backup-interval
DHCP leases backup interval in
seconds (10 - 3600, default = 60).
integer
Minimum value:
10 Maximum
value: 3600
60
dnsproxy-worker-count
DNS proxy worker count. For a
FortiGate with multiple logical
CPUs, you can set the DNS process
number from 1 to the number of
logical CPUs.
integer
Minimum value:
1 Maximum
value: 8 **
1
early-tcp-npu-session
Enable/disable early TCP NPU
session.
option
-disable
Option
Description
enable
Enable early TCP NPU session in order to guarantee packet order
of 3-way handshake.
disable
Disable early TCP NPU session in order to guarantee packet order
of 3-way handshake.
edit-vdom-prompt *
Enable/disable edit new VDOM
prompt.
option
-disable
FortiOS 8.0.0 CLI Reference
1652
Fortinet Inc.

<!-- 来源页 1653 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable edit new VDOM prompt.
disable
Disable edit new VDOM prompt.
extender-controller-reserved-network
Configure reserved network subnet
for managed LAN extension
FortiExtender units. This is available
when the FortiExtender daemon is
running.
ipv4-classnet-host
Not Specified
10.252.0.1
255.255.0.0
failtime
Fail-time for server lost.
integer
Minimum value:
0 Maximum
value:
4294967295
5
faz-disk-buffer-size
Maximum disk buffer size to
temporarily store logs destined for
FortiAnalyzer. To be used in the
event that FortiAnalyzer is
unavailable.
integer
Not Specified
0
fds-statistics
Enable/disable sending IPS,
Application Control, and AntiVirus
data to FortiGuard. This data is
used to improve FortiGuard
services and is not shared with
external parties and is protected by
Fortinet's privacy policy.
option
-enable
Option
Description
enable
Enable FortiGuard statistics.
disable
Disable FortiGuard statistics.
fds-statistics-period
FortiGuard statistics collection
period in minutes. (1 - 1440 min (1
min to 24 hours), default = 60).
integer
Minimum value:
1 Maximum
value: 1440
60
fgd-alert-subscription
Type of alert to retrieve from
FortiGuard.
option
-Option
Description
advisory
Retrieve FortiGuard advisories, report and news alerts.
latest-threat
Retrieve latest FortiGuard threats alerts.
latest-virus
Retrieve latest FortiGuard virus alerts.
FortiOS 8.0.0 CLI Reference
1653
Fortinet Inc.

<!-- 来源页 1654 -->
Parameter
Description
Type
Size
Default
Option
Description
latest-attack
Retrieve latest FortiGuard attack alerts.
new-antivirus-db
Retrieve FortiGuard AV database release alerts.
new-attack-db
Retrieve FortiGuard IPS database release alerts.
forticonverter-config-upload
Enable/disable config upload to
FortiConverter.
option
-disable
Option
Description
once
Enable one-time config upload to FortiConverter.
disable
Disable config upload to FortiConverter.
forticonverter-integration
Enable/disable FortiConverter
integration service.
option
-disable
Option
Description
enable
Enable FortiConverter integration service.
disable
Disable FortiConverter integration service.
fortiextender
Enable/disable FortiExtender.
option
-disable **
Option
Description
disable
Disable FortiExtender controller.
enable
Enable FortiExtender controller.
fortiextender-data-port
FortiExtender data port (1024 -49150, default = 25246).
integer
Minimum value:
1024 Maximum
value: 49150
25246
fortiextender-discovery-lockdown
Enable/disable FortiExtender
CAPWAP lockdown.
option
-disable
Option
Description
disable
Unlock down new FortiExtender device discovery.
enable
Lock down new FortiExtender device discovery.
fortiextender-provision-on-authorization
Enable/disable automatic
provisioning of latest FortiExtender
firmware on authorization.
option
-disable
FortiOS 8.0.0 CLI Reference
1654
Fortinet Inc.

<!-- 来源页 1655 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable FortiExtender firmware provision on authorization.
disable
Disable FortiExtender firmware provision on authorization.
fortiextender-vlan-mode *
Enable/disable FortiExtender VLAN
mode.
option
-disable
Option
Description
enable
Enable FortiExtender VLAN mode.
disable
Disable FortiExtender VLAN mode.
fortigslb-integration
Enable/disable integration with the
FortiGSLB cloud service.
option
-disable
Option
Description
disable
Disable VIP and ZTNA server integration with the FortiGSLB cloud
service.
enable
Enable VIP and ZTNA server integration with the FortiGSLB cloud
service.
fortiservice-port
FortiService port (1 - 65535, default
= 8013). Used by FortiClient
endpoint compliance. Older
versions of FortiClient used a
different port.
integer
Minimum value:
1 Maximum
value: 65535
8013
fortitoken-cloud
Enable/disable FortiToken Cloud
service.
option
-enable
Option
Description
enable
Enable FortiToken Cloud service.
disable
Disable FortiToken Cloud service.
fortitoken-cloud-push-status
Enable/disable FTM push service of
FortiToken Cloud.
option
-enable
Option
Description
enable
Enable FTM push service of FortiToken Cloud.
disable
Disable FTM push service of FortiToken Cloud.
fortitoken-cloud-region
Region domain of FortiToken Cloud
(unset to non-region).
string
Maximum
length: 63
FortiOS 8.0.0 CLI Reference
1655
Fortinet Inc.

<!-- 来源页 1656 -->
Parameter
Description
Type
Size
Default
fortitoken-cloud-sync-interval
Interval in which to clean up remote
users in FortiToken Cloud (0 - 336
hours (14 days), default = 24,
disable = 0).
integer
Minimum value:
0 Maximum
value: 336
24
geoip-full-db
When enabled, the full geographic
database will be loaded into the
kernel which enables geographic
information in traffic logs - required
for FortiView countries. Disabling
this option will conserve memory.
option
-enable **
Option
Description
enable
Full GeoDB will be downloaded. FortiView countries can be used.
disable
Full GeoDB will not be downloaded. FortiView countries cannot be
used.
gtpu-dynamic-source-port *
Enable/disable GTP-U dynamic
source port support.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
gui-allow-incompatible-fabric-fgt
Enable/disable Allow FGT with
incompatible firmware to be treated
as compatible in security fabric on
the GUI. May cause unexpected
error.
option
-disable
Option
Description
enable
Display the feature in GUI.
disable
Do not display the feature in GUI.
gui-app-detection-sdwan
Enable/disable Allow app-detection
based SD-WAN.
option
-disable
Option
Description
enable
Display the feature in GUI.
disable
Do not display the feature in GUI.
gui-auto-upgrade-setup-warning
Enable/disable the automatic patch
upgrade setup prompt on the GUI.
option
-enable
FortiOS 8.0.0 CLI Reference
1656
Fortinet Inc.

<!-- 来源页 1657 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Display the feature in GUI.
disable
Do not display the feature in GUI.
gui-cdn-domain-override
Domain of CDN server.
string
Maximum
length: 255
gui-cdn-usage
Enable/disable Load GUI static files
from a CDN.
option
-disable
Option
Description
enable
Display the feature in GUI.
disable
Do not display the feature in GUI.
gui-certificates
Enable/disable the System >
Certificate GUI page, allowing you
to add and configure certificates
from the GUI.
option
-enable **
Option
Description
enable
Display the feature in GUI.
disable
Do not display the feature in GUI.
gui-custom-language
Enable/disable custom languages in
GUI.
option
-disable
Option
Description
enable
Display the feature in GUI.
disable
Do not display the feature in GUI.
gui-custom-theme *
Custom theme that overrides the
default FortiGate themes.
string
Maximum
length: 35
gui-date-format
Default date format used
throughout GUI.
option
-yyyy/MM/dd
Option
Description
yyyy/MM/dd
Year/Month/Day.
dd/MM/yyyy
Day/Month/Year.
MM/dd/yyyy
Month/Day/Year.
FortiOS 8.0.0 CLI Reference
1657
Fortinet Inc.

<!-- 来源页 1658 -->
Parameter
Description
Type
Size
Default
Option
Description
yyyy-MM-dd
Year-Month-Day.
dd-MM-yyyy
Day-Month-Year.
MM-dd-yyyy
Month-Day-Year.
gui-date-time-source
Source from which the FortiGate
GUI uses to display date and time
entries.
option
-system
Option
Description
system
Use this FortiGate unit's configured timezone.
browser
Use the web browser's timezone.
gui-device-latitude
Add the latitude of the location of
this FortiGate to position it on the
Threat Map.
string
Maximum
length: 19
gui-device-longitude
Add the longitude of the location of
this FortiGate to position it on the
Threat Map.
string
Maximum
length: 19
gui-display-hostname
Enable/disable displaying the
FortiGate's hostname on the GUI
login page.
option
-disable
Option
Description
enable
Display the feature in GUI.
disable
Do not display the feature in GUI.
gui-firmware-upgrade-warning
Enable/disable the firmware
upgrade warning on the GUI.
option
-enable
Option
Description
enable
Display the feature in GUI.
disable
Do not display the feature in GUI.
gui-forticare-registration-setup-warning
Enable/disable the FortiCare
registration setup warning on the
GUI.
option
-enable
Option
Description
enable
Display the feature in GUI.
FortiOS 8.0.0 CLI Reference
1658
Fortinet Inc.

<!-- 来源页 1659 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Do not display the feature in GUI.
gui-fortigate-cloud-sandbox
Enable/disable displaying FortiGate
Cloud Sandbox on the GUI.
option
-disable
Option
Description
enable
Display the feature in GUI.
disable
Do not display the feature in GUI.
gui-ipv6
Enable/disable IPv6 settings on the
GUI.
option
-disable
Option
Description
enable
Display the feature in GUI.
disable
Do not display the feature in GUI.
gui-local-out
Enable/disable Local-out traffic on
the GUI.
option
-disable
Option
Description
enable
Display the feature in GUI.
disable
Do not display the feature in GUI.
gui-login-request-rate-limit *
Conifgure number of login requests
to maintain in the request queue (0
- 30, default = 0 for no rate limit).
integer
Minimum value:
0 Maximum
value: 30
0
gui-replacement-message-groups
Enable/disable replacement
message groups on the GUI.
option
-disable
Option
Description
enable
Display the feature in GUI.
disable
Do not display the feature in GUI.
gui-rest-api-cache *
Enable/disable REST API result
caching on FortiGate.
option
-enable
Option
Description
enable
Enable REST API result caching on FortiGate.
disable
Disable REST API result caching on FortiGate.
FortiOS 8.0.0 CLI Reference
1659
Fortinet Inc.

<!-- 来源页 1660 -->
Parameter
Description
Type
Size
Default
gui-restrict-theme-change *
Enable/disable restricting editing
and assigning override themes to
super admins.
option
-disable
Option
Description
enable
Enable restricting editing override themes to super-admins only.
disable
Disable restricting editing override themes to super-admins only.
gui-theme
Color scheme for the administration
GUI.
option
-jade
Option
Description
jade
Jade theme.
neutrino
Neutrino theme.
mariner
Mariner theme.
graphite
Graphite theme.
melongene
Melongene theme.
jet-stream
Jet Stream theme.
security-fabric
Security Fabric theme.
retro
FortiOS v3 Retro theme.
dark-matter
Dark Matter theme.
onyx
Onyx theme.
eclipse
Eclipse theme.
gui-wireless-opensecurity
Enable/disable wireless open
security option on the GUI.
option
-disable
Option
Description
enable
Display the feature in GUI.
disable
Do not display the feature in GUI.
gui-workflow-management
Enable/disable Workflow
management features on the GUI.
option
-disable
Option
Description
enable
Display the feature in GUI.
disable
Do not display the feature in GUI.
FortiOS 8.0.0 CLI Reference
1660
Fortinet Inc.

<!-- 来源页 1661 -->
Parameter
Description
Type
Size
Default
ha-affinity
Affinity setting for HA daemons
(hexadecimal value up to 256 bits in
the format of xxxxxxxxxxxxxxxx).
string
Maximum
length: 79
0 **
honor-df
Enable/disable honoring of Don't-Fragment (DF) flag.
option
-enable
Option
Description
enable
Enable honoring of Don't-Fragment flag.
disable
Disable honoring of Don't-Fragment flag.
hostname
FortiGate unit's hostname. Most
models will truncate names longer
than 24 characters. Some models
support hostnames up to 35
characters.
string
Maximum
length: 35
http-request-limit *
HTTP request body size limit.
integer
Minimum value:
524288000
Maximum
value:
4194304000
524288000
http-unauthenticated-request-limit *
HTTP request body size limit before
authentication.
integer
Minimum value:
1024 Maximum
value: 524288
131072
httpd-max-worker-count
Maximum number of simultaneous
HTTP requests that will be served.
This number may affect GUI and
REST API performance (0 - 128,
default = 0 means let system
decide).
integer
Minimum value:
0 Maximum
value: 128
0
hyper-scale-vdom-num *
Number of VDOMs for hyper scale
license.
integer
Minimum value:
1 Maximum
value: 250
250
igmp-state-limit
Maximum number of IGMP
memberships (96 - 64000, default
= 3200).
integer
Minimum value:
96 Maximum
value: 128000
3200
interface-subnet-usage
Enable/disable allowing use of
interface-subnet setting in firewall
addresses (default = enable).
option
-enable
FortiOS 8.0.0 CLI Reference
1661
Fortinet Inc.

<!-- 来源页 1662 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disallow use of the interface-subnet setting in firewall addresses.
Use in conjunction with the FortiGate REST API and when a large
number of firewall addresses exist in the configuration.
enable
Allow use of the interface-subnet setting in firewall addresses.
internet-service-database
Configure which Internet Service
database size to download from
FortiGuard and use.
option
-standard **
Option
Description
mini
Small sized Internet Service database with very limited IP
addresses.
standard
Medium sized Internet Service database with most IP addresses.
on-demand
Internet Service database with customer selected IP addresses.
full
Full sized Internet Service database with all IP addresses.
internet-service-download-list <id>
Configure which on-demand
Internet Service IDs are to be
downloaded.
Internet Service ID.
integer
Minimum value:
0 Maximum
value:
4294967295
interval
Dead gateway detection interval.
integer
Minimum value:
0 Maximum
value:
4294967295
5
ip-conflict-detection
Enable/disable logging of IPv4
address conflict detection.
option
-disable
Option
Description
enable
Enable logging of IPv4 address conflict detection.
disable
Disable logging of IPv4 address conflict detection.
ip-fragment-mem-thresholds
Maximum memory (MB) used to
reassemble IPv4/IPv6 fragments.
integer
Minimum value:
32 Maximum
value: 2047
32
ip-fragment-timeout
Timeout value in seconds for any
fragment not being reassembled
integer
Minimum value:
3 Maximum
value: 30
30
ip-src-port-range
IP source port range used for traffic
originating from the FortiGate unit.
user
Not Specified
1024-25000
FortiOS 8.0.0 CLI Reference
1662
Fortinet Inc.

<!-- 来源页 1663 -->
Parameter
Description
Type
Size
Default
ips-affinity *
Affinity setting for IPS (hexadecimal
value up to 256 bits in the format of
xxxxxxxxxxxxxxxx; allowed CPUs
must be less than total number of
IPS engine daemons).
string
Maximum
length: 79
0
ipsec-asic-offload *
Enable/disable ASIC offloading
(hardware acceleration) for IPsec
VPN traffic. Hardware acceleration
can offload IPsec VPN sessions and
accelerate encryption and
decryption.
option
-enable
Option
Description
enable
Enable ASIC offload for IPsec VPN.
disable
Disable ASIC offload for IPsec VPN.
ipsec-ha-seqjump-rate
ESP jump ahead rate (1G - 10G pps
equivalent).
integer
Minimum value:
1 Maximum
value: 10
10
ipsec-hmac-offload *
Enable/disable offloading
(hardware acceleration) of HMAC
processing for IPsec VPN.
option
-enable
Option
Description
enable
Enable offload IPsec HMAC processing to hardware if possible.
disable
Disable offload IPsec HMAC processing to hardware.
ipsec-qat-offload *
Enable/disable QAT offloading (Intel
QuickAssist) for IPsec VPN traffic.
QuickAssist can accelerate IPsec
encryption and decryption.
option
-enable
Option
Description
enable
Enable QAT offload for IPsec VPN.
disable
Disable QAT offload for IPsec VPN.
ipv6-accept-dad
Enable/disable acceptance of IPv6
Duplicate Address Detection (DAD).
integer
Minimum value:
0 Maximum
value: 2
1
ipv6-allow-anycast-probe
Enable/disable IPv6 address probe
through Anycast.
option
-disable
FortiOS 8.0.0 CLI Reference
1663
Fortinet Inc.

<!-- 来源页 1664 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable probing of IPv6 address space through Anycast
disable
Disable probing of IPv6 address space through Anycast
ipv6-allow-local-in-silent-drop
Enable/disable silent drop of IPv6
local-in traffic.
option
-enable
Option
Description
enable
Enable silent drop of IPv6 local-in traffic.
disable
Disable silent drop of IPv6 local-in traffic.
ipv6-allow-multicast-probe
Enable/disable IPv6 address probe
through Multicast.
option
-disable
Option
Description
enable
Enable probing of IPv6 address space through Multicast.
disable
Disable probing of IPv6 address space through Multicast.
ipv6-allow-traffic-redirect
Disable to prevent IPv6 traffic with
same local ingress and egress
interface from being forwarded
without policy check.
option
-disable
Option
Description
enable
Enable allow traffic IPv6 redirect.
disable
Disable allow traffic IPv6 redirect.
ipv6-fragment-timeout
Timeout value in seconds for any
IPv6 fragment not being
reassembled
integer
Minimum value:
5 Maximum
value: 60
60
ipv6-snat-route-change
Enable/disable the ability to change
the IPv6 source NAT route.
option
-disable
Option
Description
enable
Enable IPv6 SNAT route change.
disable
Disable IPv6 SNAT route change.
irq-time-accounting
Configure CPU IRQ time accounting
mode.
option
-auto
FortiOS 8.0.0 CLI Reference
1664
Fortinet Inc.

<!-- 来源页 1665 -->
Parameter
Description
Type
Size
Default
Option
Description
auto
Automatically switch CPU accounting mode.
force
Force the use of CPU IRQ time accounting mode.
language
GUI display language.
option
-english
Option
Description
english
English.
french
French.
spanish
Spanish.
portuguese
Portuguese.
japanese
Japanese.
trach
Traditional Chinese.
simch
Simplified Chinese.
korean
Korean.
ldapconntimeout
Global timeout for connections with
remote LDAP servers in
milliseconds (1 - 300000, default
500).
integer
Minimum value:
1 Maximum
value: 300000
500
legacy-poe-device-support *
Enable/disable legacy POE device
support.
option
-disable
Option
Description
enable
Enable legacy POE device support.
disable
Disable legacy POE device support.
lldp-reception
Enable/disable Link Layer Discovery
Protocol (LLDP) reception.
option
-disable
Option
Description
enable
Enable reception of Link Layer Discovery Protocol (LLDP).
disable
Disable reception of Link Layer Discovery Protocol (LLDP).
lldp-transmission
Enable/disable Link Layer Discovery
Protocol (LLDP) transmission.
option
-disable
FortiOS 8.0.0 CLI Reference
1665
Fortinet Inc.

<!-- 来源页 1666 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable transmission of Link Layer Discovery Protocol (LLDP).
disable
Disable transmission of Link Layer Discovery Protocol (LLDP).
log-daemon-cpu-threshold
Configure syslog daemon process
spawning threshold. Use a
percentage threshold of syslogd
CPU usage (1 - 99) or set to zero to
use dynamic scheduling based on
the number of packets in the
syslogd queue (default = 0).
integer
Minimum value:
0 Maximum
value: 99
0
log-fsck-timeout *
Configure the maximum the number
of seconds the FortiGate unit waits
while the file system check is in
progress before allowing the boot
process to complete and the
system fully is operational. Zero
seconds means the FortiGate unit
waits until the file system check is
complete (0 - 3600, default = 300).
integer
Minimum value:
0 Maximum
value: 3600
300
log-single-cpu-high
Enable/disable logging the event of
a single CPU core reaching CPU
usage threshold.
option
-disable
Option
Description
enable
Enable logging the event of a single CPU core reaching CPU
usage threshold.
disable
Disable logging the event of a single CPU core reaching CPU
usage threshold.
log-ssl-connection
Enable/disable logging of SSL
connection events.
option
-disable
Option
Description
enable
Enable logging of SSL connection events.
disable
Disable logging of SSL connection events.
log-uuid-address
Enable/disable insertion of address
UUIDs to traffic logs.
option
-disable
FortiOS 8.0.0 CLI Reference
1666
Fortinet Inc.

<!-- 来源页 1667 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable insertion of address UUID to traffic logs.
disable
Disable insertion of address UUID to traffic logs.
login-timestamp
Enable/disable login time recording.
option
-disable
Option
Description
enable
Enable login time recording.
disable
Disable login time recording.
long-vdom-name *
Enable/disable long VDOM name
support.
option
-disable
Option
Description
enable
Enable long VDOM name support.
disable
Disable long VDOM name support.
management-ip
Management IP address of this
FortiGate. Used to log into this
FortiGate from another FortiGate in
the Security Fabric.
string
Maximum
length: 255
management-port
Overriding port for management
connection (Overrides admin port).
integer
Minimum value:
1 Maximum
value: 65535
443
management-port-use-admin-sport
Enable/disable use of the admin-sport setting for the management
port. If disabled, FortiGate will allow
user to specify management-port.
option
-enable
Option
Description
enable
Enable use of the admin-sport setting for the management port.
disable
Disable use of the admin-sport setting for the management port.
management-vdom
Management virtual domain name.
string
Maximum
length: 31
root
max-route-cache-size
Maximum number of IP route cache
entries (0 - 2147483647).
integer
Minimum value:
0 Maximum
value:
2147483647
0
FortiOS 8.0.0 CLI Reference
1667
Fortinet Inc.

<!-- 来源页 1668 -->
Parameter
Description
Type
Size
Default
memory-use-threshold-extreme
Threshold at which memory usage
is considered extreme (new
sessions are dropped) (% of total
RAM, default = 95).
integer
Minimum value:
70 Maximum
value: 97
95
memory-use-threshold-green
Threshold at which memory usage
forces the FortiGate to exit
conserve mode (% of total RAM,
default = 82).
integer
Minimum value:
70 Maximum
value: 97
82
memory-use-threshold-red
Threshold at which memory usage
forces the FortiGate to enter
conserve mode (% of total RAM,
default = 88).
integer
Minimum value:
70 Maximum
value: 97
88
miglog-affinity *
Affinity setting for logging
(hexadecimal value up to 256 bits in
the format of xxxxxxxxxxxxxxxx).
string
Maximum
length: 79
0
miglogd-children
Number of logging (miglogd)
processes to be allowed to run.
Higher number can reduce
performance; lower number can
slow log processing time.
integer
Minimum value:
0 Maximum
value: 15
0
multi-factor-authentication
Enforce all login methods to require
an additional authentication factor
(default = optional).
option
-optional
Option
Description
optional
Do not enforce all login methods to require an additional
authentication factor (controlled by user settings).
mandatory
Enforce all login methods to require an additional authentication
factor.
ndp-max-entry
Maximum number of NDP table
entries (set to 65,536 or higher; if
set to 0, kernel holds 65,536
entries).
integer
Minimum value:
65536
Maximum
value:
2147483647
0
npu-neighbor-update *
Enable/disable sending of
ARP/ICMP6 probing packets to
update neighbors for offloaded
sessions.
option
-disable
FortiOS 8.0.0 CLI Reference
1668
Fortinet Inc.

<!-- 来源页 1669 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable sending of ARP/ICMP6 probing packets to update
neighbors for offloaded sessions.
disable
Disable sending of ARP/ICMP6 probing packets to update
neighbors for offloaded sessions.
per-user-bal *
Enable/disable per-user block/allow
list filter.
option
-disable
Option
Description
enable
Enable per-user block/allow list filter.
disable
Disable per-user block/allow list filter.
pmtu-discovery
Enable/disable path MTU
discovery.
option
-disable
Option
Description
enable
Enable path MTU discovery.
disable
Disable path MTU discovery.
policy-auth-concurrent
Number of concurrent firewall use
logins from the same user (1 - 100,
default = 0 means no limit).
integer
Minimum value:
0 Maximum
value: 100
0
post-login-banner
Enable/disable displaying the
administrator access disclaimer
message after an administrator
successfully logs in.
option
-disable
Option
Description
disable
Disable post-login banner.
enable
Enable post-login banner.
pre-login-banner
Enable/disable displaying the
administrator access disclaimer
message on the login page before
an administrator logs in.
option
-disable
Option
Description
enable
Enable pre-login banner.
disable
Disable pre-login banner.
FortiOS 8.0.0 CLI Reference
1669
Fortinet Inc.

<!-- 来源页 1670 -->
Parameter
Description
Type
Size
Default
private-data-encryption
Enable/disable private data
encryption using an AES 128-bit key
or passphrase.
option
-disable
Option
Description
disable
Disable private data encryption using an AES 128-bit key.
enable
Enable private data encryption using an AES 128-bit key.
proxy-auth-lifetime
Enable/disable authenticated users
lifetime control. This is a cap on the
total time a proxy user can be
authenticated for after which re-authentication will take place.
option
-disable
Option
Description
enable
Enable authenticated users lifetime control.
disable
Disable authenticated users lifetime control.
proxy-auth-lifetime-timeout
Lifetime timeout in minutes for
authenticated users (5 - 65535 min,
default=480 (8 hours)).
integer
Minimum value:
5 Maximum
value: 65535
480
proxy-auth-timeout
Authentication timeout in minutes
for authenticated users (1 - 10000
min, default = 10).
integer
Minimum value:
1 Maximum
value: 10000
10
proxy-cert-use-mgmt-vdom
Enable/disable using management
VDOM to send requests.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
proxy-hardware-acceleration *
Enable/disable email proxy
hardware acceleration.
option
-enable
Option
Description
disable
Disable email proxy hardware acceleration.
enable
Enable email proxy hardware acceleration.
FortiOS 8.0.0 CLI Reference
1670
Fortinet Inc.

<!-- 来源页 1671 -->
Parameter
Description
Type
Size
Default
proxy-keep-alive-mode
Control if users must re-authenticate after a session is
closed, traffic has been idle, or from
the point at which the user was
authenticated.
option
-session
Option
Description
session
Proxy keep-alive timeout begins at the closure of the session.
traffic
Proxy keep-alive timeout begins after traffic has not been
received.
re-authentication
Proxy keep-alive timeout begins when the user was
authenticated.
proxy-re-authentication-time
The time limit that users must re-authenticate if proxy-keep-alive-mode is set to re-authenticate (1 -86400 sec, default=30s.
integer
Minimum value:
1 Maximum
value: 86400
30
proxy-resource-mode
Enable/disable use of the maximum
memory usage on the FortiGate
unit's proxy processing of
resources, such as block lists, allow
lists, and external resources.
option
-disable
Option
Description
enable
Enable use of the maximum memory usage.
disable
Disable use of the maximum memory usage.
proxy-worker-count
Proxy worker count.
integer
Minimum value:
1 Maximum
value: 8 **
0
purdue-level
Purdue Level of this FortiGate.
option
-3
Option
Description
1
Level 1 - Basic Control
1.5
Level 1.5
2
Level 2 - Area Supervisory Control
2.5
Level 2.5
3
Level 3 - Operations & Control
3.5
Level 3.5
FortiOS 8.0.0 CLI Reference
1671
Fortinet Inc.

<!-- 来源页 1672 -->
Parameter
Description
Type
Size
Default
Option
Description
4
Level 4 - Business Planning & Logistics
5
Level 5 - Enterprise Network
5.5
Level 5.5
quic-ack-thresold
Maximum number of
unacknowledged packets before
sending ACK (2 - 5, default = 3).
integer
Minimum value:
2 Maximum
value: 5
3
quic-congestion-control-algo
QUIC congestion control algorithm
(default = cubic).
option
-cubic
Option
Description
cubic
Cubic.
bbr
BBR.
bbr2
BBR2.
reno
Reno.
quic-max-datagram-size
Maximum transmit datagram size
(1200 - 1500, default = 1500).
integer
Minimum value:
1200 Maximum
value: 1500
1500
quic-pmtud
Enable/disable path MTU discovery
(default = enable).
option
-enable
Option
Description
enable
Enable path MTU discovery.
disable
Disable path MTU discovery.
quic-tls-handshake-timeout
Time-to-live (TTL) for TLS
handshake in seconds (1 - 60,
default = 5).
integer
Minimum value:
1 Maximum
value: 60
5
quic-udp-payload-size-shaping-per-cid
Enable/disable UDP payload size
shaping per connection ID (default
= enable).
option
-enable
Option
Description
enable
Enable UDP payload size shaping per connection ID.
disable
Disable UDP payload size shaping per connection ID.
FortiOS 8.0.0 CLI Reference
1672
Fortinet Inc.

<!-- 来源页 1673 -->
Parameter
Description
Type
Size
Default
radius-port
RADIUS service port number.
integer
Minimum value:
1 Maximum
value: 65535
1812
reboot-upon-config-restore
Enable/disable reboot of system
upon restoring configuration.
option
-enable
Option
Description
enable
Enable reboot of system upon restoring configuration.
disable
Disable reboot of system upon restoring configuration.
refresh
Statistics refresh interval second(s)
in GUI.
integer
Minimum value:
0 Maximum
value:
4294967295
0
remoteauthtimeout
Number of seconds that the
FortiGate waits for responses from
remote RADIUS, LDAP, or TACACS+
authentication servers. (1-300 sec,
default = 5).
integer
Minimum value:
1 Maximum
value: 300
5
reset-sessionless-tcp
Action to perform if the FortiGate
receives a TCP packet but cannot
find a corresponding session in its
session table. NAT/Route mode
only.
option
-disable
Option
Description
enable
Enable reset session-less TCP.
disable
Disable reset session-less TCP.
rest-api-key-url-query *
Enable/disable support for passing
REST API keys through URL query
parameters.
option
-disable
Option
Description
enable
Enable support for passing REST API keys through URL query
parameters.
disable
Disable support for passing REST API keys through URL query
parameters.
restart-time
Daily restart time (hh:mm).
user
Not Specified
FortiOS 8.0.0 CLI Reference
1673
Fortinet Inc.

<!-- 来源页 1674 -->
Parameter
Description
Type
Size
Default
revision-backup-on-logout
Enable/disable back-up of the
latest configuration revision when
an administrator logs out of the CLI
or GUI.
option
-enable **
Option
Description
enable
Enable revision config backup automatically when logout.
disable
Disable revision config backup automatically when logout.
revision-image-auto-backup
Enable/disable back-up of the
latest image revision after the
firmware is upgraded.
option
-disable
Option
Description
enable
Enable revision image backup automatically when upgrading
image.
disable
Disable revision image backup automatically when upgrading
image.
router-affinity *
Affinity setting for
BFD/VRRP/BGP/OSPF daemons
(hexadecimal value up to 256 bits in
the format of xxxxxxxxxxxxxxxx).
string
Maximum
length: 79
0
scanunit-count
Number of scanunits. The range
and the default depend on the
number of CPUs. Only available on
FortiGate units with multiple CPUs.
integer
Minimum value:
1 Maximum
value: 8 **
0
scim-http-port
SCIM http port (0 - 65535, default =
44558).
integer
Minimum value:
0 Maximum
value: 65535
44558
scim-https-port
SCIM port (0 - 65535, default =
44559).
integer
Minimum value:
0 Maximum
value: 65535
44559
scim-server-cert
Server certificate that the FortiGate
uses for SCIM connections.
string
Maximum
length: 35
Fortinet_
Factory
send-pmtu-icmp
Enable/disable sending of path
maximum transmission unit (PMTU)
- ICMP destination unreachable
packet and to support PMTUD
protocol on your network to reduce
fragmentation of packets.
option
-enable
FortiOS 8.0.0 CLI Reference
1674
Fortinet Inc.

<!-- 来源页 1675 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable sending of PMTU ICMP destination unreachable packet.
disable
Disable sending of PMTU ICMP destination unreachable packet.
sflowd-max-children-num
Maximum number of sflowd child
processes allowed to run.
integer
Minimum value:
0 Maximum
value: 6 **
6 **
single-vdom-npuvlink *
Enable/disable NPU VDOMs links
for single VDOM.
option
-disable
Option
Description
enable
Enable NPU VDOM links for single VDOM.
disable
Disable NPU VDOM links for single VDOM.
snat-route-change
Enable/disable the ability to change
the source NAT route.
option
-disable
Option
Description
enable
Enable SNAT route change.
disable
Disable SNAT route change.
special-file-23-support
Enable/disable detection of those
special format files when using Data
Loss Prevention.
option
-disable
Option
Description
disable
Disable detection of those special format files when using Data
Loss Prevention.
enable
Enable detection of those special format files when using Data
Loss Prevention.
speedtest-server
Enable/disable speed test server.
option
-disable
Option
Description
enable
Enable speed test server service.
disable
Disable speed test server service.
speedtestd-ctrl-port
Speedtest server controller port
number.
integer
Minimum value:
1 Maximum
value: 65535
5200
FortiOS 8.0.0 CLI Reference
1675
Fortinet Inc.

<!-- 来源页 1676 -->
Parameter
Description
Type
Size
Default
speedtestd-server-port
Speedtest server port number.
integer
Minimum value:
1 Maximum
value: 65535
5201
split-port *
Split port(s) to multiple 10Gbps
ports.
string
Maximum
length: 15
ssd-trim-date *
Date within a month to run ssd trim.
integer
Minimum value:
1 Maximum
value: 31
1
ssd-trim-freq *
How often to run SSD Trim (default
= weekly). SSD Trim prevents SSD
drive data loss by finding and
isolating errors.
option
-weekly
Option
Description
never
Never Run SSD Trim.
hourly
Run SSD Trim Hourly.
daily
Run SSD Trim Daily.
weekly
Run SSD Trim Weekly.
monthly
Run SSD Trim Monthly.
ssd-trim-hour *
Hour of the day on which to run SSD
Trim (0 - 23, default = 1).
integer
Minimum value:
0 Maximum
value: 23
1
ssd-trim-min *
Minute of the hour on which to run
SSD Trim (0 - 59, 60 for random).
integer
Minimum value:
0 Maximum
value: 60
60
ssd-trim-weekday *
Day of week to run SSD Trim.
option
-sunday
Option
Description
sunday
Sunday
monday
Monday
tuesday
Tuesday
wednesday
Wednesday
thursday
Thursday
friday
Friday
saturday
Saturday
FortiOS 8.0.0 CLI Reference
1676
Fortinet Inc.

<!-- 来源页 1677 -->
Parameter
Description
Type
Size
Default
ssl-min-proto-version
Minimum supported protocol
version for SSL/TLS connections
(default = TLSv1.2).
option
-TLSv1-2
Option
Description
SSLv3
SSLv3.
TLSv1
TLSv1.
TLSv1-1
TLSv1.1.
TLSv1-2
TLSv1.2.
TLSv1-3
TLSv1.3.
ssl-static-key-ciphers
Enable/disable static key ciphers in
SSL/TLS connections (e.g. AES128-SHA, AES256-SHA, AES128-SHA256, AES256-SHA256).
option
-enable
Option
Description
enable
Enable static key ciphers in SSL/TLS connections.
disable
Disable static key ciphers in SSL/TLS connections.
sslvpn-affinity *
Agentless VPN CPU affinity.
string
Maximum
length: 79
0
sslvpn-max-worker-count *
Maximum number of Agentless VPN
processes. Upper limit for this value
is the number of CPUs and depends
on the model. Default value of zero
means the sslvpnd daemon decides
the number of worker processes.
integer
Minimum value:
0 Maximum
value: 7 **
0
sslvpn-web-mode *
Enable/disable Agentless VPN web
mode.
option
-disable
Option
Description
enable
Enable Agentless VPN web mode.
disable
Disable Agentless VPN web mode.
FortiOS 8.0.0 CLI Reference
1677
Fortinet Inc.

<!-- 来源页 1678 -->
Parameter
Description
Type
Size
Default
strict-dirty-session-check
Enable to check the session against
the original policy when
revalidating. This can prevent
dropping of redirected sessions
when web-filtering and
authentication are enabled
together. If this option is enabled,
the FortiGate unit deletes a session
if a routing or policy change causes
the session to no longer match the
policy that originally allowed the
session.
option
-enable
Option
Description
enable
Enable strict dirty-session check.
disable
Disable strict dirty-session check.
strong-crypto
Enable to use strong encryption and
only allow strong ciphers and digest
for HTTPS/SSH/TLS/SSL functions.
option
-enable
Option
Description
enable
Enable strong crypto for HTTPS/SSH/TLS/SSL.
disable
Disable strong crypto for HTTPS/SSH/TLS/SSL.
switch-controller
Enable/disable switch controller
feature. Switch controller allows
you to manage FortiSwitch from the
FortiGate itself.
option
-disable
Option
Description
disable
Disable switch controller feature.
enable
Enable switch controller feature.
switch-controller-reserved-network
Configure reserved network subnet
for managed switches. This is
available when the switch controller
is enabled.
ipv4-classnet-host
Not Specified
10.255.0.1
255.255.0.0
sys-perf-log-interval
Time in minutes between updates
of performance statistics logging. (1
- 15 min, default = 5, 0 = disabled).
integer
Minimum value:
0 Maximum
value: 15
5
FortiOS 8.0.0 CLI Reference
1678
Fortinet Inc.

<!-- 来源页 1679 -->
Parameter
Description
Type
Size
Default
syslog-affinity *
Affinity setting for syslog
(hexadecimal value up to 256 bits in
the format of xxxxxxxxxxxxxxxx).
string
Maximum
length: 79
0
tcp-congestion-control *
Configure TCP congestion control
algorithm (default = cubic).
option
-cubic
Option
Description
cubic
FortiGate unit employs a cubic function for TCP congestion
control.
bbr
FortiGate unit employs a bottleneck bandwidth and round-trip
propagation time (BBR) for TCP congestion control.
tcp-halfclose-timer
Number of seconds the FortiGate
unit should wait to close a session
after one peer has sent a FIN
packet but the other has not
responded (1 - 86400 sec (1 day),
default = 120).
integer
Minimum value:
1 Maximum
value: 86400
120
tcp-halfopen-timer
Number of seconds the FortiGate
unit should wait to close a session
after one peer has sent an open
session packet but the other has
not responded (1 - 86400 sec (1
day), default = 10).
integer
Minimum value:
1 Maximum
value: 86400
10
tcp-option
Enable SACK, timestamp and MSS
TCP options.
option
-enable
Option
Description
enable
Enable TCP option.
disable
Disable TCP option.
tcp-rst-timer
Length of the TCP CLOSE state in
seconds (5 - 300 sec, default = 5).
integer
Minimum value:
5 Maximum
value: 300
5
tcp-timewait-timer
Length of the TCP TIME-WAIT state
in seconds (1 - 300 sec, default = 1).
integer
Minimum value:
0 Maximum
value: 300
1
telemetry-controller
*
Enable/disable FortiTelemetry
controller to manage FortiTelemetry
agents.
option
-enable
FortiOS 8.0.0 CLI Reference
1679
Fortinet Inc.

<!-- 来源页 1680 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable FortiTelemetry controller.
disable
Disable FortiTelemetry controller.
telemetry-data-port
*
FortiTelemetry data channel port
(1024 - 49150, default = 35246).
integer
Minimum value:
1024 Maximum
value: 49150
35246
tftp
Enable/disable TFTP.
option
-enable
Option
Description
enable
Enable TFTP.
disable
Disable TFTP.
timezone
Timezone database name. Enter ?
to view the list of timezone.
string
Maximum
length: 63
tls-session-cache
Enable/disable TLS session cache.
option
-enable
Option
Description
enable
Enable TLS session cache.
disable
Disable TLS session cache.
traffic-priority
Choose Type of Service (ToS) or
Differentiated Services Code Point
(DSCP) for traffic prioritization in
traffic shaping.
option
-tos
Option
Description
tos
IP TOS.
dscp
DSCP (DiffServ) DS.
traffic-priority-level
Default system-wide level of
priority for traffic prioritization.
option
-medium
Option
Description
low
Low priority.
medium
Medium priority.
high
High priority.
FortiOS 8.0.0 CLI Reference
1680
Fortinet Inc.

<!-- 来源页 1681 -->
Parameter
Description
Type
Size
Default
two-factor-email-expiry
Email-based two-factor
authentication session timeout (30
- 300 seconds (5 minutes), default
= 60).
integer
Minimum value:
30 Maximum
value: 300
60
two-factor-fac-expiry
FortiAuthenticator token
authentication session timeout (10 -3600 seconds (1 hour), default =
60).
integer
Minimum value:
10 Maximum
value: 3600
60
two-factor-ftk-expiry
FortiToken authentication session
timeout (60 - 600 sec (10 minutes),
default = 60).
integer
Minimum value:
60 Maximum
value: 600
60
two-factor-ftm-expiry
FortiToken Mobile session timeout
(1 - 168 hours (7 days), default =
72).
integer
Minimum value:
1 Maximum
value: 168
72
two-factor-sms-expiry
SMS-based two-factor
authentication session timeout (30
- 300 sec, default = 60).
integer
Minimum value:
30 Maximum
value: 300
60
udp-idle-timer
UDP connection session timeout.
This command can be useful in
managing CPU and memory
resources (1 - 86400 seconds (1
day), default = 60).
integer
Minimum value:
1 Maximum
value: 86400
180
upgrade-report
Enable/disable the generation of an
upgrade report when upgrading the
firmware.
option
-enable
Option
Description
enable
Enable to automatically generate upgrade report when upgrading
the firmware.
disable
Disable upgrade report generation when upgrading the firmware.
url-filter-affinity *
URL filter CPU affinity.
string
Maximum
length: 79
0
url-filter-count
URL filter daemon count.
integer
Minimum value:
1 Maximum
value: 1 **
1 **
user-device-store-max-device-mem
Maximum percentage of total
system memory allowed to be used
for devices in the user device store.
integer
Minimum value:
1 Maximum
value: 5
2
FortiOS 8.0.0 CLI Reference
1681
Fortinet Inc.

<!-- 来源页 1682 -->
Parameter
Description
Type
Size
Default
user-device-store-max-devices
Maximum number of devices
allowed in user device store.
integer
Minimum value:
84219
Maximum
value: 240626
**
168438 **
user-device-store-max-unified-mem
Maximum unified memory allowed
in user device store.
integer
Minimum value:
168438251
Maximum
value:
1684382515 **
842191257 **
user-device-store-max-users
Maximum number of users allowed
in user device store.
integer
Minimum value:
84219
Maximum
value: 240626
**
168438 **
user-history-password-threshold
Maximum number of previous
passwords saved per admin/user (3
- 15, default = 3).
integer
Minimum value:
3 Maximum
value: 15
3
vdom-mode *
Enable/disable support for multiple
virtual domains (VDOMs).
option
-no-vdom
Option
Description
no-vdom
Disable multiple VDOMs mode.
multi-vdom
Enable multiple VDOMs mode.
vip-arp-range
Controls the number of ARPs that
the FortiGate sends for a Virtual IP
(VIP) address range.
option
-restricted
Option
Description
unlimited
Send ARPs for all addresses in VIP range.
restricted
Send ARPs for the first 8192 addresses in VIP range.
virtual-switch-vlan *
Enable/disable virtual switch VLAN.
option
-disable
Option
Description
enable
Enable virtual switch VLAN.
disable
Disable virtual switch VLAN.
wad-affinity *
Affinity setting for wad
(hexadecimal value up to 256 bits in
the format of xxxxxxxxxxxxxxxx).
string
Maximum
length: 79
0
FortiOS 8.0.0 CLI Reference
1682
Fortinet Inc.

<!-- 来源页 1683 -->
Parameter
Description
Type
Size
Default
wad-csvc-cs-count
Number of concurrent WAD-cache-service object-cache processes.
integer
Minimum value:
1 Maximum
value: 1
1
wad-csvc-db-count
Number of concurrent WAD-cache-service byte-cache processes.
integer
Minimum value:
0 Maximum
value: 8 **
0
wad-memory-change-granularity *
Minimum percentage change in
system memory usage detected by
the wad daemon prior to adjusting
TCP window size for any active
connection.
integer
Minimum value:
5 Maximum
value: 25
10
wad-p2s-max-body-size
Maximum size of the body of the
local out HTTP request (1 - 32
Mbytes, default = 4).
integer
Minimum value:
1 Maximum
value: 32
4
wad-restart-end-time *
WAD workers daily restart end time
(hh:mm).
user
Not Specified
wad-restart-mode *
WAD worker restart mode (default
= none).
option
-none
Option
Description
none
Disable restart of WAD workers.
time
Enable daily restart of WAD workers.
memory
Enable restart of WAD workers based on memory usage.
wad-restart-start-time *
WAD workers daily restart time
(hh:mm).
user
Not Specified
wad-source-affinity *
Enable/disable dispatching traffic
to WAD workers based on source
affinity.
option
-enable
Option
Description
disable
Disable dispatching traffic to WAD workers based on source
affinity.
enable
Enable dispatching traffic to WAD workers based on source
affinity.
FortiOS 8.0.0 CLI Reference
1683
Fortinet Inc.

<!-- 来源页 1684 -->
Parameter
Description
Type
Size
Default
wad-worker-count
Number of explicit proxy WAN
optimization daemon (WAD)
processes. By default WAN
optimization, explicit proxy, and
web caching is handled by all of the
CPU cores in a FortiGate unit.
integer
Minimum value:
0 Maximum
value: 8 **
0
wad-worker-dev-cache
Number of cached devices for each
ZTNA proxy worker. The default
value is tuned by memory
consumption. Set the option to 0 to
disable the cache.
integer
Minimum value:
0 Maximum
value: 10240
10240
wifi-ca-certificate
CA certificate that verifies the WiFi
certificate.
string
Maximum
length: 79
Fortinet_Wifi_
CA
wifi-certificate
Certificate to use for WiFi
authentication.
string
Maximum
length: 35
Fortinet_Wifi
wimax-4g-usb
Enable/disable comparability with
WiMAX 4G USB devices.
option
-disable
Option
Description
enable
Enable WiMax 4G.
disable
Disable WiMax 4G.
wireless-controller
Enable/disable the wireless
controller feature to use the
FortiGate unit to manage FortiAPs.
option
-enable
Option
Description
enable
Enable wireless controller.
disable
Disable wireless controller.
wireless-controller-port
Port used for the control channel in
wireless controller mode (wireless-mode is ac). The data channel port
is the control channel port number
plus one (1024 - 49150, default =
5246).
integer
Minimum value:
1024 Maximum
value: 49150
5246
wireless-mode *
Wireless mode setting.
option
-ac
Option
Description
ac
Wireless controller with local wireless.
FortiOS 8.0.0 CLI Reference
1684
Fortinet Inc.

---


<!-- 来源页 1801 -->
config system ipam
Configure IP address management services.
config system ipam
Description: Configure IP address management services.
set automatic-conflict-resolution [disable|enable]
set manage-lan-addresses [disable|enable]
set manage-lan-extension-addresses [disable|enable]
set manage-ssid-addresses [disable|enable]
config pools
Description: Configure IPAM pools.
edit <name>
set description {string}
config exclude
Description: Configure pool exclude subnets.
edit <ID>
set exclude-subnet {ipv4-classnet}
next
end
set subnet {ipv4-classnet}
next
end
set require-subnet-size-match [disable|enable]
config rules
Description: Configure IPAM allocation rules.
edit <name>
set description {string}
set device <name1>, <name2>, ...
set dhcp [enable|disable]
set dhcp-template {string}
set item-name <name1>, <name2>, ...
set item-type [interface|address]
set pool <name1>, <name2>, ...
set role [any|lan|...]
set vdom <name1>, <name2>, ...
next
end
set server-type {option}
set status [enable|disable]
end
config system ipam
Parameter
Description
Type
Size
Default
automatic-conflict-resolution
Enable/disable automatic conflict resolution.
option
-disable
FortiOS 8.0.0 CLI Reference
1801
Fortinet Inc.

<!-- 来源页 1802 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable automatic conflict resolution.
enable
Enable automatic conflict resolution.
manage-lan-addresses
Enable/disable default management of LAN
interface addresses.
option
-enable
Option
Description
disable
Disable LAN interface address management by default.
enable
Enable LAN interface address management by default.
manage-lan-extension-addresses
Enable/disable default management of
FortiExtender LAN extension interface addresses.
option
-enable
Option
Description
disable
Disable FortiExtender LAN extension interface address management by
default.
enable
Enable FortiExtender LAN extension interface address management by
default.
manage-ssid-addresses
Enable/disable default management of FortiAP SSID
addresses.
option
-enable
Option
Description
disable
Disable FortiAP SSID address management by default.
enable
Enable FortiAP SSID address management by default.
require-subnet-size-match
Enable/disable reassignment of subnets to make
requested and actual sizes match.
option
-enable
Option
Description
disable
Disable requiring subnet sizes to match.
enable
Enable requiring subnet sizes to match.
server-type
Configure the type of IPAM server to use.
option
-fabric-root
Option
Description
fabric-root
Use the IPAM server running on the Security Fabric root.
FortiOS 8.0.0 CLI Reference
1802
Fortinet Inc.

<!-- 来源页 1803 -->
Parameter
Description
Type
Size
Default
status
Enable/disable IP address management services.
option
-disable
Option
Description
enable
Enable integration with IP address management services.
disable
Disable integration with IP address management services.
config pools
Parameter
Description
Type
Size
Default
description
Description.
string
Maximum
length: 127
name
IPAM pool name.
string
Maximum
length: 79
subnet
Configure IPAM pool subnet, Class A - Class B
subnet.
ipv4-classnet
Not
Specified
0.0.0.0
0.0.0.0
config exclude
Parameter
Description
Type
Size
Default
ID
Exclude ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
exclude-subnet
Configure subnet to exclude from the IPAM pool.
ipv4-classnet
Not Specified
0.0.0.0
0.0.0.0
config rules
Parameter
Description
Type
Size
Default
description
Description.
string
Maximum
length: 127
device
<name>
Configure serial number or wildcard of FortiGate to
match.
FortiGate serial number or wildcard.
string
Maximum
length: 79
dhcp
Enable/disable DHCP server for matching IPAM
interfaces.
option
-disable
FortiOS 8.0.0 CLI Reference
1803
Fortinet Inc.

---


<!-- 来源页 1814 -->
Parameter
Description
Type
Size
Default
Option
Description
4-packets
4 packets.
16-packets
16 packets.
65-packets
65 packets.
262-packets
262 packets.
guaranteed-bandwidth
Guaranteed bandwidth.
integer
Minimum
value: 0
Maximum
value:
1000000000
0
maximum-bandwidth
Upper bandwidth limit enforced.
integer
Minimum
value: 0
Maximum
value:
1000000000
0
name
Profile name.
string
Maximum
length: 15
config system link-monitor
Configure Link Health Monitor.
config system link-monitor
Description: Configure Link Health Monitor.
edit <name>
set addr-mode [ipv4|ipv6]
set class-id {integer}
set diffservcode {user}
set fail-weight {integer}
set failtime {integer}
set gateway-ip {ipv4-address-any}
set gateway-ip6 {ipv6-address}
set ha-priority {integer}
set http-agent {string}
set http-get {string}
set http-match {string}
set interval {integer}
set packet-size {integer}
set password {password}
set port {integer}
set probe-count {integer}
set probe-timeout {integer}
set protocol {option1}, {option2}, ...
FortiOS 8.0.0 CLI Reference
1814
Fortinet Inc.

<!-- 来源页 1815 -->
set recoverytime {integer}
set route <subnet1>, <subnet2>, ...
set security-mode [none|authentication]
set server <address1>, <address2>, ...
set server-config [default|individual]
config server-list
Description: Servers for link-monitor to monitor.
edit <id>
set dst {string}
set port {integer}
set protocol {option1}, {option2}, ...
set weight {integer}
next
end
set server-type [static|dynamic]
set service-detection [enable|disable]
set source-ip {ipv4-address-any}
set source-ip6 {ipv6-address}
set srcintf {string}
set status [enable|disable]
set update-cascade-interface [enable|disable]
set update-policy-route [enable|disable]
set update-static-route [enable|disable]
next
end
config system link-monitor
Parameter
Description
Type
Size
Default
addr-mode
Address mode (IPv4 or IPv6).
option
-ipv4
Option
Description
ipv4
IPv4 mode.
ipv6
IPv6 mode.
class-id
Traffic class ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
diffservcode
Differentiated services code point (DSCP) in
the IP header of the probe packet.
user
Not Specified
fail-weight
Threshold weight to trigger link failure alert.
integer
Minimum value:
0 Maximum
value: 255
0
FortiOS 8.0.0 CLI Reference
1815
Fortinet Inc.

<!-- 来源页 1816 -->
Parameter
Description
Type
Size
Default
failtime
Number of retry attempts before the server
is considered down (1 - 3600, default = 5).
integer
Minimum value:
1 Maximum
value: 3600
5
gateway-ip
Gateway IP address used to probe the
server.
ipv4-address-any
Not Specified
0.0.0.0
gateway-ip6
Gateway IPv6 address used to probe the
server.
ipv6-address
Not Specified
::
ha-priority
HA election priority (1 - 50).
integer
Minimum value:
1 Maximum
value: 50
1
http-agent
String in the http-agent field in the HTTP
header.
string
Maximum
length: 1024
Chrome/
Safari/
http-get
If you are monitoring an HTML server you
can send an HTTP-GET request with a
custom string. Use this option to define the
string.
string
Maximum
length: 1024
/
http-match
String that you expect to see in the HTTP-GET requests of the traffic to be monitored.
string
Maximum
length: 1024
interval
Detection interval in milliseconds (20 - 3600
* 1000 msec, default = 500).
integer
Minimum value:
20 Maximum
value:
3600000
500
name
Link monitor name.
string
Maximum
length: 35
packet-size
Packet size of a TWAMP test session
(124/158 - 1024).
integer
Minimum value:
0 Maximum
value: 65535
124
password
TWAMP controller password in
authentication mode.
password
Not Specified
port
Port number of the traffic to be used to
monitor the server.
integer
Minimum value:
1 Maximum
value: 65535
0
probe-count
Number of most recent probes that should
be used to calculate latency and jitter (5 -30, default = 30).
integer
Minimum value:
5 Maximum
value: 30
30
probe-timeout
Time to wait before a probe packet is
considered lost (20 - 5000 msec, default =
500).
integer
Minimum value:
20 Maximum
value: 5000
500
FortiOS 8.0.0 CLI Reference
1816
Fortinet Inc.

<!-- 来源页 1817 -->
Parameter
Description
Type
Size
Default
protocol
Protocols used to monitor the server.
option
-ping
Option
Description
ping
PING link monitor.
tcp-echo
TCP echo link monitor.
udp-echo
UDP echo link monitor.
http
HTTP-GET link monitor.
https
HTTPS-GET link monitor.
twamp
TWAMP link monitor.
recoverytime
Number of successful responses received
before server is considered recovered (1 -3600, default = 5).
integer
Minimum value:
1 Maximum
value: 3600
5
route <subnet>
Subnet to monitor.
IP and netmask (x.x.x.x/y).
string
Maximum
length: 79
security-mode
Twamp controller security mode.
option
-none
Option
Description
none
Unauthenticated mode.
authentication
Authenticated mode.
server
<address>
IP address of the server(s) to be monitored.
Server address.
string
Maximum
length: 79
server-config
Mode of server configuration.
option
-default
Option
Description
default
All servers share the same attributes.
individual
Some attributes can be specified for individual servers.
server-type
Server type (static or dynamic).
option
-static
Option
Description
static
Static servers.
dynamic
Dynamic servers.
service-detection
Only use monitor to read quality values. If
enabled, static routes and cascade
interfaces will not be updated.
option
-disable
FortiOS 8.0.0 CLI Reference
1817
Fortinet Inc.

<!-- 来源页 1818 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Only use monitor for service-detection.
disable
Monitor will update routes/interfaces on link failure.
source-ip
Source IP address used in packet to the
server.
ipv4-address-any
Not Specified
0.0.0.0
source-ip6
Source IPv6 address used in packet to the
server.
ipv6-address
Not Specified
::
srcintf
Interface that receives the traffic to be
monitored.
string
Maximum
length: 15
status
Enable/disable this link monitor.
option
-enable
Option
Description
enable
Enable this link monitor.
disable
Disable this link monitor.
update-cascade-interface
Enable/disable update cascade interface.
option
-enable
Option
Description
enable
Enable update cascade interface.
disable
Disable update cascade interface.
update-policy-route
Enable/disable updating the policy route.
option
-enable
Option
Description
enable
Enable updating the policy route.
disable
Disable updating the policy route.
update-static-route
Enable/disable updating the static route.
option
-enable
Option
Description
enable
Enable updating the static route.
disable
Disable updating the static route.
FortiOS 8.0.0 CLI Reference
1818
Fortinet Inc.

---


<!-- 来源页 1853 -->
config system nd-proxy
Parameter
Description
Type
Size
Default
member
<interface-name>
Interfaces using the neighbor discovery proxy.
Interface name.
string
Maximum
length: 79
status
Enable/disable neighbor discovery proxy.
option
-disable
Option
Description
enable
Enable neighbor discovery proxy.
disable
Disable neighbor discovery proxy.
config system netflow
Configure NetFlow.
config system netflow
Description: Configure NetFlow.
set active-flow-timeout {integer}
config collectors
Description: Netflow collectors.
edit <id>
set collector-ip {string}
set collector-port {integer}
set interface {string}
set interface-select-method [auto|sdwan|...]
set source-ip {string}
set source-ip-interface {string}
set vrf-select {integer}
next
end
config exclusion-filters
Description: Exclusion filters
edit <id>
set destination-ip {user}
set destination-port {user}
set protocol {integer}
set source-ip {user}
set source-port {user}
next
end
set inactive-flow-timeout {integer}
set session-cache-size [min|default|...]
set template-tx-counter {integer}
set template-tx-timeout {integer}
end
FortiOS 8.0.0 CLI Reference
1853
Fortinet Inc.

<!-- 来源页 1854 -->
config system netflow
Parameter
Description
Type
Size
Default
active-flow-timeout
Timeout to report active flows (60 - 3600 sec,
default = 1800).
integer
Minimum
value: 60
Maximum
value: 3600
1800
inactive-flow-timeout
Timeout for periodic report of finished flows (10 -600 sec, default = 15).
integer
Minimum
value: 10
Maximum
value: 600
15
session-cache-size
Maximum RAM usage allowed for Netflow session
cache.
option
-default
Option
Description
min
Up to 0.5% of system RAM.
default
Up to 1% of system RAM.
max
Up to 2% of system RAM.
template-tx-counter
Counter of flowset records before resending a
template flowset record.
integer
Minimum
value: 10
Maximum
value: 6000
20
template-tx-timeout
Timeout for periodic template flowset transmission
(60 - 86400 sec, default = 1800).
integer
Minimum
value: 60
Maximum
value:
86400
1800
config collectors
Parameter
Description
Type
Size
Default
collector-ip
Collector IP.
string
Maximum
length: 63
collector-port
NetFlow collector port number.
integer
Minimum
value: 0
Maximum
value:
65535
2055
FortiOS 8.0.0 CLI Reference
1854
Fortinet Inc.

<!-- 来源页 1855 -->
Parameter
Description
Type
Size
Default
id
ID.
integer
Minimum
value: 1
Maximum
value: 6
0
interface
Specify outgoing interface to reach server.
string
Maximum
length: 15
interface-select-method
Specify how to select outgoing interface to reach
server.
option
-auto
Option
Description
auto
Set outgoing interface automatically.
sdwan
Set outgoing interface by SD-WAN or policy routing rules.
specify
Set outgoing interface manually.
source-ip
Source IP address for communication with the
NetFlow agent.
string
Maximum
length: 63
source-ip-interface
Name of the interface used to determine the source
IP for exporting packets.
string
Maximum
length: 15
vrf-select
VRF ID used for connection to server.
integer
Minimum
value: 0
Maximum
value: 511
0
config exclusion-filters
Parameter
Description
Type
Size
Default
destination-ip
Session destination address.
user
Not Specified
destination-port
Session destination port number or range.
user
Not Specified
id
Filter ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
protocol
Session IP protocol (0 - 255, default = 255,
meaning any).
integer
Minimum value:
0 Maximum
value: 255
255
source-ip
Session source address.
user
Not Specified
source-port
Session source port number or range.
user
Not Specified
FortiOS 8.0.0 CLI Reference
1855
Fortinet Inc.

---


<!-- 来源页 1986 -->
config system npu-vlink
Parameter
Description
Type
Size
Default
name
NPU VDOM link name in format npuX_vlink. X
means x-th pair of npu-vlink. Maximum 14
characters.
string
Maximum
length: 19
config system ntp
Configure system NTP information.
config system ntp
Description: Configure system NTP information.
set authentication [enable|disable]
set interface <interface-name1>, <interface-name2>, ...
set key {password}
set key-id {integer}
set key-type [MD5|SHA1|...]
config ntpserver
Description: Configure the FortiGate to connect to any available third-party NTP server.
edit <id>
set authentication [enable|disable]
set interface {string}
set interface-select-method [auto|sdwan|...]
set ip-type [IPv6|IPv4|...]
set key {password}
set key-id {integer}
set key-type [MD5|SHA1|...]
set ntpv3 [enable|disable]
set server {string}
set vrf-select {integer}
next
end
set ntpsync [enable|disable]
set server-mode [enable|disable]
set source-ip {ipv4-address}
set source-ip6 {ipv6-address}
set syncinterval {integer}
set type [fortiguard|custom]
end
config system ntp
Parameter
Description
Type
Size
Default
authentication
Enable/disable authentication.
option
-disable
FortiOS 8.0.0 CLI Reference
1986
Fortinet Inc.

<!-- 来源页 1987 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable authentication.
disable
Disable authentication.
interface
<interface-name>
FortiGate interface(s) with NTP server
mode enabled. Devices on your network
can contact these interfaces for NTP
services.
Interface name.
string
Maximum
length: 79
key
Key for authentication.
password
Not Specified
key-id
Key ID for authentication.
integer
Minimum value:
0 Maximum
value:
4294967295
0
key-type
Key type for authentication (MD5, SHA1,
SHA256).
option
-MD5
Option
Description
MD5
Use MD5 to authenticate the message.
SHA1
Use SHA1 to authenticate the message.
SHA256
Use SHA256 to authenticate the message.
ntpsync
Enable/disable setting the FortiGate
system time by synchronizing with an NTP
Server.
option
-disable
Option
Description
enable
Enable synchronization with NTP Server.
disable
Disable synchronization with NTP Server.
server-mode
Enable/disable FortiGate NTP Server
Mode. Your FortiGate becomes an NTP
server for other devices on your network.
The FortiGate relays NTP requests to its
configured NTP server.
option
-disable
Option
Description
enable
Enable FortiGate NTP Server Mode.
disable
Disable FortiGate NTP Server Mode.
FortiOS 8.0.0 CLI Reference
1987
Fortinet Inc.

<!-- 来源页 1988 -->
Parameter
Description
Type
Size
Default
source-ip
Source IP address for communication to
the NTP server.
ipv4-address
Not Specified
0.0.0.0
source-ip6
Source IPv6 address for communication to
the NTP server.
ipv6-address
Not Specified
::
syncinterval
NTP synchronization interval (1 - 1440
min).
integer
Minimum value:
1 Maximum
value: 1440
60
type
Use the FortiGuard NTP server or any
other available NTP Server.
option
-fortiguard
Option
Description
fortiguard
Use the FortiGuard NTP server.
custom
Use any other available NTP server.
config ntpserver
Parameter
Description
Type
Size
Default
authentication
Enable/disable authentication.
option
-disable
Option
Description
enable
Enable authentication.
disable
Disable authentication.
id
NTP server ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
interface
Specify outgoing interface to reach server.
string
Maximum
length: 15
interface-select-method
Specify how to select outgoing interface to
reach server.
option
-auto
Option
Description
auto
Set outgoing interface automatically.
sdwan
Set outgoing interface by SD-WAN or policy routing rules.
specify
Set outgoing interface manually.
ip-type
Choose to connect to IPv4 or/and IPv6 NTP
server.
option
-Both
FortiOS 8.0.0 CLI Reference
1988
Fortinet Inc.

---


<!-- 来源页 2003 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable PPPoE unnumbered negotiation.
disable
Disable PPPoE unnumbered negotiation.
service-name
PPPoE service name.
string
Maximum
length: 63
username
User name.
string
Maximum
length: 64
config system probe-response
Configure system probe response.
config system probe-response
Description: Configure system probe response.
set http-probe-value {string}
set mode [none|http-probe|...]
set password {password}
set port {integer}
set security-mode [none|authentication]
set timeout {integer}
set ttl-mode [reinit|decrease|...]
end
config system probe-response
Parameter
Description
Type
Size
Default
http-probe-value
Value to respond to the monitoring server.
string
Maximum
length:
1024
OK
mode
SLA response mode.
option
-none
Option
Description
none
Disable probe.
http-probe
HTTP probe.
twamp
Two way active measurement protocol.
password
TWAMP responder password in authentication
mode.
password
Not
Specified
FortiOS 8.0.0 CLI Reference
2003
Fortinet Inc.

---


<!-- 来源页 2004 -->
Parameter
Description
Type
Size
Default
port
Port number to response.
integer
Minimum
value: 1
Maximum
value:
65535
8008
security-mode
TWAMP responder security mode.
option
-none
Option
Description
none
Unauthenticated mode.
authentication
Authenticated mode.
timeout
An inactivity timer for a twamp test session.
integer
Minimum
value: 10
Maximum
value: 3600
300
ttl-mode
Mode for TWAMP packet TTL modification.
option
-retain
Option
Description
reinit
Reinitialize TTL.
decrease
Decrease TTL.
retain
Retain TTL.
config system proxy-arp
Configure proxy-ARP.
config system proxy-arp
Description: Configure proxy-ARP.
edit <id>
set end-ip {ipv4-address}
set interface {string}
set ip {ipv4-address}
next
end
FortiOS 8.0.0 CLI Reference
2004
Fortinet Inc.

---


<!-- 来源页 2060 -->
Parameter
Description
Type
Size
Default
Option
Description
static
Static routing.
dynamic
Dynamic routing.
sdn
SDN connector name.
string
Maximum
length: 35
status
SDN VPN status. Read-only.
integer
Minimum value:
0 Maximum
value: 255
0
subnet-id
AWS subnet id for TGW route propagation.
string
Maximum
length: 63
tgw-id
Transit gateway id.
string
Maximum
length: 63
tunnel-interface
Tunnel interface with public IP.
string
Maximum
length: 15
type
SDN VPN type. Read-only.
integer
Minimum value:
0 Maximum
value: 65535
0
vgw-id
Virtual private gateway id.
string
Maximum
length: 63
config system sdwan
Configure redundant Internet connections with multiple outbound links and health-check profiles.
config system sdwan
Description: Configure redundant Internet connections with multiple outbound links and health-check profiles.
set app-perf-log-period {integer}
config duplication
Description: Create SD-WAN duplication rules.
edit <id>
set dstaddr <name1>, <name2>, ...
set dstaddr6 <name1>, <name2>, ...
set dstintf <name1>, <name2>, ...
set members <seq-num1>, <seq-num2>, ...
set packet-de-duplication [enable|disable]
set packet-duplication [disable|force|...]
set service <name1>, <name2>, ...
set service-id <id1>, <id2>, ...
set sla-match-service [enable|disable]
set srcaddr <name1>, <name2>, ...
FortiOS 8.0.0 CLI Reference
2060
Fortinet Inc.

<!-- 来源页 2061 -->
set srcaddr6 <name1>, <name2>, ...
set srcintf <name1>, <name2>, ...
set tos {user}
set tos-mask {user}
next
end
set duplication-max-discrepancy {integer}
set duplication-max-num {integer}
set fail-alert-interfaces <name1>, <name2>, ...
set fail-detect [enable|disable]
config health-check
Description: SD-WAN status checking or health checking. Identify a server on the Internet
and determine how SD-WAN verifies that the FortiGate can communicate with it.
edit <name>
set addr-mode [ipv4|ipv6]
set agent-probe-timeout {integer}
set bandwidth-weight {integer}
set class-id {integer}
set detect-mode [active|passive|...]
set diffservcode {user}
set dns-match-ip {ipv4-address}
set dns-request-domain {string}
set embed-measured-health [enable|disable]
set failtime {integer}
set fortiguard [disable|enable]
set fortiguard-name {string}
set ftp-file {string}
set ftp-mode [passive|port]
set ha-priority {integer}
set http-agent {string}
set http-get {string}
set http-match {string}
set interval {integer}
set jitter-weight {integer}
set latency-weight {integer}
set members <seq-num1>, <seq-num2>, ...
set mos-codec [g711|g722|...]
set packet-loss-weight {integer}
set packet-size {integer}
set password {password}
set port {integer}
set probe-count {integer}
set probe-packets [disable|enable]
set probe-timeout {integer}
set protocol [ping|tcp-echo|...]
set quality-measured-method [half-open|half-close]
set recoverytime {integer}
set remote-probe-timeout {integer}
set security-mode [none|authentication]
set server {string}
config sla
Description: Service level agreement (SLA).
FortiOS 8.0.0 CLI Reference
2061
Fortinet Inc.

<!-- 来源页 2062 -->
edit <id>
set custom-profile-threshold {integer}
set jitter-threshold {integer}
set latency-threshold {integer}
set link-cost-factor {option1}, {option2}, ...
set mos-threshold {string}
set packetloss-threshold {integer}
set priority-in-sla {integer}
set priority-out-sla {integer}
next
end
set sla-fail-log-period {integer}
set sla-id-redistribute {integer}
set sla-pass-log-period {integer}
set source {ipv4-address}
set source6 {ipv6-address}
set system-dns [disable|enable]
set threshold-alert-jitter {integer}
set threshold-alert-latency {integer}
set threshold-alert-packetloss {integer}
set threshold-warning-jitter {integer}
set threshold-warning-latency {integer}
set threshold-warning-packetloss {integer}
set update-bgp-route [enable|disable]
set update-cascade-interface [enable|disable]
set update-static-route [enable|disable]
set user {string}
set vrf {integer}
next
end
set load-balance-mode [source-ip-based|weight-based|...]
config members
Description: FortiGate interfaces added to the SD-WAN.
edit <seq-num>
set billing-start-day {integer}
set comment {var-string}
set cost {integer}
set duplication-threshold-bandwidth [overlay|underlay]
set duplication-threshold-bibandwidth {integer}
set duplication-threshold-dwbandwidth {integer}
set duplication-threshold-upbandwidth {integer}
set gateway {ipv4-address}
set gateway6 {ipv6-address}
set ingress-spillover-threshold {integer}
set interface {string}
set overage [disable|enable]
set overage-cost {integer}
set overage-volume-ratio {integer}
set overage-weight {integer}
set preferred-source {ipv4-address}
set priority {integer}
set priority-in-sla {integer}
FortiOS 8.0.0 CLI Reference
2062
Fortinet Inc.

<!-- 来源页 2063 -->
set priority-out-sla {integer}
set priority6 {integer}
set quota-limit {integer}
set source {ipv4-address}
set source6 {ipv6-address}
set spillover-threshold {integer}
set status [disable|enable]
set transport-group {integer}
set volume-ratio {integer}
set weight {integer}
set zone {string}
next
end
config neighbor
Description: Create SD-WAN neighbors from BGP neighbor table to control route
advertisements according to SLA status.
edit <ip>
set health-check {string}
set member <seq-num1>, <seq-num2>, ...
set minimum-sla-meet-members {integer}
set mode [sla|speedtest]
set role [standalone|primary|...]
set route-metric [preferable|priority]
set service-id {integer}
set sla-id {integer}
next
end
set neighbor-hold-boot-time {integer}
set neighbor-hold-down [enable|disable]
set neighbor-hold-down-time {integer}
config service
Description: Create SD-WAN rules (also called services) to control how sessions are
distributed to interfaces in the SD-WAN.
edit <id>
set addr-mode [ipv4|ipv6]
set agent-exclusive [enable|disable]
set bandwidth-type [overlay|underlay]
set bandwidth-weight {integer}
set comment {var-string}
set default [enable|disable]
set dscp-forward [enable|disable]
set dscp-forward-tag {user}
set dscp-reverse [enable|disable]
set dscp-reverse-tag {user}
set dst <name1>, <name2>, ...
set dst-negate [enable|disable]
set dst6 <name1>, <name2>, ...
set end-port {integer}
set end-src-port {integer}
set fib-best-match-force [disable|enable]
set gateway [enable|disable]
set groups <name1>, <name2>, ...
FortiOS 8.0.0 CLI Reference
2063
Fortinet Inc.

<!-- 来源页 2064 -->
set hash-mode [round-robin|source-ip-based|...]
set health-check <name1>, <name2>, ...
set hold-down-time {integer}
set input-device <name1>, <name2>, ...
set input-device-negate [enable|disable]
set input-zone <name1>, <name2>, ...
set internet-service [enable|disable]
set internet-service-app-ctrl <id1>, <id2>, ...
set internet-service-app-ctrl-category <id1>, <id2>, ...
set internet-service-app-ctrl-group <name1>, <name2>, ...
set internet-service-custom <name1>, <name2>, ...
set internet-service-custom-group <name1>, <name2>, ...
set internet-service-fortiguard <name1>, <name2>, ...
set internet-service-group <name1>, <name2>, ...
set internet-service-name <name1>, <name2>, ...
set jitter-weight {integer}
set latency-weight {integer}
set link-cost-factor [latency|jitter|...]
set link-cost-threshold {integer}
set load-balance [enable|disable]
set minimum-sla-meet-members {integer}
set mode [auto|manual|...]
set name {string}
set packet-loss-weight {integer}
set passive-measurement [enable|disable]
set priority-members <seq-num1>, <seq-num2>, ...
set priority-zone <name1>, <name2>, ...
set protocol {integer}
set quality-link {integer}
set role [standalone|primary|...]
set shortcut [enable|disable]
set shortcut-priority [enable|disable|...]
config sla
Description: Service level agreement (SLA).
edit <health-check>
set id {integer}
next
end
set sla-compare-method [order|number]
set sla-stickiness [enable|disable]
set src <name1>, <name2>, ...
set src-negate [enable|disable]
set src6 <name1>, <name2>, ...
set standalone-action [enable|disable]
set start-port {integer}
set start-src-port {integer}
set status [enable|disable]
set tie-break [zone|cfg-order|...]
set tos {user}
set tos-mask {user}
set use-shortcut-sla [enable|disable]
set users <name1>, <name2>, ...
FortiOS 8.0.0 CLI Reference
2064
Fortinet Inc.

<!-- 来源页 2065 -->
set zone-mode [enable|disable]
next
end
set speedtest-bypass-routing [disable|enable]
set status [disable|enable]
config zone
Description: Configure SD-WAN zones.
edit <name>
set advpn-health-check {string}
set advpn-select [enable|disable]
set minimum-sla-meet-members {integer}
set service-sla-tie-break [cfg-order|fib-best-match|...]
next
end
end
config system sdwan
Parameter
Description
Type
Size
Default
app-perf-log-period
Time interval in seconds that application
performance logs are generated (0 - 3600,
default = 0).
integer
Minimum
value: 0
Maximum
value: 3600
0
duplication-max-discrepancy
Maximum discrepancy between two packets for
deduplication in milliseconds (250 - 1000, default
= 250).
integer
Minimum
value: 250
Maximum
value: 1000
250
duplication-max-num
Maximum number of interface members a packet
is duplicated in the SD-WAN zone (2 - 4, default =
2; if set to 3, the original packet plus 2 more
copies are created).
integer
Minimum
value: 2
Maximum
value: 4
2
fail-alert-interfaces
<name>
Physical interfaces that will be alerted.
Physical interface name.
string
Maximum
length: 79
fail-detect
Enable/disable SD-WAN Internet connection
status checking (failure detection).
option
-disable
Option
Description
enable
Enable status checking.
disable
Disable status checking.
load-balance-mode
Algorithm or mode to use for load balancing
Internet traffic to SD-WAN members.
option
-source-ip-based
FortiOS 8.0.0 CLI Reference
2065
Fortinet Inc.

<!-- 来源页 2066 -->
Parameter
Description
Type
Size
Default
Option
Description
source-ip-based
Source IP load balancing. All traffic from a source IP is sent to the same
interface.
weight-based
Weight-based load balancing. Interfaces with higher weights have
higher priority and get more traffic.
usage-based
Usage-based load balancing. All traffic is sent to the first interface on
the list. When the bandwidth on that interface exceeds the spill-over
limit new traffic is sent to the next interface.
source-dest-ip-based
Source and destination IP load balancing. All traffic from a source IP to a
destination IP is sent to the same interface.
measured-volume-based
Volume-based load balancing. Traffic is load balanced based on traffic
volume (in bytes). More traffic is sent to interfaces with higher volume
ratios.
neighbor-hold-boot-time
Waiting period in seconds when switching from
the primary neighbor to the secondary neighbor
from the neighbor start. (0 - 10000000, default =
0).
integer
Minimum
value: 0
Maximum
value:
10000000
0
neighbor-hold-down
Enable/disable hold switching from the secondary
neighbor to the primary neighbor.
option
-disable
Option
Description
enable
Enable hold switching from the secondary neighbor to the primary
neighbor.
disable
Disable hold switching from the secondary neighbor to the primary
neighbor.
neighbor-hold-down-time
Waiting period in seconds when switching from
the secondary neighbor to the primary neighbor
when hold-down is disabled. (0 - 10000000,
default = 0).
integer
Minimum
value: 0
Maximum
value:
10000000
0
speedtest-bypass-routing
Enable/disable bypass routing when speedtest on
a SD-WAN member.
option
-disable
Option
Description
disable
Disable SD-WAN.
enable
Enable SD-WAN.
FortiOS 8.0.0 CLI Reference
2066
Fortinet Inc.

<!-- 来源页 2067 -->
Parameter
Description
Type
Size
Default
status
Enable/disable SD-WAN.
option
-disable
Option
Description
disable
Disable SD-WAN.
enable
Enable SD-WAN.
config duplication
Parameter
Description
Type
Size
Default
dstaddr
<name>
Destination address or address group names.
Address or address group name.
string
Maximum
length: 79
dstaddr6
<name>
Destination address6 or address6 group names.
Address6 or address6 group name.
string
Maximum
length: 79
dstintf
<name>
Outgoing (egress) interfaces or zones.
Interface, zone or SDWAN zone name.
string
Maximum
length: 79
id
Duplication rule ID (1 - 255).
integer
Minimum value:
1 Maximum
value: 255
0
members
<seq-num> *
Member sequence number list.
Member sequence number.
integer
Minimum value:
0 Maximum
value:
4294967295
packet-de-duplication
Enable/disable discarding of packets that have
been duplicated.
option
-disable
Option
Description
enable
Enable discarding of packets that have been duplicated.
disable
Disable discarding of packets that have been duplicated.
packet-duplication
Configure packet duplication method.
option
-disable
Option
Description
disable
Disable packet duplication.
force
Duplicate packets across all interface members of the SD-WAN zone.
on-demand
Duplicate packets across all interface members of the SD-WAN zone
based on the link quality.
FortiOS 8.0.0 CLI Reference
2067
Fortinet Inc.

<!-- 来源页 2068 -->
Parameter
Description
Type
Size
Default
service
<name>
Service and service group name.
Service and service group name.
string
Maximum
length: 79
service-id
<id>
SD-WAN service rule ID list.
SD-WAN service rule ID.
integer
Minimum value:
0 Maximum
value:
4294967295
sla-match-service
Enable/disable packet duplication matching
health-check SLAs in service rule.
option
-disable
Option
Description
enable
Enable packet duplication matching health-check SLAs in service rule
(matching all SLAs of current defined service).
disable
Disable packet duplication matching health-check SLAs in service rule
(matching all SLAs of all defined health-check).
srcaddr
<name>
Source address or address group names.
Address or address group name.
string
Maximum
length: 79
srcaddr6
<name>
Source address6 or address6 group names.
Address6 or address6 group name.
string
Maximum
length: 79
srcintf
<name>
Incoming (ingress) interfaces or zones.
Interface, zone or SDWAN zone name.
string
Maximum
length: 79
tos *
Type of service bit pattern.
user
Not Specified
tos-mask *
Type of service evaluated bits.
user
Not Specified
* This parameter may not exist in some models.
config health-check
Parameter
Description
Type
Size
Default
addr-mode
Address mode (IPv4 or IPv6).
option
-ipv4
Option
Description
ipv4
IPv4 mode.
ipv6
IPv6 mode.
agent-probe-timeout
Time to wait before a probe packet
is considered lost when detect-mode is agent (5000 - 3600*1000
msec, default = 60000).
integer
Minimum value:
5000 Maximum
value:
3600000
60000
FortiOS 8.0.0 CLI Reference
2068
Fortinet Inc.

<!-- 来源页 2069 -->
Parameter
Description
Type
Size
Default
bandwidth-weight
Coefficient of reciprocal of
available bidirectional bandwidth
in the formula of custom-profile-1.
integer
Minimum value:
0 Maximum
value:
10000000
0
class-id
Traffic class ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
detect-mode
The mode determining how to
detect the server.
option
-active
Option
Description
active
The probes are sent actively.
passive
The traffic measures health without probes.
prefer-passive
The probes are sent in case of no new traffic.
remote
Link health obtained from remote peers.
agent-based
Traffic health is measured from the fabric connectors.
diffservcode
Differentiated services code point
(DSCP) in the IP header of the
probe packet.
user
Not Specified
dns-match-ip
Response IP expected from DNS
server if the protocol is DNS.
ipv4-address
Not Specified
0.0.0.0
dns-request-domain
Fully qualified domain name to
resolve for the DNS probe.
string
Maximum
length: 255
www.example.com
embed-measured-health
Enable/disable embedding
measured health information.
option
-disable
Option
Description
enable
Enable embed measured health.
disable
Disable embed measured health.
failtime
Number of failures before server is
considered lost (1 - 3600, default
= 5).
integer
Minimum value:
1 Maximum
value: 3600
5
fortiguard
Enable/disable use of FortiGuard
predefined server.
option
-disable
FortiOS 8.0.0 CLI Reference
2069
Fortinet Inc.

<!-- 来源页 2070 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable use of FortiGuard predefined server.
enable
Enable use of FortiGuard predefined server.
fortiguard-name
Predefined health-check target
name.
string
Maximum
length: 35
ftp-file
Full path and file name on the FTP
server to download for FTP health-check to probe.
string
Maximum
length: 254
ftp-mode
FTP mode.
option
-passive
Option
Description
passive
The FTP health-check initiates and establishes the data connection.
port
The FTP server initiates and establishes the data connection.
ha-priority
HA election priority (1 - 50).
integer
Minimum value:
1 Maximum
value: 50
1
http-agent
String in the http-agent field in the
HTTP header.
string
Maximum
length: 1024
Chrome/ Safari/
http-get
URL used to communicate with the
server if the protocol if the
protocol is HTTP.
string
Maximum
length: 1024
/
http-match
Response string expected from the
server if the protocol is HTTP.
string
Maximum
length: 1024
interval
Status check interval in
milliseconds, or the time between
attempting to connect to the
server (20 - 3600*1000 msec,
default = 500).
integer
Minimum value:
20 Maximum
value:
3600000
500
jitter-weight
Coefficient of jitter in the formula
of custom-profile-1.
integer
Minimum value:
0 Maximum
value:
10000000
0
latency-weight
Coefficient of latency in the
formula of custom-profile-1.
integer
Minimum value:
0 Maximum
value:
10000000
0
FortiOS 8.0.0 CLI Reference
2070
Fortinet Inc.

<!-- 来源页 2071 -->
Parameter
Description
Type
Size
Default
members
<seq-num>
Member sequence number list.
Member sequence number.
integer
Minimum value:
0 Maximum
value:
4294967295
mos-codec
Codec to use for MOS calculation
(default = g711).
option
-g711
Option
Description
g711
Calculate MOS based on the G.711 codec.
g722
Calculate MOS based on the G.722 codec.
g729
Calculate MOS based on the G.729 codec.
name
Status check or health check
name.
string
Maximum
length: 35
packet-loss-weight
Coefficient of packet-loss in the
formula of custom-profile-1.
integer
Minimum value:
0 Maximum
value:
10000000
0
packet-size
Packet size of a TWAMP test
session. (124/158 - 1024)
integer
Minimum value:
0 Maximum
value: 65535
124
password
TWAMP controller password in
authentication mode.
password
Not Specified
port
Port number used to communicate
with the server over the selected
protocol (0 - 65535, default = 0,
auto select. http, tcp-connect: 80,
udp-echo, tcp-echo: 7, dns: 53,
ftp: 21, twamp: 862).
integer
Minimum value:
0 Maximum
value: 65535
0
probe-count
Number of most recent probes
that should be used to calculate
latency and jitter (5 - 30, default =
30).
integer
Minimum value:
5 Maximum
value: 30
30
probe-packets
Enable/disable transmission of
probe packets.
option
-enable
Option
Description
disable
Disable transmission of probe packets.
enable
Enable transmission of probe packets.
FortiOS 8.0.0 CLI Reference
2071
Fortinet Inc.

<!-- 来源页 2072 -->
Parameter
Description
Type
Size
Default
probe-timeout
Time to wait before a probe packet
is considered lost (20 - 3600*1000
msec, default = 500).
integer
Minimum value:
20 Maximum
value:
3600000
500
protocol
Protocol used to determine if the
FortiGate can communicate with
the server.
option
-ping
Option
Description
ping
Use PING to test the link with the server.
tcp-echo
Use TCP echo to test the link with the server.
udp-echo
Use UDP echo to test the link with the server.
http
Use HTTP-GET to test the link with the server.
https
Use HTTPS-GET to test the link with the server.
twamp
Use TWAMP to test the link with the server.
dns
Use DNS query to test the link with the server.
tcp-connect
Use a full TCP connection to test the link with the server.
ftp
Use FTP to test the link with the server.
quality-measured-method
Method to measure the quality of
tcp-connect.
option
-half-open
Option
Description
half-open
Measure the round trip between syn and ack.
half-close
Measure the round trip between fin and ack.
recoverytime
Number of successful responses
received before server is
considered recovered (1 - 3600,
default = 5).
integer
Minimum value:
1 Maximum
value: 3600
5
remote-probe-timeout
Time to wait before a probe packet
is considered lost when detect-mode is remote (20 - 3600*1000
msec, default = 5000).
integer
Minimum value:
20 Maximum
value:
3600000
5000
security-mode
Twamp controller security mode.
option
-none
Option
Description
none
Unauthenticated mode.
FortiOS 8.0.0 CLI Reference
2072
Fortinet Inc.

<!-- 来源页 2073 -->
Parameter
Description
Type
Size
Default
Option
Description
authentication
Authenticated mode.
server
IP address or FQDN name of the
server.
string
Maximum
length: 79
sla-fail-log-period
Time interval in seconds that SLA
fail log messages will be generated
(0 - 3600, default = 0).
integer
Minimum value:
0 Maximum
value: 3600
0
sla-id-redistribute
Select the ID from the SLA sub-table. The selected SLA's priority
value will be distributed into the
routing table (0 - 32, default = 0).
integer
Minimum value:
0 Maximum
value: 32
0
sla-pass-log-period
Time interval in seconds that SLA
pass log messages will be
generated (0 - 3600, default = 0).
integer
Minimum value:
0 Maximum
value: 3600
0
source
Source IP address used in the
health-check packet to the server.
ipv4-address
Not Specified
0.0.0.0
source6
Source IPv6 address used in the
health-check packet to server.
ipv6-address
Not Specified
::
system-dns
Enable/disable system DNS as the
probe server.
option
-disable
Option
Description
disable
Disable system DNS as the probe server.
enable
Enable system DNS as the probe server.
threshold-alert-jitter
Alert threshold for jitter (ms,
default = 0).
integer
Minimum value:
0 Maximum
value:
4294967295
0
threshold-alert-latency
Alert threshold for latency (ms,
default = 0).
integer
Minimum value:
0 Maximum
value:
4294967295
0
threshold-alert-packetloss
Alert threshold for packet loss
(percentage, default = 0).
integer
Minimum value:
0 Maximum
value: 100
0
FortiOS 8.0.0 CLI Reference
2073
Fortinet Inc.

<!-- 来源页 2074 -->
Parameter
Description
Type
Size
Default
threshold-warning-jitter
Warning threshold for jitter (ms,
default = 0).
integer
Minimum value:
0 Maximum
value:
4294967295
0
threshold-warning-latency
Warning threshold for latency (ms,
default = 0).
integer
Minimum value:
0 Maximum
value:
4294967295
0
threshold-warning-packetloss
Warning threshold for packet loss
(percentage, default = 0).
integer
Minimum value:
0 Maximum
value: 100
0
update-bgp-route
Enable/disable updating the BGP
route.
option
-disable
Option
Description
enable
Enable updating the BGP route.
disable
Disable updating the BGP route.
update-cascade-interface
Enable/disable update cascade
interface.
option
-enable
Option
Description
enable
Enable update cascade interface.
disable
Disable update cascade interface.
update-static-route
Enable/disable updating the static
route.
option
-enable
Option
Description
enable
Enable updating the static route.
disable
Disable updating the static route.
user
The user name to access probe
server.
string
Maximum
length: 64
vrf
Virtual Routing Forwarding ID.
integer
Minimum value:
0 Maximum
value: 511
0
FortiOS 8.0.0 CLI Reference
2074
Fortinet Inc.

<!-- 来源页 2075 -->
config sla
Parameter
Description
Type
Size
Default
custom-profile-threshold
Custom profile threshold for SLA to be marked as
pass(0 - 10000000, default = 0).
integer
Minimum
value: 0
Maximum
value:
10000000
0
id
SLA ID.
integer
Minimum
value: 1
Maximum
value: 32
0
jitter-threshold
Jitter for SLA to make decision in milliseconds. (0 -10000000, default = 5).
integer
Minimum
value: 0
Maximum
value:
10000000
5
latency-threshold
Latency for SLA to make decision in milliseconds.
(0 - 10000000, default = 5).
integer
Minimum
value: 0
Maximum
value:
10000000
5
link-cost-factor
Criteria on which to base link selection.
option
-latency
jitter
packet-loss
custom-profile-1
Option
Description
latency
Select link based on latency.
jitter
Select link based on jitter.
packet-loss
Select link based on packet loss.
custom-profile-1
Select link based on custom profile.
mos
Select link based on Mean Opinion Score (MOS).
remote
Select link based on available remote SLA status.
mos-threshold
Minimum mean opinion score for SLA to be
marked as pass(1.0 - 5.0, default = 3.6).
string
Maximum
length: 35
3.6
FortiOS 8.0.0 CLI Reference
2075
Fortinet Inc.

<!-- 来源页 2076 -->
Parameter
Description
Type
Size
Default
packetloss-threshold
Packet loss for SLA to make decision in
percentage. (0 - 100, default = 0).
integer
Minimum
value: 0
Maximum
value: 100
0
priority-in-sla
Value to be distributed into routing table when in-sla (0 - 65535, default = 0).
integer
Minimum
value: 0
Maximum
value:
65535
0
priority-out-sla
Value to be distributed into routing table when
out-sla (0 - 65535, default = 0).
integer
Minimum
value: 0
Maximum
value:
65535
0
config members
Parameter
Description
Type
Size
Default
billing-start-day *
Volume billing start day when this member's
volume usgage will begin to calculate.
integer
Minimum value:
1 Maximum
value: 31
1
comment
Comments.
var-string
Maximum
length: 255
cost
Cost of this interface for services in SLA mode
(0 - 4294967295, default = 0).
integer
Minimum value:
0 Maximum
value:
4294967295
0
duplication-threshold-bandwidth *
Configure duplication threshold bandwidth
interface in the SD-WAN.
option
-overlay
Option
Description
overlay
Use overlay interface bandwidth for duplication in the SD-WAN.
underlay
Use underlay interface bandwidth for duplication in the SD-WAN.
duplication-threshold-bibandwidth *
Bandwidth bistream threshold value in
kilobytes per second (0 - 4294967295,
default = 0).
integer
Minimum value:
0 Maximum
value:
4294967295
0
FortiOS 8.0.0 CLI Reference
2076
Fortinet Inc.

<!-- 来源页 2077 -->
Parameter
Description
Type
Size
Default
duplication-threshold-dwbandwidth *
Bandwidth downstream threshold value in
kilobytes per second (0 - 4294967295,
default = 0).
integer
Minimum value:
0 Maximum
value:
4294967295
0
duplication-threshold-upbandwidth *
Bandwidth upstream threshold value in
kilobytes per second (0 - 4294967295,
default = 0).
integer
Minimum value:
0 Maximum
value:
4294967295
0
gateway
The default gateway for this interface. Usually
the default gateway of the Internet service
provider that this interface is connected to.
ipv4-address
Not Specified
0.0.0.0
gateway6
IPv6 gateway.
ipv6-address
Not Specified
::
ingress-spillover-threshold
Ingress spillover threshold for this interface (0
- 16776000 kbit/s). When this traffic volume
threshold is reached, new sessions spill over
to other interfaces in the SD-WAN.
integer
Minimum value:
0 Maximum
value:
16776000
0
interface
Interface name.
string
Maximum
length: 15
overage *
Enable/disable the volume overage when
member's volume usage reaches quota-limit.
option
-enable
Option
Description
disable
Disable the volume usage overage.
enable
Enable the volume usage overage.
overage-cost *
Cost value for this member when its volume is
over quota and overage is enabled(0 -4294967295, default = 0).
integer
Minimum value:
0 Maximum
value:
4294967295
0
overage-volume-ratio *
Volume ratio value for this member when its
volume is over quota and overage is enabled(1
- 255, default = 1).
integer
Minimum value:
1 Maximum
value: 255
1
overage-weight
*
Weight value for this member when its volume
is over quota and overage is enabled.
integer
Minimum value:
0 Maximum
value: 255
1
preferred-source
Preferred source of route for this member.
ipv4-address
Not Specified
0.0.0.0
FortiOS 8.0.0 CLI Reference
2077
Fortinet Inc.

<!-- 来源页 2078 -->
Parameter
Description
Type
Size
Default
priority
Priority of the interface for IPv4 (1 - 65535,
default = 1). Used for SD-WAN rules or priority
rules.
integer
Minimum value:
1 Maximum
value: 65535
1
priority-in-sla
Preferred priority of routes to this member
when this member is in-sla (0 - 65535, default
= 0).
integer
Minimum value:
0 Maximum
value: 65535
0
priority-out-sla
Preferred priority of routes to this member
when this member is out-of-sla (0 - 65535,
default = 0).
integer
Minimum value:
0 Maximum
value: 65535
0
priority6
Priority of the interface for IPv6 (1 - 65535,
default = 1024). Used for SD-WAN rules or
priority rules.
integer
Minimum value:
1 Maximum
value: 65535
1024
quota-limit *
Volume quota limit assigned to this member in
gigabytes (0 - 10485760, default = 0).
integer
Minimum value:
0 Maximum
value:
10485760
0
seq-num
Sequence number(1-512).
integer
Minimum value:
0 Maximum
value: 512
0
source
Source IP address used in the health-check
packet to the server.
ipv4-address
Not Specified
0.0.0.0
source6
Source IPv6 address used in the health-check
packet to the server.
ipv6-address
Not Specified
::
spillover-threshold
Egress spillover threshold for this interface (0
- 16776000 kbit/s). When this traffic volume
threshold is reached, new sessions spill over
to other interfaces in the SD-WAN.
integer
Minimum value:
0 Maximum
value:
16776000
0
status
Enable/disable this interface in the SD-WAN.
option
-enable
Option
Description
disable
Disable this interface in the SD-WAN.
enable
Enable this interface in the SD-WAN.
transport-group
Measured transport group (0 - 255).
integer
Minimum value:
0 Maximum
value: 255
0
volume-ratio
Measured volume ratio (this value / sum of all
values = percentage of link volume, 1 - 255).
integer
Minimum value:
1 Maximum
value: 255
1
FortiOS 8.0.0 CLI Reference
2078
Fortinet Inc.

<!-- 来源页 2079 -->
Parameter
Description
Type
Size
Default
weight
Weight of this interface for weighted load
balancing. (1 - 255) More traffic is directed to
interfaces with higher weights.
integer
Minimum value:
1 Maximum
value: 255
1
zone
Zone name.
string
Maximum
length: 35
virtual-wan-link
* This parameter may not exist in some models.
config neighbor
Parameter
Description
Type
Size
Default
health-check
SD-WAN health-check name.
string
Maximum
length: 35
ip
IP/IPv6 address of neighbor or neighbor-group name.
string
Maximum
length: 45
member
<seq-num>
Member sequence number list.
Member sequence number.
integer
Minimum value:
0 Maximum
value:
4294967295
minimum-sla-meet-members
Minimum number of members which meet
SLA when the neighbor is preferred.
integer
Minimum value:
1 Maximum
value: 255
1
mode
What metric to select the neighbor.
option
-sla
Option
Description
sla
Select neighbor based on SLA link quality.
speedtest
Select neighbor based on the speedtest status.
role
Role of neighbor.
option
-standalone
Option
Description
standalone
Standalone neighbor.
primary
Primary neighbor.
secondary
Secondary neighbor.
route-metric
Route-metric of neighbor.
option
-preferable
Option
Description
preferable
Select neighbor based on its hc to match bgp preferable/unpreferable
route_map.
FortiOS 8.0.0 CLI Reference
2079
Fortinet Inc.

<!-- 来源页 2080 -->
Parameter
Description
Type
Size
Default
Option
Description
priority
Select neighbor based on its members' priority-in-sla/priority-out-sla
value.
service-id
SD-WAN service ID to work with the
neighbor.
integer
Minimum value:
0 Maximum
value:
4294967295
0
sla-id
SLA ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config service
Parameter
Description
Type
Size
Default
addr-mode
Address mode (IPv4 or IPv6).
option
-ipv4
Option
Description
ipv4
IPv4 mode.
ipv6
IPv6 mode.
agent-exclusive
Set/unset the service as agent use
exclusively.
option
-disable
Option
Description
enable
Set the service as agent use exclusively.
disable
Unset the service as agent use exclusively.
bandwidth-type
*
Overlay/underlay bandwidth-type.
option
-overlay
Option
Description
overlay
Overlay bandwidth.
underlay
Underlay bandwidth.
bandwidth-weight
Coefficient of reciprocal of available
bidirectional bandwidth in the formula of
custom-profile-1.
integer
Minimum value:
0 Maximum
value:
10000000
0
FortiOS 8.0.0 CLI Reference
2080
Fortinet Inc.

<!-- 来源页 2081 -->
Parameter
Description
Type
Size
Default
comment
Comments.
var-string
Maximum
length: 255
default
Enable/disable use of SD-WAN as default
service.
option
-disable
Option
Description
enable
Enable use of SD-WAN as default service.
disable
Disable use of SD-WAN as default service.
dscp-forward
Enable/disable forward traffic DSCP tag.
option
-disable
Option
Description
enable
Enable use of forward DSCP tag.
disable
Disable use of forward DSCP tag.
dscp-forward-tag
Forward traffic DSCP tag.
user
Not Specified
dscp-reverse
Enable/disable reverse traffic DSCP tag.
option
-disable
Option
Description
enable
Enable use of reverse DSCP tag.
disable
Disable use of reverse DSCP tag.
dscp-reverse-tag
Reverse traffic DSCP tag.
user
Not Specified
dst <name>
Destination address name.
Address or address group name.
string
Maximum
length: 79
dst-negate
Enable/disable negation of destination
address match.
option
-disable
Option
Description
enable
Enable destination address negation.
disable
Disable destination address negation.
dst6 <name>
Destination address6 name.
Address6 or address6 group name.
string
Maximum
length: 79
end-port
End destination port number.
integer
Minimum value:
0 Maximum
value: 65535
65535
FortiOS 8.0.0 CLI Reference
2081
Fortinet Inc.

<!-- 来源页 2082 -->
Parameter
Description
Type
Size
Default
end-src-port
End source port number.
integer
Minimum value:
0 Maximum
value: 65535
65535
fib-best-match-force
Enable/disable force using fib-best-match
oif as outgoing interface.
option
-disable
Option
Description
disable
Do not force using fib-best-match oif as outgoing interface.
enable
Force using fib-best-match oif as outgoing interface.
gateway
Enable/disable SD-WAN service gateway.
option
-disable
Option
Description
enable
Enable SD-WAN service gateway.
disable
Disable SD-WAN service gateway.
groups <name>
User groups.
Group name.
string
Maximum
length: 79
hash-mode
Hash algorithm for selected priority
members for load balance mode.
option
-round-robin
Option
Description
round-robin
All traffic are distributed to selected interfaces in equal portions and
circular order.
source-ip-based
All traffic from a source IP is sent to the same interface.
source-dest-ip-based
All traffic from a source IP to a destination IP is sent to the same
interface.
inbandwidth
All traffic are distributed to a selected interface with most available
bandwidth for incoming traffic.
outbandwidth
All traffic are distributed to a selected interface with most available
bandwidth for outgoing traffic.
bibandwidth
All traffic are distributed to a selected interface with most available
bandwidth for both incoming and outgoing traffic.
health-check
<name>
Health check list.
Health check name.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
2082
Fortinet Inc.

<!-- 来源页 2083 -->
Parameter
Description
Type
Size
Default
hold-down-time
Waiting period in seconds when switching
from the back-up member to the primary
member (0 - 10000000, default = 0).
integer
Minimum value:
0 Maximum
value:
10000000
0
id
SD-WAN rule ID (1 - 4000).
integer
Minimum value:
1 Maximum
value: 4000
0
input-device
<name>
Source interface name.
Interface name.
string
Maximum
length: 79
input-device-negate
Enable/disable negation of input device
match.
option
-disable
Option
Description
enable
Enable negation of input device match.
disable
Disable negation of input device match.
input-zone
<name>
Source input-zone name.
Zone.
string
Maximum
length: 79
internet-service
Enable/disable use of Internet service for
application-based load balancing.
option
-disable
Option
Description
enable
Enable cloud service to support application-based load balancing.
disable
Disable cloud service to support application-based load balancing.
internet-service-app-ctrl <id>
Application control based Internet Service
ID list.
Application control based Internet Service
ID.
integer
Minimum value:
0 Maximum
value:
4294967295
internet-service-app-ctrl-category
<id>
IDs of one or more application control
categories.
Application control category ID.
integer
Minimum value:
0 Maximum
value:
4294967295
internet-service-app-ctrl-group
<name>
Application control based Internet Service
group list.
Application control based Internet Service
group name.
string
Maximum
length: 79
internet-service-custom
<name>
Custom Internet service name list.
Custom Internet service name.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
2083
Fortinet Inc.

<!-- 来源页 2084 -->
Parameter
Description
Type
Size
Default
internet-service-custom-group
<name>
Custom Internet Service group list.
Custom Internet Service group name.
string
Maximum
length: 79
internet-service-fortiguard
<name>
FortiGuard Internet service name list.
FortiGuard Internet service name.
string
Maximum
length: 79
internet-service-group
<name>
Internet Service group list.
Internet Service group name.
string
Maximum
length: 79
internet-service-name
<name>
Internet service name list.
Internet service name.
string
Maximum
length: 79
jitter-weight
Coefficient of jitter in the formula of
custom-profile-1.
integer
Minimum value:
0 Maximum
value:
10000000
0
latency-weight
Coefficient of latency in the formula of
custom-profile-1.
integer
Minimum value:
0 Maximum
value:
10000000
0
link-cost-factor
Link cost factor.
option
-latency
Option
Description
latency
Select link based on latency.
jitter
Select link based on jitter.
packet-loss
Select link based on packet loss.
inbandwidth
Select link based on available bandwidth of incoming traffic.
outbandwidth
Select link based on available bandwidth of outgoing traffic.
bibandwidth
Select link based on available bandwidth of bidirectional traffic.
custom-profile-1
Select link based on customized profile.
link-cost-threshold
Percentage threshold change of link cost
values that will result in policy route
regeneration (0 - 10000000, default = 10).
integer
Minimum value:
0 Maximum
value:
10000000
10
load-balance
Enable/disable load-balance.
option
-disable
FortiOS 8.0.0 CLI Reference
2084
Fortinet Inc.

<!-- 来源页 2085 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable load-balance.
disable
Disable load-balance.
minimum-sla-meet-members
Minimum number of members which meet
SLA.
integer
Minimum value:
0 Maximum
value: 255
0
mode
Control how the SD-WAN rule sets the
priority of interfaces in the SD-WAN.
option
-manual
Option
Description
auto
Assign interfaces a priority based on quality.
manual
Assign interfaces a priority manually.
priority
Assign interfaces a priority based on the link-cost-factor quality of the
interface.
sla
Assign interfaces a priority based on selected SLA settings.
name
SD-WAN rule name.
string
Maximum
length: 35
packet-loss-weight
Coefficient of packet-loss in the formula of
custom-profile-1.
integer
Minimum value:
0 Maximum
value:
10000000
0
passive-measurement
Enable/disable passive measurement based
on the service criteria.
option
-disable
Option
Description
enable
Enable passive measurement of user traffic.
disable
Disable passive measurement of user traffic.
priority-members <seq-num>
Member sequence number list.
Member sequence number.
integer
Minimum value:
0 Maximum
value:
4294967295
priority-zone
<name>
Priority zone name list.
Priority zone name.
string
Maximum
length: 79
protocol
Protocol number.
integer
Minimum value:
0 Maximum
value: 255
0
FortiOS 8.0.0 CLI Reference
2085
Fortinet Inc.

<!-- 来源页 2086 -->
Parameter
Description
Type
Size
Default
quality-link
Quality grade.
integer
Minimum value:
0 Maximum
value: 255
0
role
Service role to work with neighbor.
option
-standalone
Option
Description
standalone
Standalone service.
primary
Primary service for primary neighbor.
secondary
Secondary service for secondary neighbor.
shortcut
Enable/disable shortcut for this service.
option
-enable
Option
Description
enable
Enable use of ADVPN shortcut for this service.
disable
Disable use of ADVPN shortcut for this service.
shortcut-priority
High priority of ADVPN shortcut for this
service.
option
-auto
Option
Description
enable
Enable a high priority of ADVPN shortcut for this service.
disable
Disable a high priority of ADVPN shortcut for this service.
auto
Auto enable a high priority of ADVPN shortcut for this service if
ADVPN2.0 enabled.
sla-compare-method
Method to compare SLA value for SLA
mode.
option
-order
Option
Description
order
Compare SLA value based on the order of health-check.
number
Compare SLA value based on the number of satisfied health-check.
Limits health-checks to only configured member interfaces.
sla-stickiness
Enable/disable SLA stickiness (default =
disable).
option
-disable
Option
Description
enable
Traffic remains in the original session path if the path is within the SLA.
disable
Traffic switches to the best path regardless of the SLA.
FortiOS 8.0.0 CLI Reference
2086
Fortinet Inc.

<!-- 来源页 2087 -->
Parameter
Description
Type
Size
Default
src <name>
Source address name.
Address or address group name.
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
src6 <name>
Source address6 name.
Address6 or address6 group name.
string
Maximum
length: 79
standalone-action
Enable/disable service when selected
neighbor role is standalone while service
role is not standalone.
option
-disable
Option
Description
enable
Enable service when selected neighbor role is standalone.
disable
Disable service when selected neighbor role is standalone.
start-port
Start destination port number.
integer
Minimum value:
0 Maximum
value: 65535
1
start-src-port
Start source port number.
integer
Minimum value:
0 Maximum
value: 65535
1
status
Enable/disable SD-WAN service.
option
-enable
Option
Description
enable
Enable SD-WAN service.
disable
Disable SD-WAN service.
tie-break
Method of selecting member if more than
one meets the SLA.
option
-zone
Option
Description
zone
Use the setting that is configured for the members' zone.
cfg-order
Members that meet the SLA are selected in the order they are
configured.
FortiOS 8.0.0 CLI Reference
2087
Fortinet Inc.

<!-- 来源页 2088 -->
Parameter
Description
Type
Size
Default
Option
Description
fib-best-match
Members that meet the SLA are selected that match the longest prefix
in the routing table.
priority
Select the best members that meet the SLA based on link-cost-factor.
input-device
Members that meet the SLA are selected by matching the input
device.
tos
Type of service bit pattern.
user
Not Specified
tos-mask
Type of service evaluated bits.
user
Not Specified
use-shortcut-sla
Enable/disable use of ADVPN shortcut for
quality comparison.
option
-enable
Option
Description
enable
Enable use of ADVPN shortcut for quality comparison.
disable
Disable use of ADVPN shortcut for quality comparison.
users <name>
User name.
User name.
string
Maximum
length: 79
zone-mode
Enable/disable zone mode.
option
-disable
Option
Description
enable
Traffic steered based on zone.
disable
Traffic steered based on member.
* This parameter may not exist in some models.
config sla
Parameter
Description
Type
Size
Default
health-check
SD-WAN health-check.
string
Maximum
length: 35
id
SLA ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
FortiOS 8.0.0 CLI Reference
2088
Fortinet Inc.

---


<!-- 来源页 2092 -->
config system serial-port
Parameter
Description
Type
Size
Default
name
Serial port name.
string
Maximum length:
35
config system session-helper
Configure session helper.
config system session-helper
Description: Configure session helper.
edit <id>
set name [ftp|tftp|...]
set port {integer}
set protocol {integer}
next
end
config system session-helper
Parameter
Description
Type
Size
Default
id
Session helper ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
name
Helper name.
option
-Option
Description
ftp
FTP.
tftp
TFTP.
ras
RAS.
h323
H323.
tns
TNS.
mms
MMS.
sip
SIP.
pptp
PPTP.
FortiOS 8.0.0 CLI Reference
2092
Fortinet Inc.

---


<!-- 来源页 2093 -->
Parameter
Description
Type
Size
Default
Option
Description
rtsp
RTSP.
dns-udp
DNS UDP.
dns-tcp
DNS TCP.
pmap
PMAP.
rsh
RSH.
dcerpc
DCERPC.
mgcp
MGCP.
port
Protocol port.
integer
Minimum value:
1 Maximum
value: 65535
0
protocol
Protocol number.
integer
Minimum value:
0 Maximum
value: 255
0
config system session-ttl
Configure global session TTL timers for this FortiGate.
config system session-ttl
Description: Configure global session TTL timers for this FortiGate.
set default {user}
config port
Description: Session TTL port.
edit <id>
set end-port {integer}
set protocol {integer}
set refresh-direction [both|outgoing|...]
set start-port {integer}
set timeout {user}
next
end
end
config system session-ttl
Parameter
Description
Type
Size
Default
default
Default timeout.
user
Not Specified
FortiOS 8.0.0 CLI Reference
2093
Fortinet Inc.

---


<!-- 来源页 2094 -->
config port
Parameter
Description
Type
Size
Default
end-port
End port number.
integer
Minimum
value: 0
Maximum
value:
65535
0
id
Table entry ID.
integer
Minimum
value: 0
Maximum
value:
65535
0
protocol
Protocol (0 - 255).
integer
Minimum
value: 0
Maximum
value: 255
0
refresh-direction
Configure refresh direction.
option
-both
Option
Description
both
Refresh both directions.
outgoing
Refresh outgoing direction (original).
incoming
Refresh incoming direction (reply).
start-port
Start port number.
integer
Minimum
value: 0
Maximum
value:
65535
0
timeout
Session timeout (TTL).
user
Not
Specified
config system settings
Configure VDOM settings.
config system settings
Description: Configure VDOM settings.
set allow-linkdown-path [enable|disable]
set allow-subnet-overlap [enable|disable]
set asymroute [enable|disable]
set asymroute-icmp [enable|disable]
set asymroute6 [enable|disable]
FortiOS 8.0.0 CLI Reference
2094
Fortinet Inc.

<!-- 来源页 2095 -->
set asymroute6-icmp [enable|disable]
set auxiliary-session [enable|disable]
set bfd [enable|disable]
set bfd-desired-min-tx {integer}
set bfd-detect-mult {integer}
set bfd-dont-enforce-src-port [enable|disable]
set bfd-required-min-rx {integer}
set block-land-attack [disable|enable]
set central-nat [enable|disable]
set comments {var-string}
set default-app-port-as-service [enable|disable]
set default-policy-expiry-days {integer}
set default-voip-alg-mode [proxy-based|kernel-helper-based]
set deny-tcp-with-icmp [enable|disable]
set detect-unknown-esp [enable|disable]
set device {string}
set dhcp-proxy [enable|disable]
set dhcp-proxy-interface {string}
set dhcp-proxy-interface-select-method [auto|sdwan|...]
set dhcp-proxy-vrf-select {integer}
set dhcp-server-ip {user}
set dhcp6-server-ip {user}
set discovered-device-timeout {integer}
set dyn-addr-session-check [enable|disable]
set ecmp-max-paths {integer}
set email-portal-check-dns [disable|enable]
set ext-resource-session-check [enable|disable]
set firewall-session-dirty [check-all|check-new|...]
set fqdn-session-check [enable|disable]
set fw-session-hairpin [enable|disable]
set gateway {ipv4-address}
set gateway6 {ipv6-address}
set gui-advanced-policy [enable|disable]
set gui-advanced-switch-features [enable|disable]
set gui-advanced-wireless-features [enable|disable]
set gui-allow-unnamed-policy [enable|disable]
set gui-antivirus [enable|disable]
set gui-ap-profile [enable|disable]
set gui-application-control [enable|disable]
set gui-casb [enable|disable]
set gui-default-policy-columns <name1>, <name2>, ...
set gui-dhcp-advanced [enable|disable]
set gui-dlp-advanced [enable|disable]
set gui-dlp-profile [enable|disable]
set gui-dns-database [enable|disable]
set gui-dnsfilter [enable|disable]
set gui-dos-policy [enable|disable]
set gui-dynamic-device-os-id [enable|disable]
set gui-dynamic-routing [enable|disable]
set gui-email-collection [enable|disable]
set gui-enforce-change-summary [disable|require|...]
set gui-explicit-proxy [enable|disable]
FortiOS 8.0.0 CLI Reference
2095
Fortinet Inc.

<!-- 来源页 2096 -->
set gui-file-filter [enable|disable]
set gui-fortiap-split-tunneling [enable|disable]
set gui-fortiextender-controller [enable|disable]
set gui-fortitelemetry [enable|disable]
set gui-gtp [enable|disable]
set gui-icap [enable|disable]
set gui-implicit-policy [enable|disable]
set gui-ips [enable|disable]
set gui-load-balance [enable|disable]
set gui-local-in-policy [enable|disable]
set gui-multicast-policy [enable|disable]
set gui-multiple-interface-policy [enable|disable]
set gui-object-colors [enable|disable]
set gui-ot [enable|disable]
set gui-policy-based-ipsec [enable|disable]
set gui-policy-custom-tags [enable|disable]
set gui-policy-disclaimer [enable|disable]
set gui-reverse-connector [enable|disable]
set gui-route-tag-address-creation [enable|disable]
set gui-security-profile-group [enable|disable]
set gui-spamfilter [enable|disable]
set gui-sslvpn [enable|disable]
set gui-sslvpn-personal-bookmarks [enable|disable]
set gui-sslvpn-realms [enable|disable]
set gui-switch-controller [enable|disable]
set gui-threat-weight [enable|disable]
set gui-traffic-shaping [enable|disable]
set gui-videofilter [enable|disable]
set gui-virtual-patch-profile [enable|disable]
set gui-voip-profile [enable|disable]
set gui-vpn [enable|disable]
set gui-waf-profile [enable|disable]
set gui-wan-load-balancing [enable|disable]
set gui-wanopt-cache [enable|disable]
set gui-webfilter [enable|disable]
set gui-webfilter-advanced [enable|disable]
set gui-wireless-controller [enable|disable]
set gui-ztna [enable|disable]
set h323-direct-model [disable|enable]
set http-external-dest [fortiweb|forticache]
set ike-detailed-event-logs [disable|enable]
set ike-dn-format [with-space|no-space]
set ike-extra-ports {integer}
set ike-policy-route [enable|disable]
set ike-port {integer}
set ike-proposal-visibility [recommended|all]
set ike-quick-crash-detect [enable|disable]
set ike-session-resume [enable|disable]
set ike-tcp-port {integer}
set ike-tcp-service [enable|disable]
set ike-tls-service [enable|disable]
set internet-service-app-ctrl-size {integer}
FortiOS 8.0.0 CLI Reference
2096
Fortinet Inc.

<!-- 来源页 2097 -->
set internet-service-database-cache [disable|enable]
set intree-ses-best-route [force|disable]
set ip {ipv4-classnet-host}
set ip6 {ipv6-prefix}
set lan-extension-controller-addr {string}
set lan-extension-controller-port {integer}
set link-down-access [enable|disable]
set lldp-reception [enable|disable|...]
set lldp-transmission [enable|disable|...]
set location-id {ipv4-address}
set mac-ttl {integer}
set manageip {user}
set manageip6 {ipv6-prefix}
set multicast-forward [enable|disable]
set multicast-skip-policy [enable|disable]
set multicast-ttl-notchange [enable|disable]
set nat46-force-ipv4-packet-forwarding [enable|disable]
set nat46-generate-ipv6-fragment-header [enable|disable]
set nat64-force-ipv6-packet-forwarding [enable|disable]
set ngfw-mode [profile-based|policy-based]
set opmode [nat|transparent]
set policy-offload-level [disable|dos-offload]
set prp-trailer-action [enable|disable]
set sccp-port {integer}
set sctp-session-without-init [enable|disable]
set ses-denied-multicast-traffic [enable|disable]
set ses-denied-traffic [enable|disable]
set sip-expectation [enable|disable]
set sip-nat-trace [enable|disable]
set sip-ssl-port {integer}
set sip-tcp-port {integer}
set sip-udp-port {integer}
set snat-hairpin-traffic [enable|disable]
set src-check-reply [enable|disable]
set status [enable|disable]
set strict-src-check [enable|disable]
set tcp-session-without-syn [enable|disable]
set utf8-spam-tagging [enable|disable]
set v4-ecmp-mode [source-ip-based|weight-based|...]
set vdom-type [traffic|lan-extension|...]
set vpn-stats-log {option1}, {option2}, ...
set vpn-stats-period {integer}
set vrf-local-ip-isolation [enable|disable]
set wccp-cache-engine [enable|disable]
end
FortiOS 8.0.0 CLI Reference
2097
Fortinet Inc.

<!-- 来源页 2098 -->
config system settings
Parameter
Description
Type
Size
Default
allow-linkdown-path
Enable/disable link down path.
option
-disable
Option
Description
enable
Allow link down path.
disable
Do not allow link down path.
allow-subnet-overlap
Enable/disable allowing interface
subnets to use overlapping IP
addresses.
option
-disable
Option
Description
enable
Enable overlapping subnets.
disable
Disable overlapping subnets.
asymroute
Enable/disable IPv4 asymmetric
routing.
option
-disable
Option
Description
enable
Enable IPv4 asymmetric routing.
disable
Disable IPv4 asymmetric routing.
asymroute-icmp
Enable/disable ICMP asymmetric
routing.
option
-disable
Option
Description
enable
Enable ICMP asymmetric routing.
disable
Disable ICMP asymmetric routing.
asymroute6
Enable/disable IPv6 asymmetric
routing.
option
-disable
Option
Description
enable
Enable asymmetric IPv6 routing.
disable
Disable asymmetric IPv6 routing.
asymroute6-icmp
Enable/disable ICMPv6 asymmetric
routing.
option
-disable
FortiOS 8.0.0 CLI Reference
2098
Fortinet Inc.

<!-- 来源页 2099 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable asymmetric ICMPv6 routing.
disable
Disable asymmetric ICMPv6 routing.
auxiliary-session
Enable/disable auxiliary session.
option
-disable
Option
Description
enable
Enable auxiliary session for this VDOM.
disable
Disable auxiliary session for this VDOM.
bfd
Enable/disable Bi-directional
Forwarding Detection (BFD) on all
interfaces.
option
-disable
Option
Description
enable
Enable Bi-directional Forwarding Detection (BFD) on all interfaces.
disable
Disable Bi-directional Forwarding Detection (BFD) on all interfaces.
bfd-desired-min-tx
BFD desired minimal transmit interval (1
- 100000 ms, default = 250).
integer
Minimum value:
1 Maximum
value: 100000
250
bfd-detect-mult
BFD detection multiplier (1 - 50, default
= 3).
integer
Minimum value:
1 Maximum
value: 50
3
bfd-dont-enforce-src-port
Enable to not enforce verifying the
source port of BFD Packets.
option
-disable
Option
Description
enable
Enable verifying the source port of BFD Packets.
disable
Disable verifying the source port of BFD Packets.
bfd-required-min-rx
BFD required minimal receive interval
(1 - 100000 ms, default = 250).
integer
Minimum value:
1 Maximum
value: 100000
250
block-land-attack
Enable/disable blocking of land
attacks.
option
-disable
FortiOS 8.0.0 CLI Reference
2099
Fortinet Inc.

<!-- 来源页 2100 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Do not block land attack.
enable
Block land attack.
central-nat
Enable/disable central NAT.
option
-disable
Option
Description
enable
Enable central NAT.
disable
Disable central NAT.
comments
VDOM comments.
var-string
Maximum
length: 255
default-app-port-as-service
Enable/disable policy service
enforcement based on application
default ports.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
default-policy-expiry-days
Default policy expiry in days (0 - 365
days, default = 30).
integer
Minimum value:
0 Maximum
value: 365
30
default-voip-alg-mode
Configure how the FortiGate handles
VoIP traffic when a policy that accepts
the traffic doesn't include a VoIP
profile.
option
-proxy-based
Option
Description
proxy-based
Use a default proxy-based VoIP ALG.
kernel-helper-based
Use the SIP session helper.
deny-tcp-with-icmp
Enable/disable denying TCP by
sending an ICMP communication
prohibited packet.
option
-disable
Option
Description
enable
Deny TCP with ICMP.
disable
Disable denying TCP with ICMP.
FortiOS 8.0.0 CLI Reference
2100
Fortinet Inc.

<!-- 来源页 2101 -->
Parameter
Description
Type
Size
Default
detect-unknown-esp
Enable/disable detection of unknown
ESP packets (default = enable).
option
-enable
Option
Description
enable
Enable detection of unknown ESP packets and drop the ESP packet if
it's unknown.
disable
Disable detection of unknown ESP packets.
device
Interface to use for management
access for NAT mode.
string
Maximum
length: 35
dhcp-proxy
Enable/disable the DHCP Proxy.
option
-disable
Option
Description
enable
Enable the DHCP proxy.
disable
Disable the DHCP proxy.
dhcp-proxy-interface
Specify outgoing interface to reach
server.
string
Maximum
length: 15
dhcp-proxy-interface-select-method
Specify how to select outgoing
interface to reach server.
option
-auto
Option
Description
auto
Set outgoing interface automatically.
sdwan
Set outgoing interface by SD-WAN or policy routing rules.
specify
Set outgoing interface manually.
dhcp-proxy-vrf-select
VRF ID used for connection to server.
integer
Minimum value:
0 Maximum
value: 511
0
dhcp-server-ip
DHCP Server IPv4 address.
user
Not Specified
dhcp6-server-ip
DHCPv6 server IPv6 address.
user
Not Specified
discovered-device-timeout
Timeout for discovered devices (1 -365 days, default = 28).
integer
Minimum value:
1 Maximum
value: 365
28
dyn-addr-session-check
Enable/disable dirty session check
caused by dynamic address updates.
option
-disable
FortiOS 8.0.0 CLI Reference
2101
Fortinet Inc.

<!-- 来源页 2102 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable dirty session check caused by dynamic address updates.
disable
Disable dirty session check caused by dynamic address updates.
ecmp-max-paths
Maximum number of Equal Cost Multi-Path (ECMP) next-hops. Set to 1 to
disable ECMP routing (1 - 255, default
= 255).
integer
Minimum value:
1 Maximum
value: 255
255
email-portal-check-dns
Enable/disable using DNS to validate
email addresses collected by a captive
portal.
option
-enable
Option
Description
disable
Disable email address checking with DNS.
enable
Enable email address checking with DNS.
ext-resource-session-check
Enable/disable dirty session check
caused by external resource updates.
option
-disable
Option
Description
enable
Enable dirty session check caused by external resource updates.
disable
Disable dirty session check caused by external resource updates.
firewall-session-dirty
Select how to manage sessions
affected by firewall policy
configuration changes.
option
-check-all
Option
Description
check-all
All sessions affected by a firewall policy change are flushed from the
session table. When new packets are received they are re-evaluated
by stateful inspection and re-added to the session table.
check-new
Established sessions for changed firewall policies continue without
being affected by the policy configuration change. New sessions are
evaluated according to the new firewall policy configuration.
check-policy-option
Sessions are managed individually depending on the firewall policy.
Some sessions may restart. Some may continue.
fqdn-session-check
Enable/disable dirty session check
caused by FQDN updates.
option
-disable
FortiOS 8.0.0 CLI Reference
2102
Fortinet Inc.

<!-- 来源页 2103 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable dirty session check caused by FQDN updates.
disable
Disable dirty session check caused by FQDN updates.
fw-session-hairpin
Enable/disable checking for a matching
policy each time hairpin traffic goes
through the FortiGate.
option
-disable
Option
Description
enable
Perform a policy check every time.
disable
Perform a policy check only the first time the session is received.
gateway
Transparent mode IPv4 default
gateway IP address.
ipv4-address
Not Specified
0.0.0.0
gateway6
Transparent mode IPv6 default
gateway IP address.
ipv6-address
Not Specified
::
gui-advanced-policy
Enable/disable advanced policy
configuration on the GUI.
option
-disable
Option
Description
enable
Enable advanced policy configuration on the GUI.
disable
Disable advanced policy configuration on the GUI.
gui-advanced-switch-features
*
Enable/disable advanced switching
features on the GUI.
option
-disable
Option
Description
enable
Enable advanced switching features on the GUI.
disable
Disable advanced switching features on the GUI.
gui-advanced-wireless-features
Enable/disable advanced wireless
features in GUI.
option
-disable
Option
Description
enable
Enable advanced wireless features in GUI.
disable
Disable advanced wireless features in GUI.
gui-allow-unnamed-policy
Enable/disable the requirement for
policy naming on the GUI.
option
-disable
FortiOS 8.0.0 CLI Reference
2103
Fortinet Inc.

<!-- 来源页 2104 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable the requirement for policy naming on the GUI.
disable
Disable the requirement for policy naming on the GUI.
gui-antivirus
Enable/disable AntiVirus on the GUI.
option
-enable
Option
Description
enable
Enable AntiVirus on the GUI.
disable
Disable AntiVirus on the GUI.
gui-ap-profile
Enable/disable FortiAP profiles on the
GUI.
option
-enable
Option
Description
enable
Enable FortiAP profiles on the GUI.
disable
Disable FortiAP profiles on the GUI.
gui-application-control
Enable/disable application control on
the GUI.
option
-enable
Option
Description
enable
Enable application control on the GUI.
disable
Disable application control on the GUI.
gui-casb
Enable/disable Inline-CASB on the GUI.
option
-disable
Option
Description
enable
Enable Inline-CASB on the GUI.
disable
Disable Inline-CASB on the GUI.
gui-default-policy-columns
<name>
Default columns to display for policy
lists on GUI.
Select column name.
string
Maximum
length: 79
gui-dhcp-advanced
Enable/disable advanced DHCP
options on the GUI.
option
-enable
Option
Description
enable
Enable advanced DHCP options on the GUI.
disable
Disable advanced DHCP options on the GUI.
FortiOS 8.0.0 CLI Reference
2104
Fortinet Inc.

<!-- 来源页 2105 -->
Parameter
Description
Type
Size
Default
gui-dlp-advanced
Enable/disable Show advanced DLP
expressions on the GUI.
option
-disable
Option
Description
enable
Enable Show advanced DLP expressions on the GUI.
disable
Disable Show advanced DLP expressions on the GUI.
gui-dlp-profile
Enable/disable Data Loss Prevention
on the GUI.
option
-disable
Option
Description
enable
Enable Data Loss Prevention on the GUI.
disable
Disable Data Loss Prevention on the GUI.
gui-dns-database
Enable/disable DNS database settings
on the GUI.
option
-disable
Option
Description
enable
Enable DNS database settings on the GUI.
disable
Disable DNS database settings on the GUI.
gui-dnsfilter
Enable/disable DNS Filtering on the
GUI.
option
-enable
Option
Description
enable
Enable DNS Filtering on the GUI.
disable
Disable DNS Filtering on the GUI.
gui-dos-policy
Enable/disable DoS policies on the GUI.
option
-enable **
Option
Description
enable
Enable DoS policies on the GUI.
disable
Disable DoS policies on the GUI.
gui-dynamic-device-os-id
Enable/disable Create dynamic
addresses to manage known devices.
option
-disable
Option
Description
enable
Enable Create dynamic addresses to manage known devices.
disable
Disable Create dynamic addresses to manage known devices.
FortiOS 8.0.0 CLI Reference
2105
Fortinet Inc.

<!-- 来源页 2106 -->
Parameter
Description
Type
Size
Default
gui-dynamic-routing
Enable/disable dynamic routing on the
GUI.
option
-enable **
Option
Description
enable
Enable dynamic routing on the GUI.
disable
Disable dynamic routing on the GUI.
gui-email-collection
Enable/disable email collection on the
GUI.
option
-disable
Option
Description
enable
Enable email collection on the GUI.
disable
Disable email collection on the GUI.
gui-enforce-change-summary
Enforce change summaries for select
tables in the GUI.
option
-require
Option
Description
disable
No change summary requirement.
require
Change summary required.
optional
Change summary optional.
gui-explicit-proxy
Enable/disable the explicit proxy on the
GUI.
option
-disable
Option
Description
enable
Enable the explicit proxy on the GUI.
disable
Disable the explicit proxy on the GUI.
gui-file-filter
Enable/disable File-filter on the GUI.
option
-enable **
Option
Description
enable
Enable File-filter on the GUI.
disable
Disable File-filter on the GUI.
gui-fortiap-split-tunneling
Enable/disable FortiAP split tunneling
on the GUI.
option
-disable
FortiOS 8.0.0 CLI Reference
2106
Fortinet Inc.

<!-- 来源页 2107 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable FortiAP split tunneling on the GUI.
disable
Disable FortiAP split tunneling on the GUI.
gui-fortiextender-controller
Enable/disable FortiExtender on the
GUI.
option
-disable **
Option
Description
enable
Enable FortiExtender on the GUI.
disable
Disable FortiExtender on the GUI.
gui-fortitelemetry *
Enable/disable FortiTelemetry on the
GUI.
option
-disable
Option
Description
enable
Enable FortiTelemetry on the GUI.
disable
Disable FortiTelemetry on the GUI.
gui-gtp *
Enable/disable Manage general radio
packet service (GPRS) protocols on the
GUI.
option
-enable
Option
Description
enable
Enable Manage general radio packet service (GPRS) protocols on the
GUI.
disable
Disable Manage general radio packet service (GPRS) protocols on the
GUI.
gui-icap
Enable/disable ICAP on the GUI.
option
-disable
Option
Description
enable
Enable ICAP on the GUI.
disable
Disable ICAP on the GUI.
gui-implicit-policy
Enable/disable implicit firewall policies
on the GUI.
option
-enable
Option
Description
enable
Enable implicit firewall policies on the GUI.
disable
Disable implicit firewall policies on the GUI.
FortiOS 8.0.0 CLI Reference
2107
Fortinet Inc.

<!-- 来源页 2108 -->
Parameter
Description
Type
Size
Default
gui-ips
Enable/disable IPS on the GUI.
option
-enable **
Option
Description
enable
Enable IPS on the GUI.
disable
Disable IPS on the GUI.
gui-load-balance
Enable/disable server load balancing
on the GUI.
option
-disable
Option
Description
enable
Enable server load balancing on the GUI.
disable
Disable server load balancing on the GUI.
gui-local-in-policy
Enable/disable Local-In policies on the
GUI.
option
-disable
Option
Description
enable
Enable Local-In policies on the GUI.
disable
Disable Local-In policies on the GUI.
gui-multicast-policy
Enable/disable multicast firewall
policies on the GUI.
option
-disable
Option
Description
enable
Enable multicast firewall policies on the GUI.
disable
Disable multicast firewall policies on the GUI.
gui-multiple-interface-policy
Enable/disable adding multiple
interfaces to a policy on the GUI.
option
-disable
Option
Description
enable
Enable adding multiple interfaces to a policy on the GUI.
disable
Disable adding multiple interfaces to a policy on the GUI.
gui-object-colors
Enable/disable object colors on the
GUI.
option
-enable
Option
Description
enable
Enable object colors on the GUI.
disable
Disable object colors on the GUI.
FortiOS 8.0.0 CLI Reference
2108
Fortinet Inc.

<!-- 来源页 2109 -->
Parameter
Description
Type
Size
Default
gui-ot
Enable/disable Operational technology
features on the GUI.
option
-disable
Option
Description
enable
Enable Operational technology features on the GUI.
disable
Disable Operational technology features on the GUI.
gui-policy-based-ipsec
Enable/disable policy-based IPsec VPN
on the GUI.
option
-disable
Option
Description
enable
Enable policy-based IPsec VPN on the GUI.
disable
Disable policy-based IPsec VPN on the GUI.
gui-policy-custom-tags *
Enable/disable Allow configuring
custom tags for polices on the GUI.
option
-disable
Option
Description
enable
Enable Allow configuring custom tags for polices on the GUI.
disable
Disable Allow configuring custom tags for polices on the GUI.
gui-policy-disclaimer
Enable/disable policy disclaimer on the
GUI.
option
-disable
Option
Description
enable
Enable policy disclaimer on the GUI.
disable
Disable policy disclaimer on the GUI.
gui-reverse-connector *
Enable/disable Enable ZTNA Reverse
Proxy Connector on the GUI.
option
-disable
Option
Description
enable
Enable Enable ZTNA Reverse Proxy Connector on the GUI.
disable
Disable Enable ZTNA Reverse Proxy Connector on the GUI.
gui-route-tag-address-creation
Enable/disable route-tag addresses on
the GUI.
option
-disable
Option
Description
enable
Enable route-tag addresses on the GUI.
FortiOS 8.0.0 CLI Reference
2109
Fortinet Inc.

<!-- 来源页 2110 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable route-tag addresses on the GUI.
gui-security-profile-group
Enable/disable Security Profile Groups
on the GUI.
option
-disable
Option
Description
enable
Enable Security Profile Groups on the GUI.
disable
Disable Security Profile Groups on the GUI.
gui-spamfilter
Enable/disable Antispam on the GUI.
option
-disable
Option
Description
enable
Enable Antispam on the GUI.
disable
Disable Antispam on the GUI.
gui-sslvpn *
Enable/disable SSL-VPN settings
pages on the GUI.
option
-disable
Option
Description
enable
Enable SSL-VPN settings pages on the GUI.
disable
Disable SSL-VPN settings pages on the GUI.
gui-sslvpn-personal-bookmarks *
Enable/disable SSL-VPN personal
bookmark management on the GUI.
option
-disable
Option
Description
enable
Enable SSL-VPN personal bookmark management on the GUI.
disable
Disable SSL-VPN personal bookmark management on the GUI.
gui-sslvpn-realms *
Enable/disable SSL-VPN realms on the
GUI.
option
-disable
Option
Description
enable
Enable SSL-VPN realms on the GUI.
disable
Disable SSL-VPN realms on the GUI.
gui-switch-controller
Enable/disable the switch controller on
the GUI.
option
-enable
FortiOS 8.0.0 CLI Reference
2110
Fortinet Inc.

<!-- 来源页 2111 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable the switch controller on the GUI.
disable
Disable the switch controller on the GUI.
gui-threat-weight
Enable/disable threat weight on the
GUI.
option
-enable
Option
Description
enable
Enable threat weight on the GUI.
disable
Disable threat weight on the GUI.
gui-traffic-shaping
Enable/disable traffic shaping on the
GUI.
option
-enable
Option
Description
enable
Enable traffic shaping on the GUI.
disable
Disable traffic shaping on the GUI.
gui-videofilter
Enable/disable Video filtering on the
GUI.
option
-enable **
Option
Description
enable
Enable Video filtering on the GUI.
disable
Disable Video filtering on the GUI.
gui-virtual-patch-profile
Enable/disable Virtual Patching on the
GUI.
option
-disable
Option
Description
enable
Enable Virtual Patching on the GUI.
disable
Disable Virtual Patching on the GUI.
gui-voip-profile
Enable/disable VoIP profiles on the
GUI.
option
-disable
Option
Description
enable
Enable VoIP profiles on the GUI.
disable
Disable VoIP profiles on the GUI.
gui-vpn
Enable/disable IPsec VPN settings
pages on the GUI.
option
-enable
FortiOS 8.0.0 CLI Reference
2111
Fortinet Inc.

<!-- 来源页 2112 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable IPsec VPN settings pages on the GUI.
disable
Disable IPsec VPN settings pages on the GUI.
gui-waf-profile
Enable/disable Web Application
Firewall on the GUI.
option
-disable
Option
Description
enable
Enable Web Application Firewall on the GUI.
disable
Disable Web Application Firewall on the GUI.
gui-wan-load-balancing
Enable/disable SD-WAN on the GUI.
option
-enable
Option
Description
enable
Enable SD-WAN on the GUI.
disable
Disable SD-WAN on the GUI.
gui-wanopt-cache *
Enable/disable WAN Optimization and
Web Caching on the GUI.
option
-disable
Option
Description
enable
Enable WAN Optimization and Web Caching on the GUI.
disable
Disable WAN Optimization and Web Caching on the GUI.
gui-webfilter
Enable/disable Web filtering on the
GUI.
option
-enable
Option
Description
enable
Enable Web filtering on the GUI.
disable
Disable Web filtering on the GUI.
gui-webfilter-advanced
Enable/disable advanced web filtering
on the GUI.
option
-disable
Option
Description
enable
Enable advanced web filtering on the GUI.
disable
Disable advanced web filtering on the GUI.
gui-wireless-controller
Enable/disable the wireless controller
on the GUI.
option
-enable
FortiOS 8.0.0 CLI Reference
2112
Fortinet Inc.

<!-- 来源页 2113 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable the wireless controller on the GUI.
disable
Disable the wireless controller on the GUI.
gui-ztna
Enable/disable Zero Trust Network
Access features on the GUI.
option
-enable **
Option
Description
enable
Enable Zero Trust Network Access features on the GUI.
disable
Disable Zero Trust Network Access features on the GUI.
h323-direct-model
Enable/disable H323 direct model.
option
-disable
Option
Description
disable
Disable H323 direct model.
enable
Enable H323 direct model.
http-external-dest
Offload HTTP traffic to FortiWeb or
FortiCache.
option
-fortiweb
Option
Description
fortiweb
Offload HTTP traffic to FortiWeb for Web Application Firewall
inspection.
forticache
Offload HTTP traffic to FortiCache for external web caching and WAN
optimization.
ike-detailed-event-logs
Enable/disable detail log for IKE events.
option
-disable
Option
Description
disable
Generate brief log for IKE events.
enable
Generate detail log for IKE events.
ike-dn-format
Configure IKE ASN.1 Distinguished
Name format conventions.
option
-with-space
Option
Description
with-space
Format IKE ASN.1 Distinguished Names with spaces between attribute
names and values.
FortiOS 8.0.0 CLI Reference
2113
Fortinet Inc.

<!-- 来源页 2114 -->
Parameter
Description
Type
Size
Default
Option
Description
no-space
Format IKE ASN.1 Distinguished Names without spaces between
attribute names and values.
ike-extra-ports
*
Extra UDP ports for the IKE daemon to
listen on other than 500 and 4500
(maximum 3).
integer
Minimum value:
1024 Maximum
value: 65535
ike-policy-route
Enable/disable IKE Policy Based
Routing (PBR).
option
-disable
Option
Description
enable
Enable IKE Policy Based Routing (PBR).
disable
Disable IKE Policy Based Routing (PBR).
ike-port
UDP port for IKE/IPsec traffic (default
500).
integer
Minimum value:
1024 Maximum
value: 65535
500
ike-proposal-visibility *
Enable/disable display only
recommended proposals in IPsec
tunnel configuration.
option
-recommended
Option
Description
recommended
Display only recommended proposals in IPsec tunnel configuration.
all
Display all supported proposals in IPsec tunnel configuration.
ike-quick-crash-detect
Enable/disable IKE quick crash
detection (RFC 6290).
option
-disable
Option
Description
enable
Enable IKE quick crash detection (RFC 6290).
disable
Disable IKE quick crash detection (RFC 6290).
ike-session-resume
Enable/disable IKEv2 session
resumption (RFC 5723).
option
-disable
Option
Description
enable
Enable IKEv2 session resumption (RFC 5723).
disable
Disable IKEv2 session resumption (RFC 5723).
FortiOS 8.0.0 CLI Reference
2114
Fortinet Inc.

<!-- 来源页 2115 -->
Parameter
Description
Type
Size
Default
ike-tcp-port
TCP port for IKE/IPsec traffic (default
443).
integer
Minimum value:
1 Maximum
value: 65535
443
ike-tcp-service
*
Enable/disable IKE TCP service.
option
-disable
Option
Description
enable
Enable IKE over TCP service.
disable
Disable IKE over TCP service.
ike-tls-service *
Enable/disable IKE TLS service.
option
-disable
Option
Description
enable
Enable IKE TLS service.
disable
Disable IKE TLS service.
internet-service-app-ctrl-size
Maximum number of tuple entries
(protocol, port, IP address, application
ID) stored by the FortiGate unit (0 -4294967295, default = 32768). A
smaller value limits the FortiGate unit
from learning about internet
applications.
integer
Minimum value:
0 Maximum
value:
4294967295
32768
internet-service-database-cache
Enable/disable Internet Service
database caching.
option
-disable
Option
Description
disable
Disable Internet Service database caching.
enable
Enable Internet Service database caching.
intree-ses-best-route
Force the intree session to always use
the best route.
option
-disable
Option
Description
force
Force the intree session to always use the best route.
disable
Don't force the intree session to always use the best route.
ip
IP address and netmask.
ipv4-classnet-host
Not Specified
0.0.0.0 0.0.0.0
FortiOS 8.0.0 CLI Reference
2115
Fortinet Inc.

<!-- 来源页 2116 -->
Parameter
Description
Type
Size
Default
ip6
IPv6 address prefix for NAT mode.
ipv6-prefix
Not Specified
::/0
lan-extension-controller-addr
Controller IP address or FQDN to
connect.
string
Maximum
length: 255
lan-extension-controller-port
Controller port to connect.
integer
Minimum value:
1024 Maximum
value: 65535
5246
link-down-access
Enable/disable link down access
traffic.
option
-enable
Option
Description
enable
Allow link down access traffic.
disable
Block link down access traffic.
lldp-reception
Enable/disable Link Layer Discovery
Protocol (LLDP) reception for this
VDOM or apply global settings to this
VDOM.
option
-global
Option
Description
enable
Enable LLDP reception for this VDOM.
disable
Disable LLDP reception for this VDOM.
global
Use the global LLDP reception configuration for this VDOM.
lldp-transmission
Enable/disable Link Layer Discovery
Protocol (LLDP) transmission for this
VDOM or apply global settings to this
VDOM.
option
-global
Option
Description
enable
Enable LLDP transmission for this VDOM.
disable
Disable LLDP transmission for this VDOM.
global
Use the global LLDP transmission configuration for this VDOM.
location-id
Local location ID in the form of an IPv4
address.
ipv4-address
Not Specified
0.0.0.0
mac-ttl
Duration of MAC addresses in
Transparent mode (300 - 8640000
sec, default = 300).
integer
Minimum value:
300 Maximum
value:
8640000
300
FortiOS 8.0.0 CLI Reference
2116
Fortinet Inc.

<!-- 来源页 2117 -->
Parameter
Description
Type
Size
Default
manageip
Transparent mode IPv4 management
IP address and netmask.
user
Not Specified
manageip6
Transparent mode IPv6 management
IP address and netmask.
ipv6-prefix
Not Specified
::/0
multicast-forward
Enable/disable multicast forwarding.
option
-enable
Option
Description
enable
Enable multicast forwarding.
disable
Disable multicast forwarding.
multicast-skip-policy
Enable/disable allowing multicast
traffic through the FortiGate without a
policy check.
option
-disable
Option
Description
enable
Allowing multicast traffic through the FortiGate without creating a
multicast firewall policy.
disable
Require a multicast policy to allow multicast traffic to pass through the
FortiGate.
multicast-ttl-notchange
Enable/disable preventing the
FortiGate from changing the TTL for
forwarded multicast packets.
option
-disable
Option
Description
enable
The multicast TTL is not changed.
disable
The multicast TTL may be changed.
nat46-force-ipv4-packet-forwarding
Enable/disable mandatory IPv4 packet
forwarding in NAT46.
option
-disable
Option
Description
enable
Enable mandatory IPv4 packet forwarding when IPv4 DF is set to 1.
disable
Disable mandatory IPv4 packet forwarding when IPv4 DF is set to 1.
nat46-generate-ipv6-fragment-header
Enable/disable NAT46 IPv6 fragment
header generation.
option
-disable
FortiOS 8.0.0 CLI Reference
2117
Fortinet Inc.

<!-- 来源页 2118 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable NAT46 IPv6 fragment header generation.
disable
Disable NAT46 IPv6 fragment header generation.
nat64-force-ipv6-packet-forwarding
Enable/disable mandatory IPv6 packet
forwarding in NAT64.
option
-enable
Option
Description
enable
Enable mandatory IPv6 packet forwarding
disable
Disable mandatory IPv6 packet forwarding
ngfw-mode
Next Generation Firewall (NGFW)
mode.
option
-profile-based
Option
Description
profile-based
Application and web-filtering are configured using profiles applied to
policy entries.
policy-based
Application and web-filtering are configured as policy match
conditions.
opmode
Firewall operation mode (NAT or
Transparent).
option
-nat
Option
Description
nat
Change to NAT mode.
transparent
Change to transparent mode.
policy-offload-level *
Configure firewall policy offload level.
option
-disable
Option
Description
disable
Disable policy offloading.
dos-offload
Only enable DoS policy offloading.
prp-trailer-action
Enable/disable action to take on PRP
trailer.
option
-disable
Option
Description
enable
Try to keep PRP trailer.
disable
Trim PRP trailer.
FortiOS 8.0.0 CLI Reference
2118
Fortinet Inc.

<!-- 来源页 2119 -->
Parameter
Description
Type
Size
Default
sccp-port
TCP port the SCCP proxy monitors for
SCCP traffic (0 - 65535, default =
2000).
integer
Minimum value:
0 Maximum
value: 65535
2000
sctp-session-without-init
Enable/disable SCTP session creation
without SCTP INIT.
option
-disable
Option
Description
enable
Enable SCTP session creation without SCTP INIT.
disable
Disable SCTP session creation without SCTP INIT.
ses-denied-multicast-traffic
Enable/disable including denied
multicast session in the session table.
option
-disable
Option
Description
enable
Include denied multicast sessions in the session table.
disable
Do not add denied multicast sessions to the session table.
ses-denied-traffic
Enable/disable including denied
session in the session table.
option
-disable
Option
Description
enable
Include denied sessions in the session table.
disable
Do not add denied sessions to the session table.
sip-expectation
Enable/disable the SIP kernel session
helper to create an expectation for port
5060.
option
-disable
Option
Description
enable
Allow SIP session helper to create an expectation for port 5060.
disable
Prevent SIP session helper from creating an expectation for port
5060.
sip-nat-trace
Enable/disable recording the original
SIP source IP address when NAT is
used.
option
-enable
Option
Description
enable
Record the original SIP source IP address when NAT is used.
disable
Do not record the original SIP source IP address when NAT is used.
FortiOS 8.0.0 CLI Reference
2119
Fortinet Inc.

<!-- 来源页 2120 -->
Parameter
Description
Type
Size
Default
sip-ssl-port
TCP port the SIP proxy monitors for SIP
SSL/TLS traffic (0 - 65535, default =
5061).
integer
Minimum value:
0 Maximum
value: 65535
5061
sip-tcp-port
TCP port the SIP proxy monitors for SIP
traffic (0 - 65535, default = 5060).
integer
Minimum value:
1 Maximum
value: 65535
5060
sip-udp-port
UDP port the SIP proxy monitors for SIP
traffic (0 - 65535, default = 5060).
integer
Minimum value:
1 Maximum
value: 65535
5060
snat-hairpin-traffic
Enable/disable source NAT (SNAT) for
VIP hairpin traffic.
option
-enable
Option
Description
enable
Enable SNAT for VIP hairpin traffic.
disable
Disable SNAT for VIP hairpin traffic.
src-check-reply
*
Enable/disable source verification for
reply packets.
option
-disable
Option
Description
enable
Enable source verification for reply packets.
disable
Disable source verification for reply packets.
status
Enable/disable this VDOM.
option
-enable
Option
Description
enable
Enable this VDOM.
disable
Disable this VDOM.
strict-src-check
Enable/disable strict source
verification.
option
-disable
Option
Description
enable
Enable strict source verification.
disable
Disable strict source verification.
tcp-session-without-syn
Enable/disable allowing TCP session
without SYN flags.
option
-disable
FortiOS 8.0.0 CLI Reference
2120
Fortinet Inc.

<!-- 来源页 2121 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Allow TCP session without SYN flags.
disable
Do not allow TCP session without SYN flags.
utf8-spam-tagging
Enable/disable converting antispam
tags to UTF-8 for better non-ASCII
character support.
option
-enable
Option
Description
enable
Convert antispam tags to UTF-8.
disable
Do not convert antispam tags.
v4-ecmp-mode
IPv4 Equal-cost multi-path (ECMP)
routing and load balancing mode.
option
-source-ip-based
Option
Description
source-ip-based
Select next hop based on source IP.
weight-based
Select next hop based on weight.
usage-based
Select next hop based on usage.
source-dest-ip-based
Select next hop based on both source and destination IPs.
vdom-type
Vdom type (traffic, lan-extension or
admin).
option
-traffic
Option
Description
traffic
Change to traffic VDOM
lan-extension
Change to lan-extension VDOM
admin
Change to admin VDOM
vpn-stats-log
Enable/disable periodic VPN log
statistics for one or more types of VPN.
Separate names with a space.
option
-ipsec pptp l2tp
ssl **
Option
Description
ipsec
IPsec.
pptp
PPTP.
FortiOS 8.0.0 CLI Reference
2121
Fortinet Inc.

---


<!-- 来源页 2122 -->
Parameter
Description
Type
Size
Default
Option
Description
l2tp
L2TP.
ssl
SSL.
vpn-stats-period
Period to send VPN log statistics (0 or
60 - 86400 sec).
integer
Minimum value:
0 Maximum
value:
4294967295
600
vrf-local-ip-isolation *
Enable/disable VRF local IP address
isolation.
option
-disable
Option
Description
enable
Enable VRF local IP address isolation.
disable
Disable VRF local IP address isolation.
wccp-cache-engine
Enable/disable WCCP cache engine.
option
-disable
Option
Description
enable
Enable WCCP cache engine.
disable
Disable WCCP cache engine.
* This parameter may not exist in some models.
** Values may differ between models.
config system sflow
Configure sFlow.
config system sflow
Description: Configure sFlow.
config collectors
Description: sFlow collectors.
edit <id>
set collector-ip {ipv4-address}
set collector-port {integer}
set interface {string}
set interface-select-method [auto|sdwan|...]
set source-ip {ipv4-address}
next
end
end
FortiOS 8.0.0 CLI Reference
2122
Fortinet Inc.

---


<!-- 来源页 2127 -->
config system sms-server
Parameter
Description
Type
Size
Default
mail-server
Email-to-SMS server domain name.
string
Maximum
length: 63
name
Name of SMS server.
string
Maximum
length: 35
config system snmp community
SNMP community configuration.
config system snmp community
Description: SNMP community configuration.
edit <id>
set events {option1}, {option2}, ...
config hosts
Description: Configure IPv4 SNMP managers (hosts).
edit <id>
set ha-direct [enable|disable]
set host-type [any|query|...]
set interface {string}
set interface-select-method [auto|sdwan|...]
set ip {user}
set source-ip {ipv4-address}
set vrf-select {integer}
next
end
config hosts6
Description: Configure IPv6 SNMP managers.
edit <id>
set ha-direct [enable|disable]
set host-type [any|query|...]
set interface {string}
set interface-select-method [auto|sdwan|...]
set ipv6 {ipv6-prefix}
set source-ipv6 {ipv6-address}
set vrf-select {integer}
next
end
set mib-view {string}
set name {string}
set query-v1-port {integer}
set query-v1-status [enable|disable]
set query-v2c-port {integer}
set query-v2c-status [enable|disable]
set status [enable|disable]
set trap-v1-lport {integer}
FortiOS 8.0.0 CLI Reference
2127
Fortinet Inc.

<!-- 来源页 2128 -->
set trap-v1-rport {integer}
set trap-v1-status [enable|disable]
set trap-v2c-lport {integer}
set trap-v2c-rport {integer}
set trap-v2c-status [enable|disable]
set vdoms <name1>, <name2>, ...
next
end
FortiOS 8.0.0 CLI Reference
2128
Fortinet Inc.

<!-- 来源页 2129 -->
config system snmp community
FortiOS 8.0.0 CLI Reference
2129
Fortinet Inc.

<!-- 来源页 2130 -->
Parameter
Description
Type
Size
Default
events
SNMP trap events.
option
-cpu-high mem-low log-full
intf-ip vpn-tun-up vpn-tun-down ha-switch ha-hb-failure ips-signature ips-anomaly av-virus av-oversize av-pattern av-fragmented fm-if-change bgp-established
bgp-backward-transition ha-member-up ha-member-down
ent-conf-change av-conserve av-bypass av-oversize-passed av-oversize-blocked ips-pkg-update
ips-fail-open
temperature-high voltage-alert power-supply faz-disconnect faz
fan-failure wc-ap-up wc-ap-down fswctl-session-up
fswctl-session-down load-balance-real-server-down
per-cpu-high
dhcp pool-usage ippool
interface ospf-nbr-state-change ospf-virtnbr-state-change fsso
bfd **
FortiOS 8.0.0 CLI Reference
2130
Fortinet Inc.

<!-- 来源页 2131 -->
Parameter
Description
Type
Size
Default
Option
Description
cpu-high
Send a trap when CPU usage is high.
mem-low
Send a trap when used memory is high, free memory is low, or freeable
memory is high.
log-full
Send a trap when log disk space becomes low.
intf-ip
Send a trap when an interface IP address is changed.
vpn-tun-up
Send a trap when a VPN tunnel comes up.
vpn-tun-down
Send a trap when a VPN tunnel goes down.
ha-switch
Send a trap after an HA failover when the backup unit has taken over.
ha-hb-failure
Send a trap when HA heartbeats are not received.
ips-signature
Send a trap when IPS detects an attack.
ips-anomaly
Send a trap when IPS finds an anomaly.
av-virus
Send a trap when AntiVirus finds a virus.
av-oversize
Send a trap when AntiVirus finds an oversized file.
av-pattern
Send a trap when AntiVirus finds file matching pattern.
av-fragmented
Send a trap when AntiVirus finds a fragmented file.
fm-if-change
Send a trap when FortiManager interface changes. Send a FortiManager
trap.
fm-conf-change
Send a trap when a configuration change is made by a FortiGate
administrator and the FortiGate is managed by FortiManager.
bgp-established
Send a trap when a BGP FSM transitions to the established state.
bgp-backward-transition
Send a trap when a BGP FSM goes from a high numbered state to a
lower numbered state.
ha-member-up
Send a trap when an HA cluster member goes up.
ha-member-down
Send a trap when an HA cluster member goes down.
ent-conf-change
Send a trap when an entity MIB change occurs (RFC4133).
av-conserve
Send a trap when the FortiGate enters conserve mode.
av-bypass
Send a trap when the FortiGate enters bypass mode.
FortiOS 8.0.0 CLI Reference
2131
Fortinet Inc.

<!-- 来源页 2132 -->
Parameter
Description
Type
Size
Default
Option
Description
av-oversize-passed
Send a trap when AntiVirus passes an oversized file.
av-oversize-blocked
Send a trap when AntiVirus blocks an oversized file.
ips-pkg-update
Send a trap when the IPS signature database or engine is updated.
ips-fail-open
Send a trap when the IPS network buffer is full.
temperature-high
Send a trap when a temperature sensor registers a temperature that is
too high.
voltage-alert
Send a trap when a voltage sensor registers a voltage that is outside of
the normal range.
power-supply
Send a trap when a power supply fails or restores.
faz-disconnect
Send a trap when a FortiAnalyzer disconnects from the FortiGate.
faz
Send a trap when Fortianalyzer main server failover and alternate server
take over, or alternate server failover and main server take over.
fan-failure
Send a trap when a fan fails.
wc-ap-up
Send a trap when a managed FortiAP comes up.
wc-ap-down
Send a trap when a managed FortiAP goes down.
fswctl-session-up
Send a trap when a FortiSwitch controller session comes up.
fswctl-session-down
Send a trap when a FortiSwitch controller session goes down.
load-balance-real-server-down
Send a trap when a server load balance real server goes down.
device-new
Send a trap when a new device is found.
per-cpu-high
Send a trap when per-CPU usage is high.
dhcp
Send a trap when the DHCP server exhausts the IP pool, an IP address
already is in use, or a DHCP client interface received a DHCP-NAK.
pool-usage
Send a trap about ippool usage.
ippool
Send a trap for ippool events.
interface
Send a trap for interface event.
FortiOS 8.0.0 CLI Reference
2132
Fortinet Inc.

<!-- 来源页 2133 -->
Parameter
Description
Type
Size
Default
Option
Description
ospf-nbr-state-change
Send a trap when there has been a change in the state of a non-virtual
OSPF neighbor.
ospf-virtnbr-state-change
Send a trap when there has been a change in the state of an OSPF
virtual neighbor.
fsso
Send a trap for FSSO event.
bfd
Send a trap for bfd event.
security_level_
change
Send a trap when BIOS security level change.
enter-intf-bypass
Enter interface bypass mode.
exit-intf-bypass
Exit interface bypass mode.
dio
Send a trap when a digital io event happens.
id
Community ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
mib-view
SNMP access control MIB view.
string
Maximum
length: 32
name
Community name.
string
Maximum
length: 35
query-v1-port
SNMP v1 query port (default = 161).
integer
Minimum value:
1 Maximum
value: 65535
161
query-v1-status
Enable/disable SNMP v1 queries.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
query-v2c-port
SNMP v2c query port (default = 161).
integer
Minimum value:
0 Maximum
value: 65535
161
query-v2c-status
Enable/disable SNMP v2c queries.
option
-enable
FortiOS 8.0.0 CLI Reference
2133
Fortinet Inc.

<!-- 来源页 2134 -->
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
status
Enable/disable this SNMP community.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
trap-v1-lport
SNMP v1 trap local port (default = 162).
integer
Minimum value:
1 Maximum
value: 65535
162
trap-v1-rport
SNMP v1 trap remote port (default = 162).
integer
Minimum value:
1 Maximum
value: 65535
162
trap-v1-status
Enable/disable SNMP v1 traps.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
trap-v2c-lport
SNMP v2c trap local port (default = 162).
integer
Minimum value:
1 Maximum
value: 65535
162
trap-v2c-rport
SNMP v2c trap remote port (default = 162).
integer
Minimum value:
1 Maximum
value: 65535
162
trap-v2c-status
Enable/disable SNMP v2c traps.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
vdoms
<name>
SNMP access control VDOMs.
VDOM name.
string
Maximum
length: 79
** Values may differ between models.
FortiOS 8.0.0 CLI Reference
2134
Fortinet Inc.

<!-- 来源页 2135 -->
config hosts
Parameter
Description
Type
Size
Default
ha-direct
Enable/disable direct management of HA cluster
members.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
host-type
Control whether the SNMP manager sends
SNMP queries, receives SNMP traps, or both. No
traps will be sent when IP type is subnet.
option
-any
Option
Description
any
Accept queries from and send traps to this SNMP manager.
query
Accept queries from this SNMP manager but do not send traps.
trap
Send traps to this SNMP manager but do not accept SNMP queries from
this SNMP manager.
id
Host entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
interface
Specify outgoing interface to reach server.
string
Maximum
length: 15
interface-select-method
Specify how to select outgoing interface to
reach server.
option
-auto
Option
Description
auto
Set outgoing interface automatically.
sdwan
Set outgoing interface by SD-WAN or policy routing rules.
specify
Set outgoing interface manually.
ip
IPv4 address of the SNMP manager (host).
user
Not Specified
source-ip
Source IPv4 address for SNMP traps.
ipv4-address
Not Specified
0.0.0.0
vrf-select
VRF ID used for connection to server.
integer
Minimum value:
0 Maximum
value: 511
0
FortiOS 8.0.0 CLI Reference
2135
Fortinet Inc.

<!-- 来源页 2136 -->
config hosts6
Parameter
Description
Type
Size
Default
ha-direct
Enable/disable direct management of HA cluster
members.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
host-type
Control whether the SNMP manager sends
SNMP queries, receives SNMP traps, or both.
option
-any
Option
Description
any
Accept queries from and send traps to this SNMP manager.
query
Accept queries from this SNMP manager but do not send traps.
trap
Send traps to this SNMP manager but do not accept SNMP queries from
this SNMP manager.
id
Host6 entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
interface
Specify outgoing interface to reach server.
string
Maximum
length: 15
interface-select-method
Specify how to select outgoing interface to
reach server.
option
-auto
Option
Description
auto
Set outgoing interface automatically.
sdwan
Set outgoing interface by SD-WAN or policy routing rules.
specify
Set outgoing interface manually.
ipv6
SNMP manager IPv6 address prefix.
ipv6-prefix
Not Specified
::/0
source-ipv6
Source IPv6 address for SNMP traps.
ipv6-address
Not Specified
::
vrf-select
VRF ID used for connection to server.
integer
Minimum value:
0 Maximum
value: 511
0
FortiOS 8.0.0 CLI Reference
2136
Fortinet Inc.

---


<!-- 来源页 2137 -->
config system snmp mib-view
SNMP Access Control MIB View configuration.
config system snmp mib-view
Description: SNMP Access Control MIB View configuration.
edit <name>
set exclude {string}
set include {string}
next
end
config system snmp mib-view
Parameter
Description
Type
Size
Default
exclude
OID subtrees to be excluded in the view. Maximum
64 allowed.
string
Maximum
length: 79
include
OID subtrees to be included in the view. Maximum
16 allowed.
string
Maximum
length: 79
name
MIB view name.
string
Maximum
length: 32
config system snmp rmon-stat
SNMP Remote Network Monitoring (RMON) Ethernet statistics configuration.
config system snmp rmon-stat
Description: SNMP Remote Network Monitoring (RMON) Ethernet statistics configuration.
edit <id>
set owner {string}
set source {string}
next
end
config system snmp rmon-stat
Parameter
Description
Type
Size
Default
id
RMON Ethernet statistics entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
FortiOS 8.0.0 CLI Reference
2137
Fortinet Inc.

---


<!-- 来源页 2137 -->
config system snmp mib-view
SNMP Access Control MIB View configuration.
config system snmp mib-view
Description: SNMP Access Control MIB View configuration.
edit <name>
set exclude {string}
set include {string}
next
end
config system snmp mib-view
Parameter
Description
Type
Size
Default
exclude
OID subtrees to be excluded in the view. Maximum
64 allowed.
string
Maximum
length: 79
include
OID subtrees to be included in the view. Maximum
16 allowed.
string
Maximum
length: 79
name
MIB view name.
string
Maximum
length: 32
config system snmp rmon-stat
SNMP Remote Network Monitoring (RMON) Ethernet statistics configuration.
config system snmp rmon-stat
Description: SNMP Remote Network Monitoring (RMON) Ethernet statistics configuration.
edit <id>
set owner {string}
set source {string}
next
end
config system snmp rmon-stat
Parameter
Description
Type
Size
Default
id
RMON Ethernet statistics entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
FortiOS 8.0.0 CLI Reference
2137
Fortinet Inc.

---


<!-- 来源页 2138 -->
Parameter
Description
Type
Size
Default
owner
Owner of the Ethernet statistics entry.
string
Maximum
length: 127
source
Data source of the Ethernet statistics entry.
string
Maximum
length: 15
config system snmp sysinfo
SNMP system info configuration.
config system snmp sysinfo
Description: SNMP system info configuration.
set append-index [enable|disable]
set contact-info {var-string}
set description {var-string}
set engine-id {string}
set engine-id-type [text|hex|...]
set location {var-string}
set non-mgmt-vdom-query [enable|disable]
set status [enable|disable]
set trap-free-memory-threshold {integer}
set trap-freeable-memory-threshold {integer}
set trap-high-cpu-threshold {integer}
set trap-log-full-threshold {integer}
set trap-low-memory-threshold {integer}
end
config system snmp sysinfo
Parameter
Description
Type
Size
Default
append-index
Enable/disable allowance of appending vdom or
interface index in some RFC tables.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
contact-info
Contact information.
var-string
Maximum
length: 255
description
System description.
var-string
Maximum
length: 255
FortiOS 8.0.0 CLI Reference
2138
Fortinet Inc.

<!-- 来源页 2139 -->
Parameter
Description
Type
Size
Default
engine-id
Local SNMP engineID string (maximum 27
characters).
string
Maximum
length: 54
engine-id-type
Local SNMP engineID type (text/hex/mac).
option
-text
Option
Description
text
Text format.
hex
Octets format.
mac
MAC address format.
location
System location.
var-string
Maximum
length: 255
non-mgmt-vdom-query
Enable/disable allowance of SNMPv3 query from
non-management vdoms.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
status
Enable/disable SNMP.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
trap-free-memory-threshold
Free memory usage when trap is sent.
integer
Minimum
value: 1
Maximum
value: 100
5
trap-freeable-memory-threshold
Freeable memory usage when trap is sent.
integer
Minimum
value: 1
Maximum
value: 100
60
trap-high-cpu-threshold
CPU usage when trap is sent.
integer
Minimum
value: 1
Maximum
value: 100
80
trap-log-full-threshold
Log disk usage when trap is sent.
integer
Minimum
value: 1
Maximum
value: 100
90
FortiOS 8.0.0 CLI Reference
2139
Fortinet Inc.

---


<!-- 来源页 2140 -->
Parameter
Description
Type
Size
Default
trap-low-memory-threshold
Memory usage when trap is sent.
integer
Minimum
value: 1
Maximum
value: 100
80
config system snmp user
SNMP user configuration.
config system snmp user
Description: SNMP user configuration.
edit <name>
set auth-proto [md5|sha|...]
set auth-pwd {password}
set events {option1}, {option2}, ...
set ha-direct [enable|disable]
set interface {string}
set interface-select-method [auto|sdwan|...]
set mib-view {string}
set notify-hosts {ipv4-address}
set notify-hosts6 {ipv6-address}
set priv-proto [aes|des|...]
set priv-pwd {password}
set queries [enable|disable]
set query-port {integer}
set security-level [no-auth-no-priv|auth-no-priv|...]
set source-ip {ipv4-address}
set source-ipv6 {ipv6-address}
set status [enable|disable]
set trap-lport {integer}
set trap-rport {integer}
set trap-status [enable|disable]
set vdoms <name1>, <name2>, ...
set vrf-select {integer}
next
end
config system snmp user
Parameter
Description
Type
Size
Default
auth-proto
Authentication protocol.
option
-sha
FortiOS 8.0.0 CLI Reference
2140
Fortinet Inc.

<!-- 来源页 2141 -->
Parameter
Description
Type
Size
Default
Option
Description
md5
HMAC-MD5-96 authentication protocol.
sha
HMAC-SHA-96 authentication protocol.
sha224
HMAC-SHA224 authentication protocol.
sha256
HMAC-SHA256 authentication protocol.
sha384
HMAC-SHA384 authentication protocol.
sha512
HMAC-SHA512 authentication protocol.
auth-pwd
Password for authentication protocol.
password
Not
Specified
FortiOS 8.0.0 CLI Reference
2141
Fortinet Inc.

<!-- 来源页 2142 -->
Parameter
Description
Type
Size
Default
events
SNMP notifications (traps) to send.
option
-cpu-high mem-low log-full
intf-ip vpn-tun-up vpn-tun-down ha-switch ha-hb-failure ips-signature ips-anomaly av-virus av-oversize av-pattern av-fragmented fm-if-change bgp-established
bgp-backward-transition ha-member-up ha-member-down
ent-conf-change av-conserve av-bypass av-oversize-passed av-oversize-blocked ips-pkg-update
ips-fail-open
temperature-high voltage-alert power-supply faz-disconnect faz
fan-failure wc-ap-up wc-ap-down fswctl-session-up
fswctl-session-down load-balance-real-server-down
per-cpu-high
dhcp pool-usage ippool
interface ospf-nbr-state-change ospf-virtnbr-state-change fsso
bfd **
FortiOS 8.0.0 CLI Reference
2142
Fortinet Inc.

<!-- 来源页 2143 -->
Parameter
Description
Type
Size
Default
Option
Description
cpu-high
Send a trap when CPU usage is high.
mem-low
Send a trap when used memory is high, free memory is low, or freeable
memory is high.
log-full
Send a trap when log disk space becomes low.
intf-ip
Send a trap when an interface IP address is changed.
vpn-tun-up
Send a trap when a VPN tunnel comes up.
vpn-tun-down
Send a trap when a VPN tunnel goes down.
ha-switch
Send a trap after an HA failover when the backup unit has taken over.
ha-hb-failure
Send a trap when HA heartbeats are not received.
ips-signature
Send a trap when IPS detects an attack.
ips-anomaly
Send a trap when IPS finds an anomaly.
av-virus
Send a trap when AntiVirus finds a virus.
av-oversize
Send a trap when AntiVirus finds an oversized file.
av-pattern
Send a trap when AntiVirus finds file matching pattern.
av-fragmented
Send a trap when AntiVirus finds a fragmented file.
fm-if-change
Send a trap when FortiManager interface changes. Send a FortiManager
trap.
fm-conf-change
Send a trap when a configuration change is made by a FortiGate
administrator and the FortiGate is managed by FortiManager.
bgp-established
Send a trap when a BGP FSM transitions to the established state.
bgp-backward-transition
Send a trap when a BGP FSM goes from a high numbered state to a
lower numbered state.
ha-member-up
Send a trap when an HA cluster member goes up.
ha-member-down
Send a trap when an HA cluster member goes down.
ent-conf-change
Send a trap when an entity MIB change occurs (RFC4133).
av-conserve
Send a trap when the FortiGate enters conserve mode.
av-bypass
Send a trap when the FortiGate enters bypass mode.
FortiOS 8.0.0 CLI Reference
2143
Fortinet Inc.

<!-- 来源页 2144 -->
Parameter
Description
Type
Size
Default
Option
Description
av-oversize-passed
Send a trap when AntiVirus passes an oversized file.
av-oversize-blocked
Send a trap when AntiVirus blocks an oversized file.
ips-pkg-update
Send a trap when the IPS signature database or engine is updated.
ips-fail-open
Send a trap when the IPS network buffer is full.
temperature-high
Send a trap when a temperature sensor registers a temperature that is
too high.
voltage-alert
Send a trap when a voltage sensor registers a voltage that is outside of
the normal range.
power-supply
Send a trap when a power supply fails or restores.
faz-disconnect
Send a trap when a FortiAnalyzer disconnects from the FortiGate.
faz
Send a trap when Fortianalyzer main server failover and alternate server
take over, or alternate server failover and main server take over.
fan-failure
Send a trap when a fan fails.
wc-ap-up
Send a trap when a managed FortiAP comes up.
wc-ap-down
Send a trap when a managed FortiAP goes down.
fswctl-session-up
Send a trap when a FortiSwitch controller session comes up.
fswctl-session-down
Send a trap when a FortiSwitch controller session goes down.
load-balance-real-server-down
Send a trap when a server load balance real server goes down.
device-new
Send a trap when a new device is found.
per-cpu-high
Send a trap when per-CPU usage is high.
dhcp
Send a trap when the DHCP server exhausts the IP pool, an IP address
already is in use, or a DHCP client interface received a DHCP-NAK.
pool-usage
Send a trap about ippool usage.
ippool
Send a trap for ippool events.
interface
Send a trap for interface event.
FortiOS 8.0.0 CLI Reference
2144
Fortinet Inc.

<!-- 来源页 2145 -->
Parameter
Description
Type
Size
Default
Option
Description
ospf-nbr-state-change
Send a trap when there has been a change in the state of a non-virtual
OSPF neighbor.
ospf-virtnbr-state-change
Send a trap when there has been a change in the state of an OSPF
virtual neighbor.
fsso
Send a trap for FSSO event.
bfd
Send a trap for bfd event.
security_level_
change
Send a trap when BIOS security level change.
enter-intf-bypass
Enter interface bypass mode.
exit-intf-bypass
Exit interface bypass mode.
dio
Send a trap when a digital io event happens.
ha-direct
Enable/disable direct management of HA
cluster members.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
interface
Specify outgoing interface to reach server.
string
Maximum
length: 15
interface-select-method
Specify how to select outgoing interface to
reach server.
option
-auto
Option
Description
auto
Set outgoing interface automatically.
sdwan
Set outgoing interface by SD-WAN or policy routing rules.
specify
Set outgoing interface manually.
mib-view
SNMP access control MIB view.
string
Maximum
length: 32
name
SNMP user name.
string
Maximum
length: 32
notify-hosts
SNMP managers to send notifications (traps)
to.
ipv4-address
Not
Specified
FortiOS 8.0.0 CLI Reference
2145
Fortinet Inc.

<!-- 来源页 2146 -->
Parameter
Description
Type
Size
Default
notify-hosts6
IPv6 SNMP managers to send notifications
(traps) to.
ipv6-address
Not
Specified
priv-proto
Privacy (encryption) protocol.
option
-aes
Option
Description
aes
CFB128-AES-128 symmetric encryption protocol.
des
CBC-DES symmetric encryption protocol.
aes256
CFB128-AES-256 symmetric encryption protocol.
aes256cisco
CFB128-AES-256 symmetric encryption protocol compatible with
CISCO.
priv-pwd
Password for privacy (encryption) protocol.
password
Not
Specified
queries
Enable/disable SNMP queries for this user.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
query-port
SNMPv3 query port (default = 161).
integer
Minimum
value: 1
Maximum
value:
65535
161
security-level
Security level for message authentication and
encryption.
option
-no-auth-no-priv
Option
Description
no-auth-no-priv
Message with no authentication and no privacy (encryption).
auth-no-priv
Message with authentication but no privacy (encryption).
auth-priv
Message with authentication and privacy (encryption).
source-ip
Source IP for SNMP trap.
ipv4-address
Not
Specified
0.0.0.0
source-ipv6
Source IPv6 for SNMP trap.
ipv6-address
Not
Specified
::
status
Enable/disable this SNMP user.
option
-enable
FortiOS 8.0.0 CLI Reference
2146
Fortinet Inc.
