# 日志 / 报表 / 监控 / 告警邮件

> 来源: FortiOS-8.0.0-CLI_Reference.pdf
> 覆盖命令/章节: log, report, monitoring, alertemail
> 本文件由 extract_pdf.py 从官方 PDF 自动提取，请勿手动编辑；
> 如需修正请修改 map.json 后重跑脚本。

---


<!-- 来源页 135 -->
alertemail
This section includes syntax for the following commands:
l config alertemail setting on page 135
config alertemail setting
Configure alert email settings.
config alertemail setting
Description: Configure alert email settings.
set FDS-license-expiring-warning [enable|disable]
set FDS-update-logs [enable|disable]
set FIPS-CC-errors [enable|disable]
set FSSO-disconnect-logs [enable|disable]
set HA-logs [enable|disable]
set IPS-logs [enable|disable]
set IPsec-errors-logs [enable|disable]
set PPP-errors-logs [enable|disable]
set admin-login-logs [enable|disable]
set alert-interval {integer}
set amc-interface-bypass-mode [enable|disable]
set antivirus-logs [enable|disable]
set configuration-changes-logs [enable|disable]
set critical-interval {integer}
set debug-interval {integer}
set email-interval {integer}
set emergency-interval {integer}
set error-interval {integer}
set filter-mode [category|threshold]
set firewall-authentication-failure-logs [enable|disable]
set fortiguard-log-quota-warning [enable|disable]
set information-interval {integer}
set local-disk-usage {integer}
set log-disk-usage-warning [enable|disable]
set mailto1 {string}
set mailto2 {string}
set mailto3 {string}
set notification-interval {integer}
set severity [emergency|alert|...]
set ssh-logs [enable|disable]
set sslvpn-authentication-errors-logs [enable|disable]
set username {string}
set violation-traffic-logs [enable|disable]
set warning-interval {integer}
FortiOS 8.0.0 CLI Reference
135
Fortinet Inc.

<!-- 来源页 136 -->
set webfilter-logs [enable|disable]
end
config alertemail setting
Parameter
Description
Type
Size
Default
FDS-license-expiring-warning
Enable/disable FortiGuard license expiration
warnings in alert email.
option
-disable
Option
Description
enable
Enable FortiGuard license expiration warnings in alert email.
disable
Disable FortiGuard license expiration warnings in alert email.
FDS-update-logs
Enable/disable FortiGuard update logs in alert
email.
option
-disable
Option
Description
enable
Enable FortiGuard update logs in alert email.
disable
Disable FortiGuard update logs in alert email.
FIPS-CC-errors
Enable/disable FIPS and Common Criteria error
logs in alert email.
option
-disable
Option
Description
enable
Enable FIPS and Common Criteria error logs in alert email.
disable
Disable FIPS and Common Criteria error logs in alert email.
FSSO-disconnect-logs
Enable/disable logging of FSSO collector agent
disconnect.
option
-disable
Option
Description
enable
Enable logging of FSSO collector agent disconnect.
disable
Disable logging of FSSO collector agent disconnect.
HA-logs
Enable/disable HA logs in alert email.
option
-disable
Option
Description
enable
Enable HA logs in alert email.
disable
Disable HA logs in alert email.
IPS-logs
Enable/disable IPS logs in alert email.
option
-disable
FortiOS 8.0.0 CLI Reference
136
Fortinet Inc.

<!-- 来源页 137 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable IPS logs in alert email.
disable
Disable IPS logs in alert email.
IPsec-errors-logs
Enable/disable IPsec error logs in alert email.
option
-disable
Option
Description
enable
Enable IPsec error logs in alert email.
disable
Disable IPsec error logs in alert email.
PPP-errors-logs
Enable/disable PPP error logs in alert email.
option
-disable
Option
Description
enable
Enable PPP error logs in alert email.
disable
Disable PPP error logs in alert email.
admin-login-logs
Enable/disable administrator login/logout logs
in alert email.
option
-disable
Option
Description
enable
Enable administrator login/logout logs in alert email.
disable
Disable administrator login/logout logs in alert email.
alert-interval
Alert alert interval in minutes.
integer
Minimum
value: 1
Maximum
value:
99999
2
amc-interface-bypass-mode
Enable/disable Fortinet Advanced Mezzanine
Card (AMC) interface bypass mode logs in alert
email.
option
-disable
Option
Description
enable
Enable Fortinet Advanced Mezzanine Card (AMC) interface bypass
mode logs in alert email.
disable
Disable Fortinet Advanced Mezzanine Card (AMC) interface bypass
mode logs in alert email.
antivirus-logs
Enable/disable antivirus logs in alert email.
option
-disable
FortiOS 8.0.0 CLI Reference
137
Fortinet Inc.

<!-- 来源页 138 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable antivirus logs in alert email.
disable
Disable antivirus logs in alert email.
configuration-changes-logs
Enable/disable configuration change logs in
alert email.
option
-disable
Option
Description
enable
Enable configuration change logs in alert email.
disable
Disable configuration change logs in alert email.
critical-interval
Critical alert interval in minutes.
integer
Minimum
value: 1
Maximum
value:
99999
3
debug-interval
Debug alert interval in minutes.
integer
Minimum
value: 1
Maximum
value:
99999
60
email-interval
Interval between sending alert emails (1 -99999 min, default = 5).
integer
Minimum
value: 1
Maximum
value:
99999
5
emergency-interval
Emergency alert interval in minutes.
integer
Minimum
value: 1
Maximum
value:
99999
1
error-interval
Error alert interval in minutes.
integer
Minimum
value: 1
Maximum
value:
99999
5
filter-mode
How to filter log messages that are sent to alert
emails.
option
-category
FortiOS 8.0.0 CLI Reference
138
Fortinet Inc.

<!-- 来源页 139 -->
Parameter
Description
Type
Size
Default
Option
Description
category
Filter based on category.
threshold
Filter based on severity.
firewall-authentication-failure-logs
Enable/disable firewall authentication failure
logs in alert email.
option
-disable
Option
Description
enable
Enable firewall authentication failure logs in alert email.
disable
Disable firewall authentication failure logs in alert email.
fortiguard-log-quota-warning
Enable/disable FortiCloud log quota warnings in
alert email.
option
-disable
Option
Description
enable
Enable FortiCloud log quota warnings in alert email.
disable
Disable FortiCloud log quota warnings in alert email.
information-interval
Information alert interval in minutes.
integer
Minimum
value: 1
Maximum
value:
99999
30
local-disk-usage
Disk usage percentage at which to send alert
email (1 - 99 percent, default = 75).
integer
Minimum
value: 1
Maximum
value: 99
75
log-disk-usage-warning
Enable/disable disk usage warnings in alert
email.
option
-disable
Option
Description
enable
Enable disk usage warnings in alert email.
disable
Disable disk usage warnings in alert email.
mailto1
Email address to send alert email to (usually a
system administrator) (max. 63 characters).
string
Maximum
length: 63
mailto2
Optional second email address to send alert
email to (max. 63 characters).
string
Maximum
length: 63
FortiOS 8.0.0 CLI Reference
139
Fortinet Inc.

<!-- 来源页 140 -->
Parameter
Description
Type
Size
Default
mailto3
Optional third email address to send alert email
to (max. 63 characters).
string
Maximum
length: 63
notification-interval
Notification alert interval in minutes.
integer
Minimum
value: 1
Maximum
value:
99999
20
severity
Lowest severity level to log.
option
-alert
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
ssh-logs
Enable/disable SSH logs in alert email.
option
-disable
Option
Description
enable
Enable SSH logs in alert email.
disable
Disable SSH logs in alert email.
sslvpn-authentication-errors-logs *
Enable/disable Agentless VPN authentication
error logs in alert email.
option
-disable
Option
Description
enable
Enable Agentless VPN authentication error logs in alert email.
disable
Disable Agentless VPN authentication error logs in alert email.
username
Name that appears in the From: field of alert
emails (max. 63 characters).
string
Maximum
length: 63
violation-traffic-logs
Enable/disable violation traffic logs in alert
email.
option
-disable
FortiOS 8.0.0 CLI Reference
140
Fortinet Inc.

<!-- 来源页 141 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable violation traffic logs in alert email.
disable
Disable violation traffic logs in alert email.
warning-interval
Warning alert interval in minutes.
integer
Minimum
value: 1
Maximum
value:
99999
10
webfilter-logs
Enable/disable web filter logs in alert email.
option
-disable
Option
Description
enable
Enable web filter logs in alert email.
disable
Disable web filter logs in alert email.
* This parameter may not exist in some models.
FortiOS 8.0.0 CLI Reference
141
Fortinet Inc.

---


<!-- 来源页 881 -->
log
This section includes syntax for the following commands:
l config log azure-security-center2 filter on page 890
l config log azure-security-center2 setting on page 895
l config log azure-security-center filter on page 883
l config log azure-security-center setting on page 888
l config log custom-field on page 896
l config log custom-format on page 898
l config log disk filter on page 900
l config log disk setting on page 904
l config log eventfilter on page 910
l config log fortianalyzer-cloud filter on page 964
l config log fortianalyzer-cloud override-filter on page 968
l config log fortianalyzer-cloud override-setting on page 972
l config log fortianalyzer-cloud setting on page 973
l config log fortianalyzer2 filter on page 930
l config log fortianalyzer2 override-filter on page 934
l config log fortianalyzer2 override-setting on page 938
l config log fortianalyzer2 setting on page 943
l config log fortianalyzer3 filter on page 947
l config log fortianalyzer3 override-filter on page 951
l config log fortianalyzer3 override-setting on page 955
l config log fortianalyzer3 setting on page 960
l config log fortianalyzer filter on page 914
l config log fortianalyzer override-filter on page 917
l config log fortianalyzer override-setting on page 921
l config log fortianalyzer setting on page 926
l config log fortiguard filter on page 977
l config log fortiguard override-filter on page 980
l config log fortiguard override-setting on page 984
l config log fortiguard setting on page 986
l config log gui-display on page 989
l config log memory filter on page 990
l config log memory global-setting on page 994
l config log memory setting on page 995
l config log null-device filter on page 995
l config log null-device setting on page 999
l config log setting on page 999
FortiOS 8.0.0 CLI Reference
881
Fortinet Inc.

<!-- 来源页 882 -->
l config log syslogd2 filter on page 1022
l config log syslogd2 override-filter on page 1026
l config log syslogd2 override-setting on page 1030
l config log syslogd2 setting on page 1034
l config log syslogd3 filter on page 1039
l config log syslogd3 override-filter on page 1043
l config log syslogd3 override-setting on page 1046
l config log syslogd3 setting on page 1051
l config log syslogd4 filter on page 1055
l config log syslogd4 override-filter on page 1059
l config log syslogd4 override-setting on page 1063
l config log syslogd4 setting on page 1067
l config log syslogd filter on page 1005
l config log syslogd override-filter on page 1009
l config log syslogd override-setting on page 1013
l config log syslogd setting on page 1018
l config log tacacs+accounting2 filter on page 1074
l config log tacacs+accounting2 setting on page 1075
l config log tacacs+accounting3 filter on page 1076
l config log tacacs+accounting3 setting on page 1077
l config log tacacs+accounting filter on page 1072
l config log tacacs+accounting setting on page 1073
l config log threat-weight on page 1079
l config log webtrends filter on page 1090
l config log webtrends setting on page 1094
FortiOS 8.0.0 CLI Reference
882
Fortinet Inc.

<!-- 来源页 883 -->
config log azure-security-center filter
This command is available for model(s): FortiGate-VM64 Azure.
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
91G, FortiGate-VM64 Aliyun, FortiGate-VM64 AWS, FortiGate-VM64 GCP, FortiGate-VM64 OPC,
FortiGate-VM64, FortiGateRugged 50G 5G, FortiGateRugged 60F 3G4G, FortiGateRugged 60F
Gen2, FortiGateRugged 70F 3G4G, FortiGateRugged 70F, FortiGateRugged 70G 5G Dual,
FortiGateRugged 70G, FortiWiFi 30G, FortiWiFi 31G, FortiWiFi 40F 3G4G, FortiWiFi 40F, FortiWiFi
50G 5G, FortiWiFi 50G DSL, FortiWiFi 50G SFP, FortiWiFi 50G, FortiWiFi 51G, FortiWiFi 60F, FortiWiFi
61F, FortiWiFi 70G-POE, FortiWiFi 70G, FortiWiFi 71G, FortiWiFi 80F 2R 3G4G DSL, FortiWiFi 80F 2R,
FortiWiFi 81F 2R 3G4G DSL, FortiWiFi 81F 2R 3G4G-POE, FortiWiFi 81F 2R-POE, FortiWiFi 81F 2R.
Filters for Azure Security Center.
config log azure-security-center filter
Description: Filters for Azure Security Center.
set anomaly [enable|disable]
set debug [enable|disable]
set forti-switch [enable|disable]
set forward-traffic [enable|disable]
config free-style
Description: Free style filters.
edit <id>
set category [traffic|event|...]
set filter {string}
set filter-type [include|exclude]
next
end
set gtp [enable|disable]
set http-transaction [enable|disable]
set local-traffic [enable|disable]
set multicast-traffic [enable|disable]
set severity [emergency|alert|...]
FortiOS 8.0.0 CLI Reference
883
Fortinet Inc.

<!-- 来源页 884 -->
set sniffer-traffic [enable|disable]
set voip [enable|disable]
set ztna-traffic [enable|disable]
end
config log azure-security-center filter
Parameter
Description
Type
Size
Default
anomaly
Enable/disable anomaly logging.
option
-enable
Option
Description
enable
Enable anomaly logging.
disable
Disable anomaly logging.
debug
Enable/disable debug logging.
option
-disable
Option
Description
enable
Enable Debug logging.
disable
Disable Debug logging.
forti-switch
Enable/disable Forti-Switch logging.
option
-enable
Option
Description
enable
Enable Forti-Switch logging.
disable
Disable Forti-Switch logging.
forward-traffic
Enable/disable forward traffic logging.
option
-enable
Option
Description
enable
Enable forward traffic logging.
disable
Disable forward traffic logging.
gtp
Enable/disable GTP messages logging.
option
-enable
Option
Description
enable
Enable GTP messages logging.
disable
Disable GTP messages logging.
http-transaction
Enable/disable log HTTP transaction messages.
option
-enable
FortiOS 8.0.0 CLI Reference
884
Fortinet Inc.

<!-- 来源页 885 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable http transaction logging.
disable
Disable http transaction logging.
local-traffic
Enable/disable local in or out traffic logging.
option
-enable
Option
Description
enable
Enable local in or out traffic logging.
disable
Disable local in or out traffic logging.
multicast-traffic
Enable/disable multicast traffic logging.
option
-enable
Option
Description
enable
Enable multicast traffic logging.
disable
Disable multicast traffic logging.
severity
Lowest severity level to log.
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
sniffer-traffic
Enable/disable sniffer traffic logging.
option
-enable
Option
Description
enable
Enable sniffer traffic logging.
disable
Disable sniffer traffic logging.
voip
Enable/disable VoIP logging.
option
-enable
FortiOS 8.0.0 CLI Reference
885
Fortinet Inc.

<!-- 来源页 886 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable VoIP logging.
disable
Disable VoIP logging.
ztna-traffic
Enable/disable ztna traffic logging.
option
-enable
Option
Description
enable
Enable ztna traffic logging.
disable
Disable ztna traffic logging.
config free-style
Parameter
Description
Type
Size
Default
category
Log category.
option
-traffic
Option
Description
traffic
Traffic log.
event
Event log.
virus
Antivirus log.
webfilter
Web filter log.
attack
Attack log.
spam
Antispam log.
anomaly
Anomaly log.
voip
VoIP log.
dlp
DLP log.
app-ctrl
Application control log.
waf
Web application firewall log.
gtp
GTP log.
dns
DNS detail log.
ssh
SSH log.
ssl
SSL log.
file-filter
File filter log.
icap
ICAP log.
FortiOS 8.0.0 CLI Reference
886
Fortinet Inc.

<!-- 来源页 887 -->
Parameter
Description
Type
Size
Default
Option
Description
virtual-patch
Virtual patch log.
debug
Debug log.
filter
Free style filter string.
string
Maximum
length: 1023
filter-type
Include/exclude logs that match the filter.
option
-include
Option
Description
include
Include logs that match the filter.
exclude
Exclude logs that match the filter.
id
Entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
FortiOS 8.0.0 CLI Reference
887
Fortinet Inc.

<!-- 来源页 888 -->
config log azure-security-center setting
This command is available for model(s): FortiGate-VM64 Azure.
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
91G, FortiGate-VM64 Aliyun, FortiGate-VM64 AWS, FortiGate-VM64 GCP, FortiGate-VM64 OPC,
FortiGate-VM64, FortiGateRugged 50G 5G, FortiGateRugged 60F 3G4G, FortiGateRugged 60F
Gen2, FortiGateRugged 70F 3G4G, FortiGateRugged 70F, FortiGateRugged 70G 5G Dual,
FortiGateRugged 70G, FortiWiFi 30G, FortiWiFi 31G, FortiWiFi 40F 3G4G, FortiWiFi 40F, FortiWiFi
50G 5G, FortiWiFi 50G DSL, FortiWiFi 50G SFP, FortiWiFi 50G, FortiWiFi 51G, FortiWiFi 60F, FortiWiFi
61F, FortiWiFi 70G-POE, FortiWiFi 70G, FortiWiFi 71G, FortiWiFi 80F 2R 3G4G DSL, FortiWiFi 80F 2R,
FortiWiFi 81F 2R 3G4G DSL, FortiWiFi 81F 2R 3G4G-POE, FortiWiFi 81F 2R-POE, FortiWiFi 81F 2R.
Settings for Azure Security Center.
config log azure-security-center setting
Description: Settings for Azure Security Center.
set appliance-id {string}
config custom-field-name
Description: Custom field name for CEF format logging.
edit <id>
set custom {string}
set name {string}
next
end
set eventhub-name {string}
set policy-name {string}
set policy-saskey {string}
set servicebus-namespace {string}
set status [enable|disable]
end
FortiOS 8.0.0 CLI Reference
888
Fortinet Inc.

<!-- 来源页 889 -->
config log azure-security-center setting
Parameter
Description
Type
Size
Default
appliance-id
Appliance ID.
string
Maximum
length: 128
eventhub-name
Event hub name.
string
Maximum
length: 128
policy-name
Policy name.
string
Maximum
length: 128
policy-saskey
Policy saskey.
string
Maximum
length: 128
servicebus-namespace
Service bus namespace.
string
Maximum
length: 128
status
Enable Azure Security Center logging.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
config custom-field-name
Parameter
Description
Type
Size
Default
custom
Field custom name [A-Za-z0-9_].
string
Maximum
length: 35
id
Entry ID.
integer
Minimum
value: 0
Maximum
value: 255
0
name
Field name [A-Za-z0-9_].
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
889
Fortinet Inc.

<!-- 来源页 890 -->
config log azure-security-center2 filter
This command is available for model(s): FortiGate-VM64 Azure.
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
91G, FortiGate-VM64 Aliyun, FortiGate-VM64 AWS, FortiGate-VM64 GCP, FortiGate-VM64 OPC,
FortiGate-VM64, FortiGateRugged 50G 5G, FortiGateRugged 60F 3G4G, FortiGateRugged 60F
Gen2, FortiGateRugged 70F 3G4G, FortiGateRugged 70F, FortiGateRugged 70G 5G Dual,
FortiGateRugged 70G, FortiWiFi 30G, FortiWiFi 31G, FortiWiFi 40F 3G4G, FortiWiFi 40F, FortiWiFi
50G 5G, FortiWiFi 50G DSL, FortiWiFi 50G SFP, FortiWiFi 50G, FortiWiFi 51G, FortiWiFi 60F, FortiWiFi
61F, FortiWiFi 70G-POE, FortiWiFi 70G, FortiWiFi 71G, FortiWiFi 80F 2R 3G4G DSL, FortiWiFi 80F 2R,
FortiWiFi 81F 2R 3G4G DSL, FortiWiFi 81F 2R 3G4G-POE, FortiWiFi 81F 2R-POE, FortiWiFi 81F 2R.
Filters for Azure Security Center.
config log azure-security-center2 filter
Description: Filters for Azure Security Center.
set anomaly [enable|disable]
set debug [enable|disable]
set forti-switch [enable|disable]
set forward-traffic [enable|disable]
config free-style
Description: Free style filters.
edit <id>
set category [traffic|event|...]
set filter {string}
set filter-type [include|exclude]
next
end
set gtp [enable|disable]
set http-transaction [enable|disable]
set local-traffic [enable|disable]
set multicast-traffic [enable|disable]
set severity [emergency|alert|...]
FortiOS 8.0.0 CLI Reference
890
Fortinet Inc.

<!-- 来源页 891 -->
set sniffer-traffic [enable|disable]
set voip [enable|disable]
set ztna-traffic [enable|disable]
end
config log azure-security-center2 filter
Parameter
Description
Type
Size
Default
anomaly
Enable/disable anomaly logging.
option
-enable
Option
Description
enable
Enable anomaly logging.
disable
Disable anomaly logging.
debug
Enable/disable debug logging.
option
-disable
Option
Description
enable
Enable Debug logging.
disable
Disable Debug logging.
forti-switch
Enable/disable Forti-Switch logging.
option
-enable
Option
Description
enable
Enable Forti-Switch logging.
disable
Disable Forti-Switch logging.
forward-traffic
Enable/disable forward traffic logging.
option
-enable
Option
Description
enable
Enable forward traffic logging.
disable
Disable forward traffic logging.
gtp
Enable/disable GTP messages logging.
option
-enable
Option
Description
enable
Enable GTP messages logging.
disable
Disable GTP messages logging.
http-transaction
Enable/disable log HTTP transaction messages.
option
-enable
FortiOS 8.0.0 CLI Reference
891
Fortinet Inc.

<!-- 来源页 892 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable http transaction logging.
disable
Disable http transaction logging.
local-traffic
Enable/disable local in or out traffic logging.
option
-enable
Option
Description
enable
Enable local in or out traffic logging.
disable
Disable local in or out traffic logging.
multicast-traffic
Enable/disable multicast traffic logging.
option
-enable
Option
Description
enable
Enable multicast traffic logging.
disable
Disable multicast traffic logging.
severity
Lowest severity level to log.
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
sniffer-traffic
Enable/disable sniffer traffic logging.
option
-enable
Option
Description
enable
Enable sniffer traffic logging.
disable
Disable sniffer traffic logging.
voip
Enable/disable VoIP logging.
option
-enable
FortiOS 8.0.0 CLI Reference
892
Fortinet Inc.

<!-- 来源页 893 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable VoIP logging.
disable
Disable VoIP logging.
ztna-traffic
Enable/disable ztna traffic logging.
option
-enable
Option
Description
enable
Enable ztna traffic logging.
disable
Disable ztna traffic logging.
config free-style
Parameter
Description
Type
Size
Default
category
Log category.
option
-traffic
Option
Description
traffic
Traffic log.
event
Event log.
virus
Antivirus log.
webfilter
Web filter log.
attack
Attack log.
spam
Antispam log.
anomaly
Anomaly log.
voip
VoIP log.
dlp
DLP log.
app-ctrl
Application control log.
waf
Web application firewall log.
gtp
GTP log.
dns
DNS detail log.
ssh
SSH log.
ssl
SSL log.
file-filter
File filter log.
icap
ICAP log.
FortiOS 8.0.0 CLI Reference
893
Fortinet Inc.

<!-- 来源页 894 -->
Parameter
Description
Type
Size
Default
Option
Description
virtual-patch
Virtual patch log.
debug
Debug log.
filter
Free style filter string.
string
Maximum
length: 1023
filter-type
Include/exclude logs that match the filter.
option
-include
Option
Description
include
Include logs that match the filter.
exclude
Exclude logs that match the filter.
id
Entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
FortiOS 8.0.0 CLI Reference
894
Fortinet Inc.

<!-- 来源页 895 -->
config log azure-security-center2 setting
This command is available for model(s): FortiGate-VM64 Azure.
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
91G, FortiGate-VM64 Aliyun, FortiGate-VM64 AWS, FortiGate-VM64 GCP, FortiGate-VM64 OPC,
FortiGate-VM64, FortiGateRugged 50G 5G, FortiGateRugged 60F 3G4G, FortiGateRugged 60F
Gen2, FortiGateRugged 70F 3G4G, FortiGateRugged 70F, FortiGateRugged 70G 5G Dual,
FortiGateRugged 70G, FortiWiFi 30G, FortiWiFi 31G, FortiWiFi 40F 3G4G, FortiWiFi 40F, FortiWiFi
50G 5G, FortiWiFi 50G DSL, FortiWiFi 50G SFP, FortiWiFi 50G, FortiWiFi 51G, FortiWiFi 60F, FortiWiFi
61F, FortiWiFi 70G-POE, FortiWiFi 70G, FortiWiFi 71G, FortiWiFi 80F 2R 3G4G DSL, FortiWiFi 80F 2R,
FortiWiFi 81F 2R 3G4G DSL, FortiWiFi 81F 2R 3G4G-POE, FortiWiFi 81F 2R-POE, FortiWiFi 81F 2R.
Settings for Azure Security Center.
config log azure-security-center2 setting
Description: Settings for Azure Security Center.
set appliance-id {string}
config custom-field-name
Description: Custom field name for CEF format logging.
edit <id>
set custom {string}
set name {string}
next
end
set eventhub-name {string}
set policy-name {string}
set policy-saskey {string}
set servicebus-namespace {string}
set status [enable|disable]
end
FortiOS 8.0.0 CLI Reference
895
Fortinet Inc.

<!-- 来源页 896 -->
config log azure-security-center2 setting
Parameter
Description
Type
Size
Default
appliance-id
Appliance ID.
string
Maximum
length: 128
eventhub-name
Event hub name.
string
Maximum
length: 128
policy-name
Policy name.
string
Maximum
length: 128
policy-saskey
Policy saskey.
string
Maximum
length: 128
servicebus-namespace
Service bus namespace.
string
Maximum
length: 128
status
Enable Azure Security Center logging.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
config custom-field-name
Parameter
Description
Type
Size
Default
custom
Field custom name [A-Za-z0-9_].
string
Maximum
length: 35
id
Entry ID.
integer
Minimum
value: 0
Maximum
value: 255
0
name
Field name [A-Za-z0-9_].
string
Maximum
length: 35
config log custom-field
Configure custom log fields.
config log custom-field
Description: Configure custom log fields.
edit <id>
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
FortiOS 8.0.0 CLI Reference
896
Fortinet Inc.

<!-- 来源页 897 -->
set fabric-object-source [member|local|...]
set name {string}
set uuid {uuid}
set value {string}
next
end
config log custom-field
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
id
Field ID string.
string
Maximum
length: 35
name
Field name (max: 15 characters).
string
Maximum
length: 15
FortiOS 8.0.0 CLI Reference
897
Fortinet Inc.

<!-- 来源页 898 -->
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
value
Field value (max: 15 characters).
string
Maximum
length: 15
* This parameter may not exist in some models.
config log custom-format
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
Configure custom log format.
config log custom-format
Description: Configure custom log format.
edit <name>
set empty-value-indicator {string}
set field-exclusion-list <field1>, <field2>, ...
config log-templates
FortiOS 8.0.0 CLI Reference
898
Fortinet Inc.

<!-- 来源页 899 -->
Description: Custom log templates.
edit <name>
set category [traffic|event|...]
set subtypes <subtype1>, <subtype2>, ...
set template {string}
next
end
next
end
config log custom-format
Parameter
Description
Type
Size
Default
empty-value-indicator
A character to indicate log field is empty.
string
Maximum
length: 1
field-exclusion-list
<field>
Log fields to exclude in the log.
Log field to exclude from formatting.
string
Maximum
length: 79
name
Format name string.
string
Maximum
length: 35
config log-templates
Parameter
Description
Type
Size
Default
category
Log category.
option
-traffic
Option
Description
traffic
Traffic log.
event
Event log.
virus
Antivirus log.
webfilter
Web filter log.
attack
Attack log.
spam
Antispam log.
anomaly
Anomaly log.
voip
VoIP log.
dlp
DLP log.
app-ctrl
Application control log.
waf
Web application firewall log.
FortiOS 8.0.0 CLI Reference
899
Fortinet Inc.

<!-- 来源页 900 -->
Parameter
Description
Type
Size
Default
Option
Description
dns
DNS detail log.
ssh
SSH log.
ssl
SSL log.
file-filter
File filter log.
icap
ICAP log.
virtual-patch
Virtual patch log.
debug
Debug log.
name
Template name string.
string
Maximum
length: 35
subtypes
<subtype>
Log subtypes to apply template to.
Log subtype.
string
Maximum
length: 79
template
Log template string.
string
Maximum
length:
2047
config log disk filter
Configure filters for local disk logging. Use these filters to determine the log messages to record according to
severity and type.
config log disk filter
Description: Configure filters for local disk logging. Use these filters to determine the log
messages to record according to severity and type.
set anomaly [enable|disable]
set debug [enable|disable]
set dlp-archive [enable|disable]
set forti-switch [enable|disable]
set forward-traffic [enable|disable]
config free-style
Description: Free style filters.
edit <id>
set category [traffic|event|...]
set filter {string}
set filter-type [include|exclude]
next
end
set gtp [enable|disable]
set http-transaction [enable|disable]
set local-traffic [enable|disable]
set multicast-traffic [enable|disable]
FortiOS 8.0.0 CLI Reference
900
Fortinet Inc.

<!-- 来源页 901 -->
set severity [emergency|alert|...]
set sniffer-traffic [enable|disable]
set voip [enable|disable]
set ztna-traffic [enable|disable]
end
config log disk filter
Parameter
Description
Type
Size
Default
anomaly *
Enable/disable anomaly logging.
option
-enable
Option
Description
enable
Enable anomaly logging.
disable
Disable anomaly logging.
debug *
Enable/disable debug logging.
option
-disable
Option
Description
enable
Enable Debug logging.
disable
Disable Debug logging.
dlp-archive *
Enable/disable DLP archive logging.
option
-enable
Option
Description
enable
Enable DLP archive logging.
disable
Disable DLP archive logging.
forti-switch *
Enable/disable Forti-Switch logging.
option
-enable
Option
Description
enable
Enable Forti-Switch logging.
disable
Disable Forti-Switch logging.
forward-traffic *
Enable/disable forward traffic logging.
option
-enable
Option
Description
enable
Enable forward traffic logging.
disable
Disable forward traffic logging.
gtp *
Enable/disable GTP messages logging.
option
-enable
FortiOS 8.0.0 CLI Reference
901
Fortinet Inc.

<!-- 来源页 902 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable GTP messages logging.
disable
Disable GTP messages logging.
http-transaction *
Enable/disable log HTTP transaction messages.
option
-enable
Option
Description
enable
Enable http transaction logging.
disable
Disable http transaction logging.
local-traffic *
Enable/disable local in or out traffic logging.
option
-enable
Option
Description
enable
Enable local in or out traffic logging.
disable
Disable local in or out traffic logging.
multicast-traffic *
Enable/disable multicast traffic logging.
option
-enable
Option
Description
enable
Enable multicast traffic logging.
disable
Disable multicast traffic logging.
severity
Log to disk every message above and including
this severity level.
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
FortiOS 8.0.0 CLI Reference
902
Fortinet Inc.

<!-- 来源页 903 -->
Parameter
Description
Type
Size
Default
sniffer-traffic
*
Enable/disable sniffer traffic logging.
option
-enable
Option
Description
enable
Enable sniffer traffic logging.
disable
Disable sniffer traffic logging.
voip *
Enable/disable VoIP logging.
option
-enable
Option
Description
enable
Enable VoIP logging.
disable
Disable VoIP logging.
ztna-traffic *
Enable/disable ztna traffic logging.
option
-enable
Option
Description
enable
Enable ztna traffic logging.
disable
Disable ztna traffic logging.
* This parameter may not exist in some models.
config free-style
Parameter
Description
Type
Size
Default
category
Log category.
option
-traffic **
Option
Description
traffic
Traffic log.
event
Event log.
virus
Antivirus log.
webfilter
Web filter log.
attack
Attack log.
spam
Antispam log.
anomaly
Anomaly log.
voip
VoIP log.
dlp
DLP log.
app-ctrl
Application control log.
FortiOS 8.0.0 CLI Reference
903
Fortinet Inc.

