# 应用控制

> 来源: FortiOS-8.0.0-CLI_Reference.pdf
> 覆盖命令/章节: application
> 本文件由 extract_pdf.py 从官方 PDF 自动提取，请勿手动编辑；
> 如需修正请修改 map.json 后重跑脚本。

---


<!-- 来源页 187 -->
application
This section includes syntax for the following commands:
l config application classification-settings on page 187
l config application custom on page 188
l config application group on page 189
l config application list on page 191
l config application name on page 200
l config application rule-settings on page 202
l config application unsanctioned-apps on page 203
config application classification-settings
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
Configure app classification setting.
FortiOS 8.0.0 CLI Reference
187
Fortinet Inc.

<!-- 来源页 188 -->
config application classification-settings
Description: Configure app classification setting.
set default-app-classification [unclassified|unsanctioned|...]
end
config application classification-settings
Parameter
Description
Type
Size
Default
default-app-classification
Default application classification.
option
-unclassified
Option
Description
unclassified
Set unclassified.
unsanctioned
Set unsanctioned.
sanctioned
Set sanctioned.
config application custom
Configure custom application signatures.
config application custom
Description: Configure custom application signatures.
edit <tag>
set behavior {user}
set category {integer}
set comment {string}
set id {integer}
set protocol {user}
set signature {var-string}
set technology {user}
set vendor {user}
next
end
config application custom
Parameter
Description
Type
Size
Default
behavior
Custom application signature behavior.
user
Not Specified
FortiOS 8.0.0 CLI Reference
188
Fortinet Inc.

<!-- 来源页 189 -->
Parameter
Description
Type
Size
Default
category
Custom application category ID (use ? to view
available options).
integer
Minimum value:
0 Maximum
value:
4294967295
0
comment
Comment.
string
Maximum
length: 63
id
Custom application category ID (use ? to view
available options). Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
protocol
Custom application signature protocol.
user
Not Specified
signature
The text that makes up the actual custom
application signature.
var-string
Maximum
length: 4095
tag
Signature tag.
string
Maximum
length: 63
technology
Custom application signature technology.
user
Not Specified
vendor
Custom application signature vendor.
user
Not Specified
config application group
Configure firewall application groups.
config application group
Description: Configure firewall application groups.
edit <name>
set application <id1>, <id2>, ...
set behavior {user}
set category <id1>, <id2>, ...
set comment {var-string}
set popularity {option1}, {option2}, ...
set protocols {user}
set risk <level1>, <level2>, ...
set technology {user}
set type [application|filter]
set vendor {user}
next
end
FortiOS 8.0.0 CLI Reference
189
Fortinet Inc.

<!-- 来源页 190 -->
config application group
Parameter
Description
Type
Size
Default
application
<id>
Application ID list.
Application IDs.
integer
Minimum value:
0 Maximum
value:
4294967295
behavior
Application behavior filter.
user
Not Specified
all
category
<id>
Application category ID list.
Category IDs.
integer
Minimum value:
0 Maximum
value:
4294967295
comment
Comments.
var-string
Maximum
length: 255
name
Application group name.
string
Maximum
length: 63
popularity
Application popularity filter (1 - 5, from least to
most popular).
option
-1 2 3 4 5
Option
Description
1
Popularity level 1.
2
Popularity level 2.
3
Popularity level 3.
4
Popularity level 4.
5
Popularity level 5.
protocols
Application protocol filter.
user
Not Specified
all
risk <level>
Risk, or impact, of allowing traffic from this
application to occur (1 - 5; Low, Elevated,
Medium, High, and Critical).
Risk, or impact, of allowing traffic from this
application to occur (1 - 5; Low, Elevated,
Medium, High, and Critical).
integer
Minimum value:
0 Maximum
value:
4294967295
technology
Application technology filter.
user
Not Specified
all
type
Application group type.
option
-application
Option
Description
application
Application ID.
filter
Application filter.
vendor
Application vendor filter.
user
Not Specified
all
FortiOS 8.0.0 CLI Reference
190
Fortinet Inc.

