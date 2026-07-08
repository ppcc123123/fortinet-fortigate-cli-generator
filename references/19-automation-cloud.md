# 自动化 / 云集成 / WAN优化 / 其他

> 来源: FortiOS-8.0.0-CLI_Reference.pdf
> 覆盖命令/章节: automation, aws, azure, nsxt, telemetry-controller, wanopt, endpoint-control, icap, llm, dpdk
> 本文件由 extract_pdf.py 从官方 PDF 自动提取，请勿手动编辑；
> 如需修正请修改 map.json 后重跑脚本。

---


<!-- 来源页 216 -->
automation
This section includes syntax for the following commands:
l config automation setting on page 216
config automation setting
Automation setting configuration.
config automation setting
Description: Automation setting configuration.
set fabric-sync [enable|disable]
set max-concurrent-stitches {integer}
set secure-mode [enable|disable]
end
config automation setting
Parameter
Description
Type
Size
Default
fabric-sync
Enable/disable synchronization of automation
settings with security fabric.
option
-enable
Option
Description
enable
Synchronize automation setting with security fabric.
disable
Do not synchronize automation setting with security fabric.
max-concurrent-stitches
Maximum number of automation stitches that are
allowed to run concurrently.
integer
Minimum
value: 32
Maximum
value: 1024
**
512 **
secure-mode
Enable/disable secure running mode for
automation.
option
-disable
Option
Description
enable
Enable secure running mode for automation.
disable
Disable secure running mode for automation.
** Values may differ between models.
FortiOS 8.0.0 CLI Reference
216
Fortinet Inc.

---


<!-- 来源页 217 -->
aws
This section includes syntax for the following commands:
l config aws vpce on page 217
config aws vpce
This command is available for model(s): FortiGate-VM64 AWS.
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
91G, FortiGate-VM64 Aliyun, FortiGate-VM64 Azure, FortiGate-VM64 GCP, FortiGate-VM64 OPC,
FortiGate-VM64, FortiGateRugged 50G 5G, FortiGateRugged 60F 3G4G, FortiGateRugged 60F
Gen2, FortiGateRugged 70F 3G4G, FortiGateRugged 70F, FortiGateRugged 70G 5G Dual,
FortiGateRugged 70G, FortiWiFi 30G, FortiWiFi 31G, FortiWiFi 40F 3G4G, FortiWiFi 40F, FortiWiFi
50G 5G, FortiWiFi 50G DSL, FortiWiFi 50G SFP, FortiWiFi 50G, FortiWiFi 51G, FortiWiFi 60F, FortiWiFi
61F, FortiWiFi 70G-POE, FortiWiFi 70G, FortiWiFi 71G, FortiWiFi 80F 2R 3G4G DSL, FortiWiFi 80F 2R,
FortiWiFi 81F 2R 3G4G DSL, FortiWiFi 81F 2R 3G4G-POE, FortiWiFi 81F 2R-POE, FortiWiFi 81F 2R.
Configure AWS VPC configuration.
config aws vpce
Description: Configure AWS VPC configuration.
edit <id>
set endpoint-id {string}
set name {string}
set vdom {string}
FortiOS 8.0.0 CLI Reference
217
Fortinet Inc.

<!-- 来源页 218 -->
next
end
config aws vpce
Parameter
Description
Type
Size
Default
endpoint-id
VPC endpoint ID.
string
Maximum
length: 32
id
Entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
name
VPC endpoint name.
string
Maximum
length: 63
vdom
VDOM name.
string
Maximum
length: 31
FortiOS 8.0.0 CLI Reference
218
Fortinet Inc.

---


<!-- 来源页 219 -->
azure
This section includes syntax for the following commands:
l config azure migration on page 219
l config azure nva on page 220
l config azure vwan-ingress-public-IPs on page 221
l config azure vwan-slb on page 222
config azure migration
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
Azure post live migration process.
config azure migration
Description: Azure post live migration process.
set auto-reboot [enable|disable]
end
FortiOS 8.0.0 CLI Reference
219
Fortinet Inc.

<!-- 来源页 220 -->
config azure migration
Parameter
Description
Type
Size
Default
auto-reboot
Enable/disable automatic reboot after a live
migration finishes
option
-disable
Option
Description
enable
Enable automatic reboot after live migration
disable
Disable automatic reboot after live migration
config azure nva
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
Azure vWAN NVA info from cloudinit.
config azure nva
Description: Azure vWAN NVA info from cloudinit.
end
FortiOS 8.0.0 CLI Reference
220
Fortinet Inc.

<!-- 来源页 221 -->
config azure vwan-ingress-public-IPs
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
Display Azure vWAN SLB ingress public IPs.
config azure vwan-ingress-public-IPs
Description: Display Azure vWAN SLB ingress public IPs.
edit <name>
set ip {string}
next
end
config azure vwan-ingress-public-IPs
Parameter
Description
Type
Size
Default
ip
Public IP address.
string
Maximum length: 15
name
Name of public IP.
string
Maximum length:
127
FortiOS 8.0.0 CLI Reference
221
Fortinet Inc.

<!-- 来源页 222 -->
config azure vwan-slb
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
Configure Azure vWAN slb setting.
config azure vwan-slb
Description: Configure Azure vWAN slb setting.
set mode [passive|active]
config permanent-security-rules
Description: Configure permanent security rules.
config rules
Description: Configure security rules.
edit <name>
set applies-on {string}
set destination-port-ranges {string}
set protocol [TCP|UDP]
set source-address-prefix {string}
next
end
set status [disable|enable|...]
set version {integer}
end
config temporary-security-rules
Description: Configure temporary security rules.
FortiOS 8.0.0 CLI Reference
222
Fortinet Inc.

<!-- 来源页 223 -->
set expiration-time {string}
config rules
Description: Configure security rules.
edit <name>
set destination-port-ranges {string}
set protocol [TCP|UDP]
set source-address-prefix {string}
next
end
set status [disable|enable|...]
end
end
config azure vwan-slb
Parameter
Description
Type
Size
Default
mode
Mode of VWAN SLB setting.
option
-passive
Option
Description
passive
VWAN SLB setting is passive.
active
VWAN SLB setting is active for pushing to online.
config permanent-security-rules
Parameter
Description
Type
Size
Default
status
Status of SLB inbound security rules setting
(read-only).
option
-disable
Option
Description
disable
SLB inbound security rule is disabled.
enable
SLB inbound security rule is enabled.
updating
SLB inbound security rule is updating.
pending
SLB inbound security rule is pending.
version
Version of SLB setting (read-only).
integer
Minimum value:
0 Maximum
value:
4294967295
0
FortiOS 8.0.0 CLI Reference
223
Fortinet Inc.

<!-- 来源页 224 -->
config rules
Parameter
Description
Type
Size
Default
applies-on
Applies on target.
string
Maximum
length: 255
destination-port-ranges
Destination port ranges.
string
Maximum
length: 127
name
Name of security rule.
string
Maximum
length: 63
protocol
Protocol.
option
-TCP
Option
Description
TCP
TCP protocol.
UDP
UDP protocol.
source-address-prefix
Source address ranges.
string
Maximum
length: 63
config temporary-security-rules
Parameter
Description
Type
Size
Default
expiration-time
Expiration time (read-only).
string
Maximum
length: 31
status
Status of SLB inbound security rules setting (read-only).
option
-disable
Option
Description
disable
SLB inbound security rule is disabled.
enable
SLB inbound security rule is enabled.
updating
SLB inbound security rule is updating.
pending
SLB inbound security rule is pending.
config rules
Parameter
Description
Type
Size
Default
destination-port-ranges
Destination port ranges.
string
Maximum
length: 127
FortiOS 8.0.0 CLI Reference
224
Fortinet Inc.

<!-- 来源页 225 -->
Parameter
Description
Type
Size
Default
name
Name of security rule.
string
Maximum
length: 63
protocol
Protocol.
option
-TCP
Option
Description
TCP
TCP protocol.
UDP
UDP protocol.
source-address-prefix
Source address ranges.
string
Maximum
length: 63
FortiOS 8.0.0 CLI Reference
225
Fortinet Inc.

---


<!-- 来源页 304 -->
dpdk
This section includes syntax for the following commands:
l config dpdk cpus on page 304
l config dpdk global on page 306
config dpdk cpus
This command is available for model(s): FortiGate-VM64 AWS, FortiGate-VM64 Azure, FortiGate-VM64 GCP, FortiGate-VM64 OPC, FortiGate-VM64.
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
91G, FortiGate-VM64 Aliyun, FortiGateRugged 50G 5G, FortiGateRugged 60F 3G4G,
FortiGateRugged 60F Gen2, FortiGateRugged 70F 3G4G, FortiGateRugged 70F, FortiGateRugged
70G 5G Dual, FortiGateRugged 70G, FortiWiFi 30G, FortiWiFi 31G, FortiWiFi 40F 3G4G, FortiWiFi 40F,
FortiWiFi 50G 5G, FortiWiFi 50G DSL, FortiWiFi 50G SFP, FortiWiFi 50G, FortiWiFi 51G, FortiWiFi 60F,
FortiWiFi 61F, FortiWiFi 70G-POE, FortiWiFi 70G, FortiWiFi 71G, FortiWiFi 80F 2R 3G4G DSL, FortiWiFi
80F 2R, FortiWiFi 81F 2R 3G4G DSL, FortiWiFi 81F 2R 3G4G-POE, FortiWiFi 81F 2R-POE, FortiWiFi 81F
2R.
Configure CPUs enabled to run engines in each DPDK stage.
config dpdk cpus
Description: Configure CPUs enabled to run engines in each DPDK stage.
set ips-cpus {string}
set isolated-cpus {string}
set rx-cpus {string}
FortiOS 8.0.0 CLI Reference
304
Fortinet Inc.

<!-- 来源页 305 -->
set tx-cpus {string}
set vnp-cpus {string}
set vnpsp-cpus {string}
end
config dpdk cpus
Parameter
Description
Type
Size
Default
ips-cpus
CPUs enabled to run DPDK IPS engines.
string
Maximum
length:
1022
all
isolated-cpus
CPUs isolated to run only the DPDK engines with
the exception of processes that have affinity
explicitly set by either a user configuration or by
their implementation.
string
Maximum
length:
1022
none
rx-cpus
CPUs enabled to run DPDK RX engines.
string
Maximum
length:
1022
all
tx-cpus
CPUs enabled to run DPDK TX engines.
string
Maximum
length:
1022
all
vnp-cpus
CPUs enabled to run DPDK VNP engines.
string
Maximum
length:
1022
all
vnpsp-cpus
CPUs enabled to run DPDK VNP slow path.
string
Maximum
length:
1022
all
FortiOS 8.0.0 CLI Reference
305
Fortinet Inc.

<!-- 来源页 306 -->
config dpdk global
This command is available for model(s): FortiGate-VM64 AWS, FortiGate-VM64 Azure, FortiGate-VM64 GCP, FortiGate-VM64 OPC, FortiGate-VM64.
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
91G, FortiGate-VM64 Aliyun, FortiGateRugged 50G 5G, FortiGateRugged 60F 3G4G,
FortiGateRugged 60F Gen2, FortiGateRugged 70F 3G4G, FortiGateRugged 70F, FortiGateRugged
70G 5G Dual, FortiGateRugged 70G, FortiWiFi 30G, FortiWiFi 31G, FortiWiFi 40F 3G4G, FortiWiFi 40F,
FortiWiFi 50G 5G, FortiWiFi 50G DSL, FortiWiFi 50G SFP, FortiWiFi 50G, FortiWiFi 51G, FortiWiFi 60F,
FortiWiFi 61F, FortiWiFi 70G-POE, FortiWiFi 70G, FortiWiFi 71G, FortiWiFi 80F 2R 3G4G DSL, FortiWiFi
80F 2R, FortiWiFi 81F 2R 3G4G DSL, FortiWiFi 81F 2R 3G4G-POE, FortiWiFi 81F 2R-POE, FortiWiFi 81F
2R.
Configure global DPDK options.
config dpdk global
Description: Configure global DPDK options.
set elasticbuffer [disable|enable]
set frag-offload [disable|enable]
set hugepage-percentage {integer}
set interface <interface-name1>, <interface-name2>, ...
set ipsec-offload [disable|enable]
set multiqueue [disable|enable]
set per-session-accounting [disable|traffic-log-only|...]
set protects {string}
set session-table-percentage {integer}
set sleep-on-idle [disable|enable]
set status [disable|enable]
end
FortiOS 8.0.0 CLI Reference
306
Fortinet Inc.

<!-- 来源页 307 -->
config dpdk global
Parameter
Description
Type
Size
Default
elasticbuffer
Enable/disable elasticbuffer support for all
DPDK ports.
option
-disable
Option
Description
disable
Disable elasticbuffer support for DPDK ports.
enable
Enable elasticbuffer support for DPDK ports.
frag-offload
Enable/disable DPDK
fragmentation/defragmentation offloading
(default = enable).
option
-enable
Option
Description
disable
Disable DPDK fragmentation/defragmentation offloading.
enable
Enable DPDK fragmentation/defragmentation offloading.
hugepage-percentage
Percentage of main memory allocated to
hugepages, which are available for DPDK
operation.
integer
Minimum
value: 15
Maximum
value: 50
30
interface
<interface-name>
Physical interfaces that enable DPDK. (Only
AWS Elastic Network Adapter (ENA) is
supported.)
Physical interface name. (Only AWS Elastic
Network Adapter (ENA) is supported.)
string
Maximum
length: 31
ipsec-offload
Enable/disable DPDK IPsec phase 2
offloading.
option
-disable
Option
Description
disable
Disable DPDK IPsec phase 2 offloading.
enable
Enable DPDK IPsec phase 2 offloading.
multiqueue
Enable/disable multi-queue RX/TX support for
all DPDK ports.
option
-disable
Option
Description
disable
Disable multi-queue RX/TX support for DPDK ports.
enable
Enable multi-queue RX/TX support for DPDK ports.
per-session-accounting
Enable/disable per-session accounting.
option
-traffic-log-only
FortiOS 8.0.0 CLI Reference
307
Fortinet Inc.

<!-- 来源页 308 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable per-session accounting.
traffic-log-only
Enable per-session accounting only for VNP sessions with traffic
logging turned on in firewall policy.
enable
Enable per-session accounting for all VNP sessions. *Affect
performance.
protects
Special arguments for device
string
Maximum
length: 2047
session-table-percentage
Percentage of main memory allocated to
DPDK session table.
integer
Minimum
value: 0
Maximum
value: 60
5
sleep-on-idle
Enable/disable sleep-on-idle support for all
FDH engines.
option
-disable
Option
Description
disable
Disable sleep-on-idle support for FDH engines.
enable
Enable sleep-on-idle support for FDH engines.
status
Enable/disable DPDK operation for the entire
system.
option
-disable
Option
Description
disable
Disable DPDK operation.
enable
Enable DPDK operation. *The minimum system requirements for DPDK
is 2 vCPUs and 4GB memory.
FortiOS 8.0.0 CLI Reference
308
Fortinet Inc.

---


<!-- 来源页 332 -->
endpoint-control
This section includes syntax for the following commands:
l config endpoint-control fctems-override on page 336
l config endpoint-control fctems on page 332
l config endpoint-control settings on page 341
config endpoint-control fctems
Configure FortiClient Enterprise Management Server (EMS) entries.
config endpoint-control fctems
Description: Configure FortiClient Enterprise Management Server (EMS) entries.
edit <ems-id>
set call-timeout {integer}
set capabilities {option1}, {option2}, ...
set cloud-authentication-access-key {password}
set dirty-reason [none|mismatched-ems-sn]
set fortinetone-cloud-authentication [enable|disable]
set https-port {integer}
set interface {string}
set interface-select-method [auto|sdwan|...]
set name {string}
set out-of-sync-threshold {integer}
set pull-malware-hash [enable|disable]
set pull-sysinfo [enable|disable]
set pull-tags [enable|disable]
set pull-vulnerabilities [enable|disable]
set send-tags-to-all-vdoms [enable|disable]
set serial-number {string}
set server {string}
set source-ip {ipv4-address-any}
set status [enable|disable]
set tenant-id {string}
set trust-ca-cn [enable|disable]
set verifying-ca {string}
set websocket-override [enable|disable]
next
end
FortiOS 8.0.0 CLI Reference
332
Fortinet Inc.

<!-- 来源页 333 -->
config endpoint-control fctems
Parameter
Description
Type
Size
Default
call-timeout
FortiClient EMS call timeout in seconds (1 - 180
seconds, default = 30).
integer
Minimum
value: 1
Maximum
value: 180
30
capabilities
List of EMS capabilities.
option
-Option
Description
fabric-auth
Allow this FortiGate unit to load the authentication page provided by
EMS to authenticate itself with EMS.
silent-approval
Allow silent approval of non-root or FortiGate HA clusters on EMS in
the Security Fabric.
websocket
Enable/disable websockets for this FortiGate unit. Override behavior
using websocket-override.
websocket-malware
Allow this FortiGate unit to request malware hash notifications over
websocket.
push-ca-certs
Enable/disable syncing deep inspection certificates with EMS.
common-tags-api
Can recieve tag information from New Common Tags API from EMS.
tenant-id
Allow this FortiGate to retrieve Tenant-ID from EMS.
client-avatars
Allow this FortiGate to retrieve avatars from EMS by fingerprint.
single-vdom-connector
Allow this FortiGate to create a vdom connector to EMS.
fgt-sysinfo-api
Allow this FortiGate to send additional info to EMS.
ztna-server-info
Allow this FortiGate to send vdom's ZTNA server information to EMS.
tag-def
Allow this FortiGate to retrieve tag definitions from EMS.
used-tags
Allow this FortiGate to send used tags information to EMS.
crl
Allow this FortiGate to retrieve ZTNA certificate CRL files from EMS.
cloud-authentication-access-key
FortiClient EMS Cloud multitenancy access key
password
Not
Specified
dirty-reason
Dirty Reason for FortiClient EMS.
option
-none
FortiOS 8.0.0 CLI Reference
333
Fortinet Inc.