<!-- 来源页 904 -->
Parameter
Description
Type
Size
Default
Option
Description
waf
Web application firewall log.
dns
DNS detail log.
ssh
SSH log.
ssl
SSL log.
file-filter
File filter log.
icap
ICAP log.
virtual-patch
Virtual patch log.
debug
Debug log.
filter
Free style filter string.
string
Maximum
length: 1023
filter-type
Include/exclude logs that match the filter.
option
-include
Option
Description
include
Include logs that match the filter.
exclude
Exclude logs that match the filter.
id
Entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
** Values may differ between models.
config log disk setting
Settings for local disk logging.
config log disk setting
Description: Settings for local disk logging.
set diskfull [overwrite|nolog]
set dlp-archive-quota {integer}
set full-final-warning-threshold {integer}
set full-first-warning-threshold {integer}
set full-second-warning-threshold {integer}
set interface {string}
set interface-select-method [auto|sdwan|...]
set ips-archive [enable|disable]
set log-quota {integer}
set max-log-file-size {integer}
FortiOS 8.0.0 CLI Reference
904
Fortinet Inc.

<!-- 来源页 905 -->
set max-policy-packet-capture-size {integer}
set maximum-log-age {integer}
set report-quota {integer}
set roll-day {option1}, {option2}, ...
set roll-schedule [daily|weekly]
set roll-time {user}
set source-ip {ipv4-address}
set status [enable|disable]
set upload [enable|disable]
set upload-delete-files [enable|disable]
set upload-destination [ftp-server|sftp-server]
set upload-file-format [default|lz4]
set upload-ssl-conn [default|high|...]
set uploaddir {string}
set uploadip {ipv4-address}
set uploadpass {password}
set uploadport {integer}
set uploadsched [disable|enable]
set uploadtime {user}
set uploadtype {option1}, {option2}, ...
set uploaduser {string}
set vrf-select {integer}
end
config log disk setting
Parameter
Description
Type
Size
Default
diskfull
Action to take when disk is full. The system
can overwrite the oldest log messages or
stop logging when the disk is full (default =
overwrite).
option
-overwrite
Option
Description
overwrite
Overwrite the oldest logs when the log disk is full.
nolog
Stop logging when the log disk is full.
dlp-archive-quota *
DLP archive quota (MB).
integer
Minimum value:
0 Maximum
value:
4294967295
0
full-final-warning-threshold
Log full final warning threshold as a percent
(3 - 100, default = 95).
integer
Minimum value:
3 Maximum
value: 100
95
full-first-warning-threshold
Log full first warning threshold as a percent
(1 - 98, default = 75).
integer
Minimum value:
1 Maximum
value: 98
75
FortiOS 8.0.0 CLI Reference
905
Fortinet Inc.

<!-- 来源页 906 -->
Parameter
Description
Type
Size
Default
full-second-warning-threshold
Log full second warning threshold as a
percent (2 - 99, default = 90).
integer
Minimum value:
2 Maximum
value: 99
90
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
ips-archive *
Enable/disable IPS packet archiving to the
local disk.
option
-enable
Option
Description
enable
Enable IPS packet archiving.
disable
Disable IPS packet archiving.
log-quota
Disk log quota (MB).
integer
Minimum value:
0 Maximum
value:
4294967295
0
max-log-file-size
Maximum log file size before rolling (1 - 100
Mbytes).
integer
Minimum value:
1 Maximum
value: 100
20
max-policy-packet-capture-size
Maximum size of policy sniffer in MB (0
means unlimited).
integer
Minimum value:
0 Maximum
value:
4294967295
100
maximum-log-age
Delete log files older than (days).
integer
Minimum value:
0 Maximum
value: 3650
7
report-quota *
Report db quota (MB).
integer
Minimum value:
0 Maximum
value:
4294967295
0
roll-day
Day of week on which to roll log file.
option
-sunday
FortiOS 8.0.0 CLI Reference
906
Fortinet Inc.

<!-- 来源页 907 -->
Parameter
Description
Type
Size
Default
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
roll-schedule
Frequency to check log file for rolling.
option
-daily
Option
Description
daily
Check the log file once a day.
weekly
Check the log file once a week.
roll-time
Time of day to roll the log file (hh:mm).
user
Not Specified
source-ip
Source IP address to use for uploading disk
log files.
ipv4-address
Not Specified
0.0.0.0
status
Enable/disable local disk logging.
option
-disable **
Option
Description
enable
Log to local disk.
disable
Do not log to local disk.
upload
Enable/disable uploading log files when they
are rolled.
option
-disable
Option
Description
enable
Enable uploading log files when they are rolled.
disable
Disable uploading log files when they are rolled.
upload-delete-files
Delete log files after uploading (default =
enable).
option
-enable
Option
Description
enable
Delete log files after uploading.
disable
Do not delete log files after uploading.
FortiOS 8.0.0 CLI Reference
907
Fortinet Inc.

<!-- 来源页 908 -->
Parameter
Description
Type
Size
Default
upload-destination
The type of server to upload log files to.
option
-ftp-server
Option
Description
ftp-server
Upload rolled log files to a FTP server.
sftp-server
Upload rolled log files to a SFTP server.
upload-file-format *
Configure the file format to be used for log
files prior to being uploaded.
option
-default
Option
Description
default
Upload rolled log files as they appear on disk.
lz4
Upload rolled log files with standard LZ4 format.
upload-ssl-conn
Enable/disable encrypted FTPS
communication to upload log files.
option
-default
Option
Description
default
FTPS with high and medium encryption algorithms.
high
FTPS with high encryption algorithms.
low
FTPS with low encryption algorithms.
disable
Disable FTPS communication.
uploaddir
The remote directory on the FTP server to
upload log files to.
string
Maximum
length: 63
uploadip
IP address of the FTP/SFTP server to upload
log files to.
ipv4-address
Not Specified
0.0.0.0
uploadpass
Password required to log into the FTP server
to upload disk log files.
password
Not Specified
uploadport
TCP port to use for communicating with the
FTP/SFTP server (default FTP:21, SFTP:22).
integer
Minimum value:
0 Maximum
value: 65535
21
uploadsched
Set the schedule for uploading log files to
the FTP server (default = disable = upload
when rolling).
option
-disable
Option
Description
disable
Upload when rolling.
enable
Scheduled upload.
FortiOS 8.0.0 CLI Reference
908
Fortinet Inc.

<!-- 来源页 909 -->
Parameter
Description
Type
Size
Default
uploadtime
Time of day at which log files are uploaded if
uploadsched is enabled (hh:mm or hh).
user
Not Specified
uploadtype
Types of log files to upload. Separate
multiple entries with a space.
option
-traffic event
virus
webfilter
IPS
emailfilter
dlp-archive
anomaly
voip dlp
app-ctrl waf
dns ssh ssl
**
Option
Description
traffic
Upload traffic log.
event
Upload event log.
virus
Upload anti-virus log.
webfilter
Upload web filter log.
IPS
Upload IPS log.
emailfilter
Upload spam filter log.
dlp-archive
Upload DLP archive.
anomaly
Upload anomaly log.
voip
Upload VoIP log.
dlp
Upload DLP log.
app-ctrl
Upload application control log.
waf
Upload web application firewall log.
dns
Upload DNS log.
ssh
Upload SSH log.
ssl
Upload SSL log.
file-filter
Upload file-filter log.
icap
Upload ICAP log.
virtual-patch
Upload virtual-patch log.
debug
Upload debug log.
gtp
Upload GTP log.
FortiOS 8.0.0 CLI Reference
909
Fortinet Inc.

<!-- 来源页 910 -->
Parameter
Description
Type
Size
Default
uploaduser
Username required to log into the FTP
server to upload disk log files.
string
Maximum
length: 35
vrf-select
VRF ID used for connection to server.
integer
Minimum value:
0 Maximum
value: 511
0
* This parameter may not exist in some models.
** Values may differ between models.
config log eventfilter
Configure log event filters.
config log eventfilter
Description: Configure log event filters.
set cifs [enable|disable]
set connector [enable|disable]
set endpoint [enable|disable]
set event [enable|disable]
set fortiextender [enable|disable]
set ftnt-sec-mod [enable|disable]
set ha [enable|disable]
set rest-api [enable|disable]
set router [enable|disable]
set sdwan [enable|disable]
set security-rating [enable|disable]
set switch-controller [enable|disable]
set system [enable|disable]
set telemetry [enable|disable]
set user [enable|disable]
set vpn [enable|disable]
set wan-opt [enable|disable]
set web-svc [enable|disable]
set webproxy [enable|disable]
set wireless-activity [enable|disable]
end
config log eventfilter
Parameter
Description
Type
Size
Default
cifs
Enable/disable CIFS logging.
option
-enable
FortiOS 8.0.0 CLI Reference
910
Fortinet Inc.

<!-- 来源页 911 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable CIFS logging.
disable
Disable CIFS logging.
connector
Enable/disable SDN connector logging.
option
-enable
Option
Description
enable
Enable SDN connector logging.
disable
Disable SDN connector logging.
endpoint
Enable/disable endpoint event logging.
option
-enable
Option
Description
enable
Enable endpoint event logging.
disable
Disable endpoint event logging.
event
Enable/disable event logging.
option
-enable
Option
Description
enable
Enable event logging.
disable
Disable event logging.
fortiextender
Enable/disable FortiExtender logging.
option
-enable
Option
Description
enable
Enable Forti-Extender logging.
disable
Disable Forti-Extender logging.
ftnt-sec-mod *
Enable/disable Forti Security Module logging.
option
-enable
Option
Description
enable
Enable Forti Security Module logging.
disable
Disable Forti Security Module logging.
ha
Enable/disable ha event logging.
option
-enable
Option
Description
enable
Enable ha event logging.
disable
Disable ha event logging.
rest-api
Enable/disable REST API logging.
option
-enable
FortiOS 8.0.0 CLI Reference
911
Fortinet Inc.

<!-- 来源页 912 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable REST API logging.
disable
Disable REST API logging.
router
Enable/disable router event logging.
option
-enable
Option
Description
enable
Enable router event logging.
disable
Disable router event logging.
sdwan
Enable/disable SD-WAN logging.
option
-enable
Option
Description
enable
Enable SD-WAN logging.
disable
Disable SD-WAN logging.
security-rating
Enable/disable Security Rating result logging.
option
-enable
Option
Description
enable
Enable Security Fabric audit result logging.
disable
Disable Security Fabric audit result logging.
switch-controller
Enable/disable Switch-Controller logging.
option
-enable
Option
Description
enable
Enable Switch-Controller logging.
disable
Disable Switch-Controller logging.
system
Enable/disable system event logging.
option
-enable
Option
Description
enable
Enable system event logging.
disable
Disable system event logging.
telemetry *
Enable/disable telemetry event logging.
option
-enable
Option
Description
enable
Enable telemetry event logging.
disable
Disable telemetry event logging.
FortiOS 8.0.0 CLI Reference
912
Fortinet Inc.

<!-- 来源页 913 -->
Parameter
Description
Type
Size
Default
user
Enable/disable user authentication event logging.
option
-enable
Option
Description
enable
Enable user authentication event logging.
disable
Disable user authentication event logging.
vpn
Enable/disable VPN event logging.
option
-enable
Option
Description
enable
Enable VPN event logging.
disable
Disable VPN event logging.
wan-opt
Enable/disable WAN optimization event logging.
option
-enable
Option
Description
enable
Enable WAN optimization event logging.
disable
Disable WAN optimization event logging.
web-svc
Enable/disable web-svc performance logging.
option
-enable
Option
Description
enable
Enable web-svc daemon logging.
disable
Disable web-svc daemon logging.
webproxy *
Enable/disable web proxy event logging.
option
-enable
Option
Description
enable
Enable Web Proxy event logging.
disable
Disable Web Proxy event logging.
wireless-activity
Enable/disable wireless event logging.
option
-enable
Option
Description
enable
Enable wireless event logging.
disable
Disable wireless event logging.
* This parameter may not exist in some models.
FortiOS 8.0.0 CLI Reference
913
Fortinet Inc.

<!-- 来源页 914 -->
config log fortianalyzer filter
Filters for FortiAnalyzer.
config log fortianalyzer filter
Description: Filters for FortiAnalyzer.
set anomaly [enable|disable]
set dlp-archive [enable|disable]
set forti-switch [enable|disable]
set forward-traffic [enable|disable]
config free-style
Description: Free style filters.
edit <id>
set category [traffic|event|...]
set filter {string}
set filter-type [include|exclude]
next
end
set gtp [enable|disable]
set http-transaction [enable|disable]
set local-traffic [enable|disable]
set multicast-traffic [enable|disable]
set severity [emergency|alert|...]
set sniffer-traffic [enable|disable]
set voip [enable|disable]
set ztna-traffic [enable|disable]
end
config log fortianalyzer filter
Parameter
Description
Type
Size
Default
anomaly
Enable/disable anomaly logging.
option
-enable
Option
Description
enable
Enable anomaly logging.
disable
Disable anomaly logging.
dlp-archive
Enable/disable DLP archive logging.
option
-enable
Option
Description
enable
Enable DLP archive logging.
disable
Disable DLP archive logging.
forti-switch
Enable/disable Forti-Switch logging.
option
-enable
FortiOS 8.0.0 CLI Reference
914
Fortinet Inc.

<!-- 来源页 915 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable Forti-Switch logging.
disable
Disable Forti-Switch logging.
forward-traffic
Enable/disable forward traffic logging.
option
-enable
Option
Description
enable
Enable forward traffic logging.
disable
Disable forward traffic logging.
gtp *
Enable/disable GTP messages logging.
option
-enable
Option
Description
enable
Enable GTP messages logging.
disable
Disable GTP messages logging.
http-transaction
Enable/disable log HTTP transaction messages.
option
-enable
Option
Description
enable
Enable http transaction logging.
disable
Disable http transaction logging.
local-traffic
Enable/disable local in or out traffic logging.
option
-enable
Option
Description
enable
Enable local in or out traffic logging.
disable
Disable local in or out traffic logging.
multicast-traffic
Enable/disable multicast traffic logging.
option
-enable
Option
Description
enable
Enable multicast traffic logging.
disable
Disable multicast traffic logging.
severity
Lowest severity level to log.
option
-information
FortiOS 8.0.0 CLI Reference
915
Fortinet Inc.

<!-- 来源页 916 -->
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
sniffer-traffic
Enable/disable sniffer traffic logging.
option
-enable
Option
Description
enable
Enable sniffer traffic logging.
disable
Disable sniffer traffic logging.
voip
Enable/disable VoIP logging.
option
-enable
Option
Description
enable
Enable VoIP logging.
disable
Disable VoIP logging.
ztna-traffic
Enable/disable ztna traffic logging.
option
-enable
Option
Description
enable
Enable ztna traffic logging.
disable
Disable ztna traffic logging.
* This parameter may not exist in some models.
config free-style
Parameter
Description
Type
Size
Default
category
Log category.
option
-traffic
Option
Description
traffic
Traffic log.
FortiOS 8.0.0 CLI Reference
916
Fortinet Inc.

<!-- 来源页 917 -->
Parameter
Description
Type
Size
Default
Option
Description
event
Event log.
virus
Antivirus log.
webfilter
Web filter log.
attack
Attack log.
spam
Antispam log.
anomaly
Anomaly log.
voip
VoIP log.
dlp
DLP log.
app-ctrl
Application control log.
waf
Web application firewall log.
dns
DNS detail log.
ssh
SSH log.
ssl
SSL log.
file-filter
File filter log.
icap
ICAP log.
virtual-patch
Virtual patch log.
debug
Debug log.
filter
Free style filter string.
string
Maximum
length: 1023
filter-type
Include/exclude logs that match the filter.
option
-include
Option
Description
include
Include logs that match the filter.
exclude
Exclude logs that match the filter.
id
Entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config log fortianalyzer override-filter
Override filters for FortiAnalyzer.
FortiOS 8.0.0 CLI Reference
917
Fortinet Inc.

<!-- 来源页 918 -->
config log fortianalyzer override-filter
Description: Override filters for FortiAnalyzer.
set anomaly [enable|disable]
set dlp-archive [enable|disable]
set forti-switch [enable|disable]
set forward-traffic [enable|disable]
config free-style
Description: Free style filters.
edit <id>
set category [traffic|event|...]
set filter {string}
set filter-type [include|exclude]
next
end
set gtp [enable|disable]
set http-transaction [enable|disable]
set local-traffic [enable|disable]
set multicast-traffic [enable|disable]
set severity [emergency|alert|...]
set sniffer-traffic [enable|disable]
set voip [enable|disable]
set ztna-traffic [enable|disable]
end
config log fortianalyzer override-filter
Parameter
Description
Type
Size
Default
anomaly
Enable/disable anomaly logging.
option
-enable
Option
Description
enable
Enable anomaly logging.
disable
Disable anomaly logging.
dlp-archive
Enable/disable DLP archive logging.
option
-enable
Option
Description
enable
Enable DLP archive logging.
disable
Disable DLP archive logging.
forti-switch
Enable/disable Forti-Switch logging.
option
-enable
Option
Description
enable
Enable Forti-Switch logging.
disable
Disable Forti-Switch logging.
FortiOS 8.0.0 CLI Reference
918
Fortinet Inc.

<!-- 来源页 919 -->
Parameter
Description
Type
Size
Default
forward-traffic
Enable/disable forward traffic logging.
option
-enable
Option
Description
enable
Enable forward traffic logging.
disable
Disable forward traffic logging.
gtp *
Enable/disable GTP messages logging.
option
-enable
Option
Description
enable
Enable GTP messages logging.
disable
Disable GTP messages logging.
http-transaction
Enable/disable log HTTP transaction messages.
option
-enable
Option
Description
enable
Enable http transaction logging.
disable
Disable http transaction logging.
local-traffic
Enable/disable local in or out traffic logging.
option
-enable
Option
Description
enable
Enable local in or out traffic logging.
disable
Disable local in or out traffic logging.
multicast-traffic
Enable/disable multicast traffic logging.
option
-enable
Option
Description
enable
Enable multicast traffic logging.
disable
Disable multicast traffic logging.
severity
Lowest severity level to log.
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
FortiOS 8.0.0 CLI Reference
919
Fortinet Inc.

<!-- 来源页 920 -->
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
sniffer-traffic
Enable/disable sniffer traffic logging.
option
-enable
Option
Description
enable
Enable sniffer traffic logging.
disable
Disable sniffer traffic logging.
voip
Enable/disable VoIP logging.
option
-enable
Option
Description
enable
Enable VoIP logging.
disable
Disable VoIP logging.
ztna-traffic
Enable/disable ztna traffic logging.
option
-enable
Option
Description
enable
Enable ztna traffic logging.
disable
Disable ztna traffic logging.
* This parameter may not exist in some models.
config free-style
Parameter
Description
Type
Size
Default
category
Log category.
option
-traffic
Option
Description
traffic
Traffic log.
event
Event log.
virus
Antivirus log.
webfilter
Web filter log.
FortiOS 8.0.0 CLI Reference
920
Fortinet Inc.

<!-- 来源页 921 -->
Parameter
Description
Type
Size
Default
Option
Description
attack
Attack log.
spam
Antispam log.
anomaly
Anomaly log.
voip
VoIP log.
dlp
DLP log.
app-ctrl
Application control log.
waf
Web application firewall log.
dns
DNS detail log.
ssh
SSH log.
ssl
SSL log.
file-filter
File filter log.
icap
ICAP log.
virtual-patch
Virtual patch log.
debug
Debug log.
filter
Free style filter string.
string
Maximum
length: 1023
filter-type
Include/exclude logs that match the filter.
option
-include
Option
Description
include
Include logs that match the filter.
exclude
Exclude logs that match the filter.
id
Entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config log fortianalyzer override-setting
Override FortiAnalyzer settings.
config log fortianalyzer override-setting
Description: Override FortiAnalyzer settings.
set access-config [enable|disable]
set alt-server {string}
FortiOS 8.0.0 CLI Reference
921
Fortinet Inc.

<!-- 来源页 922 -->
set certificate {string}
set certificate-verification [enable|disable]
set conn-timeout {integer}
set enc-algorithm [high-medium|high|...]
set fallback-to-primary [enable|disable]
set hmac-algorithm {option}
set interface {string}
set interface-select-method [auto|sdwan|...]
set ips-archive [enable|disable]
set max-log-rate {integer}
set monitor-failure-retry-period {integer}
set monitor-keepalive-period {integer}
set preshared-key {password}
set priority [default|low]
set reliable [enable|disable]
set serial <name1>, <name2>, ...
set server {string}
set server-cert-ca {string}
set source-ip {string}
set ssl-min-proto-version [default|SSLv3|...]
set status [enable|disable]
set upload-day {user}
set upload-interval [daily|weekly|...]
set upload-option [store-and-upload|realtime|...]
set upload-time {user}
set use-management-vdom [enable|disable]
set vrf-select {integer}
end
config log fortianalyzer override-setting
Parameter
Description
Type
Size
Default
access-config
Enable/disable FortiAnalyzer access to
configuration and data.
option
-enable
Option
Description
enable
Enable FortiAnalyzer access to configuration and data.
disable
Disable FortiAnalyzer access to configuration and data.
alt-server
Alternate FortiAnalyzer.
string
Maximum
length: 127
certificate
Certificate used to communicate with
FortiAnalyzer.
string
Maximum
length: 35
certificate-verification
Enable/disable identity verification of
FortiAnalyzer by use of certificate.
option
-enable
FortiOS 8.0.0 CLI Reference
922
Fortinet Inc.

<!-- 来源页 923 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable identity verification of FortiAnalyzer by use of certificate.
disable
Disable identity verification of FortiAnalyzer by use of certificate.
conn-timeout
FortiAnalyzer connection time-out in seconds
(for status and log buffer).
integer
Minimum
value: 1
Maximum
value: 3600
10
enc-algorithm
Configure the level of SSL protection for secure
communication with FortiAnalyzer.
option
-high
Option
Description
high-medium
Encrypt logs using high and medium encryption algorithms.
high
Encrypt logs using high encryption algorithms.
low
Encrypt logs using all encryption algorithms.
fallback-to-primary
Enable/disable this FortiGate unit to fallback to
the primary FortiAnalyzer when it is available.
option
-enable
Option
Description
enable
Enable this FortiGate unit to fallback to the primary FortiAnalyzer
when it is available.
disable
Disable this FortiGate unit to fallback to the primary FortiAnalyzer
when it is available.
hmac-algorithm
OFTP login hash algorithm.
option
-sha256
Option
Description
sha256
Use SHA256 as HMAC algorithm.
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
FortiOS 8.0.0 CLI Reference
923
Fortinet Inc.

<!-- 来源页 924 -->
Parameter
Description
Type
Size
Default
ips-archive
Enable/disable IPS packet archive logging.
option
-enable
Option
Description
enable
Enable IPS packet archive logging.
disable
Disable IPS packet archive logging.
max-log-rate
FortiAnalyzer maximum log rate in MBps (0 =
unlimited).
integer
Minimum
value: 0
Maximum
value:
100000
0
monitor-failure-retry-period
Time between FortiAnalyzer connection retries
in seconds (for status and log buffer).
integer
Minimum
value: 1
Maximum
value:
86400
5
monitor-keepalive-period
Time between OFTP keepalives in seconds (for
status and log buffer).
integer
Minimum
value: 1
Maximum
value: 120
5
preshared-key
Preshared-key used for auto-authorization on
FortiAnalyzer.
password
**
Not
Specified **
priority
Set log transmission priority.
option
-default
Option
Description
default
Set FortiAnalyzer log transmission priority to default.
low
Set FortiAnalyzer log transmission priority to low.
reliable
Enable/disable reliable logging to FortiAnalyzer.
option
-disable
Option
Description
enable
Enable reliable logging to FortiAnalyzer.
disable
Disable reliable logging to FortiAnalyzer.
serial <name>
Serial numbers of the FortiAnalyzer.
Serial Number.
string
Maximum
length: 79
server
The remote FortiAnalyzer.
string
Maximum
length: 127
server-cert-ca
Mandatory CA on FortiGate in certificate chain
of server.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
924
Fortinet Inc.

<!-- 来源页 925 -->
Parameter
Description
Type
Size
Default
source-ip
Source IPv4 or IPv6 address used to
communicate with FortiAnalyzer.
string
Maximum
length: 63
ssl-min-proto-version
Minimum supported protocol version for
SSL/TLS connections (default is to follow
system global setting).
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
Enable/disable logging to FortiAnalyzer.
option
-disable
Option
Description
enable
Enable logging to FortiAnalyzer.
disable
Disable logging to FortiAnalyzer.
upload-day
Day of week (month) to upload logs.
user
Not
Specified
upload-interval
Frequency to upload log files to FortiAnalyzer.
option
-daily
Option
Description
daily
Upload log files to FortiAnalyzer once a day.
weekly
Upload log files to FortiAnalyzer once a week.
monthly
Upload log files to FortiAnalyzer once a month.
upload-option
Enable/disable logging to hard disk and then
uploading to FortiAnalyzer.
option
-5-minute
Option
Description
store-and-upload
Log to hard disk and then upload to FortiAnalyzer.
realtime
Log directly to FortiAnalyzer in real time.
1-minute
Log directly to FortiAnalyzer at least every 1 minute.
5-minute
Log directly to FortiAnalyzer at least every 5 minutes.
FortiOS 8.0.0 CLI Reference
925
Fortinet Inc.

<!-- 来源页 926 -->
Parameter
Description
Type
Size
Default
upload-time
Time to upload logs (hh:mm).
user
Not
Specified
use-management-vdom
Enable/disable use of management VDOM IP
address as source IP for logs sent to
FortiAnalyzer.
option
-disable
Option
Description
enable
Enable use of management VDOM IP address as source IP for logs
sent to FortiAnalyzer.
disable
Disable use of management VDOM IP address as source IP for logs
sent to FortiAnalyzer.
vrf-select
VRF ID used for connection to server.
integer
Minimum
value: 0
Maximum
value: 511
0
** Values may differ between models.
config log fortianalyzer setting
Global FortiAnalyzer settings.
config log fortianalyzer setting
Description: Global FortiAnalyzer settings.
set access-config [enable|disable]
set alt-server {string}
set certificate {string}
set certificate-verification [enable|disable]
set conn-timeout {integer}
set enc-algorithm [high-medium|high|...]
set fallback-to-primary [enable|disable]
set hmac-algorithm {option}
set interface {string}
set interface-select-method [auto|sdwan|...]
set ips-archive [enable|disable]
set max-log-rate {integer}
set monitor-failure-retry-period {integer}
set monitor-keepalive-period {integer}
set preshared-key {password}
set priority [default|low]
set reliable [enable|disable]
set serial <name1>, <name2>, ...
set server {string}
set server-cert-ca {string}
set source-ip {string}
FortiOS 8.0.0 CLI Reference
926
Fortinet Inc.

<!-- 来源页 927 -->
set ssl-min-proto-version [default|SSLv3|...]
set status [enable|disable]
set upload-day {user}
set upload-interval [daily|weekly|...]
set upload-option [store-and-upload|realtime|...]
set upload-time {user}
set vrf-select {integer}
end
config log fortianalyzer setting
Parameter
Description
Type
Size
Default
access-config
Enable/disable FortiAnalyzer access to
configuration and data.
option
-enable
Option
Description
enable
Enable FortiAnalyzer access to configuration and data.
disable
Disable FortiAnalyzer access to configuration and data.
alt-server
Alternate FortiAnalyzer.
string
Maximum
length: 127
certificate
Certificate used to communicate with
FortiAnalyzer.
string
Maximum
length: 35
certificate-verification
Enable/disable identity verification of
FortiAnalyzer by use of certificate.
option
-enable
Option
Description
enable
Enable identity verification of FortiAnalyzer by use of certificate.
disable
Disable identity verification of FortiAnalyzer by use of certificate.
conn-timeout
FortiAnalyzer connection time-out in seconds (for
status and log buffer).
integer
Minimum
value: 1
Maximum
value: 3600
10
enc-algorithm
Configure the level of SSL protection for secure
communication with FortiAnalyzer.
option
-high
Option
Description
high-medium
Encrypt logs using high and medium encryption algorithms.
high
Encrypt logs using high encryption algorithms.
low
Encrypt logs using all encryption algorithms.
FortiOS 8.0.0 CLI Reference
927
Fortinet Inc.

<!-- 来源页 928 -->
Parameter
Description
Type
Size
Default
fallback-to-primary
Enable/disable this FortiGate unit to fallback to the
primary FortiAnalyzer when it is available.
option
-enable
Option
Description
enable
Enable this FortiGate unit to fallback to the primary FortiAnalyzer when it
is available.
disable
Disable this FortiGate unit to fallback to the primary FortiAnalyzer when
it is available.
hmac-algorithm
OFTP login hash algorithm.
option
-sha256
Option
Description
sha256
Use SHA256 as HMAC algorithm.
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
ips-archive
Enable/disable IPS packet archive logging.
option
-enable
Option
Description
enable
Enable IPS packet archive logging.
disable
Disable IPS packet archive logging.
max-log-rate
FortiAnalyzer maximum log rate in MBps (0 =
unlimited).
integer
Minimum
value: 0
Maximum
value:
100000
0
monitor-failure-retry-period
Time between FortiAnalyzer connection retries in
seconds (for status and log buffer).
integer
Minimum
value: 1
Maximum
value:
86400
5
FortiOS 8.0.0 CLI Reference
928
Fortinet Inc.

<!-- 来源页 929 -->
Parameter
Description
Type
Size
Default
monitor-keepalive-period
Time between OFTP keepalives in seconds (for
status and log buffer).
integer
Minimum
value: 1
Maximum
value: 120
5
preshared-key
Preshared-key used for auto-authorization on
FortiAnalyzer.
password
**
Not
Specified **
priority
Set log transmission priority.
option
-default
Option
Description
default
Set FortiAnalyzer log transmission priority to default.
low
Set FortiAnalyzer log transmission priority to low.
reliable
Enable/disable reliable logging to FortiAnalyzer.
option
-disable
Option
Description
enable
Enable reliable logging to FortiAnalyzer.
disable
Disable reliable logging to FortiAnalyzer.
serial <name>
Serial numbers of the FortiAnalyzer.
Serial Number.
string
Maximum
length: 79
server
The remote FortiAnalyzer.
string
Maximum
length: 127
server-cert-ca
Mandatory CA on FortiGate in certificate chain of
server.
string
Maximum
length: 79
source-ip
Source IPv4 or IPv6 address used to communicate
with FortiAnalyzer.
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
FortiOS 8.0.0 CLI Reference
929
Fortinet Inc.

<!-- 来源页 930 -->
Parameter
Description
Type
Size
Default
status
Enable/disable logging to FortiAnalyzer.
option
-disable
Option
Description
enable
Enable logging to FortiAnalyzer.
disable
Disable logging to FortiAnalyzer.
upload-day
Day of week (month) to upload logs.
user
Not
Specified
upload-interval
Frequency to upload log files to FortiAnalyzer.
option
-daily
Option
Description
daily
Upload log files to FortiAnalyzer once a day.
weekly
Upload log files to FortiAnalyzer once a week.
monthly
Upload log files to FortiAnalyzer once a month.
upload-option
Enable/disable logging to hard disk and then
uploading to FortiAnalyzer.
option
-5-minute
Option
Description
store-and-upload
Log to hard disk and then upload to FortiAnalyzer.
realtime
Log directly to FortiAnalyzer in real time.
1-minute
Log directly to FortiAnalyzer at least every 1 minute.
5-minute
Log directly to FortiAnalyzer at least every 5 minutes.
upload-time
Time to upload logs (hh:mm).
user
Not
Specified
vrf-select
VRF ID used for connection to server.
integer
Minimum
value: 0
Maximum
value: 511
0
** Values may differ between models.
config log fortianalyzer2 filter
Filters for FortiAnalyzer.
config log fortianalyzer2 filter
Description: Filters for FortiAnalyzer.
FortiOS 8.0.0 CLI Reference
930
Fortinet Inc.

<!-- 来源页 931 -->
set anomaly [enable|disable]
set dlp-archive [enable|disable]
set forti-switch [enable|disable]
set forward-traffic [enable|disable]
config free-style
Description: Free style filters.
edit <id>
set category [traffic|event|...]
set filter {string}
set filter-type [include|exclude]
next
end
set gtp [enable|disable]
set http-transaction [enable|disable]
set local-traffic [enable|disable]
set multicast-traffic [enable|disable]
set severity [emergency|alert|...]
set sniffer-traffic [enable|disable]
set voip [enable|disable]
set ztna-traffic [enable|disable]
end
config log fortianalyzer2 filter
Parameter
Description
Type
Size
Default
anomaly
Enable/disable anomaly logging.
option
-enable
Option
Description
enable
Enable anomaly logging.
disable
Disable anomaly logging.
dlp-archive
Enable/disable DLP archive logging.
option
-enable
Option
Description
enable
Enable DLP archive logging.
disable
Disable DLP archive logging.
forti-switch
Enable/disable Forti-Switch logging.
option
-enable
Option
Description
enable
Enable Forti-Switch logging.
disable
Disable Forti-Switch logging.
forward-traffic
Enable/disable forward traffic logging.
option
-enable
FortiOS 8.0.0 CLI Reference
931
Fortinet Inc.