<!-- 来源页 191 -->
config application list
Configure application control lists.
config application list
Description: Configure application control lists.
edit <name>
set app-replacemsg [disable|enable]
set comment {var-string}
set control-default-network-services [disable|enable]
set deep-app-inspection [disable|enable]
config default-network-services
Description: Default network service entries.
edit <id>
set port {integer}
set services {option1}, {option2}, ...
set violation-action [pass|monitor|...]
next
end
set enforce-default-app-port [disable|enable]
config entries
Description: Application list entries.
edit <id>
set action [pass|block|...]
set application <id1>, <id2>, ...
set behavior {user}
set category <id1>, <id2>, ...
set classification [none|sanctioned|...]
set exclusion <id1>, <id2>, ...
set log [disable|enable]
set log-packet [disable|enable]
config parameters
Description: Application parameters.
edit <id>
config members
Description: Parameter tuple members.
edit <id>
set name {string}
set value {string}
next
end
next
end
set per-ip-shaper {string}
set popularity {option1}, {option2}, ...
set protocols {user}
set quarantine [none|attacker]
set quarantine-expiry {user}
set quarantine-log [disable|enable]
set rate-count {integer}
set rate-duration {integer}
FortiOS 8.0.0 CLI Reference
191
Fortinet Inc.

<!-- 来源页 192 -->
set rate-mode [periodical|continuous]
set rate-track [none|src-ip|...]
set risk <level1>, <level2>, ...
set session-ttl {integer}
set shaper {string}
set shaper-reverse {string}
set technology {user}
set vendor {user}
next
end
set extended-log [enable|disable]
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set force-inclusion-ssl-di-sigs [disable|enable]
set options {option1}, {option2}, ...
set other-application-action [pass|block]
set other-application-log [disable|enable]
set p2p-block-list {option1}, {option2}, ...
set replacemsg-group {string}
set unknown-application-action [pass|block]
set unknown-application-log [disable|enable]
set uuid {uuid}
next
end
config application list
Parameter
Description
Type
Size
Default
app-replacemsg
Enable/disable replacement messages for
blocked applications.
option
-enable
Option
Description
disable
Disable replacement messages for blocked applications.
enable
Enable replacement messages for blocked applications.
comment
Comments.
var-string
Maximum
length: 255
control-default-network-services
Enable/disable enforcement of protocols
over selected ports.
option
-disable
Option
Description
disable
Disable protocol enforcement over selected ports.
enable
Enable protocol enforcement over selected ports.
FortiOS 8.0.0 CLI Reference
192
Fortinet Inc.

<!-- 来源页 193 -->
Parameter
Description
Type
Size
Default
deep-app-inspection
Enable/disable deep application inspection.
option
-enable
Option
Description
disable
Disable deep application inspection.
enable
Enable deep application inspection.
enforce-default-app-port
Enable/disable default application port
enforcement for allowed applications.
option
-disable
Option
Description
disable
Disable default application port enforcement.
enable
Enable default application port enforcement.
extended-log
Enable/disable extended logging.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
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
FortiOS 8.0.0 CLI Reference
193
Fortinet Inc.

<!-- 来源页 194 -->
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
force-inclusion-ssl-di-sigs
Enable/disable forced inclusion of SSL
deep inspection signatures.
option
-disable
Option
Description
disable
Disable forced inclusion of signatures which normally require SSL deep
inspection.
enable
Enable forced inclusion of signatures which normally require SSL deep
inspection.
name
List name.
string
Maximum
length: 47
options
Basic application protocol signatures
allowed by default.
option
-allow-dns
Option
Description
allow-dns
Allow DNS.
allow-icmp
Allow ICMP.
allow-http
Allow generic HTTP web browsing.
allow-ssl
Allow generic SSL communication.
other-application-action
Action for other applications.
option
-pass
Option
Description
pass
Allow sessions matching an application in this application list.
block
Block sessions matching an application in this application list.
other-application-log
Enable/disable logging for other
applications.
option
-disable
Option
Description
disable
Disable logging for other applications.
enable
Enable logging for other applications.
FortiOS 8.0.0 CLI Reference
194
Fortinet Inc.

