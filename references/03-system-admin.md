# 系统：管理 / AAA / 认证 / 消息 / 自动化

> 来源: FortiOS-8.0.0-CLI_Reference.pdf
> 覆盖命令/章节: config system admin, config system accprofile, config system api-user, config system password-policy, config system password-policy-guest-admin, config system sso-admin, config system sso-forticloud-admin, config system sso-fortigate-cloud-admin, config system saml, config system central-management, config system csf, config system fortiguard, config system console, config system dedicated-mgmt, config system theme, config system timezone, config system automation-stitch, config system automation-action, config system automation-trigger, config system automation-condition, config system automation-destination, config system replacemsg-group, config system cloud-service, config system fortisandbox, config system email-server, config system sms-server, config system resource-limits, config system storage
> 本文件由 extract_pdf.py 从官方 PDF 自动提取，请勿手动编辑；
> 如需修正请修改 map.json 后重跑脚本。

---


<!-- 来源页 1456 -->
set class-id {user}
set init-string {string}
set model {string}
set modeswitch-string {string}
set product-id {user}
set vendor {string}
set vendor-id {user}
next
end
config system 3g-modem custom
Parameter
Description
Type
Size
Default
class-id
USB interface class in hexadecimal format (00-ff).
user
Not Specified
id
ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
init-string
Init string in hexadecimal format (even length).
string
Maximum
length: 127
model
MODEM model name.
string
Maximum
length: 35
modeswitch-string
USB modeswitch arguments. For example: '-v
1410 -p 9030 -V 1410 -P 9032 -u 3'.
string
Maximum
length: 127
product-id
USB product ID in hexadecimal format (0000-ffff).
user
Not Specified
vendor
MODEM vendor name.
string
Maximum
length: 35
vendor-id
USB vendor ID in hexadecimal format (0000-ffff).
user
Not Specified
config system accprofile
Configure access profiles for system administrators.
config system accprofile
Description: Configure access profiles for system administrators.
edit <name>
set admintimeout {integer}
set admintimeout-override [enable|disable]
set authgrp [none|read|...]
FortiOS 8.0.0 CLI Reference
1456
Fortinet Inc.

<!-- 来源页 1457 -->
set cli-config [enable|disable]
set cli-diagnose [enable|disable]
set cli-exec [enable|disable]
set cli-get [enable|disable]
set cli-show [enable|disable]
set comments {var-string}
set ftviewgrp [none|read|...]
set fwgrp [none|read|...]
config fwgrp-permission
Description: Custom firewall permission.
set address [none|read|...]
set others [none|read|...]
set policy [none|read|...]
set schedule [none|read|...]
set service [none|read|...]
end
set gui-ai-assistant [enable|disable]
set gui-custom-theme {string}
set gui-theme [jade|neutrino|...]
set gui-theme-type [predefined|custom]
set loggrp [none|read|...]
config loggrp-permission
Description: Custom Log & Report permission.
set config [none|read|...]
set data-access [none|read|...]
set report-access [none|read|...]
set threat-weight [none|read|...]
end
set netgrp [none|read|...]
config netgrp-permission
Description: Custom network permission.
set cfg [none|read|...]
set packet-capture [none|read|...]
set route-cfg [none|read|...]
end
set scope [vdom|global]
set secfabgrp [none|read|...]
config secfabgrp-permission
Description: Custom Security Fabric permissions.
set csffoo [none|read|...]
set csfsys [none|read|...]
end
set sysgrp [none|read|...]
config sysgrp-permission
Description: Custom system permission.
set admin [none|read|...]
set cfg [none|read|...]
set mnt [none|read|...]
set upd [none|read|...]
end
set system-execute-ssh [enable|disable]
set system-execute-telnet [enable|disable]
FortiOS 8.0.0 CLI Reference
1457
Fortinet Inc.

<!-- 来源页 1458 -->
set utmgrp [none|read|...]
config utmgrp-permission
Description: Custom Security Profile permissions.
set antivirus [none|read|...]
set application-control [none|read|...]
set casb [none|read|...]
set dlp [none|read|...]
set dnsfilter [none|read|...]
set emailfilter [none|read|...]
set endpoint-control [none|read|...]
set file-filter [none|read|...]
set icap [none|read|...]
set ips [none|read|...]
set telemetry [none|read|...]
set videofilter [none|read|...]
set virtual-patch [none|read|...]
set voip [none|read|...]
set waf [none|read|...]
set webfilter [none|read|...]
end
set vpngrp [none|read|...]
set wanoptgrp [none|read|...]
set wifi [none|read|...]
next
end
config system accprofile
Parameter
Description
Type
Size
Default
admintimeout
Administrator timeout for this access profile (0
- 480 min, default = 10, 0 means never
timeout).
integer
Minimum
value: 1
Maximum
value: 480
10
admintimeout-override
Enable/disable overriding the global
administrator idle timeout.
option
-disable
Option
Description
enable
Enable overriding the global administrator idle timeout.
disable
Disable overriding the global administrator idle timeout.
authgrp
Administrator access to Users and Devices.
option
-none
Option
Description
none
No access.
read
Read access.
FortiOS 8.0.0 CLI Reference
1458
Fortinet Inc.

<!-- 来源页 1459 -->
Parameter
Description
Type
Size
Default
Option
Description
read-write
Read/write access.
cli-config
Enable/disable permission to run config
commands.
option
-disable
Option
Description
enable
Enable permission to run config commands.
disable
Disable permission to run config commands.
cli-diagnose
Enable/disable permission to run diagnostic
commands.
option
-disable
Option
Description
enable
Enable permission to run diagnostic commands.
disable
Disable permission to run diagnostic commands.
cli-exec
Enable/disable permission to run execute
commands.
option
-disable
Option
Description
enable
Enable permission to run execute commands.
disable
Disable permission to run execute commands.
cli-get
Enable/disable permission to run get
commands.
option
-disable
Option
Description
enable
Enable permission to run get commands.
disable
Disable permission to run get commands.
cli-show
Enable/disable permission to run show
commands.
option
-disable
Option
Description
enable
Enable permission to run show commands.
disable
Disable permission to run show commands.
comments
Comment.
var-string
Maximum
length: 255
ftviewgrp
FortiView.
option
-none
FortiOS 8.0.0 CLI Reference
1459
Fortinet Inc.

<!-- 来源页 1460 -->
Parameter
Description
Type
Size
Default
Option
Description
none
No access.
read
Read access.
read-write
Read/write access.
fwgrp
Administrator access to the Firewall
configuration.
option
-none
Option
Description
none
No access.
read
Read access.
read-write
Read/write access.
custom
Customized access.
gui-ai-assistant
*
Enable/disable permission to use AI assistant.
option
-enable
Option
Description
enable
Enable permission to use AI assistant.
disable
Disable permission to use AI assistant.
gui-custom-theme *
Custom theme that overrides the default
FortiGate theme.
string
Maximum
length: 35
gui-theme *
Predefined theme that overrides the default
FortiGate theme.
option
-none
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
FortiOS 8.0.0 CLI Reference
1460
Fortinet Inc.

<!-- 来源页 1461 -->
Parameter
Description
Type
Size
Default
Option
Description
onyx
Onyx theme.
eclipse
Eclipse theme.
none
No theme.
gui-theme-type
*
Use predefined themes or custom themes.
option
-predefined
Option
Description
predefined
Use predefined theme.
custom
Use custom theme.
loggrp
Administrator access to Logging and
Reporting including viewing log messages.
option
-none
Option
Description
none
No access.
read
Read access.
read-write
Read/write access.
custom
Customized access.
name
Profile name.
string
Maximum
length: 35
netgrp
Network Configuration.
option
-none
Option
Description
none
No access.
read
Read access.
read-write
Read/write access.
custom
Customized access.
scope
Scope of admin access: global or specific
VDOM(s).
option
-vdom
Option
Description
vdom
VDOM access.
global
Global access.
FortiOS 8.0.0 CLI Reference
1461
Fortinet Inc.

<!-- 来源页 1462 -->
Parameter
Description
Type
Size
Default
secfabgrp
Security Fabric.
option
-none
Option
Description
none
No access.
read
Read access.
read-write
Read/write access.
custom
Customized access.
sysgrp
System Configuration.
option
-none
Option
Description
none
No access.
read
Read access.
read-write
Read/write access.
custom
Customized access.
system-execute-ssh
Enable/disable permission to execute SSH
commands.
option
-enable
Option
Description
enable
Enable permission to execute SSH commands.
disable
Disable permission to execute SSH commands.
system-execute-telnet
Enable/disable permission to execute TELNET
commands.
option
-enable
Option
Description
enable
Enable permission to execute TELNET commands.
disable
Disable permission to execute TELNET commands.
utmgrp
Administrator access to Security Profiles.
option
-none
Option
Description
none
No access.
read
Read access.
read-write
Read/write access.
custom
Customized access.
FortiOS 8.0.0 CLI Reference
1462
Fortinet Inc.

<!-- 来源页 1463 -->
Parameter
Description
Type
Size
Default
vpngrp
Administrator access to IPsec, SSL, PPTP, and
L2TP VPN.
option
-none
Option
Description
none
No access.
read
Read access.
read-write
Read/write access.
wanoptgrp *
Administrator access to WAN Opt & Cache.
option
-none
Option
Description
none
No access.
read
Read access.
read-write
Read/write access.
wifi
Administrator access to the WiFi controller and
Switch controller.
option
-none
Option
Description
none
No access.
read
Read access.
read-write
Read/write access.
* This parameter may not exist in some models.
config fwgrp-permission
Parameter
Description
Type
Size
Default
address
Address Configuration.
option
-none
Option
Description
none
No access.
read
Read access.
read-write
Read/write access.
others
Other Firewall Configuration.
option
-none
Option
Description
none
No access.
FortiOS 8.0.0 CLI Reference
1463
Fortinet Inc.

<!-- 来源页 1464 -->
Parameter
Description
Type
Size
Default
Option
Description
read
Read access.
read-write
Read/write access.
policy
Policy Configuration.
option
-none
Option
Description
none
No access.
read
Read access.
read-write
Read/write access.
schedule
Schedule Configuration.
option
-none
Option
Description
none
No access.
read
Read access.
read-write
Read/write access.
service
Service Configuration.
option
-none
Option
Description
none
No access.
read
Read access.
read-write
Read/write access.
config loggrp-permission
Parameter
Description
Type
Size
Default
config
Log & Report configuration.
option
-none
Option
Description
none
No access.
read
Read access.
read-write
Read/write access.
data-access
Log & Report Data Access.
option
-none
FortiOS 8.0.0 CLI Reference
1464
Fortinet Inc.

<!-- 来源页 1465 -->
Parameter
Description
Type
Size
Default
Option
Description
none
No access.
read
Read access.
read-write
Read/write access.
report-access
Log & Report Report Access.
option
-none
Option
Description
none
No access.
read
Read access.
read-write
Read/write access.
threat-weight
Log & Report Threat Weight.
option
-none
Option
Description
none
No access.
read
Read access.
read-write
Read/write access.
config netgrp-permission
Parameter
Description
Type
Size
Default
cfg
Network Configuration.
option
-none
Option
Description
none
No access.
read
Read access.
read-write
Read/write access.
packet-capture
Packet Capture Configuration.
option
-none
Option
Description
none
No access.
read
Read access.
read-write
Read/write access.
route-cfg
Router Configuration.
option
-none
FortiOS 8.0.0 CLI Reference
1465
Fortinet Inc.

<!-- 来源页 1466 -->
Parameter
Description
Type
Size
Default
Option
Description
none
No access.
read
Read access.
read-write
Read/write access.
config secfabgrp-permission
Parameter
Description
Type
Size
Default
csffoo
Fabric Overlay Orchestrator profiles and settings.
option
-none
Option
Description
none
No access.
read
Read access.
read-write
Read/write access.
csfsys
Security Fabric system profiles and settings.
option
-none
Option
Description
none
No access.
read
Read access.
read-write
Read/write access.
config sysgrp-permission
Parameter
Description
Type
Size
Default
admin
Administrator Users.
option
-none
Option
Description
none
No access.
read
Read access.
read-write
Read/write access.
cfg
System Configuration.
option
-none
Option
Description
none
No access.
FortiOS 8.0.0 CLI Reference
1466
Fortinet Inc.

<!-- 来源页 1467 -->
Parameter
Description
Type
Size
Default
Option
Description
read
Read access.
read-write
Read/write access.
mnt
Maintenance.
option
-none
Option
Description
none
No access.
read
Read access.
read-write
Read/write access.
upd
FortiGuard Updates.
option
-none
Option
Description
none
No access.
read
Read access.
read-write
Read/write access.
config utmgrp-permission
Parameter
Description
Type
Size
Default
antivirus
Antivirus profiles and settings.
option
-none
Option
Description
none
No access.
read
Read access.
read-write
Read/write access.
application-control
Application Control profiles and settings.
option
-none
Option
Description
none
No access.
read
Read access.
read-write
Read/write access.
casb
Inline CASB filter profile and settings
option
-none
FortiOS 8.0.0 CLI Reference
1467
Fortinet Inc.

<!-- 来源页 1468 -->
Parameter
Description
Type
Size
Default
Option
Description
none
No access.
read
Read access.
read-write
Read/write access.
dlp
DLP profiles and settings.
option
-none
Option
Description
none
No access.
read
Read access.
read-write
Read/write access.
dnsfilter
DNS Filter profiles and settings.
option
-none
Option
Description
none
No access.
read
Read access.
read-write
Read/write access.
emailfilter
Email Filter and settings.
option
-none
Option
Description
none
No access.
read
Read access.
read-write
Read/write access.
endpoint-control
FortiClient Profiles.
option
-none
Option
Description
none
No access.
read
Read access.
read-write
Read/write access.
file-filter
File-filter profiles and settings.
option
-none
Option
Description
none
No access.
FortiOS 8.0.0 CLI Reference
1468
Fortinet Inc.

<!-- 来源页 1469 -->
Parameter
Description
Type
Size
Default
Option
Description
read
Read access.
read-write
Read/write access.
icap
ICAP profiles and settings.
option
-none
Option
Description
none
No access.
read
Read access.
read-write
Read/write access.
ips
IPS profiles and settings.
option
-none
Option
Description
none
No access.
read
Read access.
read-write
Read/write access.
telemetry
Telemetry profile and settings.
option
-none
Option
Description
none
No access.
read
Read access.
read-write
Read/write access.
videofilter
Video filter profiles and settings.
option
-none
Option
Description
none
No access.
read
Read access.
read-write
Read/write access.
virtual-patch
Virtual patch profiles and settings.
option
-none
Option
Description
none
No access.
read
Read access.
read-write
Read/write access.
FortiOS 8.0.0 CLI Reference
1469
Fortinet Inc.

---


<!-- 来源页 1472 -->
Parameter
Description
Type
Size
Default
url
Account url.
string
Maximum
length: 511
config system admin
Configure admin users.
config system admin
Description: Configure admin users.
edit <name>
set accprofile {string}
set accprofile-override [enable|disable]
set allow-remove-admin-session [enable|disable]
set comments {var-string}
set disallowed-login-methods {option1}, {option2}, ...
set email-to {string}
set force-password-change [enable|disable]
set fortitoken {string}
set guest-auth [disable|enable]
set guest-lang {string}
set guest-usergroups <name1>, <name2>, ...
set gui-custom-theme {string}
set gui-llm-provider [fortiai|openai]
set gui-theme [jade|neutrino|...]
set gui-theme-type [predefined|custom]
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
set openai-api-key {password-3}
set openai-api-key-part2 {password-3}
set openai-model {string}
set openai-org-id {string}
set openai-project-id {string}
set password {password-2}
set password-expire {datetime}
set peer-auth [enable|disable]
set peer-group {string}
set remote-auth [enable|disable]
set remote-group {string}
set schedule {string}
set sms-custom-server {string}
FortiOS 8.0.0 CLI Reference
1472
Fortinet Inc.