<!-- 来源页 932 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable forward traffic logging.
disable
Disable forward traffic logging.
gtp *
Enable/disable GTP messages logging.
option
-enable
Option
Description
enable
Enable GTP messages logging.
disable
Disable GTP messages logging.
http-transaction
Enable/disable log HTTP transaction messages.
option
-enable
Option
Description
enable
Enable http transaction logging.
disable
Disable http transaction logging.
local-traffic
Enable/disable local in or out traffic logging.
option
-enable
Option
Description
enable
Enable local in or out traffic logging.
disable
Disable local in or out traffic logging.
multicast-traffic
Enable/disable multicast traffic logging.
option
-enable
Option
Description
enable
Enable multicast traffic logging.
disable
Disable multicast traffic logging.
severity
Log every message above and including this
severity level.
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
FortiOS 8.0.0 CLI Reference
932
Fortinet Inc.

<!-- 来源页 933 -->
Parameter
Description
Type
Size
Default
Option
Description
warning
Warning level.
notification
Notification level.
information
Information level.
debug
Debug level.
sniffer-traffic
Enable/disable sniffer traffic logging.
option
-enable
Option
Description
enable
Enable sniffer traffic logging.
disable
Disable sniffer traffic logging.
voip
Enable/disable VoIP logging.
option
-enable
Option
Description
enable
Enable VoIP logging.
disable
Disable VoIP logging.
ztna-traffic
Enable/disable ztna traffic logging.
option
-enable
Option
Description
enable
Enable ztna traffic logging.
disable
Disable ztna traffic logging.
* This parameter may not exist in some models.
config free-style
Parameter
Description
Type
Size
Default
category
Log category.
option
-traffic
Option
Description
traffic
Traffic log.
event
Event log.
virus
Antivirus log.
webfilter
Web filter log.
attack
Attack log.
FortiOS 8.0.0 CLI Reference
933
Fortinet Inc.

<!-- 来源页 934 -->
Parameter
Description
Type
Size
Default
Option
Description
spam
Antispam log.
anomaly
Anomaly log.
voip
VoIP log.
dlp
DLP log.
app-ctrl
Application control log.
waf
Web application firewall log.
dns
DNS detail log.
ssh
SSH log.
ssl
SSL log.
file-filter
File filter log.
icap
ICAP log.
virtual-patch
Virtual patch log.
debug
Debug log.
filter
Free style filter string.
string
Maximum
length: 1023
filter-type
Include/exclude logs that match the filter.
option
-include
Option
Description
include
Include logs that match the filter.
exclude
Exclude logs that match the filter.
id
Entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config log fortianalyzer2 override-filter
Override filters for FortiAnalyzer.
config log fortianalyzer2 override-filter
Description: Override filters for FortiAnalyzer.
set anomaly [enable|disable]
set dlp-archive [enable|disable]
set forti-switch [enable|disable]
set forward-traffic [enable|disable]
FortiOS 8.0.0 CLI Reference
934
Fortinet Inc.

<!-- 来源页 935 -->
config free-style
Description: Free style filters.
edit <id>
set category [traffic|event|...]
set filter {string}
set filter-type [include|exclude]
next
end
set gtp [enable|disable]
set http-transaction [enable|disable]
set local-traffic [enable|disable]
set multicast-traffic [enable|disable]
set severity [emergency|alert|...]
set sniffer-traffic [enable|disable]
set voip [enable|disable]
set ztna-traffic [enable|disable]
end
config log fortianalyzer2 override-filter
Parameter
Description
Type
Size
Default
anomaly
Enable/disable anomaly logging.
option
-enable
Option
Description
enable
Enable anomaly logging.
disable
Disable anomaly logging.
dlp-archive
Enable/disable DLP archive logging.
option
-enable
Option
Description
enable
Enable DLP archive logging.
disable
Disable DLP archive logging.
forti-switch
Enable/disable Forti-Switch logging.
option
-enable
Option
Description
enable
Enable Forti-Switch logging.
disable
Disable Forti-Switch logging.
forward-traffic
Enable/disable forward traffic logging.
option
-enable
FortiOS 8.0.0 CLI Reference
935
Fortinet Inc.

<!-- 来源页 936 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable forward traffic logging.
disable
Disable forward traffic logging.
gtp *
Enable/disable GTP messages logging.
option
-enable
Option
Description
enable
Enable GTP messages logging.
disable
Disable GTP messages logging.
http-transaction
Enable/disable log HTTP transaction messages.
option
-enable
Option
Description
enable
Enable http transaction logging.
disable
Disable http transaction logging.
local-traffic
Enable/disable local in or out traffic logging.
option
-enable
Option
Description
enable
Enable local in or out traffic logging.
disable
Disable local in or out traffic logging.
multicast-traffic
Enable/disable multicast traffic logging.
option
-enable
Option
Description
enable
Enable multicast traffic logging.
disable
Disable multicast traffic logging.
severity
Log every message above and including this
severity level.
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
FortiOS 8.0.0 CLI Reference
936
Fortinet Inc.

<!-- 来源页 937 -->
Parameter
Description
Type
Size
Default
Option
Description
warning
Warning level.
notification
Notification level.
information
Information level.
debug
Debug level.
sniffer-traffic
Enable/disable sniffer traffic logging.
option
-enable
Option
Description
enable
Enable sniffer traffic logging.
disable
Disable sniffer traffic logging.
voip
Enable/disable VoIP logging.
option
-enable
Option
Description
enable
Enable VoIP logging.
disable
Disable VoIP logging.
ztna-traffic
Enable/disable ztna traffic logging.
option
-enable
Option
Description
enable
Enable ztna traffic logging.
disable
Disable ztna traffic logging.
* This parameter may not exist in some models.
config free-style
Parameter
Description
Type
Size
Default
category
Log category.
option
-traffic
Option
Description
traffic
Traffic log.
event
Event log.
virus
Antivirus log.
webfilter
Web filter log.
attack
Attack log.
FortiOS 8.0.0 CLI Reference
937
Fortinet Inc.

<!-- 来源页 938 -->
Parameter
Description
Type
Size
Default
Option
Description
spam
Antispam log.
anomaly
Anomaly log.
voip
VoIP log.
dlp
DLP log.
app-ctrl
Application control log.
waf
Web application firewall log.
dns
DNS detail log.
ssh
SSH log.
ssl
SSL log.
file-filter
File filter log.
icap
ICAP log.
virtual-patch
Virtual patch log.
debug
Debug log.
filter
Free style filter string.
string
Maximum
length: 1023
filter-type
Include/exclude logs that match the filter.
option
-include
Option
Description
include
Include logs that match the filter.
exclude
Exclude logs that match the filter.
id
Entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config log fortianalyzer2 override-setting
Override FortiAnalyzer settings.
config log fortianalyzer2 override-setting
Description: Override FortiAnalyzer settings.
set access-config [enable|disable]
set alt-server {string}
set certificate {string}
set certificate-verification [enable|disable]
FortiOS 8.0.0 CLI Reference
938
Fortinet Inc.

<!-- 来源页 939 -->
set conn-timeout {integer}
set enc-algorithm [high-medium|high|...]
set fallback-to-primary [enable|disable]
set hmac-algorithm {option}
set interface {string}
set interface-select-method [auto|sdwan|...]
set ips-archive [enable|disable]
set max-log-rate {integer}
set monitor-failure-retry-period {integer}
set monitor-keepalive-period {integer}
set preshared-key {password}
set priority [default|low]
set reliable [enable|disable]
set serial <name1>, <name2>, ...
set server {string}
set server-cert-ca {string}
set source-ip {string}
set ssl-min-proto-version [default|SSLv3|...]
set status [enable|disable]
set upload-day {user}
set upload-interval [daily|weekly|...]
set upload-option [store-and-upload|realtime|...]
set upload-time {user}
set use-management-vdom [enable|disable]
set vrf-select {integer}
end
config log fortianalyzer2 override-setting
Parameter
Description
Type
Size
Default
access-config
Enable/disable FortiAnalyzer access to
configuration and data.
option
-enable
Option
Description
enable
Enable FortiAnalyzer access to configuration and data.
disable
Disable FortiAnalyzer access to configuration and data.
alt-server
Alternate FortiAnalyzer.
string
Maximum
length: 127
certificate
Certificate used to communicate with
FortiAnalyzer.
string
Maximum
length: 35
certificate-verification
Enable/disable identity verification of
FortiAnalyzer by use of certificate.
option
-enable
FortiOS 8.0.0 CLI Reference
939
Fortinet Inc.

<!-- 来源页 940 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable identity verification of FortiAnalyzer by use of certificate.
disable
Disable identity verification of FortiAnalyzer by use of certificate.
conn-timeout
FortiAnalyzer connection time-out in seconds
(for status and log buffer).
integer
Minimum
value: 1
Maximum
value: 3600
10
enc-algorithm
Configure the level of SSL protection for secure
communication with FortiAnalyzer.
option
-high
Option
Description
high-medium
Encrypt logs using high and medium encryption algorithms.
high
Encrypt logs using high encryption algorithms.
low
Encrypt logs using all encryption algorithms.
fallback-to-primary
Enable/disable this FortiGate unit to fallback to
the primary FortiAnalyzer when it is available.
option
-enable
Option
Description
enable
Enable this FortiGate unit to fallback to the primary FortiAnalyzer
when it is available.
disable
Disable this FortiGate unit to fallback to the primary FortiAnalyzer
when it is available.
hmac-algorithm
OFTP login hash algorithm.
option
-sha256
Option
Description
sha256
Use SHA256 as HMAC algorithm.
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
FortiOS 8.0.0 CLI Reference
940
Fortinet Inc.

<!-- 来源页 941 -->
Parameter
Description
Type
Size
Default
ips-archive
Enable/disable IPS packet archive logging.
option
-enable
Option
Description
enable
Enable IPS packet archive logging.
disable
Disable IPS packet archive logging.
max-log-rate
FortiAnalyzer maximum log rate in MBps (0 =
unlimited).
integer
Minimum
value: 0
Maximum
value:
100000
0
monitor-failure-retry-period
Time between FortiAnalyzer connection retries
in seconds (for status and log buffer).
integer
Minimum
value: 1
Maximum
value:
86400
5
monitor-keepalive-period
Time between OFTP keepalives in seconds (for
status and log buffer).
integer
Minimum
value: 1
Maximum
value: 120
5
preshared-key
Preshared-key used for auto-authorization on
FortiAnalyzer.
password
**
Not
Specified **
priority
Set log transmission priority.
option
-default
Option
Description
default
Set FortiAnalyzer log transmission priority to default.
low
Set FortiAnalyzer log transmission priority to low.
reliable
Enable/disable reliable logging to FortiAnalyzer.
option
-disable
Option
Description
enable
Enable reliable logging to FortiAnalyzer.
disable
Disable reliable logging to FortiAnalyzer.
serial <name>
Serial numbers of the FortiAnalyzer.
Serial Number.
string
Maximum
length: 79
server
The remote FortiAnalyzer.
string
Maximum
length: 127
server-cert-ca
Mandatory CA on FortiGate in certificate chain
of server.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
941
Fortinet Inc.

<!-- 来源页 942 -->
Parameter
Description
Type
Size
Default
source-ip
Source IPv4 or IPv6 address used to
communicate with FortiAnalyzer.
string
Maximum
length: 63
ssl-min-proto-version
Minimum supported protocol version for
SSL/TLS connections (default is to follow
system global setting).
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
Enable/disable logging to FortiAnalyzer.
option
-disable
Option
Description
enable
Enable logging to FortiAnalyzer.
disable
Disable logging to FortiAnalyzer.
upload-day
Day of week (month) to upload logs.
user
Not
Specified
upload-interval
Frequency to upload log files to FortiAnalyzer.
option
-daily
Option
Description
daily
Upload log files to FortiAnalyzer once a day.
weekly
Upload log files to FortiAnalyzer once a week.
monthly
Upload log files to FortiAnalyzer once a month.
upload-option
Enable/disable logging to hard disk and then
uploading to FortiAnalyzer.
option
-5-minute
Option
Description
store-and-upload
Log to hard disk and then upload to FortiAnalyzer.
realtime
Log directly to FortiAnalyzer in real time.
1-minute
Log directly to FortiAnalyzer at least every 1 minute.
5-minute
Log directly to FortiAnalyzer at least every 5 minutes.
FortiOS 8.0.0 CLI Reference
942
Fortinet Inc.

<!-- 来源页 943 -->
Parameter
Description
Type
Size
Default
upload-time
Time to upload logs (hh:mm).
user
Not
Specified
use-management-vdom
Enable/disable use of management VDOM IP
address as source IP for logs sent to
FortiAnalyzer.
option
-disable
Option
Description
enable
Enable use of management VDOM IP address as source IP for logs
sent to FortiAnalyzer.
disable
Disable use of management VDOM IP address as source IP for logs
sent to FortiAnalyzer.
vrf-select
VRF ID used for connection to server.
integer
Minimum
value: 0
Maximum
value: 511
0
** Values may differ between models.
config log fortianalyzer2 setting
Global FortiAnalyzer settings.
config log fortianalyzer2 setting
Description: Global FortiAnalyzer settings.
set access-config [enable|disable]
set alt-server {string}
set certificate {string}
set certificate-verification [enable|disable]
set conn-timeout {integer}
set enc-algorithm [high-medium|high|...]
set fallback-to-primary [enable|disable]
set hmac-algorithm {option}
set interface {string}
set interface-select-method [auto|sdwan|...]
set ips-archive [enable|disable]
set max-log-rate {integer}
set monitor-failure-retry-period {integer}
set monitor-keepalive-period {integer}
set preshared-key {password}
set priority [default|low]
set reliable [enable|disable]
set serial <name1>, <name2>, ...
set server {string}
set server-cert-ca {string}
set source-ip {string}
FortiOS 8.0.0 CLI Reference
943
Fortinet Inc.

<!-- 来源页 944 -->
set ssl-min-proto-version [default|SSLv3|...]
set status [enable|disable]
set upload-day {user}
set upload-interval [daily|weekly|...]
set upload-option [store-and-upload|realtime|...]
set upload-time {user}
set vrf-select {integer}
end
config log fortianalyzer2 setting
Parameter
Description
Type
Size
Default
access-config
Enable/disable FortiAnalyzer access to
configuration and data.
option
-enable
Option
Description
enable
Enable FortiAnalyzer access to configuration and data.
disable
Disable FortiAnalyzer access to configuration and data.
alt-server
Alternate FortiAnalyzer.
string
Maximum
length: 127
certificate
Certificate used to communicate with
FortiAnalyzer.
string
Maximum
length: 35
certificate-verification
Enable/disable identity verification of
FortiAnalyzer by use of certificate.
option
-enable
Option
Description
enable
Enable identity verification of FortiAnalyzer by use of certificate.
disable
Disable identity verification of FortiAnalyzer by use of certificate.
conn-timeout
FortiAnalyzer connection time-out in seconds (for
status and log buffer).
integer
Minimum
value: 1
Maximum
value: 3600
10
enc-algorithm
Configure the level of SSL protection for secure
communication with FortiAnalyzer.
option
-high
Option
Description
high-medium
Encrypt logs using high and medium encryption algorithms.
high
Encrypt logs using high encryption algorithms.
low
Encrypt logs using all encryption algorithms.
FortiOS 8.0.0 CLI Reference
944
Fortinet Inc.

<!-- 来源页 945 -->
Parameter
Description
Type
Size
Default
fallback-to-primary
Enable/disable this FortiGate unit to fallback to the
primary FortiAnalyzer when it is available.
option
-enable
Option
Description
enable
Enable this FortiGate unit to fallback to the primary FortiAnalyzer when it
is available.
disable
Disable this FortiGate unit to fallback to the primary FortiAnalyzer when
it is available.
hmac-algorithm
OFTP login hash algorithm.
option
-sha256
Option
Description
sha256
Use SHA256 as HMAC algorithm.
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
ips-archive
Enable/disable IPS packet archive logging.
option
-enable
Option
Description
enable
Enable IPS packet archive logging.
disable
Disable IPS packet archive logging.
max-log-rate
FortiAnalyzer maximum log rate in MBps (0 =
unlimited).
integer
Minimum
value: 0
Maximum
value:
100000
0
monitor-failure-retry-period
Time between FortiAnalyzer connection retries in
seconds (for status and log buffer).
integer
Minimum
value: 1
Maximum
value:
86400
5
FortiOS 8.0.0 CLI Reference
945
Fortinet Inc.

<!-- 来源页 946 -->
Parameter
Description
Type
Size
Default
monitor-keepalive-period
Time between OFTP keepalives in seconds (for
status and log buffer).
integer
Minimum
value: 1
Maximum
value: 120
5
preshared-key
Preshared-key used for auto-authorization on
FortiAnalyzer.
password
**
Not
Specified **
priority
Set log transmission priority.
option
-default
Option
Description
default
Set FortiAnalyzer log transmission priority to default.
low
Set FortiAnalyzer log transmission priority to low.
reliable
Enable/disable reliable logging to FortiAnalyzer.
option
-disable
Option
Description
enable
Enable reliable logging to FortiAnalyzer.
disable
Disable reliable logging to FortiAnalyzer.
serial <name>
Serial numbers of the FortiAnalyzer.
Serial Number.
string
Maximum
length: 79
server
The remote FortiAnalyzer.
string
Maximum
length: 127
server-cert-ca
Mandatory CA on FortiGate in certificate chain of
server.
string
Maximum
length: 79
source-ip
Source IPv4 or IPv6 address used to communicate
with FortiAnalyzer.
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
FortiOS 8.0.0 CLI Reference
946
Fortinet Inc.

<!-- 来源页 947 -->
Parameter
Description
Type
Size
Default
status
Enable/disable logging to FortiAnalyzer.
option
-disable
Option
Description
enable
Enable logging to FortiAnalyzer.
disable
Disable logging to FortiAnalyzer.
upload-day
Day of week (month) to upload logs.
user
Not
Specified
upload-interval
Frequency to upload log files to FortiAnalyzer.
option
-daily
Option
Description
daily
Upload log files to FortiAnalyzer once a day.
weekly
Upload log files to FortiAnalyzer once a week.
monthly
Upload log files to FortiAnalyzer once a month.
upload-option
Enable/disable logging to hard disk and then
uploading to FortiAnalyzer.
option
-5-minute
Option
Description
store-and-upload
Log to hard disk and then upload to FortiAnalyzer.
realtime
Log directly to FortiAnalyzer in real time.
1-minute
Log directly to FortiAnalyzer at least every 1 minute.
5-minute
Log directly to FortiAnalyzer at least every 5 minutes.
upload-time
Time to upload logs (hh:mm).
user
Not
Specified
vrf-select
VRF ID used for connection to server.
integer
Minimum
value: 0
Maximum
value: 511
0
** Values may differ between models.
config log fortianalyzer3 filter
Filters for FortiAnalyzer.
config log fortianalyzer3 filter
Description: Filters for FortiAnalyzer.
FortiOS 8.0.0 CLI Reference
947
Fortinet Inc.

<!-- 来源页 948 -->
set anomaly [enable|disable]
set dlp-archive [enable|disable]
set forti-switch [enable|disable]
set forward-traffic [enable|disable]
config free-style
Description: Free style filters.
edit <id>
set category [traffic|event|...]
set filter {string}
set filter-type [include|exclude]
next
end
set gtp [enable|disable]
set http-transaction [enable|disable]
set local-traffic [enable|disable]
set multicast-traffic [enable|disable]
set severity [emergency|alert|...]
set sniffer-traffic [enable|disable]
set voip [enable|disable]
set ztna-traffic [enable|disable]
end
config log fortianalyzer3 filter
Parameter
Description
Type
Size
Default
anomaly
Enable/disable anomaly logging.
option
-enable
Option
Description
enable
Enable anomaly logging.
disable
Disable anomaly logging.
dlp-archive
Enable/disable DLP archive logging.
option
-enable
Option
Description
enable
Enable DLP archive logging.
disable
Disable DLP archive logging.
forti-switch
Enable/disable Forti-Switch logging.
option
-enable
Option
Description
enable
Enable Forti-Switch logging.
disable
Disable Forti-Switch logging.
forward-traffic
Enable/disable forward traffic logging.
option
-enable
FortiOS 8.0.0 CLI Reference
948
Fortinet Inc.

<!-- 来源页 949 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable forward traffic logging.
disable
Disable forward traffic logging.
gtp *
Enable/disable GTP messages logging.
option
-enable
Option
Description
enable
Enable GTP messages logging.
disable
Disable GTP messages logging.
http-transaction
Enable/disable log HTTP transaction messages.
option
-enable
Option
Description
enable
Enable http transaction logging.
disable
Disable http transaction logging.
local-traffic
Enable/disable local in or out traffic logging.
option
-enable
Option
Description
enable
Enable local in or out traffic logging.
disable
Disable local in or out traffic logging.
multicast-traffic
Enable/disable multicast traffic logging.
option
-enable
Option
Description
enable
Enable multicast traffic logging.
disable
Disable multicast traffic logging.
severity
Lowest severity level to log.
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
FortiOS 8.0.0 CLI Reference
949
Fortinet Inc.

<!-- 来源页 950 -->
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
sniffer-traffic
Enable/disable sniffer traffic logging.
option
-enable
Option
Description
enable
Enable sniffer traffic logging.
disable
Disable sniffer traffic logging.
voip
Enable/disable VoIP logging.
option
-enable
Option
Description
enable
Enable VoIP logging.
disable
Disable VoIP logging.
ztna-traffic
Enable/disable ztna traffic logging.
option
-enable
Option
Description
enable
Enable ztna traffic logging.
disable
Disable ztna traffic logging.
* This parameter may not exist in some models.
config free-style
Parameter
Description
Type
Size
Default
category
Log category.
option
-traffic
Option
Description
traffic
Traffic log.
event
Event log.
virus
Antivirus log.
webfilter
Web filter log.
attack
Attack log.
spam
Antispam log.
FortiOS 8.0.0 CLI Reference
950
Fortinet Inc.

<!-- 来源页 951 -->
Parameter
Description
Type
Size
Default
Option
Description
anomaly
Anomaly log.
voip
VoIP log.
dlp
DLP log.
app-ctrl
Application control log.
waf
Web application firewall log.
dns
DNS detail log.
ssh
SSH log.
ssl
SSL log.
file-filter
File filter log.
icap
ICAP log.
virtual-patch
Virtual patch log.
debug
Debug log.
filter
Free style filter string.
string
Maximum
length: 1023
filter-type
Include/exclude logs that match the filter.
option
-include
Option
Description
include
Include logs that match the filter.
exclude
Exclude logs that match the filter.
id
Entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config log fortianalyzer3 override-filter
Override filters for FortiAnalyzer.
config log fortianalyzer3 override-filter
Description: Override filters for FortiAnalyzer.
set anomaly [enable|disable]
set dlp-archive [enable|disable]
set forti-switch [enable|disable]
set forward-traffic [enable|disable]
config free-style
FortiOS 8.0.0 CLI Reference
951
Fortinet Inc.

<!-- 来源页 952 -->
Description: Free style filters.
edit <id>
set category [traffic|event|...]
set filter {string}
set filter-type [include|exclude]
next
end
set gtp [enable|disable]
set http-transaction [enable|disable]
set local-traffic [enable|disable]
set multicast-traffic [enable|disable]
set severity [emergency|alert|...]
set sniffer-traffic [enable|disable]
set voip [enable|disable]
set ztna-traffic [enable|disable]
end
config log fortianalyzer3 override-filter
Parameter
Description
Type
Size
Default
anomaly
Enable/disable anomaly logging.
option
-enable
Option
Description
enable
Enable anomaly logging.
disable
Disable anomaly logging.
dlp-archive
Enable/disable DLP archive logging.
option
-enable
Option
Description
enable
Enable DLP archive logging.
disable
Disable DLP archive logging.
forti-switch
Enable/disable Forti-Switch logging.
option
-enable
Option
Description
enable
Enable Forti-Switch logging.
disable
Disable Forti-Switch logging.
forward-traffic
Enable/disable forward traffic logging.
option
-enable
Option
Description
enable
Enable forward traffic logging.
disable
Disable forward traffic logging.
FortiOS 8.0.0 CLI Reference
952
Fortinet Inc.

<!-- 来源页 953 -->
Parameter
Description
Type
Size
Default
gtp *
Enable/disable GTP messages logging.
option
-enable
Option
Description
enable
Enable GTP messages logging.
disable
Disable GTP messages logging.
http-transaction
Enable/disable log HTTP transaction messages.
option
-enable
Option
Description
enable
Enable http transaction logging.
disable
Disable http transaction logging.
local-traffic
Enable/disable local in or out traffic logging.
option
-enable
Option
Description
enable
Enable local in or out traffic logging.
disable
Disable local in or out traffic logging.
multicast-traffic
Enable/disable multicast traffic logging.
option
-enable
Option
Description
enable
Enable multicast traffic logging.
disable
Disable multicast traffic logging.
severity
Lowest severity level to log.
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
sniffer-traffic
Enable/disable sniffer traffic logging.
option
-enable
FortiOS 8.0.0 CLI Reference
953
Fortinet Inc.

<!-- 来源页 954 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable sniffer traffic logging.
disable
Disable sniffer traffic logging.
voip
Enable/disable VoIP logging.
option
-enable
Option
Description
enable
Enable VoIP logging.
disable
Disable VoIP logging.
ztna-traffic
Enable/disable ztna traffic logging.
option
-enable
Option
Description
enable
Enable ztna traffic logging.
disable
Disable ztna traffic logging.
* This parameter may not exist in some models.
config free-style
Parameter
Description
Type
Size
Default
category
Log category.
option
-traffic
Option
Description
traffic
Traffic log.
event
Event log.
virus
Antivirus log.
webfilter
Web filter log.
attack
Attack log.
spam
Antispam log.
anomaly
Anomaly log.
voip
VoIP log.
dlp
DLP log.
app-ctrl
Application control log.
waf
Web application firewall log.
FortiOS 8.0.0 CLI Reference
954
Fortinet Inc.

<!-- 来源页 955 -->
Parameter
Description
Type
Size
Default
Option
Description
dns
DNS detail log.
ssh
SSH log.
ssl
SSL log.
file-filter
File filter log.
icap
ICAP log.
virtual-patch
Virtual patch log.
debug
Debug log.
filter
Free style filter string.
string
Maximum
length: 1023
filter-type
Include/exclude logs that match the filter.
option
-include
Option
Description
include
Include logs that match the filter.
exclude
Exclude logs that match the filter.
id
Entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config log fortianalyzer3 override-setting
Override FortiAnalyzer settings.
config log fortianalyzer3 override-setting
Description: Override FortiAnalyzer settings.
set access-config [enable|disable]
set alt-server {string}
set certificate {string}
set certificate-verification [enable|disable]
set conn-timeout {integer}
set enc-algorithm [high-medium|high|...]
set fallback-to-primary [enable|disable]
set hmac-algorithm {option}
set interface {string}
set interface-select-method [auto|sdwan|...]
set ips-archive [enable|disable]
set max-log-rate {integer}
set monitor-failure-retry-period {integer}
FortiOS 8.0.0 CLI Reference
955
Fortinet Inc.

<!-- 来源页 956 -->
set monitor-keepalive-period {integer}
set preshared-key {password}
set priority [default|low]
set reliable [enable|disable]
set serial <name1>, <name2>, ...
set server {string}
set server-cert-ca {string}
set source-ip {string}
set ssl-min-proto-version [default|SSLv3|...]
set status [enable|disable]
set upload-day {user}
set upload-interval [daily|weekly|...]
set upload-option [store-and-upload|realtime|...]
set upload-time {user}
set use-management-vdom [enable|disable]
set vrf-select {integer}
end
config log fortianalyzer3 override-setting
Parameter
Description
Type
Size
Default
access-config
Enable/disable FortiAnalyzer access to
configuration and data.
option
-enable
Option
Description
enable
Enable FortiAnalyzer access to configuration and data.
disable
Disable FortiAnalyzer access to configuration and data.
alt-server
Alternate FortiAnalyzer.
string
Maximum
length: 127
certificate
Certificate used to communicate with
FortiAnalyzer.
string
Maximum
length: 35
certificate-verification
Enable/disable identity verification of
FortiAnalyzer by use of certificate.
option
-enable
Option
Description
enable
Enable identity verification of FortiAnalyzer by use of certificate.
disable
Disable identity verification of FortiAnalyzer by use of certificate.
conn-timeout
FortiAnalyzer connection time-out in seconds
(for status and log buffer).
integer
Minimum
value: 1
Maximum
value: 3600
10
FortiOS 8.0.0 CLI Reference
956
Fortinet Inc.

<!-- 来源页 957 -->
Parameter
Description
Type
Size
Default
enc-algorithm
Configure the level of SSL protection for secure
communication with FortiAnalyzer.
option
-high
Option
Description
high-medium
Encrypt logs using high and medium encryption algorithms.
high
Encrypt logs using high encryption algorithms.
low
Encrypt logs using all encryption algorithms.
fallback-to-primary
Enable/disable this FortiGate unit to fallback to
the primary FortiAnalyzer when it is available.
option
-enable
Option
Description
enable
Enable this FortiGate unit to fallback to the primary FortiAnalyzer
when it is available.
disable
Disable this FortiGate unit to fallback to the primary FortiAnalyzer
when it is available.
hmac-algorithm
OFTP login hash algorithm.
option
-sha256
Option
Description
sha256
Use SHA256 as HMAC algorithm.
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
ips-archive
Enable/disable IPS packet archive logging.
option
-enable
Option
Description
enable
Enable IPS packet archive logging.
disable
Disable IPS packet archive logging.
FortiOS 8.0.0 CLI Reference
957
Fortinet Inc.

<!-- 来源页 958 -->
Parameter
Description
Type
Size
Default
max-log-rate
FortiAnalyzer maximum log rate in MBps (0 =
unlimited).
integer
Minimum
value: 0
Maximum
value:
100000
0
monitor-failure-retry-period
Time between FortiAnalyzer connection retries
in seconds (for status and log buffer).
integer
Minimum
value: 1
Maximum
value:
86400
5
monitor-keepalive-period
Time between OFTP keepalives in seconds (for
status and log buffer).
integer
Minimum
value: 1
Maximum
value: 120
5
preshared-key
Preshared-key used for auto-authorization on
FortiAnalyzer.
password
**
Not
Specified **
priority
Set log transmission priority.
option
-default
Option
Description
default
Set FortiAnalyzer log transmission priority to default.
low
Set FortiAnalyzer log transmission priority to low.
reliable
Enable/disable reliable logging to FortiAnalyzer.
option
-disable
Option
Description
enable
Enable reliable logging to FortiAnalyzer.
disable
Disable reliable logging to FortiAnalyzer.
serial <name>
Serial numbers of the FortiAnalyzer.
Serial Number.
string
Maximum
length: 79
server
The remote FortiAnalyzer.
string
Maximum
length: 127
server-cert-ca
Mandatory CA on FortiGate in certificate chain
of server.
string
Maximum
length: 79
source-ip
Source IPv4 or IPv6 address used to
communicate with FortiAnalyzer.
string
Maximum
length: 63
ssl-min-proto-version
Minimum supported protocol version for
SSL/TLS connections (default is to follow
system global setting).
option
-default
FortiOS 8.0.0 CLI Reference
958
Fortinet Inc.

<!-- 来源页 959 -->
Parameter
Description
Type
Size
Default
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
Enable/disable logging to FortiAnalyzer.
option
-disable
Option
Description
enable
Enable logging to FortiAnalyzer.
disable
Disable logging to FortiAnalyzer.
upload-day
Day of week (month) to upload logs.
user
Not
Specified
upload-interval
Frequency to upload log files to FortiAnalyzer.
option
-daily
Option
Description
daily
Upload log files to FortiAnalyzer once a day.
weekly
Upload log files to FortiAnalyzer once a week.
monthly
Upload log files to FortiAnalyzer once a month.
upload-option
Enable/disable logging to hard disk and then
uploading to FortiAnalyzer.
option
-5-minute
Option
Description
store-and-upload
Log to hard disk and then upload to FortiAnalyzer.
realtime
Log directly to FortiAnalyzer in real time.
1-minute
Log directly to FortiAnalyzer at least every 1 minute.
5-minute
Log directly to FortiAnalyzer at least every 5 minutes.
upload-time
Time to upload logs (hh:mm).
user
Not
Specified
use-management-vdom
Enable/disable use of management VDOM IP
address as source IP for logs sent to
FortiAnalyzer.
option
-disable
FortiOS 8.0.0 CLI Reference
959
Fortinet Inc.

