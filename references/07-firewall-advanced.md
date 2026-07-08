# 防火墙：多播/接口策略/本地策略/DoS/限速/嗅探/反向代理

> 来源: FortiOS-8.0.0-CLI_Reference.pdf
> 覆盖命令/章节: config firewall multicast-policy, config firewall multicast-policy6, config firewall multicast-address, config firewall multicast-address6, config firewall interface-policy, config firewall interface-policy6, config firewall local-in-policy, config firewall local-in-policy6, config firewall DoS-policy, config firewall DoS-policy6, config firewall ttl-policy, config firewall shaping-policy, config firewall shaping-profile, config firewall shaper per-ip-shaper, config firewall shaper traffic-shaper, config firewall sniffer, config firewall on-demand-sniffer, config firewall access-proxy, config firewall access-proxy6, config firewall access-proxy-ssh-client-cert, config firewall access-proxy-virtual-host, config firewall ssl setting, config firewall ssh setting, config firewall ipmacbinding setting, config firewall ipmacbinding table, config firewall identity-based-route, config firewall auth-portal, config firewall decrypted-traffic-mirror
> 本文件由 extract_pdf.py 从官方 PDF 自动提取，请勿手动编辑；
> 如需修正请修改 map.json 后重跑脚本。

---


<!-- 来源页 396 -->
l config firewall ssh local-ca on page 715
l config firewall ssh local-key on page 716
l config firewall ssh setting on page 717
l config firewall ssl-server on page 720
l config firewall ssl-ssh-profile on page 723
l config firewall ssl setting on page 718
l config firewall traffic-class on page 755
l config firewall ttl-policy on page 756
l config firewall vendor-mac on page 757
l config firewall vip on page 758
l config firewall vip6 on page 796
l config firewall vipgrp on page 831
l config firewall vipgrp6 on page 831
l config firewall wildcard-fqdn custom on page 832
l config firewall wildcard-fqdn group on page 833
config firewall DoS-policy
Configure IPv4 DoS policies.
config firewall DoS-policy
Description: Configure IPv4 DoS policies.
edit <policyid>
config anomaly
Description: Anomaly name.
edit <name>
set action [pass|block]
set log [enable|disable]
set quarantine [none|attacker]
set quarantine-expiry {user}
set quarantine-log [disable|enable]
set status [disable|enable]
set threshold {integer}
set threshold(default) {integer}
next
end
set comments {var-string}
set custom-tags <name1>, <name2>, ...
set dstaddr <name1>, <name2>, ...
set interface {string}
set name {string}
set service <name1>, <name2>, ...
set srcaddr <name1>, <name2>, ...
set status [enable|disable]
next
end
FortiOS 8.0.0 CLI Reference
396
Fortinet Inc.

<!-- 来源页 397 -->
config firewall DoS-policy
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
custom-tags
<name> *
Custom tags.
Names of custom tags used with this policy.
string
Maximum
length: 35
dstaddr
<name>
Destination address name from available
addresses.
Address name.
string
Maximum
length: 79
interface
Incoming interface name from available interfaces.
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
**
0
service
<name>
Service object from available options.
Service name.
string
Maximum
length: 79
srcaddr
<name>
Source address name from available addresses.
Address name.
string
Maximum
length: 79
status
Enable/disable this policy.
option
-enable
Option
Description
enable
Enable this policy.
disable
Disable this policy.
* This parameter may not exist in some models.
** Values may differ between models.
config anomaly
Parameter
Description
Type
Size
Default
action
Action taken when the threshold is reached.
option
-pass
FortiOS 8.0.0 CLI Reference
397
Fortinet Inc.

<!-- 来源页 398 -->
Parameter
Description
Type
Size
Default
Option
Description
pass
Allow traffic but record a log message if logging is enabled.
block
Block traffic if this anomaly is found.
log
Enable/disable anomaly logging.
option
-disable
Option
Description
enable
Enable anomaly logging.
disable
Disable anomaly logging.
name
Anomaly name.
string
Maximum
length: 63
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
Duration of quarantine. (Format ###d##h##m,
minimum 1m, maximum 364d23h59m, default =
5m). Requires quarantine set to attacker.
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
status
Enable/disable this anomaly.
option
-disable
Option
Description
disable
Disable this status.
enable
Enable this status.
threshold
Anomaly threshold. Number of detected
instances (packets per second or concurrent
session number) that triggers the anomaly
action.
integer
Minimum value:
1 Maximum
value:
2147483647
0
FortiOS 8.0.0 CLI Reference
398
Fortinet Inc.

---


<!-- 来源页 399 -->
Parameter
Description
Type
Size
Default
threshold
(default)
Number of detected instances (packets per
second or concurrent session number) which
triggers action (1 - 2147483647, default =
1000). Note that each anomaly has a different
threshold value assigned to it. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config firewall DoS-policy6
Configure IPv6 DoS policies.
config firewall DoS-policy6
Description: Configure IPv6 DoS policies.
edit <policyid>
config anomaly
Description: Anomaly name.
edit <name>
set action [pass|block]
set log [enable|disable]
set quarantine [none|attacker]
set quarantine-expiry {user}
set quarantine-log [disable|enable]
set status [disable|enable]
set threshold {integer}
set threshold(default) {integer}
next
end
set comments {var-string}
set custom-tags <name1>, <name2>, ...
set dstaddr <name1>, <name2>, ...
set interface {string}
set name {string}
set service <name1>, <name2>, ...
set srcaddr <name1>, <name2>, ...
set status [enable|disable]
next
end
config firewall DoS-policy6
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
FortiOS 8.0.0 CLI Reference
399
Fortinet Inc.

<!-- 来源页 400 -->
Parameter
Description
Type
Size
Default
custom-tags
<name> *
Custom tags.
Names of custom tags used with this policy.
string
Maximum
length: 35
dstaddr
<name>
Destination address name from available
addresses.
Address name.
string
Maximum
length: 79
interface
Incoming interface name from available interfaces.
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
**
0
service
<name>
Service object from available options.
Service name.
string
Maximum
length: 79
srcaddr
<name>
Source address name from available addresses.
Address name.
string
Maximum
length: 79
status
Enable/disable this policy.
option
-enable
Option
Description
enable
Enable this policy.
disable
Disable this policy.
* This parameter may not exist in some models.
** Values may differ between models.
config anomaly
Parameter
Description
Type
Size
Default
action
Action taken when the threshold is reached.
option
-pass
Option
Description
pass
Allow traffic but record a log message if logging is enabled.
block
Block traffic if this anomaly is found.
log
Enable/disable anomaly logging.
option
-disable
FortiOS 8.0.0 CLI Reference
400
Fortinet Inc.

<!-- 来源页 401 -->
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
name
Anomaly name.
string
Maximum
length: 63
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
Duration of quarantine. (Format ###d##h##m,
minimum 1m, maximum 364d23h59m, default =
5m). Requires quarantine set to attacker.
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
status
Enable/disable this anomaly.
option
-disable
Option
Description
disable
Disable this status.
enable
Enable this status.
threshold
Anomaly threshold. Number of detected
instances (packets per second or concurrent
session number) that triggers the anomaly
action.
integer
Minimum value:
1 Maximum
value:
2147483647
0
threshold
(default)
Number of detected instances (packets per
second or concurrent session number) which
triggers action (1 - 2147483647, default =
1000). Note that each anomaly has a different
threshold value assigned to it. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
FortiOS 8.0.0 CLI Reference
401
Fortinet Inc.

---


<!-- 来源页 402 -->
config firewall access-proxy
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
Configure IPv4 access proxy.
config firewall access-proxy
Description: Configure IPv4 access proxy.
edit <name>
set add-vhost-domain-to-dnsdb [enable|disable]
config api-gateway
Description: Set IPv4 API Gateway.
edit <id>
set application <name1>, <name2>, ...
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
FortiOS 8.0.0 CLI Reference
402
Fortinet Inc.

<!-- 来源页 403 -->
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
Description: Select the real servers that this Access Proxy will distribute
traffic to.
edit <id>
set addr-type [ip|fqdn]
set address {string}
set domain {string}
set external-auth [enable|disable]
set health-check [disable|enable]
set health-check-proto [ping|http|...]
set holddown-interval [enable|disable]
set http-host {string}
set ip {ipv4-address-any}
set mappedport {user}
set port {integer}
set ssh-client-cert {string}
set ssh-host-key <name1>, <name2>, ...
set ssh-host-key-validation [disable|enable]
set status [active|standby|...]
set translate-host [enable|disable]
set tunnel-encryption [enable|disable]
set type [tcp-forwarding|ssh]
set verify-cert [enable|disable]
set weight {integer}
next
end
set saml-redirect [disable|enable]
set saml-server {string}
set service [http|https|...]
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
FortiOS 8.0.0 CLI Reference
403
Fortinet Inc.

<!-- 来源页 404 -->
set ssl-vpn-web-portal {string}
set url-map {string}
set url-map-type [sub-string|wildcard|...]
set virtual-host {string}
next
end
config api-gateway6
Description: Set IPv6 API Gateway.
edit <id>
set application <name1>, <name2>, ...
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
Description: Select the real servers that this Access Proxy will distribute
traffic to.
edit <id>
set addr-type [ip|fqdn]
set address {string}
set domain {string}
set external-auth [enable|disable]
set health-check [disable|enable]
set health-check-proto [ping|http|...]
set holddown-interval [enable|disable]
set http-host {string}
set ip {ipv6-address}
set mappedport {user}
set port {integer}
set ssh-client-cert {string}
set ssh-host-key <name1>, <name2>, ...
set ssh-host-key-validation [disable|enable]
set status [active|standby|...]
set translate-host [enable|disable]
FortiOS 8.0.0 CLI Reference
404
Fortinet Inc.

<!-- 来源页 405 -->
set tunnel-encryption [enable|disable]
set type [tcp-forwarding|ssh]
set verify-cert [enable|disable]
set weight {integer}
next
end
set saml-redirect [disable|enable]
set saml-server {string}
set service [http|https|...]
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
set ssl-vpn-web-portal {string}
set url-map {string}
set url-map-type [sub-string|wildcard|...]
set virtual-host {string}
next
end
set auth-portal [disable|enable]
set auth-virtual-host {string}
set decrypted-traffic-mirror {string}
set log-blocked-traffic [enable|disable]
set svr-pool-multiplex [enable|disable]
set svr-pool-server-max-concurrent-request {integer}
set svr-pool-server-max-request {integer}
set svr-pool-ttl {integer}
set vip {string}
next
end
config firewall access-proxy
Parameter
Description
Type
Size
Default
add-vhost-domain-to-dnsdb
Enable/disable adding vhost/domain to dnsdb
for ztna dox tunnel.
option
-disable
FortiOS 8.0.0 CLI Reference
405
Fortinet Inc.

<!-- 来源页 406 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
add dns entry for all vhosts used by access proxy.
disable
Do not add dns entry for all vhosts used by access proxy.
auth-portal
Enable/disable authentication portal.
option
-disable
Option
Description
disable
Disable authentication portal.
enable
Enable authentication portal.
auth-virtual-host
Virtual host for authentication portal.
string
Maximum
length: 79
decrypted-traffic-mirror
Decrypted traffic mirror.
string
Maximum
length: 35
log-blocked-traffic
Enable/disable logging of blocked traffic.
option
-enable
Option
Description
enable
Log all traffic denied by this access proxy.
disable
Do not log all traffic denied by this access proxy.
name
Access Proxy name.
string
Maximum
length: 79
svr-pool-multiplex
Enable/disable server pool multiplexing (default
= disable). Share connected server in HTTP,
HTTPS, and web-portal api-gateway.
option
-disable
Option
Description
enable
Enable server pool multiplexing. Share connected server.
disable
Disable server pool multiplexing. Do not share connected server.
svr-pool-server-max-concurrent-request
Maximum number of concurrent requests that
servers in server pool could handle (default =
unlimited).
integer
Minimum
value: 0
Maximum
value:
2147483647
0
FortiOS 8.0.0 CLI Reference
406
Fortinet Inc.

<!-- 来源页 407 -->
Parameter
Description
Type
Size
Default
svr-pool-server-max-request
Maximum number of requests that servers in
server pool handle before disconnecting
(default = unlimited).
integer
Minimum
value: 0
Maximum
value:
2147483647
0
svr-pool-ttl
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
config api-gateway
Parameter
Description
Type
Size
Default
application
<name>
SaaS application controlled by this Access
Proxy.
SaaS application name.
string
Maximum
length: 79
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
407
Fortinet Inc.

<!-- 来源页 408 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable use of HTTP cookie domain from host field in HTTP (use http-cooke-domain setting).
enable
Enable use of HTTP cookie domain from host field in HTTP.
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
Allow HTTP cookie to match any API Gateway with same IP.
https-cookie-secure
Enable/disable verification that inserted
HTTPS cookies are secure.
option
-disable
Option
Description
disable
Do not mark cookie as secure, allow sharing between an HTTP and
HTTPS connection.
enable
Mark inserted cookie as secure, cookie can only be used for HTTPS a
connection.
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
Distribute to server based on source IP.
round-robin
Distribute to server based round robin order.
FortiOS 8.0.0 CLI Reference
408
Fortinet Inc.