<!-- 来源页 334 -->
Parameter
Description
Type
Size
Default
Option
Description
none
FortiClient EMS entry not dirty.
mismatched-ems-sn
FortiClient EMS entry dirty because EMS SN is mismatched with
configured SN.
ems-id
EMS ID in order (1 - 7).
integer
Minimum
value: 1
Maximum
value: 7
0
fortinetone-cloud-authentication
Enable/disable authentication of FortiClient
EMS Cloud through FortiCloud account.
option
-disable
Option
Description
enable
Enable authentication of FortiClient EMS Cloud through FortiCloud
account.
disable
Disable authentication of FortiClient EMS Cloud through FortiCloud
account.
https-port
FortiClient EMS HTTPS access port number. (1
- 65535, default: 443).
integer
Minimum
value: 1
Maximum
value:
65535
443
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
name
FortiClient Enterprise Management Server
(EMS) name.
string
Maximum
length: 35
out-of-sync-threshold
Outdated resource threshold in seconds (10 -2592000, default = 345600).
integer
Minimum
value: 10
Maximum
value:
2592000 **
345600 **
FortiOS 8.0.0 CLI Reference
334
Fortinet Inc.

<!-- 来源页 335 -->
Parameter
Description
Type
Size
Default
pull-malware-hash
Enable/disable pulling FortiClient malware
hash from EMS.
option
-enable
Option
Description
enable
Enable pulling FortiClient malware hash from EMS.
disable
Disable pulling FortiClient malware hash from EMS.
pull-sysinfo
Enable/disable pulling SysInfo from EMS.
option
-enable
Option
Description
enable
Enable pulling FortiClient user SysInfo from EMS.
disable
Disable pulling FortiClient user SysInfo from EMS.
pull-tags
Enable/disable pulling FortiClient user tags
from EMS.
option
-enable
Option
Description
enable
Enable pulling FortiClient user tags from EMS.
disable
Disable pulling FortiClient user tags from EMS.
pull-vulnerabilities
Enable/disable pulling vulnerabilities from
EMS.
option
-enable
Option
Description
enable
Enable pulling client vulnerabilities from EMS.
disable
Disable pulling client vulnerabilities from EMS.
send-tags-to-all-vdoms
Relax restrictions on tags to send all EMS tags
to all VDOMs
option
-disable
Option
Description
enable
Enable sending tags to all vdoms.
disable
Disable sending tags to all vdoms.
serial-number
EMS Serial Number.
string
Maximum
length: 16
server
FortiClient EMS FQDN or IPv4 address.
string
Maximum
length: 255
source-ip
REST API call source IP.
ipv4-address-any
Not
Specified
0.0.0.0
FortiOS 8.0.0 CLI Reference
335
Fortinet Inc.

<!-- 来源页 336 -->
Parameter
Description
Type
Size
Default
status
Enable or disable this EMS configuration.
option
-disable
Option
Description
enable
Enable EMS configuration and operation.
disable
Disable EMS configuration and operation.
tenant-id
EMS Tenant ID.
string
Maximum
length: 32
trust-ca-cn
Enable/disable trust of the EMS certificate
issuer(CA) and common name(CN) for
certificate auto-renewal.
option
-enable
Option
Description
enable
Trust EMS certificate CA & CN to automatically renew certificate.
disable
Do not trust EMS certificate CA & CN to automatically renew
certificate.
verifying-ca
Lowest CA cert on Fortigate in verified EMS
cert chain.
string
Maximum
length: 79
websocket-override
Enable/disable override behavior for how this
FortiGate unit connects to EMS using a
WebSocket connection.
option
-disable
Option
Description
enable
Do not override the WebSocket connection. Connect to WebSocket
of this EMS server if it is capable (default).
disable
Override the WebSocket connection. Do not connect to WebSocket
even if EMS is capable of a WebSocket connection.
** Values may differ between models.
config endpoint-control fctems-override
Configure FortiClient Enterprise Management Server (EMS) entries.
config endpoint-control fctems-override
Description: Configure FortiClient Enterprise Management Server (EMS) entries.
edit <ems-id>
set call-timeout {integer}
set capabilities {option1}, {option2}, ...
set cloud-authentication-access-key {password}
set dirty-reason [none|mismatched-ems-sn]
set fortinetone-cloud-authentication [enable|disable]
FortiOS 8.0.0 CLI Reference
336
Fortinet Inc.

<!-- 来源页 337 -->
set https-port {integer}
set interface {string}
set interface-select-method [auto|sdwan|...]
set name {string}
set out-of-sync-threshold {integer}
set pull-malware-hash [enable|disable]
set pull-sysinfo [enable|disable]
set pull-tags [enable|disable]
set pull-vulnerabilities [enable|disable]
set send-tags-to-all-vdoms [enable|disable]
set serial-number {string}
set server {string}
set source-ip {ipv4-address-any}
set status [enable|disable]
set tenant-id {string}
set trust-ca-cn [enable|disable]
set verifying-ca {string}
set websocket-override [enable|disable]
next
end
config endpoint-control fctems-override
Parameter
Description
Type
Size
Default
call-timeout
FortiClient EMS call timeout in seconds (1 - 180
seconds, default = 30).
integer
Minimum
value: 1
Maximum
value: 180
30
capabilities
List of EMS capabilities.
option
-Option
Description
fabric-auth
Allow this FortiGate unit to load the authentication page provided by
EMS to authenticate itself with EMS.
silent-approval
Allow silent approval of non-root or FortiGate HA clusters on EMS in
the Security Fabric.
websocket
Enable/disable websockets for this FortiGate unit. Override behavior
using websocket-override.
websocket-malware
Allow this FortiGate unit to request malware hash notifications over
websocket.
push-ca-certs
Enable/disable syncing deep inspection certificates with EMS.
common-tags-api
Can recieve tag information from New Common Tags API from EMS.
FortiOS 8.0.0 CLI Reference
337
Fortinet Inc.

<!-- 来源页 338 -->
Parameter
Description
Type
Size
Default
Option
Description
tenant-id
Allow this FortiGate to retrieve Tenant-ID from EMS.
client-avatars
Allow this FortiGate to retrieve avatars from EMS by fingerprint.
single-vdom-connector
Allow this FortiGate to create a vdom connector to EMS.
fgt-sysinfo-api
Allow this FortiGate to send additional info to EMS.
ztna-server-info
Allow this FortiGate to send vdom's ZTNA server information to EMS.
tag-def
Allow this FortiGate to retrieve tag definitions from EMS.
used-tags
Allow this FortiGate to send used tags information to EMS.
crl
Allow this FortiGate to retrieve ZTNA certificate CRL files from EMS.
cloud-authentication-access-key
FortiClient EMS Cloud multitenancy access key
password
Not
Specified
dirty-reason
Dirty Reason for FortiClient EMS.
option
-none
Option
Description
none
FortiClient EMS entry not dirty.
mismatched-ems-sn
FortiClient EMS entry dirty because EMS SN is mismatched with
configured SN.
ems-id
EMS ID in order (1 - 7).
integer
Minimum
value: 1
Maximum
value: 7
0
fortinetone-cloud-authentication
Enable/disable authentication of FortiClient
EMS Cloud through FortiCloud account.
option
-disable
Option
Description
enable
Enable authentication of FortiClient EMS Cloud through FortiCloud
account.
disable
Disable authentication of FortiClient EMS Cloud through FortiCloud
account.
FortiOS 8.0.0 CLI Reference
338
Fortinet Inc.

<!-- 来源页 339 -->
Parameter
Description
Type
Size
Default
https-port
FortiClient EMS HTTPS access port number. (1
- 65535, default: 443).
integer
Minimum
value: 1
Maximum
value:
65535
443
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
name
FortiClient Enterprise Management Server
(EMS) name.
string
Maximum
length: 35
out-of-sync-threshold
Outdated resource threshold in seconds (10 -2592000, default = 345600).
integer
Minimum
value: 10
Maximum
value:
2592000 **
345600 **
pull-malware-hash
Enable/disable pulling FortiClient malware
hash from EMS.
option
-enable
Option
Description
enable
Enable pulling FortiClient malware hash from EMS.
disable
Disable pulling FortiClient malware hash from EMS.
pull-sysinfo
Enable/disable pulling SysInfo from EMS.
option
-enable
Option
Description
enable
Enable pulling FortiClient user SysInfo from EMS.
disable
Disable pulling FortiClient user SysInfo from EMS.
pull-tags
Enable/disable pulling FortiClient user tags
from EMS.
option
-enable
Option
Description
enable
Enable pulling FortiClient user tags from EMS.
FortiOS 8.0.0 CLI Reference
339
Fortinet Inc.

<!-- 来源页 340 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable pulling FortiClient user tags from EMS.
pull-vulnerabilities
Enable/disable pulling vulnerabilities from
EMS.
option
-enable
Option
Description
enable
Enable pulling client vulnerabilities from EMS.
disable
Disable pulling client vulnerabilities from EMS.
send-tags-to-all-vdoms
Relax restrictions on tags to send all EMS tags
to all VDOMs
option
-disable
Option
Description
enable
Enable sending tags to all vdoms.
disable
Disable sending tags to all vdoms.
serial-number
EMS Serial Number.
string
Maximum
length: 16
server
FortiClient EMS FQDN or IPv4 address.
string
Maximum
length: 255
source-ip
REST API call source IP.
ipv4-address-any
Not
Specified
0.0.0.0
status
Enable or disable this EMS configuration.
option
-disable
Option
Description
enable
Enable EMS configuration and operation.
disable
Disable EMS configuration and operation.
tenant-id
EMS Tenant ID.
string
Maximum
length: 32
trust-ca-cn
Enable/disable trust of the EMS certificate
issuer(CA) and common name(CN) for
certificate auto-renewal.
option
-enable
Option
Description
enable
Trust EMS certificate CA & CN to automatically renew certificate.
disable
Do not trust EMS certificate CA & CN to automatically renew
certificate.
FortiOS 8.0.0 CLI Reference
340
Fortinet Inc.

<!-- 来源页 341 -->
Parameter
Description
Type
Size
Default
verifying-ca
Lowest CA cert on Fortigate in verified EMS
cert chain.
string
Maximum
length: 79
websocket-override
Enable/disable override behavior for how this
FortiGate unit connects to EMS using a
WebSocket connection.
option
-disable
Option
Description
enable
Do not override the WebSocket connection. Connect to WebSocket
of this EMS server if it is capable (default).
disable
Override the WebSocket connection. Do not connect to WebSocket
even if EMS is capable of a WebSocket connection.
** Values may differ between models.
config endpoint-control settings
Configure endpoint control settings.
config endpoint-control settings
Description: Configure endpoint control settings.
set override [enable|disable]
end
config endpoint-control settings
Parameter
Description
Type
Size
Default
override
Override global EMS table for this VDOM.
option
-disable
Option
Description
enable
Enable Overriding global EMS table.
disable
Disable Overriding global EMS table.
FortiOS 8.0.0 CLI Reference
341
Fortinet Inc.

---


<!-- 来源页 838 -->
icap
This section includes syntax for the following commands:
l config icap profile on page 838
l config icap server-group on page 848
l config icap server on page 846
config icap profile
Configure ICAP profiles.
config icap profile
Description: Configure ICAP profiles.
edit <name>
set 204-response [disable|enable]
set 204-size-limit {integer}
set chunk-encap [disable|enable]
set comment {var-string}
set extension-feature {option1}, {option2}, ...
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set file-transfer {option1}, {option2}, ...
set file-transfer-failure [error|bypass]
set file-transfer-path {string}
set file-transfer-server {string}
set icap-block-log [disable|enable]
config icap-headers
Description: Configure ICAP forwarded request headers.
edit <id>
set base64-encoding [disable|enable]
set content {string}
set name {string}
next
end
set methods {option1}, {option2}, ...
set ocr-only [disable|enable]
set preview [disable|enable]
set preview-data-length {integer}
set replacemsg-group {string}
set request [disable|enable]
set request-failure [error|bypass]
set request-path {string}
set request-server {string}
set respmod-default-action [forward|bypass]
FortiOS 8.0.0 CLI Reference
838
Fortinet Inc.

<!-- 来源页 839 -->
config respmod-forward-rules
Description: ICAP response mode forward rules.
edit <name>
set action [forward|bypass]
config header-group
Description: HTTP header group.
edit <id>
set case-sensitivity [disable|enable]
set header {string}
set header-name {string}
next
end
set host {string}
set http-resp-status-code <code1>, <code2>, ...
next
end
set response [disable|enable]
set response-failure [error|bypass]
set response-path {string}
set response-req-hdr [disable|enable]
set response-server {string}
set scan-progress-interval {integer}
set streaming-content-bypass [disable|enable]
set timeout {integer}
set uuid {uuid}
next
end
config icap profile
Parameter
Description
Type
Size
Default
204-response
Enable/disable allowance of 204 response
from ICAP server.
option
-disable
Option
Description
disable
Disable allowance of 204 response from ICAP server.
enable
Enable allowance of 204 response from ICAP server.
204-size-limit
204 response size limit to be saved by ICAP
client in megabytes (1 - 10, default = 1 MB).
integer
Minimum
value: 1
Maximum
value: 10
1
chunk-encap
Enable/disable chunked encapsulation
(default = disable).
option
-disable
FortiOS 8.0.0 CLI Reference
839
Fortinet Inc.

<!-- 来源页 840 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Do not encapsulate chunked data.
enable
Encapsulate chunked data into a new chunk.
comment
Comment.
var-string
Maximum
length: 255
extension-feature
Enable/disable ICAP extension features.
option
-Option
Description
scan-progress
Support X-Scan-Progress-Interval ICAP header.
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
file-transfer
Configure the file transfer protocols to pass
transferred files to an ICAP server as
REQMOD.
option
-FortiOS 8.0.0 CLI Reference
840
Fortinet Inc.

<!-- 来源页 841 -->
Parameter
Description
Type
Size
Default
Option
Description
ssh
Forward file transfer with SSH protocol to ICAP server for further
processing.
ftp
Forward file transfer with FTP protocol to ICAP server for further
processing.
file-transfer-failure
Action to take if the ICAP server cannot be
contacted when processing a file transfer.
option
-error
Option
Description
error
Error.
bypass
Bypass.
file-transfer-path
Path component of the ICAP URI that
identifies the file transfer processing
service.
string
Maximum
length: 127
file-transfer-server
ICAP server to use for a file transfer.
string
Maximum
length: 63
icap-block-log
Enable/disable UTM log when infection
found (default = disable).
option
-disable
Option
Description
disable
Disable UTM log when infection found.
enable
Enable UTM log when infection found.
methods
The allowed HTTP methods that will be
sent to ICAP server for further processing.
option
-delete get head
options post put
trace connect
other
Option
Description
delete
Forward HTTP request or response with DELETE method to ICAP
server for further processing.
get
Forward HTTP request or response with GET method to ICAP server for
further processing.
head
Forward HTTP request or response with HEAD method to ICAP server
for further processing.
options
Forward HTTP request or response with OPTIONS method to ICAP
server for further processing.
FortiOS 8.0.0 CLI Reference
841
Fortinet Inc.

<!-- 来源页 842 -->
Parameter
Description
Type
Size
Default
Option
Description
post
Forward HTTP request or response with POST method to ICAP server
for further processing.
put
Forward HTTP request or response with PUT method to ICAP server for
further processing.
trace
Forward HTTP request or response with TRACE method to ICAP server
for further processing.
connect
Forward HTTP request or response with CONNECT method to ICAP
server for further processing.
other
Forward HTTP request or response with All other methods to ICAP
server for further processing.
name
ICAP profile name.
string
Maximum
length: 47
ocr-only
Enable/disable this FortiGate unit to submit
only OCR interested content to the ICAP
server.
option
-disable
Option
Description
disable
Disable this FortiGate unit to submit only OCR interested content to the
ICAP server.
enable
Enable this FortiGate unit to submit only OCR interested content to the
ICAP server.
preview
Enable/disable preview of data to ICAP
server.
option
-disable
Option
Description
disable
Disable preview of data to ICAP server.
enable
Enable preview of data to ICAP server.
preview-data-length
Preview data length to be sent to ICAP
server.
integer
Minimum
value: 0
Maximum
value: 4096
0
replacemsg-group
Replacement message group.
string
Maximum
length: 35
request
Enable/disable whether an HTTP request is
passed to an ICAP server.
option
-disable
FortiOS 8.0.0 CLI Reference
842
Fortinet Inc.