<!-- 来源页 1473 -->
set sms-phone {string}
set sms-server [fortiguard|custom]
set ssh-certificate {string}
set ssh-public-key1 {user}
set ssh-public-key2 {user}
set ssh-public-key3 {user}
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
set two-factor [disable|fortitoken|...]
set two-factor-authentication [fortitoken|email|...]
set two-factor-notification [email|sms]
set vdom <name1>, <name2>, ...
set vdom-override [enable|disable]
set wildcard [enable|disable]
next
end
config system admin
Parameter
Description
Type
Size
Default
accprofile
Access profile for this administrator. Access
profiles control administrator access to
FortiGate features.
string
Maximum
length: 35
accprofile-override
Enable to use the name of an access profile
provided by the remote authentication
server to control the FortiGate features that
this administrator can access.
option
-disable
Option
Description
enable
Enable access profile override.
disable
Disable access profile override.
allow-remove-admin-session
Enable/disable allow admin session to be
removed by privileged admin users.
option
-enable
Option
Description
enable
Enable allow-remove option.
disable
Disable allow-remove option.
FortiOS 8.0.0 CLI Reference
1473
Fortinet Inc.

<!-- 来源页 1474 -->
Parameter
Description
Type
Size
Default
comments
Comment.
var-string
Maximum
length: 255
disallowed-login-methods *
Configure login methods that explicitly are
disallowed. All other login methods not listed
here are permitted by default.
option
-Option
Description
console
Console.
gui
GUI (https/http).
ssh
SSH.
telnet
Telnet.
email-to
This administrator's email address.
string
Maximum
length: 63
force-password-change
Enable/disable force password change on
next login.
option
-disable
Option
Description
enable
Enable force password change on next login.
disable
Disable force password change on next login.
fortitoken
This administrator's FortiToken serial
number.
string
Maximum
length: 16
guest-auth
Enable/disable guest authentication.
option
-disable
Option
Description
disable
Disable guest authentication.
enable
Enable guest authentication.
guest-lang
Guest management portal language.
string
Maximum
length: 35
guest-usergroups
<name>
Select guest user groups.
Select guest user groups.
string
Maximum
length: 79
gui-custom-theme *
Custom theme that overrides the default
FortiGate theme.
string
Maximum
length: 35
gui-llm-provider
*
Select the LLM provider.
option
-fortiai
FortiOS 8.0.0 CLI Reference
1474
Fortinet Inc.

<!-- 来源页 1475 -->
Parameter
Description
Type
Size
Default
Option
Description
fortiai
FortiAI.
openai
Use your own OpenAI API key.
gui-theme *
Predefined theme that overrides the default
FortiGate theme.
option
-none
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
none
No theme.
gui-theme-type
*
Use predefined themes or custom themes.
option
-predefined
Option
Description
predefined
Use predefined theme.
custom
Use custom theme.
ip6-trusthost1
Any IPv6 address from which the
administrator can connect to the FortiGate
unit. Default allows access from any IPv6
address.
ipv6-prefix
Not
Specified
::/0
ip6-trusthost10
Any IPv6 address from which the
administrator can connect to the FortiGate
unit. Default allows access from any IPv6
address.
ipv6-prefix
Not
Specified
::/0
FortiOS 8.0.0 CLI Reference
1475
Fortinet Inc.

<!-- 来源页 1476 -->
Parameter
Description
Type
Size
Default
ip6-trusthost2
Any IPv6 address from which the
administrator can connect to the FortiGate
unit. Default allows access from any IPv6
address.
ipv6-prefix
Not
Specified
::/0
ip6-trusthost3
Any IPv6 address from which the
administrator can connect to the FortiGate
unit. Default allows access from any IPv6
address.
ipv6-prefix
Not
Specified
::/0
ip6-trusthost4
Any IPv6 address from which the
administrator can connect to the FortiGate
unit. Default allows access from any IPv6
address.
ipv6-prefix
Not
Specified
::/0
ip6-trusthost5
Any IPv6 address from which the
administrator can connect to the FortiGate
unit. Default allows access from any IPv6
address.
ipv6-prefix
Not
Specified
::/0
ip6-trusthost6
Any IPv6 address from which the
administrator can connect to the FortiGate
unit. Default allows access from any IPv6
address.
ipv6-prefix
Not
Specified
::/0
ip6-trusthost7
Any IPv6 address from which the
administrator can connect to the FortiGate
unit. Default allows access from any IPv6
address.
ipv6-prefix
Not
Specified
::/0
ip6-trusthost8
Any IPv6 address from which the
administrator can connect to the FortiGate
unit. Default allows access from any IPv6
address.
ipv6-prefix
Not
Specified
::/0
ip6-trusthost9
Any IPv6 address from which the
administrator can connect to the FortiGate
unit. Default allows access from any IPv6
address.
ipv6-prefix
Not
Specified
::/0
name
User name.
string
Maximum
length: 64
openai-api-key
*
Openai API key.
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
**
FortiOS 8.0.0 CLI Reference
1476
Fortinet Inc.

<!-- 来源页 1477 -->
Parameter
Description
Type
Size
Default
openai-org-id *
OpenAI organization ID.
string
Maximum
length: 35
openai-project-id *
OpenAI project ID.
string
Maximum
length: 35
password
Admin user password.
password-2
Not
Specified
password-expire
Password expire time.
datetime
Not
Specified
0000-00-00
00:00:00
peer-auth
Set to enable peer certificate authentication
(for HTTPS admin access).
option
-disable
Option
Description
enable
Enable peer.
disable
Disable peer.
peer-group
Name of peer group defined under config
user group which has PKI members. Used
for peer certificate authentication (for
HTTPS admin access).
string
Maximum
length: 35
remote-auth
Enable/disable authentication using a
remote RADIUS, LDAP, or TACACS+ server.
option
-disable
Option
Description
enable
Enable remote authentication.
disable
Disable remote authentication.
remote-group
User group name used for remote auth.
string
Maximum
length: 35
schedule
Firewall schedule used to restrict when the
administrator can log in. No schedule means
no restrictions.
string
Maximum
length: 35
sms-custom-server
Custom SMS server to send SMS messages
to.
string
Maximum
length: 35
sms-phone
Phone number on which the administrator
receives SMS messages.
string
Maximum
length: 15
sms-server
Send SMS messages using the FortiGuard
SMS server or a custom server.
option
-fortiguard
FortiOS 8.0.0 CLI Reference
1477
Fortinet Inc.

<!-- 来源页 1478 -->
Parameter
Description
Type
Size
Default
Option
Description
fortiguard
Send SMS by FortiGuard.
custom
Send SMS by custom server.
ssh-certificate
Select the certificate to be used by the
FortiGate for authentication with an SSH
client.
string
Maximum
length: 35
ssh-public-key1
Public key of an SSH client. The client is
authenticated without being asked for
credentials. Create the public-private key
pair in the SSH client application.
user
Not
Specified
ssh-public-key2
Public key of an SSH client. The client is
authenticated without being asked for
credentials. Create the public-private key
pair in the SSH client application.
user
Not
Specified
ssh-public-key3
Public key of an SSH client. The client is
authenticated without being asked for
credentials. Create the public-private key
pair in the SSH client application.
user
Not
Specified
trusthost1
Any IPv4 address or subnet address and
netmask from which the administrator can
connect to the FortiGate unit. Default allows
access from any IPv4 address.
ipv4-classnet
Not
Specified
0.0.0.0
0.0.0.0
trusthost10
Any IPv4 address or subnet address and
netmask from which the administrator can
connect to the FortiGate unit. Default allows
access from any IPv4 address.
ipv4-classnet
Not
Specified
0.0.0.0
0.0.0.0
trusthost2
Any IPv4 address or subnet address and
netmask from which the administrator can
connect to the FortiGate unit. Default allows
access from any IPv4 address.
ipv4-classnet
Not
Specified
0.0.0.0
0.0.0.0
trusthost3
Any IPv4 address or subnet address and
netmask from which the administrator can
connect to the FortiGate unit. Default allows
access from any IPv4 address.
ipv4-classnet
Not
Specified
0.0.0.0
0.0.0.0
trusthost4
Any IPv4 address or subnet address and
netmask from which the administrator can
connect to the FortiGate unit. Default allows
access from any IPv4 address.
ipv4-classnet
Not
Specified
0.0.0.0
0.0.0.0
FortiOS 8.0.0 CLI Reference
1478
Fortinet Inc.

<!-- 来源页 1479 -->
Parameter
Description
Type
Size
Default
trusthost5
Any IPv4 address or subnet address and
netmask from which the administrator can
connect to the FortiGate unit. Default allows
access from any IPv4 address.
ipv4-classnet
Not
Specified
0.0.0.0
0.0.0.0
trusthost6
Any IPv4 address or subnet address and
netmask from which the administrator can
connect to the FortiGate unit. Default allows
access from any IPv4 address.
ipv4-classnet
Not
Specified
0.0.0.0
0.0.0.0
trusthost7
Any IPv4 address or subnet address and
netmask from which the administrator can
connect to the FortiGate unit. Default allows
access from any IPv4 address.
ipv4-classnet
Not
Specified
0.0.0.0
0.0.0.0
trusthost8
Any IPv4 address or subnet address and
netmask from which the administrator can
connect to the FortiGate unit. Default allows
access from any IPv4 address.
ipv4-classnet
Not
Specified
0.0.0.0
0.0.0.0
trusthost9
Any IPv4 address or subnet address and
netmask from which the administrator can
connect to the FortiGate unit. Default allows
access from any IPv4 address.
ipv4-classnet
Not
Specified
0.0.0.0
0.0.0.0
two-factor
Enable/disable two-factor authentication.
option
-disable
Option
Description
disable
Disable two-factor authentication.
fortitoken
Use FortiToken or FortiToken mobile two-factor authentication.
fortitoken-cloud
FortiToken Cloud Service.
email
Send a two-factor authentication code to the configured email-to
email address.
sms
Send a two-factor authentication code to the configured sms-server
and sms-phone.
two-factor-authentication
Authentication method by FortiToken Cloud.
option
-Option
Description
fortitoken
FortiToken authentication.
email
Email one time password.
sms
SMS one time password.
FortiOS 8.0.0 CLI Reference
1479
Fortinet Inc.

---


<!-- 来源页 1485 -->
config system alias
Configure alias command.
config system alias
Description: Configure alias command.
edit <name>
set command {var-string}
next
end
config system alias
Parameter
Description
Type
Size
Default
command
Command list to execute.
var-string
Maximum
length: 255
name
Alias command name.
string
Maximum
length: 35
config system api-user
Configure API users.
config system api-user
Description: Configure API users.
edit <name>
set accprofile {string}
set api-key {password-2}
set comments {var-string}
set cors-allow-origin {string}
set peer-auth [enable|disable]
set peer-group {string}
set schedule {string}
config trusthost
Description: Trusthost.
edit <id>
set ipv4-trusthost {ipv4-classnet}
set ipv6-trusthost {ipv6-prefix}
set type [ipv4-trusthost|ipv6-trusthost]
next
end
set vdom <name1>, <name2>, ...
next
end
FortiOS 8.0.0 CLI Reference
1485
Fortinet Inc.

<!-- 来源页 1486 -->
config system api-user
Parameter
Description
Type
Size
Default
accprofile
Admin user access profile.
string
Maximum
length: 35
api-key
Admin user password.
password-2
Not
Specified
comments
Comment.
var-string
Maximum
length: 255
cors-allow-origin
Value for Access-Control-Allow-Origin on API
responses. Avoid using '*' if possible.
string
Maximum
length: 269
name
User name.
string
Maximum
length: 35
peer-auth
Enable/disable peer authentication.
option
-disable
Option
Description
enable
Enable peer.
disable
Disable peer.
peer-group
Peer group name.
string
Maximum
length: 35
schedule
Schedule name.
string
Maximum
length: 35
vdom <name>
Virtual domains.
Virtual domain name.
string
Maximum
length: 79
config trusthost
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
ipv4-trusthost
IPv4 trusted host address.
ipv4-classnet
Not Specified
0.0.0.0
0.0.0.0
ipv6-trusthost
IPv6 trusted host address.
ipv6-prefix
Not Specified
::/0
type
Trusthost type.
option
-ipv4-trusthost
FortiOS 8.0.0 CLI Reference
1486
Fortinet Inc.

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

<!-- 来源页 1488 -->
set action-type [email|fortiexplorer-notification|...]
set alicloud-access-key-id {string}
set alicloud-access-key-secret {password}
set alicloud-function-authorization [anonymous|function]
set aws-api-key {password}
set azure-api-key {password}
set azure-function-authorization [anonymous|function|...]
set description {var-string}
set duration {integer}
set email-from {var-string}
set email-subject {var-string}
set email-to <name1>, <name2>, ...
set execute-security-fabric [enable|disable]
set file-only [enable|disable]
config form-data
Description: Form data parts for content type multipart/form-data.
edit <id>
set key {var-string}
set value {var-string}
next
end
set forticare-email [enable|disable]
set http-body {var-string}
config http-headers
Description: Request headers.
edit <id>
set key {var-string}
set value {var-string}
next
end
set log-debug-print [enable|disable]
set message {string}
set message-type [text|json|...]
set method [post|put|...]
set minimum-interval {integer}
set output-interval {integer}
set output-size {integer}
set port {integer}
set protocol [http|https]
set regular-expression {var-string}
set replacement-message [enable|disable]
set replacemsg-group {string}
set script {var-string}
set sdn-connector <name1>, <name2>, ...
set security-tag {string}
set system-action [reboot|shutdown|...]
set timeout {integer}
set tls-certificate {string}
set uri {var-string}
set verify-host-cert [enable|disable]
next
end
FortiOS 8.0.0 CLI Reference
1488
Fortinet Inc.

<!-- 来源页 1489 -->
config system automation-action
Parameter
Description
Type
Size
Default
accprofile
Access profile for CLI script action to
access FortiGate features.
string
Maximum
length: 35
action-type
Action type.
option
-alert
Option
Description
email
Send notification email.
fortiexplorer-notification
Send push notification to FortiExplorer.
alert
Generate FortiOS dashboard alert.
disable-ssid
Disable interface.
system-actions
Perform immediate system operations on this FortiGate unit.
quarantine
Quarantine host.
quarantine-forticlient
Quarantine FortiClient by EMS.
quarantine-nsx
Quarantine NSX instance.
quarantine-fortinac
Quarantine host by FortiNAC.
ban-ip
Ban IP address.
aws-lambda
Send log data to integrated AWS service.
azure-function
Send log data to an Azure function.
google-cloud-function
Send log data to a Google Cloud function.
alicloud-function
Send log data to an AliCloud function.
webhook
Send an HTTP request.
cli-script
Run CLI script.
diagnose-script
Run diagnose script.
regular-expression
Match pattern on input text.
slack-notification
Send a notification message to a Slack incoming webhook.
FortiOS 8.0.0 CLI Reference
1489
Fortinet Inc.