<!-- 来源页 409 -->
Parameter
Description
Type
Size
Default
Option
Description
weighted
Distribute to server based on weight.
first-alive
Distribute to the first server that is alive.
http-host
Distribute to server based on host field in HTTP header.
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
saml-redirect
Enable/disable SAML redirection after
successful authentication.
option
-enable
Option
Description
disable
Do not support redirection after successful SAML authentication.
enable
Support redirection after successful SAML authentication.
saml-server
SAML service provider configuration for VIP
authentication.
string
Maximum
length: 35
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
tcp-forwarding
TCP-FORWARDING.
samlsp
SAML-SP.
web-portal
VPN-SSL-WEB-PORTAL.
saas
SAAS.
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
FortiOS 8.0.0 CLI Reference
409
Fortinet Inc.

<!-- 来源页 410 -->
Parameter
Description
Type
Size
Default
Option
Description
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
FortiOS 8.0.0 CLI Reference
410
Fortinet Inc.

<!-- 来源页 411 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable secure renegotiation.
disable
Disable secure renegotiation.
ssl-vpn-web-portal
Agentless VPN web portal.
string
Maximum
length: 35
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
virtual-host
Virtual host.
string
Maximum
length: 79
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
FortiOS 8.0.0 CLI Reference
411
Fortinet Inc.

<!-- 来源页 412 -->
Parameter
Description
Type
Size
Default
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
domain
Wildcard domain name of the real server.
string
Maximum
length: 255
external-auth
Enable/disable use of external browser as
user-agent for SAML user authentication.
option
-disable
FortiOS 8.0.0 CLI Reference
412
Fortinet Inc.

<!-- 来源页 413 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable use of external browser as user-agent for SAML user
authentication.
disable
Disable use of external browser as user-agent for SAML user
authentication.
health-check
Enable to check the responsiveness of the
real server before forwarding traffic.
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
when polling to determine server's
connectivity status.
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
Enable/disable holddown timer. Server will
be considered active and reachable once the
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
IP address of the real server.
ipv4-address-any
Not Specified
0.0.0.0
mappedport
Port for communicating with the real server.
user
Not Specified
FortiOS 8.0.0 CLI Reference
413
Fortinet Inc.

<!-- 来源页 414 -->
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
ssh-client-cert
Set access-proxy SSH client certificate
profile.
string
Maximum
length: 79
ssh-host-key
<name>
One or more server host key.
Server host key name.
string
Maximum
length: 79
ssh-host-key-validation
Enable/disable SSH real server host key
validation.
option
-disable
Option
Description
disable
Disable SSH real server host key validation.
enable
Enable SSH real server host key validation.
status
Set the status of the real server to active so
that it can accept traffic, or on standby or
disabled so no traffic is sent.
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
Enable/disable translation of hostname/IP
from virtual server to real server.
option
-enable
Option
Description
enable
Enable virtual hostname/IP translation.
disable
Disable virtual hostname/IP translation.
tunnel-encryption
Tunnel encryption.
option
-disable
Option
Description
enable
Enable tcp forwarding tunnel encryption.
disable
Disable tcp forwarding tunnel encryption.
type
TCP forwarding server type.
option
-tcp-forwarding
FortiOS 8.0.0 CLI Reference
414
Fortinet Inc.

<!-- 来源页 415 -->
Parameter
Description
Type
Size
Default
Option
Description
tcp-forwarding
TCP forwarding.
ssh
SSH.
verify-cert
Enable/disable certificate verification of the
real server.
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
-Option
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
FortiOS 8.0.0 CLI Reference
415
Fortinet Inc.

<!-- 来源页 416 -->
Parameter
Description
Type
Size
Default
Option
Description
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
TLS-DHE-DSS-WITH-AES-128-CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-AES-128-CBC-SHA.
TLS-DHE-DSS-WITH-AES-256-CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-AES-256-CBC-SHA.
TLS-DHE-DSS-WITH-AES-128-CBC-SHA256
Cipher suite TLS-DHE-DSS-WITH-AES-128-CBC-SHA256.
TLS-DHE-DSS-WITH-AES-128-GCM-SHA256
Cipher suite TLS-DHE-DSS-WITH-AES-128-GCM-SHA256.
FortiOS 8.0.0 CLI Reference
416
Fortinet Inc.

<!-- 来源页 417 -->
Parameter
Description
Type
Size
Default
Option
Description
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
TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384
Cipher suite TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384.
TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384
Cipher suite TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384.
TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA.
FortiOS 8.0.0 CLI Reference
417
Fortinet Inc.

<!-- 来源页 418 -->
Parameter
Description
Type
Size
Default
Option
Description
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
TLS-RSA-WITH-AES-128-CBC-SHA256
Cipher suite TLS-RSA-WITH-AES-128-CBC-SHA256.
TLS-RSA-WITH-AES-128-GCM-SHA256
Cipher suite TLS-RSA-WITH-AES-128-GCM-SHA256.
TLS-RSA-WITH-AES-256-CBC-SHA256
Cipher suite TLS-RSA-WITH-AES-256-CBC-SHA256.
FortiOS 8.0.0 CLI Reference
418
Fortinet Inc.

<!-- 来源页 419 -->
Parameter
Description
Type
Size
Default
Option
Description
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
TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA
Cipher suite TLS-DSS-RSA-WITH-CAMELLIA-128-CBC-SHA.
TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA.
FortiOS 8.0.0 CLI Reference
419
Fortinet Inc.

<!-- 来源页 420 -->
Parameter
Description
Type
Size
Default
Option
Description
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
TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256
Cipher suite TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256.
TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384
Cipher suite TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384.
FortiOS 8.0.0 CLI Reference
420
Fortinet Inc.

<!-- 来源页 421 -->
Parameter
Description
Type
Size
Default
Option
Description
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
TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC-SHA384
Cipher suite TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC_SHA384.
TLS-ECDHE-RSA-WITH-RC4-128-SHA
Cipher suite TLS-ECDHE-RSA-WITH-RC4-128-SHA.
FortiOS 8.0.0 CLI Reference
421
Fortinet Inc.

<!-- 来源页 422 -->
Parameter
Description
Type
Size
Default
Option
Description
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
422
Fortinet Inc.

<!-- 来源页 423 -->
config api-gateway6
Parameter
Description
Type
Size
Default
application
<name>
SaaS application controlled by this Access
Proxy.
SaaS application name.
string
Maximum
length: 79
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
Option
Description
disable
Disable use of HTTP cookie domain from host field in HTTP (use http-cooke-domain setting).
enable
Enable use of HTTP cookie domain from host field in HTTP.
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
FortiOS 8.0.0 CLI Reference
423
Fortinet Inc.

<!-- 来源页 424 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Only allow HTTP cookie to match this API Gateway.
same-ip
Allow HTTP cookie to match any API Gateway with same IP.
https-cookie-secure
Enable/disable verification that inserted
HTTPS cookies are secure.
option
-disable
Option
Description
disable
Do not mark cookie as secure, allow sharing between an HTTP and
HTTPS connection.
enable
Mark inserted cookie as secure, cookie can only be used for HTTPS a
connection.
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
Distribute to server based on source IP.
round-robin
Distribute to server based round robin order.
weighted
Distribute to server based on weight.
first-alive
Distribute to the first server that is alive.
http-host
Distribute to server based on host field in HTTP header.
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
saml-redirect
Enable/disable SAML redirection after
successful authentication.
option
-enable
FortiOS 8.0.0 CLI Reference
424
Fortinet Inc.

<!-- 来源页 425 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Do not support redirection after successful SAML authentication.
enable
Support redirection after successful SAML authentication.
saml-server
SAML service provider configuration for VIP
authentication.
string
Maximum
length: 35
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
tcp-forwarding
TCP-FORWARDING.
samlsp
SAML-SP.
web-portal
VPN-SSL-WEB-PORTAL.
saas
SAAS.
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
425
Fortinet Inc.

<!-- 来源页 426 -->
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
ssl-vpn-web-portal
Agentless VPN web portal.
string
Maximum
length: 35
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
virtual-host
Virtual host.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
426
Fortinet Inc.

<!-- 来源页 427 -->
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
427
Fortinet Inc.

<!-- 来源页 428 -->
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
domain
Wildcard domain name of the real server.
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
health-check
Enable to check the responsiveness of the
real server before forwarding traffic.
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
when polling to determine server's
connectivity status.
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
FortiOS 8.0.0 CLI Reference
428
Fortinet Inc.

<!-- 来源页 429 -->
Parameter
Description
Type
Size
Default
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
mappedport
Port for communicating with the real server.
user
Not Specified
port
Port for communicating with the real server.
integer
Minimum value:
1 Maximum
value: 65535
443
ssh-client-cert
Set access-proxy SSH client certificate
profile.
string
Maximum
length: 79
ssh-host-key
<name>
One or more server host key.
Server host key name.
string
Maximum
length: 79
ssh-host-key-validation
Enable/disable SSH real server host key
validation.
option
-disable
Option
Description
disable
Disable SSH real server host key validation.
enable
Enable SSH real server host key validation.
status
Set the status of the real server to active so
that it can accept traffic, or on standby or
disabled so no traffic is sent.
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
Enable/disable translation of hostname/IP
from virtual server to real server.
option
-enable
FortiOS 8.0.0 CLI Reference
429
Fortinet Inc.

<!-- 来源页 430 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable virtual hostname/IP translation.
disable
Disable virtual hostname/IP translation.
tunnel-encryption
Tunnel encryption.
option
-disable
Option
Description
enable
Enable tcp forwarding tunnel encryption.
disable
Disable tcp forwarding tunnel encryption.
type
TCP forwarding server type.
option
-tcp-forwarding
Option
Description
tcp-forwarding
TCP forwarding.
ssh
SSH.
verify-cert
Enable/disable certificate verification of the
real server.
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
-Option
Description
TLS-AES-128-GCM-SHA256
Cipher suite TLS-AES-128-GCM-SHA256.
TLS-AES-256-GCM-SHA384
Cipher suite TLS-AES-256-GCM-SHA384.
FortiOS 8.0.0 CLI Reference
430
Fortinet Inc.

<!-- 来源页 431 -->
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
431
Fortinet Inc.

<!-- 来源页 432 -->
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
432
Fortinet Inc.

<!-- 来源页 433 -->
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
433
Fortinet Inc.

<!-- 来源页 434 -->
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
434
Fortinet Inc.

<!-- 来源页 435 -->
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
435
Fortinet Inc.

<!-- 来源页 436 -->
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
436
Fortinet Inc.

<!-- 来源页 437 -->
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
437
Fortinet Inc.

---


<!-- 来源页 438 -->
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
config firewall access-proxy6
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
Configure IPv6 access proxy.
config firewall access-proxy6
Description: Configure IPv6 access proxy.
FortiOS 8.0.0 CLI Reference
438
Fortinet Inc.

<!-- 来源页 439 -->
edit <name>
set add-vhost-domain-to-dnsdb [enable|disable]
config api-gateway
Description: Set IPv4 API Gateway.
edit <id>
set application <name1>, <name2>, ...
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
Description: Select the real servers that this Access Proxy will distribute
traffic to.
edit <id>
set addr-type [ip|fqdn]
set address {string}
set domain {string}
set external-auth [enable|disable]
set health-check [disable|enable]
set health-check-proto [ping|http|...]
set holddown-interval [enable|disable]
set http-host {string}
set ip {ipv4-address-any}
set mappedport {user}
set port {integer}
set ssh-client-cert {string}
set ssh-host-key <name1>, <name2>, ...
set ssh-host-key-validation [disable|enable]
set status [active|standby|...]
set translate-host [enable|disable]
set tunnel-encryption [enable|disable]
set type [tcp-forwarding|ssh]
set verify-cert [enable|disable]
set weight {integer}
FortiOS 8.0.0 CLI Reference
439
Fortinet Inc.

<!-- 来源页 440 -->
next
end
set saml-redirect [disable|enable]
set saml-server {string}
set service [http|https|...]
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
set ssl-vpn-web-portal {string}
set url-map {string}
set url-map-type [sub-string|wildcard|...]
set virtual-host {string}
next
end
config api-gateway6
Description: Set IPv6 API Gateway.
edit <id>
set application <name1>, <name2>, ...
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
Description: Select the real servers that this Access Proxy will distribute
traffic to.
FortiOS 8.0.0 CLI Reference
440
Fortinet Inc.