<!-- 来源页 843 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable HTTP request passing to ICAP server.
enable
Enable HTTP request passing to ICAP server.
request-failure
Action to take if the ICAP server cannot be
contacted when processing an HTTP
request.
option
-error
Option
Description
error
Error.
bypass
Bypass.
request-path
Path component of the ICAP URI that
identifies the HTTP request processing
service.
string
Maximum
length: 127
request-server
ICAP server to use for an HTTP request.
string
Maximum
length: 63
respmod-default-action
Default action to ICAP response
modification (respmod) processing.
option
-forward
Option
Description
forward
Forward response to ICAP server unless a rule specifies not to.
bypass
Don't forward request to ICAP server unless a rule specifies to forward
the request.
response
Enable/disable whether an HTTP response
is passed to an ICAP server.
option
-disable
Option
Description
disable
Disable HTTP response passing to ICAP server.
enable
Enable HTTP response passing to ICAP server.
response-failure
Action to take if the ICAP server cannot be
contacted when processing an HTTP
response.
option
-error
Option
Description
error
Error.
bypass
Bypass.
FortiOS 8.0.0 CLI Reference
843
Fortinet Inc.

<!-- 来源页 844 -->
Parameter
Description
Type
Size
Default
response-path
Path component of the ICAP URI that
identifies the HTTP response processing
service.
string
Maximum
length: 127
response-req-hdr
Enable/disable addition of req-hdr for ICAP
response modification (respmod)
processing.
option
-enable
Option
Description
disable
Do not add req-hdr for response modification (respmod) processing.
enable
Add req-hdr for response modification (respmod) processing.
response-server
ICAP server to use for an HTTP response.
string
Maximum
length: 63
scan-progress-interval
Scan progress interval value.
integer
Minimum
value: 5
Maximum
value: 30
10
streaming-content-bypass
Enable/disable bypassing of ICAP server
for streaming content.
option
-disable
Option
Description
disable
Disable bypassing of ICAP server for streaming content.
enable
Enable bypassing of ICAP server for streaming content.
timeout
Time (in seconds) that ICAP client waits for
the response from ICAP server.
integer
Minimum
value: 30
Maximum
value: 3600
30
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be manually
reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
config icap-headers
Parameter
Description
Type
Size
Default
base64-encoding
Enable/disable use of base64 encoding of HTTP
content.
option
-disable
FortiOS 8.0.0 CLI Reference
844
Fortinet Inc.

<!-- 来源页 845 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable use of base64 encoding of HTTP content.
enable
Enable use of base64 encoding of HTTP content.
content
HTTP header content.
string
Maximum
length: 255
id
HTTP forwarded header ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
name
HTTP forwarded header name.
string
Maximum
length: 79
config respmod-forward-rules
Parameter
Description
Type
Size
Default
action
Action to be taken for ICAP server.
option
-forward
Option
Description
forward
Forward request to ICAP server when this rule is matched.
bypass
Don't forward request to ICAP server when this rule is matched.
host
Address object for the host.
string
Maximum
length: 79
http-resp-status-code
<code>
HTTP response status code.
HTTP response status code.
integer
Minimum
value: 100
Maximum
value: 599
name
Address name.
string
Maximum
length: 63
config header-group
Parameter
Description
Type
Size
Default
case-sensitivity
Enable/disable case sensitivity when matching
header.
option
-disable
Option
Description
disable
Ignore case when matching header.
FortiOS 8.0.0 CLI Reference
845
Fortinet Inc.

<!-- 来源页 846 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Do not ignore case when matching header.
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
config icap server
Configure ICAP servers.
config icap server
Description: Configure ICAP servers.
edit <name>
set addr-type [ip4|ip6|...]
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set fqdn {string}
set healthcheck [disable|enable]
set healthcheck-service {string}
set ip-address {ipv4-address-any}
set ip6-address {ipv6-address}
set max-connections {integer}
set port {integer}
set secure [disable|enable]
set ssl-cert {string}
set uuid {uuid}
next
end
config icap server
Parameter
Description
Type
Size
Default
addr-type
Address type of the remote ICAP
server: IPv4, IPv6 or FQDN.
option
-ip4
FortiOS 8.0.0 CLI Reference
846
Fortinet Inc.

<!-- 来源页 847 -->
Parameter
Description
Type
Size
Default
Option
Description
ip4
Use an IPv4 address for the remote ICAP server.
ip6
Use an IPv6 address for the remote ICAP server.
fqdn
Use the FQDN for the forwarding proxy server.
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
fqdn
ICAP remote server Fully Qualified
Domain Name (FQDN).
string
Maximum
length: 255
healthcheck
Enable/disable ICAP remote server
health checking. Attempts to connect
to the remote ICAP server to verify
that the server is operating normally.
option
-disable
Option
Description
disable
Disable health checking.
FortiOS 8.0.0 CLI Reference
847
Fortinet Inc.

<!-- 来源页 848 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable health checking.
healthcheck-service
ICAP Service name to use for health
checks.
string
Maximum
length: 127
ip-address
IPv4 address of the ICAP server.
ipv4-address-any
Not Specified
0.0.0.0
ip6-address
IPv6 address of the ICAP server.
ipv6-address
Not Specified
::
max-connections
Maximum number of concurrent
connections to ICAP server (unlimited
= 0, default = 100). Must not be less
than wad-worker-count.
integer
Minimum value:
0 Maximum
value:
4294967295
100
name
Server name.
string
Maximum
length: 63
port
ICAP server port.
integer
Minimum value:
1 Maximum
value: 65535
1344
secure
Enable/disable secure connection to
ICAP server.
option
-disable
Option
Description
disable
Disable connection to secure ICAP server.
enable
Enable connection to secure ICAP server.
ssl-cert
CA certificate name.
string
Maximum
length: 79
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
config icap server-group
Configure an ICAP server group consisting of multiple forward servers. Supports failover and load balancing.
config icap server-group
Description: Configure an ICAP server group consisting of multiple forward servers. Supports
failover and load balancing.
FortiOS 8.0.0 CLI Reference
848
Fortinet Inc.

<!-- 来源页 849 -->
edit <name>
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set ldb-method [weighted|least-session|...]
config server-list
Description: Add ICAP servers to a list to form a server group. Optionally assign
weights to each server.
edit <name>
set weight {integer}
next
end
set uuid {uuid}
next
end
config icap server-group
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
FortiOS 8.0.0 CLI Reference
849
Fortinet Inc.

<!-- 来源页 850 -->
Parameter
Description
Type
Size
Default
Option
Description
root
Source of truth for this object is the root of the fabric.
ldb-method
Load balance method.
option
-weighted
Option
Description
weighted
Load balance traffic to forward servers based on assigned weights.
least-session
Send new sessions to the server with lowest session count.
active-passive
Send new sessions to active server with high weight.
name
Configure an ICAP server group consisting
one or multiple forward servers. Supports
failover and load balancing.
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
config server-list
Parameter
Description
Type
Size
Default
name
ICAP server name.
string
Maximum
length: 63
weight
Optionally assign a weight of the forwarding server
for weighted load balancing (1 - 100, default = 10).
integer
Minimum
value: 1
Maximum
value: 100
10
FortiOS 8.0.0 CLI Reference
850
Fortinet Inc.

---


<!-- 来源页 870 -->
llm
This section includes syntax for the following commands:
l config llm profile on page 870
l config llm proxy on page 874
l config llm server on page 877
config llm profile
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
Configure LLM Proxy profiles.
config llm profile
Description: Configure LLM Proxy profiles.
edit <name>
config chat
FortiOS 8.0.0 CLI Reference
870
Fortinet Inc.

<!-- 来源页 871 -->
Description: LLM Proxy chat completions API (/v1/chat/completions).
set max-completion-tokens {integer}
set max-req-len {integer}
set status [enable|disable]
set stream [bypass|block]
set system-prompt {var-string}
set system-prompt-mode [bypass|replace|...]
end
config image-gen
Description: LLM Proxy image generation API (/v1/images/generations).
set status [enable|disable]
end
config list-models
Description: LLM Proxy list models API (/v1/models).
set status [enable|disable]
end
set log [none|blocked|...]
set unknown-api [enable|disable]
next
end
config llm profile
Parameter
Description
Type
Size
Default
log
Log option.
option
-blocked
Option
Description
none
No log.
blocked
Log blocked requests.
all
Log all requests.
name
LLM Proxy profile name.
string
Maximum
length: 35
unknown-api
Support unknown API.
option
-disable
Option
Description
enable
Enable unknown API.
disable
Disable unknown API.
FortiOS 8.0.0 CLI Reference
871
Fortinet Inc.

<!-- 来源页 872 -->
config chat
Parameter
Description
Type
Size
Default
max-completion-tokens
Maximum number of completion tokens (0 -10000000, default = 0, means no limit).
integer
Minimum
value: 0
Maximum
value:
10000000
0
max-req-len
Max size of chat completions request body, (0 -65535 KiB, default = 1024, 0 means no limit).
integer
Minimum
value: 0
Maximum
value:
65535
1024
status
Support chat completions API.
option
-enable
Option
Description
enable
Enable chat completions API.
disable
Disable chat completions API.
stream
support chat completions stream mode.
option
-bypass
Option
Description
bypass
Enable chat completions stream mode.
block
Block chat completions stream mode.
system-prompt
Replace/Append chat completions system
prompt.
var-string
Maximum
length: 255
system-prompt-mode
System prompt processing mode.
option
-bypass
Option
Description
bypass
Don't change the system prompt.
replace
Replace the system prompt with config.
prepend
Prepend the config to the system prompt.
append
Append the config to the system prompt.
config image-gen
Parameter
Description
Type
Size
Default
status
Support image generation API.
option
-enable
FortiOS 8.0.0 CLI Reference
872
Fortinet Inc.

<!-- 来源页 873 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable image generation API.
disable
Disable image generation API.
config list-models
Parameter
Description
Type
Size
Default
status
Support list models API.
option
-enable
Option
Description
enable
Enable list models API.
disable
Disable list models API.
FortiOS 8.0.0 CLI Reference
873
Fortinet Inc.

<!-- 来源页 874 -->
config llm proxy
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
Configure LLM Proxy.
config llm proxy
Description: Configure LLM Proxy.
set hostname {string}
set incoming-http-port {integer}
set incoming-https-port {integer}
set incoming-ip {ipv4-address-any}
set incoming-ip6 {ipv6-address}
set interface <name1>, <name2>, ...
set ipv6-status [enable|disable]
set name {string}
set protocol {option1}, {option2}, ...
set srv-pool-max-concurrent-request {integer}
set srv-pool-max-request {integer}
set srv-pool-ttl {integer}
set ssl-certificate <name1>, <name2>, ...
set ssl-max-version [ssl-3.0|tls-1.0|...]
set ssl-min-version [ssl-3.0|tls-1.0|...]
FortiOS 8.0.0 CLI Reference
874
Fortinet Inc.

<!-- 来源页 875 -->
set status [enable|disable]
end
config llm proxy
Parameter
Description
Type
Size
Default
hostname
hostname.
string
Maximum
length: 255
incoming-http-port
LLM Proxy HTTP incoming port.
integer
Minimum
value: 1
Maximum
value: 65535
8098
incoming-https-port
LLM Proxy HTTPS incoming port.
integer
Minimum
value: 1
Maximum
value: 65535
8099
incoming-ip
LLM Proxy incoming IP.
ipv4-address-any
Not Specified
0.0.0.0
incoming-ip6
LLM Proxy incoming IPv6.
ipv6-address
Not Specified
::
interface
<name>
Name of the interfaces to use LLM Proxy.
Interface list.
string
Maximum
length: 79
ipv6-status
Enable/disable the LLM proxy on IPv6.
option
-disable
Option
Description
enable
Enable the LLM proxy on IPv6.
disable
Disable the LLM proxy on IPv6.
name
LLM Proxy name.
string
Maximum
length: 35
protocol
Supported protocols.
option
-https
Option
Description
http
HTTP.
https
HTTPS.
FortiOS 8.0.0 CLI Reference
875
Fortinet Inc.

<!-- 来源页 876 -->
Parameter
Description
Type
Size
Default
srv-pool-max-concurrent-request
Maximum number of concurrent requests that a
server can handle (default = unlimited).
integer
Minimum
value: 0
Maximum
value:
2147483647
0
srv-pool-max-request
Maximum number of requests that a server can
handle before disconnecting sessions (default
= unlimited).
integer
Minimum
value: 0
Maximum
value:
2147483647
0
srv-pool-ttl
Time-to-live for idle connections to servers.
integer
Minimum
value: 0
Maximum
value:
2147483647
30
ssl-certificate
<name>
Name of the certificates to use for SSL
handshake.
Certificate list.
string
Maximum
length: 79
ssl-max-version
Highest SSL/TLS version acceptable from a
client.
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
Lowest SSL/TLS version acceptable from a
client.
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
status
Enable/disable the LLM proxy.
option
-disable
FortiOS 8.0.0 CLI Reference
876
Fortinet Inc.

<!-- 来源页 877 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable the LLM proxy.
disable
Disable the LLM proxy.
config llm server
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
Configure LLM Proxy servers.
config llm server
Description: Configure LLM Proxy servers.
edit <name>
set accept-custom-model [enable|disable]
set anthropic-version {string}
set api-key {string}
set azure-api-version {string}
set azure-resource-name {string}
FortiOS 8.0.0 CLI Reference
877
Fortinet Inc.

<!-- 来源页 878 -->
set built-in-server [openai|azure|...]
set chat-completions-api [none|openai|...]
set custom-model-allow-regex {string}
set custom-model-block-regex {string}
set display-name {string}
set end-point {var-string}
set image-gen-api [none|openai|...]
set models {string}
set type [built-in|customized]
set verify-cert [enable|disable]
next
end
config llm server
Parameter
Description
Type
Size
Default
accept-custom-model
accept custom model
option
-disable
Option
Description
enable
Enable custom model other than models
disable
Disable custom model other than models
anthropic-version
Anthropic version in API
string
Maximum
length: 63
2023-06-01
api-key
API Keys of the LLM server
string
Maximum
length: 255
azure-api-version
Azure API version.
string
Maximum
length: 63
2024-02-01
azure-resource-name
Azure resource name.
string
Maximum
length: 63
built-in-server
built-in LLM server
option
-openai
Option
Description
openai
OpenAI LLM server.
azure
Azure LLM server (for non-OpenAI models).
azure-openai
Azure LLM server (for OpenAI models).
gemini
Gemini LLM server.
anthropic
Anthropic LLM server.
grok
Grok LLM server.
FortiOS 8.0.0 CLI Reference
878
Fortinet Inc.

<!-- 来源页 879 -->
Parameter
Description
Type
Size
Default
Option
Description
gemini-with-openai-api
Gemini LLM server with OpenAI API.
anthropic-with-openai-api
Anthropic LLM server with OpenAI API.
chat-completions-api
Chat Completions API of this server
option
-openai
Option
Description
none
No Chat-Completions API
openai
Follow OpenAI Chat-Completions API
azure-openai
Follow Azure OpenAI Chat-Completions API
gemini
Follow Google Gemini Chat API
anthropic
Follow Anthropic Chat API
custom-model-allow-regex
custom model allow regex, allow all if empty
string
Maximum
length: 255
custom-model-block-regex
custom model block regex, no block if empty
string
Maximum
length: 255
display-name
display name of the LLM Server
string
Maximum
length: 79
end-point
Overwrite the default end-point of the vendor.
var-string
Maximum
length: 255
image-gen-api
Image-Gen API of this server
option
-openai
Option
Description
none
No Chat-Completions API
openai
Follow OpenAI Image-Gen API
azure-openai
Follow Azure OpenAI Chat-Completions API
models
models of the LLM Server
string
Maximum
length: 79
name
LLM Proxy server name.
string
Maximum
length: 35
type
LLM server type
option
-built-in
FortiOS 8.0.0 CLI Reference
879
Fortinet Inc.

<!-- 来源页 880 -->
Parameter
Description
Type
Size
Default
Option
Description
built-in
Built-in LLM server.
customized
User customized LLM server.
verify-cert
Enable/disable certificate verification.
option
-enable
Option
Description
enable
Enable certificate verification.
disable
Disable certificate verification.
FortiOS 8.0.0 CLI Reference
880
Fortinet Inc.

---


<!-- 来源页 1099 -->
nsxt
This section includes syntax for the following commands:
l config nsxt service-chain on page 1099
l config nsxt setting on page 1101
config nsxt service-chain
This command is available for model(s): FortiGate-VM64.
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
91G, FortiGate-VM64 Aliyun, FortiGate-VM64 AWS, FortiGate-VM64 Azure, FortiGate-VM64 GCP,
FortiGate-VM64 OPC, FortiGateRugged 50G 5G, FortiGateRugged 60F 3G4G, FortiGateRugged 60F
Gen2, FortiGateRugged 70F 3G4G, FortiGateRugged 70F, FortiGateRugged 70G 5G Dual,
FortiGateRugged 70G, FortiWiFi 30G, FortiWiFi 31G, FortiWiFi 40F 3G4G, FortiWiFi 40F, FortiWiFi
50G 5G, FortiWiFi 50G DSL, FortiWiFi 50G SFP, FortiWiFi 50G, FortiWiFi 51G, FortiWiFi 60F, FortiWiFi
61F, FortiWiFi 70G-POE, FortiWiFi 70G, FortiWiFi 71G, FortiWiFi 80F 2R 3G4G DSL, FortiWiFi 80F 2R,
FortiWiFi 81F 2R 3G4G DSL, FortiWiFi 81F 2R 3G4G-POE, FortiWiFi 81F 2R-POE, FortiWiFi 81F 2R.
Configure NSX-T service chain.
config nsxt service-chain
Description: Configure NSX-T service chain.
edit <id>
set name {string}
config service-index
Description: Configure service index.
FortiOS 8.0.0 CLI Reference
1099
Fortinet Inc.