<!-- 来源页 960 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable use of management VDOM IP address as source IP for logs
sent to FortiAnalyzer.
disable
Disable use of management VDOM IP address as source IP for logs
sent to FortiAnalyzer.
vrf-select
VRF ID used for connection to server.
integer
Minimum
value: 0
Maximum
value: 511
0
** Values may differ between models.
config log fortianalyzer3 setting
Global FortiAnalyzer settings.
config log fortianalyzer3 setting
Description: Global FortiAnalyzer settings.
set access-config [enable|disable]
set alt-server {string}
set certificate {string}
set certificate-verification [enable|disable]
set conn-timeout {integer}
set enc-algorithm [high-medium|high|...]
set fallback-to-primary [enable|disable]
set hmac-algorithm {option}
set interface {string}
set interface-select-method [auto|sdwan|...]
set ips-archive [enable|disable]
set max-log-rate {integer}
set monitor-failure-retry-period {integer}
set monitor-keepalive-period {integer}
set preshared-key {password}
set priority [default|low]
set reliable [enable|disable]
set serial <name1>, <name2>, ...
set server {string}
set server-cert-ca {string}
set source-ip {string}
set ssl-min-proto-version [default|SSLv3|...]
set status [enable|disable]
set upload-day {user}
set upload-interval [daily|weekly|...]
set upload-option [store-and-upload|realtime|...]
set upload-time {user}
FortiOS 8.0.0 CLI Reference
960
Fortinet Inc.

<!-- 来源页 961 -->
set vrf-select {integer}
end
config log fortianalyzer3 setting
Parameter
Description
Type
Size
Default
access-config
Enable/disable FortiAnalyzer access to
configuration and data.
option
-enable
Option
Description
enable
Enable FortiAnalyzer access to configuration and data.
disable
Disable FortiAnalyzer access to configuration and data.
alt-server
Alternate FortiAnalyzer.
string
Maximum
length: 127
certificate
Certificate used to communicate with
FortiAnalyzer.
string
Maximum
length: 35
certificate-verification
Enable/disable identity verification of
FortiAnalyzer by use of certificate.
option
-enable
Option
Description
enable
Enable identity verification of FortiAnalyzer by use of certificate.
disable
Disable identity verification of FortiAnalyzer by use of certificate.
conn-timeout
FortiAnalyzer connection time-out in seconds (for
status and log buffer).
integer
Minimum
value: 1
Maximum
value: 3600
10
enc-algorithm
Configure the level of SSL protection for secure
communication with FortiAnalyzer.
option
-high
Option
Description
high-medium
Encrypt logs using high and medium encryption algorithms.
high
Encrypt logs using high encryption algorithms.
low
Encrypt logs using all encryption algorithms.
fallback-to-primary
Enable/disable this FortiGate unit to fallback to the
primary FortiAnalyzer when it is available.
option
-enable
FortiOS 8.0.0 CLI Reference
961
Fortinet Inc.

<!-- 来源页 962 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable this FortiGate unit to fallback to the primary FortiAnalyzer when it
is available.
disable
Disable this FortiGate unit to fallback to the primary FortiAnalyzer when
it is available.
hmac-algorithm
OFTP login hash algorithm.
option
-sha256
Option
Description
sha256
Use SHA256 as HMAC algorithm.
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
ips-archive
Enable/disable IPS packet archive logging.
option
-enable
Option
Description
enable
Enable IPS packet archive logging.
disable
Disable IPS packet archive logging.
max-log-rate
FortiAnalyzer maximum log rate in MBps (0 =
unlimited).
integer
Minimum
value: 0
Maximum
value:
100000
0
monitor-failure-retry-period
Time between FortiAnalyzer connection retries in
seconds (for status and log buffer).
integer
Minimum
value: 1
Maximum
value:
86400
5
FortiOS 8.0.0 CLI Reference
962
Fortinet Inc.

<!-- 来源页 963 -->
Parameter
Description
Type
Size
Default
monitor-keepalive-period
Time between OFTP keepalives in seconds (for
status and log buffer).
integer
Minimum
value: 1
Maximum
value: 120
5
preshared-key
Preshared-key used for auto-authorization on
FortiAnalyzer.
password
**
Not
Specified **
priority
Set log transmission priority.
option
-default
Option
Description
default
Set FortiAnalyzer log transmission priority to default.
low
Set FortiAnalyzer log transmission priority to low.
reliable
Enable/disable reliable logging to FortiAnalyzer.
option
-disable
Option
Description
enable
Enable reliable logging to FortiAnalyzer.
disable
Disable reliable logging to FortiAnalyzer.
serial <name>
Serial numbers of the FortiAnalyzer.
Serial Number.
string
Maximum
length: 79
server
The remote FortiAnalyzer.
string
Maximum
length: 127
server-cert-ca
Mandatory CA on FortiGate in certificate chain of
server.
string
Maximum
length: 79
source-ip
Source IPv4 or IPv6 address used to communicate
with FortiAnalyzer.
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
FortiOS 8.0.0 CLI Reference
963
Fortinet Inc.

<!-- 来源页 964 -->
Parameter
Description
Type
Size
Default
status
Enable/disable logging to FortiAnalyzer.
option
-disable
Option
Description
enable
Enable logging to FortiAnalyzer.
disable
Disable logging to FortiAnalyzer.
upload-day
Day of week (month) to upload logs.
user
Not
Specified
upload-interval
Frequency to upload log files to FortiAnalyzer.
option
-daily
Option
Description
daily
Upload log files to FortiAnalyzer once a day.
weekly
Upload log files to FortiAnalyzer once a week.
monthly
Upload log files to FortiAnalyzer once a month.
upload-option
Enable/disable logging to hard disk and then
uploading to FortiAnalyzer.
option
-5-minute
Option
Description
store-and-upload
Log to hard disk and then upload to FortiAnalyzer.
realtime
Log directly to FortiAnalyzer in real time.
1-minute
Log directly to FortiAnalyzer at least every 1 minute.
5-minute
Log directly to FortiAnalyzer at least every 5 minutes.
upload-time
Time to upload logs (hh:mm).
user
Not
Specified
vrf-select
VRF ID used for connection to server.
integer
Minimum
value: 0
Maximum
value: 511
0
** Values may differ between models.
config log fortianalyzer-cloud filter
Filters for FortiAnalyzer Cloud.
config log fortianalyzer-cloud filter
Description: Filters for FortiAnalyzer Cloud.
FortiOS 8.0.0 CLI Reference
964
Fortinet Inc.

<!-- 来源页 965 -->
set anomaly [enable|disable]
set dlp-archive [enable|disable]
set forti-switch [enable|disable]
set forward-traffic [enable|disable]
config free-style
Description: Free style filters.
edit <id>
set category [traffic|event|...]
set filter {string}
set filter-type [include|exclude]
next
end
set gtp [enable|disable]
set http-transaction [enable|disable]
set local-traffic [enable|disable]
set multicast-traffic [enable|disable]
set severity [emergency|alert|...]
set sniffer-traffic [enable|disable]
set voip [enable|disable]
set ztna-traffic [enable|disable]
end
config log fortianalyzer-cloud filter
Parameter
Description
Type
Size
Default
anomaly
Enable/disable anomaly logging.
option
-enable
Option
Description
enable
Enable anomaly logging.
disable
Disable anomaly logging.
dlp-archive
Enable/disable DLP archive logging.
option
-disable
Option
Description
enable
Enable DLP archive logging.
disable
Disable DLP archive logging.
forti-switch
Enable/disable Forti-Switch logging.
option
-enable
Option
Description
enable
Enable Forti-Switch logging.
disable
Disable Forti-Switch logging.
forward-traffic
Enable/disable forward traffic logging.
option
-enable
FortiOS 8.0.0 CLI Reference
965
Fortinet Inc.

<!-- 来源页 966 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable forward traffic logging.
disable
Disable forward traffic logging.
gtp *
Enable/disable GTP messages logging.
option
-enable
Option
Description
enable
Enable GTP messages logging.
disable
Disable GTP messages logging.
http-transaction
Enable/disable log HTTP transaction messages.
option
-enable
Option
Description
enable
Enable http transaction logging.
disable
Disable http transaction logging.
local-traffic
Enable/disable local in or out traffic logging.
option
-enable
Option
Description
enable
Enable local in or out traffic logging.
disable
Disable local in or out traffic logging.
multicast-traffic
Enable/disable multicast traffic logging.
option
-enable
Option
Description
enable
Enable multicast traffic logging.
disable
Disable multicast traffic logging.
severity
Lowest severity level to log.
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
FortiOS 8.0.0 CLI Reference
966
Fortinet Inc.

<!-- 来源页 967 -->
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
sniffer-traffic
Enable/disable sniffer traffic logging.
option
-enable
Option
Description
enable
Enable sniffer traffic logging.
disable
Disable sniffer traffic logging.
voip
Enable/disable VoIP logging.
option
-enable
Option
Description
enable
Enable VoIP logging.
disable
Disable VoIP logging.
ztna-traffic
Enable/disable ztna traffic logging.
option
-enable
Option
Description
enable
Enable ztna traffic logging.
disable
Disable ztna traffic logging.
* This parameter may not exist in some models.
config free-style
Parameter
Description
Type
Size
Default
category
Log category.
option
-traffic
Option
Description
traffic
Traffic log.
event
Event log.
virus
Antivirus log.
webfilter
Web filter log.
attack
Attack log.
spam
Antispam log.
FortiOS 8.0.0 CLI Reference
967
Fortinet Inc.

<!-- 来源页 968 -->
Parameter
Description
Type
Size
Default
Option
Description
anomaly
Anomaly log.
voip
VoIP log.
dlp
DLP log.
app-ctrl
Application control log.
waf
Web application firewall log.
dns
DNS detail log.
ssh
SSH log.
ssl
SSL log.
file-filter
File filter log.
icap
ICAP log.
virtual-patch
Virtual patch log.
debug
Debug log.
filter
Free style filter string.
string
Maximum
length: 1023
filter-type
Include/exclude logs that match the filter.
option
-include
Option
Description
include
Include logs that match the filter.
exclude
Exclude logs that match the filter.
id
Entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config log fortianalyzer-cloud override-filter
Override filters for FortiAnalyzer Cloud.
config log fortianalyzer-cloud override-filter
Description: Override filters for FortiAnalyzer Cloud.
set anomaly [enable|disable]
set dlp-archive [enable|disable]
set forti-switch [enable|disable]
set forward-traffic [enable|disable]
config free-style
FortiOS 8.0.0 CLI Reference
968
Fortinet Inc.

<!-- 来源页 969 -->
Description: Free style filters.
edit <id>
set category [traffic|event|...]
set filter {string}
set filter-type [include|exclude]
next
end
set gtp [enable|disable]
set http-transaction [enable|disable]
set local-traffic [enable|disable]
set multicast-traffic [enable|disable]
set severity [emergency|alert|...]
set sniffer-traffic [enable|disable]
set voip [enable|disable]
set ztna-traffic [enable|disable]
end
config log fortianalyzer-cloud override-filter
Parameter
Description
Type
Size
Default
anomaly
Enable/disable anomaly logging.
option
-enable
Option
Description
enable
Enable anomaly logging.
disable
Disable anomaly logging.
dlp-archive
Enable/disable DLP archive logging.
option
-disable
Option
Description
enable
Enable DLP archive logging.
disable
Disable DLP archive logging.
forti-switch
Enable/disable Forti-Switch logging.
option
-enable
Option
Description
enable
Enable Forti-Switch logging.
disable
Disable Forti-Switch logging.
forward-traffic
Enable/disable forward traffic logging.
option
-enable
Option
Description
enable
Enable forward traffic logging.
disable
Disable forward traffic logging.
FortiOS 8.0.0 CLI Reference
969
Fortinet Inc.

<!-- 来源页 970 -->
Parameter
Description
Type
Size
Default
gtp *
Enable/disable GTP messages logging.
option
-enable
Option
Description
enable
Enable GTP messages logging.
disable
Disable GTP messages logging.
http-transaction
Enable/disable log HTTP transaction messages.
option
-enable
Option
Description
enable
Enable http transaction logging.
disable
Disable http transaction logging.
local-traffic
Enable/disable local in or out traffic logging.
option
-enable
Option
Description
enable
Enable local in or out traffic logging.
disable
Disable local in or out traffic logging.
multicast-traffic
Enable/disable multicast traffic logging.
option
-enable
Option
Description
enable
Enable multicast traffic logging.
disable
Disable multicast traffic logging.
severity
Lowest severity level to log.
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
sniffer-traffic
Enable/disable sniffer traffic logging.
option
-enable
FortiOS 8.0.0 CLI Reference
970
Fortinet Inc.

<!-- 来源页 971 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable sniffer traffic logging.
disable
Disable sniffer traffic logging.
voip
Enable/disable VoIP logging.
option
-enable
Option
Description
enable
Enable VoIP logging.
disable
Disable VoIP logging.
ztna-traffic
Enable/disable ztna traffic logging.
option
-enable
Option
Description
enable
Enable ztna traffic logging.
disable
Disable ztna traffic logging.
* This parameter may not exist in some models.
config free-style
Parameter
Description
Type
Size
Default
category
Log category.
option
-traffic
Option
Description
traffic
Traffic log.
event
Event log.
virus
Antivirus log.
webfilter
Web filter log.
attack
Attack log.
spam
Antispam log.
anomaly
Anomaly log.
voip
VoIP log.
dlp
DLP log.
app-ctrl
Application control log.
waf
Web application firewall log.
FortiOS 8.0.0 CLI Reference
971
Fortinet Inc.

<!-- 来源页 972 -->
Parameter
Description
Type
Size
Default
Option
Description
dns
DNS detail log.
ssh
SSH log.
ssl
SSL log.
file-filter
File filter log.
icap
ICAP log.
virtual-patch
Virtual patch log.
debug
Debug log.
filter
Free style filter string.
string
Maximum
length: 1023
filter-type
Include/exclude logs that match the filter.
option
-include
Option
Description
include
Include logs that match the filter.
exclude
Exclude logs that match the filter.
id
Entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config log fortianalyzer-cloud override-setting
Override FortiAnalyzer Cloud settings.
config log fortianalyzer-cloud override-setting
Description: Override FortiAnalyzer Cloud settings.
set status [enable|disable]
end
config log fortianalyzer-cloud override-setting
Parameter
Description
Type
Size
Default
status
Enable/disable logging to FortiAnalyzer Cloud.
option
-disable
FortiOS 8.0.0 CLI Reference
972
Fortinet Inc.

<!-- 来源页 973 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable logging to FortiAnalyzer Cloud.
disable
Disable logging to FortiAnalyzer Cloud.
config log fortianalyzer-cloud setting
Global FortiAnalyzer Cloud settings.
config log fortianalyzer-cloud setting
Description: Global FortiAnalyzer Cloud settings.
set access-config [enable|disable]
set certificate {string}
set certificate-verification [enable|disable]
set conn-timeout {integer}
set enc-algorithm [high-medium|high|...]
set hmac-algorithm {option}
set interface {string}
set interface-select-method [auto|sdwan|...]
set ips-archive [enable|disable]
set max-log-rate {integer}
set monitor-failure-retry-period {integer}
set monitor-keepalive-period {integer}
set preshared-key {password}
set priority [default|low]
set serial <name1>, <name2>, ...
set source-ip {string}
set ssl-min-proto-version [default|SSLv3|...]
set status [enable|disable]
set upload-day {user}
set upload-interval [daily|weekly|...]
set upload-option [store-and-upload|realtime|...]
set upload-time {user}
set vrf-select {integer}
end
config log fortianalyzer-cloud setting
Parameter
Description
Type
Size
Default
access-config
Enable/disable FortiAnalyzer access to
configuration and data.
option
-enable
FortiOS 8.0.0 CLI Reference
973
Fortinet Inc.

<!-- 来源页 974 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable FortiAnalyzer access to configuration and data.
disable
Disable FortiAnalyzer access to configuration and data.
certificate
Certificate used to communicate with
FortiAnalyzer.
string
Maximum
length: 35
certificate-verification
Enable/disable identity verification of
FortiAnalyzer by use of certificate.
option
-enable
Option
Description
enable
Enable identity verification of FortiAnalyzer by use of certificate.
disable
Disable identity verification of FortiAnalyzer by use of certificate.
conn-timeout
FortiAnalyzer connection time-out in seconds (for
status and log buffer).
integer
Minimum
value: 1
Maximum
value: 3600
10
enc-algorithm
Configure the level of SSL protection for secure
communication with FortiAnalyzer.
option
-high
Option
Description
high-medium
Encrypt logs using high and medium encryption algorithms.
high
Encrypt logs using high encryption algorithms.
low
Encrypt logs using all encryption algorithms.
hmac-algorithm
OFTP login hash algorithm.
option
-sha256
Option
Description
sha256
Use SHA256 as HMAC algorithm.
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
974
Fortinet Inc.

<!-- 来源页 975 -->
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
ips-archive
Enable/disable IPS packet archive logging.
option
-disable
Option
Description
enable
Enable IPS packet archive logging.
disable
Disable IPS packet archive logging.
max-log-rate
FortiAnalyzer maximum log rate in MBps (0 =
unlimited).
integer
Minimum
value: 0
Maximum
value:
100000
0
monitor-failure-retry-period
Time between FortiAnalyzer connection retries in
seconds (for status and log buffer).
integer
Minimum
value: 1
Maximum
value:
86400
5
monitor-keepalive-period
Time between OFTP keepalives in seconds (for
status and log buffer).
integer
Minimum
value: 1
Maximum
value: 120
5
preshared-key
Preshared-key used for auto-authorization on
FortiAnalyzer.
password
**
Not
Specified **
priority
Set log transmission priority.
option
-default
Option
Description
default
Set FortiAnalyzer log transmission priority to default.
low
Set FortiAnalyzer log transmission priority to low.
serial <name>
Serial numbers of the FortiAnalyzer.
Serial Number.
string
Maximum
length: 79
source-ip
Source IPv4 or IPv6 address used to communicate
with FortiAnalyzer.
string
Maximum
length: 63
ssl-min-proto-version
Minimum supported protocol version for SSL/TLS
connections (default is to follow system global
setting).
option
-default
FortiOS 8.0.0 CLI Reference
975
Fortinet Inc.

<!-- 来源页 976 -->
Parameter
Description
Type
Size
Default
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
Enable/disable logging to FortiAnalyzer Cloud.
option
-disable
Option
Description
enable
Enable logging to FortiAnalyzer Cloud.
disable
Disable logging to FortiAnalyzer Cloud.
upload-day
Day of week (month) to upload logs.
user
Not
Specified
upload-interval
Frequency to upload log files to FortiAnalyzer.
option
-daily
Option
Description
daily
Upload log files to FortiAnalyzer once a day.
weekly
Upload log files to FortiAnalyzer once a week.
monthly
Upload log files to FortiAnalyzer once a month.
upload-option
Enable/disable logging to hard disk and then
uploading to FortiAnalyzer.
option
-5-minute
Option
Description
store-and-upload
Log to hard disk and then upload to FortiAnalyzer.
realtime
Log directly to FortiAnalyzer in real time.
1-minute
Log directly to FortiAnalyzer at least every 1 minute.
5-minute
Log directly to FortiAnalyzer at least every 5 minutes.
upload-time
Time to upload logs (hh:mm).
user
Not
Specified
FortiOS 8.0.0 CLI Reference
976
Fortinet Inc.

<!-- 来源页 977 -->
Parameter
Description
Type
Size
Default
vrf-select
VRF ID used for connection to server.
integer
Minimum
value: 0
Maximum
value: 511
0
** Values may differ between models.
config log fortiguard filter
Filters for FortiCloud.
config log fortiguard filter
Description: Filters for FortiCloud.
set anomaly [enable|disable]
set forti-switch [enable|disable]
set forward-traffic [enable|disable]
config free-style
Description: Free style filters.
edit <id>
set category [traffic|event|...]
set filter {string}
set filter-type [include|exclude]
next
end
set gtp [enable|disable]
set http-transaction [enable|disable]
set local-traffic [enable|disable]
set multicast-traffic [enable|disable]
set severity [emergency|alert|...]
set sniffer-traffic [enable|disable]
set voip [enable|disable]
set ztna-traffic [enable|disable]
end
config log fortiguard filter
Parameter
Description
Type
Size
Default
anomaly
Enable/disable anomaly logging.
option
-enable
Option
Description
enable
Enable anomaly logging.
disable
Disable anomaly logging.
forti-switch
Enable/disable Forti-Switch logging.
option
-enable
FortiOS 8.0.0 CLI Reference
977
Fortinet Inc.

<!-- 来源页 978 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable Forti-Switch logging.
disable
Disable Forti-Switch logging.
forward-traffic
Enable/disable forward traffic logging.
option
-enable
Option
Description
enable
Enable forward traffic logging.
disable
Disable forward traffic logging.
gtp *
Enable/disable GTP messages logging.
option
-enable
Option
Description
enable
Enable GTP messages logging.
disable
Disable GTP messages logging.
http-transaction
Enable/disable log HTTP transaction messages.
option
-enable
Option
Description
enable
Enable http transaction logging.
disable
Disable http transaction logging.
local-traffic
Enable/disable local in or out traffic logging.
option
-enable
Option
Description
enable
Enable local in or out traffic logging.
disable
Disable local in or out traffic logging.
multicast-traffic
Enable/disable multicast traffic logging.
option
-enable
Option
Description
enable
Enable multicast traffic logging.
disable
Disable multicast traffic logging.
severity
Lowest severity level to log.
option
-information
FortiOS 8.0.0 CLI Reference
978
Fortinet Inc.

<!-- 来源页 979 -->
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
sniffer-traffic
Enable/disable sniffer traffic logging.
option
-enable
Option
Description
enable
Enable sniffer traffic logging.
disable
Disable sniffer traffic logging.
voip
Enable/disable VoIP logging.
option
-enable
Option
Description
enable
Enable VoIP logging.
disable
Disable VoIP logging.
ztna-traffic
Enable/disable ztna traffic logging.
option
-enable
Option
Description
enable
Enable ztna traffic logging.
disable
Disable ztna traffic logging.
* This parameter may not exist in some models.
config free-style
Parameter
Description
Type
Size
Default
category
Log category.
option
-traffic
Option
Description
traffic
Traffic log.
FortiOS 8.0.0 CLI Reference
979
Fortinet Inc.

<!-- 来源页 980 -->
Parameter
Description
Type
Size
Default
Option
Description
event
Event log.
virus
Antivirus log.
webfilter
Web filter log.
attack
Attack log.
spam
Antispam log.
anomaly
Anomaly log.
voip
VoIP log.
dlp
DLP log.
app-ctrl
Application control log.
waf
Web application firewall log.
dns
DNS detail log.
ssh
SSH log.
ssl
SSL log.
file-filter
File filter log.
icap
ICAP log.
virtual-patch
Virtual patch log.
debug
Debug log.
filter
Free style filter string.
string
Maximum
length: 1023
filter-type
Include/exclude logs that match the filter.
option
-include
Option
Description
include
Include logs that match the filter.
exclude
Exclude logs that match the filter.
id
Entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config log fortiguard override-filter
Override filters for FortiCloud.
FortiOS 8.0.0 CLI Reference
980
Fortinet Inc.

<!-- 来源页 981 -->
config log fortiguard override-filter
Description: Override filters for FortiCloud.
set anomaly [enable|disable]
set forti-switch [enable|disable]
set forward-traffic [enable|disable]
config free-style
Description: Free style filters.
edit <id>
set category [traffic|event|...]
set filter {string}
set filter-type [include|exclude]
next
end
set gtp [enable|disable]
set http-transaction [enable|disable]
set local-traffic [enable|disable]
set multicast-traffic [enable|disable]
set severity [emergency|alert|...]
set sniffer-traffic [enable|disable]
set voip [enable|disable]
set ztna-traffic [enable|disable]
end
config log fortiguard override-filter
Parameter
Description
Type
Size
Default
anomaly
Enable/disable anomaly logging.
option
-enable
Option
Description
enable
Enable anomaly logging.
disable
Disable anomaly logging.
forti-switch
Enable/disable Forti-Switch logging.
option
-enable
Option
Description
enable
Enable Forti-Switch logging.
disable
Disable Forti-Switch logging.
forward-traffic
Enable/disable forward traffic logging.
option
-enable
Option
Description
enable
Enable forward traffic logging.
disable
Disable forward traffic logging.
FortiOS 8.0.0 CLI Reference
981
Fortinet Inc.

<!-- 来源页 982 -->
Parameter
Description
Type
Size
Default
gtp *
Enable/disable GTP messages logging.
option
-enable
Option
Description
enable
Enable GTP messages logging.
disable
Disable GTP messages logging.
http-transaction
Enable/disable log HTTP transaction messages.
option
-enable
Option
Description
enable
Enable http transaction logging.
disable
Disable http transaction logging.
local-traffic
Enable/disable local in or out traffic logging.
option
-enable
Option
Description
enable
Enable local in or out traffic logging.
disable
Disable local in or out traffic logging.
multicast-traffic
Enable/disable multicast traffic logging.
option
-enable
Option
Description
enable
Enable multicast traffic logging.
disable
Disable multicast traffic logging.
severity
Lowest severity level to log.
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
sniffer-traffic
Enable/disable sniffer traffic logging.
option
-enable
FortiOS 8.0.0 CLI Reference
982
Fortinet Inc.

<!-- 来源页 983 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable sniffer traffic logging.
disable
Disable sniffer traffic logging.
voip
Enable/disable VoIP logging.
option
-enable
Option
Description
enable
Enable VoIP logging.
disable
Disable VoIP logging.
ztna-traffic
Enable/disable ztna traffic logging.
option
-enable
Option
Description
enable
Enable ztna traffic logging.
disable
Disable ztna traffic logging.
* This parameter may not exist in some models.
config free-style
Parameter
Description
Type
Size
Default
category
Log category.
option
-traffic
Option
Description
traffic
Traffic log.
event
Event log.
virus
Antivirus log.
webfilter
Web filter log.
attack
Attack log.
spam
Antispam log.
anomaly
Anomaly log.
voip
VoIP log.
dlp
DLP log.
app-ctrl
Application control log.
waf
Web application firewall log.
FortiOS 8.0.0 CLI Reference
983
Fortinet Inc.

<!-- 来源页 984 -->
Parameter
Description
Type
Size
Default
Option
Description
dns
DNS detail log.
ssh
SSH log.
ssl
SSL log.
file-filter
File filter log.
icap
ICAP log.
virtual-patch
Virtual patch log.
debug
Debug log.
filter
Free style filter string.
string
Maximum
length: 1023
filter-type
Include/exclude logs that match the filter.
option
-include
Option
Description
include
Include logs that match the filter.
exclude
Exclude logs that match the filter.
id
Entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config log fortiguard override-setting
Override global FortiCloud logging settings for this VDOM.
config log fortiguard override-setting
Description: Override global FortiCloud logging settings for this VDOM.
set access-config [enable|disable]
set max-log-rate {integer}
set override [enable|disable]
set priority [default|low]
set status [enable|disable]
set upload-day {user}
set upload-interval [daily|weekly|...]
set upload-option [store-and-upload|realtime|...]
set upload-time {user}
end
FortiOS 8.0.0 CLI Reference
984
Fortinet Inc.

<!-- 来源页 985 -->
config log fortiguard override-setting
Parameter
Description
Type
Size
Default
access-config
Enable/disable FortiCloud access to configuration
and data.
option
-enable
Option
Description
enable
Enable FortiCloud access to configuration and data.
disable
Disable FortiCloud access to configuration and data.
max-log-rate
FortiCloud maximum log rate in MBps (0 =
unlimited).
integer
Minimum
value: 0
Maximum
value:
100000
0
override
Overriding FortiCloud settings for this VDOM or use
global settings.
option
-disable
Option
Description
enable
Override FortiCloud logging settings.
disable
Use global FortiCloud logging settings.
priority
Set log transmission priority.
option
-default
Option
Description
default
Set FortiCloud log transmission priority to default.
low
Set FortiCloud log transmission priority to low.
status
Enable/disable logging to FortiCloud.
option
-disable
Option
Description
enable
Enable logging to FortiCloud.
disable
Disable logging to FortiCloud.
upload-day
Day of week to roll logs.
user
Not
Specified
upload-interval
Frequency of uploading log files to FortiCloud.
option
-daily
Option
Description
daily
Upload log files to FortiCloud once a day.
FortiOS 8.0.0 CLI Reference
985
Fortinet Inc.

<!-- 来源页 986 -->
Parameter
Description
Type
Size
Default
Option
Description
weekly
Upload log files to FortiCloud once a week.
monthly
Upload log files to FortiCloud once a month.
upload-option
Configure how log messages are sent to
FortiCloud.
option
-5-minute
Option
Description
store-and-upload
Log to the hard disk and then upload logs to FortiCloud.
realtime
Log directly to FortiCloud in real time.
1-minute
Log directly to FortiCloud at 1-minute intervals.
5-minute
Log directly to FortiCloud at 5-minute intervals.
upload-time
Time of day to roll logs (hh:mm).
user
Not
Specified
config log fortiguard setting
Configure logging to FortiCloud.
config log fortiguard setting
Description: Configure logging to FortiCloud.
set access-config [enable|disable]
set conn-timeout {integer}
set enc-algorithm [high-medium|high|...]
set interface {string}
set interface-select-method [auto|sdwan|...]
set max-log-rate {integer}
set priority [default|low]
set source-ip {ipv4-address}
set ssl-min-proto-version [default|SSLv3|...]
set status [enable|disable]
set upload-day {user}
set upload-interval [daily|weekly|...]
set upload-option [store-and-upload|realtime|...]
set upload-time {user}
set vrf-select {integer}
end
FortiOS 8.0.0 CLI Reference
986
Fortinet Inc.

<!-- 来源页 987 -->
config log fortiguard setting
Parameter
Description
Type
Size
Default
access-config
Enable/disable FortiCloud access to configuration
and data.
option
-enable
Option
Description
enable
Enable FortiCloud access to configuration and data.
disable
Disable FortiCloud access to configuration and data.
conn-timeout
FortiGate Cloud connection timeout in seconds.
integer
Minimum
value: 1
Maximum
value: 3600
10
enc-algorithm
Configure the level of SSL protection for secure
communication with FortiCloud.
option
-high
Option
Description
high-medium
Encrypt logs using high and medium encryption.
high
Encrypt logs using high encryption.
low
Encrypt logs using low encryption.
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
max-log-rate
FortiCloud maximum log rate in MBps (0 =
unlimited).
integer
Minimum
value: 0
Maximum
value:
100000
0
priority
Set log transmission priority.
option
-default
FortiOS 8.0.0 CLI Reference
987
Fortinet Inc.

<!-- 来源页 988 -->
Parameter
Description
Type
Size
Default
Option
Description
default
Set FortiCloud log transmission priority to default.
low
Set FortiCloud log transmission priority to low.
source-ip
Source IP address used to connect FortiCloud.
ipv4-address
Not
Specified
0.0.0.0
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
Enable/disable logging to FortiCloud.
option
-disable
Option
Description
enable
Enable logging to FortiCloud.
disable
Disable logging to FortiCloud.
upload-day
Day of week to roll logs.
user
Not
Specified
upload-interval
Frequency of uploading log files to FortiCloud.
option
-daily
Option
Description
daily
Upload log files to FortiCloud once a day.
weekly
Upload log files to FortiCloud once a week.
monthly
Upload log files to FortiCloud once a month.
upload-option
Configure how log messages are sent to
FortiCloud.
option
-5-minute
FortiOS 8.0.0 CLI Reference
988
Fortinet Inc.

<!-- 来源页 989 -->
Parameter
Description
Type
Size
Default
Option
Description
store-and-upload
Log to the hard disk and then upload logs to FortiCloud.
realtime
Log directly to FortiCloud in real time.
1-minute
Log directly to FortiCloud at 1-minute intervals.
5-minute
Log directly to FortiCloud at 5-minute intervals.
upload-time
Time of day to roll logs (hh:mm).
user
Not
Specified
vrf-select
VRF ID used for connection to server.
integer
Minimum
value: 0
Maximum
value: 511
0
config log gui-display
Configure how log messages are displayed on the GUI.
config log gui-display
Description: Configure how log messages are displayed on the GUI.
set fortiview-unscanned-apps [enable|disable]
set resolve-apps [enable|disable]
set resolve-hosts [enable|disable]
end
config log gui-display
Parameter
Description
Type
Size
Default
fortiview-unscanned-apps
Enable/disable showing unscanned traffic in
FortiView application charts.
option
-disable
Option
Description
enable
Enable showing unscanned traffic.
disable
Disable showing unscanned traffic.
resolve-apps
Resolve unknown applications on the GUI using
Fortinet's remote application database.
option
-enable
FortiOS 8.0.0 CLI Reference
989
Fortinet Inc.