<!-- 来源页 441 -->
edit <id>
set addr-type [ip|fqdn]
set address {string}
set domain {string}
set external-auth [enable|disable]
set health-check [disable|enable]
set health-check-proto [ping|http|...]
set holddown-interval [enable|disable]
set http-host {string}
set ip {ipv6-address}
set mappedport {user}
set port {integer}
set ssh-client-cert {string}
set ssh-host-key <name1>, <name2>, ...
set ssh-host-key-validation [disable|enable]
set status [active|standby|...]
set translate-host [enable|disable]
set tunnel-encryption [enable|disable]
set type [tcp-forwarding|ssh]
set verify-cert [enable|disable]
set weight {integer}
next
end
set saml-redirect [disable|enable]
set saml-server {string}
set service [http|https|...]
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
set ssl-vpn-web-portal {string}
set url-map {string}
set url-map-type [sub-string|wildcard|...]
set virtual-host {string}
next
end
set auth-portal [disable|enable]
set auth-virtual-host {string}
set decrypted-traffic-mirror {string}
set log-blocked-traffic [enable|disable]
set svr-pool-multiplex [enable|disable]
set svr-pool-server-max-concurrent-request {integer}
set svr-pool-server-max-request {integer}
set svr-pool-ttl {integer}
FortiOS 8.0.0 CLI Reference
441
Fortinet Inc.

<!-- 来源页 442 -->
set vip {string}
next
end
config firewall access-proxy6
Parameter
Description
Type
Size
Default
add-vhost-domain-to-dnsdb
Enable/disable adding vhost/domain to dnsdb
for ztna dox tunnel.
option
-disable
Option
Description
enable
add dns entry for all vhosts used by access proxy.
disable
Do not add dns entry for all vhosts used by access proxy.
auth-portal
Enable/disable authentication portal.
option
-disable
Option
Description
disable
Disable authentication portal.
enable
Enable authentication portal.
auth-virtual-host
Virtual host for authentication portal.
string
Maximum
length: 79
decrypted-traffic-mirror
Decrypted traffic mirror.
string
Maximum
length: 35
log-blocked-traffic
Enable/disable logging of blocked traffic.
option
-enable
Option
Description
enable
Log all traffic denied by this access proxy.
disable
Do not log all traffic denied by this access proxy.
name
Access Proxy name.
string
Maximum
length: 79
svr-pool-multiplex
Enable/disable server pool multiplexing (default
= disable). Share connected server in HTTP,
HTTPS, and web-portal api-gateway.
option
-disable
Option
Description
enable
Enable server pool multiplexing. Share connected server.
disable
Disable server pool multiplexing. Do not share connected server.
FortiOS 8.0.0 CLI Reference
442
Fortinet Inc.

<!-- 来源页 443 -->
Parameter
Description
Type
Size
Default
svr-pool-server-max-concurrent-request
Maximum number of concurrent requests that
servers in server pool could handle (default =
unlimited).
integer
Minimum
value: 0
Maximum
value:
2147483647
0
svr-pool-server-max-request
Maximum number of requests that servers in
server pool handle before disconnecting
(default = unlimited).
integer
Minimum
value: 0
Maximum
value:
2147483647
0
svr-pool-ttl
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
config api-gateway
Parameter
Description
Type
Size
Default
application
<name>
SaaS application controlled by this Access
Proxy.
SaaS application name.
string
Maximum
length: 79
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
FortiOS 8.0.0 CLI Reference
443
Fortinet Inc.

<!-- 来源页 444 -->
Parameter
Description
Type
Size
Default
http-cookie-domain-from-host
Enable/disable use of HTTP cookie domain
from host field in HTTP.
option
-disable
Option
Description
disable
Disable use of HTTP cookie domain from host field in HTTP (use http-cooke-domain setting).
enable
Enable use of HTTP cookie domain from host field in HTTP.
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
Allow HTTP cookie to match any API Gateway with same IP.
https-cookie-secure
Enable/disable verification that inserted
HTTPS cookies are secure.
option
-disable
Option
Description
disable
Do not mark cookie as secure, allow sharing between an HTTP and
HTTPS connection.
enable
Mark inserted cookie as secure, cookie can only be used for HTTPS a
connection.
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
444
Fortinet Inc.

<!-- 来源页 445 -->
Parameter
Description
Type
Size
Default
Option
Description
static
Distribute to server based on source IP.
round-robin
Distribute to server based round robin order.
weighted
Distribute to server based on weight.
first-alive
Distribute to the first server that is alive.
http-host
Distribute to server based on host field in HTTP header.
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
saml-redirect
Enable/disable SAML redirection after
successful authentication.
option
-enable
Option
Description
disable
Do not support redirection after successful SAML authentication.
enable
Support redirection after successful SAML authentication.
saml-server
SAML service provider configuration for VIP
authentication.
string
Maximum
length: 35
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
tcp-forwarding
TCP-FORWARDING.
samlsp
SAML-SP.
web-portal
VPN-SSL-WEB-PORTAL.
saas
SAAS.
ssl-algorithm
Permitted encryption algorithms for the server
side of SSL full mode sessions according to
encryption strength.
option
-high
FortiOS 8.0.0 CLI Reference
445
Fortinet Inc.

<!-- 来源页 446 -->
Parameter
Description
Type
Size
Default
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
FortiOS 8.0.0 CLI Reference
446
Fortinet Inc.

<!-- 来源页 447 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable secure renegotiation.
disable
Disable secure renegotiation.
ssl-vpn-web-portal
Agentless VPN web portal.
string
Maximum
length: 35
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
virtual-host
Virtual host.
string
Maximum
length: 79
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
FortiOS 8.0.0 CLI Reference
447
Fortinet Inc.

<!-- 来源页 448 -->
Parameter
Description
Type
Size
Default
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
domain
Wildcard domain name of the real server.
string
Maximum
length: 255
external-auth
Enable/disable use of external browser as
user-agent for SAML user authentication.
option
-disable
FortiOS 8.0.0 CLI Reference
448
Fortinet Inc.

<!-- 来源页 449 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable use of external browser as user-agent for SAML user
authentication.
disable
Disable use of external browser as user-agent for SAML user
authentication.
health-check
Enable to check the responsiveness of the
real server before forwarding traffic.
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
when polling to determine server's
connectivity status.
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
Enable/disable holddown timer. Server will
be considered active and reachable once the
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
IP address of the real server.
ipv4-address-any
Not Specified
0.0.0.0
mappedport
Port for communicating with the real server.
user
Not Specified
FortiOS 8.0.0 CLI Reference
449
Fortinet Inc.

<!-- 来源页 450 -->
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
ssh-client-cert
Set access-proxy SSH client certificate
profile.
string
Maximum
length: 79
ssh-host-key
<name>
One or more server host key.
Server host key name.
string
Maximum
length: 79
ssh-host-key-validation
Enable/disable SSH real server host key
validation.
option
-disable
Option
Description
disable
Disable SSH real server host key validation.
enable
Enable SSH real server host key validation.
status
Set the status of the real server to active so
that it can accept traffic, or on standby or
disabled so no traffic is sent.
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
Enable/disable translation of hostname/IP
from virtual server to real server.
option
-enable
Option
Description
enable
Enable virtual hostname/IP translation.
disable
Disable virtual hostname/IP translation.
tunnel-encryption
Tunnel encryption.
option
-disable
Option
Description
enable
Enable tcp forwarding tunnel encryption.
disable
Disable tcp forwarding tunnel encryption.
type
TCP forwarding server type.
option
-tcp-forwarding
FortiOS 8.0.0 CLI Reference
450
Fortinet Inc.

<!-- 来源页 451 -->
Parameter
Description
Type
Size
Default
Option
Description
tcp-forwarding
TCP forwarding.
ssh
SSH.
verify-cert
Enable/disable certificate verification of the
real server.
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
-Option
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
FortiOS 8.0.0 CLI Reference
451
Fortinet Inc.

<!-- 来源页 452 -->
Parameter
Description
Type
Size
Default
Option
Description
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
TLS-DHE-DSS-WITH-AES-128-CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-AES-128-CBC-SHA.
TLS-DHE-DSS-WITH-AES-256-CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-AES-256-CBC-SHA.
TLS-DHE-DSS-WITH-AES-128-CBC-SHA256
Cipher suite TLS-DHE-DSS-WITH-AES-128-CBC-SHA256.
TLS-DHE-DSS-WITH-AES-128-GCM-SHA256
Cipher suite TLS-DHE-DSS-WITH-AES-128-GCM-SHA256.
FortiOS 8.0.0 CLI Reference
452
Fortinet Inc.

<!-- 来源页 453 -->
Parameter
Description
Type
Size
Default
Option
Description
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
TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384
Cipher suite TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384.
TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384
Cipher suite TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384.
TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA.
FortiOS 8.0.0 CLI Reference
453
Fortinet Inc.

<!-- 来源页 454 -->
Parameter
Description
Type
Size
Default
Option
Description
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
TLS-RSA-WITH-AES-128-CBC-SHA256
Cipher suite TLS-RSA-WITH-AES-128-CBC-SHA256.
TLS-RSA-WITH-AES-128-GCM-SHA256
Cipher suite TLS-RSA-WITH-AES-128-GCM-SHA256.
TLS-RSA-WITH-AES-256-CBC-SHA256
Cipher suite TLS-RSA-WITH-AES-256-CBC-SHA256.
FortiOS 8.0.0 CLI Reference
454
Fortinet Inc.

<!-- 来源页 455 -->
Parameter
Description
Type
Size
Default
Option
Description
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
TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA
Cipher suite TLS-DSS-RSA-WITH-CAMELLIA-128-CBC-SHA.
TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA.
FortiOS 8.0.0 CLI Reference
455
Fortinet Inc.

<!-- 来源页 456 -->
Parameter
Description
Type
Size
Default
Option
Description
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
TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256
Cipher suite TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256.
TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384
Cipher suite TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384.
FortiOS 8.0.0 CLI Reference
456
Fortinet Inc.

<!-- 来源页 457 -->
Parameter
Description
Type
Size
Default
Option
Description
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
TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC-SHA384
Cipher suite TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC_SHA384.
TLS-ECDHE-RSA-WITH-RC4-128-SHA
Cipher suite TLS-ECDHE-RSA-WITH-RC4-128-SHA.
FortiOS 8.0.0 CLI Reference
457
Fortinet Inc.

<!-- 来源页 458 -->
Parameter
Description
Type
Size
Default
Option
Description
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
458
Fortinet Inc.

<!-- 来源页 459 -->
config api-gateway6
Parameter
Description
Type
Size
Default
application
<name>
SaaS application controlled by this Access
Proxy.
SaaS application name.
string
Maximum
length: 79
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
Option
Description
disable
Disable use of HTTP cookie domain from host field in HTTP (use http-cooke-domain setting).
enable
Enable use of HTTP cookie domain from host field in HTTP.
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
FortiOS 8.0.0 CLI Reference
459
Fortinet Inc.

<!-- 来源页 460 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Only allow HTTP cookie to match this API Gateway.
same-ip
Allow HTTP cookie to match any API Gateway with same IP.
https-cookie-secure
Enable/disable verification that inserted
HTTPS cookies are secure.
option
-disable
Option
Description
disable
Do not mark cookie as secure, allow sharing between an HTTP and
HTTPS connection.
enable
Mark inserted cookie as secure, cookie can only be used for HTTPS a
connection.
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
Distribute to server based on source IP.
round-robin
Distribute to server based round robin order.
weighted
Distribute to server based on weight.
first-alive
Distribute to the first server that is alive.
http-host
Distribute to server based on host field in HTTP header.
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
saml-redirect
Enable/disable SAML redirection after
successful authentication.
option
-enable
FortiOS 8.0.0 CLI Reference
460
Fortinet Inc.

<!-- 来源页 461 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Do not support redirection after successful SAML authentication.
enable
Support redirection after successful SAML authentication.
saml-server
SAML service provider configuration for VIP
authentication.
string
Maximum
length: 35
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
tcp-forwarding
TCP-FORWARDING.
samlsp
SAML-SP.
web-portal
VPN-SSL-WEB-PORTAL.
saas
SAAS.
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
461
Fortinet Inc.

<!-- 来源页 462 -->
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
ssl-vpn-web-portal
Agentless VPN web portal.
string
Maximum
length: 35
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
virtual-host
Virtual host.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
462
Fortinet Inc.

<!-- 来源页 463 -->
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
463
Fortinet Inc.

<!-- 来源页 464 -->
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
domain
Wildcard domain name of the real server.
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
health-check
Enable to check the responsiveness of the
real server before forwarding traffic.
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
when polling to determine server's
connectivity status.
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
FortiOS 8.0.0 CLI Reference
464
Fortinet Inc.

<!-- 来源页 465 -->
Parameter
Description
Type
Size
Default
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
mappedport
Port for communicating with the real server.
user
Not Specified
port
Port for communicating with the real server.
integer
Minimum value:
1 Maximum
value: 65535
443
ssh-client-cert
Set access-proxy SSH client certificate
profile.
string
Maximum
length: 79
ssh-host-key
<name>
One or more server host key.
Server host key name.
string
Maximum
length: 79
ssh-host-key-validation
Enable/disable SSH real server host key
validation.
option
-disable
Option
Description
disable
Disable SSH real server host key validation.
enable
Enable SSH real server host key validation.
status
Set the status of the real server to active so
that it can accept traffic, or on standby or
disabled so no traffic is sent.
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
Enable/disable translation of hostname/IP
from virtual server to real server.
option
-enable
FortiOS 8.0.0 CLI Reference
465
Fortinet Inc.