<!-- 来源页 1100 -->
edit <id>
set name {string}
set reverse-index {integer}
set vd {string}
next
end
next
end
config nsxt service-chain
Parameter
Description
Type
Size
Default
id
Chain ID.
integer
Minimum
value: 0
Maximum
value: 1023
0
name
Chain name.
string
Maximum
length: 63
config service-index
Parameter
Description
Type
Size
Default
id
Service index.
integer
Minimum
value: 0
Maximum
value: 255
0
name
Index name.
string
Maximum
length: 63
reverse-index
Reverse service index.
integer
Minimum
value: 1
Maximum
value: 255
1
vd
VDOM name.
string
Maximum
length: 31
FortiOS 8.0.0 CLI Reference
1100
Fortinet Inc.

<!-- 来源页 1101 -->
config nsxt setting
This command is available for model(s): FortiGate-VM64.
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
91G, FortiGate-VM64 Aliyun, FortiGate-VM64 AWS, FortiGate-VM64 Azure, FortiGate-VM64 GCP,
FortiGate-VM64 OPC, FortiGateRugged 50G 5G, FortiGateRugged 60F 3G4G, FortiGateRugged 60F
Gen2, FortiGateRugged 70F 3G4G, FortiGateRugged 70F, FortiGateRugged 70G 5G Dual,
FortiGateRugged 70G, FortiWiFi 30G, FortiWiFi 31G, FortiWiFi 40F 3G4G, FortiWiFi 40F, FortiWiFi
50G 5G, FortiWiFi 50G DSL, FortiWiFi 50G SFP, FortiWiFi 50G, FortiWiFi 51G, FortiWiFi 60F, FortiWiFi
61F, FortiWiFi 70G-POE, FortiWiFi 70G, FortiWiFi 71G, FortiWiFi 80F 2R 3G4G DSL, FortiWiFi 80F 2R,
FortiWiFi 81F 2R 3G4G DSL, FortiWiFi 81F 2R 3G4G-POE, FortiWiFi 81F 2R-POE, FortiWiFi 81F 2R.
Configure NSX-T setting.
config nsxt setting
Description: Configure NSX-T setting.
set liveness [enable|disable]
set service {string}
end
config nsxt setting
Parameter
Description
Type
Size
Default
liveness
Enable/disable liveness detection packet
forwarding.
option
-disable
FortiOS 8.0.0 CLI Reference
1101
Fortinet Inc.

<!-- 来源页 1102 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable liveness detection packet forwarding.
disable
Disable liveness detection packet forwarding.
service
Service name.
string
Maximum
length: 63
FortiOS 8.0.0 CLI Reference
1102
Fortinet Inc.

---


<!-- 来源页 2213 -->
telemetry-controller
This section includes syntax for the following commands:
l config telemetry-controller agent-profile on page 2215
l config telemetry-controller agent on page 2213
l config telemetry-controller application predefine on page 2216
l config telemetry-controller global on page 2217
l config telemetry-controller profile on page 2219
config telemetry-controller agent
This command is available for model(s): FortiGate 1000D, FortiGate 1000F, FortiGate 1001F,
FortiGate 100F, FortiGate 101F Gen2, FortiGate 1100E, FortiGate 1101E, FortiGate 120G, FortiGate
121G, FortiGate 1800F, FortiGate 1801F, FortiGate 2000E, FortiGate 200E, FortiGate 200F, FortiGate
200G, FortiGate 201E, FortiGate 201F, FortiGate 201G, FortiGate 2200E, FortiGate 2201E, FortiGate
2500E, FortiGate 2600F, FortiGate 2601F, FortiGate 3000F, FortiGate 3001F, FortiGate 300E,
FortiGate 301E, FortiGate 3200F, FortiGate 3201F Gen2, FortiGate 3300E, FortiGate 3301E,
FortiGate 3400E, FortiGate 3401E, FortiGate 3500F Gen2, FortiGate 3501F Gen2, FortiGate 3600E,
FortiGate 3601E, FortiGate 3700F, FortiGate 3701F, FortiGate 3960E, FortiGate 3980E, FortiGate
400E Bypass, FortiGate 400E, FortiGate 400F, FortiGate 401E, FortiGate 401F, FortiGate 4200F,
FortiGate 4201F Gen2, FortiGate 4400F, FortiGate 4401F Gen2, FortiGate 4800F, FortiGate 4801F,
FortiGate 500E, FortiGate 501E, FortiGate 600E, FortiGate 600F, FortiGate 601E, FortiGate 601F,
FortiGate 70F, FortiGate 70G-POE, FortiGate 70G, FortiGate 71F, FortiGate 71G-POE, FortiGate 71G,
FortiGate 800D, FortiGate 80F Bypass, FortiGate 80F DSL, FortiGate 80F Gen2, FortiGate 80F-POE,
FortiGate 81F Gen2, FortiGate 81F-POE, FortiGate 900D, FortiGate 900G, FortiGate 901G, FortiGate
90G Gen2, FortiGate 90G, FortiGate 91G Gen2, FortiGate 91G, FortiGateRugged 70F 3G4G,
FortiGateRugged 70F, FortiGateRugged 70G 5G Dual, FortiGateRugged 70G, FortiWiFi 70G-POE,
FortiWiFi 70G, FortiWiFi 71G, FortiWiFi 80F 2R 3G4G DSL, FortiWiFi 80F 2R, FortiWiFi 81F 2R 3G4G
DSL, FortiWiFi 81F 2R 3G4G-POE, FortiWiFi 81F 2R-POE, FortiWiFi 81F 2R.
It is not available for: FortiGate 30G, FortiGate 31G, FortiGate 40F 3G4G, FortiGate 40F, FortiGate
50G 5G, FortiGate 50G DSL, FortiGate 50G SFP-POE, FortiGate 50G SFP, FortiGate 50G, FortiGate
51G 5G, FortiGate 51G SFP-POE, FortiGate 51G, FortiGate 60F, FortiGate 61F, FortiGate-VM64
Aliyun, FortiGate-VM64 AWS, FortiGate-VM64 Azure, FortiGate-VM64 GCP, FortiGate-VM64 OPC,
FortiGate-VM64, FortiGateRugged 50G 5G, FortiGateRugged 60F 3G4G, FortiGateRugged 60F
Gen2, FortiWiFi 30G, FortiWiFi 31G, FortiWiFi 40F 3G4G, FortiWiFi 40F, FortiWiFi 50G 5G, FortiWiFi
50G DSL, FortiWiFi 50G SFP, FortiWiFi 50G, FortiWiFi 51G, FortiWiFi 60F, FortiWiFi 61F.
Configure FortiTelemetry agents managed by a FortiGate unit.
config telemetry-controller agent
Description: Configure FortiTelemetry agents managed by a FortiGate unit.
FortiOS 8.0.0 CLI Reference
2213
Fortinet Inc.

<!-- 来源页 2214 -->
edit <agent-id>
set agent-profile {string}
set alias {string}
set authz [rejected|authorized|...]
set comment {var-string}
next
end
config telemetry-controller agent
Parameter
Description
Type
Size
Default
agent-id
Agent ID.
string
Maximum
length: 19
agent-profile
Name of an existing agent profile.
string
Maximum
length: 35
alias
Alias used in display for ease of distinguishing
agents.
string
Maximum
length: 35
authz
Authorization status of this agent.
option
-unauthorized
Option
Description
rejected
Agent is rejected.
authorized
Agent is authorized.
unauthorized
Agent is unauthorized.
comment
Comment.
var-string
Maximum
length: 255
FortiOS 8.0.0 CLI Reference
2214
Fortinet Inc.

<!-- 来源页 2215 -->
config telemetry-controller agent-profile
This command is available for model(s): FortiGate 1000D, FortiGate 1000F, FortiGate 1001F,
FortiGate 100F, FortiGate 101F Gen2, FortiGate 1100E, FortiGate 1101E, FortiGate 120G, FortiGate
121G, FortiGate 1800F, FortiGate 1801F, FortiGate 2000E, FortiGate 200E, FortiGate 200F, FortiGate
200G, FortiGate 201E, FortiGate 201F, FortiGate 201G, FortiGate 2200E, FortiGate 2201E, FortiGate
2500E, FortiGate 2600F, FortiGate 2601F, FortiGate 3000F, FortiGate 3001F, FortiGate 300E,
FortiGate 301E, FortiGate 3200F, FortiGate 3201F Gen2, FortiGate 3300E, FortiGate 3301E,
FortiGate 3400E, FortiGate 3401E, FortiGate 3500F Gen2, FortiGate 3501F Gen2, FortiGate 3600E,
FortiGate 3601E, FortiGate 3700F, FortiGate 3701F, FortiGate 3960E, FortiGate 3980E, FortiGate
400E Bypass, FortiGate 400E, FortiGate 400F, FortiGate 401E, FortiGate 401F, FortiGate 4200F,
FortiGate 4201F Gen2, FortiGate 4400F, FortiGate 4401F Gen2, FortiGate 4800F, FortiGate 4801F,
FortiGate 500E, FortiGate 501E, FortiGate 600E, FortiGate 600F, FortiGate 601E, FortiGate 601F,
FortiGate 70F, FortiGate 70G-POE, FortiGate 70G, FortiGate 71F, FortiGate 71G-POE, FortiGate 71G,
FortiGate 800D, FortiGate 80F Bypass, FortiGate 80F DSL, FortiGate 80F Gen2, FortiGate 80F-POE,
FortiGate 81F Gen2, FortiGate 81F-POE, FortiGate 900D, FortiGate 900G, FortiGate 901G, FortiGate
90G Gen2, FortiGate 90G, FortiGate 91G Gen2, FortiGate 91G, FortiGateRugged 70F 3G4G,
FortiGateRugged 70F, FortiGateRugged 70G 5G Dual, FortiGateRugged 70G, FortiWiFi 70G-POE,
FortiWiFi 70G, FortiWiFi 71G, FortiWiFi 80F 2R 3G4G DSL, FortiWiFi 80F 2R, FortiWiFi 81F 2R 3G4G
DSL, FortiWiFi 81F 2R 3G4G-POE, FortiWiFi 81F 2R-POE, FortiWiFi 81F 2R.
It is not available for: FortiGate 30G, FortiGate 31G, FortiGate 40F 3G4G, FortiGate 40F, FortiGate
50G 5G, FortiGate 50G DSL, FortiGate 50G SFP-POE, FortiGate 50G SFP, FortiGate 50G, FortiGate
51G 5G, FortiGate 51G SFP-POE, FortiGate 51G, FortiGate 60F, FortiGate 61F, FortiGate-VM64
Aliyun, FortiGate-VM64 AWS, FortiGate-VM64 Azure, FortiGate-VM64 GCP, FortiGate-VM64 OPC,
FortiGate-VM64, FortiGateRugged 50G 5G, FortiGateRugged 60F 3G4G, FortiGateRugged 60F
Gen2, FortiWiFi 30G, FortiWiFi 31G, FortiWiFi 40F 3G4G, FortiWiFi 40F, FortiWiFi 50G 5G, FortiWiFi
50G DSL, FortiWiFi 50G SFP, FortiWiFi 50G, FortiWiFi 51G, FortiWiFi 60F, FortiWiFi 61F.
Configure FortiTelemetry agent profiles.
config telemetry-controller agent-profile
Description: Configure FortiTelemetry agent profiles.
edit <name>
set comment {var-string}
set model [ftl-100g|windows|...]
next
end
config telemetry-controller agent-profile
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
model
Model.
option
-ftl-100g
FortiOS 8.0.0 CLI Reference
2215
Fortinet Inc.

<!-- 来源页 2216 -->
Parameter
Description
Type
Size
Default
Option
Description
ftl-100g
FTL-100G.
windows
Microsoft Windows agent.
macos
Apple macOS agent.
name
Name of the agent profile.
string
Maximum
length: 35
config telemetry-controller application predefine
This command is available for model(s): FortiGate 1000D, FortiGate 1000F, FortiGate 1001F,
FortiGate 100F, FortiGate 101F Gen2, FortiGate 1100E, FortiGate 1101E, FortiGate 120G, FortiGate
121G, FortiGate 1800F, FortiGate 1801F, FortiGate 2000E, FortiGate 200E, FortiGate 200F, FortiGate
200G, FortiGate 201E, FortiGate 201F, FortiGate 201G, FortiGate 2200E, FortiGate 2201E, FortiGate
2500E, FortiGate 2600F, FortiGate 2601F, FortiGate 3000F, FortiGate 3001F, FortiGate 300E,
FortiGate 301E, FortiGate 3200F, FortiGate 3201F Gen2, FortiGate 3300E, FortiGate 3301E,
FortiGate 3400E, FortiGate 3401E, FortiGate 3500F Gen2, FortiGate 3501F Gen2, FortiGate 3600E,
FortiGate 3601E, FortiGate 3700F, FortiGate 3701F, FortiGate 3960E, FortiGate 3980E, FortiGate
400E Bypass, FortiGate 400E, FortiGate 400F, FortiGate 401E, FortiGate 401F, FortiGate 4200F,
FortiGate 4201F Gen2, FortiGate 4400F, FortiGate 4401F Gen2, FortiGate 4800F, FortiGate 4801F,
FortiGate 500E, FortiGate 501E, FortiGate 600E, FortiGate 600F, FortiGate 601E, FortiGate 601F,
FortiGate 70F, FortiGate 70G-POE, FortiGate 70G, FortiGate 71F, FortiGate 71G-POE, FortiGate 71G,
FortiGate 800D, FortiGate 80F Bypass, FortiGate 80F DSL, FortiGate 80F Gen2, FortiGate 80F-POE,
FortiGate 81F Gen2, FortiGate 81F-POE, FortiGate 900D, FortiGate 900G, FortiGate 901G, FortiGate
90G Gen2, FortiGate 90G, FortiGate 91G Gen2, FortiGate 91G, FortiGateRugged 70F 3G4G,
FortiGateRugged 70F, FortiGateRugged 70G 5G Dual, FortiGateRugged 70G, FortiWiFi 70G-POE,
FortiWiFi 70G, FortiWiFi 71G, FortiWiFi 80F 2R 3G4G DSL, FortiWiFi 80F 2R, FortiWiFi 81F 2R 3G4G
DSL, FortiWiFi 81F 2R 3G4G-POE, FortiWiFi 81F 2R-POE, FortiWiFi 81F 2R.
It is not available for: FortiGate 30G, FortiGate 31G, FortiGate 40F 3G4G, FortiGate 40F, FortiGate
50G 5G, FortiGate 50G DSL, FortiGate 50G SFP-POE, FortiGate 50G SFP, FortiGate 50G, FortiGate
51G 5G, FortiGate 51G SFP-POE, FortiGate 51G, FortiGate 60F, FortiGate 61F, FortiGate-VM64
Aliyun, FortiGate-VM64 AWS, FortiGate-VM64 Azure, FortiGate-VM64 GCP, FortiGate-VM64 OPC,
FortiGate-VM64, FortiGateRugged 50G 5G, FortiGateRugged 60F 3G4G, FortiGateRugged 60F
Gen2, FortiWiFi 30G, FortiWiFi 31G, FortiWiFi 40F 3G4G, FortiWiFi 40F, FortiWiFi 50G 5G, FortiWiFi
50G DSL, FortiWiFi 50G SFP, FortiWiFi 50G, FortiWiFi 51G, FortiWiFi 60F, FortiWiFi 61F.
Configure FortiTelemetry predefined applications.
config telemetry-controller application predefine
Description: Configure FortiTelemetry predefined applications.
edit <app-name>
set comment {var-string}
FortiOS 8.0.0 CLI Reference
2216
Fortinet Inc.

