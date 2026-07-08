# 防火墙：安全策略 / 地址 / 服务 / 调度

> 来源: FortiOS-8.0.0-CLI_Reference.pdf
> 覆盖命令/章节: config firewall policy, config firewall security-policy, config firewall address, config firewall address6, config firewall address6-template, config firewall addrgrp, config firewall addrgrp6, config firewall wildcard-fqdn custom, config firewall wildcard-fqdn group, config firewall service custom, config firewall service group, config firewall service category, config firewall schedule onetime, config firewall schedule recurring, config firewall schedule group, config firewall profile-group, config firewall profile-protocol-options, config firewall ssl-ssh-profile, config firewall proxy-policy, config firewall proxy-address, config firewall proxy-address6, config firewall proxy-addrgrp, config firewall proxy-addrgrp6, config firewall region, config firewall custom-tag, config firewall traffic-class, config firewall global, config firewall internet-service, config firewall internet-service-addition, config firewall internet-service-append, config firewall internet-service-botnet, config firewall internet-service-custom, config firewall internet-service-custom-group, config firewall internet-service-definition, config firewall internet-service-extension, config firewall internet-service-fortiguard, config firewall internet-service-group, config firewall internet-service-ipbl-reason, config firewall internet-service-ipbl-vendor, config firewall internet-service-list, config firewall internet-service-name, config firewall internet-service-owner, config firewall internet-service-reputation, config firewall internet-service-sld, config firewall internet-service-subapp
> 本文件由 extract_pdf.py 从官方 PDF 自动提取，请勿手动编辑；
> 如需修正请修改 map.json 后重跑脚本。

---


<!-- 来源页 481 -->
config firewall acl6
Parameter
Description
Type
Size
Default
comments
Comment.
var-string
Maximum
length:
1023
dstaddr
<name>
Destination address name.
Address name.
string
Maximum
length: 79
fragment
Pass/drop fragments that match L3 information.
option
-pass
Option
Description
pass
Pass fragments that match interface, srcaddr, and dstaddr.
drop
Drop fragments that match interface, srcaddr, and dstaddr.
interface
Interface name.
string
Maximum
length: 35
name
Policy name.
string
Maximum
length: 35
policyid
Policy ID.
integer
Minimum
value: 0
Maximum
value: 9999
0
service
<name>
Service name.
Service name.
string
Maximum
length: 79
srcaddr
<name>
Source address name.
Address name.
string
Maximum
length: 79
status
Enable/disable access control list status.
option
-enable
Option
Description
enable
Enable access control list status.
disable
Disable access control list status.
config firewall address
Configure IPv4 addresses.
config firewall address
Description: Configure IPv4 addresses.
edit <name>
config addr-8021x
FortiOS 8.0.0 CLI Reference
481
Fortinet Inc.

<!-- 来源页 482 -->
Description: 802.1X address. Read-only.
edit <interface>
set acct-user {string}
set ip {ipv4-address-any}
set mac {string}
set vlan-id {integer}
next
end
set agent-id {string}
set allow-routing [enable|disable]
set associated-interface {string}
set cache-ttl {integer}
set clearpass-spt [unknown|healthy|...]
set color {integer}
set comment {var-string}
set country {string}
set custom-tags <name1>, <name2>, ...
set display-with [all-tags|first-tag-only|...]
set end-ip {ipv4-address-any}
set epg-name {string}
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set filter {var-string}
set fqdn {string}
set fsso-group <name1>, <name2>, ...
set hw-model {string}
set hw-vendor {string}
set hw-version {string}
set interface {string}
set ipam-allocate-unique [enable|disable]
config list
Description: IP address list.
edit <ip>
next
end
set macaddr <macaddr1>, <macaddr2>, ...
set managed-subnetwork-size [4|8|...]
set node-ip-only [enable|disable]
set obj-id {var-string}
set obj-tag {string}
set obj-type [ip|mac]
set obsolete {integer}
set organization {string}
set os {string}
set passive-fqdn-learning [disable|enable]
set policy-group {string}
set route-tag {integer}
set sdn {string}
set sdn-addr-type [private|public|...]
set sdn-tag {string}
set sso-attribute-value <name1>, <name2>, ...
FortiOS 8.0.0 CLI Reference
482
Fortinet Inc.

<!-- 来源页 483 -->
set start-ip {ipv4-address-any}
set sub-type [sdn|clearpass-spt|...]
set subnet {ipv4-classnet-any}
set subnet-name {string}
set sw-version {string}
set tag-detection-level {string}
set tag-type {string}
config tagging
Description: Config object tagging.
edit <name>
set category {string}
set tags <name1>, <name2>, ...
next
end
set tenant {string}
set type [ipmask|iprange|...]
set uuid {uuid}
set wildcard {ipv4-classnet-any}
set wildcard-fqdn {string}
next
end
config firewall address
Parameter
Description
Type
Size
Default
agent-id *
Telemetry agent id.
string
Maximum
length: 19
allow-routing
Enable/disable use of this address in
routing configurations.
option
-disable
Option
Description
enable
Enable use of this address in routing configurations.
disable
Disable use of this address in routing configurations.
associated-interface
Network interface associated with
address.
string
Maximum
length: 35
cache-ttl
Defines the minimal TTL of individual IP
addresses in FQDN cache measured in
seconds.
integer
Minimum value:
0 Maximum
value: 86400
0
clearpass-spt
SPT (System Posture Token) value.
option
-unknown
Option
Description
unknown
UNKNOWN.
FortiOS 8.0.0 CLI Reference
483
Fortinet Inc.

<!-- 来源页 484 -->
Parameter
Description
Type
Size
Default
Option
Description
healthy
HEALTHY.
quarantine
QUARANTINE.
checkup
CHECKUP.
transient
TRANSIENT.
infected
INFECTED.
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
country
IP addresses associated to a specific
country.
string
Maximum
length: 2
custom-tags
<name> *
Custom tags.
Names of custom tags used with this
address.
string
Maximum
length: 35
display-with *
Display object with first tag, all tags, or
just the icon & color.
option
-all-tags
Option
Description
all-tags
Display object using all custom tags.
first-tag-only
Display object using first custom tag.
icon-and-color
Display object using icon and color.
end-ip
Final IP address (inclusive) in the range
for the address.
ipv4-address-any
Not Specified
0.0.0.0
epg-name
Endpoint group name.
string
Maximum
length: 255
fabric-force-sync *
Enable/disable forced synchronization
of configuration objects from the root
FortiGate unit to the downstream
devices. Configuration conflict check is
skipped.
option
-disable
FortiOS 8.0.0 CLI Reference
484
Fortinet Inc.

<!-- 来源页 485 -->
Parameter
Description
Type
Size
Default
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
filter
Match criteria filter.
var-string
Maximum
length: 2047
fqdn
Fully Qualified Domain Name address.
string
Maximum
length: 255
fsso-group
<name>
FSSO group(s).
FSSO group name.
string
Maximum
length: 511
hw-model *
Dynamic address matching hardware
model.
string
Maximum
length: 35
hw-vendor
Dynamic address matching hardware
vendor.
string
Maximum
length: 35
hw-version *
Dynamic address matching hardware
version.
string
Maximum
length: 35
interface
Name of interface whose IP address is
to be used.
string
Maximum
length: 35
ipam-allocate-unique *
Allocate unique subnet for FortiIPAM
managed fabric-object address.
option
-disable
FortiOS 8.0.0 CLI Reference
485
Fortinet Inc.

<!-- 来源页 486 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable unique subnet allocation on each FortiGate.
disable
Disable unique subnet allocation on each FortiGate.
macaddr
<macaddr>
Multiple MAC address ranges.
MAC address ranges <start>[-<end>]
separated by space.
string
Maximum
length: 127
managed-subnetwork-size *
Number of IP addresses to be
allocated by FortiIPAM for this
address.
option
-256
Option
Description
4
Allocate a subnet with 4 IP addresses.
8
Allocate a subnet with 8 IP addresses.
16
Allocate a subnet with 16 IP addresses.
32
Allocate a subnet with 32 IP addresses.
64
Allocate a subnet with 64 IP addresses.
128
Allocate a subnet with 128 IP addresses.
256
Allocate a subnet with 256 IP addresses.
512
Allocate a subnet with 512 IP addresses.
1024
Allocate a subnet with 1024 IP addresses.
2048
Allocate a subnet with 2048 IP addresses.
4096
Allocate a subnet with 4096 IP addresses.
8192
Allocate a subnet with 8192 IP addresses.
16384
Allocate a subnet with 16384 IP addresses.
32768
Allocate a subnet with 32768 IP addresses.
65536
Allocate a subnet with 65536 IP addresses.
131072
Allocate a subnet with 131072 IP addresses.
262144
Allocate a subnet with 262144 IP addresses.
524288
Allocate a subnet with 524288 IP addresses.
1048576
Allocate a subnet with 1048576 IP addresses.
2097152
Allocate a subnet with 2097152 IP addresses.
FortiOS 8.0.0 CLI Reference
486
Fortinet Inc.

<!-- 来源页 487 -->
Parameter
Description
Type
Size
Default
Option
Description
4194304
Allocate a subnet with 4194304 IP addresses.
8388608
Allocate a subnet with 8388608 IP addresses.
16777216
Allocate a subnet with 16777216 IP addresses.
name
Address name.
string
Maximum
length: 79
node-ip-only
Enable/disable collection of node
addresses only in Kubernetes.
option
-disable
Option
Description
enable
Enable collection of node addresses only in Kubernetes.
disable
Disable collection of node addresses only in Kubernetes.
obj-id
Object ID for NSX.
var-string
Maximum
length: 255
obj-tag
Tag of dynamic address object.
string
Maximum
length: 255
obj-type
Object type.
option
-ip
Option
Description
ip
IP address.
mac
MAC address
obsolete *
Indicates whether the address can be
used. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
organization
Organization domain name (Syntax:
organization/domain).
string
Maximum
length: 35
os
Dynamic address matching operating
system.
string
Maximum
length: 35
passive-fqdn-learning
Enable/disable passive learning of
FQDNs. When enabled, the FortiGate
learns, trusts, and saves FQDNs from
endpoint DNS queries (default =
enable).
option
-enable
FortiOS 8.0.0 CLI Reference
487
Fortinet Inc.

<!-- 来源页 488 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable passive learning of FQDNs.
enable
Enable passive learning of FQDNs.
policy-group
Policy group name.
string
Maximum
length: 15
route-tag
route-tag address.
integer
Minimum value:
1 Maximum
value:
4294967295
0
sdn
SDN.
string
Maximum
length: 35
sdn-addr-type
Type of addresses to collect.
option
-private
Option
Description
private
Collect private addresses only.
public
Collect public addresses only.
all
Collect both public and private addresses.
sdn-tag
SDN Tag.
string
Maximum
length: 15
sso-attribute-value <name>
RADIUS attributes value.
RADIUS attribute value.
string
Maximum
length: 511
start-ip
First IP address (inclusive) in the range
for the address.
ipv4-address-any
Not Specified
0.0.0.0
sub-type
Sub-type of address.
option
-sdn
Option
Description
sdn
SDN address.
clearpass-spt
ClearPass SPT (System Posture Token) address.
fsso
FSSO address.
rsso
RSSO address.
ems-tag
FortiClient EMS tag.
fortivoice-tag
FortiVoice tag.
fortinac-tag
FortiNAC tag.
FortiOS 8.0.0 CLI Reference
488
Fortinet Inc.

<!-- 来源页 489 -->
Parameter
Description
Type
Size
Default
Option
Description
swc-tag
Switch Controller NAC policy tag.
device-identification
Device address.
external-resource
External resource.
telemetry
Telemetry address.
obsolete
Tag from EOL product.
8021x
802.1X address.
subnet
IP address and subnet mask of
address.
ipv4-classnet-any
Not Specified
0.0.0.0 0.0.0.0
subnet-name
Subnet name.
string
Maximum
length: 255
sw-version
Dynamic address matching software
version.
string
Maximum
length: 35
tag-detection-level
Tag detection level of dynamic
address object.
string
Maximum
length: 15
tag-type
Tag type of dynamic address object.
string
Maximum
length: 63
tenant
Tenant.
string
Maximum
length: 35
type
Type of address.
option
-ipmask
Option
Description
ipmask
Standard IPv4 address with subnet mask.
iprange
Range of IPv4 addresses between two specified addresses (inclusive).
fqdn
Fully Qualified Domain Name address.
geography
IP addresses from a specified country.
wildcard
Standard IPv4 using a wildcard subnet mask.
dynamic
Dynamic address object.
interface-subnet
IP and subnet of interface.
ipam
Address with subnet mask under IP Address Management.
FortiOS 8.0.0 CLI Reference
489
Fortinet Inc.

<!-- 来源页 490 -->
Parameter
Description
Type
Size
Default
Option
Description
mac
Range of MAC addresses.
route-tag
route-tag addresses.
uuid
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not Specified
00000000-0000-0000-0000-000000000000
wildcard
IP address and wildcard netmask.
ipv4-classnet-any
Not Specified
0.0.0.0 0.0.0.0
wildcard-fqdn
Fully Qualified Domain Name with
wildcard characters.
string
Maximum
length: 255
* This parameter may not exist in some models.
config addr-8021x
Parameter
Description
Type
Size
Default
acct-user
Account user name. Read-only.
string
Maximum
length: 64
interface
Interface name. Read-only.
string
Maximum
length: 15
ip
IP address. Read-only.
ipv4-address-any
Not Specified
0.0.0.0
mac
MAC address. Read-only.
string
Maximum
length: 127
vlan-id
VLAN ID. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config list
Parameter
Description
Type
Size
Default
ip
IP.
string
Maximum length:
35
FortiOS 8.0.0 CLI Reference
490
Fortinet Inc.

---


<!-- 来源页 491 -->
config tagging
Parameter
Description
Type
Size
Default
category
Tag category.
string
Maximum
length: 63
name
Tagging entry name.
string
Maximum
length: 63
tags <name>
Tags.
Tag name.
string
Maximum
length: 79
config firewall address6
Configure IPv6 firewall addresses.
config firewall address6
Description: Configure IPv6 firewall addresses.
edit <name>
config addr-8021x
Description: 802.1X address. Read-only.
edit <interface>
set acct-user {string}
set ip6 {ipv6-address}
set mac {string}
set vlan-id {integer}
next
end
set cache-ttl {integer}
set color {integer}
set comment {var-string}
set country {string}
set custom-tags <name1>, <name2>, ...
set display-with [all-tags|first-tag-only|...]
set end-ip {ipv6-address}
set epg-name {string}
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set filter {var-string}
set fqdn {string}
set host {ipv6-address}
set host-type [any|specific]
set ip6 {ipv6-network}
config list
Description: IP address list.
edit <ip>
next
end
FortiOS 8.0.0 CLI Reference
491
Fortinet Inc.

<!-- 来源页 492 -->
set macaddr <macaddr1>, <macaddr2>, ...
set obj-id {var-string}
set obj-tag {string}
set obsolete {integer}
set passive-fqdn-learning [disable|enable]
set route-tag {integer}
set sdn {string}
set sdn-addr-type [private|public|...]
set sdn-tag {string}
set start-ip {ipv6-address}
set sub-type [sdn|ems-tag|...]
config subnet-segment
Description: IPv6 subnet segments.
edit <name>
set type [any|specific]
set value {string}
next
end
set tag-detection-level {string}
set tag-type {string}
config tagging
Description: Config object tagging.
edit <name>
set category {string}
set tags <name1>, <name2>, ...
next
end
set template {string}
set tenant {string}
set type [ipprefix|iprange|...]
set uuid {uuid}
set wildcard {ipv6-wildcard}
next
end
config firewall address6
Parameter
Description
Type
Size
Default
cache-ttl
Minimal TTL of individual IPv6 addresses in
FQDN cache.
integer
Minimum
value: 0
Maximum
value: 86400
0
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
FortiOS 8.0.0 CLI Reference
492
Fortinet Inc.

<!-- 来源页 493 -->
Parameter
Description
Type
Size
Default
comment
Comment.
var-string
Maximum
length: 255
country
IPv6 addresses associated to a specific
country.
string
Maximum
length: 2
custom-tags
<name> *
Custom tags.
Names of custom tags used with this
address.
string
Maximum
length: 35
display-with
*
Display object with first tag, all tags, or just
the icon.
option
-all-tags
Option
Description
all-tags
Display object using all custom tags.
first-tag-only
Display object using first custom tag.
icon-and-color
Display object using icon and color.
end-ip
Final IP address (inclusive) in the range for
the address (format:
xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx).
ipv6-address
Not Specified
::
epg-name
Endpoint group name.
string
Maximum
length: 255
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
Security Fabric global object setting.
option
-disable
Option
Description
enable
Object is set as a security fabric-wide global object.
disable
Object is local to this security fabric member.
FortiOS 8.0.0 CLI Reference
493
Fortinet Inc.

<!-- 来源页 494 -->
Parameter
Description
Type
Size
Default
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
filter
Match criteria filter.
var-string
Maximum
length: 2047
fqdn
Fully qualified domain name.
string
Maximum
length: 255
host
Host Address.
ipv6-address
Not Specified
::
host-type
Host type.
option
-any
Option
Description
any
Wildcard.
specific
Specific host address.
ip6
IPv6 address prefix (format:
xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xx
x).
ipv6-network
Not Specified
::/0
macaddr
<macaddr>
Multiple MAC address ranges.
MAC address ranges <start>[-<end>]
separated by space.
string
Maximum
length: 127
name
Address name.
string
Maximum
length: 79
obj-id
Object ID for NSX.
var-string
Maximum
length: 255
obj-tag *
Tag of dynamic address object.
string
Maximum
length: 255
obsolete *
Indicates whether the address can be used.
Read-only.
integer
Minimum
value: 0
Maximum
value:
4294967295
0
FortiOS 8.0.0 CLI Reference
494
Fortinet Inc.

<!-- 来源页 495 -->
Parameter
Description
Type
Size
Default
passive-fqdn-learning
Enable/disable passive learning of FQDNs.
When enabled, the FortiGate learns, trusts,
and saves FQDNs from endpoint DNS queries
(default = enable).
option
-enable
Option
Description
disable
Disable passive learning of FQDNs.
enable
Enable passive learning of FQDNs.
route-tag
route-tag address.
integer
Minimum
value: 1
Maximum
value:
4294967295
0
sdn
SDN.
string
Maximum
length: 35
sdn-addr-type
Type of addresses to collect.
option
-private
Option
Description
private
Collect private addresses only.
public
Collect public addresses only.
all
Collect both public and private addresses.
sdn-tag
SDN Tag.
string
Maximum
length: 15
start-ip
First IP address (inclusive) in the range for
the address (format:
xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx).
ipv6-address
Not Specified
::
sub-type *
Sub-type of address.
option
-sdn
Option
Description
sdn
SDN address.
ems-tag
FortiClient EMS tag.
8021x
802.1X address.
tag-detection-level *
Tag detection level of dynamic address
object.
string
Maximum
length: 15
FortiOS 8.0.0 CLI Reference
495
Fortinet Inc.

<!-- 来源页 496 -->
Parameter
Description
Type
Size
Default
tag-type *
Tag type of dynamic address object.
string
Maximum
length: 63
template
IPv6 address template.
string
Maximum
length: 63
tenant
Tenant.
string
Maximum
length: 35
type
Type of IPv6 address object (default =
ipprefix).
option
-ipprefix
Option
Description
ipprefix
Uses the IP prefix to define a range of IPv6 addresses.
iprange
Range of IPv6 addresses between two specified addresses (inclusive).
fqdn
Fully qualified domain name.
geography
IPv6 addresses from a specified country.
dynamic
Dynamic address object.
template
Template.
mac
Range of MAC addresses.
route-tag
route-tag addresses.
wildcard
Standard IPv6 using a wildcard subnet mask.
uuid
Universally Unique Identifier (UUID;
automatically assigned but can be manually
reset).
uuid
Not Specified
00000000-0000-0000-0000-000000000000
wildcard
IPv6 address and wildcard netmask.
ipv6-wildcard
Not Specified
:: ::
* This parameter may not exist in some models.
config addr-8021x
Parameter
Description
Type
Size
Default
acct-user
Account user name. Read-only.
string
Maximum
length: 64
interface
Interface name. Read-only.
string
Maximum
length: 15
ip6
IPv6 address. Read-only.
ipv6-address
Not Specified
::
FortiOS 8.0.0 CLI Reference
496
Fortinet Inc.

<!-- 来源页 497 -->
Parameter
Description
Type
Size
Default
mac
MAC address. Read-only.
string
Maximum
length: 127
vlan-id
VLAN ID. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config list
Parameter
Description
Type
Size
Default
ip
IP.
string
Maximum length:
89
config subnet-segment
Parameter
Description
Type
Size
Default
name
Name.
string
Maximum
length: 63
type
Subnet segment type.
option
-any
Option
Description
any
Wildcard.
specific
Specific subnet segment address.
value
Subnet segment value.
string
Maximum
length: 35
config tagging
Parameter
Description
Type
Size
Default
category
Tag category.
string
Maximum
length: 63
name
Tagging entry name.
string
Maximum
length: 63
tags <name>
Tags.
Tag name.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
497
Fortinet Inc.

---


<!-- 来源页 498 -->
config firewall address6-template
Configure IPv6 address templates.
config firewall address6-template
Description: Configure IPv6 address templates.
edit <name>
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set ip6 {ipv6-network}
config subnet-segment
Description: IPv6 subnet segments.
edit <id>
set bits {integer}
set exclusive [enable|disable]
set name {string}
config values
Description: Subnet segment values.
edit <name>
set value {string}
next
end
next
end
set subnet-segment-count {integer}
set uuid {uuid}
next
end
config firewall address6-template
Parameter
Description
Type
Size
Default
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
Security Fabric global object setting.
option
-disable
FortiOS 8.0.0 CLI Reference
498
Fortinet Inc.