<!-- 来源页 466 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable virtual hostname/IP translation.
disable
Disable virtual hostname/IP translation.
tunnel-encryption
Tunnel encryption.
option
-disable
Option
Description
enable
Enable tcp forwarding tunnel encryption.
disable
Disable tcp forwarding tunnel encryption.
type
TCP forwarding server type.
option
-tcp-forwarding
Option
Description
tcp-forwarding
TCP forwarding.
ssh
SSH.
verify-cert
Enable/disable certificate verification of the
real server.
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
-Option
Description
TLS-AES-128-GCM-SHA256
Cipher suite TLS-AES-128-GCM-SHA256.
TLS-AES-256-GCM-SHA384
Cipher suite TLS-AES-256-GCM-SHA384.
FortiOS 8.0.0 CLI Reference
466
Fortinet Inc.

<!-- 来源页 467 -->
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
467
Fortinet Inc.

<!-- 来源页 468 -->
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
468
Fortinet Inc.

<!-- 来源页 469 -->
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
469
Fortinet Inc.

<!-- 来源页 470 -->
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
470
Fortinet Inc.

<!-- 来源页 471 -->
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
471
Fortinet Inc.

<!-- 来源页 472 -->
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
472
Fortinet Inc.

<!-- 来源页 473 -->
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
473
Fortinet Inc.

---


<!-- 来源页 474 -->
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
config firewall access-proxy-ssh-client-cert
Configure Access Proxy SSH client certificate.
config firewall access-proxy-ssh-client-cert
Description: Configure Access Proxy SSH client certificate.
edit <name>
set auth-ca {string}
config cert-extension
Description: Configure certificate extension for user certificate.
edit <name>
set critical [no|yes]
set data {string}
set type [fixed|user]
next
end
set permit-agent-forwarding [enable|disable]
set permit-port-forwarding [enable|disable]
set permit-pty [enable|disable]
set permit-user-rc [enable|disable]
set permit-x11-forwarding [enable|disable]
set source-address [enable|disable]
next
end
config firewall access-proxy-ssh-client-cert
Parameter
Description
Type
Size
Default
auth-ca
Name of the SSH server public key authentication
CA.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
474
Fortinet Inc.

<!-- 来源页 475 -->
Parameter
Description
Type
Size
Default
name
SSH client certificate name.
string
Maximum
length: 79
permit-agent-forwarding
Enable/disable appending permit-agent-forwarding certificate extension.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
permit-port-forwarding
Enable/disable appending permit-port-forwarding
certificate extension.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
permit-pty
Enable/disable appending permit-pty certificate
extension.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
permit-user-rc
Enable/disable appending permit-user-rc
certificate extension.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
permit-x11-forwarding
Enable/disable appending permit-x11-forwarding
certificate extension.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
source-address
Enable/disable appending source-address
certificate critical option. This option ensure
certificate only accepted from FortiGate source
address.
option
-disable
FortiOS 8.0.0 CLI Reference
475
Fortinet Inc.

---


<!-- 来源页 476 -->
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
config cert-extension
Parameter
Description
Type
Size
Default
critical
Critical option.
option
-no
Option
Description
no
Certificate extension, server ignores the unsupported certificate
extension.
yes
Critical option, server refuses to authorize if it cannnot recognize the
critical option.
data
Data of certificate extension.
string
Maximum
length: 127
name
Name of certificate extension.
string
Maximum
length: 127
type
Type of certificate extension.
option
-fixed
Option
Description
fixed
Fixed certificate extension entry.
user
Certificate extension entry filled with authenticated username.
config firewall access-proxy-virtual-host
Configure Access Proxy virtual hosts.
config firewall access-proxy-virtual-host
Description: Configure Access Proxy virtual hosts.
edit <name>
set client-cert [disable|enable]
set empty-cert-action [accept|block|...]
set host {string}
set host-type [sub-string|fqdn|...]
set replacemsg-group {string}
set ssl-certificate <name1>, <name2>, ...
set user-agent-detect [disable|enable]
FortiOS 8.0.0 CLI Reference
476
Fortinet Inc.

<!-- 来源页 477 -->
next
end
config firewall access-proxy-virtual-host
Parameter
Description
Type
Size
Default
client-cert
Enable/disable requesting client certificate.
option
-enable
Option
Description
disable
Disable client certificate request.
enable
Enable client certificate request.
empty-cert-action
Action for an empty client certificate.
option
-block
Option
Description
accept
Accept the SSL handshake if the client certificate is empty.
block
Block the SSL handshake if the client certificate is empty.
accept-unmanageable
Accept the SSL handshake only if the end-point is unmanageable.
host
The host name.
string
Maximum
length: 79
host-type
Type of host pattern.
option
-fqdn **
Option
Description
sub-string
Match the pattern if a string contains the sub-string.
fqdn
Match the pattern with the FQDN or with the FQDN as domain suffix.
wildcard
Match the pattern with wildcards.
name
Virtual host name.
string
Maximum
length: 79
replacemsg-group
Access-proxy-virtual-host replacement message
override group.
string
Maximum
length: 35
ssl-certificate
<name>
SSL certificates for this host.
Certificate list.
string
Maximum
length: 79
user-agent-detect
Enable/disable detecting device type by HTTP
user-agent if no client certificate is provided.
option
-enable
FortiOS 8.0.0 CLI Reference
477
Fortinet Inc.

---


<!-- 来源页 506 -->
Parameter
Description
Type
Size
Default
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
config firewall auth-portal
Configure firewall authentication portals.
config firewall auth-portal
Description: Configure firewall authentication portals.
set groups <name1>, <name2>, ...
set identity-based-route {string}
set portal-addr {string}
set portal-addr6 {string}
set proxy-auth [enable|disable]
end
config firewall auth-portal
Parameter
Description
Type
Size
Default
groups
<name>
Firewall user groups permitted to authenticate
through this portal. Separate group names with
spaces.
Group name.
string
Maximum
length: 79
identity-based-route
Name of the identity-based route that applies to
this portal.
string
Maximum
length: 35
portal-addr
Address (or FQDN) of the authentication portal.
string
Maximum
length: 63
FortiOS 8.0.0 CLI Reference
506
Fortinet Inc.

---


<!-- 来源页 514 -->
config firewall decrypted-traffic-mirror
Configure decrypted traffic mirror.
config firewall decrypted-traffic-mirror
Description: Configure decrypted traffic mirror.
edit <name>
set dstmac {mac-address}
set interface <name1>, <name2>, ...
set traffic-source [client|server|...]
set traffic-type {option1}, {option2}, ...
next
end
config firewall decrypted-traffic-mirror
Parameter
Description
Type
Size
Default
dstmac
Set destination MAC address for mirrored
traffic.
mac-address
Not
Specified
ff:ff:ff:ff:ff:ff
interface
<name>
Decrypted traffic mirror interface.
Decrypted traffic mirror interface.
string
Maximum
length: 79
name
Name.
string
Maximum
length: 35
traffic-source
Source of decrypted traffic to be mirrored.
option
-client
Option
Description
client
Mirror client side decrypted traffic.
server
Mirror server side decrypted traffic.
both
Mirror both client and server side decrypted traffic.
traffic-type
Types of decrypted traffic to be mirrored.
option
-ssl
Option
Description
ssl
Mirror decrypted SSL traffic.
ssh
Mirror decrypted SSH traffic.
config firewall dnstranslation
Configure DNS translation.
FortiOS 8.0.0 CLI Reference
514
Fortinet Inc.

---


<!-- 来源页 516 -->
config firewall global
Parameter
Description
Type
Size
Default
banned-ip-persistency
Persistency of banned IPs across power cycling.
option
-disabled
Option
Description
disabled
No entries are kept across power cycling.
permanent-only
Only permanent IP bans are kept across power cycling.
all
All IP bans are kept across power cycling.
config firewall identity-based-route
Configure identity based routing.
config firewall identity-based-route
Description: Configure identity based routing.
edit <name>
set comments {string}
config rule
Description: Rule.
edit <id>
set device {string}
set gateway {ipv4-address}
set groups <name1>, <name2>, ...
next
end
next
end
config firewall identity-based-route
Parameter
Description
Type
Size
Default
comments
Comments.
string
Maximum length:
127
name
Name.
string
Maximum length: 35
FortiOS 8.0.0 CLI Reference
516
Fortinet Inc.

---


<!-- 来源页 517 -->
config rule
Parameter
Description
Type
Size
Default
device
Outgoing interface for the rule.
string
Maximum
length: 35
gateway
IPv4 address of the gateway (Format:
xxx.xxx.xxx.xxx , Default: 0.0.0.0).
ipv4-address
Not Specified
0.0.0.0
groups
<name>
Select one or more group(s) from available
groups that are allowed to use this route.
Separate group names with a space.
Group name.
string
Maximum
length: 79
id
Rule ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config firewall interface-policy
Configure IPv4 interface policies.
config firewall interface-policy
Description: Configure IPv4 interface policies.
edit <policyid>
set application-list {string}
set application-list-status [enable|disable]
set av-profile {string}
set av-profile-status [enable|disable]
set casb-profile {string}
set casb-profile-status [enable|disable]
set comments {var-string}
set dlp-profile {string}
set dlp-profile-status [enable|disable]
set dsri [enable|disable]
set dstaddr <name1>, <name2>, ...
set emailfilter-profile {string}
set emailfilter-profile-status [enable|disable]
set interface {string}
set ips-sensor {string}
set ips-sensor-status [enable|disable]
set logtraffic [all|utm|...]
set service <name1>, <name2>, ...
set srcaddr <name1>, <name2>, ...
set status [enable|disable]
set uuid {uuid}
set webfilter-profile {string}
set webfilter-profile-status [enable|disable]
FortiOS 8.0.0 CLI Reference
517
Fortinet Inc.

<!-- 来源页 518 -->
next
end
config firewall interface-policy
Parameter
Description
Type
Size
Default
application-list
Application list name.
string
Maximum
length: 47
application-list-status
Enable/disable application control.
option
-disable
Option
Description
enable
Enable application control
disable
Disable application control
av-profile
Antivirus profile.
string
Maximum
length: 47
av-profile-status
Enable/disable antivirus.
option
-disable
Option
Description
enable
Enable antivirus
disable
Disable antivirus
casb-profile
CASB profile.
string
Maximum
length: 47
casb-profile-status
Enable/disable CASB.
option
-disable
Option
Description
enable
Enable CASB.
disable
Disable CASB.
comments
Comments.
var-string
Maximum
length: 1023
dlp-profile
DLP profile name.
string
Maximum
length: 47
dlp-profile-status
Enable/disable DLP.
option
-disable
FortiOS 8.0.0 CLI Reference
518
Fortinet Inc.

<!-- 来源页 519 -->
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
dsri
Enable/disable DSRI.
option
-disable
Option
Description
enable
Enable DSRI.
disable
Disable DSRI.
dstaddr
<name>
Address object to limit traffic monitoring
to network traffic sent to the specified
address or range.
Address name.
string
Maximum
length: 79
emailfilter-profile
Email filter profile.
string
Maximum
length: 47
emailfilter-profile-status
Enable/disable email filter.
option
-disable
Option
Description
enable
Enable Email filter.
disable
Disable Email filter.
interface
Monitored interface name from available
interfaces.
string
Maximum
length: 35
ips-sensor
IPS sensor name.
string
Maximum
length: 47
ips-sensor-status
Enable/disable IPS.
option
-disable
Option
Description
enable
Enable IPS.
disable
Disable IPS.
logtraffic
Logging type to be used in this policy
(Options: all | utm | disable, Default: utm).
option
-utm
Option
Description
all
Log all sessions accepted or denied by this policy.
FortiOS 8.0.0 CLI Reference
519
Fortinet Inc.

---


<!-- 来源页 520 -->
Parameter
Description
Type
Size
Default
Option
Description
utm
Log traffic that has a security profile applied to it.
disable
Disable all logging for this policy.
policyid
Policy ID (0 - 4294967295).
integer
Minimum value:
0 Maximum
value:
4294967295
0
service
<name>
Service object from available options.
Service name.
string
Maximum
length: 79
srcaddr
<name>
Address object to limit traffic monitoring
to network traffic sent from the specified
address or range.
Address name.
string
Maximum
length: 79
status
Enable/disable this policy.
option
-enable
Option
Description
enable
Enable this policy.
disable
Disable this policy.
uuid
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not Specified
00000000-0000-0000-0000-000000000000
webfilter-profile
Web filter profile.
string
Maximum
length: 47
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
config firewall interface-policy6
Configure IPv6 interface policies.
config firewall interface-policy6
Description: Configure IPv6 interface policies.
edit <policyid>
set application-list {string}
FortiOS 8.0.0 CLI Reference
520
Fortinet Inc.