<!-- 来源页 990 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable unknown applications on the GUI.
disable
Disable unknown applications on the GUI.
resolve-hosts
Enable/disable resolving IP addresses to hostname
in log messages on the GUI using reverse DNS
lookup.
option
-enable
Option
Description
enable
Enable resolving IP addresses to hostnames.
disable
Disable resolving IP addresses to hostnames.
config log memory filter
Filters for memory buffer.
config log memory filter
Description: Filters for memory buffer.
set anomaly [enable|disable]
set debug [enable|disable]
set forti-switch [enable|disable]
set forward-traffic [enable|disable]
config free-style
Description: Free style filters.
edit <id>
set category [traffic|event|...]
set filter {string}
set filter-type [include|exclude]
next
end
set gtp [enable|disable]
set http-transaction [enable|disable]
set local-traffic [enable|disable]
set multicast-traffic [enable|disable]
set severity [emergency|alert|...]
set sniffer-traffic [enable|disable]
set voip [enable|disable]
set ztna-traffic [enable|disable]
end
FortiOS 8.0.0 CLI Reference
990
Fortinet Inc.

<!-- 来源页 991 -->
config log memory filter
Parameter
Description
Type
Size
Default
anomaly
Enable/disable anomaly logging.
option
-enable
Option
Description
enable
Enable anomaly logging.
disable
Disable anomaly logging.
debug
Enable/disable debug logging.
option
-disable
Option
Description
enable
Enable Debug logging.
disable
Disable Debug logging.
forti-switch
Enable/disable Forti-Switch logging.
option
-enable
Option
Description
enable
Enable Forti-Switch logging.
disable
Disable Forti-Switch logging.
forward-traffic
Enable/disable forward traffic logging.
option
-enable
Option
Description
enable
Enable forward traffic logging.
disable
Disable forward traffic logging.
gtp *
Enable/disable GTP messages logging.
option
-enable
Option
Description
enable
Enable GTP messages logging.
disable
Disable GTP messages logging.
http-transaction
Enable/disable log HTTP transaction messages.
option
-enable
Option
Description
enable
Enable http transaction logging.
disable
Disable http transaction logging.
local-traffic
Enable/disable local in or out traffic logging.
option
-enable **
FortiOS 8.0.0 CLI Reference
991
Fortinet Inc.

<!-- 来源页 992 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable local in or out traffic logging.
disable
Disable local in or out traffic logging.
multicast-traffic
Enable/disable multicast traffic logging.
option
-enable
Option
Description
enable
Enable multicast traffic logging.
disable
Disable multicast traffic logging.
severity
Log every message above and including this
severity level.
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
sniffer-traffic
Enable/disable sniffer traffic logging.
option
-enable
Option
Description
enable
Enable sniffer traffic logging.
disable
Disable sniffer traffic logging.
voip
Enable/disable VoIP logging.
option
-enable
Option
Description
enable
Enable VoIP logging.
disable
Disable VoIP logging.
ztna-traffic
Enable/disable ztna traffic logging.
option
-enable
FortiOS 8.0.0 CLI Reference
992
Fortinet Inc.

<!-- 来源页 993 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable ztna traffic logging.
disable
Disable ztna traffic logging.
* This parameter may not exist in some models.
** Values may differ between models.
config free-style
Parameter
Description
Type
Size
Default
category
Log category.
option
-traffic
Option
Description
traffic
Traffic log.
event
Event log.
virus
Antivirus log.
webfilter
Web filter log.
attack
Attack log.
spam
Antispam log.
anomaly
Anomaly log.
voip
VoIP log.
dlp
DLP log.
app-ctrl
Application control log.
waf
Web application firewall log.
dns
DNS detail log.
ssh
SSH log.
ssl
SSL log.
file-filter
File filter log.
icap
ICAP log.
virtual-patch
Virtual patch log.
debug
Debug log.
filter
Free style filter string.
string
Maximum
length: 1023
FortiOS 8.0.0 CLI Reference
993
Fortinet Inc.

<!-- 来源页 994 -->
Parameter
Description
Type
Size
Default
filter-type
Include/exclude logs that match the filter.
option
-include
Option
Description
include
Include logs that match the filter.
exclude
Exclude logs that match the filter.
id
Entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config log memory global-setting
Global settings for memory logging.
config log memory global-setting
Description: Global settings for memory logging.
set full-final-warning-threshold {integer}
set full-first-warning-threshold {integer}
set full-second-warning-threshold {integer}
set max-size {integer}
end
config log memory global-setting
Parameter
Description
Type
Size
Default
full-final-warning-threshold
Log full final warning threshold as a percent (3
- 100, default = 95).
integer
Minimum value:
3 Maximum
value: 100
95
full-first-warning-threshold
Log full first warning threshold as a percent (1
- 98, default = 75).
integer
Minimum value:
1 Maximum
value: 98
75
full-second-warning-threshold
Log full second warning threshold as a
percent (2 - 99, default = 90).
integer
Minimum value:
2 Maximum
value: 99
90
max-size
Maximum amount of memory that can be used
for memory logging in bytes.
integer
Minimum value:
0 Maximum
value:
4294967295
168438251
**
** Values may differ between models.
FortiOS 8.0.0 CLI Reference
994
Fortinet Inc.

<!-- 来源页 995 -->
config log memory setting
Settings for memory buffer.
config log memory setting
Description: Settings for memory buffer.
set status [enable|disable]
end
config log memory setting
Parameter
Description
Type
Size
Default
status
Enable/disable logging to the FortiGate's memory.
option
-enable **
Option
Description
enable
Enable logging to memory.
disable
Disable logging to memory.
** Values may differ between models.
config log null-device filter
Filters for null device logging.
config log null-device filter
Description: Filters for null device logging.
set anomaly [enable|disable]
set debug [enable|disable]
set forti-switch [enable|disable]
set forward-traffic [enable|disable]
config free-style
Description: Free style filters.
edit <id>
set category [traffic|event|...]
set filter {string}
set filter-type [include|exclude]
next
end
set gtp [enable|disable]
set http-transaction [enable|disable]
set local-traffic [enable|disable]
set multicast-traffic [enable|disable]
set severity [emergency|alert|...]
set sniffer-traffic [enable|disable]
set voip [enable|disable]
FortiOS 8.0.0 CLI Reference
995
Fortinet Inc.

<!-- 来源页 996 -->
set ztna-traffic [enable|disable]
end
config log null-device filter
Parameter
Description
Type
Size
Default
anomaly
Enable/disable anomaly logging.
option
-enable
Option
Description
enable
Enable anomaly logging.
disable
Disable anomaly logging.
debug
Enable/disable debug logging.
option
-disable
Option
Description
enable
Enable Debug logging.
disable
Disable Debug logging.
forti-switch
Enable/disable Forti-Switch logging.
option
-enable
Option
Description
enable
Enable Forti-Switch logging.
disable
Disable Forti-Switch logging.
forward-traffic
Enable/disable forward traffic logging.
option
-enable
Option
Description
enable
Enable forward traffic logging.
disable
Disable forward traffic logging.
gtp *
Enable/disable GTP messages logging.
option
-enable
Option
Description
enable
Enable GTP messages logging.
disable
Disable GTP messages logging.
http-transaction
Enable/disable log HTTP transaction messages.
option
-enable
Option
Description
enable
Enable http transaction logging.
FortiOS 8.0.0 CLI Reference
996
Fortinet Inc.

<!-- 来源页 997 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable http transaction logging.
local-traffic
Enable/disable local in or out traffic logging.
option
-enable
Option
Description
enable
Enable local in or out traffic logging.
disable
Disable local in or out traffic logging.
multicast-traffic
Enable/disable multicast traffic logging.
option
-enable
Option
Description
enable
Enable multicast traffic logging.
disable
Disable multicast traffic logging.
severity
Lowest severity level to log.
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
sniffer-traffic
Enable/disable sniffer traffic logging.
option
-enable
Option
Description
enable
Enable sniffer traffic logging.
disable
Disable sniffer traffic logging.
voip
Enable/disable VoIP logging.
option
-enable
Option
Description
enable
Enable VoIP logging.
FortiOS 8.0.0 CLI Reference
997
Fortinet Inc.

<!-- 来源页 998 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable VoIP logging.
ztna-traffic
Enable/disable ztna traffic logging.
option
-enable
Option
Description
enable
Enable ztna traffic logging.
disable
Disable ztna traffic logging.
* This parameter may not exist in some models.
config free-style
Parameter
Description
Type
Size
Default
category
Log category.
option
-traffic
Option
Description
traffic
Traffic log.
event
Event log.
virus
Antivirus log.
webfilter
Web filter log.
attack
Attack log.
spam
Antispam log.
anomaly
Anomaly log.
voip
VoIP log.
dlp
DLP log.
app-ctrl
Application control log.
waf
Web application firewall log.
dns
DNS detail log.
ssh
SSH log.
ssl
SSL log.
file-filter
File filter log.
icap
ICAP log.
virtual-patch
Virtual patch log.
debug
Debug log.
FortiOS 8.0.0 CLI Reference
998
Fortinet Inc.

<!-- 来源页 999 -->
Parameter
Description
Type
Size
Default
filter
Free style filter string.
string
Maximum
length: 1023
filter-type
Include/exclude logs that match the filter.
option
-include
Option
Description
include
Include logs that match the filter.
exclude
Exclude logs that match the filter.
id
Entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config log null-device setting
Settings for null device logging.
config log null-device setting
Description: Settings for null device logging.
set status [enable|disable]
end
config log null-device setting
Parameter
Description
Type
Size
Default
status
Enable/disable statistics collection for when no
external logging destination, such as FortiAnalyzer,
is present (data is not saved).
option
-disable
Option
Description
enable
Enable statistics collection for when no external logging destination,
such as FortiAnalyzer, is present (data is not saved).
disable
Disable statistics collection for when no external logging destination,
such as FortiAnalyzer, is present (data is not saved).
config log setting
Configure general log settings.
FortiOS 8.0.0 CLI Reference
999
Fortinet Inc.

<!-- 来源页 1000 -->
config log setting
Description: Configure general log settings.
set anonymization-hash {string}
set brief-traffic-format [enable|disable]
set custom-log-fields <field-id1>, <field-id2>, ...
set daemon-log [enable|disable]
set detailed-svc-name [enable|disable]
set expolicy-implicit-log [enable|disable]
set extended-log [enable|disable]
set extended-utm-log [enable|disable]
set faz-override [enable|disable]
set fortiview-weekly-data [enable|disable]
set fwpolicy-implicit-log [enable|disable]
set fwpolicy6-implicit-log [enable|disable]
set local-in-allow [enable|disable]
set local-in-deny-broadcast [enable|disable]
set local-in-deny-unicast [enable|disable]
set local-in-policy-log [enable|disable]
set local-out [enable|disable]
set local-out-ioc-detection [enable|disable]
set log-policy-comment [enable|disable]
set log-user-in-upper [enable|disable]
set long-live-session-stat [enable|disable]
set neighbor-event [enable|disable]
set resolve-ip [enable|disable]
set resolve-port [enable|disable]
set rest-api-get [enable|disable]
set rest-api-performance [enable|disable]
set rest-api-set [enable|disable]
set syslog-override [enable|disable]
set tacacs-accounting-server-alternate [enable|disable]
set user-anonymize [enable|disable]
set web-svc-perf [enable|disable]
set zone-name [enable|disable]
end
config log setting
Parameter
Description
Type
Size
Default
anonymization-hash
User name anonymization hash salt.
string
Maximum
length: 32
brief-traffic-format
Enable/disable brief format traffic logging.
option
-disable
Option
Description
enable
Enable brief format traffic logging.
disable
Disable brief format traffic logging.
FortiOS 8.0.0 CLI Reference
1000
Fortinet Inc.

<!-- 来源页 1001 -->
Parameter
Description
Type
Size
Default
custom-log-fields
<field-id>
Custom fields to append to all log messages.
Custom log field.
string
Maximum
length: 35
daemon-log
Enable/disable daemon logging.
option
-disable
Option
Description
enable
Enable daemon logging.
disable
Disable daemon logging.
detailed-svc-name *
Enable/disable logging of the specific service
name or the top-most service group name.
option
-disable
Option
Description
enable
Log the specific service name.
disable
Log the top-most service group name.
expolicy-implicit-log
Enable/disable proxy firewall implicit policy
logging.
option
-disable
Option
Description
enable
Enable proxy firewall implicit policy logging.
disable
Disable proxy firewall implicit policy logging.
extended-log
Enable/disable extended traffic logging.
option
-disable
Option
Description
enable
Enable extended traffic logging.
disable
Disable extended traffic logging.
extended-utm-log
Enable/disable extended UTM logging.
option
-disable
Option
Description
enable
Enable extended UTM logging.
disable
Disable extended UTM logging.
faz-override
Enable/disable override FortiAnalyzer settings.
option
-disable
Option
Description
enable
Enable override FortiAnalyzer settings.
disable
Disable override FortiAnalyzer settings.
FortiOS 8.0.0 CLI Reference
1001
Fortinet Inc.

<!-- 来源页 1002 -->
Parameter
Description
Type
Size
Default
fortiview-weekly-data *
Enable/disable FortiView weekly data.
option
-disable
Option
Description
enable
Enable FortiView weekly data.
disable
Disable FortiView weekly data.
fwpolicy-implicit-log
Enable/disable implicit firewall policy logging.
option
-disable
Option
Description
enable
Enable implicit firewall policy logging.
disable
Disable implicit firewall policy logging.
fwpolicy6-implicit-log
Enable/disable implicit firewall policy6 logging.
option
-disable
Option
Description
enable
Enable implicit firewall policy6 logging.
disable
Disable implicit firewall policy6 logging.
local-in-allow
Enable/disable local-in-allow logging.
option
-disable
Option
Description
enable
Enable local-in-allow logging.
disable
Disable local-in-allow logging.
local-in-deny-broadcast
Enable/disable local-in-deny-broadcast
logging.
option
-disable
Option
Description
enable
Enable local-in-deny-broadcast logging.
disable
Disable local-in-deny-broadcast logging.
local-in-deny-unicast
Enable/disable local-in-deny-unicast logging.
option
-disable
Option
Description
enable
Enable local-in-deny-unicast logging.
disable
Disable local-in-deny-unicast logging.
FortiOS 8.0.0 CLI Reference
1002
Fortinet Inc.

<!-- 来源页 1003 -->
Parameter
Description
Type
Size
Default
local-in-policy-log
Enable/disable local-in-policy logging.
option
-disable
Option
Description
enable
Enable local-in-policy logging.
disable
Disable local-in-policy logging.
local-out
Enable/disable local-out logging.
option
-enable
Option
Description
enable
Enable local-out logging.
disable
Disable local-out logging.
local-out-ioc-detection
Enable/disable local-out traffic IoC detection.
Requires local-out to be enabled.
option
-enable
Option
Description
enable
Enable local-out traffic IoC detection. Requires local-out to be
enabled.
disable
Disable local-out traffic IoC detection.
log-policy-comment
Enable/disable inserting policy comments into
traffic logs.
option
-disable
Option
Description
enable
Enable inserting policy comments into traffic logs.
disable
Disable inserting policy comments into traffic logs.
log-user-in-upper
Enable/disable logs with user-in-upper.
option
-disable
Option
Description
enable
Enable logs with user-in-upper.
disable
Disable logs with user-in-upper.
long-live-session-stat
Enable/disable long-live-session statistics
logging.
option
-enable
Option
Description
enable
Enable long-live-session statistics logging.
disable
Disable long-live-session statistics logging.
FortiOS 8.0.0 CLI Reference
1003
Fortinet Inc.

<!-- 来源页 1004 -->
Parameter
Description
Type
Size
Default
neighbor-event
Enable/disable neighbor event logging.
option
-disable
Option
Description
enable
Enable neighbor event logging.
disable
Disable neighbor event logging.
resolve-ip
Enable/disable adding resolved domain names
to traffic logs if possible.
option
-disable
Option
Description
enable
Enable adding resolved domain names to traffic logs.
disable
Disable adding resolved domain names to traffic logs.
resolve-port
Enable/disable adding resolved service names
to traffic logs.
option
-enable
Option
Description
enable
Enable adding resolved service names to traffic logs.
disable
Disable adding resolved service names to traffic logs.
rest-api-get
Enable/disable REST API GET request logging.
option
-disable
Option
Description
enable
Enable GET REST API logging.
disable
Disable GET REST API logging.
rest-api-performance
Enable/disable REST API memory and
performance stats in rest-api-get/set logs.
option
-disable
Option
Description
enable
Enable REST API performance stats in REST API logs.
disable
Disable REST API performance stats in REST API logs.
rest-api-set
Enable/disable REST API POST/PUT/DELETE
request logging.
option
-disable
Option
Description
enable
Enable POST/PUT/DELETE REST API logging.
disable
Disable POST/PUT/DELETE REST API logging.
syslog-override
Enable/disable override Syslog settings.
option
-disable
FortiOS 8.0.0 CLI Reference
1004
Fortinet Inc.

<!-- 来源页 1005 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable override Syslog settings.
disable
Disable override Syslog settings.
tacacs-accounting-server-alternate *
Enable/disable TACACS Acounting Server
alternating.
option
-disable
Option
Description
enable
Enable TACACS Acounting Server alternating.
disable
Disable TACACS Acounting Server alternating.
user-anonymize
Enable/disable anonymizing user names in log
messages.
option
-disable
Option
Description
enable
Enable anonymizing user names in log messages.
disable
Disable anonymizing user names in log messages.
web-svc-perf
Enable/disable web-svc performance logging.
option
-disable
Option
Description
enable
Enable web-svc performance logging.
disable
Disable web-svc performance logging.
zone-name
Enable/disable zone name logging.
option
-disable
Option
Description
enable
Enable zone name logging.
disable
Disable zone name logging.
* This parameter may not exist in some models.
config log syslogd filter
Filters for remote system server.
config log syslogd filter
Description: Filters for remote system server.
set anomaly [enable|disable]
set debug [enable|disable]
FortiOS 8.0.0 CLI Reference
1005
Fortinet Inc.

<!-- 来源页 1006 -->
set forti-switch [enable|disable]
set forward-traffic [enable|disable]
config free-style
Description: Free style filters.
edit <id>
set category [traffic|event|...]
set filter {string}
set filter-type [include|exclude]
next
end
set gtp [enable|disable]
set http-transaction [enable|disable]
set local-traffic [enable|disable]
set multicast-traffic [enable|disable]
set severity [emergency|alert|...]
set sniffer-traffic [enable|disable]
set voip [enable|disable]
set ztna-traffic [enable|disable]
end
config log syslogd filter
Parameter
Description
Type
Size
Default
anomaly
Enable/disable anomaly logging.
option
-enable
Option
Description
enable
Enable anomaly logging.
disable
Disable anomaly logging.
debug
Enable/disable debug logging.
option
-disable
Option
Description
enable
Enable Debug logging.
disable
Disable Debug logging.
forti-switch
Enable/disable Forti-Switch logging.
option
-enable
Option
Description
enable
Enable Forti-Switch logging.
disable
Disable Forti-Switch logging.
forward-traffic
Enable/disable forward traffic logging.
option
-enable
FortiOS 8.0.0 CLI Reference
1006
Fortinet Inc.

<!-- 来源页 1007 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable forward traffic logging.
disable
Disable forward traffic logging.
gtp *
Enable/disable GTP messages logging.
option
-enable
Option
Description
enable
Enable GTP messages logging.
disable
Disable GTP messages logging.
http-transaction
Enable/disable log HTTP transaction messages.
option
-enable
Option
Description
enable
Enable http transaction logging.
disable
Disable http transaction logging.
local-traffic
Enable/disable local in or out traffic logging.
option
-enable
Option
Description
enable
Enable local in or out traffic logging.
disable
Disable local in or out traffic logging.
multicast-traffic
Enable/disable multicast traffic logging.
option
-enable
Option
Description
enable
Enable multicast traffic logging.
disable
Disable multicast traffic logging.
severity
Lowest severity level to log.
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
FortiOS 8.0.0 CLI Reference
1007
Fortinet Inc.

<!-- 来源页 1008 -->
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
sniffer-traffic
Enable/disable sniffer traffic logging.
option
-enable
Option
Description
enable
Enable sniffer traffic logging.
disable
Disable sniffer traffic logging.
voip
Enable/disable VoIP logging.
option
-enable
Option
Description
enable
Enable VoIP logging.
disable
Disable VoIP logging.
ztna-traffic
Enable/disable ztna traffic logging.
option
-enable
Option
Description
enable
Enable ztna traffic logging.
disable
Disable ztna traffic logging.
* This parameter may not exist in some models.
config free-style
Parameter
Description
Type
Size
Default
category
Log category.
option
-traffic
Option
Description
traffic
Traffic log.
event
Event log.
virus
Antivirus log.
webfilter
Web filter log.
attack
Attack log.
spam
Antispam log.
FortiOS 8.0.0 CLI Reference
1008
Fortinet Inc.

<!-- 来源页 1009 -->
Parameter
Description
Type
Size
Default
Option
Description
anomaly
Anomaly log.
voip
VoIP log.
dlp
DLP log.
app-ctrl
Application control log.
waf
Web application firewall log.
dns
DNS detail log.
ssh
SSH log.
ssl
SSL log.
file-filter
File filter log.
icap
ICAP log.
virtual-patch
Virtual patch log.
debug
Debug log.
filter
Free style filter string.
string
Maximum
length: 1023
filter-type
Include/exclude logs that match the filter.
option
-include
Option
Description
include
Include logs that match the filter.
exclude
Exclude logs that match the filter.
id
Entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config log syslogd override-filter
Override filters for remote system server.
config log syslogd override-filter
Description: Override filters for remote system server.
set anomaly [enable|disable]
set debug [enable|disable]
set forti-switch [enable|disable]
set forward-traffic [enable|disable]
config free-style
FortiOS 8.0.0 CLI Reference
1009
Fortinet Inc.

<!-- 来源页 1010 -->
Description: Free style filters.
edit <id>
set category [traffic|event|...]
set filter {string}
set filter-type [include|exclude]
next
end
set gtp [enable|disable]
set http-transaction [enable|disable]
set local-traffic [enable|disable]
set multicast-traffic [enable|disable]
set severity [emergency|alert|...]
set sniffer-traffic [enable|disable]
set voip [enable|disable]
set ztna-traffic [enable|disable]
end
config log syslogd override-filter
Parameter
Description
Type
Size
Default
anomaly
Enable/disable anomaly logging.
option
-enable
Option
Description
enable
Enable anomaly logging.
disable
Disable anomaly logging.
debug
Enable/disable debug logging.
option
-disable
Option
Description
enable
Enable Debug logging.
disable
Disable Debug logging.
forti-switch
Enable/disable Forti-Switch logging.
option
-enable
Option
Description
enable
Enable Forti-Switch logging.
disable
Disable Forti-Switch logging.
forward-traffic
Enable/disable forward traffic logging.
option
-enable
Option
Description
enable
Enable forward traffic logging.
disable
Disable forward traffic logging.
FortiOS 8.0.0 CLI Reference
1010
Fortinet Inc.

<!-- 来源页 1011 -->
Parameter
Description
Type
Size
Default
gtp *
Enable/disable GTP messages logging.
option
-enable
Option
Description
enable
Enable GTP messages logging.
disable
Disable GTP messages logging.
http-transaction
Enable/disable log HTTP transaction messages.
option
-enable
Option
Description
enable
Enable http transaction logging.
disable
Disable http transaction logging.
local-traffic
Enable/disable local in or out traffic logging.
option
-enable
Option
Description
enable
Enable local in or out traffic logging.
disable
Disable local in or out traffic logging.
multicast-traffic
Enable/disable multicast traffic logging.
option
-enable
Option
Description
enable
Enable multicast traffic logging.
disable
Disable multicast traffic logging.
severity
Lowest severity level to log.
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
sniffer-traffic
Enable/disable sniffer traffic logging.
option
-enable
FortiOS 8.0.0 CLI Reference
1011
Fortinet Inc.

<!-- 来源页 1012 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable sniffer traffic logging.
disable
Disable sniffer traffic logging.
voip
Enable/disable VoIP logging.
option
-enable
Option
Description
enable
Enable VoIP logging.
disable
Disable VoIP logging.
ztna-traffic
Enable/disable ztna traffic logging.
option
-enable
Option
Description
enable
Enable ztna traffic logging.
disable
Disable ztna traffic logging.
* This parameter may not exist in some models.
config free-style
Parameter
Description
Type
Size
Default
category
Log category.
option
-traffic
Option
Description
traffic
Traffic log.
event
Event log.
virus
Antivirus log.
webfilter
Web filter log.
attack
Attack log.
spam
Antispam log.
anomaly
Anomaly log.
voip
VoIP log.
dlp
DLP log.
app-ctrl
Application control log.
waf
Web application firewall log.
FortiOS 8.0.0 CLI Reference
1012
Fortinet Inc.

<!-- 来源页 1013 -->
Parameter
Description
Type
Size
Default
Option
Description
dns
DNS detail log.
ssh
SSH log.
ssl
SSL log.
file-filter
File filter log.
icap
ICAP log.
virtual-patch
Virtual patch log.
debug
Debug log.
filter
Free style filter string.
string
Maximum
length: 1023
filter-type
Include/exclude logs that match the filter.
option
-include
Option
Description
include
Include logs that match the filter.
exclude
Exclude logs that match the filter.
id
Entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config log syslogd override-setting
Override settings for remote syslog server.
config log syslogd override-setting
Description: Override settings for remote syslog server.
set certificate {string}
config custom-field-name
Description: Custom field name for CEF format logging.
edit <id>
set custom {string}
set name {string}
next
end
set custom-log-format {string}
set enc-algorithm [high-medium|high|...]
set facility [kernel|user|...]
set format [default|csv|...]
set interface {string}
FortiOS 8.0.0 CLI Reference
1013
Fortinet Inc.

<!-- 来源页 1014 -->
set interface-select-method [auto|sdwan|...]
set max-log-rate {integer}
set mode [udp|legacy-reliable|...]
set port {integer}
set priority [default|low]
set server {string}
set source-ip {string}
set source-ip-interface {string}
set ssl-min-proto-version [default|SSLv3|...]
set status [enable|disable]
set use-management-vdom [enable|disable]
set vrf-select {integer}
end
config log syslogd override-setting
Parameter
Description
Type
Size
Default
certificate
Certificate used to communicate with Syslog
server.
string
Maximum
length: 35
custom-log-format *
Customized format for logs.
string
Maximum
length: 35
enc-algorithm
Enable/disable reliable syslogging with TLS
encryption.
option
-disable
Option
Description
high-medium
SSL communication with high and medium encryption algorithms.
high
SSL communication with high encryption algorithms.
low
SSL communication with low encryption algorithms.
disable
Disable SSL communication.
facility
Remote syslog facility.
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
Messages generated internally by syslog.
lpr
Line printer subsystem.
FortiOS 8.0.0 CLI Reference
1014
Fortinet Inc.

<!-- 来源页 1015 -->
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
Network news subsystem.
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
format
Log format.
option
-default
Option
Description
default
Syslog format.
csv
CSV (Comma Separated Values) format.
cef
CEF (Common Event Format) format.
rfc5424
Syslog RFC5424 format.
json
JSON (JavaScript Object Notation) format.
custom
Custom format.
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
FortiOS 8.0.0 CLI Reference
1015
Fortinet Inc.

<!-- 来源页 1016 -->
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
max-log-rate
Syslog maximum log rate in MBps (0 = unlimited).
integer
Minimum
value: 0
Maximum
value:
100000
0
mode
Remote syslog logging over UDP/Reliable TCP.
option
-udp
Option
Description
udp
Enable syslogging over UDP.
legacy-reliable
Enable legacy reliable syslogging by RFC3195 (Reliable Delivery for
Syslog).
reliable
Enable reliable syslogging by RFC6587 (Transmission of Syslog
Messages over TCP).
port
Server listen port.
integer
Minimum
value: 0
Maximum
value:
65535
514
priority
Set log transmission priority.
option
-default
Option
Description
default
Set Syslog transmission priority to default.
low
Set Syslog transmission priority to low.
server
Address of remote syslog server.
string
Maximum
length: 127
source-ip
Source IP address of syslog.
string
Maximum
length: 63
source-ip-interface
Source interface of syslog.
string
Maximum
length: 15
ssl-min-proto-version
Minimum supported protocol version for SSL/TLS
connections (default is to follow system global
setting).
option
-default
FortiOS 8.0.0 CLI Reference
1016
Fortinet Inc.

<!-- 来源页 1017 -->
Parameter
Description
Type
Size
Default
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
Enable/disable remote syslog logging.
option
-disable
Option
Description
enable
Log to remote syslog server.
disable
Do not log to remote syslog server.
use-management-vdom
Enable/disable use of management VDOM as
source VDOM for logs sent to syslog server.
option
-disable
Option
Description
enable
Enable use of management VDOM as source VDOM.
disable
Use the current VDOM as source VDOM.
vrf-select
VRF ID used for connection to server.
integer
Minimum
value: 0
Maximum
value: 511
0
* This parameter may not exist in some models.
config custom-field-name
Parameter
Description
Type
Size
Default
custom
Field custom name [A-Za-z0-9_].
string
Maximum
length: 35
id
Entry ID.
integer
Minimum
value: 0
Maximum
value: 255
0
name
Field name [A-Za-z0-9_].
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
1017
Fortinet Inc.

<!-- 来源页 1018 -->
config log syslogd setting
Global settings for remote syslog server.
config log syslogd setting
Description: Global settings for remote syslog server.
set certificate {string}
config custom-field-name
Description: Custom field name for CEF format logging.
edit <id>
set custom {string}
set name {string}
next
end
set custom-log-format {string}
set enc-algorithm [high-medium|high|...]
set facility [kernel|user|...]
set format [default|csv|...]
set interface {string}
set interface-select-method [auto|sdwan|...]
set max-log-rate {integer}
set mode [udp|legacy-reliable|...]
set port {integer}
set priority [default|low]
set server {string}
set source-ip {string}
set source-ip-interface {string}
set ssl-min-proto-version [default|SSLv3|...]
set status [enable|disable]
set vrf-select {integer}
end
config log syslogd setting
Parameter
Description
Type
Size
Default
certificate
Certificate used to communicate with Syslog
server.
string
Maximum
length: 35
custom-log-format *
Customized format for logs.
string
Maximum
length: 35
enc-algorithm
Enable/disable reliable syslogging with TLS
encryption.
option
-disable
Option
Description
high-medium
SSL communication with high and medium encryption algorithms.
FortiOS 8.0.0 CLI Reference
1018
Fortinet Inc.

<!-- 来源页 1019 -->
Parameter
Description
Type
Size
Default
Option
Description
high
SSL communication with high encryption algorithms.
low
SSL communication with low encryption algorithms.
disable
Disable SSL communication.
facility
Remote syslog facility.
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
Messages generated internally by syslog.
lpr
Line printer subsystem.
news
Network news subsystem.
uucp
Network news subsystem.
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
FortiOS 8.0.0 CLI Reference
1019
Fortinet Inc.

<!-- 来源页 1020 -->
Parameter
Description
Type
Size
Default
format
Log format.
option
-default
Option
Description
default
Syslog format.
csv
CSV (Comma Separated Values) format.
cef
CEF (Common Event Format) format.
rfc5424
Syslog RFC5424 format.
json
JSON (JavaScript Object Notation) format.
custom
Custom format.
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
max-log-rate
Syslog maximum log rate in MBps (0 = unlimited).
integer
Minimum
value: 0
Maximum
value:
100000
0
mode
Remote syslog logging over UDP/Reliable TCP.
option
-udp
Option
Description
udp
Enable syslogging over UDP.
legacy-reliable
Enable legacy reliable syslogging by RFC3195 (Reliable Delivery for
Syslog).
reliable
Enable reliable syslogging by RFC6587 (Transmission of Syslog
Messages over TCP).
FortiOS 8.0.0 CLI Reference
1020
Fortinet Inc.