<!-- 来源页 1490 -->
Parameter
Description
Type
Size
Default
Option
Description
microsoft-teams-notification
Send a notification message to a Microsoft Teams incoming webhook.
alicloud-access-key-id
AliCloud AccessKey ID.
string
Maximum
length: 35
alicloud-access-key-secret
AliCloud AccessKey secret.
password
Not
Specified
alicloud-function-authorization
AliCloud function authorization type.
option
-anonymous
Option
Description
anonymous
Anonymous authorization (No authorization required).
function
Function authorization (Authorization required).
aws-api-key
AWS API Gateway API key.
password
Not
Specified
azure-api-key
Azure function API key.
password
Not
Specified
azure-function-authorization
Azure function authorization level.
option
-anonymous
Option
Description
anonymous
Anonymous authorization level (No authorization required).
function
Function authorization level (Function or Host Key required).
admin
Admin authorization level (Master Host Key required).
description
Description.
var-string
Maximum
length: 255
duration
Maximum running time for this script in
seconds.
integer
Minimum
value: 1
Maximum
value:
36000
5
email-from
Email sender name.
var-string
Maximum
length: 127
FortiOS 8.0.0 CLI Reference
1490
Fortinet Inc.

<!-- 来源页 1491 -->
Parameter
Description
Type
Size
Default
email-subject
Email subject.
var-string
Maximum
length: 511
email-to <name>
Email addresses.
Email address.
string
Maximum
length: 255
execute-security-fabric
Enable/disable execution of CLI script
on all or only one FortiGate unit in the
Security Fabric.
option
-disable
Option
Description
enable
CLI script executes on all FortiGate units in the Security Fabric.
disable
CLI script executes only on the FortiGate unit that the stitch is
triggered.
file-only
Enable/disable the output in files only.
option
-disable
Option
Description
enable
The output of the diag CLI will only be files.
disable
The output of the diag CLI will be in raw text, output larger than 64KB
will be in files.
forticare-email
Enable/disable use of your FortiCare
email address as the email-to address.
option
-disable
Option
Description
enable
Enable use of your FortiCare email address as the email-to address.
disable
Disable use of your FortiCare email address as the email-to address.
http-body
Request body (if necessary). Should
be serialized json string.
var-string
Maximum
length:
4095
log-debug-print
Enable/disable logging debug print
output from diagnose action.
option
-disable
Option
Description
enable
Enable logging debug print output from diagnose action.
disable
Disable logging debug print output from diagnose action.
FortiOS 8.0.0 CLI Reference
1491
Fortinet Inc.

<!-- 来源页 1492 -->
Parameter
Description
Type
Size
Default
message
Message content.
string
Maximum
length:
4095
Time:
%%log.date%%
%%log.time%%
Device:
%%log.devid%%
(%%log.vd%%)
Level:
%%log.level%%
Event:
%%log.logdesc%%
Raw log: %%log%%
message-type
Message type.
option
-text
Option
Description
text
Plaintext.
json
Custom JSON.
form-data
Multipart/form-data
method
Request method (POST, PUT, GET,
PATCH or DELETE).
option
-post
Option
Description
post
POST.
put
PUT.
get
GET.
patch
PATCH.
delete
DELETE.
minimum-interval
Limit execution to no more than once
in this interval (in seconds).
integer
Minimum
value: 0
Maximum
value:
2592000
0
name
Name.
string
Maximum
length: 64
output-interval
Collect the outputs for each output-interval in seconds (0 = no
intermediate output).
integer
Minimum
value: 0
Maximum
value:
36000
0
FortiOS 8.0.0 CLI Reference
1492
Fortinet Inc.

<!-- 来源页 1493 -->
Parameter
Description
Type
Size
Default
output-size
Number of megabytes to limit script
output to (1 - 1024, default = 10).
integer
Minimum
value: 1
Maximum
value: 1024
10
port
Protocol port.
integer
Minimum
value: 1
Maximum
value:
65535
0
protocol
Request protocol.
option
-http
Option
Description
http
HTTP.
https
HTTPS.
regular-expression
Regular expression string.
var-string
Maximum
length:
1023
replacement-message
Enable/disable replacement message.
option
-disable
Option
Description
enable
Enable replacement message.
disable
Disable replacement message.
replacemsg-group
Replacement message group.
string
Maximum
length: 35
script
CLI script.
var-string
Maximum
length:
1023
sdn-connector
<name>
NSX SDN connector names.
SDN connector name.
string
Maximum
length: 79
security-tag
NSX security tag.
string
Maximum
length: 255
system-action
System action type.
option
-Option
Description
reboot
Reboot this FortiGate unit.
shutdown
Shutdown this FortiGate unit.
FortiOS 8.0.0 CLI Reference
1493
Fortinet Inc.

<!-- 来源页 1494 -->
Parameter
Description
Type
Size
Default
Option
Description
backup-config
Backup current configuration to the disk revisions.
timeout
Maximum running time for this script in
seconds (0 = no timeout).
integer
Minimum
value: 0
Maximum
value: 300
0
tls-certificate
Custom TLS certificate for API request.
string
Maximum
length: 35
uri
Request API URI.
var-string
Maximum
length:
1023
verify-host-cert
Enable/disable verification of the
remote host certificate.
option
-enable
Option
Description
enable
Enable verification of the remote host certificate.
disable
Disable verification of the remote host certificate.
config form-data
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
key
Key of the part of Multipart/form-data.
var-string
Maximum
length: 1023
value
Value of the part of Multipart/form-data.
var-string
Maximum
length: 4095
config http-headers
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
FortiOS 8.0.0 CLI Reference
1494
Fortinet Inc.

---


<!-- 来源页 1495 -->
Parameter
Description
Type
Size
Default
key
Request header key.
var-string
Maximum
length: 1023
value
Request header value.
var-string
Maximum
length: 4095
config system automation-condition
Condition for automation stitches.
config system automation-condition
Description: Condition for automation stitches.
edit <name>
set condition-type [cpu|memory|...]
set cpu-usage-percent {integer}
set description {var-string}
set input-id {integer}
set input-state [open|close]
set mem-usage-percent {integer}
set vdom {string}
set vpn-tunnel-name {string}
set vpn-tunnel-state [tunnel-up|tunnel-down]
next
end
config system automation-condition
Parameter
Description
Type
Size
Default
condition-type
Condition type.
option
-cpu
Option
Description
cpu
CPU usage condition,
memory
Memory usage condition,
vpn
VPN state condition.
input
input condition.
cpu-usage-percent
CPU usage reaches specified percentage.
integer
Minimum value:
0 Maximum
value: 100
0
description
Description.
var-string
Maximum
length: 255
FortiOS 8.0.0 CLI Reference
1495
Fortinet Inc.

---


<!-- 来源页 1496 -->
Parameter
Description
Type
Size
Default
input-id *
Input ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
input-state *
Input state.
option
-close
Option
Description
open
Input switch is open.
close
Input switch is closed.
mem-usage-percent
Memory usage reaches specified percentage.
integer
Minimum value:
0 Maximum
value: 100
0
name
Name.
string
Maximum
length: 35
vdom
Virtual domain which the tunnel belongs to.
string
Maximum
length: 31
root
vpn-tunnel-name
VPN tunnel name.
string
Maximum
length: 79
vpn-tunnel-state
VPN tunnel state.
option
-tunnel-up
Option
Description
tunnel-up
VPN tunnel is up.
tunnel-down
VPN tunnel is down.
* This parameter may not exist in some models.
config system automation-destination
Automation destinations.
config system automation-destination
Description: Automation destinations.
edit <name>
set destination <name1>, <name2>, ...
set ha-group-id {integer}
set type [fortigate|ha-cluster]
next
end
FortiOS 8.0.0 CLI Reference
1496
Fortinet Inc.

---


<!-- 来源页 1497 -->
config system automation-destination
Parameter
Description
Type
Size
Default
destination
<name>
Destinations.
Destination.
string
Maximum
length: 31
ha-group-id
Cluster group ID set for this destination (default =
0).
integer
Minimum
value: 0
Maximum
value: 255
0
name
Name.
string
Maximum
length: 35
type
Destination type.
option
-fortigate
Option
Description
fortigate
FortiGate set as destination.
ha-cluster
HA cluster set as destination.
config system automation-stitch
Automation stitches.
config system automation-stitch
Description: Automation stitches.
edit <name>
config actions
Description: Configure stitch actions.
edit <id>
set action {string}
set delay {integer}
set required [enable|disable]
next
end
set condition <name1>, <name2>, ...
set condition-logic [and|or]
set description {var-string}
set destination <name1>, <name2>, ...
set status [enable|disable]
set trigger {string}
next
end
FortiOS 8.0.0 CLI Reference
1497
Fortinet Inc.

<!-- 来源页 1498 -->
config system automation-stitch
Parameter
Description
Type
Size
Default
condition
<name>
Automation conditions.
Condition name.
string
Maximum
length: 79
condition-logic
Apply AND/OR logic to the specified automation
conditions.
option
-and
Option
Description
and
All specified conditions must be met.
or
At least one specified condition needs to be met.
description
Description.
var-string
Maximum
length: 255
destination
<name>
Serial number/HA group-name of destination
devices.
Destination name.
string
Maximum
length: 79
name
Name.
string
Maximum
length: 35
status
Enable/disable this stitch.
option
-enable
Option
Description
enable
Enable stitch.
disable
Disable stitch.
trigger
Trigger name.
string
Maximum
length: 35
config actions
Parameter
Description
Type
Size
Default
action
Action name.
string
Maximum
length: 64
delay
Delay before execution (in seconds).
integer
Minimum value:
0 Maximum
value: 3600
0
id
Entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
FortiOS 8.0.0 CLI Reference
1498
Fortinet Inc.

---


<!-- 来源页 1499 -->
Parameter
Description
Type
Size
Default
required
Required in action chain.
option
-disable
Option
Description
enable
Required in action chain.
disable
Not required in action chain.
config system automation-trigger
Trigger for automation stitches.
config system automation-trigger
Description: Trigger for automation stitches.
edit <name>
set description {var-string}
set event-type [ioc|event-log|...]
set fabric-event-name {var-string}
set fabric-event-severity {var-string}
set faz-event-name {var-string}
set faz-event-severity {var-string}
set faz-event-tags {var-string}
config fields
Description: Customized trigger field settings.
edit <id>
set name {string}
set value {var-string}
next
end
set license-type [forticare-support|fortiguard-webfilter|...]
set logid <id1>, <id2>, ...
set report-type [posture|coverage|...]
set serial {var-string}
set stitch-name {string}
set trigger-datetime {datetime}
set trigger-day {integer}
set trigger-frequency [hourly|daily|...]
set trigger-hour {integer}
set trigger-minute {integer}
set trigger-type [event-based|scheduled]
set trigger-weekday [sunday|monday|...]
set vdom <name1>, <name2>, ...
next
end
FortiOS 8.0.0 CLI Reference
1499
Fortinet Inc.

<!-- 来源页 1500 -->
config system automation-trigger
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
event-type
Event type.
option
-ioc
Option
Description
ioc
Indicator of compromise detected.
event-log
Use log ID as trigger.
reboot
Device reboot.
low-memory
Conserve mode due to low memory.
high-cpu
High CPU usage.
license-near-expiry
License near expiration date.
local-cert-near-expiry
The local certificate near expiration date.
ha-failover
HA failover.
config-change
Configuration change.
security-rating-summary
Security rating summary.
virus-ips-db-updated
Virus and IPS database updated.
faz-event
FortiAnalyzer event.
incoming-webhook
Incoming webhook call.
fabric-event
Fabric connector event.
ips-logs
IPS logs.
anomaly-logs
Anomaly logs.
virus-logs
Virus logs.
ssh-logs
SSH logs.
webfilter-violation
Webfilter violation.
traffic-violation
Traffic violation.
stitch
Specified stitch has been triggered.
FortiOS 8.0.0 CLI Reference
1500
Fortinet Inc.

<!-- 来源页 1501 -->
Parameter
Description
Type
Size
Default
fabric-event-name
Fabric connector event handler name.
var-string
Maximum
length: 255
fabric-event-severity
Fabric connector event severity.
var-string
Maximum
length: 255
faz-event-name
FortiAnalyzer event handler name.
var-string
Maximum
length: 255
faz-event-severity
FortiAnalyzer event severity.
var-string
Maximum
length: 255
faz-event-tags
FortiAnalyzer event tags.
var-string
Maximum
length: 255
license-type
License type.
option
-forticare-support
Option
Description
forticare-support
FortiCare support license.
fortiguard-webfilter
FortiGuard web filter license.
fortiguard-antispam
FortiGuard antispam license.
fortiguard-antivirus
FortiGuard AntiVirus license.
fortiguard-ips
FortiGuard IPS license.
fortiguard-management
FortiGuard management service license.
forticloud
FortiCloud license.
any
Any license.
logid <id>
Log IDs to trigger event.
Log ID.
integer
Minimum
value: 1
Maximum
value:
65535
name
Name.
string
Maximum
length: 35
report-type
Security Rating report.
option
-posture
FortiOS 8.0.0 CLI Reference
1501
Fortinet Inc.

<!-- 来源页 1502 -->
Parameter
Description
Type
Size
Default
Option
Description
posture
Posture report.
coverage
Coverage report.
optimization
Optimization report
any
Any report.
serial
Fabric connector serial number.
var-string
Maximum
length: 255
stitch-name
Triggering stitch name.
string
Maximum
length: 35
trigger-datetime
Trigger date and time (YYYY-MM-DD HH:MM:SS).
datetime
Not
Specified
0000-00-00
00:00:00
trigger-day
Day within a month to trigger.
integer
Minimum
value: 1
Maximum
value: 31
1
trigger-frequency
Scheduled trigger frequency (default = daily).
option
-daily
Option
Description
hourly
Run hourly.
daily
Run daily.
weekly
Run weekly.
monthly
Run monthly.
once
Run once at specified date time.
trigger-hour
Hour of the day on which to trigger (0 - 23, default
= 1).
integer
Minimum
value: 0
Maximum
value: 23
0
trigger-minute
Minute of the hour on which to trigger (0 - 59,
default = 0).
integer
Minimum
value: 0
Maximum
value: 59
0
trigger-type
Trigger type.
option
-event-based
FortiOS 8.0.0 CLI Reference
1502
Fortinet Inc.

---


<!-- 来源页 1520 -->
Parameter
Description
Type
Size
Default
Option
Description
3g|5g
connect to 3G and 5G network only.
5g
connect to 5G network only, for networks use MIMO/mm waves
technology. Applies to 5G Standalone(SA) networks.
4g
connect to 4G network only, for networks use LTE technology.
3g
connect to 3G network only, for networks use WCDMA technology
sim-data-plan
data plan for SIM.
string
Maximum
length: 35
sim-pin
PIN code for SIM(if applicable).
password
Not
Specified
status
Enable/disable Modem online mode.
option
-online
Option
Description
online
set modem to online mode.
low-power
set modem to persistant low power mode.(no RF signal)
config system central-management
Configure central management.
config system central-management
Description: Configure central management.
set allow-monitor [enable|disable]
set allow-push-configuration [enable|disable]
set allow-push-firmware [enable|disable]
set allow-remote-firmware-upgrade [enable|disable]
set allow-remote-lte-firmware-upgrade [enable|disable]
set allow-remote-modem-firmware-upgrade [enable|disable]
set ca-cert {user}
set enc-algorithm [default|high|...]
set fmg {user}
set fmg-source-ip {ipv4-address}
set fmg-source-ip6 {ipv6-address}
set fmg-update-http-header [enable|disable]
set fmg-update-port [8890|443]
set fortigate-cloud-sso-default-profile {string}
set include-default-servers [enable|disable]
set interface {string}
set interface-select-method [auto|sdwan|...]
set local-cert {string}
set ltefw-upgrade-frequency [everyHour|every12hour|...]
FortiOS 8.0.0 CLI Reference
1520
Fortinet Inc.