<!-- 来源页 195 -->
Parameter
Description
Type
Size
Default
p2p-block-list
P2P applications to be block listed.
option
-Option
Description
edonkey
Edonkey.
bittorrent
Bit torrent.
skype
Skype.
replacemsg-group
Replacement message group.
string
Maximum
length: 35
unknown-application-action
Pass or block traffic from unknown
applications.
option
-pass
Option
Description
pass
Pass or allow unknown applications.
block
Drop or block unknown applications.
unknown-application-log
Enable/disable logging for unknown
applications.
option
-disable
Option
Description
disable
Disable logging for unknown applications.
enable
Enable logging for unknown applications.
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be manually
reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
config default-network-services
Parameter
Description
Type
Size
Default
id
Entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
port
Port number.
integer
Minimum value:
0 Maximum
value: 65535
0
services
Network protocols.
option
-FortiOS 8.0.0 CLI Reference
195
Fortinet Inc.

<!-- 来源页 196 -->
Parameter
Description
Type
Size
Default
Option
Description
http
HTTP.
ssh
SSH.
telnet
TELNET.
ftp
FTP.
dns
DNS.
smtp
SMTP.
pop3
POP3.
imap
IMAP.
snmp
SNMP.
nntp
NNTP.
https
HTTPS.
violation-action
Action for protocols not in the allowlist for
selected port.
option
-block
Option
Description
pass
Allow protocols not in the allowlist for selected port.
monitor
Monitor protocols not in the allowlist for selected port.
block
Block protocols not in the allowlist for selected port.
config entries
Parameter
Description
Type
Size
Default
action
Pass or block traffic, or reset connection for
traffic from this application.
option
-block
Option
Description
pass
Pass or allow matching traffic.
block
Block or drop matching traffic.
reset
Reset sessions for matching traffic.
application
<id>
ID of allowed applications.
Application IDs.
integer
Minimum value:
0 Maximum
value:
4294967295
FortiOS 8.0.0 CLI Reference
196
Fortinet Inc.

<!-- 来源页 197 -->
Parameter
Description
Type
Size
Default
behavior
Application behavior filter.
user
Not Specified
all
category <id>
Category ID list.
Application category ID.
integer
Minimum value:
0 Maximum
value:
4294967295
classification *
Application classification filter.
option
-none
Option
Description
none
No classification filter.
sanctioned
Pass or allow sanctioned applications.
unsanctioned
Pass or allow unsanctioned applications.
unclassified
Pass or allow unclassified applications.
exclusion <id>
ID of excluded applications.
Excluded application IDs.
integer
Minimum value:
0 Maximum
value:
4294967295
id
Entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
log
Enable/disable logging for this application
list.
option
-enable
Option
Description
disable
Disable logging.
enable
Enable logging.
log-packet
Enable/disable packet logging.
option
-disable
Option
Description
disable
Disable packet logging.
enable
Enable packet logging.
per-ip-shaper
Per-IP traffic shaper.
string
Maximum
length: 35
popularity
Application popularity filter (1 - 5, from least
to most popular).
option
-1 2 3 4 5
FortiOS 8.0.0 CLI Reference
197
Fortinet Inc.

<!-- 来源页 198 -->
Parameter
Description
Type
Size
Default
Option
Description
1
Popularity level 1.
2
Popularity level 2.
3
Popularity level 3.
4
Popularity level 4.
5
Popularity level 5.
protocols
Application protocol filter.
user
Not Specified
all
quarantine
Quarantine method.
option
-none
Option
Description
none
Quarantine is disabled.
attacker
Block all traffic sent from attacker's IP address. The attacker's IP
address is also added to the banned user list. The target's address is
not affected.
quarantine-expiry
Duration of quarantine. (Format
###d##h##m, minimum 1m, maximum
364d23h59m, default = 5m). Requires
quarantine set to attacker.
user
Not Specified
5m
quarantine-log
Enable/disable quarantine logging.
option
-enable
Option
Description
disable
Disable quarantine logging.
enable
Enable quarantine logging.
rate-count
Count of the rate.
integer
Minimum value:
0 Maximum
value: 65535
0
rate-duration
Duration (sec) of the rate.
integer
Minimum value:
1 Maximum
value: 65535
60
rate-mode
Rate limit mode.
option
-continuous
Option
Description
periodical
Allow configured number of packets every rate-duration.
continuous
Block packets once the rate is reached.
rate-track
Track the packet protocol field.
option
-none
FortiOS 8.0.0 CLI Reference
198
Fortinet Inc.