<!-- 来源页 521 -->
set application-list-status [enable|disable]
set av-profile {string}
set av-profile-status [enable|disable]
set casb-profile {string}
set casb-profile-status [enable|disable]
set comments {var-string}
set dlp-profile {string}
set dlp-profile-status [enable|disable]
set dsri [enable|disable]
set dstaddr6 <name1>, <name2>, ...
set emailfilter-profile {string}
set emailfilter-profile-status [enable|disable]
set interface {string}
set ips-sensor {string}
set ips-sensor-status [enable|disable]
set logtraffic [all|utm|...]
set service6 <name1>, <name2>, ...
set srcaddr6 <name1>, <name2>, ...
set status [enable|disable]
set uuid {uuid}
set webfilter-profile {string}
set webfilter-profile-status [enable|disable]
next
end
config firewall interface-policy6
Parameter
Description
Type
Size
Default
application-list
Application list name.
string
Maximum
length: 47
application-list-status
Enable/disable application control.
option
-disable
Option
Description
enable
Enable application control
disable
Disable application control
av-profile
Antivirus profile.
string
Maximum
length: 47
av-profile-status
Enable/disable antivirus.
option
-disable
Option
Description
enable
Enable antivirus
disable
Disable antivirus
FortiOS 8.0.0 CLI Reference
521
Fortinet Inc.

<!-- 来源页 522 -->
Parameter
Description
Type
Size
Default
casb-profile
CASB profile.
string
Maximum
length: 47
casb-profile-status
Enable/disable CASB.
option
-disable
Option
Description
enable
Enable CASB.
disable
Disable CASB.
comments
Comments.
var-string
Maximum
length: 1023
dlp-profile
DLP profile name.
string
Maximum
length: 47
dlp-profile-status
Enable/disable DLP.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
dsri
Enable/disable DSRI.
option
-disable
Option
Description
enable
Enable DSRI.
disable
Disable DSRI.
dstaddr6
<name>
IPv6 address object to limit traffic
monitoring to network traffic sent to the
specified address or range.
Address name.
string
Maximum
length: 79
emailfilter-profile
Email filter profile.
string
Maximum
length: 47
emailfilter-profile-status
Enable/disable email filter.
option
-disable
Option
Description
enable
Enable Email filter.
disable
Disable Email filter.
FortiOS 8.0.0 CLI Reference
522
Fortinet Inc.

<!-- 来源页 523 -->
Parameter
Description
Type
Size
Default
interface
Monitored interface name from available
interfaces.
string
Maximum
length: 35
ips-sensor
IPS sensor name.
string
Maximum
length: 47
ips-sensor-status
Enable/disable IPS.
option
-disable
Option
Description
enable
Enable IPS.
disable
Disable IPS.
logtraffic
Logging type to be used in this policy
(Options: all | utm | disable, Default: utm).
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
policyid
Policy ID (0 - 4294967295).
integer
Minimum value:
0 Maximum
value:
4294967295
0
service6
<name>
Service name.
Service name.
string
Maximum
length: 79
srcaddr6
<name>
IPv6 address object to limit traffic
monitoring to network traffic sent from
the specified address or range.
Address name.
string
Maximum
length: 79
status
Enable/disable this policy.
option
-enable
Option
Description
enable
Enable this policy.
disable
Disable this policy.
uuid
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not Specified
00000000-0000-0000-0000-000000000000
webfilter-profile
Web filter profile.
string
Maximum
length: 47
FortiOS 8.0.0 CLI Reference
523
Fortinet Inc.

---


<!-- 来源页 548 -->
config firewall internet-service-subapp
Parameter
Description
Type
Size
Default
id
Internet Service main ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
sub-app <id>
Subapp number list.
Subapp ID.
integer
Minimum value:
0 Maximum
value:
4294967295
config firewall ipmacbinding setting
Configure IP to MAC binding settings.
config firewall ipmacbinding setting
Description: Configure IP to MAC binding settings.
set bindthroughfw [enable|disable]
set bindtofw [enable|disable]
set undefinedhost [allow|block]
end
config firewall ipmacbinding setting
Parameter
Description
Type
Size
Default
bindthroughfw
Enable/disable use of IP/MAC binding to filter
packets that would normally go through the
firewall.
option
-disable
Option
Description
enable
Enable IP/MAC binding for packets that would normally go through
the firewall.
disable
Disable IP/MAC binding for packets that would normally go through
the firewall.
bindtofw
Enable/disable use of IP/MAC binding to filter
packets that would normally go to the firewall.
option
-disable
FortiOS 8.0.0 CLI Reference
548
Fortinet Inc.

---


<!-- 来源页 549 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable IP/MAC binding for packets that would normally go to the
firewall.
disable
Disable IP/MAC binding for packets that would normally go to the
firewall.
undefinedhost
Select action to take on packets with IP/MAC
addresses not in the binding list (default = block).
option
-block
Option
Description
allow
Allow packets from MAC addresses not in the IP/MAC list.
block
Block packets from MAC addresses not in the IP/MAC list.
config firewall ipmacbinding table
Configure IP to MAC address pairs in the IP/MAC binding table.
config firewall ipmacbinding table
Description: Configure IP to MAC address pairs in the IP/MAC binding table.
edit <seq-num>
set ip {ipv4-address}
set mac {mac-address}
set name {string}
set status [enable|disable]
next
end
config firewall ipmacbinding table
Parameter
Description
Type
Size
Default
ip
IPv4 address portion of the pair
(format: xxx.xxx.xxx.xxx).
ipv4-address
Not Specified
0.0.0.0
mac
MAC address portion of the pair
(format = xx:xx:xx:xx:xx:xx in
hexadecimal).
mac-address
Not Specified
00:00:00:00:00:00
name
Name of the pair (optional, default =
no name).
string
Maximum
length: 35
noname
FortiOS 8.0.0 CLI Reference
549
Fortinet Inc.

---


<!-- 来源页 564 -->
Parameter
Description
Type
Size
Default
type
Select the Monitor type used by the health check
monitor to check the health of the server (PING |
TCP | HTTP | HTTPS | DNS).
option
-Option
Description
ping
PING health monitor.
tcp
TCP-connect health monitor.
http
HTTP-GET health monitor.
https
HTTP-GET health monitor with SSL.
dns
DNS health monitor.
config firewall local-in-policy
Configure user defined IPv4 local-in policies.
config firewall local-in-policy
Description: Configure user defined IPv4 local-in policies.
edit <policyid>
set action [accept|deny]
set comments {var-string}
set custom-tags <name1>, <name2>, ...
set dstaddr <name1>, <name2>, ...
set dstaddr-negate [enable|disable]
set ha-mgmt-intf-only [enable|disable]
set internet-service-src [enable|disable]
set internet-service-src-custom <name1>, <name2>, ...
set internet-service-src-custom-group <name1>, <name2>, ...
set internet-service-src-fortiguard <name1>, <name2>, ...
set internet-service-src-group <name1>, <name2>, ...
set internet-service-src-name <name1>, <name2>, ...
set internet-service-src-negate [enable|disable]
set intf <name1>, <name2>, ...
set logtraffic [enable|disable]
set schedule {string}
set service <name1>, <name2>, ...
set service-negate [enable|disable]
set srcaddr <name1>, <name2>, ...
set srcaddr-negate [enable|disable]
set status [enable|disable]
set uuid {uuid}
set virtual-patch [enable|disable]
next
end
FortiOS 8.0.0 CLI Reference
564
Fortinet Inc.

<!-- 来源页 565 -->
config firewall local-in-policy
Parameter
Description
Type
Size
Default
action
Action performed on traffic matching the
policy (default = deny).
option
-deny
Option
Description
accept
Allow traffic matching this policy.
deny
Deny or block traffic matching this policy.
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
dstaddr
<name>
Destination address object from available
options.
Address name.
string
Maximum
length: 79
dstaddr-negate
When enabled dstaddr specifies what the
destination address must NOT be.
option
-disable
Option
Description
enable
Enable destination address negate.
disable
Disable destination address negate.
ha-mgmt-intf-only
Enable/disable dedicating the HA
management interface only for local-in
policy.
option
-disable
Option
Description
enable
Enable dedicating HA management interface only for local-in policy.
disable
Disable dedicating HA management interface only for local-in policy.
internet-service-src
Enable/disable use of Internet Services in
source for this local-in policy. If enabled,
source address is not used.
option
-disable
Option
Description
enable
Enable use of Internet Services source in local-in policy.
disable
Disable use of Internet Services source in local-in policy.
FortiOS 8.0.0 CLI Reference
565
Fortinet Inc.

<!-- 来源页 566 -->
Parameter
Description
Type
Size
Default
internet-service-src-custom
<name>
Custom Internet Service source name.
Custom Internet Service name.
string
Maximum
length: 79
internet-service-src-custom-group <name>
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
Option
Description
enable
Enable negated Internet Service source match.
disable
Disable negated Internet Service source match.
intf <name>
Incoming interface name from available
options.
Address name.
string
Maximum
length: 79
logtraffic
Enable/disable local-in traffic logging.
option
-disable
Option
Description
enable
Enable local-in traffic logging.
disable
Disable local-in traffic logging.
policyid
User defined local in policy ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
schedule
Schedule object from available options.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
566
Fortinet Inc.

---


<!-- 来源页 567 -->
Parameter
Description
Type
Size
Default
service
<name>
Service object from available options.
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
Source address object from available
options.
Address name.
string
Maximum
length: 79
srcaddr-negate
When enabled srcaddr specifies what the
source address must NOT be.
option
-disable
Option
Description
enable
Enable source address negate.
disable
Disable source address negate.
status
Enable/disable this local-in policy.
option
-enable
Option
Description
enable
Enable this local-in policy.
disable
Disable this local-in policy.
uuid
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not Specified
00000000-0000-0000-0000-000000000000
virtual-patch
Enable/disable virtual patching.
option
-disable
Option
Description
enable
Enable virtual patching.
disable
Disable virtual patching.
* This parameter may not exist in some models.
config firewall local-in-policy6
Configure user defined IPv6 local-in policies.
FortiOS 8.0.0 CLI Reference
567
Fortinet Inc.

<!-- 来源页 568 -->
config firewall local-in-policy6
Description: Configure user defined IPv6 local-in policies.
edit <policyid>
set action [accept|deny]
set comments {var-string}
set custom-tags <name1>, <name2>, ...
set dstaddr <name1>, <name2>, ...
set dstaddr-negate [enable|disable]
set internet-service6-src [enable|disable]
set internet-service6-src-custom <name1>, <name2>, ...
set internet-service6-src-custom-group <name1>, <name2>, ...
set internet-service6-src-fortiguard <name1>, <name2>, ...
set internet-service6-src-group <name1>, <name2>, ...
set internet-service6-src-name <name1>, <name2>, ...
set internet-service6-src-negate [enable|disable]
set intf <name1>, <name2>, ...
set logtraffic [enable|disable]
set schedule {string}
set service <name1>, <name2>, ...
set service-negate [enable|disable]
set srcaddr <name1>, <name2>, ...
set srcaddr-negate [enable|disable]
set status [enable|disable]
set uuid {uuid}
set virtual-patch [enable|disable]
next
end
config firewall local-in-policy6
Parameter
Description
Type
Size
Default
action
Action performed on traffic matching the
policy (default = deny).
option
-deny
Option
Description
accept
Allow local-in traffic matching this policy.
deny
Deny or block local-in traffic matching this policy.
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
dstaddr
<name>
Destination address object from available
options.
Address name.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
568
Fortinet Inc.

<!-- 来源页 569 -->
Parameter
Description
Type
Size
Default
dstaddr-negate
When enabled dstaddr specifies what the
destination address must NOT be.
option
-disable
Option
Description
enable
Enable destination address negate.
disable
Disable destination address negate.
internet-service6-src
Enable/disable use of IPv6 Internet
Services in source for this local-in
policy.If enabled, source address is not
used.
option
-disable
Option
Description
enable
Enable use of IPv6 Internet Services source in local-in policy.
disable
Disable use of IPv6 Internet Services source in local-in policy.
internet-service6-src-custom
<name>
Custom IPv6 Internet Service source
name.
Custom Internet Service name.
string
Maximum
length: 79
internet-service6-src-custom-group <name>
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
FortiOS 8.0.0 CLI Reference
569
Fortinet Inc.

<!-- 来源页 570 -->
Parameter
Description
Type
Size
Default
intf <name>
Incoming interface name from available
options.
Address name.
string
Maximum
length: 79
logtraffic
Enable/disable local-in traffic logging.
option
-disable
Option
Description
enable
Enable local-in traffic logging.
disable
Disable local-in traffic logging.
policyid
User defined local in policy ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
schedule
Schedule object from available options.
string
Maximum
length: 35
service
<name>
Service object from available options.
Separate names with a space.
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
Source address object from available
options.
Address name.
string
Maximum
length: 79
srcaddr-negate
When enabled srcaddr specifies what the
source address must NOT be.
option
-disable
Option
Description
enable
Enable source address negate.
disable
Disable source address negate.
status
Enable/disable this local-in policy.
option
-enable
Option
Description
enable
Enable this local-in policy.
disable
Disable this local-in policy.
FortiOS 8.0.0 CLI Reference
570
Fortinet Inc.

---