<!-- 来源页 2217 -->
next
end
config telemetry-controller application predefine
Parameter
Description
Type
Size
Default
app-name
Application name.
string
Maximum
length: 79
comment
Comment. Read-only.
var-string
Maximum
length: 255
config telemetry-controller global
This command is available for model(s): FortiGate 1000D, FortiGate 1000F, FortiGate 1001F,
FortiGate 100F, FortiGate 101F Gen2, FortiGate 1100E, FortiGate 1101E, FortiGate 120G, FortiGate
121G, FortiGate 1800F, FortiGate 1801F, FortiGate 2000E, FortiGate 200E, FortiGate 200F, FortiGate
200G, FortiGate 201E, FortiGate 201F, FortiGate 201G, FortiGate 2200E, FortiGate 2201E, FortiGate
2500E, FortiGate 2600F, FortiGate 2601F, FortiGate 3000F, FortiGate 3001F, FortiGate 300E,
FortiGate 301E, FortiGate 3200F, FortiGate 3201F Gen2, FortiGate 3300E, FortiGate 3301E,
FortiGate 3400E, FortiGate 3401E, FortiGate 3500F Gen2, FortiGate 3501F Gen2, FortiGate 3600E,
FortiGate 3601E, FortiGate 3700F, FortiGate 3701F, FortiGate 3960E, FortiGate 3980E, FortiGate
400E Bypass, FortiGate 400E, FortiGate 400F, FortiGate 401E, FortiGate 401F, FortiGate 4200F,
FortiGate 4201F Gen2, FortiGate 4400F, FortiGate 4401F Gen2, FortiGate 4800F, FortiGate 4801F,
FortiGate 500E, FortiGate 501E, FortiGate 600E, FortiGate 600F, FortiGate 601E, FortiGate 601F,
FortiGate 70F, FortiGate 70G-POE, FortiGate 70G, FortiGate 71F, FortiGate 71G-POE, FortiGate 71G,
FortiGate 800D, FortiGate 80F Bypass, FortiGate 80F DSL, FortiGate 80F Gen2, FortiGate 80F-POE,
FortiGate 81F Gen2, FortiGate 81F-POE, FortiGate 900D, FortiGate 900G, FortiGate 901G, FortiGate
90G Gen2, FortiGate 90G, FortiGate 91G Gen2, FortiGate 91G, FortiGateRugged 70F 3G4G,
FortiGateRugged 70F, FortiGateRugged 70G 5G Dual, FortiGateRugged 70G, FortiWiFi 70G-POE,
FortiWiFi 70G, FortiWiFi 71G, FortiWiFi 80F 2R 3G4G DSL, FortiWiFi 80F 2R, FortiWiFi 81F 2R 3G4G
DSL, FortiWiFi 81F 2R 3G4G-POE, FortiWiFi 81F 2R-POE, FortiWiFi 81F 2R.
It is not available for: FortiGate 30G, FortiGate 31G, FortiGate 40F 3G4G, FortiGate 40F, FortiGate
50G 5G, FortiGate 50G DSL, FortiGate 50G SFP-POE, FortiGate 50G SFP, FortiGate 50G, FortiGate
51G 5G, FortiGate 51G SFP-POE, FortiGate 51G, FortiGate 60F, FortiGate 61F, FortiGate-VM64
Aliyun, FortiGate-VM64 AWS, FortiGate-VM64 Azure, FortiGate-VM64 GCP, FortiGate-VM64 OPC,
FortiGate-VM64, FortiGateRugged 50G 5G, FortiGateRugged 60F 3G4G, FortiGateRugged 60F
Gen2, FortiWiFi 30G, FortiWiFi 31G, FortiWiFi 40F 3G4G, FortiWiFi 40F, FortiWiFi 50G 5G, FortiWiFi
50G DSL, FortiWiFi 50G SFP, FortiWiFi 50G, FortiWiFi 51G, FortiWiFi 60F, FortiWiFi 61F.
Configure FortiTelemetry global settings.
config telemetry-controller global
Description: Configure FortiTelemetry global settings.
set auto-group-telemetry-addr [enable|disable]
FortiOS 8.0.0 CLI Reference
2217
Fortinet Inc.

<!-- 来源页 2218 -->
set region {option}
set retry-interval {integer}
set telemetry-ca-certificate {string}
end
config telemetry-controller global
Parameter
Description
Type
Size
Default
auto-group-telemetry-addr
Enable/disable automatically adding the telemetry
address to the default addrgrp TELEMETRY.
option
-enable
Option
Description
enable
Automatically add telemetry address to the default addrgrp
TELEMETRY.
disable
Do not automatically add telemetry address to the default addrgrp
TELEMETRY.
region
Configure telemetry cloud region.
option
-global
Option
Description
global
Set region to gloabl.
retry-interval
Configure telemetry cloud retry interval (1 - 999,
default = 60).
integer
Minimum
value: 1
Maximum
value: 999
60
telemetry-ca-certificate
Name of the CA certificate used to verify the
telemetry agent certificate.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
2218
Fortinet Inc.

<!-- 来源页 2219 -->
config telemetry-controller profile
This command is available for model(s): FortiGate 1000D, FortiGate 1000F, FortiGate 1001F,
FortiGate 100F, FortiGate 101F Gen2, FortiGate 1100E, FortiGate 1101E, FortiGate 120G, FortiGate
121G, FortiGate 1800F, FortiGate 1801F, FortiGate 2000E, FortiGate 200E, FortiGate 200F, FortiGate
200G, FortiGate 201E, FortiGate 201F, FortiGate 201G, FortiGate 2200E, FortiGate 2201E, FortiGate
2500E, FortiGate 2600F, FortiGate 2601F, FortiGate 3000F, FortiGate 3001F, FortiGate 300E,
FortiGate 301E, FortiGate 3200F, FortiGate 3201F Gen2, FortiGate 3300E, FortiGate 3301E,
FortiGate 3400E, FortiGate 3401E, FortiGate 3500F Gen2, FortiGate 3501F Gen2, FortiGate 3600E,
FortiGate 3601E, FortiGate 3700F, FortiGate 3701F, FortiGate 3960E, FortiGate 3980E, FortiGate
400E Bypass, FortiGate 400E, FortiGate 400F, FortiGate 401E, FortiGate 401F, FortiGate 4200F,
FortiGate 4201F Gen2, FortiGate 4400F, FortiGate 4401F Gen2, FortiGate 4800F, FortiGate 4801F,
FortiGate 500E, FortiGate 501E, FortiGate 600E, FortiGate 600F, FortiGate 601E, FortiGate 601F,
FortiGate 70F, FortiGate 70G-POE, FortiGate 70G, FortiGate 71F, FortiGate 71G-POE, FortiGate 71G,
FortiGate 800D, FortiGate 80F Bypass, FortiGate 80F DSL, FortiGate 80F Gen2, FortiGate 80F-POE,
FortiGate 81F Gen2, FortiGate 81F-POE, FortiGate 900D, FortiGate 900G, FortiGate 901G, FortiGate
90G Gen2, FortiGate 90G, FortiGate 91G Gen2, FortiGate 91G, FortiGateRugged 70F 3G4G,
FortiGateRugged 70F, FortiGateRugged 70G 5G Dual, FortiGateRugged 70G, FortiWiFi 70G-POE,
FortiWiFi 70G, FortiWiFi 71G, FortiWiFi 80F 2R 3G4G DSL, FortiWiFi 80F 2R, FortiWiFi 81F 2R 3G4G
DSL, FortiWiFi 81F 2R 3G4G-POE, FortiWiFi 81F 2R-POE, FortiWiFi 81F 2R.
It is not available for: FortiGate 30G, FortiGate 31G, FortiGate 40F 3G4G, FortiGate 40F, FortiGate
50G 5G, FortiGate 50G DSL, FortiGate 50G SFP-POE, FortiGate 50G SFP, FortiGate 50G, FortiGate
51G 5G, FortiGate 51G SFP-POE, FortiGate 51G, FortiGate 60F, FortiGate 61F, FortiGate-VM64
Aliyun, FortiGate-VM64 AWS, FortiGate-VM64 Azure, FortiGate-VM64 GCP, FortiGate-VM64 OPC,
FortiGate-VM64, FortiGateRugged 50G 5G, FortiGateRugged 60F 3G4G, FortiGateRugged 60F
Gen2, FortiWiFi 30G, FortiWiFi 31G, FortiWiFi 40F 3G4G, FortiWiFi 40F, FortiWiFi 50G 5G, FortiWiFi
50G DSL, FortiWiFi 50G SFP, FortiWiFi 50G, FortiWiFi 51G, FortiWiFi 60F, FortiWiFi 61F.
Configure FortiTelemetry profiles.
config telemetry-controller profile
Description: Configure FortiTelemetry profiles.
edit <name>
config application
Description: Configure applications.
edit <id>
set app-name {string}
set interval {integer}
set monitor [enable|disable]
config sla
Description: Service level agreement (SLA).
set app-throughput-threshold {integer}
set atdt-threshold {integer}
set dns-time-threshold {integer}
set experience-score-threshold {integer}
set failure-rate-threshold {integer}
set jitter-threshold {integer}
set latency-threshold {integer}
set packet-loss-threshold {integer}
FortiOS 8.0.0 CLI Reference
2219
Fortinet Inc.

<!-- 来源页 2220 -->
set sla-factor {option1}, {option2}, ...
set tcp-rtt-threshold {integer}
set tls-time-threshold {integer}
set ttfb-threshold {integer}
end
next
end
set comment {var-string}
next
end
config telemetry-controller profile
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
Name of the profile.
string
Maximum
length: 35
config application
Parameter
Description
Type
Size
Default
app-name
Application name.
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
interval
Time in milliseconds to check the application (60
* 1000 - 86,400 * 1000, default = 300 * 1000
ms).
integer
Minimum value:
60000
Maximum
value:
86400000
300000
monitor
Enable/disable monitoring of the application.
option
-enable
Option
Description
enable
Enable monitoring of the application.
disable
Disable monitoring of the application.
FortiOS 8.0.0 CLI Reference
2220
Fortinet Inc.

<!-- 来源页 2221 -->
config sla
Parameter
Description
Type
Size
Default
app-throughput-threshold
Threshold of application throughput in megabytes
(0 - 10,000, default = 2 MB).
integer
Minimum
value: 0
Maximum
value:
10000
2
atdt-threshold
Threshold of application total downloading time in
milliseconds (0 - 10,000,000, default = 3,000 ms).
integer
Minimum
value: 0
Maximum
value:
10000000
3000
dns-time-threshold
Threshold of 95th percentile of DNS resolution
time in milliseconds (0 - 10,000,000, default = 100
ms).
integer
Minimum
value: 0
Maximum
value:
10000000
100
experience-score-threshold
Threshold of experience score (0 - 10, default =
6).
integer
Minimum
value: 0
Maximum
value: 10
6
failure-rate-threshold
Threshold of failure rate (0 - 100, default = 5
percentage).
integer
Minimum
value: 0
Maximum
value: 100
5
jitter-threshold
Threshold of jitter in milliseconds (0 - 10,000,000,
default = 50 ms).
integer
Minimum
value: 0
Maximum
value:
10000000
50
latency-threshold
Threshold of latency in milliseconds (0 -10,000,000, default = 100 ms).
integer
Minimum
value: 0
Maximum
value:
10000000
100
packet-loss-threshold
Threshold of packet loss (0 - 100, default = 5
percentage).
integer
Minimum
value: 0
Maximum
value: 100
5
sla-factor
Criteria on which metric to SLA threshold list.
option
-FortiOS 8.0.0 CLI Reference
2221
Fortinet Inc.

<!-- 来源页 2222 -->
Parameter
Description
Type
Size
Default
Option
Description
experience-score
Select SLA target based on experience score.
failure-rate
Select SLA target based on failure rate.
latency
Select SLA target based on latency.
jitter
Select SLA target based on jitter.
packet-loss
Select SLA target based on packet loss.
ttfb
Select SLA target based on time to first byte.
atdt
Select SLA target based on application total downloading time.
tcp-rtt
Select SLA target based on TCP round-trip time.
dns-time
Select SLA target based on DNS resolution time.
tls-time
Select SLA target based on TLS handshake time.
app-throughput
Select SLA target based on application throughput.
tcp-rtt-threshold
Threshold of TCP round-trip time in milliseconds
(0 - 10,000,000, default = 100 ms).
integer
Minimum
value: 0
Maximum
value:
10000000
100
tls-time-threshold
Threshold of 95th percentile of TLS handshake
time in milliseconds (0 - 10,000,000, default = 200
ms).
integer
Minimum
value: 0
Maximum
value:
10000000
200
ttfb-threshold
Threshold of time to first byte in milliseconds (0 -10,000,000, default = 200 ms).
integer
Minimum
value: 0
Maximum
value:
10000000
200
FortiOS 8.0.0 CLI Reference
2222
Fortinet Inc.

---


<!-- 来源页 2568 -->
wanopt
This section includes syntax for the following commands:
l config wanopt auth-group on page 2568
l config wanopt cache-service on page 2570
l config wanopt content-delivery-network-rule on page 2573
l config wanopt peer on page 2579
l config wanopt profile on page 2580
l config wanopt remote-storage on page 2589
l config wanopt settings on page 2590
l config wanopt webcache on page 2592
config wanopt auth-group
This command is available for model(s): FortiGate 1000D, FortiGate 1001F, FortiGate 101F Gen2,
FortiGate 1101E, FortiGate 121G, FortiGate 1801F, FortiGate 2000E, FortiGate 201E, FortiGate 201F,
FortiGate 201G, FortiGate 2201E, FortiGate 2500E, FortiGate 2600F, FortiGate 2601F, FortiGate
3001F, FortiGate 301E, FortiGate 3201F Gen2, FortiGate 3301E, FortiGate 3401E, FortiGate 3501F
Gen2, FortiGate 3601E, FortiGate 3701F, FortiGate 401E, FortiGate 401F, FortiGate 4201F Gen2,
FortiGate 4401F Gen2, FortiGate 4801F, FortiGate 501E, FortiGate 601E, FortiGate 601F, FortiGate
71F, FortiGate 71G-POE, FortiGate 71G, FortiGate 800D, FortiGate 81F Gen2, FortiGate 81F-POE,
FortiGate 900D, FortiGate 901G, FortiGate 91G Gen2, FortiGate 91G, FortiGate-VM64 Aliyun,
FortiGate-VM64 AWS, FortiGate-VM64 Azure, FortiGate-VM64 GCP, FortiGate-VM64 OPC,
FortiGate-VM64, FortiGateRugged 70F 3G4G, FortiGateRugged 70F, FortiGateRugged 70G 5G Dual,
FortiGateRugged 70G, FortiWiFi 71G, FortiWiFi 80F 2R 3G4G DSL, FortiWiFi 81F 2R 3G4G DSL,
FortiWiFi 81F 2R 3G4G-POE, FortiWiFi 81F 2R-POE, FortiWiFi 81F 2R.
It is not available for: FortiGate 1000F, FortiGate 100F, FortiGate 1100E, FortiGate 120G, FortiGate
1800F, FortiGate 200E, FortiGate 200F, FortiGate 200G, FortiGate 2200E, FortiGate 3000F,
FortiGate 300E, FortiGate 30G, FortiGate 31G, FortiGate 3200F, FortiGate 3300E, FortiGate 3400E,
FortiGate 3500F Gen2, FortiGate 3600E, FortiGate 3700F, FortiGate 3960E, FortiGate 3980E,
FortiGate 400E Bypass, FortiGate 400E, FortiGate 400F, FortiGate 40F 3G4G, FortiGate 40F,
FortiGate 4200F, FortiGate 4400F, FortiGate 4800F, FortiGate 500E, FortiGate 50G 5G, FortiGate
50G DSL, FortiGate 50G SFP-POE, FortiGate 50G SFP, FortiGate 50G, FortiGate 51G 5G, FortiGate
51G SFP-POE, FortiGate 51G, FortiGate 600E, FortiGate 600F, FortiGate 60F, FortiGate 61F,
FortiGate 70F, FortiGate 70G-POE, FortiGate 70G, FortiGate 80F Bypass, FortiGate 80F DSL,
FortiGate 80F Gen2, FortiGate 80F-POE, FortiGate 900G, FortiGate 90G Gen2, FortiGate 90G,
FortiGateRugged 50G 5G, FortiGateRugged 60F 3G4G, FortiGateRugged 60F Gen2, FortiWiFi 30G,
FortiWiFi 31G, FortiWiFi 40F 3G4G, FortiWiFi 40F, FortiWiFi 50G 5G, FortiWiFi 50G DSL, FortiWiFi 50G
SFP, FortiWiFi 50G, FortiWiFi 51G, FortiWiFi 60F, FortiWiFi 61F, FortiWiFi 70G-POE, FortiWiFi 70G,
FortiWiFi 80F 2R.
FortiOS 8.0.0 CLI Reference
2568
Fortinet Inc.

<!-- 来源页 2569 -->
Configure WAN optimization authentication groups.
config wanopt auth-group
Description: Configure WAN optimization authentication groups.
edit <name>
set auth-method [cert|psk]
set cert {string}
set peer {string}
set peer-accept [any|defined|...]
set psk {password}
next
end
config wanopt auth-group
Parameter
Description
Type
Size
Default
auth-method
Select certificate or pre-shared key authentication
for this authentication group.
option
-cert
Option
Description
cert
Certificate authentication.
psk
Pre-shared secret key authentication.
cert
Name of certificate to identify this peer.
string
Maximum
length: 35
name
Auth-group name.
string
Maximum
length: 35
peer
If peer-accept is set to one, select the name of
one peer to add to this authentication group. The
peer must have added with the wanopt peer
command.
string
Maximum
length: 35
peer-accept
Determine if this auth group accepts, any peer, a
list of defined peers, or just one peer.
option
-any
Option
Description
any
Accept any peer that can authenticate with this auth group.
defined
Accept only the peers added with the wanopt peer command.
one
Accept the peer added to this auth group using the peer option.
psk
Pre-shared key used by the peers in this
authentication group.
password
Not
Specified
FortiOS 8.0.0 CLI Reference
2569
Fortinet Inc.