<!-- 来源页 1021 -->
Parameter
Description
Type
Size
Default
port
Server listen port.
integer
Minimum
value: 0
Maximum
value:
65535
514
priority
Set log transmission priority.
option
-default
Option
Description
default
Set Syslog transmission priority to default.
low
Set Syslog transmission priority to low.
server
Address of remote syslog server.
string
Maximum
length: 127
source-ip
Source IP address of syslog.
string
Maximum
length: 63
source-ip-interface
Source interface of syslog.
string
Maximum
length: 15
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
Enable/disable remote syslog logging.
option
-disable
Option
Description
enable
Log to remote syslog server.
disable
Do not log to remote syslog server.
vrf-select
VRF ID used for connection to server.
integer
Minimum
value: 0
Maximum
value: 511
0
* This parameter may not exist in some models.
FortiOS 8.0.0 CLI Reference
1021
Fortinet Inc.

<!-- 来源页 1022 -->
config custom-field-name
Parameter
Description
Type
Size
Default
custom
Field custom name [A-Za-z0-9_].
string
Maximum
length: 35
id
Entry ID.
integer
Minimum
value: 0
Maximum
value: 255
0
name
Field name [A-Za-z0-9_].
string
Maximum
length: 35
config log syslogd2 filter
Filters for remote system server.
config log syslogd2 filter
Description: Filters for remote system server.
set anomaly [enable|disable]
set debug [enable|disable]
set forti-switch [enable|disable]
set forward-traffic [enable|disable]
config free-style
Description: Free style filters.
edit <id>
set category [traffic|event|...]
set filter {string}
set filter-type [include|exclude]
next
end
set gtp [enable|disable]
set http-transaction [enable|disable]
set local-traffic [enable|disable]
set multicast-traffic [enable|disable]
set severity [emergency|alert|...]
set sniffer-traffic [enable|disable]
set voip [enable|disable]
set ztna-traffic [enable|disable]
end
config log syslogd2 filter
Parameter
Description
Type
Size
Default
anomaly
Enable/disable anomaly logging.
option
-enable
FortiOS 8.0.0 CLI Reference
1022
Fortinet Inc.

<!-- 来源页 1023 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable anomaly logging.
disable
Disable anomaly logging.
debug
Enable/disable debug logging.
option
-disable
Option
Description
enable
Enable Debug logging.
disable
Disable Debug logging.
forti-switch
Enable/disable Forti-Switch logging.
option
-enable
Option
Description
enable
Enable Forti-Switch logging.
disable
Disable Forti-Switch logging.
forward-traffic
Enable/disable forward traffic logging.
option
-enable
Option
Description
enable
Enable forward traffic logging.
disable
Disable forward traffic logging.
gtp *
Enable/disable GTP messages logging.
option
-enable
Option
Description
enable
Enable GTP messages logging.
disable
Disable GTP messages logging.
http-transaction
Enable/disable log HTTP transaction messages.
option
-enable
Option
Description
enable
Enable http transaction logging.
disable
Disable http transaction logging.
local-traffic
Enable/disable local in or out traffic logging.
option
-enable
FortiOS 8.0.0 CLI Reference
1023
Fortinet Inc.

<!-- 来源页 1024 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable local in or out traffic logging.
disable
Disable local in or out traffic logging.
multicast-traffic
Enable/disable multicast traffic logging.
option
-enable
Option
Description
enable
Enable multicast traffic logging.
disable
Disable multicast traffic logging.
severity
Lowest severity level to log.
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
sniffer-traffic
Enable/disable sniffer traffic logging.
option
-enable
Option
Description
enable
Enable sniffer traffic logging.
disable
Disable sniffer traffic logging.
voip
Enable/disable VoIP logging.
option
-enable
Option
Description
enable
Enable VoIP logging.
disable
Disable VoIP logging.
ztna-traffic
Enable/disable ztna traffic logging.
option
-enable
FortiOS 8.0.0 CLI Reference
1024
Fortinet Inc.

<!-- 来源页 1025 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable ztna traffic logging.
disable
Disable ztna traffic logging.
* This parameter may not exist in some models.
config free-style
Parameter
Description
Type
Size
Default
category
Log category.
option
-traffic
Option
Description
traffic
Traffic log.
event
Event log.
virus
Antivirus log.
webfilter
Web filter log.
attack
Attack log.
spam
Antispam log.
anomaly
Anomaly log.
voip
VoIP log.
dlp
DLP log.
app-ctrl
Application control log.
waf
Web application firewall log.
dns
DNS detail log.
ssh
SSH log.
ssl
SSL log.
file-filter
File filter log.
icap
ICAP log.
virtual-patch
Virtual patch log.
debug
Debug log.
filter
Free style filter string.
string
Maximum
length: 1023
filter-type
Include/exclude logs that match the filter.
option
-include
FortiOS 8.0.0 CLI Reference
1025
Fortinet Inc.

<!-- 来源页 1026 -->
Parameter
Description
Type
Size
Default
Option
Description
include
Include logs that match the filter.
exclude
Exclude logs that match the filter.
id
Entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config log syslogd2 override-filter
Override filters for remote system server.
config log syslogd2 override-filter
Description: Override filters for remote system server.
set anomaly [enable|disable]
set debug [enable|disable]
set forti-switch [enable|disable]
set forward-traffic [enable|disable]
config free-style
Description: Free style filters.
edit <id>
set category [traffic|event|...]
set filter {string}
set filter-type [include|exclude]
next
end
set gtp [enable|disable]
set http-transaction [enable|disable]
set local-traffic [enable|disable]
set multicast-traffic [enable|disable]
set severity [emergency|alert|...]
set sniffer-traffic [enable|disable]
set voip [enable|disable]
set ztna-traffic [enable|disable]
end
config log syslogd2 override-filter
Parameter
Description
Type
Size
Default
anomaly
Enable/disable anomaly logging.
option
-enable
FortiOS 8.0.0 CLI Reference
1026
Fortinet Inc.

<!-- 来源页 1027 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable anomaly logging.
disable
Disable anomaly logging.
debug
Enable/disable debug logging.
option
-disable
Option
Description
enable
Enable Debug logging.
disable
Disable Debug logging.
forti-switch
Enable/disable Forti-Switch logging.
option
-enable
Option
Description
enable
Enable Forti-Switch logging.
disable
Disable Forti-Switch logging.
forward-traffic
Enable/disable forward traffic logging.
option
-enable
Option
Description
enable
Enable forward traffic logging.
disable
Disable forward traffic logging.
gtp *
Enable/disable GTP messages logging.
option
-enable
Option
Description
enable
Enable GTP messages logging.
disable
Disable GTP messages logging.
http-transaction
Enable/disable log HTTP transaction messages.
option
-enable
Option
Description
enable
Enable http transaction logging.
disable
Disable http transaction logging.
local-traffic
Enable/disable local in or out traffic logging.
option
-enable
FortiOS 8.0.0 CLI Reference
1027
Fortinet Inc.

<!-- 来源页 1028 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable local in or out traffic logging.
disable
Disable local in or out traffic logging.
multicast-traffic
Enable/disable multicast traffic logging.
option
-enable
Option
Description
enable
Enable multicast traffic logging.
disable
Disable multicast traffic logging.
severity
Lowest severity level to log.
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
sniffer-traffic
Enable/disable sniffer traffic logging.
option
-enable
Option
Description
enable
Enable sniffer traffic logging.
disable
Disable sniffer traffic logging.
voip
Enable/disable VoIP logging.
option
-enable
Option
Description
enable
Enable VoIP logging.
disable
Disable VoIP logging.
ztna-traffic
Enable/disable ztna traffic logging.
option
-enable
FortiOS 8.0.0 CLI Reference
1028
Fortinet Inc.

<!-- 来源页 1029 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable ztna traffic logging.
disable
Disable ztna traffic logging.
* This parameter may not exist in some models.
config free-style
Parameter
Description
Type
Size
Default
category
Log category.
option
-traffic
Option
Description
traffic
Traffic log.
event
Event log.
virus
Antivirus log.
webfilter
Web filter log.
attack
Attack log.
spam
Antispam log.
anomaly
Anomaly log.
voip
VoIP log.
dlp
DLP log.
app-ctrl
Application control log.
waf
Web application firewall log.
dns
DNS detail log.
ssh
SSH log.
ssl
SSL log.
file-filter
File filter log.
icap
ICAP log.
virtual-patch
Virtual patch log.
debug
Debug log.
filter
Free style filter string.
string
Maximum
length: 1023
filter-type
Include/exclude logs that match the filter.
option
-include
FortiOS 8.0.0 CLI Reference
1029
Fortinet Inc.

<!-- 来源页 1030 -->
Parameter
Description
Type
Size
Default
Option
Description
include
Include logs that match the filter.
exclude
Exclude logs that match the filter.
id
Entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config log syslogd2 override-setting
Override settings for remote syslog server.
config log syslogd2 override-setting
Description: Override settings for remote syslog server.
set certificate {string}
config custom-field-name
Description: Custom field name for CEF format logging.
edit <id>
set custom {string}
set name {string}
next
end
set custom-log-format {string}
set enc-algorithm [high-medium|high|...]
set facility [kernel|user|...]
set format [default|csv|...]
set interface {string}
set interface-select-method [auto|sdwan|...]
set max-log-rate {integer}
set mode [udp|legacy-reliable|...]
set port {integer}
set priority [default|low]
set server {string}
set source-ip {string}
set source-ip-interface {string}
set ssl-min-proto-version [default|SSLv3|...]
set status [enable|disable]
set use-management-vdom [enable|disable]
set vrf-select {integer}
end
FortiOS 8.0.0 CLI Reference
1030
Fortinet Inc.

<!-- 来源页 1031 -->
config log syslogd2 override-setting
Parameter
Description
Type
Size
Default
certificate
Certificate used to communicate with Syslog
server.
string
Maximum
length: 35
custom-log-format *
Customized format for logs.
string
Maximum
length: 35
enc-algorithm
Enable/disable reliable syslogging with TLS
encryption.
option
-disable
Option
Description
high-medium
SSL communication with high and medium encryption algorithms.
high
SSL communication with high encryption algorithms.
low
SSL communication with low encryption algorithms.
disable
Disable SSL communication.
facility
Remote syslog facility.
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
Messages generated internally by syslog.
lpr
Line printer subsystem.
news
Network news subsystem.
uucp
Network news subsystem.
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
FortiOS 8.0.0 CLI Reference
1031
Fortinet Inc.

<!-- 来源页 1032 -->
Parameter
Description
Type
Size
Default
Option
Description
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
format
Log format.
option
-default
Option
Description
default
Syslog format.
csv
CSV (Comma Separated Values) format.
cef
CEF (Common Event Format) format.
rfc5424
Syslog RFC5424 format.
json
JSON (JavaScript Object Notation) format.
custom
Custom format.
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
max-log-rate
Syslog maximum log rate in MBps (0 = unlimited).
integer
Minimum
value: 0
Maximum
value:
100000
0
mode
Remote syslog logging over UDP/Reliable TCP.
option
-udp
FortiOS 8.0.0 CLI Reference
1032
Fortinet Inc.

<!-- 来源页 1033 -->
Parameter
Description
Type
Size
Default
Option
Description
udp
Enable syslogging over UDP.
legacy-reliable
Enable legacy reliable syslogging by RFC3195 (Reliable Delivery for
Syslog).
reliable
Enable reliable syslogging by RFC6587 (Transmission of Syslog
Messages over TCP).
port
Server listen port.
integer
Minimum
value: 0
Maximum
value:
65535
514
priority
Set log transmission priority.
option
-default
Option
Description
default
Set Syslog transmission priority to default.
low
Set Syslog transmission priority to low.
server
Address of remote syslog server.
string
Maximum
length: 127
source-ip
Source IP address of syslog.
string
Maximum
length: 63
source-ip-interface
Source interface of syslog.
string
Maximum
length: 15
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
Enable/disable remote syslog logging.
option
-disable
FortiOS 8.0.0 CLI Reference
1033
Fortinet Inc.

<!-- 来源页 1034 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Log to remote syslog server.
disable
Do not log to remote syslog server.
use-management-vdom
Enable/disable use of management VDOM as
source VDOM for logs sent to syslog server.
option
-disable
Option
Description
enable
Enable use of management VDOM as source VDOM.
disable
Use the current VDOM as source VDOM.
vrf-select
VRF ID used for connection to server.
integer
Minimum
value: 0
Maximum
value: 511
0
* This parameter may not exist in some models.
config custom-field-name
Parameter
Description
Type
Size
Default
custom
Field custom name [A-Za-z0-9_].
string
Maximum
length: 35
id
Entry ID.
integer
Minimum
value: 0
Maximum
value: 255
0
name
Field name [A-Za-z0-9_].
string
Maximum
length: 35
config log syslogd2 setting
Global settings for remote syslog server.
config log syslogd2 setting
Description: Global settings for remote syslog server.
set certificate {string}
config custom-field-name
Description: Custom field name for CEF format logging.
edit <id>
set custom {string}
FortiOS 8.0.0 CLI Reference
1034
Fortinet Inc.

<!-- 来源页 1035 -->
set name {string}
next
end
set custom-log-format {string}
set enc-algorithm [high-medium|high|...]
set facility [kernel|user|...]
set format [default|csv|...]
set interface {string}
set interface-select-method [auto|sdwan|...]
set max-log-rate {integer}
set mode [udp|legacy-reliable|...]
set port {integer}
set priority [default|low]
set server {string}
set source-ip {string}
set source-ip-interface {string}
set ssl-min-proto-version [default|SSLv3|...]
set status [enable|disable]
set vrf-select {integer}
end
config log syslogd2 setting
Parameter
Description
Type
Size
Default
certificate
Certificate used to communicate with Syslog
server.
string
Maximum
length: 35
custom-log-format *
Customized format for logs.
string
Maximum
length: 35
enc-algorithm
Enable/disable reliable syslogging with TLS
encryption.
option
-disable
Option
Description
high-medium
SSL communication with high and medium encryption algorithms.
high
SSL communication with high encryption algorithms.
low
SSL communication with low encryption algorithms.
disable
Disable SSL communication.
facility
Remote syslog facility.
option
-local7
Option
Description
kernel
Kernel messages.
user
Random user-level messages.
FortiOS 8.0.0 CLI Reference
1035
Fortinet Inc.

<!-- 来源页 1036 -->
Parameter
Description
Type
Size
Default
Option
Description
mail
Mail system.
daemon
System daemons.
auth
Security/authorization messages.
syslog
Messages generated internally by syslog.
lpr
Line printer subsystem.
news
Network news subsystem.
uucp
Network news subsystem.
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
format
Log format.
option
-default
Option
Description
default
Syslog format.
csv
CSV (Comma Separated Values) format.
cef
CEF (Common Event Format) format.
rfc5424
Syslog RFC5424 format.
FortiOS 8.0.0 CLI Reference
1036
Fortinet Inc.

<!-- 来源页 1037 -->
Parameter
Description
Type
Size
Default
Option
Description
json
JSON (JavaScript Object Notation) format.
custom
Custom format.
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
max-log-rate
Syslog maximum log rate in MBps (0 = unlimited).
integer
Minimum
value: 0
Maximum
value:
100000
0
mode
Remote syslog logging over UDP/Reliable TCP.
option
-udp
Option
Description
udp
Enable syslogging over UDP.
legacy-reliable
Enable legacy reliable syslogging by RFC3195 (Reliable Delivery for
Syslog).
reliable
Enable reliable syslogging by RFC6587 (Transmission of Syslog
Messages over TCP).
port
Server listen port.
integer
Minimum
value: 0
Maximum
value:
65535
514
priority
Set log transmission priority.
option
-default
Option
Description
default
Set Syslog transmission priority to default.
low
Set Syslog transmission priority to low.
FortiOS 8.0.0 CLI Reference
1037
Fortinet Inc.

<!-- 来源页 1038 -->
Parameter
Description
Type
Size
Default
server
Address of remote syslog server.
string
Maximum
length: 127
source-ip
Source IP address of syslog.
string
Maximum
length: 63
source-ip-interface
Source interface of syslog.
string
Maximum
length: 15
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
Enable/disable remote syslog logging.
option
-disable
Option
Description
enable
Log to remote syslog server.
disable
Do not log to remote syslog server.
vrf-select
VRF ID used for connection to server.
integer
Minimum
value: 0
Maximum
value: 511
0
* This parameter may not exist in some models.
config custom-field-name
Parameter
Description
Type
Size
Default
custom
Field custom name [A-Za-z0-9_].
string
Maximum
length: 35
id
Entry ID.
integer
Minimum
value: 0
Maximum
value: 255
0
FortiOS 8.0.0 CLI Reference
1038
Fortinet Inc.

<!-- 来源页 1039 -->
Parameter
Description
Type
Size
Default
name
Field name [A-Za-z0-9_].
string
Maximum
length: 35
config log syslogd3 filter
Filters for remote system server.
config log syslogd3 filter
Description: Filters for remote system server.
set anomaly [enable|disable]
set debug [enable|disable]
set forti-switch [enable|disable]
set forward-traffic [enable|disable]
config free-style
Description: Free style filters.
edit <id>
set category [traffic|event|...]
set filter {string}
set filter-type [include|exclude]
next
end
set gtp [enable|disable]
set http-transaction [enable|disable]
set local-traffic [enable|disable]
set multicast-traffic [enable|disable]
set severity [emergency|alert|...]
set sniffer-traffic [enable|disable]
set voip [enable|disable]
set ztna-traffic [enable|disable]
end
config log syslogd3 filter
Parameter
Description
Type
Size
Default
anomaly
Enable/disable anomaly logging.
option
-enable
Option
Description
enable
Enable anomaly logging.
disable
Disable anomaly logging.
debug
Enable/disable debug logging.
option
-disable
FortiOS 8.0.0 CLI Reference
1039
Fortinet Inc.

<!-- 来源页 1040 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable Debug logging.
disable
Disable Debug logging.
forti-switch
Enable/disable Forti-Switch logging.
option
-enable
Option
Description
enable
Enable Forti-Switch logging.
disable
Disable Forti-Switch logging.
forward-traffic
Enable/disable forward traffic logging.
option
-enable
Option
Description
enable
Enable forward traffic logging.
disable
Disable forward traffic logging.
gtp *
Enable/disable GTP messages logging.
option
-enable
Option
Description
enable
Enable GTP messages logging.
disable
Disable GTP messages logging.
http-transaction
Enable/disable log HTTP transaction messages.
option
-enable
Option
Description
enable
Enable http transaction logging.
disable
Disable http transaction logging.
local-traffic
Enable/disable local in or out traffic logging.
option
-enable
Option
Description
enable
Enable local in or out traffic logging.
disable
Disable local in or out traffic logging.
multicast-traffic
Enable/disable multicast traffic logging.
option
-enable
FortiOS 8.0.0 CLI Reference
1040
Fortinet Inc.

<!-- 来源页 1041 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable multicast traffic logging.
disable
Disable multicast traffic logging.
severity
Lowest severity level to log.
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
sniffer-traffic
Enable/disable sniffer traffic logging.
option
-enable
Option
Description
enable
Enable sniffer traffic logging.
disable
Disable sniffer traffic logging.
voip
Enable/disable VoIP logging.
option
-enable
Option
Description
enable
Enable VoIP logging.
disable
Disable VoIP logging.
ztna-traffic
Enable/disable ztna traffic logging.
option
-enable
Option
Description
enable
Enable ztna traffic logging.
disable
Disable ztna traffic logging.
* This parameter may not exist in some models.
FortiOS 8.0.0 CLI Reference
1041
Fortinet Inc.

<!-- 来源页 1042 -->
config free-style
Parameter
Description
Type
Size
Default
category
Log category.
option
-traffic
Option
Description
traffic
Traffic log.
event
Event log.
virus
Antivirus log.
webfilter
Web filter log.
attack
Attack log.
spam
Antispam log.
anomaly
Anomaly log.
voip
VoIP log.
dlp
DLP log.
app-ctrl
Application control log.
waf
Web application firewall log.
dns
DNS detail log.
ssh
SSH log.
ssl
SSL log.
file-filter
File filter log.
icap
ICAP log.
virtual-patch
Virtual patch log.
debug
Debug log.
filter
Free style filter string.
string
Maximum
length: 1023
filter-type
Include/exclude logs that match the filter.
option
-include
Option
Description
include
Include logs that match the filter.
exclude
Exclude logs that match the filter.
id
Entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
FortiOS 8.0.0 CLI Reference
1042
Fortinet Inc.

<!-- 来源页 1043 -->
config log syslogd3 override-filter
Override filters for remote system server.
config log syslogd3 override-filter
Description: Override filters for remote system server.
set anomaly [enable|disable]
set debug [enable|disable]
set forti-switch [enable|disable]
set forward-traffic [enable|disable]
config free-style
Description: Free style filters.
edit <id>
set category [traffic|event|...]
set filter {string}
set filter-type [include|exclude]
next
end
set gtp [enable|disable]
set http-transaction [enable|disable]
set local-traffic [enable|disable]
set multicast-traffic [enable|disable]
set severity [emergency|alert|...]
set sniffer-traffic [enable|disable]
set voip [enable|disable]
set ztna-traffic [enable|disable]
end
config log syslogd3 override-filter
Parameter
Description
Type
Size
Default
anomaly
Enable/disable anomaly logging.
option
-enable
Option
Description
enable
Enable anomaly logging.
disable
Disable anomaly logging.
debug
Enable/disable debug logging.
option
-disable
Option
Description
enable
Enable Debug logging.
disable
Disable Debug logging.
forti-switch
Enable/disable Forti-Switch logging.
option
-enable
FortiOS 8.0.0 CLI Reference
1043
Fortinet Inc.

<!-- 来源页 1044 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable Forti-Switch logging.
disable
Disable Forti-Switch logging.
forward-traffic
Enable/disable forward traffic logging.
option
-enable
Option
Description
enable
Enable forward traffic logging.
disable
Disable forward traffic logging.
gtp *
Enable/disable GTP messages logging.
option
-enable
Option
Description
enable
Enable GTP messages logging.
disable
Disable GTP messages logging.
http-transaction
Enable/disable log HTTP transaction messages.
option
-enable
Option
Description
enable
Enable http transaction logging.
disable
Disable http transaction logging.
local-traffic
Enable/disable local in or out traffic logging.
option
-enable
Option
Description
enable
Enable local in or out traffic logging.
disable
Disable local in or out traffic logging.
multicast-traffic
Enable/disable multicast traffic logging.
option
-enable
Option
Description
enable
Enable multicast traffic logging.
disable
Disable multicast traffic logging.
severity
Lowest severity level to log.
option
-information
FortiOS 8.0.0 CLI Reference
1044
Fortinet Inc.

<!-- 来源页 1045 -->
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
sniffer-traffic
Enable/disable sniffer traffic logging.
option
-enable
Option
Description
enable
Enable sniffer traffic logging.
disable
Disable sniffer traffic logging.
voip
Enable/disable VoIP logging.
option
-enable
Option
Description
enable
Enable VoIP logging.
disable
Disable VoIP logging.
ztna-traffic
Enable/disable ztna traffic logging.
option
-enable
Option
Description
enable
Enable ztna traffic logging.
disable
Disable ztna traffic logging.
* This parameter may not exist in some models.
config free-style
Parameter
Description
Type
Size
Default
category
Log category.
option
-traffic
Option
Description
traffic
Traffic log.
FortiOS 8.0.0 CLI Reference
1045
Fortinet Inc.

<!-- 来源页 1046 -->
Parameter
Description
Type
Size
Default
Option
Description
event
Event log.
virus
Antivirus log.
webfilter
Web filter log.
attack
Attack log.
spam
Antispam log.
anomaly
Anomaly log.
voip
VoIP log.
dlp
DLP log.
app-ctrl
Application control log.
waf
Web application firewall log.
dns
DNS detail log.
ssh
SSH log.
ssl
SSL log.
file-filter
File filter log.
icap
ICAP log.
virtual-patch
Virtual patch log.
debug
Debug log.
filter
Free style filter string.
string
Maximum
length: 1023
filter-type
Include/exclude logs that match the filter.
option
-include
Option
Description
include
Include logs that match the filter.
exclude
Exclude logs that match the filter.
id
Entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config log syslogd3 override-setting
Override settings for remote syslog server.
FortiOS 8.0.0 CLI Reference
1046
Fortinet Inc.

<!-- 来源页 1047 -->
config log syslogd3 override-setting
Description: Override settings for remote syslog server.
set certificate {string}
config custom-field-name
Description: Custom field name for CEF format logging.
edit <id>
set custom {string}
set name {string}
next
end
set custom-log-format {string}
set enc-algorithm [high-medium|high|...]
set facility [kernel|user|...]
set format [default|csv|...]
set interface {string}
set interface-select-method [auto|sdwan|...]
set max-log-rate {integer}
set mode [udp|legacy-reliable|...]
set port {integer}
set priority [default|low]
set server {string}
set source-ip {string}
set source-ip-interface {string}
set ssl-min-proto-version [default|SSLv3|...]
set status [enable|disable]
set use-management-vdom [enable|disable]
set vrf-select {integer}
end
config log syslogd3 override-setting
Parameter
Description
Type
Size
Default
certificate
Certificate used to communicate with Syslog
server.
string
Maximum
length: 35
custom-log-format *
Customized format for logs.
string
Maximum
length: 35
enc-algorithm
Enable/disable reliable syslogging with TLS
encryption.
option
-disable
Option
Description
high-medium
SSL communication with high and medium encryption algorithms.
high
SSL communication with high encryption algorithms.
low
SSL communication with low encryption algorithms.
disable
Disable SSL communication.
facility
Remote syslog facility.
option
-local7
FortiOS 8.0.0 CLI Reference
1047
Fortinet Inc.

<!-- 来源页 1048 -->
Parameter
Description
Type
Size
Default
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
Messages generated internally by syslog.
lpr
Line printer subsystem.
news
Network news subsystem.
uucp
Network news subsystem.
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
format
Log format.
option
-default
Option
Description
default
Syslog format.
csv
CSV (Comma Separated Values) format.
FortiOS 8.0.0 CLI Reference
1048
Fortinet Inc.

<!-- 来源页 1049 -->
Parameter
Description
Type
Size
Default
Option
Description
cef
CEF (Common Event Format) format.
rfc5424
Syslog RFC5424 format.
json
JSON (JavaScript Object Notation) format.
custom
Custom format.
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
max-log-rate
Syslog maximum log rate in MBps (0 = unlimited).
integer
Minimum
value: 0
Maximum
value:
100000
0
mode
Remote syslog logging over UDP/Reliable TCP.
option
-udp
Option
Description
udp
Enable syslogging over UDP.
legacy-reliable
Enable legacy reliable syslogging by RFC3195 (Reliable Delivery for
Syslog).
reliable
Enable reliable syslogging by RFC6587 (Transmission of Syslog
Messages over TCP).
port
Server listen port.
integer
Minimum
value: 0
Maximum
value:
65535
514
priority
Set log transmission priority.
option
-default
FortiOS 8.0.0 CLI Reference
1049
Fortinet Inc.

<!-- 来源页 1050 -->
Parameter
Description
Type
Size
Default
Option
Description
default
Set Syslog transmission priority to default.
low
Set Syslog transmission priority to low.
server
Address of remote syslog server.
string
Maximum
length: 127
source-ip
Source IP address of syslog.
string
Maximum
length: 63
source-ip-interface
Source interface of syslog.
string
Maximum
length: 15
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
Enable/disable remote syslog logging.
option
-disable
Option
Description
enable
Log to remote syslog server.
disable
Do not log to remote syslog server.
use-management-vdom
Enable/disable use of management VDOM as
source VDOM for logs sent to syslog server.
option
-disable
Option
Description
enable
Enable use of management VDOM as source VDOM.
disable
Use the current VDOM as source VDOM.
vrf-select
VRF ID used for connection to server.
integer
Minimum
value: 0
Maximum
value: 511
0
FortiOS 8.0.0 CLI Reference
1050
Fortinet Inc.

<!-- 来源页 1051 -->
* This parameter may not exist in some models.
config custom-field-name
Parameter
Description
Type
Size
Default
custom
Field custom name [A-Za-z0-9_].
string
Maximum
length: 35
id
Entry ID.
integer
Minimum
value: 0
Maximum
value: 255
0
name
Field name [A-Za-z0-9_].
string
Maximum
length: 35
config log syslogd3 setting
Global settings for remote syslog server.
config log syslogd3 setting
Description: Global settings for remote syslog server.
set certificate {string}
config custom-field-name
Description: Custom field name for CEF format logging.
edit <id>
set custom {string}
set name {string}
next
end
set custom-log-format {string}
set enc-algorithm [high-medium|high|...]
set facility [kernel|user|...]
set format [default|csv|...]
set interface {string}
set interface-select-method [auto|sdwan|...]
set max-log-rate {integer}
set mode [udp|legacy-reliable|...]
set port {integer}
set priority [default|low]
set server {string}
set source-ip {string}
set source-ip-interface {string}
set ssl-min-proto-version [default|SSLv3|...]
set status [enable|disable]
set vrf-select {integer}
end
FortiOS 8.0.0 CLI Reference
1051
Fortinet Inc.

<!-- 来源页 1052 -->
config log syslogd3 setting
Parameter
Description
Type
Size
Default
certificate
Certificate used to communicate with Syslog
server.
string
Maximum
length: 35
custom-log-format *
Customized format for logs.
string
Maximum
length: 35
enc-algorithm
Enable/disable reliable syslogging with TLS
encryption.
option
-disable
Option
Description
high-medium
SSL communication with high and medium encryption algorithms.
high
SSL communication with high encryption algorithms.
low
SSL communication with low encryption algorithms.
disable
Disable SSL communication.
facility
Remote syslog facility.
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
Messages generated internally by syslog.
lpr
Line printer subsystem.
news
Network news subsystem.
uucp
Network news subsystem.
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
FortiOS 8.0.0 CLI Reference
1052
Fortinet Inc.

<!-- 来源页 1053 -->
Parameter
Description
Type
Size
Default
Option
Description
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
format
Log format.
option
-default
Option
Description
default
Syslog format.
csv
CSV (Comma Separated Values) format.
cef
CEF (Common Event Format) format.
rfc5424
Syslog RFC5424 format.
json
JSON (JavaScript Object Notation) format.
custom
Custom format.
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
max-log-rate
Syslog maximum log rate in MBps (0 = unlimited).
integer
Minimum
value: 0
Maximum
value:
100000
0
FortiOS 8.0.0 CLI Reference
1053
Fortinet Inc.

<!-- 来源页 1054 -->
Parameter
Description
Type
Size
Default
mode
Remote syslog logging over UDP/Reliable TCP.
option
-udp
Option
Description
udp
Enable syslogging over UDP.
legacy-reliable
Enable legacy reliable syslogging by RFC3195 (Reliable Delivery for
Syslog).
reliable
Enable reliable syslogging by RFC6587 (Transmission of Syslog
Messages over TCP).
port
Server listen port.
integer
Minimum
value: 0
Maximum
value:
65535
514
priority
Set log transmission priority.
option
-default
Option
Description
default
Set Syslog transmission priority to default.
low
Set Syslog transmission priority to low.
server
Address of remote syslog server.
string
Maximum
length: 127
source-ip
Source IP address of syslog.
string
Maximum
length: 63
source-ip-interface
Source interface of syslog.
string
Maximum
length: 15
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
Enable/disable remote syslog logging.
option
-disable
FortiOS 8.0.0 CLI Reference
1054
Fortinet Inc.

<!-- 来源页 1055 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Log to remote syslog server.
disable
Do not log to remote syslog server.
vrf-select
VRF ID used for connection to server.
integer
Minimum
value: 0
Maximum
value: 511
0
* This parameter may not exist in some models.
config custom-field-name
Parameter
Description
Type
Size
Default
custom
Field custom name [A-Za-z0-9_].
string
Maximum
length: 35
id
Entry ID.
integer
Minimum
value: 0
Maximum
value: 255
0
name
Field name [A-Za-z0-9_].
string
Maximum
length: 35
config log syslogd4 filter
Filters for remote system server.
config log syslogd4 filter
Description: Filters for remote system server.
set anomaly [enable|disable]
set debug [enable|disable]
set forti-switch [enable|disable]
set forward-traffic [enable|disable]
config free-style
Description: Free style filters.
edit <id>
set category [traffic|event|...]
set filter {string}
set filter-type [include|exclude]
next
end
set gtp [enable|disable]
set http-transaction [enable|disable]
FortiOS 8.0.0 CLI Reference
1055
Fortinet Inc.