<!-- 来源页 571 -->
Parameter
Description
Type
Size
Default
uuid
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not Specified
00000000-0000-0000-0000-000000000000
virtual-patch
Enable/disable the virtual patching
feature.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
* This parameter may not exist in some models.
config firewall multicast-address
Configure multicast addresses.
config firewall multicast-address
Description: Configure multicast addresses.
edit <name>
set associated-interface {string}
set color {integer}
set comment {var-string}
set custom-tags <name1>, <name2>, ...
set display-with [all-tags|first-tag-only|...]
set end-ip {ipv4-address-any}
set start-ip {ipv4-address-any}
set subnet {ipv4-classnet-any}
config tagging
Description: Config object tagging.
edit <name>
set category {string}
set tags <name1>, <name2>, ...
next
end
set type [multicastrange|broadcastmask]
next
end
FortiOS 8.0.0 CLI Reference
571
Fortinet Inc.

<!-- 来源页 572 -->
config firewall multicast-address
Parameter
Description
Type
Size
Default
associated-interface
Interface associated with the address
object. When setting up a policy, only
addresses associated with this interface are
available.
string
Maximum
length: 35
color
Integer value to determine the color of the
icon in the GUI (1 - 32, default = 0, which
sets value to 1).
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
address.
string
Maximum
length: 35
display-with *
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
Final IPv4 address (inclusive) in the range
for the address.
ipv4-address-any
Not
Specified
0.0.0.0
name
Multicast address name.
string
Maximum
length: 79
start-ip
First IPv4 address (inclusive) in the range for
the address.
ipv4-address-any
Not
Specified
0.0.0.0
subnet
Broadcast address and subnet.
ipv4-classnet-any
Not
Specified
0.0.0.0 0.0.0.0
type
Type of address object: multicast IP address
range or broadcast IP/mask to be treated as
a multicast address.
option
-multicastrange
FortiOS 8.0.0 CLI Reference
572
Fortinet Inc.

---


<!-- 来源页 573 -->
Parameter
Description
Type
Size
Default
Option
Description
multicastrange
Multicast range.
broadcastmask
Broadcast IP/mask.
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
config firewall multicast-address6
Configure IPv6 multicast address.
config firewall multicast-address6
Description: Configure IPv6 multicast address.
edit <name>
set color {integer}
set comment {var-string}
set custom-tags <name1>, <name2>, ...
set display-with [all-tags|first-tag-only|...]
set ip6 {ipv6-network}
config tagging
Description: Config object tagging.
edit <name>
set category {string}
set tags <name1>, <name2>, ...
next
end
next
end
FortiOS 8.0.0 CLI Reference
573
Fortinet Inc.

---


<!-- 来源页 574 -->
config firewall multicast-address6
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
custom-tags
<name> *
Custom tags.
Names of custom tags used with this address.
string
Maximum
length: 35
display-with
*
Display object with first tag, all tags, or just the
icon.
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
ip6
IPv6 address prefix (format:
xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xxx).
ipv6-network
Not
Specified
::/0
name
IPv6 multicast address name.
string
Maximum
length: 79
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
config firewall multicast-policy
Configure multicast NAT policies.
FortiOS 8.0.0 CLI Reference
574
Fortinet Inc.

<!-- 来源页 575 -->
config firewall multicast-policy
Description: Configure multicast NAT policies.
edit <id>
set action [accept|deny]
set auto-asic-offload [enable|disable]
set comments {var-string}
set custom-tags <name1>, <name2>, ...
set dnat {ipv4-address-any}
set dstaddr <name1>, <name2>, ...
set dstintf {string}
set end-port {integer}
set ips-sensor {string}
set logtraffic [all|utm|...]
set name {string}
set protocol {integer}
set snat [enable|disable]
set snat-ip {ipv4-address}
set srcaddr <name1>, <name2>, ...
set srcintf {string}
set start-port {integer}
set status [enable|disable]
set traffic-shaper {string}
set utm-status [enable|disable]
set uuid {uuid}
next
end
config firewall multicast-policy
Parameter
Description
Type
Size
Default
action
Accept or deny traffic matching the
policy.
option
-accept
Option
Description
accept
Accept traffic matching the policy.
deny
Deny or block traffic matching the policy.
auto-asic-offload
Enable/disable offloading policy traffic
for hardware acceleration.
option
-enable
Option
Description
enable
Enable hardware acceleration offloading.
disable
Disable offloading for hardware acceleration.
comments
Comment.
var-string
Maximum
length: 1023
FortiOS 8.0.0 CLI Reference
575
Fortinet Inc.