<!-- 来源页 499 -->
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
ip6
IPv6 address prefix.
ipv6-network
Not
Specified
::/0
name
IPv6 address template name.
string
Maximum
length: 63
subnet-segment-count
Number of IPv6 subnet segments.
integer
Minimum
value: 1
Maximum
value: 6
0
uuid
Universally Unique Identifier (UUID;
automatically assigned but can be manually
reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
config subnet-segment
Parameter
Description
Type
Size
Default
bits
Number of bits.
integer
Minimum value:
1 Maximum
value: 16
0
exclusive
Enable/disable exclusive value.
option
-disable
Option
Description
enable
Enable exclusive value.
disable
Disable exclusive value.
FortiOS 8.0.0 CLI Reference
499
Fortinet Inc.

---


<!-- 来源页 500 -->
Parameter
Description
Type
Size
Default
id
Subnet segment ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
name
Subnet segment name.
string
Maximum
length: 63
config values
Parameter
Description
Type
Size
Default
name
Subnet segment value name.
string
Maximum
length: 63
value
Subnet segment value.
string
Maximum
length: 35
config firewall addrgrp
Configure IPv4 address groups.
config firewall addrgrp
Description: Configure IPv4 address groups.
edit <name>
set allow-routing [enable|disable]
set category [default|ztna-ems-tag|...]
set color {integer}
set comment {var-string}
set custom-tags <name1>, <name2>, ...
set display-with [all-tags|first-tag-only|...]
set exclude [enable|disable]
set exclude-member <name1>, <name2>, ...
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set member <name1>, <name2>, ...
config tagging
Description: Config object tagging.
edit <name>
set category {string}
set tags <name1>, <name2>, ...
next
end
set type [default|folder|...]
set uuid {uuid}
next
end
FortiOS 8.0.0 CLI Reference
500
Fortinet Inc.

<!-- 来源页 501 -->
config firewall addrgrp
Parameter
Description
Type
Size
Default
allow-routing
Enable/disable use of this group in routing
configurations.
option
-disable
Option
Description
enable
Enable use of this group in routing configurations.
disable
Disable use of this group in routing configurations.
category
Address group category.
option
-default
Option
Description
default
Default address group category (cannot be used as ztna-ems-tag/ztna-geo-tag in policy).
ztna-ems-tag
Members must be ztna-ems-tag group or ems-tag address, can be used
as ztna-ems-tag in policy.
ztna-geo-tag
Members must be ztna-geo-tag group or geographic address, can be
used as ztna-geo-tag in policy.
telemetry
Members must be telemetry group or telemetry address, can be used to
determine telemetry policy.
color
Color of icon on the GUI.
integer
Minimum
value: 0
Maximum
value: 32
0
comment
Comment.
var-string
Maximum
length: 255
custom-tags
<name> *
Custom tags.
Names of custom tags used with this
address group.
string
Maximum
length: 35
display-with
*
Display object with first tag, all tags, or just
the icon.
option
-all-tags
Option
Description
all-tags
Display object using all custom tags.
first-tag-only
Display object using first custom tag.
icon-and-color
Display object using icon and color.
exclude
Enable/disable address exclusion.
option
-disable
FortiOS 8.0.0 CLI Reference
501
Fortinet Inc.

<!-- 来源页 502 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable address exclusion.
disable
Disable address exclusion.
exclude-member
<name>
Address exclusion member.
Address name.
string
Maximum
length: 79
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
member
<name>
Address objects contained within the group.
Address name.
string
Maximum
length: 79
name
Address group name.
string
Maximum
length: 79
type
Address group type.
option
-default
FortiOS 8.0.0 CLI Reference
502
Fortinet Inc.

---


<!-- 来源页 503 -->
Parameter
Description
Type
Size
Default
Option
Description
default
Default address group type (address may belong to multiple groups).
folder
Address folder group (members may not belong to any other group).
dynamic-tag
Dynamic tag group (members are addresses only if they have any one of
the configured tags).
uuid
Universally Unique Identifier (UUID;
automatically assigned but can be manually
reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
config tagging
Parameter
Description
Type
Size
Default
category
Tag category.
string
Maximum
length: 63
name
Tagging entry name.
string
Maximum
length: 63
tags <name>
Tags.
Tag name.
string
Maximum
length: 79
config firewall addrgrp6
Configure IPv6 address groups.
config firewall addrgrp6
Description: Configure IPv6 address groups.
edit <name>
set category [default|ztna-ems-tag]
set color {integer}
set comment {var-string}
set custom-tags <name1>, <name2>, ...
set display-with [all-tags|first-tag-only|...]
set exclude [enable|disable]
set exclude-member <name1>, <name2>, ...
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set member <name1>, <name2>, ...
config tagging
Description: Config object tagging.
edit <name>
FortiOS 8.0.0 CLI Reference
503
Fortinet Inc.

<!-- 来源页 504 -->
set category {string}
set tags <name1>, <name2>, ...
next
end
set type [default|dynamic-tag]
set uuid {uuid}
next
end
config firewall addrgrp6
Parameter
Description
Type
Size
Default
category *
Address group category.
option
-default
Option
Description
default
Default address group category (cannot be used as ztna-ems-tag in
policy).
ztna-ems-tag
Members must be ztna-ems-tag group or ems-tag address, can be used
as ztna-ems-tag in policy.
color
Integer value to determine the color of the
icon in the GUI (1 - 32, default = 0, which
sets the value to 1).
integer
Minimum
value: 0
Maximum
value: 32
0
comment
Comment.
var-string
Maximum
length: 255
custom-tags
<name> *
Custom tags.
Names of custom tags used with this
address group.
string
Maximum
length: 35
display-with
*
Display object with first tag, all tags, or just
the icon.
option
-all-tags
Option
Description
all-tags
Display object using all custom tags.
first-tag-only
Display object using first custom tag.
icon-and-color
Display object using icon and color.
exclude
Enable/disable address6 exclusion.
option
-disable
Option
Description
enable
Enable address6 exclusion.
disable
Disable address6 exclusion.
FortiOS 8.0.0 CLI Reference
504
Fortinet Inc.

<!-- 来源页 505 -->
Parameter
Description
Type
Size
Default
exclude-member
<name>
Address6 exclusion member.
Address6 name.
string
Maximum
length: 79
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
member
<name>
Address objects contained within the group.
Address6/addrgrp6 name.
string
Maximum
length: 79
name
IPv6 address group name.
string
Maximum
length: 79
type *
Address group type.
option
-default
Option
Description
default
Default address group type (address may belong to multiple groups).
dynamic-tag
Dynamic tag group (members are addresses only if they have any one of
the configured tags).
FortiOS 8.0.0 CLI Reference
505
Fortinet Inc.

---


<!-- 来源页 512 -->
config firewall custom-tag
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
Define custom tag table.
config firewall custom-tag
Description: Define custom tag table.
edit <name>
set abbreviation {string}
set color {integer}
set comment {var-string}
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set uuid {uuid}
next
end
FortiOS 8.0.0 CLI Reference
512
Fortinet Inc.

<!-- 来源页 513 -->
config firewall custom-tag
Parameter
Description
Type
Size
Default
abbreviation
Custom tag name abbreviation.
string
Maximum
length: 3
color
Color of the custom tag on the GUI.
integer
Minimum
value: 0
Maximum
value: 32
1
comment
Comment.
var-string
Maximum
length: 255
fabric-force-sync
Enable/disable forced synchronization of
configuration objects from the root
FortiGate unit to the downstream devices.
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
Security Fabric global object setting.
option
-disable
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
name
Custom tag name.
string
Maximum
length: 35
uuid
Universally Unique Identifier (UUID;
automatically assigned but can be manually
reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
FortiOS 8.0.0 CLI Reference
513
Fortinet Inc.

---


<!-- 来源页 515 -->
config firewall dnstranslation
Description: Configure DNS translation.
edit <id>
set dst {ipv4-address}
set netmask {ipv4-netmask}
set src {ipv4-address}
next
end
config firewall dnstranslation
Parameter
Description
Type
Size
Default
dst
IPv4 address or subnet on the external
network to substitute for the resolved
address in DNS query replies. Can be
single IP address or subnet on the
external network, but number of
addresses must equal number of
mapped IP addresses in src.
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
netmask
If src and dst are subnets rather than
single IP addresses, enter the netmask
for both src and dst.
ipv4-netmask
Not Specified
255.255.255.255
src
IPv4 address or subnet on the internal
network to compare with the resolved
address in DNS query replies. If the
resolved address matches, the
resolved address is substituted with
dst.
ipv4-address
Not Specified
0.0.0.0
config firewall global
Global firewall settings.
config firewall global
Description: Global firewall settings.
set banned-ip-persistency [disabled|permanent-only|...]
end
FortiOS 8.0.0 CLI Reference
515
Fortinet Inc.

---


<!-- 来源页 524 -->
Parameter
Description
Type
Size
Default
webfilter-profile-status
Enable/disable web filtering.
option
-disable
Option
Description
enable
Enable web filtering.
disable
Disable web filtering.
config firewall internet-service
Show Internet Service application. Read-only.
config firewall internet-service
Description: Show Internet Service application. Read-only.
edit <id>
set database [isdb|irdb]
set direction [src|dst|...]
set extra-ip-range-number {integer}
set extra-ip6-range-number {integer}
set icon-id {integer}
set ip-number {integer}
set ip-range-number {integer}
set ip6-range-number {integer}
set name {string}
set obsolete {integer}
set singularity {integer}
next
end
config firewall internet-service
Parameter
Description
Type
Size
Default
database
Database name this Internet Service belongs to.
Read-only.
option
-isdb
Option
Description
isdb
Internet Service Database.
irdb
Internet RRR Database.
direction
How this service may be used in a firewall policy
(source, destination or both). Read-only.
option
-both
FortiOS 8.0.0 CLI Reference
524
Fortinet Inc.

<!-- 来源页 525 -->
Parameter
Description
Type
Size
Default
Option
Description
src
As source in the firewall policy.
dst
As destination in the firewall policy.
both
Both directions in the firewall policy.
extra-ip-range-number
Extra number of IPv4 ranges. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
extra-ip6-range-number
Extra number of IPv6 ranges. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
icon-id
Icon ID of Internet Service. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
id
Internet Service ID. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
ip-number
Total number of IPv4 addresses. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
ip-range-number
Number of IPv4 ranges. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
ip6-range-number
Number of IPv6 ranges. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
name
Internet Service name. Read-only.
string
Maximum
length: 63
obsolete
Indicates whether the Internet Service can be
used. Read-only.
integer
Minimum value:
0 Maximum
value: 255
0
singularity
Singular level of the Internet Service. Read-only.
integer
Minimum value:
0 Maximum
value: 65535
0
FortiOS 8.0.0 CLI Reference
525
Fortinet Inc.

---


<!-- 来源页 526 -->
config firewall internet-service-addition
Configure Internet Services Addition.
config firewall internet-service-addition
Description: Configure Internet Services Addition.
edit <id>
set comment {var-string}
config entry
Description: Entries added to the Internet Service addition database.
edit <id>
set addr-mode [ipv4|ipv6]
config port-range
Description: Port ranges in the custom entry.
edit <id>
set end-port {integer}
set start-port {integer}
next
end
set protocol {integer}
next
end
next
end
config firewall internet-service-addition
Parameter
Description
Type
Size
Default
comment
Comment.
var-string
Maximum
length: 255
id
Internet Service ID in the Internet Service
database.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config entry
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
FortiOS 8.0.0 CLI Reference
526
Fortinet Inc.

---


<!-- 来源页 527 -->
Parameter
Description
Type
Size
Default
id
Entry ID(1-255).
integer
Minimum
value: 0
Maximum
value: 255
0
protocol
Integer value for the protocol type as defined by
IANA (0 - 255).
integer
Minimum
value: 0
Maximum
value: 255
0
config port-range
Parameter
Description
Type
Size
Default
end-port
Integer value for ending TCP/UDP/SCTP
destination port in range (0 to 65535).
integer
Minimum value:
0 Maximum
value: 65535
65535
id
Custom entry port range ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
start-port
Integer value for starting TCP/UDP/SCTP
destination port in range (0 to 65535).
integer
Minimum value:
0 Maximum
value: 65535
1
config firewall internet-service-append
Configure additional port mappings for Internet Services.
config firewall internet-service-append
Description: Configure additional port mappings for Internet Services.
set addr-mode [ipv4|ipv6|...]
set append-port {integer}
set match-port {integer}
end
config firewall internet-service-append
Parameter
Description
Type
Size
Default
addr-mode
Address mode (IPv4 or IPv6).
option
-ipv4
FortiOS 8.0.0 CLI Reference
527
Fortinet Inc.

---


<!-- 来源页 528 -->
Parameter
Description
Type
Size
Default
Option
Description
ipv4
IPv4 mode.
ipv6
IPv6 mode.
both
Both IPv4 and IPv6 mode.
append-port
Appending TCP/UDP/SCTP destination port (1 to
65535).
integer
Minimum
value: 0
Maximum
value:
65535
0
match-port
Matching TCP/UDP/SCTP destination port (0 to
65535, 0 means any port).
integer
Minimum
value: 0
Maximum
value:
65535
0
config firewall internet-service-botnet
Show Internet Service botnet. Read-only.
config firewall internet-service-botnet
Description: Show Internet Service botnet. Read-only.
edit <id>
set name {string}
next
end
config firewall internet-service-botnet
Parameter
Description
Type
Size
Default
id
Internet Service Botnet ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
name
Internet Service Botnet name.
string
Maximum
length: 63
config firewall internet-service-custom
Configure custom Internet Services.
FortiOS 8.0.0 CLI Reference
528
Fortinet Inc.

---


<!-- 来源页 528 -->
Parameter
Description
Type
Size
Default
Option
Description
ipv4
IPv4 mode.
ipv6
IPv6 mode.
both
Both IPv4 and IPv6 mode.
append-port
Appending TCP/UDP/SCTP destination port (1 to
65535).
integer
Minimum
value: 0
Maximum
value:
65535
0
match-port
Matching TCP/UDP/SCTP destination port (0 to
65535, 0 means any port).
integer
Minimum
value: 0
Maximum
value:
65535
0
config firewall internet-service-botnet
Show Internet Service botnet. Read-only.
config firewall internet-service-botnet
Description: Show Internet Service botnet. Read-only.
edit <id>
set name {string}
next
end
config firewall internet-service-botnet
Parameter
Description
Type
Size
Default
id
Internet Service Botnet ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
name
Internet Service Botnet name.
string
Maximum
length: 63
config firewall internet-service-custom
Configure custom Internet Services.
FortiOS 8.0.0 CLI Reference
528
Fortinet Inc.

<!-- 来源页 529 -->
config firewall internet-service-custom
Description: Configure custom Internet Services.
edit <name>
set comment {var-string}
config entry
Description: Entries added to the Internet Service database and custom database.
edit <id>
set addr-mode [ipv4|ipv6]
set dst <name1>, <name2>, ...
set dst6 <name1>, <name2>, ...
config port-range
Description: Port ranges in the custom entry.
edit <id>
set end-port {integer}
set start-port {integer}
next
end
set protocol {integer}
next
end
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set reputation {integer}
set uuid {uuid}
next
end
config firewall internet-service-custom
Parameter
Description
Type
Size
Default
comment
Comment.
var-string
Maximum
length: 255
fabric-force-sync *
Enable/disable forced synchronization of
configuration objects from the root
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
FortiOS 8.0.0 CLI Reference
529
Fortinet Inc.

<!-- 来源页 530 -->
Parameter
Description
Type
Size
Default
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
name
Internet Service name.
string
Maximum
length: 63
reputation
Reputation level of the custom Internet
Service.
integer
Minimum value:
0 Maximum
value:
4294967295
3
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
config entry
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
dst <name>
Destination address or address group name.
Select the destination address or address group
object from available options.
string
Maximum
length: 79
dst6 <name>
Destination address6 or address6 group name.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
530
Fortinet Inc.

---


<!-- 来源页 531 -->
Parameter
Description
Type
Size
Default
Select the destination address6 or address group
object from available options.
id
Entry ID(1-255).
integer
Minimum
value: 0
Maximum
value: 255
0
protocol
Integer value for the protocol type as defined by
IANA (0 - 255).
integer
Minimum
value: 0
Maximum
value: 255
0
config port-range
Parameter
Description
Type
Size
Default
end-port
Integer value for ending TCP/UDP/SCTP
destination port in range (0 to 65535).
integer
Minimum value:
0 Maximum
value: 65535
65535
id
Custom entry port range ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
start-port
Integer value for starting TCP/UDP/SCTP
destination port in range (0 to 65535).
integer
Minimum value:
0 Maximum
value: 65535
1
config firewall internet-service-custom-group
Configure custom Internet Service group.
config firewall internet-service-custom-group
Description: Configure custom Internet Service group.
edit <name>
set comment {var-string}
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set member <name1>, <name2>, ...
set uuid {uuid}
next
end
FortiOS 8.0.0 CLI Reference
531
Fortinet Inc.

<!-- 来源页 532 -->
config firewall internet-service-custom-group
Parameter
Description
Type
Size
Default
comment
Comment.
var-string
Maximum
length: 255
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
member
<name>
Custom Internet Service group members.
Group member name.
string
Maximum
length: 79
name
Custom Internet Service group name.
string
Maximum
length: 63
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be manually
reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
FortiOS 8.0.0 CLI Reference
532
Fortinet Inc.

---


<!-- 来源页 533 -->
config firewall internet-service-definition
Configure Internet Service definition.
config firewall internet-service-definition
Description: Configure Internet Service definition.
edit <id>
config entry
Description: Protocol and port information in an Internet Service entry.
edit <seq-num>
set category-id {integer}
set name {string}
config port-range
Description: Port ranges in the definition entry.
edit <id>
set end-port {integer}
set start-port {integer}
next
end
set protocol {integer}
next
end
next
end
config firewall internet-service-definition
Parameter
Description
Type
Size
Default
id
Internet Service application list ID. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config entry
Parameter
Description
Type
Size
Default
category-id
Internet Service category ID. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
name
Internet Service name. Read-only.
string
Maximum
length: 63
FortiOS 8.0.0 CLI Reference
533
Fortinet Inc.

---


<!-- 来源页 534 -->
Parameter
Description
Type
Size
Default
protocol
Integer value for the protocol type as defined by
IANA (0 - 255). Read-only.
integer
Minimum value:
0 Maximum
value: 255
0
seq-num
Entry sequence number.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config port-range
Parameter
Description
Type
Size
Default
end-port
Ending TCP/UDP/SCTP destination port (1 to
65535). Read-only.
integer
Minimum value:
1 Maximum
value: 65535
65535
id
Custom entry port range ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
start-port
Starting TCP/UDP/SCTP destination port (1 to
65535). Read-only.
integer
Minimum value:
1 Maximum
value: 65535
1
config firewall internet-service-extension
Configure Internet Services Extension.
config firewall internet-service-extension
Description: Configure Internet Services Extension.
edit <id>
set comment {var-string}
config disable-entry
Description: Disable entries in the Internet Service database.
edit <id>
set addr-mode [ipv4|ipv6]
config ip-range
Description: IPv4 ranges in the disable entry.
edit <id>
set end-ip {ipv4-address-any}
set start-ip {ipv4-address-any}
next
end
config ip6-range
Description: IPv6 ranges in the disable entry.
edit <id>
FortiOS 8.0.0 CLI Reference
534
Fortinet Inc.

<!-- 来源页 535 -->
set end-ip6 {ipv6-address}
set start-ip6 {ipv6-address}
next
end
config port-range
Description: Port ranges in the disable entry.
edit <id>
set end-port {integer}
set start-port {integer}
next
end
set protocol {integer}
next
end
config entry
Description: Entries added to the Internet Service extension database.
edit <id>
set addr-mode [ipv4|ipv6]
set dst <name1>, <name2>, ...
set dst6 <name1>, <name2>, ...
config port-range
Description: Port ranges in the custom entry.
edit <id>
set end-port {integer}
set start-port {integer}
next
end
set protocol {integer}
next
end
next
end
config firewall internet-service-extension
Parameter
Description
Type
Size
Default
comment
Comment.
var-string
Maximum
length: 255
id
Internet Service ID in the Internet Service
database.
integer
Minimum value:
0 Maximum
value:
4294967295
0
FortiOS 8.0.0 CLI Reference
535
Fortinet Inc.

<!-- 来源页 536 -->
config disable-entry
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
id
Disable entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
protocol
Integer value for the protocol type as defined by
IANA (0 - 255).
integer
Minimum value:
0 Maximum
value: 255
0
config ip-range
Parameter
Description
Type
Size
Default
end-ip
End IPv4 address.
ipv4-address-any
Not Specified
0.0.0.0
id
Disable entry range ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
start-ip
Start IPv4 address.
ipv4-address-any
Not Specified
0.0.0.0
config ip6-range
Parameter
Description
Type
Size
Default
end-ip6
End IPv6 address.
ipv6-address
Not Specified
::
id
Disable entry range ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
start-ip6
Start IPv6 address.
ipv6-address
Not Specified
::
FortiOS 8.0.0 CLI Reference
536
Fortinet Inc.

<!-- 来源页 537 -->
config port-range
Parameter
Description
Type
Size
Default
end-port
Ending TCP/UDP/SCTP destination port (0 to
65535).
integer
Minimum value:
0 Maximum
value: 65535
65535
id
Custom entry port range ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
start-port
Starting TCP/UDP/SCTP destination port (0 to
65535).
integer
Minimum value:
0 Maximum
value: 65535
1
config entry
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
dst <name>
Destination address or address group name.
Select the destination address or address group
object from available options.
string
Maximum
length: 79
dst6 <name>
Destination address6 or address6 group name.
Select the destination address6 or address group
object from available options.
string
Maximum
length: 79
id
Entry ID(1-255).
integer
Minimum
value: 0
Maximum
value: 255
0
protocol
Integer value for the protocol type as defined by
IANA (0 - 255).
integer
Minimum
value: 0
Maximum
value: 255
0
FortiOS 8.0.0 CLI Reference
537
Fortinet Inc.

---


<!-- 来源页 538 -->
config port-range
Parameter
Description
Type
Size
Default
end-port
Integer value for ending TCP/UDP/SCTP
destination port in range (0 to 65535).
integer
Minimum value:
0 Maximum
value: 65535
65535
id
Custom entry port range ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
start-port
Integer value for starting TCP/UDP/SCTP
destination port in range (0 to 65535).
integer
Minimum value:
0 Maximum
value: 65535
1
config firewall internet-service-fortiguard
Configure FortiGuard Internet Services.
config firewall internet-service-fortiguard
Description: Configure FortiGuard Internet Services.
edit <name>
set comment {var-string}
config entry
Description: Entries added to the Internet Service FortiGuard database.
edit <id>
set addr-mode [ipv4|ipv6]
set dst <name1>, <name2>, ...
set dst6 <name1>, <name2>, ...
config port-range
Description: Port ranges in the custom entry.
edit <id>
set end-port {integer}
set start-port {integer}
next
end
set protocol {integer}
next
end
next
end
FortiOS 8.0.0 CLI Reference
538
Fortinet Inc.

<!-- 来源页 539 -->
config firewall internet-service-fortiguard
Parameter
Description
Type
Size
Default
comment
Comment.
var-string
Maximum
length: 255
name
Internet Service name.
string
Maximum
length: 63
config entry
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
dst <name>
Destination address or address group name.
Select the destination address or address group
object from available options.
string
Maximum
length: 79
dst6 <name>
Destination address6 or address6 group name.
Select the destination address6 or address group
object from available options.
string
Maximum
length: 79
id
Entry ID(1-255).
integer
Minimum
value: 0
Maximum
value: 255
0
protocol
Integer value for the protocol type as defined by
IANA (0 - 255).
integer
Minimum
value: 0
Maximum
value: 255
0
config port-range
Parameter
Description
Type
Size
Default
end-port
Integer value for ending TCP/UDP/SCTP
destination port in range (0 to 65535).
integer
Minimum value:
0 Maximum
value: 65535
65535
FortiOS 8.0.0 CLI Reference
539
Fortinet Inc.

---


<!-- 来源页 540 -->
Parameter
Description
Type
Size
Default
id
Custom entry port range ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
start-port
Integer value for starting TCP/UDP/SCTP
destination port in range (0 to 65535).
integer
Minimum value:
0 Maximum
value: 65535
1
config firewall internet-service-group
Configure group of Internet Service.
config firewall internet-service-group
Description: Configure group of Internet Service.
edit <name>
set comment {var-string}
set direction [source|destination|...]
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set member <name1>, <name2>, ...
set uuid {uuid}
next
end
config firewall internet-service-group
Parameter
Description
Type
Size
Default
comment
Comment.
var-string
Maximum
length: 255
direction
How this service may be used (source,
destination or both).
option
-both
Option
Description
source
As source when applied.
destination
As destination when applied.
both
Both directions when applied.
FortiOS 8.0.0 CLI Reference
540
Fortinet Inc.

---


<!-- 来源页 541 -->
Parameter
Description
Type
Size
Default
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
member
<name>
Internet Service group member.
Internet Service name.
string
Maximum
length: 79
name
Internet Service group name.
string
Maximum
length: 63
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be manually
reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
config firewall internet-service-ipbl-reason
IP block list reason. Read-only.
FortiOS 8.0.0 CLI Reference
541
Fortinet Inc.

---


<!-- 来源页 542 -->
config firewall internet-service-ipbl-reason
Description: IP block list reason. Read-only.
edit <id>
set name {string}
next
end
config firewall internet-service-ipbl-reason
Parameter
Description
Type
Size
Default
id
IP block list reason ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
name
IP block list reason name.
string
Maximum
length: 63
config firewall internet-service-ipbl-vendor
IP block list vendor. Read-only.
config firewall internet-service-ipbl-vendor
Description: IP block list vendor. Read-only.
edit <id>
set name {string}
next
end
config firewall internet-service-ipbl-vendor
Parameter
Description
Type
Size
Default
id
IP block list vendor ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
name
IP block list vendor name.
string
Maximum
length: 63
config firewall internet-service-list
Internet Service list. Read-only.
FortiOS 8.0.0 CLI Reference
542
Fortinet Inc.

---


<!-- 来源页 542 -->
config firewall internet-service-ipbl-reason
Description: IP block list reason. Read-only.
edit <id>
set name {string}
next
end
config firewall internet-service-ipbl-reason
Parameter
Description
Type
Size
Default
id
IP block list reason ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
name
IP block list reason name.
string
Maximum
length: 63
config firewall internet-service-ipbl-vendor
IP block list vendor. Read-only.
config firewall internet-service-ipbl-vendor
Description: IP block list vendor. Read-only.
edit <id>
set name {string}
next
end
config firewall internet-service-ipbl-vendor
Parameter
Description
Type
Size
Default
id
IP block list vendor ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
name
IP block list vendor name.
string
Maximum
length: 63
config firewall internet-service-list
Internet Service list. Read-only.
FortiOS 8.0.0 CLI Reference
542
Fortinet Inc.

---


<!-- 来源页 543 -->
config firewall internet-service-list
Description: Internet Service list. Read-only.
edit <id>
set name {string}
next
end
config firewall internet-service-list
Parameter
Description
Type
Size
Default
id
Internet Service category ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
name
Internet Service category name.
string
Maximum
length: 63
config firewall internet-service-name
Define internet service names.
config firewall internet-service-name
Description: Define internet service names.
edit <name>
set city-id {integer}
set country-id {integer}
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set internet-service-id {integer}
set region-id {integer}
set type [default|location]
set uuid {uuid}
next
end
config firewall internet-service-name
Parameter
Description
Type
Size
Default
city-id
City ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
FortiOS 8.0.0 CLI Reference
543
Fortinet Inc.

<!-- 来源页 544 -->
Parameter
Description
Type
Size
Default
country-id
Country or Area ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
fabric-force-sync *
Enable/disable forced synchronization of
configuration objects from the root
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
internet-service-id
Internet Service ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
name
Internet Service name.
string
Maximum
length: 63
region-id
Region ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
FortiOS 8.0.0 CLI Reference
544
Fortinet Inc.

---


<!-- 来源页 545 -->
Parameter
Description
Type
Size
Default
type
Internet Service name type.
option
-default
Option
Description
default
Automatically generated Internet Service.
location
Geography location based Internet Service.
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
config firewall internet-service-owner
Internet Service owner. Read-only.
config firewall internet-service-owner
Description: Internet Service owner. Read-only.
edit <id>
set name {string}
next
end
config firewall internet-service-owner
Parameter
Description
Type
Size
Default
id
Internet Service owner ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
name
Internet Service owner name.
string
Maximum
length: 63
config firewall internet-service-reputation
Show Internet Service reputation. Read-only.
config firewall internet-service-reputation
Description: Show Internet Service reputation. Read-only.
edit <id>
set description {string}
FortiOS 8.0.0 CLI Reference
545
Fortinet Inc.

---


<!-- 来源页 545 -->
Parameter
Description
Type
Size
Default
type
Internet Service name type.
option
-default
Option
Description
default
Automatically generated Internet Service.
location
Geography location based Internet Service.
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
config firewall internet-service-owner
Internet Service owner. Read-only.
config firewall internet-service-owner
Description: Internet Service owner. Read-only.
edit <id>
set name {string}
next
end
config firewall internet-service-owner
Parameter
Description
Type
Size
Default
id
Internet Service owner ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
name
Internet Service owner name.
string
Maximum
length: 63
config firewall internet-service-reputation
Show Internet Service reputation. Read-only.
config firewall internet-service-reputation
Description: Show Internet Service reputation. Read-only.
edit <id>
set description {string}
FortiOS 8.0.0 CLI Reference
545
Fortinet Inc.

<!-- 来源页 546 -->
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set uuid {uuid}
next
end
config firewall internet-service-reputation
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
fabric-force-sync *
Enable/disable forced synchronization of
configuration objects from the root
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
FortiOS 8.0.0 CLI Reference
546
Fortinet Inc.

---


<!-- 来源页 547 -->
Parameter
Description
Type
Size
Default
id
Internet Service Reputation ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
config firewall internet-service-sld
Internet Service Second Level Domain. Read-only.
config firewall internet-service-sld
Description: Internet Service Second Level Domain. Read-only.
edit <id>
set name {string}
next
end
config firewall internet-service-sld
Parameter
Description
Type
Size
Default
id
Second Level Domain ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
name
Second Level Domain name.
string
Maximum
length: 63
config firewall internet-service-subapp
Show Internet Service sub app ID. Read-only.
config firewall internet-service-subapp
Description: Show Internet Service sub app ID. Read-only.
edit <id>
set sub-app <id1>, <id2>, ...
next
end
FortiOS 8.0.0 CLI Reference
547
Fortinet Inc.

---


<!-- 来源页 547 -->
Parameter
Description
Type
Size
Default
id
Internet Service Reputation ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
config firewall internet-service-sld
Internet Service Second Level Domain. Read-only.
config firewall internet-service-sld
Description: Internet Service Second Level Domain. Read-only.
edit <id>
set name {string}
next
end
config firewall internet-service-sld
Parameter
Description
Type
Size
Default
id
Second Level Domain ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
name
Second Level Domain name.
string
Maximum
length: 63
config firewall internet-service-subapp
Show Internet Service sub app ID. Read-only.
config firewall internet-service-subapp
Description: Show Internet Service sub app ID. Read-only.
edit <id>
set sub-app <id1>, <id2>, ...
next
end
FortiOS 8.0.0 CLI Reference
547
Fortinet Inc.

---


<!-- 来源页 583 -->
config firewall policy
Configure IPv4/IPv6 policies.
config firewall policy
Description: Configure IPv4/IPv6 policies.
edit <policyid>
set action [accept|deny|...]
set anti-replay [enable|disable]
set app-monitor [enable|disable]
set application-list {string}
set auth-cert {string}
set auth-path [enable|disable]
set auth-redirect-addr {string}
set auto-asic-offload [enable|disable]
set av-profile {string}
set block-notification [enable|disable]
set captive-portal-exempt [enable|disable]
set capture-packet [enable|disable]
set casb-profile {string}
set comments {var-string}
set custom-log-fields <field-id1>, <field-id2>, ...
set custom-tags <name1>, <name2>, ...
set decrypted-traffic-mirror {string}
set delay-tcp-npu-session [enable|disable]
set diameter-filter-profile {string}
set diffserv-copy [enable|disable]
set diffserv-forward [enable|disable]
set diffserv-reverse [enable|disable]
set diffservcode-forward {user}
set diffservcode-rev {user}
set disclaimer [enable|disable]
set dlp-profile {string}
set dnsfilter-profile {string}
set dsri [enable|disable]
set dstaddr <name1>, <name2>, ...
set dstaddr-negate [enable|disable]
set dstaddr6 <name1>, <name2>, ...
set dstaddr6-negate [enable|disable]
set dstintf <name1>, <name2>, ...
set dynamic-shaping [enable|disable]
set email-collect [enable|disable]
set emailfilter-profile {string}
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
config fabric-policy
Description: Fabric policy related attributes.
set from {string}
set to {string}
end
FortiOS 8.0.0 CLI Reference
583
Fortinet Inc.

<!-- 来源页 584 -->
set fec [enable|disable]
set file-filter-profile {string}
set firewall-session-dirty [check-all|check-new]
set fixedport [enable|disable]
set fsso-agent-for-ntlm {string}
set fsso-groups <name1>, <name2>, ...
set geoip-anycast [enable|disable]
set geoip-match [physical-location|registered-location]
set groups <name1>, <name2>, ...
set http-policy-redirect [enable|disable|...]
set icap-profile {string}
set identity-based-route {string}
set inbound [enable|disable]
set inspection-mode [proxy|flow]
set internet-service [enable|disable]
set internet-service-custom <name1>, <name2>, ...
set internet-service-custom-group <name1>, <name2>, ...
set internet-service-fortiguard <name1>, <name2>, ...
set internet-service-group <name1>, <name2>, ...
set internet-service-name <name1>, <name2>, ...
set internet-service-negate [enable|disable]
set internet-service-src [enable|disable]
set internet-service-src-custom <name1>, <name2>, ...
set internet-service-src-custom-group <name1>, <name2>, ...
set internet-service-src-fortiguard <name1>, <name2>, ...
set internet-service-src-group <name1>, <name2>, ...
set internet-service-src-name <name1>, <name2>, ...
set internet-service-src-negate [enable|disable]
set internet-service6 [enable|disable]
set internet-service6-custom <name1>, <name2>, ...
set internet-service6-custom-group <name1>, <name2>, ...
set internet-service6-fortiguard <name1>, <name2>, ...
set internet-service6-group <name1>, <name2>, ...
set internet-service6-name <name1>, <name2>, ...
set internet-service6-negate [enable|disable]
set internet-service6-src [enable|disable]
set internet-service6-src-custom <name1>, <name2>, ...
set internet-service6-src-custom-group <name1>, <name2>, ...
set internet-service6-src-fortiguard <name1>, <name2>, ...
set internet-service6-src-group <name1>, <name2>, ...
set internet-service6-src-name <name1>, <name2>, ...
set internet-service6-src-negate [enable|disable]
set ippool [enable|disable]
set ips-sensor {string}
set ips-voip-filter {string}
set llm-profile {string}
set log-http-transaction [enable|disable]
set logtraffic [all|utm|...]
set logtraffic-start [enable|disable]
set match-vip [enable|disable]
set match-vip-only [enable|disable]
set name {string}
FortiOS 8.0.0 CLI Reference
584
Fortinet Inc.

<!-- 来源页 585 -->
set nat [enable|disable]
set nat46 [enable|disable]
set nat64 [enable|disable]
set natinbound [enable|disable]
set natip {ipv4-classnet}
set natoutbound [enable|disable]
set network-service-dynamic <name1>, <name2>, ...
set network-service-src-dynamic <name1>, <name2>, ...
set np-acceleration [enable|disable]
set ntlm [enable|disable]
set ntlm-enabled-browsers <user-agent-string1>, <user-agent-string2>, ...
set ntlm-guest [enable|disable]
set outbound [enable|disable]
set passive-wan-health-measurement [enable|disable]
set pcp-inbound [enable|disable]
set pcp-outbound [enable|disable]
set pcp-poolname <name1>, <name2>, ...
set per-ip-shaper {string}
set permit-any-host [enable|disable]
set permit-stun-host [enable|disable]
set policy-expiry [enable|disable]
set policy-expiry-date {datetime}
set policy-expiry-date-utc {user}
set poolname <name1>, <name2>, ...
set poolname6 <name1>, <name2>, ...
set port-preserve [enable|disable]
set port-random [enable|disable]
set profile-group {string}
set profile-protocol-options {string}
set profile-type [single|group]
set radius-ip-auth-bypass [enable|disable]
set radius-mac-auth-bypass [enable|disable]
set redirect-url {var-string}
set replacemsg-override-group {string}
set reputation-direction [source|destination]
set reputation-direction6 [source|destination]
set reputation-minimum {integer}
set reputation-minimum6 {integer}
set rtp-addr <name1>, <name2>, ...
set rtp-nat [disable|enable]
set schedule {string}
set schedule-timeout [enable|disable]
set sctp-filter-profile {string}
set send-deny-packet [disable|enable]
set service <name1>, <name2>, ...
set service-negate [enable|disable]
set session-ttl {user}
set sgt <id1>, <id2>, ...
set sgt-check [enable|disable]
set skip-vrf-match [enable|disable]
set src-vendor-mac <id1>, <id2>, ...
set srcaddr <name1>, <name2>, ...
FortiOS 8.0.0 CLI Reference
585
Fortinet Inc.

<!-- 来源页 586 -->
set srcaddr-negate [enable|disable]
set srcaddr6 <name1>, <name2>, ...
set srcaddr6-negate [enable|disable]
set srcintf <name1>, <name2>, ...
set ssh-filter-profile {string}
set ssh-policy-redirect [enable|disable]
set ssl-ssh-profile {string}
set status [enable|disable]
set tcp-mss-receiver {integer}
set tcp-mss-sender {integer}
set tcp-session-without-syn [all|data-only|...]
set telemetry-profile {string}
set timeout-send-rst [enable|disable]
set tos {user}
set tos-mask {user}
set tos-negate [enable|disable]
set traffic-shaper {string}
set traffic-shaper-reverse {string}
set users <name1>, <name2>, ...
set utm-status [enable|disable]
set uuid {uuid}
set videofilter-profile {string}
set virtual-patch-profile {string}
set vlan-cos-fwd {integer}
set vlan-cos-rev {integer}
set vlan-filter {user}
set voip-profile {string}
set vpntunnel {string}
set waf-profile {string}
set wanopt [enable|disable]
set wanopt-detection [active|passive|...]
set wanopt-passive-opt [default|transparent|...]
set wanopt-peer {string}
set wanopt-profile {string}
set wccp [enable|disable]
set webcache [enable|disable]
set webcache-https [disable|enable]
set webfilter-profile {string}
set webproxy-forward-server {string}
set webproxy-profile {string}
set ztna-destination <name1>, <name2>, ...
set ztna-device-ownership [enable|disable]
set ztna-ems-tag <name1>, <name2>, ...
set ztna-ems-tag-negate [enable|disable]
set ztna-ems-tag-secondary <name1>, <name2>, ...
set ztna-ems-tag6 <name1>, <name2>, ...
set ztna-geo-tag <name1>, <name2>, ...
set ztna-policy-redirect [enable|disable]
set ztna-status [enable|disable]
set ztna-tags-match-logic [or|and]
next
end
FortiOS 8.0.0 CLI Reference
586
Fortinet Inc.

<!-- 来源页 587 -->
config firewall policy
Parameter
Description
Type
Size
Default
action
Policy action (accept/deny/ipsec).
option
-deny
Option
Description
accept
Allows session that match the firewall policy.
deny
Blocks sessions that match the firewall policy.
ipsec
Firewall policy becomes a policy-based IPsec VPN policy.
anti-replay
Enable/disable anti-replay check.
option
-enable
Option
Description
enable
Enable anti-replay check.
disable
Disable anti-replay check.
app-monitor
Enable/disable application TCP
metrics in session logs.When enabled,
auto-asic-offload is disabled.
option
-disable
Option
Description
enable
Enable TCP metrics in session logs.
disable
Disable TCP metrics in session logs.
application-list
Name of an existing Application list.
string
Maximum
length: 47
auth-cert
HTTPS server certificate for policy
authentication.
string
Maximum
length: 35
auth-path
Enable/disable authentication-based
routing.
option
-disable
Option
Description
enable
Enable authentication-based routing.
disable
Disable authentication-based routing.
auth-redirect-addr
HTTP-to-HTTPS redirect address for
firewall authentication.
string
Maximum
length: 63
auto-asic-offload
Enable/disable policy traffic ASIC
offloading.
option
-enable
FortiOS 8.0.0 CLI Reference
587
Fortinet Inc.

<!-- 来源页 588 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable auto ASIC offloading.
disable
Disable ASIC offloading.
av-profile
Name of an existing Antivirus profile.
string
Maximum
length: 47
block-notification
Enable/disable block notification.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
captive-portal-exempt
Enable to exempt some users from the
captive portal.
option
-disable
Option
Description
enable
Enable exemption of captive portal.
disable
Disable exemption of captive portal.
capture-packet
*
Enable/disable capture packets.
option
-disable
Option
Description
enable
Enable capture packets.
disable
Disable capture packets.
casb-profile *
Name of an existing CASB profile.
string
Maximum
length: 47
comments
Comment.
var-string
Maximum
length: 1023
custom-log-fields <field-id>
Custom fields to append to log
messages for this policy.
Custom log field.
string
Maximum
length: 35
custom-tags
<name> *
Custom tags.
Names of custom tags used with this
policy.
string
Maximum
length: 35
decrypted-traffic-mirror
Decrypted traffic mirror.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
588
Fortinet Inc.

<!-- 来源页 589 -->
Parameter
Description
Type
Size
Default
delay-tcp-npu-session
Enable TCP NPU session delay to
guarantee packet order of 3-way
handshake.
option
-disable
Option
Description
enable
Enable TCP NPU session delay in order to guarantee packet order of
3-way handshake.
disable
Disable TCP NPU session delay in order to guarantee packet order of
3-way handshake.
diameter-filter-profile
Name of an existing Diameter filter
profile.
string
Maximum
length: 47
diffserv-copy
Enable to copy packet's DiffServ
values from session's original
direction to its reply direction.
option
-disable
Option
Description
enable
Enable DSCP copy.
disable
Disable DSCP copy.
diffserv-forward
Enable to change packet's DiffServ
values to the specified diffservcode-forward value.
option
-disable
Option
Description
enable
Enable setting forward (original) traffic Diffserv.
disable
Disable setting forward (original) traffic Diffserv.
diffserv-reverse
Enable to change packet's reverse
(reply) DiffServ values to the specified
diffservcode-rev value.
option
-disable
Option
Description
enable
Enable setting reverse (reply) traffic DiffServ.
disable
Disable setting reverse (reply) traffic DiffServ.
diffservcode-forward
Change packet's DiffServ to this
value.
user
Not Specified
diffservcode-rev
Change packet's reverse (reply)
DiffServ to this value.
user
Not Specified
FortiOS 8.0.0 CLI Reference
589
Fortinet Inc.

<!-- 来源页 590 -->
Parameter
Description
Type
Size
Default
disclaimer
Enable/disable user authentication
disclaimer.
option
-disable
Option
Description
enable
Enable user authentication disclaimer.
disable
Disable user authentication disclaimer.
dlp-profile
Name of an existing DLP profile.
string
Maximum
length: 47
dnsfilter-profile
Name of an existing DNS filter profile.
string
Maximum
length: 47
dsri
Enable DSRI to ignore HTTP server
responses.
option
-disable
Option
Description
enable
Enable DSRI.
disable
Disable DSRI.
dstaddr <name>
Destination IPv4 address and address
group names.
Address name.
string
Maximum
length: 79
dstaddr-negate
When enabled dstaddr specifies what
the destination address must NOT be.
option
-disable
Option
Description
enable
Enable destination address negate.
disable
Disable destination address negate.
dstaddr6
<name>
Destination IPv6 address name and
address group names.
Address name.
string
Maximum
length: 79
dstaddr6-negate
When enabled dstaddr6 specifies
what the destination address must
NOT be.
option
-disable
Option
Description
enable
Enable IPv6 destination address negate.
disable
Disable IPv6 destination address negate.
dstintf <name>
Outgoing (egress) interface.
Interface name.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
590
Fortinet Inc.

<!-- 来源页 591 -->
Parameter
Description
Type
Size
Default
dynamic-shaping
Enable/disable dynamic RADIUS
defined traffic shaping.
option
-disable
Option
Description
enable
Enable dynamic RADIUS defined traffic shaping.
disable
Disable dynamic RADIUS defined traffic shaping.
email-collect
Enable/disable email collection.
option
-disable
Option
Description
enable
Enable email collection.
disable
Disable email collection.
emailfilter-profile
Name of an existing email filter profile.
string
Maximum
length: 47
fabric-force-sync *
Enable/disable forced synchronization
of configuration objects from the root
FortiGate unit to the downstream
devices. Configuration conflict check
is skipped.
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
fabric-object *
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
FortiOS 8.0.0 CLI Reference
591
Fortinet Inc.

<!-- 来源页 592 -->
Parameter
Description
Type
Size
Default
fec
Enable/disable Forward Error
Correction on traffic matching this
policy on a FEC device.
option
-disable
Option
Description
enable
Enable Forward Error Correction.
disable
Disable Forward Error Correction.
file-filter-profile
Name of an existing file-filter profile.
string
Maximum
length: 47
firewall-session-dirty
How to handle sessions if the
configuration of this firewall policy
changes.
option
-check-all
Option
Description
check-all
Flush all current sessions accepted by this policy. These sessions
must be started and re-matched with policies.
check-new
Continue to allow sessions already accepted by this policy.
fixedport
Enable to prevent source NAT from
changing a session's source port.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
fsso-agent-for-ntlm
FSSO agent to use for NTLM
authentication.
string
Maximum
length: 35
fsso-groups
<name>
Names of FSSO groups.
Names of FSSO groups.
string
Maximum
length: 511
geoip-anycast
Enable/disable recognition of anycast
IP addresses using the geography IP
database.
option
-disable
Option
Description
enable
Enable recognition of anycast IP addresses using the geography IP
database.
disable
Disable recognition of anycast IP addresses using the geography IP
database.
FortiOS 8.0.0 CLI Reference
592
Fortinet Inc.

<!-- 来源页 593 -->
Parameter
Description
Type
Size
Default
geoip-match
Match geography address based
either on its physical location or
registered location.
option
-physical-location
Option
Description
physical-location
Match geography address to its physical location using the geography
IP database.
registered-location
Match geography address to its registered location using the
geography IP database.
groups <name>
Names of user groups that can
authenticate with this policy.
Group name.
string
Maximum
length: 79
http-policy-redirect
Redirect HTTP(S) traffic to matching
transparent web proxy policy.
option
-disable
Option
Description
enable
Enable HTTP(S) policy redirect.
disable
Disable HTTP(S) policy redirect.
legacy
Enable HTTP(S) policy redirect (for preserving old behavior, not
recommended for new setups).
icap-profile *
Name of an existing ICAP profile.
string
Maximum
length: 47
identity-based-route
Name of identity-based routing rule.
string
Maximum
length: 35
inbound
Policy-based IPsec VPN: only traffic
from the remote network can initiate a
VPN.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
inspection-mode
Policy inspection mode (Flow/proxy).
Default is Flow mode.
option
-flow
Option
Description
proxy
Proxy based inspection.
flow
Flow based inspection.
FortiOS 8.0.0 CLI Reference
593
Fortinet Inc.

<!-- 来源页 594 -->
Parameter
Description
Type
Size
Default
internet-service
Enable/disable use of Internet
Services for this policy. If enabled,
destination address and service are
not used.
option
-disable
Option
Description
enable
Enable use of Internet Services in policy.
disable
Disable use of Internet Services in policy.
internet-service-custom
<name>
Custom Internet Service name.
Custom Internet Service name.
string
Maximum
length: 79
internet-service-custom-group
<name>
Custom Internet Service group name.
Custom Internet Service group name.
string
Maximum
length: 79
internet-service-fortiguard
<name>
FortiGuard Internet Service name.
FortiGuard Internet Service name.
string
Maximum
length: 79
internet-service-group
<name>
Internet Service group name.
Internet Service group name.
string
Maximum
length: 79
internet-service-name
<name>
Internet Service name.
Internet Service name.
string
Maximum
length: 79
internet-service-negate
When enabled internet-service
specifies what the service must NOT
be.
option
-disable
Option
Description
enable
Enable negated Internet Service match.
disable
Disable negated Internet Service match.
internet-service-src
Enable/disable use of Internet
Services in source for this policy. If
enabled, source address is not used.
option
-disable
Option
Description
enable
Enable use of Internet Services source in policy.
disable
Disable use of Internet Services source in policy.
FortiOS 8.0.0 CLI Reference
594
Fortinet Inc.

<!-- 来源页 595 -->
Parameter
Description
Type
Size
Default
internet-service-src-custom <name>
Custom Internet Service source name.
Custom Internet Service name.
string
Maximum
length: 79
internet-service-src-custom-group
<name>
Custom Internet Service source group
name.
Custom Internet Service group name.
string
Maximum
length: 79
internet-service-src-fortiguard
<name>
FortiGuard Internet Service source
name.
FortiGuard Internet Service name.
string
Maximum
length: 79
internet-service-src-group <name>
Internet Service source group name.
Internet Service group name.
string
Maximum
length: 79
internet-service-src-name <name>
Internet Service source name.
Internet Service name.
string
Maximum
length: 79
internet-service-src-negate
When enabled internet-service-src
specifies what the service must NOT
be.
option
-disable
Option
Description
enable
Enable negated Internet Service source match.
disable
Disable negated Internet Service source match.
internet-service6
Enable/disable use of IPv6 Internet
Services for this policy. If enabled,
destination address and service are
not used.
option
-disable
Option
Description
enable
Enable use of IPv6 Internet Services in policy.
disable
Disable use of IPv6 Internet Services in policy.
internet-service6-custom <name>
Custom IPv6 Internet Service name.
Custom Internet Service name.
string
Maximum
length: 79
internet-service6-custom-group
<name>
Custom Internet Service6 group
name.
Custom Internet Service6 group
name.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
595
Fortinet Inc.

<!-- 来源页 596 -->
Parameter
Description
Type
Size
Default
internet-service6-fortiguard
<name>
FortiGuard IPv6 Internet Service
name.
FortiGuard Internet Service name.
string
Maximum
length: 79
internet-service6-group
<name>
Internet Service group name.
Internet Service group name.
string
Maximum
length: 79
internet-service6-name
<name>
IPv6 Internet Service name.
IPv6 Internet Service name.
string
Maximum
length: 79
internet-service6-negate
When enabled internet-service6
specifies what the service must NOT
be.
option
-disable
Option
Description
enable
Enable negated IPv6 Internet Service match.
disable
Disable negated IPv6 Internet Service match.
internet-service6-src
Enable/disable use of IPv6 Internet
Services in source for this policy. If
enabled, source address is not used.
option
-disable
Option
Description
enable
Enable use of IPv6 Internet Services source in policy.
disable
Disable use of IPv6 Internet Services source in policy.
internet-service6-src-custom <name>
Custom IPv6 Internet Service source
name.
Custom Internet Service name.
string
Maximum
length: 79
internet-service6-src-custom-group
<name>
Custom Internet Service6 source
group name.
Custom Internet Service6 group
name.
string
Maximum
length: 79
internet-service6-src-fortiguard
<name>
FortiGuard IPv6 Internet Service
source name.
FortiGuard Internet Service name.
string
Maximum
length: 79
internet-service6-src-group <name>
Internet Service6 source group name.
Internet Service group name.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
596
Fortinet Inc.

<!-- 来源页 597 -->
Parameter
Description
Type
Size
Default
internet-service6-src-name <name>
IPv6 Internet Service source name.
Internet Service name.
string
Maximum
length: 79
internet-service6-src-negate
When enabled internet-service6-src
specifies what the service must NOT
be.
option
-disable
Option
Description
enable
Enable negated IPv6 Internet Service source match.
disable
Disable negated IPv6 Internet Service source match.
ippool
Enable to use IP Pools for source NAT.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
ips-sensor
Name of an existing IPS sensor.
string
Maximum
length: 47
ips-voip-filter
Name of an existing VoIP (ips) profile.
string
Maximum
length: 47
llm-profile *
Name of an existing LLM profile.
string
Maximum
length: 47
log-http-transaction
Enable/disable HTTP transaction log.
option
-disable
Option
Description
enable
Enable HTTP transaction log.
disable
Disable HTTP transaction log.
logtraffic
Enable or disable logging. Log all
sessions or security profile sessions.
option
-utm
Option
Description
all
Log all sessions accepted or denied by this policy.
utm
Log traffic that has a security profile applied to it.
disable
Disable all logging for this policy.
logtraffic-start
Record logs when a session starts.
option
-disable
FortiOS 8.0.0 CLI Reference
597
Fortinet Inc.

<!-- 来源页 598 -->
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
match-vip
Enable to match packets that have
had their destination addresses
changed by a VIP.
option
-enable
Option
Description
enable
Match DNATed packet.
disable
Do not match DNATed packet.
match-vip-only
Enable/disable matching of only those
packets that have had their
destination addresses changed by a
VIP.
option
-disable
Option
Description
enable
Enable matching of only those packets that have had their destination
addresses changed by a VIP.
disable
Disable matching of only those packets that have had their destination
addresses changed by a VIP.
name
Policy name.
string
Maximum
length: 35
nat
Enable/disable source NAT.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
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
598
Fortinet Inc.

<!-- 来源页 599 -->
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
natinbound
Policy-based IPsec VPN: apply
destination NAT to inbound traffic.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
natip
Policy-based IPsec VPN: source NAT
IP address for outgoing traffic.
ipv4-classnet
Not Specified
0.0.0.0 0.0.0.0
natoutbound
Policy-based IPsec VPN: apply source
NAT to outbound traffic.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
network-service-dynamic <name>
Dynamic Network Service name.
Dynamic Network Service name.
string
Maximum
length: 79
network-service-src-dynamic <name>
Dynamic Network Service source
name.
Dynamic Network Service name.
string
Maximum
length: 79
np-acceleration
*
Enable/disable UTM Network
Processor acceleration.
option
-enable
Option
Description
enable
Enable UTM Network Processor acceleration.
disable
Disable UTM Network Processor acceleration.
ntlm
Enable/disable NTLM authentication.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
599
Fortinet Inc.

<!-- 来源页 600 -->
Parameter
Description
Type
Size
Default
ntlm-enabled-browsers
<user-agent-string>
HTTP-User-Agent value of supported
browsers.
User agent string.
string
Maximum
length: 79
ntlm-guest
Enable/disable NTLM guest user
access.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
outbound
Policy-based IPsec VPN: only traffic
from the internal network can initiate a
VPN.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
passive-wan-health-measurement
Enable/disable passive WAN health
measurement. When enabled, auto-asic-offload is disabled.
option
-disable
Option
Description
enable
Enable Passive WAN health measurement.
disable
Disable Passive WAN health measurement.
pcp-inbound
Enable/disable PCP inbound DNAT.
option
-disable
Option
Description
enable
Enable PCP inbound DNAT.
disable
Disable PCP inbound DNAT.
pcp-outbound
Enable/disable PCP outbound SNAT.
option
-disable
Option
Description
enable
Enable PCP outbound SNAT.
disable
Disable PCP outbound SNAT.
pcp-poolname
<name>
PCP pool names.
PCP pool name.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
600
Fortinet Inc.

<!-- 来源页 601 -->
Parameter
Description
Type
Size
Default
per-ip-shaper
Per-IP traffic shaper.
string
Maximum
length: 35
permit-any-host
Enable/disable fullcone NAT. Accept
UDP packets from any host.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
permit-stun-host
Accept UDP packets from any Session
Traversal Utilities for NAT (STUN)
host.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
policy-expiry
Enable/disable policy expiry.
option
-disable
Option
Description
enable
Enable policy expiry.
disable
Disable polcy expiry.
policy-expiry-date
Policy expiry date (YYYY-MM-DD
HH:MM:SS).
datetime
Not Specified
0000-00-00
00:00:00
policy-expiry-date-utc
Policy expiry date and time, in epoch
format.
user
Not Specified
policyid
Policy ID (0 - 4294967294).
integer
Minimum value:
0 Maximum
value:
4294967294
0
poolname
<name>
IP Pool names.
IP pool name.
string
Maximum
length: 79
poolname6
<name>
IPv6 pool names.
IPv6 pool name.
string
Maximum
length: 79
port-preserve
Enable/disable preservation of the
original source port from source NAT
if it has not been used.
option
-enable
FortiOS 8.0.0 CLI Reference
601
Fortinet Inc.

<!-- 来源页 602 -->
Parameter
Description
Type
Size
Default
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
profile-group
Name of profile group.
string
Maximum
length: 47
profile-protocol-options
Name of an existing Protocol options
profile.
string
Maximum
length: 47
default
profile-type
Determine whether the firewall policy
allows security profile groups or single
profiles only.
option
-single
Option
Description
single
Do not allow security profile groups.
group
Allow security profile groups.
radius-ip-auth-bypass
Enable IP authentication bypass. The
bypassed IP address must be
received from RADIUS server.
option
-disable
Option
Description
enable
Enable IP authentication bypass.
disable
Disable IP authentication bypass.
radius-mac-auth-bypass
Enable MAC authentication bypass.
The bypassed MAC address must be
received from RADIUS server.
option
-disable
Option
Description
enable
Enable MAC authentication bypass.
disable
Disable MAC authentication bypass.
FortiOS 8.0.0 CLI Reference
602
Fortinet Inc.

<!-- 来源页 603 -->
Parameter
Description
Type
Size
Default
redirect-url
URL users are directed to after seeing
and accepting the disclaimer or
authenticating.
var-string
Maximum
length: 1023
replacemsg-override-group
Override the default replacement
message group for this policy.
string
Maximum
length: 35
reputation-direction
Direction of the initial traffic for
reputation to take effect.
option
-destination
Option
Description
source
Check reputation for source address.
destination
Check reputation for destination address.
reputation-direction6
Direction of the initial traffic for IPv6
reputation to take effect.
option
-destination
Option
Description
source
Check reputation for IPv6 source address.
destination
Check reputation for IPv6 destination address.
reputation-minimum
Minimum Reputation to take action.
integer
Minimum value:
0 Maximum
value:
4294967295
0
reputation-minimum6
IPv6 Minimum Reputation to take
action.
integer
Minimum value:
0 Maximum
value:
4294967295
0
rtp-addr <name>
Address names if this is an RTP NAT
policy.
Address name.
string
Maximum
length: 79
rtp-nat
Enable Real Time Protocol (RTP) NAT.
option
-disable
Option
Description
disable
Disable setting.
enable
Enable setting.
schedule
Schedule name.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
603
Fortinet Inc.

<!-- 来源页 604 -->
Parameter
Description
Type
Size
Default
schedule-timeout
Enable to force current sessions to
end when the schedule object times
out. Disable allows them to end from
inactivity.
option
-disable
Option
Description
enable
Enable schedule timeout.
disable
Disable schedule timeout.
sctp-filter-profile
Name of an existing SCTP filter
profile.
string
Maximum
length: 47
send-deny-packet
Enable to send a reply when a session
is denied or blocked by a firewall
policy.
option
-disable
Option
Description
disable
Disable deny-packet sending.
enable
Enable deny-packet sending.
service <name>
Service and service group names.
Service and service group names.
string
Maximum
length: 79
service-negate
When enabled service specifies what
the service must NOT be.
option
-disable
Option
Description
enable
Enable negated service match.
disable
Disable negated service match.
session-ttl
TTL in seconds for sessions accepted
by this policy (0 means use the
system default session TTL).
user
Not Specified
sgt <id>
Security group tags.
Security group tag (1 - 65535).
integer
Minimum value:
1 Maximum
value: 65535
sgt-check
Enable/disable security group tags
(SGT) check.
option
-disable
Option
Description
enable
Enable SGT check.
disable
Disable SGT check.
FortiOS 8.0.0 CLI Reference
604
Fortinet Inc.

<!-- 来源页 605 -->
Parameter
Description
Type
Size
Default
skip-vrf-match
*
Enable/disable skipping VRF matching
on reply direction.
option
-disable
Option
Description
enable
Enable skipping VRF matching on reply direction.
disable
Disable skipping VRF matching on reply direction.
src-vendor-mac <id>
Vendor MAC source ID.
Vendor MAC ID.
integer
Minimum value:
0 Maximum
value:
4294967295
srcaddr <name>
Source IPv4 address and address
group names.
Address name.
string
Maximum
length: 79
srcaddr-negate
When enabled srcaddr specifies what
the source address must NOT be.
option
-disable
Option
Description
enable
Enable source address negate.
disable
Disable source address negate.
srcaddr6
<name>
Source IPv6 address name and
address group names.
Address name.
string
Maximum
length: 79
srcaddr6-negate
When enabled srcaddr6 specifies
what the source address must NOT
be.
option
-disable
Option
Description
enable
Enable IPv6 source address negate.
disable
Disable IPv6 source address negate.
srcintf <name>
Incoming (ingress) interface.
Interface name.
string
Maximum
length: 79
ssh-filter-profile *
Name of an existing SSH filter profile.
string
Maximum
length: 47
ssh-policy-redirect
Redirect SSH traffic to matching
transparent proxy policy.
option
-disable
FortiOS 8.0.0 CLI Reference
605
Fortinet Inc.

<!-- 来源页 606 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable SSH policy redirect.
disable
Disable SSH policy redirect.
ssl-ssh-profile
Name of an existing SSL SSH profile.
string
Maximum
length: 47
no-inspection
status
Enable or disable this policy.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
tcp-mss-receiver
Receiver TCP maximum segment size
(MSS).
integer
Minimum value:
0 Maximum
value: 65535
0
tcp-mss-sender
Sender TCP maximum segment size
(MSS).
integer
Minimum value:
0 Maximum
value: 65535
0
tcp-session-without-syn
Enable/disable creation of TCP
session without SYN flag.
option
-disable
Option
Description
all
Enable TCP session without SYN.
data-only
Enable TCP session data only.
disable
Disable TCP session without SYN.
telemetry-profile *
Name of an existing telemetry profile.
string
Maximum
length: 47
timeout-send-rst
Enable/disable sending RST packets
when TCP sessions expire.
option
-disable
Option
Description
enable
Enable sending of RST packet upon TCP session expiration.
disable
Disable sending of RST packet upon TCP session expiration.
tos
ToS (Type of Service) value used for
comparison.
user
Not Specified
FortiOS 8.0.0 CLI Reference
606
Fortinet Inc.

<!-- 来源页 607 -->
Parameter
Description
Type
Size
Default
tos-mask
Non-zero bit positions are used for
comparison while zero bit positions
are ignored.
user
Not Specified
tos-negate
Enable negated TOS match.
option
-disable
Option
Description
enable
Enable TOS match negate.
disable
Disable TOS match negate.
traffic-shaper
Traffic shaper.
string
Maximum
length: 35
traffic-shaper-reverse
Reverse traffic shaper.
string
Maximum
length: 35
users <name>
Names of individual users that can
authenticate with this policy.
Names of individual users that can
authenticate with this policy.
string
Maximum
length: 79
utm-status
Enable to add one or more security
profiles (AV, IPS, etc.) to the firewall
policy.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
uuid
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not Specified
00000000-0000-0000-0000-000000000000
videofilter-profile *
Name of an existing VideoFilter
profile.
string
Maximum
length: 47
virtual-patch-profile
Name of an existing virtual-patch
profile.
string
Maximum
length: 47
vlan-cos-fwd
VLAN forward direction user priority:
255 passthrough, 0 lowest, 7 highest.
integer
Minimum value:
0 Maximum
value: 7
255
vlan-cos-rev
VLAN reverse direction user priority:
255 passthrough, 0 lowest, 7 highest.
integer
Minimum value:
0 Maximum
value: 7
255
vlan-filter
VLAN ranges to allow
user
Not Specified
FortiOS 8.0.0 CLI Reference
607
Fortinet Inc.

<!-- 来源页 608 -->
Parameter
Description
Type
Size
Default
voip-profile
Name of an existing VoIP (voipd)
profile.
string
Maximum
length: 47
vpntunnel
Policy-based IPsec VPN: name of the
IPsec VPN Phase 1.
string
Maximum
length: 35
waf-profile *
Name of an existing Web application
firewall profile.
string
Maximum
length: 47
wanopt *
Enable/disable WAN optimization.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
wanopt-detection *
WAN optimization auto-detection
mode.
option
-active
Option
Description
active
Active WAN optimization peer auto-detection.
passive
Passive WAN optimization peer auto-detection.
off
Turn off WAN optimization peer auto-detection.
wanopt-passive-opt *
WAN optimization passive mode
options. This option decides what IP
address will be used to connect
server.
option
-default
Option
Description
default
Allow client side WAN opt peer to decide.
transparent
Use address of client to connect to server.
non-transparent
Use local FortiGate address to connect to server.
wanopt-peer *
WAN optimization peer.
string
Maximum
length: 35
wanopt-profile
*
WAN optimization profile.
string
Maximum
length: 35
wccp
Enable/disable forwarding traffic
matching this policy to a configured
WCCP server.
option
-disable
FortiOS 8.0.0 CLI Reference
608
Fortinet Inc.

<!-- 来源页 609 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable WCCP setting.
disable
Disable WCCP setting.
webcache *
Enable/disable web cache.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
webcache-https *
Enable/disable web cache for HTTPS.
option
-disable
Option
Description
disable
Disable web cache for HTTPS.
enable
Enable web cache for HTTPS.
webfilter-profile
Name of an existing Web filter profile.
string
Maximum
length: 47
webproxy-forward-server
Webproxy forward server name.
string
Maximum
length: 63
webproxy-profile
Webproxy profile name.
string
Maximum
length: 63
ztna-destination
<name> *
Configure ZTNA destinations. Must be
used with ZTNA traffic-forward-proxy.
ZTNA destination name.
string
Maximum
length: 79
ztna-device-ownership
Enable/disable zero trust device
ownership.
option
-disable
Option
Description
enable
Enable ZTNA device ownership check.
disable
Disable ZTNA device ownership check.
ztna-ems-tag
<name>
Source ztna-ems-tag names.
Address name.
string
Maximum
length: 79
ztna-ems-tag-negate
When enabled ztna-ems-tag specifies
what the tags must NOT be.
option
-disable
FortiOS 8.0.0 CLI Reference
609
Fortinet Inc.

<!-- 来源页 610 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable ZTNA EMS tags negate.
disable
Disable ZTNA EMS tags negate.
ztna-ems-tag-secondary
<name>
Source ztna-ems-tag-secondary
names.
Address name.
string
Maximum
length: 79
ztna-ems-tag6
<name> *
Source ZTNA FortiClient EMS tag IPv6
names.
Address name.
string
Maximum
length: 79
ztna-geo-tag
<name>
Source ztna-geo-tag names.
Address name.
string
Maximum
length: 79
ztna-policy-redirect
Redirect ZTNA traffic to matching
Access-Proxy proxy-policy.
option
-disable
Option
Description
enable
Enable ZTNA proxy-policy redirect.
disable
Disable ZTNA proxy-policy redirect.
ztna-status
Enable/disable zero trust access.
option
-disable
Option
Description
enable
Enable zero trust network access.
disable
Disable zero trust network access.
ztna-tags-match-logic
ZTNA tag matching logic.
option
-or
Option
Description
or
Match ZTNA tags using a logical OR operator.
and
Match ZTNA tags using a logical AND operator.
* This parameter may not exist in some models.
config fabric-policy
Parameter
Description
Type
Size
Default
from
From device.
string
Maximum length:
35
FortiOS 8.0.0 CLI Reference
610
Fortinet Inc.

---


<!-- 来源页 611 -->
Parameter
Description
Type
Size
Default
to
To device.
string
Maximum length:
35
config firewall profile-group
Configure profile groups.
config firewall profile-group
Description: Configure profile groups.
edit <name>
set application-list {string}
set av-profile {string}
set casb-profile {string}
set diameter-filter-profile {string}
set dlp-profile {string}
set dnsfilter-profile {string}
set emailfilter-profile {string}
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set file-filter-profile {string}
set icap-profile {string}
set ips-sensor {string}
set ips-voip-filter {string}
set llm-profile {string}
set profile-protocol-options {string}
set sctp-filter-profile {string}
set ssh-filter-profile {string}
set ssl-ssh-profile {string}
set telemetry-profile {string}
set uuid {uuid}
set videofilter-profile {string}
set virtual-patch-profile {string}
set voip-profile {string}
set waf-profile {string}
set webfilter-profile {string}
next
end
config firewall profile-group
Parameter
Description
Type
Size
Default
application-list
Name of an existing Application list.
string
Maximum
length: 47
FortiOS 8.0.0 CLI Reference
611
Fortinet Inc.

<!-- 来源页 612 -->
Parameter
Description
Type
Size
Default
av-profile
Name of an existing Antivirus profile.
string
Maximum
length: 47
casb-profile *
Name of an existing CASB profile.
string
Maximum
length: 47
diameter-filter-profile
Name of an existing Diameter filter profile.
string
Maximum
length: 47
dlp-profile
Name of an existing DLP profile.
string
Maximum
length: 47
dnsfilter-profile
Name of an existing DNS filter profile.
string
Maximum
length: 47
emailfilter-profile
Name of an existing email filter profile.
string
Maximum
length: 47
fabric-force-sync *
Enable/disable forced synchronization of
configuration objects from the root
FortiGate unit to the downstream devices.
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
file-filter-profile
Name of an existing file-filter profile.
string
Maximum
length: 47
FortiOS 8.0.0 CLI Reference
612
Fortinet Inc.

<!-- 来源页 613 -->
Parameter
Description
Type
Size
Default
icap-profile *
Name of an existing ICAP profile.
string
Maximum
length: 47
ips-sensor
Name of an existing IPS sensor.
string
Maximum
length: 47
ips-voip-filter
Name of an existing VoIP (ips) profile.
string
Maximum
length: 47
llm-profile *
Name of an existing LLM profile.
string
Maximum
length: 47
name
Profile group name.
string
Maximum
length: 47
profile-protocol-options
Name of an existing Protocol options profile.
string
Maximum
length: 47
default
sctp-filter-profile
Name of an existing SCTP filter profile.
string
Maximum
length: 47
ssh-filter-profile *
Name of an existing SSH filter profile.
string
Maximum
length: 47
ssl-ssh-profile
Name of an existing SSL SSH profile.
string
Maximum
length: 47
certificate-inspection
telemetry-profile *
Name of an existing telemetry profile.
string
Maximum
length: 47
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be manually
reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
videofilter-profile *
Name of an existing VideoFilter profile.
string
Maximum
length: 47
virtual-patch-profile
Name of an existing virtual-patch profile.
string
Maximum
length: 47
voip-profile
Name of an existing VoIP (voipd) profile.
string
Maximum
length: 47
waf-profile *
Name of an existing Web application firewall
profile.
string
Maximum
length: 47
webfilter-profile
Name of an existing Web filter profile.
string
Maximum
length: 47
* This parameter may not exist in some models.
FortiOS 8.0.0 CLI Reference
613
Fortinet Inc.

---


<!-- 来源页 614 -->
config firewall profile-protocol-options
Configure protocol options.
config firewall profile-protocol-options
Description: Configure protocol options.
edit <name>
config cifs
Description: Configure CIFS protocol options.
set domain-controller {string}
set options {option1}, {option2}, ...
set oversize-limit {integer}
set ports {integer}
set scan-bzip2 [enable|disable]
set server-credential-type [none|credential-replication|...]
config server-keytab
Description: Server keytab.
edit <principal>
set keytab {string}
next
end
set status [enable|disable]
set tcp-window-maximum {integer}
set tcp-window-minimum {integer}
set tcp-window-size {integer}
set tcp-window-type [auto-tuning|system|...]
set uncompressed-nest-limit {integer}
set uncompressed-oversize-limit {integer}
end
set comment {var-string}
config dns
Description: Configure DNS protocol options.
set ports {integer}
set status [enable|disable]
end
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
config ftp
Description: Configure FTP protocol options.
set comfort-amount {integer}
set comfort-interval {integer}
set explicit-ftp-tls [enable|disable]
set inspect-all [enable|disable]
set options {option1}, {option2}, ...
set oversize-limit {integer}
set ports {integer}
set scan-bzip2 [enable|disable]
set ssl-offloaded [no|yes]
set status [enable|disable]
set stream-based-uncompressed-limit {integer}
FortiOS 8.0.0 CLI Reference
614
Fortinet Inc.

<!-- 来源页 615 -->
set tcp-window-maximum {integer}
set tcp-window-minimum {integer}
set tcp-window-size {integer}
set tcp-window-type [auto-tuning|system|...]
set uncompressed-nest-limit {integer}
set uncompressed-oversize-limit {integer}
end
config http
Description: Configure HTTP protocol options.
set address-ip-rating [enable|disable]
set block-page-status-code {integer}
set comfort-amount {integer}
set comfort-interval {integer}
set domain-fronting [allow|monitor|...]
set h2c [enable|disable]
set http-0 9 [allow|block]
set inspect-all [enable|disable]
set options {option1}, {option2}, ...
set oversize-limit {integer}
set ports {integer}
set post-lang {option1}, {option2}, ...
set proxy-after-tcp-handshake [enable|disable]
set range-block [disable|enable]
set retry-count {integer}
set scan-bzip2 [enable|disable]
set ssl-offloaded [no|yes]
set status [enable|disable]
set stream-based-uncompressed-limit {integer}
set streaming-content-bypass [enable|disable]
set streaming-content-scan-type {option1}, {option2}, ...
set strip-x-forwarded-for [disable|enable]
set switching-protocols [bypass|block]
set tcp-window-maximum {integer}
set tcp-window-minimum {integer}
set tcp-window-size {integer}
set tcp-window-type [auto-tuning|system|...]
set tunnel-non-http [enable|disable]
set uncompressed-nest-limit {integer}
set uncompressed-oversize-limit {integer}
set unknown-content-encoding [block|inspect|...]
set unknown-http-version [reject|tunnel|...]
set verify-dns-for-policy-matching [enable|disable]
end
config imap
Description: Configure IMAP protocol options.
set inspect-all [enable|disable]
set options {option1}, {option2}, ...
set oversize-limit {integer}
set ports {integer}
set proxy-after-tcp-handshake [enable|disable]
set scan-bzip2 [enable|disable]
set ssl-offloaded [no|yes]
FortiOS 8.0.0 CLI Reference
615
Fortinet Inc.

<!-- 来源页 616 -->
set status [enable|disable]
set uncompressed-nest-limit {integer}
set uncompressed-oversize-limit {integer}
end
config mail-signature
Description: Configure Mail signature.
set signature {string}
set status [disable|enable]
end
config mapi
Description: Configure MAPI protocol options.
set options {option1}, {option2}, ...
set oversize-limit {integer}
set ports {integer}
set scan-bzip2 [enable|disable]
set status [enable|disable]
set uncompressed-nest-limit {integer}
set uncompressed-oversize-limit {integer}
end
config nntp
Description: Configure NNTP protocol options.
set inspect-all [enable|disable]
set options {option1}, {option2}, ...
set oversize-limit {integer}
set ports {integer}
set proxy-after-tcp-handshake [enable|disable]
set scan-bzip2 [enable|disable]
set status [enable|disable]
set uncompressed-nest-limit {integer}
set uncompressed-oversize-limit {integer}
end
set oversize-log [disable|enable]
config pop3
Description: Configure POP3 protocol options.
set inspect-all [enable|disable]
set options {option1}, {option2}, ...
set oversize-limit {integer}
set ports {integer}
set proxy-after-tcp-handshake [enable|disable]
set scan-bzip2 [enable|disable]
set ssl-offloaded [no|yes]
set status [enable|disable]
set uncompressed-nest-limit {integer}
set uncompressed-oversize-limit {integer}
end
set replacemsg-group {string}
set rpc-over-http [enable|disable]
config smtp
Description: Configure SMTP protocol options.
set inspect-all [enable|disable]
set options {option1}, {option2}, ...
set oversize-limit {integer}
FortiOS 8.0.0 CLI Reference
616
Fortinet Inc.

<!-- 来源页 617 -->
set ports {integer}
set proxy-after-tcp-handshake [enable|disable]
set scan-bzip2 [enable|disable]
set server-busy [enable|disable]
set ssl-offloaded [no|yes]
set status [enable|disable]
set uncompressed-nest-limit {integer}
set uncompressed-oversize-limit {integer}
end
config ssh
Description: Configure SFTP and SCP protocol options.
set comfort-amount {integer}
set comfort-interval {integer}
set options {option1}, {option2}, ...
set oversize-limit {integer}
set scan-bzip2 [enable|disable]
set ssl-offloaded [no|yes]
set stream-based-uncompressed-limit {integer}
set tcp-window-maximum {integer}
set tcp-window-minimum {integer}
set tcp-window-size {integer}
set tcp-window-type [auto-tuning|system|...]
set uncompressed-nest-limit {integer}
set uncompressed-oversize-limit {integer}
end
set switching-protocols-log [disable|enable]
set uuid {uuid}
config websocket
Description: Configure WebSocket protocol options.
set comfort-amount {integer}
set comfort-interval {integer}
set options {option1}, {option2}, ...
set oversize-limit {integer}
set scan-bzip2 [enable|disable]
set status [enable|disable]
set stream-based-uncompressed-limit {integer}
set tcp-window-maximum {integer}
set tcp-window-minimum {integer}
set tcp-window-size {integer}
set tcp-window-type [auto-tuning|system|...]
set tunnel-non-websocket [enable|disable]
set uncompressed-nest-limit {integer}
set uncompressed-oversize-limit {integer}
end
next
end
FortiOS 8.0.0 CLI Reference
617
Fortinet Inc.

<!-- 来源页 618 -->
config firewall profile-protocol-options
Parameter
Description
Type
Size
Default
comment
Optional comments.
var-string
Maximum
length: 255
fabric-force-sync *
Enable/disable forced synchronization of
configuration objects from the root
FortiGate unit to the downstream devices.
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
fabric-object *
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
name
Name.
string
Maximum
length: 47
oversize-log
Enable/disable logging for antivirus
oversize file blocking.
option
-disable
Option
Description
disable
Disable logging for antivirus oversize file blocking.
enable
Enable logging for antivirus oversize file blocking.
replacemsg-group
Name of the replacement message group
to be used.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
618
Fortinet Inc.

<!-- 来源页 619 -->
Parameter
Description
Type
Size
Default
rpc-over-http
Enable/disable inspection of RPC over
HTTP.
option
-disable
Option
Description
enable
Enable inspection of RPC over HTTP.
disable
Disable inspection of RPC over HTTP.
switching-protocols-log
Enable/disable logging for HTTP/HTTPS
switching protocols.
option
-disable
Option
Description
disable
Disable logging for HTTP/HTTPS switching protocols.
enable
Enable logging for HTTP/HTTPS switching protocols.
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be manually
reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
config cifs
Parameter
Description
Type
Size
Default
domain-controller
Domain for which to decrypt CIFS traffic.
string
Maximum
length: 63
options
One or more options that can be applied to the
session.
option
-Option
Description
oversize
Block oversized file.
oversize-limit
Maximum in-memory file size that can be
scanned (MB).
integer
Minimum
value: 1
Maximum
value: 1606
**
10
ports
Ports to scan for content (1 - 65535, default =
445).
integer
Minimum
value: 1
Maximum
value:
65535
FortiOS 8.0.0 CLI Reference
619
Fortinet Inc.

<!-- 来源页 620 -->
Parameter
Description
Type
Size
Default
scan-bzip2
Enable/disable scanning of BZip2 compressed
files.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
server-credential-type
CIFS server credential type.
option
-none
Option
Description
none
Credential derivation not set.
credential-replication
Credential derived using Replication account on Domain Controller.
credential-keytab
Credential derived using server keytab.
status
Enable/disable the active status of scanning
for this protocol.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
tcp-window-maximum
Maximum dynamic TCP window size.
integer
Minimum
value:
1048576
Maximum
value:
16777216
8388608
tcp-window-minimum
Minimum dynamic TCP window size.
integer
Minimum
value:
65536
Maximum
value:
1048576
131072
tcp-window-size
Set TCP static window size.
integer
Minimum
value:
65536
Maximum
value:
16777216
262144
FortiOS 8.0.0 CLI Reference
620
Fortinet Inc.

<!-- 来源页 621 -->
Parameter
Description
Type
Size
Default
tcp-window-type
TCP window type to use for this protocol.
option
-auto-tuning
Option
Description
auto-tuning
Allow system to auto-tune TCP window size (default).
system
Use system default TCP window size for this protocol.
static
Manually specify TCP window size.
dynamic
Vary TCP window size based on available memory and within limits
of tcp-window-minimum and tcp-window-maximum.
uncompressed-nest-limit
Maximum nested levels of compression that
can be uncompressed and scanned (2 - 100,
default = 12).
integer
Minimum
value: 2
Maximum
value: 100
12
uncompressed-oversize-limit
Maximum in-memory uncompressed file size
that can be scanned (MB).
integer
Minimum
value: 1
Maximum
value: 1606
**
10
** Values may differ between models.
config server-keytab
Parameter
Description
Type
Size
Default
keytab
Base64 encoded keytab file containing credential
of the server.
string
Maximum
length: 8191
principal
Service principal. For example,
host/cifsserver.example.com@example.com.
string
Maximum
length: 511
config dns
Parameter
Description
Type
Size
Default
ports
Ports to scan for content (1 - 65535, default = 53).
integer
Minimum
value: 1
Maximum
value:
65535
status
Enable/disable the active status of scanning for this
protocol.
option
-enable
FortiOS 8.0.0 CLI Reference
621
Fortinet Inc.

<!-- 来源页 622 -->
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
config ftp
Parameter
Description
Type
Size
Default
comfort-amount
Number of bytes to send in each
transmission for client comforting (bytes).
integer
Minimum value:
1 Maximum
value: 65535
1
comfort-interval
Interval between successive transmissions
of data for client comforting (seconds).
integer
Minimum value:
1 Maximum
value: 900
10
explicit-ftp-tls
Enable/disable FTP redirection for explicit
FTPS.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
inspect-all
Enable/disable the inspection of all ports
for the protocol.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
options
One or more options that can be applied to
the session.
option
-Option
Description
clientcomfort
Prevent client timeout.
oversize
Block oversized file.
splice
Enable splice mode.
bypass-rest-command
Bypass REST command.
bypass-mode-command
Bypass MODE command.
FortiOS 8.0.0 CLI Reference
622
Fortinet Inc.

<!-- 来源页 623 -->
Parameter
Description
Type
Size
Default
oversize-limit
Maximum in-memory file size that can be
scanned (MB).
integer
Minimum value:
1 Maximum
value: 1606 **
10
ports
Ports to scan for content (1 - 65535,
default = 21).
integer
Minimum value:
1 Maximum
value: 65535
scan-bzip2
Enable/disable scanning of BZip2
compressed files.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
ssl-offloaded
SSL decryption and encryption performed
by an external device.
option
-no
Option
Description
no
SSL decryption and encryption performed by FortiGate when deep-inspection is enabled.
yes
SSL decryption and encryption performed by an external device.
status
Enable/disable the active status of
scanning for this protocol.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
stream-based-uncompressed-limit
Maximum stream-based uncompressed
data size that will be scanned in
megabytes. Stream-based uncompression
used only under certain conditions
(unlimited = 0, default = 0).
integer
Minimum value:
0 Maximum
value:
4294967295
0
tcp-window-maximum
Maximum dynamic TCP window size.
integer
Minimum value:
1048576
Maximum
value:
16777216
8388608
tcp-window-minimum
Minimum dynamic TCP window size.
integer
Minimum value:
65536
Maximum
value: 1048576
131072
FortiOS 8.0.0 CLI Reference
623
Fortinet Inc.

<!-- 来源页 624 -->
Parameter
Description
Type
Size
Default
tcp-window-size
Set TCP static window size.
integer
Minimum value:
65536
Maximum
value:
16777216
262144
tcp-window-type
TCP window type to use for this protocol.
option
-auto-tuning
Option
Description
auto-tuning
Allow system to auto-tune TCP window size (default).
system
Use system default TCP window size for this protocol.
static
Manually specify TCP window size.
dynamic
Vary TCP window size based on available memory and within limits
of tcp-window-minimum and tcp-window-maximum.
uncompressed-nest-limit
Maximum nested levels of compression
that can be uncompressed and scanned (2
- 100, default = 12).
integer
Minimum value:
2 Maximum
value: 100
12
uncompressed-oversize-limit
Maximum in-memory uncompressed file
size that can be scanned (MB).
integer
Minimum value:
1 Maximum
value: 1606 **
10
** Values may differ between models.
config http
Parameter
Description
Type
Size
Default
address-ip-rating
Enable/disable IP based URL rating.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
block-page-status-code
Code number returned for blocked HTTP
pages (non-FortiGuard only) (100 - 599,
default = 403).
integer
Minimum value:
100 Maximum
value: 599
403
comfort-amount
Number of bytes to send in each
transmission for client comforting (bytes).
integer
Minimum value:
1 Maximum
value: 65535
1
FortiOS 8.0.0 CLI Reference
624
Fortinet Inc.

<!-- 来源页 625 -->
Parameter
Description
Type
Size
Default
comfort-interval
Interval between successive transmissions
of data for client comforting (seconds).
integer
Minimum value:
1 Maximum
value: 900
10
domain-fronting *
Configure HTTP domain fronting (default =
block).
option
-block
Option
Description
allow
Allow domain fronting.
monitor
Allow and log domain fronting.
block
Block and log domain fronting. Will not block potential matching IP
and Domain.
strict
Block and log domain fronting. Will block potential matching IP and
Domain.
h2c
Enable/disable h2c HTTP connection
upgrade.
option
-disable
Option
Description
enable
Allow h2c HTTP connection upgrades. h2c tunnels do not support
content scan.
disable
Do not allow h2c HTTP connection upgrades.
http-0 9
Configure action to take upon receipt of
HTTP 0.9 request.
option
-allow
Option
Description
allow
Allow HTTP 0.9 traffic for web filtering only.
block
Block HTTP 0.9 traffic.
inspect-all
Enable/disable the inspection of all ports
for the protocol.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
options
One or more options that can be applied to
the session.
option
-FortiOS 8.0.0 CLI Reference
625
Fortinet Inc.

<!-- 来源页 626 -->
Parameter
Description
Type
Size
Default
Option
Description
clientcomfort
Prevent client timeout.
servercomfort
Prevent server timeout.
oversize
Block oversized file.
chunkedbypass
Bypass chunked transfer encoded sites.
oversize-limit
Maximum in-memory file size that can be
scanned (MB).
integer
Minimum value:
1 Maximum
value: 1606 **
10
ports
Ports to scan for content (1 - 65535,
default = 80).
integer
Minimum value:
1 Maximum
value: 65535
post-lang
ID codes for character sets to be used to
convert to UTF-8 for banned words and
DLP on HTTP posts (maximum of 5
character sets).
option
-Option
Description
jisx0201
Japanese Industrial Standard 0201.
jisx0208
Japanese Industrial Standard 0208.
jisx0212
Japanese Industrial Standard 0212.
gb2312
Guojia Biaozhun 2312 (simplified Chinese).
ksc5601-ex
Wansung Korean standard 5601.
euc-jp
Extended Unicode Japanese.
sjis
Shift Japanese Industrial Standard.
iso2022-jp
ISO 2022 Japanese.
iso2022-jp-1
ISO 2022-1 Japanese.
iso2022-jp-2
ISO 2022-2 Japanese.
euc-cn
Extended Unicode Chinese.
ces-gbk
Extended GB2312 (simplified Chinese).
hz
Hanzi simplified Chinese.
ces-big5
Big-5 traditional Chinese.
euc-kr
Extended Unicode Korean.
iso2022-jp-3
ISO 2022-3 Japanese.
FortiOS 8.0.0 CLI Reference
626
Fortinet Inc.

<!-- 来源页 627 -->
Parameter
Description
Type
Size
Default
Option
Description
iso8859-1
ISO 8859 Part 1 (Western European).
tis620
Thai Industrial Standard 620.
cp874
Code Page 874 (Thai).
cp1252
Code Page 1252 (Western European Latin).
cp1251
Code Page 1251 (Cyrillic).
proxy-after-tcp-handshake
Proxy traffic after the TCP 3-way
handshake has been established (not
before).
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
range-block
Enable/disable blocking of partial
downloads.
option
-disable
Option
Description
disable
Disable range header blocking (allow partial file downloads)
enable
Enable range header blocking (treat all partial file downloads as full
file download)
retry-count
Number of attempts to retry HTTP
connection (0 - 100, default = 0).
integer
Minimum value:
0 Maximum
value: 100
0
scan-bzip2
Enable/disable scanning of BZip2
compressed files.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
ssl-offloaded
SSL decryption and encryption performed
by an external device.
option
-no
Option
Description
no
SSL decryption and encryption performed by FortiGate when deep-inspection is enabled.
yes
SSL decryption and encryption performed by an external device.
FortiOS 8.0.0 CLI Reference
627
Fortinet Inc.

<!-- 来源页 628 -->
Parameter
Description
Type
Size
Default
status
Enable/disable the active status of
scanning for this protocol.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
stream-based-uncompressed-limit
Maximum stream-based uncompressed
data size that will be scanned in
megabytes. Stream-based uncompression
used only under certain conditions
(unlimited = 0, default = 0).
integer
Minimum value:
0 Maximum
value:
4294967295
0
streaming-content-bypass
Enable/disable bypassing of streaming
content from buffering.
option
-enable
Option
Description
enable
Enable bypassing of streaming content from buffering
disable
Disable bypassing of streaming content from buffering
streaming-content-scan-type *
Enforce scan on certain streaming content
type when streaming-content-bypass is
enabled.
option
-octet
Option
Description
flv
Match application/flv.
octet
Match application/octet-stream.
dvi
Match application/x-dvi.
rtmp
Match application/x-fcs.
mms-framed
Match application/x-mms-framed.
msmediaview
Match application/x-msmediaview.
pncmd
Match application/x-pncmd.
rtsp-tunnel
Match application/x-rtsp-tunnelled.
audio
Match audio/.
audio-accp
Match audio/accp.
audio-mpeg
Match audio/mpeg.
pn-realaudio
Match audio/x-pn-realaudio.
FortiOS 8.0.0 CLI Reference
628
Fortinet Inc.

<!-- 来源页 629 -->
Parameter
Description
Type
Size
Default
Option
Description
pn-realaudio-plugin
Match audio/x-pn-realaudio-plugin.
mixed
Match multipart/mixed.
x-mixed
Match multipart/x-mixed-replace.
event-stream
Match text/event-stream.
video
Match video/.
video-mp4
Match video/mp4.
video-mpeg
Match video/mpeg.
video-xflv
Match video/x-flv.
video-xasf
Match video/x-ms-asf.
strip-x-forwarded-for
Enable/disable stripping of HTTP X-Forwarded-For header.
option
-disable
Option
Description
disable
Disable changing of HTTP X-Forwarded-For header.
enable
Enable replacement of X-Forwarded-For value with 1.1.1.1.
switching-protocols
Bypass from scanning, or block a
connection that attempts to switch
protocol.
option
-bypass
Option
Description
bypass
Bypass connections when switching protocols.
block
Block connections when switching protocols.
tcp-window-maximum
Maximum dynamic TCP window size.
integer
Minimum value:
1048576
Maximum
value:
16777216
8388608
tcp-window-minimum
Minimum dynamic TCP window size.
integer
Minimum value:
65536
Maximum
value: 1048576
131072
FortiOS 8.0.0 CLI Reference
629
Fortinet Inc.

<!-- 来源页 630 -->
Parameter
Description
Type
Size
Default
tcp-window-size
Set TCP static window size.
integer
Minimum value:
65536
Maximum
value:
16777216
262144
tcp-window-type
TCP window type to use for this protocol.
option
-auto-tuning
Option
Description
auto-tuning
Allow system to auto-tune TCP window size (default).
system
Use system default TCP window size for this protocol.
static
Manually specify TCP window size.
dynamic
Vary TCP window size based on available memory and within limits
of tcp-window-minimum and tcp-window-maximum.
tunnel-non-http
Configure how to process non-HTTP traffic
when a profile configured for HTTP traffic
accepts a non-HTTP session. Can occur if
an application sends non-HTTP traffic
using an HTTP destination port.
option
-enable
Option
Description
enable
Pass non-HTTP sessions through the tunnel without applying
protocol optimization, byte-caching, or web caching. TCP protocol
optimization is applied.
disable
Drop or tear down non-HTTP sessions accepted by the profile.
uncompressed-nest-limit
Maximum nested levels of compression
that can be uncompressed and scanned (2
- 100, default = 12).
integer
Minimum value:
2 Maximum
value: 100
12
uncompressed-oversize-limit
Maximum in-memory uncompressed file
size that can be scanned (MB).
integer
Minimum value:
1 Maximum
value: 1606 **
10
unknown-content-encoding
Configure the action the FortiGate unit will
take on unknown content-encoding.
option
-block
Option
Description
block
Block HTTP session when unknown content-encoding is detected.
inspect
Scan HTTP traffic as plain-text when unknown content-encoding is
detected.
bypass
Bypass scan when unknown content-encoding is detected.
FortiOS 8.0.0 CLI Reference
630
Fortinet Inc.

<!-- 来源页 631 -->
Parameter
Description
Type
Size
Default
unknown-http-version
How to handle HTTP sessions that do not
comply with HTTP 0.9, 1.0, or 1.1.
option
-reject
Option
Description
reject
Reject or tear down HTTP sessions that do not use HTTP 0.9, 1.0, or
1.1.
tunnel
Pass HTTP traffic that does not use HTTP 0.9, 1.0, or 1.1 without
applying HTTP protocol optimization, byte-caching, or web caching.
TCP protocol optimization is applied.
best-effort
Assume all HTTP sessions comply with HTTP 0.9, 1.0, or 1.1. If a
session uses a different HTTP version, it may not parse correctly and
the connection may be lost.
verify-dns-for-policy-matching
Enable/disable verification of DNS for
policy matching.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
* This parameter may not exist in some models.
** Values may differ between models.
config imap
Parameter
Description
Type
Size
Default
inspect-all
Enable/disable the inspection of all ports for the
protocol.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
options
One or more options that can be applied to the
session.
option
-Option
Description
fragmail
Pass fragmented email.
oversize
Block oversized email.
FortiOS 8.0.0 CLI Reference
631
Fortinet Inc.

<!-- 来源页 632 -->
Parameter
Description
Type
Size
Default
oversize-limit
Maximum in-memory file size that can be
scanned (MB).
integer
Minimum
value: 1
Maximum
value: 1606
**
10
ports
Ports to scan for content (1 - 65535, default =
143).
integer
Minimum
value: 1
Maximum
value:
65535
proxy-after-tcp-handshake
Proxy traffic after the TCP 3-way handshake
has been established (not before).
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
scan-bzip2
Enable/disable scanning of BZip2 compressed
files.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
ssl-offloaded
SSL decryption and encryption performed by
an external device.
option
-no
Option
Description
no
SSL decryption and encryption performed by FortiGate when deep-inspection is enabled.
yes
SSL decryption and encryption performed by an external device.
status
Enable/disable the active status of scanning for
this protocol.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
632
Fortinet Inc.

<!-- 来源页 633 -->
Parameter
Description
Type
Size
Default
uncompressed-nest-limit
Maximum nested levels of compression that
can be uncompressed and scanned (2 - 100,
default = 12).
integer
Minimum
value: 2
Maximum
value: 100
12
uncompressed-oversize-limit
Maximum in-memory uncompressed file size
that can be scanned (MB).
integer
Minimum
value: 1
Maximum
value: 1606
**
10
** Values may differ between models.
config mail-signature
Parameter
Description
Type
Size
Default
signature
Email signature to be added to outgoing email (if
the signature contains spaces, enclose with
quotation marks).
string
Maximum
length:
1023
status
Enable/disable adding an email signature to SMTP
email messages as they pass through the
FortiGate.
option
-disable
Option
Description
disable
Disable mail signature.
enable
Enable mail signature.
config mapi
Parameter
Description
Type
Size
Default
options
One or more options that can be applied to the
session.
option
-Option
Description
fragmail
Pass fragmented email.
oversize
Block oversized email.
oversize-limit
Maximum in-memory file size that can be
scanned (MB).
integer
Minimum
value: 1
Maximum
value: 1606
**
10
FortiOS 8.0.0 CLI Reference
633
Fortinet Inc.

<!-- 来源页 634 -->
Parameter
Description
Type
Size
Default
ports
Ports to scan for content (1 - 65535, default =
135).
integer
Minimum
value: 1
Maximum
value:
65535
scan-bzip2
Enable/disable scanning of BZip2 compressed
files.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
status
Enable/disable the active status of scanning for
this protocol.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
uncompressed-nest-limit
Maximum nested levels of compression that
can be uncompressed and scanned (2 - 100,
default = 12).
integer
Minimum
value: 2
Maximum
value: 100
12
uncompressed-oversize-limit
Maximum in-memory uncompressed file size
that can be scanned (MB).
integer
Minimum
value: 1
Maximum
value: 1606
**
10
** Values may differ between models.
config nntp
Parameter
Description
Type
Size
Default
inspect-all
Enable/disable the inspection of all ports for the
protocol.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
634
Fortinet Inc.

<!-- 来源页 635 -->
Parameter
Description
Type
Size
Default
options
One or more options that can be applied to the
session.
option
-Option
Description
oversize
Block oversized file.
splice
Enable splice mode.
oversize-limit
Maximum in-memory file size that can be
scanned (MB).
integer
Minimum
value: 1
Maximum
value: 1606
**
10
ports
Ports to scan for content (1 - 65535, default =
119).
integer
Minimum
value: 1
Maximum
value:
65535
proxy-after-tcp-handshake
Proxy traffic after the TCP 3-way handshake
has been established (not before).
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
scan-bzip2
Enable/disable scanning of BZip2 compressed
files.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
status
Enable/disable the active status of scanning for
this protocol.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
uncompressed-nest-limit
Maximum nested levels of compression that
can be uncompressed and scanned (2 - 100,
default = 12).
integer
Minimum
value: 2
Maximum
value: 100
12
FortiOS 8.0.0 CLI Reference
635
Fortinet Inc.

<!-- 来源页 636 -->
Parameter
Description
Type
Size
Default
uncompressed-oversize-limit
Maximum in-memory uncompressed file size
that can be scanned (MB).
integer
Minimum
value: 1
Maximum
value: 1606
**
10
** Values may differ between models.
config pop3
Parameter
Description
Type
Size
Default
inspect-all
Enable/disable the inspection of all ports for the
protocol.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
options
One or more options that can be applied to the
session.
option
-Option
Description
fragmail
Pass fragmented email.
oversize
Block oversized email.
oversize-limit
Maximum in-memory file size that can be
scanned (MB).
integer
Minimum
value: 1
Maximum
value: 1606
**
10
ports
Ports to scan for content (1 - 65535, default =
110).
integer
Minimum
value: 1
Maximum
value:
65535
proxy-after-tcp-handshake
Proxy traffic after the TCP 3-way handshake
has been established (not before).
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
636
Fortinet Inc.

<!-- 来源页 637 -->
Parameter
Description
Type
Size
Default
scan-bzip2
Enable/disable scanning of BZip2 compressed
files.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
ssl-offloaded
SSL decryption and encryption performed by
an external device.
option
-no
Option
Description
no
SSL decryption and encryption performed by FortiGate when deep-inspection is enabled.
yes
SSL decryption and encryption performed by an external device.
status
Enable/disable the active status of scanning for
this protocol.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
uncompressed-nest-limit
Maximum nested levels of compression that
can be uncompressed and scanned (2 - 100,
default = 12).
integer
Minimum
value: 2
Maximum
value: 100
12
uncompressed-oversize-limit
Maximum in-memory uncompressed file size
that can be scanned (MB).
integer
Minimum
value: 1
Maximum
value: 1606
**
10
** Values may differ between models.
config smtp
Parameter
Description
Type
Size
Default
inspect-all
Enable/disable the inspection of all ports for the
protocol.
option
-disable
Option
Description
enable
Enable setting.
FortiOS 8.0.0 CLI Reference
637
Fortinet Inc.

<!-- 来源页 638 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable setting.
options
One or more options that can be applied to the
session.
option
-Option
Description
fragmail
Pass fragmented email.
oversize
Block oversized email.
splice
Enable splice mode.
oversize-limit
Maximum in-memory file size that can be
scanned (MB).
integer
Minimum
value: 1
Maximum
value: 1606
**
10
ports
Ports to scan for content (1 - 65535, default =
25).
integer
Minimum
value: 1
Maximum
value:
65535
proxy-after-tcp-handshake
Proxy traffic after the TCP 3-way handshake
has been established (not before).
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
scan-bzip2
Enable/disable scanning of BZip2 compressed
files.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
server-busy
Enable/disable SMTP server busy when server
not available.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
638
Fortinet Inc.

<!-- 来源页 639 -->
Parameter
Description
Type
Size
Default
ssl-offloaded
SSL decryption and encryption performed by
an external device.
option
-no
Option
Description
no
SSL decryption and encryption performed by FortiGate when deep-inspection is enabled.
yes
SSL decryption and encryption performed by an external device.
status
Enable/disable the active status of scanning for
this protocol.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
uncompressed-nest-limit
Maximum nested levels of compression that
can be uncompressed and scanned (2 - 100,
default = 12).
integer
Minimum
value: 2
Maximum
value: 100
12
uncompressed-oversize-limit
Maximum in-memory uncompressed file size
that can be scanned (MB).
integer
Minimum
value: 1
Maximum
value: 1606
**
10
** Values may differ between models.
config ssh
Parameter
Description
Type
Size
Default
comfort-amount
Number of bytes to send in each
transmission for client comforting (bytes).
integer
Minimum value:
1 Maximum
value: 65535
1
comfort-interval
Interval between successive transmissions
of data for client comforting (seconds).
integer
Minimum value:
1 Maximum
value: 900
10
options
One or more options that can be applied to
the session.
option
-Option
Description
oversize
Block oversized file.
FortiOS 8.0.0 CLI Reference
639
Fortinet Inc.

<!-- 来源页 640 -->
Parameter
Description
Type
Size
Default
Option
Description
clientcomfort
Prevent client timeout.
servercomfort
Prevent server timeout.
oversize-limit
Maximum in-memory file size that can be
scanned (MB).
integer
Minimum value:
1 Maximum
value: 1606 **
10
scan-bzip2
Enable/disable scanning of BZip2
compressed files.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
ssl-offloaded
SSL decryption and encryption performed
by an external device.
option
-no
Option
Description
no
SSL decryption and encryption performed by FortiGate when deep-inspection is enabled.
yes
SSL decryption and encryption performed by an external device.
stream-based-uncompressed-limit
Maximum stream-based uncompressed
data size that will be scanned in
megabytes. Stream-based uncompression
used only under certain conditions
(unlimited = 0, default = 0).
integer
Minimum value:
0 Maximum
value:
4294967295
0
tcp-window-maximum
Maximum dynamic TCP window size.
integer
Minimum value:
1048576
Maximum
value:
16777216
8388608
tcp-window-minimum
Minimum dynamic TCP window size.
integer
Minimum value:
65536
Maximum
value: 1048576
131072
tcp-window-size
Set TCP static window size.
integer
Minimum value:
65536
Maximum
value:
16777216
262144
FortiOS 8.0.0 CLI Reference
640
Fortinet Inc.

<!-- 来源页 641 -->
Parameter
Description
Type
Size
Default
tcp-window-type
TCP window type to use for this protocol.
option
-auto-tuning
Option
Description
auto-tuning
Allow system to auto-tune TCP window size (default).
system
Use system default TCP window size for this protocol.
static
Manually specify TCP window size.
dynamic
Vary TCP window size based on available memory and within limits
of tcp-window-minimum and tcp-window-maximum.
uncompressed-nest-limit
Maximum nested levels of compression
that can be uncompressed and scanned (2
- 100, default = 12).
integer
Minimum value:
2 Maximum
value: 100
12
uncompressed-oversize-limit
Maximum in-memory uncompressed file
size that can be scanned (MB).
integer
Minimum value:
1 Maximum
value: 1606 **
10
** Values may differ between models.
config websocket
Parameter
Description
Type
Size
Default
comfort-amount
Number of bytes to send in each
transmission for client comforting (bytes).
integer
Minimum value:
1 Maximum
value: 65535
1
comfort-interval
Interval between successive transmissions
of data for client comforting (seconds).
integer
Minimum value:
1 Maximum
value: 900
10
options
One or more options that can be applied to
the session.
option
-Option
Description
oversize
Block oversized file.
clientcomfort
Prevent client timeout.
servercomfort
Prevent server timeout.
oversize-limit
Maximum in-memory file size that can be
scanned (MB).
integer
Minimum value:
1 Maximum
value: 1606 **
10
FortiOS 8.0.0 CLI Reference
641
Fortinet Inc.

<!-- 来源页 642 -->
Parameter
Description
Type
Size
Default
scan-bzip2
Enable/disable scanning of BZip2
compressed files.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
status
Enable/disable the active status of
scanning for this protocol.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
stream-based-uncompressed-limit
Maximum stream-based uncompressed
data size that will be scanned in
megabytes. Stream-based uncompression
used only under certain conditions
(unlimited = 0, default = 0).
integer
Minimum value:
0 Maximum
value:
4294967295
0
tcp-window-maximum
Maximum dynamic TCP window size.
integer
Minimum value:
1048576
Maximum
value:
16777216
8388608
tcp-window-minimum
Minimum dynamic TCP window size.
integer
Minimum value:
65536
Maximum
value: 1048576
131072
tcp-window-size
Set TCP static window size.
integer
Minimum value:
65536
Maximum
value:
16777216
262144
tcp-window-type
TCP window type to use for this protocol.
option
-auto-tuning
Option
Description
auto-tuning
Allow system to auto-tune TCP window size (default).
system
Use system default TCP window size for this protocol.
static
Manually specify TCP window size.
FortiOS 8.0.0 CLI Reference
642
Fortinet Inc.

---


<!-- 来源页 643 -->
Parameter
Description
Type
Size
Default
Option
Description
dynamic
Vary TCP window size based on available memory and within limits
of tcp-window-minimum and tcp-window-maximum.
tunnel-non-websocket
Configure how to process non-websocket
traffic when a profile configured for
websocket traffic accepts a non-websocket session.
option
-enable
Option
Description
enable
Pass non-websocket sessions through the tunnel without applying
protocol optimization, byte-caching, or web caching. TCP protocol
optimization is applied.
disable
Drop or tear down non-websocket sessions accepted by the profile.
uncompressed-nest-limit
Maximum nested levels of compression
that can be uncompressed and scanned (2
- 100, default = 12).
integer
Minimum value:
2 Maximum
value: 100
12
uncompressed-oversize-limit
Maximum in-memory uncompressed file
size that can be scanned (MB).
integer
Minimum value:
1 Maximum
value: 1606 **
10
** Values may differ between models.
config firewall proxy-address
Configure web proxy address.
config firewall proxy-address
Description: Configure web proxy address.
edit <name>
set application <name1>, <name2>, ...
set case-sensitivity [disable|enable]
set category <id1>, <id2>, ...
set color {integer}
set comment {var-string}
set custom-tags <name1>, <name2>, ...
set display-with [all-tags|first-tag-only|...]
set header {string}
config header-group
Description: HTTP header group.
edit <id>
set case-sensitivity [disable|enable]
set header {string}
set header-name {string}
FortiOS 8.0.0 CLI Reference
643
Fortinet Inc.

<!-- 来源页 644 -->
next
end
set header-name {string}
set host {string}
set host-regex {string}
set llm-servers <name1>, <name2>, ...
set method {option1}, {option2}, ...
set path {string}
set query {string}
set referrer [enable|disable]
config tagging
Description: Config object tagging.
edit <name>
set category {string}
set tags <name1>, <name2>, ...
next
end
set type [host-regex|url|...]
set ua {option1}, {option2}, ...
set ua-max-ver {string}
set ua-min-ver {string}
set uuid {uuid}
next
end
config firewall proxy-address
Parameter
Description
Type
Size
Default
application
<name>
SaaS application.
SaaS application name.
string
Maximum
length: 79
case-sensitivity
Enable to make the pattern case
sensitive.
option
-disable
Option
Description
disable
Case insensitive in pattern.
enable
Case sensitive in pattern.
category
<id>
FortiGuard category ID.
FortiGuard category ID.
integer
Minimum value:
0 Maximum
value:
4294967295
color
Integer value to determine the color of
the icon in the GUI (1 - 32, default = 0,
which sets value to 1).
integer
Minimum value:
0 Maximum
value: 32
0
FortiOS 8.0.0 CLI Reference
644
Fortinet Inc.

<!-- 来源页 645 -->
Parameter
Description
Type
Size
Default
comment
Optional comments.
var-string
Maximum
length: 255
custom-tags
<name> *
Custom tags.
Names of custom tags used with this
address.
string
Maximum
length: 35
display-with
*
Display object with first tag, all tags, or
just the icon.
option
-all-tags
Option
Description
all-tags
Display object using all custom tags.
first-tag-only
Display object using first custom tag.
icon-and-color
Display object using icon and color.
header
HTTP header value as a regular
expression.
string
Maximum
length: 255
header-name
Name of HTTP header.
string
Maximum
length: 79
host
Address object for the host.
string
Maximum
length: 79
host-regex
Host name as a regular expression.
string
Maximum
length: 255
llm-servers
<name> *
LLM Proxy server names.
Server name.
string
Maximum
length: 79
method
HTTP request methods to be used.
option
-Option
Description
get
GET method.
post
POST method.
put
PUT method.
head
HEAD method.
connect
CONNECT method.
trace
TRACE method.
options
OPTIONS method.
delete
DELETE method.
update
UPDATE method.
FortiOS 8.0.0 CLI Reference
645
Fortinet Inc.

<!-- 来源页 646 -->
Parameter
Description
Type
Size
Default
Option
Description
patch
PATCH method.
other
Other methods.
name
Address name.
string
Maximum
length: 79
path
URL path as a regular expression.
string
Maximum
length: 255
query
Match the query part of the URL as a
regular expression.
string
Maximum
length: 255
referrer
Enable/disable use of referrer field in the
HTTP header to match the address.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
type
Proxy address type.
option
-url
Option
Description
host-regex
Host regular expression.
url
HTTP URL.
category
FortiGuard URL category.
method
HTTP request method.
ua
HTTP request user agent.
header
HTTP request header.
src-advanced
HTTP advanced source criteria.
dst-advanced
HTTP advanced destination criteria.
saas
SaaS application.
llm-server
LLM server.
ua
Names of browsers to be used as user
agent.
option
-Option
Description
chrome
Google Chrome.
FortiOS 8.0.0 CLI Reference
646
Fortinet Inc.

<!-- 来源页 647 -->
Parameter
Description
Type
Size
Default
Option
Description
ms
Microsoft Internet Explorer or EDGE.
firefox
Mozilla Firefox.
safari
Apple Safari.
ie
Microsoft Internet Explorer.
edge
Microsoft Edge.
other
Other browsers.
ua-max-ver
Maximum version of the user agent
specified in dotted notation. For example,
use 120 with the ua field set to "chrome"
to require Google Chrome's maximum
version must be 120.
string
Maximum
length: 63
ua-min-ver
Minimum version of the user agent
specified in dotted notation. For example,
use 90.0.1 with the ua field set to
"chrome" to require Google Chrome's
minimum version must be 90.0.1.
string
Maximum
length: 63
uuid
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
config header-group
Parameter
Description
Type
Size
Default
case-sensitivity
Case sensitivity in pattern.
option
-disable
Option
Description
disable
Case insensitive in pattern.
enable
Case sensitive in pattern.
header
HTTP header regular expression.
string
Maximum
length: 255
header-name
HTTP header.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
647
Fortinet Inc.

<!-- 来源页 648 -->
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
config tagging
Parameter
Description
Type
Size
Default
category
Tag category.
string
Maximum
length: 63
name
Tagging entry name.
string
Maximum
length: 63
tags <name>
Tags.
Tag name.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
648
Fortinet Inc.

---


<!-- 来源页 649 -->
config firewall proxy-address6
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
Configure web proxy address6.
config firewall proxy-address6
Description: Configure web proxy address6.
edit <name>
set application <name1>, <name2>, ...
set case-sensitivity [disable|enable]
set category <id1>, <id2>, ...
set color {integer}
set comment {var-string}
set custom-tags <name1>, <name2>, ...
set display-with [all-tags|first-tag-only|...]
set header {string}
config header-group
Description: HTTP header group.
edit <id>
set case-sensitivity [disable|enable]
set header {string}
set header-name {string}
next
FortiOS 8.0.0 CLI Reference
649
Fortinet Inc.

<!-- 来源页 650 -->
end
set header-name {string}
set host {string}
set host-regex {string}
set llm-servers <name1>, <name2>, ...
set method {option1}, {option2}, ...
set path {string}
set query {string}
set referrer [enable|disable]
config tagging
Description: Config object tagging.
edit <name>
set category {string}
set tags <name1>, <name2>, ...
next
end
set type [host-regex|url|...]
set ua {option1}, {option2}, ...
set ua-max-ver {string}
set ua-min-ver {string}
set uuid {uuid}
next
end
config firewall proxy-address6
Parameter
Description
Type
Size
Default
application
<name>
SaaS application.
SaaS application name.
string
Maximum
length: 79
case-sensitivity
Enable to make the pattern case
sensitive.
option
-disable
Option
Description
disable
Case insensitive in pattern.
enable
Case sensitive in pattern.
category
<id>
FortiGuard category ID.
FortiGuard category ID.
integer
Minimum value:
0 Maximum
value:
4294967295
color
Integer value to determine the color of
the icon in the GUI (1 - 32, default = 0,
which sets value to 1).
integer
Minimum value:
0 Maximum
value: 32
0
comment
Optional comments.
var-string
Maximum
length: 255
FortiOS 8.0.0 CLI Reference
650
Fortinet Inc.

<!-- 来源页 651 -->
Parameter
Description
Type
Size
Default
custom-tags
<name>
Custom tags.
Names of custom tags used with this
address.
string
Maximum
length: 35
display-with
Display object with first tag, all tags, or
just the icon.
option
-all-tags
Option
Description
all-tags
Display object using all custom tags.
first-tag-only
Display object using first custom tag.
icon-and-color
Display object using icon and color.
header
HTTP header value as a regular
expression.
string
Maximum
length: 255
header-name
Name of HTTP header.
string
Maximum
length: 79
host
Address6 object for the host.
string
Maximum
length: 79
host-regex
Host name as a regular expression.
string
Maximum
length: 255
llm-servers
<name>
LLM Proxy server names.
Server name.
string
Maximum
length: 79
method
HTTP request methods to be used.
option
-Option
Description
get
GET method.
post
POST method.
put
PUT method.
head
HEAD method.
connect
CONNECT method.
trace
TRACE method.
options
OPTIONS method.
delete
DELETE method.
update
UPDATE method.
patch
PATCH method.
other
Other methods.
FortiOS 8.0.0 CLI Reference
651
Fortinet Inc.

<!-- 来源页 652 -->
Parameter
Description
Type
Size
Default
name
Address6 name.
string
Maximum
length: 79
path
URL path as a regular expression.
string
Maximum
length: 255
query
Match the query part of the URL as a
regular expression.
string
Maximum
length: 255
referrer
Enable/disable use of referrer field in the
HTTP header to match the address.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
type
Proxy address6 type.
option
-url
Option
Description
host-regex
Host regular expression.
url
HTTP URL.
category
FortiGuard URL category.
method
HTTP request method.
ua
HTTP request user agent.
header
HTTP request header.
src-advanced
HTTP advanced source criteria.
dst-advanced
HTTP advanced destination criteria.
saas
SaaS application.
llm-server
LLM server.
ua
Names of browsers to be used as user
agent.
option
-Option
Description
chrome
Google Chrome.
ms
Microsoft Internet Explorer or EDGE.
firefox
Mozilla Firefox.
safari
Apple Safari.
FortiOS 8.0.0 CLI Reference
652
Fortinet Inc.

<!-- 来源页 653 -->
Parameter
Description
Type
Size
Default
Option
Description
ie
Microsoft Internet Explorer.
edge
Microsoft Edge.
other
Other browsers.
ua-max-ver
Maximum version of the user agent
specified in dotted notation. For example,
use 120 with the ua field set to "chrome"
to require Google Chrome's maximum
version must be 120.
string
Maximum
length: 63
ua-min-ver
Minimum version of the user agent
specified in dotted notation. For example,
use 90.0.1 with the ua field set to
"chrome" to require Google Chrome's
minimum version must be 90.0.1.
string
Maximum
length: 63
uuid
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not Specified
00000000-0000-0000-0000-000000000000
config header-group
Parameter
Description
Type
Size
Default
case-sensitivity
Case sensitivity in pattern.
option
-disable
Option
Description
disable
Case insensitive in pattern.
enable
Case sensitive in pattern.
header
HTTP header regular expression.
string
Maximum
length: 255
header-name
HTTP header.
string
Maximum
length: 79
id
ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
FortiOS 8.0.0 CLI Reference
653
Fortinet Inc.

---


<!-- 来源页 654 -->
config tagging
Parameter
Description
Type
Size
Default
category
Tag category.
string
Maximum
length: 63
name
Tagging entry name.
string
Maximum
length: 63
tags <name>
Tags.
Tag name.
string
Maximum
length: 79
config firewall proxy-addrgrp
Configure web proxy address group.
config firewall proxy-addrgrp
Description: Configure web proxy address group.
edit <name>
set color {integer}
set comment {var-string}
set custom-tags <name1>, <name2>, ...
set display-with [all-tags|first-tag-only|...]
set member <name1>, <name2>, ...
config tagging
Description: Config object tagging.
edit <name>
set category {string}
set tags <name1>, <name2>, ...
next
end
set type [src|dst]
set uuid {uuid}
next
end
config firewall proxy-addrgrp
Parameter
Description
Type
Size
Default
color
Integer value to determine the color of the
icon in the GUI (1 - 32, default = 0, which sets
value to 1).
integer
Minimum
value: 0
Maximum
value: 32
0
comment
Optional comments.
var-string
Maximum
length: 255
FortiOS 8.0.0 CLI Reference
654
Fortinet Inc.

<!-- 来源页 655 -->
Parameter
Description
Type
Size
Default
custom-tags
<name> *
Custom tags.
Names of custom tags used with this
address.
string
Maximum
length: 35
display-with
*
Display object with first tag, all tags, or just
the icon.
option
-all-tags
Option
Description
all-tags
Display object using all custom tags.
first-tag-only
Display object using first custom tag.
icon-and-color
Display object using icon and color.
member
<name>
Members of address group.
Address name.
string
Maximum
length: 79
name
Address group name.
string
Maximum
length: 79
type
Source or destination address group type.
option
-src
Option
Description
src
Source group.
dst
Destination group.
uuid
Universally Unique Identifier (UUID;
automatically assigned but can be manually
reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
config tagging
Parameter
Description
Type
Size
Default
category
Tag category.
string
Maximum
length: 63
name
Tagging entry name.
string
Maximum
length: 63
tags <name>
Tags.
Tag name.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
655
Fortinet Inc.

---


<!-- 来源页 656 -->
config firewall proxy-addrgrp6
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
Configure web proxy address group6.
config firewall proxy-addrgrp6
Description: Configure web proxy address group6.
edit <name>
set color {integer}
set comment {var-string}
set custom-tags <name1>, <name2>, ...
set display-with [all-tags|first-tag-only|...]
set member <name1>, <name2>, ...
config tagging
Description: Config object tagging.
edit <name>
set category {string}
set tags <name1>, <name2>, ...
next
end
set type [src|dst]
set uuid {uuid}
FortiOS 8.0.0 CLI Reference
656
Fortinet Inc.

<!-- 来源页 657 -->
next
end
config firewall proxy-addrgrp6
Parameter
Description
Type
Size
Default
color
Integer value to determine the color of the
icon in the GUI (1 - 32, default = 0, which sets
value to 1).
integer
Minimum
value: 0
Maximum
value: 32
0
comment
Optional comments.
var-string
Maximum
length: 255
custom-tags
<name>
Custom tags.
Names of custom tags used with this
address.
string
Maximum
length: 35
display-with
Display object with first tag, all tags, or just
the icon.
option
-all-tags
Option
Description
all-tags
Display object using all custom tags.
first-tag-only
Display object using first custom tag.
icon-and-color
Display object using icon and color.
member
<name>
Members of address group6.
Address name.
string
Maximum
length: 79
name
Address group6.
string
Maximum
length: 79
type
Source or destination address group6 type.
option
-src
Option
Description
src
Source group.
dst
Destination group.
uuid
Universally Unique Identifier (UUID;
automatically assigned but can be manually
reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
FortiOS 8.0.0 CLI Reference
657
Fortinet Inc.

---


<!-- 来源页 658 -->
config tagging
Parameter
Description
Type
Size
Default
category
Tag category.
string
Maximum
length: 63
name
Tagging entry name.
string
Maximum
length: 63
tags <name>
Tags.
Tag name.
string
Maximum
length: 79
config firewall proxy-policy
Configure proxy policies.
config firewall proxy-policy
Description: Configure proxy policies.
edit <policyid>
set access-proxy <name1>, <name2>, ...
set access-proxy6 <name1>, <name2>, ...
set action [accept|deny|...]
set application-list {string}
set av-profile {string}
set block-notification [enable|disable]
set casb-profile {string}
set comments {var-string}
set custom-tags <name1>, <name2>, ...
set decrypted-traffic-mirror {string}
set detect-https-in-http-request [enable|disable]
set device-ownership [enable|disable]
set disclaimer [disable|domain|...]
set dlp-profile {string}
set dnsfilter-profile {string}
set dstaddr <name1>, <name2>, ...
set dstaddr-negate [enable|disable]
set dstaddr6 <name1>, <name2>, ...
set dstintf <name1>, <name2>, ...
set emailfilter-profile {string}
set file-filter-profile {string}
set fsso-groups <name1>, <name2>, ...
set groups <name1>, <name2>, ...
set http-tunnel-auth [enable|disable]
set https-sub-category [enable|disable]
set icap-profile {string}
set internet-service [enable|disable]
set internet-service-custom <name1>, <name2>, ...
set internet-service-custom-group <name1>, <name2>, ...
set internet-service-fortiguard <name1>, <name2>, ...
FortiOS 8.0.0 CLI Reference
658
Fortinet Inc.

<!-- 来源页 659 -->
set internet-service-group <name1>, <name2>, ...
set internet-service-name <name1>, <name2>, ...
set internet-service-negate [enable|disable]
set internet-service6 [enable|disable]
set internet-service6-custom <name1>, <name2>, ...
set internet-service6-custom-group <name1>, <name2>, ...
set internet-service6-fortiguard <name1>, <name2>, ...
set internet-service6-group <name1>, <name2>, ...
set internet-service6-name <name1>, <name2>, ...
set internet-service6-negate [enable|disable]
set ips-sensor {string}
set ips-voip-filter {string}
set isolator-server {string}
set llm-profile {string}
set log-http-transaction [enable|disable]
set logtraffic [all|utm|...]
set logtraffic-start [enable|disable]
set name {string}
set poolname <name1>, <name2>, ...
set poolname6 <name1>, <name2>, ...
set profile-group {string}
set profile-protocol-options {string}
set profile-type [single|group]
set proxy [explicit-web|transparent-web|...]
set redirect-url {var-string}
set replacemsg-override-group {string}
set schedule {string}
set service <name1>, <name2>, ...
set service-negate [enable|disable]
set session-ttl {integer}
set srcaddr <name1>, <name2>, ...
set srcaddr-negate [enable|disable]
set srcaddr6 <name1>, <name2>, ...
set srcintf <name1>, <name2>, ...
set ssh-filter-profile {string}
set ssh-policy-redirect [enable|disable]
set ssl-ssh-profile {string}
set status [enable|disable]
set transparent [enable|disable]
set url-risk <name1>, <name2>, ...
set users <name1>, <name2>, ...
set utm-status [enable|disable]
set uuid {uuid}
set videofilter-profile {string}
set waf-profile {string}
set webcache [enable|disable]
set webcache-https [disable|enable]
set webfilter-profile {string}
set webproxy-forward-server {string}
set webproxy-profile {string}
set ztna-destination <name1>, <name2>, ...
set ztna-ems-tag <name1>, <name2>, ...
FortiOS 8.0.0 CLI Reference
659
Fortinet Inc.

<!-- 来源页 660 -->
set ztna-ems-tag-negate [enable|disable]
set ztna-proxy <name1>, <name2>, ...
set ztna-tags-match-logic [or|and]
next
end
config firewall proxy-policy
Parameter
Description
Type
Size
Default
access-proxy
<name>
IPv4 access proxy.
string
Not Specified
**
access-proxy6
<name>
IPv6 access proxy.
string
Not Specified
**
action
Accept or deny traffic matching the
policy parameters.
option
-deny
Option
Description
accept
Action accept.
deny
Action deny.
redirect
Action redirect.
isolate
Action isolate.
application-list
Name of an existing Application list.
string
Maximum
length: 47
av-profile
Name of an existing Antivirus profile.
string
Maximum
length: 47
block-notification
Enable/disable block notification.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
casb-profile *
Name of an existing CASB profile.
string
Maximum
length: 47
comments
Optional comments.
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
FortiOS 8.0.0 CLI Reference
660
Fortinet Inc.

<!-- 来源页 661 -->
Parameter
Description
Type
Size
Default
decrypted-traffic-mirror
Decrypted traffic mirror.
string
Maximum
length: 35
detect-https-in-http-request
Enable/disable detection of HTTPS in
HTTP request.
option
-disable
Option
Description
enable
Enable detection of HTTPS in HTTP request.
disable
Disable detection of HTTPS in HTTP request.
device-ownership
When enabled, the ownership
enforcement will be done at policy level.
option
-disable
Option
Description
enable
Enable device ownership.
disable
Disable device ownership.
disclaimer
Web proxy disclaimer setting: by
domain, policy, or user.
option
-disable
Option
Description
disable
Disable disclaimer.
domain
Display disclaimer for domain
policy
Display disclaimer for policy
user
Display disclaimer for current user
dlp-profile
Name of an existing DLP profile.
string
Maximum
length: 47
dnsfilter-profile
Name of an existing DNS filter profile.
string
Maximum
length: 47
dstaddr
<name>
Destination address objects.
Address name.
string
Maximum
length: 79
dstaddr-negate
When enabled, destination addresses
match against any address EXCEPT the
specified destination addresses.
option
-disable
Option
Description
enable
Enable source address negate.
disable
Disable destination address negate.
FortiOS 8.0.0 CLI Reference
661
Fortinet Inc.

<!-- 来源页 662 -->
Parameter
Description
Type
Size
Default
dstaddr6
<name>
IPv6 destination address objects.
Address name.
string
Maximum
length: 79
dstintf <name>
Destination interface names.
Interface name.
string
Maximum
length: 79
emailfilter-profile
Name of an existing email filter profile.
string
Maximum
length: 47
file-filter-profile
Name of an existing file-filter profile.
string
Maximum
length: 47
fsso-groups
<name> *
Names of FSSO groups.
FSSO Group name.
string
Maximum
length: 511
groups <name>
Names of group objects.
Group name.
string
Maximum
length: 79
http-tunnel-auth
Enable/disable HTTP tunnel
authentication.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
https-sub-category
Enable/disable HTTPS sub-category
policy matching.
option
-disable
Option
Description
enable
Enable HTTPS sub-category policy matching.
disable
Disable HTTPS sub-category policy matching.
icap-profile *
Name of an existing ICAP profile.
string
Maximum
length: 47
internet-service
Enable/disable use of Internet Services
for this policy. If enabled, destination
address and service are not used.
option
-disable
Option
Description
enable
Enable use of Internet Services in policy.
disable
Disable use of Internet Services in policy.
internet-service-custom <name>
Custom Internet Service name.
Custom Internet Service name.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
662
Fortinet Inc.

<!-- 来源页 663 -->
Parameter
Description
Type
Size
Default
internet-service-custom-group
<name>
Custom Internet Service group name.
Custom Internet Service group name.
string
Maximum
length: 79
internet-service-fortiguard
<name>
FortiGuard Internet Service name.
FortiGuard Internet Service name.
string
Maximum
length: 79
internet-service-group
<name>
Internet Service group name.
Internet Service group name.
string
Maximum
length: 79
internet-service-name
<name>
Internet Service name.
Internet Service name.
string
Maximum
length: 79
internet-service-negate
When enabled, Internet Services match
against any internet service EXCEPT the
selected Internet Service.
option
-disable
Option
Description
enable
Enable negated Internet Service match.
disable
Disable negated Internet Service match.
internet-service6
Enable/disable use of Internet Services
IPv6 for this policy. If enabled,
destination IPv6 address and service are
not used.
option
-disable
Option
Description
enable
Enable use of IPv6 Internet Services in policy.
disable
Disable use of IPv6 Internet Services in policy.
internet-service6-custom <name>
Custom Internet Service IPv6 name.
Custom Internet Service IPv6 name.
string
Maximum
length: 79
internet-service6-custom-group
<name>
Custom Internet Service IPv6 group
name.
Custom Internet Service IPv6 group
name.
string
Maximum
length: 79
internet-service6-fortiguard
<name>
FortiGuard Internet Service IPv6 name.
FortiGuard Internet Service IPv6 name.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
663
Fortinet Inc.

<!-- 来源页 664 -->
Parameter
Description
Type
Size
Default
internet-service6-group <name>
Internet Service IPv6 group name.
Internet Service IPv6 group name.
string
Maximum
length: 79
internet-service6-name
<name>
Internet Service IPv6 name.
Internet Service IPv6 name.
string
Maximum
length: 79
internet-service6-negate
When enabled, Internet Services match
against any internet service IPv6
EXCEPT the selected Internet Service
IPv6.
option
-disable
Option
Description
enable
Enable negated IPv6 Internet Service match.
disable
Disable negated IPv6 Internet Service match.
ips-sensor
Name of an existing IPS sensor.
string
Maximum
length: 47
ips-voip-filter
Name of an existing VoIP (ips) profile.
string
Maximum
length: 47
isolator-server
Isolator server name.
string
Maximum
length: 63
llm-profile *
Name of an existing LLM profile.
string
Maximum
length: 47
log-http-transaction
Enable/disable HTTP transaction log.
option
-disable
Option
Description
enable
Enable HTTP transaction log.
disable
Disable HTTP transaction log.
logtraffic
Enable/disable logging traffic through
the policy.
option
-utm
Option
Description
all
Log all sessions.
utm
UTM event and matched application traffic log.
disable
Disable traffic and application log.
logtraffic-start
Enable/disable policy log traffic start.
option
-disable
FortiOS 8.0.0 CLI Reference
664
Fortinet Inc.

<!-- 来源页 665 -->
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
name
Policy name.
string
Maximum
length: 35
policyid
Policy ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
poolname
<name>
Name of IP pool object.
IP pool name.
string
Maximum
length: 79
poolname6
<name>
Name of IPv6 pool object.
IPv6 pool name.
string
Maximum
length: 79
profile-group
Name of profile group.
string
Maximum
length: 47
profile-protocol-options
Name of an existing Protocol options
profile.
string
Maximum
length: 47
default
profile-type
Determine whether the firewall policy
allows security profile groups or single
profiles only.
option
-single
Option
Description
single
Do not allow security profile groups.
group
Allow security profile groups.
proxy
Type of explicit proxy.
option
-Option
Description
explicit-web
Explicit Web Proxy
transparent-web
Transparent Web Proxy
ftp
Explicit FTP Proxy
ssh
SSH Proxy
ssh-tunnel
SSH Tunnel
access-proxy
Access Proxy
FortiOS 8.0.0 CLI Reference
665
Fortinet Inc.

<!-- 来源页 666 -->
Parameter
Description
Type
Size
Default
Option
Description
ztna-proxy
ZTNA Proxy
wanopt
WANopt Tunnel
redirect-url
Redirect URL for further explicit web
proxy processing.
var-string
Maximum
length: 1023
replacemsg-override-group
Authentication replacement message
override group.
string
Maximum
length: 35
schedule
Name of schedule object.
string
Maximum
length: 35
service <name>
Name of service objects.
Service name.
string
Maximum
length: 79
service-negate
When enabled, services match against
any service EXCEPT the specified
destination services.
option
-disable
Option
Description
enable
Enable negated service match.
disable
Disable negated service match.
session-ttl
TTL in seconds for sessions accepted by
this policy (0 means use the system
default session TTL).
integer
Minimum value:
300 Maximum
value:
2764800
0
srcaddr
<name>
Source address objects.
Address name.
string
Maximum
length: 79
srcaddr-negate
When enabled, source addresses match
against any address EXCEPT the
specified source addresses.
option
-disable
Option
Description
enable
Enable source address negate.
disable
Disable destination address negate.
srcaddr6
<name>
IPv6 source address objects.
Address name.
string
Maximum
length: 79
srcintf <name>
Source interface names.
Interface name.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
666
Fortinet Inc.

<!-- 来源页 667 -->
Parameter
Description
Type
Size
Default
ssh-filter-profile *
Name of an existing SSH filter profile.
string
Maximum
length: 47
ssh-policy-redirect
Redirect SSH traffic to matching
transparent proxy policy.
option
-disable
Option
Description
enable
Enable SSH policy redirect.
disable
Disable SSH policy redirect.
ssl-ssh-profile
Name of an existing SSL SSH profile.
string
Maximum
length: 47
no-inspection
status
Enable/disable the active status of the
policy.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
transparent
Enable to use the IP address of the client
to connect to the server.
option
-disable
Option
Description
enable
Enable use of IP address of client to connect to server.
disable
Disable use of IP address of client to connect to server.
url-risk <name>
URL risk level name.
Risk level name.
string
Maximum
length: 79
users <name>
Names of user objects.
Group name.
string
Maximum
length: 79
utm-status
Enable the use of UTM
profiles/sensors/lists.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
uuid
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not Specified
00000000-0000-0000-0000-000000000000
FortiOS 8.0.0 CLI Reference
667
Fortinet Inc.

<!-- 来源页 668 -->
Parameter
Description
Type
Size
Default
videofilter-profile *
Name of an existing VideoFilter profile.
string
Maximum
length: 47
waf-profile *
Name of an existing Web application
firewall profile.
string
Maximum
length: 47
webcache *
Enable/disable web caching.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
webcache-https *
Enable/disable web caching for HTTPS
(Requires deep-inspection enabled in
ssl-ssh-profile).
option
-disable
Option
Description
disable
Disable web cache for HTTPS.
enable
Enable web cache for HTTPS.
webfilter-profile
Name of an existing Web filter profile.
string
Maximum
length: 47
webproxy-forward-server
Web proxy forward server name.
string
Maximum
length: 63
webproxy-profile
Name of web proxy profile.
string
Maximum
length: 63
ztna-destination
<name> *
ZTNA destinations (effective only with
ZTNA traffic-forward-proxy).
ZTNA destination name.
string
Maximum
length: 79
ztna-ems-tag
<name>
ZTNA EMS Tag names.
EMS Tag name.
string
Maximum
length: 79
ztna-ems-tag-negate
When enabled, ZTNA EMS tags match
against any tag EXCEPT the specified
ZTNA EMS tags.
option
-disable
Option
Description
enable
Enable ZTNA EMS tags negate.
disable
Disable ZTNA EMS tags negate.
ztna-proxy
<name>
ZTNA proxies.
ZTNA proxy name.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
668
Fortinet Inc.

---


<!-- 来源页 669 -->
Parameter
Description
Type
Size
Default
ztna-tags-match-logic
ZTNA tag matching logic.
option
-or
Option
Description
or
Match ZTNA tags using a logical OR operator.
and
Match ZTNA tags using a logical AND operator.
* This parameter may not exist in some models.
** Values may differ between models.
config firewall region
Define region table. Read-only.
config firewall region
Description: Define region table. Read-only.
edit <id>
set city <id1>, <id2>, ...
set name {string}
next
end
config firewall region
Parameter
Description
Type
Size
Default
city <id>
City ID list.
City ID.
integer
Minimum
value: 0
Maximum
value:
65535
id
Region ID.
integer
Minimum
value: 0
Maximum
value:
65535
0
name
Region name.
string
Maximum
length: 63
FortiOS 8.0.0 CLI Reference
669
Fortinet Inc.

---


<!-- 来源页 670 -->
config firewall schedule group
Schedule group configuration.
config firewall schedule group
Description: Schedule group configuration.
edit <name>
set color {integer}
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set member <name1>, <name2>, ...
set uuid {uuid}
next
end
config firewall schedule group
Parameter
Description
Type
Size
Default
color
Color of icon on the GUI.
integer
Minimum
value: 0
Maximum
value: 32
0
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
FortiOS 8.0.0 CLI Reference
670
Fortinet Inc.

---


<!-- 来源页 671 -->
Parameter
Description
Type
Size
Default
Option
Description
member
Source of truth for this object is a non-root member of fabric.
local
Source of truth for this object is this security fabric member.
root
Source of truth for this object is the root of the fabric.
member
<name>
Schedules added to the schedule group.
Schedule name.
string
Maximum
length: 79
name
Schedule group name.
string
Maximum
length: 31
uuid
Universally Unique Identifier (UUID;
automatically assigned but can be manually
reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
config firewall schedule onetime
Onetime schedule configuration.
config firewall schedule onetime
Description: Onetime schedule configuration.
edit <name>
set color {integer}
set end {user}
set end-utc {user}
set expiration-days {integer}
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set start {user}
set start-utc {user}
set uuid {uuid}
next
end
FortiOS 8.0.0 CLI Reference
671
Fortinet Inc.

<!-- 来源页 672 -->
config firewall schedule onetime
Parameter
Description
Type
Size
Default
color
Color of icon on the GUI.
integer
Minimum
value: 0
Maximum
value: 32
0
end
Schedule end date and time, format hh:mm
yyyy/mm/dd.
user
Not
Specified
end-utc
Schedule end date and time, in epoch
format.
user
Not
Specified
expiration-days
Write an event log message this many days
before the schedule expires.
integer
Minimum
value: 0
Maximum
value: 100
3
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
FortiOS 8.0.0 CLI Reference
672
Fortinet Inc.

---


<!-- 来源页 673 -->
Parameter
Description
Type
Size
Default
name
Onetime schedule name.
string
Maximum
length: 31
start
Schedule start date and time, format hh:mm
yyyy/mm/dd.
user
Not
Specified
start-utc
Schedule start date and time, in epoch
format.
user
Not
Specified
uuid
Universally Unique Identifier (UUID;
automatically assigned but can be manually
reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
config firewall schedule recurring
Recurring schedule configuration.
config firewall schedule recurring
Description: Recurring schedule configuration.
edit <name>
set color {integer}
set day {option1}, {option2}, ...
set end {user}
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set label-day [none|over-night|...]
set start {user}
set uuid {uuid}
next
end
config firewall schedule recurring
Parameter
Description
Type
Size
Default
color
Color of icon on the GUI.
integer
Minimum
value: 0
Maximum
value: 32
0
day
One or more days of the week on which the
schedule is valid. Separate the names of the
days with a space.
option
-none
FortiOS 8.0.0 CLI Reference
673
Fortinet Inc.

<!-- 来源页 674 -->
Parameter
Description
Type
Size
Default
Option
Description
sunday
Sunday.
monday
Monday.
tuesday
Tuesday.
wednesday
Wednesday.
thursday
Thursday.
friday
Friday.
saturday
Saturday.
none
None.
end
Time of day to end the schedule, format
hh:mm.
user
Not
Specified
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
FortiOS 8.0.0 CLI Reference
674
Fortinet Inc.

---


<!-- 来源页 675 -->
Parameter
Description
Type
Size
Default
label-day *
Configure a window during the time of day in
which the schedule job is executed.
option
-none
Option
Description
none
None.
over-night
1 AM - 4 AM
early-morning
4 AM - 7 AM.
morning
7 AM - 10 AM.
midday
10 AM - 1 PM.
afternoon
1 PM - 4 PM.
evening
4 PM - 7 PM.
night
7 PM - 10 PM.
late-night
10 PM - 1 AM.
name
Recurring schedule name.
string
Maximum
length: 31
start
Time of day to start the schedule, format
hh:mm.
user
Not
Specified
uuid
Universally Unique Identifier (UUID;
automatically assigned but can be manually
reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
config firewall security-policy
Configure NGFW IPv4/IPv6 application policies.
config firewall security-policy
Description: Configure NGFW IPv4/IPv6 application policies.
edit <policyid>
set action [accept|deny]
set app-category <id1>, <id2>, ...
set app-group <name1>, <name2>, ...
set application <id1>, <id2>, ...
set application-list {string}
set av-profile {string}
set casb-profile {string}
set comments {var-string}
set custom-tags <name1>, <name2>, ...
set diameter-filter-profile {string}
FortiOS 8.0.0 CLI Reference
675
Fortinet Inc.

<!-- 来源页 676 -->
set dlp-profile {string}
set dnsfilter-profile {string}
set dstaddr <name1>, <name2>, ...
set dstaddr-negate [enable|disable]
set dstaddr6 <name1>, <name2>, ...
set dstaddr6-negate [enable|disable]
set dstintf <name1>, <name2>, ...
set emailfilter-profile {string}
set enforce-default-app-port [enable|disable]
set file-filter-profile {string}
set fsso-groups <name1>, <name2>, ...
set groups <name1>, <name2>, ...
set icap-profile {string}
set internet-service [enable|disable]
set internet-service-custom <name1>, <name2>, ...
set internet-service-custom-group <name1>, <name2>, ...
set internet-service-fortiguard <name1>, <name2>, ...
set internet-service-group <name1>, <name2>, ...
set internet-service-name <name1>, <name2>, ...
set internet-service-negate [enable|disable]
set internet-service-src [enable|disable]
set internet-service-src-custom <name1>, <name2>, ...
set internet-service-src-custom-group <name1>, <name2>, ...
set internet-service-src-fortiguard <name1>, <name2>, ...
set internet-service-src-group <name1>, <name2>, ...
set internet-service-src-name <name1>, <name2>, ...
set internet-service-src-negate [enable|disable]
set internet-service6 [enable|disable]
set internet-service6-custom <name1>, <name2>, ...
set internet-service6-custom-group <name1>, <name2>, ...
set internet-service6-fortiguard <name1>, <name2>, ...
set internet-service6-group <name1>, <name2>, ...
set internet-service6-name <name1>, <name2>, ...
set internet-service6-negate [enable|disable]
set internet-service6-src [enable|disable]
set internet-service6-src-custom <name1>, <name2>, ...
set internet-service6-src-custom-group <name1>, <name2>, ...
set internet-service6-src-fortiguard <name1>, <name2>, ...
set internet-service6-src-group <name1>, <name2>, ...
set internet-service6-src-name <name1>, <name2>, ...
set internet-service6-src-negate [enable|disable]
set ips-sensor {string}
set ips-voip-filter {string}
set learning-mode [enable|disable]
set llm-profile {string}
set logtraffic [all|utm|...]
set name {string}
set nat46 [enable|disable]
set nat64 [enable|disable]
set profile-group {string}
set profile-protocol-options {string}
set profile-type [single|group]
FortiOS 8.0.0 CLI Reference
676
Fortinet Inc.

<!-- 来源页 677 -->
set schedule {string}
set sctp-filter-profile {string}
set send-deny-packet [disable|enable]
set service <name1>, <name2>, ...
set service-negate [enable|disable]
set srcaddr <name1>, <name2>, ...
set srcaddr-negate [enable|disable]
set srcaddr6 <name1>, <name2>, ...
set srcaddr6-negate [enable|disable]
set srcintf <name1>, <name2>, ...
set ssh-filter-profile {string}
set ssl-ssh-profile {string}
set status [enable|disable]
set url-category {user}
set users <name1>, <name2>, ...
set uuid {uuid}
set videofilter-profile {string}
set virtual-patch-profile {string}
set voip-profile {string}
set webfilter-profile {string}
next
end
config firewall security-policy
Parameter
Description
Type
Size
Default
action
Policy action (accept/deny).
option
-deny
Option
Description
accept
Allows session that match the firewall policy.
deny
Blocks sessions that match the firewall policy.
app-category
<id>
Application category ID list.
Category IDs.
integer
Minimum value:
0 Maximum
value:
4294967295
app-group
<name>
Application group names.
Application group names.
string
Maximum
length: 79
application
<id>
Application ID list.
Application IDs.
integer
Minimum value:
0 Maximum
value:
4294967295
application-list
Name of an existing Application list.
string
Maximum
length: 47
FortiOS 8.0.0 CLI Reference
677
Fortinet Inc.

<!-- 来源页 678 -->
Parameter
Description
Type
Size
Default
av-profile
Name of an existing Antivirus profile.
string
Maximum
length: 47
casb-profile *
Name of an existing CASB profile.
string
Maximum
length: 47
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
diameter-filter-profile
Name of an existing Diameter filter
profile.
string
Maximum
length: 47
dlp-profile
Name of an existing DLP profile.
string
Maximum
length: 47
dnsfilter-profile
Name of an existing DNS filter profile.
string
Maximum
length: 47
dstaddr
<name>
Destination IPv4 address name and
address group names.
Address name.
string
Maximum
length: 79
dstaddr-negate
When enabled dstaddr specifies what
the destination address must NOT be.
option
-disable
Option
Description
enable
Enable destination address negate.
disable
Disable destination address negate.
dstaddr6
<name>
Destination IPv6 address name and
address group names.
Address name.
string
Maximum
length: 79
dstaddr6-negate
When enabled dstaddr6 specifies what
the destination address must NOT be.
option
-disable
Option
Description
enable
Enable IPv6 destination address negate.
disable
Disable IPv6 destination address negate.
dstintf <name>
Outgoing (egress) interface.
Interface name.
string
Maximum
length: 79
emailfilter-profile
Name of an existing email filter profile.
string
Maximum
length: 47
FortiOS 8.0.0 CLI Reference
678
Fortinet Inc.

<!-- 来源页 679 -->
Parameter
Description
Type
Size
Default
enforce-default-app-port
Enable/disable default application port
enforcement for allowed applications.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
file-filter-profile
Name of an existing file-filter profile.
string
Maximum
length: 47
fsso-groups
<name>
Names of FSSO groups.
Names of FSSO groups.
string
Maximum
length: 511
groups
<name>
Names of user groups that can
authenticate with this policy.
User group name.
string
Maximum
length: 79
icap-profile *
Name of an existing ICAP profile.
string
Maximum
length: 47
internet-service
Enable/disable use of Internet Services
for this policy. If enabled, destination
address, service and default application
port enforcement are not used.
option
-disable
Option
Description
enable
Enable use of Internet Services in policy.
disable
Disable use of Internet Services in policy.
internet-service-custom
<name>
Custom Internet Service name.
Custom Internet Service name.
string
Maximum
length: 79
internet-service-custom-group
<name>
Custom Internet Service group name.
Custom Internet Service group name.
string
Maximum
length: 79
internet-service-fortiguard
<name>
FortiGuard Internet Service name.
FortiGuard Internet Service name.
string
Maximum
length: 79
internet-service-group
<name>
Internet Service group name.
Internet Service group name.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
679
Fortinet Inc.

<!-- 来源页 680 -->
Parameter
Description
Type
Size
Default
internet-service-name
<name>
Internet Service name.
Internet Service name.
string
Maximum
length: 79
internet-service-negate
When enabled internet-service specifies
what the service must NOT be.
option
-disable
Option
Description
enable
Enable negated Internet Service match.
disable
Disable negated Internet Service match.
internet-service-src
Enable/disable use of Internet Services
in source for this policy. If enabled,
source address is not used.
option
-disable
Option
Description
enable
Enable use of Internet Services source in policy.
disable
Disable use of Internet Services source in policy.
internet-service-src-custom
<name>
Custom Internet Service source name.
Custom Internet Service name.
string
Maximum
length: 79
internet-service-src-custom-group
<name>
Custom Internet Service source group
name.
Custom Internet Service group name.
string
Maximum
length: 79
internet-service-src-fortiguard
<name>
FortiGuard Internet Service source name.
FortiGuard Internet Service name.
string
Maximum
length: 79
internet-service-src-group <name>
Internet Service source group name.
Internet Service group name.
string
Maximum
length: 79
internet-service-src-name <name>
Internet Service source name.
Internet Service name.
string
Maximum
length: 79
internet-service-src-negate
When enabled internet-service-src
specifies what the service must NOT be.
option
-disable
FortiOS 8.0.0 CLI Reference
680
Fortinet Inc.

<!-- 来源页 681 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable negated Internet Service source match.
disable
Disable negated Internet Service source match.
internet-service6
Enable/disable use of IPv6 Internet
Services for this policy. If enabled,
destination address, service and default
application port enforcement are not
used.
option
-disable
Option
Description
enable
Enable use of IPv6 Internet Services in policy.
disable
Disable use of IPv6 Internet Services in policy.
internet-service6-custom
<name>
Custom IPv6 Internet Service name.
Custom IPv6 Internet Service name.
string
Maximum
length: 79
internet-service6-custom-group
<name>
Custom IPv6 Internet Service group
name.
Custom IPv6 Internet Service group
name.
string
Maximum
length: 79
internet-service6-fortiguard
<name>
FortiGuard IPv6 Internet Service name.
FortiGuard Internet Service name.
string
Maximum
length: 79
internet-service6-group <name>
Internet Service group name.
Internet Service group name.
string
Maximum
length: 79
internet-service6-name <name>
IPv6 Internet Service name.
IPv6 Internet Service name.
string
Maximum
length: 79
internet-service6-negate
When enabled internet-service6
specifies what the service must NOT be.
option
-disable
Option
Description
enable
Enable negated IPv6 Internet Service match.
disable
Disable negated IPv6 Internet Service match.
FortiOS 8.0.0 CLI Reference
681
Fortinet Inc.

<!-- 来源页 682 -->
Parameter
Description
Type
Size
Default
internet-service6-src
Enable/disable use of IPv6 Internet
Services in source for this policy. If
enabled, source address is not used.
option
-disable
Option
Description
enable
Enable use of IPv6 Internet Services source in policy.
disable
Disable use of IPv6 Internet Services source in policy.
internet-service6-src-custom
<name>
Custom IPv6 Internet Service source
name.
Custom Internet Service name.
string
Maximum
length: 79
internet-service6-src-custom-group
<name>
Custom Internet Service6 source group
name.
Custom Internet Service6 group name.
string
Maximum
length: 79
internet-service6-src-fortiguard
<name>
FortiGuard IPv6 Internet Service source
name.
FortiGuard Internet Service name.
string
Maximum
length: 79
internet-service6-src-group <name>
Internet Service6 source group name.
Internet Service group name.
string
Maximum
length: 79
internet-service6-src-name <name>
IPv6 Internet Service source name.
Internet Service name.
string
Maximum
length: 79
internet-service6-src-negate
When enabled internet-service6-src
specifies what the service must NOT be.
option
-disable
Option
Description
enable
Enable negated IPv6 Internet Service source match.
disable
Disable negated IPv6 Internet Service source match.
ips-sensor
Name of an existing IPS sensor.
string
Maximum
length: 47
ips-voip-filter
Name of an existing VoIP (ips) profile.
string
Maximum
length: 47
FortiOS 8.0.0 CLI Reference
682
Fortinet Inc.

<!-- 来源页 683 -->
Parameter
Description
Type
Size
Default
learning-mode
Enable to allow everything, but log all of
the meaningful data for security
information gathering. A learning report
will be generated.
option
-disable
Option
Description
enable
Enable learning mode.
disable
Disable learning mode.
llm-profile *
Name of an existing LLM profile.
string
Maximum
length: 47
logtraffic
Enable or disable logging. Log all
sessions or security profile sessions.
option
-utm
Option
Description
all
Log all sessions accepted or denied by this policy.
utm
Log traffic that has a security profile applied to it.
disable
Disable all logging for this policy.
name
Policy name.
string
Maximum
length: 35
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
Option
Description
enable
Enable NAT64.
disable
Disable NAT64.
policyid
Policy ID.
integer
Minimum value:
0 Maximum
value:
4294967294
0
profile-group
Name of profile group.
string
Maximum
length: 47
FortiOS 8.0.0 CLI Reference
683
Fortinet Inc.

<!-- 来源页 684 -->
Parameter
Description
Type
Size
Default
profile-protocol-options
Name of an existing Protocol options
profile.
string
Maximum
length: 47
default
profile-type
Determine whether the firewall policy
allows security profile groups or single
profiles only.
option
-single
Option
Description
single
Do not allow security profile groups.
group
Allow security profile groups.
schedule
Schedule name.
string
Maximum
length: 35
sctp-filter-profile
Name of an existing SCTP filter profile.
string
Maximum
length: 47
send-deny-packet
Enable to send a reply when a session is
denied or blocked by a firewall policy.
option
-disable
Option
Description
disable
Disable deny-packet sending.
enable
Enable deny-packet sending.
service
<name>
Service and service group names.
Service name.
string
Maximum
length: 79
service-negate
When enabled service specifies what the
service must NOT be.
option
-disable
Option
Description
enable
Enable negated service match.
disable
Disable negated service match.
srcaddr
<name>
Source IPv4 address name and address
group names.
Address name.
string
Maximum
length: 79
srcaddr-negate
When enabled srcaddr specifies what
the source address must NOT be.
option
-disable
Option
Description
enable
Enable source address negate.
disable
Disable source address negate.
FortiOS 8.0.0 CLI Reference
684
Fortinet Inc.

<!-- 来源页 685 -->
Parameter
Description
Type
Size
Default
srcaddr6
<name>
Source IPv6 address name and address
group names.
Address name.
string
Maximum
length: 79
srcaddr6-negate
When enabled srcaddr6 specifies what
the source address must NOT be.
option
-disable
Option
Description
enable
Enable IPv6 source address negate.
disable
Disable IPv6 source address negate.
srcintf <name>
Incoming (ingress) interface.
Interface name.
string
Maximum
length: 79
ssh-filter-profile *
Name of an existing SSH filter profile.
string
Maximum
length: 47
ssl-ssh-profile
Name of an existing SSL SSH profile.
string
Maximum
length: 47
no-inspection
status
Enable or disable this policy.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
url-category
URL categories or groups.
user
Not Specified
users <name>
Names of individual users that can
authenticate with this policy.
User name.
string
Maximum
length: 79
uuid
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not Specified
00000000-0000-0000-0000-000000000000
videofilter-profile *
Name of an existing VideoFilter profile.
string
Maximum
length: 47
virtual-patch-profile
Name of an existing virtual-patch profile.
string
Maximum
length: 47
voip-profile
Name of an existing VoIP (voipd) profile.
string
Maximum
length: 47
webfilter-profile
Name of an existing Web filter profile.
string
Maximum
length: 47
* This parameter may not exist in some models.
FortiOS 8.0.0 CLI Reference
685
Fortinet Inc.

---


<!-- 来源页 686 -->
config firewall service category
Configure service categories.
config firewall service category
Description: Configure service categories.
edit <name>
set comment {var-string}
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set uuid {uuid}
next
end
config firewall service category
Parameter
Description
Type
Size
Default
comment
Comment.
var-string
Maximum
length: 255
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
FortiOS 8.0.0 CLI Reference
686
Fortinet Inc.

---


<!-- 来源页 687 -->
Parameter
Description
Type
Size
Default
Option
Description
local
Source of truth for this object is this security fabric member.
root
Source of truth for this object is the root of the fabric.
name
Service category name.
string
Maximum
length: 63
uuid
Universally Unique Identifier (UUID;
automatically assigned but can be manually
reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
config firewall service custom
Configure custom services.
config firewall service custom
Description: Configure custom services.
edit <name>
set app-category <id1>, <id2>, ...
set app-service-type [disable|app-id|...]
set application <id1>, <id2>, ...
set category {string}
set check-reset-range [disable|strict|...]
set color {integer}
set comment {var-string}
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set fqdn {string}
set helper [auto|disable|...]
set icmpcode {integer}
set icmptype {integer}
set iprange {user}
set protocol [TCP/UDP/UDP-Lite/SCTP|ICMP|...]
set protocol-number {integer}
set proxy [enable|disable]
set sctp-portrange {user}
set session-ttl {user}
set tcp-halfclose-timer {integer}
set tcp-halfopen-timer {integer}
set tcp-portrange {user}
set tcp-rst-timer {integer}
set tcp-timewait-timer {integer}
set udp-idle-timer {integer}
set udp-portrange {user}
FortiOS 8.0.0 CLI Reference
687
Fortinet Inc.

<!-- 来源页 688 -->
set udplite-portrange {user}
set uuid {uuid}
next
end
config firewall service custom
Parameter
Description
Type
Size
Default
app-category
<id>
Application category ID.
Application category id.
integer
Minimum value:
0 Maximum
value:
4294967295
app-service-type
Application service type.
option
-disable
Option
Description
disable
Disable application type.
app-id
Application ID.
app-category
Applicatin category.
application
<id>
Application ID.
Application id.
integer
Minimum value:
0 Maximum
value:
4294967295
category
Service category.
string
Maximum
length: 63
check-reset-range
Configure the type of ICMP error
message verification.
option
-default
Option
Description
disable
Disable RST range check.
strict
Check RST range strictly.
default
Using system default setting.
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
FortiOS 8.0.0 CLI Reference
688
Fortinet Inc.

<!-- 来源页 689 -->
Parameter
Description
Type
Size
Default
fabric-force-sync *
Enable/disable forced synchronization of
configuration objects from the root
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
fqdn
Fully qualified domain name.
string
Maximum
length: 255
helper
Helper name.
option
-auto
Option
Description
auto
Automatically select helper based on protocol and port.
disable
Disable helper.
ftp
FTP.
tftp
TFTP.
ras
RAS.
h323
H323.
FortiOS 8.0.0 CLI Reference
689
Fortinet Inc.

<!-- 来源页 690 -->
Parameter
Description
Type
Size
Default
Option
Description
tns
TNS.
mms
MMS.
sip
SIP.
pptp
PPTP.
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
icmpcode
ICMP code.
integer
Minimum value:
0 Maximum
value: 255
icmptype
ICMP type.
integer
Minimum value:
0 Maximum
value:
4294967295
iprange
Start and end of the IP range associated
with service.
user
Not Specified
name
Custom service name.
string
Maximum
length: 79
protocol
Protocol type based on IANA numbers.
option
-TCP/UDP/UDP-Lite/SCTP
Option
Description
TCP/UDP/UDP-Lite/SCTP
TCP, UDP, UDP-Lite and SCTP.
ICMP
ICMP.
ICMP6
ICMP6.
IP
IP.
HTTP
HTTP - for web proxy.
FTP
FTP - for web proxy.
FortiOS 8.0.0 CLI Reference
690
Fortinet Inc.

<!-- 来源页 691 -->
Parameter
Description
Type
Size
Default
Option
Description
CONNECT
Connect - for web proxy.
SOCKS-TCP
Socks TCP - for web proxy.
SOCKS-UDP
Socks UDP - for web proxy.
ALL
All - for web proxy.
protocol-number
IP protocol number.
integer
Minimum value:
0 Maximum
value: 254
0
proxy
Enable/disable web proxy service.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
sctp-portrange
Multiple SCTP port ranges.
user
Not Specified
session-ttl
Session TTL (300 - 2764800, 0 =
default).
user
Not Specified
tcp-halfclose-timer
Wait time to close a TCP session waiting
for an unanswered FIN packet (1 - 86400
sec, 0 = default).
integer
Minimum value:
0 Maximum
value: 86400
0
tcp-halfopen-timer
Wait time to close a TCP session waiting
for an unanswered open session packet
(1 - 86400 sec, 0 = default).
integer
Minimum value:
0 Maximum
value: 86400
0
tcp-portrange
Multiple TCP port ranges.
user
Not Specified
tcp-rst-timer
Set the length of the TCP CLOSE state in
seconds (5 - 300 sec, 0 = default).
integer
Minimum value:
5 Maximum
value: 300
0
tcp-timewait-timer
Set the length of the TCP TIME-WAIT
state in seconds (1 - 300 sec, 0 =
default).
integer
Minimum value:
0 Maximum
value: 300
0
udp-idle-timer
Number of seconds before an idle
UDP/UDP-Lite connection times out (0 -86400 sec, 0 = default).
integer
Minimum value:
0 Maximum
value: 86400
0
udp-portrange
Multiple UDP port ranges.
user
Not Specified
FortiOS 8.0.0 CLI Reference
691
Fortinet Inc.

---


<!-- 来源页 692 -->
Parameter
Description
Type
Size
Default
udplite-portrange
Multiple UDP-Lite port ranges.
user
Not Specified
uuid
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
config firewall service group
Configure service groups.
config firewall service group
Description: Configure service groups.
edit <name>
set color {integer}
set comment {var-string}
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set member <name1>, <name2>, ...
set proxy [enable|disable]
set uuid {uuid}
next
end
config firewall service group
Parameter
Description
Type
Size
Default
color
Color of icon on the GUI.
integer
Minimum
value: 0
Maximum
value: 32
0
comment
Comment.
var-string
Maximum
length: 255
fabric-force-sync *
Enable/disable forced synchronization of
configuration objects from the root FortiGate
unit to the downstream devices.
Configuration conflict check is skipped.
option
-disable
FortiOS 8.0.0 CLI Reference
692
Fortinet Inc.

---


<!-- 来源页 723 -->
Parameter
Description
Type
Size
Default
ssl-min-version
Lowest SSL/TLS version to negotiate.
option
-tls-1.1
Option
Description
tls-1.0
TLS 1.0.
tls-1.1
TLS 1.1.
tls-1.2
TLS 1.2.
tls-1.3
TLS 1.3.
ssl-mode
SSL/TLS mode for encryption and decryption of
traffic.
option
-full
Option
Description
half
Client to FortiGate SSL.
full
Client to FortiGate and FortiGate to Server SSL.
ssl-send-empty-frags
Enable/disable sending empty fragments to avoid
attack on CBC IV.
option
-enable
Option
Description
enable
Send empty fragments.
disable
Do not send empty fragments.
url-rewrite
Enable/disable rewriting the URL.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
config firewall ssl-ssh-profile
Configure SSL/SSH protocol options.
config firewall ssl-ssh-profile
Description: Configure SSL/SSH protocol options.
edit <name>
set allowlist [enable|disable]
set block-blocklisted-certificates [disable|enable]
set caname {string}
set comment {var-string}
config dot
Description: Configure DNS over TLS options.
FortiOS 8.0.0 CLI Reference
723
Fortinet Inc.

<!-- 来源页 724 -->
set cert-validation-failure [allow|block|...]
set cert-validation-timeout [allow|block|...]
set client-certificate [bypass|inspect|...]
set expired-server-cert [allow|block|...]
set proxy-after-tcp-handshake [enable|disable]
set quic [inspect|bypass|...]
set revoked-server-cert [allow|block|...]
set sni-server-cert-check [enable|strict|...]
set status [disable|deep-inspection]
set udp-not-quic [allow|block]
set unsupported-ssl-cipher [allow|block]
set unsupported-ssl-negotiation [allow|block]
set unsupported-ssl-version [allow|block]
set untrusted-server-cert [allow|block|...]
end
config ech-outer-sni
Description: ClientHelloOuter SNIs to be blocked.
edit <name>
set sni {string}
next
end
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
config ftps
Description: Configure FTPS options.
set cert-validation-failure [allow|block|...]
set cert-validation-timeout [allow|block|...]
set client-certificate [bypass|inspect|...]
set expired-server-cert [allow|block|...]
set min-allowed-ssl-version [ssl-3.0|tls-1.0|...]
set ports {integer}
set revoked-server-cert [allow|block|...]
set sni-server-cert-check [enable|strict|...]
set status [disable|deep-inspection]
set unsupported-ssl-cipher [allow|block]
set unsupported-ssl-negotiation [allow|block]
set unsupported-ssl-version [allow|block]
set untrusted-server-cert [allow|block|...]
end
config https
Description: Configure HTTPS options.
set cert-probe-failure [allow|block]
set cert-validation-failure [allow|block|...]
set cert-validation-timeout [allow|block|...]
set client-certificate [bypass|inspect|...]
set encrypted-client-hello [allow|block]
set expired-server-cert [allow|block|...]
set min-allowed-ssl-version [ssl-3.0|tls-1.0|...]
set ports {integer}
set proxy-after-tcp-handshake [enable|disable]
set quic [inspect|bypass|...]
FortiOS 8.0.0 CLI Reference
724
Fortinet Inc.

<!-- 来源页 725 -->
set revoked-server-cert [allow|block|...]
set sni-server-cert-check [enable|strict|...]
set status [disable|certificate-inspection|...]
set udp-not-quic [allow|block]
set unsupported-ssl-cipher [allow|block]
set unsupported-ssl-negotiation [allow|block]
set unsupported-ssl-version [allow|block]
set untrusted-server-cert [allow|block|...]
end
config imaps
Description: Configure IMAPS options.
set cert-validation-failure [allow|block|...]
set cert-validation-timeout [allow|block|...]
set client-certificate [bypass|inspect|...]
set expired-server-cert [allow|block|...]
set ports {integer}
set proxy-after-tcp-handshake [enable|disable]
set revoked-server-cert [allow|block|...]
set sni-server-cert-check [enable|strict|...]
set status [disable|deep-inspection]
set unsupported-ssl-cipher [allow|block]
set unsupported-ssl-negotiation [allow|block]
set unsupported-ssl-version [allow|block]
set untrusted-server-cert [allow|block|...]
end
set mapi-over-https [enable|disable]
config pop3s
Description: Configure POP3S options.
set cert-validation-failure [allow|block|...]
set cert-validation-timeout [allow|block|...]
set client-certificate [bypass|inspect|...]
set expired-server-cert [allow|block|...]
set ports {integer}
set proxy-after-tcp-handshake [enable|disable]
set revoked-server-cert [allow|block|...]
set sni-server-cert-check [enable|strict|...]
set status [disable|deep-inspection]
set unsupported-ssl-cipher [allow|block]
set unsupported-ssl-negotiation [allow|block]
set unsupported-ssl-version [allow|block]
set untrusted-server-cert [allow|block|...]
end
set rpc-over-https [enable|disable]
set server-cert <name1>, <name2>, ...
set server-cert-mode [re-sign|replace]
config smtps
Description: Configure SMTPS options.
set cert-validation-failure [allow|block|...]
set cert-validation-timeout [allow|block|...]
set client-certificate [bypass|inspect|...]
set expired-server-cert [allow|block|...]
set ports {integer}
FortiOS 8.0.0 CLI Reference
725
Fortinet Inc.

<!-- 来源页 726 -->
set proxy-after-tcp-handshake [enable|disable]
set revoked-server-cert [allow|block|...]
set sni-server-cert-check [enable|strict|...]
set status [disable|deep-inspection]
set unsupported-ssl-cipher [allow|block]
set unsupported-ssl-negotiation [allow|block]
set unsupported-ssl-version [allow|block]
set untrusted-server-cert [allow|block|...]
end
config ssh
Description: Configure SSH options.
set inspect-all [disable|deep-inspection]
set ports {integer}
set proxy-after-tcp-handshake [enable|disable]
set ssh-algorithm [compatible|high-encryption]
set ssh-tun-policy-check [disable|enable]
set status [disable|deep-inspection]
set unsupported-version [bypass|block]
end
config ssl
Description: Configure SSL options.
set cert-probe-failure [allow|block]
set cert-validation-failure [allow|block|...]
set cert-validation-timeout [allow|block|...]
set client-certificate [bypass|inspect|...]
set encrypted-client-hello [allow|block]
set expired-server-cert [allow|block|...]
set inspect-all [disable|certificate-inspection|...]
set min-allowed-ssl-version [ssl-3.0|tls-1.0|...]
set revoked-server-cert [allow|block|...]
set sni-server-cert-check [enable|strict|...]
set unsupported-ssl-cipher [allow|block]
set unsupported-ssl-negotiation [allow|block]
set unsupported-ssl-version [allow|block]
set untrusted-server-cert [allow|block|...]
end
set ssl-anomaly-log [disable|enable]
config ssl-exempt
Description: Servers to exempt from SSL inspection.
edit <id>
set address {string}
set address6 {string}
set fortiguard-category {integer}
set regex {string}
set type [fortiguard-category|address|...]
set wildcard-fqdn {string}
next
end
set ssl-exemption-ip-rating [enable|disable]
set ssl-exemption-log [disable|enable]
set ssl-handshake-log [disable|enable]
set ssl-negotiation-log [disable|enable]
FortiOS 8.0.0 CLI Reference
726
Fortinet Inc.

<!-- 来源页 727 -->
config ssl-server
Description: SSL server settings used for client certificate request.
edit <id>
set ftps-client-certificate [bypass|inspect|...]
set https-client-certificate [bypass|inspect|...]
set imaps-client-certificate [bypass|inspect|...]
set ip {ipv4-address-any}
set pop3s-client-certificate [bypass|inspect|...]
set smtps-client-certificate [bypass|inspect|...]
set ssl-other-client-certificate [bypass|inspect|...]
next
end
set ssl-server-cert-log [disable|enable]
set supported-alpn [http1-1|http2|...]
set untrusted-caname {string}
set use-ssl-server [disable|enable]
set uuid {uuid}
next
end
config firewall ssl-ssh-profile
Parameter
Description
Type
Size
Default
allowlist
Enable/disable exempting servers by
FortiGuard allowlist.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
block-blocklisted-certificates
Enable/disable blocking SSL-based botnet
communication by FortiGuard certificate
blocklist.
option
-enable
Option
Description
disable
Disable FortiGuard certificate blocklist.
enable
Enable FortiGuard certificate blocklist.
caname
CA certificate used by SSL Inspection.
string
Maximum
length: 35
Fortinet_CA_SSL
comment
Optional comments.
var-string
Maximum
length: 255
FortiOS 8.0.0 CLI Reference
727
Fortinet Inc.

<!-- 来源页 728 -->
Parameter
Description
Type
Size
Default
fabric-force-sync *
Enable/disable forced synchronization of
configuration objects from the root
FortiGate unit to the downstream devices.
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
fabric-object *
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
mapi-over-https
Enable/disable inspection of MAPI over
HTTPS.
option
-disable
Option
Description
enable
Enable inspection of MAPI over HTTPS.
disable
Disable inspection of MAPI over HTTPS.
name
Name.
string
Maximum
length: 47
rpc-over-https
Enable/disable inspection of RPC over
HTTPS.
option
-disable
Option
Description
enable
Enable inspection of RPC over HTTPS.
disable
Disable inspection of RPC over HTTPS.
FortiOS 8.0.0 CLI Reference
728
Fortinet Inc.

<!-- 来源页 729 -->
Parameter
Description
Type
Size
Default
server-cert
<name>
Certificate used by SSL Inspection to
replace server certificate.
Certificate list.
string
Maximum
length: 79
server-cert-mode
Re-sign or replace the server's certificate.
option
-re-sign
Option
Description
re-sign
Multiple clients connecting to multiple servers.
replace
Protect an SSL server.
ssl-anomaly-log
Enable/disable logging of SSL anomalies.
option
-enable
Option
Description
disable
Disable logging of SSL anomalies.
enable
Enable logging of SSL anomalies.
ssl-exemption-ip-rating
Enable/disable IP based URL rating.
option
-enable
Option
Description
enable
Enable IP based URL rating.
disable
Disable IP based URL rating.
ssl-exemption-log
Enable/disable logging of SSL exemptions.
option
-disable
Option
Description
disable
Disable logging of SSL exemptions.
enable
Enable logging of SSL exemptions.
ssl-handshake-log
Enable/disable logging of TLS handshakes.
option
-disable
Option
Description
disable
Disable logging of TLS handshakes.
enable
Enable logging of TLS handshakes.
FortiOS 8.0.0 CLI Reference
729
Fortinet Inc.

<!-- 来源页 730 -->
Parameter
Description
Type
Size
Default
ssl-negotiation-log
Enable/disable logging of SSL negotiation
events.
option
-enable
Option
Description
disable
Disable logging of SSL negotiation events.
enable
Enable logging of SSL negotiation events.
ssl-server-cert-log
Enable/disable logging of server certificate
information.
option
-disable
Option
Description
disable
Disable logging of server certificate information.
enable
Enable logging of server certificate information.
supported-alpn
Configure ALPN option.
option
-all
Option
Description
http1-1
Enable all ALPN including HTTP1.1 except HTTP2 and SPDY.
http2
Enable all ALPN including HTTP2 except HTTP1.1 and SPDY.
all
Allow all ALPN extensions except SPDY.
none
Do not use ALPN.
untrusted-caname
Untrusted CA certificate used by SSL
Inspection.
string
Maximum
length: 35
Fortinet_CA_
Untrusted
use-ssl-server
Enable/disable the use of SSL server table
for SSL offloading.
option
-disable
Option
Description
disable
Don't use SSL server configuration.
enable
Use SSL server configuration.
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be manually
reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
FortiOS 8.0.0 CLI Reference
730
Fortinet Inc.

<!-- 来源页 731 -->
config dot
Parameter
Description
Type
Size
Default
cert-validation-failure
Action based on certificate validation failure.
option
-block
Option
Description
allow
Allow the server certificate.
block
Block the session.
ignore
Re-sign the server certificate as trusted.
cert-validation-timeout
Action based on certificate validation timeout.
option
-allow
Option
Description
allow
Allow the server certificate.
block
Block the session.
ignore
Re-sign the server certificate as trusted.
client-certificate
Action based on received client certificate.
option
-bypass
Option
Description
bypass
Bypass the session.
inspect
Inspect the session.
block
Block the session.
expired-server-cert
Action based on server certificate is expired.
option
-block
Option
Description
allow
Allow the server certificate.
block
Block the session.
ignore
Re-sign the server certificate as trusted.
proxy-after-tcp-handshake
Proxy traffic after the TCP 3-way handshake has
been established (not before).
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
731
Fortinet Inc.

<!-- 来源页 732 -->
Parameter
Description
Type
Size
Default
quic
QUIC inspection status (default = inspect).
option
-inspect
Option
Description
inspect
Inspect QUIC traffic.
bypass
Bypass QUIC traffic.
block
Block QUIC traffic.
revoked-server-cert
Action based on server certificate is revoked.
option
-block
Option
Description
allow
Allow the server certificate.
block
Block the session.
ignore
Re-sign the server certificate as trusted.
sni-server-cert-check
Check the SNI in the client hello message with the
CN or SAN fields in the returned server certificate.
option
-enable
Option
Description
enable
Check the SNI in the client hello message with the CN or SAN fields in
the returned server certificate. If mismatched, use the CN in the server
certificate to do URL filtering.
strict
Check the SNI in the client hello message with the CN or SAN fields in
the returned server certificate. If mismatched, close the connection.
disable
Do not check the SNI in the client hello message with the CN or SAN
fields in the returned server certificate.
status
Configure protocol inspection status.
option
-disable
Option
Description
disable
Disable.
deep-inspection
Full SSL inspection.
udp-not-quic
Action to be taken when matched UDP packet is
not QUIC.
option
-allow
Option
Description
allow
Bypass the session when UDP packet is not QUIC.
block
Block the session when UDP packet is not QUIC.
FortiOS 8.0.0 CLI Reference
732
Fortinet Inc.

<!-- 来源页 733 -->
Parameter
Description
Type
Size
Default
unsupported-ssl-cipher
Action based on the SSL cipher used being
unsupported.
option
-allow
Option
Description
allow
Bypass the session when the cipher is not supported.
block
Block the session when the cipher is not supported.
unsupported-ssl-negotiation
Action based on the SSL negotiation used being
unsupported.
option
-allow
Option
Description
allow
Bypass the session when the negotiation is not supported.
block
Block the session when the negotiation is not supported.
unsupported-ssl-version
Action based on the SSL version used being
unsupported.
option
-block
Option
Description
allow
Bypass the session when the version is not supported.
block
Block the session when the version is not supported.
untrusted-server-cert
Action based on server certificate is not issued by
a trusted CA.
option
-allow
Option
Description
allow
Allow the server certificate.
block
Block the session.
ignore
Re-sign the server certificate as trusted.
config ech-outer-sni
Parameter
Description
Type
Size
Default
name
ClientHelloOuter SNI name.
string
Maximum
length: 79
sni
ClientHelloOuter SNI to be blocked.
string
Maximum
length: 255
FortiOS 8.0.0 CLI Reference
733
Fortinet Inc.

<!-- 来源页 734 -->
config ftps
Parameter
Description
Type
Size
Default
cert-validation-failure
Action based on certificate validation failure.
option
-block
Option
Description
allow
Allow the server certificate.
block
Block the session.
ignore
Re-sign the server certificate as trusted.
cert-validation-timeout
Action based on certificate validation timeout.
option
-allow
Option
Description
allow
Allow the server certificate.
block
Block the session.
ignore
Re-sign the server certificate as trusted.
client-certificate
Action based on received client certificate.
option
-bypass
Option
Description
bypass
Bypass the session.
inspect
Inspect the session.
block
Block the session.
expired-server-cert
Action based on server certificate is expired.
option
-block
Option
Description
allow
Allow the server certificate.
block
Block the session.
ignore
Re-sign the server certificate as trusted.
min-allowed-ssl-version
Minimum SSL version to be allowed. Flow-based inspection does not support SSL version
control.
option
-tls-1.1
Option
Description
ssl-3.0
SSL 3.0.
FortiOS 8.0.0 CLI Reference
734
Fortinet Inc.

<!-- 来源页 735 -->
Parameter
Description
Type
Size
Default
Option
Description
tls-1.0
TLS 1.0.
tls-1.1
TLS 1.1.
tls-1.2
TLS 1.2.
tls-1.3
TLS 1.3.
ports
Ports to use for scanning (1 - 65535, default =
443).
integer
Minimum
value: 1
Maximum
value:
65535
revoked-server-cert
Action based on server certificate is revoked.
option
-block
Option
Description
allow
Allow the server certificate.
block
Block the session.
ignore
Re-sign the server certificate as trusted.
sni-server-cert-check
Check the SNI in the client hello message with
the CN or SAN fields in the returned server
certificate.
option
-enable
Option
Description
enable
Check the SNI in the client hello message with the CN or SAN fields in
the returned server certificate. If mismatched, use the CN in the
server certificate to do URL filtering.
strict
Check the SNI in the client hello message with the CN or SAN fields in
the returned server certificate. If mismatched, close the connection.
disable
Do not check the SNI in the client hello message with the CN or SAN
fields in the returned server certificate.
status
Configure protocol inspection status.
option
-deep-inspection
Option
Description
disable
Disable.
deep-inspection
Full SSL inspection.
FortiOS 8.0.0 CLI Reference
735
Fortinet Inc.

<!-- 来源页 736 -->
Parameter
Description
Type
Size
Default
unsupported-ssl-cipher
Action based on the SSL cipher used being
unsupported.
option
-allow
Option
Description
allow
Bypass the session when the cipher is not supported.
block
Block the session when the cipher is not supported.
unsupported-ssl-negotiation
Action based on the SSL negotiation used being
unsupported.
option
-allow
Option
Description
allow
Bypass the session when the negotiation is not supported.
block
Block the session when the negotiation is not supported.
unsupported-ssl-version
Action based on the SSL version used being
unsupported.
option
-block
Option
Description
allow
Bypass the session when the version is not supported.
block
Block the session when the version is not supported.
untrusted-server-cert
Action based on server certificate is not issued
by a trusted CA.
option
-allow
Option
Description
allow
Allow the server certificate.
block
Block the session.
ignore
Re-sign the server certificate as trusted.
config https
Parameter
Description
Type
Size
Default
cert-probe-failure
Action based on certificate probe failure.
option
-allow
Option
Description
allow
Bypass the session when unable to retrieve server's certificate for
inspection.
block
Block the session when unable to retrieve server's certificate for
inspection.
FortiOS 8.0.0 CLI Reference
736
Fortinet Inc.

<!-- 来源页 737 -->
Parameter
Description
Type
Size
Default
cert-validation-failure
Action based on certificate validation failure.
option
-block
Option
Description
allow
Allow the server certificate.
block
Block the session.
ignore
Re-sign the server certificate as trusted.
cert-validation-timeout
Action based on certificate validation timeout.
option
-allow
Option
Description
allow
Allow the server certificate.
block
Block the session.
ignore
Re-sign the server certificate as trusted.
client-certificate
Action based on received client certificate.
option
-bypass
Option
Description
bypass
Bypass the session.
inspect
Inspect the session.
block
Block the session.
encrypted-client-hello
Block/allow session based on existence of
encrypted-client-hello.
option
-block
Option
Description
allow
Pass the session when encrypted-client-hello exists.
block
Block the session when encrypted-client-hello exists.
expired-server-cert
Action based on server certificate is expired.
option
-block
Option
Description
allow
Allow the server certificate.
block
Block the session.
ignore
Re-sign the server certificate as trusted.
FortiOS 8.0.0 CLI Reference
737
Fortinet Inc.

<!-- 来源页 738 -->
Parameter
Description
Type
Size
Default
min-allowed-ssl-version
Minimum SSL version to be allowed. Flow-based inspection does not support SSL version
control.
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
ports
Ports to use for scanning (1 - 65535, default =
443).
integer
Minimum
value: 1
Maximum
value:
65535
proxy-after-tcp-handshake
Proxy traffic after the TCP 3-way handshake
has been established (not before).
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
quic
QUIC inspection status (default = inspect).
option
-inspect
Option
Description
inspect
Inspect QUIC traffic.
bypass
Bypass QUIC traffic.
block
Block QUIC traffic.
revoked-server-cert
Action based on server certificate is revoked.
option
-block
Option
Description
allow
Allow the server certificate.
block
Block the session.
ignore
Re-sign the server certificate as trusted.
FortiOS 8.0.0 CLI Reference
738
Fortinet Inc.

<!-- 来源页 739 -->
Parameter
Description
Type
Size
Default
sni-server-cert-check
Check the SNI in the client hello message with
the CN or SAN fields in the returned server
certificate.
option
-enable
Option
Description
enable
Check the SNI in the client hello message with the CN or SAN fields in
the returned server certificate. If mismatched, use the CN in the
server certificate to do URL filtering.
strict
Check the SNI in the client hello message with the CN or SAN fields in
the returned server certificate. If mismatched, close the connection.
disable
Do not check the SNI in the client hello message with the CN or SAN
fields in the returned server certificate.
status
Configure protocol inspection status.
option
-deep-inspection
Option
Description
disable
Disable.
certificate-inspection
Inspect SSL handshake only.
deep-inspection
Full SSL inspection.
udp-not-quic
Action to be taken when matched UDP packet is
not QUIC.
option
-allow
Option
Description
allow
Bypass the session when UDP packet is not QUIC.
block
Block the session when UDP packet is not QUIC.
unsupported-ssl-cipher
Action based on the SSL cipher used being
unsupported.
option
-allow
Option
Description
allow
Bypass the session when the cipher is not supported.
block
Block the session when the cipher is not supported.
unsupported-ssl-negotiation
Action based on the SSL negotiation used being
unsupported.
option
-allow
FortiOS 8.0.0 CLI Reference
739
Fortinet Inc.

<!-- 来源页 740 -->
Parameter
Description
Type
Size
Default
Option
Description
allow
Bypass the session when the negotiation is not supported.
block
Block the session when the negotiation is not supported.
unsupported-ssl-version
Action based on the SSL version used being
unsupported.
option
-block
Option
Description
allow
Bypass the session when the version is not supported.
block
Block the session when the version is not supported.
untrusted-server-cert
Action based on server certificate is not issued
by a trusted CA.
option
-allow
Option
Description
allow
Allow the server certificate.
block
Block the session.
ignore
Re-sign the server certificate as trusted.
config imaps
Parameter
Description
Type
Size
Default
cert-validation-failure
Action based on certificate validation failure.
option
-block
Option
Description
allow
Allow the server certificate.
block
Block the session.
ignore
Re-sign the server certificate as trusted.
cert-validation-timeout
Action based on certificate validation timeout.
option
-allow
Option
Description
allow
Allow the server certificate.
block
Block the session.
ignore
Re-sign the server certificate as trusted.
FortiOS 8.0.0 CLI Reference
740
Fortinet Inc.

<!-- 来源页 741 -->
Parameter
Description
Type
Size
Default
client-certificate
Action based on received client certificate.
option
-inspect
Option
Description
bypass
Bypass the session.
inspect
Inspect the session.
block
Block the session.
expired-server-cert
Action based on server certificate is expired.
option
-block
Option
Description
allow
Allow the server certificate.
block
Block the session.
ignore
Re-sign the server certificate as trusted.
ports
Ports to use for scanning (1 - 65535, default =
443).
integer
Minimum
value: 1
Maximum
value:
65535
proxy-after-tcp-handshake
Proxy traffic after the TCP 3-way handshake
has been established (not before).
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
revoked-server-cert
Action based on server certificate is revoked.
option
-block
Option
Description
allow
Allow the server certificate.
block
Block the session.
ignore
Re-sign the server certificate as trusted.
sni-server-cert-check
Check the SNI in the client hello message with
the CN or SAN fields in the returned server
certificate.
option
-enable
FortiOS 8.0.0 CLI Reference
741
Fortinet Inc.

<!-- 来源页 742 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Check the SNI in the client hello message with the CN or SAN fields in
the returned server certificate. If mismatched, use the CN in the
server certificate to do URL filtering.
strict
Check the SNI in the client hello message with the CN or SAN fields in
the returned server certificate. If mismatched, close the connection.
disable
Do not check the SNI in the client hello message with the CN or SAN
fields in the returned server certificate.
status
Configure protocol inspection status.
option
-deep-inspection
Option
Description
disable
Disable.
deep-inspection
Full SSL inspection.
unsupported-ssl-cipher
Action based on the SSL cipher used being
unsupported.
option
-allow
Option
Description
allow
Bypass the session when the cipher is not supported.
block
Block the session when the cipher is not supported.
unsupported-ssl-negotiation
Action based on the SSL negotiation used being
unsupported.
option
-allow
Option
Description
allow
Bypass the session when the negotiation is not supported.
block
Block the session when the negotiation is not supported.
unsupported-ssl-version
Action based on the SSL version used being
unsupported.
option
-block
Option
Description
allow
Bypass the session when the version is not supported.
block
Block the session when the version is not supported.
untrusted-server-cert
Action based on server certificate is not issued
by a trusted CA.
option
-allow
FortiOS 8.0.0 CLI Reference
742
Fortinet Inc.

<!-- 来源页 743 -->
Parameter
Description
Type
Size
Default
Option
Description
allow
Allow the server certificate.
block
Block the session.
ignore
Re-sign the server certificate as trusted.
config pop3s
Parameter
Description
Type
Size
Default
cert-validation-failure
Action based on certificate validation failure.
option
-block
Option
Description
allow
Allow the server certificate.
block
Block the session.
ignore
Re-sign the server certificate as trusted.
cert-validation-timeout
Action based on certificate validation timeout.
option
-allow
Option
Description
allow
Allow the server certificate.
block
Block the session.
ignore
Re-sign the server certificate as trusted.
client-certificate
Action based on received client certificate.
option
-inspect
Option
Description
bypass
Bypass the session.
inspect
Inspect the session.
block
Block the session.
expired-server-cert
Action based on server certificate is expired.
option
-block
Option
Description
allow
Allow the server certificate.
FortiOS 8.0.0 CLI Reference
743
Fortinet Inc.

<!-- 来源页 744 -->
Parameter
Description
Type
Size
Default
Option
Description
block
Block the session.
ignore
Re-sign the server certificate as trusted.
ports
Ports to use for scanning (1 - 65535, default =
443).
integer
Minimum
value: 1
Maximum
value:
65535
proxy-after-tcp-handshake
Proxy traffic after the TCP 3-way handshake
has been established (not before).
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
revoked-server-cert
Action based on server certificate is revoked.
option
-block
Option
Description
allow
Allow the server certificate.
block
Block the session.
ignore
Re-sign the server certificate as trusted.
sni-server-cert-check
Check the SNI in the client hello message with
the CN or SAN fields in the returned server
certificate.
option
-enable
Option
Description
enable
Check the SNI in the client hello message with the CN or SAN fields in
the returned server certificate. If mismatched, use the CN in the
server certificate to do URL filtering.
strict
Check the SNI in the client hello message with the CN or SAN fields in
the returned server certificate. If mismatched, close the connection.
disable
Do not check the SNI in the client hello message with the CN or SAN
fields in the returned server certificate.
status
Configure protocol inspection status.
option
-deep-inspection
FortiOS 8.0.0 CLI Reference
744
Fortinet Inc.

<!-- 来源页 745 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable.
deep-inspection
Full SSL inspection.
unsupported-ssl-cipher
Action based on the SSL cipher used being
unsupported.
option
-allow
Option
Description
allow
Bypass the session when the cipher is not supported.
block
Block the session when the cipher is not supported.
unsupported-ssl-negotiation
Action based on the SSL negotiation used being
unsupported.
option
-allow
Option
Description
allow
Bypass the session when the negotiation is not supported.
block
Block the session when the negotiation is not supported.
unsupported-ssl-version
Action based on the SSL version used being
unsupported.
option
-block
Option
Description
allow
Bypass the session when the version is not supported.
block
Block the session when the version is not supported.
untrusted-server-cert
Action based on server certificate is not issued
by a trusted CA.
option
-allow
Option
Description
allow
Allow the server certificate.
block
Block the session.
ignore
Re-sign the server certificate as trusted.
config smtps
Parameter
Description
Type
Size
Default
cert-validation-failure
Action based on certificate validation failure.
option
-block
FortiOS 8.0.0 CLI Reference
745
Fortinet Inc.

<!-- 来源页 746 -->
Parameter
Description
Type
Size
Default
Option
Description
allow
Allow the server certificate.
block
Block the session.
ignore
Re-sign the server certificate as trusted.
cert-validation-timeout
Action based on certificate validation timeout.
option
-allow
Option
Description
allow
Allow the server certificate.
block
Block the session.
ignore
Re-sign the server certificate as trusted.
client-certificate
Action based on received client certificate.
option
-inspect
Option
Description
bypass
Bypass the session.
inspect
Inspect the session.
block
Block the session.
expired-server-cert
Action based on server certificate is expired.
option
-block
Option
Description
allow
Allow the server certificate.
block
Block the session.
ignore
Re-sign the server certificate as trusted.
ports
Ports to use for scanning (1 - 65535, default =
443).
integer
Minimum
value: 1
Maximum
value:
65535
proxy-after-tcp-handshake
Proxy traffic after the TCP 3-way handshake
has been established (not before).
option
-disable
FortiOS 8.0.0 CLI Reference
746
Fortinet Inc.

<!-- 来源页 747 -->
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
revoked-server-cert
Action based on server certificate is revoked.
option
-block
Option
Description
allow
Allow the server certificate.
block
Block the session.
ignore
Re-sign the server certificate as trusted.
sni-server-cert-check
Check the SNI in the client hello message with
the CN or SAN fields in the returned server
certificate.
option
-enable
Option
Description
enable
Check the SNI in the client hello message with the CN or SAN fields in
the returned server certificate. If mismatched, use the CN in the
server certificate to do URL filtering.
strict
Check the SNI in the client hello message with the CN or SAN fields in
the returned server certificate. If mismatched, close the connection.
disable
Do not check the SNI in the client hello message with the CN or SAN
fields in the returned server certificate.
status
Configure protocol inspection status.
option
-deep-inspection
Option
Description
disable
Disable.
deep-inspection
Full SSL inspection.
unsupported-ssl-cipher
Action based on the SSL cipher used being
unsupported.
option
-allow
Option
Description
allow
Bypass the session when the cipher is not supported.
block
Block the session when the cipher is not supported.
FortiOS 8.0.0 CLI Reference
747
Fortinet Inc.

<!-- 来源页 748 -->
Parameter
Description
Type
Size
Default
unsupported-ssl-negotiation
Action based on the SSL negotiation used being
unsupported.
option
-allow
Option
Description
allow
Bypass the session when the negotiation is not supported.
block
Block the session when the negotiation is not supported.
unsupported-ssl-version
Action based on the SSL version used being
unsupported.
option
-block
Option
Description
allow
Bypass the session when the version is not supported.
block
Block the session when the version is not supported.
untrusted-server-cert
Action based on server certificate is not issued
by a trusted CA.
option
-allow
Option
Description
allow
Allow the server certificate.
block
Block the session.
ignore
Re-sign the server certificate as trusted.
config ssh
Parameter
Description
Type
Size
Default
inspect-all
Level of SSL inspection.
option
-disable
Option
Description
disable
Disable.
deep-inspection
Full SSL inspection.
ports
Ports to use for scanning (1 - 65535, default =
443).
integer
Minimum
value: 1
Maximum
value:
65535
proxy-after-tcp-handshake
Proxy traffic after the TCP 3-way handshake
has been established (not before).
option
-disable
FortiOS 8.0.0 CLI Reference
748
Fortinet Inc.

<!-- 来源页 749 -->
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
ssh-algorithm
Relative strength of encryption algorithms
accepted during negotiation.
option
-compatible
Option
Description
compatible
Allow a broader set of encryption algorithms for best compatibility.
high-encryption
Allow only AES-CTR, AES-GCM ciphers and high encryption
algorithms.
ssh-tun-policy-check
Enable/disable SSH tunnel policy check.
option
-disable
Option
Description
disable
Disable SSH tunnel policy check.
enable
Enable SSH tunnel policy check.
status
Configure protocol inspection status.
option
-disable
Option
Description
disable
Disable.
deep-inspection
Full SSL inspection.
unsupported-version
Action based on SSH version being
unsupported.
option
-bypass
Option
Description
bypass
Bypass the session.
block
Block the session.
config ssl
Parameter
Description
Type
Size
Default
cert-probe-failure
Action based on certificate probe failure.
option
-allow
FortiOS 8.0.0 CLI Reference
749
Fortinet Inc.

<!-- 来源页 750 -->
Parameter
Description
Type
Size
Default
Option
Description
allow
Bypass the session when unable to retrieve server's certificate for
inspection.
block
Block the session when unable to retrieve server's certificate for
inspection.
cert-validation-failure
Action based on certificate validation failure.
option
-block
Option
Description
allow
Allow the server certificate.
block
Block the session.
ignore
Re-sign the server certificate as trusted.
cert-validation-timeout
Action based on certificate validation timeout.
option
-allow
Option
Description
allow
Allow the server certificate.
block
Block the session.
ignore
Re-sign the server certificate as trusted.
client-certificate
Action based on received client certificate.
option
-bypass
Option
Description
bypass
Bypass the session.
inspect
Inspect the session.
block
Block the session.
encrypted-client-hello
Block/allow session based on existence of
encrypted-client-hello.
option
-block
Option
Description
allow
Pass the session when encrypted-client-hello exists.
block
Block the session when encrypted-client-hello exists.
expired-server-cert
Action based on server certificate is expired.
option
-block
FortiOS 8.0.0 CLI Reference
750
Fortinet Inc.

<!-- 来源页 751 -->
Parameter
Description
Type
Size
Default
Option
Description
allow
Allow the server certificate.
block
Block the session.
ignore
Re-sign the server certificate as trusted.
inspect-all
Level of SSL inspection.
option
-disable
Option
Description
disable
Disable.
certificate-inspection
Inspect SSL handshake only.
deep-inspection
Full SSL inspection.
min-allowed-ssl-version
Minimum SSL version to be allowed. Flow-based
inspection does not support SSL version control.
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
revoked-server-cert
Action based on server certificate is revoked.
option
-block
Option
Description
allow
Allow the server certificate.
block
Block the session.
ignore
Re-sign the server certificate as trusted.
sni-server-cert-check
Check the SNI in the client hello message with the
CN or SAN fields in the returned server certificate.
option
-enable
Option
Description
enable
Check the SNI in the client hello message with the CN or SAN fields in
the returned server certificate. If mismatched, use the CN in the server
certificate to do URL filtering.
FortiOS 8.0.0 CLI Reference
751
Fortinet Inc.

<!-- 来源页 752 -->
Parameter
Description
Type
Size
Default
Option
Description
strict
Check the SNI in the client hello message with the CN or SAN fields in
the returned server certificate. If mismatched, close the connection.
disable
Do not check the SNI in the client hello message with the CN or SAN
fields in the returned server certificate.
unsupported-ssl-cipher
Action based on the SSL cipher used being
unsupported.
option
-allow
Option
Description
allow
Bypass the session when the cipher is not supported.
block
Block the session when the cipher is not supported.
unsupported-ssl-negotiation
Action based on the SSL negotiation used being
unsupported.
option
-allow
Option
Description
allow
Bypass the session when the negotiation is not supported.
block
Block the session when the negotiation is not supported.
unsupported-ssl-version
Action based on the SSL version used being
unsupported.
option
-block
Option
Description
allow
Bypass the session when the version is not supported.
block
Block the session when the version is not supported.
untrusted-server-cert
Action based on server certificate is not issued by
a trusted CA.
option
-allow
Option
Description
allow
Allow the server certificate.
block
Block the session.
ignore
Re-sign the server certificate as trusted.
config ssl-exempt
Parameter
Description
Type
Size
Default
address
IPv4 address object.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
752
Fortinet Inc.

<!-- 来源页 753 -->
Parameter
Description
Type
Size
Default
address6
IPv6 address object.
string
Maximum
length: 79
fortiguard-category
FortiGuard category ID.
integer
Minimum
value: 0
Maximum
value: 255
0
id
ID number.
integer
Minimum
value: 0
Maximum
value: 512
0
regex
Exempt servers by regular expression.
string
Maximum
length: 255
type
Type of address object (IPv4 or IPv6) or
FortiGuard category.
option
-fortiguard-category
Option
Description
fortiguard-category
FortiGuard category.
address
Firewall IPv4 address.
address6
Firewall IPv6 address.
wildcard-fqdn
Fully Qualified Domain Name with wildcard characters.
regex
Regular expression FQDN.
wildcard-fqdn
Exempt servers by wildcard FQDN.
string
Maximum
length: 79
config ssl-server
Parameter
Description
Type
Size
Default
ftps-client-certificate
Action based on received client certificate
during the FTPS handshake.
option
-bypass
Option
Description
bypass
Bypass the session.
inspect
Inspect the session.
block
Block the session.
https-client-certificate
Action based on received client certificate
during the HTTPS handshake.
option
-bypass
FortiOS 8.0.0 CLI Reference
753
Fortinet Inc.

<!-- 来源页 754 -->
Parameter
Description
Type
Size
Default
Option
Description
bypass
Bypass the session.
inspect
Inspect the session.
block
Block the session.
id
SSL server ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
imaps-client-certificate
Action based on received client certificate
during the IMAPS handshake.
option
-bypass
Option
Description
bypass
Bypass the session.
inspect
Inspect the session.
block
Block the session.
ip
IPv4 address of the SSL server.
ipv4-address-any
Not Specified
0.0.0.0
pop3s-client-certificate
Action based on received client certificate
during the POP3S handshake.
option
-bypass
Option
Description
bypass
Bypass the session.
inspect
Inspect the session.
block
Block the session.
smtps-client-certificate
Action based on received client certificate
during the SMTPS handshake.
option
-bypass
Option
Description
bypass
Bypass the session.
inspect
Inspect the session.
block
Block the session.
ssl-other-client-certificate
Action based on received client certificate
during an SSL protocol handshake.
option
-bypass
FortiOS 8.0.0 CLI Reference
754
Fortinet Inc.

---


<!-- 来源页 755 -->
Parameter
Description
Type
Size
Default
Option
Description
bypass
Bypass the session.
inspect
Inspect the session.
block
Block the session.
config firewall traffic-class
Configure names for shaping classes.
config firewall traffic-class
Description: Configure names for shaping classes.
edit <class-id>
set class-name {string}
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set uuid {uuid}
next
end
config firewall traffic-class
Parameter
Description
Type
Size
Default
class-id
Class ID to be named.
integer
Minimum
value: 2
Maximum
value: 31
0
class-name
Define the name for this class-id.
string
Maximum
length: 35
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
FortiOS 8.0.0 CLI Reference
755
Fortinet Inc.

---


<!-- 来源页 832 -->
set color {integer}
set comments {var-string}
set member <name1>, <name2>, ...
set uuid {uuid}
next
end
config firewall vipgrp6
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
member
<name>
Member VIP objects of the group (Separate
multiple objects with a space).
IPv6 VIP name.
string
Maximum
length: 79
name
IPv6 VIP group name.
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
config firewall wildcard-fqdn custom
Config global/VDOM Wildcard FQDN address.
config firewall wildcard-fqdn custom
Description: Config global/VDOM Wildcard FQDN address.
edit <name>
set color {integer}
set comment {var-string}
set uuid {uuid}
set wildcard-fqdn {string}
next
end
FortiOS 8.0.0 CLI Reference
832
Fortinet Inc.

---


<!-- 来源页 833 -->
config firewall wildcard-fqdn custom
Parameter
Description
Type
Size
Default
color
GUI icon color.
integer
Minimum
value: 0
Maximum
value: 32
0
comment
Comment.
var-string
Maximum
length: 255
name
Address name.
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
wildcard-fqdn
Wildcard FQDN.
string
Maximum
length: 255
config firewall wildcard-fqdn group
Config global Wildcard FQDN address groups.
config firewall wildcard-fqdn group
Description: Config global Wildcard FQDN address groups.
edit <name>
set color {integer}
set comment {var-string}
set member <name1>, <name2>, ...
set uuid {uuid}
next
end
config firewall wildcard-fqdn group
Parameter
Description
Type
Size
Default
color
GUI icon color.
integer
Minimum
value: 0
Maximum
value: 32
0
comment
Comment.
var-string
Maximum
length: 255
FortiOS 8.0.0 CLI Reference
833
Fortinet Inc.

<!-- 来源页 834 -->
Parameter
Description
Type
Size
Default
member
<name>
Address group members.
Address name.
string
Maximum
length: 79
name
Address group name.
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
FortiOS 8.0.0 CLI Reference
834
Fortinet Inc.