<!-- 来源页 1521 -->
set ltefw-upgrade-time {string}
set mode [normal|backup]
set modem-upgrade-frequency [everyHour|every12hour|...]
set modem-upgrade-time {string}
set schedule-config-restore [enable|disable]
set schedule-script-restore [enable|disable]
set serial-number {user}
config server-list
Description: Additional severs that the FortiGate can use for updates (for AV, IPS,
updates) and ratings (for web filter and antispam ratings) servers.
edit <id>
set addr-type [ipv4|ipv6|...]
set fqdn {string}
set server-address {ipv4-address}
set server-address6 {ipv6-address}
set server-type {option1}, {option2}, ...
next
end
set type [fortimanager|fortiguard|...]
set use-default-servers-as-main [enable|disable]
set vdom {string}
set vrf-select {integer}
end
config system central-management
Parameter
Description
Type
Size
Default
allow-monitor
Enable/disable allowing the central management
server to remotely monitor this FortiGate unit.
option
-enable
Option
Description
enable
Enable remote monitoring of device.
disable
Disable remote monitoring of device.
allow-push-configuration
Enable/disable allowing the central management
server to push configuration changes to this
FortiGate.
option
-enable
Option
Description
enable
Enable push configuration.
disable
Disable push configuration.
allow-push-firmware
Enable/disable allowing the central management
server to push firmware updates to this FortiGate.
option
-enable
FortiOS 8.0.0 CLI Reference
1521
Fortinet Inc.

<!-- 来源页 1522 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable push firmware.
disable
Disable push firmware.
allow-remote-firmware-upgrade
Enable/disable remotely upgrading the firmware
on this FortiGate from the central management
server.
option
-enable
Option
Description
enable
Enable remote firmware upgrade.
disable
Disable remote firmware upgrade.
allow-remote-lte-firmware-upgrade *
Enable/disable remotely upgrading the lte
firmware on this FortiGate from the central
management server.
option
-enable
Option
Description
enable
Enable remote lte firmware upgrade.
disable
Disable remote lte firmware upgrade.
allow-remote-modem-firmware-upgrade *
Enable/disable remotely upgrading the internal
cellular modem firmware on this FortiGate from
the central management server.
option
-enable
Option
Description
enable
Enable remote lte firmware upgrade.
disable
Disable remote lte firmware upgrade.
ca-cert
CA certificate to be used by FGFM protocol.
user
Not
Specified
enc-algorithm
Encryption strength for communications between
the FortiGate and central management.
option
-high
Option
Description
default
High strength algorithms and medium-strength 128-bit key length
algorithms.
high
128-bit and larger key length algorithms.
low
64-bit or 56-bit key length algorithms without export restrictions.
FortiOS 8.0.0 CLI Reference
1522
Fortinet Inc.

<!-- 来源页 1523 -->
Parameter
Description
Type
Size
Default
fmg
IP address or FQDN of the FortiManager.
user
Not
Specified
fmg-source-ip
IPv4 source address that this FortiGate uses
when communicating with FortiManager.
ipv4-address
Not
Specified
0.0.0.0
fmg-source-ip6
IPv6 source address that this FortiGate uses
when communicating with FortiManager.
ipv6-address
Not
Specified
::
fmg-update-http-header
Enable/disable inclusion of HTTP header in
update request.
option
-disable
Option
Description
enable
Enable inclusion of HTTP header in update request.
disable
Disable inclusion of HTTP header in update request.
fmg-update-port
Port used to communicate with FortiManager that
is acting as a FortiGuard update server.
option
-8890
Option
Description
8890
Use port 8890 to communicate with FortiManager that is acting as a
FortiGuard update server.
443
Use port 443 to communicate with FortiManager that is acting as a
FortiGuard update server.
fortigate-cloud-sso-default-profile
Override access profile. Permission is set to read-only without a FortiGate Cloud Central
Management license.
string
Maximum
length: 35
include-default-servers
Enable/disable inclusion of public FortiGuard
servers in the override server list.
option
-enable
Option
Description
enable
Enable inclusion of public FortiGuard servers in the override server list.
disable
Disable inclusion of public FortiGuard servers in the override server
list.
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
FortiOS 8.0.0 CLI Reference
1523
Fortinet Inc.

<!-- 来源页 1524 -->
Parameter
Description
Type
Size
Default
Option
Description
sdwan
Set outgoing interface by SD-WAN or policy routing rules.
specify
Set outgoing interface manually.
local-cert
Certificate to be used by FGFM protocol.
string
Maximum
length: 35
ltefw-upgrade-frequency *
Set LTE firmware auto pushdown frequency.
option
-Option
Description
everyHour
Auto check and pushdown LTE firmware every hour
every12hour
Auto check and pushdown LTE firmware every 12 hours
everyDay
Auto check and pushdown LTE firmware every day
everyWeek
Auto check and pushdown LTE firmware every week
ltefw-upgrade-time *
Schedule next LTE firmware upgrade time (Local
Time). Format: YYYY-MM-DD HH:MM:SS
string
Maximum
length: 35
mode
Central management mode.
option
-normal
Option
Description
normal
Manage and configure this FortiGate from FortiManager.
backup
Manage and configure this FortiGate locally and back up its
configuration to FortiManager.
modem-upgrade-frequency *
Set internal cellular modem firmware auto
pushdown frequency.
option
-Option
Description
everyHour
Auto check and pushdown internal cellular modem firmware every
hour
every12hour
Auto check and pushdown internal cellular modem firmware every 12
hours
everyDay
Auto check and pushdown internal cellular modem firmware every day
everyWeek
Auto check and pushdown internal cellular modem firmware every
week
FortiOS 8.0.0 CLI Reference
1524
Fortinet Inc.

<!-- 来源页 1525 -->
Parameter
Description
Type
Size
Default
modem-upgrade-time *
Schedule next internal cellular modem firmware
upgrade time (Local Time). Format: YYYY-MM-DD HH:MM:SS
string
Maximum
length: 35
schedule-config-restore
Enable/disable allowing the central management
server to restore the configuration of this
FortiGate.
option
-enable
Option
Description
enable
Enable scheduled configuration restore.
disable
Disable scheduled configuration restore.
schedule-script-restore
Enable/disable allowing the central management
server to restore the scripts stored on this
FortiGate.
option
-enable
Option
Description
enable
Enable scheduled script restore.
disable
Disable scheduled script restore.
serial-number
Serial number.
user
Not
Specified
type
Central management type.
option
-none
Option
Description
fortimanager
FortiManager.
fortiguard
Central management of this FortiGate using FortiCloud.
none
No central management.
use-default-servers-as-main *
Enable/disable use of the public FortiGuard
servers as main servers.
option
-disable
Option
Description
enable
Enable use of the public FortiGuard servers as main servers.
disable
Disable use of the public FortiGuard servers as main servers.
vdom
Virtual domain (VDOM) name to use when
communicating with FortiManager.
string
Maximum
length: 31
root
vrf-select
VRF ID used for connection to server.
integer
Minimum
value: 0
Maximum
value: 511
0
FortiOS 8.0.0 CLI Reference
1525
Fortinet Inc.

---


<!-- 来源页 1526 -->
* This parameter may not exist in some models.
config server-list
Parameter
Description
Type
Size
Default
addr-type
Indicate whether the FortiGate communicates
with the override server using an IPv4 address,
an IPv6 address or a FQDN.
option
-ipv4
Option
Description
ipv4
IPv4 address.
ipv6
IPv6 address.
fqdn
FQDN.
fqdn
FQDN address of override server.
string
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
server-address
IPv4 address of override server.
ipv4-address
Not Specified
0.0.0.0
server-address6
IPv6 address of override server.
ipv6-address
Not Specified
::
server-type
FortiGuard service type.
option
-Option
Description
update
AV and IPS update server.
rating
AV-query, web filter, and anti-spam rating server.
iotv-query
IoT vulnerability query server.
iot-collect
IoT device collection server.
iot-query
IoT device query server.
config system cloud-service
Configure system cloud service.
config system cloud-service
Description: Configure system cloud service.
edit <name>
FortiOS 8.0.0 CLI Reference
1526
Fortinet Inc.

---


<!-- 来源页 1527 -->
set gck-access-token-lifetime {integer}
set gck-keyid {string}
set gck-private-key {string}
set gck-service-account {string}
set traffic-vdom {string}
set vendor [unknown|google-cloud-kms]
next
end
config system cloud-service
Parameter
Description
Type
Size
Default
gck-access-token-lifetime
Lifetime of automatically generated access tokens
in minutes (default is 60 minutes).
integer
Minimum
value: 1
Maximum
value: 3600
60
gck-keyid
Key id, also referred as "kid".
string
Maximum
length: 127
gck-private-key
Service account private key in PEM format (e.g. "-----BEGIN PRIVATE KEY-----\ ...").
string
Maximum
length: 8191
gck-service-account
Service account (e.g. "account-id@sampledomain.com").
string
Maximum
length: 285
name
Name.
string
Maximum
length: 35
traffic-vdom
Vdom used to communicate with cloud service.
string
Maximum
length: 31
vendor
Cloud service vendor.
option
-unknown
Option
Description
unknown
Unknown type of cloud service vendor.
google-cloud-kms
Google Cloud KMS service.
config system console
Configure console.
config system console
Description: Configure console.
set fortiexplorer [enable|disable]
set login [enable|disable]
FortiOS 8.0.0 CLI Reference
1527
Fortinet Inc.

---


<!-- 来源页 1528 -->
set output [standard|more]
end
config system console
Parameter
Description
Type
Size
Default
fortiexplorer *
Enable/disable access for FortiExplorer.
option
-enable
Option
Description
enable
Enable FortiExplorer access.
disable
Disable FortiExplorer access.
login
Enable/disable serial console and FortiExplorer.
option
-enable
Option
Description
enable
Console login enable.
disable
Console login disable.
output
Console output mode.
option
-more
Option
Description
standard
Standard output.
more
More page output.
* This parameter may not exist in some models.
config system csf
Add this FortiGate to a Security Fabric or set up a new Security Fabric on this FortiGate.
config system csf
Description: Add this FortiGate to a Security Fabric or set up a new Security Fabric on this
FortiGate.
set accept-auth-by-cert [disable|enable]
set authorization-request-type [serial|certificate]
set autoclear-removed-shared-objects [enable|disable]
set certificate {string}
set configuration-sync [default|local]
set downstream-access [enable|disable]
set downstream-accprofile {string}
config fabric-connector
Description: Fabric connector configuration.
edit <serial>
FortiOS 8.0.0 CLI Reference
1528
Fortinet Inc.

<!-- 来源页 1529 -->
set accprofile {string}
set configuration-write-access [enable|disable]
set vdom <name1>, <name2>, ...
next
end
config fabric-datasource-exemption
Description: Disable the fabric datasource check on the tables when synchronizing them.
edit <name>
set status [enable|disable]
next
end
set fabric-object-change-auto-cascade [enable|disable]
set fabric-object-unification [default|local]
set fabric-workers {integer}
set file-mgmt [enable|disable]
set file-quota {integer}
set file-quota-warning {integer}
set forticloud-account-enforcement [enable|disable]
set group-name {string}
set group-password {password}
set legacy-authentication [disable|enable]
set log-unification [disable|enable]
set saml-configuration-sync [default|local]
config shared-objects
Description: Fabric-wide objects shared by non-root nodes.
edit <name>
config objects
Description: CMDB table entries.
edit <pathname>
config keys
Description: Keys of CMDB table entries.
edit <name>
next
end
next
end
set trusted-list-entry {string}
next
end
set source-ip {ipv4-address}
set status [enable|disable]
config trusted-list
Description: Pre-authorized and blocked security fabric nodes.
edit <name>
set action [accept|deny]
set ca {string}
set ca-fingerprint {string}
set cn {string}
set index {integer}
set role [downstream|upstream]
next
end
FortiOS 8.0.0 CLI Reference
1529
Fortinet Inc.

<!-- 来源页 1530 -->
set uid {string}
set upload-shared-objects [enable|disable]
set upstream {string}
set upstream-interface {string}
set upstream-interface-select-method [auto|sdwan|...]
set upstream-port {integer}
end
config system csf
Parameter
Description
Type
Size
Default
accept-auth-by-cert
Accept connections with unknown
certificates and ask admin for approval.
option
-enable
Option
Description
disable
Do not accept SSL connections with unknown certificates.
enable
Accept SSL connections without automatic certificate verification.
authorization-request-type
Authorization request type.
option
-certificate
**
Option
Description
serial
Request verification by serial number.
certificate
Request verification by certificate.
autoclear-removed-shared-objects
*
Control system behavior for deleted
shared objects.
option
-enable
Option
Description
enable
Enable automatic clearing of configuration related to deleted shared
objects.
disable
Disable automatic clearing of configuration related to deleted shared
objects.
certificate
Certificate.
string
Maximum
length: 35
Fortinet_
Factory **
configuration-sync
Configuration sync mode.
option
-default
FortiOS 8.0.0 CLI Reference
1530
Fortinet Inc.

<!-- 来源页 1531 -->
Parameter
Description
Type
Size
Default
Option
Description
default
Synchronize configuration for IPAM, FortiAnalyzer, FortiSandbox, and
Central Management to root node.
local
Do not synchronize configuration with root node.
downstream-access
Enable/disable downstream device access
to this device's configuration and data.
option
-disable
Option
Description
enable
Enable downstream device access to this device's configuration and
data.
disable
Disable downstream device access to this device's configuration and
data.
downstream-accprofile
Default access profile for requests from
downstream devices.
string
Maximum
length: 35
fabric-object-change-auto-cascade *
Enable/disable the cascade mode for
fabric objects datasource check.
option
-disable
Option
Description
enable
Enable the fabric datasource check cascade mode. This will change
all related datasource to be a fabric-enabled object when setting an
entry to fabric-enabled.
disable
Disable the fabric datasource check cascade mode. This will no
longer change all related datasource to be a fabric-enabled object
when setting an entry to fabric-enabled.
fabric-object-unification
Fabric CMDB Object Unification.
option
-default
Option
Description
default
Global CMDB objects will be synchronized in Security Fabric.
local
Global CMDB objects will not be synchronized to and from this device.
fabric-workers
Number of worker processes for Security
Fabric daemon.
integer
Minimum value:
1 Maximum
value: 4
2
file-mgmt
Enable/disable Security Fabric daemon file
management.
option
-enable
FortiOS 8.0.0 CLI Reference
1531
Fortinet Inc.

<!-- 来源页 1532 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable daemon file management.
disable
Disable daemon file management.
file-quota
Maximum amount of memory that can be
used by the daemon files (in bytes).
integer
Minimum value:
0 Maximum
value:
4294967295
0
file-quota-warning
Warn when the set percentage of quota
has been used.
integer
Minimum value:
1 Maximum
value: 99
90
forticloud-account-enforcement
Fabric FortiCloud account unification.
option
-enable
Option
Description
enable
Enable FortiCloud account ID matching for Security Fabric.
disable
Disable FortiCloud accound ID matching for Security Fabric.
group-name
Security Fabric group name. All FortiGates
in a Security Fabric must have the same
group name.
string
Maximum
length: 35
group-password
Security Fabric group password. For
legacy authentication, fabric members
must have the same group password.
password
Not Specified
legacy-authentication
Enable/disable legacy authentication.
option
-disable
Option
Description
disable
Do not accept legacy authentication requests.
enable
Accept legacy authentication requests.
log-unification
Enable/disable broadcast of discovery
messages for log unification.
option
-enable
Option
Description
disable
Disable broadcast of discovery messages for log unification.
enable
Enable broadcast of discovery messages for log unification.
FortiOS 8.0.0 CLI Reference
1532
Fortinet Inc.