<!-- 来源页 1056 -->
set local-traffic [enable|disable]
set multicast-traffic [enable|disable]
set severity [emergency|alert|...]
set sniffer-traffic [enable|disable]
set voip [enable|disable]
set ztna-traffic [enable|disable]
end
config log syslogd4 filter
Parameter
Description
Type
Size
Default
anomaly
Enable/disable anomaly logging.
option
-enable
Option
Description
enable
Enable anomaly logging.
disable
Disable anomaly logging.
debug
Enable/disable debug logging.
option
-disable
Option
Description
enable
Enable Debug logging.
disable
Disable Debug logging.
forti-switch
Enable/disable Forti-Switch logging.
option
-enable
Option
Description
enable
Enable Forti-Switch logging.
disable
Disable Forti-Switch logging.
forward-traffic
Enable/disable forward traffic logging.
option
-enable
Option
Description
enable
Enable forward traffic logging.
disable
Disable forward traffic logging.
gtp *
Enable/disable GTP messages logging.
option
-enable
Option
Description
enable
Enable GTP messages logging.
disable
Disable GTP messages logging.
FortiOS 8.0.0 CLI Reference
1056
Fortinet Inc.

<!-- 来源页 1057 -->
Parameter
Description
Type
Size
Default
http-transaction
Enable/disable log HTTP transaction messages.
option
-enable
Option
Description
enable
Enable http transaction logging.
disable
Disable http transaction logging.
local-traffic
Enable/disable local in or out traffic logging.
option
-enable
Option
Description
enable
Enable local in or out traffic logging.
disable
Disable local in or out traffic logging.
multicast-traffic
Enable/disable multicast traffic logging.
option
-enable
Option
Description
enable
Enable multicast traffic logging.
disable
Disable multicast traffic logging.
severity
Lowest severity level to log.
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
sniffer-traffic
Enable/disable sniffer traffic logging.
option
-enable
Option
Description
enable
Enable sniffer traffic logging.
disable
Disable sniffer traffic logging.
voip
Enable/disable VoIP logging.
option
-enable
FortiOS 8.0.0 CLI Reference
1057
Fortinet Inc.

<!-- 来源页 1058 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable VoIP logging.
disable
Disable VoIP logging.
ztna-traffic
Enable/disable ztna traffic logging.
option
-enable
Option
Description
enable
Enable ztna traffic logging.
disable
Disable ztna traffic logging.
* This parameter may not exist in some models.
config free-style
Parameter
Description
Type
Size
Default
category
Log category.
option
-traffic
Option
Description
traffic
Traffic log.
event
Event log.
virus
Antivirus log.
webfilter
Web filter log.
attack
Attack log.
spam
Antispam log.
anomaly
Anomaly log.
voip
VoIP log.
dlp
DLP log.
app-ctrl
Application control log.
waf
Web application firewall log.
dns
DNS detail log.
ssh
SSH log.
ssl
SSL log.
file-filter
File filter log.
icap
ICAP log.
FortiOS 8.0.0 CLI Reference
1058
Fortinet Inc.

<!-- 来源页 1059 -->
Parameter
Description
Type
Size
Default
Option
Description
virtual-patch
Virtual patch log.
debug
Debug log.
filter
Free style filter string.
string
Maximum
length: 1023
filter-type
Include/exclude logs that match the filter.
option
-include
Option
Description
include
Include logs that match the filter.
exclude
Exclude logs that match the filter.
id
Entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config log syslogd4 override-filter
Override filters for remote system server.
config log syslogd4 override-filter
Description: Override filters for remote system server.
set anomaly [enable|disable]
set debug [enable|disable]
set forti-switch [enable|disable]
set forward-traffic [enable|disable]
config free-style
Description: Free style filters.
edit <id>
set category [traffic|event|...]
set filter {string}
set filter-type [include|exclude]
next
end
set gtp [enable|disable]
set http-transaction [enable|disable]
set local-traffic [enable|disable]
set multicast-traffic [enable|disable]
set severity [emergency|alert|...]
set sniffer-traffic [enable|disable]
set voip [enable|disable]
set ztna-traffic [enable|disable]
end
FortiOS 8.0.0 CLI Reference
1059
Fortinet Inc.

<!-- 来源页 1060 -->
config log syslogd4 override-filter
Parameter
Description
Type
Size
Default
anomaly
Enable/disable anomaly logging.
option
-enable
Option
Description
enable
Enable anomaly logging.
disable
Disable anomaly logging.
debug
Enable/disable debug logging.
option
-disable
Option
Description
enable
Enable Debug logging.
disable
Disable Debug logging.
forti-switch
Enable/disable Forti-Switch logging.
option
-enable
Option
Description
enable
Enable Forti-Switch logging.
disable
Disable Forti-Switch logging.
forward-traffic
Enable/disable forward traffic logging.
option
-enable
Option
Description
enable
Enable forward traffic logging.
disable
Disable forward traffic logging.
gtp *
Enable/disable GTP messages logging.
option
-enable
Option
Description
enable
Enable GTP messages logging.
disable
Disable GTP messages logging.
http-transaction
Enable/disable log HTTP transaction messages.
option
-enable
Option
Description
enable
Enable http transaction logging.
disable
Disable http transaction logging.
local-traffic
Enable/disable local in or out traffic logging.
option
-enable
FortiOS 8.0.0 CLI Reference
1060
Fortinet Inc.

<!-- 来源页 1061 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable local in or out traffic logging.
disable
Disable local in or out traffic logging.
multicast-traffic
Enable/disable multicast traffic logging.
option
-enable
Option
Description
enable
Enable multicast traffic logging.
disable
Disable multicast traffic logging.
severity
Lowest severity level to log.
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
sniffer-traffic
Enable/disable sniffer traffic logging.
option
-enable
Option
Description
enable
Enable sniffer traffic logging.
disable
Disable sniffer traffic logging.
voip
Enable/disable VoIP logging.
option
-enable
Option
Description
enable
Enable VoIP logging.
disable
Disable VoIP logging.
ztna-traffic
Enable/disable ztna traffic logging.
option
-enable
FortiOS 8.0.0 CLI Reference
1061
Fortinet Inc.

<!-- 来源页 1062 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable ztna traffic logging.
disable
Disable ztna traffic logging.
* This parameter may not exist in some models.
config free-style
Parameter
Description
Type
Size
Default
category
Log category.
option
-traffic
Option
Description
traffic
Traffic log.
event
Event log.
virus
Antivirus log.
webfilter
Web filter log.
attack
Attack log.
spam
Antispam log.
anomaly
Anomaly log.
voip
VoIP log.
dlp
DLP log.
app-ctrl
Application control log.
waf
Web application firewall log.
dns
DNS detail log.
ssh
SSH log.
ssl
SSL log.
file-filter
File filter log.
icap
ICAP log.
virtual-patch
Virtual patch log.
debug
Debug log.
filter
Free style filter string.
string
Maximum
length: 1023
filter-type
Include/exclude logs that match the filter.
option
-include
FortiOS 8.0.0 CLI Reference
1062
Fortinet Inc.

<!-- 来源页 1063 -->
Parameter
Description
Type
Size
Default
Option
Description
include
Include logs that match the filter.
exclude
Exclude logs that match the filter.
id
Entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config log syslogd4 override-setting
Override settings for remote syslog server.
config log syslogd4 override-setting
Description: Override settings for remote syslog server.
set certificate {string}
config custom-field-name
Description: Custom field name for CEF format logging.
edit <id>
set custom {string}
set name {string}
next
end
set custom-log-format {string}
set enc-algorithm [high-medium|high|...]
set facility [kernel|user|...]
set format [default|csv|...]
set interface {string}
set interface-select-method [auto|sdwan|...]
set max-log-rate {integer}
set mode [udp|legacy-reliable|...]
set port {integer}
set priority [default|low]
set server {string}
set source-ip {string}
set source-ip-interface {string}
set ssl-min-proto-version [default|SSLv3|...]
set status [enable|disable]
set use-management-vdom [enable|disable]
set vrf-select {integer}
end
FortiOS 8.0.0 CLI Reference
1063
Fortinet Inc.

<!-- 来源页 1064 -->
config log syslogd4 override-setting
Parameter
Description
Type
Size
Default
certificate
Certificate used to communicate with Syslog
server.
string
Maximum
length: 35
custom-log-format *
Customized format for logs.
string
Maximum
length: 35
enc-algorithm
Enable/disable reliable syslogging with TLS
encryption.
option
-disable
Option
Description
high-medium
SSL communication with high and medium encryption algorithms.
high
SSL communication with high encryption algorithms.
low
SSL communication with low encryption algorithms.
disable
Disable SSL communication.
facility
Remote syslog facility.
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
Messages generated internally by syslog.
lpr
Line printer subsystem.
news
Network news subsystem.
uucp
Network news subsystem.
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
FortiOS 8.0.0 CLI Reference
1064
Fortinet Inc.

<!-- 来源页 1065 -->
Parameter
Description
Type
Size
Default
Option
Description
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
format
Log format.
option
-default
Option
Description
default
Syslog format.
csv
CSV (Comma Separated Values) format.
cef
CEF (Common Event Format) format.
rfc5424
Syslog RFC5424 format.
json
JSON (JavaScript Object Notation) format.
custom
Custom format.
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
max-log-rate
Syslog maximum log rate in MBps (0 = unlimited).
integer
Minimum
value: 0
Maximum
value:
100000
0
mode
Remote syslog logging over UDP/Reliable TCP.
option
-udp
FortiOS 8.0.0 CLI Reference
1065
Fortinet Inc.

<!-- 来源页 1066 -->
Parameter
Description
Type
Size
Default
Option
Description
udp
Enable syslogging over UDP.
legacy-reliable
Enable legacy reliable syslogging by RFC3195 (Reliable Delivery for
Syslog).
reliable
Enable reliable syslogging by RFC6587 (Transmission of Syslog
Messages over TCP).
port
Server listen port.
integer
Minimum
value: 0
Maximum
value:
65535
514
priority
Set log transmission priority.
option
-default
Option
Description
default
Set Syslog transmission priority to default.
low
Set Syslog transmission priority to low.
server
Address of remote syslog server.
string
Maximum
length: 127
source-ip
Source IP address of syslog.
string
Maximum
length: 63
source-ip-interface
Source interface of syslog.
string
Maximum
length: 15
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
Enable/disable remote syslog logging.
option
-disable
FortiOS 8.0.0 CLI Reference
1066
Fortinet Inc.

<!-- 来源页 1067 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Log to remote syslog server.
disable
Do not log to remote syslog server.
use-management-vdom
Enable/disable use of management VDOM as
source VDOM for logs sent to syslog server.
option
-disable
Option
Description
enable
Enable use of management VDOM as source VDOM.
disable
Use the current VDOM as source VDOM.
vrf-select
VRF ID used for connection to server.
integer
Minimum
value: 0
Maximum
value: 511
0
* This parameter may not exist in some models.
config custom-field-name
Parameter
Description
Type
Size
Default
custom
Field custom name [A-Za-z0-9_].
string
Maximum
length: 35
id
Entry ID.
integer
Minimum
value: 0
Maximum
value: 255
0
name
Field name [A-Za-z0-9_].
string
Maximum
length: 35
config log syslogd4 setting
Global settings for remote syslog server.
config log syslogd4 setting
Description: Global settings for remote syslog server.
set certificate {string}
config custom-field-name
Description: Custom field name for CEF format logging.
edit <id>
set custom {string}
FortiOS 8.0.0 CLI Reference
1067
Fortinet Inc.

<!-- 来源页 1068 -->
set name {string}
next
end
set custom-log-format {string}
set enc-algorithm [high-medium|high|...]
set facility [kernel|user|...]
set format [default|csv|...]
set interface {string}
set interface-select-method [auto|sdwan|...]
set max-log-rate {integer}
set mode [udp|legacy-reliable|...]
set port {integer}
set priority [default|low]
set server {string}
set source-ip {string}
set source-ip-interface {string}
set ssl-min-proto-version [default|SSLv3|...]
set status [enable|disable]
set vrf-select {integer}
end
config log syslogd4 setting
Parameter
Description
Type
Size
Default
certificate
Certificate used to communicate with Syslog
server.
string
Maximum
length: 35
custom-log-format *
Customized format for logs.
string
Maximum
length: 35
enc-algorithm
Enable/disable reliable syslogging with TLS
encryption.
option
-disable
Option
Description
high-medium
SSL communication with high and medium encryption algorithms.
high
SSL communication with high encryption algorithms.
low
SSL communication with low encryption algorithms.
disable
Disable SSL communication.
facility
Remote syslog facility.
option
-local7
Option
Description
kernel
Kernel messages.
user
Random user-level messages.
FortiOS 8.0.0 CLI Reference
1068
Fortinet Inc.

<!-- 来源页 1069 -->
Parameter
Description
Type
Size
Default
Option
Description
mail
Mail system.
daemon
System daemons.
auth
Security/authorization messages.
syslog
Messages generated internally by syslog.
lpr
Line printer subsystem.
news
Network news subsystem.
uucp
Network news subsystem.
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
format
Log format.
option
-default
Option
Description
default
Syslog format.
csv
CSV (Comma Separated Values) format.
cef
CEF (Common Event Format) format.
rfc5424
Syslog RFC5424 format.
FortiOS 8.0.0 CLI Reference
1069
Fortinet Inc.

<!-- 来源页 1070 -->
Parameter
Description
Type
Size
Default
Option
Description
json
JSON (JavaScript Object Notation) format.
custom
Custom format.
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
max-log-rate
Syslog maximum log rate in MBps (0 = unlimited).
integer
Minimum
value: 0
Maximum
value:
100000
0
mode
Remote syslog logging over UDP/Reliable TCP.
option
-udp
Option
Description
udp
Enable syslogging over UDP.
legacy-reliable
Enable legacy reliable syslogging by RFC3195 (Reliable Delivery for
Syslog).
reliable
Enable reliable syslogging by RFC6587 (Transmission of Syslog
Messages over TCP).
port
Server listen port.
integer
Minimum
value: 0
Maximum
value:
65535
514
priority
Set log transmission priority.
option
-default
Option
Description
default
Set Syslog transmission priority to default.
low
Set Syslog transmission priority to low.
FortiOS 8.0.0 CLI Reference
1070
Fortinet Inc.

<!-- 来源页 1071 -->
Parameter
Description
Type
Size
Default
server
Address of remote syslog server.
string
Maximum
length: 127
source-ip
Source IP address of syslog.
string
Maximum
length: 63
source-ip-interface
Source interface of syslog.
string
Maximum
length: 15
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
Enable/disable remote syslog logging.
option
-disable
Option
Description
enable
Log to remote syslog server.
disable
Do not log to remote syslog server.
vrf-select
VRF ID used for connection to server.
integer
Minimum
value: 0
Maximum
value: 511
0
* This parameter may not exist in some models.
config custom-field-name
Parameter
Description
Type
Size
Default
custom
Field custom name [A-Za-z0-9_].
string
Maximum
length: 35
id
Entry ID.
integer
Minimum
value: 0
Maximum
value: 255
0
FortiOS 8.0.0 CLI Reference
1071
Fortinet Inc.

<!-- 来源页 1072 -->
Parameter
Description
Type
Size
Default
name
Field name [A-Za-z0-9_].
string
Maximum
length: 35
config log tacacs+accounting filter
Settings for TACACS+ accounting events filter.
config log tacacs+accounting filter
Description: Settings for TACACS+ accounting events filter.
set cli-cmd-audit [enable|disable]
set config-change-audit [enable|disable]
set login-audit [enable|disable]
end
config log tacacs+accounting filter
Parameter
Description
Type
Size
Default
cli-cmd-audit
Enable/disable TACACS+ accounting for CLI
commands audit.
option
-disable
Option
Description
enable
Enable TACACS+ accounting for CLI commands audit.
disable
Disable TACACS+ accounting for CLI commands audit.
config-change-audit
Enable/disable TACACS+ accounting for
configuration change events audit.
option
-enable
Option
Description
enable
Enable TACACS+ accounting for configuration change events audit.
disable
Disable TACACS+ accounting for configuration change events audit.
login-audit
Enable/disable TACACS+ accounting for login
events audit.
option
-enable
Option
Description
enable
Enable TACACS+ accounting for login events audit.
disable
Disable TACACS+ accounting for login events audit.
FortiOS 8.0.0 CLI Reference
1072
Fortinet Inc.

<!-- 来源页 1073 -->
config log tacacs+accounting setting
Settings for TACACS+ accounting.
config log tacacs+accounting setting
Description: Settings for TACACS+ accounting.
set interface {string}
set interface-select-method [auto|sdwan|...]
set port {integer}
set server {string}
set server-key {password}
set source-ip {string}
set status [enable|disable]
set timeout {integer}
set vrf-select {integer}
end
config log tacacs+accounting setting
Parameter
Description
Type
Size
Default
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
port *
Server listen port.
integer
Minimum
value: 1
Maximum
value:
65535
49
server
Address of TACACS+ server.
string
Maximum
length: 63
server-key
Key to access the TACACS+ server.
password
Not
Specified
source-ip
Source IP address for communication to TACACS+
server.
string
Maximum
length: 63
FortiOS 8.0.0 CLI Reference
1073
Fortinet Inc.

<!-- 来源页 1074 -->
Parameter
Description
Type
Size
Default
status
Enable/disable TACACS+ accounting.
option
-disable
Option
Description
enable
Enable TACACS+ accounting.
disable
Disable TACACS+ accounting.
timeout *
connection time-out in seconds.
integer
Minimum
value: 1
Maximum
value: 3600
5
vrf-select
VRF ID used for connection to server.
integer
Minimum
value: 0
Maximum
value: 511
0
* This parameter may not exist in some models.
config log tacacs+accounting2 filter
Settings for TACACS+ accounting events filter.
config log tacacs+accounting2 filter
Description: Settings for TACACS+ accounting events filter.
set cli-cmd-audit [enable|disable]
set config-change-audit [enable|disable]
set login-audit [enable|disable]
end
config log tacacs+accounting2 filter
Parameter
Description
Type
Size
Default
cli-cmd-audit
Enable/disable TACACS+ accounting for CLI
commands audit.
option
-disable
Option
Description
enable
Enable TACACS+ accounting for CLI commands audit.
disable
Disable TACACS+ accounting for CLI commands audit.
config-change-audit
Enable/disable TACACS+ accounting for
configuration change events audit.
option
-enable
FortiOS 8.0.0 CLI Reference
1074
Fortinet Inc.

<!-- 来源页 1075 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable TACACS+ accounting for configuration change events audit.
disable
Disable TACACS+ accounting for configuration change events audit.
login-audit
Enable/disable TACACS+ accounting for login
events audit.
option
-enable
Option
Description
enable
Enable TACACS+ accounting for login events audit.
disable
Disable TACACS+ accounting for login events audit.
config log tacacs+accounting2 setting
Settings for TACACS+ accounting.
config log tacacs+accounting2 setting
Description: Settings for TACACS+ accounting.
set interface {string}
set interface-select-method [auto|sdwan|...]
set port {integer}
set server {string}
set server-key {password}
set source-ip {string}
set status [enable|disable]
set timeout {integer}
set vrf-select {integer}
end
config log tacacs+accounting2 setting
Parameter
Description
Type
Size
Default
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
1075
Fortinet Inc.

<!-- 来源页 1076 -->
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
port *
Server listen port.
integer
Minimum
value: 1
Maximum
value:
65535
49
server
Address of TACACS+ server.
string
Maximum
length: 63
server-key
Key to access the TACACS+ server.
password
Not
Specified
source-ip
Source IP address for communication to TACACS+
server.
string
Maximum
length: 63
status
Enable/disable TACACS+ accounting.
option
-disable
Option
Description
enable
Enable TACACS+ accounting.
disable
Disable TACACS+ accounting.
timeout *
connection time-out in seconds.
integer
Minimum
value: 1
Maximum
value: 3600
5
vrf-select
VRF ID used for connection to server.
integer
Minimum
value: 0
Maximum
value: 511
0
* This parameter may not exist in some models.
config log tacacs+accounting3 filter
Settings for TACACS+ accounting events filter.
config log tacacs+accounting3 filter
Description: Settings for TACACS+ accounting events filter.
set cli-cmd-audit [enable|disable]
set config-change-audit [enable|disable]
set login-audit [enable|disable]
end
FortiOS 8.0.0 CLI Reference
1076
Fortinet Inc.

<!-- 来源页 1077 -->
config log tacacs+accounting3 filter
Parameter
Description
Type
Size
Default
cli-cmd-audit
Enable/disable TACACS+ accounting for CLI
commands audit.
option
-disable
Option
Description
enable
Enable TACACS+ accounting for CLI commands audit.
disable
Disable TACACS+ accounting for CLI commands audit.
config-change-audit
Enable/disable TACACS+ accounting for
configuration change events audit.
option
-enable
Option
Description
enable
Enable TACACS+ accounting for configuration change events audit.
disable
Disable TACACS+ accounting for configuration change events audit.
login-audit
Enable/disable TACACS+ accounting for login
events audit.
option
-enable
Option
Description
enable
Enable TACACS+ accounting for login events audit.
disable
Disable TACACS+ accounting for login events audit.
config log tacacs+accounting3 setting
Settings for TACACS+ accounting.
config log tacacs+accounting3 setting
Description: Settings for TACACS+ accounting.
set interface {string}
set interface-select-method [auto|sdwan|...]
set port {integer}
set server {string}
set server-key {password}
set source-ip {string}
set status [enable|disable]
set timeout {integer}
set vrf-select {integer}
end
FortiOS 8.0.0 CLI Reference
1077
Fortinet Inc.

<!-- 来源页 1078 -->
config log tacacs+accounting3 setting
Parameter
Description
Type
Size
Default
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
port *
Server listen port.
integer
Minimum
value: 1
Maximum
value:
65535
49
server
Address of TACACS+ server.
string
Maximum
length: 63
server-key
Key to access the TACACS+ server.
password
Not
Specified
source-ip
Source IP address for communication to TACACS+
server.
string
Maximum
length: 63
status
Enable/disable TACACS+ accounting.
option
-disable
Option
Description
enable
Enable TACACS+ accounting.
disable
Disable TACACS+ accounting.
timeout *
connection time-out in seconds.
integer
Minimum
value: 1
Maximum
value: 3600
5
vrf-select
VRF ID used for connection to server.
integer
Minimum
value: 0
Maximum
value: 511
0
* This parameter may not exist in some models.
FortiOS 8.0.0 CLI Reference
1078
Fortinet Inc.

<!-- 来源页 1079 -->
config log threat-weight
Configure threat weight settings.
config log threat-weight
Description: Configure threat weight settings.
config application
Description: Application-control threat weight settings.
edit <id>
set category {integer}
set level [disable|low|...]
next
end
set blocked-connection [disable|low|...]
set botnet-connection-detected [disable|low|...]
set failed-connection [disable|low|...]
config geolocation
Description: Geolocation-based threat weight settings.
edit <id>
set country {string}
set level [disable|low|...]
next
end
config ips
Description: IPS threat weight settings.
set critical-severity [disable|low|...]
set high-severity [disable|low|...]
set info-severity [disable|low|...]
set low-severity [disable|low|...]
set medium-severity [disable|low|...]
end
config level
Description: Score mapping for threat weight levels.
set critical {integer}
set high {integer}
set low {integer}
set medium {integer}
end
config malware
Description: Anti-virus malware threat weight settings.
set command-blocked [disable|low|...]
set content-disarm [disable|low|...]
set ems-threat-feed [disable|low|...]
set file-blocked [disable|low|...]
set fsa-high-risk [disable|low|...]
set fsa-malicious [disable|low|...]
set fsa-medium-risk [disable|low|...]
set inline-block [disable|low|...]
set malware-list [disable|low|...]
set mimefragmented [disable|low|...]
set oversized [disable|low|...]
FortiOS 8.0.0 CLI Reference
1079
Fortinet Inc.

<!-- 来源页 1080 -->
set switch-proto [disable|low|...]
set virus-file-type-executable [disable|low|...]
set virus-infected [disable|low|...]
set virus-outbreak-prevention [disable|low|...]
set virus-scan-error [disable|low|...]
end
set status [enable|disable]
set url-block-detected [disable|low|...]
config web
Description: Web filtering threat weight settings.
edit <id>
set category {integer}
set level [disable|low|...]
next
end
end
config log threat-weight
Parameter
Description
Type
Size
Default
blocked-connection
Threat weight score for blocked connections.
option
-high
Option
Description
disable
Disable threat weight scoring for blocked connections.
low
Use the low level score for blocked connections.
medium
Use the medium level score for blocked connections.
high
Use the high level score for blocked connections.
critical
Use the critical level score for blocked connections.
botnet-connection-detected
Threat weight score for detected botnet
connections.
option
-critical
Option
Description
disable
Disable threat weight scoring for detected botnet connections.
low
Use the low level score for detected botnet connections.
medium
Use the medium level score for detected botnet connections.
high
Use the high level score for detected botnet connections.
critical
Use the critical level score for detected botnet connections.
FortiOS 8.0.0 CLI Reference
1080
Fortinet Inc.

<!-- 来源页 1081 -->
Parameter
Description
Type
Size
Default
failed-connection
Threat weight score for failed connections.
option
-low
Option
Description
disable
Disable threat weight scoring for failed connections.
low
Use the low level score for failed connections.
medium
Use the medium level score for failed connections.
high
Use the high level score for failed connections.
critical
Use the critical level score for failed connections.
status
Enable/disable the threat weight feature.
option
-enable
Option
Description
enable
Enable the threat weight feature.
disable
Disable the threat weight feature.
url-block-detected
Threat weight score for URL blocking.
option
-high
Option
Description
disable
Disable threat weight scoring for URL blocking.
low
Use the low level score for URL blocking.
medium
Use the medium level score for URL blocking.
high
Use the high level score for URL blocking.
critical
Use the critical level score for URL blocking.
config application
Parameter
Description
Type
Size
Default
category
Application category.
integer
Minimum
value: 0
Maximum
value:
65535
0
id
Entry ID.
integer
Minimum
value: 0
Maximum
value: 255
0
FortiOS 8.0.0 CLI Reference
1081
Fortinet Inc.

<!-- 来源页 1082 -->
Parameter
Description
Type
Size
Default
level
Threat weight score for Application events.
option
-low
Option
Description
disable
Disable threat weight scoring for Application events.
low
Use the low level score for Application events.
medium
Use the medium level score for Application events.
high
Use the high level score for Application events.
critical
Use the critical level score for Application events.
config geolocation
Parameter
Description
Type
Size
Default
country
Country code.
string
Maximum
length: 2
id
Entry ID.
integer
Minimum
value: 0
Maximum
value: 255
0
level
Threat weight score for Geolocation-based events.
option
-low
Option
Description
disable
Disable threat weight scoring for Geolocation-based events.
low
Use the low level score for Geolocation-based events.
medium
Use the medium level score for Geolocation-based events.
high
Use the high level score for Geolocation-based events.
critical
Use the critical level score for Geolocation-based events.
config ips
Parameter
Description
Type
Size
Default
critical-severity
Threat weight score for IPS critical severity events.
option
-critical
Option
Description
disable
Disable threat weight scoring for IPS critical severity events.
FortiOS 8.0.0 CLI Reference
1082
Fortinet Inc.

<!-- 来源页 1083 -->
Parameter
Description
Type
Size
Default
Option
Description
low
Use the low level score for IPS critical severity events.
medium
Use the medium level score for IPS critical severity events.
high
Use the high level score for IPS critical severity events.
critical
Use the critical level score for IPS critical severity events.
high-severity
Threat weight score for IPS high severity events.
option
-high
Option
Description
disable
Disable threat weight scoring for IPS high severity events.
low
Use the low level score for IPS high severity events.
medium
Use the medium level score for IPS high severity events.
high
Use the high level score for IPS high severity events.
critical
Use the critical level score for IPS high severity events.
info-severity
Threat weight score for IPS info severity events.
option
-disable
Option
Description
disable
Disable threat weight scoring for IPS info severity events.
low
Use the low level score for IPS info severity events.
medium
Use the medium level score for IPS info severity events.
high
Use the high level score for IPS info severity events.
critical
Use the critical level score for IPS info severity events.
low-severity
Threat weight score for IPS low severity events.
option
-low
Option
Description
disable
Disable threat weight scoring for IPS low severity events.
low
Use the low level score for IPS low severity events.
medium
Use the medium level score for IPS low severity events.
high
Use the high level score for IPS low severity events.
critical
Use the critical level score for IPS low severity events.
medium-severity
Threat weight score for IPS medium severity events.
option
-medium
FortiOS 8.0.0 CLI Reference
1083
Fortinet Inc.

<!-- 来源页 1084 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable threat weight scoring for IPS medium severity events.
low
Use the low level score for IPS medium severity events.
medium
Use the medium level score for IPS medium severity events.
high
Use the high level score for IPS medium severity events.
critical
Use the critical level score for IPS medium severity events.
config level
Parameter
Description
Type
Size
Default
critical
Critical level score value (1 - 100).
integer
Minimum
value: 1
Maximum
value: 100
50
high
High level score value (1 - 100).
integer
Minimum
value: 1
Maximum
value: 100
30
low
Low level score value (1 - 100).
integer
Minimum
value: 1
Maximum
value: 100
5
medium
Medium level score value (1 - 100).
integer
Minimum
value: 1
Maximum
value: 100
10
config malware
Parameter
Description
Type
Size
Default
command-blocked
Threat weight score for blocked command
detected.
option
-disable
Option
Description
disable
Disable threat weight scoring for blocked command detected.
low
Use the low level score for blocked command detected.
medium
Use the medium level score for blocked command detected.
FortiOS 8.0.0 CLI Reference
1084
Fortinet Inc.

<!-- 来源页 1085 -->
Parameter
Description
Type
Size
Default
Option
Description
high
Use the high level score for blocked command detected.
critical
Use the critical level score for blocked command detected.
content-disarm
Threat weight score for virus (content disarm)
detected.
option
-medium
Option
Description
disable
Disable threat weight scoring for virus (content disarm) detected.
low
Use the low level score for virus (content disarm) detected.
medium
Use the medium level score for virus (content disarm) detected.
high
Use the high level score for virus (content disarm) detected.
critical
Use the critical level score for virus (content disarm) detected.
ems-threat-feed
Threat weight score for virus (EMS threat feed)
detected.
option
-medium
Option
Description
disable
Disable threat weight scoring for virus (EMS threat feed) detected.
low
Use the low level score for virus (EMS threat feed) detected.
medium
Use the medium level score for virus (EMS threat feed) detected.
high
Use the high level score for virus (EMS threat feed) detected.
critical
Use the critical level score for virus (EMS threat feed) detected.
file-blocked
Threat weight score for blocked file detected.
option
-low
Option
Description
disable
Disable threat weight scoring for blocked file detected.
low
Use the low level score for blocked file detected.
medium
Use the medium level score for blocked file detected.
high
Use the high level score for blocked file detected.
critical
Use the critical level score for blocked file detected.
fsa-high-risk
Threat weight score for FortiSandbox high risk
malware detected.
option
-high
FortiOS 8.0.0 CLI Reference
1085
Fortinet Inc.

<!-- 来源页 1086 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable threat weight scoring for FortiSandbox high risk malware
detected.
low
Use the low level score for FortiSandbox high risk malware
detected.
medium
Use the medium level score for FortiSandbox high risk malware
detected.
high
Use the high level score for FortiSandbox high risk malware
detected.
critical
Use the critical level score for FortiSandbox high risk malware
detected.
fsa-malicious
Threat weight score for FortiSandbox malicious
malware detected.
option
-critical
Option
Description
disable
Disable threat weight scoring for FortiSandbox malicious malware
detected.
low
Use the low level score for FortiSandbox malicious malware
detected.
medium
Use the medium level score for FortiSandbox malicious malware
detected.
high
Use the high level score for FortiSandbox malicious malware
detected.
critical
Use the critical level score for FortiSandbox malicious malware
detected.
fsa-medium-risk
Threat weight score for FortiSandbox medium
risk malware detected.
option
-medium
Option
Description
disable
Disable threat weight scoring for FortiSandbox medium risk
malware detected.
low
Use the low level score for FortiSandbox medium risk malware
detected.
medium
Use the medium level score for FortiSandbox medium risk malware
detected.
FortiOS 8.0.0 CLI Reference
1086
Fortinet Inc.

<!-- 来源页 1087 -->
Parameter
Description
Type
Size
Default
Option
Description
high
Use the high level score for FortiSandbox medium risk malware
detected.
critical
Use the critical level score for FortiSandbox medium risk malware
detected.
inline-block
Threat weight score for malware detected by
inline block.
option
-critical
Option
Description
disable
Disable threat weight scoring for virus detected by inline block.
low
Use the low level score for virus detected by inline block.
medium
Use the medium level score for virus detected by inline block.
high
Use the high level score for virus detected by inline block.
critical
Use the critical level score for virus detected by inline block.
malware-list
Threat weight score for virus (malware list)
detected.
option
-medium
Option
Description
disable
Disable threat weight scoring for virus (malware list) detected.
low
Use the low level score for virus (malware list) detected.
medium
Use the medium level score for virus (malware list) detected.
high
Use the high level score for virus (malware list) detected.
critical
Use the critical level score for virus (malware list) detected.
mimefragmented
Threat weight score for mimefragmented
detected.
option
-disable
Option
Description
disable
Disable threat weight scoring for mimefragmented detected.
low
Use the low level score for mimefragmented detected.
medium
Use the medium level score for mimefragmented detected.
high
Use the high level score for mimefragmented detected.
critical
Use the critical level score for mimefragmented detected.
oversized
Threat weight score for oversized file detected.
option
-disable
FortiOS 8.0.0 CLI Reference
1087
Fortinet Inc.

