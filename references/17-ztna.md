# 零信任网络访问 (ZTNA)

> 来源: FortiOS-8.0.0-CLI_Reference.pdf
> 覆盖命令/章节: ztna
> 本文件由 extract_pdf.py 从官方 PDF 自动提取，请勿手动编辑；
> 如需修正请修改 map.json 后重跑脚本。

---


<!-- 来源页 2933 -->
ztna
This section includes syntax for the following commands:
l config ztna connector-edge on page 2933
l config ztna destination on page 2935
l config ztna reverse-connector on page 2937
l config ztna service-connector on page 2940
l config ztna traffic-forward-proxy on page 2943
l config ztna web-portal-bookmark on page 2949
l config ztna web-portal on page 2944
l config ztna web-proxy on page 2956
config ztna connector-edge
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
FortiOS 8.0.0 CLI Reference
2933
Fortinet Inc.

<!-- 来源页 2934 -->
Configure ZTNA connector edge.
config ztna connector-edge
Description: Configure ZTNA connector edge.
set interface <name1>, <name2>, ...
set port {integer}
set server-cert {string}
set ssl-max-version [tls-1.1|tls-1.2|...]
set ssl-min-version [tls-1.1|tls-1.2|...]
set status [enable|disable]
set trusted-client-ca <name1>, <name2>, ...
end
config ztna connector-edge
Parameter
Description
Type
Size
Default
interface
<name>
Connector edge interface.
Interface name.
string
Maximum
length: 79
port
Connector service edge port(1-65535, default
8443).
integer
Minimum
value: 1
Maximum
value:
65535
8443
server-cert
Server certificate for mTLS.
string
Maximum
length: 79
ssl-max-version
Highest TLS version accepted by server.
option
-tls-1.3
Option
Description
tls-1.1
TLS 1.1.
tls-1.2
TLS 1.2.
tls-1.3
TLS 1.3.
ssl-min-version
Lowest TLS version accepted by server.
option
-tls-1.2
Option
Description
tls-1.1
TLS 1.1.
tls-1.2
TLS 1.2.
tls-1.3
TLS 1.3.
status
Connector service edge status.
option
-disable
FortiOS 8.0.0 CLI Reference
2934
Fortinet Inc.

<!-- 来源页 2935 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable the connector edge.
disable
Disable the connector edge.
trusted-client-ca
<name>
CA certificate used for client certificate verification.
CA certificate list.
string
Maximum
length: 79
config ztna destination
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
Configure ZTNA destination.
config ztna destination
Description: Configure ZTNA destination.
edit <name>
set address {string}
set conn-type [traffic-forwarding|ssh]
FortiOS 8.0.0 CLI Reference
2935
Fortinet Inc.

<!-- 来源页 2936 -->
set domain {string}
set external-auth [enable|disable]
set mappedport {user}
set protocol [TCP|UDP|...]
set saas-application <name1>, <name2>, ...
set ssh-client-cert {string}
set ssh-host-key <name1>, <name2>, ...
set ssh-host-key-validation [disable|enable]
set tunnel-encryption [enable|disable]
set type [on-premise|saas]
set uuid {uuid}
next
end
config ztna destination
Parameter
Description
Type
Size
Default
address
Address or address group of the ZTNA
destination.
string
Maximum
length: 79
conn-type
Connection type.
option
-traffic-forwarding
Option
Description
traffic-forwarding
Traffic forwarding.
ssh
SSH.
domain
Wildcard domain name of the ZTNA
destination.
string
Maximum
length: 255
external-auth
Enable/disable use of external browser as
user-agent for SAML user authentication.
option
-disable
Option
Description
enable
Enable use of external browser as user-agent for SAML user
authentication.
disable
Disable use of external browser as user-agent for SAML user
authentication.
mappedport
Port for communicating with the real server.
user
Not
Specified
name
Destination name.
string
Maximum
length: 79
protocol
Protocol type based on IANA numbers.
option
-ALL
FortiOS 8.0.0 CLI Reference
2936
Fortinet Inc.