<!-- 来源页 1533 -->
Parameter
Description
Type
Size
Default
saml-configuration-sync
SAML setting configuration
synchronization.
option
-default
Option
Description
default
SAML setting for fabric members is created by fabric root.
local
Do not apply SAML configuration generated by root.
source-ip
Source IP address for communication with
the upstream FortiGate.
ipv4-address
Not Specified
0.0.0.0
status
Enable/disable Security Fabric.
option
-disable
Option
Description
enable
Enable Security Fabric.
disable
Disable Security Fabric.
uid
Unique ID of the current CSF node
string
Maximum
length: 35
upload-shared-objects *
Configure uploading shared objects
entries to the tree.
option
-enable
Option
Description
enable
Enable sharing objects referenced in shared-object table within the
fabric tree.
disable
Disable sharing objects referenced in shared-object table within the
fabric tree.
upstream
IP/FQDN of the FortiGate upstream from
this FortiGate in the Security Fabric.
string
Maximum
length: 255
upstream-interface
Specify outgoing interface to reach server.
string
Maximum
length: 15
upstream-interface-select-method
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
FortiOS 8.0.0 CLI Reference
1533
Fortinet Inc.

<!-- 来源页 1534 -->
Parameter
Description
Type
Size
Default
upstream-port
The port number to use to communicate
with the FortiGate upstream from this
FortiGate in the Security Fabric (default =
8013).
integer
Minimum value:
1 Maximum
value: 65535
8013
* This parameter may not exist in some models.
** Values may differ between models.
config fabric-connector
Parameter
Description
Type
Size
Default
accprofile
Override access profile.
string
Maximum
length: 35
configuration-write-access
Enable/disable downstream device write access
to configuration.
option
-disable
Option
Description
enable
Enable downstream device write access to configuration.
disable
Disable downstream device write access to configuration.
serial
Serial.
string
Maximum
length: 19
vdom <name>
Virtual domains that the connector has access
to. If none are set, the connector will only have
access to the VDOM that it joins the Security
Fabric through.
Virtual domain name.
string
Maximum
length: 79
config fabric-datasource-exemption
Parameter
Description
Type
Size
Default
name
Name.
string
Maximum
length: 255
status
Enable/disable the fabric datasource check on the
target table.
option
-disable
Option
Description
enable
Enable fabric datasource check bypass on the table.
disable
Disable fabric datasource check bypass on the table.
FortiOS 8.0.0 CLI Reference
1534
Fortinet Inc.

<!-- 来源页 1535 -->
config shared-objects
Parameter
Description
Type
Size
Default
name
UID of the source device.
string
Maximum
length: 35
trusted-list-entry
Trusted list entry name.
string
Maximum
length: 35
config objects
Parameter
Description
Type
Size
Default
pathname
CMDB path and object name.
string
Maximum
length: 192
config keys
Parameter
Description
Type
Size
Default
name
key.
string
Maximum length:
79
config trusted-list
Parameter
Description
Type
Size
Default
action
Security fabric authorization action.
option
-accept
Option
Description
accept
Accept authorization request.
deny
Deny authorization request.
ca *
Name of a CA on the downstream's certificat
chain.
string
Maximum
length: 79
ca-fingerprint
*
SHA512 fingerprint of a CA on the downstream's
certificate chain.
string
Maximum
length: 191
cn *
Certificate CNs used by HA members.
string
Maximum
length: 64
index
Index of the downstream in tree.
integer
Minimum
value: 1
Maximum
value: 1025
**
0
FortiOS 8.0.0 CLI Reference
1535
Fortinet Inc.

---


<!-- 来源页 1539 -->
Parameter
Description
Type
Size
Default
ddns-username
DDNS user name.
string
Maximum
length: 64
ddns-zone
Zone of your domain name (for example,
DDNS.com).
string
Maximum
length: 64
ddnsid
DDNS ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
monitor-interface
<interface-name>
Monitored interface.
Interface name.
string
Maximum
length: 79
server-type
Address type of the DDNS server.
option
-ipv4
Option
Description
ipv4
Use IPv4 addressing.
ipv6
Use IPv6 addressing.
ssl-certificate
Name of local certificate for SSL
connections.
string
Maximum
length: 35
Fortinet_
Factory **
update-interval
DDNS update interval (60 - 2592000 sec,
0 means default).
integer
Minimum value:
60 Maximum
value:
2592000
0
use-public-ip
Enable/disable use of public IP address.
option
-disable
Option
Description
disable
Disable use of public IP address.
enable
Enable use of public IP address.
** Values may differ between models.
config system dedicated-mgmt
Configure dedicated management.
config system dedicated-mgmt
Description: Configure dedicated management.
set default-gateway {ipv4-address}
set dhcp-end-ip {ipv4-address}
set dhcp-netmask {ipv4-netmask}
FortiOS 8.0.0 CLI Reference
1539
Fortinet Inc.

---


<!-- 来源页 1591 -->
edit <id>
set ds {integer}
set priority [low|medium|...]
next
end
config system dscp-based-priority
Parameter
Description
Type
Size
Default
ds
DSCP(DiffServ) DS value (0 - 63).
integer
Minimum value:
0 Maximum
value: 63
0
id
Item ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
priority
DSCP based priority level.
option
-high
Option
Description
low
Low priority.
medium
Medium priority.
high
High priority.
config system email-server
Configure the email server used by the FortiGate various things. For example, for sending email messages to
users to support user authentication features.
config system email-server
Description: Configure the email server used by the FortiGate various things. For example, for
sending email messages to users to support user authentication features.
set authenticate [enable|disable]
set interface {string}
set interface-select-method [auto|sdwan|...]
set password {password}
set port {integer}
set security [none|starttls|...]
set server {string}
set source-ip {ipv4-address}
set source-ip6 {ipv6-address}
set ssl-min-proto-version [default|SSLv3|...]
set type {option}
set username {string}
FortiOS 8.0.0 CLI Reference
1591
Fortinet Inc.

<!-- 来源页 1592 -->
set validate-server [enable|disable]
set vrf-select {integer}
end
config system email-server
Parameter
Description
Type
Size
Default
authenticate
Enable/disable authentication.
option
-disable
Option
Description
enable
Enable authentication.
disable
Disable authentication.
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
password
SMTP server user password for authentication.
password
Not
Specified
port
SMTP server port.
integer
Minimum
value: 1
Maximum
value:
65535
25
security
Connection security used by the email server.
option
-none
Option
Description
none
None.
starttls
STARTTLS.
smtps
SSL/TLS.
server
SMTP server IP address or hostname.
string
Maximum
length: 63
source-ip
SMTP server IPv4 source IP.
ipv4-address
Not
Specified
0.0.0.0
FortiOS 8.0.0 CLI Reference
1592
Fortinet Inc.

---


<!-- 来源页 1612 -->
Parameter
Description
Type
Size
Default
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
Source IPv4 address used to communicate with
FortiData.
user
Not
Specified
status
Enable/disable FortiData.
option
-disable
Option
Description
disable
Disable FortiData.
enable
Enable FortiData.
vrf-select
VRF ID used for connection to server.
integer
Minimum
value: 0
Maximum
value: 511
0
config system fortiguard
Configure FortiGuard services.
config system fortiguard
Description: Configure FortiGuard services.
set FDS-license-expiring-days {integer}
set antispam-cache [enable|disable]
set antispam-cache-mpermille {integer}
set antispam-cache-ttl {integer}
set antispam-expiration {integer}
set antispam-force-off [enable|disable]
set antispam-license {integer}
set antispam-timeout {integer}
set anycast-sdns-server-ip {ipv4-address}
set anycast-sdns-server-port {integer}
set auto-firmware-upgrade [enable|disable]
set auto-firmware-upgrade-day {option1}, {option2}, ...
set auto-firmware-upgrade-delay {integer}
set auto-firmware-upgrade-end-hour {integer}
set auto-firmware-upgrade-start-hour {integer}
set auto-join-forticloud [enable|disable]
FortiOS 8.0.0 CLI Reference
1612
Fortinet Inc.

<!-- 来源页 1613 -->
set ddns-server-ip {ipv4-address}
set ddns-server-ip6 {ipv6-address}
set ddns-server-port {integer}
set fortiguard-anycast [enable|disable]
set fortiguard-anycast-source [fortinet|aws|...]
set interface {string}
set interface-select-method [auto|sdwan|...]
set load-balance-servers {integer}
set outbreak-prevention-cache [enable|disable]
set outbreak-prevention-cache-mpermille {integer}
set outbreak-prevention-cache-ttl {integer}
set outbreak-prevention-expiration {integer}
set outbreak-prevention-force-off [enable|disable]
set outbreak-prevention-license {integer}
set outbreak-prevention-timeout {integer}
set persistent-connection [enable|disable]
set port [8888|53|...]
set protocol [udp|http|...]
set proxy-fqdn-host [enable|disable]
set proxy-password {password}
set proxy-server-ip {string}
set proxy-server-port {integer}
set proxy-username {string}
set sandbox-inline-scan [enable|disable]
set sandbox-region {string}
set sdns-options {option1}, {option2}, ...
set sdns-server-ip {user}
set sdns-server-port {integer}
set service-account-id {string}
set source-ip {ipv4-address}
set source-ip6 {ipv6-address}
set subscribe-update-notification [enable|disable]
set update-build-proxy [enable|disable]
set update-dldb [enable|disable]
set update-extdb [enable|disable]
set update-ffdb [enable|disable]
set update-server-location [automatic|usa|...]
set update-uwdb [enable|disable]
set vdom {string}
set vrf-select {integer}
set webfilter-cache [enable|disable]
set webfilter-cache-ttl {integer}
set webfilter-expiration {integer}
set webfilter-force-off [enable|disable]
set webfilter-license {integer}
set webfilter-timeout {integer}
end
FortiOS 8.0.0 CLI Reference
1613
Fortinet Inc.

<!-- 来源页 1614 -->
config system fortiguard
Parameter
Description
Type
Size
Default
FDS-license-expiring-days
Threshold for number of days before
FortiGuard license expiration to generate
license expiring event log (1 - 100 days,
default = 15).
integer
Minimum value:
1 Maximum
value: 100
15
antispam-cache
Enable/disable FortiGuard antispam
request caching. Uses a small amount of
memory but improves performance.
option
-enable
Option
Description
enable
Enable FortiGuard antispam request caching.
disable
Disable FortiGuard antispam request caching.
antispam-cache-mpermille
Maximum permille of FortiGate memory
the antispam cache is allowed to use (1 -150).
integer
Minimum value:
1 Maximum
value: 150
1
antispam-cache-ttl
Time-to-live for antispam cache entries in
seconds (300 - 86400). Lower times
reduce the cache size. Higher times may
improve performance since the cache will
have more entries.
integer
Minimum value:
300 Maximum
value: 86400
1800
antispam-expiration
Expiration date of the FortiGuard antispam
contract. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
antispam-force-off
Enable/disable turning off the FortiGuard
antispam service.
option
-disable
Option
Description
enable
Turn off the FortiGuard antispam service.
disable
Allow the FortiGuard antispam service.
antispam-license
Interval of time between license checks
for the FortiGuard antispam contract.
Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
4294967295
antispam-timeout
Antispam query time out (1 - 30 sec,
default = 7).
integer
Minimum value:
1 Maximum
value: 30
7
FortiOS 8.0.0 CLI Reference
1614
Fortinet Inc.

<!-- 来源页 1615 -->
Parameter
Description
Type
Size
Default
anycast-sdns-server-ip
IP address of the FortiGuard anycast DNS
rating server.
ipv4-address
Not Specified
0.0.0.0
anycast-sdns-server-port
Port to connect to on the FortiGuard
anycast DNS rating server.
integer
Minimum value:
1 Maximum
value: 65535
853
auto-firmware-upgrade
Enable/disable automatic patch-level
firmware upgrade from FortiGuard. The
FortiGate unit searches for new patches
only in the same major and minor version.
Enabled by default for entry-level
FortiGates; see Automatic firmware
updates.
option
-enable
Option
Description
enable
Enable automatic patch-level firmware upgrade to latest version from
FortiGuard.
disable
Disable automatic patch-level firmware upgrade to latest version from
FortiGuard.
auto-firmware-upgrade-day
Allowed day(s) of the week to install an
automatic patch-level firmware upgrade
from FortiGuard (default is none). Disallow
any day of the week to use auto-firmware-upgrade-delay instead, which waits for
designated days before installing an
automatic patch-level firmware upgrade.
option
-Option
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
FortiOS 8.0.0 CLI Reference
1615
Fortinet Inc.

<!-- 来源页 1616 -->
Parameter
Description
Type
Size
Default
auto-firmware-upgrade-delay
Delay of day(s) before installing an
automatic patch-level firmware upgrade
from FortiGuard (default = 3). Set it 0 to
use auto-firmware-upgrade-day instead,
which selects allowed day(s) of the week
for installing an automatic patch-level
firmware upgrade.
integer
Minimum value:
0 Maximum
value: 14
3
auto-firmware-upgrade-end-hour
End time in the designated time window
for automatic patch-level firmware
upgrade from FortiGuard in 24 hour time
(0 ~ 23, default = 4). When the end time is
smaller than the start time, the end time is
interpreted as the next day. The actual
upgrade time is selected randomly within
the time window.
integer
Minimum value:
0 Maximum
value: 23
4
auto-firmware-upgrade-start-hour
Start time in the designated time window
for automatic patch-level firmware
upgrade from FortiGuard in 24 hour time
(0 ~ 23, default = 2). The actual upgrade
time is selected randomly within the time
window.
integer
Minimum value:
0 Maximum
value: 23
2 **
auto-join-forticloud *
Automatically connect to and login to
FortiCloud.
option
-enable
Option
Description
enable
Enable automatic connection and login to FortiCloud.
disable
Disable automatic connection and login to FortiCloud.
ddns-server-ip
IP address of the FortiDDNS server.
ipv4-address
Not Specified
0.0.0.0
ddns-server-ip6
IPv6 address of the FortiDDNS server.
ipv6-address
Not Specified
::
ddns-server-port
Port used to communicate with FortiDDNS
servers.
integer
Minimum value:
1 Maximum
value: 65535
443
fortiguard-anycast
Enable/disable use of FortiGuard's
Anycast network.
option
-enable
Option
Description
enable
Enable use of FortiGuard's Anycast network.
disable
Disable use of FortiGuard's Anycast network.
FortiOS 8.0.0 CLI Reference
1616
Fortinet Inc.

<!-- 来源页 1617 -->
Parameter
Description
Type
Size
Default
fortiguard-anycast-source
Configure which of Fortinet's servers to
provide FortiGuard services in
FortiGuard's anycast network. Default is
Fortinet.
option
-fortinet
Option
Description
fortinet
Use Fortinet's servers to provide FortiGuard services in FortiGuard's
anycast network.
aws
Use Fortinet's AWS servers to provide FortiGuard services in
FortiGuard's anycast network.
debug
Use Fortinet's internal test servers to provide FortiGuard services in
FortiGuard's anycast network.
interface
Specify outgoing interface to reach server.
string
Maximum
length: 15
interface-select-method
Specify how to select outgoing interface
to reach server.
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
load-balance-servers
Number of servers to alternate between
as first FortiGuard option.
integer
Minimum value:
1 Maximum
value: 255 **
5 **
outbreak-prevention-cache
Enable/disable FortiGuard Virus Outbreak
Prevention cache.
option
-enable
Option
Description
enable
Enable FortiGuard antivirus caching.
disable
Disable FortiGuard antivirus caching.
outbreak-prevention-cache-mpermille
Maximum permille of memory FortiGuard
Virus Outbreak Prevention cache can use
(1 - 150 permille, default = 1).
integer
Minimum value:
1 Maximum
value: 150
1
FortiOS 8.0.0 CLI Reference
1617
Fortinet Inc.