<!-- 来源页 2570 -->
config wanopt cache-service
This command is available for model(s): FortiGate 1000D, FortiGate 1001F, FortiGate 101F Gen2,
FortiGate 1101E, FortiGate 121G, FortiGate 1801F, FortiGate 2000E, FortiGate 201E, FortiGate 201F,
FortiGate 201G, FortiGate 2201E, FortiGate 2500E, FortiGate 2600F, FortiGate 2601F, FortiGate
3001F, FortiGate 301E, FortiGate 3201F Gen2, FortiGate 3301E, FortiGate 3401E, FortiGate 3501F
Gen2, FortiGate 3601E, FortiGate 3701F, FortiGate 401E, FortiGate 401F, FortiGate 4201F Gen2,
FortiGate 4401F Gen2, FortiGate 4801F, FortiGate 501E, FortiGate 601E, FortiGate 601F, FortiGate
71F, FortiGate 71G-POE, FortiGate 71G, FortiGate 800D, FortiGate 81F Gen2, FortiGate 81F-POE,
FortiGate 900D, FortiGate 901G, FortiGate 91G Gen2, FortiGate 91G, FortiGate-VM64 Aliyun,
FortiGate-VM64 AWS, FortiGate-VM64 Azure, FortiGate-VM64 GCP, FortiGate-VM64 OPC,
FortiGate-VM64, FortiGateRugged 70F 3G4G, FortiGateRugged 70F, FortiGateRugged 70G 5G Dual,
FortiGateRugged 70G, FortiWiFi 71G, FortiWiFi 80F 2R 3G4G DSL, FortiWiFi 81F 2R 3G4G DSL,
FortiWiFi 81F 2R 3G4G-POE, FortiWiFi 81F 2R-POE, FortiWiFi 81F 2R.
It is not available for: FortiGate 1000F, FortiGate 100F, FortiGate 1100E, FortiGate 120G, FortiGate
1800F, FortiGate 200E, FortiGate 200F, FortiGate 200G, FortiGate 2200E, FortiGate 3000F,
FortiGate 300E, FortiGate 30G, FortiGate 31G, FortiGate 3200F, FortiGate 3300E, FortiGate 3400E,
FortiGate 3500F Gen2, FortiGate 3600E, FortiGate 3700F, FortiGate 3960E, FortiGate 3980E,
FortiGate 400E Bypass, FortiGate 400E, FortiGate 400F, FortiGate 40F 3G4G, FortiGate 40F,
FortiGate 4200F, FortiGate 4400F, FortiGate 4800F, FortiGate 500E, FortiGate 50G 5G, FortiGate
50G DSL, FortiGate 50G SFP-POE, FortiGate 50G SFP, FortiGate 50G, FortiGate 51G 5G, FortiGate
51G SFP-POE, FortiGate 51G, FortiGate 600E, FortiGate 600F, FortiGate 60F, FortiGate 61F,
FortiGate 70F, FortiGate 70G-POE, FortiGate 70G, FortiGate 80F Bypass, FortiGate 80F DSL,
FortiGate 80F Gen2, FortiGate 80F-POE, FortiGate 900G, FortiGate 90G Gen2, FortiGate 90G,
FortiGateRugged 50G 5G, FortiGateRugged 60F 3G4G, FortiGateRugged 60F Gen2, FortiWiFi 30G,
FortiWiFi 31G, FortiWiFi 40F 3G4G, FortiWiFi 40F, FortiWiFi 50G 5G, FortiWiFi 50G DSL, FortiWiFi 50G
SFP, FortiWiFi 50G, FortiWiFi 51G, FortiWiFi 60F, FortiWiFi 61F, FortiWiFi 70G-POE, FortiWiFi 70G,
FortiWiFi 80F 2R.
Designate cache-service for wan-optimization and webcache.
config wanopt cache-service
Description: Designate cache-service for wan-optimization and webcache.
set acceptable-connections [any|peers]
set collaboration [enable|disable]
set device-id {string}
config dst-peer
Description: Modify cache-service destination peer list.
edit <device-id>
set auth-type {integer}
set encode-type {integer}
set ip {ipv4-address-any}
set priority {integer}
next
end
set prefer-scenario [balance|prefer-speed|...]
config src-peer
Description: Modify cache-service source peer list.
edit <device-id>
FortiOS 8.0.0 CLI Reference
2570
Fortinet Inc.

<!-- 来源页 2571 -->
set auth-type {integer}
set encode-type {integer}
set ip {ipv4-address-any}
set priority {integer}
next
end
end
config wanopt cache-service
Parameter
Description
Type
Size
Default
acceptable-connections
Set strategy when accepting cache collaboration
connection.
option
-any
Option
Description
any
We can accept any cache-collaboration connection.
peers
We can only accept connections that are already in src-peers.
collaboration
Enable/disable cache-collaboration between
cache-service clusters.
option
-disable
Option
Description
enable
Enable cache cache-collaboration.
disable
Disable cache cache-collaboration.
device-id
Set identifier for this cache device.
string
Maximum
length: 35
default_
dev_id
prefer-scenario
Set the preferred cache behavior towards the
balance between latency and hit-ratio.
option
-balance
Option
Description
balance
Balance between speed and cache hit ratio.
prefer-speed
Prefer response speed at the expense of increased cache bypasses.
prefer-cache
Prefer improving hit-ratio through increasing latency tolerance.
FortiOS 8.0.0 CLI Reference
2571
Fortinet Inc.

<!-- 来源页 2572 -->
config dst-peer
Parameter
Description
Type
Size
Default
auth-type
Set authentication type for this peer.
integer
Minimum
value: 0
Maximum
value: 255
0
device-id
Device ID of this peer.
string
Maximum
length: 35
encode-type
Set encode type for this peer.
integer
Minimum
value: 0
Maximum
value: 255
0
ip
Set cluster IP address of this peer.
ipv4-address-any
Not
Specified
0.0.0.0
priority
Set priority for this peer.
integer
Minimum
value: 0
Maximum
value: 255
1
config src-peer
Parameter
Description
Type
Size
Default
auth-type
Set authentication type for this peer.
integer
Minimum
value: 0
Maximum
value: 255
0
device-id
Device ID of this peer.
string
Maximum
length: 35
encode-type
Set encode type for this peer.
integer
Minimum
value: 0
Maximum
value: 255
0
ip
Set cluster IP address of this peer.
ipv4-address-any
Not
Specified
0.0.0.0
priority
Set priority for this peer.
integer
Minimum
value: 0
Maximum
value: 255
1
FortiOS 8.0.0 CLI Reference
2572
Fortinet Inc.

<!-- 来源页 2573 -->
config wanopt content-delivery-network-rule
This command is available for model(s): FortiGate 1000D, FortiGate 1001F, FortiGate 101F Gen2,
FortiGate 1101E, FortiGate 121G, FortiGate 1801F, FortiGate 2000E, FortiGate 201E, FortiGate 201F,
FortiGate 201G, FortiGate 2201E, FortiGate 2500E, FortiGate 2600F, FortiGate 2601F, FortiGate
3001F, FortiGate 301E, FortiGate 3201F Gen2, FortiGate 3301E, FortiGate 3401E, FortiGate 3501F
Gen2, FortiGate 3601E, FortiGate 3701F, FortiGate 401E, FortiGate 401F, FortiGate 4201F Gen2,
FortiGate 4401F Gen2, FortiGate 4801F, FortiGate 501E, FortiGate 601E, FortiGate 601F, FortiGate
71F, FortiGate 71G-POE, FortiGate 71G, FortiGate 800D, FortiGate 81F Gen2, FortiGate 81F-POE,
FortiGate 900D, FortiGate 901G, FortiGate 91G Gen2, FortiGate 91G, FortiGate-VM64 Aliyun,
FortiGate-VM64 AWS, FortiGate-VM64 Azure, FortiGate-VM64 GCP, FortiGate-VM64 OPC,
FortiGate-VM64, FortiGateRugged 70F 3G4G, FortiGateRugged 70F, FortiGateRugged 70G 5G Dual,
FortiGateRugged 70G, FortiWiFi 71G, FortiWiFi 80F 2R 3G4G DSL, FortiWiFi 81F 2R 3G4G DSL,
FortiWiFi 81F 2R 3G4G-POE, FortiWiFi 81F 2R-POE, FortiWiFi 81F 2R.
It is not available for: FortiGate 1000F, FortiGate 100F, FortiGate 1100E, FortiGate 120G, FortiGate
1800F, FortiGate 200E, FortiGate 200F, FortiGate 200G, FortiGate 2200E, FortiGate 3000F,
FortiGate 300E, FortiGate 30G, FortiGate 31G, FortiGate 3200F, FortiGate 3300E, FortiGate 3400E,
FortiGate 3500F Gen2, FortiGate 3600E, FortiGate 3700F, FortiGate 3960E, FortiGate 3980E,
FortiGate 400E Bypass, FortiGate 400E, FortiGate 400F, FortiGate 40F 3G4G, FortiGate 40F,
FortiGate 4200F, FortiGate 4400F, FortiGate 4800F, FortiGate 500E, FortiGate 50G 5G, FortiGate
50G DSL, FortiGate 50G SFP-POE, FortiGate 50G SFP, FortiGate 50G, FortiGate 51G 5G, FortiGate
51G SFP-POE, FortiGate 51G, FortiGate 600E, FortiGate 600F, FortiGate 60F, FortiGate 61F,
FortiGate 70F, FortiGate 70G-POE, FortiGate 70G, FortiGate 80F Bypass, FortiGate 80F DSL,
FortiGate 80F Gen2, FortiGate 80F-POE, FortiGate 900G, FortiGate 90G Gen2, FortiGate 90G,
FortiGateRugged 50G 5G, FortiGateRugged 60F 3G4G, FortiGateRugged 60F Gen2, FortiWiFi 30G,
FortiWiFi 31G, FortiWiFi 40F 3G4G, FortiWiFi 40F, FortiWiFi 50G 5G, FortiWiFi 50G DSL, FortiWiFi 50G
SFP, FortiWiFi 50G, FortiWiFi 51G, FortiWiFi 60F, FortiWiFi 61F, FortiWiFi 70G-POE, FortiWiFi 70G,
FortiWiFi 80F 2R.
Configure WAN optimization content delivery network rules.
config wanopt content-delivery-network-rule
Description: Configure WAN optimization content delivery network rules.
edit <name>
set category [vcache|youtube]
set comment {var-string}
set host-domain-name-suffix <name1>, <name2>, ...
set request-cache-control [enable|disable]
set response-cache-control [enable|disable]
set response-expires [enable|disable]
config rules
Description: WAN optimization content delivery network rule entries.
edit <name>
config content-id
Description: Content ID settings.
set end-direction [forward|backward]
set end-skip {integer}
set end-str {string}
set range-str {string}
FortiOS 8.0.0 CLI Reference
2573
Fortinet Inc.

<!-- 来源页 2574 -->
set start-direction [forward|backward]
set start-skip {integer}
set start-str {string}
set target [path|parameter|...]
end
config match-entries
Description: List of entries to match.
edit <id>
set pattern <string1>, <string2>, ...
set target [path|parameter|...]
next
end
set match-mode [all|any]
config skip-entries
Description: List of entries to skip.
edit <id>
set pattern <string1>, <string2>, ...
set target [path|parameter|...]
next
end
set skip-rule-mode [all|any]
next
end
set status [enable|disable]
set updateserver [enable|disable]
next
end
config wanopt content-delivery-network-rule
Parameter
Description
Type
Size
Default
category
Content delivery network rule category.
option
-vcache
Option
Description
vcache
Vcache content delivery network.
youtube
Youtube content delivery network.
comment
Comment about this CDN-rule.
var-string
Maximum
length: 255
host-domain-name-suffix
<name>
Suffix portion of the fully qualified domain name.
For example, fortinet.com in "www.fortinet.com".
Suffix portion of the fully qualified domain name.
string
Maximum
length: 79
name
Name of table.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
2574
Fortinet Inc.

<!-- 来源页 2575 -->
Parameter
Description
Type
Size
Default
request-cache-control
Enable/disable HTTP request cache control.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
response-cache-control
Enable/disable HTTP response cache control.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
response-expires
Enable/disable HTTP response cache expires.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
status
Enable/disable WAN optimization content
delivery network rules.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
updateserver
Enable/disable update server.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
config rules
Parameter
Description
Type
Size
Default
match-mode
Match criteria for collecting content ID.
option
-all
FortiOS 8.0.0 CLI Reference
2575
Fortinet Inc.

<!-- 来源页 2576 -->
Parameter
Description
Type
Size
Default
Option
Description
all
Must match all of the match entries.
any
Must match any of the match entries.
name
WAN optimization content delivery network rule
name.
string
Maximum
length: 35
skip-rule-mode
Skip mode when evaluating skip-rules.
option
-all
Option
Description
all
Must match all skip entries.
any
Must match any skip entries.
config content-id
Parameter
Description
Type
Size
Default
end-direction
Search direction from end-str match.
option
-forward
Option
Description
forward
Forward direction.
backward
Backward direction.
end-skip
Number of characters in URL to skip after end-str has been matched.
integer
Minimum value:
0 Maximum
value:
4294967295
0
end-str
String from which to end search.
string
Maximum
length: 35
range-str
Name of content ID within the start string and
end string.
string
Maximum
length: 35
start-direction
Search direction from start-str match.
option
-forward
Option
Description
forward
Forward direction.
backward
Backward direction.
FortiOS 8.0.0 CLI Reference
2576
Fortinet Inc.

<!-- 来源页 2577 -->
Parameter
Description
Type
Size
Default
start-skip
Number of characters in URL to skip after start-str has been matched.
integer
Minimum value:
0 Maximum
value:
4294967295
0
start-str
String from which to start search.
string
Maximum
length: 35
/
target
Option in HTTP header or URL parameter to
match.
option
-path
Option
Description
path
Match with the URL path.
parameter
Match with the URL parameters.
referrer
Match with the Referrer option in HTTP header.
youtube-map
Match Youtube content-id collection.
youtube-id
Match Youtube content-id.
youku-id
Match Youku content-id.
hls-manifest
Match with HLS manifest.
dash-manifest
Match with DASH manifest.
hls-fragment
Match HLS stream fragment.
dash-fragment
Match DASH stream fragment.
config match-entries
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
pattern
<string>
Pattern string for matching target (Referrer or
URL pattern). For example, a, a*c, *a*, a*c*e,
and *.
Pattern strings.
string
Maximum
length: 79
target
Option in HTTP header or URL parameter to
match.
option
-path
Option
Description
path
Match with the URL path.
FortiOS 8.0.0 CLI Reference
2577
Fortinet Inc.

<!-- 来源页 2578 -->
Parameter
Description
Type
Size
Default
Option
Description
parameter
Match with the URL parameters.
referrer
Match with the Referrer option in HTTP header.
youtube-map
Match Youtube content-id collection.
youtube-id
Match Youtube content-id.
youku-id
Match Youku content-id.
config skip-entries
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
pattern
<string>
Pattern string for matching target (Referrer or
URL pattern). For example, a, a*c, *a*, a*c*e,
and *.
Pattern strings.
string
Maximum
length: 79
target
Option in HTTP header or URL parameter to
match.
option
-path
Option
Description
path
Match with the URL path.
parameter
Match with the URL parameters.
referrer
Match with the Referrer option in HTTP header.
youtube-map
Match Youtube content-id collection.
youtube-id
Match Youtube content-id.
youku-id
Match Youku content-id.
FortiOS 8.0.0 CLI Reference
2578
Fortinet Inc.

<!-- 来源页 2579 -->
config wanopt peer
This command is available for model(s): FortiGate 1000D, FortiGate 1001F, FortiGate 101F Gen2,
FortiGate 1101E, FortiGate 121G, FortiGate 1801F, FortiGate 2000E, FortiGate 201E, FortiGate 201F,
FortiGate 201G, FortiGate 2201E, FortiGate 2500E, FortiGate 2600F, FortiGate 2601F, FortiGate
3001F, FortiGate 301E, FortiGate 3201F Gen2, FortiGate 3301E, FortiGate 3401E, FortiGate 3501F
Gen2, FortiGate 3601E, FortiGate 3701F, FortiGate 401E, FortiGate 401F, FortiGate 4201F Gen2,
FortiGate 4401F Gen2, FortiGate 4801F, FortiGate 501E, FortiGate 601E, FortiGate 601F, FortiGate
71F, FortiGate 71G-POE, FortiGate 71G, FortiGate 800D, FortiGate 81F Gen2, FortiGate 81F-POE,
FortiGate 900D, FortiGate 901G, FortiGate 91G Gen2, FortiGate 91G, FortiGate-VM64 Aliyun,
FortiGate-VM64 AWS, FortiGate-VM64 Azure, FortiGate-VM64 GCP, FortiGate-VM64 OPC,
FortiGate-VM64, FortiGateRugged 70F 3G4G, FortiGateRugged 70F, FortiGateRugged 70G 5G Dual,
FortiGateRugged 70G, FortiWiFi 71G, FortiWiFi 80F 2R 3G4G DSL, FortiWiFi 81F 2R 3G4G DSL,
FortiWiFi 81F 2R 3G4G-POE, FortiWiFi 81F 2R-POE, FortiWiFi 81F 2R.
It is not available for: FortiGate 1000F, FortiGate 100F, FortiGate 1100E, FortiGate 120G, FortiGate
1800F, FortiGate 200E, FortiGate 200F, FortiGate 200G, FortiGate 2200E, FortiGate 3000F,
FortiGate 300E, FortiGate 30G, FortiGate 31G, FortiGate 3200F, FortiGate 3300E, FortiGate 3400E,
FortiGate 3500F Gen2, FortiGate 3600E, FortiGate 3700F, FortiGate 3960E, FortiGate 3980E,
FortiGate 400E Bypass, FortiGate 400E, FortiGate 400F, FortiGate 40F 3G4G, FortiGate 40F,
FortiGate 4200F, FortiGate 4400F, FortiGate 4800F, FortiGate 500E, FortiGate 50G 5G, FortiGate
50G DSL, FortiGate 50G SFP-POE, FortiGate 50G SFP, FortiGate 50G, FortiGate 51G 5G, FortiGate
51G SFP-POE, FortiGate 51G, FortiGate 600E, FortiGate 600F, FortiGate 60F, FortiGate 61F,
FortiGate 70F, FortiGate 70G-POE, FortiGate 70G, FortiGate 80F Bypass, FortiGate 80F DSL,
FortiGate 80F Gen2, FortiGate 80F-POE, FortiGate 900G, FortiGate 90G Gen2, FortiGate 90G,
FortiGateRugged 50G 5G, FortiGateRugged 60F 3G4G, FortiGateRugged 60F Gen2, FortiWiFi 30G,
FortiWiFi 31G, FortiWiFi 40F 3G4G, FortiWiFi 40F, FortiWiFi 50G 5G, FortiWiFi 50G DSL, FortiWiFi 50G
SFP, FortiWiFi 50G, FortiWiFi 51G, FortiWiFi 60F, FortiWiFi 61F, FortiWiFi 70G-POE, FortiWiFi 70G,
FortiWiFi 80F 2R.
Configure WAN optimization peers.
config wanopt peer
Description: Configure WAN optimization peers.
edit <peer-host-id>
set ip {ipv4-address-any}
next
end
config wanopt peer
Parameter
Description
Type
Size
Default
ip
Peer IP address.
ipv4-address-any
Not
Specified
0.0.0.0
peer-host-id
Peer host ID.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
2579
Fortinet Inc.