<!-- 来源页 199 -->
Parameter
Description
Type
Size
Default
Option
Description
none
none
src-ip
Source IP.
dest-ip
Destination IP.
dhcp-client-mac
DHCP client.
dns-domain
DNS domain.
risk <level>
Risk, or impact, of allowing traffic from this
application to occur (1 - 5; Low, Elevated,
Medium, High, and Critical).
Risk, or impact, of allowing traffic from this
application to occur (1 - 5; Low, Elevated,
Medium, High, and Critical).
integer
Minimum value:
0 Maximum
value:
4294967295
session-ttl
Session TTL (0 = default).
integer
Minimum value:
0 Maximum
value:
4294967295
0
shaper
Traffic shaper.
string
Maximum
length: 35
shaper-reverse
Reverse traffic shaper.
string
Maximum
length: 35
technology
Application technology filter.
user
Not Specified
all
vendor
Application vendor filter.
user
Not Specified
all
* This parameter may not exist in some models.
config parameters
Parameter
Description
Type
Size
Default
id
Parameter tuple ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
FortiOS 8.0.0 CLI Reference
199
Fortinet Inc.

<!-- 来源页 200 -->
config members
Parameter
Description
Type
Size
Default
id
Parameter.
integer
Minimum value:
0 Maximum
value:
4294967295
0
name
Parameter name.
string
Maximum
length: 31
value
Parameter value.
string
Maximum
length: 199
config application name
Configure application signatures. Read-only.
config application name
Description: Configure application signatures. Read-only.
edit <name>
set behavior {user}
set category {integer}
set id {integer}
config metadata
Description: Meta data. Read-only.
edit <id>
set metaid {integer}
set valueid {integer}
next
end
config parameters
Description: Application parameters. Read-only.
edit <name>
set default value {string}
next
end
set popularity {integer}
set protocol {user}
set risk {integer}
set technology {user}
set vendor {user}
set weight {integer}
next
end
FortiOS 8.0.0 CLI Reference
200
Fortinet Inc.

<!-- 来源页 201 -->
config application name
Parameter
Description
Type
Size
Default
behavior
Application behavior. Read-only.
user
Not Specified
category
Application category ID. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
id
Application ID. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
name
Application name.
string
Maximum
length: 63
popularity
Application popularity. Read-only.
integer
Minimum value:
0 Maximum
value: 255
0
protocol
Application protocol. Read-only.
user
Not Specified
risk
Application risk. Read-only.
integer
Minimum value:
0 Maximum
value: 255
0
technology
Application technology. Read-only.
user
Not Specified
vendor
Application vendor. Read-only.
user
Not Specified
weight
Application weight. Read-only.
integer
Minimum value:
0 Maximum
value: 255
0
config metadata
Parameter
Description
Type
Size
Default
id
ID. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
metaid
Meta ID. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
FortiOS 8.0.0 CLI Reference
201
Fortinet Inc.

<!-- 来源页 202 -->
Parameter
Description
Type
Size
Default
valueid
Value ID. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config parameters
Parameter
Description
Type
Size
Default
default value
Parameter default value. Read-only.
string
Maximum
length: 199
name
Parameter name. Read-only.
string
Maximum
length: 31
config application rule-settings
Configure application rule settings. Read-only.
config application rule-settings
Description: Configure application rule settings. Read-only.
edit <id>
next
end
config application rule-settings
Parameter
Description
Type
Size
Default
id
Rule ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
FortiOS 8.0.0 CLI Reference
202
Fortinet Inc.

<!-- 来源页 203 -->
config application unsanctioned-apps
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
Configure unsanctioned applications.
config application unsanctioned-apps
Description: Configure unsanctioned applications.
edit <id>
set app {integer}
set category {user}
set status [unsanctioned|sanctioned]
set type [app|category]
next
end
FortiOS 8.0.0 CLI Reference
203
Fortinet Inc.

<!-- 来源页 204 -->
config application unsanctioned-apps
Parameter
Description
Type
Size
Default
app
Application ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
category
Application category.
user
Not Specified
id
Entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
status
Status.
option
-unsanctioned
Option
Description
unsanctioned
Set unsanctioned.
sanctioned
Set sanctioned.
type
Type.
option
-app
Option
Description
app
Application.
category
Category.
FortiOS 8.0.0 CLI Reference
204
Fortinet Inc.