<!-- 来源页 1618 -->
Parameter
Description
Type
Size
Default
outbreak-prevention-cache-ttl
Time-to-live for FortiGuard Virus Outbreak
Prevention cache entries (300 - 86400
sec, default = 300).
integer
Minimum value:
300 Maximum
value: 86400
300
outbreak-prevention-expiration
Expiration date of FortiGuard Virus
Outbreak Prevention contract. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
outbreak-prevention-force-off
Turn off FortiGuard Virus Outbreak
Prevention service.
option
-disable
Option
Description
enable
Turn off FortiGuard antivirus service.
disable
Allow the FortiGuard antivirus service.
outbreak-prevention-license
Interval of time between license checks
for FortiGuard Virus Outbreak Prevention
contract. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
4294967295
outbreak-prevention-timeout
FortiGuard Virus Outbreak Prevention time
out (1 - 30 sec, default = 7).
integer
Minimum value:
1 Maximum
value: 30
7
persistent-connection
Enable/disable use of persistent
connection to receive update notification
from FortiGuard.
option
-disable
Option
Description
enable
Enable persistent connection to receive update notification from
FortiGuard.
disable
Disable persistent connection to receive update notification from
FortiGuard.
port
Port used to communicate with the
FortiGuard servers.
option
-443
Option
Description
8888
port 8888 for server communication.
53
port 53 for server communication.
80
port 80 for server communication.
443
port 443 for server communication.
FortiOS 8.0.0 CLI Reference
1618
Fortinet Inc.

<!-- 来源页 1619 -->
Parameter
Description
Type
Size
Default
protocol
Protocol used to communicate with the
FortiGuard servers.
option
-https
Option
Description
udp
UDP for server communication (for use by FortiGuard or FortiManager).
http
HTTP for server communication (for use only by FortiManager).
https
HTTPS for server communication (for use by FortiGuard or
FortiManager).
proxy-fqdn-host *
Enable/disable preference of the FQDN as
host header, if resolved by DNS, in the
CONNECT request to FortiGuard servers.
For use when the FortiGate unit is behind a
proxy server.
option
-enable
Option
Description
enable
Enable preference of the FQDN as host header, if resolved by DNS, in
the CONNECT request to FortiGuard servers.
disable
Disable preference of the FQDN as host header, if resolved by DNS, in
the CONNECT request to FortiGuard servers.
proxy-password
Proxy user password.
password
Not Specified
proxy-server-ip
Hostname or IPv4 address of the proxy
server.
string
Maximum
length: 63
proxy-server-port
Port used to communicate with the proxy
server.
integer
Minimum value:
0 Maximum
value: 65535
0
proxy-username
Proxy user name.
string
Maximum
length: 64
sandbox-inline-scan *
Enable/disable FortiCloud Sandbox inline-scan.
option
-disable
Option
Description
enable
Enable FortiCloud Sandbox inline scan.
disable
Disable FortiCloud Sandbox inline scan.
sandbox-region
FortiCloud Sandbox region.
string
Maximum
length: 63
sdns-options
Customization options for the FortiGuard
DNS service.
option
-FortiOS 8.0.0 CLI Reference
1619
Fortinet Inc.

<!-- 来源页 1620 -->
Parameter
Description
Type
Size
Default
Option
Description
include-question-section
Include DNS question section in the FortiGuard DNS setup message.
sdns-server-ip
IP address of the FortiGuard DNS rating
server.
user
Not Specified
sdns-server-port
Port to connect to on the FortiGuard DNS
rating server.
integer
Minimum value:
1 Maximum
value: 65535
53
service-account-id
Service account ID.
string
Maximum
length: 50
source-ip
Source IPv4 address used to
communicate with FortiGuard.
ipv4-address
Not Specified
0.0.0.0
source-ip6
Source IPv6 address used to
communicate with FortiGuard.
ipv6-address
Not Specified
::
subscribe-update-notification
Enable/disable subscription to receive
update notification from FortiGuard.
option
-disable
Option
Description
enable
Enable subscription to receive update notification from FortiGuard.
disable
Disable subscription to receive update notification from FortiGuard.
update-build-proxy
Enable/disable proxy dictionary rebuild.
option
-enable
Option
Description
enable
Enable proxy dictionary rebuild.
disable
Disable proxy dictionary rebuild.
update-dldb
Enable/disable DLP signature update.
option
-enable
Option
Description
enable
Enable DLP signature update.
disable
Disable DLP signature update.
update-extdb
Enable/disable external resource update.
option
-enable
FortiOS 8.0.0 CLI Reference
1620
Fortinet Inc.

<!-- 来源页 1621 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable external resource update.
disable
Disable external resource update.
update-ffdb
Enable/disable Internet Service Database
update.
option
-enable
Option
Description
enable
Enable Internet Service Database update.
disable
Disable Internet Service Database update.
update-server-location
Location from which to receive FortiGuard
updates.
option
-automatic
Option
Description
automatic
FortiGuard servers chosen based on closest proximity to FortiGate unit.
usa
FortiGuard servers in United States.
eu
FortiGuard servers in the European Union.
update-uwdb
Enable/disable allowlist update.
option
-enable
Option
Description
enable
Enable allowlist update.
disable
Disable allowlist update.
vdom
FortiGuard Service virtual domain name.
string
Maximum
length: 31
vrf-select
VRF ID used for connection to server.
integer
Minimum value:
0 Maximum
value: 511
0
webfilter-cache
Enable/disable FortiGuard web filter
caching.
option
-enable
Option
Description
enable
Enable FortiGuard web filter caching.
disable
Disable FortiGuard web filter caching.
FortiOS 8.0.0 CLI Reference
1621
Fortinet Inc.

<!-- 来源页 1622 -->
Parameter
Description
Type
Size
Default
webfilter-cache-ttl
Time-to-live for web filter cache entries in
seconds (300 - 86400).
integer
Minimum value:
300 Maximum
value: 86400
3600
webfilter-expiration
Expiration date of the FortiGuard web filter
contract. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
webfilter-force-off
Enable/disable turning off the FortiGuard
web filtering service.
option
-disable
Option
Description
enable
Turn off the FortiGuard web filtering service.
disable
Allow the FortiGuard web filtering service to operate.
webfilter-license
Interval of time between license checks
for the FortiGuard web filter contract.
Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
4294967295
webfilter-timeout
Web filter query time out (1 - 30 sec,
default = 15).
integer
Minimum value:
1 Maximum
value: 30
15
* This parameter may not exist in some models.
** Values may differ between models.
FortiOS 8.0.0 CLI Reference
1622
Fortinet Inc.

---


<!-- 来源页 1626 -->
Parameter
Description
Type
Size
Default
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
Source IP address for communications to FortiNDR.
string
Maximum
length: 63
status
Enable/disable FortiNDR.
option
-disable
Option
Description
disable
Disable FortiNDR.
enable
Enable FortiNDR.
vrf-select
VRF ID used for connection to server.
integer
Minimum
value: 0
Maximum
value: 511
0
config system fortisandbox
Configure FortiSandbox.
config system fortisandbox
Description: Configure FortiSandbox.
edit <device>
set ca {string}
set certificate-verification [enable|disable]
set cn {string}
set cn-list <cn1>, <cn2>, ...
set default {option}
set email {string}
set enc-algorithm [default|high|...]
set forticloud [enable|disable]
set inline-scan [enable|disable]
set interface {string}
set interface-select-method [auto|sdwan|...]
set server {string}
set source-ip {string}
set ssl-min-proto-version [default|SSLv3|...]
set status [enable|disable]
FortiOS 8.0.0 CLI Reference
1626
Fortinet Inc.

<!-- 来源页 1627 -->
set vrf-select {integer}
next
end
config system fortisandbox
Parameter
Description
Type
Size
Default
ca
The CA that signs remote FortiSandbox certificate,
empty for no check.
string
Maximum
length: 79
certificate-verification
Enable/disable identity verification of FortiSandbox
by use of certificate.
option
-disable
Option
Description
enable
Enable identity verification of FortiSandbox by use of certificate.
disable
Disable identity verification of FortiSandbox by use of certificate.
cn *
The CN of remote server certificate, case sensitive,
empty for no check.
string
Maximum
length: 127
cn-list <cn> *
The CN list of remote server certificate, case
sensitive, empty for no check.
CN Name.
string
Maximum
length: 63
default *
Set as default FortiSandbox.
option
-Option
Description
enable
Default FortiSandbox.
device *
Device Name.
string
Maximum
length: 35
email
Notifier email address.
string
Maximum
length: 63
enc-algorithm
Configure the level of SSL protection for secure
communication with FortiSandbox.
option
-default
Option
Description
default
SSL communication with high and medium encryption algorithms.
high
SSL communication with high encryption algorithms.
low
SSL communication with low encryption algorithms.
forticloud *
Enable/disable FortiSandbox Cloud.
option
-disable
FortiOS 8.0.0 CLI Reference
1627
Fortinet Inc.

<!-- 来源页 1628 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable FortiSandbox Cloud.
disable
Disable FortiSandbox Cloud.
inline-scan *
Enable/disable FortiSandbox inline scan.
option
-disable
Option
Description
enable
Enable FortiSandbox inline scan.
disable
Disable FortiSandbox inline scan.
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
server
Server IP address or FQDN of the remote
FortiSandbox.
string
Maximum
length: 63
source-ip
Source IP address for communications to
FortiSandbox.
string
Maximum
length: 63
ssl-min-proto-version
Minimum supported protocol version for SSL/TLS
connections (default is to follow system global
setting).
option
-default
Option
Description
default
Follow system global setting.
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
status
Enable/disable FortiSandbox.
option
-disable
FortiOS 8.0.0 CLI Reference
1628
Fortinet Inc.

---


<!-- 来源页 1991 -->
Parameter
Description
Type
Size
Default
tags <name>
Tags.
Tag name.
string
Maximum
length: 79
config system password-policy
Configure password policy for locally defined administrator passwords and IPsec VPN pre-shared keys.
config system password-policy
Description: Configure password policy for locally defined administrator passwords and IPsec
VPN pre-shared keys.
set apply-to {option1}, {option2}, ...
set expire-day {integer}
set expire-status [enable|disable]
set login-lockout-upon-weaker-encryption [enable|disable]
set min-lower-case-letter {integer}
set min-non-alphanumeric {integer}
set min-number {integer}
set min-upper-case-letter {integer}
set minimum-length {integer}
set reuse-password [enable|disable]
set reuse-password-limit {integer}
set status [enable|disable]
end
config system password-policy
Parameter
Description
Type
Size
Default
apply-to
Apply password policy to administrator
passwords or IPsec pre-shared keys or both.
Separate entries with a space.
option
-admin-password
Option
Description
admin-password
Apply to administrator passwords.
ipsec-preshared-key
Apply to IPsec pre-shared keys.
expire-day
Number of days after which passwords expire (1
- 999 days, default = 90).
integer
Minimum
value: 1
Maximum
value: 999
90
expire-status
Enable/disable password expiration.
option
-disable
FortiOS 8.0.0 CLI Reference
1991
Fortinet Inc.

<!-- 来源页 1992 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Passwords expire after expire-day days.
disable
Passwords do not expire.
login-lockout-upon-weaker-encryption
Enable/disable administrative user login lockout
upon downgrade (default = disable). If enabled,
changing the FortiOS firmware to a version
where safer passwords are unsupported will
lock out administrative users.
option
-disable
Option
Description
enable
Enable administrative user login lockout upon downgrade.
disable
Disable administrative user login lockout upon downgrade.
min-lower-case-letter
Minimum number of lowercase characters in
password (0 - 128, default = 1).
integer
Minimum
value: 0
Maximum
value: 128
1
min-non-alphanumeric
Minimum number of non-alphanumeric
characters in password (0 - 128, default = 1).
integer
Minimum
value: 0
Maximum
value: 128
1
min-number
Minimum number of numeric characters in
password (0 - 128, default = 1).
integer
Minimum
value: 0
Maximum
value: 128
1
min-upper-case-letter
Minimum number of uppercase characters in
password (0 - 128, default = 1).
integer
Minimum
value: 0
Maximum
value: 128
1
minimum-length
Minimum password length (12 - 128, default =
12).
integer
Minimum
value: 12
Maximum
value: 128
12
reuse-password
Enable/disable reuse of password.
option
-enable
Option
Description
enable
Administrators are allowed to reuse the same password up to a limit.
disable
Administrators must create a new password.
FortiOS 8.0.0 CLI Reference
1992
Fortinet Inc.

---


<!-- 来源页 1993 -->
Parameter
Description
Type
Size
Default
reuse-password-limit
Number of times passwords can be reused (0 -20, default = 0. If set to 0, can reuse password
an unlimited number of times.).
integer
Minimum
value: 0
Maximum
value: 20
0
status
Enable/disable setting a password policy for
locally defined administrator passwords and
IPsec VPN pre-shared keys.
option
-enable
Option
Description
enable
Enable password policy.
disable
Disable password policy.
config system password-policy-guest-admin
Configure the password policy for guest administrators.
config system password-policy-guest-admin
Description: Configure the password policy for guest administrators.
set apply-to {option1}, {option2}, ...
set expire-day {integer}
set expire-status [enable|disable]
set min-lower-case-letter {integer}
set min-non-alphanumeric {integer}
set min-number {integer}
set min-upper-case-letter {integer}
set minimum-length {integer}
set reuse-password [enable|disable]
set reuse-password-limit {integer}
set status [enable|disable]
end
config system password-policy-guest-admin
Parameter
Description
Type
Size
Default
apply-to
Guest administrator to which this password
policy applies.
option
-guest-admin-password
Option
Description
guest-admin-password
Apply to guest administrator password.
FortiOS 8.0.0 CLI Reference
1993
Fortinet Inc.

<!-- 来源页 1994 -->
Parameter
Description
Type
Size
Default
expire-day
Number of days after which passwords expire (1
- 999 days, default = 90).
integer
Minimum
value: 1
Maximum
value: 999
90
expire-status
Enable/disable password expiration.
option
-disable
Option
Description
enable
Passwords expire after expire-day days.
disable
Passwords do not expire.
min-lower-case-letter
Minimum number of lowercase characters in
password (0 - 128, default = 1).
integer
Minimum
value: 0
Maximum
value: 128
1
min-non-alphanumeric
Minimum number of non-alphanumeric
characters in password (0 - 128, default = 1).
integer
Minimum
value: 0
Maximum
value: 128
1
min-number
Minimum number of numeric characters in
password (0 - 128, default = 1).
integer
Minimum
value: 0
Maximum
value: 128
1
min-upper-case-letter
Minimum number of uppercase characters in
password (0 - 128, default = 1).
integer
Minimum
value: 0
Maximum
value: 128
1
minimum-length
Minimum password length (12 - 128, default =
12).
integer
Minimum
value: 12
Maximum
value: 128
12
reuse-password
Enable/disable reuse of password.
option
-enable
Option
Description
enable
Administrators are allowed to reuse the same password up to a limit.
disable
Administrators must create a new password.
reuse-password-limit
Number of times passwords can be reused (0 -20, default = 0. If set to 0, can reuse password
an unlimited number of times.).
integer
Minimum
value: 0
Maximum
value: 20
0
FortiOS 8.0.0 CLI Reference
1994
Fortinet Inc.

---