<!-- 来源页 2580 -->
config wanopt profile
This command is available for model(s): FortiGate 1000D, FortiGate 1001F, FortiGate 101F Gen2,
FortiGate 1101E, FortiGate 121G, FortiGate 1801F, FortiGate 2000E, FortiGate 201E, FortiGate 201F,
FortiGate 201G, FortiGate 2201E, FortiGate 2500E, FortiGate 2600F, FortiGate 2601F, FortiGate
3001F, FortiGate 301E, FortiGate 3201F Gen2, FortiGate 3301E, FortiGate 3401E, FortiGate 3501F
Gen2, FortiGate 3601E, FortiGate 3701F, FortiGate 401E, FortiGate 401F, FortiGate 4201F Gen2,
FortiGate 4401F Gen2, FortiGate 4801F, FortiGate 501E, FortiGate 601E, FortiGate 601F, FortiGate
71F, FortiGate 71G-POE, FortiGate 71G, FortiGate 800D, FortiGate 81F Gen2, FortiGate 81F-POE,
FortiGate 900D, FortiGate 901G, FortiGate 91G Gen2, FortiGate 91G, FortiGate-VM64 Aliyun,
FortiGate-VM64 AWS, FortiGate-VM64 Azure, FortiGate-VM64 GCP, FortiGate-VM64 OPC,
FortiGate-VM64, FortiGateRugged 70F 3G4G, FortiGateRugged 70F, FortiGateRugged 70G 5G Dual,
FortiGateRugged 70G, FortiWiFi 71G, FortiWiFi 80F 2R 3G4G DSL, FortiWiFi 81F 2R 3G4G DSL,
FortiWiFi 81F 2R 3G4G-POE, FortiWiFi 81F 2R-POE, FortiWiFi 81F 2R.
It is not available for: FortiGate 1000F, FortiGate 100F, FortiGate 1100E, FortiGate 120G, FortiGate
1800F, FortiGate 200E, FortiGate 200F, FortiGate 200G, FortiGate 2200E, FortiGate 3000F,
FortiGate 300E, FortiGate 30G, FortiGate 31G, FortiGate 3200F, FortiGate 3300E, FortiGate 3400E,
FortiGate 3500F Gen2, FortiGate 3600E, FortiGate 3700F, FortiGate 3960E, FortiGate 3980E,
FortiGate 400E Bypass, FortiGate 400E, FortiGate 400F, FortiGate 40F 3G4G, FortiGate 40F,
FortiGate 4200F, FortiGate 4400F, FortiGate 4800F, FortiGate 500E, FortiGate 50G 5G, FortiGate
50G DSL, FortiGate 50G SFP-POE, FortiGate 50G SFP, FortiGate 50G, FortiGate 51G 5G, FortiGate
51G SFP-POE, FortiGate 51G, FortiGate 600E, FortiGate 600F, FortiGate 60F, FortiGate 61F,
FortiGate 70F, FortiGate 70G-POE, FortiGate 70G, FortiGate 80F Bypass, FortiGate 80F DSL,
FortiGate 80F Gen2, FortiGate 80F-POE, FortiGate 900G, FortiGate 90G Gen2, FortiGate 90G,
FortiGateRugged 50G 5G, FortiGateRugged 60F 3G4G, FortiGateRugged 60F Gen2, FortiWiFi 30G,
FortiWiFi 31G, FortiWiFi 40F 3G4G, FortiWiFi 40F, FortiWiFi 50G 5G, FortiWiFi 50G DSL, FortiWiFi 50G
SFP, FortiWiFi 50G, FortiWiFi 51G, FortiWiFi 60F, FortiWiFi 61F, FortiWiFi 70G-POE, FortiWiFi 70G,
FortiWiFi 80F 2R.
Configure WAN optimization profiles.
config wanopt profile
Description: Configure WAN optimization profiles.
edit <name>
set auth-group {string}
config cifs
Description: Enable/disable CIFS (Windows sharing) WAN Optimization and configure CIFS
WAN Optimization features.
set byte-caching [enable|disable]
set prefer-chunking [dynamic|fix]
set protocol-opt [protocol|tcp]
set secure-tunnel [enable|disable]
set status [enable|disable]
set tunnel-sharing [shared|express-shared|...]
end
set comments {var-string}
config ftp
Description: Enable/disable FTP WAN Optimization and configure FTP WAN Optimization
features.
FortiOS 8.0.0 CLI Reference
2580
Fortinet Inc.

<!-- 来源页 2581 -->
set byte-caching [enable|disable]
set prefer-chunking [dynamic|fix]
set protocol-opt [protocol|tcp]
set secure-tunnel [enable|disable]
set status [enable|disable]
set tunnel-sharing [shared|express-shared|...]
end
config http
Description: Enable/disable HTTP WAN Optimization and configure HTTP WAN Optimization
features.
set byte-caching [enable|disable]
set prefer-chunking [dynamic|fix]
set protocol-opt [protocol|tcp]
set secure-tunnel [enable|disable]
set ssl [enable|disable]
set status [enable|disable]
set tunnel-sharing [shared|express-shared|...]
end
config mapi
Description: Enable/disable MAPI email WAN Optimization and configure MAPI WAN
Optimization features.
set byte-caching [enable|disable]
set secure-tunnel [enable|disable]
set status [enable|disable]
set tunnel-sharing [shared|express-shared|...]
end
config tcp
Description: Enable/disable TCP WAN Optimization and configure TCP WAN Optimization
features.
set byte-caching [enable|disable]
set byte-caching-opt [mem-only|mem-disk]
set port {user}
set secure-tunnel [enable|disable]
set ssl [enable|disable]
set ssl-port {user}
set status [enable|disable]
set tunnel-sharing [shared|express-shared|...]
end
set transparent [enable|disable]
next
end
config wanopt profile
Parameter
Description
Type
Size
Default
auth-group
Optionally add an authentication group to restrict
access to the WAN Optimization tunnel to peers in
the authentication group.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
2581
Fortinet Inc.

<!-- 来源页 2582 -->
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
name
Profile name.
string
Maximum
length: 35
transparent
Enable/disable transparent mode.
option
-enable
Option
Description
enable
Determine if WAN Optimization changes client packet source
addresses. Affects the routing configuration on the server network.
disable
Disable transparent mode. Client packets source addresses are
changed to the source address of the FortiGate internal interface.
Similar to source NAT.
config cifs
Parameter
Description
Type
Size
Default
byte-caching
Enable/disable byte-caching. Byte caching reduces
the amount of traffic by caching file data sent
across the WAN and in future serving if from the
cache.
option
-enable
Option
Description
enable
Enable byte-caching.
disable
Disable byte-caching.
prefer-chunking
Select dynamic or fixed-size data chunking for
WAN Optimization.
option
-fix
Option
Description
dynamic
Select dynamic data chunking to help to detect persistent data chunks
in a changed file or in an embedded unknown protocol.
fix
Select fixed data chunking.
protocol-opt
Select protocol specific optimization or generic
TCP optimization.
option
-protocol
Option
Description
protocol
Using protocol-specific optimization.
tcp
Using generic TCP optimization.
FortiOS 8.0.0 CLI Reference
2582
Fortinet Inc.

<!-- 来源页 2583 -->
Parameter
Description
Type
Size
Default
secure-tunnel
Enable/disable securing the WAN Opt tunnel using
SSL. Secure and non-secure tunnels use the same
TCP port (7810).
option
-disable
Option
Description
enable
Enable SSL-secured tunnelling.
disable
Disable SSL-secured tunnelling.
status
Enable/disable WAN Optimization.
option
-disable
Option
Description
enable
Enable WAN Optimization.
disable
Disable WAN Optimization.
tunnel-sharing
Tunnel sharing mode for aggressive/non-aggressive and/or interactive/non-interactive
protocols.
option
-private
Option
Description
shared
For profiles that accept nonaggressive and non-interactive protocols.
express-shared
For profiles that accept interactive protocols such as Telnet.
private
For profiles that accept aggressive protocols such as HTTP and FTP so
that these aggressive protocols do not share tunnels with less-aggressive protocols.
config ftp
Parameter
Description
Type
Size
Default
byte-caching
Enable/disable byte-caching. Byte caching reduces
the amount of traffic by caching file data sent
across the WAN and in future serving if from the
cache.
option
-enable
Option
Description
enable
Enable byte-caching.
disable
Disable byte-caching.
prefer-chunking
Select dynamic or fixed-size data chunking for
WAN Optimization.
option
-fix
FortiOS 8.0.0 CLI Reference
2583
Fortinet Inc.

<!-- 来源页 2584 -->
Parameter
Description
Type
Size
Default
Option
Description
dynamic
Select dynamic data chunking to help to detect persistent data chunks
in a changed file or in an embedded unknown protocol.
fix
Select fixed data chunking.
protocol-opt
Select protocol specific optimization or generic
TCP optimization.
option
-protocol
Option
Description
protocol
Using protocol-specific optimization.
tcp
Using generic TCP optimization.
secure-tunnel
Enable/disable securing the WAN Opt tunnel using
SSL. Secure and non-secure tunnels use the same
TCP port (7810).
option
-disable
Option
Description
enable
Enable SSL-secured tunnelling.
disable
Disable SSL-secured tunnelling.
status
Enable/disable WAN Optimization.
option
-disable
Option
Description
enable
Enable WAN Optimization.
disable
Disable WAN Optimization.
tunnel-sharing
Tunnel sharing mode for aggressive/non-aggressive and/or interactive/non-interactive
protocols.
option
-private
Option
Description
shared
For profiles that accept nonaggressive and non-interactive protocols.
express-shared
For profiles that accept interactive protocols such as Telnet.
private
For profiles that accept aggressive protocols such as HTTP and FTP so
that these aggressive protocols do not share tunnels with less-aggressive protocols.
FortiOS 8.0.0 CLI Reference
2584
Fortinet Inc.

<!-- 来源页 2585 -->
config http
Parameter
Description
Type
Size
Default
byte-caching
Enable/disable byte-caching. Byte caching reduces
the amount of traffic by caching file data sent
across the WAN and in future serving if from the
cache.
option
-enable
Option
Description
enable
Enable byte-caching.
disable
Disable byte-caching.
prefer-chunking
Select dynamic or fixed-size data chunking for
WAN Optimization.
option
-fix
Option
Description
dynamic
Select dynamic data chunking to help to detect persistent data chunks
in a changed file or in an embedded unknown protocol.
fix
Select fixed data chunking.
protocol-opt
Select protocol specific optimization or generic
TCP optimization.
option
-protocol
Option
Description
protocol
Using protocol-specific optimization.
tcp
Using generic TCP optimization.
secure-tunnel
Enable/disable securing the WAN Opt tunnel using
SSL. Secure and non-secure tunnels use the same
TCP port (7810).
option
-disable
Option
Description
enable
Enable SSL-secured tunnelling.
disable
Disable SSL-secured tunnelling.
ssl
Enable/disable SSL/TLS offloading (hardware
acceleration) for traffic in this tunnel.
option
-disable
Option
Description
enable
Enable SSL/TLS offloading.
disable
Disable SSL/TLS offloading.
status
Enable/disable WAN Optimization.
option
-disable
FortiOS 8.0.0 CLI Reference
2585
Fortinet Inc.

<!-- 来源页 2586 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable WAN Optimization.
disable
Disable WAN Optimization.
tunnel-sharing
Tunnel sharing mode for aggressive/non-aggressive and/or interactive/non-interactive
protocols.
option
-private
Option
Description
shared
For profiles that accept nonaggressive and non-interactive protocols.
express-shared
For profiles that accept interactive protocols such as Telnet.
private
For profiles that accept aggressive protocols such as HTTP and FTP so
that these aggressive protocols do not share tunnels with less-aggressive protocols.
config mapi
Parameter
Description
Type
Size
Default
byte-caching
Enable/disable byte-caching. Byte caching reduces
the amount of traffic by caching file data sent
across the WAN and in future serving if from the
cache.
option
-enable
Option
Description
enable
Enable byte-caching.
disable
Disable byte-caching.
secure-tunnel
Enable/disable securing the WAN Opt tunnel using
SSL. Secure and non-secure tunnels use the same
TCP port (7810).
option
-disable
Option
Description
enable
Enable SSL-secured tunnelling.
disable
Disable SSL-secured tunnelling.
status
Enable/disable WAN Optimization.
option
-disable
Option
Description
enable
Enable WAN Optimization.
disable
Disable WAN Optimization.
FortiOS 8.0.0 CLI Reference
2586
Fortinet Inc.

<!-- 来源页 2587 -->
Parameter
Description
Type
Size
Default
tunnel-sharing
Tunnel sharing mode for aggressive/non-aggressive and/or interactive/non-interactive
protocols.
option
-private
Option
Description
shared
For profiles that accept nonaggressive and non-interactive protocols.
express-shared
For profiles that accept interactive protocols such as Telnet.
private
For profiles that accept aggressive protocols such as HTTP and FTP so
that these aggressive protocols do not share tunnels with less-aggressive protocols.
config tcp
Parameter
Description
Type
Size
Default
byte-caching
Enable/disable byte-caching. Byte caching reduces
the amount of traffic by caching file data sent
across the WAN and in future serving if from the
cache.
option
-disable
Option
Description
enable
Enable byte-caching.
disable
Disable byte-caching.
byte-caching-opt
Select whether TCP byte-caching uses system
memory only or both memory and disk space.
option
-mem-only
Option
Description
mem-only
Byte caching with memory only.
mem-disk
Byte caching with memory and disk.
port
Port numbers or port number ranges for TCP. Only
packets with a destination port number that
matches this port number or range are accepted by
this profile.
user
Not
Specified
secure-tunnel
Enable/disable securing the WAN Opt tunnel using
SSL. Secure and non-secure tunnels use the same
TCP port (7810).
option
-disable
Option
Description
enable
Enable SSL-secured tunnelling.
disable
Disable SSL-secured tunnelling.
FortiOS 8.0.0 CLI Reference
2587
Fortinet Inc.

<!-- 来源页 2588 -->
Parameter
Description
Type
Size
Default
ssl
Enable/disable SSL/TLS offloading (hardware
acceleration) for traffic in this tunnel.
option
-disable
Option
Description
enable
Enable SSL/TLS offloading.
disable
Disable SSL/TLS offloading.
ssl-port
Port numbers or port number ranges on which to
expect HTTPS traffic for SSL/TLS offloading.
user
Not
Specified
status
Enable/disable WAN Optimization.
option
-disable
Option
Description
enable
Enable WAN Optimization.
disable
Disable WAN Optimization.
tunnel-sharing
Tunnel sharing mode for aggressive/non-aggressive and/or interactive/non-interactive
protocols.
option
-private
Option
Description
shared
For profiles that accept nonaggressive and non-interactive protocols.
express-shared
For profiles that accept interactive protocols such as Telnet.
private
For profiles that accept aggressive protocols such as HTTP and FTP so
that these aggressive protocols do not share tunnels with less-aggressive protocols.
FortiOS 8.0.0 CLI Reference
2588
Fortinet Inc.

