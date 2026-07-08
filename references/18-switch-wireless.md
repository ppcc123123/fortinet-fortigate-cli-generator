# 交换机 / 无线 / 扩展控制器

> 来源: FortiOS-8.0.0-CLI_Reference.pdf
> 覆盖命令/章节: switch-controller, wireless-controller, extension-controller, ethernet-oam
> 本文件由 extract_pdf.py 从官方 PDF 自动提取，请勿手动编辑；
> 如需修正请修改 map.json 后重跑脚本。

---


<!-- 来源页 342 -->
ethernet-oam
This section includes syntax for the following commands:
l config ethernet-oam cfm on page 342
config ethernet-oam cfm
This command is available for model(s): FortiGate 100F, FortiGate 101F Gen2, FortiGate 1100E,
FortiGate 200E, FortiGate 200F, FortiGate 201F, FortiGate 40F 3G4G, FortiGate 40F, FortiGate 60F,
FortiGate 61F, FortiGate 80F Bypass, FortiGate 80F Gen2, FortiGate 80F-POE, FortiGate 81F Gen2,
FortiGate 81F-POE, FortiWiFi 40F 3G4G, FortiWiFi 40F, FortiWiFi 60F, FortiWiFi 61F.
It is not available for: FortiGate 1000D, FortiGate 1000F, FortiGate 1001F, FortiGate 1101E, FortiGate
120G, FortiGate 121G, FortiGate 1800F, FortiGate 1801F, FortiGate 2000E, FortiGate 200G, FortiGate
201E, FortiGate 201G, FortiGate 2200E, FortiGate 2201E, FortiGate 2500E, FortiGate 2600F,
FortiGate 2601F, FortiGate 3000F, FortiGate 3001F, FortiGate 300E, FortiGate 301E, FortiGate 30G,
FortiGate 31G, FortiGate 3200F, FortiGate 3201F Gen2, FortiGate 3300E, FortiGate 3301E, FortiGate
3400E, FortiGate 3401E, FortiGate 3500F Gen2, FortiGate 3501F Gen2, FortiGate 3600E, FortiGate
3601E, FortiGate 3700F, FortiGate 3701F, FortiGate 3960E, FortiGate 3980E, FortiGate 400E
Bypass, FortiGate 400E, FortiGate 400F, FortiGate 401E, FortiGate 401F, FortiGate 4200F, FortiGate
4201F Gen2, FortiGate 4400F, FortiGate 4401F Gen2, FortiGate 4800F, FortiGate 4801F, FortiGate
500E, FortiGate 501E, FortiGate 50G 5G, FortiGate 50G DSL, FortiGate 50G SFP-POE, FortiGate 50G
SFP, FortiGate 50G, FortiGate 51G 5G, FortiGate 51G SFP-POE, FortiGate 51G, FortiGate 600E,
FortiGate 600F, FortiGate 601E, FortiGate 601F, FortiGate 70F, FortiGate 70G-POE, FortiGate 70G,
FortiGate 71F, FortiGate 71G-POE, FortiGate 71G, FortiGate 800D, FortiGate 80F DSL, FortiGate
900D, FortiGate 900G, FortiGate 901G, FortiGate 90G Gen2, FortiGate 90G, FortiGate 91G Gen2,
FortiGate 91G, FortiGate-VM64 Aliyun, FortiGate-VM64 AWS, FortiGate-VM64 Azure, FortiGate-VM64 GCP, FortiGate-VM64 OPC, FortiGate-VM64, FortiGateRugged 50G 5G, FortiGateRugged 60F
3G4G, FortiGateRugged 60F Gen2, FortiGateRugged 70F 3G4G, FortiGateRugged 70F,
FortiGateRugged 70G 5G Dual, FortiGateRugged 70G, FortiWiFi 30G, FortiWiFi 31G, FortiWiFi 50G
5G, FortiWiFi 50G DSL, FortiWiFi 50G SFP, FortiWiFi 50G, FortiWiFi 51G, FortiWiFi 70G-POE, FortiWiFi
70G, FortiWiFi 71G, FortiWiFi 80F 2R 3G4G DSL, FortiWiFi 80F 2R, FortiWiFi 81F 2R 3G4G DSL,
FortiWiFi 81F 2R 3G4G-POE, FortiWiFi 81F 2R-POE, FortiWiFi 81F 2R.
CFM domain configuration.
config ethernet-oam cfm
Description: CFM domain configuration.
edit <domain-id>
set domain-level {integer}
set domain-name {text}
config service
Description: CFM service configuration.
FortiOS 8.0.0 CLI Reference
342
Fortinet Inc.

<!-- 来源页 343 -->
edit <service-id>
set cos {integer}
set interface {string}
set mepid {integer}
set message-interval [100|1000|...]
set sender-id [None|Hostname]
set service-name {text}
next
end
next
end
config ethernet-oam cfm
Parameter
Description
Type
Size
Default
domain-id
OAM domain ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
domain-level
OAM maintenance level (0 - 7)
integer
Minimum value:
0 Maximum
value: 7
7
domain-name
OAM domain name. Maintenance Domain
Identifier (MDID).
text
Not Specified
config service
Parameter
Description
Type
Size
Default
cos
Set Class of service (CoS) bit for continuity-check messages. range[0 - 7]
integer
Minimum value:
0 Maximum
value: 7
0
interface
VLAN interface name where service is enabled
string
Maximum
length: 63
mepid
ID of the local MEP. range[1 - 8191]
integer
Minimum value:
1 Maximum
value: 8191
1
message-interval
Continuity-check message frequency interval in
ms
option
-1000
Option
Description
100
100 msc
FortiOS 8.0.0 CLI Reference
343
Fortinet Inc.

<!-- 来源页 344 -->
Parameter
Description
Type
Size
Default
Option
Description
1000
1000 msc
10000
10000 msc
60000
60000 msc
600000
600000 msc
sender-id
TLV Sender ID. {None | Hostname}
option
-None
Option
Description
None
None
Hostname
Hostname
service-id
Service ID to specify service
integer
Minimum value:
0 Maximum
value:
4294967295
0
service-name
Short MA Name (SMAN)
text
Not Specified
FortiOS 8.0.0 CLI Reference
344
Fortinet Inc.

---


<!-- 来源页 345 -->
extension-controller
This section includes syntax for the following commands:
l config extension-controller dataplan on page 345
l config extension-controller extender-profile on page 352
l config extension-controller extender-vap on page 383
l config extension-controller extender on page 348
l config extension-controller fortigate-profile on page 388
l config extension-controller fortigate on page 387
config extension-controller dataplan
FortiExtender dataplan configuration.
config extension-controller dataplan
Description: FortiExtender dataplan configuration.
edit <name>
set apn {string}
set auth-type [none|pap|...]
set billing-date {integer}
set capacity {integer}
set carrier {string}
set iccid {string}
set modem-id [modem1|modem2|...]
set monthly-fee {integer}
set overage [disable|enable]
set password {password}
set pdn [ipv4-only|ipv6-only|...]
set preferred-subnet {integer}
set private-network [disable|enable]
set signal-period {integer}
set signal-threshold {integer}
set slot [sim1|sim2]
set type [carrier|slot|...]
set username {string}
next
end
FortiOS 8.0.0 CLI Reference
345
Fortinet Inc.

<!-- 来源页 346 -->
config extension-controller dataplan
Parameter
Description
Type
Size
Default
apn
APN configuration.
string
Maximum
length: 63
auth-type
Authentication type.
option
-none
Option
Description
none
No authentication.
pap
PAP.
chap
CHAP.
billing-date
Billing day of the month (1 - 31).
integer
Minimum
value: 1
Maximum
value: 31
1
capacity
Capacity in MB (0 - 102400000).
integer
Minimum
value: 0
Maximum
value:
102400000
0
carrier
Carrier configuration.
string
Maximum
length: 31
iccid
ICCID configuration.
string
Maximum
length: 31
modem-id
Dataplan's modem specifics, if any.
option
-all
Option
Description
modem1
Modem one.
modem2
Modem two.
all
All modems.
monthly-fee
Monthly fee of dataplan (0 - 100000, in local
currency).
integer
Minimum
value: 0
Maximum
value:
1000000
0
name
FortiExtender data plan name.
string
Maximum
length: 31
overage
Enable/disable dataplan overage detection.
option
-disable
FortiOS 8.0.0 CLI Reference
346
Fortinet Inc.

<!-- 来源页 347 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable dataplan overage detection.
enable
Enable dataplan overage detection.
password
Password.
password
Not Specified
pdn
PDN type.
option
-ipv4-only
Option
Description
ipv4-only
IPv4 only PDN activation.
ipv6-only
IPv6 only PDN activation.
ipv4-ipv6
Both IPv4 and IPv6 PDN activations.
preferred-subnet
Preferred subnet mask (0 - 32).
integer
Minimum
value: 0
Maximum
value: 32
0
private-network
Enable/disable dataplan private network
support.
option
-disable
Option
Description
disable
Disable dataplan private network support.
enable
Enable dataplan private network support.
signal-period
Signal period (600 to 18000 seconds).
integer
Minimum
value: 600
Maximum
value: 18000
3600
signal-threshold
Signal threshold. Specify the range between 50 -100, where 50/100 means -50/-100 dBm.
integer
Minimum
value: 50
Maximum
value: 100
100
slot
SIM slot configuration.
option
-Option
Description
sim1
Sim slot one.
sim2
Sim slot two.
type
Type preferences configuration.
option
-generic
FortiOS 8.0.0 CLI Reference
347
Fortinet Inc.

<!-- 来源页 348 -->
Parameter
Description
Type
Size
Default
Option
Description
carrier
Assign by SIM carrier.
slot
Assign to SIM slot 1 or 2.
iccid
Assign to a specific SIM by ICCID.
generic
Compatible with any SIM. Assigned if no other dataplan matches the
chosen SIM.
username
Username.
string
Maximum
length: 127
config extension-controller extender
Extender controller configuration.
config extension-controller extender
Description: Extender controller configuration.
edit <name>
set allowaccess {option1}, {option2}, ...
set authorized [discovered|disable|...]
set bandwidth-limit {integer}
set description {string}
set device-id {integer}
set enforce-bandwidth [enable|disable]
set ext-name {string}
set extension-type [wan-extension|lan-extension]
set firmware-provision-latest [disable|once]
set id {string}
set login-password {password}
set login-password-change [yes|default|...]
set override-allowaccess [enable|disable]
set override-enforce-bandwidth [enable|disable]
set override-login-password-change [enable|disable]
set profile {string}
set vdom {integer}
config wan-extension
Description: FortiExtender wan extension configuration.
set modem1-extension {string}
set modem1-pdn1-interface {string}
set modem1-pdn2-interface {string}
set modem1-pdn3-interface {string}
set modem1-pdn4-interface {string}
set modem2-extension {string}
set modem2-pdn1-interface {string}
set modem2-pdn2-interface {string}
set modem2-pdn3-interface {string}
FortiOS 8.0.0 CLI Reference
348
Fortinet Inc.

<!-- 来源页 349 -->
set modem2-pdn4-interface {string}
end
next
end
config extension-controller extender
Parameter
Description
Type
Size
Default
allowaccess
Control management access to the
managed extender. Separate entries with a
space.
option
-Option
Description
ping
PING access.
telnet
TELNET access.
http
HTTP access.
https
HTTPS access.
ssh
SSH access.
snmp
SNMP access.
authorized
FortiExtender Administration (enable or
disable).
option
-discovered
Option
Description
discovered
Controller discovered this FortiExtender.
disable
Controller is configured to not provide service to this FortiExtender.
enable
Controller is configured to provide service to this FortiExtender.
bandwidth-limit
FortiExtender LAN extension bandwidth
limit (Mbps).
integer
Minimum value:
1 Maximum
value:
16776000
1024
description
Description.
string
Maximum
length: 255
device-id
Device ID.
integer
Minimum value:
0 Maximum
value:
4294967295
1026
enforce-bandwidth
Enable/disable enforcement of bandwidth
on LAN extension interface.
option
-disable
FortiOS 8.0.0 CLI Reference
349
Fortinet Inc.

<!-- 来源页 350 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable to enforce bandwidth limit on LAN extension interface.
disable
Disable to enforce bandwidth limit on LAN extension interface.
ext-name
FortiExtender name.
string
Maximum
length: 31
extension-type
Extension type for this FortiExtender.
option
-Option
Description
wan-extension
FortiExtender WAN extension mode.
lan-extension
FortiExtender LAN extension mode.
firmware-provision-latest
Enable/disable one-time automatic
provisioning of the latest firmware version.
option
-disable
Option
Description
disable
Do not automatically provision the latest available firmware.
once
Automatically attempt a one-time upgrade to the latest available
firmware version.
id
FortiExtender serial number.
string
Maximum
length: 19
login-password
Set the managed extender's administrator
password.
password
Not Specified
login-password-change
Change or reset the administrator password
of a managed extender (yes, default, or no,
default = no).
option
-no
Option
Description
yes
Change the managed extender's administrator password. Use the
login-password option to set the password.
default
Keep the managed extender's administrator password set to the
factory default.
no
Do not change the managed extender's administrator password.
name
FortiExtender entry name.
string
Maximum
length: 19
FortiOS 8.0.0 CLI Reference
350
Fortinet Inc.

<!-- 来源页 351 -->
Parameter
Description
Type
Size
Default
override-allowaccess
Enable to override the extender profile
management access configuration.
option
-disable
Option
Description
enable
Override the extender profile management access configuration.
disable
Use the extender profile management access configuration.
override-enforce-bandwidth
Enable to override the extender profile
enforce-bandwidth setting.
option
-disable
Option
Description
enable
Enable override of FortiExtender profile bandwidth setting.
disable
Disable override of FortiExtender profile bandwidth setting.
override-login-password-change
Enable to override the extender profile
login-password (administrator password)
setting.
option
-disable
Option
Description
enable
Override the WTP profile login-password (administrator password)
setting.
disable
Use the the WTP profile login-password (administrator password)
setting.
profile
FortiExtender profile configuration.
string
Maximum
length: 31
vdom
VDOM. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
1
config wan-extension
Parameter
Description
Type
Size
Default
modem1-extension
FortiExtender interface name.
string
Maximum
length: 31
modem1-pdn1-interface
FortiExtender interface name.
string
Maximum
length: 31
FortiOS 8.0.0 CLI Reference
351
Fortinet Inc.

<!-- 来源页 352 -->
Parameter
Description
Type
Size
Default
modem1-pdn2-interface
FortiExtender interface name.
string
Maximum
length: 31
modem1-pdn3-interface
FortiExtender interface name.
string
Maximum
length: 31
modem1-pdn4-interface
FortiExtender interface name.
string
Maximum
length: 31
modem2-extension
FortiExtender interface name.
string
Maximum
length: 31
modem2-pdn1-interface
FortiExtender interface name.
string
Maximum
length: 31
modem2-pdn2-interface
FortiExtender interface name.
string
Maximum
length: 31
modem2-pdn3-interface
FortiExtender interface name.
string
Maximum
length: 31
modem2-pdn4-interface
FortiExtender interface name.
string
Maximum
length: 31
config extension-controller extender-profile
FortiExtender extender profile configuration.
config extension-controller extender-profile
Description: FortiExtender extender profile configuration.
edit <name>
set allowaccess {option1}, {option2}, ...
set bandwidth-limit {integer}
config cellular
Description: FortiExtender cellular configuration.
config controller-report
Description: FortiExtender controller report configuration.
set interval {integer}
set signal-threshold {integer}
set status [disable|enable]
end
set dataplan <name1>, <name2>, ...
config modem1
FortiOS 8.0.0 CLI Reference
352
Fortinet Inc.

<!-- 来源页 353 -->
Description: Configuration options for modem 1.
config auto-switch
Description: FortiExtender auto switch configuration.
set dataplan [disable|enable]
set disconnect [disable|enable]
set disconnect-period {integer}
set disconnect-threshold {integer}
set signal [disable|enable]
set switch-back {option1}, {option2}, ...
set switch-back-time {string}
set switch-back-timer {integer}
end
set conn-status {integer}
set default-sim [sim1|sim2|...]
set gps [disable|enable]
set multiple-PDN [disable|enable]
set pdn1-dataplan {string}
set pdn2-dataplan {string}
set pdn3-dataplan {string}
set pdn4-dataplan {string}
set preferred-carrier {string}
set redundant-intf {string}
set redundant-mode [disable|enable]
set sim1-pin [disable|enable]
set sim1-pin-code {password}
set sim2-pin [disable|enable]
set sim2-pin-code {password}
end
config modem2
Description: Configuration options for modem 2.
config auto-switch
Description: FortiExtender auto switch configuration.
set dataplan [disable|enable]
set disconnect [disable|enable]
set disconnect-period {integer}
set disconnect-threshold {integer}
set signal [disable|enable]
set switch-back {option1}, {option2}, ...
set switch-back-time {string}
set switch-back-timer {integer}
end
set conn-status {integer}
set default-sim [sim1|sim2|...]
set gps [disable|enable]
set multiple-PDN [disable|enable]
set pdn1-dataplan {string}
set pdn2-dataplan {string}
set pdn3-dataplan {string}
set pdn4-dataplan {string}
set preferred-carrier {string}
set redundant-intf {string}
set redundant-mode [disable|enable]
FortiOS 8.0.0 CLI Reference
353
Fortinet Inc.

<!-- 来源页 354 -->
set sim1-pin [disable|enable]
set sim1-pin-code {password}
set sim2-pin [disable|enable]
set sim2-pin-code {password}
end
config sms-notification
Description: FortiExtender cellular SMS notification configuration.
config alert
Description: SMS alert list.
set data-exhausted {string}
set fgt-backup-mode-switch {string}
set low-signal-strength {string}
set mode-switch {string}
set os-image-fallback {string}
set session-disconnect {string}
set system-reboot {string}
end
config receiver
Description: SMS notification receiver list.
edit <name>
set alert {option1}, {option2}, ...
set phone-number {string}
set status [disable|enable]
next
end
set status [disable|enable]
end
end
set enforce-bandwidth [enable|disable]
set extension [wan-extension|lan-extension]
set id {integer}
config lan-extension
Description: FortiExtender LAN extension configuration.
config backhaul
Description: LAN extension backhaul tunnel configuration.
edit <name>
set health-check-fail-cnt {integer}
set health-check-interval {integer}
set health-check-probe-cnt {integer}
set health-check-probe-tm {integer}
set health-check-recovery-cnt {integer}
set port [wan|lte1|...]
set role [primary|secondary]
set weight {integer}
next
end
set backhaul-interface {string}
set backhaul-ip {string}
config downlinks
Description: Config FortiExtender downlink interface for LAN extension.
edit <name>
set port [port1|port2|...]
FortiOS 8.0.0 CLI Reference
354
Fortinet Inc.

<!-- 来源页 355 -->
set pvid {integer}
set type [port|vap]
set vap {string}
set vids <vid1>, <vid2>, ...
next
end
set ipsec-tunnel {string}
set link-loadbalance [activebackup|loadbalance]
config traffic-split-services
Description: Config FortiExtender traffic split interface for LAN extension.
edit <name>
set address {string}
set service {string}
set vsdb [disable|enable]
next
end
end
set login-password {password}
set login-password-change [yes|default|...]
set model [FX201E|FX211E|...]
config wifi
Description: FortiExtender Wi-Fi configuration.
set country [--|AF|...]
config radio-1
Description: Radio-1 config for Wi-Fi 2.4GHz
set 80211d [disable|enable]
set band {option}
set bandwidth [auto|20MHz|...]
set beacon-interval {integer}
set bss-color {integer}
set bss-color-mode [auto|static]
set channel {option1}, {option2}, ...
set extension-channel [auto|higher|...]
set guard-interval [auto|400ns|...]
set lan-ext-vap {string}
set local-vaps <name1>, <name2>, ...
set max-clients {integer}
set mode [AP|Client]
set operating-standard [auto|11A-N-AC-AX|...]
set power-level {integer}
set status [disable|enable]
end
config radio-2
Description: Radio-2 config for Wi-Fi 5GHz
set 80211d [disable|enable]
set band {option}
set bandwidth [auto|20MHz|...]
set beacon-interval {integer}
set bss-color {integer}
set bss-color-mode [auto|static]
set channel {option1}, {option2}, ...
set extension-channel [auto|higher|...]
FortiOS 8.0.0 CLI Reference
355
Fortinet Inc.

<!-- 来源页 356 -->
set guard-interval [auto|400ns|...]
set lan-ext-vap {string}
set local-vaps <name1>, <name2>, ...
set max-clients {integer}
set mode [AP|Client]
set operating-standard [auto|11A-N-AC-AX|...]
set power-level {integer}
set status [disable|enable]
end
end
next
end
config extension-controller extender-profile
Parameter
Description
Type
Size
Default
allowaccess
Control management access to the managed
extender. Separate entries with a space.
option
-Option
Description
ping
PING access.
telnet
TELNET access.
http
HTTP access.
https
HTTPS access.
ssh
SSH access.
snmp
SNMP access.
bandwidth-limit
FortiExtender LAN extension bandwidth limit
(Mbps).
integer
Minimum
value: 1
Maximum
value:
16776000
1024
enforce-bandwidth
Enable/disable enforcement of bandwidth on
LAN extension interface.
option
-disable
Option
Description
enable
Enable to enforce bandwidth limit on LAN extension interface.
disable
Disable to enforce bandwidth limit on LAN extension interface.
extension
Extension option.
option
-wan-extension
**
FortiOS 8.0.0 CLI Reference
356
Fortinet Inc.

<!-- 来源页 357 -->
Parameter
Description
Type
Size
Default
Option
Description
wan-extension
WAN extension.
lan-extension
LAN extension.
id
ID.
integer
Minimum
value: 0
Maximum
value:
102400000
32
login-password
Set the managed extender's administrator
password.
password
Not Specified
login-password-change
Change or reset the administrator password of
a managed extender (yes, default, or no,
default = no).
option
-no
Option
Description
yes
Change the managed extender's administrator password. Use the
login-password option to set the password.
default
Keep the managed extender's administrator password set to the
factory default.
no
Do not change the managed extender's administrator password.
model
Model.
option
-FX201E
Option
Description
FX201E
FEX-201E model.
FX211E
FEX-211E model.
FX200F
FEX-200F model.
FXA11F
FEX-101F-AM model.
FXE11F
FEX-101F-EA model.
FXA21F
FEX-201F-AM model.
FXE21F
FEX-201F-EA model.
FXA22F
FEX-202F-AM model.
FXE22F
FEX-202F-EA model.
FX212F
FEX-212F model.
FX311F
FEX-311F model.
FortiOS 8.0.0 CLI Reference
357
Fortinet Inc.

<!-- 来源页 358 -->
Parameter
Description
Type
Size
Default
Option
Description
FX312F
FEX-312F model.
FX511F
FEX-511F model.
FXR51G
FER-511G model.
FXN51G
FEX-511G model.
FXW51G
FEX-511G-Wifi model.
FVG21F
FEV-211F model.
FVA21F
FEV-211F-AM model.
FVG22F
FEV-212F model.
FVA22F
FEV-212F-AM model.
FX04DA
FX40D-AMEU model.
FG
FG-CONNECTOR model.
BS10FW
FBS-10FW model.
BS20GW
FBS-20GW model.
BS20GN
FBS-20G model.
FVG51G
FEV-511G model.
FXE11G
FEX-101G model.
FX211G
FEX-211G model.
FWE50G
FEW-50G-EA model.
FWA50G
FEW-50G-AM model.
name
FortiExtender profile name.
string
Maximum
length: 31
** Values may differ between models.
config cellular
Parameter
Description
Type
Size
Default
dataplan
<name>
Dataplan names.
Dataplan name.
string
Maximum length:
79
FortiOS 8.0.0 CLI Reference
358
Fortinet Inc.

<!-- 来源页 359 -->
config controller-report
Parameter
Description
Type
Size
Default
interval
Controller report interval.
integer
Minimum value:
0 Maximum
value:
4294967295
300
signal-threshold
Controller report signal threshold.
integer
Minimum value:
10 Maximum
value: 50
10
status
FortiExtender controller report status.
option
-disable
Option
Description
disable
Controller is configured to not provide service to this FortiExtender.
enable
Controller is configured to provide service to this FortiExtender.
config modem1
Parameter
Description
Type
Size
Default
conn-status
Connection status. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
default-sim
Default SIM selection.
option
-sim1
Option
Description
sim1
Use SIM #1 by default.
sim2
Use SIM #2 by default.
carrier
Assign default SIM based on carrier.
cost
Assign default SIM based on cost.
gps
FortiExtender GPS enable/disable.
option
-enable
Option
Description
disable
Disable GPS.
enable
Enable GPS.
multiple-PDN
Multiple-PDN enable/disable.
option
-disable
FortiOS 8.0.0 CLI Reference
359
Fortinet Inc.

<!-- 来源页 360 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable multiple PDN.
enable
Enable multiple PDN.
pdn1-dataplan
PDN1-dataplan.
string
Maximum
length: 31
pdn2-dataplan
PDN2-dataplan.
string
Maximum
length: 31
pdn3-dataplan
PDN3-dataplan.
string
Maximum
length: 31
pdn4-dataplan
PDN4-dataplan.
string
Maximum
length: 31
preferred-carrier
Preferred carrier.
string
Maximum
length: 31
redundant-intf
Redundant interface.
string
Maximum
length: 15
redundant-mode
FortiExtender mode.
option
-disable
Option
Description
disable
Disable interface redundancy.
enable
Enable interface redundancy.
sim1-pin
SIM #1 PIN status.
option
-disable
Option
Description
disable
Disable SIM #1 PIN.
enable
Enable SIM #1 PIN.
sim1-pin-code
SIM #1 PIN password.
password
Not Specified
sim2-pin
SIM #2 PIN status.
option
-disable
Option
Description
disable
Disable SIM #2 PIN.
enable
Enable SIM #2 PIN.
sim2-pin-code
SIM #2 PIN password.
password
Not Specified
FortiOS 8.0.0 CLI Reference
360
Fortinet Inc.

<!-- 来源页 361 -->
config auto-switch
Parameter
Description
Type
Size
Default
dataplan
Automatically switch based on data usage.
option
-disable
Option
Description
disable
Disable switching of SIM card based on cellular data usage.
enable
Enable switching of SIM card based on cellular data usage.
disconnect
Auto switch by disconnect.
option
-disable
Option
Description
disable
Disable switching of SIM card based on cellular disconnections.
enable
Enable switching of SIM card based on cellular disconnections.
disconnect-period
Automatically switch based on disconnect
period.
integer
Minimum
value: 600
Maximum
value: 18000
600
disconnect-threshold
Automatically switch based on disconnect
threshold.
integer
Minimum
value: 1
Maximum
value: 100
3
signal
Automatically switch based on signal strength.
option
-disable
Option
Description
disable
Disable switching of SIM card based on cellular signal quality.
enable
Enable switching of SIM card based on cellular signal quality.
switch-back
Auto switch with switch back multi-options.
option
-Option
Description
time
Switch back based on specific time in UTC (HH:MM).
timer
Switch back based on an interval.
switch-back-time
Automatically switch over to preferred
SIM/carrier at a specified time in UTC (HH:MM).
string
Maximum
length: 31
00:01
switch-back-timer
Automatically switch over to preferred
SIM/carrier after the given time (3600 -2147483647 sec).
integer
Minimum
value: 3600
Maximum
value:
2147483647
86400
FortiOS 8.0.0 CLI Reference
361
Fortinet Inc.

<!-- 来源页 362 -->
config modem2
Parameter
Description
Type
Size
Default
conn-status
Connection status. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
default-sim
Default SIM selection.
option
-sim1
Option
Description
sim1
Use SIM #1 by default.
sim2
Use SIM #2 by default.
carrier
Assign default SIM based on carrier.
cost
Assign default SIM based on cost.
gps
FortiExtender GPS enable/disable.
option
-enable
Option
Description
disable
Disable GPS.
enable
Enable GPS.
multiple-PDN
Multiple-PDN enable/disable.
option
-disable
Option
Description
disable
Disable multiple PDN.
enable
Enable multiple PDN.
pdn1-dataplan
PDN1-dataplan.
string
Maximum
length: 31
pdn2-dataplan
PDN2-dataplan.
string
Maximum
length: 31
pdn3-dataplan
PDN3-dataplan.
string
Maximum
length: 31
pdn4-dataplan
PDN4-dataplan.
string
Maximum
length: 31
preferred-carrier
Preferred carrier.
string
Maximum
length: 31
redundant-intf
Redundant interface.
string
Maximum
length: 15
redundant-mode
FortiExtender mode.
option
-disable
FortiOS 8.0.0 CLI Reference
362
Fortinet Inc.

<!-- 来源页 363 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable interface redundancy.
enable
Enable interface redundancy.
sim1-pin
SIM #1 PIN status.
option
-disable
Option
Description
disable
Disable SIM #1 PIN.
enable
Enable SIM #1 PIN.
sim1-pin-code
SIM #1 PIN password.
password
Not Specified
sim2-pin
SIM #2 PIN status.
option
-disable
Option
Description
disable
Disable SIM #2 PIN.
enable
Enable SIM #2 PIN.
sim2-pin-code
SIM #2 PIN password.
password
Not Specified
config auto-switch
Parameter
Description
Type
Size
Default
dataplan
Automatically switch based on data usage.
option
-disable
Option
Description
disable
Disable switching of SIM card based on cellular data usage.
enable
Enable switching of SIM card based on cellular data usage.
disconnect
Auto switch by disconnect.
option
-disable
Option
Description
disable
Disable switching of SIM card based on cellular disconnections.
enable
Enable switching of SIM card based on cellular disconnections.
disconnect-period
Automatically switch based on disconnect
period.
integer
Minimum
value: 600
Maximum
value: 18000
600
FortiOS 8.0.0 CLI Reference
363
Fortinet Inc.

<!-- 来源页 364 -->
Parameter
Description
Type
Size
Default
disconnect-threshold
Automatically switch based on disconnect
threshold.
integer
Minimum
value: 1
Maximum
value: 100
3
signal
Automatically switch based on signal strength.
option
-disable
Option
Description
disable
Disable switching of SIM card based on cellular signal quality.
enable
Enable switching of SIM card based on cellular signal quality.
switch-back
Auto switch with switch back multi-options.
option
-Option
Description
time
Switch back based on specific time in UTC (HH:MM).
timer
Switch back based on an interval.
switch-back-time
Automatically switch over to preferred
SIM/carrier at a specified time in UTC (HH:MM).
string
Maximum
length: 31
00:01
switch-back-timer
Automatically switch over to preferred
SIM/carrier after the given time (3600 -2147483647 sec).
integer
Minimum
value: 3600
Maximum
value:
2147483647
86400
config sms-notification
Parameter
Description
Type
Size
Default
status
FortiExtender SMS notification status.
option
-disable
Option
Description
disable
SMS notification is configured to not provide service to this
FortiExtender.
enable
SMS notification is configured to provide service to this FortiExtender.
config alert
Parameter
Description
Type
Size
Default
data-exhausted
Display string when data exhausted.
string
Maximum
length: 63
data plan is
exhausted
FortiOS 8.0.0 CLI Reference
364
Fortinet Inc.

<!-- 来源页 365 -->
Parameter
Description
Type
Size
Default
fgt-backup-mode-switch
Display string when FortiGate backup mode
switched.
string
Maximum
length: 63
FortiGate
backup work
mode switched
low-signal-strength
Display string when signal strength is low.
string
Maximum
length: 63
LTE signal
strength is too
low
mode-switch
Display string when mode is switched.
string
Maximum
length: 63
system
networking
mode switched
os-image-fallback
Display string when falling back to a previous
OS image.
string
Maximum
length: 63
system start to
fallback OS
image
session-disconnect
Display string when session disconnected.
string
Maximum
length: 63
LTE data
session is
disconnected
system-reboot
Display string when system rebooted.
string
Maximum
length: 63
system will
reboot
config receiver
Parameter
Description
Type
Size
Default
alert
Alert multi-options.
option
-Option
Description
system-reboot
System will reboot.
data-exhausted
Data plan is exhausted.
session-disconnect
LTE data session is disconnected.
low-signal-strength
LTE signal strength is too low.
mode-switch
System is starting to use fallback OS image.
os-image-fallback
System networking mode switched.
fgt-backup-mode-switch
FortiGate backup work mode switched.
name
FortiExtender SMS notification receiver name.
string
Maximum
length: 31
FortiOS 8.0.0 CLI Reference
365
Fortinet Inc.

<!-- 来源页 366 -->
Parameter
Description
Type
Size
Default
phone-number
Receiver phone number. Format: [+][country code]
[area code][local phone number]. For example,
+16501234567.
string
Maximum
length: 31
status
SMS notification receiver status.
option
-disable
Option
Description
disable
Disable SMS notification receiver.
enable
Enable SMS notification receiver.
config lan-extension
Parameter
Description
Type
Size
Default
backhaul-interface
IPsec phase1 interface.
string
Maximum
length: 15
backhaul-ip
IPsec phase1 IPv4/FQDN. Used to specify the
external IP/FQDN when the FortiGate unit is
behind a NAT device.
string
Maximum
length: 63
ipsec-tunnel
IPsec tunnel name.
string
Maximum
length: 15
link-loadbalance
LAN extension link load balance strategy.
option
-activebackup
Option
Description
activebackup
FortiExtender LAN extension active-backup.
loadbalance
FortiExtender LAN extension load-balance.
config backhaul
Parameter
Description
Type
Size
Default
health-check-fail-cnt
Number of failures before the link is considered
dead (1 - 10, default = 5).
integer
Minimum
value: 1
Maximum
value: 10
5
health-check-interval
Health monitoring interval in seconds (1 - 3600,
default = 5).
integer
Minimum
value: 1
Maximum
value: 3600
5
FortiOS 8.0.0 CLI Reference
366
Fortinet Inc.

<!-- 来源页 367 -->
Parameter
Description
Type
Size
Default
health-check-probe-cnt
Number of health monitoring probes to send within
an interval (1 - 10, default = 1).
integer
Minimum
value: 1
Maximum
value: 10
1
health-check-probe-tm
Health monitoring probe timeout in seconds (1 - 10,
default = 2).
integer
Minimum
value: 1
Maximum
value: 10
2
health-check-recovery-cnt
Number of successful checks before the link is
considered alive (1 - 10, default = 5).
integer
Minimum
value: 1
Maximum
value: 10
5
name
FortiExtender LAN extension backhaul name.
string
Maximum
length: 31
port
FortiExtender uplink port.
option
-wan
Option
Description
wan
FortiExtender WAN port.
lte1
FortiExtender LTE1 port.
lte2
FortiExtender LTE2 port.
port1
FortiExtender port1 port.
port2
FortiExtender port2 port.
port3
FortiExtender port3 port.
port4
FortiExtender port4 port.
port5
FortiExtender port5 port.
sfp
FortiExtender SFP port.
role
FortiExtender uplink port.
option
-primary
Option
Description
primary
FortiExtender LAN extension primary role.
secondary
FortiExtender LAN extension secondary role.
weight
WRR weight parameter.
integer
Minimum
value: 1
Maximum
value: 256
1
FortiOS 8.0.0 CLI Reference
367
Fortinet Inc.

<!-- 来源页 368 -->
config downlinks
Parameter
Description
Type
Size
Default
name
FortiExtender LAN extension downlink config entry
name.
string
Maximum
length: 31
port
FortiExtender LAN extension downlink port.
option
-Option
Description
port1
FortiExtender port1 port.
port2
FortiExtender port2 port.
port3
FortiExtender port3 port.
port4
FortiExtender port4 port.
port5
FortiExtender port5 port.
lan1
FortiExtender LAN1 port.
lan2
FortiExtender LAN2 port.
lan
FortiExtender LAN port.
pvid
FortiExtender LAN extension downlink PVID (1 -4089).
integer
Minimum
value: 1
Maximum
value: 4089
1
type
FortiExtender LAN extension downlink type
[port/vap].
option
-port
Option
Description
port
LAN extension Downlink type: port
vap
LAN extension Downlink type: Wi-Fi VAP
vap
FortiExtender LAN extension downlink vap.
string
Maximum
length: 31
vids <vid>
FortiExtender LAN extension downlink VIDs.
Enter VID numbers (1 - 4089) separated by spaces.
Up to 50 VIDs can be configured.
integer
Minimum
value: 1
Maximum
value: 4089
config traffic-split-services
Parameter
Description
Type
Size
Default
address
Address selection.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
368
Fortinet Inc.

<!-- 来源页 369 -->
Parameter
Description
Type
Size
Default
name
FortiExtender LAN extension tunnel split entry
name.
string
Maximum
length: 31
service
Service selection.
string
Maximum
length: 79
ALL
vsdb
Set video streaming traffic goes through local WAN
[enable/disable].
option
-disable
Option
Description
disable
Disable video streaming traffic goes through FortiExtender local WAN
enable
Enable video streaming traffic goes through FortiExtender local WAN
config wifi
Parameter
Description
Type
Size
Default
country
Country in which this FEX will operate (default =
NA).
option
---Option
Description
--NO_COUNTRY_SET
AF
AFGHANISTAN
AL
ALBANIA
DZ
ALGERIA
AS
AMERICAN SAMOA
AO
ANGOLA
AR
ARGENTINA
AM
ARMENIA
AU
AUSTRALIA
AT
AUSTRIA
AZ
AZERBAIJAN
BS
BAHAMAS
BH
BAHRAIN
BD
BANGLADESH
BB
BARBADOS
BY
BELARUS
FortiOS 8.0.0 CLI Reference
369
Fortinet Inc.

<!-- 来源页 370 -->
Parameter
Description
Type
Size
Default
Option
Description
BE
BELGIUM
BZ
BELIZE
BJ
BENIN
BM
BERMUDA
BT
BHUTAN
BO
BOLIVIA
BA
BOSNIA AND HERZEGOVINA
BW
BOTSWANA
BR
BRAZIL
BN
BRUNEI DARUSSALAM
BG
BULGARIA
BF
BURKINA-FASO
KH
CAMBODIA
CM
CAMEROON
KY
CAYMAN ISLANDS
CF
CENTRAL AFRICA REPUBLIC
TD
CHAD
CL
CHILE
CN
CHINA
CX
CHRISTMAS ISLAND
CO
COLOMBIA
CG
CONGO REPUBLIC
CD
DEMOCRATIC REPUBLIC OF CONGO
CR
COSTA RICA
HR
CROATIA
CY
CYPRUS
CZ
CZECH REPUBLIC
DK
DENMARK
DJ
DJIBOUTI
FortiOS 8.0.0 CLI Reference
370
Fortinet Inc.

<!-- 来源页 371 -->
Parameter
Description
Type
Size
Default
Option
Description
DM
DOMINICA
DO
DOMINICAN REPUBLIC
EC
ECUADOR
EG
EGYPT
SV
EL SALVADOR
ET
ETHIOPIA
EE
ESTONIA
GF
FRENCH GUIANA
PF
FRENCH POLYNESIA
FO
FAEROE ISLANDS
FJ
FIJI
FI
FINLAND
FR
FRANCE
GA
GABON
GE
GEORGIA
GM
GAMBIA
DE
GERMANY
GH
GHANA
GI
GIBRALTAR
GR
GREECE
GL
GREENLAND
GD
GRENADA
GP
GUADELOUPE
GU
GUAM
GT
GUATEMALA
GY
GUYANA
HT
HAITI
HN
HONDURAS
HK
HONG KONG
FortiOS 8.0.0 CLI Reference
371
Fortinet Inc.

<!-- 来源页 372 -->
Parameter
Description
Type
Size
Default
Option
Description
HU
HUNGARY
IS
ICELAND
IN
INDIA
ID
INDONESIA
IQ
IRAQ
IE
IRELAND
IM
ISLE OF MAN
IL
ISRAEL
IT
ITALY
CI
COTE_D_IVOIRE
JM
JAMAICA
JO
JORDAN
KZ
KAZAKHSTAN
KE
KENYA
KR
KOREA REPUBLIC
KW
KUWAIT
LA
LAOS
LV
LATVIA
LB
LEBANON
LS
LESOTHO
LR
LIBERIA
LY
LIBYA
LI
LIECHTENSTEIN
LT
LITHUANIA
LU
LUXEMBOURG
MO
MACAU SAR
MK
MACEDONIA, FYRO
MG
MADAGASCAR
MW
MALAWI
FortiOS 8.0.0 CLI Reference
372
Fortinet Inc.

<!-- 来源页 373 -->
Parameter
Description
Type
Size
Default
Option
Description
MY
MALAYSIA
MV
MALDIVES
ML
MALI
MT
MALTA
MH
MARSHALL ISLANDS
MQ
MARTINIQUE
MR
MAURITANIA
MU
MAURITIUS
YT
MAYOTTE
MX
MEXICO
FM
MICRONESIA
MD
REPUBLIC OF MOLDOVA
MC
MONACO
MN
MONGOLIA
MA
MOROCCO
MZ
MOZAMBIQUE
MM
MYANMAR
NA
NAMIBIA
NP
NEPAL
NL
NETHERLANDS
AN
NETHERLANDS ANTILLES
AW
ARUBA
NZ
NEW ZEALAND
NI
NICARAGUA
NE
NIGER
NG
NIGERIA
NO
NORWAY
MP
NORTHERN MARIANA ISLANDS
OM
OMAN
FortiOS 8.0.0 CLI Reference
373
Fortinet Inc.

<!-- 来源页 374 -->
Parameter
Description
Type
Size
Default
Option
Description
PK
PAKISTAN
PW
PALAU
PA
PANAMA
PG
PAPUA NEW GUINEA
PY
PARAGUAY
PE
PERU
PH
PHILIPPINES
PL
POLAND
PT
PORTUGAL
PR
PUERTO RICO
QA
QATAR
RE
REUNION
RO
ROMANIA
RU
RUSSIA
RW
RWANDA
BL
SAINT BARTHELEMY
KN
SAINT KITTS AND NEVIS
LC
SAINT LUCIA
MF
SAINT MARTIN
PM
SAINT PIERRE AND MIQUELON
VC
SAINT VINCENT AND GRENADIENS
SA
SAUDI ARABIA
SN
SENEGAL
RS
REPUBLIC OF SERBIA
ME
MONTENEGRO
SL
SIERRA LEONE
SG
SINGAPORE
SK
SLOVAKIA
SI
SLOVENIA
FortiOS 8.0.0 CLI Reference
374
Fortinet Inc.

<!-- 来源页 375 -->
Parameter
Description
Type
Size
Default
Option
Description
SO
SOMALIA
ZA
SOUTH AFRICA
ES
SPAIN
LK
SRI LANKA
SR
SURINAME
SZ
SWAZILAND
SE
SWEDEN
CH
SWITZERLAND
TW
TAIWAN
TZ
TANZANIA
TH
THAILAND
TL
TIMOR-LESTE
TG
TOGO
TT
TRINIDAD AND TOBAGO
TN
TUNISIA
TR
TURKEY
TM
TURKMENISTAN
AE
UNITED ARAB EMIRATES
TC
TURKS AND CAICOS
UG
UGANDA
UA
UKRAINE
GB
UNITED KINGDOM
US
UNITED STATES
PS
UNITED STATES (PUBLIC SAFETY)
UY
URUGUAY
UZ
UZBEKISTAN
VU
VANUATU
VE
VENEZUELA
VN
VIET NAM
FortiOS 8.0.0 CLI Reference
375
Fortinet Inc.

<!-- 来源页 376 -->
Parameter
Description
Type
Size
Default
Option
Description
VI
VIRGIN ISLANDS
WF
WALLIS AND FUTUNA
YE
YEMEN
ZM
ZAMBIA
ZW
ZIMBABWE
JP
JAPAN
CA
CANADA
config radio-1
Parameter
Description
Type
Size
Default
80211d
Enable/disable Wi-Fi 802.11d.
option
-enable
Option
Description
disable
Disable 802.11d.
enable
Enable 802.11d.
band
Wi-Fi band selection 2.4GHz / 5GHz.
option
-2.4GHz
Option
Description
2.4GHz
Wi-Fi 2.4GHz
bandwidth
Wi-Fi channel bandwidth.
option
-auto
Option
Description
auto
Wi-Fi channel bandwidth auto
20MHz
Wi-Fi channel bandwidth 20MHz
40MHz
Wi-Fi channel bandwidth 40MHz
80MHz
Wi-Fi channel bandwidth 80MHz
beacon-interval
Wi-Fi beacon interval in miliseconds (100 - 3500,
default = 100).
integer
Minimum
value: 100
Maximum
value: 3500
100
FortiOS 8.0.0 CLI Reference
376
Fortinet Inc.

<!-- 来源页 377 -->
Parameter
Description
Type
Size
Default
bss-color
Wi-Fi 802.11AX BSS color value (0 - 63, 0 = disable,
default = 0).
integer
Minimum
value: 0
Maximum
value: 63
0
bss-color-mode
Wi-Fi 802.11AX BSS color mode.
option
-auto
Option
Description
auto
Wi-Fi BSS color mode auto
static
Wi-Fi BSS color mode static
channel
Wi-Fi channels.
option
-Option
Description
CH1
Channel 1
CH2
Channel 2
CH3
Channel 3
CH4
Channel 4
CH5
Channel 5
CH6
Channel 6
CH7
Channel 7
CH8
Channel 8
CH9
Channel 9
CH10
Channel 10
CH11
Channel 11
extension-channel
Wi-Fi extension channel.
option
-auto
Option
Description
auto
Wi-Fi extension channel auto.
higher
Wi-Fi extension channel higher.
lower
Wi-Fi extension channel lower.
guard-interval
Wi-Fi guard interval.
option
-auto
FortiOS 8.0.0 CLI Reference
377
Fortinet Inc.

<!-- 来源页 378 -->
Parameter
Description
Type
Size
Default
Option
Description
auto
Wi-Fi guard_interval auto
400ns
Wi-Fi guard_interval 400ns
800ns
Wi-Fi guard_interval 800ns
lan-ext-vap
Wi-Fi LAN-Extention VAP. Select only one VAP.
string
Maximum
length: 31
local-vaps
<name>
Wi-Fi local VAP. Select up to three VAPs.
Wi-Fi local VAP name.
string
Maximum
length: 79
max-clients
Maximum number of Wi-Fi radio clients (0 - 512, 0 =
unlimited, default = 0).
integer
Minimum
value: 0
Maximum
value: 512
0
mode
Wi-Fi radio mode AP(LAN mode) / Client(WAN
mode).
option
-AP
Option
Description
AP
AP Mode (LAN mode)
Client
Client mode (WAN mode)
operating-standard
Wi-Fi operating standard.
option
-auto
Option
Description
auto
Wi-Fi operating standard auto
11A-N-AC-AX
Wi-Fi support 802.11 A-N-AC
11A-N-AC
Wi-Fi support 802.11 A-N-AC
11A-N
Wi-Fi support 802.11 A-N
11A
Wi-Fi support 802.11 A
11N-AC-AX
Wi-Fi support 802.11 N-AC-AX
11AC-AX
Wi-Fi support 802.11 AC-AX
11AC
Wi-Fi support 802.11 AC
11N-AC
Wi-Fi support 802.11 N-AC
11B-G-N-AX
Wi-Fi support 802.11 B-G-N-AX
11B-G-N
Wi-Fi support 802.11 B-G-N
FortiOS 8.0.0 CLI Reference
378
Fortinet Inc.

<!-- 来源页 379 -->
Parameter
Description
Type
Size
Default
Option
Description
11B-G
Wi-Fi support 802.11 B-G
11B
Wi-Fi support 802.11 B
11G-N-AX
Wi-Fi support 802.11 G-N-AX
11N-AX
Wi-Fi support 802.11 N-AX
11AX
Wi-Fi support 802.11 AX
11G-N
Wi-Fi support 802.11 G-N
11N
Wi-Fi support 802.11 N
11G
Wi-Fi support 802.11 G
power-level
Wi-Fi power level in percent (0 - 100, 0 = auto,
default = 100).
integer
Minimum
value: 0
Maximum
value: 100
100
status
Enable/disable Wi-Fi radio.
option
-disable
Option
Description
disable
Disable Wi-Fi radio.
enable
Enable Wi-Fi radio.
config radio-2
Parameter
Description
Type
Size
Default
80211d
Enable/disable Wi-Fi 802.11d.
option
-enable
Option
Description
disable
Disable 802.11d.
enable
Enable 802.11d.
band
Wi-Fi band selection 2.4GHz / 5GHz.
option
-5GHz
Option
Description
5GHz
Wi-Fi 5GHz
bandwidth
Wi-Fi channel bandwidth.
option
-auto
Option
Description
auto
Wi-Fi channel bandwidth auto
FortiOS 8.0.0 CLI Reference
379
Fortinet Inc.

<!-- 来源页 380 -->
Parameter
Description
Type
Size
Default
Option
Description
20MHz
Wi-Fi channel bandwidth 20MHz
40MHz
Wi-Fi channel bandwidth 40MHz
80MHz
Wi-Fi channel bandwidth 80MHz
beacon-interval
Wi-Fi beacon interval in miliseconds (100 - 3500,
default = 100).
integer
Minimum
value: 100
Maximum
value: 3500
100
bss-color
Wi-Fi 802.11AX BSS color value (0 - 63, 0 = disable,
default = 0).
integer
Minimum
value: 0
Maximum
value: 63
0
bss-color-mode
Wi-Fi 802.11AX BSS color mode.
option
-auto
Option
Description
auto
Wi-Fi BSS color mode auto
static
Wi-Fi BSS color mode static
channel
Wi-Fi channels.
option
-Option
Description
CH36
Channel 36
CH40
Channel 40
CH44
Channel 44
CH48
Channel 48
CH52
Channel 52
CH56
Channel 56
CH60
Channel 60
CH64
Channel 64
CH100
Channel 100
CH104
Channel 104
CH108
Channel 108
CH112
Channel 112
FortiOS 8.0.0 CLI Reference
380
Fortinet Inc.

<!-- 来源页 381 -->
Parameter
Description
Type
Size
Default
Option
Description
CH116
Channel 116
CH120
Channel 120
CH124
Channel 124
CH128
Channel 128
CH132
Channel 132
CH136
Channel 136
CH140
Channel 140
CH144
Channel 144
CH149
Channel 149
CH153
Channel 153
CH157
Channel 157
CH161
Channel 161
CH165
Channel 165
extension-channel
Wi-Fi extension channel.
option
-auto
Option
Description
auto
Wi-Fi extension channel auto.
higher
Wi-Fi extension channel higher.
lower
Wi-Fi extension channel lower.
guard-interval
Wi-Fi guard interval.
option
-auto
Option
Description
auto
Wi-Fi guard_interval auto
400ns
Wi-Fi guard_interval 400ns
800ns
Wi-Fi guard_interval 800ns
lan-ext-vap
Wi-Fi LAN-Extention VAP. Select only one VAP.
string
Maximum
length: 31
local-vaps
<name>
Wi-Fi local VAP. Select up to three VAPs.
Wi-Fi local VAP name.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
381
Fortinet Inc.

<!-- 来源页 382 -->
Parameter
Description
Type
Size
Default
max-clients
Maximum number of Wi-Fi radio clients (0 - 512, 0 =
unlimited, default = 0).
integer
Minimum
value: 0
Maximum
value: 512
0
mode
Wi-Fi radio mode AP(LAN mode) / Client(WAN
mode).
option
-AP
Option
Description
AP
AP Mode (LAN mode)
Client
Client mode (WAN mode)
operating-standard
Wi-Fi operating standard.
option
-auto
Option
Description
auto
Wi-Fi operating standard auto
11A-N-AC-AX
Wi-Fi support 802.11 A-N-AC
11A-N-AC
Wi-Fi support 802.11 A-N-AC
11A-N
Wi-Fi support 802.11 A-N
11A
Wi-Fi support 802.11 A
11N-AC-AX
Wi-Fi support 802.11 N-AC-AX
11AC-AX
Wi-Fi support 802.11 AC-AX
11AC
Wi-Fi support 802.11 AC
11N-AC
Wi-Fi support 802.11 N-AC
11B-G-N-AX
Wi-Fi support 802.11 B-G-N-AX
11B-G-N
Wi-Fi support 802.11 B-G-N
11B-G
Wi-Fi support 802.11 B-G
11B
Wi-Fi support 802.11 B
11G-N-AX
Wi-Fi support 802.11 G-N-AX
11N-AX
Wi-Fi support 802.11 N-AX
11AX
Wi-Fi support 802.11 AX
11G-N
Wi-Fi support 802.11 G-N
11N
Wi-Fi support 802.11 N
11G
Wi-Fi support 802.11 G
FortiOS 8.0.0 CLI Reference
382
Fortinet Inc.

<!-- 来源页 383 -->
Parameter
Description
Type
Size
Default
power-level
Wi-Fi power level in percent (0 - 100, 0 = auto,
default = 100).
integer
Minimum
value: 0
Maximum
value: 100
100
status
Enable/disable Wi-Fi radio.
option
-disable
Option
Description
disable
Disable Wi-Fi radio.
enable
Enable Wi-Fi radio.
config extension-controller extender-vap
FortiExtender wifi vap configuration.
config extension-controller extender-vap
Description: FortiExtender wifi vap configuration.
edit <name>
set allowaccess {option1}, {option2}, ...
set auth-server-address {string}
set auth-server-port {integer}
set auth-server-secret {string}
set broadcast-ssid [disable|enable]
set bss-color-partial [disable|enable]
set dtim {integer}
set end-ip {ipv4-address}
set ip-address {ipv4-classnet-host}
set max-clients {integer}
set mu-mimo [disable|enable]
set passphrase {password}
set pmf [disabled|optional|...]
set rts-threshold {integer}
set sae-password {password}
set security [OPEN|WPA2-Personal|...]
set security-exempt-list {string}
set security-external-web {string}
set security-groups <name1>, <name2>, ...
set security-mode [none|captive-portal]
set security-redirect-url {string}
set ssid {string}
set start-ip {ipv4-address}
set target-wake-time [disable|enable]
set type [local-vap|lan-ext-vap]
next
end
FortiOS 8.0.0 CLI Reference
383
Fortinet Inc.

<!-- 来源页 384 -->
config extension-controller extender-vap
Parameter
Description
Type
Size
Default
allowaccess
Control management access to the managed
extender. Separate entries with a space.
option
-Option
Description
ping
PING access.
telnet
TELNET access.
http
HTTP access.
https
HTTPS access.
ssh
SSH access.
snmp
SNMP access.
auth-server-address
Wi-Fi Authentication Server Address (IPv4
format).
string
Maximum
length: 63
auth-server-port
Wi-Fi Authentication Server Port.
integer
Minimum
value: 1
Maximum
value:
65535
0
auth-server-secret
Wi-Fi Authentication Server Secret.
string
Maximum
length: 63
broadcast-ssid
Enable/disable Wi-Fi broadcast SSID.
option
-enable
Option
Description
disable
Disable broadcast SSID.
enable
Enable broadcast SSID.
bss-color-partial
Enable/disable Wi-Fi 802.11AX BSS color partial
(default = enable).
option
-enable
Option
Description
disable
Disable bss color partial.
enable
Enable bss color partial.
dtim
Wi-Fi DTIM (1 - 255, default = 1).
integer
Minimum
value: 1
Maximum
value: 255
1
FortiOS 8.0.0 CLI Reference
384
Fortinet Inc.

<!-- 来源页 385 -->
Parameter
Description
Type
Size
Default
end-ip
End IP address.
ipv4-address
Not
Specified
0.0.0.0
ip-address
Extender IP address.
ipv4-classnet-host
Not
Specified
0.0.0.0
0.0.0.0
max-clients
Wi-Fi maximum clients (0 - 512, default = 0,
which means no limit).
integer
Minimum
value: 0
Maximum
value: 512
0
mu-mimo
Enable/disable Wi-Fi multi-user MIMO (default =
enable).
option
-enable
Option
Description
disable
Disable multi-user MIMO.
enable
Enable multi-user MIMO.
name
Wi-Fi VAP name.
string
Maximum
length: 15
passphrase
Wi-Fi passphrase.
password
Not
Specified
pmf
Enable/disable Wi-Fi PMF (default = disable).
option
-disabled
Option
Description
disabled
Disable PMF (Protected Management Frames).
optional
Set PMF (Protected Management Frames) optional.
required
Require PMF (Protected Management Frames).
rts-threshold
Wi-Fi RTS threshold (256 - 2347, default = 2347,
which disables RTS/CTS).
integer
Minimum
value: 256
Maximum
value: 2347
2347
sae-password
Wi-Fi SAE Password.
password
Not
Specified
security
Wi-Fi security.
option
-WPA2-Personal
Option
Description
OPEN
Wi-Fi security OPEN
FortiOS 8.0.0 CLI Reference
385
Fortinet Inc.

<!-- 来源页 386 -->
Parameter
Description
Type
Size
Default
Option
Description
WPA2-Personal
Wi-Fi security WPA2 Personal
WPA-WPA2-Personal
Wi-Fi security WPA-WPA2 Personal
WPA3-SAE
Wi-Fi security WPA3 SAE
WPA3-SAE-Transition
Wi-Fi security WPA3 SAE Transition
WPA2-Enterprise
Wi-Fi security WPA2 Enterprise
WPA3-Enterprise-only
Wi-Fi security WPA3 Enterprise only
WPA3-Enterprise-transition
Wi-Fi security WPA3 Enterprise Transition
WPA3-Enterprise-192-bit
Wi-Fi security WPA3 Enterprise 192-bit
security-exempt-list *
Name of security exempt list.
string
Maximum
length: 35
security-external-web
*
URL of external authentication web server.
string
Maximum
length: 255
security-groups <name>
*
User groups that can authenticate with the
captive portal.
Names of user groups that can authenticate with
the captive portal.
string
Maximum
length: 79
security-mode *
Turn on captive portal authentication for this Wi-Fi interface.
option
-none
Option
Description
none
No security option.
captive-portal
Captive portal authentication.
security-redirect-url *
Optional URL for redirecting users after they pass
captive portal authentication.
string
Maximum
length: 255
ssid
Wi-Fi SSID.
string
Maximum
length: 32
FortiOS 8.0.0 CLI Reference
386
Fortinet Inc.

<!-- 来源页 387 -->
Parameter
Description
Type
Size
Default
start-ip
Start IP address.
ipv4-address
Not
Specified
0.0.0.0
target-wake-time
Enable/disable Wi-Fi 802.11AX target wake time
(default = enable).
option
-enable
Option
Description
disable
Disable target wake time.
enable
Enable target wake time.
type
Wi-Fi VAP type local-vap / lan-extension-vap.
option
-Option
Description
local-vap
Local VAP.
lan-ext-vap
Lan Extension VAP.
* This parameter may not exist in some models.
config extension-controller fortigate
FortiGate controller configuration.
config extension-controller fortigate
Description: FortiGate controller configuration.
edit <name>
set authorized [discovered|disable|...]
set description {string}
set device-id {integer}
set hostname {string}
set id {string}
set profile {string}
set vdom {integer}
next
end
config extension-controller fortigate
Parameter
Description
Type
Size
Default
authorized
Enable/disable FortiGate administration.
option
-discovered
FortiOS 8.0.0 CLI Reference
387
Fortinet Inc.

<!-- 来源页 388 -->
Parameter
Description
Type
Size
Default
Option
Description
discovered
Controller discovered this FortiGate.
disable
Controller is configured to not provide service to this FortiGate.
enable
Controller is configured to provide service to this FortiGate.
description
Description.
string
Maximum
length: 255
device-id
Device ID.
integer
Minimum value:
0 Maximum
value:
4294967295
1026
hostname
FortiGate hostname.
string
Maximum
length: 31
id
FortiGate serial number.
string
Maximum
length: 19
name
FortiGate entry name.
string
Maximum
length: 19
profile
FortiGate profile configuration.
string
Maximum
length: 31
vdom
VDOM. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config extension-controller fortigate-profile
FortiGate connector profile configuration.
config extension-controller fortigate-profile
Description: FortiGate connector profile configuration.
edit <name>
set extension {option}
set id {integer}
config lan-extension
Description: FortiGate connector LAN extension configuration.
set backhaul-interface {string}
set backhaul-ip {string}
set ipsec-tunnel {string}
end
next
end
FortiOS 8.0.0 CLI Reference
388
Fortinet Inc.

<!-- 来源页 389 -->
config extension-controller fortigate-profile
Parameter
Description
Type
Size
Default
extension
Extension option. Read-only.
option
-lan-extension
Option
Description
lan-extension
LAN extension.
id
ID.
integer
Minimum
value: 0
Maximum
value:
102400000
32
name
FortiGate connector profile name.
string
Maximum
length: 31
config lan-extension
Parameter
Description
Type
Size
Default
backhaul-interface
IPsec phase1 interface.
string
Maximum
length: 15
backhaul-ip
IPsec phase1 IPv4/FQDN. Used to specify the
external IP/FQDN when the FortiGate unit is behind
a NAT device.
string
Maximum
length: 63
ipsec-tunnel
IPsec tunnel name.
string
Maximum
length: 15
FortiOS 8.0.0 CLI Reference
389
Fortinet Inc.

---


<!-- 来源页 1310 -->
switch-controller
This section includes syntax for the following commands:
l config switch-controller 802-1X-settings on page 1311
l config switch-controller acl group on page 1314
l config switch-controller acl ingress on page 1314
l config switch-controller auto-config custom on page 1316
l config switch-controller auto-config default on page 1317
l config switch-controller auto-config policy on page 1317
l config switch-controller custom-command on page 1318
l config switch-controller dsl policy on page 1320
l config switch-controller dynamic-port-policy on page 1322
l config switch-controller flow-tracking on page 1325
l config switch-controller fortilink-settings on page 1329
l config switch-controller global on page 1331
l config switch-controller igmp-snooping-static-group on page 1338
l config switch-controller igmp-snooping on page 1337
l config switch-controller initial-config template on page 1339
l config switch-controller initial-config vlans on page 1341
l config switch-controller ip-source-guard-log on page 1342
l config switch-controller lldp-profile on page 1343
l config switch-controller lldp-settings on page 1347
l config switch-controller location on page 1348
l config switch-controller mac-policy on page 1353
l config switch-controller managed-switch on page 1354
l config switch-controller network-monitor-settings on page 1407
l config switch-controller ptp interface-policy on page 1407
l config switch-controller ptp profile on page 1408
l config switch-controller qos dot1p-map on page 1409
l config switch-controller qos ip-dscp-map on page 1413
l config switch-controller qos qos-policy on page 1415
l config switch-controller qos queue-policy on page 1416
l config switch-controller quarantine on page 1418
l config switch-controller remote-log on page 1419
l config switch-controller security-policy 802-1X on page 1421
l config switch-controller security-policy admin on page 1426
l config switch-controller security-policy local-access on page 1428
l config switch-controller sflow on page 1430
l config switch-controller snmp-community on page 1430
FortiOS 8.0.0 CLI Reference
1310
Fortinet Inc.

<!-- 来源页 1311 -->
l config switch-controller snmp-sysinfo on page 1433
l config switch-controller snmp-trap-threshold on page 1434
l config switch-controller snmp-user on page 1434
l config switch-controller storm-control-policy on page 1437
l config switch-controller storm-control on page 1436
l config switch-controller stp-instance on page 1439
l config switch-controller stp-settings on page 1439
l config switch-controller switch-group on page 1440
l config switch-controller switch-interface-tag on page 1441
l config switch-controller switch-log on page 1441
l config switch-controller switch-profile on page 1442
l config switch-controller system on page 1444
l config switch-controller traffic-policy on page 1446
l config switch-controller traffic-sniffer on page 1447
l config switch-controller virtual-port-pool on page 1449
l config switch-controller vlan-policy on page 1449
config switch-controller 802-1X-settings
Configure global 802.1X settings.
config switch-controller 802-1X-settings
Description: Configure global 802.1X settings.
set allow-mac-move [disable|enable]
set link-down-auth [set-unauth|no-action]
set mab-entry-as [static|dynamic]
set mab-reauth [disable|enable]
set mac-called-station-delimiter [colon|hyphen|...]
set mac-calling-station-delimiter [colon|hyphen|...]
set mac-case [lowercase|uppercase]
set mac-password-delimiter [colon|hyphen|...]
set mac-username-delimiter [colon|hyphen|...]
set max-reauth-attempt {integer}
set reauth-period {integer}
set tx-period {integer}
end
config switch-controller 802-1X-settings
Parameter
Description
Type
Size
Default
allow-mac-move *
Enable/disable MAC move (default = enable).
option
-enable
FortiOS 8.0.0 CLI Reference
1311
Fortinet Inc.

<!-- 来源页 1312 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable MAC move.
enable
Enable MAC move.
link-down-auth
Interface-reauthentication state to set if a link is
down.
option
-set-unauth
Option
Description
set-unauth
Interface set to unauth when down. Reauthentication is needed.
no-action
Interface reauthentication is not needed.
mab-entry-as
*
Configure MAB MAC entry as static or dynamic
(default = static).
option
-static
Option
Description
static
MAB MAC entry as static.
dynamic
MAB MAC entry as dynamic.
mab-reauth
Enable/disable MAB re-authentication.
option
-disable
Option
Description
disable
Disable MAB re-authentication.
enable
Enable MAB re-authentication.
mac-called-station-delimiter
MAC called station delimiter (default = hyphen).
option
-hyphen
Option
Description
colon
Use colon as delimiter for called station.
hyphen
Use hyphen as delimiter for called station.
none
No delimiter for called station.
single-hyphen
Use single hyphen as delimiter for called station.
mac-calling-station-delimiter
MAC calling station delimiter (default = hyphen).
option
-hyphen
FortiOS 8.0.0 CLI Reference
1312
Fortinet Inc.

<!-- 来源页 1313 -->
Parameter
Description
Type
Size
Default
Option
Description
colon
Use colon as delimiter for calling station.
hyphen
Use hyphen as delimiter for calling station.
none
No delimiter for calling station.
single-hyphen
Use single hyphen as delimiter for calling station.
mac-case
MAC case (default = lowercase).
option
-lowercase
Option
Description
lowercase
Use lowercase MAC.
uppercase
Use uppercase MAC.
mac-password-delimiter
MAC authentication password delimiter (default =
hyphen).
option
-hyphen
Option
Description
colon
Use colon as delimiter for MAC auth password.
hyphen
Use hyphen as delimiter for MAC auth password.
none
No delimiter for MAC auth password.
single-hyphen
Use single hyphen as delimiter for MAC auth password.
mac-username-delimiter
MAC authentication username delimiter (default =
hyphen).
option
-hyphen
Option
Description
colon
Use colon as delimiter for MAC auth username.
hyphen
Use hyphen as delimiter for MAC auth username.
none
No delimiter for MAC auth username.
single-hyphen
Use single hyphen as delimiter for MAC auth username.
max-reauth-attempt
Maximum number of authentication attempts (0 -15, default = 3).
integer
Minimum
value: 0
Maximum
value: 15
3
FortiOS 8.0.0 CLI Reference
1313
Fortinet Inc.

<!-- 来源页 1314 -->
Parameter
Description
Type
Size
Default
reauth-period
Period of time to allow for reauthentication (1 -1440 sec, default = 60, 0 = disable
reauthentication).
integer
Minimum
value: 0
Maximum
value: 1440
60
tx-period
802.1X Tx period (seconds, default=30).
integer
Minimum
value: 12
Maximum
value: 60
30
* This parameter may not exist in some models.
config switch-controller acl group
Configure ACL groups to be applied on managed FortiSwitch ports.
config switch-controller acl group
Description: Configure ACL groups to be applied on managed FortiSwitch ports.
edit <name>
set ingress <id1>, <id2>, ...
next
end
config switch-controller acl group
Parameter
Description
Type
Size
Default
ingress <id>
Configure ingress ACL policies in group.
ACL ID.
integer
Minimum value:
0 Maximum
value:
4294967295
name
Group name.
string
Maximum
length: 63
config switch-controller acl ingress
Configure ingress ACL policies to be applied on managed FortiSwitch ports.
config switch-controller acl ingress
Description: Configure ingress ACL policies to be applied on managed FortiSwitch ports.
edit <id>
config action
Description: ACL actions.
set count [enable|disable]
FortiOS 8.0.0 CLI Reference
1314
Fortinet Inc.

<!-- 来源页 1315 -->
set drop [enable|disable]
end
config classifier
Description: ACL classifiers.
set dst-ip-prefix {ipv4-classnet}
set dst-mac {mac-address}
set src-ip-prefix {ipv4-classnet}
set src-mac {mac-address}
set vlan {integer}
end
set description {string}
next
end
config switch-controller acl ingress
Parameter
Description
Type
Size
Default
description
Description for the ACL policy.
string
Maximum
length: 63
id
ACL ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config action
Parameter
Description
Type
Size
Default
count
Enable/disable count.
option
-disable
Option
Description
enable
Enable count.
disable
Disable count.
drop
Enable/disable drop.
option
-disable
Option
Description
enable
Enable drop.
disable
Disable drop.
FortiOS 8.0.0 CLI Reference
1315
Fortinet Inc.

<!-- 来源页 1316 -->
config classifier
Parameter
Description
Type
Size
Default
dst-ip-prefix
Destination IP address to be matched.
ipv4-classnet
Not
Specified
0.0.0.0 0.0.0.0
dst-mac
Destination MAC address to be matched.
mac-address
Not
Specified
00:00:00:00:00:00
src-ip-prefix
Source IP address to be matched.
ipv4-classnet
Not
Specified
0.0.0.0 0.0.0.0
src-mac
Source MAC address to be matched.
mac-address
Not
Specified
00:00:00:00:00:00
vlan
VLAN ID to be matched.
integer
Minimum
value: 1
Maximum
value: 4094
0
config switch-controller auto-config custom
Policies which can override the 'default' for specific ISL/ICL/FortiLink interface.
config switch-controller auto-config custom
Description: Policies which can override the 'default' for specific ISL/ICL/FortiLink
interface.
edit <name>
config switch-binding
Description: Switch binding list.
edit <switch-id>
set policy {string}
next
end
next
end
config switch-controller auto-config custom
Parameter
Description
Type
Size
Default
name
Auto-Config FortiLink or ISL/ICL interface name.
string
Maximum
length: 15
FortiOS 8.0.0 CLI Reference
1316
Fortinet Inc.

<!-- 来源页 1317 -->
config switch-binding
Parameter
Description
Type
Size
Default
policy
Custom auto-config policy.
string
Maximum
length: 63
default
switch-id
Switch name.
string
Maximum
length: 35
config switch-controller auto-config default
Policies which are applied automatically to all ISL/ICL/FortiLink interfaces.
config switch-controller auto-config default
Description: Policies which are applied automatically to all ISL/ICL/FortiLink interfaces.
set fgt-policy {string}
set icl-policy {string}
set isl-policy {string}
end
config switch-controller auto-config default
Parameter
Description
Type
Size
Default
fgt-policy
Default FortiLink auto-config policy.
string
Maximum
length: 63
default
icl-policy
Default ICL auto-config policy.
string
Maximum
length: 63
default-icl
isl-policy
Default ISL auto-config policy.
string
Maximum
length: 63
default
config switch-controller auto-config policy
Policy definitions which can define the behavior on auto configured interfaces.
config switch-controller auto-config policy
Description: Policy definitions which can define the behavior on auto configured interfaces.
edit <name>
set igmp-flood-report [enable|disable]
set igmp-flood-traffic [enable|disable]
set poe-status [enable|disable]
set qos-policy {string}
set storm-control-policy {string}
FortiOS 8.0.0 CLI Reference
1317
Fortinet Inc.

<!-- 来源页 1318 -->
next
end
config switch-controller auto-config policy
Parameter
Description
Type
Size
Default
igmp-flood-report
Enable/disable IGMP flood report.
option
-disable
Option
Description
enable
Enable IGMP flood report.
disable
Disable IGMP flood report.
igmp-flood-traffic
Enable/disable IGMP flood traffic.
option
-disable
Option
Description
enable
Enable IGMP flood traffic.
disable
Disable IGMP flood traffic.
name
Auto-config policy name.
string
Maximum
length: 63
poe-status
Enable/disable PoE status.
option
-enable
Option
Description
enable
Enable PoE status.
disable
Disable PoE status.
qos-policy
Auto-Config QoS policy.
string
Maximum
length: 63
default
storm-control-policy
Auto-Config storm control policy.
string
Maximum
length: 63
auto-config
config switch-controller custom-command
Configure the FortiGate switch controller to send custom commands to managed FortiSwitch devices.
config switch-controller custom-command
Description: Configure the FortiGate switch controller to send custom commands to managed
FortiSwitch devices.
edit <command-name>
FortiOS 8.0.0 CLI Reference
1318
Fortinet Inc.

<!-- 来源页 1319 -->
set command {var-string}
set description {string}
next
end
config switch-controller custom-command
Parameter
Description
Type
Size
Default
command
String of commands to send to FortiSwitch devices
(For example (%0a = return key): config switch
trunk %0a edit myTrunk %0a set members port1
port2 %0a end %0a).
var-string
Maximum
length:
4095
command-name
Command name called by the FortiGate switch
controller in the execute command.
string
Maximum
length: 35
description
Description.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
1319
Fortinet Inc.

<!-- 来源页 1320 -->
config switch-controller dsl policy
This command is available for model(s): FortiGate 40F 3G4G, FortiGate 60F, FortiGate 80F Bypass,
FortiGate 80F Gen2, FortiGate 80F-POE, FortiGate 81F Gen2, FortiGate 81F-POE, FortiGateRugged
60F 3G4G, FortiGateRugged 60F Gen2, FortiGateRugged 70F 3G4G, FortiGateRugged 70F, FortiWiFi
81F 2R 3G4G-POE, FortiWiFi 81F 2R-POE.
It is not available for: FortiGate 1000D, FortiGate 1000F, FortiGate 1001F, FortiGate 100F, FortiGate
101F Gen2, FortiGate 1100E, FortiGate 1101E, FortiGate 120G, FortiGate 121G, FortiGate 1800F,
FortiGate 1801F, FortiGate 2000E, FortiGate 200E, FortiGate 200F, FortiGate 200G, FortiGate 201E,
FortiGate 201F, FortiGate 201G, FortiGate 2200E, FortiGate 2201E, FortiGate 2500E, FortiGate
2600F, FortiGate 2601F, FortiGate 3000F, FortiGate 3001F, FortiGate 300E, FortiGate 301E,
FortiGate 30G, FortiGate 31G, FortiGate 3200F, FortiGate 3201F Gen2, FortiGate 3300E, FortiGate
3301E, FortiGate 3400E, FortiGate 3401E, FortiGate 3500F Gen2, FortiGate 3501F Gen2, FortiGate
3600E, FortiGate 3601E, FortiGate 3700F, FortiGate 3701F, FortiGate 3960E, FortiGate 3980E,
FortiGate 400E Bypass, FortiGate 400E, FortiGate 400F, FortiGate 401E, FortiGate 401F, FortiGate
40F, FortiGate 4200F, FortiGate 4201F Gen2, FortiGate 4400F, FortiGate 4401F Gen2, FortiGate
4800F, FortiGate 4801F, FortiGate 500E, FortiGate 501E, FortiGate 50G 5G, FortiGate 50G DSL,
FortiGate 50G SFP-POE, FortiGate 50G SFP, FortiGate 50G, FortiGate 51G 5G, FortiGate 51G SFP-POE, FortiGate 51G, FortiGate 600E, FortiGate 600F, FortiGate 601E, FortiGate 601F, FortiGate 61F,
FortiGate 70F, FortiGate 70G-POE, FortiGate 70G, FortiGate 71F, FortiGate 71G-POE, FortiGate 71G,
FortiGate 800D, FortiGate 80F DSL, FortiGate 900D, FortiGate 900G, FortiGate 901G, FortiGate 90G
Gen2, FortiGate 90G, FortiGate 91G Gen2, FortiGate 91G, FortiGate-VM64 Aliyun, FortiGate-VM64
AWS, FortiGate-VM64 Azure, FortiGate-VM64 GCP, FortiGate-VM64 OPC, FortiGate-VM64,
FortiGateRugged 50G 5G, FortiGateRugged 70G 5G Dual, FortiGateRugged 70G, FortiWiFi 30G,
FortiWiFi 31G, FortiWiFi 40F 3G4G, FortiWiFi 40F, FortiWiFi 50G 5G, FortiWiFi 50G DSL, FortiWiFi 50G
SFP, FortiWiFi 50G, FortiWiFi 51G, FortiWiFi 60F, FortiWiFi 61F, FortiWiFi 70G-POE, FortiWiFi 70G,
FortiWiFi 71G, FortiWiFi 80F 2R 3G4G DSL, FortiWiFi 80F 2R, FortiWiFi 81F 2R 3G4G DSL, FortiWiFi
81F 2R.
DSL policy.
config switch-controller dsl policy
Description: DSL policy.
edit <name>
set append_padding [disable|enable]
set cpe-aele [disable|enable]
set cpe-aele-mode [ELE_M0|ELE_DS|...]
set cs {option1}, {option2}, ...
set ds-bitswap [disable|enable]
set pause-frame [disable|enable]
set profile [auto-30a|auto-17a|...]
set type {option}
set us-bitswap [disable|enable]
next
end
FortiOS 8.0.0 CLI Reference
1320
Fortinet Inc.

<!-- 来源页 1321 -->
config switch-controller dsl policy
Parameter
Description
Type
Size
Default
append_
padding
Device pause frame configuration.
option
-enable
Option
Description
disable
Disable.
enable
Enable.
cpe-aele
CPE AELE.
option
-enable
Option
Description
disable
Disable.
enable
Enable.
cpe-aele-mode
CPE AELE-Mode with given string.
option
-ELE_MIN
Option
Description
ELE_M0
cpe AELE-Mode with given string.
ELE_DS
cpe AELE-Mode with given string.
ELE_PB
cpe AELE-Mode with given string.
ELE_MIN
cpe AELE-Mode with given string.
cs
CPE carrier set.
option
-A43 B43
A43C
Option
Description
A43
CPE carrier set.
B43
CPE carrier set.
A43C
CPE carrier set.
V43
CPE carrier set.
ds-bitswap
Enable/disable bitswap.
option
-enable
Option
Description
disable
Disable.
enable
Enable.
FortiOS 8.0.0 CLI Reference
1321
Fortinet Inc.

<!-- 来源页 1322 -->
Parameter
Description
Type
Size
Default
name
Policy name.
string
Maximum
length: 63
pause-frame
Device pause frame configuration.
option
-enable
Option
Description
disable
Disable.
enable
Enable.
profile
VDSL CPE profile.
option
-auto-30a
Option
Description
auto-30a
vdsl CPE profile.
auto-17a
vdsl CPE profile.
auto-12ab
vdsl CPE profile.
type
Type.
option
-Proscend
Option
Description
Proscend
Proscend.
us-bitswap
Enable/disable bitswap.
option
-enable
Option
Description
disable
Disable.
enable
Enable.
config switch-controller dynamic-port-policy
Configure Dynamic port policy to be applied on the managed FortiSwitch ports through DPP device.
config switch-controller dynamic-port-policy
Description: Configure Dynamic port policy to be applied on the managed FortiSwitch ports
through DPP device.
edit <name>
set description {string}
set fortilink {string}
config policy
Description: Port policies with matching criteria and actions.
edit <name>
set 802-1x {string}
set bounce-port-duration {integer}
set bounce-port-link [disable|enable]
FortiOS 8.0.0 CLI Reference
1322
Fortinet Inc.

<!-- 来源页 1323 -->
set category [device|interface-tag]
set description {string}
set family {string}
set host {string}
set hw-vendor {string}
set interface-tags <tag-name1>, <tag-name2>, ...
set lldp-profile {string}
set mac {string}
set match-period {integer}
set match-remove [default|link-down]
set match-type [dynamic|override]
set poe-reset [disable|enable]
set qos-policy {string}
set status [enable|disable]
set type {string}
set vlan-policy {string}
next
end
next
end
config switch-controller dynamic-port-policy
Parameter
Description
Type
Size
Default
description
Description for the Dynamic port policy.
string
Maximum
length: 63
fortilink
FortiLink interface for which this Dynamic port
policy belongs to.
string
Maximum
length: 15
name
Dynamic port policy name.
string
Maximum
length: 63
config policy
Parameter
Description
Type
Size
Default
802-1x
802.1x security policy to be applied when using
this policy.
string
Maximum
length: 31
bounce-port-duration
Bounce duration in seconds of a switch port where
this policy is applied.
integer
Minimum
value: 1
Maximum
value: 30
5
bounce-port-link
Enable/disable bouncing (administratively bring
the link down, up) of a switch port where this policy
is applied. Helps to clear and reassign VLAN from
lldp-profile.
option
-enable
FortiOS 8.0.0 CLI Reference
1323
Fortinet Inc.

<!-- 来源页 1324 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable bouncing (administratively bring the link down, up) of a switch
port where this policy is applied.
enable
Enable bouncing (administratively bring the link down, up) of a switch
port where this policy is applied.
category
Category of Dynamic port policy.
option
-device
Option
Description
device
Device category.
interface-tag
Interface Tag category.
description
Description for the policy.
string
Maximum
length: 63
family
Match policy based on family.
string
Maximum
length: 31
host
Match policy based on host.
string
Maximum
length: 64
hw-vendor
Match policy based on hardware vendor.
string
Maximum
length: 15
interface-tags <tag-name>
Match policy based on the FortiSwitch interface
object tags.
FortiSwitch port tag name.
string
Maximum
length: 63
lldp-profile
LLDP profile to be applied when using this policy.
string
Maximum
length: 63
mac
Match policy based on MAC address.
string
Maximum
length: 17
match-period
Duration in hours to retain the matched devices (0
- 3072, 0 = always retain).
integer
Minimum
value: 0
Maximum
value: 3072
**
0
match-remove
Options to remove the matched override devices.
option
-default
Option
Description
default
Remove the matched override devices based on the match period.
link-down
Remove the matched override devices based on switch port link down
event.
FortiOS 8.0.0 CLI Reference
1324
Fortinet Inc.

<!-- 来源页 1325 -->
Parameter
Description
Type
Size
Default
match-type
Match and retain the devices based on the type.
option
-dynamic
Option
Description
dynamic
Matched devices will be removed on dynamic events like link-down,device-inactivity,switch-offline.
override
Matched devices will be retained until the match-period.
name
Policy name.
string
Maximum
length: 63
poe-reset
Enable/disable POE reset of a switch port where
this policy is applied.
option
-disable
Option
Description
disable
Disable POE reset of a switch port where this policy is applied.
enable
Enable POE reset of a switch port where this policy is applied.
qos-policy
QoS policy to be applied when using this policy.
string
Maximum
length: 63
status
Enable/disable policy.
option
-enable
Option
Description
enable
Enable policy.
disable
Disable policy.
type
Match policy based on type.
string
Maximum
length: 15
vlan-policy
VLAN policy to be applied when using this policy.
string
Maximum
length: 63
** Values may differ between models.
config switch-controller flow-tracking
Configure FortiSwitch flow tracking and export via ipfix/netflow.
config switch-controller flow-tracking
Description: Configure FortiSwitch flow tracking and export via ipfix/netflow.
config aggregates
Description: Configure aggregates in which all traffic sessions matching the IP Address
will be grouped into the same flow.
edit <id>
set ip {ipv4-classnet}
FortiOS 8.0.0 CLI Reference
1325
Fortinet Inc.

<!-- 来源页 1326 -->
next
end
config collectors
Description: Configure collectors for the flow.
edit <name>
set ip {ipv4-address-any}
set port {integer}
set transport [udp|tcp|...]
next
end
set format [netflow1|netflow5|...]
set level [vlan|ip|...]
set max-export-pkt-size {integer}
set sample-mode [local|perimeter|...]
set sample-rate {integer}
set template-export-period {integer}
set timeout-general {integer}
set timeout-icmp {integer}
set timeout-max {integer}
set timeout-tcp {integer}
set timeout-tcp-fin {integer}
set timeout-tcp-rst {integer}
set timeout-udp {integer}
end
config switch-controller flow-tracking
Parameter
Description
Type
Size
Default
format
Configure flow tracking protocol.
option
-netflow9
Option
Description
netflow1
Netflow version 1 sampling.
netflow5
Netflow version 5 sampling.
netflow9
Netflow version 9 sampling.
ipfix
Ipfix sampling.
level
Configure flow tracking level.
option
-ip
Option
Description
vlan
Collects srcip/dstip/srcport/dstport/protocol/tos/vlan from the sample
packet.
ip
Collects srcip/dstip from the sample packet.
port
Collects srcip/dstip/srcport/dstport/protocol from the sample packet.
FortiOS 8.0.0 CLI Reference
1326
Fortinet Inc.

<!-- 来源页 1327 -->
Parameter
Description
Type
Size
Default
Option
Description
proto
Collects srcip/dstip/protocol from the sample packet.
mac
Collects smac/dmac from the sample packet.
max-export-pkt-size
Configure flow max export packet
size (512-9216, default=512 bytes).
integer
Minimum value:
512 Maximum
value: 9216
512
sample-mode
Configure sample mode for the flow
tracking.
option
-perimeter
Option
Description
local
Set local mode which samples on the specific switch port.
perimeter
Set perimeter mode which samples on all switch fabric ports and
fortilink port at the ingress.
device-ingress
Set device -ingress mode which samples across all switch ports at the
ingress.
sample-rate
Configure sample rate for the
perimeter and device-ingress
sampling(0 - 99999).
integer
Minimum value:
0 Maximum
value: 99999
512
template-export-period
Configure template export period (1-60, default=5 minutes).
integer
Minimum value:
1 Maximum
value: 60
5
timeout-general
Configure flow session general
timeout (60-604800, default=3600
seconds).
integer
Minimum value:
60 Maximum
value: 604800
3600
timeout-icmp
Configure flow session ICMP timeout
(60-604800, default=300 seconds).
integer
Minimum value:
60 Maximum
value: 604800
300
timeout-max
Configure flow session max timeout
(60-604800, default=604800
seconds).
integer
Minimum value:
60 Maximum
value: 604800
604800
timeout-tcp
Configure flow session TCP timeout
(60-604800, default=3600 seconds).
integer
Minimum value:
60 Maximum
value: 604800
3600
timeout-tcp-fin
Configure flow session TCP FIN
timeout (60-604800, default=300
seconds).
integer
Minimum value:
60 Maximum
value: 604800
300
FortiOS 8.0.0 CLI Reference
1327
Fortinet Inc.

<!-- 来源页 1328 -->
Parameter
Description
Type
Size
Default
timeout-tcp-rst
Configure flow session TCP RST
timeout (60-604800, default=120
seconds).
integer
Minimum value:
60 Maximum
value: 604800
120
timeout-udp
Configure flow session UDP timeout
(60-604800, default=300 seconds).
integer
Minimum value:
60 Maximum
value: 604800
300
config aggregates
Parameter
Description
Type
Size
Default
id
Aggregate id.
integer
Minimum value:
0 Maximum
value:
4294967295
0
ip
IP address to group all matching traffic sessions
to a flow.
ipv4-classnet
Not Specified
0.0.0.0
0.0.0.0
config collectors
Parameter
Description
Type
Size
Default
ip
Collector IP address.
ipv4-address-any
Not
Specified
0.0.0.0
name
Collector name.
string
Maximum
length: 63
port
Collector port number(0-65535, default:0,
netflow:2055, ipfix:4739).
integer
Minimum
value: 0
Maximum
value:
65535
0
transport
Collector L4 transport protocol for exporting
packets.
option
-udp
Option
Description
udp
UDP protocol.
tcp
TCP protocol.
sctp
SCTP protocol.
FortiOS 8.0.0 CLI Reference
1328
Fortinet Inc.

<!-- 来源页 1329 -->
config switch-controller fortilink-settings
Configure integrated FortiLink settings for FortiSwitch.
config switch-controller fortilink-settings
Description: Configure integrated FortiLink settings for FortiSwitch.
edit <name>
set access-vlan-mode [legacy|fail-open|...]
set admin-policy {string}
set fortilink {string}
set inactive-timer {integer}
set link-down-flush [disable|enable]
config nac-ports
Description: NAC specific configuration.
set lan-segment [enabled|disabled]
set member-change {integer}
set nac-lan-interface {string}
set nac-segment-vlans <vlan-name1>, <vlan-name2>, ...
set onboarding-vlan {string}
set parent-key {string}
end
next
end
config switch-controller fortilink-settings
Parameter
Description
Type
Size
Default
access-vlan-mode
Intra VLAN traffic behavior with loss of connection
to the FortiGate.
option
-legacy
Option
Description
legacy
Backward compatible behavior.
fail-open
When connection to FortiGate is lost, traffic on the VLAN may continue
directly between end points.
fail-close
When connection to FortiGate is lost, traffic between endpoints on the
VLAN is blocked.
admin-policy
*
FortiSwitch's admin security-policy applied to all
switch on this Fortilink interface.
string
Maximum
length: 31
fortilink
FortiLink interface to which this fortilink-setting
belongs.
string
Maximum
length: 15
FortiOS 8.0.0 CLI Reference
1329
Fortinet Inc.

<!-- 来源页 1330 -->
Parameter
Description
Type
Size
Default
inactive-timer
Time interval(minutes) to be included in the
inactive devices expiry calculation (mac age-out +
inactive-time + periodic scan interval).
integer
Minimum
value: 1
Maximum
value: 1440
15
link-down-flush
Clear NAC and dynamic devices on switch ports on
link down event.
option
-enable
Option
Description
disable
Disable clearing NAC and dynamic devices on a switch port when link
down event happens.
enable
Enable clearing NAC and dynamic devices on a switch port when link
down event happens.
name
FortiLink settings name.
string
Maximum
length: 35
* This parameter may not exist in some models.
config nac-ports
Parameter
Description
Type
Size
Default
lan-segment
Enable/disable LAN segment feature on the
FortiLink interface.
option
-disabled
Option
Description
enabled
Enable lan-segment on this interface.
disabled
Disable lan-segment on this interface.
member-change
Member change flag. Read-only.
integer
Minimum
value: 0
Maximum
value: 255
0
nac-lan-interface
Configure NAC LAN interface.
string
Maximum
length: 15
nac-segment-vlans <vlan-name>
Configure NAC segment VLANs.
VLAN interface name.
string
Maximum
length: 79
onboarding-vlan
Default NAC Onboarding VLAN when NAC devices
are discovered.
string
Maximum
length: 15
parent-key
Parent key name. Read-only.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
1330
Fortinet Inc.

<!-- 来源页 1331 -->
config switch-controller global
Configure FortiSwitch global settings.
config switch-controller global
Description: Configure FortiSwitch global settings.
set bounce-quarantined-link [disable|enable]
config custom-command
Description: List of custom commands to be pushed to all FortiSwitches in the VDOM.
edit <command-entry>
set command-name {string}
next
end
set default-virtual-switch-vlan {string}
set dhcp-option82-circuit-id {option1}, {option2}, ...
set dhcp-option82-format [ascii|legacy]
set dhcp-option82-remote-id {option1}, {option2}, ...
set dhcp-server-access-list [enable|disable]
set dhcp-snoop-client-db-exp {integer}
set dhcp-snoop-client-req [drop-untrusted|forward-untrusted]
set dhcp-snoop-db-per-port-learn-limit {integer}
set disable-discovery <name1>, <name2>, ...
set fips-enforce [disable|enable]
set firewall-auth-user-hold-period {integer}
set firmware-provision-on-authorization [enable|disable]
set https-image-push [enable|disable]
set log-mac-limit-violations [enable|disable]
set mac-aging-interval {integer}
set mac-event-logging [enable|disable]
set mac-retention-period {integer}
set mac-violation-timer {integer}
set quarantine-mode [by-vlan|by-redirect]
set sn-dns-resolution [enable|disable]
set switch-custom-cmd [on-replay|on-any]
set switch-on-deauth [no-op|factory-reset]
set update-user-device {option1}, {option2}, ...
set vlan-all-mode [all|defined]
set vlan-identity [description|name]
set vlan-optimization [prune|configured|...]
end
FortiOS 8.0.0 CLI Reference
1331
Fortinet Inc.

<!-- 来源页 1332 -->
config switch-controller global
Parameter
Description
Type
Size
Default
bounce-quarantined-link
Enable/disable bouncing
(administratively bring the link down,
up) of a switch port where a
quarantined device was seen last.
Helps to re-initiate the DHCP
process for a device.
option
-disable
Option
Description
disable
Disable bouncing (administratively bring the link down, up) of a switch
port where a quarantined device was seen last.
enable
Enable bouncing (administratively bring the link down, up) of a switch
port where a quarantined device was seen last.
default-virtual-switch-vlan
Default VLAN for ports when added
to the virtual-switch.
string
Maximum
length: 15
dhcp-option82-circuit-id
List the parameters to be included to
inform about client identification.
option
-intfname vlan
mode
Option
Description
intfname
Interface name.
vlan
VLAN name.
hostname
Hostname.
mode
Mode.
description
Description.
dhcp-option82-format
DHCP option-82 format string.
option
-ascii
Option
Description
ascii
Allow user to choose values for circuit-id and remote-id. Format: cid=
[hostname,interface,mode,vlan,description] rid=
[hostname,xx:xx:xx:xx:xx:xx,ip]
legacy
Generate predefine fixed format for circuit-id and remote. Format:
cid=hostname-[<vlan:16><mod:8><port:8>].32bit, rid= [mac
(0.6)].48bit
FortiOS 8.0.0 CLI Reference
1332
Fortinet Inc.

<!-- 来源页 1333 -->
Parameter
Description
Type
Size
Default
dhcp-option82-remote-id
List the parameters to be included to
inform about client identification.
option
-mac
Option
Description
mac
MAC address.
hostname
Hostname.
ip
IP address.
dhcp-server-access-list
Enable/disable DHCP snooping
server access list.
option
-disable
Option
Description
enable
Enable DHCP server access list.
disable
Disable DHCP server access list.
dhcp-snoop-client-db-exp
Expiry time for DHCP snooping
server database entries (300 -259200 sec, default = 86400 sec).
integer
Minimum value:
300 Maximum
value: 259200
86400
dhcp-snoop-client-req
Client DHCP packet broadcast
mode.
option
-drop-untrusted
Option
Description
drop-untrusted
Broadcast packets on trusted ports in the VLAN.
forward-untrusted
Broadcast packets on all ports in the VLAN.
dhcp-snoop-db-per-port-learn-limit
Per Interface dhcp-server entries
learn limit (0 - 1024, default = 64).
integer
Minimum value:
0 Maximum
value: 2048
64
disable-discovery
<name>
Prevent this FortiSwitch from
discovering.
FortiSwitch Serial-number.
string
Maximum
length: 79
fips-enforce
Enable/disable enforcement of FIPS
on managed FortiSwitch devices.
option
-enable
Option
Description
disable
Disable enforcement of FIPS on managed FortiSwitch devices.
enable
Enable enforcement of FIPS on managed FortiSwitch devices.
FortiOS 8.0.0 CLI Reference
1333
Fortinet Inc.

<!-- 来源页 1334 -->
Parameter
Description
Type
Size
Default
firewall-auth-user-hold-period
Time period in minutes to hold
firewall authenticated MAC users (5
- 1440, default = 5, disable = 0).
integer
Minimum value:
5 Maximum
value: 1440
5
firmware-provision-on-authorization
Enable/disable automatic
provisioning of latest firmware on
authorization.
option
-disable
Option
Description
enable
Enable firmware provision on authorization.
disable
Disable firmware provision on authorization.
https-image-push
Enable/disable image push to
FortiSwitch using HTTPS.
option
-enable
Option
Description
enable
Enable image push to FortiSwitch using HTTPS.
disable
Disable image push to FortiSwitch using HTTPS.
log-mac-limit-violations
Enable/disable logs for Learning
Limit Violations.
option
-disable
Option
Description
enable
Enable Learn Limit Violation.
disable
Disable Learn Limit Violation.
mac-aging-interval
Time after which an inactive MAC is
aged out (10 - 1000000 sec, default
= 300, 0 = disable).
integer
Minimum value:
10 Maximum
value: 1000000
300
mac-event-logging
Enable/disable MAC address event
logging.
option
-disable
Option
Description
enable
Enable MAC address event logging.
disable
Disable MAC address event logging.
mac-retention-period
Time in hours after which an inactive
MAC is removed from client DB (0 =
aged out based on mac-aging-interval).
integer
Minimum value:
0 Maximum
value: 168
24
FortiOS 8.0.0 CLI Reference
1334
Fortinet Inc.

<!-- 来源页 1335 -->
Parameter
Description
Type
Size
Default
mac-violation-timer
Set timeout for Learning Limit
Violations (0 = disabled).
integer
Minimum value:
0 Maximum
value:
4294967295
0
quarantine-mode
Quarantine mode.
option
-by-vlan
Option
Description
by-vlan
Quarantined device traffic is sent to FortiGate on a separate
quarantine VLAN.
by-redirect
Quarantined device traffic is redirected only to the FortiGate on the
received VLAN.
sn-dns-resolution
Enable/disable DNS resolution of the
FortiSwitch unit's IP address with
switch name.
option
-enable
Option
Description
enable
Enable DNS resolution of the FortiSwitch unit's IP address with switch
name.
disable
Disable DNS resolution of the FortiSwitch unit's IP address with switch
name.
switch-custom-cmd *
Configure push method for switch
bound custom command.
option
-on-replay
Option
Description
on-replay
Push switch bound custom command only when full config is replayed.
on-any
Push switch bound custom command whenever any config on FSW is
updated.
switch-on-deauth
No-operation/Factory-reset the
managed FortiSwitch on
deauthorization.
option
-no-op
Option
Description
no-op
No-operation on the managed FortiSwitch on deauthorization.
factory-reset
Factory-reset the managed FortiSwitch on deauthorization.
update-user-device
Control which sources update the
device user list.
option
-mac-cache lldp
dhcp-snooping
l2-db l3-db
FortiOS 8.0.0 CLI Reference
1335
Fortinet Inc.

<!-- 来源页 1336 -->
Parameter
Description
Type
Size
Default
Option
Description
mac-cache
Update MAC address from switch-controller mac-cache.
lldp
Update from FortiSwitch LLDP neighbor database.
dhcp-snooping
Update from FortiSwitch DHCP snooping client and server databases.
l2-db
Update from FortiSwitch Network-monitor Layer 2 tracking database.
l3-db
Update from FortiSwitch Network-monitor Layer 3 tracking database.
vlan-all-mode
VLAN configuration mode, user-defined-vlans or all-possible-vlans.
option
-defined
Option
Description
all
Include all possible VLANs (1-4093).
defined
Include user defined VLANs.
vlan-identity
Identity of the VLAN. Commonly
used for RADIUS Tunnel-Private-Group-Id.
option
-name
Option
Description
description
Configure the VLAN description to that of the FortiOS interface
description if available; otherwise use the interface name.
name
Configure the VLAN description to that of the FortiOS interface name.
vlan-optimization
FortiLink VLAN optimization.
option
-configured
Option
Description
prune
Enable VLAN optimization (only VLANs necessary on or along path
between destinations) on FortiSwitch units for auto-generated trunks.
configured
Enable VLAN optimization (only VLANs created on Fortilink interface)
on FortiSwitch units for auto-generated trunks.
none
Disable VLAN optimization on FortiSwitch units for auto-generated
trunks.
* This parameter may not exist in some models.
FortiOS 8.0.0 CLI Reference
1336
Fortinet Inc.

<!-- 来源页 1337 -->
config custom-command
Parameter
Description
Type
Size
Default
command-entry
List of FortiSwitch commands.
string
Maximum
length: 35
command-name
Name of custom command to push to all
FortiSwitches in VDOM.
string
Maximum
length: 35
config switch-controller igmp-snooping
Configure FortiSwitch IGMP snooping global settings.
config switch-controller igmp-snooping
Description: Configure FortiSwitch IGMP snooping global settings.
set aging-time {integer}
set flood-unknown-multicast [enable|disable]
set query-interval {integer}
end
config switch-controller igmp-snooping
Parameter
Description
Type
Size
Default
aging-time
Maximum number of seconds to retain a multicast
snooping entry for which no packets have been
seen (15 - 3600 sec, default = 300).
integer
Minimum
value: 15
Maximum
value: 3600
300
flood-unknown-multicast
Enable/disable unknown multicast flooding.
option
-disable
Option
Description
enable
Enable unknown multicast flooding.
disable
Disable unknown multicast flooding.
query-interval
Maximum time after which IGMP query will be sent
(10 - 1200 sec, default = 125).
integer
Minimum
value: 10
Maximum
value: 1200
125
FortiOS 8.0.0 CLI Reference
1337
Fortinet Inc.

<!-- 来源页 1338 -->
config switch-controller igmp-snooping-static-group
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
Configure FortiSwitch IGMP snooping static group settings.
config switch-controller igmp-snooping-static-group
Description: Configure FortiSwitch IGMP snooping static group settings.
edit <name>
set description {string}
set ignore-reports [disable|enable]
set mcast-addr {ipv4-address-multicast}
config ports
Description: Configure static group in switches.
edit <id>
set ports <igmp-port-name1>, <igmp-port-name2>, ...
set switch-id {string}
next
end
set vlan {string}
next
end
FortiOS 8.0.0 CLI Reference
1338
Fortinet Inc.

<!-- 来源页 1339 -->
config switch-controller igmp-snooping-static-group
Parameter
Description
Type
Size
Default
description
IGMP snooping static group description.
string
Maximum
length: 35
ignore-reports
Enable/disable this ignore-reports.
option
-disable
Option
Description
disable
Disable to ignore all IGMP membership reports received for this group.
enable
Enable to ignore all IGMP membership reports received for this group.
mcast-addr
IGMP snooping static group multicast IP.
ipv4-address-multicast
Not
Specified
0.0.0.0
name
IGMP snooping static group name.
string
Maximum
length: 35
vlan
VLAN name.
string
Maximum
length: 15
config ports
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
ports <igmp-port-name>
Port members.
Interface name from available options.
string
Maximum
length: 79
switch-id
Switch ID.
string
Maximum
length: 35
config switch-controller initial-config template
Configure template for auto-generated VLANs.
config switch-controller initial-config template
Description: Configure template for auto-generated VLANs.
edit <name>
set allowaccess {option1}, {option2}, ...
set auto-ip [enable|disable]
FortiOS 8.0.0 CLI Reference
1339
Fortinet Inc.

<!-- 来源页 1340 -->
set dhcp-server [enable|disable]
set ip {ipv4-classnet-host}
set vlanid {integer}
next
end
config switch-controller initial-config template
Parameter
Description
Type
Size
Default
allowaccess
Permitted types of management access to this
interface.
option
-Option
Description
ping
PING access.
https
HTTPS access.
ssh
SSH access.
snmp
SNMP access.
http
HTTP access.
telnet
TELNET access.
fgfm
FortiManager access.
radius-acct
RADIUS accounting access.
probe-response
Probe access.
fabric
Security Fabric access.
ftm
FTM access.
dnp
DNP access.
auto-ip
Automatically allocate interface address and
subnet block.
option
-enable
Option
Description
enable
Enable auto-ip status.
disable
Disable auto-ip status.
dhcp-server
Enable/disable a DHCP server on this interface.
option
-disable
Option
Description
enable
Enable DHCP server.
disable
Disable DHCP server.
FortiOS 8.0.0 CLI Reference
1340
Fortinet Inc.

<!-- 来源页 1341 -->
Parameter
Description
Type
Size
Default
ip
Interface IPv4 address and subnet mask.
ipv4-classnet-host
Not
Specified
0.0.0.0
0.0.0.0
name
Initial config template name.
string
Maximum
length: 63
vlanid
Unique VLAN ID.
integer
Minimum
value: 1
Maximum
value: 4094
0
config switch-controller initial-config vlans
Configure initial template for auto-generated VLAN interfaces.
config switch-controller initial-config vlans
Description: Configure initial template for auto-generated VLAN interfaces.
set default-vlan {string}
set nac {string}
set nac-segment {string}
set optional-vlans [enable|disable]
set quarantine {string}
set rspan {string}
set video {string}
set voice {string}
end
config switch-controller initial-config vlans
Parameter
Description
Type
Size
Default
default-vlan
Default VLAN (native) assigned to all switch ports
upon discovery.
string
Maximum
length: 63
_default
nac
VLAN for NAC onboarding devices.
string
Maximum
length: 63
onboarding
nac-segment
VLAN for NAC segment primary interface.
string
Maximum
length: 63
nac_segment
optional-vlans
Auto-generate pre-configured VLANs upon
switch discovery.
option
-enable
FortiOS 8.0.0 CLI Reference
1341
Fortinet Inc.

<!-- 来源页 1342 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable auto-generated VLANs.
disable
Disable auto-generated VLANs.
quarantine
VLAN for quarantined traffic.
string
Maximum
length: 63
quarantine
rspan
VLAN for RSPAN/ERSPAN mirrored traffic.
string
Maximum
length: 63
rspan
video
VLAN dedicated for video devices.
string
Maximum
length: 63
video
voice
VLAN dedicated for voice devices.
string
Maximum
length: 63
voice
config switch-controller ip-source-guard-log
Configure FortiSwitch ip source guard log.
config switch-controller ip-source-guard-log
Description: Configure FortiSwitch ip source guard log.
set log-violations [enable|disable]
set violation-timer {integer}
end
config switch-controller ip-source-guard-log
Parameter
Description
Type
Size
Default
log-violations
Enable/Disable log violations for IP source guard
logging.
option
-disable
Option
Description
enable
Enable log violations for IP source guard logging.
disable
Disable log violations for IP source guard logging.
violation-timer
IP source gurad log violation timer in seconds (0 -1500, default = 0).
integer
Minimum
value: 0
Maximum
value: 1500
0
FortiOS 8.0.0 CLI Reference
1342
Fortinet Inc.

<!-- 来源页 1343 -->
config switch-controller lldp-profile
Configure FortiSwitch LLDP profiles.
config switch-controller lldp-profile
Description: Configure FortiSwitch LLDP profiles.
edit <name>
set 802 1-tlvs {option1}, {option2}, ...
set 802 3-tlvs {option1}, {option2}, ...
set auto-isl [disable|enable]
set auto-isl-auth [legacy|strict|...]
set auto-isl-auth-encrypt [none|mixed|...]
set auto-isl-auth-identity {string}
set auto-isl-auth-macsec-profile {string}
set auto-isl-auth-reauth {integer}
set auto-isl-auth-user {string}
set auto-isl-hello-timer {integer}
set auto-isl-port-group {integer}
set auto-isl-receive-timeout {integer}
set auto-mclag-icl [disable|enable]
config custom-tlvs
Description: Configuration method to edit custom TLV entries.
edit <name>
set information-string {user}
set oui {user}
set subtype {integer}
next
end
config med-location-service
Description: Configuration method to edit Media Endpoint Discovery (MED) location
service type-length-value (TLV) categories.
edit <name>
set status [disable|enable]
set sys-location-id {string}
next
end
config med-network-policy
Description: Configuration method to edit Media Endpoint Discovery (MED) network
policy type-length-value (TLV) categories.
edit <name>
set assign-vlan [disable|enable]
set dscp {integer}
set priority {integer}
set status [disable|enable]
set vlan-intf {string}
next
end
set med-tlvs {option1}, {option2}, ...
next
end
FortiOS 8.0.0 CLI Reference
1343
Fortinet Inc.

<!-- 来源页 1344 -->
config switch-controller lldp-profile
Parameter
Description
Type
Size
Default
802 1-tlvs
Transmitted IEEE 802.1 TLVs.
option
-Option
Description
port-vlan-id
Port native VLAN TLV.
802 3-tlvs
Transmitted IEEE 802.3 TLVs.
option
-Option
Description
max-frame-size
Maximum frame size TLV.
power-negotiation
PoE+ classification TLV.
eee-negotiation
Energy Efficient Ethernet TLV.
auto-isl
Enable/disable auto inter-switch LAG.
option
-enable
Option
Description
disable
Disable automatic MCLAG inter chassis link.
enable
Enable automatic MCLAG inter chassis link.
auto-isl-auth
Auto inter-switch LAG authentication mode.
option
-legacy
Option
Description
legacy
No auto inter-switch-LAG authentication.
strict
Strict auto inter-switch-LAG authentication.
relax
Relax auto inter-switch-LAG authentication.
auto-isl-auth-encrypt
Auto inter-switch LAG encryption mode.
option
-none
Option
Description
none
No auto inter-switch-LAG encryption.
mixed
Mixed auto inter-switch-LAG encryption.
must
Must auto inter-switch-LAG encryption.
auto-isl-auth-identity
Auto inter-switch LAG authentication identity.
string
Maximum
length: 63
FortiOS 8.0.0 CLI Reference
1344
Fortinet Inc.

<!-- 来源页 1345 -->
Parameter
Description
Type
Size
Default
auto-isl-auth-macsec-profile
Auto inter-switch LAG macsec profile for
encryption.
string
Maximum
length: 63
auto-isl-auth-reauth
Auto inter-switch LAG authentication reauth period
in seconds(10 - 3600, default = 3600).
integer
Minimum
value: 180
Maximum
value: 3600
3600
auto-isl-auth-user
Auto inter-switch LAG authentication user
certificate.
string
Maximum
length: 63
auto-isl-hello-timer
Auto inter-switch LAG hello timer duration (1 - 30
sec, default = 3).
integer
Minimum
value: 1
Maximum
value: 30
3
auto-isl-port-group
Auto inter-switch LAG port group ID (0 - 9).
integer
Minimum
value: 0
Maximum
value: 9
0
auto-isl-receive-timeout
Auto inter-switch LAG timeout if no response is
received (3 - 90 sec, default = 9).
integer
Minimum
value: 0
Maximum
value: 90
60
auto-mclag-icl
Enable/disable MCLAG inter chassis link.
option
-disable
Option
Description
disable
Disable auto inter-switch-LAG.
enable
Enable auto inter-switch-LAG.
med-tlvs
Transmitted LLDP-MED TLVs (type-length-value
descriptions).
option
-Option
Description
inventory-management
Inventory management TLVs.
network-policy
Network policy TLVs.
power-management
Power manangement TLVs.
location-identification
Location identificaion TLVs.
FortiOS 8.0.0 CLI Reference
1345
Fortinet Inc.

<!-- 来源页 1346 -->
Parameter
Description
Type
Size
Default
name
Profile name.
string
Maximum
length: 63
config custom-tlvs
Parameter
Description
Type
Size
Default
information-string
Organizationally defined information string (0 -507 hexadecimal bytes).
user
Not
Specified
name
TLV name (not sent).
string
Maximum
length: 63
oui
Organizationally unique identifier (OUI), a 3-byte
hexadecimal number, for this TLV.
user
Not
Specified
000000
subtype
Organizationally defined subtype (0 - 255).
integer
Minimum
value: 0
Maximum
value: 255
0
config med-location-service
Parameter
Description
Type
Size
Default
name
Location service type name.
string
Maximum
length: 63
status
Enable or disable this TLV.
option
-disable
Option
Description
disable
Do not transmit this location service TLV.
enable
Transmit this location service TLV.
sys-location-id
Location service ID.
string
Maximum
length: 63
config med-network-policy
Parameter
Description
Type
Size
Default
assign-vlan
Enable/disable VLAN assignment when this profile
is applied on managed FortiSwitch port.
option
-disable
FortiOS 8.0.0 CLI Reference
1346
Fortinet Inc.

<!-- 来源页 1347 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable VLAN assignment when this profile is applied on port.
enable
Enable VLAN assignment when this profile is applied on port.
dscp
Advertised Differentiated Services Code Point
(DSCP) value, a packet header value indicating the
level of service requested for traffic, such as high
priority or best effort delivery.
integer
Minimum
value: 0
Maximum
value: 63
0
name
Policy type name.
string
Maximum
length: 63
priority
Advertised Layer 2 priority (0 - 7; from lowest to
highest priority).
integer
Minimum
value: 0
Maximum
value: 7
0
status
Enable or disable this TLV.
option
-disable
Option
Description
disable
Do not transmit this network policy TLV.
enable
Transmit this TLV if a VLAN has been addded to the port.
vlan-intf
VLAN interface to advertise; if configured on port.
string
Maximum
length: 15
config switch-controller lldp-settings
Configure FortiSwitch LLDP settings.
config switch-controller lldp-settings
Description: Configure FortiSwitch LLDP settings.
set device-detection [disable|enable]
set fast-start-interval {integer}
set management-interface [internal|mgmt]
set tx-hold {integer}
set tx-interval {integer}
end
FortiOS 8.0.0 CLI Reference
1347
Fortinet Inc.

<!-- 来源页 1348 -->
config switch-controller lldp-settings
Parameter
Description
Type
Size
Default
device-detection
Enable/disable dynamic detection of LLDP
neighbor devices for VLAN assignment.
option
-enable
Option
Description
disable
Disable dynamic detection of LLDP neighbor devices.
enable
Enable dynamic detection of LLDP neighbor devices.
fast-start-interval
Frequency of LLDP PDU transmission from
FortiSwitch for the first 4 packets when the link
is up (2 - 5 sec, default = 2, 0 = disable fast
start).
integer
Minimum
value: 0
Maximum
value: 255
2
management-interface
Primary management interface to be advertised
in LLDP and CDP PDUs.
option
-internal
Option
Description
internal
Use internal interface.
mgmt
Use management interface.
tx-hold
Number of tx-intervals before local LLDP data
expires (1 - 16, default = 4). Packet TTL is tx-hold * tx-interval.
integer
Minimum
value: 1
Maximum
value: 16
4
tx-interval
Frequency of LLDP PDU transmission from
FortiSwitch (5 - 4095 sec, default = 30). Packet
TTL is tx-hold * tx-interval.
integer
Minimum
value: 5
Maximum
value: 4095
30
config switch-controller location
Configure FortiSwitch location services.
config switch-controller location
Description: Configure FortiSwitch location services.
edit <name>
config address-civic
Description: Configure location civic address.
set additional {string}
set additional-code {string}
set block {string}
set branch-road {string}
set building {string}
FortiOS 8.0.0 CLI Reference
1348
Fortinet Inc.

<!-- 来源页 1349 -->
set city {string}
set city-division {string}
set country {string}
set country-subdivision {string}
set county {string}
set direction {string}
set floor {string}
set landmark {string}
set language {string}
set name {string}
set number {string}
set number-suffix {string}
set parent-key {string}
set place-type {string}
set post-office-box {string}
set postal-community {string}
set primary-road {string}
set road-section {string}
set room {string}
set script {string}
set seat {string}
set street {string}
set street-name-post-mod {string}
set street-name-pre-mod {string}
set street-suffix {string}
set sub-branch-road {string}
set trailing-str-suffix {string}
set unit {string}
set zip {string}
end
config coordinates
Description: Configure location GPS coordinates.
set altitude {string}
set altitude-unit [m|f]
set datum [WGS84|NAD83|...]
set latitude {string}
set longitude {string}
set parent-key {string}
end
config elin-number
Description: Configure location ELIN number.
set elin-num {string}
set parent-key {string}
end
next
end
FortiOS 8.0.0 CLI Reference
1349
Fortinet Inc.

<!-- 来源页 1350 -->
config switch-controller location
Parameter
Description
Type
Size
Default
name
Unique location item name.
string
Maximum
length: 63
config address-civic
Parameter
Description
Type
Size
Default
additional
Location additional details.
string
Maximum
length: 47
additional-code
Location additional code details.
string
Maximum
length: 47
block
Location block details.
string
Maximum
length: 47
branch-road
Location branch road details.
string
Maximum
length: 47
building
Location building details.
string
Maximum
length: 47
city
Location city details.
string
Maximum
length: 47
city-division
Location city division details.
string
Maximum
length: 47
country
The two-letter ISO 3166 country code in capital
ASCII letters eg. US, CA, DK, DE.
string
Maximum
length: 47
country-subdivision
National subdivisions (state, canton, region,
province, or prefecture).
string
Maximum
length: 47
county
County, parish, gun (JP), or district (IN).
string
Maximum
length: 47
direction
Leading street direction.
string
Maximum
length: 47
floor
Floor.
string
Maximum
length: 47
landmark
Landmark or vanity address.
string
Maximum
length: 47
language
Language.
string
Maximum
length: 47
FortiOS 8.0.0 CLI Reference
1350
Fortinet Inc.

<!-- 来源页 1351 -->
Parameter
Description
Type
Size
Default
name
Name (residence and office occupant).
string
Maximum
length: 47
number
House number.
string
Maximum
length: 47
number-suffix
House number suffix.
string
Maximum
length: 47
parent-key
Parent key name. Read-only.
string
Maximum
length: 63
place-type
Place type.
string
Maximum
length: 47
post-office-box
Post office box.
string
Maximum
length: 47
postal-community
Postal community name.
string
Maximum
length: 47
primary-road
Primary road name.
string
Maximum
length: 47
road-section
Road section.
string
Maximum
length: 47
room
Room number.
string
Maximum
length: 47
script
Script used to present the address information.
string
Maximum
length: 47
seat
Seat number.
string
Maximum
length: 47
street
Street.
string
Maximum
length: 47
street-name-post-mod
Street name post modifier.
string
Maximum
length: 47
street-name-pre-mod
Street name pre modifier.
string
Maximum
length: 47
street-suffix
Street suffix.
string
Maximum
length: 47
sub-branch-road
Sub branch road name.
string
Maximum
length: 47
trailing-str-suffix
Trailing street suffix.
string
Maximum
length: 47
FortiOS 8.0.0 CLI Reference
1351
Fortinet Inc.

<!-- 来源页 1352 -->
Parameter
Description
Type
Size
Default
unit
Unit (apartment, suite).
string
Maximum
length: 47
zip
Postal/zip code.
string
Maximum
length: 47
config coordinates
Parameter
Description
Type
Size
Default
altitude
Plus or minus floating point number. For example,
117.47.
string
Maximum
length: 15
altitude-unit
Configure the unit for which the altitude is to (m =
meters, f = floors of a building).
option
-m
Option
Description
m
set altitude unit meters
f
set altitude unit floors
datum
WGS84, NAD83, NAD83/MLLW.
option
-WGS84
Option
Description
WGS84
set coordinates datum WGS84
NAD83
set coordinates datum NAD83
NAD83/MLLW
set coordinates datum NAD83/MLLW
latitude
Floating point starting with +/- or ending with (N or
S). For example, +/-16.67 or 16.67N.
string
Maximum
length: 15
longitude
Floating point starting with +/- or ending with (N or
S). For example, +/-26.789 or 26.789E.
string
Maximum
length: 15
parent-key
Parent key name. Read-only.
string
Maximum
length: 63
config elin-number
Parameter
Description
Type
Size
Default
elin-num
Configure ELIN callback number.
string
Maximum
length: 31
parent-key
Parent key name. Read-only.
string
Maximum
length: 63
FortiOS 8.0.0 CLI Reference
1352
Fortinet Inc.

<!-- 来源页 1353 -->
config switch-controller mac-policy
Configure MAC policy to be applied on the managed FortiSwitch devices through NAC device.
config switch-controller mac-policy
Description: Configure MAC policy to be applied on the managed FortiSwitch devices through NAC
device.
edit <name>
set bounce-port-duration {integer}
set bounce-port-link [disable|enable]
set count [disable|enable]
set description {string}
set fortilink {string}
set poe-reset [disable|enable]
set traffic-policy {string}
set vlan {string}
next
end
config switch-controller mac-policy
Parameter
Description
Type
Size
Default
bounce-port-duration
Bounce duration in seconds of a switch port where
this mac-policy is applied.
integer
Minimum
value: 1
Maximum
value: 30
5
bounce-port-link
Enable/disable bouncing (administratively bring the
link down, up) of a switch port where this mac-policy is applied.
option
-enable
Option
Description
disable
Disable bouncing (administratively bring the link down, up) of a switch
port where this mac-policy is applied.
enable
Enable bouncing (administratively bring the link down, up) of a switch
port where this mac-policy is applied.
count
Enable/disable packet count on the NAC device.
option
-disable
Option
Description
disable
Enable packet count on the NAC device.
enable
Disable packet count on the NAC device.
description
Description for the MAC policy.
string
Maximum
length: 63
FortiOS 8.0.0 CLI Reference
1353
Fortinet Inc.

<!-- 来源页 1354 -->
Parameter
Description
Type
Size
Default
fortilink
FortiLink interface for which this MAC policy
belongs to.
string
Maximum
length: 15
name
MAC policy name.
string
Maximum
length: 63
poe-reset
Enable/disable POE reset of a switch port where
this mac-policy is applied.
option
-disable
Option
Description
disable
Disable POE reset of a switch port where this mac-policy is applied.
enable
Enable POE reset of a switch port where this mac-policy is applied.
traffic-policy
Traffic policy to be applied when using this MAC
policy.
string
Maximum
length: 63
vlan
Ingress traffic VLAN assignment for the MAC
address matching this MAC policy.
string
Maximum
length: 15
config switch-controller managed-switch
Configure FortiSwitch devices that are managed by this FortiGate.
config switch-controller managed-switch
Description: Configure FortiSwitch devices that are managed by this FortiGate.
edit <switch-id>
config 802-1X-settings
Description: Configuration method to edit FortiSwitch 802.1X global settings.
set allow-mac-move [disable|enable]
set link-down-auth [set-unauth|no-action]
set local-override [enable|disable]
set mab-entry-as [static|dynamic]
set mab-reauth [disable|enable]
set mac-called-station-delimiter [colon|hyphen|...]
set mac-calling-station-delimiter [colon|hyphen|...]
set mac-case [lowercase|uppercase]
set mac-password-delimiter [colon|hyphen|...]
set mac-username-delimiter [colon|hyphen|...]
set max-reauth-attempt {integer}
set reauth-period {integer}
set tx-period {integer}
end
set access-profile {string}
config components
Description: Managed-switch component list.
edit <name>
set admin-status [disable|enable]
set capability {user}
FortiOS 8.0.0 CLI Reference
1354
Fortinet Inc.

<!-- 来源页 1355 -->
set component-id {integer}
set description {string}
set dynamically-discovered {integer}
set max-allowed-trunk-members {integer}
set poe-detection-type {integer}
set role [None|Primary|...]
set serial-number {string}
set status [offline|online]
set sw-version {string}
set switch-id {string}
set type [stack-node|supervisor|...]
set version {integer}
next
end
config custom-command
Description: Configuration method to edit FortiSwitch commands to be pushed to this
FortiSwitch device upon rebooting the FortiGate switch controller or the FortiSwitch.
edit <command-entry>
set command-name {string}
next
end
set delayed-restart-trigger {integer}
set description {string}
set dhcp-server-access-list [global|enable|...]
config dhcp-snooping-static-client
Description: Configure FortiSwitch DHCP snooping static clients.
edit <name>
set ip {ipv4-address}
set mac {mac-address}
set port {string}
set vlan {string}
next
end
set directly-connected {integer}
set dynamic-capability {user}
set dynamically-discovered {integer}
set firmware-provision [enable|disable]
set firmware-provision-latest [disable|once]
set firmware-provision-version {string}
set flow-identity {user}
set fsw-wan1-admin [discovered|disable|...]
set fsw-wan1-peer {string}
config igmp-snooping
Description: Configure FortiSwitch IGMP snooping global settings.
set aging-time {integer}
set flood-unknown-multicast [enable|disable]
set local-override [enable|disable]
config vlans
Description: Configure IGMP snooping VLAN.
edit <vlan-name>
set proxy [disable|enable|...]
set querier [disable|enable]
FortiOS 8.0.0 CLI Reference
1355
Fortinet Inc.

<!-- 来源页 1356 -->
set querier-addr {ipv4-address}
set version {integer}
next
end
end
config ip-source-guard
Description: IP source guard.
edit <port>
config binding-entry
Description: IP and MAC address configuration.
edit <entry-name>
set ip {ipv4-address-any}
set mac {mac-address}
next
end
set description {string}
next
end
set l3-discovered {integer}
set max-allowed-trunk-members {integer}
set max-poe-budget {integer}
set mclag-igmp-snooping-aware [enable|disable]
set mgmt-mode {integer}
config mirror
Description: Configuration method to edit FortiSwitch packet mirror.
edit <name>
set dst {string}
set src-egress <name1>, <name2>, ...
set src-ingress <name1>, <name2>, ...
set status [active|inactive]
set switching-packet [enable|disable]
next
end
set override-snmp-community [enable|disable]
set override-snmp-sysinfo [disable|enable]
set override-snmp-trap-threshold [enable|disable]
set override-snmp-user [enable|disable]
set owner-vdom {string}
set poe-detection-type {integer}
set poe-pre-standard-detection [enable|disable]
set port-selection-criteria [src-mac|dst-mac|...]
config ports
Description: Managed-switch port list.
edit <port-name>
set access-mode [dynamic|nac|...]
set acl-group <name1>, <name2>, ...
set aggregator-mode [bandwidth|count]
set allow-arp-monitor [disable|enable]
set allowed-vlans <vlan-name1>, <vlan-name2>, ...
set allowed-vlans-all [enable|disable]
set arp-inspection-trust [untrusted|trusted]
set authenticated-port {integer}
FortiOS 8.0.0 CLI Reference
1356
Fortinet Inc.

<!-- 来源页 1357 -->
set bundle [enable|disable]
set description {string}
config dhcp-snoop-option82-override
Description: Configure DHCP snooping option 82 override.
edit <vlan-name>
set circuit-id {string}
set remote-id {string}
next
end
set dhcp-snoop-option82-trust [enable|disable]
set dhcp-snooping [untrusted|trusted]
set discard-mode [none|all-untagged|...]
set edge-port [enable|disable]
set eee-tx-idle-time {integer}
set eee-tx-wake-time {integer}
set encrypted-port {integer}
set energy-efficient-ethernet [disable|enable]
set export-to {string}
set export-to-pool {string}
set fallback-port {string}
set fec-capable {integer}
set fec-state [disabled|cl74|...]
set fgt-peer-device-name {string}
set fgt-peer-port-name {string}
set fiber-port {integer}
set flags {integer}
set flap-duration {integer}
set flap-rate {integer}
set flap-timeout {integer}
set flapguard [enable|disable]
set flow-control [disable|tx|...]
set fortilink-port {integer}
set fortiswitch-acls <id1>, <id2>, ...
set igmp-snooping-flood-reports [enable|disable]
set interface-tags <tag-name1>, <tag-name2>, ...
set ip-source-guard [disable|enable]
set isl-local-trunk-name {string}
set isl-peer-device-name {string}
set isl-peer-device-sn {string}
set isl-peer-port-name {string}
set lacp-speed [slow|fast]
set learning-limit {integer}
set lldp-profile {string}
set lldp-status [disable|rx-only|...]
set log-mac-event [disable|enable]
set loop-guard [enabled|disabled]
set loop-guard-timeout {integer}
set mac-addr {mac-address}
set matched-dpp-intf-tags {string}
set matched-dpp-policy {string}
set max-bundle {integer}
set mcast-snooping-flood-traffic [enable|disable]
FortiOS 8.0.0 CLI Reference
1357
Fortinet Inc.

<!-- 来源页 1358 -->
set mclag [enable|disable]
set mclag-icl-port {integer}
set media-type {string}
set member-withdrawal-behavior [forward|block]
set members <member-name1>, <member-name2>, ...
set min-bundle {integer}
set mode [static|lacp-passive|...]
set p2p-port {integer}
set packet-sample-rate {integer}
set packet-sampler [enabled|disabled]
set pause-meter {integer}
set pause-meter-resume [75%|50%|...]
set pd-capable {integer}
set poe-capable {integer}
set poe-max-power {string}
set poe-max-power-mode [class-based|30W|...]
set poe-mode-bt-cabable {integer}
set poe-port-mode [ieee802-3af|ieee802-3at|...]
set poe-port-power [normal|perpetual|...]
set poe-port-priority [critical-priority|high-priority|...]
set poe-pre-standard-detection [enable|disable]
set poe-standard {string}
set poe-status [enable|disable]
set port-number {integer}
set port-owner {string}
set port-policy {string}
set port-prefix-type {integer}
set port-security-policy {string}
set port-selection-criteria [src-mac|dst-mac|...]
set ptp-policy {string}
set ptp-status [disable|enable]
set qnq {string}
set qos-policy {string}
set restricted-auth-port {integer}
set rpvst-port [disabled|enabled]
set sample-direction [tx|rx|...]
set sflow-counter-interval {integer}
set speed [10half|10full|...]
set stacking-port {integer}
set status [up|down]
set sticky-mac [enable|disable]
set storm-control-policy {string}
set stp-bpdu-guard [enabled|disabled]
set stp-bpdu-guard-timeout {integer}
set stp-root-guard [enabled|disabled]
set stp-state [enabled|disabled]
set switch-id {string}
set type [physical|trunk]
set untagged-vlans <vlan-name1>, <vlan-name2>, ...
set vlan {string}
next
end
FortiOS 8.0.0 CLI Reference
1358
Fortinet Inc.

<!-- 来源页 1359 -->
set pre-provisioned {integer}
set ptp-profile {string}
set ptp-status [disable|enable]
set purdue-level [1|1.5|...]
set qos-drop-policy [taildrop|random-early-detection]
set qos-red-probability {integer}
set radius-nas-ip {ipv4-address}
set radius-nas-ip-override [disable|enable]
config remote-log
Description: Configure logging by FortiSwitch device to a remote syslog server.
edit <name>
set csv [enable|disable]
set facility [kernel|user|...]
set port {integer}
set server {string}
set severity [emergency|alert|...]
set status [enable|disable]
next
end
set route-offload [disable|enable]
set route-offload-mclag [disable|enable]
config route-offload-router
Description: Configure route offload MCLAG IP address.
edit <vlan-name>
set router-ip {ipv4-address}
next
end
config router-static
Description: Configure static routes.
edit <id>
set blackhole [disable|enable]
set comment {string}
set device {string}
set distance {integer}
set dst {ipv4-classnet}
set dynamic-gateway [disable|enable]
set gateway {ipv4-address}
set status [disable|enable]
set switch-id {string}
set vrf {string}
next
end
config router-vrf
Description: Configure VRF.
edit <name>
set switch-id {string}
set vrfid {integer}
next
end
set sn {string}
config snmp-community
Description: Configuration method to edit Simple Network Management Protocol (SNMP)
FortiOS 8.0.0 CLI Reference
1359
Fortinet Inc.

<!-- 来源页 1360 -->
communities.
edit <id>
set events {option1}, {option2}, ...
config hosts
Description: Configure IPv4 SNMP managers (hosts).
edit <id>
set ip {user}
next
end
set name {string}
set query-v1-port {integer}
set query-v1-status [disable|enable]
set query-v2c-port {integer}
set query-v2c-status [disable|enable]
set status [disable|enable]
set trap-v1-lport {integer}
set trap-v1-rport {integer}
set trap-v1-status [disable|enable]
set trap-v2c-lport {integer}
set trap-v2c-rport {integer}
set trap-v2c-status [disable|enable]
next
end
config snmp-sysinfo
Description: Configuration method to edit Simple Network Management Protocol (SNMP)
system info.
set contact-info {string}
set description {string}
set engine-id {string}
set location {string}
set status [disable|enable]
end
config snmp-trap-threshold
Description: Configuration method to edit Simple Network Management Protocol (SNMP)
trap threshold values.
set trap-high-cpu-threshold {integer}
set trap-log-full-threshold {integer}
set trap-low-memory-threshold {integer}
end
config snmp-user
Description: Configuration method to edit Simple Network Management Protocol (SNMP)
users.
edit <name>
set auth-proto [md5|sha1|...]
set auth-pwd {password}
set priv-proto [aes128|aes192|...]
set priv-pwd {password}
set queries [disable|enable]
set query-port {integer}
set security-level [no-auth-no-priv|auth-no-priv|...]
next
end
FortiOS 8.0.0 CLI Reference
1360
Fortinet Inc.

<!-- 来源页 1361 -->
set staged-image-version {string}
config static-mac
Description: Configuration method to edit FortiSwitch Static and Sticky MAC.
edit <id>
set description {string}
set interface {string}
set mac {mac-address}
set type [static|sticky]
set vlan {string}
next
end
config storm-control
Description: Configuration method to edit FortiSwitch storm control for measuring
traffic activity using data rates to prevent traffic disruption.
set broadcast [enable|disable]
set burst-size-level {integer}
set local-override [enable|disable]
set rate {integer}
set unknown-multicast [enable|disable]
set unknown-unicast [enable|disable]
end
config stp-instance
Description: Configuration method to edit Spanning Tree Protocol (STP) instances.
edit <id>
set priority [0|4096|...]
next
end
config stp-settings
Description: Configuration method to edit Spanning Tree Protocol (STP) settings used
to prevent bridge loops.
set forward-time {integer}
set hello-time {integer}
set local-override [enable|disable]
set max-age {integer}
set max-hops {integer}
set name {string}
set pending-timer {integer}
set revision {integer}
end
set switch-device-tag {string}
set switch-dhcp_opt43_key {string}
config switch-log
Description: Configuration method to edit FortiSwitch logging settings (logs are
transferred to and inserted into the FortiGate event log).
set local-override [enable|disable]
set severity [emergency|alert|...]
set status [enable|disable]
end
set switch-profile {string}
config system-dhcp-server
Description: Configure DHCP servers.
edit <id>
FortiOS 8.0.0 CLI Reference
1361
Fortinet Inc.

<!-- 来源页 1362 -->
set default-gateway {ipv4-address}
set dns-server1 {ipv4-address}
set dns-server2 {ipv4-address}
set dns-server3 {ipv4-address}
set dns-service [local|default|...]
set interface {string}
config ip-range
Description: DHCP IP range configuration.
edit <id>
set end-ip {ipv4-address}
set start-ip {ipv4-address}
next
end
set lease-time {integer}
set netmask {ipv4-netmask}
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
set value {string}
next
end
set status [disable|enable]
set switch-id {string}
next
end
config system-interface
Description: Configure system interface on FortiSwitch.
edit <name>
set allowaccess {option1}, {option2}, ...
set interface {string}
set ip {ipv4-classnet-host}
set mode [static|dhcp]
set status [disable|enable]
set switch-id {string}
set type [vlan|physical]
set vlan {string}
set vrf {string}
next
end
set tdr-supported {string}
set tunnel-discovered {integer}
set type [virtual|physical]
set version {integer}
config vlan
Description: Configure VLAN assignment priority.
FortiOS 8.0.0 CLI Reference
1362
Fortinet Inc.

<!-- 来源页 1363 -->
edit <vlan-name>
set assignment-priority {integer}
next
end
next
end
config switch-controller managed-switch
Parameter
Description
Type
Size
Default
access-profile
FortiSwitch access
profile.
string
Maximum
length: 31
default
delayed-restart-trigger
Delayed restart
triggered for this
FortiSwitch.
integer
Minimum
value: 0
Maximum
value: 255
0
description
Description.
string
Maximum
length: 63
dhcp-server-access-list
DHCP snooping
server access list.
option
-global
Option
Description
global
Use global setting for DHCP snooping server access list.
enable
Override global setting and enable DHCP server access list.
disable
Override global setting and disable DHCP server access list.
directly-connected
Directly connected
FortiSwitch. Read-only.
integer
Minimum
value: 0
Maximum
value: 1
0
dynamic-capability
List of features this
FortiSwitch
supports (not
configurable) that
is sent to the
FortiGate device
for subsequent
configuration
initiated by the
FortiGate device.
user
Not
Specified
0x0000000000000000000000000000000
0
FortiOS 8.0.0 CLI Reference
1363
Fortinet Inc.

<!-- 来源页 1364 -->
Parameter
Description
Type
Size
Default
dynamically-discovered
Dynamically
discovered
FortiSwitch. Read-only.
integer
Minimum
value: 0
Maximum
value: 1
0
firmware-provision
Enable/disable
provisioning of
firmware to
FortiSwitches on
join connection.
option
-disable
Option
Description
enable
Enable firmware-provision.
disable
Disable firmware-provision.
firmware-provision-latest
Enable/disable
one-time automatic
provisioning of the
latest firmware
version.
option
-disable
Option
Description
disable
Do not automatically provision the latest available firmware.
once
Automatically attempt a one-time upgrade to the latest available
firmware version.
firmware-provision-version
Firmware version to
provision to this
FortiSwitch on
bootup
(major.minor.build,
i.e. 6.2.1234).
string
Maximum
length: 35
flow-identity
Flow-tracking
netflow ipfix switch
identity in hex
format(00000000-FFFFFFFF
default=0).
user
Not
Specified
00000000
fsw-wan1-admin
FortiSwitch WAN1
admin status;
enable to authorize
the FortiSwitch as a
managed switch.
option
-discovered
FortiOS 8.0.0 CLI Reference
1364
Fortinet Inc.

<!-- 来源页 1365 -->
Parameter
Description
Type
Size
Default
Option
Description
discovered
Link waiting to be authorized.
disable
Link unauthorized.
enable
Link authorized.
fsw-wan1-peer
FortiSwitch WAN1
peer port.
string
Maximum
length: 35
l3-discovered
Layer 3
management
discovered. Read-only.
integer
Minimum
value: 0
Maximum
value: 1
0
max-allowed-trunk-members
FortiSwitch
maximum allowed
trunk members.
integer
Minimum
value: 0
Maximum
value: 255
0
max-poe-budget
Max PoE budget for
FortiSwitch. Read-only.
integer
Minimum
value: 0
Maximum
value:
65535
0
mclag-igmp-snooping-aware
Enable/disable
MCLAG IGMP-snooping
awareness.
option
-enable
Option
Description
enable
Enable MCLAG IGMP-snooping awareness.
disable
Disable MCLAG IGMP-snooping awareness.
mgmt-mode
FortiLink
management
mode.
integer
Minimum
value: 0
Maximum
value: 255
0
override-snmp-community
Enable/disable
overriding the
global SNMP
communities.
option
-disable
Option
Description
enable
Override the global SNMP communities.
FortiOS 8.0.0 CLI Reference
1365
Fortinet Inc.

<!-- 来源页 1366 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Use the global SNMP communities.
override-snmp-sysinfo
Enable/disable
overriding the
global SNMP
system information.
option
-disable
Option
Description
disable
Use the global SNMP system information.
enable
Override the global SNMP system information.
override-snmp-trap-threshold
Enable/disable
overriding the
global SNMP trap
threshold values.
option
-disable
Option
Description
enable
Override the global SNMP trap threshold values.
disable
Use the global SNMP trap threshold values.
override-snmp-user
Enable/disable
overriding the
global SNMP users.
option
-disable
Option
Description
enable
Override the global SNMPv3 users.
disable
Use the global SNMPv3 users.
owner-vdom
VDOM which owner
of port belongs to.
string
Maximum
length: 31
poe-detection-type
PoE detection type
for FortiSwitch.
Read-only.
integer
Minimum
value: 0
Maximum
value: 255
0
poe-pre-standard-detection
Enable/disable PoE
pre-standard
detection.
option
-disable
Option
Description
enable
Enable PoE pre-standard detection.
FortiOS 8.0.0 CLI Reference
1366
Fortinet Inc.

<!-- 来源页 1367 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable PoE pre-standard detection.
port-selection-criteria *
Algorithm for
aggregate port
selection.
option
-src-dst-ip
Option
Description
src-mac
Source MAC address.
dst-mac
Destination MAC address.
src-dst-mac
Source and destination MAC address.
src-ip
Source IP address.
dst-ip
Destination IP address.
src-dst-ip
Source and destination IP address.
pre-provisioned
Pre-provisioned
managed switch.
integer
Minimum
value: 0
Maximum
value: 255
0
ptp-profile
PTP profile
configuration.
string
Maximum
length: 63
default
ptp-status
Enable/disable PTP
profile on this
FortiSwitch.
option
-disable
Option
Description
disable
Disable PTP profile.
enable
Enable PTP profile.
purdue-level
Purdue Level of this
FortiSwitch.
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
FortiOS 8.0.0 CLI Reference
1367
Fortinet Inc.

<!-- 来源页 1368 -->
Parameter
Description
Type
Size
Default
Option
Description
3
Level 3 - Operations & Control
3.5
Level 3.5
4
Level 4 - Business Planning & Logistics
5
Level 5 - Enterprise Network
5.5
Level 5.5
qos-drop-policy
Set QoS drop-policy.
option
-taildrop
Option
Description
taildrop
Taildrop policy.
random-early-detection
Random early detection drop policy.
qos-red-probability
Set QoS RED/WRED
drop probability.
integer
Minimum
value: 0
Maximum
value: 100
12
radius-nas-ip
NAS-IP address.
ipv4-address
Not
Specified
0.0.0.0
radius-nas-ip-override
Use locally defined
NAS-IP.
option
-disable
Option
Description
disable
Disable radius-nas-ip-override.
enable
Enable radius-nas-ip-override.
route-offload
Enable/disable
route offload on
this FortiSwitch.
option
-disable
Option
Description
disable
Disable route offload.
enable
Enable route offload.
route-offload-mclag
Enable/disable
route offload
MCLAG on this
FortiSwitch.
option
-disable
FortiOS 8.0.0 CLI Reference
1368
Fortinet Inc.

<!-- 来源页 1369 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable route offload MCLAG.
enable
Enable route offload MCLAG.
sn
Managed-switch
serial number.
string
Maximum
length: 16
staged-image-version
Staged image
version for
FortiSwitch.
string
Maximum
length: 127
switch-device-tag
User definable
label/tag.
string
Maximum
length: 32
switch-dhcp_
opt43_key
DHCP option43
key.
string
Maximum
length: 63
switch-id
Managed-switch
name.
string
Maximum
length: 35
switch-profile
FortiSwitch profile.
string
Maximum
length: 35
default
tdr-supported
TDR supported.
Read-only.
string
Maximum
length: 31
tunnel-discovered
SOCKS tunnel
management
discovered. Read-only.
integer
Minimum
value: 0
Maximum
value: 1
0
type
Indication of switch
type, physical or
virtual.
option
-physical
Option
Description
virtual
Switch is of type virtual.
physical
Switch is of type physical.
version
FortiSwitch version.
integer
Minimum
value: 0
Maximum
value: 255
0
* This parameter may not exist in some models.
FortiOS 8.0.0 CLI Reference
1369
Fortinet Inc.

<!-- 来源页 1370 -->
config 802-1X-settings
Parameter
Description
Type
Size
Default
allow-mac-move *
Enable/disable MAC move (default = enable).
option
-enable
Option
Description
disable
Disable MAC move.
enable
Enable MAC move.
link-down-auth
Authentication state to set if a link is down.
option
-set-unauth
Option
Description
set-unauth
Interface set to unauth when down. Reauthentication is needed.
no-action
Interface reauthentication is not needed.
local-override
Enable to override global 802.1X settings on
individual FortiSwitches.
option
-disable
Option
Description
enable
Override global 802.1X settings.
disable
Use global 802.1X settings.
mab-entry-as
*
Configure MAB MAC entry as static or dynamic
(default = static).
option
-static
Option
Description
static
MAB MAC entry as static.
dynamic
MAB MAC entry as dynamic.
mab-reauth
Enable or disable MAB reauthentication settings.
option
-disable
Option
Description
disable
Disable MAB re-authentication setttings.
enable
Enable MAB re-authentication setttings.
mac-called-station-delimiter
MAC called station delimiter (default = hyphen).
option
-hyphen
FortiOS 8.0.0 CLI Reference
1370
Fortinet Inc.

<!-- 来源页 1371 -->
Parameter
Description
Type
Size
Default
Option
Description
colon
Use colon as delimiter for called station.
hyphen
Use hyphen as delimiter for called station.
none
No delimiter for called station.
single-hyphen
Use single hyphen as delimiter for called station.
mac-calling-station-delimiter
MAC calling station delimiter (default = hyphen).
option
-hyphen
Option
Description
colon
Use colon as delimiter for calling station.
hyphen
Use hyphen as delimiter for calling station.
none
No delimiter for calling station.
single-hyphen
Use single hyphen as delimiter for calling station.
mac-case
MAC case (default = lowercase).
option
-lowercase
Option
Description
lowercase
Use lowercase MAC.
uppercase
Use uppercase MAC.
mac-password-delimiter
MAC authentication password delimiter (default =
hyphen).
option
-hyphen
Option
Description
colon
Use colon as delimiter for MAC auth password.
hyphen
Use hyphen as delimiter for MAC auth password.
none
No delimiter for MAC auth password.
single-hyphen
Use single hyphen as delimiter for MAC auth password.
mac-username-delimiter
MAC authentication username delimiter (default =
hyphen).
option
-hyphen
Option
Description
colon
Use colon as delimiter for MAC auth username.
FortiOS 8.0.0 CLI Reference
1371
Fortinet Inc.

<!-- 来源页 1372 -->
Parameter
Description
Type
Size
Default
Option
Description
hyphen
Use hyphen as delimiter for MAC auth username.
none
No delimiter for MAC auth username.
single-hyphen
Use single hyphen as delimiter for MAC auth username.
max-reauth-attempt
Maximum number of authentication attempts (0 -15, default = 3).
integer
Minimum
value: 0
Maximum
value: 15
3
reauth-period
Reauthentication time interval (1 - 1440 min,
default = 60, 0 = disable).
integer
Minimum
value: 0
Maximum
value: 1440
60
tx-period
802.1X Tx period (seconds, default=30).
integer
Minimum
value: 12
Maximum
value: 60
30
* This parameter may not exist in some models.
config components
Parameter
Description
Type
Size
Default
admin-status
Managed-switch
component admin-status.
option
-disable
Option
Description
disable
Disable the component.
enable
Enable the component.
capability
Managed-switch
feature capability
list.
user
Not
Specified
0x00000000000000000000000000000000
component-id
Managed-switch
component id in
stacking/chassis.
integer
Minimum
value: 1
Maximum
value: 10
0
description
Managed-switch
component
description.
string
Maximum
length: 63
FortiOS 8.0.0 CLI Reference
1372
Fortinet Inc.

<!-- 来源页 1373 -->
Parameter
Description
Type
Size
Default
dynamically-discovered
Managed-switch
component is
dynamically
discovered or not.
Read-only.
integer
Minimum
value: 0
Maximum
value: 1
0
max-allowed-trunk-members
Managed-switch
component
maximum allowed
trunk members.
integer
Minimum
value: 0
Maximum
value: 255
0
name
Managed-switch
component name.
string
Maximum
length: 63
poe-detection-type
Managed-switch
component PoE
detection type.
Read-only.
integer
Minimum
value: 0
Maximum
value: 255
0
role
Managed-switch
components role.
option
-None
Option
Description
None
No Status.
Primary
HA Primary node.
Backup
HA Backup node.
Follower
Follower node.
Standalone
Standalone node.
serial-number
Managed-switch
component serial
number.
string
Maximum
length: 16
status
Managed-switch
component status.
Read-only.
option
-offline
Option
Description
offline
Operational down
online
Operational Up
sw-version
Managed-switch
component
software version.
string
Maximum
length: 63
FortiOS 8.0.0 CLI Reference
1373
Fortinet Inc.

<!-- 来源页 1374 -->
Parameter
Description
Type
Size
Default
switch-id
Managed-switch
component parent
switch id. Read-only.
string
Maximum
length: 35
type
Managed-switch
component type.
option
-stack-node
Option
Description
stack-node
Stacking node.
supervisor
Chassis supervisor module.
linecard
Chassis linecard module.
version
Managed-switch
component
version.
integer
Minimum
value: 0
Maximum
value: 255
0
config custom-command
Parameter
Description
Type
Size
Default
command-entry
List of FortiSwitch commands.
string
Maximum
length: 35
command-name
Names of commands to be pushed to this
FortiSwitch device, as configured under config
switch-controller custom-command.
string
Maximum
length: 35
config dhcp-snooping-static-client
Parameter
Description
Type
Size
Default
ip
Client static IP address.
ipv4-address
Not
Specified
0.0.0.0
mac
Client MAC address.
mac-address
Not
Specified
00:00:00:00:00:00
name
Client name.
string
Maximum
length: 35
port
Interface name.
string
Maximum
length: 15
vlan
VLAN name.
string
Maximum
length: 15
FortiOS 8.0.0 CLI Reference
1374
Fortinet Inc.

<!-- 来源页 1375 -->
config igmp-snooping
Parameter
Description
Type
Size
Default
aging-time
Maximum time to retain a multicast snooping entry
for which no packets have been seen (15 - 3600
sec, default = 300).
integer
Minimum
value: 15
Maximum
value: 3600
300
flood-unknown-multicast
Enable/disable unknown multicast flooding.
option
-disable
Option
Description
enable
Enable unknown multicast flooding.
disable
Disable unknown multicast flooding.
local-override
Enable/disable overriding the global IGMP
snooping configuration.
option
-disable
Option
Description
enable
Override the global IGMP snooping configuration.
disable
Use the global IGMP snooping configuration.
config vlans
Parameter
Description
Type
Size
Default
proxy
IGMP snooping proxy for the VLAN interface.
option
-global
Option
Description
disable
Disable IGMP snooping proxy on VLAN interface.
enable
Enable IGMP snooping proxy on VLAN interface.
global
Use global setting for IGMP snooping proxy on VLAN interface.
querier
Enable/disable IGMP snooping querier for the VLAN
interface.
option
-disable
Option
Description
disable
Disable IGMP snooping querier on VLAN interface.
enable
Enable IGMP snooping querier on VLAN interface.
querier-addr
IGMP snooping querier address.
ipv4-address
Not
Specified
0.0.0.0
FortiOS 8.0.0 CLI Reference
1375
Fortinet Inc.

<!-- 来源页 1376 -->
Parameter
Description
Type
Size
Default
version
IGMP snooping querying version.
integer
Minimum
value: 2
Maximum
value: 3
2
vlan-name
List of FortiSwitch VLANs.
string
Maximum
length: 15
default
config ip-source-guard
Parameter
Description
Type
Size
Default
description
Description.
string
Maximum
length: 63
port
Ingress interface to which source guard is bound.
string
Maximum
length: 15
config binding-entry
Parameter
Description
Type
Size
Default
entry-name
Configure binding pair.
string
Maximum
length: 16
ip
Source IP for this rule.
ipv4-address-any
Not
Specified
0.0.0.0
mac
MAC address for this rule.
mac-address
Not
Specified
00:00:00:00:00:00
config mirror
Parameter
Description
Type
Size
Default
dst
Destination port.
string
Maximum
length: 63
name
Mirror name.
string
Maximum
length: 63
src-egress
<name>
Source egress interfaces.
Interface name.
string
Maximum
length: 79
src-ingress
<name>
Source ingress interfaces.
Interface name.
string
Maximum
length: 79
status
Active/inactive mirror configuration.
option
-inactive
FortiOS 8.0.0 CLI Reference
1376
Fortinet Inc.

<!-- 来源页 1377 -->
Parameter
Description
Type
Size
Default
Option
Description
active
Activate mirror configuration.
inactive
Deactivate mirror configuration.
switching-packet
Enable/disable switching functionality when
mirroring.
option
-disable
Option
Description
enable
Enable switching functionality when mirroring.
disable
Disable switching functionality when mirroring.
config ports
Parameter
Description
Type
Size
Default
access-mode
Access mode of the port.
option
-static
Option
Description
dynamic
Dynamic mode.
nac
NAC mode.
static
Static mode.
acl-group <name>
ACL groups on this port.
ACL group name.
string
Maximum
length: 79
aggregator-mode
LACP member select mode.
option
-bandwidth
Option
Description
bandwidth
Member selection based on largest total bandwidth of links of similar
speed.
count
Member selection based on largest count of similar link speed.
allow-arp-monitor
Enable/Disable allow ARP monitor.
option
-disable
Option
Description
disable
Disable allow ARP monitor.
enable
Enable allow ARP monitor.
allowed-vlans
<vlan-name>
Configure switch port tagged
VLANs.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
1377
Fortinet Inc.

<!-- 来源页 1378 -->
Parameter
Description
Type
Size
Default
VLAN name.
allowed-vlans-all
Enable/disable all defined vlans on
this port.
option
-disable
Option
Description
enable
Enable all defined VLANs on this port.
disable
Disable all defined VLANs on this port.
arp-inspection-trust
Trusted or untrusted dynamic ARP
inspection.
option
-untrusted
Option
Description
untrusted
Untrusted dynamic ARP inspection.
trusted
Trusted dynamic ARP inspection.
authenticated-port
Peer to Peer Authenticated port.
Read-only.
integer
Minimum value:
0 Maximum
value: 1
0
bundle
Enable/disable Link Aggregation
Group (LAG) bundling for non-FortiLink interfaces.
option
-disable
Option
Description
enable
Enable bundling.
disable
Disable bundling.
description
Description for port.
string
Maximum
length: 63
dhcp-snoop-option82-trust
Enable/disable allowance of DHCP
with option-82 on untrusted
interface.
option
-disable
Option
Description
enable
Enable allowance of DHCP with option-82 on untrusted interface.
disable
Disable allowance of DHCP with option-82 on untrusted interface.
dhcp-snooping
Trusted or untrusted DHCP-snooping interface.
option
-untrusted
FortiOS 8.0.0 CLI Reference
1378
Fortinet Inc.

<!-- 来源页 1379 -->
Parameter
Description
Type
Size
Default
Option
Description
untrusted
Untrusted DHCP snooping interface.
trusted
Trusted DHCP snooping interface.
discard-mode
Configure discard mode for port.
option
-none
Option
Description
none
Discard disabled.
all-untagged
Discard all frames that are untagged.
all-tagged
Discard all frames that are tagged.
edge-port
Enable/disable this interface as an
edge port, bridging connections
between workstations and/or
computers.
option
-enable
Option
Description
enable
Enable this interface as an edge port.
disable
Disable this interface as an edge port.
eee-tx-idle-time
*
Time in which the transmitter is in
low power idle (LPI) before
transitioning to the refresh state in
microseconds (0 - 2560, default =
60).
integer
Minimum value:
0 Maximum
value: 2560
60
eee-tx-wake-time *
Time for the transmitter to
transition from low power idle
(LPI) to its normal operating state
in microseconds (0 - 2560, default
= 30).
integer
Minimum value:
0 Maximum
value: 2560
30
encrypted-port
Peer to Peer Encrypted port.
Read-only.
integer
Minimum value:
0 Maximum
value: 1
0
energy-efficient-ethernet *
Enable/disable energy efficient
events.
option
-disable
Option
Description
disable
Disable energy efficient ethernet.
enable
Enable energy efficient ethernet.
FortiOS 8.0.0 CLI Reference
1379
Fortinet Inc.

<!-- 来源页 1380 -->
Parameter
Description
Type
Size
Default
export-to
Export managed-switch port to a
tenant VDOM.
string
Maximum
length: 31
export-to-pool
Switch controller export port to
pool-list.
string
Maximum
length: 35
fallback-port
LACP fallback port.
string
Maximum
length: 79
fec-capable
FEC capable.
integer
Minimum value:
0 Maximum
value: 1
0
fec-state
State of forward error correction.
option
-detect-by-module
Option
Description
disabled
Disable forward error correction.
cl74
Enable Clause 74 FC-FEC, which only applies to 25Gbps.
cl91
Enable Clause 91 RS-FEC, which only applies to 100Gbps.
detect-by-module
FEC supported by module.
fgt-peer-device-name
FGT peer device name. Read-only.
string
Maximum
length: 35
fgt-peer-port-name
FGT peer port name. Read-only.
string
Maximum
length: 15
fiber-port
Fiber-port. Read-only.
integer
Minimum value:
0 Maximum
value: 1
0
flags
Port properties flags. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
flap-duration
Period over which flap events are
calculated (seconds).
integer
Minimum value:
5 Maximum
value: 300
30
flap-rate
Number of stage change events
needed within flap-duration.
integer
Minimum value:
1 Maximum
value: 30
5
flap-timeout
Flap guard disabling protection
(min).
integer
Minimum value:
0 Maximum
value: 120
0
FortiOS 8.0.0 CLI Reference
1380
Fortinet Inc.

<!-- 来源页 1381 -->
Parameter
Description
Type
Size
Default
flapguard
Enable/disable flap guard.
option
-disable
Option
Description
enable
Enable FlapGuard for this port.
disable
Disable FlapGuard for this port.
flow-control
Flow control direction.
option
-disable
Option
Description
disable
Disable flow control.
tx
Enable flow control for transmission pause control frames.
rx
Enable flow control for receive pause control frames.
both
Enable flow control for both transmission and receive pause control
frames.
fortilink-port
FortiLink uplink port. Read-only.
integer
Minimum value:
0 Maximum
value: 1
0
fortiswitch-acls
<id>
ACLs on this port.
ACL ID.
integer
Minimum value:
0 Maximum
value:
4294967295
igmp-snooping-flood-reports
Enable/disable flooding of IGMP
reports to this interface when
igmp-snooping enabled.
option
-disable
Option
Description
enable
Enable flooding of IGMP snooping reports to this interface.
disable
Disable flooding of IGMP snooping reports to this interface.
interface-tags
<tag-name>
Tag(s) associated with the
interface for various features
including virtual port pool,
dynamic port policy.
FortiSwitch port tag name when
exported to a virtual port pool or
matched to dynamic port policy.
string
Maximum
length: 63
ip-source-guard
Enable/disable IP source guard.
option
-disable
FortiOS 8.0.0 CLI Reference
1381
Fortinet Inc.

<!-- 来源页 1382 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable IP source guard.
enable
Enable IP source guard.
isl-local-trunk-name
ISL local trunk name. Read-only.
string
Maximum
length: 15
isl-peer-device-name
ISL peer device name. Read-only.
string
Maximum
length: 35
isl-peer-device-sn
ISL peer device serial number.
Read-only.
string
Maximum
length: 16
isl-peer-port-name
ISL peer port name. Read-only.
string
Maximum
length: 15
lacp-speed
End Link Aggregation Control
Protocol (LACP) messages every
30 seconds (slow) or every
second (fast).
option
-slow
Option
Description
slow
Send LACP message every 30 seconds.
fast
Send LACP message every second.
learning-limit
Limit the number of dynamic MAC
addresses on this Port (1 - 128, 0
= no limit, default).
integer
Minimum value:
0 Maximum
value: 128
0
lldp-profile
LLDP port TLV profile.
string
Maximum
length: 63
default-auto-isl
lldp-status
LLDP transmit and receive status.
option
-tx-rx
Option
Description
disable
Disable LLDP TX and RX.
rx-only
Enable LLDP as RX only.
tx-only
Enable LLDP as TX only.
tx-rx
Enable LLDP TX and RX.
log-mac-event
Enable/disable logging for
dynamic MAC address events.
option
-disable
FortiOS 8.0.0 CLI Reference
1382
Fortinet Inc.

<!-- 来源页 1383 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable log MAC event for this interface.
enable
Enable log MAC event for this interface.
loop-guard
Enable/disable loop-guard on this
interface, an STP optimization
used to prevent network loops.
option
-disabled
Option
Description
enabled
Enable loop-guard on this interface.
disabled
Disable loop-guard on this interface.
loop-guard-timeout
Loop-guard timeout (0 - 120 min,
default = 45).
integer
Minimum value:
0 Maximum
value: 120
45
mac-addr
Port/Trunk MAC.
mac-address
Not Specified
00:00:00:00:00:00
matched-dpp-intf-tags
Matched interface tags in the
dynamic port policy.
string
Maximum
length: 63
matched-dpp-policy
Matched child policy in the
dynamic port policy.
string
Maximum
length: 63
max-bundle
Maximum size of LAG bundle (1 -24, default = 24).
integer
Minimum value:
1 Maximum
value: 24
24
mcast-snooping-flood-traffic
Enable/disable flooding of IGMP
snooping traffic to this interface.
option
-disable
Option
Description
enable
Enable flooding of IGMP snooping traffic to this interface.
disable
Disable flooding of IGMP snooping traffic to this interface.
mclag
Enable/disable multi-chassis link
aggregation (MCLAG).
option
-disable
Option
Description
enable
Enable MCLAG.
disable
Disable MCLAG.
FortiOS 8.0.0 CLI Reference
1383
Fortinet Inc.

<!-- 来源页 1384 -->
Parameter
Description
Type
Size
Default
mclag-icl-port
MCLAG-ICL port. Read-only.
integer
Minimum value:
0 Maximum
value: 1
0
media-type
Media type. Read-only.
string
Maximum
length: 31
member-withdrawal-behavior
Port behavior after it withdraws
because of loss of control
packets.
option
-block
Option
Description
forward
Forward traffic.
block
Block traffic.
members
<member-name>
Aggregated LAG bundle
interfaces.
Interface name from available
options.
string
Maximum
length: 79
min-bundle
Minimum size of LAG bundle (1 -24, default = 1).
integer
Minimum value:
1 Maximum
value: 24
1
mode
LACP mode: ignore and do not
send control messages, or
negotiate 802.3ad aggregation
passively or actively.
option
-static
Option
Description
static
Static aggregation, do not send and ignore any control messages.
lacp-passive
Passively use LACP to negotiate 802.3ad aggregation.
lacp-active
Actively use LACP to negotiate 802.3ad aggregation.
p2p-port
General peer to peer tunnel port.
Read-only.
integer
Minimum value:
0 Maximum
value: 1
0
packet-sample-rate
Packet sampling rate (0 - 99999
p/sec).
integer
Minimum value:
0 Maximum
value: 99999
512
packet-sampler
Enable/disable packet sampling
on this interface.
option
-disabled
FortiOS 8.0.0 CLI Reference
1384
Fortinet Inc.

<!-- 来源页 1385 -->
Parameter
Description
Type
Size
Default
Option
Description
enabled
Enable packet sampling on this interface.
disabled
Disable packet sampling on this interface.
pause-meter
Configure ingress pause metering
rate, in kbps (default = 0,
disabled).
integer
Minimum value:
128 Maximum
value:
2147483647
0
pause-meter-resume
Resume threshold for resuming
traffic on ingress port.
option
-50%
Option
Description
75%
Back pressure state won't be cleared until bucket count falls below
75% of pause threshold.
50%
Back pressure state won't be cleared until bucket count falls below
50% of pause threshold.
25%
Back pressure state won't be cleared until bucket count falls below
25% of pause threshold.
pd-capable
Powered device capable.
integer
Minimum value:
0 Maximum
value: 1
0
poe-capable
PoE capable.
integer
Minimum value:
0 Maximum
value: 1
0
poe-max-power
PoE maximum power. Read-only.
string
Maximum
length: 35
poe-max-power-mode *
PoE maximum power mode.
option
-class-based
Option
Description
class-based
Port will draw a maximum amount of power based on class.
30W
Port will be limited to draw a maximum of 30W.
60W
Port will be limited to draw a maximum of 60W.
poe-mode-bt-cabable
PoE mode IEEE 802.3BT capable.
integer
Minimum value:
0 Maximum
value: 1
0
poe-port-mode
Configure PoE port mode.
option
-ieee802-3at
FortiOS 8.0.0 CLI Reference
1385
Fortinet Inc.

<!-- 来源页 1386 -->
Parameter
Description
Type
Size
Default
Option
Description
ieee802-3af
IEEE802.3 AF.
ieee802-3at
IEEE802.3 AT.
ieee802-3bt
IEEE802.3 BT.
poe-port-power
Configure PoE port power.
option
-normal
Option
Description
normal
Power not delivered during boot.
perpetual
Power delivered during soft reboot.
perpetual-fast
Early power delivered during cold boot.
poe-port-priority
Configure PoE port priority.
option
-low-priority
Option
Description
critical-priority
Critical Priority.
high-priority
High Priority.
low-priority
Low Priority.
medium-priority
Medium Priority.
poe-pre-standard-detection
Enable/disable PoE pre-standard
detection.
option
-disable
Option
Description
enable
Enable PoE pre-standard detection.
disable
Disable PoE pre-standard detection.
poe-standard
PoE standard supported. Read-only.
string
Maximum
length: 63
poe-status
Enable/disable PoE status.
option
-enable
Option
Description
enable
Enable PoE status.
disable
Disable PoE status.
port-name
Switch port name.
string
Maximum
length: 15
FortiOS 8.0.0 CLI Reference
1386
Fortinet Inc.

<!-- 来源页 1387 -->
Parameter
Description
Type
Size
Default
port-number
Port number. Read-only.
integer
Minimum value:
1 Maximum
value: 64
0
port-owner
Switch port name.
string
Maximum
length: 15
port-policy
Switch controller dynamic port
policy from available options.
string
Maximum
length: 63
port-prefix-type
Port prefix type. Read-only.
integer
Minimum value:
0 Maximum
value: 1
0
port-security-policy
Switch controller authentication
policy to apply to this managed
switch from available options.
string
Maximum
length: 31
port-selection-criteria
Algorithm for aggregate port
selection.
option
-src-dst-ip
Option
Description
src-mac
Source MAC address.
dst-mac
Destination MAC address.
src-dst-mac
Source and destination MAC address.
src-ip
Source IP address.
dst-ip
Destination IP address.
src-dst-ip
Source and destination IP address.
ptp-policy
PTP policy configuration.
string
Maximum
length: 63
default
ptp-status
Enable/disable PTP policy on this
FortiSwitch port.
option
-enable
Option
Description
disable
Disable PTP policy.
enable
Enable PTP policy.
qnq
802.1AD VLANs in the VDom.
string
Maximum
length: 15
qos-policy
Switch controller QoS policy from
available options.
string
Maximum
length: 63
default
FortiOS 8.0.0 CLI Reference
1387
Fortinet Inc.

<!-- 来源页 1388 -->
Parameter
Description
Type
Size
Default
restricted-auth-port
Peer to Peer Restricted
Authenticated port. Read-only.
integer
Minimum value:
0 Maximum
value: 1
0
rpvst-port
Enable/disable inter-operability
with rapid PVST on this interface.
option
-disabled
Option
Description
disabled
Disable inter-operability with rapid PVST on this interface.
enabled
Enable inter-operability with rapid PVST on this interface.
sample-direction
Packet sampling direction.
option
-both
Option
Description
tx
Monitor transmitted traffic.
rx
Monitor received traffic.
both
Monitor transmitted and received traffic.
sflow-counter-interval
sFlow sampling counter polling
interval in seconds (0 - 255).
integer
Minimum value:
0 Maximum
value: 255
0
speed
Switch port speed; default and
available settings depend on
hardware.
option
-auto
Option
Description
10half
10M half-duplex.
10full
10M full-duplex.
100half
100M half-duplex.
100full
100M full-duplex.
1000full
1G full-duplex
10000full
10G full-duplex
auto
Auto-negotiation.
1000auto
Auto-negotiation (1G full-duplex only).
1000full-fiber
1G full-duplex (fiber SFPs only)
40000full
40G full-duplex
FortiOS 8.0.0 CLI Reference
1388
Fortinet Inc.

<!-- 来源页 1389 -->
Parameter
Description
Type
Size
Default
Option
Description
detect-by-module
Detect by Module.
100FX-half
100Mbps half-duplex.100Base-FX.
100FX-full
100Mbps full-duplex.100Base-FX.
100000full
100Gbps full-duplex.
2500auto
Auto-Negotiation (2.5Gbps Only).
2500full
2.5Gbps full-duplex.
25000full
25Gbps full-duplex.
50000full
50Gbps full-duplex.
10000cr
10Gbps copper interface.
10000sr
10Gbps SFI interface.
100000sr4
100Gbps SFI interface.
100000cr4
100Gbps copper interface.
40000sr4
40Gbps SFI interface.
40000cr4
40Gbps copper interface.
40000auto
Auto-Negotiation (40Gbps Only).
25000cr
25Gbps copper interface.
25000sr
25Gbps SFI interface.
50000cr
50Gbps copper interface.
50000sr
50Gbps SFI interface.
5000auto
5Gbps full-duplex.
sgmii-auto
Auto-negotiation in SGMII mode.
stacking-port
Stacking port. Read-only.
integer
Minimum value:
0 Maximum
value: 1
0
status
Switch port admin status: up or
down.
option
-up
Option
Description
up
Set admin status up.
down
Set admin status down.
FortiOS 8.0.0 CLI Reference
1389
Fortinet Inc.

<!-- 来源页 1390 -->
Parameter
Description
Type
Size
Default
sticky-mac
Enable or disable sticky-mac on
the interface.
option
-disable
Option
Description
enable
Enable sticky mac on the interface.
disable
Disable sticky mac on the interface.
storm-control-policy
Switch controller storm control
policy from available options.
string
Maximum
length: 63
default
stp-bpdu-guard
Enable/disable STP BPDU guard
on this interface.
option
-disabled
Option
Description
enabled
Enable STP BPDU guard on this interface.
disabled
Disable STP BPDU guard on this interface.
stp-bpdu-guard-timeout
BPDU Guard disabling protection
(0 - 120 min).
integer
Minimum value:
0 Maximum
value: 120
5
stp-root-guard
Enable/disable STP root guard on
this interface.
option
-disabled
Option
Description
enabled
Enable STP root-guard on this interface.
disabled
Disable STP root-guard on this interface.
stp-state
Enable/disable Spanning Tree
Protocol (STP) on this interface.
option
-enabled
Option
Description
enabled
Enable STP on this interface.
disabled
Disable STP on this interface.
switch-id
Switch id. Read-only.
string
Maximum
length: 35
type
Interface type: physical or trunk
port.
option
-physical
Option
Description
physical
Physical port.
trunk
Trunk port.
FortiOS 8.0.0 CLI Reference
1390
Fortinet Inc.

<!-- 来源页 1391 -->
Parameter
Description
Type
Size
Default
untagged-vlans
<vlan-name>
Configure switch port untagged
VLANs.
VLAN name.
string
Maximum
length: 79
vlan
Assign switch ports to a VLAN.
string
Maximum
length: 15
* This parameter may not exist in some models.
config dhcp-snoop-option82-override
Parameter
Description
Type
Size
Default
circuit-id
Circuit ID string.
string
Maximum
length: 254
remote-id
Remote ID string.
string
Maximum
length: 254
vlan-name
DHCP snooping option 82 VLAN.
string
Maximum
length: 15
config remote-log
Parameter
Description
Type
Size
Default
csv
Enable/disable comma-separated value (CSV)
strings.
option
-disable
Option
Description
enable
Enable comma-separated value (CSV) strings.
disable
Disable comma-separated value (CSV) strings.
facility
Facility to log to remote syslog server.
option
-local7
Option
Description
kernel
Kernel messages.
user
Random user-level messages.
mail
Mail system.
daemon
System daemons.
auth
Security/authorization messages.
syslog
Messages generated internally by syslogd.
lpr
Line printer subsystem.
FortiOS 8.0.0 CLI Reference
1391
Fortinet Inc.

<!-- 来源页 1392 -->
Parameter
Description
Type
Size
Default
Option
Description
news
Network news subsystem.
uucp
UUCP server messages.
cron
Clock daemon.
authpriv
Security/authorization messages (private).
ftp
FTP daemon.
ntp
NTP daemon.
audit
Log audit.
alert
Log alert.
clock
Clock daemon.
local0
Reserved for local use.
local1
Reserved for local use.
local2
Reserved for local use.
local3
Reserved for local use.
local4
Reserved for local use.
local5
Reserved for local use.
local6
Reserved for local use.
local7
Reserved for local use.
name
Remote log name.
string
Maximum
length: 35
port
Remote syslog server listening port.
integer
Minimum
value: 0
Maximum
value:
65535
514
server
IPv4 address of the remote syslog server.
string
Maximum
length: 63
severity
Severity of logs to be transferred to remote log
server.
option
-information
Option
Description
emergency
Emergency level.
alert
Alert level.
FortiOS 8.0.0 CLI Reference
1392
Fortinet Inc.

<!-- 来源页 1393 -->
Parameter
Description
Type
Size
Default
Option
Description
critical
Critical level.
error
Error level.
warning
Warning level.
notification
Notification level.
information
Information level.
debug
Debug level.
status
Enable/disable logging by FortiSwitch device to a
remote syslog server.
option
-disable
Option
Description
enable
Enable logging by FortiSwitch device to a remote syslog server.
disable
Disable logging by FortiSwitch device to a remote syslog server.
config route-offload-router
Parameter
Description
Type
Size
Default
router-ip
Router IP address.
ipv4-address
Not
Specified
0.0.0.0
vlan-name
VLAN name.
string
Maximum
length: 15
config router-static
Parameter
Description
Type
Size
Default
blackhole
Enable/disable blackhole on this route.
option
-disable
Option
Description
disable
Disable blackhole on this route.
enable
Enable blackhole on this route.
comment
Comment.
string
Maximum
length: 63
device
Gateway out interface.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
1393
Fortinet Inc.

<!-- 来源页 1394 -->
Parameter
Description
Type
Size
Default
distance
Administrative distance for the route (1 - 255,
default = 10).
integer
Minimum value:
1 Maximum
value: 255
10
dst
Destination ip and mask for this route.
ipv4-classnet
Not Specified
0.0.0.0
0.0.0.0
dynamic-gateway
Enable/disable dynamic gateway.
option
-disable
Option
Description
disable
Disable dynamic gateway on this route.
enable
Disable dynamic gateway on this route.
gateway
Gateway ip for this route.
ipv4-address
Not Specified
0.0.0.0
id
Entry sequence number.
integer
Minimum value:
0 Maximum
value:
4294967295
0
status
Enable/disable route status.
option
-enable
Option
Description
disable
Disable route status.
enable
Enable route status.
switch-id
Switch ID.
string
Maximum
length: 35
vrf
VRF for this route.
string
Maximum
length: 35
config router-vrf
Parameter
Description
Type
Size
Default
name
VRF entry name.
string
Maximum
length: 35
switch-id
Switch ID.
string
Maximum
length: 35
vrfid
VRF ID.
integer
Minimum
value: 0
Maximum
value: 1023
0
FortiOS 8.0.0 CLI Reference
1394
Fortinet Inc.

<!-- 来源页 1395 -->
config snmp-community
Parameter
Description
Type
Size
Default
events
SNMP notifications (traps) to send.
option
-cpu-high
mem-low
log-full intf-ip ent-conf-change
l2mac
Option
Description
cpu-high
Send a trap when CPU usage too high.
mem-low
Send a trap when available memory is low.
log-full
Send a trap when log disk space becomes low.
intf-ip
Send a trap when an interface IP address is changed.
ent-conf-change
Send a trap when an entity MIB change occurs (RFC4133).
l2mac
Send a trap for Learning event (add/delete/movefrom/moveto).
id
SNMP community ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
name
SNMP community name.
string
Maximum
length: 35
query-v1-port
SNMP v1 query port (default = 161).
integer
Minimum value:
0 Maximum
value: 65535
161
query-v1-status
Enable/disable SNMP v1 queries.
option
-enable
Option
Description
disable
Disable SNMP v1 queries.
enable
Enable SNMP v1 queries.
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
1395
Fortinet Inc.

<!-- 来源页 1396 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable SNMP v2c queries.
enable
Enable SNMP v2c queries.
status
Enable/disable this SNMP community.
option
-enable
Option
Description
disable
Disable SNMP community.
enable
Enable SNMP community.
trap-v1-lport
SNMP v2c trap local port (default = 162).
integer
Minimum value:
0 Maximum
value: 65535
162
trap-v1-rport
SNMP v2c trap remote port (default = 162).
integer
Minimum value:
0 Maximum
value: 65535
162
trap-v1-status
Enable/disable SNMP v1 traps.
option
-enable
Option
Description
disable
Disable SNMP v1 traps.
enable
Enable SNMP v1 traps.
trap-v2c-lport
SNMP v2c trap local port (default = 162).
integer
Minimum value:
0 Maximum
value: 65535
162
trap-v2c-rport
SNMP v2c trap remote port (default = 162).
integer
Minimum value:
0 Maximum
value: 65535
162
trap-v2c-status
Enable/disable SNMP v2c traps.
option
-enable
Option
Description
disable
Disable SNMP v2c traps.
enable
Enable SNMP v2c traps.
FortiOS 8.0.0 CLI Reference
1396
Fortinet Inc.

<!-- 来源页 1397 -->
config hosts
Parameter
Description
Type
Size
Default
id
Host entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
ip
IPv4 address of the SNMP manager (host).
user
Not Specified
config snmp-sysinfo
Parameter
Description
Type
Size
Default
contact-info
Contact information.
string
Maximum
length: 35
description
System description.
string
Maximum
length: 35
engine-id
Local SNMP engine ID string (max 24 char).
string
Maximum
length: 24
location
System location.
string
Maximum
length: 35
status
Enable/disable SNMP.
option
-disable
Option
Description
disable
Disable SNMP.
enable
Enable SNMP.
config snmp-trap-threshold
Parameter
Description
Type
Size
Default
trap-high-cpu-threshold
CPU usage when trap is sent.
integer
Minimum value:
0 Maximum
value:
4294967295
80
trap-log-full-threshold
Log disk usage when trap is sent.
integer
Minimum value:
0 Maximum
value:
4294967295
90
trap-low-memory-threshold
Memory usage when trap is sent.
integer
Minimum value:
0 Maximum
value:
4294967295
80
FortiOS 8.0.0 CLI Reference
1397
Fortinet Inc.

<!-- 来源页 1398 -->
config snmp-user
Parameter
Description
Type
Size
Default
auth-proto
Authentication protocol.
option
-sha256
Option
Description
md5
HMAC-MD5-96 authentication protocol.
sha1
HMAC-SHA-1 authentication protocol.
sha224
HMAC-SHA-224 authentication protocol.
sha256
HMAC-SHA-256 authentication protocol.
sha384
HMAC-SHA-384 authentication protocol.
sha512
HMAC-SHA-512 authentication protocol.
auth-pwd
Password for authentication protocol.
password
Not
Specified
name
SNMP user name.
string
Maximum
length: 32
priv-proto
Privacy (encryption) protocol.
option
-aes128
Option
Description
aes128
CFB128-AES-128 symmetric encryption protocol.
aes192
CFB128-AES-192 symmetric encryption protocol.
aes192c
CFB128-AES-192-C symmetric encryption protocol.
aes256
CFB128-AES-256 symmetric encryption protocol.
aes256c
CFB128-AES-256-C symmetric encryption protocol.
des
CBC-DES symmetric encryption protocol.
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
disable
Disable SNMP queries for this user.
enable
Enable SNMP queries for this user.
query-port
SNMPv3 query port (default = 161).
integer
Minimum
value: 0
Maximum
value:
65535
161
FortiOS 8.0.0 CLI Reference
1398
Fortinet Inc.

<!-- 来源页 1399 -->
Parameter
Description
Type
Size
Default
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
config static-mac
Parameter
Description
Type
Size
Default
description
Description.
string
Maximum
length: 63
id
ID.
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
length: 35
mac
MAC address.
mac-address
Not Specified
00:00:00:00:00:00
type
Type.
option
-static
Option
Description
static
Static MAC.
sticky
Sticky MAC.
vlan
Vlan.
string
Maximum
length: 15
config storm-control
Parameter
Description
Type
Size
Default
broadcast
Enable/disable storm control to drop broadcast
traffic.
option
-disable
Option
Description
enable
Drop broadcast traffic.
disable
Allow broadcast traffic.
FortiOS 8.0.0 CLI Reference
1399
Fortinet Inc.

<!-- 来源页 1400 -->
Parameter
Description
Type
Size
Default
burst-size-level
Increase level to handle bursty traffic (0 - 4,
default = 0).
integer
Minimum
value: 0
Maximum
value: 4
0
local-override
Enable to override global FortiSwitch storm control
settings for this FortiSwitch.
option
-disable
Option
Description
enable
Override global storm control settings.
disable
Use global storm control settings.
rate
Rate in packets per second at which storm control
drops excess traffic(0-10000000, default=500,
drop-all=0).
integer
Minimum
value: 0
Maximum
value:
10000000
500
unknown-multicast
Enable/disable storm control to drop unknown
multicast traffic.
option
-disable
Option
Description
enable
Drop unknown multicast traffic.
disable
Allow unknown multicast traffic.
unknown-unicast
Enable/disable storm control to drop unknown
unicast traffic.
option
-disable
Option
Description
enable
Drop unknown unicast traffic.
disable
Allow unknown unicast traffic.
config stp-instance
Parameter
Description
Type
Size
Default
id
Instance ID.
string
Maximum length:
2
priority
Priority.
option
-32768
Option
Description
0
0.
FortiOS 8.0.0 CLI Reference
1400
Fortinet Inc.

<!-- 来源页 1401 -->
Parameter
Description
Type
Size
Default
Option
Description
4096
4096.
8192
8192.
12288
12288.
16384
16384.
20480
20480.
24576
24576.
28672
28672.
32768
32768.
36864
36864.
40960
40960.
45056
45056.
49152
49152.
53248
53248.
57344
57344.
61440
61440.
config stp-settings
Parameter
Description
Type
Size
Default
forward-time
Period of time a port is in listening and learning
state (4 - 30 sec, default = 15).
integer
Minimum
value: 4
Maximum
value: 30
15
hello-time
Period of time between successive STP frame
Bridge Protocol Data Units (BPDUs) sent on a port
(1 - 10 sec, default = 2).
integer
Minimum
value: 1
Maximum
value: 10
2
local-override
Enable to configure local STP settings that override
global STP settings.
option
-disable
Option
Description
enable
Override global STP settings.
disable
Use global STP settings.
FortiOS 8.0.0 CLI Reference
1401
Fortinet Inc.

<!-- 来源页 1402 -->
Parameter
Description
Type
Size
Default
max-age
Maximum time before a bridge port saves its
configuration BPDU information (6 - 40 sec, default
= 20).
integer
Minimum
value: 6
Maximum
value: 40
20
max-hops
Maximum number of hops between the root bridge
and the furthest bridge (1- 40, default = 20).
integer
Minimum
value: 1
Maximum
value: 40
20
name
Name of local STP settings configuration.
string
Maximum
length: 31
pending-timer
Pending time (1 - 15 sec, default = 4).
integer
Minimum
value: 1
Maximum
value: 15
4
revision
STP revision number (0 - 65535).
integer
Minimum
value: 0
Maximum
value:
65535
0
config switch-log
Parameter
Description
Type
Size
Default
local-override
Enable to configure local logging settings that
override global logging settings.
option
-disable
Option
Description
enable
Override global logging settings.
disable
Use global logging settings.
severity
Severity of FortiSwitch logs that are added to the
FortiGate event log.
option
-notification
Option
Description
emergency
Emergency level.
alert
Alert level.
critical
Critical level.
error
Error level.
warning
Warning level.
FortiOS 8.0.0 CLI Reference
1402
Fortinet Inc.

<!-- 来源页 1403 -->
Parameter
Description
Type
Size
Default
Option
Description
notification
Notification level.
information
Information level.
debug
Debug level.
status
Enable/disable adding FortiSwitch logs to the
FortiGate event log.
option
-enable
Option
Description
enable
Add FortiSwitch logs to the FortiGate event log.
disable
Do not add FortiSwitch logs to the FortiGate event log.
config system-dhcp-server
Parameter
Description
Type
Size
Default
default-gateway
Default gateway IP address assigned by the
DHCP server.
ipv4-address
Not Specified
0.0.0.0
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
FortiOS 8.0.0 CLI Reference
1403
Fortinet Inc.

<!-- 来源页 1404 -->
Parameter
Description
Type
Size
Default
lease-time
Lease time in seconds, 0 means unlimited.
integer
Minimum value:
0 Maximum
value:
4294967295
604800
netmask
Netmask assigned by the DHCP server.
ipv4-netmask
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
Option
Description
local
IP address of the interface the DHCP server is added to becomes the
client's NTP server IP address.
default
Clients are assigned the FortiGate's configured NTP servers.
specify
Specify up to 3 NTP servers in the DHCP server configuration.
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
switch-id
Switch ID.
string
Maximum
length: 35
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
start-ip
Start of IP range.
ipv4-address
Not Specified
0.0.0.0
FortiOS 8.0.0 CLI Reference
1404
Fortinet Inc.

<!-- 来源页 1405 -->
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
value
DHCP option value.
string
Maximum
length: 312
config system-interface
Parameter
Description
Type
Size
Default
allowaccess
Permitted types of management access to this
interface.
option
-Option
Description
ping
PING.
https
HTTPS.
http
HTTP.
ssh
SSH.
snmp
SNMP.
telnet
TELNET.
radius-acct
RADIUS ACCOUNTING.
interface
Interface name.
string
Maximum
length: 63
FortiOS 8.0.0 CLI Reference
1405
Fortinet Inc.

<!-- 来源页 1406 -->
Parameter
Description
Type
Size
Default
ip
IP and mask for this interface.
ipv4-classnet-host
Not
Specified
0.0.0.0
0.0.0.0
mode
Interface addressing mode.
option
-static
Option
Description
static
static addressing mode.
dhcp
DHCP addressing mode.
name
Interface name.
string
Maximum
length: 15
status
Enable/disable interface status.
option
-enable
Option
Description
disable
Disable interface.
enable
Enable interface.
switch-id
Switch ID.
string
Maximum
length: 35
type
Interface type.
option
-vlan
Option
Description
vlan
VLAN interface.
physical
Physical interface.
vlan
VLAN name.
string
Maximum
length: 15
vrf
VRF for this route.
string
Maximum
length: 63
config vlan
Parameter
Description
Type
Size
Default
assignment-priority
802.1x Radius (Tunnel-Private-Group-Id) VLANID
assign-by-name priority. A smaller value has a
higher priority.
integer
Minimum
value: 1
Maximum
value: 255
128
vlan-name
VLAN name.
string
Maximum
length: 15
FortiOS 8.0.0 CLI Reference
1406
Fortinet Inc.

<!-- 来源页 1407 -->
config switch-controller network-monitor-settings
Configure network monitor settings.
config switch-controller network-monitor-settings
Description: Configure network monitor settings.
set network-monitoring [enable|disable]
end
config switch-controller network-monitor-settings
Parameter
Description
Type
Size
Default
network-monitoring
Enable/disable passive gathering of information by
FortiSwitch units concerning other network
devices.
option
-disable
Option
Description
enable
Enable network monitoring on FortiSwitch.
disable
Disable network monitoring on FortiSwitch.
config switch-controller ptp interface-policy
PTP interface-policy configuration.
config switch-controller ptp interface-policy
Description: PTP interface-policy configuration.
edit <name>
set description {string}
set vlan {string}
set vlan-pri {integer}
next
end
config switch-controller ptp interface-policy
Parameter
Description
Type
Size
Default
description
Description.
string
Maximum
length: 63
name
Policy name.
string
Maximum
length: 63
FortiOS 8.0.0 CLI Reference
1407
Fortinet Inc.

<!-- 来源页 1408 -->
Parameter
Description
Type
Size
Default
vlan
PTP VLAN.
string
Maximum
length: 15
vlan-pri
Configure PTP VLAN priority (0 - 7, default = 4).
integer
Minimum
value: 0
Maximum
value: 7
4
config switch-controller ptp profile
Global PTP profile.
config switch-controller ptp profile
Description: Global PTP profile.
edit <name>
set description {string}
set domain {integer}
set mode [transparent-e2e|transparent-p2p]
set pdelay-req-interval [1sec|2sec|...]
set ptp-profile {option}
set transport {option}
next
end
config switch-controller ptp profile
Parameter
Description
Type
Size
Default
description
Description.
string
Maximum
length: 63
domain
Configure PTP domain value (0 - 255, default =
254).
integer
Minimum
value: 0
Maximum
value: 255
254
mode
Select PTP mode.
option
-transparent-e2e
Option
Description
transparent-e2e
End-to-end transparent clock.
transparent-p2p
Peer-to-peer transparent clock.
FortiOS 8.0.0 CLI Reference
1408
Fortinet Inc.

<!-- 来源页 1409 -->
Parameter
Description
Type
Size
Default
name
Profile name.
string
Maximum
length: 63
pdelay-req-interval
Configure PTP peer delay request interval.
option
-1sec
Option
Description
1sec
1 sec.
2sec
2 sec.
4sec
4 sec.
8sec
8 sec.
16sec
16 sec.
32sec
32 sec.
ptp-profile
Configure PTP power profile.
option
-C37.238-2017
Option
Description
C37.238-2017
C37.238-2017 power profile.
transport
Configure PTP transport mode.
option
-l2-mcast
Option
Description
l2-mcast
L2 multicast.
config switch-controller qos dot1p-map
Configure FortiSwitch QoS 802.1p.
config switch-controller qos dot1p-map
Description: Configure FortiSwitch QoS 802.1p.
edit <name>
set description {string}
set egress-pri-tagging [disable|enable]
set priority-0 [queue-0|queue-1|...]
set priority-1 [queue-0|queue-1|...]
set priority-2 [queue-0|queue-1|...]
set priority-3 [queue-0|queue-1|...]
set priority-4 [queue-0|queue-1|...]
set priority-5 [queue-0|queue-1|...]
set priority-6 [queue-0|queue-1|...]
set priority-7 [queue-0|queue-1|...]
next
end
FortiOS 8.0.0 CLI Reference
1409
Fortinet Inc.

<!-- 来源页 1410 -->
config switch-controller qos dot1p-map
Parameter
Description
Type
Size
Default
description
Description of the 802.1p name.
string
Maximum
length: 63
egress-pri-tagging
Enable/disable egress priority-tag frame.
option
-disable
Option
Description
disable
Disable egress priority tagging.
enable
Enable egress priority tagging.
name
Dot1p map name.
string
Maximum
length: 63
priority-0
COS queue mapped to dot1p priority number.
option
-queue-0
Option
Description
queue-0
COS queue 0 (lowest priority).
queue-1
COS queue 1.
queue-2
COS queue 2.
queue-3
COS queue 3.
queue-4
COS queue 4.
queue-5
COS queue 5.
queue-6
COS queue 6.
queue-7
COS queue 7 (highest priority).
priority-1
COS queue mapped to dot1p priority number.
option
-queue-0
Option
Description
queue-0
COS queue 0 (lowest priority).
queue-1
COS queue 1.
queue-2
COS queue 2.
queue-3
COS queue 3.
queue-4
COS queue 4.
queue-5
COS queue 5.
queue-6
COS queue 6.
queue-7
COS queue 7 (highest priority).
FortiOS 8.0.0 CLI Reference
1410
Fortinet Inc.

<!-- 来源页 1411 -->
Parameter
Description
Type
Size
Default
priority-2
COS queue mapped to dot1p priority number.
option
-queue-0
Option
Description
queue-0
COS queue 0 (lowest priority).
queue-1
COS queue 1.
queue-2
COS queue 2.
queue-3
COS queue 3.
queue-4
COS queue 4.
queue-5
COS queue 5.
queue-6
COS queue 6.
queue-7
COS queue 7 (highest priority).
priority-3
COS queue mapped to dot1p priority number.
option
-queue-0
Option
Description
queue-0
COS queue 0 (lowest priority).
queue-1
COS queue 1.
queue-2
COS queue 2.
queue-3
COS queue 3.
queue-4
COS queue 4.
queue-5
COS queue 5.
queue-6
COS queue 6.
queue-7
COS queue 7 (highest priority).
priority-4
COS queue mapped to dot1p priority number.
option
-queue-0
Option
Description
queue-0
COS queue 0 (lowest priority).
queue-1
COS queue 1.
queue-2
COS queue 2.
queue-3
COS queue 3.
queue-4
COS queue 4.
queue-5
COS queue 5.
queue-6
COS queue 6.
FortiOS 8.0.0 CLI Reference
1411
Fortinet Inc.

<!-- 来源页 1412 -->
Parameter
Description
Type
Size
Default
Option
Description
queue-7
COS queue 7 (highest priority).
priority-5
COS queue mapped to dot1p priority number.
option
-queue-0
Option
Description
queue-0
COS queue 0 (lowest priority).
queue-1
COS queue 1.
queue-2
COS queue 2.
queue-3
COS queue 3.
queue-4
COS queue 4.
queue-5
COS queue 5.
queue-6
COS queue 6.
queue-7
COS queue 7 (highest priority).
priority-6
COS queue mapped to dot1p priority number.
option
-queue-0
Option
Description
queue-0
COS queue 0 (lowest priority).
queue-1
COS queue 1.
queue-2
COS queue 2.
queue-3
COS queue 3.
queue-4
COS queue 4.
queue-5
COS queue 5.
queue-6
COS queue 6.
queue-7
COS queue 7 (highest priority).
priority-7
COS queue mapped to dot1p priority number.
option
-queue-0
Option
Description
queue-0
COS queue 0 (lowest priority).
queue-1
COS queue 1.
queue-2
COS queue 2.
queue-3
COS queue 3.
FortiOS 8.0.0 CLI Reference
1412
Fortinet Inc.

<!-- 来源页 1413 -->
Parameter
Description
Type
Size
Default
Option
Description
queue-4
COS queue 4.
queue-5
COS queue 5.
queue-6
COS queue 6.
queue-7
COS queue 7 (highest priority).
config switch-controller qos ip-dscp-map
Configure FortiSwitch QoS IP precedence/DSCP.
config switch-controller qos ip-dscp-map
Description: Configure FortiSwitch QoS IP precedence/DSCP.
edit <name>
set description {string}
config map
Description: Maps between IP-DSCP value to COS queue.
edit <name>
set cos-queue {integer}
set diffserv {option1}, {option2}, ...
set ip-precedence {option1}, {option2}, ...
set value {user}
next
end
next
end
config switch-controller qos ip-dscp-map
Parameter
Description
Type
Size
Default
description
Description of the ip-dscp map name.
string
Maximum
length: 63
name
Dscp map name.
string
Maximum
length: 63
FortiOS 8.0.0 CLI Reference
1413
Fortinet Inc.

<!-- 来源页 1414 -->
config map
Parameter
Description
Type
Size
Default
cos-queue
COS queue number.
integer
Minimum
value: 0
Maximum
value: 7
0
diffserv
Differentiated service.
option
-Option
Description
CS0
DSCP CS0.
CS1
DSCP CS1.
AF11
DSCP AF11.
AF12
DSCP AF12.
AF13
DSCP AF13.
CS2
DSCP CS2.
AF21
DSCP AF21.
AF22
DSCP AF22.
AF23
DSCP AF23.
CS3
DSCP CS3.
AF31
DSCP AF31.
AF32
DSCP AF32.
AF33
DSCP AF33.
CS4
DSCP CS4.
AF41
DSCP AF41.
AF42
DSCP AF42.
AF43
DSCP AF43.
CS5
DSCP CS5.
EF
DSCP EF.
CS6
DSCP CS6.
CS7
DSCP CS7.
ip-precedence
IP Precedence.
option
-FortiOS 8.0.0 CLI Reference
1414
Fortinet Inc.

<!-- 来源页 1415 -->
Parameter
Description
Type
Size
Default
Option
Description
network-control
Network control.
internetwork-control
Internetwork control.
critic-ecp
Critic ECP.
flashoverride
Flash override.
flash
Flash.
immediate
Immediate.
priority
Priority.
routine
Routine.
name
Dscp mapping entry name.
string
Maximum
length: 63
value
Raw values of DSCP (0 - 63).
user
Not
Specified
config switch-controller qos qos-policy
Configure FortiSwitch QoS policy.
config switch-controller qos qos-policy
Description: Configure FortiSwitch QoS policy.
edit <name>
set default-cos {integer}
set queue-policy {string}
set trust-dot1p-map {string}
set trust-ip-dscp-map {string}
next
end
config switch-controller qos qos-policy
Parameter
Description
Type
Size
Default
default-cos
Default cos queue for untagged packets.
integer
Minimum
value: 0
Maximum
value: 7
0
FortiOS 8.0.0 CLI Reference
1415
Fortinet Inc.

<!-- 来源页 1416 -->
Parameter
Description
Type
Size
Default
name
QoS policy name.
string
Maximum
length: 63
queue-policy
QoS egress queue policy.
string
Maximum
length: 63
default
trust-dot1p-map
QoS trust 802.1p map.
string
Maximum
length: 63
trust-ip-dscp-map
QoS trust ip dscp map.
string
Maximum
length: 63
config switch-controller qos queue-policy
Configure FortiSwitch QoS egress queue policy.
config switch-controller qos queue-policy
Description: Configure FortiSwitch QoS egress queue policy.
edit <name>
config cos-queue
Description: COS queue configuration.
edit <name>
set description {string}
set drop-policy [taildrop|weighted-random-early-detection]
set ecn [disable|enable]
set max-rate {integer}
set max-rate-percent {integer}
set min-rate {integer}
set min-rate-percent {integer}
set weight {integer}
next
end
set rate-by [kbps|percent]
set schedule [strict|round-robin|...]
next
end
config switch-controller qos queue-policy
Parameter
Description
Type
Size
Default
name
QoS policy name.
string
Maximum
length: 63
rate-by
COS queue rate by kbps or percent.
option
-kbps
FortiOS 8.0.0 CLI Reference
1416
Fortinet Inc.

<!-- 来源页 1417 -->
Parameter
Description
Type
Size
Default
Option
Description
kbps
Rate by kbps.
percent
Rate by percent.
schedule
COS queue scheduling.
option
-round-robin
Option
Description
strict
Strict scheduling (queue7: highest priority, queue0: lowest priority).
round-robin
Round robin scheduling.
weighted
Weighted round robin scheduling.
config cos-queue
Parameter
Description
Type
Size
Default
description
Description of the COS queue.
string
Maximum
length: 63
drop-policy
COS queue drop policy.
option
-taildrop
Option
Description
taildrop
Taildrop policy.
weighted-random-early-detection
Weighted random early detection drop policy.
ecn
Enable/disable ECN packet marking to drop
eligible packets.
option
-disable
Option
Description
disable
Disable ECN packet marking to drop eligible packets.
enable
Enable ECN packet marking to drop eligible packets.
max-rate
Maximum rate (0 - 4294967295 kbps, 0 to
disable).
integer
Minimum value:
0 Maximum
value:
4294967295
0
max-rate-percent
Maximum rate (% of link speed).
integer
Minimum value:
0 Maximum
value:
4294967295
0
FortiOS 8.0.0 CLI Reference
1417
Fortinet Inc.

<!-- 来源页 1418 -->
Parameter
Description
Type
Size
Default
min-rate
Minimum rate (0 - 4294967295 kbps, 0 to
disable).
integer
Minimum value:
0 Maximum
value:
4294967295
0
min-rate-percent
Minimum rate (% of link speed).
integer
Minimum value:
0 Maximum
value:
4294967295
0
name
Cos queue ID.
string
Maximum
length: 63
weight
Weight of weighted round robin scheduling.
integer
Minimum value:
0 Maximum
value:
4294967295
1
config switch-controller quarantine
Configure FortiSwitch quarantine support.
config switch-controller quarantine
Description: Configure FortiSwitch quarantine support.
set quarantine [enable|disable]
config targets
Description: Quarantine MACs.
edit <mac>
set description {string}
set tag <tags1>, <tags2>, ...
next
end
end
config switch-controller quarantine
Parameter
Description
Type
Size
Default
quarantine
Enable/disable quarantine.
option
-disable
Option
Description
enable
Enable quarantine.
disable
Disable quarantine.
FortiOS 8.0.0 CLI Reference
1418
Fortinet Inc.

<!-- 来源页 1419 -->
config targets
Parameter
Description
Type
Size
Default
description
Description for the quarantine MAC.
string
Maximum
length: 63
mac
Quarantine MAC.
mac-address
Not
Specified
00:00:00:00:00:00
tag <tags>
Tags for the quarantine MAC.
Tag string. For example, string1 string2
string3.
string
Maximum
length: 63
config switch-controller remote-log
Configure logging by FortiSwitch device to a remote syslog server.
config switch-controller remote-log
Description: Configure logging by FortiSwitch device to a remote syslog server.
edit <name>
set csv [enable|disable]
set facility [kernel|user|...]
set port {integer}
set server {string}
set severity [emergency|alert|...]
set status [enable|disable]
next
end
config switch-controller remote-log
Parameter
Description
Type
Size
Default
csv
Enable/disable comma-separated value (CSV)
strings.
option
-disable
Option
Description
enable
Enable comma-separated value (CSV) strings.
disable
Disable comma-separated value (CSV) strings.
facility
Facility to log to remote syslog server.
option
-local7
Option
Description
kernel
Kernel messages.
FortiOS 8.0.0 CLI Reference
1419
Fortinet Inc.

<!-- 来源页 1420 -->
Parameter
Description
Type
Size
Default
Option
Description
user
Random user-level messages.
mail
Mail system.
daemon
System daemons.
auth
Security/authorization messages.
syslog
Messages generated internally by syslogd.
lpr
Line printer subsystem.
news
Network news subsystem.
uucp
UUCP server messages.
cron
Clock daemon.
authpriv
Security/authorization messages (private).
ftp
FTP daemon.
ntp
NTP daemon.
audit
Log audit.
alert
Log alert.
clock
Clock daemon.
local0
Reserved for local use.
local1
Reserved for local use.
local2
Reserved for local use.
local3
Reserved for local use.
local4
Reserved for local use.
local5
Reserved for local use.
local6
Reserved for local use.
local7
Reserved for local use.
name
Remote log name.
string
Maximum
length: 35
port
Remote syslog server listening port.
integer
Minimum
value: 0
Maximum
value:
65535
514
FortiOS 8.0.0 CLI Reference
1420
Fortinet Inc.

<!-- 来源页 1421 -->
Parameter
Description
Type
Size
Default
server
IPv4 address of the remote syslog server.
string
Maximum
length: 63
severity
Severity of logs to be transferred to remote log
server.
option
-information
Option
Description
emergency
Emergency level.
alert
Alert level.
critical
Critical level.
error
Error level.
warning
Warning level.
notification
Notification level.
information
Information level.
debug
Debug level.
status
Enable/disable logging by FortiSwitch device to a
remote syslog server.
option
-disable
Option
Description
enable
Enable logging by FortiSwitch device to a remote syslog server.
disable
Disable logging by FortiSwitch device to a remote syslog server.
config switch-controller security-policy 802-1X
Configure 802.1x MAC Authentication Bypass (MAB) policies.
config switch-controller security-policy 802-1X
Description: Configure 802.1x MAC Authentication Bypass (MAB) policies.
edit <name>
set allow-mac-move [disable|enable]
set auth-fail-vlan [disable|enable]
set auth-fail-vlan-id {string}
set auth-order [dot1x-mab|mab-dot1x|...]
set auth-priority [legacy|dot1x-mab|...]
set authserver-timeout-period {integer}
set authserver-timeout-tagged [disable|lldp-voice|...]
set authserver-timeout-tagged-vlanid {string}
set authserver-timeout-vlan [disable|enable]
set authserver-timeout-vlanid {string}
set client-limit {integer}
set dacl [disable|enable]
FortiOS 8.0.0 CLI Reference
1421
Fortinet Inc.

<!-- 来源页 1422 -->
set eap-auto-untagged-vlans [disable|enable]
set eap-egress-tagged [disable|enable]
set eap-passthru [disable|enable]
set framevid-apply [disable|enable]
set guest-auth-delay {integer}
set guest-vlan [disable|enable]
set guest-vlan-id {string}
set mac-auth-bypass [disable|enable]
set open-auth [disable|enable]
set policy-type {option}
set radius-timeout-overwrite [disable|enable]
set security-mode [802.1X|802.1X-mac-based]
set user-group <name1>, <name2>, ...
next
end
config switch-controller security-policy 802-1X
Parameter
Description
Type
Size
Default
allow-mac-move *
Enable/disable MAC move (default = enable).
option
-enable
Option
Description
disable
Disable MAC move.
enable
Enable MAC move.
auth-fail-vlan
Enable to allow limited access to clients that
cannot authenticate.
option
-disable
Option
Description
disable
Disable authentication fail VLAN on this interface.
enable
Enable authentication fail VLAN on this interface.
auth-fail-vlan-id
VLAN ID on which authentication failed.
string
Maximum
length: 15
auth-order
Configure authentication order.
option
-mab-dot1x
Option
Description
dot1x-mab
Use EAP 1X authentication first then MAB.
mab-dot1x
Use MAB authentication first then EAP 1X.
mab
Use MAB authentication only.
auth-priority
Configure authentication priority.
option
-legacy
FortiOS 8.0.0 CLI Reference
1422
Fortinet Inc.

<!-- 来源页 1423 -->
Parameter
Description
Type
Size
Default
Option
Description
legacy
EAP 1X authentication has a higher priority than MAB with the legacy
implementation.
dot1x-mab
EAP 1X authentication has a higher priority than MAB.
mab-dot1x
MAB authentication has a higher priority than EAP 1X.
authserver-timeout-period
Authentication server timeout period (3 - 15 sec,
default = 3).
integer
Minimum
value: 3
Maximum
value: 15
3
authserver-timeout-tagged
Configure timeout option for the tagged VLAN
which allows limited access when the
authentication server is unavailable.
option
-disable
Option
Description
disable
Disable authentication server timeout on this interface.
lldp-voice
LLDP voice timeout for the tagged VLAN on this interface.
static
Static timeout for the tagged VLAN on this interface.
authserver-timeout-tagged-vlanid
Tagged VLAN name for which the timeout option is
applied to (only one VLAN ID).
string
Maximum
length: 15
authserver-timeout-vlan
Enable/disable the authentication server timeout
VLAN to allow limited access when RADIUS is
unavailable.
option
-disable
Option
Description
disable
Disable authentication server timeout VLAN on this interface.
enable
Enable authentication server timeout VLAN on this interface.
authserver-timeout-vlanid
Authentication server timeout VLAN name.
string
Maximum
length: 15
client-limit *
Configure the maximum number of endpoint
devices this FortiGate unit will accept while
configured in MAC mode.
integer
Minimum
value: 2
Maximum
value: 20
20
dacl
Enable/disable dynamic access control list on this
interface.
option
-disable
FortiOS 8.0.0 CLI Reference
1423
Fortinet Inc.

<!-- 来源页 1424 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable dynamic access control list on this interface.
enable
Enable dynamic access control on this interface.
eap-auto-untagged-vlans
Enable/disable automatic inclusion of untagged
VLANs.
option
-enable
Option
Description
disable
Disable automatic inclusion of untagged VLANs.
enable
Enable automatic inclusion of untagged VLANs.
eap-egress-tagged *
Enable/disable egress frame tag (default =
disable).
option
-disable
Option
Description
disable
Disable egress frame tag.
enable
Enable egress frame tag.
eap-passthru
Enable/disable EAP pass-through mode, allowing
protocols (such as LLDP) to pass through ports for
more flexible authentication.
option
-enable
Option
Description
disable
Disable EAP pass-through mode on this interface.
enable
Enable EAP pass-through mode on this interface.
framevid-apply
Enable/disable the capability to apply the
EAP/MAB frame VLAN to the port native VLAN.
option
-enable
Option
Description
disable
Disable the capability to apply the EAP/MAB frame VLAN to the port
native VLAN.
enable
Enable the capability to apply the EAP/MAB frame VLAN to the port
native VLAN.
guest-auth-delay
Guest authentication delay (1 - 900 sec, default =
30).
integer
Minimum
value: 1
Maximum
value: 900
30
FortiOS 8.0.0 CLI Reference
1424
Fortinet Inc.

<!-- 来源页 1425 -->
Parameter
Description
Type
Size
Default
guest-vlan
Enable the guest VLAN feature to allow limited
access to non-802.1X-compliant clients.
option
-disable
Option
Description
disable
Disable guest VLAN on this interface.
enable
Enable guest VLAN on this interface.
guest-vlan-id
Guest VLAN name.
string
Maximum
length: 15
mac-auth-bypass
Enable/disable MAB for this policy.
option
-disable
Option
Description
disable
Disable MAB.
enable
Enable MAB.
name
Policy name.
string
Maximum
length: 31
open-auth
Enable/disable open authentication for this policy.
option
-disable
Option
Description
disable
Disable open authentication.
enable
Enable open authentication.
policy-type
Policy type.
option
-802.1X
Option
Description
802.1X
802.1X security policy.
radius-timeout-overwrite
Enable to override the global RADIUS session
timeout.
option
-disable
Option
Description
disable
Override the global RADIUS session timeout.
enable
Use the global RADIUS session timeout.
security-mode
Port or MAC based 802.1X security mode.
option
-802.1X
FortiOS 8.0.0 CLI Reference
1425
Fortinet Inc.

<!-- 来源页 1426 -->
Parameter
Description
Type
Size
Default
Option
Description
802.1X
802.1X port based authentication.
802.1X-mac-based
802.1X MAC based authentication.
user-group
<name>
Name of user-group to assign to this MAC
Authentication Bypass (MAB) policy.
Group name.
string
Maximum
length: 79
* This parameter may not exist in some models.
config switch-controller security-policy admin
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
Configure fortiswitch's admin security-policy.
config switch-controller security-policy admin
Description: Configure fortiswitch's admin security-policy.
FortiOS 8.0.0 CLI Reference
1426
Fortinet Inc.

<!-- 来源页 1427 -->
edit <name>
set auto [disable|enable]
set ip6-trusthost1 {ipv6-prefix}
set ip6-trusthost10 {ipv6-prefix}
set ip6-trusthost2 {ipv6-prefix}
set ip6-trusthost3 {ipv6-prefix}
set ip6-trusthost4 {ipv6-prefix}
set ip6-trusthost5 {ipv6-prefix}
set ip6-trusthost6 {ipv6-prefix}
set ip6-trusthost7 {ipv6-prefix}
set ip6-trusthost8 {ipv6-prefix}
set ip6-trusthost9 {ipv6-prefix}
set trusthost1 {ipv4-classnet}
set trusthost10 {ipv4-classnet}
set trusthost2 {ipv4-classnet}
set trusthost3 {ipv4-classnet}
set trusthost4 {ipv4-classnet}
set trusthost5 {ipv4-classnet}
set trusthost6 {ipv4-classnet}
set trusthost7 {ipv4-classnet}
set trusthost8 {ipv4-classnet}
set trusthost9 {ipv4-classnet}
next
end
config switch-controller security-policy admin
Parameter
Description
Type
Size
Default
auto
Automatically set based on the host ip connected
via the Fortilink interface.
option
-disable
Option
Description
disable
Disable.
enable
Enable.
ip6-trusthost1
Trusted IPv6 host.
ipv6-prefix
Not
Specified
::/0
ip6-trusthost10
Trusted IPv6 host.
ipv6-prefix
Not
Specified
::/0
ip6-trusthost2
Trusted IPv6 host.
ipv6-prefix
Not
Specified
::/0
ip6-trusthost3
Trusted IPv6 host.
ipv6-prefix
Not
Specified
::/0
ip6-trusthost4
Trusted IPv6 host.
ipv6-prefix
Not
Specified
::/0
FortiOS 8.0.0 CLI Reference
1427
Fortinet Inc.

<!-- 来源页 1428 -->
Parameter
Description
Type
Size
Default
ip6-trusthost5
Trusted IPv6 host.
ipv6-prefix
Not
Specified
::/0
ip6-trusthost6
Trusted IPv6 host.
ipv6-prefix
Not
Specified
::/0
ip6-trusthost7
Trusted IPv6 host.
ipv6-prefix
Not
Specified
::/0
ip6-trusthost8
Trusted IPv6 host.
ipv6-prefix
Not
Specified
::/0
ip6-trusthost9
Trusted IPv6 host.
ipv6-prefix
Not
Specified
::/0
name
Policy name.
string
Maximum
length: 31
trusthost1
Trusted IPv4 host.
ipv4-classnet
Not
Specified
0.0.0.0
0.0.0.0
trusthost10
Trusted IPv4 host.
ipv4-classnet
Not
Specified
0.0.0.0
0.0.0.0
trusthost2
Trusted IPv4 host.
ipv4-classnet
Not
Specified
0.0.0.0
0.0.0.0
trusthost3
Trusted IPv4 host.
ipv4-classnet
Not
Specified
0.0.0.0
0.0.0.0
trusthost4
Trusted IPv4 host.
ipv4-classnet
Not
Specified
0.0.0.0
0.0.0.0
trusthost5
Trusted IPv4 host.
ipv4-classnet
Not
Specified
0.0.0.0
0.0.0.0
trusthost6
Trusted IPv4 host.
ipv4-classnet
Not
Specified
0.0.0.0
0.0.0.0
trusthost7
Trusted IPv4 host.
ipv4-classnet
Not
Specified
0.0.0.0
0.0.0.0
trusthost8
Trusted IPv4 host.
ipv4-classnet
Not
Specified
0.0.0.0
0.0.0.0
trusthost9
Trusted IPv4 host.
ipv4-classnet
Not
Specified
0.0.0.0
0.0.0.0
config switch-controller security-policy local-access
Configure allowaccess list for mgmt and internal interfaces on managed FortiSwitch units.
FortiOS 8.0.0 CLI Reference
1428
Fortinet Inc.

<!-- 来源页 1429 -->
config switch-controller security-policy local-access
Description: Configure allowaccess list for mgmt and internal interfaces on managed
FortiSwitch units.
edit <name>
set internal-allowaccess {option1}, {option2}, ...
set mgmt-allowaccess {option1}, {option2}, ...
next
end
config switch-controller security-policy local-access
Parameter
Description
Type
Size
Default
internal-allowaccess
Allowed access on the switch internal interface.
option
-https ping
ssh
Option
Description
https
HTTPS access.
ping
PING access.
ssh
SSH access.
snmp
SNMP access.
http
HTTP access.
telnet
TELNET access.
radius-acct
RADIUS accounting access.
mgmt-allowaccess
Allowed access on the switch management
interface.
option
-https ping
ssh
Option
Description
https
HTTPS access.
ping
PING access.
ssh
SSH access.
snmp
SNMP access.
http
HTTP access.
telnet
TELNET access.
radius-acct
RADIUS accounting access.
name
Policy name.
string
Maximum
length: 31
FortiOS 8.0.0 CLI Reference
1429
Fortinet Inc.

<!-- 来源页 1430 -->
config switch-controller sflow
Configure FortiSwitch sFlow.
config switch-controller sflow
Description: Configure FortiSwitch sFlow.
set collector-ip {ipv4-address}
set collector-port {integer}
end
config switch-controller sflow
Parameter
Description
Type
Size
Default
collector-ip
Collector IP.
ipv4-address
Not
Specified
0.0.0.0
collector-port
SFlow collector port (0 - 65535).
integer
Minimum
value: 0
Maximum
value:
65535
6343
config switch-controller snmp-community
Configure FortiSwitch SNMP v1/v2c communities globally.
config switch-controller snmp-community
Description: Configure FortiSwitch SNMP v1/v2c communities globally.
edit <id>
set events {option1}, {option2}, ...
config hosts
Description: Configure IPv4 SNMP managers (hosts).
edit <id>
set ip {user}
next
end
set name {string}
set query-v1-port {integer}
set query-v1-status [disable|enable]
set query-v2c-port {integer}
set query-v2c-status [disable|enable]
set status [disable|enable]
set trap-v1-lport {integer}
set trap-v1-rport {integer}
set trap-v1-status [disable|enable]
set trap-v2c-lport {integer}
FortiOS 8.0.0 CLI Reference
1430
Fortinet Inc.

<!-- 来源页 1431 -->
set trap-v2c-rport {integer}
set trap-v2c-status [disable|enable]
next
end
config switch-controller snmp-community
Parameter
Description
Type
Size
Default
events
SNMP notifications (traps) to send.
option
-cpu-high
mem-low
log-full intf-ip ent-conf-change
l2mac
Option
Description
cpu-high
Send a trap when CPU usage too high.
mem-low
Send a trap when available memory is low.
log-full
Send a trap when log disk space becomes low.
intf-ip
Send a trap when an interface IP address is changed.
ent-conf-change
Send a trap when an entity MIB change occurs (RFC4133).
l2mac
Send a trap for Learning event (add/delete/movefrom/moveto).
id
SNMP community ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
name
SNMP community name.
string
Maximum
length: 35
query-v1-port
SNMP v1 query port (default = 161).
integer
Minimum value:
0 Maximum
value: 65535
161
query-v1-status
Enable/disable SNMP v1 queries.
option
-enable
Option
Description
disable
Disable SNMP v1 queries.
enable
Enable SNMP v1 queries.
FortiOS 8.0.0 CLI Reference
1431
Fortinet Inc.

<!-- 来源页 1432 -->
Parameter
Description
Type
Size
Default
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
Option
Description
disable
Disable SNMP v2c queries.
enable
Enable SNMP v2c queries.
status
Enable/disable this SNMP community.
option
-enable
Option
Description
disable
Disable SNMP community.
enable
Enable SNMP community.
trap-v1-lport
SNMP v2c trap local port (default = 162).
integer
Minimum value:
0 Maximum
value: 65535
162
trap-v1-rport
SNMP v2c trap remote port (default = 162).
integer
Minimum value:
0 Maximum
value: 65535
162
trap-v1-status
Enable/disable SNMP v1 traps.
option
-enable
Option
Description
disable
Disable SNMP v1 traps.
enable
Enable SNMP v1 traps.
trap-v2c-lport
SNMP v2c trap local port (default = 162).
integer
Minimum value:
0 Maximum
value: 65535
162
trap-v2c-rport
SNMP v2c trap remote port (default = 162).
integer
Minimum value:
0 Maximum
value: 65535
162
trap-v2c-status
Enable/disable SNMP v2c traps.
option
-enable
Option
Description
disable
Disable SNMP v2c traps.
enable
Enable SNMP v2c traps.
FortiOS 8.0.0 CLI Reference
1432
Fortinet Inc.

<!-- 来源页 1433 -->
config hosts
Parameter
Description
Type
Size
Default
id
Host entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
ip
IPv4 address of the SNMP manager (host).
user
Not Specified
config switch-controller snmp-sysinfo
Configure FortiSwitch SNMP system information globally.
config switch-controller snmp-sysinfo
Description: Configure FortiSwitch SNMP system information globally.
set contact-info {string}
set description {string}
set engine-id {string}
set location {string}
set status [disable|enable]
end
config switch-controller snmp-sysinfo
Parameter
Description
Type
Size
Default
contact-info
Contact information.
string
Maximum
length: 35
description
System description.
string
Maximum
length: 35
engine-id
Local SNMP engine ID string (max 24 char).
string
Maximum
length: 24
location
System location.
string
Maximum
length: 35
status
Enable/disable SNMP.
option
-disable
Option
Description
disable
Disable SNMP.
enable
Enable SNMP.
FortiOS 8.0.0 CLI Reference
1433
Fortinet Inc.

<!-- 来源页 1434 -->
config switch-controller snmp-trap-threshold
Configure FortiSwitch SNMP trap threshold values globally.
config switch-controller snmp-trap-threshold
Description: Configure FortiSwitch SNMP trap threshold values globally.
set trap-high-cpu-threshold {integer}
set trap-log-full-threshold {integer}
set trap-low-memory-threshold {integer}
end
config switch-controller snmp-trap-threshold
Parameter
Description
Type
Size
Default
trap-high-cpu-threshold
CPU usage when trap is sent.
integer
Minimum value:
0 Maximum
value:
4294967295
80
trap-log-full-threshold
Log disk usage when trap is sent.
integer
Minimum value:
0 Maximum
value:
4294967295
90
trap-low-memory-threshold
Memory usage when trap is sent.
integer
Minimum value:
0 Maximum
value:
4294967295
80
config switch-controller snmp-user
Configure FortiSwitch SNMP v3 users globally.
config switch-controller snmp-user
Description: Configure FortiSwitch SNMP v3 users globally.
edit <name>
set auth-proto [md5|sha1|...]
set auth-pwd {password}
set priv-proto [aes128|aes192|...]
set priv-pwd {password}
set queries [disable|enable]
set query-port {integer}
set security-level [no-auth-no-priv|auth-no-priv|...]
next
end
FortiOS 8.0.0 CLI Reference
1434
Fortinet Inc.

<!-- 来源页 1435 -->
config switch-controller snmp-user
Parameter
Description
Type
Size
Default
auth-proto
Authentication protocol.
option
-sha256
Option
Description
md5
HMAC-MD5-96 authentication protocol.
sha1
HMAC-SHA-1 authentication protocol.
sha224
HMAC-SHA-224 authentication protocol.
sha256
HMAC-SHA-256 authentication protocol.
sha384
HMAC-SHA-384 authentication protocol.
sha512
HMAC-SHA-512 authentication protocol.
auth-pwd
Password for authentication protocol.
password
Not
Specified
name
SNMP user name.
string
Maximum
length: 32
priv-proto
Privacy (encryption) protocol.
option
-aes128
Option
Description
aes128
CFB128-AES-128 symmetric encryption protocol.
aes192
CFB128-AES-192 symmetric encryption protocol.
aes192c
CFB128-AES-192-C symmetric encryption protocol.
aes256
CFB128-AES-256 symmetric encryption protocol.
aes256c
CFB128-AES-256-C symmetric encryption protocol.
des
CBC-DES symmetric encryption protocol.
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
disable
Disable SNMP queries for this user.
enable
Enable SNMP queries for this user.
query-port
SNMPv3 query port (default = 161).
integer
Minimum
value: 0
Maximum
value:
65535
161
FortiOS 8.0.0 CLI Reference
1435
Fortinet Inc.

<!-- 来源页 1436 -->
Parameter
Description
Type
Size
Default
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
config switch-controller storm-control
Configure FortiSwitch storm control.
config switch-controller storm-control
Description: Configure FortiSwitch storm control.
set broadcast [enable|disable]
set burst-size-level {integer}
set rate {integer}
set unknown-multicast [enable|disable]
set unknown-unicast [enable|disable]
end
config switch-controller storm-control
Parameter
Description
Type
Size
Default
broadcast
Enable/disable storm control to drop broadcast
traffic.
option
-disable
Option
Description
enable
Enable broadcast storm control.
disable
Disable broadcast storm control.
burst-size-level
Increase level to handle bursty traffic (0 - 4,
default = 0).
integer
Minimum
value: 0
Maximum
value: 4
0
rate
Rate in packets per second at which storm control
drops excess traffic(0-10000000, default=500,
drop-all=0).
integer
Minimum
value: 0
Maximum
value:
10000000
500
FortiOS 8.0.0 CLI Reference
1436
Fortinet Inc.

<!-- 来源页 1437 -->
Parameter
Description
Type
Size
Default
unknown-multicast
Enable/disable storm control to drop unknown
multicast traffic.
option
-disable
Option
Description
enable
Enable unknown multicast storm control.
disable
Disable unknown multicast storm control.
unknown-unicast
Enable/disable storm control to drop unknown
unicast traffic.
option
-disable
Option
Description
enable
Enable unknown unicast storm control.
disable
Disable unknown unicast storm control.
config switch-controller storm-control-policy
Configure FortiSwitch storm control policy to be applied on managed-switch ports.
config switch-controller storm-control-policy
Description: Configure FortiSwitch storm control policy to be applied on managed-switch ports.
edit <name>
set broadcast [enable|disable]
set burst-size-level {integer}
set description {string}
set rate {integer}
set storm-control-mode [global|override|...]
set unknown-multicast [enable|disable]
set unknown-unicast [enable|disable]
next
end
config switch-controller storm-control-policy
Parameter
Description
Type
Size
Default
broadcast
Enable/disable storm control to drop/allow
broadcast traffic in override mode.
option
-disable
Option
Description
enable
Enable storm control for broadcast traffic to drop packets which exceed
configured rate limits.
disable
Disable storm control for broadcast traffic to allow all packets.
FortiOS 8.0.0 CLI Reference
1437
Fortinet Inc.

<!-- 来源页 1438 -->
Parameter
Description
Type
Size
Default
burst-size-level
Increase level to handle bursty traffic (0 - 4,
default = 0).
integer
Minimum
value: 0
Maximum
value: 4
0
description
Description of the storm control policy.
string
Maximum
length: 63
name
Storm control policy name.
string
Maximum
length: 63
rate
Threshold rate in packets per second at which
storm traffic is controlled in override mode
(default=500, 0 to drop all).
integer
Minimum
value: 0
Maximum
value:
10000000
500
storm-control-mode
Set Storm control mode.
option
-global
Option
Description
global
Apply Global or switch level storm control configuration.
override
Override global and switch level storm control to use port level
configuration.
disabled
Disable storm control on the port entirely overriding global and switch
level storm control.
unknown-multicast
Enable/disable storm control to drop/allow
unknown multicast traffic in override mode.
option
-disable
Option
Description
enable
Enable storm control for unknown multicast traffic to drop packets
which exceed configured rate limits.
disable
Disable storm control for unknown multicast traffic to allow all packets.
unknown-unicast
Enable/disable storm control to drop/allow
unknown unicast traffic in override mode.
option
-disable
Option
Description
enable
Enable storm control for unknown unicast traffic to drop packets which
exceed configured rate limits.
disable
Disable storm control for unknown unicast traffic to allow all packets.
FortiOS 8.0.0 CLI Reference
1438
Fortinet Inc.

<!-- 来源页 1439 -->
config switch-controller stp-instance
Configure FortiSwitch multiple spanning tree protocol (MSTP) instances.
config switch-controller stp-instance
Description: Configure FortiSwitch multiple spanning tree protocol (MSTP) instances.
edit <id>
set vlan-range <vlan-name1>, <vlan-name2>, ...
next
end
config switch-controller stp-instance
Parameter
Description
Type
Size
Default
id
Instance ID.
string
Maximum
length: 2
vlan-range
<vlan-name>
Configure VLAN range for STP instance.
VLAN name.
string
Maximum
length: 79
config switch-controller stp-settings
Configure FortiSwitch spanning tree protocol (STP).
config switch-controller stp-settings
Description: Configure FortiSwitch spanning tree protocol (STP).
set forward-time {integer}
set hello-time {integer}
set max-age {integer}
set max-hops {integer}
set name {string}
set pending-timer {integer}
set revision {integer}
end
config switch-controller stp-settings
Parameter
Description
Type
Size
Default
forward-time
Period of time a port is in listening and learning
state (4 - 30 sec, default = 15).
integer
Minimum
value: 4
Maximum
value: 30
15
FortiOS 8.0.0 CLI Reference
1439
Fortinet Inc.

<!-- 来源页 1440 -->
Parameter
Description
Type
Size
Default
hello-time
Period of time between successive STP frame
Bridge Protocol Data Units (BPDUs) sent on a port
(1 - 10 sec, default = 2).
integer
Minimum
value: 1
Maximum
value: 10
2
max-age
Maximum time before a bridge port expires its
configuration BPDU information (6 - 40 sec, default
= 20).
integer
Minimum
value: 6
Maximum
value: 40
20
max-hops
Maximum number of hops between the root bridge
and the furthest bridge (1- 40, default = 20).
integer
Minimum
value: 1
Maximum
value: 40
20
name
Name of global STP settings configuration.
string
Maximum
length: 31
pending-timer
Pending time (1 - 15 sec, default = 4).
integer
Minimum
value: 1
Maximum
value: 15
4
revision
STP revision number (0 - 65535).
integer
Minimum
value: 0
Maximum
value:
65535
0
config switch-controller switch-group
Configure FortiSwitch switch groups.
config switch-controller switch-group
Description: Configure FortiSwitch switch groups.
edit <name>
set description {string}
set fortilink {string}
set members <switch-id1>, <switch-id2>, ...
next
end
FortiOS 8.0.0 CLI Reference
1440
Fortinet Inc.

<!-- 来源页 1441 -->
config switch-controller switch-group
Parameter
Description
Type
Size
Default
description
Optional switch group description.
string
Maximum
length: 63
fortilink
FortiLink interface to which switch group members
belong.
string
Maximum
length: 15
members
<switch-id>
FortiSwitch members belonging to this switch
group.
Managed device ID.
string
Maximum
length: 79
name
Switch group name.
string
Maximum
length: 35
config switch-controller switch-interface-tag
Configure switch object tags.
config switch-controller switch-interface-tag
Description: Configure switch object tags.
edit <name>
next
end
config switch-controller switch-interface-tag
Parameter
Description
Type
Size
Default
name
Tag name.
string
Maximum length:
63
config switch-controller switch-log
Configure FortiSwitch logging (logs are transferred to and inserted into FortiGate event log).
config switch-controller switch-log
Description: Configure FortiSwitch logging (logs are transferred to and inserted into
FortiGate event log).
set severity [emergency|alert|...]
set status [enable|disable]
end
FortiOS 8.0.0 CLI Reference
1441
Fortinet Inc.

<!-- 来源页 1442 -->
config switch-controller switch-log
Parameter
Description
Type
Size
Default
severity
Severity of FortiSwitch logs that are added to the
FortiGate event log.
option
-notification
Option
Description
emergency
Emergency level.
alert
Alert level.
critical
Critical level.
error
Error level.
warning
Warning level.
notification
Notification level.
information
Information level.
debug
Debug level.
status
Enable/disable adding FortiSwitch logs to
FortiGate event log.
option
-enable
Option
Description
enable
Add FortiSwitch logs to FortiGate event log.
disable
Do not add FortiSwitch logs to FortiGate event log.
config switch-controller switch-profile
Configure FortiSwitch switch profile.
config switch-controller switch-profile
Description: Configure FortiSwitch switch profile.
edit <name>
set login [enable|disable]
set login-passwd {password}
set login-passwd-override [enable|disable]
set private-data-encryption [enable|disable]
set private-data-encryption-key {password}
set revision-backup-on-logout [enable|disable]
set revision-backup-on-upgrade [enable|disable]
next
end
FortiOS 8.0.0 CLI Reference
1442
Fortinet Inc.

<!-- 来源页 1443 -->
config switch-controller switch-profile
Parameter
Description
Type
Size
Default
login
Enable/disable FortiSwitch serial console.
option
-enable
Option
Description
enable
Enable FortiSwitch serial console.
disable
Disable FortiSwitch serial console.
login-passwd
Login password of managed FortiSwitch.
password
Not
Specified
login-passwd-override
Enable/disable overriding the admin administrator
password for a managed FortiSwitch with the
FortiGate admin administrator account password.
option
-disable
Option
Description
enable
Override a managed FortiSwitch's admin administrator password.
disable
Use the managed FortiSwitch admin administrator account password.
name
FortiSwitch Profile name.
string
Maximum
length: 35
private-data-encryption *
Enable/disable private data encryption for non-admin passwords.
option
-disable
Option
Description
enable
Enable private data encryption.
disable
Disable private data encryption.
private-data-encryption-key *
Private data encryption key length (32
hexadecimal numbers).
password
Not
Specified
revision-backup-on-logout
Enable/disable automatic revision backup upon
logout from FortiSwitch.
option
-disable
Option
Description
enable
Enable automatic revision backup upon logout from FortiSwitch.
disable
Disable automatic revision backup upon logout from FortiSwitch.
revision-backup-on-upgrade
Enable/disable automatic revision backup upon
FortiSwitch image upgrade.
option
-disable
FortiOS 8.0.0 CLI Reference
1443
Fortinet Inc.

<!-- 来源页 1444 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable automatic revision backup upon FortiSwitch image upgrade.
disable
Disable automatic revision backup upon FortiSwitch image upgrade.
* This parameter may not exist in some models.
config switch-controller system
Configure system-wide switch controller settings.
config switch-controller system
Description: Configure system-wide switch controller settings.
set caputp-echo-interval {integer}
set caputp-max-retransmit {integer}
set data-sync-interval {integer}
set dynamic-periodic-interval {integer}
set iot-holdoff {integer}
set iot-mac-idle {integer}
set iot-scan-interval {integer}
set iot-weight-threshold {integer}
set nac-periodic-interval {integer}
set parallel-process {integer}
set parallel-process-override [disable|enable]
set tunnel-mode [compatible|moderate|...]
end
config switch-controller system
Parameter
Description
Type
Size
Default
caputp-echo-interval
Echo interval for the caputp echo requests from
swtp.
integer
Minimum
value: 8
Maximum
value: 600
30
caputp-max-retransmit
Maximum retransmission count for the caputp
tunnel packets.
integer
Minimum
value: 0
Maximum
value: 64
5
data-sync-interval
Time interval between collection of switch data
(30 - 1800 sec, default = 60, 0 = disable).
integer
Minimum
value: 30
Maximum
value: 1800
60
FortiOS 8.0.0 CLI Reference
1444
Fortinet Inc.

<!-- 来源页 1445 -->
Parameter
Description
Type
Size
Default
dynamic-periodic-interval
Periodic time interval to run Dynamic port policy
engine (5 - 180 sec, default = 60).
integer
Minimum
value: 5
Maximum
value: 180
60
iot-holdoff
MAC entry's creation time. Time must be greater
than this value for an entry to be created (0 -10080 mins, default = 5 mins).
integer
Minimum
value: 0
Maximum
value:
10080
5
iot-mac-idle
MAC entry's idle time. MAC entry is removed
after this value (0 - 10080 mins, default = 1440
mins).
integer
Minimum
value: 0
Maximum
value:
10080
1440
iot-scan-interval
IoT scan interval (2 - 10080 mins, default = 60
mins, 0 = disable).
integer
Minimum
value: 2
Maximum
value:
10080
60
iot-weight-threshold
MAC entry's confidence value. Value is re-queried when below this value (default = 1, 0 =
disable).
integer
Minimum
value: 0
Maximum
value: 255
1
nac-periodic-interval
Periodic time interval to run NAC engine (5 - 180
sec, default = 60).
integer
Minimum
value: 5
Maximum
value: 180
60
parallel-process
Maximum number of parallel processes.
integer
Minimum
value: 1
Maximum
value: 128
**
1
parallel-process-override
Enable/disable parallel process override.
option
-disable
Option
Description
disable
Disable maximum parallel process override.
enable
Enable maximum parallel process override.
tunnel-mode
Configure tunnel mode security (default =
compatible).
option
-compatible
FortiOS 8.0.0 CLI Reference
1445
Fortinet Inc.

<!-- 来源页 1446 -->
Parameter
Description
Type
Size
Default
Option
Description
compatible
Least restrictive. Supports the lowest levels of security but highest
compatibility between all FortiSwitch and FortiGate devices. 3rd party
certificates permitted.
moderate
Moderate level of security. 3rd party certificates permitted.
strict
Highest level of security requirements. If enabled, the FortiGate device
follows the same security mode requirements as in FIPS/CC mode.
** Values may differ between models.
config switch-controller traffic-policy
Configure FortiSwitch traffic policy.
config switch-controller traffic-policy
Description: Configure FortiSwitch traffic policy.
edit <name>
set cos-queue {integer}
set description {string}
set guaranteed-bandwidth {integer}
set guaranteed-burst {integer}
set maximum-burst {integer}
set policer-status [enable|disable]
set type [ingress|egress]
next
end
config switch-controller traffic-policy
Parameter
Description
Type
Size
Default
cos-queue
COS queue(0 - 7), or unset to disable.
integer
Minimum value:
0 Maximum
value: 7
description
Description of the traffic policy.
string
Maximum
length: 63
guaranteed-bandwidth
Guaranteed bandwidth in kbps (max value =
524287000).
integer
Minimum value:
0 Maximum
value:
524287000
10000
FortiOS 8.0.0 CLI Reference
1446
Fortinet Inc.

<!-- 来源页 1447 -->
Parameter
Description
Type
Size
Default
guaranteed-burst
Guaranteed burst size in bytes (max value =
4294967295).
integer
Minimum value:
0 Maximum
value:
4294967295
45000
maximum-burst
Maximum burst size in bytes (max value =
4294967295).
integer
Minimum value:
0 Maximum
value:
4294967295
67500
name
Traffic policy name.
string
Maximum
length: 63
policer-status
Enable/disable policer config on the traffic
policy.
option
-enable
Option
Description
enable
Enable policer config on the traffic policy.
disable
Disable policer config on the traffic policy.
type
Configure type of policy(ingress/egress). Read-only.
option
-ingress
Option
Description
ingress
Ingress policy.
egress
Egress policy.
config switch-controller traffic-sniffer
Configure FortiSwitch RSPAN/ERSPAN traffic sniffing parameters.
config switch-controller traffic-sniffer
Description: Configure FortiSwitch RSPAN/ERSPAN traffic sniffing parameters.
set erspan-ip {ipv4-address}
set mode [erspan-auto|rspan|...]
config target-ip
Description: Sniffer IPs to filter.
edit <ip>
set description {string}
next
end
config target-mac
Description: Sniffer MACs to filter.
edit <mac>
set description {string}
next
FortiOS 8.0.0 CLI Reference
1447
Fortinet Inc.

<!-- 来源页 1448 -->
end
config target-port
Description: Sniffer ports to filter.
edit <switch-id>
set description {string}
set in-ports <name1>, <name2>, ...
set out-ports <name1>, <name2>, ...
next
end
end
config switch-controller traffic-sniffer
Parameter
Description
Type
Size
Default
erspan-ip
Configure ERSPAN collector IP address.
ipv4-address
Not
Specified
0.0.0.0
mode
Configure traffic sniffer mode.
option
-erspan-auto
Option
Description
erspan-auto
Mirror traffic using a GRE tunnel.
rspan
Mirror traffic on a layer2 VLAN.
none
Disable traffic mirroring (sniffer).
config target-ip
Parameter
Description
Type
Size
Default
description
Description for the sniffer IP.
string
Maximum
length: 63
ip
Sniffer IP.
ipv4-address
Not
Specified
0.0.0.0
config target-mac
Parameter
Description
Type
Size
Default
description
Description for the sniffer MAC.
string
Maximum
length: 63
mac
Sniffer MAC.
mac-address
Not
Specified
00:00:00:00:00:00
FortiOS 8.0.0 CLI Reference
1448
Fortinet Inc.

<!-- 来源页 1449 -->
config target-port
Parameter
Description
Type
Size
Default
description
Description for the sniffer port entry.
string
Maximum
length: 63
in-ports
<name>
Configure source ingress port interfaces.
Interface name.
string
Maximum
length: 79
out-ports
<name>
Configure source egress port interfaces.
Interface name.
string
Maximum
length: 79
switch-id
Managed-switch ID.
string
Maximum
length: 35
config switch-controller virtual-port-pool
Configure virtual pool.
config switch-controller virtual-port-pool
Description: Configure virtual pool.
edit <name>
set description {string}
next
end
config switch-controller virtual-port-pool
Parameter
Description
Type
Size
Default
description
Virtual switch pool description.
string
Maximum
length: 63
name
Virtual switch pool name.
string
Maximum
length: 35
config switch-controller vlan-policy
Configure VLAN policy to be applied on the managed FortiSwitch ports through dynamic-port-policy.
config switch-controller vlan-policy
Description: Configure VLAN policy to be applied on the managed FortiSwitch ports through
dynamic-port-policy.
edit <name>
set allowed-vlans <vlan-name1>, <vlan-name2>, ...
set allowed-vlans-all [enable|disable]
FortiOS 8.0.0 CLI Reference
1449
Fortinet Inc.

<!-- 来源页 1450 -->
set description {string}
set discard-mode [none|all-untagged|...]
set fortilink {string}
set untagged-vlans <vlan-name1>, <vlan-name2>, ...
set vlan {string}
next
end
config switch-controller vlan-policy
Parameter
Description
Type
Size
Default
allowed-vlans <vlan-name>
Allowed VLANs to be applied when using this VLAN
policy.
VLAN name.
string
Maximum
length: 79
allowed-vlans-all
Enable/disable all defined VLANs when using this
VLAN policy.
option
-disable
Option
Description
enable
Enable all defined VLANs.
disable
Disable all defined VLANs.
description
Description for the VLAN policy.
string
Maximum
length: 63
discard-mode
Discard mode to be applied when using this VLAN
policy.
option
-none
Option
Description
none
Discard disabled.
all-untagged
Discard all frames that are untagged.
all-tagged
Discard all frames that are tagged.
fortilink
FortiLink interface for which this VLAN policy
belongs to.
string
Maximum
length: 15
name
VLAN policy name.
string
Maximum
length: 63
untagged-vlans <vlan-name>
Untagged VLANs to be applied when using this
VLAN policy.
VLAN name.
string
Maximum
length: 79
vlan
Native VLAN to be applied when using this VLAN
policy.
string
Maximum
length: 15
FortiOS 8.0.0 CLI Reference
1450
Fortinet Inc.

---


<!-- 来源页 2666 -->
wireless-controller
This section includes syntax for the following commands:
l config wireless-controller access-control-list on page 2667
l config wireless-controller ap-status on page 2672
l config wireless-controller apcfg-profile on page 2670
l config wireless-controller arrp-profile on page 2672
l config wireless-controller ble-profile on page 2676
l config wireless-controller bonjour-profile on page 2679
l config wireless-controller global on page 2681
l config wireless-controller hotspot20 anqp-3gpp-cellular on page 2686
l config wireless-controller hotspot20 anqp-ip-address-type on page 2687
l config wireless-controller hotspot20 anqp-nai-realm on page 2688
l config wireless-controller hotspot20 anqp-network-auth-type on page 2692
l config wireless-controller hotspot20 anqp-roaming-consortium on page 2693
l config wireless-controller hotspot20 anqp-venue-name on page 2694
l config wireless-controller hotspot20 anqp-venue-url on page 2695
l config wireless-controller hotspot20 h2qp-advice-of-charge on page 2696
l config wireless-controller hotspot20 h2qp-conn-capability on page 2697
l config wireless-controller hotspot20 h2qp-operator-name on page 2700
l config wireless-controller hotspot20 h2qp-osu-provider-nai on page 2702
l config wireless-controller hotspot20 h2qp-osu-provider on page 2701
l config wireless-controller hotspot20 h2qp-terms-and-conditions on page 2703
l config wireless-controller hotspot20 h2qp-wan-metric on page 2704
l config wireless-controller hotspot20 hs-profile on page 2705
l config wireless-controller hotspot20 icon on page 2713
l config wireless-controller hotspot20 qos-map on page 2715
l config wireless-controller inter-controller on page 2716
l config wireless-controller log on page 2718
l config wireless-controller lw-profile on page 2723
l config wireless-controller mpsk-profile on page 2725
l config wireless-controller nac-profile on page 2728
l config wireless-controller qos-profile on page 2728
l config wireless-controller region on page 2732
l config wireless-controller setting on page 2733
l config wireless-controller snmp on page 2742
l config wireless-controller ssid-policy on page 2747
l config wireless-controller syslog-profile on page 2748
l config wireless-controller timers on page 2749
FortiOS 8.0.0 CLI Reference
2666
Fortinet Inc.

<!-- 来源页 2667 -->
l config wireless-controller vap-group on page 2786
l config wireless-controller vap on page 2752
l config wireless-controller wag-profile on page 2787
l config wireless-controller wids-profile on page 2788
l config wireless-controller wtp-group on page 2833
l config wireless-controller wtp-profile on page 2836
l config wireless-controller wtp on page 2806
config wireless-controller access-control-list
Configure WiFi bridge access control list.
config wireless-controller access-control-list
Description: Configure WiFi bridge access control list.
edit <name>
set comment {string}
config layer3-ipv4-rules
Description: AP ACL layer3 ipv4 rule list.
edit <rule-id>
set action [allow|deny]
set comment {string}
set dstaddr {user}
set dstport {integer}
set protocol {integer}
set srcaddr {user}
set srcport {integer}
next
end
config layer3-ipv6-rules
Description: AP ACL layer3 ipv6 rule list.
edit <rule-id>
set action [allow|deny]
set comment {string}
set dstaddr {user}
set dstport {integer}
set protocol {integer}
set srcaddr {user}
set srcport {integer}
next
end
next
end
FortiOS 8.0.0 CLI Reference
2667
Fortinet Inc.

<!-- 来源页 2668 -->
config wireless-controller access-control-list
Parameter
Description
Type
Size
Default
comment
Description.
string
Maximum
length: 63
name
AP access control list name.
string
Maximum
length: 35
config layer3-ipv4-rules
Parameter
Description
Type
Size
Default
action
Policy action (allow | deny).
option
-Option
Description
allow
Allows traffic matching the policy.
deny
Blocks traffic matching the policy.
comment
Description.
string
Maximum
length: 63
dstaddr
Destination IP address (any | local-LAN | IPv4
address[/<network mask | mask length>], default =
any).
user
Not
Specified
dstport
Destination port (0 - 65535, default = 0, meaning
any).
integer
Minimum
value: 0
Maximum
value:
65535
0
protocol
Protocol type as defined by IANA (0 - 255, default
= 255, meaning any).
integer
Minimum
value: 0
Maximum
value: 255
255
rule-id
Rule ID (1 - 65535).
integer
Minimum
value: 1
Maximum
value:
65535
0
srcaddr
Source IP address (any | local-LAN | IPv4 address
[/<network mask | mask length>] | fqdn, default =
any).
user
Not
Specified
FortiOS 8.0.0 CLI Reference
2668
Fortinet Inc.

<!-- 来源页 2669 -->
Parameter
Description
Type
Size
Default
srcport
Source port (0 - 65535, default = 0, meaning any).
integer
Minimum
value: 0
Maximum
value:
65535
0
config layer3-ipv6-rules
Parameter
Description
Type
Size
Default
action
Policy action (allow | deny).
option
-Option
Description
allow
Allows traffic matching the policy.
deny
Blocks traffic matching the policy.
comment
Description.
string
Maximum
length: 63
dstaddr
Destination IPv6 address (any | local-LAN | IPv6
address[/prefix length]), default = any.
user
Not
Specified
dstport
Destination port (0 - 65535, default = 0, meaning
any).
integer
Minimum
value: 0
Maximum
value:
65535
0
protocol
Protocol type as defined by IANA (0 - 255, default
= 255, meaning any).
integer
Minimum
value: 0
Maximum
value: 255
255
rule-id
Rule ID (1 - 65535).
integer
Minimum
value: 1
Maximum
value:
65535
0
srcaddr
Source IPv6 address (any | local-LAN | IPv6
address[/prefix length] | fqdn), default = any.
user
Not
Specified
srcport
Source port (0 - 65535, default = 0, meaning any).
integer
Minimum
value: 0
Maximum
value:
65535
0
FortiOS 8.0.0 CLI Reference
2669
Fortinet Inc.

<!-- 来源页 2670 -->
config wireless-controller apcfg-profile
Configure AP local configuration profiles.
config wireless-controller apcfg-profile
Description: Configure AP local configuration profiles.
edit <name>
set ac-ip {ipv4-address}
set ac-port {integer}
set ac-timer {integer}
set ac-type [default|specify|...]
set ap-family [fap|fap-u|...]
config command-list
Description: AP local configuration command list.
edit <id>
set name {string}
set passwd-value {password}
set type [non-password|password]
set value {string}
next
end
set comment {var-string}
next
end
config wireless-controller apcfg-profile
Parameter
Description
Type
Size
Default
ac-ip
IP address of the validation controller that AP must
be able to join after applying AP local configuration.
ipv4-address
Not
Specified
0.0.0.0
ac-port
Port of the validation controller that AP must be
able to join after applying AP local configuration
(1024 - 49150, default = 5246).
integer
Minimum
value: 1024
Maximum
value:
49150
5246
ac-timer
Maximum waiting time for the AP to join the
validation controller after applying AP local
configuration (3 - 30 min, default = 10).
integer
Minimum
value: 3
Maximum
value: 30
10
ac-type
Validation controller type (default = default).
option
-default
Option
Description
default
This controller is the one and only controller that the AP could join after
applying AP local configuration.
FortiOS 8.0.0 CLI Reference
2670
Fortinet Inc.

<!-- 来源页 2671 -->
Parameter
Description
Type
Size
Default
Option
Description
specify
Specified controller is the one and only controller that the AP could join
after applying AP local configuration.
apcfg
Any controller defined by AP local configuration after applying AP local
configuration.
ap-family
FortiAP family type (default = fap).
option
-fap
Option
Description
fap
FortiAP Family.
fap-u
FortiAP-U Family.
fap-c
FortiAP-C Family.
comment
Comment.
var-string
Maximum
length: 255
name
AP local configuration profile name.
string
Maximum
length: 35
config command-list
Parameter
Description
Type
Size
Default
id
Command ID.
integer
Minimum
value: 1
Maximum
value: 255
0
name
AP local configuration command name.
string
Maximum
length: 63
passwd-value
AP local configuration command password value.
password
Not
Specified
type
The command type (default = non-password).
option
-non-password
Option
Description
non-password
Non-password command.
password
Password command.
value
AP local configuration command value.
string
Maximum
length: 127
FortiOS 8.0.0 CLI Reference
2671
Fortinet Inc.

<!-- 来源页 2672 -->
config wireless-controller ap-status
Configure access point status (rogue | accepted | suppressed).
config wireless-controller ap-status
Description: Configure access point status (rogue | accepted | suppressed).
edit <id>
set bssid {mac-address}
set ssid {string}
set status [rogue|accepted|...]
next
end
config wireless-controller ap-status
Parameter
Description
Type
Size
Default
bssid
Access Point's (AP's) BSSID.
mac-address
Not Specified
00:00:00:00:00:00
id
AP ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
ssid
Access Point's (AP's) SSID.
string
Maximum
length: 32
status
Access Point's (AP's) status: rogue,
accepted, or suppressed.
option
-rogue
Option
Description
rogue
Rogue AP.
accepted
Accepted AP.
suppressed
Suppressed AP.
config wireless-controller arrp-profile
Configure WiFi Automatic Radio Resource Provisioning (ARRP) profiles.
config wireless-controller arrp-profile
Description: Configure WiFi Automatic Radio Resource Provisioning (ARRP) profiles.
edit <name>
set comment {var-string}
set darrp-optimize {integer}
set darrp-optimize-schedules <name1>, <name2>, ...
FortiOS 8.0.0 CLI Reference
2672
Fortinet Inc.

<!-- 来源页 2673 -->
set include-dfs-channel [enable|disable]
set include-weather-channel [enable|disable]
set monitor-period {integer}
set override-darrp-optimize [enable|disable]
set selection-period {integer}
set threshold-ap {integer}
set threshold-channel-load {integer}
set threshold-noise-floor {string}
set threshold-rx-errors {integer}
set threshold-spectral-rssi {string}
set threshold-tx-retries {integer}
set weight-channel-load {integer}
set weight-dfs-channel {integer}
set weight-managed-ap {integer}
set weight-noise-floor {integer}
set weight-rogue-ap {integer}
set weight-spectral-rssi {integer}
set weight-weather-channel {integer}
next
end
config wireless-controller arrp-profile
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
darrp-optimize
Time for running Distributed Automatic Radio
Resource Provisioning (DARRP) optimizations (0 -86400 sec, default = 86400, 0 = disable).
integer
Minimum
value: 0
Maximum
value:
86400
86400
darrp-optimize-schedules
<name>
Firewall schedules for DARRP running time. DARRP
will run periodically based on darrp-optimize within
the schedules. Separate multiple schedule names
with a space.
Schedule name.
string
Maximum
length: 35
include-dfs-channel
Enable/disable use of DFS channel in DARRP
channel selection phase 1 (default = enable).
option
-enable
Option
Description
enable
Include DFS channel in darrp channel selection phase 1.
disable
Exclude DFS channel in darrp channel selection phase 1.
FortiOS 8.0.0 CLI Reference
2673
Fortinet Inc.

<!-- 来源页 2674 -->
Parameter
Description
Type
Size
Default
include-weather-channel
Enable/disable use of weather channel in DARRP
channel selection phase 1 (default = enable).
option
-enable
Option
Description
enable
Include weather channel in darrp channel selection phase 1.
disable
Exclude weather channel in darrp channel selection phase 1.
monitor-period
Period in seconds to measure average transmit
retries and receive errors (default = 300).
integer
Minimum
value: 0
Maximum
value:
65535
300
name
WiFi ARRP profile name.
string
Maximum
length: 35
override-darrp-optimize
Enable to override setting darrp-optimize and
darrp-optimize-schedules (default = disable).
option
-disable
Option
Description
enable
Override setting darrp-optimize and darrp-optimize-schedules.
disable
Use setting darrp-optimize and darrp-optimize-schedules.
selection-period
Period in seconds to measure average channel
load, noise floor, spectral RSSI (default = 3600).
integer
Minimum
value: 0
Maximum
value:
65535
3600
threshold-ap
Threshold to reject channel in DARRP channel
selection phase 1 due to surrounding APs (0 - 500,
default = 250).
integer
Minimum
value: 0
Maximum
value: 500
250
threshold-channel-load
Threshold in percentage to reject channel in
DARRP channel selection phase 1 due to channel
load (0 - 100, default = 60).
integer
Minimum
value: 0
Maximum
value: 100
60
threshold-noise-floor
Threshold in dBm to reject channel in DARRP
channel selection phase 1 due to noise floor (-95 to
-20, default = -85).
string
Maximum
length: 7
-85
FortiOS 8.0.0 CLI Reference
2674
Fortinet Inc.

<!-- 来源页 2675 -->
Parameter
Description
Type
Size
Default
threshold-rx-errors
Threshold in percentage for receive errors to
trigger channel reselection in DARRP monitor stage
(0 - 100, default = 50).
integer
Minimum
value: 0
Maximum
value: 100
50
threshold-spectral-rssi
Threshold in dBm to reject channel in DARRP
channel selection phase 1 due to spectral RSSI (-95
to -20, default = -65).
string
Maximum
length: 7
-65
threshold-tx-retries
Threshold in percentage for transmit retries to
trigger channel reselection in DARRP monitor stage
(0 - 1000, default = 300).
integer
Minimum
value: 0
Maximum
value: 1000
300
weight-channel-load
Weight in DARRP channel score calculation for
channel load (0 - 200, default = 20).
integer
Minimum
value: 0
Maximum
value: 200
**
20
weight-dfs-channel
Weight in DARRP channel score calculation for DFS
channel (0 - 200, default = 50).
integer
Minimum
value: 0
Maximum
value: 200
**
50 **
weight-managed-ap
Weight in DARRP channel score calculation for
managed APs (0 - 200, default = 50).
integer
Minimum
value: 0
Maximum
value: 200
**
50
weight-noise-floor
Weight in DARRP channel score calculation for
noise floor (0 - 200, default = 40).
integer
Minimum
value: 0
Maximum
value: 200
**
40
weight-rogue-ap
Weight in DARRP channel score calculation for
rogue APs (0 - 200, default = 0).
integer
Minimum
value: 0
Maximum
value: 200
**
0 **
weight-spectral-rssi
Weight in DARRP channel score calculation for
spectral RSSI (0 - 200, default = 40).
integer
Minimum
value: 0
Maximum
value: 200
**
40
FortiOS 8.0.0 CLI Reference
2675
Fortinet Inc.

<!-- 来源页 2676 -->
Parameter
Description
Type
Size
Default
weight-weather-channel
Weight in DARRP channel score calculation for
weather channel (0 - 200, default = 100).
integer
Minimum
value: 0
Maximum
value: 200
**
100 **
** Values may differ between models.
config wireless-controller ble-profile
Configure Bluetooth Low Energy profile.
config wireless-controller ble-profile
Description: Configure Bluetooth Low Energy profile.
edit <name>
set advertising {option1}, {option2}, ...
set beacon-interval {integer}
set ble-scanning [enable|disable]
set comment {string}
set eddystone-instance {string}
set eddystone-namespace {string}
set eddystone-url {string}
set ibeacon-uuid {string}
set major-id {integer}
set minor-id {integer}
set scan-interval {integer}
set scan-period {integer}
set scan-threshold {string}
set scan-time {integer}
set scan-type [active|passive]
set scan-window {integer}
set txpower [0|1|...]
next
end
config wireless-controller ble-profile
Parameter
Description
Type
Size
Default
advertising
Advertising type.
option
-Option
Description
ibeacon
iBeacon advertising.
eddystone-uid
Eddystone UID advertising.
FortiOS 8.0.0 CLI Reference
2676
Fortinet Inc.

<!-- 来源页 2677 -->
Parameter
Description
Type
Size
Default
Option
Description
eddystone-url
Eddystone URL advertising.
beacon-interval
Beacon interval (default = 100 msec).
integer
Minimum
value: 40
Maximum
value: 3500
100
ble-scanning
Enable/disable Bluetooth Low Energy
(BLE) scanning.
option
-disable
Option
Description
enable
Enable BLE scanning.
disable
Disable BLE scanning.
comment
Comment.
string
Maximum
length: 63
eddystone-instance
Eddystone instance ID.
string
Maximum
length: 12
abcdef
eddystone-namespace
Eddystone namespace ID.
string
Maximum
length: 20
0102030405
eddystone-url
Eddystone URL.
string
Maximum
length: 127
http://www.fortinet.com
ibeacon-uuid
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
string
Maximum
length: 63
005ea414-cbd1-11e5-9956-625662870761
major-id
Major ID.
integer
Minimum
value: 0
Maximum
value:
65535
1000
minor-id
Minor ID.
integer
Minimum
value: 0
Maximum
value:
65535
2000
name
Bluetooth Low Energy profile name.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
2677
Fortinet Inc.

<!-- 来源页 2678 -->
Parameter
Description
Type
Size
Default
scan-interval
Scan Interval (default = 50 msec).
integer
Minimum
value: 10
Maximum
value: 1000
50
scan-period
Scan Period (default = 4000 msec).
integer
Minimum
value: 1000
Maximum
value:
10000
4000
scan-threshold
Minimum signal level/threshold in
dBm required for the AP to report
detected BLE device (-95 to -20,
default = -90).
string
Maximum
length: 7
-90
scan-time
Scan Time (default = 1000 msec).
integer
Minimum
value: 1000
Maximum
value:
10000
1000
scan-type
Scan Type (default = active).
option
-active
Option
Description
active
Active BLE scanning.
passive
Passive BLE scanning.
scan-window
Scan Windows (default = 50 msec).
integer
Minimum
value: 10
Maximum
value: 1000
50
txpower
Transmit power level (default = 0).
option
-0
Option
Description
0
Transmit power level 0 (-21 dBm)
1
Transmit power level 1 (-18 dBm)
2
Transmit power level 2 (-15 dBm)
3
Transmit power level 3 (-12 dBm)
4
Transmit power level 4 (-9 dBm)
5
Transmit power level 5 (-6 dBm)
6
Transmit power level 6 (-3 dBm)
FortiOS 8.0.0 CLI Reference
2678
Fortinet Inc.

<!-- 来源页 2679 -->
Parameter
Description
Type
Size
Default
Option
Description
7
Transmit power level 7 (0 dBm)
8
Transmit power level 8 (1 dBm)
9
Transmit power level 9 (2 dBm)
10
Transmit power level 10 (3 dBm)
11
Transmit power level 11 (4 dBm)
12
Transmit power level 12 (5 dBm)
13
Transmit power level 13 (8 dBm)
14
Transmit power level 14 (11 dBm)
15
Transmit power level 15 (14 dBm)
16
Transmit power level 16 (17 dBm)
17
Transmit power level 17 (20 dBm)
config wireless-controller bonjour-profile
Configure Bonjour profiles. Bonjour is Apple's zero configuration networking protocol. Bonjour profiles allow APs
and FortiAPs to connect to networks using Bonjour.
config wireless-controller bonjour-profile
Description: Configure Bonjour profiles. Bonjour is Apple's zero configuration networking
protocol. Bonjour profiles allow APs and FortiAPs to connect to networks using Bonjour.
edit <name>
set comment {string}
set micro-location [enable|disable]
config policy-list
Description: Bonjour policy list.
edit <policy-id>
set description {string}
set from-vlan {string}
set services {option1}, {option2}, ...
set to-vlan {string}
next
end
next
end
FortiOS 8.0.0 CLI Reference
2679
Fortinet Inc.

<!-- 来源页 2680 -->
config wireless-controller bonjour-profile
Parameter
Description
Type
Size
Default
comment
Comment.
string
Maximum
length: 63
micro-location
Enable/disable Micro location for Bonjour profile
(default = disable).
option
-disable
Option
Description
enable
Enable Micro location.
disable
Disable Micro location.
name
Bonjour profile name.
string
Maximum
length: 35
config policy-list
Parameter
Description
Type
Size
Default
description
Description.
string
Maximum
length: 63
from-vlan
VLAN ID from which the Bonjour service is
advertised (0 - 4094, default = 0).
string
Maximum
length: 63
0
policy-id
Policy ID.
integer
Minimum
value: 1
Maximum
value:
65535
0
services
Bonjour services for the VLAN connecting to the
Bonjour network.
option
-all
Option
Description
all
All services.
airplay
AirPlay.
afp
AFP (Apple File Sharing).
bit-torrent
BitTorrent.
ftp
FTP.
ichat
iChat.
itunes
iTunes.
FortiOS 8.0.0 CLI Reference
2680
Fortinet Inc.

<!-- 来源页 2681 -->
Parameter
Description
Type
Size
Default
Option
Description
printers
Printers.
samba
Samba.
scanners
Scanners.
ssh
SSH.
chromecast
ChromeCast.
miracast
Miracast.
to-vlan
VLAN ID to which the Bonjour service is made
available (0 - 4094, default = all).
string
Maximum
length: 63
all
config wireless-controller global
Configure wireless controller global settings.
config wireless-controller global
Description: Configure wireless controller global settings.
set acd-process-count {integer}
set ap-log-server [enable|disable]
set ap-log-server-ip {ipv4-address}
set ap-log-server-port {integer}
set control-message-offload {option1}, {option2}, ...
set data-ethernet-II [enable|disable]
set dfs-lab-test [enable|disable]
set discovery-mc-addr {ipv4-address-multicast}
set discovery-mc-addr6 {ipv6-address}
set fiapp-eth-type {integer}
set image-download [enable|disable]
set ipsec-base-ip {ipv4-address}
set link-aggregation [enable|disable]
set local-radio-vdom {string}
set location {string}
set max-ble-device {integer}
set max-clients {integer}
set max-retransmit {integer}
set max-rogue-ap {integer}
set max-rogue-ap-wtp {integer}
set max-rogue-sta {integer}
set max-sta-cap {integer}
set max-sta-cap-wtp {integer}
set max-sta-offline {integer}
set max-sta-offline-ip2mac {integer}
set max-vap-per-radio [8|16]
set max-wids-entry {integer}
FortiOS 8.0.0 CLI Reference
2681
Fortinet Inc.

<!-- 来源页 2682 -->
set mesh-eth-type {integer}
set nac-interval {integer}
set name {string}
set rogue-scan-mac-adjacency {integer}
set rolling-wtp-upgrade [enable|disable]
set rolling-wtp-upgrade-threshold {string}
set tunnel-mode [compatible|strict]
set wpad-process-count {integer}
set wtp-share [enable|disable]
end
config wireless-controller global
Parameter
Description
Type
Size
Default
acd-process-count
Configure the number cw_acd daemons for
multi-core CPU support (default = 0).
integer
Minimum value:
0 Maximum
value: 255
0
ap-log-server
Enable/disable configuring FortiGate to
redirect wireless event log messages or
FortiAPs to send UTM log messages to a
syslog server (default = disable).
option
-disable
Option
Description
enable
Enable AP log server.
disable
Disable AP log server.
ap-log-server-ip
IP address that FortiGate or FortiAPs send
log messages to.
ipv4-address
Not Specified
0.0.0.0
ap-log-server-port
Port that FortiGate or FortiAPs send log
messages to.
integer
Minimum value:
0 Maximum
value: 65535
0
control-message-offload
Configure CAPWAP control message data
channel offload.
option
-ebp-frame
aeroscout-tag ap-list
sta-list sta-cap-list stats
aeroscout-mu sta-health
spectral-analysis
Option
Description
ebp-frame
Ekahau blink protocol (EBP) frames.
FortiOS 8.0.0 CLI Reference
2682
Fortinet Inc.

<!-- 来源页 2683 -->
Parameter
Description
Type
Size
Default
Option
Description
aeroscout-tag
AeroScout tag.
ap-list
Rogue AP list.
sta-list
Rogue STA list.
sta-cap-list
STA capability list.
stats
WTP, radio, VAP, and STA statistics.
aeroscout-mu
AeroScout Mobile Unit (MU) report.
sta-health
STA health log.
spectral-analysis
Spectral analysis report.
data-ethernet-II
Configure the wireless controller to use
Ethernet II or 802.3 frames with 802.3 data
tunnel mode (default = enable).
option
-enable
Option
Description
enable
Use Ethernet II frames with 802.3 data tunnel mode.
disable
Use 802.3 Ethernet frames with 802.3 data tunnel mode.
dfs-lab-test
Enable/disable DFS certificate lab test
mode.
option
-disable
Option
Description
enable
Enable DFS certificate lab test mode.
disable
Disable DFS certificate lab test mode.
discovery-mc-addr
Multicast IP address for AP discovery
(default = 224.0.1.140).
ipv4-address-multicast
Not Specified
224.0.1.140
discovery-mc-addr6
Multicast IPv6 address for AP discovery
(default = FF02::18C).
ipv6-address
Not Specified
ff02::18c
fiapp-eth-type
Ethernet type for Fortinet Inter-Access
Point Protocol (IAPP), or IEEE 802.11f,
packets (0 - 65535, default = 5252).
integer
Minimum value:
0 Maximum
value: 65535
5252
image-download
Enable/disable WTP image download at join
time.
option
-enable
FortiOS 8.0.0 CLI Reference
2683
Fortinet Inc.

<!-- 来源页 2684 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable WTP image download at join time.
disable
Disable WTP image download at join time.
ipsec-base-ip
Base IP address for IPsec VPN tunnels
between the access points and the wireless
controller (default = 169.254.0.1).
ipv4-address
Not Specified
169.254.0.1
link-aggregation
Enable/disable calculating the CAPWAP
transmit hash to load balance sessions to
link aggregation nodes (default = disable).
option
-disable
Option
Description
enable
Enable calculating the CAPWAP transmit hash.
disable
Disable calculating the CAPWAP transmit hash.
local-radio-vdom *
Assign local radio's virtual domain.
string
Maximum
length: 31
root
location
Description of the location of the wireless
controller.
string
Maximum
length: 35
max-ble-device
Maximum number of BLE devices stored on
the controller (default = 0).
integer
Minimum value:
0 Maximum
value:
4294967295
0
max-clients
Maximum number of clients that can
connect simultaneously (default = 0,
meaning no limitation).
integer
Minimum value:
0 Maximum
value:
4294967295
0
max-retransmit
Maximum number of tunnel packet
retransmissions (0 - 64, default = 3).
integer
Minimum value:
0 Maximum
value: 64
3
max-rogue-ap
Maximum number of rogue APs stored on
the controller (default = 0).
integer
Minimum value:
0 Maximum
value:
4294967295
0
max-rogue-ap-wtp
Maximum number of rogue AP's wtp info
stored on the controller (1 - 16, default = 16).
integer
Minimum value:
1 Maximum
value: 16
16
FortiOS 8.0.0 CLI Reference
2684
Fortinet Inc.

<!-- 来源页 2685 -->
Parameter
Description
Type
Size
Default
max-rogue-sta
Maximum number of rogue stations stored
on the controller (default = 0).
integer
Minimum value:
0 Maximum
value:
4294967295
0
max-sta-cap
Maximum number of station cap stored on
the controller (default = 0).
integer
Minimum value:
0 Maximum
value:
4294967295
0
max-sta-cap-wtp
Maximum number of station cap's wtp info
stored on the controller (1 - 16, default = 8).
integer
Minimum value:
1 Maximum
value: 8
8
max-sta-offline
Maximum number of station offline stored
on the controller (default = 0).
integer
Minimum value:
0 Maximum
value:
4294967295
0
max-sta-offline-ip2mac
Maximum number of station offline ip2mac
stored on the controller (default = 0).
integer
Minimum value:
0 Maximum
value:
4294967295
0
max-vap-per-radio *
Maximum number of SSIDs supported on
the radio (default = 8).
option
-8
Option
Description
8
Support at most 8 SSIDs on the radio.
16
Support at most 16 SSIDs on the radio.
max-wids-entry
Maximum number of wids entries stored on
the controller (default = 0).
integer
Minimum value:
0 Maximum
value:
4294967295
0
mesh-eth-type
Mesh Ethernet identifier included in
backhaul packets (0 - 65535, default =
8755).
integer
Minimum value:
0 Maximum
value: 65535
8755
nac-interval
Interval in seconds between two WiFi
network access control (NAC) checks (10 -600, default = 120).
integer
Minimum value:
10 Maximum
value: 600
120
name
Name of the wireless controller.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
2685
Fortinet Inc.

<!-- 来源页 2686 -->
Parameter
Description
Type
Size
Default
rogue-scan-mac-adjacency
Maximum numerical difference between an
AP's Ethernet and wireless MAC values to
match for rogue detection (0 - 31, default =
7).
integer
Minimum value:
0 Maximum
value: 31
7
rolling-wtp-upgrade
Enable/disable rolling WTP upgrade (default
= disable).
option
-disable
Option
Description
enable
Enable rolling WTP upgrade.
disable
Disable rolling WTP upgrade.
rolling-wtp-upgrade-threshold
Minimum signal level/threshold in dBm
required for the managed WTP to be
included in rolling WTP upgrade (-95 to -20,
default = -80).
string
Maximum
length: 7
-80
tunnel-mode
Configure tunnel mode security (default =
compatible).
option
-compatible
Option
Description
compatible
Allow for backward compatible ciphers(3DES+SHA1+Strong list).
strict
Follow system level strong-crypto ciphers.
wpad-process-count
Wpad daemon process count for multi-core
CPU support.
integer
Minimum value:
0 Maximum
value: 255
0
wtp-share
Enable/disable sharing of WTPs between
VDOMs.
option
-disable
Option
Description
enable
WTP can be shared between all VDOMs.
disable
WTP can be used only in its own VDOM.
* This parameter may not exist in some models.
config wireless-controller hotspot20 anqp-3gpp-cellular
Configure 3GPP public land mobile network (PLMN).
config wireless-controller hotspot20 anqp-3gpp-cellular
Description: Configure 3GPP public land mobile network (PLMN).
edit <name>
config mcc-mnc-list
FortiOS 8.0.0 CLI Reference
2686
Fortinet Inc.

<!-- 来源页 2687 -->
Description: Mobile Country Code and Mobile Network Code configuration.
edit <id>
set mcc {string}
set mnc {string}
next
end
next
end
config wireless-controller hotspot20 anqp-3gpp-cellular
Parameter
Description
Type
Size
Default
name
3GPP PLMN name.
string
Maximum length:
35
config mcc-mnc-list
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
mcc
Mobile country code.
string
Maximum
length: 3
mnc
Mobile network code.
string
Maximum
length: 3
config wireless-controller hotspot20 anqp-ip-address-type
Configure IP address type availability.
config wireless-controller hotspot20 anqp-ip-address-type
Description: Configure IP address type availability.
edit <name>
set ipv4-address-type [not-available|public|...]
set ipv6-address-type [not-available|available|...]
next
end
FortiOS 8.0.0 CLI Reference
2687
Fortinet Inc.

<!-- 来源页 2688 -->
config wireless-controller hotspot20 anqp-ip-address-type
Parameter
Description
Type
Size
Default
ipv4-address-type
IPv4 address type.
option
-not-available
Option
Description
not-available
Address type not available.
public
Public IPv4 address available.
port-restricted
Port-restricted IPv4 address available.
single-NATed-private
Single NATed private IPv4 address available.
double-NATed-private
Double NATed private IPv4 address available.
port-restricted-and-single-NATed
Port-restricted IPv4 address and single NATed IPv4 address available.
port-restricted-and-double-NATed
Port-restricted IPv4 address and double NATed IPv4 address available.
not-known
Availability of the address type is not known.
ipv6-address-type
IPv6 address type.
option
-not-available
Option
Description
not-available
Address type not available.
available
Address type available.
not-known
Availability of the address type not known.
name
IP type name.
string
Maximum
length: 35
config wireless-controller hotspot20 anqp-nai-realm
Configure network access identifier (NAI) realm.
config wireless-controller hotspot20 anqp-nai-realm
Description: Configure network access identifier (NAI) realm.
edit <name>
config nai-list
FortiOS 8.0.0 CLI Reference
2688
Fortinet Inc.

<!-- 来源页 2689 -->
Description: NAI list.
edit <name>
config eap-method
Description: EAP Methods.
edit <index>
config auth-param
Description: EAP auth param.
edit <index>
set id [non-eap-inner-auth|inner-auth-eap|...]
set val [eap-identity|eap-md5|...]
next
end
set method [eap-identity|eap-md5|...]
next
end
set encoding [disable|enable]
set nai-realm {string}
next
end
next
end
config wireless-controller hotspot20 anqp-nai-realm
Parameter
Description
Type
Size
Default
name
NAI realm list name.
string
Maximum
length: 35
config nai-list
Parameter
Description
Type
Size
Default
encoding
Enable/disable format in accordance with IETF RFC
4282.
option
-enable
Option
Description
disable
Disable format in accordance with IETF RFC 4282.
enable
Enable format in accordance with IETF RFC 4282.
nai-realm
Configure NAI realms (delimited by a semi-colon
character).
string
Maximum
length: 255
name
NAI realm name.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
2689
Fortinet Inc.

<!-- 来源页 2690 -->
config eap-method
Parameter
Description
Type
Size
Default
index
EAP method index.
integer
Minimum
value: 1
Maximum
value: 5
0
method
EAP method type.
option
-eap-identity
Option
Description
eap-identity
Identity.
eap-md5
MD5.
eap-tls
TLS.
eap-ttls
TTLS.
eap-peap
PEAP.
eap-sim
SIM.
eap-aka
AKA.
eap-aka-prime
AKA'.
config auth-param
Parameter
Description
Type
Size
Default
id
ID of authentication parameter.
option
-inner-auth-eap
Option
Description
non-eap-inner-auth
Non-EAP inner authentication type.
inner-auth-eap
Inner authentication EAP method type.
credential
Credential type.
tunneled-credential
Tunneled EAP method credential type.
index
Param index.
integer
Minimum
value: 1
Maximum
value: 4
0
FortiOS 8.0.0 CLI Reference
2690
Fortinet Inc.

<!-- 来源页 2691 -->
Parameter
Description
Type
Size
Default
val
Value of authentication parameter.
option
-eap-identity
Option
Description
eap-identity
EAP Identity.
eap-md5
EAP MD5.
eap-tls
EAP TLS.
eap-ttls
EAP TTLS.
eap-peap
EAP PEAP.
eap-sim
EAP SIM.
eap-aka
EAP AKA.
eap-aka-prime
EAP AKA'.
non-eap-pap
Non EAP PAP.
non-eap-chap
Non EAP CHAP.
non-eap-mschap
Non EAP MSCHAP.
non-eap-mschapv2
Non EAP MSCHAPV2.
cred-sim
Credential SIM.
cred-usim
Credential USIM.
cred-nfc
Credential NFC secure element.
cred-hardware-token
Credential hardware token.
cred-softoken
Credential softoken.
cred-certificate
Credential certificate.
cred-user-pwd
Credential username password.
cred-none
Credential none.
cred-vendor-specific
Credential vendor specific.
tun-cred-sim
Tunneled credential SIM.
tun-cred-usim
Tunneled credential USIM.
tun-cred-nfc
Tunneled credential NFC secure element.
FortiOS 8.0.0 CLI Reference
2691
Fortinet Inc.

<!-- 来源页 2692 -->
Parameter
Description
Type
Size
Default
Option
Description
tun-cred-hardware-token
Tunneled credential hardware token.
tun-cred-softoken
Tunneled credential softoken.
tun-cred-certificate
Tunneled credential certificate.
tun-cred-user-pwd
Tunneled credential username password.
tun-cred-anonymous
Tunneled credential anonymous.
tun-cred-vendor-specific
Tunneled credential vendor specific.
config wireless-controller hotspot20 anqp-network-auth-type
Configure network authentication type.
config wireless-controller hotspot20 anqp-network-auth-type
Description: Configure network authentication type.
edit <name>
set auth-type [acceptance-of-terms|online-enrollment|...]
set url {string}
next
end
config wireless-controller hotspot20 anqp-network-auth-type
Parameter
Description
Type
Size
Default
auth-type
Network authentication type.
option
-acceptance-of-terms
Option
Description
acceptance-of-terms
Acceptance of terms and conditions.
FortiOS 8.0.0 CLI Reference
2692
Fortinet Inc.

<!-- 来源页 2693 -->
Parameter
Description
Type
Size
Default
Option
Description
online-enrollment
Online enrollment supported.
http-redirection
HTTP and HTTPS redirection.
dns-redirection
DNS redirection.
name
Authentication type name.
string
Maximum
length: 35
url
Redirect URL.
string
Maximum
length: 255
config wireless-controller hotspot20 anqp-roaming-consortium
Configure roaming consortium.
config wireless-controller hotspot20 anqp-roaming-consortium
Description: Configure roaming consortium.
edit <name>
config oi-list
Description: Organization identifier list.
edit <index>
set comment {string}
set oi {string}
next
end
next
end
config wireless-controller hotspot20 anqp-roaming-consortium
Parameter
Description
Type
Size
Default
name
Roaming consortium name.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
2693
Fortinet Inc.

<!-- 来源页 2694 -->
config oi-list
Parameter
Description
Type
Size
Default
comment
Comment.
string
Maximum
length: 35
index
OI index.
integer
Minimum
value: 1
Maximum
value: 10
0
oi
Organization identifier.
string
Maximum
length: 10
config wireless-controller hotspot20 anqp-venue-name
Configure venue name duple.
config wireless-controller hotspot20 anqp-venue-name
Description: Configure venue name duple.
edit <name>
config value-list
Description: Name list.
edit <index>
set lang {string}
set value {string}
next
end
next
end
config wireless-controller hotspot20 anqp-venue-name
Parameter
Description
Type
Size
Default
name
Name of venue name duple.
string
Maximum
length: 35
config value-list
Parameter
Description
Type
Size
Default
index
Value index.
integer
Minimum
value: 1
Maximum
value: 10
0
FortiOS 8.0.0 CLI Reference
2694
Fortinet Inc.

<!-- 来源页 2695 -->
Parameter
Description
Type
Size
Default
lang
Language code.
string
Maximum
length: 3
eng
value
Venue name value.
string
Maximum
length: 252
config wireless-controller hotspot20 anqp-venue-url
Configure venue URL.
config wireless-controller hotspot20 anqp-venue-url
Description: Configure venue URL.
edit <name>
config value-list
Description: URL list.
edit <index>
set number {integer}
set value {string}
next
end
next
end
config wireless-controller hotspot20 anqp-venue-url
Parameter
Description
Type
Size
Default
name
Name of venue url.
string
Maximum length:
35
config value-list
Parameter
Description
Type
Size
Default
index
URL index.
integer
Minimum
value: 1
Maximum
value: 10
0
number
Venue number.
integer
Minimum
value: 0
Maximum
value: 255
0
value
Venue URL value.
string
Maximum
length: 254
FortiOS 8.0.0 CLI Reference
2695
Fortinet Inc.

<!-- 来源页 2696 -->
config wireless-controller hotspot20 h2qp-advice-of-charge
Configure advice of charge.
config wireless-controller hotspot20 h2qp-advice-of-charge
Description: Configure advice of charge.
edit <name>
config aoc-list
Description: AOC list.
edit <name>
set nai-realm {string}
set nai-realm-encoding {string}
config plan-info
Description: Plan info.
edit <name>
set currency {string}
set info-file {string}
set lang {string}
next
end
set type [time-based|volume-based|...]
next
end
next
end
config wireless-controller hotspot20 h2qp-advice-of-charge
Parameter
Description
Type
Size
Default
name
Plan name.
string
Maximum length:
35
config aoc-list
Parameter
Description
Type
Size
Default
nai-realm
NAI realm list name.
string
Maximum
length: 255
nai-realm-encoding
NAI realm encoding.
string
Maximum
length: 1
name
Advice of charge ID.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
2696
Fortinet Inc.

<!-- 来源页 2697 -->
Parameter
Description
Type
Size
Default
type
Usage charge type.
option
-time-based
Option
Description
time-based
Time based usage charge.
volume-based
Volume based usage charge.
time-and-volume-based
Time and volume based usage charge.
unlimited
Unlimited usage.
config plan-info
Parameter
Description
Type
Size
Default
currency
Currency code.
string
Maximum length: 3
info-file
Info file.
string
Maximum length:
255
lang
Language code.
string
Maximum length: 3
name
Plan name.
string
Maximum length: 35
config wireless-controller hotspot20 h2qp-conn-capability
Configure connection capability.
config wireless-controller hotspot20 h2qp-conn-capability
Description: Configure connection capability.
edit <name>
set esp-port [closed|open|...]
set ftp-port [closed|open|...]
set http-port [closed|open|...]
set icmp-port [closed|open|...]
set ikev2-port [closed|open|...]
set ikev2-xx-port [closed|open|...]
set pptp-vpn-port [closed|open|...]
set ssh-port [closed|open|...]
set tls-port [closed|open|...]
set voip-tcp-port [closed|open|...]
set voip-udp-port [closed|open|...]
next
end
FortiOS 8.0.0 CLI Reference
2697
Fortinet Inc.

<!-- 来源页 2698 -->
config wireless-controller hotspot20 h2qp-conn-capability
Parameter
Description
Type
Size
Default
esp-port
Set ESP port service (used by IPsec VPNs) status.
option
-unknown
Option
Description
closed
The port is not open for communication.
open
The port is open for communication.
unknown
The port may or may not be open for communication.
ftp-port
Set FTP port service status.
option
-unknown
Option
Description
closed
The port is not open for communication.
open
The port is open for communication.
unknown
The port may or may not be open for communication.
http-port
Set HTTP port service status.
option
-unknown
Option
Description
closed
The port is not open for communication.
open
The port is open for communication.
unknown
The port may or may not be open for communication.
icmp-port
Set ICMP port service status.
option
-unknown
Option
Description
closed
The port is not open for communication.
open
The port is open for communication.
unknown
The port may or may not be open for communication.
ikev2-port
Set IKEv2 port service for IPsec VPN status.
option
-unknown
Option
Description
closed
The port is not open for communication.
open
The port is open for communication.
unknown
The port may or may not be open for communication.
ikev2-xx-port
Set UDP port 4500 (which may be used by IKEv2
for IPsec VPN) service status.
option
-unknown
FortiOS 8.0.0 CLI Reference
2698
Fortinet Inc.

<!-- 来源页 2699 -->
Parameter
Description
Type
Size
Default
Option
Description
closed
The port is not open for communication.
open
The port is open for communication.
unknown
The port may or may not be open for communication.
name
Connection capability name.
string
Maximum
length: 35
pptp-vpn-port
Set Point to Point Tunneling Protocol (PPTP) VPN
port service status.
option
-unknown
Option
Description
closed
The port is not open for communication.
open
The port is open for communication.
unknown
The port may or may not be open for communication.
ssh-port
Set SSH port service status.
option
-unknown
Option
Description
closed
The port is not open for communication.
open
The port is open for communication.
unknown
The port may or may not be open for communication.
tls-port
Set TLS VPN (HTTPS) port service status.
option
-unknown
Option
Description
closed
The port is not open for communication.
open
The port is open for communication.
unknown
The port may or may not be open for communication.
voip-tcp-port
Set VoIP TCP port service status.
option
-unknown
Option
Description
closed
The port is not open for communication.
open
The port is open for communication.
unknown
The port may or may not be open for communication.
voip-udp-port
Set VoIP UDP port service status.
option
-unknown
FortiOS 8.0.0 CLI Reference
2699
Fortinet Inc.

<!-- 来源页 2700 -->
Parameter
Description
Type
Size
Default
Option
Description
closed
The port is not open for communication.
open
The port is open for communication.
unknown
The port may or may not be open for communication.
config wireless-controller hotspot20 h2qp-operator-name
Configure operator friendly name.
config wireless-controller hotspot20 h2qp-operator-name
Description: Configure operator friendly name.
edit <name>
config value-list
Description: Name list.
edit <index>
set lang {string}
set value {string}
next
end
next
end
config wireless-controller hotspot20 h2qp-operator-name
Parameter
Description
Type
Size
Default
name
Friendly name ID.
string
Maximum length:
35
config value-list
Parameter
Description
Type
Size
Default
index
Value index.
integer
Minimum
value: 1
Maximum
value: 10
0
lang
Language code.
string
Maximum
length: 3
eng
value
Friendly name value.
string
Maximum
length: 252
FortiOS 8.0.0 CLI Reference
2700
Fortinet Inc.

<!-- 来源页 2701 -->
config wireless-controller hotspot20 h2qp-osu-provider
Configure online sign up (OSU) provider list.
config wireless-controller hotspot20 h2qp-osu-provider
Description: Configure online sign up (OSU) provider list.
edit <name>
config friendly-name
Description: OSU provider friendly name.
edit <index>
set friendly-name {string}
set lang {string}
next
end
set icon {string}
set osu-method {option1}, {option2}, ...
set osu-nai {string}
set server-uri {string}
config service-description
Description: OSU service name.
edit <service-id>
set lang {string}
set service-description {string}
next
end
next
end
config wireless-controller hotspot20 h2qp-osu-provider
Parameter
Description
Type
Size
Default
icon
OSU provider icon.
string
Maximum
length: 35
name
OSU provider ID.
string
Maximum
length: 35
osu-method
OSU method list.
option
-Option
Description
oma-dm
OMA DM.
soap-xml-spp
SOAP XML SPP.
reserved
Reserved.
osu-nai
OSU NAI.
string
Maximum
length: 255
FortiOS 8.0.0 CLI Reference
2701
Fortinet Inc.

<!-- 来源页 2702 -->
Parameter
Description
Type
Size
Default
server-uri
Server URI.
string
Maximum
length: 255
config friendly-name
Parameter
Description
Type
Size
Default
friendly-name
OSU provider friendly name.
string
Maximum
length: 252
index
OSU provider friendly name index.
integer
Minimum
value: 1
Maximum
value: 10
0
lang
Language code.
string
Maximum
length: 3
eng
config service-description
Parameter
Description
Type
Size
Default
lang
Language code.
string
Maximum
length: 3
eng
service-description
Service description.
string
Maximum
length: 252
service-id
OSU service ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config wireless-controller hotspot20 h2qp-osu-provider-nai
Configure online sign up (OSU) provider NAI list.
config wireless-controller hotspot20 h2qp-osu-provider-nai
Description: Configure online sign up (OSU) provider NAI list.
edit <name>
config nai-list
Description: OSU NAI list.
edit <name>
set osu-nai {string}
next
FortiOS 8.0.0 CLI Reference
2702
Fortinet Inc.

<!-- 来源页 2703 -->
end
next
end
config wireless-controller hotspot20 h2qp-osu-provider-nai
Parameter
Description
Type
Size
Default
name
OSU provider NAI ID.
string
Maximum
length: 35
config nai-list
Parameter
Description
Type
Size
Default
name
OSU NAI ID.
string
Maximum length: 35
osu-nai
OSU NAI.
string
Maximum length:
255
config wireless-controller hotspot20 h2qp-terms-and-conditions
Configure terms and conditions.
config wireless-controller hotspot20 h2qp-terms-and-conditions
Description: Configure terms and conditions.
edit <name>
set filename {string}
set timestamp {integer}
set url {string}
next
end
config wireless-controller hotspot20 h2qp-terms-and-conditions
Parameter
Description
Type
Size
Default
filename
Filename.
string
Maximum
length: 254
name
Terms and Conditions ID.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
2703
Fortinet Inc.

<!-- 来源页 2704 -->
Parameter
Description
Type
Size
Default
timestamp
Timestamp.
integer
Minimum value:
0 Maximum
value:
4294967295
0
url
URL.
string
Maximum
length: 253
config wireless-controller hotspot20 h2qp-wan-metric
Configure WAN metrics.
config wireless-controller hotspot20 h2qp-wan-metric
Description: Configure WAN metrics.
edit <name>
set downlink-load {integer}
set downlink-speed {integer}
set link-at-capacity [enable|disable]
set link-status [up|down|...]
set load-measurement-duration {integer}
set symmetric-wan-link [symmetric|asymmetric]
set uplink-load {integer}
set uplink-speed {integer}
next
end
config wireless-controller hotspot20 h2qp-wan-metric
Parameter
Description
Type
Size
Default
downlink-load
Downlink load.
integer
Minimum value:
0 Maximum
value: 255
0
downlink-speed
Downlink speed (in kilobits/s).
integer
Minimum value:
0 Maximum
value:
4294967295
2400
link-at-capacity
Link at capacity.
option
-disable
Option
Description
enable
Link at capacity (not allow additional mobile devices to associate).
disable
Link not at capacity (allow additional mobile devices to associate).
FortiOS 8.0.0 CLI Reference
2704
Fortinet Inc.

<!-- 来源页 2705 -->
Parameter
Description
Type
Size
Default
link-status
Link status.
option
-up
Option
Description
up
Link up.
down
Link down.
in-test
Link in test state.
load-measurement-duration
Load measurement duration (in tenths of
a second).
integer
Minimum value:
0 Maximum
value: 65535
0
name
WAN metric name.
string
Maximum
length: 35
symmetric-wan-link
WAN link symmetry.
option
-asymmetric
Option
Description
symmetric
Symmetric WAN link (uplink and downlink speeds are the same).
asymmetric
Asymmetric WAN link (uplink and downlink speeds are not the same).
uplink-load
Uplink load.
integer
Minimum value:
0 Maximum
value: 255
0
uplink-speed
Uplink speed (in kilobits/s).
integer
Minimum value:
0 Maximum
value:
4294967295
2400
config wireless-controller hotspot20 hs-profile
Configure hotspot profile.
config wireless-controller hotspot20 hs-profile
Description: Configure hotspot profile.
edit <name>
set 3gpp-plmn {string}
set access-network-asra [enable|disable]
set access-network-esr [enable|disable]
set access-network-internet [enable|disable]
set access-network-type [private-network|private-network-with-guest-access|...]
set access-network-uesa [enable|disable]
set advice-of-charge {string}
set anqp-domain-id {integer}
set bss-transition [enable|disable]
FortiOS 8.0.0 CLI Reference
2705
Fortinet Inc.

<!-- 来源页 2706 -->
set conn-cap {string}
set deauth-request-timeout {integer}
set dgaf [enable|disable]
set domain-name {string}
set gas-comeback-delay {integer}
set gas-fragmentation-limit {integer}
set hessid {mac-address}
set ip-addr-type {string}
set l2tif [enable|disable]
set nai-realm {string}
set network-auth {string}
set oper-friendly-name {string}
set oper-icon {string}
set osu-provider <name1>, <name2>, ...
set osu-provider-nai {string}
set osu-ssid {string}
set pame-bi [disable|enable]
set proxy-arp [enable|disable]
set qos-map {string}
set release {integer}
set roaming-consortium {string}
set terms-and-conditions {string}
set venue-group [unspecified|assembly|...]
set venue-name {string}
set venue-type [unspecified|arena|...]
set venue-url {string}
set wan-metrics {string}
set wba-charging-currency {string}
set wba-charging-rate {integer}
set wba-data-clearing-provider {string}
set wba-financial-clearing-provider {string}
set wba-open-roaming [disable|enable]
set wnm-sleep-mode [enable|disable]
next
end
config wireless-controller hotspot20 hs-profile
Parameter
Description
Type
Size
Default
3gpp-plmn
3GPP PLMN name.
string
Maximum
length: 35
access-network-asra
Enable/disable additional step
required for access (ASRA).
option
-disable
Option
Description
enable
Enable additional step required for access (ASRA).
disable
Disable additional step required for access (ASRA).
FortiOS 8.0.0 CLI Reference
2706
Fortinet Inc.

<!-- 来源页 2707 -->
Parameter
Description
Type
Size
Default
access-network-esr
Enable/disable emergency
services reachable (ESR).
option
-disable
Option
Description
enable
Enable emergency services reachable (ESR).
disable
Disable emergency services reachable (ESR).
access-network-internet
Enable/disable connectivity to the
Internet.
option
-disable
Option
Description
enable
Enable connectivity to the Internet.
disable
Disable connectivity to the Internet.
access-network-type
Access network type.
option
-private-network
Option
Description
private-network
Private network.
private-network-with-guest-access
Private network with guest access.
chargeable-public-network
Chargeable public network.
free-public-network
Free public network.
personal-device-network
Personal devices network.
emergency-services-only-network
Emergency services only network.
test-or-experimental
Test or experimental.
wildcard
Wildcard.
access-network-uesa
Enable/disable unauthenticated
emergency service accessible
(UESA).
option
-disable
FortiOS 8.0.0 CLI Reference
2707
Fortinet Inc.

<!-- 来源页 2708 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable unauthenticated emergency service accessible (UESA).
disable
Disable unauthenticated emergency service accessible (UESA).
advice-of-charge
Advice of charge.
string
Maximum
length: 35
anqp-domain-id
ANQP Domain ID (0-65535).
integer
Minimum value:
0 Maximum
value: 65535
0
bss-transition
Enable/disable basic service set
(BSS) transition Support.
option
-disable
Option
Description
enable
Enable basic service set (BSS) transition support.
disable
Disable basic service set (BSS) transition support.
conn-cap
Connection capability name.
string
Maximum
length: 35
deauth-request-timeout
Deauthentication request timeout
(in seconds).
integer
Minimum value:
30 Maximum
value: 120
60
dgaf
Enable/disable downstream
group-addressed forwarding
(DGAF).
option
-disable
Option
Description
enable
Enable downstream group-addressed forwarding (DGAF).
disable
Disable downstream group-addressed forwarding (DGAF).
domain-name
Domain name.
string
Maximum
length: 255
gas-comeback-delay
GAS comeback delay (0 or 100 -10000 milliseconds, default =
500).
integer
Minimum value:
100 Maximum
value: 10000
500
gas-fragmentation-limit
GAS fragmentation limit (512 -4096, default = 1024).
integer
Minimum value:
512 Maximum
value: 4096
1024
hessid
Homogeneous extended service
set identifier (HESSID).
mac-address
Not Specified
00:00:00:00:00:00
FortiOS 8.0.0 CLI Reference
2708
Fortinet Inc.

<!-- 来源页 2709 -->
Parameter
Description
Type
Size
Default
ip-addr-type
IP address type name.
string
Maximum
length: 35
l2tif
Enable/disable Layer 2 traffic
inspection and filtering.
option
-disable
Option
Description
enable
Enable Layer 2 traffic inspection and filtering.
disable
Disable Layer 2 traffic inspection and filtering.
nai-realm
NAI realm list name.
string
Maximum
length: 35
name
Hotspot profile name.
string
Maximum
length: 35
network-auth
Network authentication name.
string
Maximum
length: 35
oper-friendly-name
Operator friendly name.
string
Maximum
length: 35
oper-icon
Operator icon.
string
Maximum
length: 35
osu-provider
<name>
Manually selected list of OSU
provider(s).
OSU provider name.
string
Maximum
length: 35
osu-provider-nai
OSU Provider NAI.
string
Maximum
length: 35
osu-ssid
Online sign up (OSU) SSID.
string
Maximum
length: 255
pame-bi
Enable/disable Pre-Association
Message Exchange BSSID
Independent (PAME-BI).
option
-enable
Option
Description
disable
Disable Pre-Association Message Exchange BSSID Independent
(PAME-BI).
enable
Enable Pre-Association Message Exchange BSSID Independent
(PAME-BI).
proxy-arp
Enable/disable Proxy ARP.
option
-enable
FortiOS 8.0.0 CLI Reference
2709
Fortinet Inc.

<!-- 来源页 2710 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable Proxy ARP.
disable
Disable Proxy ARP.
qos-map
QoS MAP set ID.
string
Maximum
length: 35
release
Hotspot 2.0 Release number (1, 2,
3, default = 2).
integer
Minimum value:
1 Maximum
value: 3
2
roaming-consortium
Roaming consortium list name.
string
Maximum
length: 35
terms-and-conditions
Terms and conditions.
string
Maximum
length: 35
venue-group
Venue group.
option
-unspecified
Option
Description
unspecified
Unspecified.
assembly
Assembly.
business
Business.
educational
Educational.
factory
Factory and industrial.
institutional
Institutional.
mercantile
Mercantile.
residential
Residential.
storage
Storage.
utility
Utility and miscellaneous.
vehicular
Vehicular.
outdoor
Outdoor.
venue-name
Venue name.
string
Maximum
length: 35
venue-type
Venue type.
option
-unspecified
Option
Description
unspecified
Unspecified.
FortiOS 8.0.0 CLI Reference
2710
Fortinet Inc.

<!-- 来源页 2711 -->
Parameter
Description
Type
Size
Default
Option
Description
arena
Arena.
stadium
Stadium.
passenger-terminal
Passenger terminal.
amphitheater
Amphitheater.
amusement-park
Amusement park.
place-of-worship
Place of worship.
convention-center
Convention center.
library
Library.
museum
Museum.
restaurant
Restaurant.
theater
Theater.
bar
Bar.
coffee-shop
Coffee shop.
zoo-or-aquarium
Zoo or aquarium.
emergency-center
Emergency coordination center.
doctor-office
Doctor or dentist office.
bank
Bank.
fire-station
Fire station.
police-station
Police station.
post-office
Post office.
professional-office
Professional office.
research-facility
Research and development facility.
attorney-office
Attorney office.
primary-school
Primary school.
secondary-school
Secondary school.
university-or-college
University or college.
factory
Factory.
hospital
Hospital.
long-term-care-facility
Long term care facility.
FortiOS 8.0.0 CLI Reference
2711
Fortinet Inc.

<!-- 来源页 2712 -->
Parameter
Description
Type
Size
Default
Option
Description
rehab-center
Alcohol and drug rehabilitation center.
group-home
Group home.
prison-or-jail
Prison or jail.
retail-store
Retail store.
grocery-market
Grocery market.
auto-service-station
Auto service station.
shopping-mall
Shopping mall.
gas-station
Gas station.
private
Private residence.
hotel-or-motel
Hotel or motel.
dormitory
Dormitory.
boarding-house
Boarding house.
automobile
Automobile or truck.
airplane
Airplane.
bus
Bus.
ferry
Ferry.
ship-or-boat
Ship or boat.
train
Train.
motor-bike
Motor bike.
muni-mesh-network
Muni mesh network.
city-park
City park.
rest-area
Rest area.
traffic-control
Traffic control.
bus-stop
Bus stop.
kiosk
Kiosk.
venue-url
Venue name.
string
Maximum
length: 35
wan-metrics
WAN metric name.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
2712
Fortinet Inc.

<!-- 来源页 2713 -->
Parameter
Description
Type
Size
Default
wba-charging-currency
Three letter currency code.
string
Maximum
length: 3
wba-charging-rate
Number of currency units per
kilobyte.
integer
Minimum value:
0 Maximum
value:
4294967295
0
wba-data-clearing-provider
WBA ID of data clearing provider.
string
Maximum
length: 127
wba-financial-clearing-provider
WBA ID of financial clearing
provider.
string
Maximum
length: 127
wba-open-roaming
Enable/disable WBA open
roaming support.
option
-disable
Option
Description
disable
Disable WBA open roaming support.
enable
Enable WBA open roaming support.
wnm-sleep-mode
Enable/disable wireless network
management (WNM) sleep mode.
option
-disable
Option
Description
enable
Enable wireless network management (WNM) sleep mode.
disable
Disable wireless network management (WNM) sleep mode.
config wireless-controller hotspot20 icon
Configure OSU provider icon.
config wireless-controller hotspot20 icon
Description: Configure OSU provider icon.
edit <name>
config icon-list
Description: Icon list.
edit <name>
set file {string}
set height {integer}
set lang {string}
set type [bmp|gif|...]
set width {integer}
next
end
FortiOS 8.0.0 CLI Reference
2713
Fortinet Inc.

<!-- 来源页 2714 -->
next
end
config wireless-controller hotspot20 icon
Parameter
Description
Type
Size
Default
name
Icon list ID.
string
Maximum length:
35
config icon-list
Parameter
Description
Type
Size
Default
file
Icon file.
string
Maximum
length: 255
height
Icon height.
integer
Minimum
value: 1
Maximum
value:
65535
0
lang
Language code.
string
Maximum
length: 3
eng
name
Icon name.
string
Maximum
length: 255
type
Icon type.
option
-png
Option
Description
bmp
BMP image.
gif
GIF image.
jpeg
JPEG image.
png
PNG image.
tiff
TIFF image.
width
Icon width.
integer
Minimum
value: 1
Maximum
value:
65535
0
FortiOS 8.0.0 CLI Reference
2714
Fortinet Inc.

<!-- 来源页 2715 -->
config wireless-controller hotspot20 qos-map
Configure QoS map set.
config wireless-controller hotspot20 qos-map
Description: Configure QoS map set.
edit <name>
config dscp-except
Description: Differentiated Services Code Point (DSCP) exceptions.
edit <index>
set dscp {integer}
set up {integer}
next
end
config dscp-range
Description: Differentiated Services Code Point (DSCP) ranges.
edit <index>
set high {integer}
set low {integer}
set up {integer}
next
end
next
end
config wireless-controller hotspot20 qos-map
Parameter
Description
Type
Size
Default
name
QOS-MAP name.
string
Maximum length:
35
config dscp-except
Parameter
Description
Type
Size
Default
dscp
DSCP value.
integer
Minimum
value: 0
Maximum
value: 63
0
index
DSCP exception index.
integer
Minimum
value: 1
Maximum
value: 21
0
up
User priority.
integer
Minimum
value: 0
Maximum
value: 7
0
FortiOS 8.0.0 CLI Reference
2715
Fortinet Inc.

<!-- 来源页 2716 -->
config dscp-range
Parameter
Description
Type
Size
Default
high
DSCP high value.
integer
Minimum
value: 0
Maximum
value: 63
255
index
DSCP range index.
integer
Minimum
value: 1
Maximum
value: 8
0
low
DSCP low value.
integer
Minimum
value: 0
Maximum
value: 63
255
up
User priority.
integer
Minimum
value: 0
Maximum
value: 7
0
config wireless-controller inter-controller
Configure inter wireless controller operation.
config wireless-controller inter-controller
Description: Configure inter wireless controller operation.
set fast-failover-max {integer}
set fast-failover-wait {integer}
set inter-controller-key {password}
set inter-controller-mode [disable|l2-roaming|...]
config inter-controller-peer
Description: Fast failover peer wireless controller list.
edit <id>
set peer-ip {ipv4-address}
set peer-port {integer}
set peer-priority [primary|secondary]
next
end
set inter-controller-pri [primary|secondary]
set l3-roaming [enable|disable]
end
FortiOS 8.0.0 CLI Reference
2716
Fortinet Inc.

<!-- 来源页 2717 -->
config wireless-controller inter-controller
Parameter
Description
Type
Size
Default
fast-failover-max
Maximum number of retransmissions for fast
failover HA messages between peer wireless
controllers (3 - 64, default = 10).
integer
Minimum
value: 3
Maximum
value: 64
10
fast-failover-wait
Minimum wait time before an AP transitions from
secondary controller to primary controller (10 -86400 sec, default = 10).
integer
Minimum
value: 10
Maximum
value:
86400
10
inter-controller-key
Secret key for inter-controller communications.
password
Not
Specified
inter-controller-mode
Configure inter-controller mode (disable, l2-roaming, 1+1, default = disable).
option
-disable
Option
Description
disable
Disable inter-controller mode.
l2-roaming
Enable layer 2 roaming support between inter-controllers.
1+1
Enable 1+1 fast failover mode.
inter-controller-pri
Configure inter-controller's priority (primary or
secondary, default = primary).
option
-primary
Option
Description
primary
Primary fast failover mode.
secondary
Secondary fast failover mode.
l3-roaming
Enable/disable layer 3 roaming (default = disable).
option
-disable
Option
Description
enable
Enable layer 3 roaming.
disable
Disable layer 3 roaming.
FortiOS 8.0.0 CLI Reference
2717
Fortinet Inc.

<!-- 来源页 2718 -->
config inter-controller-peer
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
peer-ip
Peer wireless controller's IP address.
ipv4-address
Not Specified
0.0.0.0
peer-port
Port used by the wireless controller's for inter-controller communications (1024 - 49150,
default = 5246).
integer
Minimum value:
1024 Maximum
value: 49150
5246
peer-priority
Peer wireless controller's priority (primary or
secondary, default = primary).
option
-primary
Option
Description
primary
Primary fast failover mode.
secondary
Secondary fast failover mode.
config wireless-controller log
Configure wireless controller event log filters.
config wireless-controller log
Description: Configure wireless controller event log filters.
set addrgrp-log [emergency|alert|...]
set ble-log [emergency|alert|...]
set clb-log [emergency|alert|...]
set dhcp-starv-log [emergency|alert|...]
set led-sched-log [emergency|alert|...]
set radio-event-log [emergency|alert|...]
set rogue-event-log [emergency|alert|...]
set sta-event-log [emergency|alert|...]
set sta-locate-log [emergency|alert|...]
set status [enable|disable]
set wids-log [emergency|alert|...]
set wtp-event-log [emergency|alert|...]
set wtp-fips-event-log [emergency|alert|...]
end
FortiOS 8.0.0 CLI Reference
2718
Fortinet Inc.

<!-- 来源页 2719 -->
config wireless-controller log
Parameter
Description
Type
Size
Default
addrgrp-log
Lowest severity level to log address group
message.
option
-notification
Option
Description
emergency
Emergency level.
alert
Alert level.
critical
Critical level.
error
Error level.
warning
Warning level.
notification
Notification level.
information
Information level.
debug
Debug level.
ble-log
Lowest severity level to log BLE detection
message.
option
-notification
Option
Description
emergency
Emergency level.
alert
Alert level.
critical
Critical level.
error
Error level.
warning
Warning level.
notification
Notification level.
information
Information level.
debug
Debug level.
clb-log
Lowest severity level to log client load balancing
message.
option
-notification
Option
Description
emergency
Emergency level.
alert
Alert level.
critical
Critical level.
FortiOS 8.0.0 CLI Reference
2719
Fortinet Inc.

<!-- 来源页 2720 -->
Parameter
Description
Type
Size
Default
Option
Description
error
Error level.
warning
Warning level.
notification
Notification level.
information
Information level.
debug
Debug level.
dhcp-starv-log
Lowest severity level to log DHCP starvation
event message.
option
-notification
Option
Description
emergency
Emergency level.
alert
Alert level.
critical
Critical level.
error
Error level.
warning
Warning level.
notification
Notification level.
information
Information level.
debug
Debug level.
led-sched-log
Lowest severity level to log LED schedule event
message.
option
-notification
Option
Description
emergency
Emergency level.
alert
Alert level.
critical
Critical level.
error
Error level.
warning
Warning level.
notification
Notification level.
information
Information level.
debug
Debug level.
radio-event-log
Lowest severity level to log radio event message.
option
-notification
FortiOS 8.0.0 CLI Reference
2720
Fortinet Inc.

<!-- 来源页 2721 -->
Parameter
Description
Type
Size
Default
Option
Description
emergency
Emergency level.
alert
Alert level.
critical
Critical level.
error
Error level.
warning
Warning level.
notification
Notification level.
information
Information level.
debug
Debug level.
rogue-event-log
Lowest severity level to log rogue AP event
message.
option
-notification
Option
Description
emergency
Emergency level.
alert
Alert level.
critical
Critical level.
error
Error level.
warning
Warning level.
notification
Notification level.
information
Information level.
debug
Debug level.
sta-event-log
Lowest severity level to log station event
message.
option
-notification
Option
Description
emergency
Emergency level.
alert
Alert level.
critical
Critical level.
error
Error level.
warning
Warning level.
notification
Notification level.
FortiOS 8.0.0 CLI Reference
2721
Fortinet Inc.

<!-- 来源页 2722 -->
Parameter
Description
Type
Size
Default
Option
Description
information
Information level.
debug
Debug level.
sta-locate-log
Lowest severity level to log station locate
message.
option
-notification
Option
Description
emergency
Emergency level.
alert
Alert level.
critical
Critical level.
error
Error level.
warning
Warning level.
notification
Notification level.
information
Information level.
debug
Debug level.
status
Enable/disable wireless event logging.
option
-enable
Option
Description
enable
Enable wireless event logging.
disable
Disable wireless event logging.
wids-log
Lowest severity level to log WIDS message.
option
-notification
Option
Description
emergency
Emergency level.
alert
Alert level.
critical
Critical level.
error
Error level.
warning
Warning level.
notification
Notification level.
information
Information level.
debug
Debug level.
FortiOS 8.0.0 CLI Reference
2722
Fortinet Inc.

<!-- 来源页 2723 -->
Parameter
Description
Type
Size
Default
wtp-event-log
Lowest severity level to log WTP event message.
option
-notification
Option
Description
emergency
Emergency level.
alert
Alert level.
critical
Critical level.
error
Error level.
warning
Warning level.
notification
Notification level.
information
Information level.
debug
Debug level.
wtp-fips-event-log
Lowest severity level to log FAP fips event
message.
option
-notification
Option
Description
emergency
Emergency level.
alert
Alert level.
critical
Critical level.
error
Error level.
warning
Warning level.
notification
Notification level.
information
Information level.
debug
Debug level.
config wireless-controller lw-profile
Configure LoRaWAN profile.
config wireless-controller lw-profile
Description: Configure LoRaWAN profile.
edit <name>
set comment {string}
set cups-api-key {password}
set cups-server {string}
set cups-server-port {integer}
set lw-protocol [basics-station|packet-forwarder]
FortiOS 8.0.0 CLI Reference
2723
Fortinet Inc.

<!-- 来源页 2724 -->
set tc-api-key {password}
set tc-server {string}
set tc-server-port {integer}
next
end
config wireless-controller lw-profile
Parameter
Description
Type
Size
Default
comment
Comment.
string
Maximum
length: 63
cups-api-key
CUPS API key of LoRaWAN device.
password
Not
Specified
cups-server
CUPS (Configuration and Update Server) domain
name or IP address of LoRaWAN device.
string
Maximum
length: 255
cups-server-port
CUPS Port value of LoRaWAN device.
integer
Minimum
value: 0
Maximum
value:
65535
0
lw-protocol
Configure LoRaWAN protocol (default = basics-station)
option
-basics-station
Option
Description
basics-station
Configure LoRaWAN protocol to Basics Station.
packet-forwarder
Configure LoRaWAN protocol to UDP Packet Forwarder.
name
LoRaWAN profile name.
string
Maximum
length: 35
tc-api-key
TC API key of LoRaWAN device.
password
Not
Specified
tc-server
TC (Traffic Controller) domain name or IP address
of LoRaWAN device.
string
Maximum
length: 255
tc-server-port
TC Port value of LoRaWAN device.
integer
Minimum
value: 0
Maximum
value:
65535
0
FortiOS 8.0.0 CLI Reference
2724
Fortinet Inc.

<!-- 来源页 2725 -->
config wireless-controller mpsk-profile
Configure MPSK profile.
config wireless-controller mpsk-profile
Description: Configure MPSK profile.
edit <name>
set mpsk-concurrent-clients {integer}
set mpsk-external-server {string}
set mpsk-external-server-auth [enable|disable]
config mpsk-group
Description: List of multiple PSK groups.
edit <name>
config mpsk-key
Description: List of multiple PSK entries.
edit <name>
set comment {var-string}
set concurrent-client-limit-type [default|unlimited|...]
set concurrent-clients {integer}
set key-type [wpa2-personal|wpa3-sae]
set mac {mac-address}
set mpsk-schedules <name1>, <name2>, ...
set passphrase {password}
set sae-password {password}
set sae-pk [enable|disable]
set sae-private-key {string}
next
end
set vlan-id {integer}
set vlan-type [no-vlan|fixed-vlan]
next
end
set mpsk-type [wpa2-personal|wpa3-sae|...]
next
end
config wireless-controller mpsk-profile
Parameter
Description
Type
Size
Default
mpsk-concurrent-clients
Maximum number of concurrent clients that
connect using the same passphrase in multiple
PSK authentication (0 - 65535, default = 0,
meaning no limitation).
integer
Minimum
value: 0
Maximum
value:
65535
0
mpsk-external-server
RADIUS server to be used to authenticate MPSK
users.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
2725
Fortinet Inc.

<!-- 来源页 2726 -->
Parameter
Description
Type
Size
Default
mpsk-external-server-auth
Enable/Disable MPSK external server
authentication (default = disable).
option
-disable
Option
Description
enable
Enable MPSK external server authentication.
disable
Disable MPSK external server authentication.
mpsk-type
Select the security type of keys for this profile.
option
-wpa2-personal
Option
Description
wpa2-personal
WPA2 personal.
wpa3-sae
WPA3 SAE.
wpa3-sae-transition
WPA3 SAE transition.
name
MPSK profile name.
string
Maximum
length: 35
config mpsk-group
Parameter
Description
Type
Size
Default
name
MPSK group name.
string
Maximum
length: 35
vlan-id
Optional VLAN ID.
integer
Minimum
value: 1
Maximum
value: 4094
0
vlan-type
MPSK group VLAN options.
option
-no-vlan
Option
Description
no-vlan
No VLAN.
fixed-vlan
Fixed VLAN ID.
config mpsk-key
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
FortiOS 8.0.0 CLI Reference
2726
Fortinet Inc.

<!-- 来源页 2727 -->
Parameter
Description
Type
Size
Default
concurrent-client-limit-type
MPSK client limit type options.
option
-default
Option
Description
default
Using the value in profile configuration.
unlimited
Unlimited.
specified
Specified value.
concurrent-clients
Number of clients that can connect
using this pre-shared key (1 - 65535,
default is 256).
integer
Minimum
value: 1
Maximum
value:
65535
256
key-type
Select the type of the key.
option
-wpa2-personal
Option
Description
wpa2-personal
WPA2 personal.
wpa3-sae
WPA3 SAE.
mac
MAC address.
mac-address
Not
Specified
00:00:00:00:00:00
mpsk-schedules
<name>
Firewall schedule for MPSK passphrase.
The passphrase will be effective only
when at least one schedule is valid.
Schedule name.
string
Maximum
length: 35
name
Pre-shared key name.
string
Maximum
length: 35
passphrase
WPA Pre-shared key.
password
Not
Specified
sae-password
WPA3 SAE password.
password
Not
Specified
sae-pk
Enable/disable WPA3 SAE-PK (default =
disable).
option
-disable
Option
Description
enable
Enable WPA3 SAE-PK.
disable
Disable WPA3 SAE-PK.
sae-private-key
Private key used for WPA3 SAE-PK
authentication.
string
Maximum
length: 359
FortiOS 8.0.0 CLI Reference
2727
Fortinet Inc.

<!-- 来源页 2728 -->
config wireless-controller nac-profile
Configure WiFi network access control (NAC) profiles.
config wireless-controller nac-profile
Description: Configure WiFi network access control (NAC) profiles.
edit <name>
set comment {var-string}
set onboarding-vlan {string}
next
end
config wireless-controller nac-profile
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
Name.
string
Maximum
length: 35
onboarding-vlan
VLAN interface name.
string
Maximum
length: 35
config wireless-controller qos-profile
Configure WiFi quality of service (QoS) profiles.
config wireless-controller qos-profile
Description: Configure WiFi quality of service (QoS) profiles.
edit <name>
set bandwidth-admission-control [enable|disable]
set bandwidth-capacity {integer}
set burst [enable|disable]
set call-admission-control [enable|disable]
set call-capacity {integer}
set comment {string}
set downlink {integer}
set downlink-sta {integer}
set dscp-wmm-be <id1>, <id2>, ...
set dscp-wmm-bk <id1>, <id2>, ...
set dscp-wmm-mapping [enable|disable]
set dscp-wmm-vi <id1>, <id2>, ...
set dscp-wmm-vo <id1>, <id2>, ...
set uplink {integer}
set uplink-sta {integer}
set wmm [enable|disable]
FortiOS 8.0.0 CLI Reference
2728
Fortinet Inc.

<!-- 来源页 2729 -->
set wmm-be-dscp {integer}
set wmm-bk-dscp {integer}
set wmm-dscp-marking [enable|disable]
set wmm-uapsd [enable|disable]
set wmm-vi-dscp {integer}
set wmm-vo-dscp {integer}
next
end
config wireless-controller qos-profile
Parameter
Description
Type
Size
Default
bandwidth-admission-control
Enable/disable WMM bandwidth admission control.
option
-disable
Option
Description
enable
Enable WMM bandwidth admission control.
disable
Disable WMM bandwidth admission control.
bandwidth-capacity
Maximum bandwidth capacity allowed (1 - 600000
Kbps, default = 2000).
integer
Minimum
value: 1
Maximum
value:
600000
2000
burst
Enable/disable client rate burst.
option
-disable
Option
Description
enable
Enable client rate burst.
disable
Disable client rate burst.
call-admission-control
Enable/disable WMM call admission control.
option
-disable
Option
Description
enable
Enable WMM call admission control.
disable
Disable WMM call admission control.
call-capacity
Maximum number of Voice over WLAN (VoWLAN)
phones allowed (0 - 60, default = 10).
integer
Minimum
value: 0
Maximum
value: 60
10
FortiOS 8.0.0 CLI Reference
2729
Fortinet Inc.

<!-- 来源页 2730 -->
Parameter
Description
Type
Size
Default
comment
Comment.
string
Maximum
length: 63
downlink
Maximum downlink bandwidth for Virtual Access
Points (VAPs) (0 - 2097152 Kbps, default = 0, 0
means no limit).
integer
Minimum
value: 0
Maximum
value:
2097152
0
downlink-sta
Maximum downlink bandwidth for clients (0 -2097152 Kbps, default = 0, 0 means no limit).
integer
Minimum
value: 0
Maximum
value:
2097152
0
dscp-wmm-be <id>
DSCP mapping for best effort access (default = 0
24).
DSCP WMM mapping numbers (0 - 63).
integer
Minimum
value: 0
Maximum
value: 63
dscp-wmm-bk <id>
DSCP mapping for background access (default = 8
16).
DSCP WMM mapping numbers (0 - 63).
integer
Minimum
value: 0
Maximum
value: 63
dscp-wmm-mapping
Enable/disable Differentiated Services Code Point
(DSCP) mapping.
option
-disable
Option
Description
enable
Enable Differentiated Services Code Point (DSCP) mapping.
disable
Disable Differentiated Services Code Point (DSCP) mapping.
dscp-wmm-vi
<id>
DSCP mapping for video access (default = 32 40).
DSCP WMM mapping numbers (0 - 63).
integer
Minimum
value: 0
Maximum
value: 63
dscp-wmm-vo <id>
DSCP mapping for voice access (default = 48 56).
DSCP WMM mapping numbers (0 - 63).
integer
Minimum
value: 0
Maximum
value: 63
name
WiFi QoS profile name.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
2730
Fortinet Inc.

<!-- 来源页 2731 -->
Parameter
Description
Type
Size
Default
uplink
Maximum uplink bandwidth for Virtual Access
Points (VAPs) (0 - 2097152 Kbps, default = 0, 0
means no limit).
integer
Minimum
value: 0
Maximum
value:
2097152
0
uplink-sta
Maximum uplink bandwidth for clients (0 - 2097152
Kbps, default = 0, 0 means no limit).
integer
Minimum
value: 0
Maximum
value:
2097152
0
wmm
Enable/disable WiFi multi-media (WMM) control.
option
-enable
Option
Description
enable
Enable WiFi multi-media (WMM) control.
disable
Disable WiFi multi-media (WMM) control.
wmm-be-dscp
DSCP marking for best effort access (default = 0).
integer
Minimum
value: 0
Maximum
value: 63
0
wmm-bk-dscp
DSCP marking for background access (default = 8).
integer
Minimum
value: 0
Maximum
value: 63
8
wmm-dscp-marking
Enable/disable WMM Differentiated Services Code
Point (DSCP) marking.
option
-disable
Option
Description
enable
Enable WMM Differentiated Services Code Point (DSCP) marking.
disable
Disable WMM Differentiated Services Code Point (DSCP) marking.
wmm-uapsd
Enable/disable WMM Unscheduled Automatic
Power Save Delivery (U-APSD) power save mode.
option
-enable
Option
Description
enable
Enable WMM Unscheduled Automatic Power Save Delivery (U-APSD)
power save mode.
disable
Disable WMM Unscheduled Automatic Power Save Delivery (U-APSD)
power save mode.
FortiOS 8.0.0 CLI Reference
2731
Fortinet Inc.

<!-- 来源页 2732 -->
Parameter
Description
Type
Size
Default
wmm-vi-dscp
DSCP marking for video access (default = 32).
integer
Minimum
value: 0
Maximum
value: 63
32
wmm-vo-dscp
DSCP marking for voice access (default = 48).
integer
Minimum
value: 0
Maximum
value: 63
48
config wireless-controller region
Configure FortiAP regions (for floor plans and maps).
config wireless-controller region
Description: Configure FortiAP regions (for floor plans and maps).
edit <name>
set comments {string}
set grayscale [enable|disable]
set opacity {integer}
next
end
config wireless-controller region
Parameter
Description
Type
Size
Default
comments
Comments.
string
Maximum
length:
1027
grayscale
Region image grayscale.
option
-disable
Option
Description
enable
Enable region image grayscale.
disable
Disable region image grayscale.
name
FortiAP region name.
string
Maximum
length: 35
opacity
Region image opacity (0 - 100).
integer
Minimum
value: 0
Maximum
value: 100
100
FortiOS 8.0.0 CLI Reference
2732
Fortinet Inc.

<!-- 来源页 2733 -->
config wireless-controller setting
VDOM wireless controller configuration.
config wireless-controller setting
Description: VDOM wireless controller configuration.
set account-id {string}
set country [--|AF|...]
set darrp-optimize {integer}
set darrp-optimize-schedules <name1>, <name2>, ...
set device-holdoff {integer}
set device-idle {integer}
set device-weight {integer}
set duplicate-ssid [enable|disable]
set fake-ssid-action {option1}, {option2}, ...
set fapc-compatibility [enable|disable]
set firmware-provision-on-authorization [enable|disable]
config offending-ssid
Description: Configure offending SSID.
edit <id>
set action {option1}, {option2}, ...
set ssid-pattern {string}
next
end
set phishing-ssid-detect [enable|disable]
set rolling-wtp-upgrade [enable|disable]
set wfa-compatibility [enable|disable]
end
config wireless-controller setting
Parameter
Description
Type
Size
Default
account-id
FortiCloud customer account ID.
string
Maximum
length: 63
country
Country or region in which the FortiGate is
located. The country determines the 802.11
bands and channels that are available.
option
-US **
Option
Description
--NO_COUNTRY_SET
AF
AFGHANISTAN
AL
ALBANIA
DZ
ALGERIA
FortiOS 8.0.0 CLI Reference
2733
Fortinet Inc.

<!-- 来源页 2734 -->
Parameter
Description
Type
Size
Default
Option
Description
AS
AMERICAN SAMOA
AO
ANGOLA
AR
ARGENTINA
AM
ARMENIA
AU
AUSTRALIA
AT
AUSTRIA
AZ
AZERBAIJAN
BS
BAHAMAS
BH
BAHRAIN
BD
BANGLADESH
BB
BARBADOS
BY
BELARUS
BE
BELGIUM
BZ
BELIZE
BJ
BENIN
BM
BERMUDA
BT
BHUTAN
BO
BOLIVIA
BA
BOSNIA AND HERZEGOVINA
BW
BOTSWANA
BR
BRAZIL
BN
BRUNEI DARUSSALAM
BG
BULGARIA
BF
BURKINA-FASO
KH
CAMBODIA
CM
CAMEROON
KY
CAYMAN ISLANDS
CF
CENTRAL AFRICA REPUBLIC
TD
CHAD
FortiOS 8.0.0 CLI Reference
2734
Fortinet Inc.

<!-- 来源页 2735 -->
Parameter
Description
Type
Size
Default
Option
Description
CL
CHILE
CN
CHINA
CX
CHRISTMAS ISLAND
CO
COLOMBIA
CG
CONGO REPUBLIC
CD
DEMOCRATIC REPUBLIC OF CONGO
CR
COSTA RICA
HR
CROATIA
CY
CYPRUS
CZ
CZECH REPUBLIC
DK
DENMARK
DJ
DJIBOUTI
DM
DOMINICA
DO
DOMINICAN REPUBLIC
EC
ECUADOR
EG
EGYPT
SV
EL SALVADOR
ET
ETHIOPIA
EE
ESTONIA
GF
FRENCH GUIANA
PF
FRENCH POLYNESIA
FO
FAEROE ISLANDS
FJ
FIJI
FI
FINLAND
FR
FRANCE
GA
GABON
GE
GEORGIA
GM
GAMBIA
DE
GERMANY
FortiOS 8.0.0 CLI Reference
2735
Fortinet Inc.

<!-- 来源页 2736 -->
Parameter
Description
Type
Size
Default
Option
Description
GH
GHANA
GI
GIBRALTAR
GR
GREECE
GL
GREENLAND
GD
GRENADA
GP
GUADELOUPE
GU
GUAM
GT
GUATEMALA
GY
GUYANA
HT
HAITI
HN
HONDURAS
HK
HONG KONG
HU
HUNGARY
IS
ICELAND
IN
INDIA
ID
INDONESIA
IQ
IRAQ
IE
IRELAND
IM
ISLE OF MAN
IL
ISRAEL
IT
ITALY
CI
COTE_D_IVOIRE
JM
JAMAICA
JO
JORDAN
KZ
KAZAKHSTAN
KE
KENYA
KR
KOREA REPUBLIC
KW
KUWAIT
LA
LAOS
FortiOS 8.0.0 CLI Reference
2736
Fortinet Inc.

<!-- 来源页 2737 -->
Parameter
Description
Type
Size
Default
Option
Description
LV
LATVIA
LB
LEBANON
LS
LESOTHO
LR
LIBERIA
LY
LIBYA
LI
LIECHTENSTEIN
LT
LITHUANIA
LU
LUXEMBOURG
MO
MACAU SAR
MK
MACEDONIA, FYRO
MG
MADAGASCAR
MW
MALAWI
MY
MALAYSIA
MV
MALDIVES
ML
MALI
MT
MALTA
MH
MARSHALL ISLANDS
MQ
MARTINIQUE
MR
MAURITANIA
MU
MAURITIUS
YT
MAYOTTE
MX
MEXICO
FM
MICRONESIA
MD
REPUBLIC OF MOLDOVA
MC
MONACO
MN
MONGOLIA
MA
MOROCCO
MZ
MOZAMBIQUE
MM
MYANMAR
FortiOS 8.0.0 CLI Reference
2737
Fortinet Inc.

<!-- 来源页 2738 -->
Parameter
Description
Type
Size
Default
Option
Description
NA
NAMIBIA
NP
NEPAL
NL
NETHERLANDS
AN
NETHERLANDS ANTILLES
AW
ARUBA
NZ
NEW ZEALAND
NI
NICARAGUA
NE
NIGER
NG
NIGERIA
NO
NORWAY
MP
NORTHERN MARIANA ISLANDS
OM
OMAN
PK
PAKISTAN
PW
PALAU
PA
PANAMA
PG
PAPUA NEW GUINEA
PY
PARAGUAY
PE
PERU
PH
PHILIPPINES
PL
POLAND
PT
PORTUGAL
PR
PUERTO RICO
QA
QATAR
RE
REUNION
RO
ROMANIA
RU
RUSSIA
RW
RWANDA
BL
SAINT BARTHELEMY
KN
SAINT KITTS AND NEVIS
FortiOS 8.0.0 CLI Reference
2738
Fortinet Inc.

<!-- 来源页 2739 -->
Parameter
Description
Type
Size
Default
Option
Description
LC
SAINT LUCIA
MF
SAINT MARTIN
PM
SAINT PIERRE AND MIQUELON
VC
SAINT VINCENT AND GRENADIENS
SA
SAUDI ARABIA
SN
SENEGAL
RS
REPUBLIC OF SERBIA
ME
MONTENEGRO
SL
SIERRA LEONE
SG
SINGAPORE
SK
SLOVAKIA
SI
SLOVENIA
SO
SOMALIA
ZA
SOUTH AFRICA
ES
SPAIN
LK
SRI LANKA
SR
SURINAME
SZ
SWAZILAND
SE
SWEDEN
CH
SWITZERLAND
TW
TAIWAN
TZ
TANZANIA
TH
THAILAND
TL
TIMOR-LESTE
TG
TOGO
TT
TRINIDAD AND TOBAGO
TN
TUNISIA
TR
TURKEY
TM
TURKMENISTAN
FortiOS 8.0.0 CLI Reference
2739
Fortinet Inc.

<!-- 来源页 2740 -->
Parameter
Description
Type
Size
Default
Option
Description
AE
UNITED ARAB EMIRATES
TC
TURKS AND CAICOS
UG
UGANDA
UA
UKRAINE
GB
UNITED KINGDOM
US
UNITED STATES
PS
UNITED STATES (PUBLIC SAFETY)
UY
URUGUAY
UZ
UZBEKISTAN
VU
VANUATU
VE
VENEZUELA
VN
VIET NAM
VI
VIRGIN ISLANDS
WF
WALLIS AND FUTUNA
YE
YEMEN
ZM
ZAMBIA
ZW
ZIMBABWE
JP
JAPAN
CA
CANADA
darrp-optimize
Time for running Distributed Automatic Radio
Resource Provisioning (DARRP) optimizations (0 -86400 sec, default = 86400, 0 = disable).
integer
Minimum
value: 0
Maximum
value:
86400
86400
darrp-optimize-schedules
<name>
Firewall schedules for DARRP running time.
DARRP will run periodically based on darrp-optimize within the schedules. Separate multiple
schedule names with a space.
Schedule name.
string
Maximum
length: 35
device-holdoff
Lower limit of creation time of device for
identification in minutes (0 - 60, default = 5).
integer
Minimum
value: 0
Maximum
value: 60
5
FortiOS 8.0.0 CLI Reference
2740
Fortinet Inc.

<!-- 来源页 2741 -->
Parameter
Description
Type
Size
Default
device-idle
Upper limit of idle time of device for identification
in minutes (0 - 14400, default = 1440).
integer
Minimum
value: 0
Maximum
value:
14400
1440
device-weight
Upper limit of confidence of device for
identification (0 - 255, default = 1, 0 = disable).
integer
Minimum
value: 0
Maximum
value: 255
1
duplicate-ssid
Enable/disable allowing Virtual Access Points
(VAPs) to use the same SSID name in the same
VDOM.
option
-disable
Option
Description
enable
Allow VAPs to use the same SSID name in the same VDOM.
disable
Do not allow VAPs to use the same SSID name in the same VDOM.
fake-ssid-action
Actions taken for detected fake SSID.
option
-log
Option
Description
log
Write logs for detected fake SSID.
suppress
Suppress detected fake SSID.
fapc-compatibility
Enable/disable FAP-C series compatibility.
option
-disable
Option
Description
enable
Enable FAP-C series compatibility.
disable
Disable FAP-C series compatibility.
firmware-provision-on-authorization
Enable/disable automatic provisioning of latest
firmware on authorization.
option
-disable
Option
Description
enable
Enable firmware provision on authorization.
disable
Disable firmware provision on authorization.
phishing-ssid-detect
Enable/disable phishing SSID detection.
option
-enable
FortiOS 8.0.0 CLI Reference
2741
Fortinet Inc.

<!-- 来源页 2742 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable phishing SSID detection.
disable
Disable phishing SSID detection.
rolling-wtp-upgrade
Enable/disable rolling WTP upgrade (default =
disable).
option
-disable
Option
Description
enable
Enable rolling WTP upgrade.
disable
Disable rolling WTP upgrade.
wfa-compatibility
Enable/disable WFA compatibility.
option
-disable
Option
Description
enable
Enable Wi-Fi Alliance Certification compatibility.
disable
Disable Wi-Fi Alliance Certification compatibility.
** Values may differ between models.
config offending-ssid
Parameter
Description
Type
Size
Default
action
Actions taken for detected offending SSID.
option
-log
Option
Description
log
Generate logs for detected offending SSID.
suppress
Suppress detected offending SSID.
id
ID.
integer
Minimum
value: 0
Maximum
value:
65535
0
ssid-pattern
Define offending SSID pattern (case insensitive).
For example, word, word*, *word, wo*rd.
string
Maximum
length: 33
config wireless-controller snmp
Configure SNMP.
FortiOS 8.0.0 CLI Reference
2742
Fortinet Inc.

<!-- 来源页 2743 -->
config wireless-controller snmp
Description: Configure SNMP.
config community
Description: SNMP Community Configuration.
edit <id>
config hosts
Description: Configure IPv4 SNMP managers (hosts).
edit <id>
set ip {user}
next
end
config hosts6
Description: Configure IPv6 SNMP managers (hosts).
edit <id>
set ipv6 {ipv6-prefix}
next
end
set name {string}
set query-v1-status [enable|disable]
set query-v2c-status [enable|disable]
set status [enable|disable]
set trap-v1-status [enable|disable]
set trap-v2c-status [enable|disable]
next
end
set contact-info {string}
set engine-id {string}
set trap-high-cpu-threshold {integer}
set trap-high-mem-threshold {integer}
config user
Description: SNMP User Configuration.
edit <name>
set auth-proto [md5|sha|...]
set auth-pwd {password}
set notify-hosts {ipv4-address}
set notify-hosts6 {ipv6-address}
set priv-proto [aes|des|...]
set priv-pwd {password}
set queries [enable|disable]
set security-level [no-auth-no-priv|auth-no-priv|...]
set status [enable|disable]
set trap-status [enable|disable]
next
end
end
FortiOS 8.0.0 CLI Reference
2743
Fortinet Inc.

<!-- 来源页 2744 -->
config wireless-controller snmp
Parameter
Description
Type
Size
Default
contact-info
Contact Information.
string
Maximum
length: 31
engine-id
AC SNMP engineID string (maximum 24
characters).
string
Maximum
length: 23
trap-high-cpu-threshold
CPU usage when trap is sent.
integer
Minimum
value: 10
Maximum
value: 100
80
trap-high-mem-threshold
Memory usage when trap is sent.
integer
Minimum
value: 10
Maximum
value: 100
80
config community
Parameter
Description
Type
Size
Default
id
Community ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
name
Community name.
string
Maximum
length: 35
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
query-v2c-status
Enable/disable SNMP v2c queries.
option
-enable
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
FortiOS 8.0.0 CLI Reference
2744
Fortinet Inc.

<!-- 来源页 2745 -->
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
config hosts
Parameter
Description
Type
Size
Default
id
Host entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
ip
IPv4 address of the SNMP manager (host).
user
Not Specified
config hosts6
Parameter
Description
Type
Size
Default
id
Host6 entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
ipv6
IPv6 address of the SNMP manager (host).
ipv6-prefix
Not Specified
::/0
FortiOS 8.0.0 CLI Reference
2745
Fortinet Inc.

<!-- 来源页 2746 -->
config user
Parameter
Description
Type
Size
Default
auth-proto
Authentication protocol.
option
-sha
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
name
SNMP user name.
string
Maximum
length: 32
notify-hosts
Configure SNMP User Notify Hosts.
ipv4-address
Not
Specified
notify-hosts6
Configure IPv6 SNMP User Notify Hosts.
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
security-level
Security level for message authentication and
encryption.
option
-no-auth-no-priv
FortiOS 8.0.0 CLI Reference
2746
Fortinet Inc.

<!-- 来源页 2747 -->
Parameter
Description
Type
Size
Default
Option
Description
no-auth-no-priv
Message with no authentication and no privacy (encryption).
auth-no-priv
Message with authentication but no privacy (encryption).
auth-priv
Message with authentication and privacy (encryption).
status
SNMP user enable.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
trap-status
Enable/disable traps for this SNMP user.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
config wireless-controller ssid-policy
Configure WiFi SSID policies.
config wireless-controller ssid-policy
Description: Configure WiFi SSID policies.
edit <name>
set description {var-string}
set vlan {string}
next
end
config wireless-controller ssid-policy
Parameter
Description
Type
Size
Default
description
Description.
var-string
Maximum
length: 255
name
Name.
string
Maximum
length: 35
vlan
VLAN interface name.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
2747
Fortinet Inc.

<!-- 来源页 2748 -->
config wireless-controller syslog-profile
Configure Wireless Termination Points (WTP) system log server profile.
config wireless-controller syslog-profile
Description: Configure Wireless Termination Points (WTP) system log server profile.
edit <name>
set comment {var-string}
set log-level [emergency|alert|...]
set server {string}
set server-port {integer}
set server-status [enable|disable]
set server-type [standard|fortianalyzer]
next
end
config wireless-controller syslog-profile
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
log-level
Lowest level of log messages that FortiAP units
send to this server (default = information).
option
-information
Option
Description
emergency
Level 0
alert
Level 1
critical
Level 2
error
Level 3
warning
Level 4
notification
Level 5
information
Level 6
debugging
Level 7
name
WTP system log server profile name.
string
Maximum
length: 35
server
Syslog server CN domain name or IP address.
string
Maximum
length: 63
FortiOS 8.0.0 CLI Reference
2748
Fortinet Inc.

<!-- 来源页 2749 -->
Parameter
Description
Type
Size
Default
server-port
Port number of syslog server that FortiAP units
send log messages to (default = 514).
integer
Minimum
value: 0
Maximum
value:
65535
514
server-status
Enable/disable FortiAP units to send log
messages to a syslog server (default = enable).
option
-enable
Option
Description
enable
Enable syslog server.
disable
Disable syslog server.
server-type
Configure syslog server type (default =
standard).
option
-standard
Option
Description
standard
Standard syslog server hosted on an server endpoint.
fortianalyzer
Syslog server hosted on a FortiAnalyzer device.
config wireless-controller timers
Configure CAPWAP timers.
config wireless-controller timers
Description: Configure CAPWAP timers.
set ap-reboot-wait-interval1 {integer}
set ap-reboot-wait-interval2 {integer}
set ap-reboot-wait-time {string}
set auth-timeout {integer}
set ble-device-cleanup {integer}
set ble-scan-report-intv {integer}
set client-idle-rehome-timeout {integer}
set client-idle-timeout {integer}
set discovery-interval {integer}
set drma-interval {integer}
set echo-interval {integer}
set fake-ap-log {integer}
set ipsec-intf-cleanup {integer}
set keep-alive-interval {integer}
set max-retransmit-interval {integer}
set nat-session-keep-alive {integer}
set radio-stats-interval {integer}
set rogue-ap-cleanup {integer}
set rogue-ap-log {integer}
FortiOS 8.0.0 CLI Reference
2749
Fortinet Inc.

<!-- 来源页 2750 -->
set rogue-sta-cleanup {integer}
set sta-cap-cleanup {integer}
set sta-capability-interval {integer}
set sta-locate-timer {integer}
set sta-offline-cleanup {integer}
set sta-offline-ip2mac-cleanup {integer}
set sta-stats-interval {integer}
set vap-stats-interval {integer}
set wids-entry-cleanup {integer}
end
config wireless-controller timers
Parameter
Description
Type
Size
Default
ap-reboot-wait-interval1
Time in minutes to wait before AP reboots when
there is no controller detected (5 - 65535,
default = 0, 0 for no reboot).
integer
Minimum value:
5 Maximum
value: 65535
0
ap-reboot-wait-interval2
Time in minutes to wait before AP reboots when
there is no controller detected and standalone
SSIDs are pushed to the AP in the previous
session (5 - 65535, default = 0, 0 for no reboot).
integer
Minimum value:
5 Maximum
value: 65535
0
ap-reboot-wait-time
Time to reboot the AP when there is no
controller detected and standalone SSIDs are
pushed to the AP in the previous session,
format hh:mm.
string
Maximum
length: 7
auth-timeout
Time after which a client is considered failed in
RADIUS authentication and times out (5 - 30
sec, default = 5).
integer
Minimum value:
5 Maximum
value: 30
5
ble-device-cleanup
Time period in minutes to keep BLE device after
it is gone (default = 60).
integer
Minimum value:
0 Maximum
value:
4294967295
60
ble-scan-report-intv
Time between running Bluetooth Low Energy
(BLE) reports (10 - 3600 sec, default = 30).
integer
Minimum value:
10 Maximum
value: 3600
30
client-idle-rehome-timeout
Time after which a client is considered idle and
disconnected from the home controller (2 -3600 sec, default = 20, 0 for no timeout).
integer
Minimum value:
2 Maximum
value: 3600
20
client-idle-timeout
Time after which a client is considered idle and
times out (20 - 3600 sec, default = 300, 0 for no
timeout).
integer
Minimum value:
20 Maximum
value: 3600
300
FortiOS 8.0.0 CLI Reference
2750
Fortinet Inc.

<!-- 来源页 2751 -->
Parameter
Description
Type
Size
Default
discovery-interval
Time between discovery requests (2 - 180 sec,
default = 5).
integer
Minimum value:
2 Maximum
value: 180
5
drma-interval
Dynamic radio mode assignment (DRMA)
schedule interval in minutes (1 - 1440, default =
60).
integer
Minimum value:
1 Maximum
value: 1440
60
echo-interval
Time between echo requests sent by the
managed WTP, AP, or FortiAP (1 - 255 sec,
default = 30).
integer
Minimum value:
1 Maximum
value: 255
30
fake-ap-log
Time between recording logs about fake APs if
periodic fake AP logging is configured (1 - 1440
min, default = 1).
integer
Minimum value:
1 Maximum
value: 1440
1
ipsec-intf-cleanup
Time period to keep IPsec VPN interfaces up
after WTP sessions are disconnected (30 -3600 sec, default = 120).
integer
Minimum value:
30 Maximum
value: 3600
120
keep-alive-interval *
Time between data keep alive message sent by
the managed WTP, AP, or FortiAP (1 - 255 sec,
default = 0 which means the interval is derived
from the echo-interval setting).
integer
Minimum value:
0 Maximum
value: 255
0
max-retransmit-interval *
Maximal time to retransmit a control packet by
the managed WTP, AP, or FortiAP (2 - 255 sec,
default = 0 which means the interval is derived
from the echo-interval setting).
integer
Minimum value:
2 Maximum
value: 255
0
nat-session-keep-alive
Maximal time in seconds between control
requests sent by the managed WTP, AP, or
FortiAP (0 - 255 sec, default = 0).
integer
Minimum value:
0 Maximum
value: 255
0
radio-stats-interval
Time between running radio reports (1 - 255
sec, default = 15).
integer
Minimum value:
1 Maximum
value: 255
15
rogue-ap-cleanup
Time period in minutes to keep rogue AP after it
is gone (default = 0).
integer
Minimum value:
0 Maximum
value:
4294967295
0
rogue-ap-log
Time between logging rogue AP messages if
periodic rogue AP logging is configured (0 -1440 min, default = 0).
integer
Minimum value:
0 Maximum
value: 1440
0
rogue-sta-cleanup
Time period in minutes to keep rogue station
after it is gone (default = 0).
integer
Minimum value:
0 Maximum
value:
4294967295
0
FortiOS 8.0.0 CLI Reference
2751
Fortinet Inc.

<!-- 来源页 2752 -->
Parameter
Description
Type
Size
Default
sta-cap-cleanup
Time period in minutes to keep station
capability data after it is gone (default = 0).
integer
Minimum value:
0 Maximum
value:
4294967295
0
sta-capability-interval
Time between running station capability reports
(1 - 255 sec, default = 30).
integer
Minimum value:
1 Maximum
value: 255
30
sta-locate-timer
Time between running client presence flushes
to remove clients that are listed but no longer
present (0 - 86400 sec, default = 1800).
integer
Minimum value:
0 Maximum
value: 86400
1800
sta-offline-cleanup
Time period in seconds to keep station offline
data after it is gone (default = 300).
integer
Minimum value:
0 Maximum
value:
4294967295
300
sta-offline-ip2mac-cleanup
Time period in seconds to keep station offline
Ip2mac data after it is gone (default = 300).
integer
Minimum value:
0 Maximum
value:
4294967295
300
sta-stats-interval
Time between running client (station) reports (1
- 255 sec, default = 10).
integer
Minimum value:
1 Maximum
value: 255
10
vap-stats-interval
Time between running Virtual Access Point
(VAP) reports (1 - 255 sec, default = 15).
integer
Minimum value:
1 Maximum
value: 255
15
wids-entry-cleanup
Time period in minutes to keep wids entry after
it is gone (default = 0).
integer
Minimum value:
0 Maximum
value:
4294967295
0
* This parameter may not exist in some models.
config wireless-controller vap
Configure Virtual Access Points (VAPs).
config wireless-controller vap
Description: Configure Virtual Access Points (VAPs).
edit <name>
set 80211k [disable|enable]
set 80211v [disable|enable]
set access-control-list {string}
set additional-akms {option1}, {option2}, ...
set address-group {string}
FortiOS 8.0.0 CLI Reference
2752
Fortinet Inc.

<!-- 来源页 2753 -->
set address-group-policy [disable|allow|...]
set akm24-only [disable|enable]
set antivirus-profile {string}
set application-detection-engine [enable|disable]
set application-dscp-marking [enable|disable]
set application-list {string}
set application-report-intv {integer}
set atf-weight {integer}
set auth [radius|usergroup]
set auth-cert {string}
set auth-portal-addr {string}
set beacon-advertising {option1}, {option2}, ...
set beacon-protection [disable|enable]
set broadcast-ssid [enable|disable]
set broadcast-suppression {option1}, {option2}, ...
set bss-color-partial [enable|disable]
set bstm-disassociation-imminent [enable|disable]
set bstm-load-balancing-disassoc-timer {integer}
set bstm-rssi-disassoc-timer {integer}
set called-station-id-type [mac|ip|...]
set captive-network-assistant-bypass [enable|disable]
set captive-portal [enable|disable]
set captive-portal-ac-name {string}
set captive-portal-auth-timeout {integer}
set captive-portal-dynamic-redirect-url [enable|disable]
set captive-portal-fw-accounting [enable|disable]
set dhcp-address-enforcement [enable|disable]
set dhcp-lease-time {integer}
set dhcp-option43-insertion [enable|disable]
set dhcp-option82-circuit-id-insertion {option1}, {option2}, ...
set dhcp-option82-delimiter {string}
set dhcp-option82-insertion [enable|disable]
set dhcp-option82-remote-id-insertion {option1}, {option2}, ...
set domain-name-stripping [disable|enable]
set dynamic-vlan [enable|disable]
set eap-reauth [enable|disable]
set eap-reauth-intv {integer}
set eapol-key-retries [disable|enable]
set encrypt [TKIP|AES|...]
set external-logout {string}
set external-pre-auth [enable|disable]
set external-web {var-string}
set external-web-format [auto-detect|no-query-string|...]
set fast-bss-transition [disable|enable]
set ft-mobility-domain {integer}
set ft-over-ds [disable|enable]
set ft-r0-key-lifetime {integer}
set gas-comeback-delay {integer}
set gas-fragmentation-limit {integer}
set gtk-rekey [enable|disable]
set gtk-rekey-intv {integer}
set high-efficiency [enable|disable]
FortiOS 8.0.0 CLI Reference
2753
Fortinet Inc.

<!-- 来源页 2754 -->
set hotspot20-profile {string}
set igmp-snooping [enable|disable]
set intra-vap-privacy [enable|disable]
set ip {ipv4-classnet-host}
set ips-sensor {string}
set ipv6-rules {option1}, {option2}, ...
set key {password}
set keyindex {integer}
set l3-roaming [enable|disable]
set l3-roaming-mode [direct|indirect]
set ldpc [disable|rx|...]
set local-authentication [enable|disable]
set local-bridging [enable|disable]
set local-lan [allow|deny]
set local-lan-partition [enable|disable]
set local-standalone [enable|disable]
set local-standalone-dns [enable|disable]
set local-standalone-dns-ip {ipv4-address}
set local-standalone-nat [enable|disable]
set mac-auth-bypass [enable|disable]
set mac-called-station-delimiter [hyphen|single-hyphen|...]
set mac-calling-station-delimiter [hyphen|single-hyphen|...]
set mac-case [uppercase|lowercase]
set mac-password-delimiter [hyphen|single-hyphen|...]
set mac-username-delimiter [hyphen|single-hyphen|...]
set max-clients {integer}
set max-clients-ap {integer}
set mbo [disable|enable]
set mbo-cell-data-conn-pref [excluded|prefer-not|...]
set me-disable-thresh {integer}
set mesh-backhaul [enable|disable]
set mlo [disable|enable]
set mpsk-profile {string}
set mu-mimo [enable|disable]
set multicast-enhance [enable|disable]
set multicast-rate [0|6000|...]
set nac [enable|disable]
set nac-profile {string}
set nas-filter-rule [enable|disable]
set neighbor-report-dual-band [disable|enable]
set okc [disable|enable]
set osen [enable|disable]
set owe-groups {option1}, {option2}, ...
set owe-transition [disable|enable]
set owe-transition-ssid {string}
set passphrase {password}
set pmf [disable|enable|...]
set pmf-assoc-comeback-timeout {integer}
set pmf-sa-query-retry-timeout {integer}
set port-macauth [disable|radius|...]
set port-macauth-reauth-timeout {integer}
set port-macauth-timeout {integer}
FortiOS 8.0.0 CLI Reference
2754
Fortinet Inc.

<!-- 来源页 2755 -->
set portal-message-override-group {string}
config portal-message-overrides
Description: Individual message overrides.
set auth-disclaimer-page {string}
set auth-login-failed-page {string}
set auth-login-page {string}
set auth-reject-page {string}
end
set portal-type [auth|auth+disclaimer|...]
set pre-auth [enable|disable]
set primary-wag-profile {string}
set probe-resp-suppression [enable|disable]
set probe-resp-threshold {string}
set ptk-rekey [enable|disable]
set ptk-rekey-intv {integer}
set qos-profile {string}
set quarantine [enable|disable]
set radio-2g-threshold {string}
set radio-5g-threshold {string}
set radio-sensitivity [enable|disable]
set radius-auth-surviv-intv {integer}
set radius-auth-survivability [disable|enable]
set radius-mac-auth [enable|disable]
set radius-mac-auth-block-interval {integer}
set radius-mac-auth-server {string}
set radius-mac-auth-usergroups <name1>, <name2>, ...
set radius-mac-mpsk-auth [enable|disable]
set radius-mac-mpsk-timeout {integer}
set radius-server {string}
set rates-11a {option1}, {option2}, ...
set rates-11ac-mcs-map {string}
set rates-11ax-mcs-map {string}
set rates-11be-mcs-map {string}
set rates-11be-mcs-map-160 {string}
set rates-11be-mcs-map-320 {string}
set rates-11bg {option1}, {option2}, ...
set rates-11n-ss12 {option1}, {option2}, ...
set rates-11n-ss34 {option1}, {option2}, ...
set roaming-acct-interim-update [enable|disable]
set sae-groups {option1}, {option2}, ...
set sae-h2e-only [enable|disable]
set sae-hnp-only [enable|disable]
set sae-password {password}
set sae-pk [enable|disable]
set sae-private-key {string}
set scan-botnet-connections [disable|monitor|...]
set schedule <name1>, <name2>, ...
set secondary-wag-profile {string}
set security [open|wep64|...]
set security-exempt-list {string}
set security-redirect-url {var-string}
set selected-usergroups <name1>, <name2>, ...
FortiOS 8.0.0 CLI Reference
2755
Fortinet Inc.

<!-- 来源页 2756 -->
set split-tunneling [enable|disable]
set ssid {string}
set sticky-client-remove [enable|disable]
set sticky-client-threshold-2g {string}
set sticky-client-threshold-5g {string}
set sticky-client-threshold-6g {string}
set target-wake-time [enable|disable]
set tkip-counter-measure [enable|disable]
set tunnel-echo-interval {integer}
set tunnel-fallback-interval {integer}
set usergroup <name1>, <name2>, ...
set utm-log [enable|disable]
set utm-profile {string}
set utm-status [enable|disable]
set vlan-auto [enable|disable]
config vlan-name
Description: Table for mapping VLAN name to VLAN ID.
edit <name>
set vlan-id {integer}
next
end
config vlan-pool
Description: VLAN pool.
edit <id>
set wtp-group <name1>, <name2>, ...
next
end
set vlan-pooling [wtp-group|round-robin|...]
set vlanid {integer}
set webfilter-profile {string}
next
end
config wireless-controller vap
Parameter
Description
Type
Size
Default
80211k
Enable/disable 802.11k assisted
roaming (default = enable).
option
-enable
Option
Description
disable
Disable 802.11k assisted roaming.
enable
Enable 802.11k assisted roaming.
80211v
Enable/disable 802.11v assisted
roaming (default = enable).
option
-enable
FortiOS 8.0.0 CLI Reference
2756
Fortinet Inc.

<!-- 来源页 2757 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable 802.11v assisted roaming.
enable
Enable 802.11v assisted roaming.
access-control-list
Profile name for access-control-list.
string
Maximum
length: 35
additional-akms
Additional AKMs.
option
-Option
Description
akm6
Use AKM suite employing PSK_SHA256.
akm24
Use AKM suite employing SAE_EXT.
address-group
Firewall Address Group Name.
string
Maximum
length: 79
address-group-policy
Configure MAC address filtering policy
for MAC addresses that are in the
address-group.
option
-disable
Option
Description
disable
Disable MAC address filtering policy for MAC addresses that are in
the address-group
allow
Allow clients with MAC addresses that are in the address-group.
deny
Block clients with MAC addresses that are in the address-group.
akm24-only
WPA3 SAE using group-dependent
hash only (default = disable).
option
-disable
Option
Description
disable
Disable WPA3 SAE using group-dependent hash only.
enable
Enable WPA3 SAE using group-dependent hash only.
antivirus-profile
AntiVirus profile name.
string
Maximum
length: 47
application-detection-engine
Enable/disable application detection
engine (default = disable).
option
-disable
Option
Description
enable
Enable application detection engine.
disable
Disable application detection engine.
FortiOS 8.0.0 CLI Reference
2757
Fortinet Inc.

<!-- 来源页 2758 -->
Parameter
Description
Type
Size
Default
application-dscp-marking
Enable/disable application attribute
based DSCP marking (default =
disable).
option
-disable
Option
Description
enable
Enable application based DSCP marking.
disable
Disable application based DSCP marking.
application-list
Application control list name.
string
Maximum
length: 47
application-report-intv
Application report interval (30 -864000 sec, default = 120).
integer
Minimum value:
30 Maximum
value: 864000
120
atf-weight
Airtime weight in percentage (default =
20).
integer
Minimum value:
0 Maximum
value: 100
20
auth
Authentication protocol.
option
-Option
Description
radius
Use a RADIUS server to authenticate clients.
usergroup
Use a firewall usergroup to authenticate clients.
auth-cert
HTTPS server certificate.
string
Maximum
length: 35
auth-portal-addr
Address of captive portal.
string
Maximum
length: 63
beacon-advertising
Fortinet beacon advertising IE data
(default = empty).
option
-Option
Description
name
AP name.
model
AP model abbreviation.
serial-number
AP serial number.
beacon-protection
Enable/disable beacon protection
support (default = disable).
option
-disable
Option
Description
disable
Disable beacon protection.
enable
Enable beacon protection.
FortiOS 8.0.0 CLI Reference
2758
Fortinet Inc.

<!-- 来源页 2759 -->
Parameter
Description
Type
Size
Default
broadcast-ssid
Enable/disable broadcasting the SSID
(default = enable).
option
-enable
Option
Description
enable
Enable broadcasting the SSID.
disable
Disable broadcasting the SSID.
broadcast-suppression
Optional suppression of broadcast
messages. For example, you can keep
DHCP messages, ARP broadcasts, and
so on off of the wireless network.
option
-dhcp-up
dhcp-ucast
arp-known
Option
Description
dhcp-up
Suppress broadcast uplink DHCP messages.
dhcp-down
Suppress broadcast downlink DHCP messages.
dhcp-starvation
Suppress broadcast DHCP starvation req messages.
dhcp-ucast
Convert downlink broadcast DHCP messages to unicast messages.
arp-known
Suppress broadcast ARP for known wireless clients.
arp-unknown
Suppress broadcast ARP for unknown wireless clients.
arp-reply
Suppress broadcast ARP reply from wireless clients.
arp-poison
Suppress ARP poison messages from wireless clients.
arp-proxy
Reply ARP requests for wireless clients as a proxy.
netbios-ns
Suppress NetBIOS name services packets with UDP port 137.
netbios-ds
Suppress NetBIOS datagram services packets with UDP port 138.
ipv6
Suppress IPv6 packets.
all-other-mc
Suppress all other multicast messages.
all-other-bc
Suppress all other broadcast messages.
bss-color-partial
Enable/disable 802.11ax partial BSS
color (default = enable).
option
-enable
Option
Description
enable
Enable 802.11ax partial BSS color.
disable
Disable 802.11ax partial BSS color.
FortiOS 8.0.0 CLI Reference
2759
Fortinet Inc.

<!-- 来源页 2760 -->
Parameter
Description
Type
Size
Default
bstm-disassociation-imminent
Enable/disable forcing of
disassociation after the BSTM request
timer has been reached (default =
enable).
option
-enable
Option
Description
enable
Enable BSTM disassociation imminent.
disable
Disable BSTM disassociation imminent.
bstm-load-balancing-disassoc-timer
Time interval for client to voluntarily
leave AP before forcing a
disassociation due to AP load-balancing (0 to 30, default = 10).
integer
Minimum value:
1 Maximum
value: 30
10
bstm-rssi-disassoc-timer
Time interval for client to voluntarily
leave AP before forcing a
disassociation due to low RSSI (0 to
2000, default = 200).
integer
Minimum value:
1 Maximum
value: 2000
200
called-station-id-type
The format type of RADIUS attribute
Called-Station-Id (default = mac).
option
-mac
Option
Description
mac
Use MAC:SSID format.
ip
Use IP:SSID format.
apname
Use APName:SSID format.
captive-network-assistant-bypass
Enable/disable Captive Network
Assistant bypass.
option
-disable
Option
Description
enable
Enable captive bypass.
disable
Disable captive bypass.
captive-portal
Enable/disable captive portal.
option
-disable
Option
Description
enable
Enable captive portal.
disable
Disable captive portal.
captive-portal-ac-name
Local-bridging captive portal ac-name.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
2760
Fortinet Inc.

<!-- 来源页 2761 -->
Parameter
Description
Type
Size
Default
captive-portal-auth-timeout
Hard timeout - AP will always clear the
session after timeout regardless of
traffic (0 - 864000 sec, default = 0).
integer
Minimum value:
0 Maximum
value: 864000
0
captive-portal-dynamic-redirect-url *
Enable/disable captive portal dynamic
redirect URL (default = disable).
option
-disable
Option
Description
enable
Enable captive portal dynamic redirect URL.
disable
Disable captive portal dynamic redirect URL.
captive-portal-fw-accounting
Enable/disable RADIUS accounting for
captive portal firewall authentication
session.
option
-disable
Option
Description
enable
Enable RADIUS accounting for captive portal firewall authentication
session.
disable
Disable RADIUS accounting for captive portal firewall authentication
session.
dhcp-address-enforcement
Enable/disable DHCP address
enforcement (default = disable).
option
-disable
Option
Description
enable
Enable DHCP enforcement, data from clients that have not
completed the DHCP process will be blocked.
disable
Disable DHCP enforcement, clients can access the network without
DHCP process.
dhcp-lease-time
DHCP lease time in seconds for NAT IP
address.
integer
Minimum value:
300 Maximum
value:
8640000
2400
dhcp-option43-insertion
Enable/disable insertion of DHCP
option 43 (default = enable).
option
-enable
Option
Description
enable
Enable insertion of DHCP option 43.
disable
Disable insertion of DHCP option 43.
FortiOS 8.0.0 CLI Reference
2761
Fortinet Inc.

<!-- 来源页 2762 -->
Parameter
Description
Type
Size
Default
dhcp-option82-circuit-id-insertion
Selected fields of DHCP option 82
circuit-id insert.
option
-**
Option
Description
ap-mac
AP MAC.
ap-model
AP Model.
ap-hostname
AP Hostname.
ssid
SSID.
ssid-type
SSID Type.
network-type
Network Type.
vlan
VLAN ID.
wtp-profile
WTP Profile Name.
style-1
ASCII string composed of AP-MAC;SSID;SSID-TYPE. For example,
"xx:xx:xx:xx:xx:xx;wifi;s".
style-2
ASCII string composed of AP-MAC. For example, "xx:xx:xx:xx:xx:xx".
style-3
ASCII string composed of NETWORK-TYPE:WTPPROF-NAME:VLAN:SSID:AP-MODEL:AP-HOSTNAME:AP-MAC. For
example,"WLAN:FAPS221E-default:100:wifi:PS221E:FortiAP-S221E:xx:xx:xx:xx:xx:xx".
disable
Disable DHCP option 82 circuit-id insert.
dhcp-option82-delimiter *
DHCP option 82 field delimiter.
string
Maximum
length: 4
;
dhcp-option82-insertion
Enable/disable DHCP option 82 insert
(default = disable).
option
-disable
Option
Description
enable
Enable DHCP option 82 insert.
disable
Disable DHCP option 82 insert.
dhcp-option82-remote-id-insertion
Selected fields of DHCP option 82
remote-id insert.
option
-**
Option
Description
client-mac
Client MAC.
FortiOS 8.0.0 CLI Reference
2762
Fortinet Inc.

<!-- 来源页 2763 -->
Parameter
Description
Type
Size
Default
Option
Description
style-1
ASCII string in the format "xx:xx:xx:xx:xx:xx" containing MAC address
of client device.
disable
Disable DHCP option 82 remote-id insert.
domain-name-stripping
Enable/disable stripping domain name
from identity (default = disable).
option
-disable
Option
Description
disable
Disable stripping domain name from identity.
enable
Enable stripping domain name from identity.
dynamic-vlan
Enable/disable dynamic VLAN
assignment.
option
-disable
Option
Description
enable
Enable dynamic VLAN assignment.
disable
Disable dynamic VLAN assignment.
eap-reauth
Enable/disable EAP re-authentication
for WPA-Enterprise security.
option
-disable
Option
Description
enable
Enable EAP re-authentication for WPA-Enterprise security.
disable
Disable EAP re-authentication for WPA-Enterprise security.
eap-reauth-intv
EAP re-authentication interval (1800 -864000 sec, default = 86400).
integer
Minimum value:
1800 Maximum
value: 864000
86400
eapol-key-retries
Enable/disable retransmission of
EAPOL-Key frames (message 3/4 and
group message 1/2) (default = enable).
option
-enable
Option
Description
disable
Disable retransmission of EAPOL-Key frames (message 3/4 and
group message 1/2).
enable
Enable retransmission of EAPOL-Key frames (message 3/4 and
group message 1/2).
FortiOS 8.0.0 CLI Reference
2763
Fortinet Inc.

<!-- 来源页 2764 -->
Parameter
Description
Type
Size
Default
encrypt
Encryption protocol to use (only
available when security is set to a WPA
type).
option
-AES
Option
Description
TKIP
Use TKIP encryption.
AES
Use AES encryption.
TKIP-AES
Use TKIP and AES encryption.
external-logout
URL of external authentication logout
server.
string
Maximum
length: 127
external-pre-auth
Enable/disable pre-authentication with
external APs not managed by the
FortiGate (default = disable).
option
-disable
Option
Description
enable
Enable pre-authentication with external APs.
disable
Disable pre-authentication with external APs.
external-web
URL of external authentication web
server.
var-string
Maximum
length: 1023
external-web-format
URL query parameter detection (default
= auto-detect).
option
-auto-detect
Option
Description
auto-detect
Automatically detect if "external-web" URL has any query parameter.
no-query-string
"external-web" URL does not have any query parameter.
partial-query-string
"external-web" URL has some query parameters.
fast-bss-transition
Enable/disable 802.11r Fast BSS
Transition (FT) (default = disable).
option
-disable
Option
Description
disable
Disable 802.11r Fast BSS Transition (FT).
enable
Enable 802.11r Fast BSS Transition (FT).
ft-mobility-domain
Mobility domain identifier in FT (1 -65535, default = 1000).
integer
Minimum value:
1 Maximum
value: 65535
1000
FortiOS 8.0.0 CLI Reference
2764
Fortinet Inc.

<!-- 来源页 2765 -->
Parameter
Description
Type
Size
Default
ft-over-ds
Enable/disable FT over the Distribution
System (DS).
option
-disable
Option
Description
disable
Disable FT over the Distribution System (DS).
enable
Enable FT over the Distribution System (DS).
ft-r0-key-lifetime
Lifetime of the PMK-R0 key in FT, 1-65535 minutes.
integer
Minimum value:
1 Maximum
value: 65535
480
gas-comeback-delay
GAS comeback delay (0 or 100 - 10000
milliseconds, default = 500).
integer
Minimum value:
100 Maximum
value: 10000
500
gas-fragmentation-limit
GAS fragmentation limit (512 - 4096,
default = 1024).
integer
Minimum value:
512 Maximum
value: 4096
1024
gtk-rekey
Enable/disable GTK rekey for WPA
security.
option
-disable
Option
Description
enable
Enable GTK rekey for WPA security.
disable
Disable GTK rekey for WPA security.
gtk-rekey-intv
GTK rekey interval (600 - 864000 sec,
default = 86400).
integer
Minimum value:
600 Maximum
value: 864000
86400
high-efficiency
Enable/disable 802.11ax high efficiency
(default = enable).
option
-enable
Option
Description
enable
Enable 802.11ax high efficiency.
disable
Disable 802.11ax high efficiency.
hotspot20-profile
Hotspot 2.0 profile name.
string
Maximum
length: 35
igmp-snooping
Enable/disable IGMP snooping.
option
-disable
Option
Description
enable
Enable IGMP snooping.
disable
Disable IGMP snooping.
FortiOS 8.0.0 CLI Reference
2765
Fortinet Inc.

<!-- 来源页 2766 -->
Parameter
Description
Type
Size
Default
intra-vap-privacy
Enable/disable blocking communication
between clients on the same SSID
(called intra-SSID privacy) (default =
disable).
option
-disable
Option
Description
enable
Enable intra-SSID privacy.
disable
Disable intra-SSID privacy.
ip
IP address and subnet mask for the
local standalone NAT subnet.
ipv4-classnet-host
Not Specified
0.0.0.0
0.0.0.0
ips-sensor
IPS sensor name.
string
Maximum
length: 47
ipv6-rules
Optional rules of IPv6 packets. For
example, you can keep RA, RS and so
on off of the wireless network.
option
-drop-icmp6ra
drop-icmp6rs
drop-llmnr6
drop-icmp6mld2
drop-dhcp6s
drop-dhcp6c
ndp-proxy
drop-ns-dad
Option
Description
drop-icmp6ra
Drop ICMP6 Router Advertisement (RA) packets that originate from
wireless clients.
drop-icmp6rs
Drop ICMP6 Router Solicitation (RS) packets to be sent to wireless
clients.
drop-llmnr6
Drop Link-Local Multicast Name Resolution (LLMNR) packets
drop-icmp6mld2
Drop ICMP6 Multicast Listener Report V2 (MLD2) packets
drop-dhcp6s
Drop DHCP6 server generated packets that originate from wireless
clients.
drop-dhcp6c
Drop DHCP6 client generated packets to be sent to wireless clients.
ndp-proxy
Enable IPv6 ndp proxy - send back na on behalf of the client and drop
the ns.
FortiOS 8.0.0 CLI Reference
2766
Fortinet Inc.

<!-- 来源页 2767 -->
Parameter
Description
Type
Size
Default
Option
Description
drop-ns-dad
Drop ICMP6 NS-DAD when target address is not found in ndp proxy
cache.
drop-ns-nondad
Drop ICMP6 NS-NonDAD when target address is not found in ndp
proxy cache.
key
WEP Key.
password
Not Specified
keyindex
WEP key index (1 - 4).
integer
Minimum value:
1 Maximum
value: 4
1
l3-roaming
Enable/disable layer 3 roaming (default
= disable).
option
-disable
Option
Description
enable
Enable layer 3 roaming.
disable
Disable layer 3 roaming.
l3-roaming-mode
Select the way that layer 3 roaming
traffic is passed (default = direct).
option
-direct
Option
Description
direct
Layer 3 roaming traffic is passed between home AP and guest AP
directly.
indirect
Layer 3 roaming traffic is passed between home AP and guest AP
through controllers.
ldpc
VAP low-density parity-check (LDPC)
coding configuration.
option
-rxtx
Option
Description
disable
Disable LDPC.
rx
Enable LDPC when receiving traffic.
tx
Enable LDPC when transmitting traffic.
rxtx
Enable LDPC when both receiving and transmitting traffic.
local-authentication
Enable/disable AP local authentication.
option
-disable
FortiOS 8.0.0 CLI Reference
2767
Fortinet Inc.

<!-- 来源页 2768 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable AP local authentication.
disable
Disable AP local authentication.
local-bridging
Enable/disable bridging of wireless and
Ethernet interfaces on the FortiAP
(default = disable).
option
-disable
Option
Description
enable
Enable AP local VAP to Ethernet bridging.
disable
Disable AP local VAP to Ethernet bridging.
local-lan
Allow/deny traffic destined for a Class
A, B, or C private IP address (default =
allow).
option
-allow
Option
Description
allow
Allow traffic destined for a Class A, B, or C private IP address.
deny
Deny traffic destined for a Class A, B, or C private IP address.
local-lan-partition
Enable/disable segregating client
traffic to local LAN side (default =
disable).
option
-disable
Option
Description
enable
Enable AP local LAN segregation.
disable
Disable AP local LAN segregation.
local-standalone
Enable/disable AP local standalone
(default = disable).
option
-disable
Option
Description
enable
Enable AP local standalone.
disable
Disable AP local standalone.
local-standalone-dns
Enable/disable AP local standalone
DNS.
option
-disable
Option
Description
enable
Enable AP local standalone DNS.
disable
Disable AP local standalone DNS.
FortiOS 8.0.0 CLI Reference
2768
Fortinet Inc.

<!-- 来源页 2769 -->
Parameter
Description
Type
Size
Default
local-standalone-dns-ip
IPv4 addresses for the local standalone
DNS.
ipv4-address
Not Specified
local-standalone-nat
Enable/disable AP local standalone
NAT mode.
option
-disable
Option
Description
enable
Enable AP local standalone NAT mode.
disable
Disable AP local standalone NAT mode.
mac-auth-bypass
Enable/disable MAC authentication
bypass.
option
-disable
Option
Description
enable
Enable MAC authentication bypass.
disable
Disable MAC authentication bypass.
mac-called-station-delimiter
MAC called station delimiter (default =
hyphen).
option
-hyphen
Option
Description
hyphen
Use hyphen as delimiter for called station.
single-hyphen
Use single hyphen as delimiter for called station.
colon
Use colon as delimiter for called station.
none
No delimiter for called station.
mac-calling-station-delimiter
MAC calling station delimiter (default =
hyphen).
option
-hyphen
Option
Description
hyphen
Use hyphen as delimiter for calling station.
single-hyphen
Use single hyphen as delimiter for calling station.
colon
Use colon as delimiter for calling station.
none
No delimiter for calling station.
mac-case
MAC case (default = uppercase).
option
-uppercase
Option
Description
uppercase
Use uppercase MAC.
lowercase
Use lowercase MAC.
FortiOS 8.0.0 CLI Reference
2769
Fortinet Inc.

<!-- 来源页 2770 -->
Parameter
Description
Type
Size
Default
mac-password-delimiter
MAC authentication password delimiter
(default = hyphen).
option
-hyphen
Option
Description
hyphen
Use hyphen as delimiter for MAC auth password.
single-hyphen
Use single hyphen as delimiter for MAC auth password.
colon
Use colon as delimiter for MAC auth password.
none
No delimiter for MAC auth password.
mac-username-delimiter
MAC authentication username delimiter
(default = hyphen).
option
-hyphen
Option
Description
hyphen
Use hyphen as delimiter for MAC auth username.
single-hyphen
Use single hyphen as delimiter for MAC auth username.
colon
Use colon as delimiter for MAC auth username.
none
No delimiter for MAC auth username.
max-clients
Maximum number of clients that can
connect simultaneously to the VAP
(default = 0, meaning no limitation).
integer
Minimum value:
0 Maximum
value:
4294967295
0
max-clients-ap
Maximum number of clients that can
connect simultaneously to the VAP per
AP radio (default = 0, meaning no
limitation).
integer
Minimum value:
0 Maximum
value:
4294967295
0
mbo
Enable/disable Multiband Operation
(default = disable).
option
-disable
Option
Description
disable
Disable Multiband Operation (MBO).
enable
Enable Multiband Operation (MBO).
mbo-cell-data-conn-pref
MBO cell data connection preference
(0, 1, or 255, default = 1).
option
-prefer-not
Option
Description
excluded
Wi-Fi Agile Multiband AP does not want the Wi-Fi Agile Multiband
STA to use the cellular data connection.
FortiOS 8.0.0 CLI Reference
2770
Fortinet Inc.

<!-- 来源页 2771 -->
Parameter
Description
Type
Size
Default
Option
Description
prefer-not
Wi-Fi Agile Multiband AP prefers the Wi-Fi Agile Multiband STA
should not use cellular data connection.
prefer-use
Wi-Fi Agile Multiband AP prefers the Wi-Fi Agile Multiband STA
should use cellular data connection.
me-disable-thresh
Disable multicast enhancement when
this many clients are receiving
multicast traffic.
integer
Minimum value:
2 Maximum
value: 256
32
mesh-backhaul
Enable/disable using this VAP as a WiFi
mesh backhaul (default = disable). This
entry is only available when security is
set to a WPA type or open.
option
-disable
Option
Description
enable
Enable mesh backhaul.
disable
Disable mesh backhaul.
mlo
Enable/disable WiFi7 Multi-Link-Operation (default = disable).
option
-disable
Option
Description
disable
Disable WiFi7 Multi-Link-Operation.
enable
Enable WiFi7 Multi-Link-Operation.
mpsk-profile
MPSK profile name.
string
Maximum
length: 35
mu-mimo
Enable/disable Multi-user MIMO
(default = enable).
option
-enable
Option
Description
enable
Enable Multi-user MIMO.
disable
Disable Multi-user MIMO.
multicast-enhance
Enable/disable converting multicast to
unicast to improve performance
(default = disable).
option
-disable
Option
Description
enable
Enable multicast enhancement.
disable
Disable multicast enhancement.
FortiOS 8.0.0 CLI Reference
2771
Fortinet Inc.

<!-- 来源页 2772 -->
Parameter
Description
Type
Size
Default
multicast-rate
Multicast rate (0, 6000, 12000, or
24000 kbps, default = 0).
option
-0
Option
Description
0
Use the default multicast rate.
6000
6 Mbps.
12000
12 Mbps.
24000
24 Mbps.
nac
Enable/disable network access control.
option
-disable
Option
Description
enable
Enable network access control.
disable
Disable network access control.
nac-profile
NAC profile name.
string
Maximum
length: 35
name
Virtual AP name.
string
Maximum
length: 15
nas-filter-rule
Enable/disable NAS filter rule support
(default = disable).
option
-disable
Option
Description
enable
Enable NAS filter rule for RADIUS server.
disable
Disable NAS filter rule for RADIUS server.
neighbor-report-dual-band
Enable/disable dual-band neighbor
report (default = disable).
option
-disable
Option
Description
disable
Disable dual-band neighbor report.
enable
Enable dual-band neighbor report.
okc
Enable/disable Opportunistic Key
Caching (OKC) (default = enable).
option
-enable
Option
Description
disable
Disable Opportunistic Key Caching (OKC).
enable
Enable Opportunistic Key Caching (OKC).
FortiOS 8.0.0 CLI Reference
2772
Fortinet Inc.

<!-- 来源页 2773 -->
Parameter
Description
Type
Size
Default
osen
Enable/disable OSEN as part of key
management (default = disable).
option
-disable
Option
Description
enable
Enable OSEN auth.
disable
Disable OSEN auth.
owe-groups
OWE-Groups.
option
-Option
Description
19
DH Group 19.
20
DH Group 20.
21
DH Group 21.
owe-transition
Enable/disable OWE transition mode
support.
option
-disable
Option
Description
disable
Disable OWE transition mode support.
enable
Enable OWE transition mode support.
owe-transition-ssid
OWE transition mode peer SSID.
string
Maximum
length: 32
passphrase
WPA pre-shared key (PSK) to be used
to authenticate WiFi users.
password
Not Specified
pmf
Protected Management Frames (PMF)
support (default = disable).
option
-disable
Option
Description
disable
Disable PMF completely.
enable
Enable PMF but deny clients without PMF.
optional
Enable PMF and allow clients without PMF.
pmf-assoc-comeback-timeout
Protected Management Frames (PMF)
comeback maximum timeout (1-20
sec).
integer
Minimum value:
1 Maximum
value: 20
1
pmf-sa-query-retry-timeout
Protected Management Frames (PMF)
SA query retry timeout interval (1 - 5
100s of msec).
integer
Minimum value:
1 Maximum
value: 5
2
FortiOS 8.0.0 CLI Reference
2773
Fortinet Inc.

<!-- 来源页 2774 -->
Parameter
Description
Type
Size
Default
port-macauth
Enable/disable LAN port MAC
authentication (default = disable).
option
-disable
Option
Description
disable
Disable LAN port MAC authentication.
radius
Enable LAN port RADIUS-based MAC authentication.
address-group
Enable LAN port address-group based MAC authentication.
port-macauth-reauth-timeout
LAN port MAC authentication re-authentication timeout value (default =
7200 sec).
integer
Minimum value:
120 Maximum
value: 65535
7200
port-macauth-timeout
LAN port MAC authentication idle
timeout value (default = 600 sec).
integer
Minimum value:
60 Maximum
value: 65535
600
portal-message-override-group
Replacement message group for this
VAP (only available when security is set
to a captive portal type).
string
Maximum
length: 35
portal-type
Captive portal functionality. Configure
how the captive portal authenticates
users and whether it includes a
disclaimer.
option
-auth
Option
Description
auth
Portal for authentication.
auth+disclaimer
Portal for authentication and disclaimer.
disclaimer
Portal for disclaimer.
email-collect
Portal for email collection.
cmcc
Portal for CMCC.
cmcc-macauth
Portal for CMCC and MAC authentication.
auth-mac
Portal for authentication and MAC authentication.
external-auth
Portal for external portal authentication.
external-macauth
Portal for external portal MAC authentication.
pre-auth
Enable/disable pre-authentication,
where supported by clients (default =
enable).
option
-enable
FortiOS 8.0.0 CLI Reference
2774
Fortinet Inc.

<!-- 来源页 2775 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable pre-authentication.
disable
Disable pre-authentication.
primary-wag-profile
Primary wireless access gateway
profile name.
string
Maximum
length: 35
probe-resp-suppression
Enable/disable probe response
suppression (to ignore weak signals)
(default = disable).
option
-disable
Option
Description
enable
Enable probe response suppression.
disable
Disable probe response suppression.
probe-resp-threshold
Minimum signal level/threshold in dBm
required for the AP response to probe
requests (-95 to -20, default = -80).
string
Maximum
length: 7
-80
ptk-rekey
Enable/disable PTK rekey for WPA-Enterprise security.
option
-disable
Option
Description
enable
Enable PTK rekey for WPA-Enterprise security.
disable
Disable PTK rekey for WPA-Enterprise security.
ptk-rekey-intv
PTK rekey interval (600 - 864000 sec,
default = 86400).
integer
Minimum value:
600 Maximum
value: 864000
86400
qos-profile
Quality of service profile name.
string
Maximum
length: 35
quarantine
Enable/disable station quarantine
(default = disable).
option
-disable
Option
Description
enable
Enable station quarantine.
disable
Disable station quarantine.
radio-2g-threshold
Minimum signal level/threshold in dBm
required for the AP response to receive
a packet in 2.4G band (-95 to -20,
default = -79).
string
Maximum
length: 7
-79
FortiOS 8.0.0 CLI Reference
2775
Fortinet Inc.

<!-- 来源页 2776 -->
Parameter
Description
Type
Size
Default
radio-5g-threshold
Minimum signal level/threshold in dBm
required for the AP response to receive
a packet in 5G band(-95 to -20, default
= -76).
string
Maximum
length: 7
-76
radio-sensitivity
Enable/disable software radio
sensitivity (to ignore weak signals)
(default = disable).
option
-disable
Option
Description
enable
Enable software radio sensitivity.
disable
Disable software radio sensitivity.
radius-auth-surviv-intv *
RADIUS authentication survivability
cache timeout interval in seconds
(3600 - 864000, default = 86400).
integer
Minimum value:
3600 Maximum
value: 864000
86400
radius-auth-survivability *
Enable/disable RADIUS authentication
survivability (default = disable).
option
-disable
Option
Description
disable
Disable RADIUS authentication survivability.
enable
Enable RADIUS authentication survivability.
radius-mac-auth
Enable/disable RADIUS-based MAC
authentication of clients (default =
disable).
option
-disable
Option
Description
enable
Enable RADIUS-based MAC authentication.
disable
Disable RADIUS-based MAC authentication.
radius-mac-auth-block-interval
Don't send RADIUS MAC auth request
again if the client has been rejected
within specific interval (0 or 30 -864000 seconds, default = 0, 0 to
disable blocking).
integer
Minimum value:
30 Maximum
value: 864000
0
radius-mac-auth-server
RADIUS-based MAC authentication
server.
string
Maximum
length: 35
radius-mac-auth-usergroups
<name>
Selective user groups that are
permitted for RADIUS mac
authentication.
User group name.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
2776
Fortinet Inc.

<!-- 来源页 2777 -->
Parameter
Description
Type
Size
Default
radius-mac-mpsk-auth
Enable/disable RADIUS-based MAC
authentication of clients for MPSK
authentication (default = disable).
option
-disable
Option
Description
enable
Enable RADIUS-based MAC authentication for MPSK authentication.
disable
Disable RADIUS-based MAC authentication for MPSK authentication.
radius-mac-mpsk-timeout
RADIUS MAC MPSK cache timeout
interval (0 or 300 - 864000, default =
86400, 0 to disable caching).
integer
Minimum value:
300 Maximum
value: 864000
86400
radius-server
RADIUS server to be used to
authenticate WiFi users.
string
Maximum
length: 35
rates-11a
Allowed data rates for 802.11a.
option
-Option
Description
6
6 Mbps supported rate.
6-basic
6 Mbps BSS basic rate.
9
9 Mbps supported rate.
9-basic
9 Mbps BSS basic rate.
12
12 Mbps supported rate.
12-basic
12 Mbps BSS basic rate.
18
18 Mbps supported rate.
18-basic
18 Mbps BSS basic rate.
24
24 Mbps supported rate.
24-basic
24 Mbps BSS basic rate.
36
36 Mbps supported rate.
36-basic
36 Mbps BSS basic rate.
48
48 Mbps supported rate.
48-basic
48 Mbps BSS basic rate.
54
54 Mbps supported rate.
54-basic
54 Mbps BSS basic rate.
rates-11ac-mcs-map
Comma separated list of max
supported VHT MCS for spatial streams
1 through 8.
string
Maximum
length: 63
FortiOS 8.0.0 CLI Reference
2777
Fortinet Inc.

<!-- 来源页 2778 -->
Parameter
Description
Type
Size
Default
rates-11ax-mcs-map
Comma separated list of max
supported HE MCS for spatial streams 1
through 8.
string
Maximum
length: 63
rates-11be-mcs-map
Comma separated list of max nss that
supports EHT-MCS 0-9, 10-11, 12-13
for 20MHz/40MHz/80MHz bandwidth.
string
Maximum
length: 15
rates-11be-mcs-map-160
Comma separated list of max nss that
supports EHT-MCS 0-9, 10-11, 12-13
for 160MHz bandwidth.
string
Maximum
length: 15
rates-11be-mcs-map-320
Comma separated list of max nss that
supports EHT-MCS 0-9, 10-11, 12-13
for 320MHz bandwidth.
string
Maximum
length: 15
rates-11bg
Allowed data rates for 802.11b/g.
option
-Option
Description
1
1 Mbps supported rate.
1-basic
1 Mbps BSS basic rate.
2
2 Mbps supported rate.
2-basic
2 Mbps BSS basic rate.
5.5
5.5 Mbps supported rate.
5.5-basic
5.5 Mbps BSS basic rate.
11
11 Mbps supported rate.
11-basic
11 Mbps BSS basic rate.
6
6 Mbps supported rate.
6-basic
6 Mbps BSS basic rate.
9
9 Mbps supported rate.
9-basic
9 Mbps BSS basic rate.
12
12 Mbps supported rate.
12-basic
12 Mbps BSS basic rate.
18
18 Mbps supported rate.
18-basic
18 Mbps BSS basic rate.
24
24 Mbps supported rate.
24-basic
24 Mbps BSS basic rate.
FortiOS 8.0.0 CLI Reference
2778
Fortinet Inc.

<!-- 来源页 2779 -->
Parameter
Description
Type
Size
Default
Option
Description
36
36 Mbps supported rate.
36-basic
36 Mbps BSS basic rate.
48
48 Mbps supported rate.
48-basic
48 Mbps BSS basic rate.
54
54 Mbps supported rate.
54-basic
54 Mbps BSS basic rate.
rates-11n-ss12
Allowed data rates for 802.11n with 1 or
2 spatial streams.
option
-Option
Description
mcs0/1
Data rate for MCS index 0 with 1 spatial stream.
mcs1/1
Data rate for MCS index 1 with 1 spatial stream.
mcs2/1
Data rate for MCS index 2 with 1 spatial stream.
mcs3/1
Data rate for MCS index 3 with 1 spatial stream.
mcs4/1
Data rate for MCS index 4 with 1 spatial stream.
mcs5/1
Data rate for MCS index 5 with 1 spatial stream.
mcs6/1
Data rate for MCS index 6 with 1 spatial stream.
mcs7/1
Data rate for MCS index 7 with 1 spatial stream.
mcs8/2
Data rate for MCS index 8 with 2 spatial streams.
mcs9/2
Data rate for MCS index 9 with 2 spatial streams.
mcs10/2
Data rate for MCS index 10 with 2 spatial streams.
mcs11/2
Data rate for MCS index 11 with 2 spatial streams.
mcs12/2
Data rate for MCS index 12 with 2 spatial streams.
mcs13/2
Data rate for MCS index 13 with 2 spatial streams.
mcs14/2
Data rate for MCS index 14 with 2 spatial streams.
mcs15/2
Data rate for MCS index 15 with 2 spatial streams.
rates-11n-ss34
Allowed data rates for 802.11n with 3 or
4 spatial streams.
option
-FortiOS 8.0.0 CLI Reference
2779
Fortinet Inc.

<!-- 来源页 2780 -->
Parameter
Description
Type
Size
Default
Option
Description
mcs16/3
Data rate for MCS index 16 with 3 spatial streams.
mcs17/3
Data rate for MCS index 17 with 3 spatial streams.
mcs18/3
Data rate for MCS index 18 with 3 spatial streams.
mcs19/3
Data rate for MCS index 19 with 3 spatial streams.
mcs20/3
Data rate for MCS index 20 with 3 spatial streams.
mcs21/3
Data rate for MCS index 21 with 3 spatial streams.
mcs22/3
Data rate for MCS index 22 with 3 spatial streams.
mcs23/3
Data rate for MCS index 23 with 3 spatial streams.
mcs24/4
Data rate for MCS index 24 with 4 spatial streams.
mcs25/4
Data rate for MCS index 25 with 4 spatial streams.
mcs26/4
Data rate for MCS index 26 with 4 spatial streams.
mcs27/4
Data rate for MCS index 27 with 4 spatial streams.
mcs28/4
Data rate for MCS index 28 with 4 spatial streams.
mcs29/4
Data rate for MCS index 29 with 4 spatial streams.
mcs30/4
Data rate for MCS index 30 with 4 spatial streams.
mcs31/4
Data rate for MCS index 31 with 4 spatial streams.
roaming-acct-interim-update
Enable/disable using accounting
interim update instead of accounting
start/stop on roaming for WPA-Enterprise security.
option
-disable
Option
Description
enable
Enable using accounting interim update on roaming for WPA-Enterprise security.
disable
Disable using accounting interim update on roaming for WPA-Enterprise security.
sae-groups
SAE-Groups.
option
-Option
Description
19
DH Group 19.
20
DH Group 20.
21
DH Group 21.
FortiOS 8.0.0 CLI Reference
2780
Fortinet Inc.

<!-- 来源页 2781 -->
Parameter
Description
Type
Size
Default
sae-h2e-only
Use hash-to-element-only mechanism
for PWE derivation (default = disable).
option
-disable
Option
Description
enable
Enable WPA3 SAE-H2E-only.
disable
Disable WPA3 SAE-H2E-only.
sae-hnp-only
Use hunting-and-pecking-only
mechanism for PWE derivation (default
= disable).
option
-disable
Option
Description
enable
Enable WPA3 SAE-HNP-only.
disable
Disable WPA3 SAE-HNP-only.
sae-password
WPA3 SAE password to be used to
authenticate WiFi users.
password
Not Specified
sae-pk
Enable/disable WPA3 SAE-PK (default
= disable).
option
-disable
Option
Description
enable
Enable WPA3 SAE-PK.
disable
Disable WPA3 SAE-PK.
sae-private-key
Private key used for WPA3 SAE-PK
authentication.
string
Maximum
length: 359
scan-botnet-connections
Block or monitor connections to Botnet
servers or disable Botnet scanning.
option
-monitor
Option
Description
disable
Do not scan connections to botnet servers.
monitor
Log connections to botnet servers.
block
Block connections to botnet servers.
schedule <name>
Firewall schedules for enabling this
VAP on the FortiAP. This VAP will be
enabled when at least one of the
schedules is valid. Separate multiple
schedule names with a space.
Schedule name.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
2781
Fortinet Inc.

<!-- 来源页 2782 -->
Parameter
Description
Type
Size
Default
secondary-wag-profile
Secondary wireless access gateway
profile name.
string
Maximum
length: 35
security
Security mode for the wireless
interface (default = wpa2-only-personal).
option
-wpa2-only-personal
Option
Description
open
Open.
wep64
WEP 64-bit.
wep128
WEP 128-bit.
wpa-personal
WPA/WPA2 personal.
wpa-enterprise
WPA/WPA2 enterprise.
wpa-only-personal
WPA personal.
wpa-only-enterprise
WPA enterprise.
wpa2-only-personal
WPA2 personal.
wpa2-only-enterprise
WPA2 enterprise.
wpa3-enterprise
WPA3 enterprise with 192-bit encryption and PMF mandatory.
wpa3-only-enterprise
WPA3 enterprise with PMF mandatory.
wpa3-enterprise-transition
WPA3 enterprise with PMF optional.
wpa3-sae
WPA3 SAE.
wpa3-sae-transition
WPA3 SAE transition.
owe
Opportunistic wireless encryption.
osen
OSEN.
security-exempt-list
Optional security exempt list for captive
portal authentication.
string
Maximum
length: 35
security-redirect-url
Optional URL for redirecting users after
they pass captive portal authentication.
var-string
Maximum
length: 1023
FortiOS 8.0.0 CLI Reference
2782
Fortinet Inc.

<!-- 来源页 2783 -->
Parameter
Description
Type
Size
Default
selected-usergroups
<name>
Selective user groups that are
permitted to authenticate.
User group name.
string
Maximum
length: 79
split-tunneling
Enable/disable split tunneling (default =
disable).
option
-disable
Option
Description
enable
Enable split tunneling.
disable
Disable split tunneling.
ssid
IEEE 802.11 service set identifier (SSID)
for the wireless interface. Users who
wish to use the wireless network must
configure their computers to access
this SSID name.
string
Maximum
length: 32
fortinet
sticky-client-remove
Enable/disable sticky client remove to
maintain good signal level clients in
SSID (default = disable).
option
-disable
Option
Description
enable
Enable sticky client remove.
disable
Disable sticky client remove.
sticky-client-threshold-2g
Minimum signal level/threshold in dBm
required for the 2G client to be serviced
by the AP (-95 to -20, default = -79).
string
Maximum
length: 7
-79
sticky-client-threshold-5g
Minimum signal level/threshold in dBm
required for the 5G client to be serviced
by the AP (-95 to -20, default = -76).
string
Maximum
length: 7
-76
sticky-client-threshold-6g
Minimum signal level/threshold in dBm
required for the 6G client to be serviced
by the AP (-95 to -20, default = -76).
string
Maximum
length: 7
-76
target-wake-time
Enable/disable 802.11ax target wake
time (default = enable).
option
-enable
Option
Description
enable
Enable 802.11ax target wake time.
disable
Disable 802.11ax target wake time.
tkip-counter-measure
Enable/disable TKIP counter measure.
option
-enable
FortiOS 8.0.0 CLI Reference
2783
Fortinet Inc.

<!-- 来源页 2784 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable TKIP counter measure.
disable
Disable TKIP counter measure.
tunnel-echo-interval
The time interval to send echo to both
primary and secondary tunnel peers (1 -65535 sec, default = 300).
integer
Minimum value:
1 Maximum
value: 65535
300
tunnel-fallback-interval
The time interval for secondary tunnel
to fall back to primary tunnel (0 - 65535
sec, default = 7200).
integer
Minimum value:
0 Maximum
value: 65535
7200
usergroup
<name>
Firewall user group to be used to
authenticate WiFi users.
User group name.
string
Maximum
length: 79
utm-log
Enable/disable UTM logging.
option
-enable
Option
Description
enable
Enable UTM logging.
disable
Disable UTM logging.
utm-profile
UTM profile name.
string
Maximum
length: 35
utm-status
Enable to add one or more security
profiles (AV, IPS, etc.) to the VAP.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
vlan-auto
Enable/disable automatic management
of SSID VLAN interface.
option
-disable
Option
Description
enable
Enable automatic management of SSID VLAN interface.
disable
Disable automatic management of SSID VLAN interface.
FortiOS 8.0.0 CLI Reference
2784
Fortinet Inc.

<!-- 来源页 2785 -->
Parameter
Description
Type
Size
Default
vlan-pooling
Enable/disable VLAN pooling, to allow
grouping of multiple wireless controller
VLANs into VLAN pools (default =
disable). When set to wtp-group, VLAN
pooling occurs with VLAN assignment
by wtp-group.
option
-disable
Option
Description
wtp-group
Enable VLAN pooling with VLAN assignment by wtp-group.
round-robin
Enable VLAN pooling with round-robin VLAN assignment.
hash
Enable VLAN pooling with hash-based VLAN assignment.
disable
Disable VLAN pooling.
vlanid
Optional VLAN ID.
integer
Minimum value:
0 Maximum
value: 4094
0
webfilter-profile
WebFilter profile name.
string
Maximum
length: 47
* This parameter may not exist in some models.
** Values may differ between models.
config portal-message-overrides
Parameter
Description
Type
Size
Default
auth-disclaimer-page
Override auth-disclaimer-page message with
message from portal-message-overrides group.
string
Maximum
length: 35
auth-login-failed-page
Override auth-login-failed-page message with
message from portal-message-overrides group.
string
Maximum
length: 35
auth-login-page
Override auth-login-page message with message
from portal-message-overrides group.
string
Maximum
length: 35
auth-reject-page
Override auth-reject-page message with message
from portal-message-overrides group.
string
Maximum
length: 35
config vlan-name
Parameter
Description
Type
Size
Default
name
VLAN name.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
2785
Fortinet Inc.

<!-- 来源页 2786 -->
Parameter
Description
Type
Size
Default
vlan-id
VLAN IDs (maximum 8 VLAN IDs).
integer
Minimum
value: 0
Maximum
value: 4094
config vlan-pool
Parameter
Description
Type
Size
Default
id
ID.
integer
Minimum
value: 0
Maximum
value: 4094
0
wtp-group
<name> *
WTP group list(maximum 16 WTP groups).
WTP group name.
string
Maximum
length: 35
* This parameter may not exist in some models.
config wireless-controller vap-group
Configure virtual Access Point (VAP) groups.
config wireless-controller vap-group
Description: Configure virtual Access Point (VAP) groups.
edit <name>
set comment {var-string}
set vaps <name1>, <name2>, ...
next
end
config wireless-controller vap-group
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
Group Name.
string
Maximum
length: 35
vaps <name>
List of SSIDs to be included in the VAP group.
VAP name.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
2786
Fortinet Inc.

<!-- 来源页 2787 -->
config wireless-controller wag-profile
Configure wireless access gateway (WAG) profiles used for tunnels on AP.
config wireless-controller wag-profile
Description: Configure wireless access gateway (WAG) profiles used for tunnels on AP.
edit <name>
set comment {var-string}
set dhcp-ip-addr {ipv4-address}
set ping-interval {integer}
set ping-number {integer}
set return-packet-timeout {integer}
set tunnel-type [l2tpv3|gre]
set wag-ip {ipv4-address}
set wag-port {integer}
next
end
config wireless-controller wag-profile
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
dhcp-ip-addr
IP address of the monitoring DHCP request packet
sent through the tunnel.
ipv4-address
Not
Specified
0.0.0.0
name
Tunnel profile name.
string
Maximum
length: 35
ping-interval
Interval between two tunnel monitoring echo
packets (1 - 65535 sec, default = 1).
integer
Minimum
value: 1
Maximum
value:
65535
1
ping-number
Number of the tunnel monitoring echo packets (1 -65535, default = 5).
integer
Minimum
value: 1
Maximum
value:
65535
5
return-packet-timeout
Window of time for the return packets from the
tunnel's remote end (1 - 65535 sec, default = 160).
integer
Minimum
value: 1
Maximum
value:
65535
160
tunnel-type
Tunnel type.
option
-l2tpv3
FortiOS 8.0.0 CLI Reference
2787
Fortinet Inc.

<!-- 来源页 2788 -->
Parameter
Description
Type
Size
Default
Option
Description
l2tpv3
L2TPV3 Ethernet Pseudowire.
gre
GRE Ethernet tunnel.
wag-ip
IP Address of the wireless access gateway.
ipv4-address
Not
Specified
0.0.0.0
wag-port
UDP port of the wireless access gateway.
integer
Minimum
value: 0
Maximum
value:
65535
1701
config wireless-controller wids-profile
Configure wireless intrusion detection system (WIDS) profiles.
config wireless-controller wids-profile
Description: Configure wireless intrusion detection system (WIDS) profiles.
edit <name>
set adhoc-network [enable|disable]
set adhoc-valid-ssid [enable|disable]
set air-jack [enable|disable]
set ap-auto-suppress [enable|disable]
set ap-bgscan-disable-schedules <name1>, <name2>, ...
set ap-bgscan-duration {integer}
set ap-bgscan-idle {integer}
set ap-bgscan-intv {integer}
set ap-bgscan-period {integer}
set ap-bgscan-report-intv {integer}
set ap-fgscan-report-intv {integer}
set ap-impersonation [enable|disable]
set ap-scan [disable|enable]
set ap-scan-channel-list-2G-5G <chan1>, <chan2>, ...
set ap-scan-channel-list-6G <chan1>, <chan2>, ...
set ap-scan-passive [enable|disable]
set ap-scan-threshold {string}
set ap-spoofing [enable|disable]
set asleap-attack [enable|disable]
set assoc-flood-thresh {integer}
set assoc-flood-time {integer}
set assoc-frame-flood [enable|disable]
set auth-flood-thresh {integer}
set auth-flood-time {integer}
set auth-frame-flood [enable|disable]
set bcn-flood [enable|disable]
set bcn-flood-thresh {integer}
FortiOS 8.0.0 CLI Reference
2788
Fortinet Inc.

<!-- 来源页 2789 -->
set bcn-flood-time {integer}
set beacon-wrong-channel [enable|disable]
set block_ack-flood [enable|disable]
set block_ack-flood-thresh {integer}
set block_ack-flood-time {integer}
set chan-based-mitm [enable|disable]
set client-flood [enable|disable]
set client-flood-thresh {integer}
set client-flood-time {integer}
set comment {string}
set cts-flood [enable|disable]
set cts-flood-thresh {integer}
set cts-flood-time {integer}
set deauth-broadcast [enable|disable]
set deauth-unknown-src-thresh {integer}
set disassoc-broadcast [enable|disable]
set disconnect-station [enable|disable]
set eapol-fail-flood [enable|disable]
set eapol-fail-intv {integer}
set eapol-fail-thresh {integer}
set eapol-key-overflow [enable|disable]
set eapol-logoff-flood [enable|disable]
set eapol-logoff-intv {integer}
set eapol-logoff-thresh {integer}
set eapol-pre-fail-flood [enable|disable]
set eapol-pre-fail-intv {integer}
set eapol-pre-fail-thresh {integer}
set eapol-pre-succ-flood [enable|disable]
set eapol-pre-succ-intv {integer}
set eapol-pre-succ-thresh {integer}
set eapol-start-flood [enable|disable]
set eapol-start-intv {integer}
set eapol-start-thresh {integer}
set eapol-succ-flood [enable|disable]
set eapol-succ-intv {integer}
set eapol-succ-thresh {integer}
set fata-jack [enable|disable]
set fuzzed-beacon [enable|disable]
set fuzzed-probe-request [enable|disable]
set fuzzed-probe-response [enable|disable]
set hotspotter-attack [enable|disable]
set ht-40mhz-intolerance [enable|disable]
set ht-greenfield [enable|disable]
set invalid-addr-combination [enable|disable]
set invalid-mac-oui [enable|disable]
set long-duration-attack [enable|disable]
set long-duration-thresh {integer}
set malformed-association [enable|disable]
set malformed-auth [enable|disable]
set malformed-ht-ie [enable|disable]
set netstumbler [enable|disable]
set netstumbler-thresh {integer}
FortiOS 8.0.0 CLI Reference
2789
Fortinet Inc.

<!-- 来源页 2790 -->
set netstumbler-time {integer}
set null-ssid-probe-resp [enable|disable]
set omerta-attack [enable|disable]
set overflow-ie [enable|disable]
set probe-flood [enable|disable]
set probe-flood-thresh {integer}
set probe-flood-time {integer}
set pspoll-flood [enable|disable]
set pspoll-flood-thresh {integer}
set pspoll-flood-time {integer}
set pwsave-dos-attack [enable|disable]
set reassoc-flood [enable|disable]
set reassoc-flood-thresh {integer}
set reassoc-flood-time {integer}
set risky-encryption [enable|disable]
set rts-flood [enable|disable]
set rts-flood-thresh {integer}
set rts-flood-time {integer}
set sensor-mode [disable|foreign|...]
set spoofed-deauth [enable|disable]
set unencrypted-valid [enable|disable]
set valid-client-misassociation [enable|disable]
set valid-ssid-misuse [enable|disable]
set weak-wep-iv [enable|disable]
set wellenreiter [enable|disable]
set wellenreiter-thresh {integer}
set wellenreiter-time {integer}
set windows-bridge [enable|disable]
set wireless-bridge [enable|disable]
set wpa-ft-attack [enable|disable]
next
end
config wireless-controller wids-profile
Parameter
Description
Type
Size
Default
adhoc-network
Enable/disable adhoc network detection
(default = disable).
option
-disable
Option
Description
enable
Enable adhoc network detection.
disable
Disable adhoc network detection.
adhoc-valid-ssid
Enable/disable adhoc using valid SSID detection
(default = disable).
option
-disable
FortiOS 8.0.0 CLI Reference
2790
Fortinet Inc.

<!-- 来源页 2791 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable adhoc using valid SSID detection.
disable
Disable adhoc using valid SSID detection.
air-jack
Enable/disable AirJack detection (default =
disable).
option
-disable
Option
Description
enable
Enable AirJack detection.
disable
Disable AirJack detection.
ap-auto-suppress
Enable/disable on-wire rogue AP auto-suppression (default = disable).
option
-disable
Option
Description
enable
Enable on-wire rogue AP auto-suppression.
disable
Disable on-wire rogue AP auto-suppression.
ap-bgscan-disable-schedules
<name>
Firewall schedules for turning off FortiAP radio
background scan. Background scan will be
disabled when at least one of the schedules is
valid. Separate multiple schedule names with a
space.
Schedule name.
string
Maximum
length: 35
ap-bgscan-duration
Listen time on scanning a channel (10 - 1000
msec, default = 30).
integer
Minimum
value: 10
Maximum
value: 1000
30
ap-bgscan-idle
Wait time for channel inactivity before scanning
this channel (0 - 1000 msec, default = 20).
integer
Minimum
value: 0
Maximum
value: 1000
20
ap-bgscan-intv
Period between successive channel scans (1 -600 sec, default = 3).
integer
Minimum
value: 1
Maximum
value: 600
3
ap-bgscan-period
Period between background scans (10 - 3600
sec, default = 600).
integer
Minimum
value: 10
Maximum
value: 3600
600
FortiOS 8.0.0 CLI Reference
2791
Fortinet Inc.

<!-- 来源页 2792 -->
Parameter
Description
Type
Size
Default
ap-bgscan-report-intv
Period between background scan reports (15 -600 sec, default = 30).
integer
Minimum
value: 15
Maximum
value: 600
30
ap-fgscan-report-intv
Period between foreground scan reports (15 -600 sec, default = 15).
integer
Minimum
value: 15
Maximum
value: 600
15
ap-impersonation
Enable/disable AP impersonation detection
(default = disable).
option
-disable
Option
Description
enable
Enable AP impersonation detection.
disable
Disable AP impersonation detection.
ap-scan
Enable/disable rogue AP detection.
option
-disable
Option
Description
disable
Disable rogue AP detection.
enable
Enable rogue AP detection.
ap-scan-channel-list-2G-5G <chan>
Selected ap scan channel list for 2.4G and 5G
bands.
Channel number.
string
Maximum
length: 3
ap-scan-channel-list-6G
<chan>
Selected ap scan channel list for 6G band.
Channel 6g number.
string
Maximum
length: 3
ap-scan-passive
Enable/disable passive scanning. Enable means
do not send probe request on any channels
(default = disable).
option
-disable
Option
Description
enable
Passive scanning on all channels.
disable
Passive scanning only on DFS channels.
ap-scan-threshold
Minimum signal level/threshold in dBm required
for the AP to report detected rogue AP (-95 to -20, default = -90).
string
Maximum
length: 7
-90
ap-spoofing
Enable/disable AP spoofing detection (default =
disable).
option
-disable
FortiOS 8.0.0 CLI Reference
2792
Fortinet Inc.

<!-- 来源页 2793 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable AP spoofing detection.
disable
Disable AP spoofing detection.
asleap-attack
Enable/disable asleap attack detection (default
= disable).
option
-disable
Option
Description
enable
Enable asleap attack detection.
disable
Disable asleap attack detection.
assoc-flood-thresh
The threshold value for association frame
flooding.
integer
Minimum
value: 1
Maximum
value: 100
30
assoc-flood-time
Number of seconds after which a station is
considered not connected.
integer
Minimum
value: 5
Maximum
value: 120
10
assoc-frame-flood
Enable/disable association frame flooding
detection (default = disable).
option
-disable
Option
Description
enable
Enable association frame flooding detection.
disable
Disable association frame flooding detection.
auth-flood-thresh
The threshold value for authentication frame
flooding.
integer
Minimum
value: 1
Maximum
value: 100
30
auth-flood-time
Number of seconds after which a station is
considered not connected.
integer
Minimum
value: 5
Maximum
value: 120
10
auth-frame-flood
Enable/disable authentication frame flooding
detection (default = disable).
option
-disable
Option
Description
enable
Enable authentication frame flooding detection.
disable
Disable authentication frame flooding detection.
FortiOS 8.0.0 CLI Reference
2793
Fortinet Inc.

<!-- 来源页 2794 -->
Parameter
Description
Type
Size
Default
bcn-flood
Enable/disable bcn flood detection (default =
disable).
option
-disable
Option
Description
enable
Enable bcn flood detection.
disable
Disable bcn flood detection.
bcn-flood-thresh
The threshold value for bcn flood.
integer
Minimum
value: 1
Maximum
value:
65100
15
bcn-flood-time
Detection Window Period.
integer
Minimum
value: 1
Maximum
value: 120
1
beacon-wrong-channel
Enable/disable beacon wrong channel detection
(default = disable).
option
-disable
Option
Description
enable
Enable beacon wrong channel detection.
disable
Disable beacon wrong channel detection.
block_ack-flood
Enable/disable block_ack flood detection
(default = disable).
option
-disable
Option
Description
enable
Enable block_ack flood detection.
disable
Disable block_ack flood detection.
block_ack-flood-thresh
The threshold value for block_ack flood.
integer
Minimum
value: 1
Maximum
value:
65100
50
block_ack-flood-time
Detection Window Period.
integer
Minimum
value: 1
Maximum
value: 120
1
chan-based-mitm
Enable/disable channel based mitm detection
(default = disable).
option
-disable
FortiOS 8.0.0 CLI Reference
2794
Fortinet Inc.

<!-- 来源页 2795 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable channel based mitm detection.
disable
Disable channel based mitm detection.
client-flood
Enable/disable client flood detection (default =
disable).
option
-disable
Option
Description
enable
Enable client flood detection.
disable
Disable client flood detection.
client-flood-thresh
The threshold value for client flood.
integer
Minimum
value: 1
Maximum
value:
65100
30
client-flood-time
Detection Window Period.
integer
Minimum
value: 1
Maximum
value: 120
10
comment
Comment.
string
Maximum
length: 63
cts-flood
Enable/disable cts flood detection (default =
disable).
option
-disable
Option
Description
enable
Enable cts flood detection.
disable
Disable cts flood detection.
cts-flood-thresh
The threshold value for cts flood.
integer
Minimum
value: 1
Maximum
value:
65100
30
cts-flood-time
Detection Window Period.
integer
Minimum
value: 1
Maximum
value: 120
10
deauth-broadcast
Enable/disable broadcasting de-authentication
detection (default = disable).
option
-disable
FortiOS 8.0.0 CLI Reference
2795
Fortinet Inc.

<!-- 来源页 2796 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable broadcast de-authentication detection.
disable
Disable broadcast de-authentication detection.
deauth-unknown-src-thresh
Threshold value per second to deauth unknown
src for DoS attack (0: no limit).
integer
Minimum
value: 0
Maximum
value:
65535
10
disassoc-broadcast
Enable/disable broadcast dis-association
detection (default = disable).
option
-disable
Option
Description
enable
Enable broadcast dis-association detection.
disable
Disable broadcast dis-association detection.
disconnect-station
Enable/disable disconnect station detection
(default = disable).
option
-disable
Option
Description
enable
Enable disconnect station detection.
disable
Disable disconnect station detection.
eapol-fail-flood
Enable/disable EAPOL-Failure flooding (to AP)
detection (default = disable).
option
-disable
Option
Description
enable
Enable EAPOL-Failure flooding detection.
disable
Disable EAPOL-Failure flooding detection.
eapol-fail-intv
The detection interval for EAPOL-Failure
flooding (1 - 3600 sec).
integer
Minimum
value: 1
Maximum
value: 3600
1
eapol-fail-thresh
The threshold value for EAPOL-Failure flooding
in specified interval.
integer
Minimum
value: 2
Maximum
value: 100
10
eapol-key-overflow
Enable/disable overflow EAPOL key detection
(default = disable).
option
-disable
FortiOS 8.0.0 CLI Reference
2796
Fortinet Inc.

<!-- 来源页 2797 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable overflow EAPOL key detection.
disable
Disable overflow EAPOL key detection.
eapol-logoff-flood
Enable/disable EAPOL-Logoff flooding (to AP)
detection (default = disable).
option
-disable
Option
Description
enable
Enable EAPOL-Logoff flooding detection.
disable
Disable EAPOL-Logoff flooding detection.
eapol-logoff-intv
The detection interval for EAPOL-Logoff
flooding (1 - 3600 sec).
integer
Minimum
value: 1
Maximum
value: 3600
1
eapol-logoff-thresh
The threshold value for EAPOL-Logoff flooding
in specified interval.
integer
Minimum
value: 2
Maximum
value: 100
10
eapol-pre-fail-flood
Enable/disable premature EAPOL-Failure
flooding (to STA) detection (default = disable).
option
-disable
Option
Description
enable
Enable premature EAPOL-Failure flooding detection.
disable
Disable premature EAPOL-Failure flooding detection.
eapol-pre-fail-intv
The detection interval for premature EAPOL-Failure flooding (1 - 3600 sec).
integer
Minimum
value: 1
Maximum
value: 3600
1
eapol-pre-fail-thresh
The threshold value for premature EAPOL-Failure flooding in specified interval.
integer
Minimum
value: 2
Maximum
value: 100
10
eapol-pre-succ-flood
Enable/disable premature EAPOL-Success
flooding (to STA) detection (default = disable).
option
-disable
Option
Description
enable
Enable premature EAPOL-Success flooding detection.
disable
Disable premature EAPOL-Success flooding detection.
FortiOS 8.0.0 CLI Reference
2797
Fortinet Inc.

<!-- 来源页 2798 -->
Parameter
Description
Type
Size
Default
eapol-pre-succ-intv
The detection interval for premature EAPOL-Success flooding (1 - 3600 sec).
integer
Minimum
value: 1
Maximum
value: 3600
1
eapol-pre-succ-thresh
The threshold value for premature EAPOL-Success flooding in specified interval.
integer
Minimum
value: 2
Maximum
value: 100
10
eapol-start-flood
Enable/disable EAPOL-Start flooding (to AP)
detection (default = disable).
option
-disable
Option
Description
enable
Enable EAPOL-Start flooding detection.
disable
Disable EAPOL-Start flooding detection.
eapol-start-intv
The detection interval for EAPOL-Start flooding
(1 - 3600 sec).
integer
Minimum
value: 1
Maximum
value: 3600
1
eapol-start-thresh
The threshold value for EAPOL-Start flooding in
specified interval.
integer
Minimum
value: 2
Maximum
value: 100
10
eapol-succ-flood
Enable/disable EAPOL-Success flooding (to AP)
detection (default = disable).
option
-disable
Option
Description
enable
Enable EAPOL-Success flooding detection.
disable
Disable EAPOL-Success flooding detection.
eapol-succ-intv
The detection interval for EAPOL-Success
flooding (1 - 3600 sec).
integer
Minimum
value: 1
Maximum
value: 3600
1
eapol-succ-thresh
The threshold value for EAPOL-Success
flooding in specified interval.
integer
Minimum
value: 2
Maximum
value: 100
10
fata-jack
Enable/disable FATA-Jack detection (default =
disable).
option
-disable
FortiOS 8.0.0 CLI Reference
2798
Fortinet Inc.

<!-- 来源页 2799 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable FATA-Jack detection.
disable
Disable FATA-Jack detection.
fuzzed-beacon
Enable/disable fuzzed beacon detection
(default = disable).
option
-disable
Option
Description
enable
Enable fuzzed beacon detection.
disable
Disable fuzzed beacon detection.
fuzzed-probe-request
Enable/disable fuzzed probe request detection
(default = disable).
option
-disable
Option
Description
enable
Enable fuzzed probe request detection.
disable
Disable fuzzed probe request detection.
fuzzed-probe-response
Enable/disable fuzzed probe response
detection (default = disable).
option
-disable
Option
Description
enable
Enable fuzzed probe response detection.
disable
Disable fuzzed probe response detection.
hotspotter-attack
Enable/disable hotspotter attack detection
(default = disable).
option
-disable
Option
Description
enable
Enable hotspotter attack detection.
disable
Disable hotspotter attack detection.
ht-40mhz-intolerance
Enable/disable HT 40 MHz intolerance
detection (default = disable).
option
-disable
Option
Description
enable
Enable HT 40 MHz intolerance detection.
disable
Disable HT 40 MHz intolerance detection.
ht-greenfield
Enable/disable HT greenfield detection (default
= disable).
option
-disable
FortiOS 8.0.0 CLI Reference
2799
Fortinet Inc.

<!-- 来源页 2800 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable HT greenfield detection.
disable
Disable HT greenfield detection.
invalid-addr-combination
Enable/disable invalid address combination
detection (default = disable).
option
-disable
Option
Description
enable
Enable invalid address combination detection.
disable
Disable invalid address combination detection.
invalid-mac-oui
Enable/disable invalid MAC OUI detection.
option
-disable
Option
Description
enable
Enable invalid MAC OUI detection.
disable
Disable invalid MAC OUI detection.
long-duration-attack
Enable/disable long duration attack detection
based on user configured threshold (default =
disable).
option
-disable
Option
Description
enable
Enable long duration attack detection.
disable
Disable long duration attack detection.
long-duration-thresh
Threshold value for long duration attack
detection (1000 - 32767 usec, default = 8200).
integer
Minimum
value: 1000
Maximum
value:
32767
8200
malformed-association
Enable/disable malformed association request
detection (default = disable).
option
-disable
Option
Description
enable
Enable malformed association request detection.
disable
Disable malformed association request detection.
malformed-auth
Enable/disable malformed auth frame detection
(default = disable).
option
-disable
FortiOS 8.0.0 CLI Reference
2800
Fortinet Inc.

<!-- 来源页 2801 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable malformed auth frame detection.
disable
Disable malformed auth frame detection.
malformed-ht-ie
Enable/disable malformed HT IE detection
(default = disable).
option
-disable
Option
Description
enable
Enable malformed HT IE detection.
disable
Disable malformed HT IE detection.
name
WIDS profile name.
string
Maximum
length: 35
netstumbler
Enable/disable netstumbler detection (default =
disable).
option
-disable
Option
Description
enable
Enable netstumbler detection.
disable
Disable netstumbler detection.
netstumbler-thresh
The threshold value for netstumbler.
integer
Minimum
value: 1
Maximum
value:
65100
5
netstumbler-time
Detection Window Period.
integer
Minimum
value: 1
Maximum
value: 120
30
null-ssid-probe-resp
Enable/disable null SSID probe response
detection (default = disable).
option
-disable
Option
Description
enable
Enable null SSID probe resp detection.
disable
Disable null SSID probe resp detection.
omerta-attack
Enable/disable omerta attack detection (default
= disable).
option
-disable
FortiOS 8.0.0 CLI Reference
2801
Fortinet Inc.

<!-- 来源页 2802 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable omerta attack detection.
disable
Disable omerta attack detection.
overflow-ie
Enable/disable overflow IE detection (default =
disable).
option
-disable
Option
Description
enable
Enable overflow IE detection.
disable
Disable overflow IE detection.
probe-flood
Enable/disable probe flood detection (default =
disable).
option
-disable
Option
Description
enable
Enable probe flood detection.
disable
Disable probe flood detection.
probe-flood-thresh
The threshold value for probe flood.
integer
Minimum
value: 1
Maximum
value:
65100
30
probe-flood-time
Detection Window Period.
integer
Minimum
value: 1
Maximum
value: 120
1
pspoll-flood
Enable/disable pspoll flood detection (default =
disable).
option
-disable
Option
Description
enable
Enable pspoll flood detection.
disable
Disable pspoll flood detection.
pspoll-flood-thresh
The threshold value for pspoll flood.
integer
Minimum
value: 1
Maximum
value:
65100
30
FortiOS 8.0.0 CLI Reference
2802
Fortinet Inc.

<!-- 来源页 2803 -->
Parameter
Description
Type
Size
Default
pspoll-flood-time
Detection Window Period.
integer
Minimum
value: 1
Maximum
value: 120
1
pwsave-dos-attack
Enable/disable power save DOS attack
detection (default = disable).
option
-disable
Option
Description
enable
Enable power save DOS attack detection.
disable
Disable power save DOS attack detection.
reassoc-flood
Enable/disable reassociation flood detection
(default = disable).
option
-disable
Option
Description
enable
Enable reassociation flood detection.
disable
Disable reassociation flood detection.
reassoc-flood-thresh
The threshold value for reassociation flood.
integer
Minimum
value: 1
Maximum
value:
65100
30
reassoc-flood-time
Detection Window Period.
integer
Minimum
value: 1
Maximum
value: 120
10
risky-encryption
Enable/disable Risky Encryption detection
(default = disable).
option
-disable
Option
Description
enable
Enable Risky Encryption detection.
disable
Disable Risky Encryption detection.
rts-flood
Enable/disable rts flood detection (default =
disable).
option
-disable
Option
Description
enable
Enable rts flood detection.
disable
Disable rts flood detection.
FortiOS 8.0.0 CLI Reference
2803
Fortinet Inc.

<!-- 来源页 2804 -->
Parameter
Description
Type
Size
Default
rts-flood-thresh
The threshold value for rts flood.
integer
Minimum
value: 1
Maximum
value:
65100
30
rts-flood-time
Detection Window Period.
integer
Minimum
value: 1
Maximum
value: 120
10
sensor-mode
Scan nearby WiFi stations (default = disable).
option
-disable
Option
Description
disable
Disable the scan.
foreign
Enable the scan and monitor foreign channels. Foreign channels are
all other available channels than the current operating channel.
both
Enable the scan and monitor both foreign and home channels. Select
this option to monitor all WiFi channels.
spoofed-deauth
Enable/disable spoofed de-authentication
attack detection (default = disable).
option
-disable
Option
Description
enable
Enable spoofed de-authentication attack detection.
disable
Disable spoofed de-authentication attack detection.
unencrypted-valid
Enable/disable unencrypted valid detection
(default = disable).
option
-disable
Option
Description
enable
Enable unencrypted valid detection.
disable
Disable unencrypted valid detection.
valid-client-misassociation
Enable/disable valid client misassociation
detection (default = disable).
option
-disable
Option
Description
enable
Enable valid client misassociation detection.
disable
Disable valid client misassociation detection.
valid-ssid-misuse
Enable/disable valid SSID misuse detection
(default = disable).
option
-disable
FortiOS 8.0.0 CLI Reference
2804
Fortinet Inc.

<!-- 来源页 2805 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable valid SSID misuse detection.
disable
Disable valid SSID misuse detection.
weak-wep-iv
Enable/disable weak WEP IV (Initialization
Vector) detection (default = disable).
option
-disable
Option
Description
enable
Enable weak WEP IV detection.
disable
Disable weak WEP IV detection.
wellenreiter
Enable/disable wellenreiter detection (default =
disable).
option
-disable
Option
Description
enable
Enable wellenreiter detection.
disable
Disable wellenreiter detection.
wellenreiter-thresh
The threshold value for wellenreiter.
integer
Minimum
value: 1
Maximum
value:
65100
5
wellenreiter-time
Detection Window Period.
integer
Minimum
value: 1
Maximum
value: 120
30
windows-bridge
Enable/disable windows bridge detection
(default = disable).
option
-disable
Option
Description
enable
Enable windows bridge detection.
disable
Disable windows bridge detection.
wireless-bridge
Enable/disable wireless bridge detection
(default = disable).
option
-disable
Option
Description
enable
Enable wireless bridge detection.
disable
Disable wireless bridge detection.
FortiOS 8.0.0 CLI Reference
2805
Fortinet Inc.

<!-- 来源页 2806 -->
Parameter
Description
Type
Size
Default
wpa-ft-attack
Enable/disable WPA FT attack detection
(default = disable).
option
-disable
Option
Description
enable
Enable WPA FT attack detection.
disable
Disable WPA FT attack detection.
config wireless-controller wtp
Configure Wireless Termination Points (WTPs), that is, FortiAPs or APs to be managed by FortiGate.
config wireless-controller wtp
Description: Configure Wireless Termination Points (WTPs), that is, FortiAPs or APs to be
managed by FortiGate.
edit <wtp-id>
set admin [discovered|disable|...]
set allowaccess {option1}, {option2}, ...
set apcfg-profile {string}
set ble-major-id {integer}
set ble-minor-id {integer}
set bonjour-profile {string}
set comment {var-string}
set coordinate-latitude {string}
set coordinate-longitude {string}
set default-mesh-root [enable|disable]
set firmware-provision {string}
set firmware-provision-latest [disable|once]
set image-download [enable|disable]
set index {integer}
set ip-fragment-preventing {option1}, {option2}, ...
config lan
Description: WTP LAN port mapping.
set port-esl-mode [offline|nat-to-wan|...]
set port-esl-ssid {string}
set port-mode [offline|nat-to-wan|...]
set port-ssid {string}
set port1-mode [offline|nat-to-wan|...]
set port1-ssid {string}
set port2-mode [offline|nat-to-wan|...]
set port2-ssid {string}
set port3-mode [offline|nat-to-wan|...]
set port3-ssid {string}
set port4-mode [offline|nat-to-wan|...]
set port4-ssid {string}
set port5-mode [offline|nat-to-wan|...]
set port5-ssid {string}
set port6-mode [offline|nat-to-wan|...]
FortiOS 8.0.0 CLI Reference
2806
Fortinet Inc.

<!-- 来源页 2807 -->
set port6-ssid {string}
set port7-mode [offline|nat-to-wan|...]
set port7-ssid {string}
set port8-mode [offline|nat-to-wan|...]
set port8-ssid {string}
end
set led-state [enable|disable]
set location {string}
set login-passwd {password}
set login-passwd-change [yes|default|...]
set mesh-bridge-enable [default|enable|...]
set name {string}
set override-allowaccess [enable|disable]
set override-default-mesh-root [enable|disable]
set override-ip-fragment [enable|disable]
set override-lan [enable|disable]
set override-led-state [enable|disable]
set override-login-passwd-change [enable|disable]
set override-split-tunnel [enable|disable]
set override-wan-port-mode [enable|disable]
set purdue-level [1|1.5|...]
config radio-1
Description: Configuration options for radio 1.
set auto-power-high {integer}
set auto-power-level [enable|disable]
set auto-power-low {integer}
set auto-power-target {string}
set band {option1}, {option2}, ...
set cca-threshold {string}
set channel <chan1>, <chan2>, ...
set drma-manual-mode [ap|monitor|...]
set override-band [enable|disable]
set override-cca-threshold [enable|disable]
set override-channel [enable|disable]
set override-txpower [enable|disable]
set override-vap-status [enable|disable]
set override-vaps [enable|disable]
set power-level {integer}
set power-mode [dBm|percentage]
set power-value {integer}
set vap-all [tunnel|bridge|...]
set vap-status [enable|disable]
set vaps <name1>, <name2>, ...
end
config radio-2
Description: Configuration options for radio 2.
set auto-power-high {integer}
set auto-power-level [enable|disable]
set auto-power-low {integer}
set auto-power-target {string}
set band {option1}, {option2}, ...
set cca-threshold {string}
FortiOS 8.0.0 CLI Reference
2807
Fortinet Inc.

<!-- 来源页 2808 -->
set channel <chan1>, <chan2>, ...
set drma-manual-mode [ap|monitor|...]
set override-band [enable|disable]
set override-cca-threshold [enable|disable]
set override-channel [enable|disable]
set override-txpower [enable|disable]
set override-vap-status [enable|disable]
set override-vaps [enable|disable]
set power-level {integer}
set power-mode [dBm|percentage]
set power-value {integer}
set vap-all [tunnel|bridge|...]
set vap-status [enable|disable]
set vaps <name1>, <name2>, ...
end
config radio-3
Description: Configuration options for radio 3.
set auto-power-high {integer}
set auto-power-level [enable|disable]
set auto-power-low {integer}
set auto-power-target {string}
set band {option1}, {option2}, ...
set cca-threshold {string}
set channel <chan1>, <chan2>, ...
set drma-manual-mode [ap|monitor|...]
set override-band [enable|disable]
set override-cca-threshold [enable|disable]
set override-channel [enable|disable]
set override-txpower [enable|disable]
set override-vap-status [enable|disable]
set override-vaps [enable|disable]
set power-level {integer}
set power-mode [dBm|percentage]
set power-value {integer}
set vap-all [tunnel|bridge|...]
set vap-status [enable|disable]
set vaps <name1>, <name2>, ...
end
config radio-4
Description: Configuration options for radio 4.
set auto-power-high {integer}
set auto-power-level [enable|disable]
set auto-power-low {integer}
set auto-power-target {string}
set band {option1}, {option2}, ...
set cca-threshold {string}
set channel <chan1>, <chan2>, ...
set drma-manual-mode [ap|monitor|...]
set override-band [enable|disable]
set override-cca-threshold [enable|disable]
set override-channel [enable|disable]
set override-txpower [enable|disable]
FortiOS 8.0.0 CLI Reference
2808
Fortinet Inc.

<!-- 来源页 2809 -->
set override-vap-status [enable|disable]
set override-vaps [enable|disable]
set power-level {integer}
set power-mode [dBm|percentage]
set power-value {integer}
set vap-all [tunnel|bridge|...]
set vap-status [enable|disable]
set vaps <name1>, <name2>, ...
end
set region {string}
set region-x {string}
set region-y {string}
config split-tunneling-acl
Description: Split tunneling ACL filter list.
edit <id>
set dest-ip {ipv4-classnet}
next
end
set split-tunneling-acl-local-ap-subnet [enable|disable]
set split-tunneling-acl-path [tunnel|local]
set static-lowi [enable|disable]
set static-lowi-alt {integer}
set static-lowi-alt-err {integer}
set static-lowi-lat {string}
set static-lowi-lat-err {integer}
set static-lowi-lon {string}
set static-lowi-lon-err {integer}
set tun-mtu-downlink {integer}
set tun-mtu-uplink {integer}
set uuid {uuid}
set wan-port-mode [wan-lan|wan-only]
set wtp-profile {string}
next
end
config wireless-controller wtp
Parameter
Description
Type
Size
Default
admin
Configure how the FortiGate operating
as a wireless controller discovers and
manages this WTP, AP or FortiAP.
option
-enable
Option
Description
discovered
FortiGate wireless controller discovers the WTP, AP, or FortiAP though
discovery or join request messages.
FortiOS 8.0.0 CLI Reference
2809
Fortinet Inc.

<!-- 来源页 2810 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
FortiGate wireless controller is configured to not provide service to this
WTP.
enable
FortiGate wireless controller is configured to provide service to this
WTP.
allowaccess
Control management access to the
managed WTP, FortiAP, or AP.
Separate entries with a space.
option
-Option
Description
https
HTTPS access.
ssh
SSH access.
snmp
SNMP access.
apcfg-profile
AP local configuration profile name.
string
Maximum
length: 35
ble-major-id
Override BLE Major ID.
integer
Minimum value:
0 Maximum
value: 65535
0
ble-minor-id
Override BLE Minor ID.
integer
Minimum value:
0 Maximum
value: 65535
0
bonjour-profile
Bonjour profile name.
string
Maximum
length: 35
comment
Comment.
var-string
Maximum
length: 255
coordinate-latitude
WTP latitude coordinate.
string
Maximum
length: 19
coordinate-longitude
WTP longitude coordinate.
string
Maximum
length: 19
default-mesh-root
Configure default mesh root SSID
when it is not included by radio's SSID
configuration.
option
-disable
Option
Description
enable
Enable default mesh root SSID if it is not included by radio's SSID
configuration.
FortiOS 8.0.0 CLI Reference
2810
Fortinet Inc.

<!-- 来源页 2811 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Do not enable default mesh root SSID if it is not included by radio's SSID
configuration.
firmware-provision
Firmware version to provision to this
FortiAP on bootup (major.minor.build,
i.e. 6.2.1234).
string
Maximum
length: 35
firmware-provision-latest
Enable/disable one-time automatic
provisioning of the latest firmware
version.
option
-disable
Option
Description
disable
Do not automatically provision the latest available firmware.
once
Automatically attempt a one-time upgrade to the latest available
firmware version.
image-download
Enable/disable WTP image download.
option
-enable
Option
Description
enable
Enable WTP image download at join time.
disable
Disable WTP image download at join time.
index
Index (0 - 4294967295). Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
ip-fragment-preventing
Method(s) by which IP fragmentation is
prevented for control and data packets
through CAPWAP tunnel (default =
tcp-mss-adjust).
option
-tcp-mss-adjust
Option
Description
tcp-mss-adjust
TCP maximum segment size adjustment.
icmp-unreachable
Drop packet and send ICMP Destination Unreachable
led-state
Enable to allow the FortiAPs LEDs to
light. Disable to keep the LEDs off. You
may want to keep the LEDs off so they
are not distracting in low light areas
etc.
option
-enable
FortiOS 8.0.0 CLI Reference
2811
Fortinet Inc.

<!-- 来源页 2812 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Allow the LEDs on this FortiAP to light.
disable
Keep the LEDs on this FortiAP off.
location
Field for describing the physical
location of the WTP, AP or FortiAP.
string
Maximum
length: 35
login-passwd
Set the managed WTP, FortiAP, or AP's
administrator password.
password
Not Specified
login-passwd-change
Change or reset the administrator
password of a managed WTP, FortiAP
or AP (yes, default, or no, default = no).
option
-no
Option
Description
yes
Change the managed WTP, FortiAP or AP's administrator password.
Use the login-password option to set the password.
default
Keep the managed WTP, FortiAP or AP's administrator password set to
the factory default.
no
Do not change the managed WTP, FortiAP or AP's administrator
password.
mesh-bridge-enable
Enable/disable mesh Ethernet bridge
when WTP is configured as a mesh
branch/leaf AP.
option
-default
Option
Description
default
Use mesh Ethernet bridge local setting on the WTP.
enable
Turn on mesh Ethernet bridge on the WTP.
disable
Turn off mesh Ethernet bridge on the WTP.
name
WTP, AP or FortiAP configuration
name.
string
Maximum
length: 35
override-allowaccess
Enable to override the WTP profile
management access configuration.
option
-disable
Option
Description
enable
Override the WTP profile management access configuration.
disable
Use the WTP profile management access configuration.
FortiOS 8.0.0 CLI Reference
2812
Fortinet Inc.

<!-- 来源页 2813 -->
Parameter
Description
Type
Size
Default
override-default-mesh-root
Enable to override the WTP profile
default mesh root SSID setting.
option
-disable
Option
Description
enable
Override the WTP profile default mesh root SSID setting.
disable
Use the WTP profile default mesh root SSID setting.
override-ip-fragment
Enable/disable overriding the WTP
profile IP fragment prevention setting.
option
-disable
Option
Description
enable
Override the WTP profile IP fragment prevention setting.
disable
Use the WTP profile IP fragment prevention setting.
override-lan
Enable to override the WTP profile LAN
port setting.
option
-disable
Option
Description
enable
Override the WTP profile LAN port setting.
disable
Use the WTP profile LAN port setting.
override-led-state
Enable to override the profile LED state
setting for this FortiAP. You must
enable this option to use the led-state
command to turn off the FortiAP's
LEDs.
option
-disable
Option
Description
enable
Override the WTP profile LED state.
disable
Use the WTP profile LED state.
override-login-passwd-change
Enable to override the WTP profile
login-password (administrator
password) setting.
option
-disable
Option
Description
enable
Override the WTP profile login-password (administrator password)
setting.
disable
Use the the WTP profile login-password (administrator password)
setting.
FortiOS 8.0.0 CLI Reference
2813
Fortinet Inc.

<!-- 来源页 2814 -->
Parameter
Description
Type
Size
Default
override-split-tunnel
Enable/disable overriding the WTP
profile split tunneling setting.
option
-disable
Option
Description
enable
Override the WTP profile split tunneling setting.
disable
Use the WTP profile split tunneling setting.
override-wan-port-mode
Enable/disable overriding the wan-port-mode in the WTP profile.
option
-disable
Option
Description
enable
Override the WTP profile wan-port-mode.
disable
Use the wan-port-mode in the WTP profile.
purdue-level
Purdue Level of this WTP.
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
4
Level 4 - Business Planning & Logistics
5
Level 5 - Enterprise Network
5.5
Level 5.5
region
Region name WTP is associated with.
string
Maximum
length: 35
region-x
Relative horizontal region coordinate
(between 0 and 1).
string
Maximum
length: 15
0
region-y
Relative vertical region coordinate
(between 0 and 1).
string
Maximum
length: 15
0
split-tunneling-acl-local-ap-subnet
Enable/disable automatically adding
local subnetwork of FortiAP to split-tunneling ACL (default = disable).
option
-disable
FortiOS 8.0.0 CLI Reference
2814
Fortinet Inc.

<!-- 来源页 2815 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable automatically adding local subnetwork of FortiAP to split-tunneling ACL.
disable
Disable automatically adding local subnetwork of FortiAP to split-tunneling ACL.
split-tunneling-acl-path
Split tunneling ACL path is local/tunnel.
option
-local
Option
Description
tunnel
Split tunneling ACL list traffic will be tunnel.
local
Split tunneling ACL list traffic will be local NATed.
static-lowi *
Enable/disable static LOWI position of
the FortiAP.
option
-disable
Option
Description
enable
Enable static LOWI position of the FortiAP.
disable
Disable static LOWI position of the FortiAP.
static-lowi-alt
*
Static LOWI altitude position of the AP
(between 0 and 500 meters).
integer
Minimum value:
0 Maximum
value: 500
0
static-lowi-alt-err *
Static LOWI altitude error of the AP
(between 0 and 50 meters).
integer
Minimum value:
0 Maximum
value: 50
0
static-lowi-lat
*
Static LOWI latitude position of the AP
(between -90 and 90 degrees).
string
Maximum
length: 15
0
static-lowi-lat-err *
Static LOWI latitude error of the AP
(between 0 and 50 meters).
integer
Minimum value:
0 Maximum
value: 50
0
static-lowi-lon
*
Static LOWI longitude position of the
AP (between -180 and 180 degrees).
string
Maximum
length: 15
0
static-lowi-lon-err *
Static LOWI longitude error of the AP
(between 0 and 50 meters).
integer
Minimum value:
0 Maximum
value: 50
0
tun-mtu-downlink
The MTU of downlink CAPWAP tunnel
(576 - 1500 bytes or 0; 0 means the
local MTU of FortiAP; default = 0).
integer
Minimum value:
576 Maximum
value: 1500
0
FortiOS 8.0.0 CLI Reference
2815
Fortinet Inc.

<!-- 来源页 2816 -->
Parameter
Description
Type
Size
Default
tun-mtu-uplink
The maximum transmission unit (MTU)
of uplink CAPWAP tunnel (576 - 1500
bytes or 0; 0 means the local MTU of
FortiAP; default = 0).
integer
Minimum value:
576 Maximum
value: 1500
0
uuid
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not Specified
00000000-0000-0000-0000-000000000000
wan-port-mode
Enable/disable using the FortiAP WAN
port as a LAN port.
option
-wan-only
Option
Description
wan-lan
Use the FortiAP WAN port as a LAN port.
wan-only
Do not use the WAN port as a LAN port.
wtp-id
WTP ID.
string
Maximum
length: 35
wtp-profile
WTP profile name to apply to this WTP,
AP or FortiAP.
string
Maximum
length: 35
* This parameter may not exist in some models.
config lan
Parameter
Description
Type
Size
Default
port-esl-mode
ESL port mode.
option
-offline
Option
Description
offline
Offline.
nat-to-wan
NAT WTP ESL port to WTP WAN port.
bridge-to-wan
Bridge WTP ESL port to WTP WAN port.
bridge-to-ssid
Bridge WTP ESL port to SSID.
port-esl-ssid
Bridge ESL port to SSID.
string
Maximum
length: 15
port-mode
LAN port mode.
option
-offline
Option
Description
offline
Offline.
FortiOS 8.0.0 CLI Reference
2816
Fortinet Inc.

<!-- 来源页 2817 -->
Parameter
Description
Type
Size
Default
Option
Description
nat-to-wan
NAT WTP LAN port to WTP WAN port.
bridge-to-wan
Bridge WTP LAN port to WTP WAN port.
bridge-to-ssid
Bridge WTP LAN port to SSID.
port-ssid
Bridge LAN port to SSID.
string
Maximum
length: 15
port1-mode
LAN port 1 mode.
option
-offline
Option
Description
offline
Offline.
nat-to-wan
NAT WTP LAN port to WTP WAN port.
bridge-to-wan
Bridge WTP LAN port to WTP WAN port.
bridge-to-ssid
Bridge WTP LAN port to SSID.
port1-ssid
Bridge LAN port 1 to SSID.
string
Maximum
length: 15
port2-mode
LAN port 2 mode.
option
-offline
Option
Description
offline
Offline.
nat-to-wan
NAT WTP LAN port to WTP WAN port.
bridge-to-wan
Bridge WTP LAN port to WTP WAN port.
bridge-to-ssid
Bridge WTP LAN port to SSID.
port2-ssid
Bridge LAN port 2 to SSID.
string
Maximum
length: 15
port3-mode
LAN port 3 mode.
option
-offline
Option
Description
offline
Offline.
nat-to-wan
NAT WTP LAN port to WTP WAN port.
bridge-to-wan
Bridge WTP LAN port to WTP WAN port.
bridge-to-ssid
Bridge WTP LAN port to SSID.
port3-ssid
Bridge LAN port 3 to SSID.
string
Maximum
length: 15
FortiOS 8.0.0 CLI Reference
2817
Fortinet Inc.

<!-- 来源页 2818 -->
Parameter
Description
Type
Size
Default
port4-mode
LAN port 4 mode.
option
-offline
Option
Description
offline
Offline.
nat-to-wan
NAT WTP LAN port to WTP WAN port.
bridge-to-wan
Bridge WTP LAN port to WTP WAN port.
bridge-to-ssid
Bridge WTP LAN port to SSID.
port4-ssid
Bridge LAN port 4 to SSID.
string
Maximum
length: 15
port5-mode
LAN port 5 mode.
option
-offline
Option
Description
offline
Offline.
nat-to-wan
NAT WTP LAN port to WTP WAN port.
bridge-to-wan
Bridge WTP LAN port to WTP WAN port.
bridge-to-ssid
Bridge WTP LAN port to SSID.
port5-ssid
Bridge LAN port 5 to SSID.
string
Maximum
length: 15
port6-mode
LAN port 6 mode.
option
-offline
Option
Description
offline
Offline.
nat-to-wan
NAT WTP LAN port to WTP WAN port.
bridge-to-wan
Bridge WTP LAN port to WTP WAN port.
bridge-to-ssid
Bridge WTP LAN port to SSID.
port6-ssid
Bridge LAN port 6 to SSID.
string
Maximum
length: 15
port7-mode
LAN port 7 mode.
option
-offline
Option
Description
offline
Offline.
nat-to-wan
NAT WTP LAN port to WTP WAN port.
bridge-to-wan
Bridge WTP LAN port to WTP WAN port.
bridge-to-ssid
Bridge WTP LAN port to SSID.
FortiOS 8.0.0 CLI Reference
2818
Fortinet Inc.

<!-- 来源页 2819 -->
Parameter
Description
Type
Size
Default
port7-ssid
Bridge LAN port 7 to SSID.
string
Maximum
length: 15
port8-mode
LAN port 8 mode.
option
-offline
Option
Description
offline
Offline.
nat-to-wan
NAT WTP LAN port to WTP WAN port.
bridge-to-wan
Bridge WTP LAN port to WTP WAN port.
bridge-to-ssid
Bridge WTP LAN port to SSID.
port8-ssid
Bridge LAN port 8 to SSID.
string
Maximum
length: 15
config radio-1
Parameter
Description
Type
Size
Default
auto-power-high
The upper bound of automatic transmit
power adjustment in dBm (the actual range of
transmit power depends on the AP platform
type).
integer
Minimum value:
0 Maximum
value:
4294967295
17
auto-power-level
Enable/disable automatic power-level
adjustment to prevent co-channel
interference (default = enable).
option
-disable
Option
Description
enable
Enable automatic transmit power adjustment.
disable
Disable automatic transmit power adjustment.
auto-power-low
The lower bound of automatic transmit power
adjustment in dBm (the actual range of
transmit power depends on the AP platform
type).
integer
Minimum value:
0 Maximum
value:
4294967295
10
auto-power-target
Target of automatic transmit power
adjustment in dBm (-95 to -20, default = -70).
string
Maximum
length: 7
-70
band
WiFi band that Radio 1 operates on.
option
-Option
Description
802.11a
802.11a.
FortiOS 8.0.0 CLI Reference
2819
Fortinet Inc.

<!-- 来源页 2820 -->
Parameter
Description
Type
Size
Default
Option
Description
802.11b
802.11b.
802.11g
802.11g.
802.11n-2G
802.11n (WiFi 4) at 2.4GHz.
802.11n-5G
802.11n (WiFi 4) at 5GHz.
802.11ac-2G
802.11ac (WiFi 5) at 2.4GHz.
802.11ac-5G
802.11ac (WiFi 5) at 5GHz.
802.11ax-2G
802.11ax (WiFi 6) at 2.4GHz.
802.11ax-5G
802.11ax (WiFi 6) at 5GHz.
802.11ax-6G
802.11ax (WiFi 6) at 6GHz.
802.11be-2G
802.11be (WiFi 7) at 2.4GHz.
802.11be-5G
802.11be (WiFi 7) at 5GHz.
802.11be-6G
802.11be (WiFi 7) at 6GHz.
cca-threshold *
Configure Clear Channel Assessment (CCA)
threshold in dBm (-94 to -11, default = 0, 0
for unconfigured).
string
Maximum
length: 7
0
channel
<chan>
Selected list of wireless radio channels.
Channel number.
string
Maximum
length: 3
drma-manual-mode
Radio mode to be used for DRMA manual
mode (default = ncf).
option
-ncf
Option
Description
ap
Set the radio to AP mode.
monitor
Set the radio to monitor mode
ncf
Select and set the radio mode based on NCF score.
ncf-peek
Select the radio mode based on NCF score, but do not apply.
override-band
Enable to override the WTP profile band
setting.
option
-disable
Option
Description
enable
Override the WTP profile band setting.
disable
Use the WTP profile band setting.
FortiOS 8.0.0 CLI Reference
2820
Fortinet Inc.

<!-- 来源页 2821 -->
Parameter
Description
Type
Size
Default
override-cca-threshold *
Enable to override WTP profile CCA threshold
enable/disable settings.
option
-disable
Option
Description
enable
Override WTP profile CCA threshold enable/disable settings.
disable
Use WTP profile CCA threshold enable/disable settings.
override-channel
Enable to override WTP profile channel
settings.
option
-disable
Option
Description
enable
Override WTP profile channel settings.
disable
Use WTP profile channel settings.
override-txpower
Enable to override the WTP profile power
level configuration.
option
-disable
Option
Description
enable
Override the WTP profile power level configuration.
disable
Use the WTP profile power level configuration.
override-vap-status *
Enable to override WTP profile Virtual Access
Point (VAP) enable/disable settings.
option
-disable
Option
Description
enable
Override WTP profile VAP enable/disable settings.
disable
Use WTP profile VAP enable/disable settings.
override-vaps
Enable to override WTP profile Virtual Access
Point (VAP) settings.
option
-disable
Option
Description
enable
Override WTP profile VAP settings.
disable
Use WTP profile VAP settings.
power-level
Radio EIRP power level as a percentage of
the maximum EIRP power (0 - 100, default =
100).
integer
Minimum value:
0 Maximum
value: 100
100
FortiOS 8.0.0 CLI Reference
2821
Fortinet Inc.

<!-- 来源页 2822 -->
Parameter
Description
Type
Size
Default
power-mode
Set radio effective isotropic radiated power
(EIRP) in dBm or by a percentage of the
maximum EIRP (default = percentage). This
power takes into account both radio transmit
power and antenna gain. Higher power level
settings may be constrained by local
regulatory requirements and AP capabilities.
option
-percentage
Option
Description
dBm
Set radio EIRP power in dBm.
percentage
Set radio EIRP power by percentage.
power-value
Radio EIRP power in dBm (1 - 33, default =
27).
integer
Minimum value:
1 Maximum
value: 33
27
vap-all
Configure method for assigning SSIDs to this
FortiAP (default = automatically assign tunnel
SSIDs).
option
-tunnel
Option
Description
tunnel
Automatically select tunnel SSIDs.
bridge
Automatically select local-bridging SSIDs.
manual
Manually select SSIDs.
vap-status *
Enable/disable all configured SSIDs on this
radio (default = enable).
option
-enable
Option
Description
enable
Enable all configured SSIDs on this radio.
disable
Disable all configured SSIDs on this radio.
vaps <name>
Manually selected list of Virtual Access
Points (VAPs).
Virtual Access Point (VAP) name.
string
Maximum
length: 35
* This parameter may not exist in some models.
FortiOS 8.0.0 CLI Reference
2822
Fortinet Inc.

<!-- 来源页 2823 -->
config radio-2
Parameter
Description
Type
Size
Default
auto-power-high
The upper bound of automatic transmit
power adjustment in dBm (the actual range of
transmit power depends on the AP platform
type).
integer
Minimum value:
0 Maximum
value:
4294967295
17
auto-power-level
Enable/disable automatic power-level
adjustment to prevent co-channel
interference (default = enable).
option
-disable
Option
Description
enable
Enable automatic transmit power adjustment.
disable
Disable automatic transmit power adjustment.
auto-power-low
The lower bound of automatic transmit power
adjustment in dBm (the actual range of
transmit power depends on the AP platform
type).
integer
Minimum value:
0 Maximum
value:
4294967295
10
auto-power-target
Target of automatic transmit power
adjustment in dBm (-95 to -20, default = -70).
string
Maximum
length: 7
-70
band
WiFi band that Radio 2 operates on.
option
-Option
Description
802.11a
802.11a.
802.11b
802.11b.
802.11g
802.11g.
802.11n-2G
802.11n (WiFi 4) at 2.4GHz.
802.11n-5G
802.11n (WiFi 4) at 5GHz.
802.11ac-2G
802.11ac (WiFi 5) at 2.4GHz.
802.11ac-5G
802.11ac (WiFi 5) at 5GHz.
802.11ax-2G
802.11ax (WiFi 6) at 2.4GHz.
802.11ax-5G
802.11ax (WiFi 6) at 5GHz.
802.11ax-6G
802.11ax (WiFi 6) at 6GHz.
802.11be-2G
802.11be (WiFi 7) at 2.4GHz.
802.11be-5G
802.11be (WiFi 7) at 5GHz.
802.11be-6G
802.11be (WiFi 7) at 6GHz.
FortiOS 8.0.0 CLI Reference
2823
Fortinet Inc.

<!-- 来源页 2824 -->
Parameter
Description
Type
Size
Default
cca-threshold *
Configure Clear Channel Assessment (CCA)
threshold in dBm (-94 to -11, default = 0, 0
for unconfigured).
string
Maximum
length: 7
0
channel
<chan>
Selected list of wireless radio channels.
Channel number.
string
Maximum
length: 3
drma-manual-mode
Radio mode to be used for DRMA manual
mode (default = ncf).
option
-ncf
Option
Description
ap
Set the radio to AP mode.
monitor
Set the radio to monitor mode
ncf
Select and set the radio mode based on NCF score.
ncf-peek
Select the radio mode based on NCF score, but do not apply.
override-band
Enable to override the WTP profile band
setting.
option
-disable
Option
Description
enable
Override the WTP profile band setting.
disable
Use the WTP profile band setting.
override-cca-threshold *
Enable to override WTP profile CCA threshold
enable/disable settings.
option
-disable
Option
Description
enable
Override WTP profile CCA threshold enable/disable settings.
disable
Use WTP profile CCA threshold enable/disable settings.
override-channel
Enable to override WTP profile channel
settings.
option
-disable
Option
Description
enable
Override WTP profile channel settings.
disable
Use WTP profile channel settings.
override-txpower
Enable to override the WTP profile power
level configuration.
option
-disable
FortiOS 8.0.0 CLI Reference
2824
Fortinet Inc.

<!-- 来源页 2825 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Override the WTP profile power level configuration.
disable
Use the WTP profile power level configuration.
override-vap-status *
Enable to override WTP profile Virtual Access
Point (VAP) enable/disable settings.
option
-disable
Option
Description
enable
Override WTP profile VAP enable/disable settings.
disable
Use WTP profile VAP enable/disable settings.
override-vaps
Enable to override WTP profile Virtual Access
Point (VAP) settings.
option
-disable
Option
Description
enable
Override WTP profile VAP settings.
disable
Use WTP profile VAP settings.
power-level
Radio EIRP power level as a percentage of
the maximum EIRP power (0 - 100, default =
100).
integer
Minimum value:
0 Maximum
value: 100
100
power-mode
Set radio effective isotropic radiated power
(EIRP) in dBm or by a percentage of the
maximum EIRP (default = percentage). This
power takes into account both radio transmit
power and antenna gain. Higher power level
settings may be constrained by local
regulatory requirements and AP capabilities.
option
-percentage
Option
Description
dBm
Set radio EIRP power in dBm.
percentage
Set radio EIRP power by percentage.
power-value
Radio EIRP power in dBm (1 - 33, default =
27).
integer
Minimum value:
1 Maximum
value: 33
27
vap-all
Configure method for assigning SSIDs to this
FortiAP (default = automatically assign tunnel
SSIDs).
option
-tunnel
FortiOS 8.0.0 CLI Reference
2825
Fortinet Inc.

<!-- 来源页 2826 -->
Parameter
Description
Type
Size
Default
Option
Description
tunnel
Automatically select tunnel SSIDs.
bridge
Automatically select local-bridging SSIDs.
manual
Manually select SSIDs.
vap-status *
Enable/disable all configured SSIDs on this
radio (default = enable).
option
-enable
Option
Description
enable
Enable all configured SSIDs on this radio.
disable
Disable all configured SSIDs on this radio.
vaps <name>
Manually selected list of Virtual Access
Points (VAPs).
Virtual Access Point (VAP) name.
string
Maximum
length: 35
* This parameter may not exist in some models.
config radio-3
Parameter
Description
Type
Size
Default
auto-power-high
The upper bound of automatic transmit
power adjustment in dBm (the actual range of
transmit power depends on the AP platform
type).
integer
Minimum value:
0 Maximum
value:
4294967295
17
auto-power-level
Enable/disable automatic power-level
adjustment to prevent co-channel
interference (default = enable).
option
-disable
Option
Description
enable
Enable automatic transmit power adjustment.
disable
Disable automatic transmit power adjustment.
auto-power-low
The lower bound of automatic transmit power
adjustment in dBm (the actual range of
transmit power depends on the AP platform
type).
integer
Minimum value:
0 Maximum
value:
4294967295
10
auto-power-target
Target of automatic transmit power
adjustment in dBm (-95 to -20, default = -70).
string
Maximum
length: 7
-70
band
WiFi band that Radio 3 operates on.
option
-FortiOS 8.0.0 CLI Reference
2826
Fortinet Inc.

<!-- 来源页 2827 -->
Parameter
Description
Type
Size
Default
Option
Description
802.11a
802.11a.
802.11b
802.11b.
802.11g
802.11g.
802.11n-2G
802.11n (WiFi 4) at 2.4GHz.
802.11n-5G
802.11n (WiFi 4) at 5GHz.
802.11ac-2G
802.11ac (WiFi 5) at 2.4GHz.
802.11ac-5G
802.11ac (WiFi 5) at 5GHz.
802.11ax-2G
802.11ax (WiFi 6) at 2.4GHz.
802.11ax-5G
802.11ax (WiFi 6) at 5GHz.
802.11ax-6G
802.11ax (WiFi 6) at 6GHz.
802.11be-2G
802.11be (WiFi 7) at 2.4GHz.
802.11be-5G
802.11be (WiFi 7) at 5GHz.
802.11be-6G
802.11be (WiFi 7) at 6GHz.
cca-threshold *
Configure Clear Channel Assessment (CCA)
threshold in dBm (-94 to -11, default = 0, 0
for unconfigured).
string
Maximum
length: 7
0
channel
<chan>
Selected list of wireless radio channels.
Channel number.
string
Maximum
length: 3
drma-manual-mode
Radio mode to be used for DRMA manual
mode (default = ncf).
option
-ncf
Option
Description
ap
Set the radio to AP mode.
monitor
Set the radio to monitor mode
ncf
Select and set the radio mode based on NCF score.
ncf-peek
Select the radio mode based on NCF score, but do not apply.
override-band
Enable to override the WTP profile band
setting.
option
-disable
Option
Description
enable
Override the WTP profile band setting.
disable
Use the WTP profile band setting.
FortiOS 8.0.0 CLI Reference
2827
Fortinet Inc.

<!-- 来源页 2828 -->
Parameter
Description
Type
Size
Default
override-cca-threshold *
Enable to override WTP profile CCA threshold
enable/disable settings.
option
-disable
Option
Description
enable
Override WTP profile CCA threshold enable/disable settings.
disable
Use WTP profile CCA threshold enable/disable settings.
override-channel
Enable to override WTP profile channel
settings.
option
-disable
Option
Description
enable
Override WTP profile channel settings.
disable
Use WTP profile channel settings.
override-txpower
Enable to override the WTP profile power
level configuration.
option
-disable
Option
Description
enable
Override the WTP profile power level configuration.
disable
Use the WTP profile power level configuration.
override-vap-status *
Enable to override WTP profile Virtual Access
Point (VAP) enable/disable settings.
option
-disable
Option
Description
enable
Override WTP profile VAP enable/disable settings.
disable
Use WTP profile VAP enable/disable settings.
override-vaps
Enable to override WTP profile Virtual Access
Point (VAP) settings.
option
-disable
Option
Description
enable
Override WTP profile VAP settings.
disable
Use WTP profile VAP settings.
power-level
Radio EIRP power level as a percentage of
the maximum EIRP power (0 - 100, default =
100).
integer
Minimum value:
0 Maximum
value: 100
100
FortiOS 8.0.0 CLI Reference
2828
Fortinet Inc.

<!-- 来源页 2829 -->
Parameter
Description
Type
Size
Default
power-mode
Set radio effective isotropic radiated power
(EIRP) in dBm or by a percentage of the
maximum EIRP (default = percentage). This
power takes into account both radio transmit
power and antenna gain. Higher power level
settings may be constrained by local
regulatory requirements and AP capabilities.
option
-percentage
Option
Description
dBm
Set radio EIRP power in dBm.
percentage
Set radio EIRP power by percentage.
power-value
Radio EIRP power in dBm (1 - 33, default =
27).
integer
Minimum value:
1 Maximum
value: 33
27
vap-all
Configure method for assigning SSIDs to this
FortiAP (default = automatically assign tunnel
SSIDs).
option
-tunnel
Option
Description
tunnel
Automatically select tunnel SSIDs.
bridge
Automatically select local-bridging SSIDs.
manual
Manually select SSIDs.
vap-status *
Enable/disable all configured SSIDs on this
radio (default = enable).
option
-enable
Option
Description
enable
Enable all configured SSIDs on this radio.
disable
Disable all configured SSIDs on this radio.
vaps <name>
Manually selected list of Virtual Access
Points (VAPs).
Virtual Access Point (VAP) name.
string
Maximum
length: 35
* This parameter may not exist in some models.
FortiOS 8.0.0 CLI Reference
2829
Fortinet Inc.

<!-- 来源页 2830 -->
config radio-4
Parameter
Description
Type
Size
Default
auto-power-high
The upper bound of automatic transmit
power adjustment in dBm (the actual range of
transmit power depends on the AP platform
type).
integer
Minimum value:
0 Maximum
value:
4294967295
17
auto-power-level
Enable/disable automatic power-level
adjustment to prevent co-channel
interference (default = enable).
option
-disable
Option
Description
enable
Enable automatic transmit power adjustment.
disable
Disable automatic transmit power adjustment.
auto-power-low
The lower bound of automatic transmit power
adjustment in dBm (the actual range of
transmit power depends on the AP platform
type).
integer
Minimum value:
0 Maximum
value:
4294967295
10
auto-power-target
Target of automatic transmit power
adjustment in dBm (-95 to -20, default = -70).
string
Maximum
length: 7
-70
band
WiFi band that Radio 4 operates on.
option
-Option
Description
802.11a
802.11a.
802.11b
802.11b.
802.11g
802.11g.
802.11n-2G
802.11n (WiFi 4) at 2.4GHz.
802.11n-5G
802.11n (WiFi 4) at 5GHz.
802.11ac-2G
802.11ac (WiFi 5) at 2.4GHz.
802.11ac-5G
802.11ac (WiFi 5) at 5GHz.
802.11ax-2G
802.11ax (WiFi 6) at 2.4GHz.
802.11ax-5G
802.11ax (WiFi 6) at 5GHz.
802.11ax-6G
802.11ax (WiFi 6) at 6GHz.
802.11be-2G
802.11be (WiFi 7) at 2.4GHz.
802.11be-5G
802.11be (WiFi 7) at 5GHz.
802.11be-6G
802.11be (WiFi 7) at 6GHz.
FortiOS 8.0.0 CLI Reference
2830
Fortinet Inc.

<!-- 来源页 2831 -->
Parameter
Description
Type
Size
Default
cca-threshold *
Configure Clear Channel Assessment (CCA)
threshold in dBm (-94 to -11, default = 0, 0
for unconfigured).
string
Maximum
length: 7
0
channel
<chan>
Selected list of wireless radio channels.
Channel number.
string
Maximum
length: 3
drma-manual-mode
Radio mode to be used for DRMA manual
mode (default = ncf).
option
-ncf
Option
Description
ap
Set the radio to AP mode.
monitor
Set the radio to monitor mode
ncf
Select and set the radio mode based on NCF score.
ncf-peek
Select the radio mode based on NCF score, but do not apply.
override-band
Enable to override the WTP profile band
setting.
option
-disable
Option
Description
enable
Override the WTP profile band setting.
disable
Use the WTP profile band setting.
override-cca-threshold *
Enable to override WTP profile CCA threshold
enable/disable settings.
option
-disable
Option
Description
enable
Override WTP profile CCA threshold enable/disable settings.
disable
Use WTP profile CCA threshold enable/disable settings.
override-channel
Enable to override WTP profile channel
settings.
option
-disable
Option
Description
enable
Override WTP profile channel settings.
disable
Use WTP profile channel settings.
override-txpower
Enable to override the WTP profile power
level configuration.
option
-disable
FortiOS 8.0.0 CLI Reference
2831
Fortinet Inc.

<!-- 来源页 2832 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Override the WTP profile power level configuration.
disable
Use the WTP profile power level configuration.
override-vap-status *
Enable to override WTP profile Virtual Access
Point (VAP) enable/disable settings.
option
-disable
Option
Description
enable
Override WTP profile VAP enable/disable settings.
disable
Use WTP profile VAP enable/disable settings.
override-vaps
Enable to override WTP profile Virtual Access
Point (VAP) settings.
option
-disable
Option
Description
enable
Override WTP profile VAP settings.
disable
Use WTP profile VAP settings.
power-level
Radio EIRP power level as a percentage of
the maximum EIRP power (0 - 100, default =
100).
integer
Minimum value:
0 Maximum
value: 100
100
power-mode
Set radio effective isotropic radiated power
(EIRP) in dBm or by a percentage of the
maximum EIRP (default = percentage). This
power takes into account both radio transmit
power and antenna gain. Higher power level
settings may be constrained by local
regulatory requirements and AP capabilities.
option
-percentage
Option
Description
dBm
Set radio EIRP power in dBm.
percentage
Set radio EIRP power by percentage.
power-value
Radio EIRP power in dBm (1 - 33, default =
27).
integer
Minimum value:
1 Maximum
value: 33
27
vap-all
Configure method for assigning SSIDs to this
FortiAP (default = automatically assign tunnel
SSIDs).
option
-tunnel
FortiOS 8.0.0 CLI Reference
2832
Fortinet Inc.

<!-- 来源页 2833 -->
Parameter
Description
Type
Size
Default
Option
Description
tunnel
Automatically select tunnel SSIDs.
bridge
Automatically select local-bridging SSIDs.
manual
Manually select SSIDs.
vap-status *
Enable/disable all configured SSIDs on this
radio (default = enable).
option
-enable
Option
Description
enable
Enable all configured SSIDs on this radio.
disable
Disable all configured SSIDs on this radio.
vaps <name>
Manually selected list of Virtual Access
Points (VAPs).
Virtual Access Point (VAP) name.
string
Maximum
length: 35
* This parameter may not exist in some models.
config split-tunneling-acl
Parameter
Description
Type
Size
Default
dest-ip
Destination IP and mask for the split-tunneling
subnet.
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
config wireless-controller wtp-group
Configure WTP groups.
config wireless-controller wtp-group
Description: Configure WTP groups.
edit <name>
set ble-major-id {integer}
set platform-type [AP-11N|421E|...]
set wtps <wtp-id1>, <wtp-id2>, ...
next
end
FortiOS 8.0.0 CLI Reference
2833
Fortinet Inc.

<!-- 来源页 2834 -->
config wireless-controller wtp-group
Parameter
Description
Type
Size
Default
ble-major-id
Override BLE Major ID.
integer
Minimum
value: 0
Maximum
value:
65535
0
name
WTP group name.
string
Maximum
length: 35
platform-type
FortiAP models to define the WTP group platform
type.
option
-Option
Description
AP-11N
Default 11n AP.
421E
FAP421E.
423E
FAP423E.
221E
FAP221E.
223E
FAP223E.
431F
FAP431F.
431FL
FAP431FL.
432F
FAP432F.
432FR
FAP432FR.
433F
FAP433F.
433FL
FAP433FL.
231F
FAP231F.
231FL
FAP231FL.
234F
FAP234F.
23JF
FAP23JF.
831F
FAP831F.
231G
FAP231G.
233G
FAP233G.
234G
FAP234G.
431G
FAP431G.
FortiOS 8.0.0 CLI Reference
2834
Fortinet Inc.

<!-- 来源页 2835 -->
Parameter
Description
Type
Size
Default
Option
Description
432G
FAP432G.
433G
FAP433G.
221K
FAP221K.
231K
FAP231K.
231KD
FAP231KD.
23JK
FAP23JK.
222KL
FAP222KL.
241K
FAP241K.
243K
FAP243K.
244K
FAP244K.
441K
FAP441K.
435K
FAP435K.
443K
FAP443K.
U431F
FAPU431F.
U433F
FAPU433F.
U231F
FAPU231F.
U234F
FAPU234F.
U432F
FAPU432F.
U231G
FAPU231G.
MVP
FAP MVP.
C24JE
FAPC24JE.
222E
FAP222E.
224E
FAP224E.
231E
FAP231E.
321E
FAP321E.
432K
FAP432K.
U421E
FAPU421EV.
U422EV
FAPU422EV.
U423E
FAPU423EV.
FortiOS 8.0.0 CLI Reference
2835
Fortinet Inc.

<!-- 来源页 2836 -->
Parameter
Description
Type
Size
Default
Option
Description
U221EV
FAPU221EV.
U223EV
FAPU223EV.
U24JEV
FAPU24JEV.
U321EV
FAPU321EV.
U323EV
FAPU323EV.
FWF
FortiWiFi local radio.
wtps <wtp-id>
WTP list.
WTP ID.
string
Maximum
length: 35
config wireless-controller wtp-profile
Configure WTP profiles or FortiAP profiles that define radio settings for manageable FortiAP platforms.
config wireless-controller wtp-profile
Description: Configure WTP profiles or FortiAP profiles that define radio settings for
manageable FortiAP platforms.
edit <name>
set 80211mc-mode [auto|initiator|...]
set admin-auth-tacacs+ {string}
set admin-restrict-local [enable|disable]
set allowaccess {option1}, {option2}, ...
set ap-country [--|AF|...]
set ap-handoff [enable|disable]
set apcfg-auto-cert [enable|disable]
set apcfg-auto-cert-auto-regen-days {integer}
set apcfg-auto-cert-crypto-algo [rsa-1024|rsa-1536|...]
set apcfg-auto-cert-enroll-protocol [none|est|...]
set apcfg-auto-cert-est-ca-id {string}
set apcfg-auto-cert-est-http-password {password}
set apcfg-auto-cert-est-http-username {string}
set apcfg-auto-cert-est-https-ca {string}
set apcfg-auto-cert-est-server {string}
set apcfg-auto-cert-est-subject {string}
set apcfg-auto-cert-est-subject-alt-name {string}
set apcfg-auto-cert-scep-ca-id {string}
set apcfg-auto-cert-scep-ec-name [secp256r1|secp384r1|...]
set apcfg-auto-cert-scep-https-ca {string}
set apcfg-auto-cert-scep-keysize [1024|1536|...]
set apcfg-auto-cert-scep-keytype [rsa|ec]
set apcfg-auto-cert-scep-password {password}
set apcfg-auto-cert-scep-sub-fully-dn {string}
set apcfg-auto-cert-scep-subject-alt-name {string}
FortiOS 8.0.0 CLI Reference
2836
Fortinet Inc.

<!-- 来源页 2837 -->
set apcfg-auto-cert-scep-url {string}
set apcfg-mesh [enable|disable]
set apcfg-mesh-ap-type [ethernet|mesh|...]
set apcfg-mesh-eth-bridge [enable|disable]
set apcfg-mesh-ssid {string}
set apcfg-profile {string}
set ble-profile {string}
set bonjour-profile {string}
set comment {var-string}
set console-login [enable|disable]
set control-message-offload {option1}, {option2}, ...
set default-mesh-root [enable|disable]
config deny-mac-list
Description: List of MAC addresses that are denied access to this WTP, FortiAP, or AP.
edit <id>
set mac {mac-address}
next
end
set dtls-in-kernel [enable|disable]
set dtls-policy {option1}, {option2}, ...
set energy-efficient-ethernet [enable|disable]
config esl-ses-dongle
Description: ESL SES-imagotag dongle configuration.
set apc-addr-type [fqdn|ip]
set apc-fqdn {string}
set apc-ip {ipv4-address}
set apc-port {integer}
set coex-level {option}
set compliance-level {option}
set esl-channel [-1|0|...]
set output-power [a|b|...]
set scd-enable [enable|disable]
set tls-cert-verification [enable|disable]
set tls-fqdn-verification [enable|disable]
end
set ext-info-enable [enable|disable]
set frequency-handoff [enable|disable]
set handoff-roaming [enable|disable]
set handoff-rssi {integer}
set handoff-sta-thresh {integer}
set indoor-outdoor-deployment [platform-determined|outdoor|...]
set ip-fragment-preventing {option1}, {option2}, ...
set ipsec-offload [enable|disable]
config lan
Description: WTP LAN port mapping.
set port-esl-mode [offline|nat-to-wan|...]
set port-esl-ssid {string}
set port-mode [offline|nat-to-wan|...]
set port-ssid {string}
set port1-mode [offline|nat-to-wan|...]
set port1-ssid {string}
set port2-mode [offline|nat-to-wan|...]
FortiOS 8.0.0 CLI Reference
2837
Fortinet Inc.

<!-- 来源页 2838 -->
set port2-ssid {string}
set port3-mode [offline|nat-to-wan|...]
set port3-ssid {string}
set port4-mode [offline|nat-to-wan|...]
set port4-ssid {string}
set port5-mode [offline|nat-to-wan|...]
set port5-ssid {string}
set port6-mode [offline|nat-to-wan|...]
set port6-ssid {string}
set port7-mode [offline|nat-to-wan|...]
set port7-ssid {string}
set port8-mode [offline|nat-to-wan|...]
set port8-ssid {string}
end
config lbs
Description: Set various location based service (LBS) options.
set aeroscout [enable|disable]
set aeroscout-ap-mac [bssid|board-mac]
set aeroscout-mmu-report [enable|disable]
set aeroscout-mu [enable|disable]
set aeroscout-mu-factor {integer}
set aeroscout-mu-timeout {integer}
set aeroscout-server-ip {ipv4-address-any}
set aeroscout-server-port {integer}
set ble-rtls [none|polestar|...]
set ble-rtls-accumulation-interval {integer}
set ble-rtls-asset-addrgrp-list {string}
set ble-rtls-asset-uuid-list1 {string}
set ble-rtls-asset-uuid-list2 {string}
set ble-rtls-asset-uuid-list3 {string}
set ble-rtls-asset-uuid-list4 {string}
set ble-rtls-protocol {option}
set ble-rtls-reporting-interval {integer}
set ble-rtls-server-fqdn {string}
set ble-rtls-server-path {string}
set ble-rtls-server-port {integer}
set ble-rtls-server-token {string}
set ekahau-blink-mode [enable|disable]
set ekahau-tag {mac-address}
set erc-server-ip {ipv4-address-any}
set erc-server-port {integer}
set fortipresence [foreign|both|...]
set fortipresence-ble [enable|disable]
set fortipresence-frequency {integer}
set fortipresence-port {integer}
set fortipresence-project {string}
set fortipresence-rogue [enable|disable]
set fortipresence-secret {password}
set fortipresence-server {ipv4-address-any}
set fortipresence-server-addr-type [ipv4|fqdn]
set fortipresence-server-fqdn {string}
set fortipresence-unassoc [enable|disable]
FortiOS 8.0.0 CLI Reference
2838
Fortinet Inc.

<!-- 来源页 2839 -->
set station-locate [enable|disable]
end
set led-schedules <name1>, <name2>, ...
set led-state [enable|disable]
set lldp [enable|disable]
set login-passwd {password}
set login-passwd-change [yes|default|...]
set lw-profile {string}
set max-clients {integer}
config platform
Description: WTP, FortiAP, or AP platform.
set ddscan [enable|disable]
set mode [single-5G|dual-5G]
set type [AP-11N|421E|...]
end
set poe-mode [auto|8023af|...]
config radio-1
Description: Configuration options for radio 1.
set 80211d [enable|disable]
set 80211mc [enable|disable]
set ai-darrp-support [enable|disable]
set airtime-fairness [enable|disable]
set amsdu [enable|disable]
set ap-sniffer-addr {mac-address}
set ap-sniffer-bufsize {integer}
set ap-sniffer-chan {integer}
set ap-sniffer-chan-width [320MHz|240MHz|...]
set ap-sniffer-ctl [enable|disable]
set ap-sniffer-data [enable|disable]
set ap-sniffer-mgmt-beacon [enable|disable]
set ap-sniffer-mgmt-other [enable|disable]
set ap-sniffer-mgmt-probe [enable|disable]
set arrp-profile {string}
set auto-power-high {integer}
set auto-power-level [enable|disable]
set auto-power-low {integer}
set auto-power-target {string}
set band {option1}, {option2}, ...
set band-5g-type [5g-full|5g-high|...]
set bandwidth-admission-control [enable|disable]
set bandwidth-capacity {integer}
set beacon-interval {integer}
set bss-color {integer}
set bss-color-mode [auto|static]
set call-admission-control [enable|disable]
set call-capacity {integer}
set cca-threshold {string}
set channel <chan1>, <chan2>, ...
set channel-bonding [320MHz|240MHz|...]
set channel-bonding-ext [320MHz-1|320MHz-2]
set channel-utilization [enable|disable]
set coexistence [enable|disable]
FortiOS 8.0.0 CLI Reference
2839
Fortinet Inc.

<!-- 来源页 2840 -->
set darrp [enable|disable]
set drma [disable|enable]
set drma-sensitivity [low|medium|...]
set dtim {integer}
set frag-threshold {integer}
set iperf-protocol [udp|tcp]
set iperf-server-port {integer}
set max-clients {integer}
set max-distance {integer}
set mimo-mode [default|1x1|...]
set mode [disabled|ap|...]
set optional-antenna [none|custom|...]
set optional-antenna-gain {string}
set power-level {integer}
set power-mode [dBm|percentage]
set power-value {integer}
set powersave-optimize {option1}, {option2}, ...
set protection-mode [rtscts|ctsonly|...]
set rts-threshold {integer}
set sam-bssid {mac-address}
set sam-ca-certificate {string}
set sam-captive-portal [enable|disable]
set sam-client-certificate {string}
set sam-cwp-failure-string {string}
set sam-cwp-match-string {string}
set sam-cwp-password {password}
set sam-cwp-success-string {string}
set sam-cwp-test-url {string}
set sam-cwp-username {string}
set sam-eap-method [both|tls|...]
set sam-password {password}
set sam-private-key {string}
set sam-private-key-password {password}
set sam-report-intv {integer}
set sam-security-type [open|wpa-personal|...]
set sam-server-fqdn {string}
set sam-server-ip {ipv4-address}
set sam-server-type [ip|fqdn]
set sam-ssid {string}
set sam-test [ping|iperf]
set sam-username {string}
set short-guard-interval [enable|disable]
set transmit-optimize {option1}, {option2}, ...
set vap-all [tunnel|bridge|...]
set vap-status [enable|disable]
set vaps <name1>, <name2>, ...
set wids-profile {string}
set zero-wait-dfs [enable|disable]
end
config radio-2
Description: Configuration options for radio 2.
set 80211d [enable|disable]
FortiOS 8.0.0 CLI Reference
2840
Fortinet Inc.

<!-- 来源页 2841 -->
set 80211mc [enable|disable]
set ai-darrp-support [enable|disable]
set airtime-fairness [enable|disable]
set amsdu [enable|disable]
set ap-sniffer-addr {mac-address}
set ap-sniffer-bufsize {integer}
set ap-sniffer-chan {integer}
set ap-sniffer-chan-width [320MHz|240MHz|...]
set ap-sniffer-ctl [enable|disable]
set ap-sniffer-data [enable|disable]
set ap-sniffer-mgmt-beacon [enable|disable]
set ap-sniffer-mgmt-other [enable|disable]
set ap-sniffer-mgmt-probe [enable|disable]
set arrp-profile {string}
set auto-power-high {integer}
set auto-power-level [enable|disable]
set auto-power-low {integer}
set auto-power-target {string}
set band {option1}, {option2}, ...
set band-5g-type [5g-full|5g-high|...]
set bandwidth-admission-control [enable|disable]
set bandwidth-capacity {integer}
set beacon-interval {integer}
set bss-color {integer}
set bss-color-mode [auto|static]
set call-admission-control [enable|disable]
set call-capacity {integer}
set cca-threshold {string}
set channel <chan1>, <chan2>, ...
set channel-bonding [320MHz|240MHz|...]
set channel-bonding-ext [320MHz-1|320MHz-2]
set channel-utilization [enable|disable]
set coexistence [enable|disable]
set darrp [enable|disable]
set drma [disable|enable]
set drma-sensitivity [low|medium|...]
set dtim {integer}
set frag-threshold {integer}
set iperf-protocol [udp|tcp]
set iperf-server-port {integer}
set max-clients {integer}
set max-distance {integer}
set mimo-mode [default|1x1|...]
set mode [disabled|ap|...]
set optional-antenna [none|custom|...]
set optional-antenna-gain {string}
set power-level {integer}
set power-mode [dBm|percentage]
set power-value {integer}
set powersave-optimize {option1}, {option2}, ...
set protection-mode [rtscts|ctsonly|...]
set rts-threshold {integer}
FortiOS 8.0.0 CLI Reference
2841
Fortinet Inc.

<!-- 来源页 2842 -->
set sam-bssid {mac-address}
set sam-ca-certificate {string}
set sam-captive-portal [enable|disable]
set sam-client-certificate {string}
set sam-cwp-failure-string {string}
set sam-cwp-match-string {string}
set sam-cwp-password {password}
set sam-cwp-success-string {string}
set sam-cwp-test-url {string}
set sam-cwp-username {string}
set sam-eap-method [both|tls|...]
set sam-password {password}
set sam-private-key {string}
set sam-private-key-password {password}
set sam-report-intv {integer}
set sam-security-type [open|wpa-personal|...]
set sam-server-fqdn {string}
set sam-server-ip {ipv4-address}
set sam-server-type [ip|fqdn]
set sam-ssid {string}
set sam-test [ping|iperf]
set sam-username {string}
set short-guard-interval [enable|disable]
set transmit-optimize {option1}, {option2}, ...
set vap-all [tunnel|bridge|...]
set vap-status [enable|disable]
set vaps <name1>, <name2>, ...
set wids-profile {string}
set zero-wait-dfs [enable|disable]
end
config radio-3
Description: Configuration options for radio 3.
set 80211d [enable|disable]
set 80211mc [enable|disable]
set ai-darrp-support [enable|disable]
set airtime-fairness [enable|disable]
set amsdu [enable|disable]
set ap-sniffer-addr {mac-address}
set ap-sniffer-bufsize {integer}
set ap-sniffer-chan {integer}
set ap-sniffer-chan-width [320MHz|240MHz|...]
set ap-sniffer-ctl [enable|disable]
set ap-sniffer-data [enable|disable]
set ap-sniffer-mgmt-beacon [enable|disable]
set ap-sniffer-mgmt-other [enable|disable]
set ap-sniffer-mgmt-probe [enable|disable]
set arrp-profile {string}
set auto-power-high {integer}
set auto-power-level [enable|disable]
set auto-power-low {integer}
set auto-power-target {string}
set band {option1}, {option2}, ...
FortiOS 8.0.0 CLI Reference
2842
Fortinet Inc.

<!-- 来源页 2843 -->
set band-5g-type [5g-full|5g-high|...]
set bandwidth-admission-control [enable|disable]
set bandwidth-capacity {integer}
set beacon-interval {integer}
set bss-color {integer}
set bss-color-mode [auto|static]
set call-admission-control [enable|disable]
set call-capacity {integer}
set cca-threshold {string}
set channel <chan1>, <chan2>, ...
set channel-bonding [320MHz|240MHz|...]
set channel-bonding-ext [320MHz-1|320MHz-2]
set channel-utilization [enable|disable]
set coexistence [enable|disable]
set darrp [enable|disable]
set drma [disable|enable]
set drma-sensitivity [low|medium|...]
set dtim {integer}
set frag-threshold {integer}
set iperf-protocol [udp|tcp]
set iperf-server-port {integer}
set max-clients {integer}
set max-distance {integer}
set mimo-mode [default|1x1|...]
set mode [disabled|ap|...]
set optional-antenna [none|custom|...]
set optional-antenna-gain {string}
set power-level {integer}
set power-mode [dBm|percentage]
set power-value {integer}
set powersave-optimize {option1}, {option2}, ...
set protection-mode [rtscts|ctsonly|...]
set rts-threshold {integer}
set sam-bssid {mac-address}
set sam-ca-certificate {string}
set sam-captive-portal [enable|disable]
set sam-client-certificate {string}
set sam-cwp-failure-string {string}
set sam-cwp-match-string {string}
set sam-cwp-password {password}
set sam-cwp-success-string {string}
set sam-cwp-test-url {string}
set sam-cwp-username {string}
set sam-eap-method [both|tls|...]
set sam-password {password}
set sam-private-key {string}
set sam-private-key-password {password}
set sam-report-intv {integer}
set sam-security-type [open|wpa-personal|...]
set sam-server-fqdn {string}
set sam-server-ip {ipv4-address}
set sam-server-type [ip|fqdn]
FortiOS 8.0.0 CLI Reference
2843
Fortinet Inc.

<!-- 来源页 2844 -->
set sam-ssid {string}
set sam-test [ping|iperf]
set sam-username {string}
set short-guard-interval [enable|disable]
set transmit-optimize {option1}, {option2}, ...
set vap-all [tunnel|bridge|...]
set vap-status [enable|disable]
set vaps <name1>, <name2>, ...
set wids-profile {string}
set zero-wait-dfs [enable|disable]
end
config radio-4
Description: Configuration options for radio 4.
set 80211d [enable|disable]
set 80211mc [enable|disable]
set ai-darrp-support [enable|disable]
set airtime-fairness [enable|disable]
set amsdu [enable|disable]
set ap-sniffer-addr {mac-address}
set ap-sniffer-bufsize {integer}
set ap-sniffer-chan {integer}
set ap-sniffer-chan-width [320MHz|240MHz|...]
set ap-sniffer-ctl [enable|disable]
set ap-sniffer-data [enable|disable]
set ap-sniffer-mgmt-beacon [enable|disable]
set ap-sniffer-mgmt-other [enable|disable]
set ap-sniffer-mgmt-probe [enable|disable]
set arrp-profile {string}
set auto-power-high {integer}
set auto-power-level [enable|disable]
set auto-power-low {integer}
set auto-power-target {string}
set band {option1}, {option2}, ...
set band-5g-type [5g-full|5g-high|...]
set bandwidth-admission-control [enable|disable]
set bandwidth-capacity {integer}
set beacon-interval {integer}
set bss-color {integer}
set bss-color-mode [auto|static]
set call-admission-control [enable|disable]
set call-capacity {integer}
set cca-threshold {string}
set channel <chan1>, <chan2>, ...
set channel-bonding [320MHz|240MHz|...]
set channel-bonding-ext [320MHz-1|320MHz-2]
set channel-utilization [enable|disable]
set coexistence [enable|disable]
set darrp [enable|disable]
set drma [disable|enable]
set drma-sensitivity [low|medium|...]
set dtim {integer}
set frag-threshold {integer}
FortiOS 8.0.0 CLI Reference
2844
Fortinet Inc.

<!-- 来源页 2845 -->
set iperf-protocol [udp|tcp]
set iperf-server-port {integer}
set max-clients {integer}
set max-distance {integer}
set mimo-mode [default|1x1|...]
set mode [disabled|ap|...]
set optional-antenna [none|custom|...]
set optional-antenna-gain {string}
set power-level {integer}
set power-mode [dBm|percentage]
set power-value {integer}
set powersave-optimize {option1}, {option2}, ...
set protection-mode [rtscts|ctsonly|...]
set rts-threshold {integer}
set sam-bssid {mac-address}
set sam-ca-certificate {string}
set sam-captive-portal [enable|disable]
set sam-client-certificate {string}
set sam-cwp-failure-string {string}
set sam-cwp-match-string {string}
set sam-cwp-password {password}
set sam-cwp-success-string {string}
set sam-cwp-test-url {string}
set sam-cwp-username {string}
set sam-eap-method [both|tls|...]
set sam-password {password}
set sam-private-key {string}
set sam-private-key-password {password}
set sam-report-intv {integer}
set sam-security-type [open|wpa-personal|...]
set sam-server-fqdn {string}
set sam-server-ip {ipv4-address}
set sam-server-type [ip|fqdn]
set sam-ssid {string}
set sam-test [ping|iperf]
set sam-username {string}
set short-guard-interval [enable|disable]
set transmit-optimize {option1}, {option2}, ...
set vap-all [tunnel|bridge|...]
set vap-status [enable|disable]
set vaps <name1>, <name2>, ...
set wids-profile {string}
set zero-wait-dfs [enable|disable]
end
config split-tunneling-acl
Description: Split tunneling ACL filter list.
edit <id>
set dest-ip {ipv4-classnet}
next
end
set split-tunneling-acl-local-ap-subnet [enable|disable]
set split-tunneling-acl-path [tunnel|local]
FortiOS 8.0.0 CLI Reference
2845
Fortinet Inc.

<!-- 来源页 2846 -->
set syslog-profile {string}
set tun-mtu-downlink {integer}
set tun-mtu-uplink {integer}
set unii-4-5ghz-band [enable|disable]
set usb-port [enable|disable]
set wan-port-auth [none|802.1x]
set wan-port-auth-macsec [enable|disable]
set wan-port-auth-methods [all|EAP-FAST|...]
set wan-port-auth-password {password}
set wan-port-auth-usrname {string}
set wan-port-mode [wan-lan|wan-only]
next
end
config wireless-controller wtp-profile
Parame
ter
Description
Type
Size
Default
80211m
c-mode
*
Set 802.11mc mode of the AP (default = auto).
option
-auto
Option
Description
auto
Set AP 802.11mc automatically with LOWI.
initiator
Set AP 802.11mc in initiator mode.
responder
Set AP 802.11mc in responder mode.
admin-auth-tacacs+
Remote authentication server for admin user.
string
Maximu
m
length:
35
admin-restrict-local
Enable/disable local admin authentication restriction
when remote authenticator is up and running (default
= disable).
option
-disable
Option
Description
enable
Enable local admin authentication restriction.
disable
Diable local admin authentication restriction.
allowac
cess
Control management access to the managed WTP,
FortiAP, or AP. Separate entries with a space.
option
-FortiOS 8.0.0 CLI Reference
2846
Fortinet Inc.

<!-- 来源页 2847 -->
Parame
ter
Description
Type
Size
Default
Option
Description
https
HTTPS access.
ssh
SSH access.
snmp
SNMP access.
ap-country
Country in which this WTP, FortiAP, or AP will operate
(default = NA, automatically use the country
configured for the current VDOM).
option
---Option
Description
--NO_COUNTRY_SET
AF
AFGHANISTAN
AL
ALBANIA
DZ
ALGERIA
AS
AMERICAN SAMOA
AO
ANGOLA
AR
ARGENTINA
AM
ARMENIA
AU
AUSTRALIA
AT
AUSTRIA
AZ
AZERBAIJAN
BS
BAHAMAS
BH
BAHRAIN
BD
BANGLADESH
BB
BARBADOS
BY
BELARUS
BE
BELGIUM
BZ
BELIZE
BJ
BENIN
BM
BERMUDA
BT
BHUTAN
BO
BOLIVIA
FortiOS 8.0.0 CLI Reference
2847
Fortinet Inc.

<!-- 来源页 2848 -->
Parame
ter
Description
Type
Size
Default
Option
Description
BA
BOSNIA AND HERZEGOVINA
BW
BOTSWANA
BR
BRAZIL
BN
BRUNEI DARUSSALAM
BG
BULGARIA
BF
BURKINA-FASO
KH
CAMBODIA
CM
CAMEROON
KY
CAYMAN ISLANDS
CF
CENTRAL AFRICA REPUBLIC
TD
CHAD
CL
CHILE
CN
CHINA
CX
CHRISTMAS ISLAND
CO
COLOMBIA
CG
CONGO REPUBLIC
CD
DEMOCRATIC REPUBLIC OF CONGO
CR
COSTA RICA
HR
CROATIA
CY
CYPRUS
CZ
CZECH REPUBLIC
DK
DENMARK
DJ
DJIBOUTI
DM
DOMINICA
DO
DOMINICAN REPUBLIC
EC
ECUADOR
EG
EGYPT
SV
EL SALVADOR
FortiOS 8.0.0 CLI Reference
2848
Fortinet Inc.

<!-- 来源页 2849 -->
Parame
ter
Description
Type
Size
Default
Option
Description
ET
ETHIOPIA
EE
ESTONIA
GF
FRENCH GUIANA
PF
FRENCH POLYNESIA
FO
FAEROE ISLANDS
FJ
FIJI
FI
FINLAND
FR
FRANCE
GA
GABON
GE
GEORGIA
GM
GAMBIA
DE
GERMANY
GH
GHANA
GI
GIBRALTAR
GR
GREECE
GL
GREENLAND
GD
GRENADA
GP
GUADELOUPE
GU
GUAM
GT
GUATEMALA
GY
GUYANA
HT
HAITI
HN
HONDURAS
HK
HONG KONG
HU
HUNGARY
IS
ICELAND
IN
INDIA
ID
INDONESIA
FortiOS 8.0.0 CLI Reference
2849
Fortinet Inc.

<!-- 来源页 2850 -->
Parame
ter
Description
Type
Size
Default
Option
Description
IQ
IRAQ
IE
IRELAND
IM
ISLE OF MAN
IL
ISRAEL
IT
ITALY
CI
COTE_D_IVOIRE
JM
JAMAICA
JO
JORDAN
KZ
KAZAKHSTAN
KE
KENYA
KR
KOREA REPUBLIC
KW
KUWAIT
LA
LAOS
LV
LATVIA
LB
LEBANON
LS
LESOTHO
LR
LIBERIA
LY
LIBYA
LI
LIECHTENSTEIN
LT
LITHUANIA
LU
LUXEMBOURG
MO
MACAU SAR
MK
MACEDONIA, FYRO
MG
MADAGASCAR
MW
MALAWI
MY
MALAYSIA
MV
MALDIVES
ML
MALI
FortiOS 8.0.0 CLI Reference
2850
Fortinet Inc.

<!-- 来源页 2851 -->
Parame
ter
Description
Type
Size
Default
Option
Description
MT
MALTA
MH
MARSHALL ISLANDS
MQ
MARTINIQUE
MR
MAURITANIA
MU
MAURITIUS
YT
MAYOTTE
MX
MEXICO
FM
MICRONESIA
MD
REPUBLIC OF MOLDOVA
MC
MONACO
MN
MONGOLIA
MA
MOROCCO
MZ
MOZAMBIQUE
MM
MYANMAR
NA
NAMIBIA
NP
NEPAL
NL
NETHERLANDS
AN
NETHERLANDS ANTILLES
AW
ARUBA
NZ
NEW ZEALAND
NI
NICARAGUA
NE
NIGER
NG
NIGERIA
NO
NORWAY
MP
NORTHERN MARIANA ISLANDS
OM
OMAN
PK
PAKISTAN
PW
PALAU
FortiOS 8.0.0 CLI Reference
2851
Fortinet Inc.

<!-- 来源页 2852 -->
Parame
ter
Description
Type
Size
Default
Option
Description
PA
PANAMA
PG
PAPUA NEW GUINEA
PY
PARAGUAY
PE
PERU
PH
PHILIPPINES
PL
POLAND
PT
PORTUGAL
PR
PUERTO RICO
QA
QATAR
RE
REUNION
RO
ROMANIA
RU
RUSSIA
RW
RWANDA
BL
SAINT BARTHELEMY
KN
SAINT KITTS AND NEVIS
LC
SAINT LUCIA
MF
SAINT MARTIN
PM
SAINT PIERRE AND MIQUELON
VC
SAINT VINCENT AND GRENADIENS
SA
SAUDI ARABIA
SN
SENEGAL
RS
REPUBLIC OF SERBIA
ME
MONTENEGRO
SL
SIERRA LEONE
SG
SINGAPORE
SK
SLOVAKIA
SI
SLOVENIA
SO
SOMALIA
FortiOS 8.0.0 CLI Reference
2852
Fortinet Inc.

<!-- 来源页 2853 -->
Parame
ter
Description
Type
Size
Default
Option
Description
ZA
SOUTH AFRICA
ES
SPAIN
LK
SRI LANKA
SR
SURINAME
SZ
SWAZILAND
SE
SWEDEN
CH
SWITZERLAND
TW
TAIWAN
TZ
TANZANIA
TH
THAILAND
TL
TIMOR-LESTE
TG
TOGO
TT
TRINIDAD AND TOBAGO
TN
TUNISIA
TR
TURKEY
TM
TURKMENISTAN
AE
UNITED ARAB EMIRATES
TC
TURKS AND CAICOS
UG
UGANDA
UA
UKRAINE
GB
UNITED KINGDOM
US
UNITED STATES
PS
UNITED STATES (PUBLIC SAFETY)
UY
URUGUAY
UZ
UZBEKISTAN
VU
VANUATU
VE
VENEZUELA
VN
VIET NAM
FortiOS 8.0.0 CLI Reference
2853
Fortinet Inc.

<!-- 来源页 2854 -->
Parame
ter
Description
Type
Size
Default
Option
Description
VI
VIRGIN ISLANDS
WF
WALLIS AND FUTUNA
YE
YEMEN
ZM
ZAMBIA
ZW
ZIMBABWE
JP
JAPAN
CA
CANADA
ap-handoff
Enable/disable AP handoff of clients to other APs
(default = disable).
option
-disable
Option
Description
enable
Enable AP handoff.
disable
Disable AP handoff.
apcfg-auto-cert
Enable/disable AP local auto cert configuration
(default = disable).
option
-disable
Option
Description
enable
Enable AP local auto cert configuration.
disable
Disable AP local auto cert configuration.
apcfg-auto-cert-auto-regen-days
Number of days to wait before expiry of an updated
local certificate is requested (0 = disabled) (default =
30).
intege
r
Minimu
m value:
0
Maximu
m value:
429496
7295
30
apcfg-auto-cert-crypto-algo
Cryptography algorithm: rsa-1024, rsa-1536, rsa-2048, rsa-4096, ec-secp256r1, ec-secp384r1, ec-secp521r1 (default = ec-secp256r1)
option
-ec-secp256r1
FortiOS 8.0.0 CLI Reference
2854
Fortinet Inc.

<!-- 来源页 2855 -->
Parame
ter
Description
Type
Size
Default
Option
Description
rsa-1024
Cryptography algorithm rsa-1024.
rsa-1536
Cryptography algorithm rsa-1536.
rsa-2048
Cryptography algorithm rsa-2048.
rsa-4096
Cryptography algorithm rsa-4096.
ec-secp256r1
Cryptography algorithm ec-secp256r1.
ec-secp384r1
Cryptography algorithm ec-secp384r1.
ec-secp521r1
Cryptography algorithm ec-secp521r1.
apcfg-auto-cert-enroll-protocol
Certificate enrollment protocol (default = none)
option
-none
Option
Description
none
None (default).
est
Enrollment over Secure Transport.
scep
Simple Certificate Enrollment Protocol.
apcfg-auto-cert-est-ca-id
CA identifier of the CA server for signing via EST.
string
Maximu
m
length:
255
apcfg-auto-cert-est-http-passwo
rd
HTTP Authentication password for signing via EST.
passw
ord
Not
Specifie
d
apcfg-auto-cert-est-http-userna
me
HTTP Authentication username for signing via EST.
string
Maximu
m
length:
63
FortiOS 8.0.0 CLI Reference
2855
Fortinet Inc.

<!-- 来源页 2856 -->
Parame
ter
Description
Type
Size
Default
apcfg-auto-cert-est-https-ca
PEM format https CA Certificate.
string
Maximu
m
length:
79
apcfg-auto-cert-est-server
Address and port for EST server (e.g.
https://example.com:1234).
string
Maximu
m
length:
255
apcfg-auto-cert-est-subject
Subject e.g. "CN=User,DC=example,DC=COM"
(default = CN=FortiAP,DC=local,DC=COM)
string
Maximu
m
length:
127
CN=FortiAP,DC=loc
al,DC=COM
apcfg-auto-cert-est-subject-alt-name
Subject alternative name (optional, e.g.
"DNS:dns1.com,IP:192.168.1.99")
string
Maximu
m
length:
127
apcfg-auto-cert-scep-ca-id
CA identifier of the CA server for signing via SCEP.
string
Maximu
m
length:
255
apcfg-auto-cert-scep-ec-name
Elliptic curve name: secp256r1, secp384r1 and
secp521r1. (default secp256r1).
option
-secp256r1
Option
Description
secp256r1
Elliptic curve name secp256r1.
secp384r1
Elliptic curve name secp384r1.
secp521r1
Elliptic curve name secp521r1.
FortiOS 8.0.0 CLI Reference
2856
Fortinet Inc.

<!-- 来源页 2857 -->
Parame
ter
Description
Type
Size
Default
apcfg-auto-cert-scep-https-ca
PEM format https CA Certificate.
string
Maximu
m
length:
79
apcfg-auto-cert-scep-keysize
Key size: 1024, 1536, 2048, 4096 (default 2048).
option
-2048
Option
Description
1024
keysize 1024.
1536
keysize 1536.
2048
keysize 2048.
4096
keysize 4096.
apcfg-auto-cert-scep-keytype
Key type (default = rsa)
option
-rsa
Option
Description
rsa
Generate a RSA certificate request.
ec
Generate an elliptic curve certificate request.
apcfg-auto-cert-scep-passwo
rd
SCEP server challenge password for auto-regeneration.
passw
ord
Not
Specifie
d
apcfg-auto-cert-scep-sub-fully-dn
Full DN of the subject (e.g
C=US,ST=CA,L=Sunnyvale,O=Fortinet,OU=Dep1,emai
lAddress=test@example.com). There should be no
space in between the attributes. Supported DN
attributes (case-sensitive)
are:C,ST,L,O,OU,emailAddress. The CN defaults to the
device’s SN and cannot be changed.
string
Maximu
m
length:
255
FortiOS 8.0.0 CLI Reference
2857
Fortinet Inc.

<!-- 来源页 2858 -->
Parame
ter
Description
Type
Size
Default
apcfg-auto-cert-scep-subject-alt-name
Subject alternative name (optional, e.g.
"DNS:dns1.com,IP:192.168.1.99")
string
Maximu
m
length:
127
apcfg-auto-cert-scep-url
SCEP server URL.
string
Maximu
m
length:
255
apcfg-mesh
Enable/disable AP local mesh configuration (default =
disable).
option
-disable
Option
Description
enable
Enable AP local mesh configuration.
disable
Disable AP local mesh configuration.
apcfg-mesh-ap-type
Mesh AP Type (default = ethernet).
option
-ethernet
Option
Description
ethernet
Use ethernet uplink.
mesh
Use mesh uplink.
auto
Ethernet with mesh backup support.
apcfg-mesh-eth-bridge
Enable/disable mesh ethernet bridge (default =
disable).
option
-disable
Option
Description
enable
Enable AP local mesh eth bridge configuration.
disable
Disable AP local mesh eth bridge configuration.
apcfg-mesh-ssid
Mesh SSID (default = none).
string
Maximu
m
length:
15
FortiOS 8.0.0 CLI Reference
2858
Fortinet Inc.

<!-- 来源页 2859 -->
Parame
ter
Description
Type
Size
Default
apcfg-profile
AP local configuration profile name.
string
Maximu
m
length:
35
ble-profile
Bluetooth Low Energy profile name.
string
Maximu
m
length:
35
bonjou
r-profile
Bonjour profile name.
string
Maximu
m
length:
35
comme
nt
Comment.
var-string
Maximu
m
length:
255
consol
e-login
Enable/disable FortiAP console login access (default =
enable).
option
-enable
Option
Description
enable
Enable FAP console login access.
disable
Disable FAP console login access.
control-messag
e-offload
Enable/disable CAPWAP control message data
channel offload.
option
-ebp-frame
aeroscout-tag ap-list sta-list sta-cap-list stats aeroscout-mu sta-health
spectral-analysis
Option
Description
ebp-frame
Ekahau blink protocol (EBP) frames.
aeroscout-tag
AeroScout tag.
ap-list
Rogue AP list.
sta-list
Rogue STA list.
sta-cap-list
STA capability list.
stats
WTP, radio, VAP, and STA statistics.
aeroscout-mu
AeroScout Mobile Unit (MU) report.
FortiOS 8.0.0 CLI Reference
2859
Fortinet Inc.

<!-- 来源页 2860 -->
Parame
ter
Description
Type
Size
Default
Option
Description
sta-health
STA health log.
spectral-analysis
Spectral analysis report.
default-mesh-root
Configure default mesh root SSID when it is not
included by radio's SSID configuration.
option
-disable
Option
Description
enable
Enable default mesh root SSID if it is not included by radio's SSID
configuration.
disable
Do not enable default mesh root SSID if it is not included by radio's SSID
configuration.
dtls-in-kernel
Enable/disable data channel DTLS in kernel.
option
-disable
Option
Description
enable
Enable data channel DTLS in kernel.
disable
Disable data channel DTLS in kernel.
dtls-policy
WTP data channel DTLS policy (default = clear-text).
option
-clear-text
Option
Description
clear-text
Clear Text Data Channel.
dtls-enabled
DTLS Enabled Data Channel.
ipsec-vpn
IPsec VPN Data Channel.
ipsec-sn-vpn
IPsec VPN Data Channel with FortiAP's SN in the first IKE messages.
energy-efficien
t-etherne
t
Enable/disable use of energy efficient Ethernet on
WTP.
option
-disable
Option
Description
enable
Enable use of energy efficient Ethernet on WTP.
disable
Disable use of energy efficient Ethernet on WTP.
FortiOS 8.0.0 CLI Reference
2860
Fortinet Inc.

<!-- 来源页 2861 -->
Parame
ter
Description
Type
Size
Default
ext-info-enable
Enable/disable station/VAP/radio extension
information.
option
-enable
Option
Description
enable
Enable station/VAP/radio extension information.
disable
Disable station/VAP/radio extension information.
frequen
cy-handoff
Enable/disable frequency handoff of clients to other
channels (default = disable).
option
-disable
Option
Description
enable
Enable frequency handoff.
disable
Disable frequency handoff.
handof
f-roaming
Enable/disable client load balancing during roaming to
avoid roaming delay (default = enable).
option
-enable
Option
Description
enable
Enable handoff roaming.
disable
Disable handoff roaming.
handof
f-rssi
Minimum received signal strength indicator (RSSI)
value for handoff (20 - 30, default = 25).
intege
r
Minimu
m value:
20
Maximu
m value:
30
25
handof
f-sta-thresh
Threshold value for AP handoff.
intege
r
Minimu
m value:
5
Maximu
m value:
60
0
indoor-outdoo
r-deploy
ment
Set to allow indoor/outdoor-only channels under
regulatory rules (default = platform-determined).
option
-platform-determined
FortiOS 8.0.0 CLI Reference
2861
Fortinet Inc.

<!-- 来源页 2862 -->
Parame
ter
Description
Type
Size
Default
Option
Description
platform-determined
Set AP deployment type based on its platform.
outdoor
Set AP deployment type to outdoor.
indoor
Set AP deployment type to indoor.
ip-fragmen
t-preventi
ng
Method(s) by which IP fragmentation is prevented for
control and data packets through CAPWAP tunnel
(default = tcp-mss-adjust).
option
-tcp-mss-adjust
Option
Description
tcp-mss-adjust
TCP maximum segment size adjustment.
icmp-unreachable
Drop packet and send ICMP Destination Unreachable
ipsec-offload
*
Enable/disable data channel IPSec offloading (default
= enable).
option
-enable
Option
Description
enable
Enable data channel IPSec offloading.
disable
Disable data channel IPSec offloading.
led-schedul
es
<name>
Recurring firewall schedules for illuminating LEDs on
the FortiAP. If led-state is enabled, LEDs will be visible
when at least one of the schedules is valid. Separate
multiple schedule names with a space.
Schedule name.
string
Maximu
m
length:
35
led-state
Enable/disable use of LEDs on WTP (default = enable).
option
-enable
Option
Description
enable
Enable use of LEDs on WTP.
disable
Disable use of LEDs on WTP.
lldp
Enable/disable Link Layer Discovery Protocol (LLDP)
for the WTP, FortiAP, or AP (default = enable).
option
-enable
FortiOS 8.0.0 CLI Reference
2862
Fortinet Inc.

<!-- 来源页 2863 -->
Parame
ter
Description
Type
Size
Default
Option
Description
enable
Enable LLDP.
disable
Disable LLDP.
login-passwd
Set the managed WTP, FortiAP, or AP's administrator
password.
passw
ord
Not
Specifie
d
login-passw
d-change
Change or reset the administrator password of a
managed WTP, FortiAP or AP (yes, default, or no,
default = no).
option
-no
Option
Description
yes
Change the managed WTP, FortiAP or AP's administrator password. Use the
login-password option to set the password.
default
Keep the managed WTP, FortiAP or AP's administrator password set to the
factory default.
no
Do not change the managed WTP, FortiAP or AP's administrator password.
lw-profile
LoRaWAN profile name.
string
Maximu
m
length:
35
max-clients
Maximum number of stations (STAs) supported by the
WTP (default = 0, meaning no client limitation).
intege
r
Minimu
m value:
0
Maximu
m value:
429496
7295
0
name
WTP (or FortiAP or AP) profile name.
string
Maximu
m
length:
35
poe-mode
Set the WTP, FortiAP, or AP's PoE mode.
option
-auto
Option
Description
auto
Automatically detect the PoE mode.
FortiOS 8.0.0 CLI Reference
2863
Fortinet Inc.

<!-- 来源页 2864 -->
Parame
ter
Description
Type
Size
Default
Option
Description
8023af
Use 802.3af PoE mode.
8023at
Use 802.3at PoE mode.
power-adapter
Use the power adapter to control the PoE mode.
full
Use full power mode.
high
Use high power mode.
high-pse
Use high power mode with PSE-OUT.
low
Use low power mode.
split-tunnelin
g-acl-local-ap-subnet
Enable/disable automatically adding local subnetwork
of FortiAP to split-tunneling ACL (default = disable).
option
-disable
Option
Description
enable
Enable automatically adding local subnetwork of FortiAP to split-tunneling
ACL.
disable
Disable automatically adding local subnetwork of FortiAP to split-tunneling
ACL.
split-tunnelin
g-acl-path
Split tunneling ACL path is local/tunnel.
option
-local
Option
Description
tunnel
Split tunneling ACL list traffic will be tunnel.
local
Split tunneling ACL list traffic will be local NATed.
syslog-profile
System log server configuration profile name.
string
Maximu
m
length:
35
FortiOS 8.0.0 CLI Reference
2864
Fortinet Inc.

<!-- 来源页 2865 -->
Parame
ter
Description
Type
Size
Default
tun-mtu-downlin
k
The MTU of downlink CAPWAP tunnel (576 - 1500
bytes or 0; 0 means the local MTU of FortiAP; default =
0).
intege
r
Minimu
m value:
576
Maximu
m value:
1500
0
tun-mtu-uplink
The maximum transmission unit (MTU) of uplink
CAPWAP tunnel (576 - 1500 bytes or 0; 0 means the
local MTU of FortiAP; default = 0).
intege
r
Minimu
m value:
576
Maximu
m value:
1500
0
unii-4-5ghz-band
Enable/disable UNII-4 5Ghz band channels (default =
disable).
option
-disable
Option
Description
enable
Enable UNII-4 5Ghz band channels.
disable
Disable UNII-4 5Ghz band channels.
usb-port
Enable/disable USB port of the WTP (default = enable).
option
-enable
Option
Description
enable
Enable USB port.
disable
Disable USB port.
wan-port-auth
Set WAN port authentication mode (default = none).
option
-none
Option
Description
none
Disable WAN port authentication.
802.1x
Enable WAN port 802.1x authentication.
wan-port-auth-macsec
Enable/disable WAN port 802.1x supplicant MACsec
policy (default = disable).
option
-disable
FortiOS 8.0.0 CLI Reference
2865
Fortinet Inc.

<!-- 来源页 2866 -->
Parame
ter
Description
Type
Size
Default
Option
Description
enable
Enable WAN port 802.1x supplicant MACsec policy.
disable
Disable WAN port 802.1x supplicant MACsec policy.
wan-port-auth-method
s
WAN port 802.1x supplicant EAP methods (default =
all).
option
-all
Option
Description
all
Do not specify any EAP methods.
EAP-FAST
Enable EAP-FAST.
EAP-TLS
Enable EAP-TLS.
EAP-PEAP
Enable EAP-PEAP.
wan-port-auth-passwo
rd
Set WAN port 802.1x supplicant password.
passw
ord
Not
Specifie
d
wan-port-auth-usrnam
e
Set WAN port 802.1x supplicant user name.
string
Maximu
m
length:
63
wan-port-mode
Enable/disable using a WAN port as a LAN port.
option
-wan-only
Option
Description
wan-lan
Enable using a WAN port as a LAN port.
wan-only
Disable using a WAN port as a LAN port.
* This parameter may not exist in some models.
FortiOS 8.0.0 CLI Reference
2866
Fortinet Inc.

<!-- 来源页 2867 -->
config deny-mac-list
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
mac
A WiFi device with this MAC address
is denied access to this WTP, FortiAP
or AP.
mac-address
Not Specified
00:00:00:00:00:00
config esl-ses-dongle
Parameter
Description
Type
Size
Default
apc-addr-type
ESL SES-imagotag APC address type (default =
fqdn).
option
-fqdn
Option
Description
fqdn
Fully Qualified Domain Name address.
ip
IPv4 address.
apc-fqdn
FQDN of ESL SES-imagotag Access Point
Controller (APC).
string
Maximum
length: 63
apc-ip
IP address of ESL SES-imagotag Access Point
Controller (APC).
ipv4-address
Not
Specified
0.0.0.0
apc-port
Port of ESL SES-imagotag Access Point
Controller (APC).
integer
Minimum
value: 0
Maximum
value:
65535
0
coex-level
ESL SES-imagotag dongle coexistence level
(default = none).
option
-none
Option
Description
none
No support for coexistence of USB-Dongle with WiFi AP.
compliance-level
Compliance levels for the ESL solution
integration (default = compliance-level-2).
option
-compliance-level-2
Option
Description
compliance-level-2
Compliance Level 2 - Full Cloud Support, IoT and Fast-Response.
FortiOS 8.0.0 CLI Reference
2867
Fortinet Inc.

<!-- 来源页 2868 -->
Parameter
Description
Type
Size
Default
esl-channel
ESL SES-imagotag dongle channel (default =
127).
option
-127
Option
Description
-1
No esl-channel is set.
0
ESL channel 0.
1
ESL channel 1.
2
ESL channel 2.
3
ESL channel 3.
4
ESL channel 4.
5
ESL channel 5.
6
ESL channel 6.
7
ESL channel 7.
8
ESL channel 8.
9
ESL channel 9.
10
ESL channel 10.
127
Managed channel enabled, indicates that the APC (server) is setting
the esl-channel via the slot channel
output-power
ESL SES-imagotag dongle output power
(default = A).
option
-a
Option
Description
a
About 15mW.
b
About 7mW.
c
About 5mW.
d
About 1mW.
e
About 13mW.
f
About 10mW.
g
About 3mW.
h
About 2mW.
scd-enable
Enable/disable ESL SES-imagotag Serial
Communication Daemon (SCD) (default =
disable).
option
-disable
FortiOS 8.0.0 CLI Reference
2868
Fortinet Inc.

<!-- 来源页 2869 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable ESL SES-imagotag SCD.
disable
Disable ESL SES-imagotag SCD.
tls-cert-verification
Enable/disable TLS certificate verification
(default = enable).
option
-enable
Option
Description
enable
Enable TLS Certificate verification.
disable
Disable TLS Certificate verification.
tls-fqdn-verification
Enable/disable TLS FQDN verification (default =
disable).
option
-disable
Option
Description
enable
Enable TLS FQDN verification.
disable
Disable TLS FQDN verification.
config lan
Parameter
Description
Type
Size
Default
port-esl-mode
ESL port mode.
option
-offline
Option
Description
offline
Offline.
nat-to-wan
NAT WTP ESL port to WTP WAN port.
bridge-to-wan
Bridge WTP ESL port to WTP WAN port.
bridge-to-ssid
Bridge WTP ESL port to SSID.
port-esl-ssid
Bridge ESL port to SSID.
string
Maximum
length: 15
port-mode
LAN port mode.
option
-offline
Option
Description
offline
Offline.
nat-to-wan
NAT WTP LAN port to WTP WAN port.
FortiOS 8.0.0 CLI Reference
2869
Fortinet Inc.

<!-- 来源页 2870 -->
Parameter
Description
Type
Size
Default
Option
Description
bridge-to-wan
Bridge WTP LAN port to WTP WAN port.
bridge-to-ssid
Bridge WTP LAN port to SSID.
port-ssid
Bridge LAN port to SSID.
string
Maximum
length: 15
port1-mode
LAN port 1 mode.
option
-offline
Option
Description
offline
Offline.
nat-to-wan
NAT WTP LAN port to WTP WAN port.
bridge-to-wan
Bridge WTP LAN port to WTP WAN port.
bridge-to-ssid
Bridge WTP LAN port to SSID.
port1-ssid
Bridge LAN port 1 to SSID.
string
Maximum
length: 15
port2-mode
LAN port 2 mode.
option
-offline
Option
Description
offline
Offline.
nat-to-wan
NAT WTP LAN port to WTP WAN port.
bridge-to-wan
Bridge WTP LAN port to WTP WAN port.
bridge-to-ssid
Bridge WTP LAN port to SSID.
port2-ssid
Bridge LAN port 2 to SSID.
string
Maximum
length: 15
port3-mode
LAN port 3 mode.
option
-offline
Option
Description
offline
Offline.
nat-to-wan
NAT WTP LAN port to WTP WAN port.
bridge-to-wan
Bridge WTP LAN port to WTP WAN port.
bridge-to-ssid
Bridge WTP LAN port to SSID.
port3-ssid
Bridge LAN port 3 to SSID.
string
Maximum
length: 15
port4-mode
LAN port 4 mode.
option
-offline
FortiOS 8.0.0 CLI Reference
2870
Fortinet Inc.

<!-- 来源页 2871 -->
Parameter
Description
Type
Size
Default
Option
Description
offline
Offline.
nat-to-wan
NAT WTP LAN port to WTP WAN port.
bridge-to-wan
Bridge WTP LAN port to WTP WAN port.
bridge-to-ssid
Bridge WTP LAN port to SSID.
port4-ssid
Bridge LAN port 4 to SSID.
string
Maximum
length: 15
port5-mode
LAN port 5 mode.
option
-offline
Option
Description
offline
Offline.
nat-to-wan
NAT WTP LAN port to WTP WAN port.
bridge-to-wan
Bridge WTP LAN port to WTP WAN port.
bridge-to-ssid
Bridge WTP LAN port to SSID.
port5-ssid
Bridge LAN port 5 to SSID.
string
Maximum
length: 15
port6-mode
LAN port 6 mode.
option
-offline
Option
Description
offline
Offline.
nat-to-wan
NAT WTP LAN port to WTP WAN port.
bridge-to-wan
Bridge WTP LAN port to WTP WAN port.
bridge-to-ssid
Bridge WTP LAN port to SSID.
port6-ssid
Bridge LAN port 6 to SSID.
string
Maximum
length: 15
port7-mode
LAN port 7 mode.
option
-offline
Option
Description
offline
Offline.
nat-to-wan
NAT WTP LAN port to WTP WAN port.
bridge-to-wan
Bridge WTP LAN port to WTP WAN port.
bridge-to-ssid
Bridge WTP LAN port to SSID.
FortiOS 8.0.0 CLI Reference
2871
Fortinet Inc.

<!-- 来源页 2872 -->
Parameter
Description
Type
Size
Default
port7-ssid
Bridge LAN port 7 to SSID.
string
Maximum
length: 15
port8-mode
LAN port 8 mode.
option
-offline
Option
Description
offline
Offline.
nat-to-wan
NAT WTP LAN port to WTP WAN port.
bridge-to-wan
Bridge WTP LAN port to WTP WAN port.
bridge-to-ssid
Bridge WTP LAN port to SSID.
port8-ssid
Bridge LAN port 8 to SSID.
string
Maximum
length: 15
config lbs
Parameter
Description
Type
Size
Default
aeroscout
Enable/disable AeroScout Real
Time Location Service (RTLS)
support (default = disable).
option
-disable
Option
Description
enable
Enable AeroScout support.
disable
Disable AeroScout support.
aeroscout-ap-mac
Use BSSID or board MAC address
as AP MAC address in AeroScout
AP messages (default = bssid).
option
-bssid
Option
Description
bssid
Use BSSID as AP MAC address in AeroScout AP messages.
board-mac
Use board MAC address as AP MAC address in AeroScout AP
messages.
aeroscout-mmu-report
Enable/disable compounded
AeroScout tag and MU report
(default = enable).
option
-enable
Option
Description
enable
Enable compounded AeroScout tag and MU report.
disable
Disable compounded AeroScout tag and MU report.
FortiOS 8.0.0 CLI Reference
2872
Fortinet Inc.

<!-- 来源页 2873 -->
Parameter
Description
Type
Size
Default
aeroscout-mu
Enable/disable AeroScout Mobile
Unit (MU) support (default =
disable).
option
-disable
Option
Description
enable
Enable AeroScout MU mode support.
disable
Disable AeroScout MU mode support.
aeroscout-mu-factor
AeroScout MU mode dilution
factor (default = 20).
integer
Minimum value:
0 Maximum
value:
4294967295
20
aeroscout-mu-timeout
AeroScout MU mode timeout (0 -65535 sec, default = 5).
integer
Minimum value:
0 Maximum
value: 65535
5
aeroscout-server-ip
IP address of AeroScout server.
ipv4-address-any
Not Specified
0.0.0.0
aeroscout-server-port
AeroScout server UDP listening
port.
integer
Minimum value:
1024 Maximum
value: 65535
0
ble-rtls
Set BLE Real Time Location
Service (RTLS) support (default =
none).
option
-none
Option
Description
none
Set BLE RTLS to none (default = none).
polestar
Set BLE RTLS to PoleStar.
evresys
Set BLE RTLS to Evresys.
ble-rtls-accumulation-interval
Time that measurements should
be accumulated in seconds
(default = 2).
integer
Minimum value:
1 Maximum
value: 60
2
ble-rtls-asset-addrgrp-list
Tags and asset addrgrp list to be
reported.
string
Maximum
length: 79
ble-rtls-asset-uuid-list1
Tags and asset UUID list 1 to be
reported (string in the format of
'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX').
string
Maximum
length: 36
FortiOS 8.0.0 CLI Reference
2873
Fortinet Inc.

<!-- 来源页 2874 -->
Parameter
Description
Type
Size
Default
ble-rtls-asset-uuid-list2
Tags and asset UUID list 2 to be
reported (string in the format of
'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX').
string
Maximum
length: 36
ble-rtls-asset-uuid-list3
Tags and asset UUID list 3 to be
reported (string in the format of
'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX').
string
Maximum
length: 36
ble-rtls-asset-uuid-list4
Tags and asset UUID list 4 to be
reported (string in the format of
'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX').
string
Maximum
length: 36
ble-rtls-protocol
Select the protocol to report
Measurements, Advertising Data,
or Location Data to Cloud Server
(default = WSS).
option
-WSS
Option
Description
WSS
Use WebSocket protocol to report Measurements, Advertising Data,
or Location Data to Cloud Server.
ble-rtls-reporting-interval
Time between reporting
accumulated measurements in
seconds (default = 2).
integer
Minimum value:
1 Maximum
value: 600
2
ble-rtls-server-fqdn
FQDN of BLE Real Time Location
Service (RTLS) Server.
string
Maximum
length: 255
ble-rtls-server-path
Path of BLE Real Time Location
Service (RTLS) Server.
string
Maximum
length: 255
ble-rtls-server-port
Port of BLE Real Time Location
Service (RTLS) Server (default =
443).
integer
Minimum value:
1 Maximum
value: 65535
443
ble-rtls-server-token
Access Token of BLE Real Time
Location Service (RTLS) Server.
string
Maximum
length: 31
ekahau-blink-mode
Enable/disable Ekahau blink mode
(now known as AiRISTA Flow) to
track and locate WiFi tags (default
= disable).
option
-disable
Option
Description
enable
Enable Ekahau blink mode.
disable
Disable Ekahau blink mode.
FortiOS 8.0.0 CLI Reference
2874
Fortinet Inc.

<!-- 来源页 2875 -->
Parameter
Description
Type
Size
Default
ekahau-tag
WiFi frame MAC address or WiFi
Tag.
mac-address
Not Specified
01:18:8e:00:00:00
erc-server-ip
IP address of Ekahau RTLS
Controller (ERC).
ipv4-address-any
Not Specified
0.0.0.0
erc-server-port
Ekahau RTLS Controller (ERC) UDP
listening port.
integer
Minimum value:
1024 Maximum
value: 65535
8569
fortipresence
Enable/disable FortiPresence to
monitor the location and activity of
WiFi clients even if they don't
connect to this WiFi network
(default = disable).
option
-disable
Option
Description
foreign
FortiPresence monitors foreign channels only. Foreign channels mean
all other available channels than the current operating channel of the
WTP, AP, or FortiAP.
both
Enable FortiPresence on both foreign and home channels. Select this
option to have FortiPresence monitor all WiFi channels.
disable
Disable FortiPresence.
fortipresence-ble
Enable/disable FortiPresence
finding and reporting BLE devices.
option
-enable
Option
Description
enable
Enable FortiPresence finding and reporting BLE devices.
disable
Disable FortiPresence finding and reporting BLE devices.
fortipresence-frequency
FortiPresence report transmit
frequency (5 - 65535 sec, default
= 30).
integer
Minimum value:
5 Maximum
value: 65535
30
fortipresence-port
UDP listening port of
FortiPresence server (default =
3000).
integer
Minimum value:
300 Maximum
value: 65535
3000
fortipresence-project
FortiPresence project name (max.
16 characters, default =
fortipresence).
string
Maximum
length: 16
fortipresence
fortipresence-rogue
Enable/disable FortiPresence
finding and reporting rogue APs.
option
-disable
FortiOS 8.0.0 CLI Reference
2875
Fortinet Inc.

<!-- 来源页 2876 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable FortiPresence finding and reporting rogue APs.
disable
Disable FortiPresence finding and reporting rogue APs.
fortipresence-secret
FortiPresence secret password
(max. 16 characters).
password
Not Specified
fortipresence-server
IP address of FortiPresence
server.
ipv4-address-any
Not Specified
0.0.0.0
fortipresence-server-addr-type
FortiPresence server address type
(default = ipv4).
option
-ipv4
Option
Description
ipv4
IPv4 address.
fqdn
Fully Qualified Domain Name address.
fortipresence-server-fqdn
FQDN of FortiPresence server.
string
Maximum
length: 255
fortipresence-unassoc
Enable/disable FortiPresence
finding and reporting unassociated
stations.
option
-enable
Option
Description
enable
Enable FortiPresence finding and reporting unassociated stations.
disable
Disable FortiPresence finding and reporting unassociated stations.
station-locate
Enable/disable client station
locating services for all clients,
whether associated or not (default
= disable).
option
-disable
Option
Description
enable
Enable station locating service.
disable
Disable station locating service.
FortiOS 8.0.0 CLI Reference
2876
Fortinet Inc.

<!-- 来源页 2877 -->
config platform
Parameter
Description
Type
Size
Default
ddscan
Enable/disable use of one radio for dedicated full-band scanning to detect RF characterization and
wireless threat management.
option
-disable
Option
Description
enable
Enable dedicated full-band scan mode.
disable
Disable dedicated full-band scan mode.
mode
Configure operation mode of 5G radios (default =
single-5G).
option
-single-5G
Option
Description
single-5G
Configure radios as one 5GHz band, one 2.4GHz band, and one
dedicated monitor or sniffer.
dual-5G
Configure radios as one lower 5GHz band, one higher 5GHz band and
one 2.4GHz band respectively.
type
WTP, FortiAP or AP platform type. There are built-in
WTP profiles for all supported FortiAP models. You
can select a built-in profile and customize it or
create a new profile.
option
-221E
Option
Description
AP-11N
Default 11n AP.
421E
FAP421E.
423E
FAP423E.
221E
FAP221E.
223E
FAP223E.
431F
FAP431F.
431FL
FAP431FL.
432F
FAP432F.
432FR
FAP432FR.
433F
FAP433F.
433FL
FAP433FL.
231F
FAP231F.
231FL
FAP231FL.
FortiOS 8.0.0 CLI Reference
2877
Fortinet Inc.

<!-- 来源页 2878 -->
Parameter
Description
Type
Size
Default
Option
Description
234F
FAP234F.
23JF
FAP23JF.
831F
FAP831F.
231G
FAP231G.
233G
FAP233G.
234G
FAP234G.
431G
FAP431G.
432G
FAP432G.
433G
FAP433G.
221K
FAP221K.
231K
FAP231K.
231KD
FAP231KD.
23JK
FAP23JK.
222KL
FAP222KL.
241K
FAP241K.
243K
FAP243K.
244K
FAP244K.
441K
FAP441K.
435K
FAP435K.
443K
FAP443K.
U431F
FAPU431F.
U433F
FAPU433F.
U231F
FAPU231F.
U234F
FAPU234F.
U432F
FAPU432F.
U231G
FAPU231G.
MVP
FAP MVP.
FortiOS 8.0.0 CLI Reference
2878
Fortinet Inc.

<!-- 来源页 2879 -->
config radio-1
Parameter
Description
Type
Size
Default
80211d
Enable/disable 802.11d countryie
(default = enable).
option
-enable
Option
Description
enable
Enable 802.11d countryie.
disable
Disable 802.11d countryie.
80211mc
Enable/disable radio 802.11mc
capability (default = disable).
option
-disable
Option
Description
enable
Enable radio 802.11mc capability.
disable
Disable radio 802.11mc capability.
ai-darrp-support
Enable/disable support for
FortiAIOps to retrieve Distributed
Automatic Radio Resource
Provisioning (DARRP) data through
REST API calls (default = disable).
option
-disable
Option
Description
enable
Enable support for FortiAIOps REST API calls for DARRP data.
disable
Disable support for FortiAIOps REST API calls for DARRP data.
airtime-fairness
Enable/disable airtime fairness
(default = disable).
option
-disable
Option
Description
enable
Enable airtime fairness (ATF) support.
disable
Disable airtime fairness (ATF) support.
amsdu
Enable/disable 802.11n AMSDU
support. AMSDU can improve
performance if supported by your
WiFi clients (default = enable).
option
-enable
Option
Description
enable
Enable AMSDU support.
disable
Disable AMSDU support.
FortiOS 8.0.0 CLI Reference
2879
Fortinet Inc.

<!-- 来源页 2880 -->
Parameter
Description
Type
Size
Default
ap-sniffer-addr
MAC address to monitor.
mac-address
Not Specified
00:00:00:00:00:00
ap-sniffer-bufsize
Sniffer buffer size (1 - 32 MB,
default = 16).
integer
Minimum value:
1 Maximum
value: 32
16
ap-sniffer-chan
Channel on which to operate the
sniffer (default = 6).
integer
Minimum value:
0 Maximum
value:
4294967295
36
ap-sniffer-chan-width
Channel bandwidth for sniffer.
option
-20MHz
Option
Description
320MHz
320 MHz channel width.
240MHz
240 MHz channel width.
160MHz
160 MHz channel width.
80MHz
80 MHz channel width.
40MHz
40 MHz channel width.
20MHz
20 MHz channel width.
ap-sniffer-ctl
Enable/disable sniffer on WiFi
control frame (default = enable).
option
-enable
Option
Description
enable
Enable sniffer on WiFi control frame.
disable
Disable sniffer on WiFi control frame.
ap-sniffer-data
Enable/disable sniffer on WiFi data
frame (default = enable).
option
-enable
Option
Description
enable
Enable sniffer on WiFi data frame
disable
Disable sniffer on WiFi data frame
ap-sniffer-mgmt-beacon
Enable/disable sniffer on WiFi
management Beacon frames
(default = enable).
option
-enable
FortiOS 8.0.0 CLI Reference
2880
Fortinet Inc.

<!-- 来源页 2881 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable sniffer on WiFi management beacon frame.
disable
Disable sniffer on WiFi management beacon frame.
ap-sniffer-mgmt-other
Enable/disable sniffer on WiFi
management other frames (default
= enable).
option
-enable
Option
Description
enable
Enable sniffer on WiFi management other frame.
disable
Disable sniffer on WiFi management other frame.
ap-sniffer-mgmt-probe
Enable/disable sniffer on WiFi
management probe frames (default
= enable).
option
-enable
Option
Description
enable
Enable sniffer on WiFi management probe frame.
disable
Enable sniffer on WiFi management probe frame.
arrp-profile
Distributed Automatic Radio
Resource Provisioning (DARRP)
profile name to assign to the radio.
string
Maximum
length: 35
auto-power-high
The upper bound of automatic
transmit power adjustment in dBm
(the actual range of transmit power
depends on the AP platform type).
integer
Minimum value:
0 Maximum
value:
4294967295
17
auto-power-level
Enable/disable automatic power-level adjustment to prevent co-channel interference (default =
disable).
option
-disable
Option
Description
enable
Enable automatic transmit power adjustment.
disable
Disable automatic transmit power adjustment.
auto-power-low
The lower bound of automatic
transmit power adjustment in dBm
(the actual range of transmit power
depends on the AP platform type).
integer
Minimum value:
0 Maximum
value:
4294967295
10
FortiOS 8.0.0 CLI Reference
2881
Fortinet Inc.

<!-- 来源页 2882 -->
Parameter
Description
Type
Size
Default
auto-power-target
Target of automatic transmit power
adjustment in dBm (-95 to -20,
default = -70).
string
Maximum
length: 7
-70
band
WiFi band that Radio 1 operates on.
option
-Option
Description
802.11a
802.11a.
802.11b
802.11b.
802.11g
802.11g.
802.11n-2G
802.11n (WiFi 4) at 2.4GHz.
802.11n-5G
802.11n (WiFi 4) at 5GHz.
802.11ac-2G
802.11ac (WiFi 5) at 2.4GHz.
802.11ac-5G
802.11ac (WiFi 5) at 5GHz.
802.11ax-2G
802.11ax (WiFi 6) at 2.4GHz.
802.11ax-5G
802.11ax (WiFi 6) at 5GHz.
802.11ax-6G
802.11ax (WiFi 6) at 6GHz.
802.11be-2G
802.11be (WiFi 7) at 2.4GHz.
802.11be-5G
802.11be (WiFi 7) at 5GHz.
802.11be-6G
802.11be (WiFi 7) at 6GHz.
band-5g-type
WiFi 5G band type.
option
-5g-full
Option
Description
5g-full
Full 5G band.
5g-high
High 5G band.
5g-low
Low 5G band.
bandwidth-admission-control
Enable/disable WiFi multimedia
(WMM) bandwidth admission
control to optimize WiFi bandwidth
use. A request to join the wireless
network is only allowed if the access
point has enough bandwidth to
support it.
option
-disable
FortiOS 8.0.0 CLI Reference
2882
Fortinet Inc.

<!-- 来源页 2883 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable WMM bandwidth admission control.
disable
Disable WMM bandwidth admission control.
bandwidth-capacity
Maximum bandwidth capacity
allowed (1 - 600000 Kbps, default =
2000).
integer
Minimum value:
1 Maximum
value: 600000
2000
beacon-interval
Beacon interval. The time between
beacon frames in milliseconds.
Actual range of beacon interval
depends on the AP platform type
(default = 100).
integer
Minimum value:
0 Maximum
value: 65535
100
bss-color
BSS color value for this 11ax radio (0
- 63, disable = 0, default = 0).
integer
Minimum value:
0 Maximum
value: 63
0
bss-color-mode
BSS color mode for this 11ax radio
(default = auto).
option
-auto
Option
Description
auto
Automatically select BSS color value on AP.
static
Set BSS color value on this radio based on 'bss-color' CLI.
call-admission-control
Enable/disable WiFi multimedia
(WMM) call admission control to
optimize WiFi bandwidth use for
VoIP calls. New VoIP calls are only
accepted if there is enough
bandwidth available to support
them.
option
-disable
Option
Description
enable
Enable WMM call admission control.
disable
Disable WMM call admission control.
call-capacity
Maximum number of Voice over
WLAN (VoWLAN) phones supported
by the radio (0 - 60, default = 10).
integer
Minimum value:
0 Maximum
value: 60
10
cca-threshold
*
Configure Clear Channel
Assessment (CCA) threshold in dBm
(-94 to -11, default = 0, 0 for
unconfigured).
string
Maximum
length: 7
0
FortiOS 8.0.0 CLI Reference
2883
Fortinet Inc.

<!-- 来源页 2884 -->
Parameter
Description
Type
Size
Default
channel
<chan>
Selected list of wireless radio
channels.
Channel number.
string
Maximum
length: 3
channel-bonding
Channel bandwidth: 320, 240, 160,
80, 40, or 20MHz. Channels may
use both 20 and 40 by enabling
coexistence.
option
-20MHz
Option
Description
320MHz
320 MHz channel width.
240MHz
240 MHz channel width.
160MHz
160 MHz channel width.
80MHz
80 MHz channel width.
40MHz
40 MHz channel width.
20MHz
20 MHz channel width.
channel-bonding-ext
Channel bandwidth extension: 320
MHz-1 and 320 MHz-2 (default =
320 MHz-2).
option
-320MHz-2
Option
Description
320MHz-1
320 MHz channel with channel center frequency numbered 31, 95, and
159.
320MHz-2
320 MHz channel with channel center frequency numbered 63, 127,
and 191.
channel-utilization
Enable/disable measuring channel
utilization.
option
-enable
Option
Description
enable
Enable measuring channel utilization.
disable
Disable measuring channel utilization.
coexistence
Enable/disable allowing both HT20
and HT40 on the same radio
(default = enable).
option
-enable
Option
Description
enable
Enable support for both HT20 and HT40 on the same radio.
disable
Disable support for both HT20 and HT40 on the same radio.
FortiOS 8.0.0 CLI Reference
2884
Fortinet Inc.

<!-- 来源页 2885 -->
Parameter
Description
Type
Size
Default
darrp
Enable/disable Distributed
Automatic Radio Resource
Provisioning (DARRP) to make sure
the radio is always using the most
optimal channel (default = disable).
option
-disable
Option
Description
enable
Enable distributed automatic radio resource provisioning.
disable
Disable distributed automatic radio resource provisioning.
drma
Enable/disable dynamic radio mode
assignment (DRMA) (default =
disable).
option
-disable
Option
Description
disable
Disable dynamic radio mode assignment (DRMA).
enable
Enable dynamic radio mode assignment (DRMA).
drma-sensitivity
Network Coverage Factor (NCF)
percentage required to consider a
radio as redundant (default = low).
option
-low
Option
Description
low
Consider a radio as redundant when its NCF is 100%.
medium
Consider a radio as redundant when its NCF is 95%.
high
Consider a radio as redundant when its NCF is 90%.
dtim
Delivery Traffic Indication Map
(DTIM) period (1 - 255, default = 1).
Set higher to save battery life of
WiFi client in power-save mode.
integer
Minimum value:
1 Maximum
value: 255
1
frag-threshold
Maximum packet size that can be
sent without fragmentation (800 -2346 bytes, default = 2346).
integer
Minimum value:
800 Maximum
value: 2346
2346
iperf-protocol
Iperf test protocol (default = "UDP").
option
-udp
Option
Description
udp
UDP.
tcp
TCP.
FortiOS 8.0.0 CLI Reference
2885
Fortinet Inc.

<!-- 来源页 2886 -->
Parameter
Description
Type
Size
Default
iperf-server-port
Iperf service port number.
integer
Minimum value:
0 Maximum
value: 65535
5001
max-clients
Maximum number of stations (STAs)
or WiFi clients supported by the
radio. Range depends on the
hardware.
integer
Minimum value:
0 Maximum
value:
4294967295
0
max-distance
Maximum expected distance
between the AP and clients (0 -54000 m, default = 0).
integer
Minimum value:
0 Maximum
value: 54000
0
mimo-mode
Configure radio MIMO mode (default
= default).
option
-default
Option
Description
default
Default radio MIMO mode.
1x1
1x1 radio MIMO mode.
2x2
2x2 radio MIMO mode.
3x3
3x3 radio MIMO mode.
4x4
4x4 radio MIMO mode.
8x8
8x8 radio MIMO mode.
mode
Mode of radio 1. Radio 1 can be
disabled, configured as an access
point, a rogue AP monitor, a sniffer,
or a station.
option
-ap
Option
Description
disabled
Radio 1 is disabled.
ap
Radio 1 operates as an access point that allows WiFi clients to connect
to your network.
monitor
Radio 1 operates as a dedicated monitor. As a monitor, the radio scans
for other WiFi access points and adds them to the Rogue AP monitor
list.
sniffer
Radio 1 operates as a sniffer capturing WiFi frames on air.
sam
Radio 1 operates as a station that can connect to a neighboring AP for
connectivity and health check.
optional-antenna
Optional antenna used on FAP
(default = none).
option
-none
FortiOS 8.0.0 CLI Reference
2886
Fortinet Inc.

<!-- 来源页 2887 -->
Parameter
Description
Type
Size
Default
Option
Description
none
None.
custom
Customize optional antenna gain.
FANT-04ABGN-0606-O-N
6 dBi(2.4GHz) and 6 dBi(5GHz).
FANT-04ABGN-1414-P-N
14 dBi(2.4GHz) and 14 dBi(5GHz).
FANT-04ABGN-8065-P-N
8 dBi(2.4GHz) and 6.5 dBi(5GHz).
FANT-04ABGN-0606-O-R
6 dBi(2.4GHz) and 6 dBi(5GHz).
FANT-04ABGN-0606-P-R
6 dBi(2.4GHz) and 6 dBi(5GHz).
FANT-10ACAX-1213-D-N
12 dBi(2.4GHz) and 13 dBi(5GHz).
FANT-08ABGN-1213-D-R
12 dBi(2.4GHz) and 13 dBi(5GHz).
FANT-04BEAX-0606-P-R
6 dBi(2.4GHz), 6 dBi(5GHz) and 6 dBi(6GHz).
optional-antenna-gain
Optional antenna gain in dBi (0 to
20, default = 0).
string
Maximum
length: 7
0
power-level
Radio EIRP power level as a
percentage of the maximum EIRP
power (0 - 100, default = 100).
integer
Minimum value:
0 Maximum
value: 100
100
power-mode
Set radio effective isotropic radiated
power (EIRP) in dBm or by a
percentage of the maximum EIRP
(default = percentage). This power
takes into account both radio
transmit power and antenna gain.
Higher power level settings may be
constrained by local regulatory
requirements and AP capabilities.
option
-percentage
FortiOS 8.0.0 CLI Reference
2887
Fortinet Inc.

<!-- 来源页 2888 -->
Parameter
Description
Type
Size
Default
Option
Description
dBm
Set radio EIRP power in dBm.
percentage
Set radio EIRP power by percentage.
power-value
Radio EIRP power in dBm (1 - 33,
default = 27).
integer
Minimum value:
1 Maximum
value: 33
27
powersave-optimize
Enable client power-saving features
such as TIM, AC VO, and OBSS etc.
option
-Option
Description
tim
TIM bit for client in power save mode.
ac-vo
Use AC VO priority to send out packets in the power save queue.
no-obss-scan
Do not put OBSS scan IE into beacon and probe response frames.
no-11b-rate
Do not send frame using 11b data rate.
client-rate-follow
Adapt transmitting PHY rate with receiving PHY rate from a client.
protection-mode
Enable/disable 802.11g protection
modes to support backwards
compatibility with older clients
(rtscts, ctsonly, disable).
option
-disable
Option
Description
rtscts
Enable 802.11g protection RTS/CTS mode.
ctsonly
Enable 802.11g protection CTS only mode.
disable
Disable 802.11g protection mode.
rts-threshold
Maximum packet size for RTS
transmissions, specifying the
maximum size of a data packet
before RTS/CTS (256 - 2346 bytes,
default = 2346).
integer
Minimum value:
256 Maximum
value: 2346
2346
sam-bssid
BSSID for WiFi network.
mac-address
Not Specified
00:00:00:00:00:00
sam-ca-certificate
CA certificate for WPA2/WPA3-ENTERPRISE.
string
Maximum
length: 79
sam-captive-portal
Enable/disable Captive Portal
Authentication (default = disable).
option
-disable
FortiOS 8.0.0 CLI Reference
2888
Fortinet Inc.

<!-- 来源页 2889 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable Captive Portal Authentication.
disable
Disable Captive Portal Authentication.
sam-client-certificate
Client certificate for WPA2/WPA3-ENTERPRISE.
string
Maximum
length: 35
sam-cwp-failure-string
Failure identification on the page
after an incorrect login.
string
Maximum
length: 64
sam-cwp-match-string
Identification string from the captive
portal login form.
string
Maximum
length: 64
sam-cwp-password
Password for captive portal
authentication.
password
Not Specified
sam-cwp-success-string
Success identification on the page
after a successful login.
string
Maximum
length: 64
sam-cwp-test-url
Website the client is trying to
access.
string
Maximum
length: 255
sam-cwp-username
Username for captive portal
authentication.
string
Maximum
length: 35
sam-eap-method
Select WPA2/WPA3-ENTERPRISE
EAP Method (default = PEAP).
option
-peap
Option
Description
both
EAP PEAP and TLS. (Not applicable in FIPS mode)
tls
EAP TLS.
peap
EAP PEAP. (Not applicable in FIPS mode)
sam-password
Passphrase for WiFi network
connection.
password
Not Specified
sam-private-key
Private key for WPA2/WPA3-ENTERPRISE.
string
Maximum
length: 35
sam-private-key-password
Password for private key file for
WPA2/WPA3-ENTERPRISE.
password
Not Specified
sam-report-intv
SAM report interval (sec), 0 for a
one-time report.
integer
Minimum value:
60 Maximum
value: 864000
0
FortiOS 8.0.0 CLI Reference
2889
Fortinet Inc.

<!-- 来源页 2890 -->
Parameter
Description
Type
Size
Default
sam-security-type
Select WiFi network security type
(default = "wpa-personal" for
2.4/5G radio, "wpa3-sae" for 6G
radio).
option
-wpa-personal
Option
Description
open
Open.
wpa-personal
WPA/WPA2 personal.
wpa-enterprise
WPA2/WPA3 enterprise.
wpa3-sae
WPA3 SAE.
owe
OWE.
sam-server-fqdn
SAM test server domain name.
string
Maximum
length: 255
sam-server-ip
SAM test server IP address.
ipv4-address
Not Specified
0.0.0.0
sam-server-type
Select SAM server type (default =
"IP").
option
-ip
Option
Description
ip
IPv4 address.
fqdn
Fully Qualified Domain Name address.
sam-ssid
SSID for WiFi network.
string
Maximum
length: 32
sam-test
Select SAM test type (default =
"PING").
option
-ping
Option
Description
ping
PING test.
iperf
IPERF test.
sam-username
Username for WiFi network
connection.
string
Maximum
length: 35
short-guard-interval
Use either the short guard interval
(Short GI) of 400 ns or the long
guard interval (Long GI) of 800 ns.
option
-disable
FortiOS 8.0.0 CLI Reference
2890
Fortinet Inc.

<!-- 来源页 2891 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Select the 400 ns short guard interval (Short GI).
disable
Select the 800 ns long guard interval (Long GI).
transmit-optimize
Packet transmission optimization
options including power saving,
aggregation limiting, retry limiting,
etc. All are enabled by default.
option
-power-save aggr-limit retry-limit send-bar
Option
Description
disable
Disable packet transmission optimization.
power-save
Tag client as operating in power save mode if excessive transmit retries
occur.
aggr-limit
Set aggregation limit to a lower value when data rate is low.
retry-limit
Set software retry limit to a lower value when data rate is low.
send-bar
Limit transmission of BAR frames.
vap-all
Configure method for assigning
SSIDs to this FortiAP (default =
automatically assign tunnel SSIDs).
option
-tunnel
Option
Description
tunnel
Automatically select tunnel SSIDs.
bridge
Automatically select local-bridging SSIDs.
manual
Manually select SSIDs.
vap-status *
Enable/disable all configured SSIDs
on this radio (default = enable).
option
-enable
Option
Description
enable
Enable all configured SSIDs on this radio.
disable
Disable all configured SSIDs on this radio.
vaps <name>
Manually selected list of Virtual
Access Points (VAPs).
Virtual Access Point (VAP) name.
string
Maximum
length: 35
wids-profile
Wireless Intrusion Detection System
(WIDS) profile name to assign to the
radio.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
2891
Fortinet Inc.

<!-- 来源页 2892 -->
Parameter
Description
Type
Size
Default
zero-wait-dfs
Enable/disable zero wait DFS on
radio (default = enable).
option
-enable
Option
Description
enable
Enable zero wait DFS
disable
Disable zero wait DFS
* This parameter may not exist in some models.
config radio-2
Parameter
Description
Type
Size
Default
80211d
Enable/disable 802.11d countryie
(default = enable).
option
-enable
Option
Description
enable
Enable 802.11d countryie.
disable
Disable 802.11d countryie.
80211mc
Enable/disable radio 802.11mc
capability (default = disable).
option
-disable
Option
Description
enable
Enable radio 802.11mc capability.
disable
Disable radio 802.11mc capability.
ai-darrp-support
Enable/disable support for
FortiAIOps to retrieve Distributed
Automatic Radio Resource
Provisioning (DARRP) data through
REST API calls (default = disable).
option
-disable
Option
Description
enable
Enable support for FortiAIOps REST API calls for DARRP data.
disable
Disable support for FortiAIOps REST API calls for DARRP data.
airtime-fairness
Enable/disable airtime fairness
(default = disable).
option
-disable
Option
Description
enable
Enable airtime fairness (ATF) support.
FortiOS 8.0.0 CLI Reference
2892
Fortinet Inc.

<!-- 来源页 2893 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable airtime fairness (ATF) support.
amsdu
Enable/disable 802.11n AMSDU
support. AMSDU can improve
performance if supported by your
WiFi clients (default = enable).
option
-enable
Option
Description
enable
Enable AMSDU support.
disable
Disable AMSDU support.
ap-sniffer-addr
MAC address to monitor.
mac-address
Not Specified
00:00:00:00:00:00
ap-sniffer-bufsize
Sniffer buffer size (1 - 32 MB,
default = 16).
integer
Minimum value:
1 Maximum
value: 32
16
ap-sniffer-chan
Channel on which to operate the
sniffer (default = 6).
integer
Minimum value:
0 Maximum
value:
4294967295
6
ap-sniffer-chan-width
Channel bandwidth for sniffer.
option
-20MHz
Option
Description
320MHz
320 MHz channel width.
240MHz
240 MHz channel width.
160MHz
160 MHz channel width.
80MHz
80 MHz channel width.
40MHz
40 MHz channel width.
20MHz
20 MHz channel width.
ap-sniffer-ctl
Enable/disable sniffer on WiFi
control frame (default = enable).
option
-enable
Option
Description
enable
Enable sniffer on WiFi control frame.
disable
Disable sniffer on WiFi control frame.
FortiOS 8.0.0 CLI Reference
2893
Fortinet Inc.

<!-- 来源页 2894 -->
Parameter
Description
Type
Size
Default
ap-sniffer-data
Enable/disable sniffer on WiFi data
frame (default = enable).
option
-enable
Option
Description
enable
Enable sniffer on WiFi data frame
disable
Disable sniffer on WiFi data frame
ap-sniffer-mgmt-beacon
Enable/disable sniffer on WiFi
management Beacon frames
(default = enable).
option
-enable
Option
Description
enable
Enable sniffer on WiFi management beacon frame.
disable
Disable sniffer on WiFi management beacon frame.
ap-sniffer-mgmt-other
Enable/disable sniffer on WiFi
management other frames (default
= enable).
option
-enable
Option
Description
enable
Enable sniffer on WiFi management other frame.
disable
Disable sniffer on WiFi management other frame.
ap-sniffer-mgmt-probe
Enable/disable sniffer on WiFi
management probe frames (default
= enable).
option
-enable
Option
Description
enable
Enable sniffer on WiFi management probe frame.
disable
Enable sniffer on WiFi management probe frame.
arrp-profile
Distributed Automatic Radio
Resource Provisioning (DARRP)
profile name to assign to the radio.
string
Maximum
length: 35
auto-power-high
The upper bound of automatic
transmit power adjustment in dBm
(the actual range of transmit power
depends on the AP platform type).
integer
Minimum value:
0 Maximum
value:
4294967295
17
auto-power-level
Enable/disable automatic power-level adjustment to prevent co-channel interference (default =
disable).
option
-disable
FortiOS 8.0.0 CLI Reference
2894
Fortinet Inc.

<!-- 来源页 2895 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable automatic transmit power adjustment.
disable
Disable automatic transmit power adjustment.
auto-power-low
The lower bound of automatic
transmit power adjustment in dBm
(the actual range of transmit power
depends on the AP platform type).
integer
Minimum value:
0 Maximum
value:
4294967295
10
auto-power-target
Target of automatic transmit power
adjustment in dBm (-95 to -20,
default = -70).
string
Maximum
length: 7
-70
band
WiFi band that Radio 2 operates on.
option
-Option
Description
802.11a
802.11a.
802.11b
802.11b.
802.11g
802.11g.
802.11n-2G
802.11n (WiFi 4) at 2.4GHz.
802.11n-5G
802.11n (WiFi 4) at 5GHz.
802.11ac-2G
802.11ac (WiFi 5) at 2.4GHz.
802.11ac-5G
802.11ac (WiFi 5) at 5GHz.
802.11ax-2G
802.11ax (WiFi 6) at 2.4GHz.
802.11ax-5G
802.11ax (WiFi 6) at 5GHz.
802.11ax-6G
802.11ax (WiFi 6) at 6GHz.
802.11be-2G
802.11be (WiFi 7) at 2.4GHz.
802.11be-5G
802.11be (WiFi 7) at 5GHz.
802.11be-6G
802.11be (WiFi 7) at 6GHz.
band-5g-type
WiFi 5G band type.
option
-5g-full
Option
Description
5g-full
Full 5G band.
5g-high
High 5G band.
5g-low
Low 5G band.
FortiOS 8.0.0 CLI Reference
2895
Fortinet Inc.

<!-- 来源页 2896 -->
Parameter
Description
Type
Size
Default
bandwidth-admission-control
Enable/disable WiFi multimedia
(WMM) bandwidth admission
control to optimize WiFi bandwidth
use. A request to join the wireless
network is only allowed if the access
point has enough bandwidth to
support it.
option
-disable
Option
Description
enable
Enable WMM bandwidth admission control.
disable
Disable WMM bandwidth admission control.
bandwidth-capacity
Maximum bandwidth capacity
allowed (1 - 600000 Kbps, default =
2000).
integer
Minimum value:
1 Maximum
value: 600000
2000
beacon-interval
Beacon interval. The time between
beacon frames in milliseconds.
Actual range of beacon interval
depends on the AP platform type
(default = 100).
integer
Minimum value:
0 Maximum
value: 65535
100
bss-color
BSS color value for this 11ax radio (0
- 63, disable = 0, default = 0).
integer
Minimum value:
0 Maximum
value: 63
0
bss-color-mode
BSS color mode for this 11ax radio
(default = auto).
option
-auto
Option
Description
auto
Automatically select BSS color value on AP.
static
Set BSS color value on this radio based on 'bss-color' CLI.
call-admission-control
Enable/disable WiFi multimedia
(WMM) call admission control to
optimize WiFi bandwidth use for
VoIP calls. New VoIP calls are only
accepted if there is enough
bandwidth available to support
them.
option
-disable
Option
Description
enable
Enable WMM call admission control.
disable
Disable WMM call admission control.
FortiOS 8.0.0 CLI Reference
2896
Fortinet Inc.

<!-- 来源页 2897 -->
Parameter
Description
Type
Size
Default
call-capacity
Maximum number of Voice over
WLAN (VoWLAN) phones supported
by the radio (0 - 60, default = 10).
integer
Minimum value:
0 Maximum
value: 60
10
cca-threshold
*
Configure Clear Channel
Assessment (CCA) threshold in dBm
(-94 to -11, default = 0, 0 for
unconfigured).
string
Maximum
length: 7
0
channel
<chan>
Selected list of wireless radio
channels.
Channel number.
string
Maximum
length: 3
channel-bonding
Channel bandwidth: 320, 240, 160,
80, 40, or 20MHz. Channels may
use both 20 and 40 by enabling
coexistence.
option
-20MHz
Option
Description
320MHz
320 MHz channel width.
240MHz
240 MHz channel width.
160MHz
160 MHz channel width.
80MHz
80 MHz channel width.
40MHz
40 MHz channel width.
20MHz
20 MHz channel width.
channel-bonding-ext
Channel bandwidth extension: 320
MHz-1 and 320 MHz-2 (default =
320 MHz-2).
option
-320MHz-2
Option
Description
320MHz-1
320 MHz channel with channel center frequency numbered 31, 95, and
159.
320MHz-2
320 MHz channel with channel center frequency numbered 63, 127,
and 191.
channel-utilization
Enable/disable measuring channel
utilization.
option
-enable
Option
Description
enable
Enable measuring channel utilization.
disable
Disable measuring channel utilization.
FortiOS 8.0.0 CLI Reference
2897
Fortinet Inc.

<!-- 来源页 2898 -->
Parameter
Description
Type
Size
Default
coexistence
Enable/disable allowing both HT20
and HT40 on the same radio
(default = enable).
option
-enable
Option
Description
enable
Enable support for both HT20 and HT40 on the same radio.
disable
Disable support for both HT20 and HT40 on the same radio.
darrp
Enable/disable Distributed
Automatic Radio Resource
Provisioning (DARRP) to make sure
the radio is always using the most
optimal channel (default = disable).
option
-disable
Option
Description
enable
Enable distributed automatic radio resource provisioning.
disable
Disable distributed automatic radio resource provisioning.
drma
Enable/disable dynamic radio mode
assignment (DRMA) (default =
disable).
option
-disable
Option
Description
disable
Disable dynamic radio mode assignment (DRMA).
enable
Enable dynamic radio mode assignment (DRMA).
drma-sensitivity
Network Coverage Factor (NCF)
percentage required to consider a
radio as redundant (default = low).
option
-low
Option
Description
low
Consider a radio as redundant when its NCF is 100%.
medium
Consider a radio as redundant when its NCF is 95%.
high
Consider a radio as redundant when its NCF is 90%.
dtim
Delivery Traffic Indication Map
(DTIM) period (1 - 255, default = 1).
Set higher to save battery life of
WiFi client in power-save mode.
integer
Minimum value:
1 Maximum
value: 255
1
frag-threshold
Maximum packet size that can be
sent without fragmentation (800 -2346 bytes, default = 2346).
integer
Minimum value:
800 Maximum
value: 2346
2346
FortiOS 8.0.0 CLI Reference
2898
Fortinet Inc.

<!-- 来源页 2899 -->
Parameter
Description
Type
Size
Default
iperf-protocol
Iperf test protocol (default = "UDP").
option
-udp
Option
Description
udp
UDP.
tcp
TCP.
iperf-server-port
Iperf service port number.
integer
Minimum value:
0 Maximum
value: 65535
5001
max-clients
Maximum number of stations (STAs)
or WiFi clients supported by the
radio. Range depends on the
hardware.
integer
Minimum value:
0 Maximum
value:
4294967295
0
max-distance
Maximum expected distance
between the AP and clients (0 -54000 m, default = 0).
integer
Minimum value:
0 Maximum
value: 54000
0
mimo-mode
Configure radio MIMO mode (default
= default).
option
-default
Option
Description
default
Default radio MIMO mode.
1x1
1x1 radio MIMO mode.
2x2
2x2 radio MIMO mode.
3x3
3x3 radio MIMO mode.
4x4
4x4 radio MIMO mode.
8x8
8x8 radio MIMO mode.
mode
Mode of radio 2. Radio 2 can be
disabled, configured as an access
point, a rogue AP monitor, a sniffer,
or a station.
option
-ap
Option
Description
disabled
Radio 2 is disabled.
ap
Radio 2 operates as an access point that allows WiFi clients to connect
to your network.
FortiOS 8.0.0 CLI Reference
2899
Fortinet Inc.

<!-- 来源页 2900 -->
Parameter
Description
Type
Size
Default
Option
Description
monitor
Radio 2 operates as a dedicated monitor. As a monitor, the radio scans
for other WiFi access points and adds them to the Rogue AP monitor
list.
sniffer
Radio 2 operates as a sniffer capturing WiFi frames on air.
sam
Radio 2 operates as a station that can connect to a neighboring AP for
connectivity and health check.
optional-antenna
Optional antenna used on FAP
(default = none).
option
-none
Option
Description
none
None.
custom
Customize optional antenna gain.
FANT-04ABGN-0606-O-N
6 dBi(2.4GHz) and 6 dBi(5GHz).
FANT-04ABGN-1414-P-N
14 dBi(2.4GHz) and 14 dBi(5GHz).
FANT-04ABGN-8065-P-N
8 dBi(2.4GHz) and 6.5 dBi(5GHz).
FANT-04ABGN-0606-O-R
6 dBi(2.4GHz) and 6 dBi(5GHz).
FANT-04ABGN-0606-P-R
6 dBi(2.4GHz) and 6 dBi(5GHz).
FANT-10ACAX-1213-D-N
12 dBi(2.4GHz) and 13 dBi(5GHz).
FANT-08ABGN-1213-D-R
12 dBi(2.4GHz) and 13 dBi(5GHz).
FANT-04BEAX-0606-P-R
6 dBi(2.4GHz), 6 dBi(5GHz) and 6 dBi(6GHz).
optional-antenna-gain
Optional antenna gain in dBi (0 to
20, default = 0).
string
Maximum
length: 7
0
FortiOS 8.0.0 CLI Reference
2900
Fortinet Inc.

<!-- 来源页 2901 -->
Parameter
Description
Type
Size
Default
power-level
Radio EIRP power level as a
percentage of the maximum EIRP
power (0 - 100, default = 100).
integer
Minimum value:
0 Maximum
value: 100
100
power-mode
Set radio effective isotropic radiated
power (EIRP) in dBm or by a
percentage of the maximum EIRP
(default = percentage). This power
takes into account both radio
transmit power and antenna gain.
Higher power level settings may be
constrained by local regulatory
requirements and AP capabilities.
option
-percentage
Option
Description
dBm
Set radio EIRP power in dBm.
percentage
Set radio EIRP power by percentage.
power-value
Radio EIRP power in dBm (1 - 33,
default = 27).
integer
Minimum value:
1 Maximum
value: 33
27
powersave-optimize
Enable client power-saving features
such as TIM, AC VO, and OBSS etc.
option
-Option
Description
tim
TIM bit for client in power save mode.
ac-vo
Use AC VO priority to send out packets in the power save queue.
no-obss-scan
Do not put OBSS scan IE into beacon and probe response frames.
no-11b-rate
Do not send frame using 11b data rate.
client-rate-follow
Adapt transmitting PHY rate with receiving PHY rate from a client.
protection-mode
Enable/disable 802.11g protection
modes to support backwards
compatibility with older clients
(rtscts, ctsonly, disable).
option
-disable
Option
Description
rtscts
Enable 802.11g protection RTS/CTS mode.
ctsonly
Enable 802.11g protection CTS only mode.
disable
Disable 802.11g protection mode.
FortiOS 8.0.0 CLI Reference
2901
Fortinet Inc.

<!-- 来源页 2902 -->
Parameter
Description
Type
Size
Default
rts-threshold
Maximum packet size for RTS
transmissions, specifying the
maximum size of a data packet
before RTS/CTS (256 - 2346 bytes,
default = 2346).
integer
Minimum value:
256 Maximum
value: 2346
2346
sam-bssid
BSSID for WiFi network.
mac-address
Not Specified
00:00:00:00:00:00
sam-ca-certificate
CA certificate for WPA2/WPA3-ENTERPRISE.
string
Maximum
length: 79
sam-captive-portal
Enable/disable Captive Portal
Authentication (default = disable).
option
-disable
Option
Description
enable
Enable Captive Portal Authentication.
disable
Disable Captive Portal Authentication.
sam-client-certificate
Client certificate for WPA2/WPA3-ENTERPRISE.
string
Maximum
length: 35
sam-cwp-failure-string
Failure identification on the page
after an incorrect login.
string
Maximum
length: 64
sam-cwp-match-string
Identification string from the captive
portal login form.
string
Maximum
length: 64
sam-cwp-password
Password for captive portal
authentication.
password
Not Specified
sam-cwp-success-string
Success identification on the page
after a successful login.
string
Maximum
length: 64
sam-cwp-test-url
Website the client is trying to
access.
string
Maximum
length: 255
sam-cwp-username
Username for captive portal
authentication.
string
Maximum
length: 35
sam-eap-method
Select WPA2/WPA3-ENTERPRISE
EAP Method (default = PEAP).
option
-peap
Option
Description
both
EAP PEAP and TLS. (Not applicable in FIPS mode)
tls
EAP TLS.
peap
EAP PEAP. (Not applicable in FIPS mode)
FortiOS 8.0.0 CLI Reference
2902
Fortinet Inc.

<!-- 来源页 2903 -->
Parameter
Description
Type
Size
Default
sam-password
Passphrase for WiFi network
connection.
password
Not Specified
sam-private-key
Private key for WPA2/WPA3-ENTERPRISE.
string
Maximum
length: 35
sam-private-key-password
Password for private key file for
WPA2/WPA3-ENTERPRISE.
password
Not Specified
sam-report-intv
SAM report interval (sec), 0 for a
one-time report.
integer
Minimum value:
60 Maximum
value: 864000
0
sam-security-type
Select WiFi network security type
(default = "wpa-personal" for
2.4/5G radio, "wpa3-sae" for 6G
radio).
option
-wpa-personal
Option
Description
open
Open.
wpa-personal
WPA/WPA2 personal.
wpa-enterprise
WPA2/WPA3 enterprise.
wpa3-sae
WPA3 SAE.
owe
OWE.
sam-server-fqdn
SAM test server domain name.
string
Maximum
length: 255
sam-server-ip
SAM test server IP address.
ipv4-address
Not Specified
0.0.0.0
sam-server-type
Select SAM server type (default =
"IP").
option
-ip
Option
Description
ip
IPv4 address.
fqdn
Fully Qualified Domain Name address.
sam-ssid
SSID for WiFi network.
string
Maximum
length: 32
sam-test
Select SAM test type (default =
"PING").
option
-ping
Option
Description
ping
PING test.
FortiOS 8.0.0 CLI Reference
2903
Fortinet Inc.

<!-- 来源页 2904 -->
Parameter
Description
Type
Size
Default
Option
Description
iperf
IPERF test.
sam-username
Username for WiFi network
connection.
string
Maximum
length: 35
short-guard-interval
Use either the short guard interval
(Short GI) of 400 ns or the long
guard interval (Long GI) of 800 ns.
option
-disable
Option
Description
enable
Select the 400 ns short guard interval (Short GI).
disable
Select the 800 ns long guard interval (Long GI).
transmit-optimize
Packet transmission optimization
options including power saving,
aggregation limiting, retry limiting,
etc. All are enabled by default.
option
-power-save aggr-limit retry-limit send-bar
Option
Description
disable
Disable packet transmission optimization.
power-save
Tag client as operating in power save mode if excessive transmit retries
occur.
aggr-limit
Set aggregation limit to a lower value when data rate is low.
retry-limit
Set software retry limit to a lower value when data rate is low.
send-bar
Limit transmission of BAR frames.
vap-all
Configure method for assigning
SSIDs to this FortiAP (default =
automatically assign tunnel SSIDs).
option
-tunnel
Option
Description
tunnel
Automatically select tunnel SSIDs.
bridge
Automatically select local-bridging SSIDs.
manual
Manually select SSIDs.
vap-status *
Enable/disable all configured SSIDs
on this radio (default = enable).
option
-enable
FortiOS 8.0.0 CLI Reference
2904
Fortinet Inc.

<!-- 来源页 2905 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable all configured SSIDs on this radio.
disable
Disable all configured SSIDs on this radio.
vaps <name>
Manually selected list of Virtual
Access Points (VAPs).
Virtual Access Point (VAP) name.
string
Maximum
length: 35
wids-profile
Wireless Intrusion Detection System
(WIDS) profile name to assign to the
radio.
string
Maximum
length: 35
zero-wait-dfs
Enable/disable zero wait DFS on
radio (default = enable).
option
-enable
Option
Description
enable
Enable zero wait DFS
disable
Disable zero wait DFS
* This parameter may not exist in some models.
config radio-3
Parameter
Description
Type
Size
Default
80211d
Enable/disable 802.11d countryie
(default = enable).
option
-enable
Option
Description
enable
Enable 802.11d countryie.
disable
Disable 802.11d countryie.
80211mc
Enable/disable radio 802.11mc
capability (default = disable).
option
-disable
Option
Description
enable
Enable radio 802.11mc capability.
disable
Disable radio 802.11mc capability.
FortiOS 8.0.0 CLI Reference
2905
Fortinet Inc.

<!-- 来源页 2906 -->
Parameter
Description
Type
Size
Default
ai-darrp-support
Enable/disable support for
FortiAIOps to retrieve Distributed
Automatic Radio Resource
Provisioning (DARRP) data through
REST API calls (default = disable).
option
-disable
Option
Description
enable
Enable support for FortiAIOps REST API calls for DARRP data.
disable
Disable support for FortiAIOps REST API calls for DARRP data.
airtime-fairness
Enable/disable airtime fairness
(default = disable).
option
-disable
Option
Description
enable
Enable airtime fairness (ATF) support.
disable
Disable airtime fairness (ATF) support.
amsdu
Enable/disable 802.11n AMSDU
support. AMSDU can improve
performance if supported by your
WiFi clients (default = enable).
option
-enable
Option
Description
enable
Enable AMSDU support.
disable
Disable AMSDU support.
ap-sniffer-addr
MAC address to monitor.
mac-address
Not Specified
00:00:00:00:00:00
ap-sniffer-bufsize
Sniffer buffer size (1 - 32 MB,
default = 16).
integer
Minimum value:
1 Maximum
value: 32
16
ap-sniffer-chan
Channel on which to operate the
sniffer (default = 6).
integer
Minimum value:
0 Maximum
value:
4294967295
37
ap-sniffer-chan-width
Channel bandwidth for sniffer.
option
-20MHz
Option
Description
320MHz
320 MHz channel width.
FortiOS 8.0.0 CLI Reference
2906
Fortinet Inc.

<!-- 来源页 2907 -->
Parameter
Description
Type
Size
Default
Option
Description
240MHz
240 MHz channel width.
160MHz
160 MHz channel width.
80MHz
80 MHz channel width.
40MHz
40 MHz channel width.
20MHz
20 MHz channel width.
ap-sniffer-ctl
Enable/disable sniffer on WiFi
control frame (default = enable).
option
-enable
Option
Description
enable
Enable sniffer on WiFi control frame.
disable
Disable sniffer on WiFi control frame.
ap-sniffer-data
Enable/disable sniffer on WiFi data
frame (default = enable).
option
-enable
Option
Description
enable
Enable sniffer on WiFi data frame
disable
Disable sniffer on WiFi data frame
ap-sniffer-mgmt-beacon
Enable/disable sniffer on WiFi
management Beacon frames
(default = enable).
option
-enable
Option
Description
enable
Enable sniffer on WiFi management beacon frame.
disable
Disable sniffer on WiFi management beacon frame.
ap-sniffer-mgmt-other
Enable/disable sniffer on WiFi
management other frames (default
= enable).
option
-enable
Option
Description
enable
Enable sniffer on WiFi management other frame.
disable
Disable sniffer on WiFi management other frame.
ap-sniffer-mgmt-probe
Enable/disable sniffer on WiFi
management probe frames (default
= enable).
option
-enable
FortiOS 8.0.0 CLI Reference
2907
Fortinet Inc.

<!-- 来源页 2908 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable sniffer on WiFi management probe frame.
disable
Enable sniffer on WiFi management probe frame.
arrp-profile
Distributed Automatic Radio
Resource Provisioning (DARRP)
profile name to assign to the radio.
string
Maximum
length: 35
auto-power-high
The upper bound of automatic
transmit power adjustment in dBm
(the actual range of transmit power
depends on the AP platform type).
integer
Minimum value:
0 Maximum
value:
4294967295
17
auto-power-level
Enable/disable automatic power-level adjustment to prevent co-channel interference (default =
disable).
option
-disable
Option
Description
enable
Enable automatic transmit power adjustment.
disable
Disable automatic transmit power adjustment.
auto-power-low
The lower bound of automatic
transmit power adjustment in dBm
(the actual range of transmit power
depends on the AP platform type).
integer
Minimum value:
0 Maximum
value:
4294967295
10
auto-power-target
Target of automatic transmit power
adjustment in dBm (-95 to -20,
default = -70).
string
Maximum
length: 7
-70
band
WiFi band that Radio 3 operates on.
option
-Option
Description
802.11a
802.11a.
802.11b
802.11b.
802.11g
802.11g.
802.11n-2G
802.11n (WiFi 4) at 2.4GHz.
802.11n-5G
802.11n (WiFi 4) at 5GHz.
802.11ac-2G
802.11ac (WiFi 5) at 2.4GHz.
802.11ac-5G
802.11ac (WiFi 5) at 5GHz.
802.11ax-2G
802.11ax (WiFi 6) at 2.4GHz.
FortiOS 8.0.0 CLI Reference
2908
Fortinet Inc.

<!-- 来源页 2909 -->
Parameter
Description
Type
Size
Default
Option
Description
802.11ax-5G
802.11ax (WiFi 6) at 5GHz.
802.11ax-6G
802.11ax (WiFi 6) at 6GHz.
802.11be-2G
802.11be (WiFi 7) at 2.4GHz.
802.11be-5G
802.11be (WiFi 7) at 5GHz.
802.11be-6G
802.11be (WiFi 7) at 6GHz.
band-5g-type
WiFi 5G band type.
option
-5g-full
Option
Description
5g-full
Full 5G band.
5g-high
High 5G band.
5g-low
Low 5G band.
bandwidth-admission-control
Enable/disable WiFi multimedia
(WMM) bandwidth admission
control to optimize WiFi bandwidth
use. A request to join the wireless
network is only allowed if the access
point has enough bandwidth to
support it.
option
-disable
Option
Description
enable
Enable WMM bandwidth admission control.
disable
Disable WMM bandwidth admission control.
bandwidth-capacity
Maximum bandwidth capacity
allowed (1 - 600000 Kbps, default =
2000).
integer
Minimum value:
1 Maximum
value: 600000
2000
beacon-interval
Beacon interval. The time between
beacon frames in milliseconds.
Actual range of beacon interval
depends on the AP platform type
(default = 100).
integer
Minimum value:
0 Maximum
value: 65535
100
bss-color
BSS color value for this 11ax radio (0
- 63, disable = 0, default = 0).
integer
Minimum value:
0 Maximum
value: 63
0
bss-color-mode
BSS color mode for this 11ax radio
(default = auto).
option
-auto
FortiOS 8.0.0 CLI Reference
2909
Fortinet Inc.

<!-- 来源页 2910 -->
Parameter
Description
Type
Size
Default
Option
Description
auto
Automatically select BSS color value on AP.
static
Set BSS color value on this radio based on 'bss-color' CLI.
call-admission-control
Enable/disable WiFi multimedia
(WMM) call admission control to
optimize WiFi bandwidth use for
VoIP calls. New VoIP calls are only
accepted if there is enough
bandwidth available to support
them.
option
-disable
Option
Description
enable
Enable WMM call admission control.
disable
Disable WMM call admission control.
call-capacity
Maximum number of Voice over
WLAN (VoWLAN) phones supported
by the radio (0 - 60, default = 10).
integer
Minimum value:
0 Maximum
value: 60
10
cca-threshold
*
Configure Clear Channel
Assessment (CCA) threshold in dBm
(-94 to -11, default = 0, 0 for
unconfigured).
string
Maximum
length: 7
0
channel
<chan>
Selected list of wireless radio
channels.
Channel number.
string
Maximum
length: 3
channel-bonding
Channel bandwidth: 320, 240, 160,
80, 40, or 20MHz. Channels may
use both 20 and 40 by enabling
coexistence.
option
-20MHz
Option
Description
320MHz
320 MHz channel width.
240MHz
240 MHz channel width.
160MHz
160 MHz channel width.
80MHz
80 MHz channel width.
40MHz
40 MHz channel width.
20MHz
20 MHz channel width.
FortiOS 8.0.0 CLI Reference
2910
Fortinet Inc.

<!-- 来源页 2911 -->
Parameter
Description
Type
Size
Default
channel-bonding-ext
Channel bandwidth extension: 320
MHz-1 and 320 MHz-2 (default =
320 MHz-2).
option
-320MHz-2
Option
Description
320MHz-1
320 MHz channel with channel center frequency numbered 31, 95, and
159.
320MHz-2
320 MHz channel with channel center frequency numbered 63, 127,
and 191.
channel-utilization
Enable/disable measuring channel
utilization.
option
-enable
Option
Description
enable
Enable measuring channel utilization.
disable
Disable measuring channel utilization.
coexistence
Enable/disable allowing both HT20
and HT40 on the same radio
(default = enable).
option
-enable
Option
Description
enable
Enable support for both HT20 and HT40 on the same radio.
disable
Disable support for both HT20 and HT40 on the same radio.
darrp
Enable/disable Distributed
Automatic Radio Resource
Provisioning (DARRP) to make sure
the radio is always using the most
optimal channel (default = disable).
option
-disable
Option
Description
enable
Enable distributed automatic radio resource provisioning.
disable
Disable distributed automatic radio resource provisioning.
drma
Enable/disable dynamic radio mode
assignment (DRMA) (default =
disable).
option
-disable
Option
Description
disable
Disable dynamic radio mode assignment (DRMA).
enable
Enable dynamic radio mode assignment (DRMA).
FortiOS 8.0.0 CLI Reference
2911
Fortinet Inc.

<!-- 来源页 2912 -->
Parameter
Description
Type
Size
Default
drma-sensitivity
Network Coverage Factor (NCF)
percentage required to consider a
radio as redundant (default = low).
option
-low
Option
Description
low
Consider a radio as redundant when its NCF is 100%.
medium
Consider a radio as redundant when its NCF is 95%.
high
Consider a radio as redundant when its NCF is 90%.
dtim
Delivery Traffic Indication Map
(DTIM) period (1 - 255, default = 1).
Set higher to save battery life of
WiFi client in power-save mode.
integer
Minimum value:
1 Maximum
value: 255
1
frag-threshold
Maximum packet size that can be
sent without fragmentation (800 -2346 bytes, default = 2346).
integer
Minimum value:
800 Maximum
value: 2346
2346
iperf-protocol
Iperf test protocol (default = "UDP").
option
-udp
Option
Description
udp
UDP.
tcp
TCP.
iperf-server-port
Iperf service port number.
integer
Minimum value:
0 Maximum
value: 65535
5001
max-clients
Maximum number of stations (STAs)
or WiFi clients supported by the
radio. Range depends on the
hardware.
integer
Minimum value:
0 Maximum
value:
4294967295
0
max-distance
Maximum expected distance
between the AP and clients (0 -54000 m, default = 0).
integer
Minimum value:
0 Maximum
value: 54000
0
mimo-mode
Configure radio MIMO mode (default
= default).
option
-default
Option
Description
default
Default radio MIMO mode.
1x1
1x1 radio MIMO mode.
2x2
2x2 radio MIMO mode.
FortiOS 8.0.0 CLI Reference
2912
Fortinet Inc.

<!-- 来源页 2913 -->
Parameter
Description
Type
Size
Default
Option
Description
3x3
3x3 radio MIMO mode.
4x4
4x4 radio MIMO mode.
8x8
8x8 radio MIMO mode.
mode
Mode of radio 3. Radio 3 can be
disabled, configured as an access
point, a rogue AP monitor, a sniffer,
or a station.
option
-ap
Option
Description
disabled
Radio 3 is disabled.
ap
Radio 3 operates as an access point that allows WiFi clients to connect
to your network.
monitor
Radio 3 operates as a dedicated monitor. As a monitor, the radio scans
for other WiFi access points and adds them to the Rogue AP monitor
list.
sniffer
Radio 3 operates as a sniffer capturing WiFi frames on air.
sam
Radio 3 operates as a station that can connect to a neighboring AP for
connectivity and health check.
optional-antenna
Optional antenna used on FAP
(default = none).
option
-none
Option
Description
none
None.
custom
Customize optional antenna gain.
FANT-04ABGN-0606-O-N
6 dBi(2.4GHz) and 6 dBi(5GHz).
FANT-04ABGN-1414-P-N
14 dBi(2.4GHz) and 14 dBi(5GHz).
FANT-04ABGN-8065-P-N
8 dBi(2.4GHz) and 6.5 dBi(5GHz).
FortiOS 8.0.0 CLI Reference
2913
Fortinet Inc.

<!-- 来源页 2914 -->
Parameter
Description
Type
Size
Default
Option
Description
FANT-04ABGN-0606-O-R
6 dBi(2.4GHz) and 6 dBi(5GHz).
FANT-04ABGN-0606-P-R
6 dBi(2.4GHz) and 6 dBi(5GHz).
FANT-10ACAX-1213-D-N
12 dBi(2.4GHz) and 13 dBi(5GHz).
FANT-08ABGN-1213-D-R
12 dBi(2.4GHz) and 13 dBi(5GHz).
FANT-04BEAX-0606-P-R
6 dBi(2.4GHz), 6 dBi(5GHz) and 6 dBi(6GHz).
optional-antenna-gain
Optional antenna gain in dBi (0 to
20, default = 0).
string
Maximum
length: 7
0
power-level
Radio EIRP power level as a
percentage of the maximum EIRP
power (0 - 100, default = 100).
integer
Minimum value:
0 Maximum
value: 100
100
power-mode
Set radio effective isotropic radiated
power (EIRP) in dBm or by a
percentage of the maximum EIRP
(default = percentage). This power
takes into account both radio
transmit power and antenna gain.
Higher power level settings may be
constrained by local regulatory
requirements and AP capabilities.
option
-percentage
Option
Description
dBm
Set radio EIRP power in dBm.
percentage
Set radio EIRP power by percentage.
power-value
Radio EIRP power in dBm (1 - 33,
default = 27).
integer
Minimum value:
1 Maximum
value: 33
27
powersave-optimize
Enable client power-saving features
such as TIM, AC VO, and OBSS etc.
option
-FortiOS 8.0.0 CLI Reference
2914
Fortinet Inc.

<!-- 来源页 2915 -->
Parameter
Description
Type
Size
Default
Option
Description
tim
TIM bit for client in power save mode.
ac-vo
Use AC VO priority to send out packets in the power save queue.
no-obss-scan
Do not put OBSS scan IE into beacon and probe response frames.
no-11b-rate
Do not send frame using 11b data rate.
client-rate-follow
Adapt transmitting PHY rate with receiving PHY rate from a client.
protection-mode
Enable/disable 802.11g protection
modes to support backwards
compatibility with older clients
(rtscts, ctsonly, disable).
option
-disable
Option
Description
rtscts
Enable 802.11g protection RTS/CTS mode.
ctsonly
Enable 802.11g protection CTS only mode.
disable
Disable 802.11g protection mode.
rts-threshold
Maximum packet size for RTS
transmissions, specifying the
maximum size of a data packet
before RTS/CTS (256 - 2346 bytes,
default = 2346).
integer
Minimum value:
256 Maximum
value: 2346
2346
sam-bssid
BSSID for WiFi network.
mac-address
Not Specified
00:00:00:00:00:00
sam-ca-certificate
CA certificate for WPA2/WPA3-ENTERPRISE.
string
Maximum
length: 79
sam-captive-portal
Enable/disable Captive Portal
Authentication (default = disable).
option
-disable
Option
Description
enable
Enable Captive Portal Authentication.
disable
Disable Captive Portal Authentication.
sam-client-certificate
Client certificate for WPA2/WPA3-ENTERPRISE.
string
Maximum
length: 35
sam-cwp-failure-string
Failure identification on the page
after an incorrect login.
string
Maximum
length: 64
FortiOS 8.0.0 CLI Reference
2915
Fortinet Inc.

<!-- 来源页 2916 -->
Parameter
Description
Type
Size
Default
sam-cwp-match-string
Identification string from the captive
portal login form.
string
Maximum
length: 64
sam-cwp-password
Password for captive portal
authentication.
password
Not Specified
sam-cwp-success-string
Success identification on the page
after a successful login.
string
Maximum
length: 64
sam-cwp-test-url
Website the client is trying to
access.
string
Maximum
length: 255
sam-cwp-username
Username for captive portal
authentication.
string
Maximum
length: 35
sam-eap-method
Select WPA2/WPA3-ENTERPRISE
EAP Method (default = PEAP).
option
-peap
Option
Description
both
EAP PEAP and TLS. (Not applicable in FIPS mode)
tls
EAP TLS.
peap
EAP PEAP. (Not applicable in FIPS mode)
sam-password
Passphrase for WiFi network
connection.
password
Not Specified
sam-private-key
Private key for WPA2/WPA3-ENTERPRISE.
string
Maximum
length: 35
sam-private-key-password
Password for private key file for
WPA2/WPA3-ENTERPRISE.
password
Not Specified
sam-report-intv
SAM report interval (sec), 0 for a
one-time report.
integer
Minimum value:
60 Maximum
value: 864000
0
sam-security-type
Select WiFi network security type
(default = "wpa-personal" for
2.4/5G radio, "wpa3-sae" for 6G
radio).
option
-wpa-personal
Option
Description
open
Open.
wpa-personal
WPA/WPA2 personal.
wpa-enterprise
WPA2/WPA3 enterprise.
FortiOS 8.0.0 CLI Reference
2916
Fortinet Inc.

<!-- 来源页 2917 -->
Parameter
Description
Type
Size
Default
Option
Description
wpa3-sae
WPA3 SAE.
owe
OWE.
sam-server-fqdn
SAM test server domain name.
string
Maximum
length: 255
sam-server-ip
SAM test server IP address.
ipv4-address
Not Specified
0.0.0.0
sam-server-type
Select SAM server type (default =
"IP").
option
-ip
Option
Description
ip
IPv4 address.
fqdn
Fully Qualified Domain Name address.
sam-ssid
SSID for WiFi network.
string
Maximum
length: 32
sam-test
Select SAM test type (default =
"PING").
option
-ping
Option
Description
ping
PING test.
iperf
IPERF test.
sam-username
Username for WiFi network
connection.
string
Maximum
length: 35
short-guard-interval
Use either the short guard interval
(Short GI) of 400 ns or the long
guard interval (Long GI) of 800 ns.
option
-disable
Option
Description
enable
Select the 400 ns short guard interval (Short GI).
disable
Select the 800 ns long guard interval (Long GI).
transmit-optimize
Packet transmission optimization
options including power saving,
aggregation limiting, retry limiting,
etc. All are enabled by default.
option
-power-save aggr-limit retry-limit send-bar
FortiOS 8.0.0 CLI Reference
2917
Fortinet Inc.

<!-- 来源页 2918 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable packet transmission optimization.
power-save
Tag client as operating in power save mode if excessive transmit retries
occur.
aggr-limit
Set aggregation limit to a lower value when data rate is low.
retry-limit
Set software retry limit to a lower value when data rate is low.
send-bar
Limit transmission of BAR frames.
vap-all
Configure method for assigning
SSIDs to this FortiAP (default =
automatically assign tunnel SSIDs).
option
-tunnel
Option
Description
tunnel
Automatically select tunnel SSIDs.
bridge
Automatically select local-bridging SSIDs.
manual
Manually select SSIDs.
vap-status *
Enable/disable all configured SSIDs
on this radio (default = enable).
option
-enable
Option
Description
enable
Enable all configured SSIDs on this radio.
disable
Disable all configured SSIDs on this radio.
vaps <name>
Manually selected list of Virtual
Access Points (VAPs).
Virtual Access Point (VAP) name.
string
Maximum
length: 35
wids-profile
Wireless Intrusion Detection System
(WIDS) profile name to assign to the
radio.
string
Maximum
length: 35
zero-wait-dfs
Enable/disable zero wait DFS on
radio (default = enable).
option
-enable
Option
Description
enable
Enable zero wait DFS
disable
Disable zero wait DFS
* This parameter may not exist in some models.
FortiOS 8.0.0 CLI Reference
2918
Fortinet Inc.

<!-- 来源页 2919 -->
config radio-4
Parameter
Description
Type
Size
Default
80211d
Enable/disable 802.11d countryie
(default = enable).
option
-enable
Option
Description
enable
Enable 802.11d countryie.
disable
Disable 802.11d countryie.
80211mc
Enable/disable radio 802.11mc
capability (default = disable).
option
-disable
Option
Description
enable
Enable radio 802.11mc capability.
disable
Disable radio 802.11mc capability.
ai-darrp-support
Enable/disable support for
FortiAIOps to retrieve Distributed
Automatic Radio Resource
Provisioning (DARRP) data through
REST API calls (default = disable).
option
-disable
Option
Description
enable
Enable support for FortiAIOps REST API calls for DARRP data.
disable
Disable support for FortiAIOps REST API calls for DARRP data.
airtime-fairness
Enable/disable airtime fairness
(default = disable).
option
-disable
Option
Description
enable
Enable airtime fairness (ATF) support.
disable
Disable airtime fairness (ATF) support.
amsdu
Enable/disable 802.11n AMSDU
support. AMSDU can improve
performance if supported by your
WiFi clients (default = enable).
option
-enable
Option
Description
enable
Enable AMSDU support.
disable
Disable AMSDU support.
FortiOS 8.0.0 CLI Reference
2919
Fortinet Inc.

<!-- 来源页 2920 -->
Parameter
Description
Type
Size
Default
ap-sniffer-addr
MAC address to monitor.
mac-address
Not Specified
00:00:00:00:00:00
ap-sniffer-bufsize
Sniffer buffer size (1 - 32 MB,
default = 16).
integer
Minimum value:
1 Maximum
value: 32
16
ap-sniffer-chan
Channel on which to operate the
sniffer (default = 6).
integer
Minimum value:
0 Maximum
value:
4294967295
6
ap-sniffer-chan-width
Channel bandwidth for sniffer.
option
-20MHz
Option
Description
320MHz
320 MHz channel width.
240MHz
240 MHz channel width.
160MHz
160 MHz channel width.
80MHz
80 MHz channel width.
40MHz
40 MHz channel width.
20MHz
20 MHz channel width.
ap-sniffer-ctl
Enable/disable sniffer on WiFi
control frame (default = enable).
option
-enable
Option
Description
enable
Enable sniffer on WiFi control frame.
disable
Disable sniffer on WiFi control frame.
ap-sniffer-data
Enable/disable sniffer on WiFi data
frame (default = enable).
option
-enable
Option
Description
enable
Enable sniffer on WiFi data frame
disable
Disable sniffer on WiFi data frame
ap-sniffer-mgmt-beacon
Enable/disable sniffer on WiFi
management Beacon frames
(default = enable).
option
-enable
FortiOS 8.0.0 CLI Reference
2920
Fortinet Inc.

<!-- 来源页 2921 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable sniffer on WiFi management beacon frame.
disable
Disable sniffer on WiFi management beacon frame.
ap-sniffer-mgmt-other
Enable/disable sniffer on WiFi
management other frames (default
= enable).
option
-enable
Option
Description
enable
Enable sniffer on WiFi management other frame.
disable
Disable sniffer on WiFi management other frame.
ap-sniffer-mgmt-probe
Enable/disable sniffer on WiFi
management probe frames (default
= enable).
option
-enable
Option
Description
enable
Enable sniffer on WiFi management probe frame.
disable
Enable sniffer on WiFi management probe frame.
arrp-profile
Distributed Automatic Radio
Resource Provisioning (DARRP)
profile name to assign to the radio.
string
Maximum
length: 35
auto-power-high
The upper bound of automatic
transmit power adjustment in dBm
(the actual range of transmit power
depends on the AP platform type).
integer
Minimum value:
0 Maximum
value:
4294967295
17
auto-power-level
Enable/disable automatic power-level adjustment to prevent co-channel interference (default =
disable).
option
-disable
Option
Description
enable
Enable automatic transmit power adjustment.
disable
Disable automatic transmit power adjustment.
auto-power-low
The lower bound of automatic
transmit power adjustment in dBm
(the actual range of transmit power
depends on the AP platform type).
integer
Minimum value:
0 Maximum
value:
4294967295
10
FortiOS 8.0.0 CLI Reference
2921
Fortinet Inc.

<!-- 来源页 2922 -->
Parameter
Description
Type
Size
Default
auto-power-target
Target of automatic transmit power
adjustment in dBm (-95 to -20,
default = -70).
string
Maximum
length: 7
-70
band
WiFi band that Radio 4 operates on.
option
-Option
Description
802.11a
802.11a.
802.11b
802.11b.
802.11g
802.11g.
802.11n-2G
802.11n (WiFi 4) at 2.4GHz.
802.11n-5G
802.11n (WiFi 4) at 5GHz.
802.11ac-2G
802.11ac (WiFi 5) at 2.4GHz.
802.11ac-5G
802.11ac (WiFi 5) at 5GHz.
802.11ax-2G
802.11ax (WiFi 6) at 2.4GHz.
802.11ax-5G
802.11ax (WiFi 6) at 5GHz.
802.11ax-6G
802.11ax (WiFi 6) at 6GHz.
802.11be-2G
802.11be (WiFi 7) at 2.4GHz.
802.11be-5G
802.11be (WiFi 7) at 5GHz.
802.11be-6G
802.11be (WiFi 7) at 6GHz.
band-5g-type
WiFi 5G band type.
option
-5g-full
Option
Description
5g-full
Full 5G band.
5g-high
High 5G band.
5g-low
Low 5G band.
bandwidth-admission-control
Enable/disable WiFi multimedia
(WMM) bandwidth admission
control to optimize WiFi bandwidth
use. A request to join the wireless
network is only allowed if the access
point has enough bandwidth to
support it.
option
-disable
FortiOS 8.0.0 CLI Reference
2922
Fortinet Inc.

<!-- 来源页 2923 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable WMM bandwidth admission control.
disable
Disable WMM bandwidth admission control.
bandwidth-capacity
Maximum bandwidth capacity
allowed (1 - 600000 Kbps, default =
2000).
integer
Minimum value:
1 Maximum
value: 600000
2000
beacon-interval
Beacon interval. The time between
beacon frames in milliseconds.
Actual range of beacon interval
depends on the AP platform type
(default = 100).
integer
Minimum value:
0 Maximum
value: 65535
100
bss-color
BSS color value for this 11ax radio (0
- 63, disable = 0, default = 0).
integer
Minimum value:
0 Maximum
value: 63
0
bss-color-mode
BSS color mode for this 11ax radio
(default = auto).
option
-auto
Option
Description
auto
Automatically select BSS color value on AP.
static
Set BSS color value on this radio based on 'bss-color' CLI.
call-admission-control
Enable/disable WiFi multimedia
(WMM) call admission control to
optimize WiFi bandwidth use for
VoIP calls. New VoIP calls are only
accepted if there is enough
bandwidth available to support
them.
option
-disable
Option
Description
enable
Enable WMM call admission control.
disable
Disable WMM call admission control.
call-capacity
Maximum number of Voice over
WLAN (VoWLAN) phones supported
by the radio (0 - 60, default = 10).
integer
Minimum value:
0 Maximum
value: 60
10
cca-threshold
*
Configure Clear Channel
Assessment (CCA) threshold in dBm
(-94 to -11, default = 0, 0 for
unconfigured).
string
Maximum
length: 7
0
FortiOS 8.0.0 CLI Reference
2923
Fortinet Inc.

<!-- 来源页 2924 -->
Parameter
Description
Type
Size
Default
channel
<chan>
Selected list of wireless radio
channels.
Channel number.
string
Maximum
length: 3
channel-bonding
Channel bandwidth: 320, 240, 160,
80, 40, or 20MHz. Channels may
use both 20 and 40 by enabling
coexistence.
option
-20MHz
Option
Description
320MHz
320 MHz channel width.
240MHz
240 MHz channel width.
160MHz
160 MHz channel width.
80MHz
80 MHz channel width.
40MHz
40 MHz channel width.
20MHz
20 MHz channel width.
channel-bonding-ext
Channel bandwidth extension: 320
MHz-1 and 320 MHz-2 (default =
320 MHz-2).
option
-320MHz-2
Option
Description
320MHz-1
320 MHz channel with channel center frequency numbered 31, 95, and
159.
320MHz-2
320 MHz channel with channel center frequency numbered 63, 127,
and 191.
channel-utilization
Enable/disable measuring channel
utilization.
option
-enable
Option
Description
enable
Enable measuring channel utilization.
disable
Disable measuring channel utilization.
coexistence
Enable/disable allowing both HT20
and HT40 on the same radio
(default = enable).
option
-enable
Option
Description
enable
Enable support for both HT20 and HT40 on the same radio.
disable
Disable support for both HT20 and HT40 on the same radio.
FortiOS 8.0.0 CLI Reference
2924
Fortinet Inc.

<!-- 来源页 2925 -->
Parameter
Description
Type
Size
Default
darrp
Enable/disable Distributed
Automatic Radio Resource
Provisioning (DARRP) to make sure
the radio is always using the most
optimal channel (default = disable).
option
-disable
Option
Description
enable
Enable distributed automatic radio resource provisioning.
disable
Disable distributed automatic radio resource provisioning.
drma
Enable/disable dynamic radio mode
assignment (DRMA) (default =
disable).
option
-disable
Option
Description
disable
Disable dynamic radio mode assignment (DRMA).
enable
Enable dynamic radio mode assignment (DRMA).
drma-sensitivity
Network Coverage Factor (NCF)
percentage required to consider a
radio as redundant (default = low).
option
-low
Option
Description
low
Consider a radio as redundant when its NCF is 100%.
medium
Consider a radio as redundant when its NCF is 95%.
high
Consider a radio as redundant when its NCF is 90%.
dtim
Delivery Traffic Indication Map
(DTIM) period (1 - 255, default = 1).
Set higher to save battery life of
WiFi client in power-save mode.
integer
Minimum value:
1 Maximum
value: 255
1
frag-threshold
Maximum packet size that can be
sent without fragmentation (800 -2346 bytes, default = 2346).
integer
Minimum value:
800 Maximum
value: 2346
2346
iperf-protocol
Iperf test protocol (default = "UDP").
option
-udp
Option
Description
udp
UDP.
tcp
TCP.
FortiOS 8.0.0 CLI Reference
2925
Fortinet Inc.

<!-- 来源页 2926 -->
Parameter
Description
Type
Size
Default
iperf-server-port
Iperf service port number.
integer
Minimum value:
0 Maximum
value: 65535
5001
max-clients
Maximum number of stations (STAs)
or WiFi clients supported by the
radio. Range depends on the
hardware.
integer
Minimum value:
0 Maximum
value:
4294967295
0
max-distance
Maximum expected distance
between the AP and clients (0 -54000 m, default = 0).
integer
Minimum value:
0 Maximum
value: 54000
0
mimo-mode
Configure radio MIMO mode (default
= default).
option
-default
Option
Description
default
Default radio MIMO mode.
1x1
1x1 radio MIMO mode.
2x2
2x2 radio MIMO mode.
3x3
3x3 radio MIMO mode.
4x4
4x4 radio MIMO mode.
8x8
8x8 radio MIMO mode.
mode
Mode of radio 4. Radio 4 can be
disabled, configured as an access
point, a rogue AP monitor, a sniffer,
or a station.
option
-ap
Option
Description
disabled
Radio 4 is disabled.
ap
Radio 4 operates as an access point that allows WiFi clients to connect
to your network.
monitor
Radio 4 operates as a dedicated monitor. As a monitor, the radio scans
for other WiFi access points and adds them to the Rogue AP monitor
list.
sniffer
Radio 4 operates as a sniffer capturing WiFi frames on air.
sam
Radio 4 operates as a station that can connect to a neighboring AP for
connectivity and health check.
optional-antenna
Optional antenna used on FAP
(default = none).
option
-none
FortiOS 8.0.0 CLI Reference
2926
Fortinet Inc.

<!-- 来源页 2927 -->
Parameter
Description
Type
Size
Default
Option
Description
none
None.
custom
Customize optional antenna gain.
FANT-04ABGN-0606-O-N
6 dBi(2.4GHz) and 6 dBi(5GHz).
FANT-04ABGN-1414-P-N
14 dBi(2.4GHz) and 14 dBi(5GHz).
FANT-04ABGN-8065-P-N
8 dBi(2.4GHz) and 6.5 dBi(5GHz).
FANT-04ABGN-0606-O-R
6 dBi(2.4GHz) and 6 dBi(5GHz).
FANT-04ABGN-0606-P-R
6 dBi(2.4GHz) and 6 dBi(5GHz).
FANT-10ACAX-1213-D-N
12 dBi(2.4GHz) and 13 dBi(5GHz).
FANT-08ABGN-1213-D-R
12 dBi(2.4GHz) and 13 dBi(5GHz).
FANT-04BEAX-0606-P-R
6 dBi(2.4GHz), 6 dBi(5GHz) and 6 dBi(6GHz).
optional-antenna-gain
Optional antenna gain in dBi (0 to
20, default = 0).
string
Maximum
length: 7
0
power-level
Radio EIRP power level as a
percentage of the maximum EIRP
power (0 - 100, default = 100).
integer
Minimum value:
0 Maximum
value: 100
100
power-mode
Set radio effective isotropic radiated
power (EIRP) in dBm or by a
percentage of the maximum EIRP
(default = percentage). This power
takes into account both radio
transmit power and antenna gain.
Higher power level settings may be
constrained by local regulatory
requirements and AP capabilities.
option
-percentage
FortiOS 8.0.0 CLI Reference
2927
Fortinet Inc.

<!-- 来源页 2928 -->
Parameter
Description
Type
Size
Default
Option
Description
dBm
Set radio EIRP power in dBm.
percentage
Set radio EIRP power by percentage.
power-value
Radio EIRP power in dBm (1 - 33,
default = 27).
integer
Minimum value:
1 Maximum
value: 33
27
powersave-optimize
Enable client power-saving features
such as TIM, AC VO, and OBSS etc.
option
-Option
Description
tim
TIM bit for client in power save mode.
ac-vo
Use AC VO priority to send out packets in the power save queue.
no-obss-scan
Do not put OBSS scan IE into beacon and probe response frames.
no-11b-rate
Do not send frame using 11b data rate.
client-rate-follow
Adapt transmitting PHY rate with receiving PHY rate from a client.
protection-mode
Enable/disable 802.11g protection
modes to support backwards
compatibility with older clients
(rtscts, ctsonly, disable).
option
-disable
Option
Description
rtscts
Enable 802.11g protection RTS/CTS mode.
ctsonly
Enable 802.11g protection CTS only mode.
disable
Disable 802.11g protection mode.
rts-threshold
Maximum packet size for RTS
transmissions, specifying the
maximum size of a data packet
before RTS/CTS (256 - 2346 bytes,
default = 2346).
integer
Minimum value:
256 Maximum
value: 2346
2346
sam-bssid
BSSID for WiFi network.
mac-address
Not Specified
00:00:00:00:00:00
sam-ca-certificate
CA certificate for WPA2/WPA3-ENTERPRISE.
string
Maximum
length: 79
sam-captive-portal
Enable/disable Captive Portal
Authentication (default = disable).
option
-disable
FortiOS 8.0.0 CLI Reference
2928
Fortinet Inc.

<!-- 来源页 2929 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable Captive Portal Authentication.
disable
Disable Captive Portal Authentication.
sam-client-certificate
Client certificate for WPA2/WPA3-ENTERPRISE.
string
Maximum
length: 35
sam-cwp-failure-string
Failure identification on the page
after an incorrect login.
string
Maximum
length: 64
sam-cwp-match-string
Identification string from the captive
portal login form.
string
Maximum
length: 64
sam-cwp-password
Password for captive portal
authentication.
password
Not Specified
sam-cwp-success-string
Success identification on the page
after a successful login.
string
Maximum
length: 64
sam-cwp-test-url
Website the client is trying to
access.
string
Maximum
length: 255
sam-cwp-username
Username for captive portal
authentication.
string
Maximum
length: 35
sam-eap-method
Select WPA2/WPA3-ENTERPRISE
EAP Method (default = PEAP).
option
-peap
Option
Description
both
EAP PEAP and TLS. (Not applicable in FIPS mode)
tls
EAP TLS.
peap
EAP PEAP. (Not applicable in FIPS mode)
sam-password
Passphrase for WiFi network
connection.
password
Not Specified
sam-private-key
Private key for WPA2/WPA3-ENTERPRISE.
string
Maximum
length: 35
sam-private-key-password
Password for private key file for
WPA2/WPA3-ENTERPRISE.
password
Not Specified
sam-report-intv
SAM report interval (sec), 0 for a
one-time report.
integer
Minimum value:
60 Maximum
value: 864000
0
FortiOS 8.0.0 CLI Reference
2929
Fortinet Inc.

<!-- 来源页 2930 -->
Parameter
Description
Type
Size
Default
sam-security-type
Select WiFi network security type
(default = "wpa-personal" for
2.4/5G radio, "wpa3-sae" for 6G
radio).
option
-wpa-personal
Option
Description
open
Open.
wpa-personal
WPA/WPA2 personal.
wpa-enterprise
WPA2/WPA3 enterprise.
wpa3-sae
WPA3 SAE.
owe
OWE.
sam-server-fqdn
SAM test server domain name.
string
Maximum
length: 255
sam-server-ip
SAM test server IP address.
ipv4-address
Not Specified
0.0.0.0
sam-server-type
Select SAM server type (default =
"IP").
option
-ip
Option
Description
ip
IPv4 address.
fqdn
Fully Qualified Domain Name address.
sam-ssid
SSID for WiFi network.
string
Maximum
length: 32
sam-test
Select SAM test type (default =
"PING").
option
-ping
Option
Description
ping
PING test.
iperf
IPERF test.
sam-username
Username for WiFi network
connection.
string
Maximum
length: 35
short-guard-interval
Use either the short guard interval
(Short GI) of 400 ns or the long
guard interval (Long GI) of 800 ns.
option
-disable
FortiOS 8.0.0 CLI Reference
2930
Fortinet Inc.

<!-- 来源页 2931 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Select the 400 ns short guard interval (Short GI).
disable
Select the 800 ns long guard interval (Long GI).
transmit-optimize
Packet transmission optimization
options including power saving,
aggregation limiting, retry limiting,
etc. All are enabled by default.
option
-power-save aggr-limit retry-limit send-bar
Option
Description
disable
Disable packet transmission optimization.
power-save
Tag client as operating in power save mode if excessive transmit retries
occur.
aggr-limit
Set aggregation limit to a lower value when data rate is low.
retry-limit
Set software retry limit to a lower value when data rate is low.
send-bar
Limit transmission of BAR frames.
vap-all
Configure method for assigning
SSIDs to this FortiAP (default =
automatically assign tunnel SSIDs).
option
-tunnel
Option
Description
tunnel
Automatically select tunnel SSIDs.
bridge
Automatically select local-bridging SSIDs.
manual
Manually select SSIDs.
vap-status *
Enable/disable all configured SSIDs
on this radio (default = enable).
option
-enable
Option
Description
enable
Enable all configured SSIDs on this radio.
disable
Disable all configured SSIDs on this radio.
vaps <name>
Manually selected list of Virtual
Access Points (VAPs).
Virtual Access Point (VAP) name.
string
Maximum
length: 35
wids-profile
Wireless Intrusion Detection System
(WIDS) profile name to assign to the
radio.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
2931
Fortinet Inc.

<!-- 来源页 2932 -->
Parameter
Description
Type
Size
Default
zero-wait-dfs
Enable/disable zero wait DFS on
radio (default = enable).
option
-enable
Option
Description
enable
Enable zero wait DFS
disable
Disable zero wait DFS
* This parameter may not exist in some models.
config split-tunneling-acl
Parameter
Description
Type
Size
Default
dest-ip
Destination IP and mask for the split-tunneling
subnet.
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
FortiOS 8.0.0 CLI Reference
2932
Fortinet Inc.