<!-- 来源页 2025 -->
Parameter
Description
Type
Size
Default
format
Format flag.
option
-none
Option
Description
none
No format type.
text
Text format.
html
HTML format.
header
Header flag.
option
-none
Option
Description
none
No header type.
http
HTTP
8bit
8 bit.
msg-type
Message type.
string
Maximum
length: 28
config system replacemsg-group
Configure replacement message groups.
config system replacemsg-group
Description: Configure replacement message groups.
edit <name>
config admin
Description: Replacement message table entries.
edit <msg-type>
set buffer {var-string}
set format [none|text|...]
set header [none|http|...]
next
end
config alertmail
Description: Replacement message table entries.
edit <msg-type>
set buffer {var-string}
set format [none|text|...]
set header [none|http|...]
next
end
config auth
Description: Replacement message table entries.
edit <msg-type>
set buffer {var-string}
FortiOS 8.0.0 CLI Reference
2025
Fortinet Inc.

<!-- 来源页 2026 -->
set format [none|text|...]
set header [none|http|...]
next
end
config automation
Description: Replacement message table entries.
edit <msg-type>
set buffer {var-string}
set format [none|text|...]
set header [none|http|...]
next
end
set comment {var-string}
config custom-message
Description: Replacement message table entries.
edit <msg-type>
set buffer {var-string}
set format [none|text|...]
set header [none|http|...]
next
end
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
config fortiguard-wf
Description: Replacement message table entries.
edit <msg-type>
set buffer {var-string}
set format [none|text|...]
set header [none|http|...]
next
end
config ftp
Description: Replacement message table entries.
edit <msg-type>
set buffer {var-string}
set format [none|text|...]
set header [none|http|...]
next
end
set group-type [default|utm|...]
config http
Description: Replacement message table entries.
edit <msg-type>
set buffer {var-string}
set format [none|text|...]
set header [none|http|...]
next
end
config icap
Description: Replacement message table entries.
edit <msg-type>
FortiOS 8.0.0 CLI Reference
2026
Fortinet Inc.

<!-- 来源页 2027 -->
set buffer {var-string}
set format [none|text|...]
set header [none|http|...]
next
end
config mail
Description: Replacement message table entries.
edit <msg-type>
set buffer {var-string}
set format [none|text|...]
set header [none|http|...]
next
end
config nac-quar
Description: Replacement message table entries.
edit <msg-type>
set buffer {var-string}
set format [none|text|...]
set header [none|http|...]
next
end
config spam
Description: Replacement message table entries.
edit <msg-type>
set buffer {var-string}
set format [none|text|...]
set header [none|http|...]
next
end
config sslvpn
Description: Replacement message table entries.
edit <msg-type>
set buffer {var-string}
set format [none|text|...]
set header [none|http|...]
next
end
config traffic-quota
Description: Replacement message table entries.
edit <msg-type>
set buffer {var-string}
set format [none|text|...]
set header [none|http|...]
next
end
config utm
Description: Replacement message table entries.
edit <msg-type>
set buffer {var-string}
set format [none|text|...]
set header [none|http|...]
next
FortiOS 8.0.0 CLI Reference
2027
Fortinet Inc.

<!-- 来源页 2028 -->
end
set uuid {uuid}
config webproxy
Description: Replacement message table entries.
edit <msg-type>
set buffer {var-string}
set format [none|text|...]
set header [none|http|...]
next
end
next
end
config system replacemsg-group
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
FortiOS 8.0.0 CLI Reference
2028
Fortinet Inc.

<!-- 来源页 2029 -->
Parameter
Description
Type
Size
Default
group-type
Group type.
option
-default
Option
Description
default
Per-vdom replacement messages.
utm
For use with UTM settings in firewall policies.
auth
For use with authentication pages in firewall policies.
name
Group name.
string
Maximum
length: 35
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be manually
reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
config admin
Parameter
Description
Type
Size
Default
buffer
Message string.
var-string
Maximum
length:
32768
format
Format flag.
option
-none
Option
Description
none
No format type.
text
Text format.
html
HTML format.
header
Header flag.
option
-none
Option
Description
none
No header type.
http
HTTP
8bit
8 bit.
msg-type
Message type.
string
Maximum
length: 28
FortiOS 8.0.0 CLI Reference
2029
Fortinet Inc.

<!-- 来源页 2030 -->
config alertmail
Parameter
Description
Type
Size
Default
buffer
Message string.
var-string
Maximum
length:
32768
format
Format flag.
option
-none
Option
Description
none
No format type.
text
Text format.
html
HTML format.
header
Header flag.
option
-none
Option
Description
none
No header type.
http
HTTP
8bit
8 bit.
msg-type
Message type.
string
Maximum
length: 28
config auth
Parameter
Description
Type
Size
Default
buffer
Message string.
var-string
Maximum
length:
32768
format
Format flag.
option
-none
Option
Description
none
No format type.
text
Text format.
html
HTML format.
header
Header flag.
option
-none
Option
Description
none
No header type.
FortiOS 8.0.0 CLI Reference
2030
Fortinet Inc.

<!-- 来源页 2031 -->
Parameter
Description
Type
Size
Default
Option
Description
http
HTTP
8bit
8 bit.
msg-type
Message type.
string
Maximum
length: 28
config automation
Parameter
Description
Type
Size
Default
buffer
Message string.
var-string
Maximum
length:
32768
format
Format flag.
option
-none
Option
Description
none
No format type.
text
Text format.
html
HTML format.
header
Header flag.
option
-none
Option
Description
none
No header type.
http
HTTP
8bit
8 bit.
msg-type
Message type.
string
Maximum
length: 28
config custom-message
Parameter
Description
Type
Size
Default
buffer
Message string.
var-string
Maximum
length:
32768
format
Format flag.
option
-none
FortiOS 8.0.0 CLI Reference
2031
Fortinet Inc.

<!-- 来源页 2032 -->
Parameter
Description
Type
Size
Default
Option
Description
none
No format type.
text
Text format.
html
HTML format.
header
Header flag.
option
-none
Option
Description
none
No header type.
http
HTTP
8bit
8 bit.
msg-type
Message type.
string
Maximum
length: 28
config fortiguard-wf
Parameter
Description
Type
Size
Default
buffer
Message string.
var-string
Maximum
length:
32768
format
Format flag.
option
-none
Option
Description
none
No format type.
text
Text format.
html
HTML format.
header
Header flag.
option
-none
Option
Description
none
No header type.
http
HTTP
8bit
8 bit.
msg-type
Message type.
string
Maximum
length: 28
FortiOS 8.0.0 CLI Reference
2032
Fortinet Inc.

<!-- 来源页 2033 -->
config ftp
Parameter
Description
Type
Size
Default
buffer
Message string.
var-string
Maximum
length:
32768
format
Format flag.
option
-none
Option
Description
none
No format type.
text
Text format.
html
HTML format.
header
Header flag.
option
-none
Option
Description
none
No header type.
http
HTTP
8bit
8 bit.
msg-type
Message type.
string
Maximum
length: 28
config http
Parameter
Description
Type
Size
Default
buffer
Message string.
var-string
Maximum
length:
32768
format
Format flag.
option
-none
Option
Description
none
No format type.
text
Text format.
html
HTML format.
header
Header flag.
option
-none
Option
Description
none
No header type.
FortiOS 8.0.0 CLI Reference
2033
Fortinet Inc.

<!-- 来源页 2034 -->
Parameter
Description
Type
Size
Default
Option
Description
http
HTTP
8bit
8 bit.
msg-type
Message type.
string
Maximum
length: 28
config icap
Parameter
Description
Type
Size
Default
buffer
Message string.
var-string
Maximum
length:
32768
format
Format flag.
option
-none
Option
Description
none
No format type.
text
Text format.
html
HTML format.
header
Header flag.
option
-none
Option
Description
none
No header type.
http
HTTP
8bit
8 bit.
msg-type
Message type.
string
Maximum
length: 28
config mail
Parameter
Description
Type
Size
Default
buffer
Message string.
var-string
Maximum
length:
32768
format
Format flag.
option
-none
FortiOS 8.0.0 CLI Reference
2034
Fortinet Inc.

<!-- 来源页 2035 -->
Parameter
Description
Type
Size
Default
Option
Description
none
No format type.
text
Text format.
html
HTML format.
header
Header flag.
option
-none
Option
Description
none
No header type.
http
HTTP
8bit
8 bit.
msg-type
Message type.
string
Maximum
length: 28
config nac-quar
Parameter
Description
Type
Size
Default
buffer
Message string.
var-string
Maximum
length:
32768
format
Format flag.
option
-none
Option
Description
none
No format type.
text
Text format.
html
HTML format.
header
Header flag.
option
-none
Option
Description
none
No header type.
http
HTTP
8bit
8 bit.
msg-type
Message type.
string
Maximum
length: 28
FortiOS 8.0.0 CLI Reference
2035
Fortinet Inc.

<!-- 来源页 2036 -->
config spam
Parameter
Description
Type
Size
Default
buffer
Message string.
var-string
Maximum
length:
32768
format
Format flag.
option
-none
Option
Description
none
No format type.
text
Text format.
html
HTML format.
header
Header flag.
option
-none
Option
Description
none
No header type.
http
HTTP
8bit
8 bit.
msg-type
Message type.
string
Maximum
length: 28
config sslvpn
Parameter
Description
Type
Size
Default
buffer
Message string.
var-string
Maximum
length:
32768
format
Format flag.
option
-none
Option
Description
none
No format type.
text
Text format.
html
HTML format.
header
Header flag.
option
-none
Option
Description
none
No header type.
FortiOS 8.0.0 CLI Reference
2036
Fortinet Inc.

<!-- 来源页 2037 -->
Parameter
Description
Type
Size
Default
Option
Description
http
HTTP
8bit
8 bit.
msg-type
Message type.
string
Maximum
length: 28
config traffic-quota
Parameter
Description
Type
Size
Default
buffer
Message string.
var-string
Maximum
length:
32768
format
Format flag.
option
-none
Option
Description
none
No format type.
text
Text format.
html
HTML format.
header
Header flag.
option
-none
Option
Description
none
No header type.
http
HTTP
8bit
8 bit.
msg-type
Message type.
string
Maximum
length: 28
config utm
Parameter
Description
Type
Size
Default
buffer
Message string.
var-string
Maximum
length:
32768
format
Format flag.
option
-none
FortiOS 8.0.0 CLI Reference
2037
Fortinet Inc.

<!-- 来源页 2038 -->
Parameter
Description
Type
Size
Default
Option
Description
none
No format type.
text
Text format.
html
HTML format.
header
Header flag.
option
-none
Option
Description
none
No header type.
http
HTTP
8bit
8 bit.
msg-type
Message type.
string
Maximum
length: 28
config webproxy
Parameter
Description
Type
Size
Default
buffer
Message string.
var-string
Maximum
length:
32768
format
Format flag.
option
-none
Option
Description
none
No format type.
text
Text format.
html
HTML format.
header
Header flag.
option
-none
Option
Description
none
No header type.
http
HTTP
8bit
8 bit.
msg-type
Message type.
string
Maximum
length: 28
FortiOS 8.0.0 CLI Reference
2038
Fortinet Inc.

---


<!-- 来源页 2039 -->
config system replacemsg-image
Configure replacement message images.
config system replacemsg-image
Description: Configure replacement message images.
edit <name>
set image-base64 {var-string}
set image-type [gif|jpg|...]
next
end
config system replacemsg-image
Parameter
Description
Type
Size
Default
image-base64
Image data.
var-string
Maximum
length:
32768
image-type
Image type.
option
-png
Option
Description
gif
GIF image.
jpg
JPEG image.
tiff
TIFF image.
png
PNG image.
name
Image name.
string
Maximum
length: 23
config system resource-limits
Configure resource limits.
config system resource-limits
Description: Configure resource limits.
set custom-service {integer}
set dialup-tunnel {integer}
set firewall-address {integer}
set firewall-addrgrp {integer}
set firewall-policy {integer}
set ipsec-phase1 {integer}
set ipsec-phase1-interface {integer}
set ipsec-phase2 {integer}
FortiOS 8.0.0 CLI Reference
2039
Fortinet Inc.

<!-- 来源页 2040 -->
set ipsec-phase2-interface {integer}
set log-disk-quota {integer}
set onetime-schedule {integer}
set proxy {integer}
set recurring-schedule {integer}
set service-group {integer}
set session {integer}
set sslvpn {integer}
set user {integer}
set user-group {integer}
end
config system resource-limits
Parameter
Description
Type
Size
Default
custom-service
Maximum number of firewall custom services.
integer
Minimum value:
0 Maximum
value:
4294967295
dialup-tunnel
Maximum number of dial-up tunnels.
integer
Minimum value:
0 Maximum
value:
4294967295
firewall-address
Maximum number of firewall addresses (IPv4,
IPv6, multicast).
integer
Minimum value:
0 Maximum
value:
4294967295
firewall-addrgrp
Maximum number of firewall address groups
(IPv4, IPv6).
integer
Minimum value:
0 Maximum
value:
4294967295
firewall-policy
Maximum number of firewall policies (policy,
DoS-policy4, DoS-policy6, multicast).
integer
Minimum value:
0 Maximum
value:
4294967295
ipsec-phase1
Maximum number of VPN IPsec phase1 tunnels.
integer
Minimum value:
0 Maximum
value:
4294967295
ipsec-phase1-interface
Maximum number of VPN IPsec phase1 interface
tunnels.
integer
Minimum value:
0 Maximum
value:
4294967295
FortiOS 8.0.0 CLI Reference
2040
Fortinet Inc.

<!-- 来源页 2041 -->
Parameter
Description
Type
Size
Default
ipsec-phase2
Maximum number of VPN IPsec phase2 tunnels.
integer
Minimum value:
0 Maximum
value:
4294967295
ipsec-phase2-interface
Maximum number of VPN IPsec phase2 interface
tunnels.
integer
Minimum value:
0 Maximum
value:
4294967295
log-disk-quota
Log disk quota in megabytes (MB).
integer
Minimum value:
0 Maximum
value:
4294967295
**
0
onetime-schedule
Maximum number of firewall one-time
schedules.
integer
Minimum value:
0 Maximum
value:
4294967295
proxy *
Maximum number of concurrent proxy users.
integer
Minimum value:
0 Maximum
value:
4294967295
recurring-schedule
Maximum number of firewall recurring
schedules.
integer
Minimum value:
0 Maximum
value:
4294967295
service-group
Maximum number of firewall service groups.
integer
Minimum value:
0 Maximum
value:
4294967295
session
Maximum number of sessions.
integer
Minimum value:
0 Maximum
value:
4294967295
sslvpn *
Maximum number of Agentless VPN.
integer
Minimum value:
0 Maximum
value:
4294967295
user
Maximum number of local users.
integer
Minimum value:
0 Maximum
value:
4294967295
FortiOS 8.0.0 CLI Reference
2041
Fortinet Inc.

---


<!-- 来源页 2042 -->
Parameter
Description
Type
Size
Default
user-group
Maximum number of user groups.
integer
Minimum value:
0 Maximum
value:
4294967295
* This parameter may not exist in some models.
** Values may differ between models.
config system saml
Global settings for SAML authentication.
config system saml
Description: Global settings for SAML authentication.
set binding-protocol [post|redirect]
set cert {string}
set default-login-page [normal|sso]
set default-profile {string}
set entity-id {string}
set idp-cert {string}
set idp-entity-id {string}
set idp-single-logout-url {string}
set idp-single-sign-on-url {string}
set life {integer}
set portal-url {string}
set require-signed-resp-and-asrt [enable|disable]
set role [identity-provider|service-provider]
set server-address {string}
config service-providers
Description: Authorized service providers.
edit <name>
config assertion-attributes
Description: Customized SAML attributes to send along with assertion.
edit <name>
set type [username|email|...]
next
end
set idp-entity-id {string}
set idp-single-logout-url {string}
set idp-single-sign-on-url {string}
set prefix {string}
set sp-binding-protocol [post|redirect]
set sp-cert {string}
set sp-entity-id {string}
set sp-portal-url {string}
set sp-single-logout-url {string}
set sp-single-sign-on-url {string}
next
FortiOS 8.0.0 CLI Reference
2042
Fortinet Inc.