<!-- 来源页 1088 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable threat weight scoring for oversized file detected.
low
Use the low level score for oversized file detected.
medium
Use the medium level score for oversized file detected.
high
Use the high level score for oversized file detected.
critical
Use the critical level score for oversized file detected.
switch-proto
Threat weight score for switch proto detected.
option
-disable
Option
Description
disable
Disable threat weight scoring for switch proto detected.
low
Use the low level score for switch proto detected.
medium
Use the medium level score for switch proto detected.
high
Use the high level score for switch proto detected.
critical
Use the critical level score for switch proto detected.
virus-file-type-executable
Threat weight score for virus (file type
executable) detected.
option
-medium
Option
Description
disable
Disable threat weight scoring for virus (filetype executable)
detected.
low
Use the low level score for virus (filetype executable) detected.
medium
Use the medium level score for virus (filetype executable) detected.
high
Use the high level score for virus (filetype executable) detected.
critical
Use the critical level score for virus (filetype executable) detected.
virus-infected
Threat weight score for virus (infected)
detected.
option
-critical
Option
Description
disable
Disable threat weight scoring for virus (infected) detected.
low
Use the low level score for virus (infected) detected.
medium
Use the medium level score for virus (infected) detected.
high
Use the high level score for virus (infected) detected.
critical
Use the critical level score for virus (infected) detected.
FortiOS 8.0.0 CLI Reference
1088
Fortinet Inc.

<!-- 来源页 1089 -->
Parameter
Description
Type
Size
Default
virus-outbreak-prevention
Threat weight score for virus (outbreak
prevention) event.
option
-critical
Option
Description
disable
Disable threat weight scoring for virus (outbreak prevention) event.
low
Use the low level score for virus (outbreak prevention) event.
medium
Use the medium level score for virus (outbreak prevention) event.
high
Use the high level score for virus (outbreak prevention) event.
critical
Use the critical level score for virus (outbreak prevention) event.
virus-scan-error
Threat weight score for virus (scan error)
detected.
option
-high
Option
Description
disable
Disable threat weight scoring for virus (scan error) detected.
low
Use the low level score for virus (scan error) detected.
medium
Use the medium level score for virus (scan error) detected.
high
Use the high level score for virus (scan error) detected.
critical
Use the critical level score for virus (scan error) detected.
config web
Parameter
Description
Type
Size
Default
category
Threat weight score for web category filtering
matches.
integer
Minimum
value: 0
Maximum
value: 255
0
id
Entry ID.
integer
Minimum
value: 0
Maximum
value: 255
0
level
Threat weight score for web category filtering
matches.
option
-low
Option
Description
disable
Disable threat weight scoring for web category filtering matches.
low
Use the low level score for web category filtering matches.
FortiOS 8.0.0 CLI Reference
1089
Fortinet Inc.

<!-- 来源页 1090 -->
Parameter
Description
Type
Size
Default
Option
Description
medium
Use the medium level score for web category filtering matches.
high
Use the high level score for web category filtering matches.
critical
Use the critical level score for web category filtering matches.
config log webtrends filter
Filters for WebTrends.
config log webtrends filter
Description: Filters for WebTrends.
set anomaly [enable|disable]
set debug [enable|disable]
set forti-switch [enable|disable]
set forward-traffic [enable|disable]
config free-style
Description: Free style filters.
edit <id>
set category [traffic|event|...]
set filter {string}
set filter-type [include|exclude]
next
end
set gtp [enable|disable]
set http-transaction [enable|disable]
set local-traffic [enable|disable]
set multicast-traffic [enable|disable]
set severity [emergency|alert|...]
set sniffer-traffic [enable|disable]
set voip [enable|disable]
set ztna-traffic [enable|disable]
end
config log webtrends filter
Parameter
Description
Type
Size
Default
anomaly
Enable/disable anomaly logging.
option
-enable
Option
Description
enable
Enable anomaly logging.
disable
Disable anomaly logging.
FortiOS 8.0.0 CLI Reference
1090
Fortinet Inc.

<!-- 来源页 1091 -->
Parameter
Description
Type
Size
Default
debug
Enable/disable debug logging.
option
-disable
Option
Description
enable
Enable Debug logging.
disable
Disable Debug logging.
forti-switch
Enable/disable Forti-Switch logging.
option
-enable
Option
Description
enable
Enable Forti-Switch logging.
disable
Disable Forti-Switch logging.
forward-traffic
Enable/disable forward traffic logging.
option
-enable
Option
Description
enable
Enable forward traffic logging.
disable
Disable forward traffic logging.
gtp *
Enable/disable GTP messages logging.
option
-enable
Option
Description
enable
Enable GTP messages logging.
disable
Disable GTP messages logging.
http-transaction
Enable/disable log HTTP transaction messages.
option
-enable
Option
Description
enable
Enable http transaction logging.
disable
Disable http transaction logging.
local-traffic
Enable/disable local in or out traffic logging.
option
-enable
Option
Description
enable
Enable local in or out traffic logging.
disable
Disable local in or out traffic logging.
multicast-traffic
Enable/disable multicast traffic logging.
option
-enable
FortiOS 8.0.0 CLI Reference
1091
Fortinet Inc.

<!-- 来源页 1092 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable multicast traffic logging.
disable
Disable multicast traffic logging.
severity
Lowest severity level to log to WebTrends.
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
sniffer-traffic
Enable/disable sniffer traffic logging.
option
-enable
Option
Description
enable
Enable sniffer traffic logging.
disable
Disable sniffer traffic logging.
voip
Enable/disable VoIP logging.
option
-enable
Option
Description
enable
Enable VoIP logging.
disable
Disable VoIP logging.
ztna-traffic
Enable/disable ztna traffic logging.
option
-enable
Option
Description
enable
Enable ztna traffic logging.
disable
Disable ztna traffic logging.
* This parameter may not exist in some models.
FortiOS 8.0.0 CLI Reference
1092
Fortinet Inc.

<!-- 来源页 1093 -->
config free-style
Parameter
Description
Type
Size
Default
category
Log category.
option
-traffic
Option
Description
traffic
Traffic log.
event
Event log.
virus
Antivirus log.
webfilter
Web filter log.
attack
Attack log.
spam
Antispam log.
anomaly
Anomaly log.
voip
VoIP log.
dlp
DLP log.
app-ctrl
Application control log.
waf
Web application firewall log.
dns
DNS detail log.
ssh
SSH log.
ssl
SSL log.
file-filter
File filter log.
icap
ICAP log.
virtual-patch
Virtual patch log.
debug
Debug log.
filter
Free style filter string.
string
Maximum
length: 1023
filter-type
Include/exclude logs that match the filter.
option
-include
Option
Description
include
Include logs that match the filter.
exclude
Exclude logs that match the filter.
id
Entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
FortiOS 8.0.0 CLI Reference
1093
Fortinet Inc.

<!-- 来源页 1094 -->
config log webtrends setting
Settings for WebTrends.
config log webtrends setting
Description: Settings for WebTrends.
set server {string}
set status [enable|disable]
end
config log webtrends setting
Parameter
Description
Type
Size
Default
server
Address of the remote WebTrends server.
string
Maximum
length: 63
status
Enable/disable logging to WebTrends.
option
-disable
Option
Description
enable
Enable logging to WebTrends.
disable
Disble logging to WebTrends.
FortiOS 8.0.0 CLI Reference
1094
Fortinet Inc.

---


<!-- 来源页 1095 -->
monitoring
This section includes syntax for the following commands:
l config monitoring np6-ipsec-engine on page 1095
l config monitoring npu-hpe on page 1097
config monitoring np6-ipsec-engine
This command is available for model(s): FortiGate 1000D, FortiGate 1100E, FortiGate 1101E, FortiGate
2000E, FortiGate 2200E, FortiGate 2201E, FortiGate 2500E, FortiGate 300E, FortiGate 301E,
FortiGate 3300E, FortiGate 3301E, FortiGate 3400E, FortiGate 3401E, FortiGate 3600E, FortiGate
3601E, FortiGate 3960E, FortiGate 3980E, FortiGate 400E Bypass, FortiGate 400E, FortiGate 401E,
FortiGate 500E, FortiGate 501E, FortiGate 600E, FortiGate 601E, FortiGate 800D, FortiGate 900D.
It is not available for: FortiGate 1000F, FortiGate 1001F, FortiGate 100F, FortiGate 101F Gen2,
FortiGate 120G, FortiGate 121G, FortiGate 1800F, FortiGate 1801F, FortiGate 200E, FortiGate 200F,
FortiGate 200G, FortiGate 201E, FortiGate 201F, FortiGate 201G, FortiGate 2600F, FortiGate 2601F,
FortiGate 3000F, FortiGate 3001F, FortiGate 30G, FortiGate 31G, FortiGate 3200F, FortiGate 3201F
Gen2, FortiGate 3500F Gen2, FortiGate 3501F Gen2, FortiGate 3700F, FortiGate 3701F, FortiGate
400F, FortiGate 401F, FortiGate 40F 3G4G, FortiGate 40F, FortiGate 4200F, FortiGate 4201F Gen2,
FortiGate 4400F, FortiGate 4401F Gen2, FortiGate 4800F, FortiGate 4801F, FortiGate 50G 5G,
FortiGate 50G DSL, FortiGate 50G SFP-POE, FortiGate 50G SFP, FortiGate 50G, FortiGate 51G 5G,
FortiGate 51G SFP-POE, FortiGate 51G, FortiGate 600F, FortiGate 601F, FortiGate 60F, FortiGate 61F,
FortiGate 70F, FortiGate 70G-POE, FortiGate 70G, FortiGate 71F, FortiGate 71G-POE, FortiGate 71G,
FortiGate 80F Bypass, FortiGate 80F DSL, FortiGate 80F Gen2, FortiGate 80F-POE, FortiGate 81F
Gen2, FortiGate 81F-POE, FortiGate 900G, FortiGate 901G, FortiGate 90G Gen2, FortiGate 90G,
FortiGate 91G Gen2, FortiGate 91G, FortiGate-VM64 Aliyun, FortiGate-VM64 AWS, FortiGate-VM64
Azure, FortiGate-VM64 GCP, FortiGate-VM64 OPC, FortiGate-VM64, FortiGateRugged 50G 5G,
FortiGateRugged 60F 3G4G, FortiGateRugged 60F Gen2, FortiGateRugged 70F 3G4G,
FortiGateRugged 70F, FortiGateRugged 70G 5G Dual, FortiGateRugged 70G, FortiWiFi 30G, FortiWiFi
31G, FortiWiFi 40F 3G4G, FortiWiFi 40F, FortiWiFi 50G 5G, FortiWiFi 50G DSL, FortiWiFi 50G SFP,
FortiWiFi 50G, FortiWiFi 51G, FortiWiFi 60F, FortiWiFi 61F, FortiWiFi 70G-POE, FortiWiFi 70G,
FortiWiFi 71G, FortiWiFi 80F 2R 3G4G DSL, FortiWiFi 80F 2R, FortiWiFi 81F 2R 3G4G DSL, FortiWiFi
81F 2R 3G4G-POE, FortiWiFi 81F 2R-POE, FortiWiFi 81F 2R.
Configure NP6 IPsec engine status monitoring.
config monitoring np6-ipsec-engine
Description: Configure NP6 IPsec engine status monitoring.
set interval {integer}
set status [enable|disable]
set threshold {user}
end
FortiOS 8.0.0 CLI Reference
1095
Fortinet Inc.

<!-- 来源页 1096 -->
config monitoring np6-ipsec-engine
Parameter
Description
Type
Size
Default
interval
IPsec engine status check interval (1 - 60 seconds,
default = 1).
integer
Minimum
value: 1
Maximum
value: 60
1
status
Enable/disable NP6 IPsec engine status
monitoring.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
threshold
IPsec engine status check threshold (x x x x x x x x,
8 integers from <1> to <255>, default = 15 15 12 12
8 8 5 5). Example: Log is generated if IPsec engine
0 is busy each of every 15 consecutive interval
checks.
user
Not
Specified
FortiOS 8.0.0 CLI Reference
1096
Fortinet Inc.

<!-- 来源页 1097 -->
config monitoring npu-hpe
This command is available for model(s): FortiGate 1000D, FortiGate 1000F, FortiGate 1001F,
FortiGate 100F, FortiGate 101F Gen2, FortiGate 1100E, FortiGate 1101E, FortiGate 1800F, FortiGate
1801F, FortiGate 2000E, FortiGate 200F, FortiGate 201F, FortiGate 2200E, FortiGate 2201E,
FortiGate 2500E, FortiGate 2600F, FortiGate 2601F, FortiGate 3000F, FortiGate 3001F, FortiGate
300E, FortiGate 301E, FortiGate 30G, FortiGate 31G, FortiGate 3200F, FortiGate 3201F Gen2,
FortiGate 3300E, FortiGate 3301E, FortiGate 3400E, FortiGate 3401E, FortiGate 3500F Gen2,
FortiGate 3501F Gen2, FortiGate 3600E, FortiGate 3601E, FortiGate 3700F, FortiGate 3701F,
FortiGate 3960E, FortiGate 3980E, FortiGate 400E Bypass, FortiGate 400E, FortiGate 400F,
FortiGate 401E, FortiGate 401F, FortiGate 40F 3G4G, FortiGate 40F, FortiGate 4200F, FortiGate
4201F Gen2, FortiGate 4400F, FortiGate 4401F Gen2, FortiGate 4800F, FortiGate 4801F, FortiGate
500E, FortiGate 501E, FortiGate 600E, FortiGate 600F, FortiGate 601E, FortiGate 601F, FortiGate
60F, FortiGate 61F, FortiGate 70F, FortiGate 71F, FortiGate 800D, FortiGate 80F Bypass, FortiGate
80F DSL, FortiGate 80F Gen2, FortiGate 80F-POE, FortiGate 81F Gen2, FortiGate 81F-POE, FortiGate
900D, FortiGate 900G, FortiGate 901G, FortiGateRugged 60F 3G4G, FortiGateRugged 60F Gen2,
FortiGateRugged 70F 3G4G, FortiGateRugged 70F, FortiWiFi 30G, FortiWiFi 31G, FortiWiFi 40F
3G4G, FortiWiFi 40F, FortiWiFi 60F, FortiWiFi 61F, FortiWiFi 80F 2R 3G4G DSL, FortiWiFi 80F 2R,
FortiWiFi 81F 2R 3G4G DSL, FortiWiFi 81F 2R 3G4G-POE, FortiWiFi 81F 2R-POE, FortiWiFi 81F 2R.
It is not available for: FortiGate 120G, FortiGate 121G, FortiGate 200E, FortiGate 200G, FortiGate
201E, FortiGate 201G, FortiGate 50G 5G, FortiGate 50G DSL, FortiGate 50G SFP-POE, FortiGate 50G
SFP, FortiGate 50G, FortiGate 51G 5G, FortiGate 51G SFP-POE, FortiGate 51G, FortiGate 70G-POE,
FortiGate 70G, FortiGate 71G-POE, FortiGate 71G, FortiGate 90G Gen2, FortiGate 90G, FortiGate 91G
Gen2, FortiGate 91G, FortiGate-VM64 Aliyun, FortiGate-VM64 AWS, FortiGate-VM64 Azure,
FortiGate-VM64 GCP, FortiGate-VM64 OPC, FortiGate-VM64, FortiGateRugged 50G 5G,
FortiGateRugged 70G 5G Dual, FortiGateRugged 70G, FortiWiFi 50G 5G, FortiWiFi 50G DSL, FortiWiFi
50G SFP, FortiWiFi 50G, FortiWiFi 51G, FortiWiFi 70G-POE, FortiWiFi 70G, FortiWiFi 71G.
Configure npu-hpe status monitoring.
config monitoring npu-hpe
Description: Configure npu-hpe status monitoring.
set interval {integer}
set multipliers {user}
set status [enable|disable]
end
config monitoring npu-hpe
Parameter
Description
Type
Size
Default
interval
HPE status check interval (1 - 60 seconds, default
= 1 second).
integer
Minimum
value: 1
Maximum
value: 60
1
FortiOS 8.0.0 CLI Reference
1097
Fortinet Inc.

<!-- 来源页 1098 -->
Parameter
Description
Type
Size
Default
multipliers
HPE type interval multipliers (12 integers from <1>
to <255>, default = 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8).
An event log is generated after every (interval *
multiplier)seconds as configured for any HPE type
when drops occur for that HPE type. An attack log
is generated after every (4 * multiplier) number of
continuous event logs.
user
Not
Specified
status
Enable/disable HPE status monitoring.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
1098
Fortinet Inc.

---


<!-- 来源页 1103 -->
report
This section includes syntax for the following commands:
l config report layout on page 1103
l config report setting on page 1112
config report layout
This command is available for model(s): FortiGate 1000D, FortiGate 1001F, FortiGate 101F Gen2,
FortiGate 1101E, FortiGate 121G, FortiGate 1801F, FortiGate 2000E, FortiGate 201E, FortiGate 201F,
FortiGate 201G, FortiGate 2201E, FortiGate 2500E, FortiGate 2600F, FortiGate 2601F, FortiGate
3001F, FortiGate 301E, FortiGate 31G, FortiGate 3201F Gen2, FortiGate 3301E, FortiGate 3401E,
FortiGate 3501F Gen2, FortiGate 3601E, FortiGate 3701F, FortiGate 401E, FortiGate 401F, FortiGate
4201F Gen2, FortiGate 4401F Gen2, FortiGate 4801F, FortiGate 501E, FortiGate 50G 5G, FortiGate
50G DSL, FortiGate 50G SFP-POE, FortiGate 50G SFP, FortiGate 50G, FortiGate 51G 5G, FortiGate
51G SFP-POE, FortiGate 51G, FortiGate 601E, FortiGate 601F, FortiGate 61F, FortiGate 71F, FortiGate
71G-POE, FortiGate 71G, FortiGate 800D, FortiGate 81F Gen2, FortiGate 81F-POE, FortiGate 900D,
FortiGate 901G, FortiGate 91G Gen2, FortiGate 91G, FortiGate-VM64 Aliyun, FortiGate-VM64 AWS,
FortiGate-VM64 Azure, FortiGate-VM64 GCP, FortiGate-VM64 OPC, FortiGate-VM64,
FortiGateRugged 70F 3G4G, FortiGateRugged 70F, FortiGateRugged 70G 5G Dual, FortiGateRugged
70G, FortiWiFi 31G, FortiWiFi 50G 5G, FortiWiFi 50G DSL, FortiWiFi 50G SFP, FortiWiFi 50G, FortiWiFi
51G, FortiWiFi 61F, FortiWiFi 71G, FortiWiFi 81F 2R 3G4G DSL, FortiWiFi 81F 2R 3G4G-POE, FortiWiFi
81F 2R-POE, FortiWiFi 81F 2R.
It is not available for: FortiGate 1000F, FortiGate 100F, FortiGate 1100E, FortiGate 120G, FortiGate
1800F, FortiGate 200E, FortiGate 200F, FortiGate 200G, FortiGate 2200E, FortiGate 3000F,
FortiGate 300E, FortiGate 30G, FortiGate 3200F, FortiGate 3300E, FortiGate 3400E, FortiGate
3500F Gen2, FortiGate 3600E, FortiGate 3700F, FortiGate 3960E, FortiGate 3980E, FortiGate 400E
Bypass, FortiGate 400E, FortiGate 400F, FortiGate 40F 3G4G, FortiGate 40F, FortiGate 4200F,
FortiGate 4400F, FortiGate 4800F, FortiGate 500E, FortiGate 600E, FortiGate 600F, FortiGate 60F,
FortiGate 70F, FortiGate 70G-POE, FortiGate 70G, FortiGate 80F Bypass, FortiGate 80F DSL,
FortiGate 80F Gen2, FortiGate 80F-POE, FortiGate 900G, FortiGate 90G Gen2, FortiGate 90G,
FortiGateRugged 50G 5G, FortiGateRugged 60F 3G4G, FortiGateRugged 60F Gen2, FortiWiFi 30G,
FortiWiFi 40F 3G4G, FortiWiFi 40F, FortiWiFi 60F, FortiWiFi 70G-POE, FortiWiFi 70G, FortiWiFi 80F 2R
3G4G DSL, FortiWiFi 80F 2R.
Report layout configuration.
config report layout
Description: Report layout configuration.
edit <name>
config body-item
Description: Configure report body item.
FortiOS 8.0.0 CLI Reference
1103
Fortinet Inc.

<!-- 来源页 1104 -->
edit <id>
set chart {string}
set chart-options {option1}, {option2}, ...
set content {string}
set description {string}
set img-src {string}
set misc-component [hline|page-break|...]
config parameters
Description: Parameters.
edit <id>
set name {string}
set value {string}
next
end
set style {string}
set text-component [text|heading1|...]
set title {string}
set top-n {integer}
set type [text|image|...]
next
end
set cutoff-option [run-time|custom]
set cutoff-time {user}
set day [sunday|monday|...]
set description {string}
set email-recipients {string}
set email-send [enable|disable]
set format {option1}, {option2}, ...
set max-pdf-report {integer}
set options {option1}, {option2}, ...
config page
Description: Configure report page.
set column-break-before {option1}, {option2}, ...
config footer
Description: Configure report page footer.
config footer-item
Description: Configure report footer item.
edit <id>
set content {string}
set description {string}
set img-src {string}
set style {string}
set type [text|image]
next
end
set style {string}
end
config header
Description: Configure report page header.
config header-item
Description: Configure report header item.
edit <id>
FortiOS 8.0.0 CLI Reference
1104
Fortinet Inc.

<!-- 来源页 1105 -->
set content {string}
set description {string}
set img-src {string}
set style {string}
set type [text|image]
next
end
set style {string}
end
set options {option1}, {option2}, ...
set page-break-before {option1}, {option2}, ...
set paper [a4|letter]
end
set schedule-type [demand|daily|...]
set style-theme {string}
set subtitle {string}
set time {user}
set title {string}
next
end
config report layout
Parameter
Description
Type
Size
Default
cutoff-option
Cutoff-option is either run-time or custom.
option
-run-time
Option
Description
run-time
Run time.
custom
Custom.
cutoff-time
Custom cutoff time to generate report (format =
hh:mm).
user
Not
Specified
day
Schedule days of week to generate report.
option
-sunday
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
FortiOS 8.0.0 CLI Reference
1105
Fortinet Inc.

<!-- 来源页 1106 -->
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
email-recipients
Email recipients for generated reports.
string
Maximum
length: 511
email-send
Enable/disable sending emails after reports are
generated.
option
-disable
Option
Description
enable
Enable sending emails after generating reports.
disable
Disable sending emails after generating reports.
format
Report format.
option
-pdf
Option
Description
pdf
PDF.
max-pdf-report
Maximum number of PDF reports to keep at one
time (oldest report is overwritten).
integer
Minimum
value: 1
Maximum
value: 365
31
name
Report layout name.
string
Maximum
length: 35
options
Report layout options.
option
-include-table-of-content auto-numbering-heading
view-chart-as-heading
Option
Description
include-table-of-content
Include table of content in the report.
auto-numbering-heading
Prepend heading with auto numbering.
view-chart-as-heading
Auto add heading for each chart.
FortiOS 8.0.0 CLI Reference
1106
Fortinet Inc.

<!-- 来源页 1107 -->
Parameter
Description
Type
Size
Default
Option
Description
show-html-navbar-before-heading
Show HTML navigation bar before each heading.
dummy-option
Use this option if you need none of the above options.
schedule-type
Report schedule type.
option
-daily
Option
Description
demand
Run on demand.
daily
Schedule daily.
weekly
Schedule weekly.
style-theme
Report style theme.
string
Maximum
length: 35
subtitle
Report subtitle.
string
Maximum
length: 127
time
Schedule time to generate report (format =
hh:mm).
user
Not
Specified
title
Report title.
string
Maximum
length: 127
config body-item
Parameter
Description
Type
Size
Default
chart
Report item chart name.
string
Maximum
length: 71
chart-options
Report chart options.
option
-include-no-data
hide-title
show-caption
Option
Description
include-no-data
Include chart with no data.
hide-title
Hide chart title.
show-caption
Show chart caption.
FortiOS 8.0.0 CLI Reference
1107
Fortinet Inc.

<!-- 来源页 1108 -->
Parameter
Description
Type
Size
Default
content
Report item text content.
string
Maximum
length: 511
description
Description.
string
Maximum
length: 63
id
Report item ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
img-src
Report item image file name.
string
Maximum
length: 127
misc-component
Report item miscellaneous component.
option
-hline
Option
Description
hline
Horizontal line.
page-break
Page break.
column-break
Column break.
section-start
Section start.
style
Report item style.
string
Maximum
length: 71
text-component
Report item text component.
option
-text
Option
Description
text
Normal text.
heading1
Heading 1.
heading2
Heading 2.
heading3
Heading 3.
title
Report section title.
string
Maximum
length: 511
top-n
Value of top.
integer
Minimum value:
0 Maximum
value:
4294967295
0
type
Report item type.
option
-text
FortiOS 8.0.0 CLI Reference
1108
Fortinet Inc.

<!-- 来源页 1109 -->
Parameter
Description
Type
Size
Default
Option
Description
text
Text.
image
Image.
chart
Chart.
misc
Miscellaneous.
config parameters
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
name
Field name that match field of parameters
defined in dataset.
string
Maximum
length: 127
value
Value to replace corresponding field of
parameters defined in dataset.
string
Maximum
length: 1023
config page
Parameter
Description
Type
Size
Default
column-break-before
Report page auto column break before heading.
option
-Option
Description
heading1
Column break before heading 1.
heading2
Column break before heading 2.
heading3
Column break before heading 3.
options
Report page options.
option
-Option
Description
header-on-first-page
Show header on first page.
footer-on-first-page
Show footer on first page.
FortiOS 8.0.0 CLI Reference
1109
Fortinet Inc.

<!-- 来源页 1110 -->
Parameter
Description
Type
Size
Default
page-break-before
Report page auto page break before heading.
option
-Option
Description
heading1
Page break before heading 1.
heading2
Page break before heading 2.
heading3
Page break before heading 3.
paper
Report page paper.
option
-a4
Option
Description
a4
A4 paper.
letter
Letter paper.
config footer
Parameter
Description
Type
Size
Default
style
Report footer style.
string
Maximum length:
71
config footer-item
Parameter
Description
Type
Size
Default
content
Report item text content.
string
Maximum
length: 511
description
Description.
string
Maximum
length: 63
id
Report item ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
img-src
Report item image file name.
string
Maximum
length: 127
style
Report item style.
string
Maximum
length: 71
type
Report item type.
option
-text
FortiOS 8.0.0 CLI Reference
1110
Fortinet Inc.

<!-- 来源页 1111 -->
Parameter
Description
Type
Size
Default
Option
Description
text
Text.
image
Image.
config header
Parameter
Description
Type
Size
Default
style
Report header style.
string
Maximum
length: 71
config header-item
Parameter
Description
Type
Size
Default
content
Report item text content.
string
Maximum
length: 511
description
Description.
string
Maximum
length: 63
id
Report item ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
img-src
Report item image file name.
string
Maximum
length: 127
style
Report item style.
string
Maximum
length: 71
type
Report item type.
option
-text
Option
Description
text
Text.
image
Image.
FortiOS 8.0.0 CLI Reference
1111
Fortinet Inc.

<!-- 来源页 1112 -->
config report setting
This command is available for model(s): FortiGate 1000D, FortiGate 1001F, FortiGate 101F Gen2,
FortiGate 1101E, FortiGate 121G, FortiGate 1801F, FortiGate 2000E, FortiGate 201E, FortiGate 201F,
FortiGate 201G, FortiGate 2201E, FortiGate 2500E, FortiGate 2600F, FortiGate 2601F, FortiGate
3001F, FortiGate 301E, FortiGate 31G, FortiGate 3201F Gen2, FortiGate 3301E, FortiGate 3401E,
FortiGate 3501F Gen2, FortiGate 3601E, FortiGate 3701F, FortiGate 401E, FortiGate 401F, FortiGate
4201F Gen2, FortiGate 4401F Gen2, FortiGate 4801F, FortiGate 501E, FortiGate 50G 5G, FortiGate
50G DSL, FortiGate 50G SFP-POE, FortiGate 50G SFP, FortiGate 50G, FortiGate 51G 5G, FortiGate
51G SFP-POE, FortiGate 51G, FortiGate 601E, FortiGate 601F, FortiGate 61F, FortiGate 71F, FortiGate
71G-POE, FortiGate 71G, FortiGate 800D, FortiGate 81F Gen2, FortiGate 81F-POE, FortiGate 900D,
FortiGate 901G, FortiGate 91G Gen2, FortiGate 91G, FortiGate-VM64 Aliyun, FortiGate-VM64 AWS,
FortiGate-VM64 Azure, FortiGate-VM64 GCP, FortiGate-VM64 OPC, FortiGate-VM64,
FortiGateRugged 70F 3G4G, FortiGateRugged 70F, FortiGateRugged 70G 5G Dual, FortiGateRugged
70G, FortiWiFi 31G, FortiWiFi 50G 5G, FortiWiFi 50G DSL, FortiWiFi 50G SFP, FortiWiFi 50G, FortiWiFi
51G, FortiWiFi 61F, FortiWiFi 71G, FortiWiFi 81F 2R 3G4G DSL, FortiWiFi 81F 2R 3G4G-POE, FortiWiFi
81F 2R-POE, FortiWiFi 81F 2R.
It is not available for: FortiGate 1000F, FortiGate 100F, FortiGate 1100E, FortiGate 120G, FortiGate
1800F, FortiGate 200E, FortiGate 200F, FortiGate 200G, FortiGate 2200E, FortiGate 3000F,
FortiGate 300E, FortiGate 30G, FortiGate 3200F, FortiGate 3300E, FortiGate 3400E, FortiGate
3500F Gen2, FortiGate 3600E, FortiGate 3700F, FortiGate 3960E, FortiGate 3980E, FortiGate 400E
Bypass, FortiGate 400E, FortiGate 400F, FortiGate 40F 3G4G, FortiGate 40F, FortiGate 4200F,
FortiGate 4400F, FortiGate 4800F, FortiGate 500E, FortiGate 600E, FortiGate 600F, FortiGate 60F,
FortiGate 70F, FortiGate 70G-POE, FortiGate 70G, FortiGate 80F Bypass, FortiGate 80F DSL,
FortiGate 80F Gen2, FortiGate 80F-POE, FortiGate 900G, FortiGate 90G Gen2, FortiGate 90G,
FortiGateRugged 50G 5G, FortiGateRugged 60F 3G4G, FortiGateRugged 60F Gen2, FortiWiFi 30G,
FortiWiFi 40F 3G4G, FortiWiFi 40F, FortiWiFi 60F, FortiWiFi 70G-POE, FortiWiFi 70G, FortiWiFi 80F 2R
3G4G DSL, FortiWiFi 80F 2R.
Report setting configuration.
config report setting
Description: Report setting configuration.
set fortiview [enable|disable]
set pdf-report [enable|disable]
set report-source {option1}, {option2}, ...
set top-n {integer}
set web-browsing-threshold {integer}
end
config report setting
Parameter
Description
Type
Size
Default
fortiview
Enable/disable historical FortiView.
option
-enable **
FortiOS 8.0.0 CLI Reference
1112
Fortinet Inc.

<!-- 来源页 1113 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable historical FortiView.
disable
Disable historical FortiView.
pdf-report
Enable/disable PDF report.
option
-enable **
Option
Description
enable
Enable PDF report.
disable
Disable PDF report.
report-source
Report log source.
option
-forward-traffic
Option
Description
forward-traffic
Report includes forward traffic logs.
sniffer-traffic
Report includes sniffer traffic logs.
local-deny-traffic
Report includes local deny traffic logs.
top-n
Number of items to populate (1000 - 20000).
integer
Minimum
value: 1000
Maximum
value:
20000
1000
web-browsing-threshold
Web browsing time calculation threshold (3 - 15
min).
integer
Minimum
value: 3
Maximum
value: 15
3
** Values may differ between models.
FortiOS 8.0.0 CLI Reference
1113
Fortinet Inc.