<!-- 来源页 2937 -->
Parameter
Description
Type
Size
Default
Option
Description
TCP
TCP.
UDP
UDP.
ALL
All.
saas-application
<name>
SaaS application controlled by this ZTNA
destination.
SaaS application name.
string
Maximum
length: 79
ssh-client-cert
Configure access-proxy SSH client
certificate profile.
string
Maximum
length: 79
ssh-host-key
<name>
Configure host keys (one or more may be
configured).
Host key name.
string
Maximum
length: 79
ssh-host-key-validation
Enable/disable SSH host key validation.
option
-disable
Option
Description
disable
Disable SSH server host key validation.
enable
Enable SSH server host key validation.
tunnel-encryption
Tunnel encryption.
option
-disable
Option
Description
enable
Enable traffic forwarding tunnel encryption.
disable
Disable traffic forwarding tunnel encryption.
type
ZTNA destination type.
option
-on-premise
Option
Description
on-premise
On-Premise.
saas
SaaS.
uuid
Universally Unique Identifier (UUID;
automatically assigned but can be manually
reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
config ztna reverse-connector
Configure ZTNA Reverse-Connector.
FortiOS 8.0.0 CLI Reference
2937
Fortinet Inc.

<!-- 来源页 2938 -->
config ztna reverse-connector
Description: Configure ZTNA Reverse-Connector.
edit <name>
set address {string}
set certificate {string}
set default-incoming-vip {string}
set health-check-interval {integer}
set interface {string}
set interface-select-method [auto|sdwan|...]
set port {integer}
set source-ip {ipv4-address}
set source-ip-interface {string}
set ssl-max-version [tls-1.1|tls-1.2|...]
set ssl-min-version [tls-1.1|tls-1.2|...]
set status [enable|disable]
set trusted-server-ca {string}
set vrf-select {integer}
next
end
config ztna reverse-connector
Parameter
Description
Type
Size
Default
address
Connector service edge adress(IP or FQDN).
string
Maximum
length: 255
certificate
The name of the certificate to use for SSL
handshake.
string
Maximum
length: 35
default-incoming-vip
*
Default Incoming Virtual IP name.
string
Maximum
length: 79
health-check-interval
Health check interval in seconds (0 - 600, default =
60, 0 = disable).
integer
Minimum
value: 0
Maximum
value: 600
60
interface *
Specify outgoing interface to reach server.
string
Maximum
length: 15
interface-select-method *
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
FortiOS 8.0.0 CLI Reference
2938
Fortinet Inc.

<!-- 来源页 2939 -->
Parameter
Description
Type
Size
Default
Option
Description
specify
Set outgoing interface manually.
name
Reverse-Connector name
string
Maximum
length: 35
port
Port number that traffic uses to connect to
connector service edge(1 - 65535;).
integer
Minimum
value: 1
Maximum
value:
65535 **
0
source-ip *
FortiGate IPv4 address to be used for ZTNA
reverse-connector connection.
ipv4-address
Not
Specified
0.0.0.0
source-ip-interface *
Source interface to be used for ZTNA reverse-connector connection.
string
Maximum
length: 15
ssl-max-version
Highest TLS version acceptable from a server.
option
-tls-1.3
Option
Description
tls-1.1
TLS 1.1.
tls-1.2
TLS 1.2.
tls-1.3
TLS 1.3.
ssl-min-version *
Lowest SSL/TLS version acceptable from a server.
option
-tls-1.2
Option
Description
tls-1.1
TLS 1.1.
tls-1.2
TLS 1.2.
tls-1.3
TLS 1.3.
status
Reverse-Connector status.
option
-enable
Option
Description
enable
Enable the reverse-connector.
disable
Disable the reverse-connector.
trusted-server-ca
Trusted Server CA certificate used by SSL
connection.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
2939
Fortinet Inc.

<!-- 来源页 2940 -->
Parameter
Description
Type
Size
Default
vrf-select *
VRF ID used for connection to server.
integer
Minimum
value: 0
Maximum
value: 511
0
* This parameter may not exist in some models.
** Values may differ between models.
config ztna service-connector
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
Configure ZTNA service connector.
config ztna service-connector
Description: Configure ZTNA service connector.
edit <name>
set certificate {string}
set connection-mode [forward|reverse]
set encryption [enable|disable]
FortiOS 8.0.0 CLI Reference
2940
Fortinet Inc.

<!-- 来源页 2941 -->
set forward-address {string}
set forward-destination-cn {string}
set forward-port {integer}
set health-check-interval {integer}
set log [enable|disable]
set relay-dev-info [enable|disable]
set relay-user-info [enable|disable]
set ssl-max-version [ssl-3.0|tls-1.0|...]
set ssl-min-version [ssl-3.0|tls-1.0|...]
set trusted-ca {string}
set url-map {string}
next
end
config ztna service-connector
Parameter
Description
Type
Size
Default
certificate
The name of the certificate to use for SSL
handshake.
string
Maximum
length: 35
connection-mode
Connection mode.
option
-forward
Option
Description
forward
Forward Service.
reverse
Reverse Service.
encryption
Enable/disable Encryption (default = disable).
option
-enable
Option
Description
enable
Enable Encryption.
disable
Disable Encryption.
forward-address
service-connector address(IP or FQDN).
string
Maximum
length: 255
forward-destination-cn
CN for forward server.
string
Maximum
length: 255
forward-port
Port number that forward traffic uses to connect to
integer
Minimum
value: 1
Maximum
value:
65535
0
FortiOS 8.0.0 CLI Reference
2941
Fortinet Inc.

<!-- 来源页 2942 -->
Parameter
Description
Type
Size
Default
health-check-interval
health check interval(0-600 seconds, default 60, 0
means disable).
integer
Minimum
value: 0
Maximum
value: 600
60
log
Enable/disable logging of traffic.
option
-enable
Option
Description
enable
Log all traffic by this service connector.
disable
Do not log traffic by this service connector.
name
Service-connector name
string
Maximum
length: 79
relay-dev-info
Enable/disable device info relay.
option
-disable
Option
Description
enable
Relay device information to service connector
disable
Do not relay device information to service connector.
relay-user-info
Enable/disable user info relay.
option
-disable
Option
Description
enable
Relay user information to service connector
disable
Do not relay user information to service connector.
ssl-max-version
Highest SSL/TLS version acceptable from a server.
option
-tls-1.2
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
Lowest SSL/TLS version acceptable from a server.
option
-tls-1.1
Option
Description
ssl-3.0
SSL 3.0.
FortiOS 8.0.0 CLI Reference
2942
Fortinet Inc.

<!-- 来源页 2943 -->
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
trusted-ca
Trusted CA certificate used by SSL inspection.
string
Maximum
length: 79
url-map
URL pattern to match.
string
Maximum
length: 63
/tcp
config ztna traffic-forward-proxy
Configure ZTNA traffic forward proxy.
config ztna traffic-forward-proxy
Description: Configure ZTNA traffic forward proxy.
edit <name>
set auth-portal [disable|enable]
set auth-virtual-host {string}
set decrypted-traffic-mirror {string}
set host {string}
set log-blocked-traffic [disable|enable]
config url-route
Description: Configure URL-based routing rules.
edit <name>
set service-connector {string}
set url-pattern {string}
next
end
set vip {string}
set vip6 {string}
next
end
config ztna traffic-forward-proxy
Parameter
Description
Type
Size
Default
auth-portal *
Enable/disable authentication portal.
option
-disable
FortiOS 8.0.0 CLI Reference
2943
Fortinet Inc.

<!-- 来源页 2944 -->
Parameter
Description
Type
Size
Default
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
decrypted-traffic-mirror
Decrypted traffic mirror.
string
Maximum
length: 35
host
Virtual or real host name.
string
Maximum
length: 79
log-blocked-traffic *
Enable/disable logging of blocked traffic.
option
-enable
Option
Description
disable
Do not log all traffic denied by this ZTNA web-proxy.
enable
Log all traffic denied by this ZTNA web-proxy.
name
ZTNA traffic forward proxy name.
string
Maximum
length: 79
vip
Virtual IP name.
string
Maximum
length: 79
vip6
Virtual IPv6 name.
string
Maximum
length: 79
* This parameter may not exist in some models.
config url-route
Parameter
Description
Type
Size
Default
name
Name of the URL route.
string
Maximum
length: 79
service-connector
Service-connector to handle matched requests.
string
Maximum
length: 79
url-pattern
URL pattern used to match incoming requests.
string
Maximum
length: 511
/tcp
config ztna web-portal
Configure ztna web-portal.
FortiOS 8.0.0 CLI Reference
2944
Fortinet Inc.

<!-- 来源页 2945 -->
config ztna web-portal
Description: Configure ztna web-portal.
edit <name>
set auth-portal [disable|enable]
set auth-rule {string}
set auth-virtual-host {string}
set bookmarks {string}
set clipboard [enable|disable]
set cookie-age {integer}
set customize-forticlient-download-url [enable|disable]
set decrypted-traffic-mirror {string}
set default-window-height {integer}
set default-window-width {integer}
set display-bookmark [enable|disable]
set display-history [enable|disable]
set display-status [enable|disable]
set focus-bookmark [enable|disable]
set forticlient-download [enable|disable]
set heading {string}
set host {string}
set llm-profile {string}
set llm-proxy [enable|disable]
set log-blocked-traffic [disable|enable]
set macos-forticlient-download-url {var-string}
set policy-auth-sso [enable|disable]
set theme [jade|neutrino|...]
set vip {string}
set vip6 {string}
set windows-forticlient-download-url {var-string}
next
end
config ztna web-portal
Parameter
Description
Type
Size
Default
auth-portal *
Enable/disable authentication portal.
option
-disable
Option
Description
disable
Disable authentication portal.
enable
Enable authentication portal.
auth-rule
Authentication Rule.
string
Maximum
length: 35
auth-virtual-host *
Virtual host for authentication portal.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
2945
Fortinet Inc.

<!-- 来源页 2946 -->
Parameter
Description
Type
Size
Default
bookmarks *
Dynamic bookmarks.
string
Maximum
length: 35
clipboard
Enable to support RDP/VPC clipboard functionality.
option
-enable
Option
Description
enable
Enable support of RDP/VNC clipboard.
disable
Disable support of RDP/VNC clipboard.
cookie-age
Time in minutes that client web browsers should
keep a cookie. Default is 60 minutes. 0 = no time
limit.
integer
Minimum
value: 0
Maximum
value:
525600
60
customize-forticlient-download-url
Enable support of customized download URL for
FortiClient.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
decrypted-traffic-mirror
Decrypted traffic mirror.
string
Maximum
length: 35
default-window-height
Screen height (range from 0 - 65535, default =
768).
integer
Minimum
value: 0
Maximum
value:
65535
768
default-window-width
Screen width (range from 0 - 65535, default =
1024).
integer
Minimum
value: 0
Maximum
value:
65535
1024
display-bookmark
Enable to display the web portal bookmark widget.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
2946
Fortinet Inc.

<!-- 来源页 2947 -->
Parameter
Description
Type
Size
Default
display-history
Enable to display the web portal user login history
widget.
option
-enable **
Option
Description
enable
Enable setting.
disable
Disable setting.
display-status
Enable to display the web portal status widget.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
focus-bookmark
Enable to prioritize the placement of the bookmark
section over the quick-connection section in the
ztna web-portal.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
forticlient-download
Enable/disable download option for FortiClient.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
heading
Web portal heading message.
string
Maximum
length: 31
ZTNA
Portal
host
Virtual or real host name.
string
Maximum
length: 79
llm-profile *
LLM Profile.
string
Maximum
length: 79
llm-proxy *
Enable LLM Proxy.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
2947
Fortinet Inc.

<!-- 来源页 2948 -->
Parameter
Description
Type
Size
Default
log-blocked-traffic *
Enable/disable logging of blocked traffic.
option
-enable
Option
Description
disable
Do not log all traffic denied by this ZTNA web-proxy.
enable
Log all traffic denied by this ZTNA web-proxy.
macos-forticlient-download-url
Download URL for Mac FortiClient.
var-string
Maximum
length:
1023
name
ZTNA web portal name.
string
Maximum
length: 79
policy-auth-sso
Enable policy sso authentication.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
theme
Web portal color scheme.
option
-security-fabric
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
dark-matter
Dark Matter theme.
onyx
Onyx theme.
eclipse
Eclipse theme.
vip
Virtual IP name.
string
Maximum
length: 79
vip6
Virtual IPv6 name.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
2948
Fortinet Inc.

<!-- 来源页 2949 -->
Parameter
Description
Type
Size
Default
windows-forticlient-download-url
Download URL for Windows FortiClient.
var-string
Maximum
length:
1023
* This parameter may not exist in some models.
** Values may differ between models.
config ztna web-portal-bookmark
Configure ztna web-portal bookmark.
config ztna web-portal-bookmark
Description: Configure ztna web-portal bookmark.
edit <name>
config bookmarks
Description: Bookmark table.
edit <name>
set apptype [ftp|rdp|...]
set color-depth [32|16|...]
set description {var-string}
set domain {var-string}
set folder {var-string}
set height {integer}
set host {var-string}
set keyboard-layout [ar-101|ar-102|...]
set load-balancing-info {var-string}
set logon-password {password}
set logon-user {var-string}
set port {integer}
set preconnection-blob {var-string}
set preconnection-id {integer}
set restricted-admin [enable|disable]
set security [any|rdp|...]
set send-preconnection-id [enable|disable]
set sso [disable|enable]
set url {var-string}
set verify-cert [enable|disable]
set vnc-keyboard-layout [default|da|...]
set width {integer}
next
end
set groups <name1>, <name2>, ...
config llm-secure-proxy
Description: LLM secure proxy.
set all-llm-servers [enable|disable]
set llm-servers <name1>, <name2>, ...
end
set type [user|ldap-dynamic|...]
FortiOS 8.0.0 CLI Reference
2949
Fortinet Inc.

<!-- 来源页 2950 -->
set users <name1>, <name2>, ...
next
end
config ztna web-portal-bookmark
Parameter
Description
Type
Size
Default
groups
<name>
User groups.
Group name.
string
Maximum length:
79
name
Bookmark name.
string
Maximum length:
35
type *
Bookmark type.
option
-user
Option
Description
user
Users/Groups.
ldap-dynamic
LDAP attributes dynamic.
saml-dynamic
SAML attributes dynamic.
users <name>
User name.
User name.
string
Maximum length:
79
* This parameter may not exist in some models.
config bookmarks
Parameter
Description
Type
Size
Default
apptype
Application type.
option
-web
Option
Description
ftp
FTP.
rdp
RDP.
sftp
SFTP.
smb
SMB/CIFS.
ssh
SSH.
telnet
Telnet.
vnc
VNC.
web
HTTP/HTTPS.
color-depth
Color depth per pixel.
option
-16
FortiOS 8.0.0 CLI Reference
2950
Fortinet Inc.

<!-- 来源页 2951 -->
Parameter
Description
Type
Size
Default
Option
Description
32
32bits per pixel.
16
16bits per pixel.
8
8bits per pixel.
description
Description.
var-string
Maximum
length: 128
domain
Login domain.
var-string
Maximum
length: 128
folder
Network shared file folder parameter.
var-string
Maximum
length: 128
height
Screen height (range from 0 - 65535,
default = 0).
integer
Minimum value:
0 Maximum
value: 65535
0
host
Host name/IP parameter.
var-string
Maximum
length: 128
keyboard-layout
Keyboard layout.
option
-en-us
Option
Description
ar-101
Arabic (101).
ar-102
Arabic (102).
ar-102-azerty
Arabic (102) AZERTY.
can-mul
Canadian Multilingual Standard.
cz
Czech.
cz-qwerty
Czech (QWERTY).
cz-pr
Czech Programmers.
da
Danish.
nl
Dutch.
de
German.
de-ch
German, Switzerland.
de-ibm
German (IBM).
en-uk
English, United Kingdom.
en-uk-ext
English, United Kingdom Extended.
FortiOS 8.0.0 CLI Reference
2951
Fortinet Inc.

<!-- 来源页 2952 -->
Parameter
Description
Type
Size
Default
Option
Description
en-us
English, United States.
en-us-dvorak
English, United States-Dvorak.
es
Spanish.
es-var
Spanish Variation.
fi
Finnish.
fi-sami
Finnish with Sami.
fr
French.
fr-apple
French, Apple.
fr-ca
French, Canada.
fr-ch
French, Switzerland.
fr-be
French, Belgium.
hr
Croatian.
hu
Hungarian.
hu-101
Hungarian 101-Key.
it
Italian.
it-142
Italian (142).
ja
Japanese.
ja-106
Japanese 106/109 key.
ko
Korean.
la-am
Latin American.
lt
Lithuanian.
lt-ibm
Lithuanian IBM.
lt-std
Lithuanian Standard.
lav-std
Latvian (Standard).
lav-leg
Latvian (Legacy).
mk
Macedonian (FYROM).
mk-std
Macedonia (FYROM) - Standard.
no
Norwegian.
no-sami
Norwegian with Sami.
FortiOS 8.0.0 CLI Reference
2952
Fortinet Inc.

<!-- 来源页 2953 -->
Parameter
Description
Type
Size
Default
Option
Description
pol-214
Polish (214).
pol-pr
Polish (Programmers).
pt
Portuguese.
pt-br
Portuguese (Brazilian ABNT).
pt-br-abnt2
Portuguese (Brazilian ABNT2).
ru
Russian.
ru-mne
Russian - Mnemonic.
ru-t
Russian (Typewriter).
sl
Slovenian.
sv
Swedish.
sv-sami
Swedish with Sami.
tuk
Turkmen.
tur-f
Turkish F.
tur-q
Turkish Q.
zh-sym-sg-us
Chinese (Simplified, Singapore) - US keyboard.
zh-sym-us
Chinese (Simplified) - US Keyboard.
zh-tr-hk
Chinese (Traditional, Hong Kong S.A.R.).
zh-tr-mo
Chinese (Traditional Macao S.A.R.) - US Keyboard.
zh-tr-us
Chinese (Traditional) - US keyboard.
load-balancing-info
The load balancing information or cookie
which should be provided to the
connection broker.
var-string
Maximum
length: 511
logon-password
Logon password.
password
Not Specified
logon-user
Logon user.
var-string
Maximum
length: 35
name
Bookmark name.
string
Maximum
length: 35
port
Remote port.
integer
Minimum value:
0 Maximum
value: 65535
0
FortiOS 8.0.0 CLI Reference
2953
Fortinet Inc.

<!-- 来源页 2954 -->
Parameter
Description
Type
Size
Default
preconnection-blob
An arbitrary string which identifies the RDP
source.
var-string
Maximum
length: 511
preconnection-id
The numeric ID of the RDP source (0-4294967295).
integer
Minimum value:
0 Maximum
value:
4294967295
0
restricted-admin
Enable/disable restricted admin mode for
RDP.
option
-disable
Option
Description
enable
Enable restricted admin mode for RDP.
disable
Disable restricted admin mode for RDP.
security
Security mode for RDP connection (default
= any).
option
-any
Option
Description
any
Allow the server to choose the type of security.
rdp
Standard RDP encryption.
nla
Network Level Authentication.
tls
TLS encryption.
send-preconnection-id
Enable/disable sending of preconnection
ID.
option
-disable
Option
Description
enable
Enable sending of preconnection ID.
disable
Disable sending of preconnection ID.
sso
Single sign-on.
option
-disable
Option
Description
disable
Disable SSO.
enable
Enable SSO.
url
URL parameter.
var-string
Maximum
length: 128
verify-cert *
Enable/disable certificate verification of
the real server.
option
-enable
FortiOS 8.0.0 CLI Reference
2954
Fortinet Inc.

<!-- 来源页 2955 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable certificate verification.
disable
Disable certificate verification.
vnc-keyboard-layout
Keyboard layout.
option
-default
Option
Description
default
Default.
da
Danish.
nl
Dutch.
en-uk
English, United Kingdom.
en-uk-ext
English, United Kingdom Extended.
fi
Finnish.
fr
French.
fr-be
French, Belgium.
fr-ca-mul
French, Canadian Multilingual Std.
de
German.
de-ch
German, Switzerland.
it
Italian.
it-142
Italian (142).
pt
Portuguese.
pt-br-abnt2
Portuguese (Brazilian ABNT2).
no
Norwegian.
gd
Scottish Gaelic.
es
Spanish.
sv
Swedish.
us-intl
United States-International.
width
Screen width (range from 0 - 65535,
default = 0).
integer
Minimum value:
0 Maximum
value: 65535
0
* This parameter may not exist in some models.
FortiOS 8.0.0 CLI Reference
2955
Fortinet Inc.

<!-- 来源页 2956 -->
config llm-secure-proxy
Parameter
Description
Type
Size
Default
all-llm-servers
Include all LLM servers.
option
-enable
Option
Description
enable
Enable all LLM servers.
disable
Disable all LLM servers.
llm-servers
<name>
LLM proxy server names.
Server name.
string
Maximum
length: 79
config ztna web-proxy
Configure ZTNA web-proxy.
config ztna web-proxy
Description: Configure ZTNA web-proxy.
edit <name>
config api-gateway
Description: Set IPv4 API Gateway.
edit <id>
set h2-support [enable|disable]
set h3-support [enable|disable]
set http-cookie-age {integer}
set http-cookie-domain {string}
set http-cookie-domain-from-host [disable|enable]
set http-cookie-generation {integer}
set http-cookie-path {string}
set http-cookie-share [disable|same-ip]
set https-cookie-secure [disable|enable]
set ldb-method [static|round-robin|...]
set persistence [none|http-cookie]
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
Description: Select the real servers that this ZTNA web-proxy will distribute
FortiOS 8.0.0 CLI Reference
2956
Fortinet Inc.

<!-- 来源页 2957 -->
traffic to.
edit <id>
set addr-type [ip|fqdn]
set address {string}
set health-check [disable|enable]
set health-check-proto [ping|http|...]
set holddown-interval [enable|disable]
set http-host {string}
set ip {ipv4-address-any}
set port {integer}
set status [active|standby|...]
set translate-host [enable|disable]
set verify-cert [enable|disable]
set weight {integer}
next
end
set service [http|https]
set ssl-algorithm [high|medium|...]
config ssl-cipher-suites
Description: SSL/TLS cipher suites to offer to a server, ordered by priority.
edit <priority>
set cipher [TLS-AES-128-GCM-SHA256|TLS-AES-256-GCM-SHA384|...]
set versions {option1}, {option2}, ...
next
end
set ssl-dh-bits [768|1024|...]
set ssl-max-version [tls-1.0|tls-1.1|...]
set ssl-min-version [tls-1.0|tls-1.1|...]
set ssl-renegotiation [enable|disable]
set url-map {string}
set url-map-type [sub-string|wildcard|...]
next
end
config api-gateway6
Description: Set IPv6 API Gateway.
edit <id>
set h2-support [enable|disable]
set h3-support [enable|disable]
set http-cookie-age {integer}
set http-cookie-domain {string}
set http-cookie-domain-from-host [disable|enable]
set http-cookie-generation {integer}
set http-cookie-path {string}
set http-cookie-share [disable|same-ip]
set https-cookie-secure [disable|enable]
set ldb-method [static|round-robin|...]
set persistence [none|http-cookie]
config quic
Description: QUIC setting.
set ack-delay-exponent {integer}
set active-connection-id-limit {integer}
set active-migration [enable|disable]
FortiOS 8.0.0 CLI Reference
2957
Fortinet Inc.

<!-- 来源页 2958 -->
set grease-quic-bit [enable|disable]
set max-ack-delay {integer}
set max-datagram-frame-size {integer}
set max-idle-timeout {integer}
set max-udp-payload-size {integer}
end
config realservers
Description: Select the real servers that this ZTNA web-proxy will distribute
traffic to.
edit <id>
set addr-type [ip|fqdn]
set address {string}
set health-check [disable|enable]
set health-check-proto [ping|http|...]
set holddown-interval [enable|disable]
set http-host {string}
set ip {ipv6-address}
set port {integer}
set status [active|standby|...]
set translate-host [enable|disable]
set verify-cert [enable|disable]
set weight {integer}
next
end
set service [http|https]
set ssl-algorithm [high|medium|...]
config ssl-cipher-suites
Description: SSL/TLS cipher suites to offer to a server, ordered by priority.
edit <priority>
set cipher [TLS-AES-128-GCM-SHA256|TLS-AES-256-GCM-SHA384|...]
set versions {option1}, {option2}, ...
next
end
set ssl-dh-bits [768|1024|...]
set ssl-max-version [tls-1.0|tls-1.1|...]
set ssl-min-version [tls-1.0|tls-1.1|...]
set ssl-renegotiation [enable|disable]
set url-map {string}
set url-map-type [sub-string|wildcard|...]
next
end
set auth-portal [disable|enable]
set auth-virtual-host {string}
set decrypted-traffic-mirror {string}
set host {string}
set log-blocked-traffic [disable|enable]
set svr-pool-multiplex [enable|disable]
set svr-pool-server-max-concurrent-request {integer}
set svr-pool-server-max-request {integer}
set svr-pool-ttl {integer}
set vip {string}
set vip6 {string}
FortiOS 8.0.0 CLI Reference
2958
Fortinet Inc.

<!-- 来源页 2959 -->
next
end
config ztna web-proxy
Parameter
Description
Type
Size
Default
auth-portal *
Enable/disable authentication portal.
option
-disable
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
decrypted-traffic-mirror
Decrypted traffic mirror.
string
Maximum
length: 35
host
Virtual or real host name.
string
Maximum
length: 79
log-blocked-traffic *
Enable/disable logging of blocked traffic.
option
-enable
Option
Description
disable
Do not log all traffic denied by this ZTNA web-proxy.
enable
Log all traffic denied by this ZTNA web-proxy.
name
ZTNA web proxy name.
string
Maximum
length: 79
svr-pool-multiplex *
Enable/disable server pool multiplexing (default
= disable). Share connected server in HTTP and
HTTPS api-gateways.
option
-disable
Option
Description
enable
Enable server pool multiplexing. Share connected server.
disable
Disable server pool multiplexing. Do not share connected server.
svr-pool-server-max-concurrent-request *
Maximum number of concurrent requests that
servers in the server pool could handle (default
= unlimited).
integer
Minimum
value: 0
Maximum
value:
2147483647
0
FortiOS 8.0.0 CLI Reference
2959
Fortinet Inc.

<!-- 来源页 2960 -->
Parameter
Description
Type
Size
Default
svr-pool-server-max-request *
Maximum number of requests that servers in the
server pool handle before disconnecting
(default = unlimited).
integer
Minimum
value: 0
Maximum
value:
2147483647
0
svr-pool-ttl *
Time-to-live in the server pool for idle
connections to servers.
integer
Minimum
value: 0
Maximum
value:
2147483647
15
vip
Virtual IP name.
string
Maximum
length: 79
vip6
Virtual IPv6 name.
string
Maximum
length: 79
* This parameter may not exist in some models.
config api-gateway
Parameter
Description
Type
Size
Default
h2-support
HTTP2 support, default=Enable.
option
-enable
Option
Description
enable
Enable HTTP2 support.
disable
Disable HTTP2 support.
h3-support
HTTP3/QUIC support, default=Disable.
option
-disable
Option
Description
enable
Enable HTTP3/QUIC support.
disable
Disable HTTP3/QUIC support.
http-cookie-age
Time in minutes that client web browsers
should keep a cookie. Default is 60 minutes. 0
= no time limit.
integer
Minimum value:
0 Maximum
value: 525600
60
http-cookie-domain
Domain that HTTP cookie persistence should
apply to.
string
Maximum
length: 35
http-cookie-domain-from-host
Enable/disable use of HTTP cookie domain
from host field in HTTP.
option
-disable
FortiOS 8.0.0 CLI Reference
2960
Fortinet Inc.

<!-- 来源页 2961 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable use of HTTP cookie domain from the host field in HTTP (use
http-cooke-domain setting).
enable
Enable use of HTTP cookie domain from the host field in HTTP.
http-cookie-generation
Generation of HTTP cookie to be accepted.
Changing invalidates all existing cookies.
integer
Minimum value:
0 Maximum
value:
4294967295
0
http-cookie-path
Limit HTTP cookie persistence to the specified
path.
string
Maximum
length: 35
http-cookie-share
Control sharing of cookies across API
Gateway. Use of same-ip means a cookie from
one virtual server can be used by another.
Disable stops cookie sharing.
option
-same-ip
Option
Description
disable
Only allow HTTP cookie to match this API Gateway.
same-ip
Allow HTTP cookie to match any API Gateway with the same IP.
https-cookie-secure
Enable/disable verification that inserted
HTTPS cookies are secure.
option
-disable
Option
Description
disable
Do not mark the cookie as secure. Allows sharing the cookie between
HTTP and HTTPS connections.
enable
Mark the inserted cookie as secure. The cookie can only be used for
HTTPS connections.
id
API Gateway ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
ldb-method
Method used to distribute sessions to real
servers.
option
-static
Option
Description
static
Distribute to servers based on source IP.
round-robin
Distribute to servers based on round-robin order.
FortiOS 8.0.0 CLI Reference
2961
Fortinet Inc.

<!-- 来源页 2962 -->
Parameter
Description
Type
Size
Default
Option
Description
weighted
Distribute to servers based on weight.
first-alive
Distribute to the first server that is alive.
http-host
Distribute to servers based on the host field in HTTP header.
persistence
Configure how to make sure that clients
connect to the same server every time they
make a request that is part of the same
session.
option
-none
Option
Description
none
None.
http-cookie
HTTP cookie.
service
Service.
option
-https
Option
Description
http
HTTP.
https
HTTPS.
ssl-algorithm
Permitted encryption algorithms for the server
side of SSL full mode sessions according to
encryption strength.
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
ssl-dh-bits
Number of bits to use in the Diffie-Hellman
exchange for RSA encryption of SSL sessions.
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
FortiOS 8.0.0 CLI Reference
2962
Fortinet Inc.

<!-- 来源页 2963 -->
Parameter
Description
Type
Size
Default
ssl-max-version
Highest SSL/TLS version acceptable from a
server.
option
-tls-1.3
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
ssl-min-version
Lowest SSL/TLS version acceptable from a
server.
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
ssl-renegotiation
Enable/disable secure renegotiation to comply
with RFC 5746.
option
-enable
Option
Description
enable
Enable secure renegotiation.
disable
Disable secure renegotiation.
url-map
URL pattern to match.
string
Maximum
length: 511
/
url-map-type
Type of url-map.
option
-sub-string
Option
Description
sub-string
Match the pattern if a string contains the sub-string.
wildcard
Match the pattern with wildcards.
regex
Match the pattern with a regular expression.
FortiOS 8.0.0 CLI Reference
2963
Fortinet Inc.

<!-- 来源页 2964 -->
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
2964
Fortinet Inc.

<!-- 来源页 2965 -->
config realservers
Parameter
Description
Type
Size
Default
addr-type
Type of address.
option
-ip
Option
Description
ip
Standard IPv4 address.
fqdn
Non-wildcard FQDN address object.
address
Address or address group of the real server.
string
Maximum
length: 79
health-check
Enable to check the responsiveness of the real
server before forwarding traffic.
option
-disable
Option
Description
disable
Disable per server health check.
enable
Enable per server health check.
health-check-proto
Protocol of the health check monitor to use
when polling to determine server's connectivity
status.
option
-ping
Option
Description
ping
Use PING to test the link with the server.
http
Use HTTP-GET to test the link with the server.
tcp-connect
Use a full TCP connection to test the link with the server.
holddown-interval
Enable/disable holddown timer. Server will be
considered active and reachable once the
holddown period has expired (30 seconds).
option
-enable
Option
Description
enable
Enable per server holddown.
disable
Disable per server holddown.
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
FortiOS 8.0.0 CLI Reference
2965
Fortinet Inc.

<!-- 来源页 2966 -->
Parameter
Description
Type
Size
Default
ip
IP address of the real server.
ipv4-address-any
Not Specified
0.0.0.0
port
Port for communicating with the real server.
integer
Minimum value:
1 Maximum
value: 65535
443
status
Set the status of the real server to active so that
it can accept traffic, or on standby or disabled
so no traffic is sent.
option
-active
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
verify-cert
Enable/disable certificate verification of the real
server.
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
-FortiOS 8.0.0 CLI Reference
2966
Fortinet Inc.

<!-- 来源页 2967 -->
Parameter
Description
Type
Size
Default
Option
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
TLS-DHE-RSA-WITH-AES-128-CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-AES-128-CBC-SHA.
TLS-DHE-RSA-WITH-AES-256-CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-AES-256-CBC-SHA.
TLS-DHE-RSA-WITH-AES-128-CBC-SHA256
Cipher suite TLS-DHE-RSA-WITH-AES-128-CBC-SHA256.
TLS-DHE-RSA-WITH-AES-128-GCM-SHA256
Cipher suite TLS-DHE-RSA-WITH-AES-128-GCM-SHA256.
FortiOS 8.0.0 CLI Reference
2967
Fortinet Inc.

<!-- 来源页 2968 -->
Parameter
Description
Type
Size
Default
Option
Description
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
TLS-DHE-DSS-WITH-AES-256-GCM-SHA384
Cipher suite TLS-DHE-DSS-WITH-AES-256-GCM-SHA384.
TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA
Cipher suite TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA.
TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256
Cipher suite TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256.
FortiOS 8.0.0 CLI Reference
2968
Fortinet Inc.

<!-- 来源页 2969 -->
Parameter
Description
Type
Size
Default
Option
Description
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
TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256.
TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA.
TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384.
FortiOS 8.0.0 CLI Reference
2969
Fortinet Inc.

<!-- 来源页 2970 -->
Parameter
Description
Type
Size
Default
Option
Description
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
TLS-RSA-WITH-CAMELLIA-128-CBC-SHA
Cipher suite TLS-RSA-WITH-CAMELLIA-128-CBC-SHA.
TLS-RSA-WITH-CAMELLIA-256-CBC-SHA
Cipher suite TLS-RSA-WITH-CAMELLIA-256-CBC-SHA.
TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256
Cipher suite TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256.
FortiOS 8.0.0 CLI Reference
2970
Fortinet Inc.

<!-- 来源页 2971 -->
Parameter
Description
Type
Size
Default
Option
Description
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
TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256
Cipher suite TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256.
TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256
Cipher suite TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256.
TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256
Cipher suite TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256.
FortiOS 8.0.0 CLI Reference
2971
Fortinet Inc.

<!-- 来源页 2972 -->
Parameter
Description
Type
Size
Default
Option
Description
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
TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384
Cipher suite TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384.
TLS-RSA-WITH-SEED-CBC-SHA
Cipher suite TLS-RSA-WITH-SEED-CBC-SHA.
TLS-RSA-WITH-ARIA-128-CBC-SHA256
Cipher suite TLS-RSA-WITH-ARIA-128-CBC-SHA256.
TLS-RSA-WITH-ARIA-256-CBC-SHA384
Cipher suite TLS-RSA-WITH-ARIA-256-CBC-SHA384.
FortiOS 8.0.0 CLI Reference
2972
Fortinet Inc.

<!-- 来源页 2973 -->
Parameter
Description
Type
Size
Default
Option
Description
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
FortiOS 8.0.0 CLI Reference
2973
Fortinet Inc.

<!-- 来源页 2974 -->
Parameter
Description
Type
Size
Default
Option
Description
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
-tls-1.0 tls-1.1 tls-1.2
tls-1.3
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
config api-gateway6
Parameter
Description
Type
Size
Default
h2-support
HTTP2 support, default=Enable.
option
-enable
Option
Description
enable
Enable HTTP2 support.
disable
Disable HTTP2 support.
h3-support
HTTP3/QUIC support, default=Disable.
option
-disable
Option
Description
enable
Enable HTTP3/QUIC support.
disable
Disable HTTP3/QUIC support.
http-cookie-age
Time in minutes that client web browsers
should keep a cookie. Default is 60 minutes. 0
= no time limit.
integer
Minimum value:
0 Maximum
value: 525600
60
FortiOS 8.0.0 CLI Reference
2974
Fortinet Inc.

<!-- 来源页 2975 -->
Parameter
Description
Type
Size
Default
http-cookie-domain
Domain that HTTP cookie persistence should
apply to.
string
Maximum
length: 35
http-cookie-domain-from-host
Enable/disable use of HTTP cookie domain
from host field in HTTP.
option
-disable
Option
Description
disable
Disable use of HTTP cookie domain from the host field in HTTP (use
http-cooke-domain setting).
enable
Enable use of HTTP cookie domain from the host field in HTTP.
http-cookie-generation
Generation of HTTP cookie to be accepted.
Changing invalidates all existing cookies.
integer
Minimum value:
0 Maximum
value:
4294967295
0
http-cookie-path
Limit HTTP cookie persistence to the specified
path.
string
Maximum
length: 35
http-cookie-share
Control sharing of cookies across API
Gateway. Use of same-ip means a cookie from
one virtual server can be used by another.
Disable stops cookie sharing.
option
-same-ip
Option
Description
disable
Only allow HTTP cookie to match this API Gateway.
same-ip
Allow HTTP cookie to match any API Gateway with the same IP.
https-cookie-secure
Enable/disable verification that inserted
HTTPS cookies are secure.
option
-disable
Option
Description
disable
Do not mark the cookie as secure. Allows sharing the cookie between
HTTP and HTTPS connections.
enable
Mark the inserted cookie as secure. The cookie can only be used for
HTTPS connections.
id
API Gateway ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
ldb-method
Method used to distribute sessions to real
servers.
option
-static
FortiOS 8.0.0 CLI Reference
2975
Fortinet Inc.

<!-- 来源页 2976 -->
Parameter
Description
Type
Size
Default
Option
Description
static
Distribute to servers based on source IP.
round-robin
Distribute to servers based on round-robin order.
weighted
Distribute to servers based on weight.
first-alive
Distribute to the first server that is alive.
http-host
Distribute to servers based on the host field in HTTP header.
persistence
Configure how to make sure that clients
connect to the same server every time they
make a request that is part of the same
session.
option
-none
Option
Description
none
None.
http-cookie
HTTP cookie.
service
Service.
option
-https
Option
Description
http
HTTP.
https
HTTPS.
ssl-algorithm
Permitted encryption algorithms for the server
side of SSL full mode sessions according to
encryption strength.
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
ssl-dh-bits
Number of bits to use in the Diffie-Hellman
exchange for RSA encryption of SSL sessions.
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
FortiOS 8.0.0 CLI Reference
2976
Fortinet Inc.

<!-- 来源页 2977 -->
Parameter
Description
Type
Size
Default
Option
Description
2048
2048-bit Diffie-Hellman prime.
3072
3072-bit Diffie-Hellman prime.
4096
4096-bit Diffie-Hellman prime.
ssl-max-version
Highest SSL/TLS version acceptable from a
server.
option
-tls-1.3
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
ssl-min-version
Lowest SSL/TLS version acceptable from a
server.
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
ssl-renegotiation
Enable/disable secure renegotiation to comply
with RFC 5746.
option
-enable
Option
Description
enable
Enable secure renegotiation.
disable
Disable secure renegotiation.
url-map
URL pattern to match.
string
Maximum
length: 511
/
url-map-type
Type of url-map.
option
-sub-string
Option
Description
sub-string
Match the pattern if a string contains the sub-string.
wildcard
Match the pattern with wildcards.
regex
Match the pattern with a regular expression.
FortiOS 8.0.0 CLI Reference
2977
Fortinet Inc.

<!-- 来源页 2978 -->
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
2978
Fortinet Inc.

<!-- 来源页 2979 -->
config realservers
Parameter
Description
Type
Size
Default
addr-type
Type of address.
option
-ip
Option
Description
ip
Standard IPv4 address.
fqdn
Non-wildcard FQDN address object.
address
Address or address group of the real server.
string
Maximum
length: 79
health-check
Enable to check the responsiveness of the real
server before forwarding traffic.
option
-disable
Option
Description
disable
Disable per server health check.
enable
Enable per server health check.
health-check-proto
Protocol of the health check monitor to use
when polling to determine server's connectivity
status.
option
-ping
Option
Description
ping
Use PING to test the link with the server.
http
Use HTTP-GET to test the link with the server.
tcp-connect
Use a full TCP connection to test the link with the server.
holddown-interval
Enable/disable holddown timer. Server will be
considered active and reachable once the
holddown period has expired (30 seconds).
option
-enable
Option
Description
enable
Enable per server holddown.
disable
Disable per server holddown.
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
IPv6 address of the real server.
ipv6-address
Not Specified
::
FortiOS 8.0.0 CLI Reference
2979
Fortinet Inc.

<!-- 来源页 2980 -->
Parameter
Description
Type
Size
Default
port
Port for communicating with the real server.
integer
Minimum value:
1 Maximum
value: 65535
443
status
Set the status of the real server to active so that
it can accept traffic, or on standby or disabled
so no traffic is sent.
option
-active
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
verify-cert
Enable/disable certificate verification of the real
server.
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
balancing is enabled, the server with the highest
weight gets more connections.
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
2980
Fortinet Inc.

<!-- 来源页 2981 -->
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
2981
Fortinet Inc.

<!-- 来源页 2982 -->
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
2982
Fortinet Inc.

<!-- 来源页 2983 -->
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
2983
Fortinet Inc.

<!-- 来源页 2984 -->
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
2984
Fortinet Inc.

<!-- 来源页 2985 -->
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
2985
Fortinet Inc.

<!-- 来源页 2986 -->
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
2986
Fortinet Inc.

<!-- 来源页 2987 -->
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
2987
Fortinet Inc.

<!-- 来源页 2988 -->
Parameter
Description
Type
Size
Default
versions
SSL/TLS versions that the cipher suite can be
used with.
option
-tls-1.0 tls-1.1 tls-1.2
tls-1.3
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
FortiOS 8.0.0 CLI Reference
2988
Fortinet Inc.