<!-- 来源页 576 -->
Parameter
Description
Type
Size
Default
custom-tags
<name> *
Custom tags.
Names of custom tags used with this
policy.
string
Maximum
length: 35
dnat
IPv4 DNAT address used for multicast
destination addresses.
ipv4-address-any
Not Specified
0.0.0.0
dstaddr
<name>
Destination address objects.
Destination address objects.
string
Maximum
length: 79
dstintf
Destination interface name.
string
Maximum
length: 35
end-port
Integer value for ending TCP/UDP/SCTP
destination port in range (1 - 65535,
default = 1).
integer
Minimum value:
0 Maximum
value: 65535
65535
id
Policy ID ((0 - 4294967294).
integer
Minimum value:
0 Maximum
value:
4294967294
0
ips-sensor
Name of an existing IPS sensor.
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
Enable logging traffic accepted by this policy.
utm
Log traffic that has a security profile applied to it.
disable
Disable all logging for this policy.
name
Policy name.
string
Maximum
length: 35
protocol
Integer value for the protocol type as
defined by IANA (0 - 255, default = 0).
integer
Minimum value:
0 Maximum
value: 255
0
snat
Enable/disable substitution of the
outgoing interface IP address for the
original source IP address (called source
NAT or SNAT).
option
-disable
FortiOS 8.0.0 CLI Reference
576
Fortinet Inc.

---


<!-- 来源页 577 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable source NAT.
disable
Disable source NAT.
snat-ip
IPv4 address to be used as the source
address for NATed traffic.
ipv4-address
Not Specified
0.0.0.0
srcaddr
<name>
Source address objects.
Source address objects.
string
Maximum
length: 79
srcintf
Source interface name.
string
Maximum
length: 35
start-port
Integer value for starting
TCP/UDP/SCTP destination port in
range (1 - 65535, default = 1).
integer
Minimum value:
0 Maximum
value: 65535
1
status
Enable/disable this policy.
option
-enable
Option
Description
enable
Enable this policy.
disable
Disable this policy.
traffic-shaper
Traffic shaper to apply to traffic
forwarded by the multicast policy.
string
Maximum
length: 35
utm-status
Enable to add an IPS security profile to
the policy.
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
* This parameter may not exist in some models.
config firewall multicast-policy6
Configure IPv6 multicast NAT policies.
config firewall multicast-policy6
Description: Configure IPv6 multicast NAT policies.
FortiOS 8.0.0 CLI Reference
577
Fortinet Inc.

<!-- 来源页 578 -->
edit <id>
set action [accept|deny]
set auto-asic-offload [enable|disable]
set comments {var-string}
set custom-tags <name1>, <name2>, ...
set dstaddr <name1>, <name2>, ...
set dstintf {string}
set end-port {integer}
set ips-sensor {string}
set logtraffic [all|utm|...]
set name {string}
set protocol {integer}
set srcaddr <name1>, <name2>, ...
set srcintf {string}
set start-port {integer}
set status [enable|disable]
set utm-status [enable|disable]
set uuid {uuid}
next
end
config firewall multicast-policy6
Parameter
Description
Type
Size
Default
action
Accept or deny traffic matching the
policy.
option
-accept
Option
Description
accept
Accept.
deny
Deny.
auto-asic-offload
Enable/disable offloading policy traffic for
hardware acceleration.
option
-enable
Option
Description
enable
Enable offloading policy traffic for hardware acceleration.
disable
Disable offloading policy traffic for hardware acceleration.
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
dstaddr
<name>
IPv6 destination address name.
Address name.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
578
Fortinet Inc.

<!-- 来源页 579 -->
Parameter
Description
Type
Size
Default
dstintf
IPv6 destination interface name.
string
Maximum
length: 35
end-port
Integer value for ending TCP/UDP/SCTP
destination port in range (1 - 65535,
default = 65535).
integer
Minimum value:
0 Maximum
value: 65535
65535
id
Policy ID (0 - 4294967294).
integer
Minimum value:
0 Maximum
value:
4294967294
0
ips-sensor
Name of an existing IPS sensor.
string
Maximum
length: 47
logtraffic
Enable or disable logging. Log all sessions
or security profile sessions.
option
-utm
Option
Description
all
Enable logging traffic accepted by this policy.
utm
Log traffic that has a security profile applied to it.
disable
Disable all logging for this policy.
name
Policy name.
string
Maximum
length: 35
protocol
Integer value for the protocol type as
defined by IANA (0 - 255, default = 0).
integer
Minimum value:
0 Maximum
value: 255
0
srcaddr
<name>
IPv6 source address name.
Address name.
string
Maximum
length: 79
srcintf
IPv6 source interface name.
string
Maximum
length: 35
start-port
Integer value for starting TCP/UDP/SCTP
destination port in range (1 - 65535,
default = 1).
integer
Minimum value:
0 Maximum
value: 65535
1
status
Enable/disable this policy.
option
-enable
Option
Description
enable
Enable this policy.
disable
Disable this policy.
utm-status
Enable to add an IPS security profile to
the policy.
option
-disable
FortiOS 8.0.0 CLI Reference
579
Fortinet Inc.

---


<!-- 来源页 581 -->
Parameter
Description
Type
Size
Default
Option
Description
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
filter
Match criteria filter.
var-string
Maximum
length:
2047
name
Dynamic Network Service name.
string
Maximum
length: 63
sdn
SDN connector name.
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
config firewall on-demand-sniffer
Configure on-demand packet sniffer.
config firewall on-demand-sniffer
Description: Configure on-demand packet sniffer.
edit <name>
set advanced-filter {var-string}
set hosts <host1>, <host2>, ...
FortiOS 8.0.0 CLI Reference
581
Fortinet Inc.

<!-- 来源页 582 -->
set interface {string}
set max-packet-count {integer}
set non-ip-packet [enable|disable]
set ports <port1>, <port2>, ...
set protocols <protocol1>, <protocol2>, ...
next
end
config firewall on-demand-sniffer
Parameter
Description
Type
Size
Default
advanced-filter
Advanced freeform filter that will be used over
existing filter settings if set. Can only be used by
super admin.
var-string
Maximum
length: 255
hosts <host>
IPv4 or IPv6 hosts to filter in this traffic sniffer.
IPv4 or IPv6 host.
string
Maximum
length: 255
interface
Interface name that on-demand packet sniffer will
take place.
string
Maximum
length: 35
max-packet-count
Maximum number of packets to capture per on-demand packet sniffer.
integer
Minimum
value: 1
Maximum
value:
20000 **
0
name
On-demand packet sniffer name.
string
Maximum
length: 35
non-ip-packet
Include non-IP packets.
option
-disable
Option
Description
enable
Enable non-IP packets to be included capture.
disable
Disable non-IP packets to be included in capture.
ports <port>
Ports to filter for in this traffic sniffer.
Port to filter in this traffic sniffer.
integer
Minimum
value: 1
Maximum
value:
65536
protocols
<protocol>
Protocols to filter in this traffic sniffer.
Integer value for the protocol type as defined by
IANA (0 - 255).
integer
Minimum
value: 0
Maximum
value: 255
** Values may differ between models.
FortiOS 8.0.0 CLI Reference
582
Fortinet Inc.

---


<!-- 来源页 693 -->
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
member
<name>
Service objects contained within the group.
Service or service group name.
string
Maximum
length: 79
name
Service group name.
string
Maximum
length: 79
proxy
Enable/disable web proxy service group.
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
automatically assigned but can be manually
reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
config firewall shaper per-ip-shaper
Configure per-IP traffic shaper.
FortiOS 8.0.0 CLI Reference
693
Fortinet Inc.

<!-- 来源页 694 -->
config firewall shaper per-ip-shaper
Description: Configure per-IP traffic shaper.
edit <name>
set bandwidth-unit [kbps|mbps|...]
set diffserv-forward [enable|disable]
set diffserv-reverse [enable|disable]
set diffservcode-forward {user}
set diffservcode-rev {user}
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set max-bandwidth {integer}
set max-concurrent-session {integer}
set max-concurrent-tcp-session {integer}
set max-concurrent-udp-session {integer}
set uuid {uuid}
next
end
config firewall shaper per-ip-shaper
Parameter
Description
Type
Size
Default
bandwidth-unit
Unit of measurement for maximum
bandwidth for this shaper (Kbps, Mbps or
Gbps).
option
-kbps
Option
Description
kbps
Kilobits per second.
mbps
Megabits per second.
gbps
Gigabits per second.
diffserv-forward
Enable/disable changing the Forward
(original) DiffServ setting applied to
traffic accepted by this shaper.
option
-disable
Option
Description
enable
Enable setting forward (original) traffic DiffServ.
disable
Disable setting forward (original) traffic DiffServ.
diffserv-reverse
Enable/disable changing the Reverse
(reply) DiffServ setting applied to traffic
accepted by this shaper.
option
-disable
FortiOS 8.0.0 CLI Reference
694
Fortinet Inc.

<!-- 来源页 695 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable setting reverse (reply) traffic DiffServ.
disable
Disable setting reverse (reply) traffic DiffServ.
diffservcode-forward
Forward (original) DiffServ setting to be
applied to traffic accepted by this shaper.
user
Not
Specified
diffservcode-rev
Reverse (reply) DiffServ setting to be
applied to traffic accepted by this shaper.
user
Not
Specified
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
max-bandwidth
Upper bandwidth limit enforced by this
shaper (0 - 80000000). 0 means no limit.
Units depend on the bandwidth-unit
setting.
integer
Minimum
value: 0
Maximum
value:
80000000
**
0
FortiOS 8.0.0 CLI Reference
695
Fortinet Inc.

---


<!-- 来源页 696 -->
Parameter
Description
Type
Size
Default
max-concurrent-session
Maximum number of concurrent sessions
allowed by this shaper (0 - 2097000). 0
means no limit.
integer
Minimum
value: 0
Maximum
value:
2097000
0
max-concurrent-tcp-session
Maximum number of concurrent TCP
sessions allowed by this shaper (0 -2097000). 0 means no limit.
integer
Minimum
value: 0
Maximum
value:
2097000
0
max-concurrent-udp-session
Maximum number of concurrent UDP
sessions allowed by this shaper (0 -2097000). 0 means no limit.
integer
Minimum
value: 0
Maximum
value:
2097000
0
name
Traffic shaper name.
string
Maximum
length: 35
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
** Values may differ between models.
config firewall shaper traffic-shaper
Configure shared traffic shaper.
config firewall shaper traffic-shaper
Description: Configure shared traffic shaper.
edit <name>
set bandwidth-unit [kbps|mbps|...]
set cos {user}
set cos-marking [enable|disable]
set cos-marking-method [multi-stage|static]
set diffserv [enable|disable]
set diffservcode {user}
set dscp-marking-method [multi-stage|static]
set exceed-bandwidth {integer}
set exceed-class-id {integer}
set exceed-cos {user}
set exceed-dscp {user}
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
FortiOS 8.0.0 CLI Reference
696
Fortinet Inc.

<!-- 来源页 697 -->
set fabric-object-source [member|local|...]
set guaranteed-bandwidth {integer}
set maximum-bandwidth {integer}
set maximum-cos {user}
set maximum-dscp {user}
set overhead {integer}
set per-policy [disable|enable]
set priority [low|medium|...]
set uuid {uuid}
next
end
config firewall shaper traffic-shaper
Parameter
Description
Type
Size
Default
bandwidth-unit
Unit of measurement for guaranteed
and maximum bandwidth for this shaper
(Kbps, Mbps or Gbps).
option
-kbps
Option
Description
kbps
Kilobits per second.
mbps
Megabits per second.
gbps
Gigabits per second.
cos
VLAN CoS mark.
user
Not Specified
cos-marking
Enable/disable VLAN CoS marking.
option
-disable
Option
Description
enable
Enable VLAN CoS marking.
disable
Disable VLAN CoS marking.
cos-marking-method
Select VLAN CoS marking method.
option
-static
Option
Description
multi-stage
Multi stage marking.
static
Static marking.
diffserv
Enable/disable changing the DiffServ
setting applied to traffic accepted by
this shaper.
option
-disable
FortiOS 8.0.0 CLI Reference
697
Fortinet Inc.

<!-- 来源页 698 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable setting traffic DiffServ.
disable
Disable setting traffic DiffServ.
diffservcode
DiffServ setting to be applied to traffic
accepted by this shaper.
user
Not Specified
dscp-marking-method
Select DSCP marking method.
option
-static
Option
Description
multi-stage
Multistage marking.
static
Static marking.
exceed-bandwidth
Exceed bandwidth used for DSCP/VLAN
CoS multi-stage marking. Units depend
on the bandwidth-unit setting.
integer
Minimum value:
0 Maximum
value:
80000000 **
0
exceed-class-id
Class ID for traffic in guaranteed-bandwidth and maximum-bandwidth.
integer
Minimum value:
0 Maximum
value:
4294967295
0
exceed-cos
VLAN CoS mark for traffic in
[guaranteed-bandwidth, exceed-bandwidth].
user
Not Specified
exceed-dscp
DSCP mark for traffic in guaranteed-bandwidth and exceed-bandwidth.
user
Not Specified
fabric-force-sync *
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
fabric-object *
Security Fabric global object setting.
option
-disable
FortiOS 8.0.0 CLI Reference
698
Fortinet Inc.

<!-- 来源页 699 -->
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
guaranteed-bandwidth
Amount of bandwidth guaranteed for
this shaper (0 - 80000000). Units
depend on the bandwidth-unit setting.
integer
Minimum value:
0 Maximum
value:
80000000 **
0
maximum-bandwidth
Upper bandwidth limit enforced by this
shaper (0 - 80000000). 0 means no
limit. Units depend on the bandwidth-unit setting.
integer
Minimum value:
0 Maximum
value:
80000000 **
0
maximum-cos
VLAN CoS mark for traffic in [exceed-bandwidth, maximum-bandwidth].
user
Not Specified
maximum-dscp
DSCP mark for traffic in exceed-bandwidth and maximum-bandwidth.
user
Not Specified
name
Traffic shaper name.
string
Maximum
length: 35
overhead
Per-packet size overhead used in rate
computations.
integer
Minimum value:
0 Maximum
value: 100
0
per-policy
Enable/disable applying a separate
shaper for each policy. For example, if
enabled the guaranteed bandwidth is
applied separately for each policy.
option
-disable
Option
Description
disable
All referring policies share one traffic shaper.
enable
Each referring policy has its own traffic shaper.
FortiOS 8.0.0 CLI Reference
699
Fortinet Inc.

---


<!-- 来源页 700 -->
Parameter
Description
Type
Size
Default
priority
Higher priority traffic is more likely to be
forwarded without delays and without
compromising the guaranteed
bandwidth.
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
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
** Values may differ between models.
config firewall shaping-policy
Configure shaping policies.
config firewall shaping-policy
Description: Configure shaping policies.
edit <id>
set app-category <id1>, <id2>, ...
set app-group <name1>, <name2>, ...
set application <id1>, <id2>, ...
set class-id {integer}
set comment {var-string}
set cos {user}
set cos-mask {user}
set diffserv-forward [enable|disable]
set diffserv-reverse [enable|disable]
set diffservcode-forward {user}
set diffservcode-rev {user}
set dstaddr <name1>, <name2>, ...
set dstaddr6 <name1>, <name2>, ...
set dstintf <name1>, <name2>, ...
set groups <name1>, <name2>, ...
set internet-service [enable|disable]
set internet-service-custom <name1>, <name2>, ...
set internet-service-custom-group <name1>, <name2>, ...
set internet-service-fortiguard <name1>, <name2>, ...
set internet-service-group <name1>, <name2>, ...
set internet-service-name <name1>, <name2>, ...
set internet-service-src [enable|disable]
FortiOS 8.0.0 CLI Reference
700
Fortinet Inc.

<!-- 来源页 701 -->
set internet-service-src-custom <name1>, <name2>, ...
set internet-service-src-custom-group <name1>, <name2>, ...
set internet-service-src-fortiguard <name1>, <name2>, ...
set internet-service-src-group <name1>, <name2>, ...
set internet-service-src-name <name1>, <name2>, ...
set ip-version [4|6]
set name {string}
set per-ip-shaper {string}
set schedule {string}
set service <name1>, <name2>, ...
set srcaddr <name1>, <name2>, ...
set srcaddr6 <name1>, <name2>, ...
set srcintf <name1>, <name2>, ...
set status [enable|disable]
set tos {user}
set tos-mask {user}
set tos-negate [enable|disable]
set traffic-shaper {string}
set traffic-shaper-reverse {string}
set traffic-type [forwarding|local-in|...]
set url-category <id1>, <id2>, ...
set users <name1>, <name2>, ...
set uuid {uuid}
next
end
config firewall shaping-policy
Parameter
Description
Type
Size
Default
app-category
<id>
IDs of one or more application
categories that this shaper applies
application control traffic shaping to.
Category IDs.
integer
Minimum value:
0 Maximum
value:
4294967295
app-group
<name>
One or more application group names.
Application group name.
string
Maximum
length: 79
application
<id>
IDs of one or more applications that this
shaper applies application control
traffic shaping to.
Application IDs.
integer
Minimum value:
0 Maximum
value:
4294967295
class-id
Traffic class ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
comment
Comments.
var-string
Maximum
length: 255
FortiOS 8.0.0 CLI Reference
701
Fortinet Inc.

<!-- 来源页 702 -->
Parameter
Description
Type
Size
Default
cos
VLAN CoS bit pattern.
user
Not Specified
cos-mask
VLAN CoS evaluated bits.
user
Not Specified
diffserv-forward
Enable to change packet's DiffServ
values to the specified diffservcode-forward value.
option
-disable
Option
Description
enable
Enable setting forward (original) traffic DiffServ.
disable
Disable setting forward (original) traffic DiffServ.
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
Change packet's DiffServ to this value.
user
Not Specified
diffservcode-rev
Change packet's reverse (reply)
DiffServ to this value.
user
Not Specified
dstaddr <name>
IPv4 destination address and address
group names.
Address name.
string
Maximum
length: 79
dstaddr6
<name>
IPv6 destination address and address
group names.
Address name.
string
Maximum
length: 79
dstintf <name>
One or more outgoing (egress)
interfaces.
Interface name.
string
Maximum
length: 79
groups <name>
Apply this traffic shaping policy to user
groups that have authenticated with
the FortiGate.
Group name.
string
Maximum
length: 79
id
Shaping policy ID (0 - 4294967295).
integer
Minimum value:
0 Maximum
value:
4294967295
0
FortiOS 8.0.0 CLI Reference
702
Fortinet Inc.

<!-- 来源页 703 -->
Parameter
Description
Type
Size
Default
internet-service
Enable/disable use of Internet Services
for this policy. If enabled, destination
address and service are not used.
option
-disable
Option
Description
enable
Enable use of Internet Service in shaping-policy.
disable
Disable use of Internet Service in shaping-policy.
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
Internet Service ID.
Internet Service name.
string
Maximum
length: 79
internet-service-src
Enable/disable use of Internet Services
in source for this policy. If enabled,
source address is not used.
option
-disable
Option
Description
enable
Enable use of Internet Service source in shaping-policy.
disable
Disable use of Internet Service source in shaping-policy.
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
FortiOS 8.0.0 CLI Reference
703
Fortinet Inc.

<!-- 来源页 704 -->
Parameter
Description
Type
Size
Default
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
ip-version
Apply this traffic shaping policy to IPv4
or IPv6 traffic.
option
-4
Option
Description
4
Use IPv4 addressing for Configuration Method.
6
Use IPv6 addressing for Configuration Method.
name
Shaping policy name.
string
Maximum
length: 35
per-ip-shaper
Per-IP traffic shaper to apply with this
policy.
string
Maximum
length: 35
schedule
Schedule name.
string
Maximum
length: 35
service <name>
Service and service group names.
Service name.
string
Maximum
length: 79
srcaddr <name>
IPv4 source address and address group
names.
Address name.
string
Maximum
length: 79
srcaddr6
<name>
IPv6 source address and address group
names.
Address name.
string
Maximum
length: 79
srcintf <name>
One or more incoming (ingress)
interfaces.
Interface name.
string
Maximum
length: 79
status
Enable/disable this traffic shaping
policy.
option
-enable
FortiOS 8.0.0 CLI Reference
704
Fortinet Inc.

<!-- 来源页 705 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable traffic shaping policy.
disable
Disable traffic shaping policy.
tos
ToS (Type of Service) value used for
comparison.
user
Not Specified
tos-mask
Non-zero bit positions are used for
comparison while zero bit positions are
ignored.
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
Traffic shaper to apply to traffic
forwarded by the firewall policy.
string
Maximum
length: 35
traffic-shaper-reverse
Traffic shaper to apply to response
traffic received by the firewall policy.
string
Maximum
length: 35
traffic-type
Traffic type.
option
-forwarding
Option
Description
forwarding
Forwarding traffic.
local-in
Local-in traffic.
local-out
Local-out traffic.
url-category
<id>
IDs of one or more FortiGuard Web
Filtering categories that this shaper
applies traffic shaping to.
URL category ID.
integer
Minimum value:
0 Maximum
value:
4294967295
users <name>
Apply this traffic shaping policy to
individual users that have authenticated
with the FortiGate.
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
FortiOS 8.0.0 CLI Reference
705
Fortinet Inc.

---


<!-- 来源页 706 -->
config firewall shaping-profile
Configure shaping profiles.
config firewall shaping-profile
Description: Configure shaping profiles.
edit <profile-name>
set comment {var-string}
set default-class-id {integer}
set npu-offloading [disable|enable]
config shaping-entries
Description: Define shaping entries of this shaping profile.
edit <id>
set burst-in-msec {integer}
set cburst-in-msec {integer}
set class-id {integer}
set guaranteed-bandwidth-percentage {integer}
set limit {integer}
set max {integer}
set maximum-bandwidth-percentage {integer}
set min {integer}
set priority [top|critical|...]
set red-probability {integer}
next
end
set type [policing|queuing]
next
end
config firewall shaping-profile
Parameter
Description
Type
Size
Default
comment
Comment.
var-string
Maximum
length: 1023
default-class-id
Default class ID to handle unclassified packets
(including all local traffic).
integer
Minimum value:
0 Maximum
value:
4294967295
0
npu-offloading
Enable/disable NPU offloading.
option
-enable
Option
Description
disable
Diable shaper offloading.
enable
Enable shaper offloading.
FortiOS 8.0.0 CLI Reference
706
Fortinet Inc.

<!-- 来源页 707 -->
Parameter
Description
Type
Size
Default
profile-name
Shaping profile name.
string
Maximum
length: 35
type
Select shaping profile type: policing / queuing.
option
-policing
Option
Description
policing
Enable policing mode.
queuing
Enable queuing mode.
config shaping-entries
Parameter
Description
Type
Size
Default
burst-in-msec
Number of bytes that can be burst at
maximum-bandwidth speed. Formula: burst =
maximum-bandwidth*burst-in-msec.
integer
Minimum value:
0 Maximum
value: 2000
0
cburst-in-msec
Number of bytes that can be burst as fast as
the interface can transmit. Formula: cburst =
maximum-bandwidth*cburst-in-msec.
integer
Minimum value:
0 Maximum
value: 2000
0
class-id
Class ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
guaranteed-bandwidth-percentage
Guaranteed bandwidth in percentage.
integer
Minimum value:
0 Maximum
value: 100
0
id
ID number.
integer
Minimum value:
0 Maximum
value:
4294967295
0
limit
Hard limit on the real queue size in packets.
integer
Minimum value:
5 Maximum
value: 10000
100
max
Average queue size in packets at which RED
drop probability is maximal.
integer
Minimum value:
3 Maximum
value: 3000
250
maximum-bandwidth-percentage
Maximum bandwidth in percentage.
integer
Minimum value:
1 Maximum
value: 100
1
FortiOS 8.0.0 CLI Reference
707
Fortinet Inc.

---


<!-- 来源页 708 -->
Parameter
Description
Type
Size
Default
min
Average queue size in packets at which RED
drop becomes a possibility.
integer
Minimum value:
3 Maximum
value: 3000
83
priority
Priority.
option
-high
Option
Description
top
Top priority.
critical
Critical priority.
high
High priority.
medium
Medium priority.
low
Low priority.
red-probability
Maximum probability (in percentage) for RED
marking.
integer
Minimum value:
0 Maximum
value: 20
0
config firewall sniffer
Configure sniffer.
config firewall sniffer
Description: Configure sniffer.
edit <id>
config anomaly
Description: Configuration method to edit Denial of Service (DoS) anomaly settings.
edit <name>
set action [pass|block]
set log [enable|disable]
set quarantine [none|attacker]
set quarantine-expiry {user}
set quarantine-log [disable|enable]
set status [disable|enable]
set threshold {integer}
set threshold(default) {integer}
next
end
set application-list {string}
set application-list-status [enable|disable]
set av-profile {string}
set av-profile-status [enable|disable]
set dlp-profile {string}
set dlp-profile-status [enable|disable]
set dsri [enable|disable]
set emailfilter-profile {string}
FortiOS 8.0.0 CLI Reference
708
Fortinet Inc.

<!-- 来源页 709 -->
set emailfilter-profile-status [enable|disable]
set file-filter-profile {string}
set file-filter-profile-status [enable|disable]
set host {string}
set interface {string}
set ip-threatfeed <name1>, <name2>, ...
set ip-threatfeed-status [enable|disable]
set ips-dos-status [enable|disable]
set ips-sensor {string}
set ips-sensor-status [enable|disable]
set ipv6 [enable|disable]
set logtraffic [all|utm|...]
set non-ip [enable|disable]
set port {string}
set protocol {string}
set status [enable|disable]
set uuid {uuid}
set vlan {string}
set webfilter-profile {string}
set webfilter-profile-status [enable|disable]
next
end
config firewall sniffer
Parameter
Description
Type
Size
Default
application-list
Name of an existing application list.
string
Maximum
length: 47
application-list-status
Enable/disable application control profile.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
av-profile
Name of an existing antivirus profile.
string
Maximum
length: 47
av-profile-status
Enable/disable antivirus profile.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
709
Fortinet Inc.

<!-- 来源页 710 -->
Parameter
Description
Type
Size
Default
dlp-profile
Name of an existing DLP profile.
string
Maximum
length: 47
dlp-profile-status
Enable/disable DLP profile.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
dsri
Enable/disable DSRI.
option
-disable
Option
Description
enable
Enable DSRI.
disable
Disable DSRI.
emailfilter-profile
Name of an existing email filter profile.
string
Maximum
length: 47
emailfilter-profile-status
Enable/disable emailfilter.
option
-disable
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
file-filter-profile-status
Enable/disable file filter.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
host
Hosts to filter for in sniffer traffic (Format
examples: 1.1.1.1, 2.2.2.0/24,
3.3.3.3/255.255.255.0, 4.4.4.0-4.4.4.240).
string
Maximum
length: 63
id
Sniffer ID (0 - 9999).
integer
Minimum
value: 0
Maximum
value: 9999
0
FortiOS 8.0.0 CLI Reference
710
Fortinet Inc.

<!-- 来源页 711 -->
Parameter
Description
Type
Size
Default
interface
Interface name that traffic sniffing will take
place on.
string
Maximum
length: 35
ip-threatfeed
<name>
Name of an existing IP threat feed.
Threat feed name.
string
Maximum
length: 79
ip-threatfeed-status
Enable/disable IP threat feed.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
ips-dos-status
Enable/disable IPS DoS anomaly detection.
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
ips-sensor-status
Enable/disable IPS sensor.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
ipv6
Enable/disable sniffing IPv6 packets.
option
-disable
Option
Description
enable
Enable sniffer for IPv6 packets.
disable
Disable sniffer for IPv6 packets.
logtraffic
Either log all sessions, only sessions that
have a security profile applied, or disable all
logging for this policy.
option
-utm
Option
Description
all
Log all sessions accepted or denied by this policy.
FortiOS 8.0.0 CLI Reference
711
Fortinet Inc.

<!-- 来源页 712 -->
Parameter
Description
Type
Size
Default
Option
Description
utm
Log traffic that has a security profile applied to it.
disable
Disable all logging for this policy.
non-ip
Enable/disable sniffing non-IP packets.
option
-disable
Option
Description
enable
Enable sniffer for non-IP packets.
disable
Disable sniffer for non-IP packets.
port
Ports to sniff (Format examples: 10, :20,
30:40, 50-, 100-200).
string
Maximum
length: 63
protocol
Integer value for the protocol type as
defined by IANA (0 - 255).
string
Maximum
length: 63
status
Enable/disable the active status of the
sniffer.
option
-enable
Option
Description
enable
Enable sniffer status.
disable
Disable sniffer status.
uuid
Universally Unique Identifier (UUID;
automatically assigned but can be manually
reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
vlan
List of VLANs to sniff.
string
Maximum
length: 63
webfilter-profile
Name of an existing web filter profile.
string
Maximum
length: 47
webfilter-profile-status
Enable/disable web filter profile.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
config anomaly
Parameter
Description
Type
Size
Default
action
Action taken when the threshold is reached.
option
-pass
FortiOS 8.0.0 CLI Reference
712
Fortinet Inc.

<!-- 来源页 713 -->
Parameter
Description
Type
Size
Default
Option
Description
pass
Allow traffic but record a log message if logging is enabled.
block
Block traffic if this anomaly is found.
log
Enable/disable anomaly logging.
option
-disable
Option
Description
enable
Enable anomaly logging.
disable
Disable anomaly logging.
name
Anomaly name.
string
Maximum
length: 63
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
Duration of quarantine. (Format ###d##h##m,
minimum 1m, maximum 364d23h59m, default =
5m). Requires quarantine set to attacker.
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
status
Enable/disable this anomaly.
option
-disable
Option
Description
disable
Disable this status.
enable
Enable this status.
threshold
Anomaly threshold. Number of detected
instances (packets per second or concurrent
session number) that triggers the anomaly
action.
integer
Minimum value:
1 Maximum
value:
2147483647
0
FortiOS 8.0.0 CLI Reference
713
Fortinet Inc.

---


<!-- 来源页 717 -->
config firewall ssh local-key
Parameter
Description
Type
Size
Default
name
SSH proxy local key name.
string
Maximum
length: 35
password
Password for SSH private key.
password
Not
Specified
private-key
SSH proxy private key, encrypted with a
password.
user
Not
Specified
public-key
SSH proxy public key.
user
Not
Specified
source
SSH proxy local key source type.
option
-user
Option
Description
built-in
Built-in SSH proxy local keys.
user
User imported SSH proxy local keys.
config firewall ssh setting
SSH proxy settings.
config firewall ssh setting
Description: SSH proxy settings.
set caname {string}
set host-trusted-checking [enable|disable]
set hostkey-dsa1024 {string}
set hostkey-ecdsa256 {string}
set hostkey-ecdsa384 {string}
set hostkey-ecdsa521 {string}
set hostkey-ed25519 {string}
set hostkey-rsa2048 {string}
set untrusted-caname {string}
end
config firewall ssh setting
Parameter
Description
Type
Size
Default
caname
CA certificate used by SSH Inspection.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
717
Fortinet Inc.

---


<!-- 来源页 718 -->
Parameter
Description
Type
Size
Default
host-trusted-checking
Enable/disable host trusted checking.
option
-enable
Option
Description
enable
Enable host key trusted checking.
disable
Disable host key trusted checking.
hostkey-dsa1024
DSA certificate used by SSH proxy.
string
Maximum
length: 35
hostkey-ecdsa256
ECDSA nid256 certificate used by SSH proxy.
string
Maximum
length: 35
hostkey-ecdsa384
ECDSA nid384 certificate used by SSH proxy.
string
Maximum
length: 35
hostkey-ecdsa521
ECDSA nid384 certificate used by SSH proxy.
string
Maximum
length: 35
hostkey-ed25519
ED25519 hostkey used by SSH proxy.
string
Maximum
length: 35
hostkey-rsa2048
RSA certificate used by SSH proxy.
string
Maximum
length: 35
untrusted-caname
Untrusted CA certificate used by SSH Inspection.
string
Maximum
length: 35
config firewall ssl setting
SSL proxy settings.
config firewall ssl setting
Description: SSL proxy settings.
set abbreviate-handshake [enable|disable]
set cert-cache-capacity {integer}
set cert-cache-timeout {integer}
set cert-manager-cache-timeout {integer}
set kxp-queue-threshold {integer}
set no-matching-cipher-action [bypass|drop]
set proxy-connect-timeout {integer}
set resigned-short-lived-certificate [enable|disable]
set session-cache-capacity {integer}
set session-cache-timeout {integer}
set ssl-dh-bits [768|1024|...]
set ssl-queue-threshold {integer}
set ssl-send-empty-frags [enable|disable]
end
FortiOS 8.0.0 CLI Reference
718
Fortinet Inc.

<!-- 来源页 719 -->
config firewall ssl setting
Parameter
Description
Type
Size
Default
abbreviate-handshake
Enable/disable use of SSL abbreviated handshake.
option
-enable
Option
Description
enable
Enable use of SSL abbreviated handshake.
disable
Disable use of SSL abbreviated handshake.
cert-cache-capacity
Maximum capacity of the host certificate cache (0
- 500, default = 200).
integer
Minimum
value: 0
Maximum
value: 500
200
cert-cache-timeout
Time limit to keep certificate cache (1 - 120 min,
default = 10).
integer
Minimum
value: 1
Maximum
value: 120
10
cert-manager-cache-timeout
Time limit for certificate manager to keep FortiGate
re-signed server certificate (24 - 720 hours,
default = 72).
integer
Minimum
value: 24
Maximum
value: 720
72
kxp-queue-threshold *
Maximum length of the CP KXP queue. When the
queue becomes full, the proxy switches cipher
functions to the main CPU (0 - 512, default = 16).
integer
Minimum
value: 0
Maximum
value: 512
16
no-matching-cipher-action
Bypass or drop the connection when no matching
cipher is found.
option
-bypass
Option
Description
bypass
Bypass connection.
drop
Drop connection.
proxy-connect-timeout
Time limit to make an internal connection to the
appropriate proxy process (1 - 60 sec, default =
30).
integer
Minimum
value: 1
Maximum
value: 60
30
resigned-short-lived-certificate
Enable/disable short-lived certificate.
option
-enable
FortiOS 8.0.0 CLI Reference
719
Fortinet Inc.

---


<!-- 来源页 756 -->
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
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be manually
reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
config firewall ttl-policy
Configure TTL policies.
config firewall ttl-policy
Description: Configure TTL policies.
edit <id>
set action [accept|deny]
set schedule {string}
set service <name1>, <name2>, ...
set srcaddr <name1>, <name2>, ...
set srcintf {string}
set status [enable|disable]
set ttl {user}
next
end
FortiOS 8.0.0 CLI Reference
756
Fortinet Inc.