<!-- 来源页 2589 -->
config wanopt remote-storage
This command is available for model(s): FortiGate 1000D, FortiGate 1001F, FortiGate 101F Gen2,
FortiGate 1101E, FortiGate 121G, FortiGate 1801F, FortiGate 2000E, FortiGate 201E, FortiGate 201F,
FortiGate 201G, FortiGate 2201E, FortiGate 2500E, FortiGate 2600F, FortiGate 2601F, FortiGate
3001F, FortiGate 301E, FortiGate 3201F Gen2, FortiGate 3301E, FortiGate 3401E, FortiGate 3501F
Gen2, FortiGate 3601E, FortiGate 3701F, FortiGate 401E, FortiGate 401F, FortiGate 4201F Gen2,
FortiGate 4401F Gen2, FortiGate 4801F, FortiGate 501E, FortiGate 601E, FortiGate 601F, FortiGate
71F, FortiGate 71G-POE, FortiGate 71G, FortiGate 800D, FortiGate 81F Gen2, FortiGate 81F-POE,
FortiGate 900D, FortiGate 901G, FortiGate 91G Gen2, FortiGate 91G, FortiGate-VM64 Aliyun,
FortiGate-VM64 AWS, FortiGate-VM64 Azure, FortiGate-VM64 GCP, FortiGate-VM64 OPC,
FortiGate-VM64, FortiGateRugged 70F 3G4G, FortiGateRugged 70F, FortiGateRugged 70G 5G Dual,
FortiGateRugged 70G, FortiWiFi 71G, FortiWiFi 80F 2R 3G4G DSL, FortiWiFi 81F 2R 3G4G DSL,
FortiWiFi 81F 2R 3G4G-POE, FortiWiFi 81F 2R-POE, FortiWiFi 81F 2R.
It is not available for: FortiGate 1000F, FortiGate 100F, FortiGate 1100E, FortiGate 120G, FortiGate
1800F, FortiGate 200E, FortiGate 200F, FortiGate 200G, FortiGate 2200E, FortiGate 3000F,
FortiGate 300E, FortiGate 30G, FortiGate 31G, FortiGate 3200F, FortiGate 3300E, FortiGate 3400E,
FortiGate 3500F Gen2, FortiGate 3600E, FortiGate 3700F, FortiGate 3960E, FortiGate 3980E,
FortiGate 400E Bypass, FortiGate 400E, FortiGate 400F, FortiGate 40F 3G4G, FortiGate 40F,
FortiGate 4200F, FortiGate 4400F, FortiGate 4800F, FortiGate 500E, FortiGate 50G 5G, FortiGate
50G DSL, FortiGate 50G SFP-POE, FortiGate 50G SFP, FortiGate 50G, FortiGate 51G 5G, FortiGate
51G SFP-POE, FortiGate 51G, FortiGate 600E, FortiGate 600F, FortiGate 60F, FortiGate 61F,
FortiGate 70F, FortiGate 70G-POE, FortiGate 70G, FortiGate 80F Bypass, FortiGate 80F DSL,
FortiGate 80F Gen2, FortiGate 80F-POE, FortiGate 900G, FortiGate 90G Gen2, FortiGate 90G,
FortiGateRugged 50G 5G, FortiGateRugged 60F 3G4G, FortiGateRugged 60F Gen2, FortiWiFi 30G,
FortiWiFi 31G, FortiWiFi 40F 3G4G, FortiWiFi 40F, FortiWiFi 50G 5G, FortiWiFi 50G DSL, FortiWiFi 50G
SFP, FortiWiFi 50G, FortiWiFi 51G, FortiWiFi 60F, FortiWiFi 61F, FortiWiFi 70G-POE, FortiWiFi 70G,
FortiWiFi 80F 2R.
Configure a remote cache device as Web cache storage.
config wanopt remote-storage
Description: Configure a remote cache device as Web cache storage.
set local-cache-id {string}
set remote-cache-id {string}
set remote-cache-ip {ipv4-address-any}
set status [disable|enable]
end
config wanopt remote-storage
Parameter
Description
Type
Size
Default
local-cache-id
ID that this device uses to connect to the remote
device.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
2589
Fortinet Inc.

<!-- 来源页 2590 -->
Parameter
Description
Type
Size
Default
remote-cache-id
ID of the remote device to which the device
connects.
string
Maximum
length: 35
remote-cache-ip
IP address of the remote device to which the
device connects.
ipv4-address-any
Not
Specified
0.0.0.0
status
Enable/disable using remote device as Web cache
storage.
option
-disable
Option
Description
disable
Use local disks as Web cache storage.
enable
Use a remote device as Web cache storage.
config wanopt settings
This command is available for model(s): FortiGate 1000D, FortiGate 1001F, FortiGate 101F Gen2,
FortiGate 1101E, FortiGate 121G, FortiGate 1801F, FortiGate 2000E, FortiGate 201E, FortiGate 201F,
FortiGate 201G, FortiGate 2201E, FortiGate 2500E, FortiGate 2600F, FortiGate 2601F, FortiGate
3001F, FortiGate 301E, FortiGate 3201F Gen2, FortiGate 3301E, FortiGate 3401E, FortiGate 3501F
Gen2, FortiGate 3601E, FortiGate 3701F, FortiGate 401E, FortiGate 401F, FortiGate 4201F Gen2,
FortiGate 4401F Gen2, FortiGate 4801F, FortiGate 501E, FortiGate 601E, FortiGate 601F, FortiGate
71F, FortiGate 71G-POE, FortiGate 71G, FortiGate 800D, FortiGate 81F Gen2, FortiGate 81F-POE,
FortiGate 900D, FortiGate 901G, FortiGate 91G Gen2, FortiGate 91G, FortiGate-VM64 Aliyun,
FortiGate-VM64 AWS, FortiGate-VM64 Azure, FortiGate-VM64 GCP, FortiGate-VM64 OPC,
FortiGate-VM64, FortiGateRugged 70F 3G4G, FortiGateRugged 70F, FortiGateRugged 70G 5G Dual,
FortiGateRugged 70G, FortiWiFi 71G, FortiWiFi 80F 2R 3G4G DSL, FortiWiFi 81F 2R 3G4G DSL,
FortiWiFi 81F 2R 3G4G-POE, FortiWiFi 81F 2R-POE, FortiWiFi 81F 2R.
It is not available for: FortiGate 1000F, FortiGate 100F, FortiGate 1100E, FortiGate 120G, FortiGate
1800F, FortiGate 200E, FortiGate 200F, FortiGate 200G, FortiGate 2200E, FortiGate 3000F,
FortiGate 300E, FortiGate 30G, FortiGate 31G, FortiGate 3200F, FortiGate 3300E, FortiGate 3400E,
FortiGate 3500F Gen2, FortiGate 3600E, FortiGate 3700F, FortiGate 3960E, FortiGate 3980E,
FortiGate 400E Bypass, FortiGate 400E, FortiGate 400F, FortiGate 40F 3G4G, FortiGate 40F,
FortiGate 4200F, FortiGate 4400F, FortiGate 4800F, FortiGate 500E, FortiGate 50G 5G, FortiGate
50G DSL, FortiGate 50G SFP-POE, FortiGate 50G SFP, FortiGate 50G, FortiGate 51G 5G, FortiGate
51G SFP-POE, FortiGate 51G, FortiGate 600E, FortiGate 600F, FortiGate 60F, FortiGate 61F,
FortiGate 70F, FortiGate 70G-POE, FortiGate 70G, FortiGate 80F Bypass, FortiGate 80F DSL,
FortiGate 80F Gen2, FortiGate 80F-POE, FortiGate 900G, FortiGate 90G Gen2, FortiGate 90G,
FortiGateRugged 50G 5G, FortiGateRugged 60F 3G4G, FortiGateRugged 60F Gen2, FortiWiFi 30G,
FortiWiFi 31G, FortiWiFi 40F 3G4G, FortiWiFi 40F, FortiWiFi 50G 5G, FortiWiFi 50G DSL, FortiWiFi 50G
SFP, FortiWiFi 50G, FortiWiFi 51G, FortiWiFi 60F, FortiWiFi 61F, FortiWiFi 70G-POE, FortiWiFi 70G,
FortiWiFi 80F 2R.
Configure WAN optimization settings.
FortiOS 8.0.0 CLI Reference
2590
Fortinet Inc.

<!-- 来源页 2591 -->
config wanopt settings
Description: Configure WAN optimization settings.
set auto-detect-algorithm [simple|diff-req-resp]
set host-id {string}
set tunnel-optimization [memory-usage|balanced|...]
set tunnel-ssl-algorithm [high|medium|...]
end
config wanopt settings
Parameter
Description
Type
Size
Default
auto-detect-algorithm
Auto detection algorithms used in tunnel
negotiations.
option
-simple
Option
Description
simple
Use the same TCP option value in SYN/SYNACK packets. Backward
compatible.
diff-req-resp
Use different TCP option values in SYN/SYNACK packets to avoid false
positive detection.
host-id
Local host ID (must also be entered in the remote
FortiGate's peer list).
string
Maximum
length: 35
default-id
tunnel-optimization
WANOpt tunnel optimization option.
option
-balanced
**
Option
Description
memory-usage
Optimize tunnel for low system memory usage.
balanced
Optimize tunnel to balance between system memory usage and
throughput.
throughput
Optimize tunnel for throughput.
tunnel-ssl-algorithm
Relative strength of encryption algorithms
accepted during tunnel negotiation.
option
-high
Option
Description
high
High encryption. Allow only AES and ChaCha.
medium
Medium encryption. Allow AES, ChaCha, 3DES, and RC4.
low
Low encryption. Allow AES, ChaCha, 3DES, RC4, and DES.
** Values may differ between models.
FortiOS 8.0.0 CLI Reference
2591
Fortinet Inc.

<!-- 来源页 2592 -->
config wanopt webcache
This command is available for model(s): FortiGate 1000D, FortiGate 1001F, FortiGate 101F Gen2,
FortiGate 1101E, FortiGate 121G, FortiGate 1801F, FortiGate 2000E, FortiGate 201E, FortiGate 201F,
FortiGate 201G, FortiGate 2201E, FortiGate 2500E, FortiGate 2600F, FortiGate 2601F, FortiGate
3001F, FortiGate 301E, FortiGate 3201F Gen2, FortiGate 3301E, FortiGate 3401E, FortiGate 3501F
Gen2, FortiGate 3601E, FortiGate 3701F, FortiGate 401E, FortiGate 401F, FortiGate 4201F Gen2,
FortiGate 4401F Gen2, FortiGate 4801F, FortiGate 501E, FortiGate 601E, FortiGate 601F, FortiGate
71F, FortiGate 71G-POE, FortiGate 71G, FortiGate 800D, FortiGate 81F Gen2, FortiGate 81F-POE,
FortiGate 900D, FortiGate 901G, FortiGate 91G Gen2, FortiGate 91G, FortiGate-VM64 Aliyun,
FortiGate-VM64 AWS, FortiGate-VM64 Azure, FortiGate-VM64 GCP, FortiGate-VM64 OPC,
FortiGate-VM64, FortiGateRugged 70F 3G4G, FortiGateRugged 70F, FortiGateRugged 70G 5G Dual,
FortiGateRugged 70G, FortiWiFi 71G, FortiWiFi 80F 2R 3G4G DSL, FortiWiFi 81F 2R 3G4G DSL,
FortiWiFi 81F 2R 3G4G-POE, FortiWiFi 81F 2R-POE, FortiWiFi 81F 2R.
It is not available for: FortiGate 1000F, FortiGate 100F, FortiGate 1100E, FortiGate 120G, FortiGate
1800F, FortiGate 200E, FortiGate 200F, FortiGate 200G, FortiGate 2200E, FortiGate 3000F,
FortiGate 300E, FortiGate 30G, FortiGate 31G, FortiGate 3200F, FortiGate 3300E, FortiGate 3400E,
FortiGate 3500F Gen2, FortiGate 3600E, FortiGate 3700F, FortiGate 3960E, FortiGate 3980E,
FortiGate 400E Bypass, FortiGate 400E, FortiGate 400F, FortiGate 40F 3G4G, FortiGate 40F,
FortiGate 4200F, FortiGate 4400F, FortiGate 4800F, FortiGate 500E, FortiGate 50G 5G, FortiGate
50G DSL, FortiGate 50G SFP-POE, FortiGate 50G SFP, FortiGate 50G, FortiGate 51G 5G, FortiGate
51G SFP-POE, FortiGate 51G, FortiGate 600E, FortiGate 600F, FortiGate 60F, FortiGate 61F,
FortiGate 70F, FortiGate 70G-POE, FortiGate 70G, FortiGate 80F Bypass, FortiGate 80F DSL,
FortiGate 80F Gen2, FortiGate 80F-POE, FortiGate 900G, FortiGate 90G Gen2, FortiGate 90G,
FortiGateRugged 50G 5G, FortiGateRugged 60F 3G4G, FortiGateRugged 60F Gen2, FortiWiFi 30G,
FortiWiFi 31G, FortiWiFi 40F 3G4G, FortiWiFi 40F, FortiWiFi 50G 5G, FortiWiFi 50G DSL, FortiWiFi 50G
SFP, FortiWiFi 50G, FortiWiFi 51G, FortiWiFi 60F, FortiWiFi 61F, FortiWiFi 70G-POE, FortiWiFi 70G,
FortiWiFi 80F 2R.
Configure global Web cache settings.
config wanopt webcache
Description: Configure global Web cache settings.
set always-revalidate [enable|disable]
set cache-by-default [enable|disable]
set cache-cookie [enable|disable]
set cache-expired [enable|disable]
set default-ttl {integer}
set external [enable|disable]
set fresh-factor {integer}
set host-validate [enable|disable]
set ignore-conditional [enable|disable]
set ignore-ie-reload [enable|disable]
set ignore-ims [enable|disable]
set ignore-pnc [enable|disable]
set max-object-size {integer}
set max-ttl {integer}
set min-ttl {integer}
set neg-resp-time {integer}
FortiOS 8.0.0 CLI Reference
2592
Fortinet Inc.

<!-- 来源页 2593 -->
set reval-pnc [enable|disable]
end
config wanopt webcache
Parameter
Description
Type
Size
Default
always-revalidate
Enable/disable revalidation of requested
cached objects, which have content on the
server, before serving it to the client.
option
-disable
Option
Description
enable
Enable revalidation of requested cached objects.
disable
Disable revalidation of requested cached objects.
cache-by-default
Enable/disable caching content that lacks
explicit caching policies from the server.
option
-disable
Option
Description
enable
Enable caching content that lacks explicit caching policies.
disable
Disable caching content that lacks explicit caching policies.
cache-cookie
Enable/disable caching cookies. Since cookies
contain information for or about individual
users, they not usually cached.
option
-disable
Option
Description
enable
Cache cookies.
disable
Do not cache cookies.
cache-expired
Enable/disable caching type-1 objects that are
already expired on arrival.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
default-ttl
Default object expiry time (default = 1440 min (1
day); maximum = 5256000 min (10 years)). This
only applies to those objects that do not have
an expiry time set by the web server.
integer
Minimum value:
1 Maximum
value:
5256000
1440
external
Enable/disable external Web caching.
option
-disable
FortiOS 8.0.0 CLI Reference
2593
Fortinet Inc.

<!-- 来源页 2594 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable external Web caching.
disable
Disable external Web caching.
fresh-factor
Frequency that the server is checked to see if
any objects have expired (1 - 100, default =
100). The higher the fresh factor, the less often
the checks occur.
integer
Minimum value:
1 Maximum
value: 100
100
host-validate
Enable/disable validating "Host:" with original
server IP.
option
-disable
Option
Description
enable
Enable validating "Host:" with original server IP.
disable
Disable validating "Host:" with original server IP.
ignore-conditional
Enable/disable controlling the behavior of
cache-control HTTP 1.1 header values.
option
-disable
Option
Description
enable
Enable ignoring cache-control HTTP 1.1 header values.
disable
Disable ignoring cache-control HTTP 1.1 header values.
ignore-ie-reload
Enable/disable ignoring the PNC-interpretation
of Internet Explorer's Accept: / header.
option
-enable
Option
Description
enable
Enable Enable/disable ignoring the PNC-interpretation of Internet
Explorer's Accept: / header.
disable
Disable Enable/disable ignoring the PNC-interpretation of Internet
Explorer's Accept: / header.
ignore-ims
Enable/disable ignoring the if-modified-since
(IMS) header.
option
-disable
Option
Description
enable
Enable ignoring the if-modified-since (IMS) header.
disable
Disable ignoring the if-modified-since (IMS) header.
ignore-pnc
Enable/disable ignoring the pragma no-cache
(PNC) header.
option
-disable
FortiOS 8.0.0 CLI Reference
2594
Fortinet Inc.

<!-- 来源页 2595 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable ignoring the pragma no-cache (PNC) header.
disable
Disable ignoring the pragma no-cache (PNC) header.
max-object-size
Maximum cacheable object size in kB (1 -2147483 kb (2GB). All objects that exceed this
are delivered to the client but not stored in the
web cache.
integer
Minimum value:
1 Maximum
value: 2147483
512000
max-ttl
Maximum time an object can stay in the web
cache without checking to see if it has expired
on the server (default = 7200 min (5 days);
maximum = 5256000 min (10 years)).
integer
Minimum value:
1 Maximum
value:
5256000
7200
min-ttl
Minimum time an object can stay in the web
cache without checking to see if it has expired
on the server (default = 5 min; maximum =
5256000 (10 years)).
integer
Minimum value:
1 Maximum
value:
5256000
5
neg-resp-time
Time in minutes to cache negative responses or
errors (0 - 4294967295, default = 0 which
means negative responses are not cached).
integer
Minimum value:
0 Maximum
value:
4294967295
0
reval-pnc
Enable/disable revalidation of pragma-no-cache (PNC) to address bandwidth concerns.
option
-disable
Option
Description
enable
Enable revalidation of pragma-no-cache (PNC).
disable
Disable revalidation of pragma-no-cache (PNC).
FortiOS 8.0.0 CLI Reference
2595
Fortinet Inc.