<!-- 来源页 2043 -->
end
set single-logout-url {string}
set single-sign-on-url {string}
set status [enable|disable]
set tolerance {integer}
end
config system saml
Parameter
Description
Type
Size
Default
binding-protocol
IdP Binding protocol.
option
-redirect
Option
Description
post
HTTP POST binding.
redirect
HTTP Redirect binding.
cert
Certificate to sign SAML messages.
string
Maximum
length: 35
default-login-page
Choose default login page.
option
-normal
Option
Description
normal
Use local login page as default.
sso
Use IdP's Single Sign-On page as default.
default-profile
Default profile for new SSO admin.
string
Maximum
length: 35
entity-id
SP entity ID.
string
Maximum
length: 255
idp-cert
IDP certificate name.
string
Maximum
length: 35
idp-entity-id
IDP entity ID.
string
Maximum
length: 255
idp-single-logout-url
IDP single logout URL.
string
Maximum
length: 255
idp-single-sign-on-url
IDP single sign-on URL.
string
Maximum
length: 255
FortiOS 8.0.0 CLI Reference
2043
Fortinet Inc.

<!-- 来源页 2044 -->
Parameter
Description
Type
Size
Default
life
Length of the range of time when the assertion is
valid (in minutes).
integer
Minimum value:
0 Maximum
value:
4294967295
30
portal-url
SP portal URL. Read-only.
string
Maximum
length: 255
require-signed-resp-and-asrt
Require both response and assertion from IDP to
be signed when FGT acts as SP (default =
disable).
option
-disable
Option
Description
enable
Both response and assertion must be signed and valid.
disable
At least one of response or assertion must be signed and valid.
role
SAML role.
option
-service-provider
Option
Description
identity-provider
Identity Provider.
service-provider
Service Provider.
server-address
Server address.
string
Maximum
length: 63
single-logout-url
SP single logout URL. Read-only.
string
Maximum
length: 255
single-sign-on-url
SP single sign-on URL. Read-only.
string
Maximum
length: 255
status
Enable/disable SAML authentication (default =
disable).
option
-disable
Option
Description
enable
Enable SAML authentication.
disable
Disable SAML authentication.
tolerance
Tolerance to the range of time when the
assertion is valid (in minutes).
integer
Minimum value:
0 Maximum
value:
4294967295
5
FortiOS 8.0.0 CLI Reference
2044
Fortinet Inc.

<!-- 来源页 2045 -->
config service-providers
Parameter
Description
Type
Size
Default
idp-entity-id
IDP entity ID. Read-only.
string
Maximum
length: 255
idp-single-logout-url
IDP single logout URL. Read-only.
string
Maximum
length: 255
idp-single-sign-on-url
IDP single sign-on URL. Read-only.
string
Maximum
length: 255
name
Name.
string
Maximum
length: 35
prefix
Prefix.
string
Maximum
length: 35
sp-binding-protocol
SP binding protocol.
option
-post
Option
Description
post
HTTP POST binding.
redirect
HTTP Redirect binding.
sp-cert
SP certificate name.
string
Maximum
length: 35
sp-entity-id
SP entity ID.
string
Maximum
length: 255
sp-portal-url
SP portal URL.
string
Maximum
length: 255
sp-single-logout-url
SP single logout URL.
string
Maximum
length: 255
sp-single-sign-on-url
SP single sign-on URL.
string
Maximum
length: 255
config assertion-attributes
Parameter
Description
Type
Size
Default
name
Name.
string
Maximum
length: 35
type
Type.
option
-username
FortiOS 8.0.0 CLI Reference
2045
Fortinet Inc.

---


<!-- 来源页 2126 -->
config system smc-ntp
Parameter
Description
Type
Size
Default
channel
SMC NTP client will send NTP packets through this
channel.
integer
Minimum
value: 1
Maximum
value:
65535
5
ntpsync
Enable/disable setting the FortiGate SMC system
time by synchronizing with an NTP server.
option
-disable
Option
Description
enable
Enable synchronization with NTP server in SMC.
disable
Disable synchronization with NTP server in SMC.
syncinterval
SMC NTP synchronization interval (1 - 65535
secs).
integer
Minimum
value: 1
Maximum
value:
65535
60
config ntpserver
Parameter
Description
Type
Size
Default
id
NTP server ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
server
IP address of the NTP server.
ipv4-address
Not Specified
0.0.0.0
config system sms-server
Configure SMS server for sending SMS messages to support user authentication.
config system sms-server
Description: Configure SMS server for sending SMS messages to support user authentication.
edit <name>
set mail-server {string}
next
end
FortiOS 8.0.0 CLI Reference
2126
Fortinet Inc.

---


<!-- 来源页 2158 -->
Parameter
Description
Type
Size
Default
Option
Description
hmac-sha2-256-etm@openssh.com
hmac-sha2-256-etm@openssh.com
hmac-sha2-512
hmac-sha2-512
hmac-sha2-512-etm@openssh.com
hmac-sha2-512-etm@openssh.com
hmac-ripemd160
hmac-ripemd160
hmac-ripemd160@openssh.com
hmac-ripemd160@openssh.com
hmac-ripemd160-etm@openssh.com
hmac-ripemd160-etm@openssh.com
umac-64@openssh.com
umac-64@openssh.com
umac-128@openssh.com
umac-128@openssh.com
umac-64-etm@openssh.com
umac-64-etm@openssh.com
umac-128-etm@openssh.com
umac-128-etm@openssh.com
** Values may differ between models.
config system sso-admin
Configure SSO admin users.
config system sso-admin
Description: Configure SSO admin users.
edit <name>
set accprofile {string}
set gui-custom-theme {string}
set gui-llm-provider [fortiai|openai]
set gui-theme [jade|neutrino|...]
set gui-theme-type [predefined|custom]
set openai-api-key {password-3}
set openai-api-key-part2 {password-3}
set openai-model {string}
set openai-org-id {string}
set openai-project-id {string}
set vdom <name1>, <name2>, ...
next
end
FortiOS 8.0.0 CLI Reference
2158
Fortinet Inc.

<!-- 来源页 2159 -->
config system sso-admin
Parameter
Description
Type
Size
Default
accprofile
SSO admin user access profile.
string
Maximum
length: 35
gui-custom-theme *
Custom theme that overrides the default
FortiGate theme.
string
Maximum
length: 35
gui-llm-provider *
Select the LLM provider.
option
-fortiai
Option
Description
fortiai
FortiAI.
openai
Use your own OpenAI API key.
gui-theme *
Predefined theme that overrides the default
FortiGate theme.
option
-none
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
none
No theme.
gui-theme-type *
Use predefined themes or custom themes.
option
-predefined
Option
Description
predefined
Use predefined theme.
custom
Use custom theme.
FortiOS 8.0.0 CLI Reference
2159
Fortinet Inc.

---


<!-- 来源页 2160 -->
Parameter
Description
Type
Size
Default
name
SSO admin name.
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
C௭௭**
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
config system sso-forticloud-admin
Configure FortiCloud SSO admin users.
config system sso-forticloud-admin
Description: Configure FortiCloud SSO admin users.
edit <name>
set accprofile {string}
set gui-custom-theme {string}
set gui-llm-provider [fortiai|openai]
set gui-theme [jade|neutrino|...]
set gui-theme-type [predefined|custom]
set openai-api-key {password-3}
set openai-api-key-part2 {password-3}
set openai-model {string}
set openai-org-id {string}
set openai-project-id {string}
set vdom <name1>, <name2>, ...
next
end
FortiOS 8.0.0 CLI Reference
2160
Fortinet Inc.

<!-- 来源页 2161 -->
config system sso-forticloud-admin
Parameter
Description
Type
Size
Default
accprofile
FortiCloud SSO admin user access profile.
Permission is set to read-only without a
FortiGate Cloud Central Management license.
string
Maximum
length: 35
gui-custom-theme *
Custom theme that overrides the default
FortiGate theme.
string
Maximum
length: 35
gui-llm-provider *
Select the LLM provider.
option
-fortiai
Option
Description
fortiai
FortiAI.
openai
Use your own OpenAI API key.
gui-theme *
Predefined theme that overrides the default
FortiGate theme.
option
-none
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
none
No theme.
gui-theme-type *
Use predefined themes or custom themes.
option
-predefined
Option
Description
predefined
Use predefined theme.
custom
Use custom theme.
FortiOS 8.0.0 CLI Reference
2161
Fortinet Inc.

---


<!-- 来源页 2162 -->
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
**
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
config system sso-fortigate-cloud-admin
Configure FortiCloud SSO admin users.
config system sso-fortigate-cloud-admin
Description: Configure FortiCloud SSO admin users.
edit <name>
set accprofile {string}
set gui-custom-theme {string}
set gui-llm-provider [fortiai|openai]
set gui-theme [jade|neutrino|...]
set gui-theme-type [predefined|custom]
set openai-api-key {password-3}
set openai-api-key-part2 {password-3}
set openai-model {string}
set openai-org-id {string}
set openai-project-id {string}
set vdom <name1>, <name2>, ...
next
end
FortiOS 8.0.0 CLI Reference
2162
Fortinet Inc.

<!-- 来源页 2163 -->
config system sso-fortigate-cloud-admin
Parameter
Description
Type
Size
Default
accprofile
FortiCloud SSO admin user access profile.
Permission is set to read-only without a
FortiGate Cloud Central Management license.
string
Maximum
length: 35
gui-custom-theme *
Custom theme that overrides the default
FortiGate theme.
string
Maximum
length: 35
gui-llm-provider *
Select the LLM provider.
option
-fortiai
Option
Description
fortiai
FortiAI.
openai
Use your own OpenAI API key.
gui-theme *
Predefined theme that overrides the default
FortiGate theme.
option
-none
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
none
No theme.
gui-theme-type *
Use predefined themes or custom themes.
option
-predefined
Option
Description
predefined
Use predefined theme.
custom
Use custom theme.
FortiOS 8.0.0 CLI Reference
2163
Fortinet Inc.

---


<!-- 来源页 2169 -->
config custom-service
Parameter
Description
Type
Size
Default
dst-port-range
Custom service destination port range.
user
Not Specified
0-0
id
Custom service ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
src-port-range
Custom service source port range.
user
Not Specified
0-0
config monitor-prefix
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
prefix
Prefix.
ipv4-classnet-any
Not Specified
0.0.0.0
0.0.0.0
vdom
VDOM name.
string
Maximum
length: 31
vrf
VRF ID.
integer
Minimum value:
0 Maximum
value: 511
0
config system storage
Configure logical storage.
config system storage
Description: Configure logical storage.
edit <name>
set device {string}
set media-status [enable|disable|...]
set order {integer}
set partition {string}
set size {integer}
set status [enable|disable]
set usage [log|wanopt|...]
set wanopt-mode [mix|wanopt|...]
FortiOS 8.0.0 CLI Reference
2169
Fortinet Inc.

<!-- 来源页 2170 -->
next
end
config system storage
Parameter
Description
Type
Size
Default
device
Partition device.
string
Maximum
length: 19
?
media-status
The physical status of current media.
option
-disable
Option
Description
enable
Storage is enabled.
disable
Storage is disabled.
fail
Storage have some fail sector.
name
Storage name.
string
Maximum
length: 35
default_n
order
Set storage order.
integer
Minimum value:
0 Maximum
value: 255
0
partition
Label of underlying partition.
string
Maximum
length: 16
<unknown>
size
Partition size.
integer
Minimum value:
0 Maximum
value:
4294967295
0
status
Enable/disable storage.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
usage *
Use hard disk for logging or WAN
Optimization (default = log).
option
-log **
Option
Description
log
Use hard disk for logging.
wanopt
Use hard disk for WAN Optimization.
mix
Use hard disk for logging and WAN Optimization.
FortiOS 8.0.0 CLI Reference
2170
Fortinet Inc.

---


<!-- 来源页 2175 -->
Parameter
Description
Type
Size
Default
type
Type of switch based on functionality: switch for
normal functionality, or hub to duplicate packets
to all port members.
option
-switch
Option
Description
switch
Switch for normal switch functionality (available in NAT mode only).
hub
Hub to duplicate packets to all member ports.
vdom
VDOM that the software switch belongs to.
string
Maximum
length: 31
config system theme
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
Configure custom gui themes.
config system theme
Description: Configure custom gui themes.
FortiOS 8.0.0 CLI Reference
2175
Fortinet Inc.

<!-- 来源页 2176 -->
edit <name>
set accent-color {string}
set banner-msg {string}
set banner-msg-severity [info|warning|...]
set base-theme [light|dark]
set border-radius [enable|disable]
set call-to-action-color {string}
set font [lato|inter]
set font-weight [light|standard]
set header-color {string}
set nav-color [light|dark|...]
set nav-style [standard|full-height]
set selected-color {string}
set table-style [fill|float]
set theme-template [jade|neutrino|...]
next
end
config system theme
Parameter
Description
Type
Size
Default
accent-color
Hexidecimal color code for the accent color.
string
Maximum
length: 7
banner-msg
Optional message to appear on the fortigate
header.
string
Maximum
length: 63
banner-msg-severity
Severity color of the banner message.
option
-info
Option
Description
info
Banner message on a blue background. Default severity.
warning
Banner message on a yellow background.
critical
Banner message on a red background.
base-theme
Base theme that will be used as a template.
option
-light
Option
Description
light
Light theme.
dark
Dark theme.
border-radius
Enable/disable border radius.
option
-disable
Option
Description
enable
Enable having curved borders for buttons and input fields.
FortiOS 8.0.0 CLI Reference
2176
Fortinet Inc.

<!-- 来源页 2177 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable having curved borders for buttons and input fields.
call-to-action-color
Hexidecimal color code for the call to action color.
string
Maximum
length: 7
font
Font family.
option
-lato
Option
Description
lato
Use the Lato font.
inter
Use the Inter font.
font-weight
Font weight.
option
-standard
Option
Description
light
Use a thin font-weight.
standard
Use a standard font-weight.
header-color
Hexidecimal color code for the header color.
string
Maximum
length: 7
name
Custom theme name.
string
Maximum
length: 35
nav-color
Color of the navigation bar.
option
-light
Option
Description
light
Light colored navigation bar.
dark
Dark colored navigation bar.
gray
Gray colored navigation bar.
nav-style
Navigation bar style.
option
-standard
Option
Description
standard
Use the standard navigation bar style.
full-height
Use the full-height navigation bar style.
selected-color
Hexidecimal color code for the selected color.
string
Maximum
length: 7
table-style
Table style.
option
-fill
FortiOS 8.0.0 CLI Reference
2177
Fortinet Inc.

---


<!-- 来源页 2178 -->
Parameter
Description
Type
Size
Default
Option
Description
fill
Tables will fill the available space.
float
Tables will be separated by a margin.
theme-template
Theme template that will be used in place of the
base theme.
option
-none
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
none
No theme template.
config system timezone
Show timezone. Read-only.
config system timezone
Description: Show timezone. Read-only.
edit <name>
next
end
config system timezone
Parameter
Description
Type
Size
Default
name
Database name of a timezone.
string
Maximum
length: 63
FortiOS 8.0.0 CLI Reference
2178
Fortinet Inc.
