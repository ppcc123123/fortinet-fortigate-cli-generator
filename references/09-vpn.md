# VPN (IPsec / SSL / 拨号)

> 来源: FortiOS-8.0.0-CLI_Reference.pdf
> 覆盖命令/章节: vpn
> 本文件由 extract_pdf.py 从官方 PDF 自动提取，请勿手动编辑；
> 如需修正请修改 map.json 后重跑脚本。

---


<!-- 来源页 2346 -->
vpn
This section includes syntax for the following commands:
l config vpn certificate ca on page 2346
l config vpn certificate crl on page 2348
l config vpn certificate hsm-local on page 2350
l config vpn certificate local on page 2354
l config vpn certificate ocsp-server on page 2359
l config vpn certificate remote on page 2360
l config vpn certificate setting on page 2361
l config vpn ipsec concentrator on page 2367
l config vpn ipsec fec on page 2368
l config vpn ipsec manualkey-interface on page 2373
l config vpn ipsec manualkey on page 2371
l config vpn ipsec phase1-interface on page 2411
l config vpn ipsec phase1 on page 2375
l config vpn ipsec phase2-interface on page 2471
l config vpn ipsec phase2 on page 2453
l config vpn kmip-server on page 2489
l config vpn l2tp on page 2491
l config vpn pptp on page 2493
l config vpn qkd on page 2493
l config vpn ssl settings on page 2495
l config vpn ssl web portal on page 2508
l config vpn ssl web realm on page 2523
l config vpn ssl web user-bookmark on page 2525
l config vpn ssl web user-group-bookmark on page 2533
config vpn certificate ca
CA certificate.
config vpn certificate ca
Description: CA certificate.
edit <name>
set auto-update-days {integer}
set auto-update-days-warning {integer}
set ca {user}
set ca-identifier {string}
FortiOS 8.0.0 CLI Reference
2346
Fortinet Inc.

<!-- 来源页 2347 -->
set est-url {string}
set fabric-ca [disable|enable]
set obsolete [disable|enable]
set range [global|vdom]
set scep-url {string}
set source [factory|user|...]
set source-ip {ipv4-address}
set ssl-inspection-trusted [enable|disable]
next
end
config vpn certificate ca
Parameter
Description
Type
Size
Default
auto-update-days
Number of days to wait before requesting an
updated CA certificate (0 - 4294967295, 0 =
disabled).
integer
Minimum value:
0 Maximum
value:
4294967295
0
auto-update-days-warning
Number of days before an expiry-warning
message is generated (0 - 4294967295, 0 =
disabled).
integer
Minimum value:
0 Maximum
value:
4294967295
0
ca
CA certificate as a PEM file.
user
Not Specified
ca-identifier
CA identifier of the SCEP server.
string
Maximum
length: 255
est-url
URL of the EST server.
string
Maximum
length: 255
fabric-ca
Enable/disable synchronization of CA across
Security Fabric.
option
-disable
Option
Description
disable
Disable synchronization of CA across Security Fabric.
enable
Enable synchronization of CA across Security Fabric.
name
Name.
string
Maximum
length: 79
obsolete
Enable/disable this CA as obsoleted.
option
-disable
Option
Description
disable
Alive.
enable
Obsolete.
FortiOS 8.0.0 CLI Reference
2347
Fortinet Inc.

<!-- 来源页 2348 -->
Parameter
Description
Type
Size
Default
range
Either global or VDOM IP address range for the
CA certificate.
option
-vdom
Option
Description
global
Global range.
vdom
VDOM IP address range.
scep-url
URL of the SCEP server.
string
Maximum
length: 255
source
CA certificate source type.
option
-user
Option
Description
factory
Factory installed certificate.
user
User generated certificate.
bundle
Bundle file certificate.
source-ip
Source IP address for communications to the
SCEP server.
ipv4-address
Not Specified
0.0.0.0
ssl-inspection-trusted
Enable/disable this CA as a trusted CA for SSL
inspection.
option
-enable
Option
Description
enable
Trusted CA for SSL inspection.
disable
Untrusted CA for SSL inspection.
config vpn certificate crl
Certificate Revocation List as a PEM file.
config vpn certificate crl
Description: Certificate Revocation List as a PEM file.
edit <name>
set crl {user}
set http-url {string}
set ldap-password {password}
set ldap-server {string}
set ldap-username {string}
set range [global|vdom]
set scep-cert {string}
set scep-url {string}
set source [factory|user|...]
FortiOS 8.0.0 CLI Reference
2348
Fortinet Inc.

<!-- 来源页 2349 -->
set source-ip {ipv4-address}
set update-interval {integer}
set update-vdom {string}
next
end
config vpn certificate crl
Parameter
Description
Type
Size
Default
crl
Certificate Revocation List as a PEM file.
user
Not Specified
http-url
HTTP server URL for CRL auto-update.
string
Maximum
length: 255
ldap-password
LDAP server user password.
password
Not Specified
ldap-server
LDAP server name for CRL auto-update.
string
Maximum
length: 35
ldap-username
LDAP server user name.
string
Maximum
length: 63
name
Name.
string
Maximum
length: 35
range
Either global or VDOM IP address range for the
certificate.
option
-vdom
Option
Description
global
Global range.
vdom
VDOM IP address range.
scep-cert
Local certificate for SCEP communication for
CRL auto-update.
string
Maximum
length: 35
Fortinet_
CA_SSL
scep-url
SCEP server URL for CRL auto-update.
string
Maximum
length: 255
source
Certificate source type.
option
-user
Option
Description
factory
Factory installed certificate.
user
User generated certificate.
bundle
Bundle file certificate.
source-ip
Source IP address for communications to a
HTTP or SCEP CA server.
ipv4-address
Not Specified
0.0.0.0
FortiOS 8.0.0 CLI Reference
2349
Fortinet Inc.

<!-- 来源页 2350 -->
Parameter
Description
Type
Size
Default
update-interval
Time in seconds before the FortiGate checks
for an updated CRL. Set to 0 to update only
when it expires.
integer
Minimum value:
0 Maximum
value:
4294967295
0
update-vdom
VDOM for CRL update.
string
Maximum
length: 31
root
config vpn certificate hsm-local
Local certificates whose keys are stored on HSM.
config vpn certificate hsm-local
Description: Local certificates whose keys are stored on HSM.
edit <name>
set api-version [unknown|gch-default]
set certificate {user}
set comments {string}
set gch-cloud-service-name {string}
set gch-cryptokey {string}
set gch-cryptokey-algorithm [rsa-sign-pkcs1-2048-sha256|rsa-sign-pkcs1-3072-sha256|...]
set gch-cryptokey-version {string}
set gch-keyring {string}
set gch-location {string}
set gch-project {string}
set gch-url {string}
set range [global|vdom]
set source [factory|user|...]
set vendor [unknown|gch]
next
end
config vpn certificate hsm-local
Para
met
er
Description
Ty
pe
Size
Def
ault
api-versi
on
API version for communicating with HSM.
opt
ion
-unk
now
n
Option
Description
unknown
Unknown API version.
gch-default
Google Cloud HSM default API.
FortiOS 8.0.0 CLI Reference
2350
Fortinet Inc.

<!-- 来源页 2351 -->
Para
met
er
Description
Ty
pe
Size
Def
ault
certif
icate
PEM format certificate.
use
r
Not
Spe
cifie
d
com
ment
s
Comment.
stri
ng
Max
imu
m
leng
th:
511
gch-clou
d-servi
ce-name
Cloud service config name to generate access token.
stri
ng
Max
imu
m
leng
th:
35
gch-crypt
okey
Google Cloud HSM cryptokey.
stri
ng
Max
imu
m
leng
th:
63
gch-crypt
oke
y-algor
ithm
Google Cloud HSM cryptokey algorithm.
opt
ion
-rsa-sig
n-pkc
s1-204
8-sha
256
Option
Description
rsa-sign-pkcs1-2048-sha256
2048 bit RSA - PKCS#1 v1.5 padding - SHA256 Digest.
rsa-sign-pkcs1-3072-sha256
3072 bit RSA - PKCS#1 v1.5 padding - SHA256 Digest.
rsa-sign-pkcs1-4096-sha256
4096 bit RSA - PKCS#1 v1.5 padding - SHA256 Digest.
FortiOS 8.0.0 CLI Reference
2351
Fortinet Inc.

<!-- 来源页 2352 -->
Para
met
er
Description
Ty
pe
Size
Def
ault
Option
Description
rsa-sign-pkcs1-4096-sha512
4096 bit RSA - PKCS#1 v1.5 padding - SHA512 Digest.
rsa-sign-pss-2048-sha256
2048 bit RSA - PSS padding - SHA256 Digest.
rsa-sign-pss-3072-sha256
3072 bit RSA - PSS padding - SHA256 Digest.
rsa-sign-pss-4096-sha256
4096 bit RSA - PSS padding - SHA256 Digest.
rsa-sign-pss-4096-sha512
4096 bit RSA - PSS padding - SHA256 Digest.
ec-sign-p256-sha256
Elliptic Curve P-256 - SHA256 Digest.
ec-sign-p384-sha384
Elliptic Curve P-384 - SHA384 Digest.
ec-sign-secp256k1-sha256
Elliptic Curvesecp256k1 - SHA256 Digest.
gch-crypt
oke
y-versi
on
Google Cloud HSM cryptokey version.
stri
ng
Max
imu
m
leng
th:
31
gch-keyri
ng
Google Cloud HSM keyring.
stri
ng
Max
imu
m
leng
th:
63
gch-locati
on
Google Cloud HSM location.
stri
ng
Max
imu
m
leng
th:
63
FortiOS 8.0.0 CLI Reference
2352
Fortinet Inc.

<!-- 来源页 2353 -->
Para
met
er
Description
Ty
pe
Size
Def
ault
gch-proje
ct
Google Cloud HSM project ID.
stri
ng
Max
imu
m
leng
th:
31
gch-url
Google Cloud HSM key URL (e.g.
"https://cloudkms.googleapis.com/v1/projects/sampleproject/locations/samplelo
cation/keyRings/samplekeyring/cryptoKeys/sampleKeyName/cryptoKeyVersions
/1"). Read-only.
stri
ng
Max
imu
m
leng
th:
102
4
name
Name.
stri
ng
Max
imu
m
leng
th:
35
rang
e
Either a global or VDOM IP address range for the certificate.
opt
ion
-vdo
m
Option
Description
global
Global range.
vdom
VDOM IP address range.
sour
ce
Certificate source type.
opt
ion
-user
Option
Description
factory
Factory installed certificate.
user
User generated certificate.
bundle
Bundle file certificate.
vend
or
HSM vendor.
opt
ion
-unk
now
n
FortiOS 8.0.0 CLI Reference
2353
Fortinet Inc.

<!-- 来源页 2354 -->
Para
met
er
Description
Ty
pe
Size
Def
ault
Option
Description
unknown
Unknown type of HSM.
gch
Google Cloud HSM.
config vpn certificate local
Local keys and certificates.
config vpn certificate local
Description: Local keys and certificates.
edit <name>
set acme-ca-url {string}
set acme-domain {string}
set acme-eab-key-hmac {password}
set acme-eab-key-id {var-string}
set acme-email {string}
set acme-renew-window {integer}
set acme-rsa-key-size {integer}
set auto-regenerate-days {integer}
set auto-regenerate-days-warning {integer}
set ca-identifier {string}
set certificate {user}
set cmp-path {string}
set cmp-regeneration-method [keyupate|renewal]
set cmp-server {string}
set cmp-server-cert {string}
set comments {string}
set csr {user}
set enroll-protocol [none|scep|...]
set est-ca-id {string}
set est-client-cert {string}
set est-http-password {password}
set est-http-username {string}
set est-regeneration-method [create-new-key|use-existing-key]
set est-server {string}
set est-server-cert {string}
set est-srp-password {password}
set est-srp-username {string}
set ike-localid {string}
set ike-localid-type [asn1dn|fqdn]
set name-encoding [printable|utf8]
set password {password}
set private-key {user}
set private-key-retain [enable|disable]
FortiOS 8.0.0 CLI Reference
2354
Fortinet Inc.

<!-- 来源页 2355 -->
set range [global|vdom]
set scep-password {password}
set scep-url {string}
set source [factory|user|...]
set source-ip {ipv4-address}
set state {user}
next
end
config vpn certificate local
Parameter
Description
Type
Size
Default
acme-ca-url
The URL for the ACME CA
server (Let's Encrypt is the
default provider).
string
Maximum
length: 255
https://acme-v02.api.letsencrypt.org/director
y
acme-domain
A valid domain that
resolves to this FortiGate
unit.
string
Maximum
length: 255
acme-eab-key-hmac
External Account Binding
HMAC Key (URL-encoded
base64).
password
Not Specified
acme-eab-key-id
External Account Binding
Key ID (optional setting).
var-string
Maximum
length: 255
acme-email
Contact email address that
is required by some CAs
like LetsEncrypt.
string
Maximum
length: 255
acme-renew-window
Beginning of the renewal
window (in days before
certificate expiration, 30 by
default).
integer
Minimum
value: 1
Maximum
value: 100
30
acme-rsa-key-size
Length of the RSA private
key of the generated cert
(Minimum 2048 bits).
integer
Minimum
value: 2048
Maximum
value: 4096
2048
auto-regenerate-days
Number of days to wait
before expiry of an
updated local certificate is
requested (0 = disabled).
integer
Minimum
value: 0
Maximum
value:
4294967295
0
FortiOS 8.0.0 CLI Reference
2355
Fortinet Inc.

<!-- 来源页 2356 -->
Parameter
Description
Type
Size
Default
auto-regenerate-days-warning
Number of days to wait
before an expiry warning
message is generated (0 =
disabled).
integer
Minimum
value: 0
Maximum
value:
4294967295
0
ca-identifier
CA identifier of the CA
server for signing via SCEP.
string
Maximum
length: 255
certificate
PEM format certificate.
user
Not Specified
cmp-path
Path location inside CMP
server.
string
Maximum
length: 255
cmp-regeneration-method
CMP auto-regeneration
method.
option
-keyupate
Option
Description
keyupate
Key Update.
renewal
Renewal.
cmp-server
Address and port for CMP
server (format =
address:port).
string
Maximum
length: 63
cmp-server-cert
CMP server certificate.
string
Maximum
length: 79
comments
Comment.
string
Maximum
length: 511
csr
Certificate Signing
Request.
user
Not Specified
enroll-protocol
Certificate enrollment
protocol.
option
-none
Option
Description
none
None (default).
scep
Simple Certificate Enrollment Protocol.
cmpv2
Certificate Management Protocol Version 2.
acme2
Automated Certificate Management Environment Version 2.
est
Enrollment over Secure Transport.
est-ca-id
CA identifier of the CA
server for signing via EST.
string
Maximum
length: 255
FortiOS 8.0.0 CLI Reference
2356
Fortinet Inc.

<!-- 来源页 2357 -->
Parameter
Description
Type
Size
Default
est-client-cert
Certificate used to
authenticate this FortiGate
to EST server.
string
Maximum
length: 79
est-http-password
HTTP Authentication
password for signing via
EST.
password
Not Specified
est-http-username
HTTP Authentication
username for signing via
EST.
string
Maximum
length: 63
est-regeneration-method
EST behavioral options
during re-enrollment.
option
-create-new-key
Option
Description
create-new-key
Create new private key during re-enrollment.
use-existing-key
Reuse existing private key during re-enrollment.
est-server
Address and port for EST
server (e.g.
https://example.com:123
4).
string
Maximum
length: 255
est-server-cert
EST server's certificate
must be verifiable by this
certificate to be
authenticated.
string
Maximum
length: 79
est-srp-password
EST SRP authentication
password.
password
Not Specified
est-srp-username
EST SRP authentication
username.
string
Maximum
length: 63
ike-localid
Local ID the FortiGate uses
for authentication as a VPN
client.
string
Maximum
length: 63
ike-localid-type
IKE local ID type.
option
-asn1dn
Option
Description
asn1dn
ASN.1 distinguished name.
fqdn
Fully qualified domain name.
FortiOS 8.0.0 CLI Reference
2357
Fortinet Inc.

<!-- 来源页 2358 -->
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
name-encoding
Name encoding method for
auto-regeneration.
option
-printable
Option
Description
printable
Printable encoding (default).
utf8
UTF-8 encoding.
password
Password as a PEM file.
password
Not Specified
private-key
PEM format key encrypted
with a password.
user
Not Specified
private-key-retain
Enable/disable retention of
private key during SCEP
renewal (default = disable).
option
-disable
Option
Description
enable
Keep the existing private key during SCEP renewal.
disable
Generate a new private key during SCEP renewal.
range
Either a global or VDOM IP
address range for the
certificate.
option
-vdom
Option
Description
global
Global range.
vdom
VDOM IP address range.
scep-password
SCEP server challenge
password for auto-regeneration.
password
Not Specified
scep-url
SCEP server URL.
string
Maximum
length: 255
source
Certificate source type.
option
-user
Option
Description
factory
Factory installed certificate.
user
User generated certificate.
bundle
Bundle file certificate.
FortiOS 8.0.0 CLI Reference
2358
Fortinet Inc.

<!-- 来源页 2359 -->
Parameter
Description
Type
Size
Default
source-ip
Source IP address for
communications to the
SCEP server.
ipv4-address
Not Specified
0.0.0.0
state
Certificate Signing Request
State. Read-only.
user
Not Specified
config vpn certificate ocsp-server
OCSP server configuration.
config vpn certificate ocsp-server
Description: OCSP server configuration.
edit <name>
set cert {string}
set secondary-cert {string}
set secondary-url {string}
set source-ip {string}
set unavail-action [revoke|ignore]
set url {string}
next
end
config vpn certificate ocsp-server
Parameter
Description
Type
Size
Default
cert
OCSP server certificate.
string
Maximum
length: 127
name
OCSP server entry name.
string
Maximum
length: 35
secondary-cert
Secondary OCSP server certificate.
string
Maximum
length: 127
secondary-url
Secondary OCSP server URL.
string
Maximum
length: 127
source-ip
Source IP address for dynamic AIA and OCSP
queries.
string
Maximum
length: 63
unavail-action
Action when server is unavailable (revoke the
certificate or ignore the result of the check).
option
-revoke
FortiOS 8.0.0 CLI Reference
2359
Fortinet Inc.

<!-- 来源页 2360 -->
Parameter
Description
Type
Size
Default
Option
Description
revoke
Revoke certificate if server is unavailable.
ignore
Ignore OCSP check if server is unavailable.
url
OCSP server URL.
string
Maximum
length: 127
config vpn certificate remote
Remote certificate as a PEM file.
config vpn certificate remote
Description: Remote certificate as a PEM file.
edit <name>
set range [global|vdom]
set remote {user}
set source [factory|user|...]
next
end
config vpn certificate remote
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
range
Either the global or VDOM IP address range for the
remote certificate.
option
-vdom
Option
Description
global
Global range.
vdom
VDOM IP address range.
remote
Remote certificate.
user
Not
Specified
source
Remote certificate source type.
option
-user
Option
Description
factory
Factory installed certificate.
FortiOS 8.0.0 CLI Reference
2360
Fortinet Inc.

<!-- 来源页 2361 -->
Parameter
Description
Type
Size
Default
Option
Description
user
User generated certificate.
bundle
Bundle file certificate.
config vpn certificate setting
VPN certificate setting.
config vpn certificate setting
Description: VPN certificate setting.
set cert-expire-warning {integer}
set certname-dsa1024 {string}
set certname-dsa2048 {string}
set certname-ecdsa256 {string}
set certname-ecdsa384 {string}
set certname-ecdsa521 {string}
set certname-ed25519 {string}
set certname-ed448 {string}
set certname-rsa1024 {string}
set certname-rsa2048 {string}
set certname-rsa4096 {string}
set check-ca-cert [enable|disable]
set check-ca-chain [enable|disable]
set cmp-key-usage-checking [enable|disable]
set cmp-save-extra-certs [enable|disable]
set cn-allow-multi [disable|enable]
set cn-match [substring|value]
config crl-verification
Description: CRL verification options.
set chain-crl-absence [ignore|revoke]
set expiry [ignore|revoke]
set leaf-crl-absence [ignore|revoke]
end
set csr-include-device-sn [enable|disable]
set interface {string}
set interface-select-method [auto|sdwan|...]
set ocsp-default-server {string}
set ocsp-option [certificate|server]
set ocsp-status [enable|mandatory|...]
set proxy {string}
set proxy-password {password}
set proxy-port {integer}
set proxy-username {string}
set source-ip {string}
set ssl-min-proto-version [default|SSLv3|...]
set strict-ocsp-check [enable|disable]
FortiOS 8.0.0 CLI Reference
2361
Fortinet Inc.

<!-- 来源页 2362 -->
set subject-match [substring|value]
set subject-set [subset|superset]
set vrf-select {integer}
end
config vpn certificate setting
Parameter
Description
Type
Size
Default
cert-expire-warning
Number of days before a certificate expires to
send a warning. Set to 0 to disable sending of
the warning (0 - 100, default = 14).
integer
Minimum
value: 0
Maximum
value: 100
14
certname-dsa1024
1024 bit DSA key certificate for re-signing
server certificates for SSL inspection.
string
Maximum
length: 35
Fortinet_
SSL_
DSA1024
certname-dsa2048
2048 bit DSA key certificate for re-signing
server certificates for SSL inspection.
string
Maximum
length: 35
Fortinet_
SSL_
DSA2048
certname-ecdsa256
256 bit ECDSA key certificate for re-signing
server certificates for SSL inspection.
string
Maximum
length: 35
Fortinet_
SSL_
ECDSA256
certname-ecdsa384
384 bit ECDSA key certificate for re-signing
server certificates for SSL inspection.
string
Maximum
length: 35
Fortinet_
SSL_
ECDSA384
certname-ecdsa521
521 bit ECDSA key certificate for re-signing
server certificates for SSL inspection.
string
Maximum
length: 35
Fortinet_
SSL_
ECDSA521
certname-ed25519
253 bit EdDSA key certificate for re-signing
server certificates for SSL inspection.
string
Maximum
length: 35
Fortinet_
SSL_
ED25519
certname-ed448
456 bit EdDSA key certificate for re-signing
server certificates for SSL inspection.
string
Maximum
length: 35
Fortinet_
SSL_ED448
certname-rsa1024
1024 bit RSA key certificate for re-signing
server certificates for SSL inspection.
string
Maximum
length: 35
Fortinet_
SSL_
RSA1024
certname-rsa2048
2048 bit RSA key certificate for re-signing
server certificates for SSL inspection.
string
Maximum
length: 35
Fortinet_
SSL_
RSA2048
certname-rsa4096
4096 bit RSA key certificate for re-signing
server certificates for SSL inspection.
string
Maximum
length: 35
Fortinet_
SSL_
RSA4096
FortiOS 8.0.0 CLI Reference
2362
Fortinet Inc.

<!-- 来源页 2363 -->
Parameter
Description
Type
Size
Default
check-ca-cert
Enable/disable verification of the user
certificate and pass authentication if any CA in
the chain is trusted (default = enable).
option
-enable
Option
Description
enable
Enable verification of the user certificate.
disable
Disable verification of the user certificate.
check-ca-chain
Enable/disable verification of the entire
certificate chain and pass authentication only if
the chain is complete and all of the CAs in the
chain are trusted (default = disable).
option
-disable
Option
Description
enable
Enable verification of the entire certificate chain.
disable
Disable verification of the entire certificate chain.
cmp-key-usage-checking
Enable/disable server certificate key usage
checking in CMP mode (default = enable).
option
-enable
Option
Description
enable
Enable server certificate key usage checking in CMP mode.
disable
Disable server certificate key usage checking in CMP mode.
cmp-save-extra-certs
Enable/disable saving extra certificates in CMP
mode (default = disable).
option
-disable
Option
Description
enable
Enable saving extra certificates in CMP mode.
disable
Disable saving extra certificates in CMP mode.
cn-allow-multi
When searching for a matching certificate, allow
multiple CN fields in certificate subject name
(default = enable).
option
-enable
Option
Description
disable
Does not allow multiple CN entries in certificate matching.
enable
Allow multiple CN entries in certificate matching.
FortiOS 8.0.0 CLI Reference
2363
Fortinet Inc.

<!-- 来源页 2364 -->
Parameter
Description
Type
Size
Default
cn-match
When searching for a matching certificate,
control how to do CN value matching with
certificate subject name (default = substring).
option
-substring
Option
Description
substring
Find a match if the name being searched for is a part or the same as a
certificate CN.
value
Find a match if the name being searched for is same as a certificate CN.
csr-include-device-sn *
Enable/disable inclusion of device serial number
in CSR (default = enable).
option
-enable
Option
Description
enable
Include device serial number in CSR by default.
disable
Do not include device serial number in CSR by default.
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
ocsp-default-server
Default OCSP server.
string
Maximum
length: 35
ocsp-option
Specify whether the OCSP URL is from
certificate or configured OCSP server.
option
-server
Option
Description
certificate
Use URL from certificate.
server
Use URL from configured OCSP server.
ocsp-status
Enable/disable receiving certificates using the
OCSP.
option
-disable
FortiOS 8.0.0 CLI Reference
2364
Fortinet Inc.

<!-- 来源页 2365 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
OCSP is performed if CRL is not checked.
mandatory
If cert is not revoked by CRL, OCSP is performed.
disable
OCSP is not performed.
proxy
Proxy server FQDN or IP for OCSP/CA queries
during certificate verification.
string
Maximum
length: 127
proxy-password
Proxy server password.
password
Not
Specified
proxy-port
Proxy server port (1 - 65535, default = 8080).
integer
Minimum
value: 1
Maximum
value:
65535
8080
proxy-username
Proxy server user name.
string
Maximum
length: 63
source-ip
Source IP address for dynamic AIA and OCSP
queries.
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
strict-ocsp-check
Enable/disable strict mode OCSP checking.
option
-disable
Option
Description
enable
Enable strict mode OCSP checking.
disable
Disable strict mode OCSP checking.
FortiOS 8.0.0 CLI Reference
2365
Fortinet Inc.

<!-- 来源页 2366 -->
Parameter
Description
Type
Size
Default
subject-match
When searching for a matching certificate,
control how to do RDN value matching with
certificate subject name (default = substring).
option
-substring
Option
Description
substring
Find a match if the name being searched for is a part or the same as a
certificate subject RDN.
value
Find a match if the name being searched for is same as a certificate
subject RDN.
subject-set
When searching for a matching certificate,
control how to do RDN set matching with
certificate subject name (default = subset).
option
-subset
Option
Description
subset
Find a match if the name being searched for is a subset of a certificate
subject.
superset
Find a match if the name being searched for is a superset of a certificate
subject.
vrf-select
VRF ID used for connection to server.
integer
Minimum
value: 0
Maximum
value: 511
0
* This parameter may not exist in some models.
config crl-verification
Parameter
Description
Type
Size
Default
chain-crl-absence
CRL verification option when CRL of any certificate
in chain is absent (default = ignore).
option
-ignore
Option
Description
ignore
CRL verification is ignored if CRL of any certificate in chain is absent.
revoke
Certificate will be revoked if CRL of any certificate in chain is absent.
expiry
CRL verification option when CRL is expired (default
= ignore).
option
-ignore
Option
Description
ignore
Certificate status will be verified even if CRL is expired.
revoke
Certificate will be revoked if CRL is expired.
FortiOS 8.0.0 CLI Reference
2366
Fortinet Inc.

<!-- 来源页 2367 -->
Parameter
Description
Type
Size
Default
leaf-crl-absence
CRL verification option when leaf CRL is absent
(default = ignore).
option
-ignore
Option
Description
ignore
CRL verification against leaf certificate is ignored if CRL is absent.
revoke
Certificate will be revoked if CRL of leaf certificate is absent.
config vpn ipsec concentrator
Concentrator configuration.
config vpn ipsec concentrator
Description: Concentrator configuration.
edit <id>
set member <name1>, <name2>, ...
set name {string}
set src-check [disable|enable]
next
end
config vpn ipsec concentrator
Parameter
Description
Type
Size
Default
id
Concentrator ID (1 - 65535).
integer
Minimum
value: 1
Maximum
value:
65535
0
member
<name>
Names of up to 3 VPN tunnels to add to the
concentrator.
Member name.
string
Maximum
length: 79
name
Concentrator name.
string
Maximum
length: 35
src-check
Enable to check source address of phase 2
selector. Disable to check only the destination
selector.
option
-disable
Option
Description
disable
Ignore source selector when choosing tunnel.
enable
Use source selector to choose tunnel.
FortiOS 8.0.0 CLI Reference
2367
Fortinet Inc.

<!-- 来源页 2368 -->
config vpn ipsec fec
Configure Forward Error Correction (FEC) mapping profiles.
config vpn ipsec fec
Description: Configure Forward Error Correction (FEC) mapping profiles.
edit <name>
config mappings
Description: FEC redundancy mapping table.
edit <seqno>
set bandwidth-bi-threshold {integer}
set bandwidth-bi-threshold-negate [enable|disable]
set bandwidth-down-threshold {integer}
set bandwidth-down-threshold-negate [enable|disable]
set bandwidth-up-threshold {integer}
set bandwidth-up-threshold-negate [enable|disable]
set base {integer}
set latency-threshold {integer}
set latency-threshold-negate [enable|disable]
set packet-loss-threshold {integer}
set packet-loss-threshold-negate [enable|disable]
set redundant {integer}
config tos
Description: FEC redundancy mapping table for specific type of service (TOS).
edit <seqno>
set base {integer}
set redundant {integer}
set tos {user}
set tos-mask {user}
next
end
next
end
next
end
config vpn ipsec fec
Parameter
Description
Type
Size
Default
name
Profile name.
string
Maximum length:
35
FortiOS 8.0.0 CLI Reference
2368
Fortinet Inc.

<!-- 来源页 2369 -->
config mappings
Parameter
Description
Type
Size
Default
bandwidth-bi-threshold
Apply FEC parameters when available bi-bandwidth is >= threshold (kbps, 0 means no
threshold).
integer
Minimum value:
0 Maximum
value:
4294967295
0
bandwidth-bi-threshold-negate *
Negate bi-bandwidth threshold.
option
-disable
Option
Description
enable
Enable negated bi-bandwidth threshold.
disable
Disable negated bi-bandwidth threshold.
bandwidth-down-threshold
Apply FEC parameters when available down
bandwidth is >= threshold (kbps, 0 means no
threshold).
integer
Minimum value:
0 Maximum
value:
4294967295
0
bandwidth-down-threshold-negate *
Negate down bandwidth threshold.
option
-disable
Option
Description
enable
Enable negated down bandwidth threshold.
disable
Disable negated down bandwidth threshold.
bandwidth-up-threshold
Apply FEC parameters when available up
bandwidth is >= threshold (kbps, 0 means no
threshold).
integer
Minimum value:
0 Maximum
value:
4294967295
0
bandwidth-up-threshold-negate *
Negate up bandwidth threshold.
option
-disable
Option
Description
enable
Enable negated up bandwidth threshold.
disable
Disable negated up bandwidth threshold.
base
Number of base FEC packets (1 - 40).
integer
Minimum value:
1 Maximum
value: 40 **
0
FortiOS 8.0.0 CLI Reference
2369
Fortinet Inc.

<!-- 来源页 2370 -->
Parameter
Description
Type
Size
Default
latency-threshold
Apply FEC parameters when latency is <=
threshold (0 means no threshold).
integer
Minimum value:
0 Maximum
value:
4294967295
0
latency-threshold-negate *
Negate latency threshold.
option
-disable
Option
Description
enable
Enable negated latency threshold.
disable
Disable negated latency threshold.
packet-loss-threshold
Apply FEC parameters when packet loss is >=
threshold (0 - 100, 0 means no threshold).
integer
Minimum value:
0 Maximum
value: 100
0
packet-loss-threshold-negate *
Negate packet loss threshold.
option
-disable
Option
Description
enable
Enable negated packet loss threshold.
disable
Disable negated packet loss threshold.
redundant
Number of redundant FEC packets (0 - 20).
integer
Minimum value:
0 Maximum
value: 20 **
0
seqno
Sequence number (1 - 64).
integer
Minimum value:
0 Maximum
value: 64
0
* This parameter may not exist in some models.
** Values may differ between models.
config tos
Parameter
Description
Type
Size
Default
base
Number of base FEC packets (1 - 40).
integer
Minimum
value: 1
Maximum
value: 40
0
FortiOS 8.0.0 CLI Reference
2370
Fortinet Inc.

<!-- 来源页 2371 -->
Parameter
Description
Type
Size
Default
redundant
Number of redundant FEC packets (0 - 20).
integer
Minimum
value: 0
Maximum
value: 20
0
seqno
Sequence number (1 - 8).
integer
Minimum
value: 1
Maximum
value: 8
0
tos
Type of service bit pattern.
user
Not
Specified
tos-mask
Type of service evaluated bits.
user
Not
Specified
config vpn ipsec manualkey
Configure IPsec manual keys.
config vpn ipsec manualkey
Description: Configure IPsec manual keys.
edit <name>
set authentication [null|md5|...]
set authkey {user}
set enckey {user}
set encryption [null|des|...]
set interface {string}
set local-gw {ipv4-address-any}
set localspi {user}
set npu-offload [enable|disable]
set remote-gw {ipv4-address}
set remotespi {user}
next
end
config vpn ipsec manualkey
Parameter
Description
Type
Size
Default
authentication
Authentication algorithm. Must be the same for
both ends of the tunnel.
option
-null
Option
Description
null
Null.
FortiOS 8.0.0 CLI Reference
2371
Fortinet Inc.

<!-- 来源页 2372 -->
Parameter
Description
Type
Size
Default
Option
Description
md5
MD5.
sha1
SHA1.
sha256
SHA256.
sha384
SHA384.
sha512
SHA512.
authkey
Hexadecimal authentication key in 16-digit (8-byte) segments separated by hyphens.
user
Not
Specified
enckey
Hexadecimal encryption key in 16-digit (8-byte)
segments separated by hyphens.
user
Not
Specified
encryption
Encryption algorithm. Must be the same for both
ends of the tunnel.
option
-null
Option
Description
null
Null.
des
DES.
3des
3DES.
aes128
AES128.
aes192
AES192.
aes256
AES256.
aria128
ARIA128.
aria192
ARIA192.
aria256
ARIA256.
seed
Seed.
interface
Name of the physical, aggregate, or VLAN
interface.
string
Maximum
length: 15
local-gw
Local gateway.
ipv4-address-any
Not
Specified
0.0.0.0
localspi
Local SPI, a hexadecimal 8-digit (4-byte) tag.
Discerns between two traffic streams with
different encryption rules.
user
Not
Specified
name
IPsec tunnel name.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
2372
Fortinet Inc.

<!-- 来源页 2373 -->
Parameter
Description
Type
Size
Default
npu-offload *
Enable/disable NPU offloading.
option
-enable
Option
Description
enable
Enable NPU offloading.
disable
Disable NPU offloading.
remote-gw
Peer gateway.
ipv4-address
Not
Specified
0.0.0.0
remotespi
Remote SPI, a hexadecimal 8-digit (4-byte) tag.
Discerns between two traffic streams with
different encryption rules.
user
Not
Specified
* This parameter may not exist in some models.
config vpn ipsec manualkey-interface
Configure IPsec manual keys.
config vpn ipsec manualkey-interface
Description: Configure IPsec manual keys.
edit <name>
set addr-type [4|6]
set auth-alg [null|md5|...]
set auth-key {user}
set enc-alg [null|des|...]
set enc-key {user}
set interface {string}
set ip-version [4|6]
set local-gw {ipv4-address-any}
set local-gw6 {ipv6-address}
set local-spi {user}
set npu-offload [enable|disable]
set remote-gw {ipv4-address}
set remote-gw6 {ipv6-address}
set remote-spi {user}
next
end
config vpn ipsec manualkey-interface
Parameter
Description
Type
Size
Default
addr-type
IP version to use for IP packets.
option
-4
FortiOS 8.0.0 CLI Reference
2373
Fortinet Inc.

<!-- 来源页 2374 -->
Parameter
Description
Type
Size
Default
Option
Description
4
Use IPv4 addressing for IP packets.
6
Use IPv6 addressing for IP packets.
auth-alg
Authentication algorithm. Must be the same for
both ends of the tunnel.
option
-null
Option
Description
null
null
md5
md5
sha1
sha1
sha256
sha256
sha384
sha384
sha512
sha512
auth-key
Hexadecimal authentication key in 16-digit (8-byte) segments separated by hyphens.
user
Not
Specified
enc-alg
Encryption algorithm. Must be the same for both
ends of the tunnel.
option
-null
Option
Description
null
null
des
des
3des
3des
aes128
aes128
aes192
aes192
aes256
aes256
aria128
aria128
aria192
aria192
aria256
aria256
seed
seed
enc-key
Hexadecimal encryption key in 16-digit (8-byte)
segments separated by hyphens.
user
Not
Specified
interface
Name of the physical, aggregate, or VLAN
interface.
string
Maximum
length: 15
FortiOS 8.0.0 CLI Reference
2374
Fortinet Inc.

<!-- 来源页 2375 -->
Parameter
Description
Type
Size
Default
ip-version
IP version to use for VPN interface.
option
-4
Option
Description
4
Use IPv4 addressing for gateways.
6
Use IPv6 addressing for gateways.
local-gw
IPv4 address of the local gateway's external
interface.
ipv4-address-any
Not
Specified
0.0.0.0
local-gw6
Local IPv6 address of VPN gateway.
ipv6-address
Not
Specified
::
local-spi
Local SPI, a hexadecimal 8-digit (4-byte) tag.
Discerns between two traffic streams with
different encryption rules.
user
Not
Specified
name
IPsec tunnel name.
string
Maximum
length: 15
npu-offload *
Enable/disable offloading IPsec VPN manual key
sessions to NPUs.
option
-enable
Option
Description
enable
Enable NPU offloading.
disable
Disable NPU offloading.
remote-gw
IPv4 address of the remote gateway's external
interface.
ipv4-address
Not
Specified
0.0.0.0
remote-gw6
Remote IPv6 address of VPN gateway.
ipv6-address
Not
Specified
::
remote-spi
Remote SPI, a hexadecimal 8-digit (4-byte) tag.
Discerns between two traffic streams with
different encryption rules.
user
Not
Specified
* This parameter may not exist in some models.
config vpn ipsec phase1
Configure VPN remote gateway.
config vpn ipsec phase1
Description: Configure VPN remote gateway.
edit <name>
set acct-verify [enable|disable]
set add-gw-route [enable|disable]
FortiOS 8.0.0 CLI Reference
2375
Fortinet Inc.

<!-- 来源页 2376 -->
set add-route [disable|enable]
set addke1 {option1}, {option2}, ...
set addke2 {option1}, {option2}, ...
set addke3 {option1}, {option2}, ...
set addke4 {option1}, {option2}, ...
set addke5 {option1}, {option2}, ...
set addke6 {option1}, {option2}, ...
set addke7 {option1}, {option2}, ...
set assign-ip [disable|enable]
set assign-ip-from [range|usrgrp|...]
set authmethod [psk|signature]
set authmethod-remote [psk|signature]
set authpasswd {password}
set authusr {string}
set authusrgrp {string}
set auto-negotiate [enable|disable]
set auto-transport-threshold {integer}
set azure-ad-autoconnect [enable|disable]
set backup-gateway <address1>, <address2>, ...
set banner {var-string}
set cert-id-validation [enable|disable]
set cert-peer-username-strip [disable|enable]
set cert-peer-username-validation [none|othername|...]
set cert-trust-store [local|ems]
set certificate <name1>, <name2>, ...
set childless-ike [enable|disable]
set client-auto-negotiate [disable|enable]
set client-keep-alive [disable|enable]
set client-resume [enable|disable]
set client-resume-interval {integer}
set comments {var-string}
set dev-id {string}
set dev-id-notification [disable|enable]
set dhcp-ra-giaddr {ipv4-address}
set dhcp6-ra-linkaddr {ipv6-address}
set dhgrp {option1}, {option2}, ...
set digital-signature-auth [enable|disable]
set distance {integer}
set dns-mode [manual|auto]
set dns-suffix-search <dns-suffix1>, <dns-suffix2>, ...
set domain {string}
set dpd [disable|on-idle|...]
set dpd-retrycount {integer}
set dpd-retryinterval {user}
set eap [enable|disable]
set eap-cert-auth [enable|disable]
set eap-exclude-peergrp {string}
set eap-identity [use-id-payload|send-request]
set ems-sn-check [enable|disable]
set enforce-unique-id [disable|keep-new|...]
set esn [require|allow|...]
set exchange-fgt-device-id [enable|disable]
FortiOS 8.0.0 CLI Reference
2376
Fortinet Inc.

<!-- 来源页 2377 -->
set fec-base {integer}
set fec-codec [rs|xor]
set fec-egress [enable|disable]
set fec-health-check {string}
set fec-ingress [enable|disable]
set fec-mapping-profile {string}
set fec-receive-timeout {integer}
set fec-redundant {integer}
set fec-send-timeout {integer}
set fec-separate-redundant-tunnel [enable|disable]
set fgsp-sync [enable|disable]
set fortinet-esp [enable|disable]
set fragmentation [enable|disable]
set fragmentation-mtu {integer}
set group-authentication [enable|disable]
set group-authentication-secret {password-3}
set ha-sync-esp-seqno [enable|disable]
set idle-timeout [enable|disable]
set idle-timeoutinterval {integer}
set ike-version [1|2]
set inbound-dscp-copy [enable|disable]
set include-local-lan [disable|enable]
set interface {string}
set internal-domain-list <domain-name1>, <domain-name2>, ...
set ip-delay-interval {integer}
set ipv4-dns-server1 {ipv4-address}
set ipv4-dns-server2 {ipv4-address}
set ipv4-dns-server3 {ipv4-address}
set ipv4-end-ip {ipv4-address}
config ipv4-exclude-range
Description: Configuration Method IPv4 exclude ranges.
edit <id>
set end-ip {ipv4-address}
set start-ip {ipv4-address}
next
end
set ipv4-name {string}
set ipv4-netmask {ipv4-netmask}
set ipv4-split-exclude {string}
set ipv4-split-include {string}
set ipv4-start-ip {ipv4-address}
set ipv4-wins-server1 {ipv4-address}
set ipv4-wins-server2 {ipv4-address}
set ipv6-auto-linklocal [enable|disable]
set ipv6-dns-server1 {ipv6-address}
set ipv6-dns-server2 {ipv6-address}
set ipv6-dns-server3 {ipv6-address}
set ipv6-end-ip {ipv6-address}
config ipv6-exclude-range
Description: Configuration method IPv6 exclude ranges.
edit <id>
set end-ip {ipv6-address}
FortiOS 8.0.0 CLI Reference
2377
Fortinet Inc.

<!-- 来源页 2378 -->
set start-ip {ipv6-address}
next
end
set ipv6-name {string}
set ipv6-prefix {integer}
set ipv6-split-exclude {string}
set ipv6-split-include {string}
set ipv6-start-ip {ipv6-address}
set keepalive {integer}
set keylife {integer}
set kms {string}
set link-cost {integer}
set local-gw {ipv4-address}
set localid {string}
set localid-type [auto|fqdn|...]
set loopback-asymroute [enable|disable]
set mesh-selector-type [disable|subnet|...]
set mode [aggressive|main]
set mode-cfg [disable|enable]
set mode-cfg-allow-client-selector [disable|enable]
set nattraversal [enable|disable|...]
set negotiate-timeout {integer}
set network-id {integer}
set network-overlay [disable|enable]
set npu-offload [enable|disable]
set peer {string}
set peergrp {string}
set peerid {string}
set peertype [any|one|...]
set ppk [disable|allow|...]
set ppk-identity {string}
set ppk-secret {password-3}
set priority {integer}
set proposal {option1}, {option2}, ...
set psksecret {password-3}
set psksecret-remote {password-3}
set qkd [disable|allow|...]
set qkd-hybrid [disable|allow|...]
set qkd-profile {string}
set reauth [disable|enable]
set rekey [enable|disable]
set remote-gw {ipv4-address}
set remote-gw-country {string}
set remote-gw-end-ip {ipv4-address-any}
set remote-gw-match [any|ipmask|...]
set remote-gw-start-ip {ipv4-address-any}
set remote-gw-subnet {ipv4-classnet-any}
set remote-gw-ztna-tags <name1>, <name2>, ...
set remote-gw6-country {string}
set remote-gw6-end-ip {ipv6-address}
set remote-gw6-match [any|ipprefix|...]
set remote-gw6-start-ip {ipv6-address}
FortiOS 8.0.0 CLI Reference
2378
Fortinet Inc.

<!-- 来源页 2379 -->
set remote-gw6-subnet {ipv6-network}
set remotegw-ddns {string}
set rsa-signature-format [pkcs1|pss]
set rsa-signature-hash-override [enable|disable]
set save-password [disable|enable]
set send-cert-chain [enable|disable]
set shared-idle-timeout [enable|disable]
set signature-hash-alg {option1}, {option2}, ...
set split-include-service {string}
set suite-b [disable|suite-b-gcm-128|...]
set transport [udp|auto|...]
set type [static|dynamic|...]
set unity-support [disable|enable]
set usrgrp {string}
set wizard-type [custom|dialup-forticlient|...]
set xauthtype [disable|client|...]
next
end
config vpn ipsec phase1
Parameter
Description
Type
Size
Default
acct-verify
Enable/disable verification of
RADIUS accounting record.
option
-disable
Option
Description
enable
Enable verification of RADIUS accounting record.
disable
Disable verification of RADIUS accounting record.
add-gw-route
Enable/disable automatically add a
route to the remote gateway.
option
-disable
Option
Description
enable
Automatically add a route to the remote gateway.
disable
Do not automatically add a route to the remote gateway.
add-route
Enable/disable control addition of a
route to peer destination selector.
option
-disable
Option
Description
disable
Do not add a route to destination of peer selector.
enable
Add route to destination of peer selector.
addke1
ADDKE1 group.
option
-FortiOS 8.0.0 CLI Reference
2379
Fortinet Inc.

<!-- 来源页 2380 -->
Parameter
Description
Type
Size
Default
Option
Description
none
NONE.
ml-kem-512
ML-KEM-512.
ml-kem-768
ML-KEM-768.
ml-kem-1024
ML-KEM-1024.
kyber512
KYBER512.
kyber768
KYBER768.
kyber1024
KYBER1024.
frodo-l1
FRODO L1.
frodo-l3
FRODO L3.
frodo-l5
FRODO L5.
bike-l1
BIKE L1.
bike-l3
BIKE L3.
bike-l5
BIKE L5.
hqc128
HQC128.
hqc192
HQC192.
hqc256
HQC256.
0
NONE.
35
ML-KEM-512.
36
ML-KEM-768.
37
ML-KEM-1024.
1080
KYBER512.
1081
KYBER768.
1082
KYBER1024.
1083
FRODO L1.
1084
FRODO L3.
1085
FRODO L5.
1089
BIKE L1.
1090
BIKE L3.
1091
BIKE L5.
FortiOS 8.0.0 CLI Reference
2380
Fortinet Inc.

<!-- 来源页 2381 -->
Parameter
Description
Type
Size
Default
Option
Description
1092
HQC128.
1093
HQC192.
1094
HQC256.
addke2
ADDKE2 group.
option
-Option
Description
none
NONE.
ml-kem-512
ML-KEM-512.
ml-kem-768
ML-KEM-768.
ml-kem-1024
ML-KEM-1024.
kyber512
KYBER512.
kyber768
KYBER768.
kyber1024
KYBER1024.
frodo-l1
FRODO L1.
frodo-l3
FRODO L3.
frodo-l5
FRODO L5.
bike-l1
BIKE L1.
bike-l3
BIKE L3.
bike-l5
BIKE L5.
hqc128
HQC128.
hqc192
HQC192.
hqc256
HQC256.
0
NONE.
35
ML-KEM-512.
36
ML-KEM-768.
37
ML-KEM-1024.
1080
KYBER512.
1081
KYBER768.
1082
KYBER1024.
FortiOS 8.0.0 CLI Reference
2381
Fortinet Inc.

<!-- 来源页 2382 -->
Parameter
Description
Type
Size
Default
Option
Description
1083
FRODO L1.
1084
FRODO L3.
1085
FRODO L5.
1089
BIKE L1.
1090
BIKE L3.
1091
BIKE L5.
1092
HQC128.
1093
HQC192.
1094
HQC256.
addke3
ADDKE3 group.
option
-Option
Description
none
NONE.
ml-kem-512
ML-KEM-512.
ml-kem-768
ML-KEM-768.
ml-kem-1024
ML-KEM-1024.
kyber512
KYBER512.
kyber768
KYBER768.
kyber1024
KYBER1024.
frodo-l1
FRODO L1.
frodo-l3
FRODO L3.
frodo-l5
FRODO L5.
bike-l1
BIKE L1.
bike-l3
BIKE L3.
bike-l5
BIKE L5.
hqc128
HQC128.
hqc192
HQC192.
hqc256
HQC256.
0
NONE.
FortiOS 8.0.0 CLI Reference
2382
Fortinet Inc.

<!-- 来源页 2383 -->
Parameter
Description
Type
Size
Default
Option
Description
35
ML-KEM-512.
36
ML-KEM-768.
37
ML-KEM-1024.
1080
KYBER512.
1081
KYBER768.
1082
KYBER1024.
1083
FRODO L1.
1084
FRODO L3.
1085
FRODO L5.
1089
BIKE L1.
1090
BIKE L3.
1091
BIKE L5.
1092
HQC128.
1093
HQC192.
1094
HQC256.
addke4
ADDKE4 group.
option
-Option
Description
none
NONE.
ml-kem-512
ML-KEM-512.
ml-kem-768
ML-KEM-768.
ml-kem-1024
ML-KEM-1024.
kyber512
KYBER512.
kyber768
KYBER768.
kyber1024
KYBER1024.
frodo-l1
FRODO L1.
frodo-l3
FRODO L3.
frodo-l5
FRODO L5.
bike-l1
BIKE L1.
FortiOS 8.0.0 CLI Reference
2383
Fortinet Inc.

<!-- 来源页 2384 -->
Parameter
Description
Type
Size
Default
Option
Description
bike-l3
BIKE L3.
bike-l5
BIKE L5.
hqc128
HQC128.
hqc192
HQC192.
hqc256
HQC256.
0
NONE.
35
ML-KEM-512.
36
ML-KEM-768.
37
ML-KEM-1024.
1080
KYBER512.
1081
KYBER768.
1082
KYBER1024.
1083
FRODO L1.
1084
FRODO L3.
1085
FRODO L5.
1089
BIKE L1.
1090
BIKE L3.
1091
BIKE L5.
1092
HQC128.
1093
HQC192.
1094
HQC256.
addke5
ADDKE5 group.
option
-Option
Description
none
NONE.
ml-kem-512
ML-KEM-512.
ml-kem-768
ML-KEM-768.
ml-kem-1024
ML-KEM-1024.
kyber512
KYBER512.
FortiOS 8.0.0 CLI Reference
2384
Fortinet Inc.

<!-- 来源页 2385 -->
Parameter
Description
Type
Size
Default
Option
Description
kyber768
KYBER768.
kyber1024
KYBER1024.
frodo-l1
FRODO L1.
frodo-l3
FRODO L3.
frodo-l5
FRODO L5.
bike-l1
BIKE L1.
bike-l3
BIKE L3.
bike-l5
BIKE L5.
hqc128
HQC128.
hqc192
HQC192.
hqc256
HQC256.
0
NONE.
35
ML-KEM-512.
36
ML-KEM-768.
37
ML-KEM-1024.
1080
KYBER512.
1081
KYBER768.
1082
KYBER1024.
1083
FRODO L1.
1084
FRODO L3.
1085
FRODO L5.
1089
BIKE L1.
1090
BIKE L3.
1091
BIKE L5.
1092
HQC128.
1093
HQC192.
1094
HQC256.
addke6
ADDKE6 group.
option
-FortiOS 8.0.0 CLI Reference
2385
Fortinet Inc.

<!-- 来源页 2386 -->
Parameter
Description
Type
Size
Default
Option
Description
none
NONE.
ml-kem-512
ML-KEM-512.
ml-kem-768
ML-KEM-768.
ml-kem-1024
ML-KEM-1024.
kyber512
KYBER512.
kyber768
KYBER768.
kyber1024
KYBER1024.
frodo-l1
FRODO L1.
frodo-l3
FRODO L3.
frodo-l5
FRODO L5.
bike-l1
BIKE L1.
bike-l3
BIKE L3.
bike-l5
BIKE L5.
hqc128
HQC128.
hqc192
HQC192.
hqc256
HQC256.
0
NONE.
35
ML-KEM-512.
36
ML-KEM-768.
37
ML-KEM-1024.
1080
KYBER512.
1081
KYBER768.
1082
KYBER1024.
1083
FRODO L1.
1084
FRODO L3.
1085
FRODO L5.
1089
BIKE L1.
1090
BIKE L3.
1091
BIKE L5.
FortiOS 8.0.0 CLI Reference
2386
Fortinet Inc.

<!-- 来源页 2387 -->
Parameter
Description
Type
Size
Default
Option
Description
1092
HQC128.
1093
HQC192.
1094
HQC256.
addke7
ADDKE7 group.
option
-Option
Description
none
NONE.
ml-kem-512
ML-KEM-512.
ml-kem-768
ML-KEM-768.
ml-kem-1024
ML-KEM-1024.
kyber512
KYBER512.
kyber768
KYBER768.
kyber1024
KYBER1024.
frodo-l1
FRODO L1.
frodo-l3
FRODO L3.
frodo-l5
FRODO L5.
bike-l1
BIKE L1.
bike-l3
BIKE L3.
bike-l5
BIKE L5.
hqc128
HQC128.
hqc192
HQC192.
hqc256
HQC256.
0
NONE.
35
ML-KEM-512.
36
ML-KEM-768.
37
ML-KEM-1024.
1080
KYBER512.
1081
KYBER768.
1082
KYBER1024.
FortiOS 8.0.0 CLI Reference
2387
Fortinet Inc.

<!-- 来源页 2388 -->
Parameter
Description
Type
Size
Default
Option
Description
1083
FRODO L1.
1084
FRODO L3.
1085
FRODO L5.
1089
BIKE L1.
1090
BIKE L3.
1091
BIKE L5.
1092
HQC128.
1093
HQC192.
1094
HQC256.
assign-ip
Enable/disable assignment of IP to
IPsec interface via configuration
method.
option
-enable
Option
Description
disable
Do not assign an IP address to the IPsec interface.
enable
Assign an IP address to the IPsec interface.
assign-ip-from
Method by which the IP address will
be assigned.
option
-range
Option
Description
range
Assign IP address from locally defined range.
usrgrp
Assign IP address via user group.
dhcp
Assign IP address via DHCP.
name
Assign IP address from firewall address or group.
authmethod
Authentication method.
option
-psk
Option
Description
psk
PSK authentication method.
signature
Signature authentication method.
authmethod-remote
Authentication method (remote
side).
option
-FortiOS 8.0.0 CLI Reference
2388
Fortinet Inc.

<!-- 来源页 2389 -->
Parameter
Description
Type
Size
Default
Option
Description
psk
PSK authentication method.
signature
Signature authentication method.
authpasswd
XAuth password (max 35
characters).
password
Not
Specified
authusr
XAuth user name.
string
Maximum
length: 64
authusrgrp
Authentication user group.
string
Maximum
length: 35
auto-negotiate
Enable/disable automatic initiation
of IKE SA negotiation.
option
-enable
Option
Description
enable
Enable automatic initiation of IKE SA negotiation.
disable
Disable automatic initiation of IKE SA negotiation.
auto-transport-threshold
Timeout in seconds before falling
back to next transport protocol.
integer
Minimum
value: 1
Maximum
value: 300
15
azure-ad-autoconnect
Enable/disable Azure AD Auto-Connect for FortiClient.
option
-disable
Option
Description
enable
Enable Azure AD Auto-Connect for FortiClient.
disable
Disable Azure AD Auto-Connect for FortiClient.
backup-gateway
<address>
Instruct unity clients about the
backup gateway address(es).
Address of backup gateway.
string
Maximum
length: 79
banner
Message that unity client should
display after connecting.
var-string
Maximum
length: 1024
cert-id-validation
Enable/disable cross validation of
peer ID and the identity in the peer's
certificate as specified in RFC 4945.
option
-enable
FortiOS 8.0.0 CLI Reference
2389
Fortinet Inc.

<!-- 来源页 2390 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable cross validation of peer ID and the identity in the peer's
certificate as specified in RFC 4945.
disable
Disable cross validation of peer ID and the identity in the peer's
certificate as specified in RFC 4945.
cert-peer-username-strip
Enable/disable domain stripping on
certificate identity.
option
-disable
Option
Description
disable
Disable domain stripping on certificate identity.
enable
Enable domain stripping on certificate identity.
cert-peer-username-validation
Enable/disable cross validation of
peer username and the identity in
the peer's certificate.
option
-none
Option
Description
none
Disable cross validation of peer username and the identity in the
peer's certificate.
othername
Validate principal name in SAN othername.
rfc822name
Validate RFC822 email address in SAN.
cn
Validate CN in subject.
cert-trust-store
CA certificate trust store.
option
-local
Option
Description
local
Use local CA certificate.
ems
Use EMS CA certificate.
certificate <name>
Names of up to 4 signed personal
certificates.
Certificate name.
string
Maximum
length: 79
childless-ike
Enable/disable childless IKEv2
initiation (RFC 6023).
option
-disable
Option
Description
enable
Enable childless IKEv2 initiation (RFC 6023).
disable
Disable childless IKEv2 initiation (RFC 6023).
FortiOS 8.0.0 CLI Reference
2390
Fortinet Inc.

<!-- 来源页 2391 -->
Parameter
Description
Type
Size
Default
client-auto-negotiate
Enable/disable allowing the VPN
client to bring up the tunnel when
there is no traffic.
option
-disable
Option
Description
disable
Disable allowing the VPN client to bring up the tunnel when there is
no traffic.
enable
Enable allowing the VPN client to bring up the tunnel when there is no
traffic.
client-keep-alive
Enable/disable allowing the VPN
client to keep the tunnel up when
there is no traffic.
option
-disable
Option
Description
disable
Disable allowing the VPN client to keep the tunnel up when there is
no traffic.
enable
Enable allowing the VPN client to keep the tunnel up when there is no
traffic.
client-resume
Enable/disable resumption of offline
FortiClient sessions. When a
FortiClient enabled laptop is closed
or enters sleep/hibernate mode,
enabling this feature allows
FortiClient to keep the tunnel during
this period, and allows users to
immediately resume using the IPsec
tunnel when the device wakes up.
option
-disable
Option
Description
enable
Enable client session resumption.
disable
Disable client session resumption.
client-resume-interval
Maximum time in seconds during
which a VPN client may resume
using a tunnel after a client PC has
entered sleep mode or temporarily
lost its network connection (120 -172800, default = 7200).
integer
Minimum
value: 120
Maximum
value:
172800
7200
comments
Comment.
var-string
Maximum
length: 255
FortiOS 8.0.0 CLI Reference
2391
Fortinet Inc.

<!-- 来源页 2392 -->
Parameter
Description
Type
Size
Default
dev-id
Device ID carried by the device ID
notification.
string
Maximum
length: 63
dev-id-notification
Enable/disable device ID
notification.
option
-disable
Option
Description
disable
Disable device ID notification.
enable
Enable device ID notification.
dhcp-ra-giaddr
Relay agent gateway IP address to
use in the giaddr field of DHCP
requests.
ipv4-address
Not
Specified
0.0.0.0
dhcp6-ra-linkaddr
Relay agent IPv6 link address to use
in DHCP6 requests.
ipv6-address
Not
Specified
::
dhgrp
DH group.
option
-20
Option
Description
1
DH Group 1.
2
DH Group 2.
5
DH Group 5.
14
DH Group 14.
15
DH Group 15.
16
DH Group 16.
17
DH Group 17.
18
DH Group 18.
19
DH Group 19.
20
DH Group 20.
21
DH Group 21.
27
DH Group 27.
28
DH Group 28.
29
DH Group 29.
30
DH Group 30.
31
DH Group 31.
32
DH Group 32.
FortiOS 8.0.0 CLI Reference
2392
Fortinet Inc.

<!-- 来源页 2393 -->
Parameter
Description
Type
Size
Default
digital-signature-auth
Enable/disable IKEv2 Digital
Signature Authentication (RFC
7427).
option
-disable
Option
Description
enable
Enable IKEv2 Digital Signature Authentication (RFC 7427).
disable
Disable IKEv2 Digital Signature Authentication (RFC 7427).
distance
Distance for routes added by IKE (1
- 255).
integer
Minimum
value: 1
Maximum
value: 255
15
dns-mode
DNS server mode.
option
-manual
Option
Description
manual
Manually configure DNS servers.
auto
Use default DNS servers.
dns-suffix-search <dns-suffix>
One or more DNS domain name
suffixes in quotes separated by
spaces.
DNS suffix.
string
Maximum
length: 79
domain
Instruct unity clients about the
single default DNS domain.
string
Maximum
length: 63
dpd
Dead Peer Detection mode.
option
-on-demand
Option
Description
disable
Disable Dead Peer Detection.
on-idle
Trigger Dead Peer Detection when IPsec is idle.
on-demand
Trigger Dead Peer Detection when IPsec traffic is sent but no reply is
received from the peer.
dpd-retrycount
Number of DPD retry attempts.
integer
Minimum
value: 1
Maximum
value: 10
3
dpd-retryinterval
DPD retry interval.
user
Not
Specified
eap
Enable/disable IKEv2 EAP
authentication.
option
-disable
FortiOS 8.0.0 CLI Reference
2393
Fortinet Inc.

<!-- 来源页 2394 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable IKEv2 EAP authentication.
disable
Disable IKEv2 EAP authentication.
eap-cert-auth
Enable/disable peer certificate
authentication in addition to EAP if
peer is a FortiClient endpoint.
option
-disable
Option
Description
enable
Enable peer certificate authentication in addition to EAP if peer is a
FortiClient endpoint.
disable
Disable peer certificate authentication in addition to EAP if peer is a
FortiClient endpoint.
eap-exclude-peergrp
Peer group excluded from EAP
authentication.
string
Maximum
length: 35
eap-identity
IKEv2 EAP peer identity type.
option
-use-id-payload
Option
Description
use-id-payload
Use IKEv2 IDi payload to resolve peer identity.
send-request
Use EAP identity request to resolve peer identity.
ems-sn-check
Enable/disable verification of EMS
serial number.
option
-disable
Option
Description
enable
Enable EMS serial number verification.
disable
Disable EMS serial number verification.
enforce-unique-id
Enable/disable peer ID uniqueness
check.
option
-disable
Option
Description
disable
Disable peer ID uniqueness enforcement.
keep-new
Enforce peer ID uniqueness, keep new connection if collision found.
keep-old
Enforce peer ID uniqueness, keep old connection if collision found.
esn *
Extended sequence number (ESN)
negotiation.
option
-disable
FortiOS 8.0.0 CLI Reference
2394
Fortinet Inc.

<!-- 来源页 2395 -->
Parameter
Description
Type
Size
Default
Option
Description
require
Require extended sequence number.
allow
Allow extended sequence number.
disable
Disable extended sequence number.
exchange-fgt-device-id
Enable/disable device identifier
exchange with peer FortiGate units
for use of VPN monitor data by
FortiManager.
option
-disable
Option
Description
enable
Enable exchange of FortiGate device identifier.
disable
Disable exchange of FortiGate device identifier.
fec-base
Number of base Forward Error
Correction packets (1 - 40).
integer
Minimum
value: 1
Maximum
value: 40 **
10
fec-codec
Forward Error Correction
encoding/decoding algorithm.
option
-rs
Option
Description
rs
Reed-Solomon FEC algorithm.
xor
XOR FEC algorithm.
fec-egress
Enable/disable Forward Error
Correction for egress IPsec traffic.
option
-disable
Option
Description
enable
Enable Forward Error Correction for egress IPsec traffic.
disable
Disable Forward Error Correction for egress IPsec traffic.
fec-health-check
SD-WAN health check.
string
Maximum
length: 35
fec-ingress
Enable/disable Forward Error
Correction for ingress IPsec traffic.
option
-disable
Option
Description
enable
Enable Forward Error Correction for ingress IPsec traffic.
disable
Disable Forward Error Correction for ingress IPsec traffic.
FortiOS 8.0.0 CLI Reference
2395
Fortinet Inc.

<!-- 来源页 2396 -->
Parameter
Description
Type
Size
Default
fec-mapping-profile
Forward Error Correction (FEC)
mapping profile.
string
Maximum
length: 35
fec-receive-timeout
Timeout in milliseconds before
dropping Forward Error Correction
packets (1 - 1000).
integer
Minimum
value: 1
Maximum
value: 1000
50
fec-redundant
Number of redundant Forward Error
Correction packets (1 - 20 for reed-solomon, 1 for xor).
integer
Minimum
value: 1
Maximum
value: 20 **
1
fec-send-timeout
Timeout in milliseconds before
sending Forward Error Correction
packets (1 - 1000).
integer
Minimum
value: 1
Maximum
value: 1000
5
fec-separate-redundant-tunnel
*
Enable/disable Forward Error
Correction redundancy on separate
tunnel.
option
-disable
Option
Description
enable
Enable Forward Error Correction redundancy on separate tunnel.
disable
Disable Forward Error Correction redundancy on separate tunnel.
fgsp-sync
Enable/disable IPsec syncing of
tunnels for FGSP IPsec.
option
-disable
Option
Description
enable
Enable IPsec syncing of tunnels to other cluster members.
disable
Disable IPsec syncing of tunnels to other cluster members.
fortinet-esp
Enable/disable Fortinet ESP
encapsulation.
option
-disable
Option
Description
enable
Enable Fortinet ESP encapsulation.
disable
Disable Fortinet ESP encapsulation.
fragmentation
Enable/disable fragment IKE
message on re-transmission.
option
-enable
FortiOS 8.0.0 CLI Reference
2396
Fortinet Inc.

<!-- 来源页 2397 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable intra-IKE fragmentation support on re-transmission.
disable
Disable intra-IKE fragmentation support.
fragmentation-mtu
IKE fragmentation MTU (500 -16000).
integer
Minimum
value: 500
Maximum
value: 16000
1200
group-authentication
Enable/disable IKEv2 IDi group
authentication.
option
-disable
Option
Description
enable
Enable IKEv2 IDi group authentication.
disable
Disable IKEv2 IDi group authentication.
group-authentication-secret
Password for IKEv2 ID group
authentication. ASCII string or
hexadecimal indicated by a leading
0x.
password-3
Not
Specified
ha-sync-esp-seqno
Enable/disable sequence number
jump ahead for IPsec HA.
option
-enable
Option
Description
enable
Enable HA syncing of ESP sequence numbers.
disable
Disable HA syncing of ESP sequence numbers.
idle-timeout
Enable/disable IPsec tunnel idle
timeout.
option
-disable
Option
Description
enable
Enable IPsec tunnel idle timeout.
disable
Disable IPsec tunnel idle timeout.
idle-timeoutinterval
IPsec tunnel idle timeout in minutes
(5 - 43200).
integer
Minimum
value: 5
Maximum
value:
43200
15
ike-version
IKE protocol version.
option
-2 **
FortiOS 8.0.0 CLI Reference
2397
Fortinet Inc.

<!-- 来源页 2398 -->
Parameter
Description
Type
Size
Default
Option
Description
1
Use IKEv1 protocol.
2
Use IKEv2 protocol.
inbound-dscp-copy
Enable/disable copy the dscp in the
ESP header to the inner IP Header.
option
-disable
Option
Description
enable
Enable copy the dscp in the ESP header to the inner IP Header.
disable
Disable copy the dscp in the ESP header to the inner IP Header.
include-local-lan
Enable/disable allow local LAN
access on unity clients.
option
-disable
Option
Description
disable
Disable local LAN access on Unity clients.
enable
Enable local LAN access on Unity clients.
interface
Local physical, aggregate,
loopback, or VLAN outgoing
interface.
string
Maximum
length: 35
internal-domain-list <domain-name>
One or more internal domain names
in quotes separated by spaces.
Domain name.
string
Maximum
length: 79
ip-delay-interval
IP address reuse delay interval in
seconds (0 - 28800).
integer
Minimum
value: 0
Maximum
value: 28800
0
ipv4-dns-server1
IPv4 DNS server 1.
ipv4-address
Not
Specified
0.0.0.0
ipv4-dns-server2
IPv4 DNS server 2.
ipv4-address
Not
Specified
0.0.0.0
ipv4-dns-server3
IPv4 DNS server 3.
ipv4-address
Not
Specified
0.0.0.0
ipv4-end-ip
End of IPv4 range.
ipv4-address
Not
Specified
0.0.0.0
ipv4-name
IPv4 address name.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
2398
Fortinet Inc.

<!-- 来源页 2399 -->
Parameter
Description
Type
Size
Default
ipv4-netmask
IPv4 Netmask.
ipv4-netmask
Not
Specified
255.255.255.255
ipv4-split-exclude
IPv4 subnets that should not be
sent over the IPsec tunnel.
string
Maximum
length: 79
ipv4-split-include
IPv4 split-include subnets.
string
Maximum
length: 79
ipv4-start-ip
Start of IPv4 range.
ipv4-address
Not
Specified
0.0.0.0
ipv4-wins-server1
WINS server 1.
ipv4-address
Not
Specified
0.0.0.0
ipv4-wins-server2
WINS server 2.
ipv4-address
Not
Specified
0.0.0.0
ipv6-auto-linklocal
Enable/disable auto generation of
IPv6 link-local address using last 8
bytes of mode-cfg assigned IPv6
address.
option
-disable
Option
Description
enable
Enable mode-cfg auto configuration of IPv6 link-local address.
disable
Disable mode-cfg auto configuration of IPv6 link-local address.
ipv6-dns-server1
IPv6 DNS server 1.
ipv6-address
Not
Specified
::
ipv6-dns-server2
IPv6 DNS server 2.
ipv6-address
Not
Specified
::
ipv6-dns-server3
IPv6 DNS server 3.
ipv6-address
Not
Specified
::
ipv6-end-ip
End of IPv6 range.
ipv6-address
Not
Specified
::
ipv6-name
IPv6 address name.
string
Maximum
length: 79
ipv6-prefix
IPv6 prefix.
integer
Minimum
value: 1
Maximum
value: 128
128
ipv6-split-exclude
IPv6 subnets that should not be
sent over the IPsec tunnel.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
2399
Fortinet Inc.

<!-- 来源页 2400 -->
Parameter
Description
Type
Size
Default
ipv6-split-include
IPv6 split-include subnets.
string
Maximum
length: 79
ipv6-start-ip
Start of IPv6 range.
ipv6-address
Not
Specified
::
keepalive
NAT-T keep alive interval.
integer
Minimum
value: 5
Maximum
value: 900
10
keylife
Time to wait in seconds before
phase 1 encryption key expires.
integer
Minimum
value: 120
Maximum
value:
172800
86400
kms
Key Management Services server.
string
Maximum
length: 35
link-cost
VPN tunnel underlay link cost.
integer
Minimum
value: 0
Maximum
value: 255
0
local-gw
Local VPN gateway.
ipv4-address
Not
Specified
0.0.0.0
localid
Local ID.
string
Maximum
length: 63
localid-type
Local ID type.
option
-auto
Option
Description
auto
Select ID type automatically.
fqdn
Use fully qualified domain name.
user-fqdn
Use user fully qualified domain name.
keyid
Use key-id string.
address
Use local IP address.
asn1dn
Use ASN.1 distinguished name.
loopback-asymroute
Enable/disable asymmetric routing
for IKE traffic on loopback interface.
option
-enable
FortiOS 8.0.0 CLI Reference
2400
Fortinet Inc.

<!-- 来源页 2401 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Allow ingress/egress IKE traffic to be routed over different
interfaces.
disable
Ingress/egress IKE traffic must be routed over the same interface.
mesh-selector-type
Add selectors containing subsets of
the configuration depending on
traffic.
option
-disable
Option
Description
disable
Disable.
subnet
Enable addition of matching subnet selector.
host
Enable addition of host to host selector.
mode
ID protection mode used to
establish a secure channel.
option
-main
Option
Description
aggressive
Aggressive mode.
main
Main mode.
mode-cfg
Enable/disable configuration
method.
option
-disable
Option
Description
disable
Disable Configuration Method.
enable
Enable Configuration Method.
mode-cfg-allow-client-selector
Enable/disable mode-cfg client to
use custom phase2 selectors.
option
-disable
Option
Description
disable
Mode-cfg client to use wildcard selectors.
enable
Mode-cfg client to use custom selectors.
name
IPsec remote gateway name.
string
Maximum
length: 35
nattraversal
Enable/disable NAT traversal.
option
-enable
FortiOS 8.0.0 CLI Reference
2401
Fortinet Inc.

<!-- 来源页 2402 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable IPsec NAT traversal.
disable
Disable IPsec NAT traversal.
forced
Force IPsec NAT traversal on.
negotiate-timeout
IKE SA negotiation timeout in
seconds (1 - 300).
integer
Minimum
value: 1
Maximum
value: 300
30
network-id
VPN gateway network ID.
integer
Minimum
value: 0
Maximum
value: 255
0
network-overlay
Enable/disable network overlays.
option
-disable
Option
Description
disable
Disable network overlays.
enable
Enable network overlays.
npu-offload *
Enable/disable offloading NPU.
option
-enable
Option
Description
enable
Enable NPU offloading.
disable
Disable NPU offloading.
peer
Accept this peer certificate.
string
Maximum
length: 35
peergrp
Accept this peer certificate group.
string
Maximum
length: 35
peerid
Accept this peer identity.
string
Maximum
length: 255
peertype
Accept this peer type.
option
-peer
Option
Description
any
Accept any peer ID.
one
Accept this peer ID.
dialup
Accept peer ID in dialup group.
FortiOS 8.0.0 CLI Reference
2402
Fortinet Inc.

<!-- 来源页 2403 -->
Parameter
Description
Type
Size
Default
Option
Description
peer
Accept this peer certificate.
peergrp
Accept this peer certificate group.
ppk
Enable/disable IKEv2 Postquantum
Preshared Key (PPK).
option
-disable
Option
Description
disable
Disable use of IKEv2 Postquantum Preshared Key (PPK).
allow
Allow, but do not require, use of IKEv2 Postquantum Preshared Key
(PPK).
require
Require use of IKEv2 Postquantum Preshared Key (PPK).
ppk-identity
IKEv2 Postquantum Preshared Key
Identity.
string
Maximum
length: 35
ppk-secret
IKEv2 Postquantum Preshared Key
(ASCII string or hexadecimal
encoded with a leading 0x).
password-3
Not
Specified
priority
Priority for routes added by IKE (1 -65535).
integer
Minimum
value: 1
Maximum
value: 65535
1
proposal
Phase1 proposal.
option
-Option
Description
des-md5
des-md5
des-sha1
des-sha1
des-sha256
des-sha256
des-sha384
des-sha384
des-sha512
des-sha512
3des-md5
3des-md5
3des-sha1
3des-sha1
3des-sha256
3des-sha256
3des-sha384
3des-sha384
3des-sha512
3des-sha512
FortiOS 8.0.0 CLI Reference
2403
Fortinet Inc.

<!-- 来源页 2404 -->
Parameter
Description
Type
Size
Default
Option
Description
aes128-md5
aes128-md5
aes128-sha1
aes128-sha1
aes128-sha256
aes128-sha256
aes128-sha384
aes128-sha384
aes128-sha512
aes128-sha512
aes128gcm-prfsha1
aes128gcm-prfsha1
aes128gcm-prfsha256
aes128gcm-prfsha256
aes128gcm-prfsha384
aes128gcm-prfsha384
aes128gcm-prfsha512
aes128gcm-prfsha512
aes192-md5
aes192-md5
aes192-sha1
aes192-sha1
aes192-sha256
aes192-sha256
aes192-sha384
aes192-sha384
aes192-sha512
aes192-sha512
aes256-md5
aes256-md5
aes256-sha1
aes256-sha1
aes256-sha256
aes256-sha256
aes256-sha384
aes256-sha384
aes256-sha512
aes256-sha512
aes256gcm-prfsha1
aes256gcm-prfsha1
aes256gcm-prfsha256
aes256gcm-prfsha256
aes256gcm-prfsha384
aes256gcm-prfsha384
aes256gcm-prfsha512
aes256gcm-prfsha512
chacha20poly1305-prfsha1
chacha20poly1305-prfsha1
chacha20poly1305-prfsha256
chacha20poly1305-prfsha256
chacha20poly1305-prfsha384
chacha20poly1305-prfsha384
chacha20poly1305-prfsha512
chacha20poly1305-prfsha512
aria128-md5
aria128-md5
aria128-sha1
aria128-sha1
FortiOS 8.0.0 CLI Reference
2404
Fortinet Inc.

<!-- 来源页 2405 -->
Parameter
Description
Type
Size
Default
Option
Description
aria128-sha256
aria128-sha256
aria128-sha384
aria128-sha384
aria128-sha512
aria128-sha512
aria192-md5
aria192-md5
aria192-sha1
aria192-sha1
aria192-sha256
aria192-sha256
aria192-sha384
aria192-sha384
aria192-sha512
aria192-sha512
aria256-md5
aria256-md5
aria256-sha1
aria256-sha1
aria256-sha256
aria256-sha256
aria256-sha384
aria256-sha384
aria256-sha512
aria256-sha512
seed-md5
seed-md5
seed-sha1
seed-sha1
seed-sha256
seed-sha256
seed-sha384
seed-sha384
seed-sha512
seed-sha512
sm4-sm3
sm4-sm3
psksecret
Pre-shared secret for PSK
authentication (ASCII string or
hexadecimal encoded with a leading
0x).
password-3
Not
Specified
psksecret-remote
Pre-shared secret for remote side
PSK authentication (ASCII string or
hexadecimal encoded with a leading
0x).
password-3
Not
Specified
qkd
Enable/disable use of Quantum Key
Distribution (QKD) server.
option
-disable
Option
Description
disable
Disable use of a Quantum Key Distribution (QKD) server.
FortiOS 8.0.0 CLI Reference
2405
Fortinet Inc.

<!-- 来源页 2406 -->
Parameter
Description
Type
Size
Default
Option
Description
allow
Allow, but do not require, use of a Quantum Key Distribution (QKD)
server.
require
Require use of a Quantum Key Distribution (QKD) server.
qkd-hybrid
Enable/disable use of Quantum Key
Distribution (QKD) hybrid keys.
option
-disable
Option
Description
disable
Disable use of Quantum Key Distribution (QKD) hybrid keys.
allow
Allow, but do not require, use of Quantum Key Distribution (QKD)
hybrid keys.
require
Require use of Quantum Key Distribution (QKD) hybrid keys.
qkd-profile
Quantum Key Distribution (QKD)
server profile.
string
Maximum
length: 35
reauth
Enable/disable re-authentication
upon IKE SA lifetime expiration.
option
-disable
Option
Description
disable
Disable IKE SA re-authentication.
enable
Enable IKE SA re-authentication.
rekey
Enable/disable phase1 rekey.
option
-enable
Option
Description
enable
Enable phase1 rekey.
disable
Disable phase1 rekey.
remote-gw
Remote VPN gateway.
ipv4-address
Not
Specified
0.0.0.0
remote-gw-country
IPv4 addresses associated to a
specific country.
string
Maximum
length: 2
remote-gw-end-ip
Last IPv4 address in the range.
ipv4-address-any
Not
Specified
0.0.0.0
remote-gw-match
Set type of IPv4 remote gateway
address matching.
option
-any
FortiOS 8.0.0 CLI Reference
2406
Fortinet Inc.

<!-- 来源页 2407 -->
Parameter
Description
Type
Size
Default
Option
Description
any
Match any IPv4 gateway address.
ipmask
Match IPv4 gateway address and mask.
iprange
Match IPv4 gateway address range.
geography
Match IPv4 gateway address from a specified country.
ztna
Match IPv4 gateway address against ZTNA posture tags.
remote-gw-start-ip
First IPv4 address in the range.
ipv4-address-any
Not
Specified
0.0.0.0
remote-gw-subnet
IPv4 address and subnet mask.
ipv4-classnet-any
Not
Specified
0.0.0.0 0.0.0.0
remote-gw-ztna-tags <name>
IPv4 ZTNA posture tags.
Address name.
string
Maximum
length: 79
remote-gw6-country
IPv6 addresses associated to a
specific country.
string
Maximum
length: 2
remote-gw6-end-ip
Last IPv6 address in the range.
ipv6-address
Not
Specified
::
remote-gw6-match
Set type of IPv6 remote gateway
address matching.
option
-any
Option
Description
any
Match any IPv6 gateway address.
ipprefix
Match IPv6 gateway address and prefix.
iprange
Match IPv6 gateway address range.
geography
Match IPv6 gateway address from a specified country.
remote-gw6-start-ip
First IPv6 address in the range.
ipv6-address
Not
Specified
::
remote-gw6-subnet
IPv6 address and prefix.
ipv6-network
Not
Specified
::/0
remotegw-ddns
Domain name of remote gateway.
For example, name.ddns.com.
string
Maximum
length: 63
rsa-signature-format
Digital Signature Authentication RSA
signature format.
option
-pkcs1
FortiOS 8.0.0 CLI Reference
2407
Fortinet Inc.

<!-- 来源页 2408 -->
Parameter
Description
Type
Size
Default
Option
Description
pkcs1
RSASSA PKCS#1 v1.5.
pss
RSASSA Probabilistic Signature Scheme (PSS).
rsa-signature-hash-override
Enable/disable IKEv2 RSA signature
hash algorithm override.
option
-disable
Option
Description
enable
Enable IKEv2 RSA signature hash algorithm override.
disable
Disable IKEv2 RSA signature hash algorithm override.
save-password
Enable/disable saving XAuth
username and password on VPN
clients.
option
-disable
Option
Description
disable
Disable saving XAuth username and password on VPN clients.
enable
Enable saving XAuth username and password on VPN clients.
send-cert-chain
Enable/disable sending certificate
chain.
option
-enable
Option
Description
enable
Enable sending certificate chain.
disable
Disable sending certificate chain.
shared-idle-timeout
Enable/disable IPsec tunnel shared
idle timeout.
option
-disable
Option
Description
enable
Enable IPsec tunnel shared idle timeout. The location-id attribute
must be configured on both spokes. Shared idle timeout is supported
only on IKEv2 since remote-location is availabe only for IKEv2.
disable
Disable IPsec tunnel shared idle timeout.
signature-hash-alg
Digital Signature Authentication
hash algorithms.
option
-identity **
Option
Description
sha1
SHA1.
FortiOS 8.0.0 CLI Reference
2408
Fortinet Inc.

<!-- 来源页 2409 -->
Parameter
Description
Type
Size
Default
Option
Description
sha2-256
SHA2-256.
sha2-384
SHA2-384.
sha2-512
SHA2-512.
identity
Identity.
split-include-service
Split-include services.
string
Maximum
length: 79
suite-b
Use Suite-B.
option
-disable
Option
Description
disable
Do not use UI suite.
suite-b-gcm-128
Use Suite-B-GCM-128.
suite-b-gcm-256
Use Suite-B-GCM-256.
transport
Set IKE transport protocol.
option
-udp **
Option
Description
udp
Use UDP transport for IKE.
auto
Use AUTO transport for IKE.
tcp
Use TCP transport for IKE.
type
Remote gateway type.
option
-static
Option
Description
static
Remote VPN gateway has fixed IP address.
dynamic
Remote VPN gateway has dynamic IP address.
ddns
Remote VPN gateway has dynamic IP address and is a dynamic DNS
client.
unity-support
Enable/disable support for Cisco
UNITY Configuration Method
extensions.
option
-enable
Option
Description
disable
Disable Cisco Unity Configuration Method Extensions.
enable
Enable Cisco Unity Configuration Method Extensions.
FortiOS 8.0.0 CLI Reference
2409
Fortinet Inc.

<!-- 来源页 2410 -->
Parameter
Description
Type
Size
Default
usrgrp
User group name for dialup peers.
string
Maximum
length: 35
wizard-type
GUI VPN Wizard Type.
option
-custom
Option
Description
custom
Custom VPN configuration.
dialup-forticlient
Dial Up - FortiClient Windows, Mac and Android.
dialup-ikev2
Dial Up - IKEv2.
dialup-l2tp
Dial Up - L2TP over IPSec.
static-fortigate
Site to Site - FortiGate.
dialup-fortigate
Dial Up - FortiGate.
static-cisco
Site to Site - Cisco.
dialup-cisco-fw
Dialup Up - Cisco Firewall.
simplified-static-fortigate
Site to Site - FortiGate (SD-WAN).
hub-fortigate-auto-discovery
Hub role in a Hub-and-Spoke auto-discovery VPN.
spoke-fortigate-auto-discovery
Spoke role in a Hub-and-Spoke auto-discovery VPN.
fabric-overlay-orchestrator
Fabric Overlay Orchestrator.
cloud-sdn-orchestration
Cloud SDN Orchestration.
dialup-ios
Dial Up - iPhone / iPad Native IPsec Client.
dialup-android
Dial Up - Android Native IPsec Client.
dialup-windows
Dial Up - Windows Native IPsec Client.
dialup-cisco
Dial Up - Cisco IPsec Client.
xauthtype
XAuth type.
option
-disable
Option
Description
disable
Disable.
FortiOS 8.0.0 CLI Reference
2410
Fortinet Inc.

<!-- 来源页 2411 -->
Parameter
Description
Type
Size
Default
Option
Description
client
Enable as client.
pap
Enable as server PAP.
chap
Enable as server CHAP.
auto
Enable as server auto.
* This parameter may not exist in some models.
** Values may differ between models.
config ipv4-exclude-range
Parameter
Description
Type
Size
Default
end-ip
End of IPv4 exclusive range.
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
Start of IPv4 exclusive range.
ipv4-address
Not Specified
0.0.0.0
config ipv6-exclude-range
Parameter
Description
Type
Size
Default
end-ip
End of IPv6 exclusive range.
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
start-ip
Start of IPv6 exclusive range.
ipv6-address
Not Specified
::
config vpn ipsec phase1-interface
Configure VPN remote gateway.
FortiOS 8.0.0 CLI Reference
2411
Fortinet Inc.

<!-- 来源页 2412 -->
config vpn ipsec phase1-interface
Description: Configure VPN remote gateway.
edit <name>
set acct-verify [enable|disable]
set add-gw-route [enable|disable]
set add-route [disable|enable]
set addke1 {option1}, {option2}, ...
set addke2 {option1}, {option2}, ...
set addke3 {option1}, {option2}, ...
set addke4 {option1}, {option2}, ...
set addke5 {option1}, {option2}, ...
set addke6 {option1}, {option2}, ...
set addke7 {option1}, {option2}, ...
set aggregate-member [enable|disable]
set aggregate-weight {integer}
set assign-ip [disable|enable]
set assign-ip-from [range|usrgrp|...]
set authmethod [psk|signature]
set authmethod-remote [psk|signature]
set authpasswd {password}
set authusr {string}
set authusrgrp {string}
set auto-discovery-crossover [allow|block]
set auto-discovery-dialup-placeholder [disable|enable]
set auto-discovery-forwarder [enable|disable]
set auto-discovery-offer-interval {integer}
set auto-discovery-psk [enable|disable]
set auto-discovery-receiver [enable|disable]
set auto-discovery-sender [enable|disable]
set auto-discovery-shortcuts [independent|dependent]
set auto-negotiate [enable|disable]
set auto-transport-threshold {integer}
set azure-ad-autoconnect [enable|disable]
set backup-gateway <address1>, <address2>, ...
set banner {var-string}
set cert-id-validation [enable|disable]
set cert-peer-username-strip [disable|enable]
set cert-peer-username-validation [none|othername|...]
set cert-trust-store [local|ems]
set certificate <name1>, <name2>, ...
set childless-ike [enable|disable]
set client-auto-negotiate [disable|enable]
set client-keep-alive [disable|enable]
set client-resume [enable|disable]
set client-resume-interval {integer}
set comments {var-string}
set default-gw {ipv4-address}
set default-gw-priority {integer}
set dev-id {string}
set dev-id-notification [disable|enable]
set dhcp-ra-giaddr {ipv4-address}
set dhcp6-ra-linkaddr {ipv6-address}
FortiOS 8.0.0 CLI Reference
2412
Fortinet Inc.

<!-- 来源页 2413 -->
set dhgrp {option1}, {option2}, ...
set digital-signature-auth [enable|disable]
set distance {integer}
set dns-mode [manual|auto]
set dns-suffix-search <dns-suffix1>, <dns-suffix2>, ...
set domain {string}
set dpd [disable|on-idle|...]
set dpd-retrycount {integer}
set dpd-retryinterval {user}
set eap [enable|disable]
set eap-cert-auth [enable|disable]
set eap-exclude-peergrp {string}
set eap-identity [use-id-payload|send-request]
set ems-sn-check [enable|disable]
set encap-local-gw4 {ipv4-address}
set encap-local-gw6 {ipv6-address}
set encap-remote-gw4 {ipv4-address}
set encap-remote-gw6 {ipv6-address}
set encapsulation [none|gre|...]
set encapsulation-address [ike|ipv4|...]
set enforce-unique-id [disable|keep-new|...]
set esn [require|allow|...]
set exchange-fgt-device-id [enable|disable]
set exchange-interface-ip [enable|disable]
set exchange-ip-addr4 {ipv4-address}
set exchange-ip-addr6 {ipv6-address}
set fec-base {integer}
set fec-codec [rs|xor]
set fec-egress [enable|disable]
set fec-health-check {string}
set fec-ingress [enable|disable]
set fec-mapping-profile {string}
set fec-receive-timeout {integer}
set fec-redundant {integer}
set fec-send-timeout {integer}
set fec-separate-redundant-tunnel [enable|disable]
set fgsp-sync [enable|disable]
set fortinet-esp [enable|disable]
set fragmentation [enable|disable]
set fragmentation-mtu {integer}
set group-authentication [enable|disable]
set group-authentication-secret {password-3}
set ha-sync-esp-seqno [enable|disable]
set idle-timeout [enable|disable]
set idle-timeoutinterval {integer}
set ike-version [1|2]
set inbound-dscp-copy [enable|disable]
set include-local-lan [disable|enable]
set interface {string}
set internal-domain-list <domain-name1>, <domain-name2>, ...
set ip-delay-interval {integer}
set ip-fragmentation [pre-encapsulation|post-encapsulation]
FortiOS 8.0.0 CLI Reference
2413
Fortinet Inc.

<!-- 来源页 2414 -->
set ip-version [4|6]
set ipv4-dns-server1 {ipv4-address}
set ipv4-dns-server2 {ipv4-address}
set ipv4-dns-server3 {ipv4-address}
set ipv4-end-ip {ipv4-address}
config ipv4-exclude-range
Description: Configuration Method IPv4 exclude ranges.
edit <id>
set end-ip {ipv4-address}
set start-ip {ipv4-address}
next
end
set ipv4-name {string}
set ipv4-netmask {ipv4-netmask}
set ipv4-split-exclude {string}
set ipv4-split-include {string}
set ipv4-start-ip {ipv4-address}
set ipv4-wins-server1 {ipv4-address}
set ipv4-wins-server2 {ipv4-address}
set ipv6-auto-linklocal [enable|disable]
set ipv6-dns-server1 {ipv6-address}
set ipv6-dns-server2 {ipv6-address}
set ipv6-dns-server3 {ipv6-address}
set ipv6-end-ip {ipv6-address}
config ipv6-exclude-range
Description: Configuration method IPv6 exclude ranges.
edit <id>
set end-ip {ipv6-address}
set start-ip {ipv6-address}
next
end
set ipv6-name {string}
set ipv6-prefix {integer}
set ipv6-split-exclude {string}
set ipv6-split-include {string}
set ipv6-start-ip {ipv6-address}
set keepalive {integer}
set keylife {integer}
set kms {string}
set link-cost {integer}
set local-gw {ipv4-address}
set local-gw6 {ipv6-address}
set localid {string}
set localid-type [auto|fqdn|...]
set loopback-asymroute [enable|disable]
set mesh-selector-type [disable|subnet|...]
set mode [aggressive|main]
set mode-cfg [disable|enable]
set mode-cfg-allow-client-selector [disable|enable]
set monitor <name1>, <name2>, ...
set monitor-hold-down-delay {integer}
set monitor-hold-down-time {user}
FortiOS 8.0.0 CLI Reference
2414
Fortinet Inc.

<!-- 来源页 2415 -->
set monitor-hold-down-type [immediate|delay|...]
set monitor-hold-down-weekday [everyday|sunday|...]
set monitor-min {integer}
set nattraversal [enable|disable|...]
set negotiate-timeout {integer}
set net-device [enable|disable]
set network-id {integer}
set network-overlay [disable|enable]
set npu-offload [enable|disable]
set packet-redistribution [enable|disable]
set passive-mode [enable|disable]
set peer {string}
set peer-egress-shaping [enable|disable]
set peer-egress-shaping-value {integer}
set peergrp {string}
set peerid {string}
set peertype [any|one|...]
set ppk [disable|allow|...]
set ppk-identity {string}
set ppk-secret {password-3}
set priority {integer}
set proposal {option1}, {option2}, ...
set psksecret {password-3}
set psksecret-remote {password-3}
set qkd [disable|allow|...]
set qkd-hybrid [disable|allow|...]
set qkd-profile {string}
set reauth [disable|enable]
set rekey [enable|disable]
set remote-gw {ipv4-address}
set remote-gw-country {string}
set remote-gw-end-ip {ipv4-address-any}
set remote-gw-match [any|ipmask|...]
set remote-gw-start-ip {ipv4-address-any}
set remote-gw-subnet {ipv4-classnet-any}
set remote-gw-ztna-tags <name1>, <name2>, ...
set remote-gw6 {ipv6-address}
set remote-gw6-country {string}
set remote-gw6-end-ip {ipv6-address}
set remote-gw6-match [any|ipprefix|...]
set remote-gw6-start-ip {ipv6-address}
set remote-gw6-subnet {ipv6-network}
set remotegw-ddns {string}
set rsa-signature-format [pkcs1|pss]
set rsa-signature-hash-override [enable|disable]
set save-password [disable|enable]
set send-cert-chain [enable|disable]
set shared-idle-timeout [enable|disable]
set signature-hash-alg {option1}, {option2}, ...
set split-include-service {string}
set suite-b [disable|suite-b-gcm-128|...]
set transport [udp|auto|...]
FortiOS 8.0.0 CLI Reference
2415
Fortinet Inc.

<!-- 来源页 2416 -->
set type [static|dynamic|...]
set unity-support [disable|enable]
set usrgrp {string}
set vni {integer}
set wizard-type [custom|dialup-forticlient|...]
set xauthtype [disable|client|...]
next
end
config vpn ipsec phase1-interface
Parameter
Description
Type
Size
Default
acct-verify
Enable/disable verification of
RADIUS accounting record.
option
-disable
Option
Description
enable
Enable verification of RADIUS accounting record.
disable
Disable verification of RADIUS accounting record.
add-gw-route
Enable/disable automatically add
a route to the remote gateway.
option
-disable
Option
Description
enable
Automatically add a route to the remote gateway.
disable
Do not automatically add a route to the remote gateway.
add-route
Enable/disable control addition of
a route to peer destination
selector.
option
-enable
Option
Description
disable
Do not add a route to destination of peer selector.
enable
Add route to destination of peer selector.
addke1
ADDKE1 group.
option
-Option
Description
none
NONE.
ml-kem-512
ML-KEM-512.
ml-kem-768
ML-KEM-768.
ml-kem-1024
ML-KEM-1024.
FortiOS 8.0.0 CLI Reference
2416
Fortinet Inc.

<!-- 来源页 2417 -->
Parameter
Description
Type
Size
Default
Option
Description
kyber512
KYBER512.
kyber768
KYBER768.
kyber1024
KYBER1024.
frodo-l1
FRODO L1.
frodo-l3
FRODO L3.
frodo-l5
FRODO L5.
bike-l1
BIKE L1.
bike-l3
BIKE L3.
bike-l5
BIKE L5.
hqc128
HQC128.
hqc192
HQC192.
hqc256
HQC256.
0
NONE.
35
ML-KEM-512.
36
ML-KEM-768.
37
ML-KEM-1024.
1080
KYBER512.
1081
KYBER768.
1082
KYBER1024.
1083
FRODO L1.
1084
FRODO L3.
1085
FRODO L5.
1089
BIKE L1.
1090
BIKE L3.
1091
BIKE L5.
1092
HQC128.
1093
HQC192.
1094
HQC256.
addke2
ADDKE2 group.
option
-FortiOS 8.0.0 CLI Reference
2417
Fortinet Inc.

<!-- 来源页 2418 -->
Parameter
Description
Type
Size
Default
Option
Description
none
NONE.
ml-kem-512
ML-KEM-512.
ml-kem-768
ML-KEM-768.
ml-kem-1024
ML-KEM-1024.
kyber512
KYBER512.
kyber768
KYBER768.
kyber1024
KYBER1024.
frodo-l1
FRODO L1.
frodo-l3
FRODO L3.
frodo-l5
FRODO L5.
bike-l1
BIKE L1.
bike-l3
BIKE L3.
bike-l5
BIKE L5.
hqc128
HQC128.
hqc192
HQC192.
hqc256
HQC256.
0
NONE.
35
ML-KEM-512.
36
ML-KEM-768.
37
ML-KEM-1024.
1080
KYBER512.
1081
KYBER768.
1082
KYBER1024.
1083
FRODO L1.
1084
FRODO L3.
1085
FRODO L5.
1089
BIKE L1.
1090
BIKE L3.
1091
BIKE L5.
FortiOS 8.0.0 CLI Reference
2418
Fortinet Inc.

<!-- 来源页 2419 -->
Parameter
Description
Type
Size
Default
Option
Description
1092
HQC128.
1093
HQC192.
1094
HQC256.
addke3
ADDKE3 group.
option
-Option
Description
none
NONE.
ml-kem-512
ML-KEM-512.
ml-kem-768
ML-KEM-768.
ml-kem-1024
ML-KEM-1024.
kyber512
KYBER512.
kyber768
KYBER768.
kyber1024
KYBER1024.
frodo-l1
FRODO L1.
frodo-l3
FRODO L3.
frodo-l5
FRODO L5.
bike-l1
BIKE L1.
bike-l3
BIKE L3.
bike-l5
BIKE L5.
hqc128
HQC128.
hqc192
HQC192.
hqc256
HQC256.
0
NONE.
35
ML-KEM-512.
36
ML-KEM-768.
37
ML-KEM-1024.
1080
KYBER512.
1081
KYBER768.
1082
KYBER1024.
FortiOS 8.0.0 CLI Reference
2419
Fortinet Inc.

<!-- 来源页 2420 -->
Parameter
Description
Type
Size
Default
Option
Description
1083
FRODO L1.
1084
FRODO L3.
1085
FRODO L5.
1089
BIKE L1.
1090
BIKE L3.
1091
BIKE L5.
1092
HQC128.
1093
HQC192.
1094
HQC256.
addke4
ADDKE4 group.
option
-Option
Description
none
NONE.
ml-kem-512
ML-KEM-512.
ml-kem-768
ML-KEM-768.
ml-kem-1024
ML-KEM-1024.
kyber512
KYBER512.
kyber768
KYBER768.
kyber1024
KYBER1024.
frodo-l1
FRODO L1.
frodo-l3
FRODO L3.
frodo-l5
FRODO L5.
bike-l1
BIKE L1.
bike-l3
BIKE L3.
bike-l5
BIKE L5.
hqc128
HQC128.
hqc192
HQC192.
hqc256
HQC256.
0
NONE.
FortiOS 8.0.0 CLI Reference
2420
Fortinet Inc.

<!-- 来源页 2421 -->
Parameter
Description
Type
Size
Default
Option
Description
35
ML-KEM-512.
36
ML-KEM-768.
37
ML-KEM-1024.
1080
KYBER512.
1081
KYBER768.
1082
KYBER1024.
1083
FRODO L1.
1084
FRODO L3.
1085
FRODO L5.
1089
BIKE L1.
1090
BIKE L3.
1091
BIKE L5.
1092
HQC128.
1093
HQC192.
1094
HQC256.
addke5
ADDKE5 group.
option
-Option
Description
none
NONE.
ml-kem-512
ML-KEM-512.
ml-kem-768
ML-KEM-768.
ml-kem-1024
ML-KEM-1024.
kyber512
KYBER512.
kyber768
KYBER768.
kyber1024
KYBER1024.
frodo-l1
FRODO L1.
frodo-l3
FRODO L3.
frodo-l5
FRODO L5.
bike-l1
BIKE L1.
FortiOS 8.0.0 CLI Reference
2421
Fortinet Inc.

<!-- 来源页 2422 -->
Parameter
Description
Type
Size
Default
Option
Description
bike-l3
BIKE L3.
bike-l5
BIKE L5.
hqc128
HQC128.
hqc192
HQC192.
hqc256
HQC256.
0
NONE.
35
ML-KEM-512.
36
ML-KEM-768.
37
ML-KEM-1024.
1080
KYBER512.
1081
KYBER768.
1082
KYBER1024.
1083
FRODO L1.
1084
FRODO L3.
1085
FRODO L5.
1089
BIKE L1.
1090
BIKE L3.
1091
BIKE L5.
1092
HQC128.
1093
HQC192.
1094
HQC256.
addke6
ADDKE6 group.
option
-Option
Description
none
NONE.
ml-kem-512
ML-KEM-512.
ml-kem-768
ML-KEM-768.
ml-kem-1024
ML-KEM-1024.
kyber512
KYBER512.
FortiOS 8.0.0 CLI Reference
2422
Fortinet Inc.

<!-- 来源页 2423 -->
Parameter
Description
Type
Size
Default
Option
Description
kyber768
KYBER768.
kyber1024
KYBER1024.
frodo-l1
FRODO L1.
frodo-l3
FRODO L3.
frodo-l5
FRODO L5.
bike-l1
BIKE L1.
bike-l3
BIKE L3.
bike-l5
BIKE L5.
hqc128
HQC128.
hqc192
HQC192.
hqc256
HQC256.
0
NONE.
35
ML-KEM-512.
36
ML-KEM-768.
37
ML-KEM-1024.
1080
KYBER512.
1081
KYBER768.
1082
KYBER1024.
1083
FRODO L1.
1084
FRODO L3.
1085
FRODO L5.
1089
BIKE L1.
1090
BIKE L3.
1091
BIKE L5.
1092
HQC128.
1093
HQC192.
1094
HQC256.
addke7
ADDKE7 group.
option
-FortiOS 8.0.0 CLI Reference
2423
Fortinet Inc.

<!-- 来源页 2424 -->
Parameter
Description
Type
Size
Default
Option
Description
none
NONE.
ml-kem-512
ML-KEM-512.
ml-kem-768
ML-KEM-768.
ml-kem-1024
ML-KEM-1024.
kyber512
KYBER512.
kyber768
KYBER768.
kyber1024
KYBER1024.
frodo-l1
FRODO L1.
frodo-l3
FRODO L3.
frodo-l5
FRODO L5.
bike-l1
BIKE L1.
bike-l3
BIKE L3.
bike-l5
BIKE L5.
hqc128
HQC128.
hqc192
HQC192.
hqc256
HQC256.
0
NONE.
35
ML-KEM-512.
36
ML-KEM-768.
37
ML-KEM-1024.
1080
KYBER512.
1081
KYBER768.
1082
KYBER1024.
1083
FRODO L1.
1084
FRODO L3.
1085
FRODO L5.
1089
BIKE L1.
1090
BIKE L3.
1091
BIKE L5.
FortiOS 8.0.0 CLI Reference
2424
Fortinet Inc.

<!-- 来源页 2425 -->
Parameter
Description
Type
Size
Default
Option
Description
1092
HQC128.
1093
HQC192.
1094
HQC256.
aggregate-member
Enable/disable use as an
aggregate member.
option
-disable
Option
Description
enable
Enable use as an aggregate member.
disable
Disable use as an aggregate member.
aggregate-weight
Link weight for aggregate.
integer
Minimum value:
1 Maximum
value: 100
1
assign-ip
Enable/disable assignment of IP
to IPsec interface via
configuration method.
option
-enable
Option
Description
disable
Do not assign an IP address to the IPsec interface.
enable
Assign an IP address to the IPsec interface.
assign-ip-from
Method by which the IP address
will be assigned.
option
-range
Option
Description
range
Assign IP address from locally defined range.
usrgrp
Assign IP address via user group.
dhcp
Assign IP address via DHCP.
name
Assign IP address from firewall address or group.
authmethod
Authentication method.
option
-psk
Option
Description
psk
PSK authentication method.
signature
Signature authentication method.
FortiOS 8.0.0 CLI Reference
2425
Fortinet Inc.

<!-- 来源页 2426 -->
Parameter
Description
Type
Size
Default
authmethod-remote
Authentication method (remote
side).
option
-Option
Description
psk
PSK authentication method.
signature
Signature authentication method.
authpasswd
XAuth password (max 35
characters).
password
Not Specified
authusr
XAuth user name.
string
Maximum
length: 64
authusrgrp
Authentication user group.
string
Maximum
length: 35
auto-discovery-crossover
Allow/block set-up of short-cut
tunnels between different
network IDs.
option
-allow
Option
Description
allow
Allow set-up of short-cut tunnels between different network IDs.
block
Block set-up of short-cut tunnels between different network IDs.
auto-discovery-dialup-placeholder
Control if this dynamic gateway is
used for shortcut connections
only.
option
-disable
Option
Description
disable
Disable placeholder restriction.
enable
Enable placeholder restriction to only accept shortcut connections
on this dial-up gateway.
auto-discovery-forwarder
Enable/disable forwarding auto-discovery short-cut messages.
option
-disable
Option
Description
enable
Enable forwarding auto-discovery short-cut messages.
disable
Disable forwarding auto-discovery short-cut messages.
auto-discovery-offer-interval
Interval between shortcut offer
messages in seconds (1 - 300,
default = 5).
integer
Minimum value:
1 Maximum
value: 300
5
FortiOS 8.0.0 CLI Reference
2426
Fortinet Inc.

<!-- 来源页 2427 -->
Parameter
Description
Type
Size
Default
auto-discovery-psk
Enable/disable use of pre-shared
secrets for authentication of
auto-discovery tunnels.
option
-disable
Option
Description
enable
Enable use of pre-shared-secret authentication for auto-discovery
tunnels.
disable
Disable use of authentication defined by 'authmethod' for auto-discovery tunnels.
auto-discovery-receiver
Enable/disable accepting auto-discovery short-cut messages.
option
-disable
Option
Description
enable
Enable receiving auto-discovery short-cut messages.
disable
Disable receiving auto-discovery short-cut messages.
auto-discovery-sender
Enable/disable sending auto-discovery short-cut messages.
option
-disable
Option
Description
enable
Enable sending auto-discovery short-cut messages.
disable
Disable sending auto-discovery short-cut messages.
auto-discovery-shortcuts
Control deletion of child short-cut
tunnels when the parent tunnel
goes down.
option
-independent
Option
Description
independent
Short-cut tunnels remain up if the parent tunnel goes down.
dependent
Short-cut tunnels are brought down if the parent tunnel goes down.
auto-negotiate
Enable/disable automatic
initiation of IKE SA negotiation.
option
-enable
Option
Description
enable
Enable automatic initiation of IKE SA negotiation.
disable
Disable automatic initiation of IKE SA negotiation.
auto-transport-threshold
Timeout in seconds before falling
back to next transport protocol.
integer
Minimum value:
1 Maximum
value: 300
15
FortiOS 8.0.0 CLI Reference
2427
Fortinet Inc.

<!-- 来源页 2428 -->
Parameter
Description
Type
Size
Default
azure-ad-autoconnect
Enable/disable Azure AD Auto-Connect for FortiClient.
option
-disable
Option
Description
enable
Enable Azure AD Auto-Connect for FortiClient.
disable
Disable Azure AD Auto-Connect for FortiClient.
backup-gateway
<address>
Instruct unity clients about the
backup gateway address(es).
Address of backup gateway.
string
Maximum
length: 79
banner
Message that unity client should
display after connecting.
var-string
Maximum
length: 1024
cert-id-validation
Enable/disable cross validation of
peer ID and the identity in the
peer's certificate as specified in
RFC 4945.
option
-enable
Option
Description
enable
Enable cross validation of peer ID and the identity in the peer's
certificate as specified in RFC 4945.
disable
Disable cross validation of peer ID and the identity in the peer's
certificate as specified in RFC 4945.
cert-peer-username-strip
Enable/disable domain stripping
on certificate identity.
option
-disable
Option
Description
disable
Disable domain stripping on certificate identity.
enable
Enable domain stripping on certificate identity.
cert-peer-username-validation
Enable/disable cross validation of
peer username and the identity in
the peer's certificate.
option
-none
Option
Description
none
Disable cross validation of peer username and the identity in the
peer's certificate.
othername
Validate principal name in SAN othername.
rfc822name
Validate RFC822 email address in SAN.
cn
Validate CN in subject.
FortiOS 8.0.0 CLI Reference
2428
Fortinet Inc.

<!-- 来源页 2429 -->
Parameter
Description
Type
Size
Default
cert-trust-store
CA certificate trust store.
option
-local
Option
Description
local
Use local CA certificate.
ems
Use EMS CA certificate.
certificate <name>
The names of up to 4 signed
personal certificates.
Certificate name.
string
Maximum
length: 79
childless-ike
Enable/disable childless IKEv2
initiation (RFC 6023).
option
-disable
Option
Description
enable
Enable childless IKEv2 initiation (RFC 6023).
disable
Disable childless IKEv2 initiation (RFC 6023).
client-auto-negotiate
Enable/disable allowing the VPN
client to bring up the tunnel when
there is no traffic.
option
-disable
Option
Description
disable
Disable allowing the VPN client to bring up the tunnel when there is
no traffic.
enable
Enable allowing the VPN client to bring up the tunnel when there is no
traffic.
client-keep-alive
Enable/disable allowing the VPN
client to keep the tunnel up when
there is no traffic.
option
-disable
Option
Description
disable
Disable allowing the VPN client to keep the tunnel up when there is
no traffic.
enable
Enable allowing the VPN client to keep the tunnel up when there is no
traffic.
FortiOS 8.0.0 CLI Reference
2429
Fortinet Inc.

<!-- 来源页 2430 -->
Parameter
Description
Type
Size
Default
client-resume
Enable/disable resumption of
offline FortiClient sessions. When
a FortiClient enabled laptop is
closed or enters sleep/hibernate
mode, enabling this feature
allows FortiClient to keep the
tunnel during this period, and
allows users to immediately
resume using the IPsec tunnel
when the device wakes up.
option
-disable
Option
Description
enable
Enable client session resumption.
disable
Disable client session resumption.
client-resume-interval
Maximum time in seconds during
which a VPN client may resume
using a tunnel after a client PC
has entered sleep mode or
temporarily lost its network
connection (120 - 172800, default
= 7200).
integer
Minimum value:
120 Maximum
value: 172800
7200
comments
Comment.
var-string
Maximum
length: 255
default-gw
IPv4 address of default route
gateway to use for traffic exiting
the interface.
ipv4-address
Not Specified
0.0.0.0
default-gw-priority
Priority for default gateway route.
A higher priority number signifies
a less preferred route.
integer
Minimum value:
0 Maximum
value:
4294967295
0
dev-id
Device ID carried by the device ID
notification.
string
Maximum
length: 63
dev-id-notification
Enable/disable device ID
notification.
option
-disable
Option
Description
disable
Disable device ID notification.
enable
Enable device ID notification.
FortiOS 8.0.0 CLI Reference
2430
Fortinet Inc.

<!-- 来源页 2431 -->
Parameter
Description
Type
Size
Default
dhcp-ra-giaddr
Relay agent gateway IP address
to use in the giaddr field of DHCP
requests.
ipv4-address
Not Specified
0.0.0.0
dhcp6-ra-linkaddr
Relay agent IPv6 link address to
use in DHCP6 requests.
ipv6-address
Not Specified
::
dhgrp
DH group.
option
-20
Option
Description
1
DH Group 1.
2
DH Group 2.
5
DH Group 5.
14
DH Group 14.
15
DH Group 15.
16
DH Group 16.
17
DH Group 17.
18
DH Group 18.
19
DH Group 19.
20
DH Group 20.
21
DH Group 21.
27
DH Group 27.
28
DH Group 28.
29
DH Group 29.
30
DH Group 30.
31
DH Group 31.
32
DH Group 32.
digital-signature-auth
Enable/disable IKEv2 Digital
Signature Authentication (RFC
7427).
option
-disable
Option
Description
enable
Enable IKEv2 Digital Signature Authentication (RFC 7427).
disable
Disable IKEv2 Digital Signature Authentication (RFC 7427).
FortiOS 8.0.0 CLI Reference
2431
Fortinet Inc.

<!-- 来源页 2432 -->
Parameter
Description
Type
Size
Default
distance
Distance for routes added by IKE
(1 - 255).
integer
Minimum value:
1 Maximum
value: 255
15
dns-mode
DNS server mode.
option
-manual
Option
Description
manual
Manually configure DNS servers.
auto
Use default DNS servers.
dns-suffix-search <dns-suffix>
One or more DNS domain name
suffixes in quotes separated by
spaces.
DNS suffix.
string
Maximum
length: 79
domain
Instruct unity clients about the
single default DNS domain.
string
Maximum
length: 63
dpd
Dead Peer Detection mode.
option
-on-demand
Option
Description
disable
Disable Dead Peer Detection.
on-idle
Trigger Dead Peer Detection when IPsec is idle.
on-demand
Trigger Dead Peer Detection when IPsec traffic is sent but no reply is
received from the peer.
dpd-retrycount
Number of DPD retry attempts.
integer
Minimum value:
1 Maximum
value: 10
3
dpd-retryinterval
DPD retry interval.
user
Not Specified
eap
Enable/disable IKEv2 EAP
authentication.
option
-disable
Option
Description
enable
Enable IKEv2 EAP authentication.
disable
Disable IKEv2 EAP authentication.
eap-cert-auth
Enable/disable peer certificate
authentication in addition to EAP
if peer is a FortiClient endpoint.
option
-disable
FortiOS 8.0.0 CLI Reference
2432
Fortinet Inc.

<!-- 来源页 2433 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable peer certificate authentication in addition to EAP if peer is a
FortiClient endpoint.
disable
Disable peer certificate authentication in addition to EAP if peer is a
FortiClient endpoint.
eap-exclude-peergrp
Peer group excluded from EAP
authentication.
string
Maximum
length: 35
eap-identity
IKEv2 EAP peer identity type.
option
-use-id-payload
Option
Description
use-id-payload
Use IKEv2 IDi payload to resolve peer identity.
send-request
Use EAP identity request to resolve peer identity.
ems-sn-check
Enable/disable verification of
EMS serial number.
option
-disable
Option
Description
enable
Enable EMS serial number verification.
disable
Disable EMS serial number verification.
encap-local-gw4
Local IPv4 address of GRE tunnel.
ipv4-address
Not Specified
0.0.0.0
encap-local-gw6
Local IPv6 address of GRE tunnel.
ipv6-address
Not Specified
::
encap-remote-gw4
Remote IPv4 address of GRE
tunnel.
ipv4-address
Not Specified
0.0.0.0
encap-remote-gw6
Remote IPv6 address of GRE
tunnel.
ipv6-address
Not Specified
::
encapsulation
Enable/disable GRE/VPNID
encapsulation.
option
-none
Option
Description
none
No additional encapsulation.
gre
GRE encapsulation.
vpn-id-ipip
VPN ID with IPIP encapsulation.
vxlan
VXLAN encapsulation.
FortiOS 8.0.0 CLI Reference
2433
Fortinet Inc.

<!-- 来源页 2434 -->
Parameter
Description
Type
Size
Default
encapsulation-address
Source for GRE tunnel address.
option
-ike
Option
Description
ike
Use IKE/IPsec gateway addresses.
ipv4
Specify separate GRE tunnel address.
ipv6
Specify separate GRE tunnel address.
enforce-unique-id
Enable/disable peer ID
uniqueness check.
option
-disable
Option
Description
disable
Disable peer ID uniqueness enforcement.
keep-new
Enforce peer ID uniqueness, keep new connection if collision found.
keep-old
Enforce peer ID uniqueness, keep old connection if collision found.
esn *
Extended sequence number
(ESN) negotiation.
option
-disable
Option
Description
require
Require extended sequence number.
allow
Allow extended sequence number.
disable
Disable extended sequence number.
exchange-fgt-device-id
Enable/disable device identifier
exchange with peer FortiGate
units for use of VPN monitor data
by FortiManager.
option
-disable
Option
Description
enable
Enable exchange of FortiGate device identifier.
disable
Disable exchange of FortiGate device identifier.
exchange-interface-ip
Enable/disable exchange of IPsec
interface IP address.
option
-disable
Option
Description
enable
Enable exchange of IPsec interface IP address.
disable
Disable exchange of IPsec interface IP address.
FortiOS 8.0.0 CLI Reference
2434
Fortinet Inc.

<!-- 来源页 2435 -->
Parameter
Description
Type
Size
Default
exchange-ip-addr4
IPv4 address to exchange with
peers.
ipv4-address
Not Specified
0.0.0.0
exchange-ip-addr6
IPv6 address to exchange with
peers.
ipv6-address
Not Specified
::
fec-base
Number of base Forward Error
Correction packets (1 - 40).
integer
Minimum value:
1 Maximum
value: 40 **
10
fec-codec
Forward Error Correction
encoding/decoding algorithm.
option
-rs
Option
Description
rs
Reed-Solomon FEC algorithm.
xor
XOR FEC algorithm.
fec-egress
Enable/disable Forward Error
Correction for egress IPsec
traffic.
option
-disable
Option
Description
enable
Enable Forward Error Correction for egress IPsec traffic.
disable
Disable Forward Error Correction for egress IPsec traffic.
fec-health-check
SD-WAN health check.
string
Maximum
length: 35
fec-ingress
Enable/disable Forward Error
Correction for ingress IPsec
traffic.
option
-disable
Option
Description
enable
Enable Forward Error Correction for ingress IPsec traffic.
disable
Disable Forward Error Correction for ingress IPsec traffic.
fec-mapping-profile
Forward Error Correction (FEC)
mapping profile.
string
Maximum
length: 35
fec-receive-timeout
Timeout in milliseconds before
dropping Forward Error
Correction packets (1 - 1000).
integer
Minimum value:
1 Maximum
value: 1000
50
fec-redundant
Number of redundant Forward
Error Correction packets (1 - 20
for reed-solomon, 1 for xor).
integer
Minimum value:
1 Maximum
value: 20 **
1
FortiOS 8.0.0 CLI Reference
2435
Fortinet Inc.

<!-- 来源页 2436 -->
Parameter
Description
Type
Size
Default
fec-send-timeout
Timeout in milliseconds before
sending Forward Error Correction
packets (1 - 1000).
integer
Minimum value:
1 Maximum
value: 1000
5
fec-separate-redundant-tunnel
*
Enable/disable Forward Error
Correction redundancy on
separate tunnel.
option
-disable
Option
Description
enable
Enable Forward Error Correction redundancy on separate tunnel.
disable
Disable Forward Error Correction redundancy on separate tunnel.
fgsp-sync
Enable/disable IPsec syncing of
tunnels for FGSP IPsec.
option
-disable
Option
Description
enable
Enable IPsec syncing of tunnels to other cluster members.
disable
Disable IPsec syncing of tunnels to other cluster members.
fortinet-esp
Enable/disable Fortinet ESP
encapsulation.
option
-disable
Option
Description
enable
Enable Fortinet ESP encapsulation.
disable
Disable Fortinet ESP encapsulation.
fragmentation
Enable/disable fragment IKE
message on re-transmission.
option
-enable
Option
Description
enable
Enable intra-IKE fragmentation support on re-transmission.
disable
Disable intra-IKE fragmentation support.
fragmentation-mtu
IKE fragmentation MTU (500 -16000).
integer
Minimum value:
500 Maximum
value: 16000
1200
group-authentication
Enable/disable IKEv2 IDi group
authentication.
option
-disable
Option
Description
enable
Enable IKEv2 IDi group authentication.
disable
Disable IKEv2 IDi group authentication.
FortiOS 8.0.0 CLI Reference
2436
Fortinet Inc.

<!-- 来源页 2437 -->
Parameter
Description
Type
Size
Default
group-authentication-secret
Password for IKEv2 ID group
authentication. ASCII string or
hexadecimal indicated by a
leading 0x.
password-3
Not Specified
ha-sync-esp-seqno
Enable/disable sequence number
jump ahead for IPsec HA.
option
-enable
Option
Description
enable
Enable HA syncing of ESP sequence numbers.
disable
Disable HA syncing of ESP sequence numbers.
idle-timeout
Enable/disable IPsec tunnel idle
timeout.
option
-disable
Option
Description
enable
Enable IPsec tunnel idle timeout.
disable
Disable IPsec tunnel idle timeout.
idle-timeoutinterval
IPsec tunnel idle timeout in
minutes (5 - 43200).
integer
Minimum value:
5 Maximum
value: 43200
15
ike-version
IKE protocol version.
option
-2 **
Option
Description
1
Use IKEv1 protocol.
2
Use IKEv2 protocol.
inbound-dscp-copy
Enable/disable copy the dscp in
the ESP header to the inner IP
Header.
option
-disable
Option
Description
enable
Enable copy the dscp in the ESP header to the inner IP Header.
disable
Disable copy the dscp in the ESP header to the inner IP Header.
include-local-lan
Enable/disable allow local LAN
access on unity clients.
option
-disable
Option
Description
disable
Disable local LAN access on Unity clients.
enable
Enable local LAN access on Unity clients.
FortiOS 8.0.0 CLI Reference
2437
Fortinet Inc.

<!-- 来源页 2438 -->
Parameter
Description
Type
Size
Default
interface
Local physical, aggregate,
loopback, or VLAN outgoing
interface.
string
Maximum
length: 35
internal-domain-list <domain-name>
One or more internal domain
names in quotes separated by
spaces.
Domain name.
string
Maximum
length: 79
ip-delay-interval
IP address reuse delay interval in
seconds (0 - 28800).
integer
Minimum value:
0 Maximum
value: 28800
0
ip-fragmentation
Determine whether IP packets are
fragmented before or after IPsec
encapsulation.
option
-post-encapsulation
Option
Description
pre-encapsulation
Fragment before IPsec encapsulation.
post-encapsulation
Fragment after IPsec encapsulation (RFC compliant).
ip-version
IP version to use for VPN
interface.
option
-4
Option
Description
4
Use IPv4 addressing for gateways.
6
Use IPv6 addressing for gateways.
ipv4-dns-server1
IPv4 DNS server 1.
ipv4-address
Not Specified
0.0.0.0
ipv4-dns-server2
IPv4 DNS server 2.
ipv4-address
Not Specified
0.0.0.0
ipv4-dns-server3
IPv4 DNS server 3.
ipv4-address
Not Specified
0.0.0.0
ipv4-end-ip
End of IPv4 range.
ipv4-address
Not Specified
0.0.0.0
ipv4-name
IPv4 address name.
string
Maximum
length: 79
ipv4-netmask
IPv4 Netmask.
ipv4-netmask
Not Specified
255.255.255.255
FortiOS 8.0.0 CLI Reference
2438
Fortinet Inc.

<!-- 来源页 2439 -->
Parameter
Description
Type
Size
Default
ipv4-split-exclude
IPv4 subnets that should not be
sent over the IPsec tunnel.
string
Maximum
length: 79
ipv4-split-include
IPv4 split-include subnets.
string
Maximum
length: 79
ipv4-start-ip
Start of IPv4 range.
ipv4-address
Not Specified
0.0.0.0
ipv4-wins-server1
WINS server 1.
ipv4-address
Not Specified
0.0.0.0
ipv4-wins-server2
WINS server 2.
ipv4-address
Not Specified
0.0.0.0
ipv6-auto-linklocal
Enable/disable auto generation of
IPv6 link-local address using last
8 bytes of mode-cfg assigned
IPv6 address.
option
-disable
Option
Description
enable
Enable mode-cfg auto configuration of IPv6 link-local address.
disable
Disable mode-cfg auto configuration of IPv6 link-local address.
ipv6-dns-server1
IPv6 DNS server 1.
ipv6-address
Not Specified
::
ipv6-dns-server2
IPv6 DNS server 2.
ipv6-address
Not Specified
::
ipv6-dns-server3
IPv6 DNS server 3.
ipv6-address
Not Specified
::
ipv6-end-ip
End of IPv6 range.
ipv6-address
Not Specified
::
ipv6-name
IPv6 address name.
string
Maximum
length: 79
ipv6-prefix
IPv6 prefix.
integer
Minimum value:
1 Maximum
value: 128
128
ipv6-split-exclude
IPv6 subnets that should not be
sent over the IPsec tunnel.
string
Maximum
length: 79
ipv6-split-include
IPv6 split-include subnets.
string
Maximum
length: 79
ipv6-start-ip
Start of IPv6 range.
ipv6-address
Not Specified
::
FortiOS 8.0.0 CLI Reference
2439
Fortinet Inc.

<!-- 来源页 2440 -->
Parameter
Description
Type
Size
Default
keepalive
NAT-T keep alive interval.
integer
Minimum value:
5 Maximum
value: 900
10
keylife
Time to wait in seconds before
phase 1 encryption key expires.
integer
Minimum value:
120 Maximum
value: 172800
86400
kms
Key Management Services
server.
string
Maximum
length: 35
link-cost
VPN tunnel underlay link cost.
integer
Minimum value:
0 Maximum
value: 255
0
local-gw
IPv4 address of the local
gateway's external interface.
ipv4-address
Not Specified
0.0.0.0
local-gw6
IPv6 address of the local
gateway's external interface.
ipv6-address
Not Specified
::
localid
Local ID.
string
Maximum
length: 63
localid-type
Local ID type.
option
-auto
Option
Description
auto
Select ID type automatically.
fqdn
Use fully qualified domain name.
user-fqdn
Use user fully qualified domain name.
keyid
Use key-id string.
address
Use local IP address.
asn1dn
Use ASN.1 distinguished name.
loopback-asymroute
Enable/disable asymmetric
routing for IKE traffic on loopback
interface.
option
-enable
Option
Description
enable
Allow ingress/egress IKE traffic to be routed over different
interfaces.
disable
Ingress/egress IKE traffic must be routed over the same interface.
mesh-selector-type
Add selectors containing subsets
of the configuration depending on
traffic.
option
-disable
FortiOS 8.0.0 CLI Reference
2440
Fortinet Inc.

<!-- 来源页 2441 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable.
subnet
Enable addition of matching subnet selector.
host
Enable addition of host to host selector.
mode
The ID protection mode used to
establish a secure channel.
option
-main
Option
Description
aggressive
Aggressive mode.
main
Main mode.
mode-cfg
Enable/disable configuration
method.
option
-disable
Option
Description
disable
Disable Configuration Method.
enable
Enable Configuration Method.
mode-cfg-allow-client-selector
Enable/disable mode-cfg client to
use custom phase2 selectors.
option
-disable
Option
Description
disable
Mode-cfg client to use wildcard selectors.
enable
Mode-cfg client to use custom selectors.
monitor <name>
IPsec interface as backup for
primary interface.
IPsec interface as backup for
primary interface.
string
Maximum
length: 79
monitor-hold-down-delay
Time to wait in seconds before
recovery once primary re-establishes.
integer
Minimum value:
0 Maximum
value:
31536000
0
monitor-hold-down-time
Time of day at which to fail back
to primary after it re-establishes.
user
Not Specified
monitor-hold-down-type
Recovery time method when
primary interface re-establishes.
option
-immediate
FortiOS 8.0.0 CLI Reference
2441
Fortinet Inc.

<!-- 来源页 2442 -->
Parameter
Description
Type
Size
Default
Option
Description
immediate
Fail back immediately after primary recovers.
delay
Number of seconds to delay fail back after primary recovers.
time
Specify a time at which to fail back after primary recovers.
monitor-hold-down-weekday
Day of the week to recover once
primary re-establishes.
option
-sunday
Option
Description
everyday
Every Day.
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
monitor-min
Minimum number of links to
become degraded before
activating this interface. Zero (0)
means all links must be down
before activating this interface.
integer
Minimum value:
0 Maximum
value:
4294967295
0
name
IPsec remote gateway name.
string
Maximum
length: 15
nattraversal
Enable/disable NAT traversal.
option
-enable
Option
Description
enable
Enable IPsec NAT traversal.
disable
Disable IPsec NAT traversal.
forced
Force IPsec NAT traversal on.
negotiate-timeout
IKE SA negotiation timeout in
seconds (1 - 300).
integer
Minimum value:
1 Maximum
value: 300
30
net-device
Enable/disable kernel device
creation.
option
-disable
FortiOS 8.0.0 CLI Reference
2442
Fortinet Inc.

<!-- 来源页 2443 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Create a kernel device for every tunnel.
disable
Do not create a kernel device for tunnels.
network-id
VPN gateway network ID.
integer
Minimum value:
0 Maximum
value: 255
0
network-overlay
Enable/disable network overlays.
option
-disable
Option
Description
disable
Disable network overlays.
enable
Enable network overlays.
npu-offload *
Enable/disable offloading NPU.
option
-enable
Option
Description
enable
Enable NPU offloading.
disable
Disable NPU offloading.
packet-redistribution *
Enable/disable packet
distribution (RPS) on the IPsec
interface.
option
-disable
Option
Description
enable
Enable packet redistribution.
disable
Disable packet redistribution.
passive-mode
Enable/disable IPsec passive
mode for static tunnels.
option
-disable
Option
Description
enable
Enable IPsec passive mode.
disable
Disable IPsec passive mode.
peer
Accept this peer certificate.
string
Maximum
length: 35
peer-egress-shaping
Enable/disable peer egress
shaping.
option
-disable
FortiOS 8.0.0 CLI Reference
2443
Fortinet Inc.

<!-- 来源页 2444 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable peer egress shaping.
disable
Disable peer egress shaping.
peer-egress-shaping-value
Configure outbound bandwidth to
use for peer egress shaping in
kbps (0 - 80000000, default = 0).
integer
Minimum value:
0 Maximum
value:
80000000 **
0
peergrp
Accept this peer certificate
group.
string
Maximum
length: 35
peerid
Accept this peer identity.
string
Maximum
length: 255
peertype
Accept this peer type.
option
-peer
Option
Description
any
Accept any peer ID.
one
Accept this peer ID.
dialup
Accept peer ID in dialup group.
peer
Accept this peer certificate.
peergrp
Accept this peer certificate group.
ppk
Enable/disable IKEv2
Postquantum Preshared Key
(PPK).
option
-disable
Option
Description
disable
Disable use of IKEv2 Postquantum Preshared Key (PPK).
allow
Allow, but do not require, use of IKEv2 Postquantum Preshared Key
(PPK).
require
Require use of IKEv2 Postquantum Preshared Key (PPK).
ppk-identity
IKEv2 Postquantum Preshared
Key Identity.
string
Maximum
length: 35
ppk-secret
IKEv2 Postquantum Preshared
Key (ASCII string or hexadecimal
encoded with a leading 0x).
password-3
Not Specified
FortiOS 8.0.0 CLI Reference
2444
Fortinet Inc.

<!-- 来源页 2445 -->
Parameter
Description
Type
Size
Default
priority
Priority for routes added by IKE (1
- 65535).
integer
Minimum value:
1 Maximum
value: 65535
1
proposal
Phase1 proposal.
option
-Option
Description
des-md5
des-md5
des-sha1
des-sha1
des-sha256
des-sha256
des-sha384
des-sha384
des-sha512
des-sha512
3des-md5
3des-md5
3des-sha1
3des-sha1
3des-sha256
3des-sha256
3des-sha384
3des-sha384
3des-sha512
3des-sha512
aes128-md5
aes128-md5
aes128-sha1
aes128-sha1
aes128-sha256
aes128-sha256
aes128-sha384
aes128-sha384
aes128-sha512
aes128-sha512
aes128gcm-prfsha1
aes128gcm-prfsha1
aes128gcm-prfsha256
aes128gcm-prfsha256
aes128gcm-prfsha384
aes128gcm-prfsha384
aes128gcm-prfsha512
aes128gcm-prfsha512
aes192-md5
aes192-md5
aes192-sha1
aes192-sha1
aes192-sha256
aes192-sha256
aes192-sha384
aes192-sha384
aes192-sha512
aes192-sha512
aes256-md5
aes256-md5
FortiOS 8.0.0 CLI Reference
2445
Fortinet Inc.

<!-- 来源页 2446 -->
Parameter
Description
Type
Size
Default
Option
Description
aes256-sha1
aes256-sha1
aes256-sha256
aes256-sha256
aes256-sha384
aes256-sha384
aes256-sha512
aes256-sha512
aes256gcm-prfsha1
aes256gcm-prfsha1
aes256gcm-prfsha256
aes256gcm-prfsha256
aes256gcm-prfsha384
aes256gcm-prfsha384
aes256gcm-prfsha512
aes256gcm-prfsha512
chacha20poly1305-prfsha1
chacha20poly1305-prfsha1
chacha20poly1305-prfsha256
chacha20poly1305-prfsha256
chacha20poly1305-prfsha384
chacha20poly1305-prfsha384
chacha20poly1305-prfsha512
chacha20poly1305-prfsha512
aria128-md5
aria128-md5
aria128-sha1
aria128-sha1
aria128-sha256
aria128-sha256
aria128-sha384
aria128-sha384
aria128-sha512
aria128-sha512
aria192-md5
aria192-md5
aria192-sha1
aria192-sha1
aria192-sha256
aria192-sha256
aria192-sha384
aria192-sha384
aria192-sha512
aria192-sha512
aria256-md5
aria256-md5
aria256-sha1
aria256-sha1
aria256-sha256
aria256-sha256
aria256-sha384
aria256-sha384
aria256-sha512
aria256-sha512
seed-md5
seed-md5
seed-sha1
seed-sha1
FortiOS 8.0.0 CLI Reference
2446
Fortinet Inc.

<!-- 来源页 2447 -->
Parameter
Description
Type
Size
Default
Option
Description
seed-sha256
seed-sha256
seed-sha384
seed-sha384
seed-sha512
seed-sha512
sm4-sm3
sm4-sm3
psksecret
Pre-shared secret for PSK
authentication (ASCII string or
hexadecimal encoded with a
leading 0x).
password-3
Not Specified
psksecret-remote
Pre-shared secret for remote side
PSK authentication (ASCII string
or hexadecimal encoded with a
leading 0x).
password-3
Not Specified
qkd
Enable/disable use of Quantum
Key Distribution (QKD) server.
option
-disable
Option
Description
disable
Disable use of a Quantum Key Distribution (QKD) server.
allow
Allow, but do not require, use of a Quantum Key Distribution (QKD)
server.
require
Require use of a Quantum Key Distribution (QKD) server.
qkd-hybrid
Enable/disable use of Quantum
Key Distribution (QKD) hybrid
keys.
option
-disable
Option
Description
disable
Disable use of Quantum Key Distribution (QKD) hybrid keys.
allow
Allow, but do not require, use of Quantum Key Distribution (QKD)
hybrid keys.
require
Require use of Quantum Key Distribution (QKD) hybrid keys.
qkd-profile
Quantum Key Distribution (QKD)
server profile.
string
Maximum
length: 35
reauth
Enable/disable re-authentication
upon IKE SA lifetime expiration.
option
-disable
FortiOS 8.0.0 CLI Reference
2447
Fortinet Inc.

<!-- 来源页 2448 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable IKE SA re-authentication.
enable
Enable IKE SA re-authentication.
rekey
Enable/disable phase1 rekey.
option
-enable
Option
Description
enable
Enable phase1 rekey.
disable
Disable phase1 rekey.
remote-gw
IPv4 address of the remote
gateway's external interface.
ipv4-address
Not Specified
0.0.0.0
remote-gw-country
IPv4 addresses associated to a
specific country.
string
Maximum
length: 2
remote-gw-end-ip
Last IPv4 address in the range.
ipv4-address-any
Not Specified
0.0.0.0
remote-gw-match
Set type of IPv4 remote gateway
address matching.
option
-any
Option
Description
any
Match any IPv4 gateway address.
ipmask
Match IPv4 gateway address and mask.
iprange
Match IPv4 gateway address range.
geography
Match IPv4 gateway address from a specified country.
ztna
Match IPv4 gateway address against ZTNA posture tags.
remote-gw-start-ip
First IPv4 address in the range.
ipv4-address-any
Not Specified
0.0.0.0
remote-gw-subnet
IPv4 address and subnet mask.
ipv4-classnet-any
Not Specified
0.0.0.0 0.0.0.0
remote-gw-ztna-tags <name>
IPv4 ZTNA posture tags.
Address name.
string
Maximum
length: 79
remote-gw6
IPv6 address of the remote
gateway's external interface.
ipv6-address
Not Specified
::
remote-gw6-country
IPv6 addresses associated to a
specific country.
string
Maximum
length: 2
FortiOS 8.0.0 CLI Reference
2448
Fortinet Inc.

<!-- 来源页 2449 -->
Parameter
Description
Type
Size
Default
remote-gw6-end-ip
Last IPv6 address in the range.
ipv6-address
Not Specified
::
remote-gw6-match
Set type of IPv6 remote gateway
address matching.
option
-any
Option
Description
any
Match any IPv6 gateway address.
ipprefix
Match IPv6 gateway address and prefix.
iprange
Match IPv6 gateway address range.
geography
Match IPv6 gateway address from a specified country.
remote-gw6-start-ip
First IPv6 address in the range.
ipv6-address
Not Specified
::
remote-gw6-subnet
IPv6 address and prefix.
ipv6-network
Not Specified
::/0
remotegw-ddns
Domain name of remote gateway.
For example, name.ddns.com.
string
Maximum
length: 63
rsa-signature-format
Digital Signature Authentication
RSA signature format.
option
-pkcs1
Option
Description
pkcs1
RSASSA PKCS#1 v1.5.
pss
RSASSA Probabilistic Signature Scheme (PSS).
rsa-signature-hash-override
Enable/disable IKEv2 RSA
signature hash algorithm
override.
option
-disable
Option
Description
enable
Enable IKEv2 RSA signature hash algorithm override.
disable
Disable IKEv2 RSA signature hash algorithm override.
save-password
Enable/disable saving XAuth
username and password on VPN
clients.
option
-disable
Option
Description
disable
Disable saving XAuth username and password on VPN clients.
enable
Enable saving XAuth username and password on VPN clients.
FortiOS 8.0.0 CLI Reference
2449
Fortinet Inc.

<!-- 来源页 2450 -->
Parameter
Description
Type
Size
Default
send-cert-chain
Enable/disable sending
certificate chain.
option
-enable
Option
Description
enable
Enable sending certificate chain.
disable
Disable sending certificate chain.
shared-idle-timeout
Enable/disable IPsec tunnel
shared idle timeout.
option
-disable
Option
Description
enable
Enable IPsec tunnel shared idle timeout. The location-id attribute
must be configured on both spokes. Shared idle timeout is supported
only on IKEv2 since remote-location is availabe only for IKEv2.
disable
Disable IPsec tunnel shared idle timeout.
signature-hash-alg
Digital Signature Authentication
hash algorithms.
option
-identity **
Option
Description
sha1
SHA1.
sha2-256
SHA2-256.
sha2-384
SHA2-384.
sha2-512
SHA2-512.
identity
Identity.
split-include-service
Split-include services.
string
Maximum
length: 79
suite-b
Use Suite-B.
option
-disable
Option
Description
disable
Do not use UI suite.
suite-b-gcm-128
Use Suite-B-GCM-128.
suite-b-gcm-256
Use Suite-B-GCM-256.
transport
Set IKE transport protocol.
option
-udp **
FortiOS 8.0.0 CLI Reference
2450
Fortinet Inc.

<!-- 来源页 2451 -->
Parameter
Description
Type
Size
Default
Option
Description
udp
Use UDP transport for IKE.
auto
Use AUTO transport for IKE.
tcp
Use TCP transport for IKE.
type
Remote gateway type.
option
-static
Option
Description
static
Remote VPN gateway has fixed IP address.
dynamic
Remote VPN gateway has dynamic IP address.
ddns
Remote VPN gateway has dynamic IP address and is a dynamic DNS
client.
unity-support
Enable/disable support for Cisco
UNITY Configuration Method
extensions.
option
-enable
Option
Description
disable
Disable Cisco Unity Configuration Method Extensions.
enable
Enable Cisco Unity Configuration Method Extensions.
usrgrp
User group name for dialup peers.
string
Maximum
length: 35
vni *
VNI of VXLAN tunnel.
integer
Minimum value:
1 Maximum
value:
16777215
0
wizard-type
GUI VPN Wizard Type.
option
-custom
Option
Description
custom
Custom VPN configuration.
dialup-forticlient
Dial Up - FortiClient Windows, Mac and Android.
dialup-ikev2
Dial Up - IKEv2.
dialup-l2tp
Dial Up - L2TP over IPSec.
static-fortigate
Site to Site - FortiGate.
dialup-fortigate
Dial Up - FortiGate.
FortiOS 8.0.0 CLI Reference
2451
Fortinet Inc.

<!-- 来源页 2452 -->
Parameter
Description
Type
Size
Default
Option
Description
static-cisco
Site to Site - Cisco.
dialup-cisco-fw
Dialup Up - Cisco Firewall.
simplified-static-fortigate
Site to Site - FortiGate (SD-WAN).
hub-fortigate-auto-discovery
Hub role in a Hub-and-Spoke auto-discovery VPN.
spoke-fortigate-auto-discovery
Spoke role in a Hub-and-Spoke auto-discovery VPN.
fabric-overlay-orchestrator
Fabric Overlay Orchestrator.
cloud-sdn-orchestration
Cloud SDN Orchestration.
dialup-ios
Dial Up - iPhone / iPad Native IPsec Client.
dialup-android
Dial Up - Android Native IPsec Client.
dialup-windows
Dial Up - Windows Native IPsec Client.
dialup-cisco
Dial Up - Cisco IPsec Client.
xauthtype
XAuth type.
option
-disable
Option
Description
disable
Disable.
client
Enable as client.
pap
Enable as server PAP.
chap
Enable as server CHAP.
auto
Enable as server auto.
* This parameter may not exist in some models.
** Values may differ between models.
FortiOS 8.0.0 CLI Reference
2452
Fortinet Inc.

<!-- 来源页 2453 -->
config ipv4-exclude-range
Parameter
Description
Type
Size
Default
end-ip
End of IPv4 exclusive range.
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
Start of IPv4 exclusive range.
ipv4-address
Not Specified
0.0.0.0
config ipv6-exclude-range
Parameter
Description
Type
Size
Default
end-ip
End of IPv6 exclusive range.
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
start-ip
Start of IPv6 exclusive range.
ipv6-address
Not Specified
::
config vpn ipsec phase2
Configure VPN autokey tunnel.
config vpn ipsec phase2
Description: Configure VPN autokey tunnel.
edit <name>
set add-route [phase1|enable|...]
set addke1 {option1}, {option2}, ...
set addke2 {option1}, {option2}, ...
set addke3 {option1}, {option2}, ...
set addke4 {option1}, {option2}, ...
set addke5 {option1}, {option2}, ...
set addke6 {option1}, {option2}, ...
set addke7 {option1}, {option2}, ...
set auto-negotiate [enable|disable]
set comments {var-string}
set dhcp-ipsec [enable|disable]
set dhgrp {option1}, {option2}, ...
set diffserv [enable|disable]
FortiOS 8.0.0 CLI Reference
2453
Fortinet Inc.

<!-- 来源页 2454 -->
set diffservcode {user}
set dst-addr-type [subnet|range|...]
set dst-end-ip {ipv4-address-any}
set dst-end-ip6 {ipv6-address}
set dst-name {string}
set dst-name6 {string}
set dst-port {integer}
set dst-start-ip {ipv4-address-any}
set dst-start-ip6 {ipv6-address}
set dst-subnet {ipv4-classnet-any}
set dst-subnet6 {ipv6-prefix}
set encapsulation [tunnel-mode|transport-mode]
set inbound-dscp-copy [phase1|enable|...]
set initiator-ts-narrow [enable|disable]
set keepalive [enable|disable]
set keylife-type [seconds|kbs|...]
set keylifekbs {integer}
set keylifeseconds {integer}
set l2tp [enable|disable]
set pfs [enable|disable]
set phase1name {string}
set proposal {option1}, {option2}, ...
set protocol {integer}
set replay [enable|disable]
set route-overlap [use-old|use-new|...]
set selector-match [exact|subset|...]
set single-source [enable|disable]
set src-addr-type [subnet|range|...]
set src-end-ip {ipv4-address-any}
set src-end-ip6 {ipv6-address}
set src-name {string}
set src-name6 {string}
set src-port {integer}
set src-start-ip {ipv4-address-any}
set src-start-ip6 {ipv6-address}
set src-subnet {ipv4-classnet-any}
set src-subnet6 {ipv6-prefix}
set use-natip [enable|disable]
next
end
config vpn ipsec phase2
Parameter
Description
Type
Size
Default
add-route
Enable/disable automatic route addition.
option
-phase1
FortiOS 8.0.0 CLI Reference
2454
Fortinet Inc.

<!-- 来源页 2455 -->
Parameter
Description
Type
Size
Default
Option
Description
phase1
Add route according to phase1 add-route setting.
enable
Add route for remote proxy ID.
disable
Do not add route for remote proxy ID.
addke1
phase2 ADDKE1 group.
option
-Option
Description
none
NONE.
ml-kem-512
ML-KEM-512.
ml-kem-768
ML-KEM-768.
ml-kem-1024
ML-KEM-1024.
kyber512
KYBER512.
kyber768
KYBER768.
kyber1024
KYBER1024.
frodo-l1
FRODO L1.
frodo-l3
FRODO L3.
frodo-l5
FRODO L5.
bike-l1
BIKE L1.
bike-l3
BIKE L3.
bike-l5
BIKE L5.
hqc128
HQC128.
hqc192
HQC192.
hqc256
HQC256.
0
NONE.
35
ML-KEM-512.
36
ML-KEM-768.
37
ML-KEM-1024.
1080
KYBER512.
1081
KYBER768.
1082
KYBER1024.
FortiOS 8.0.0 CLI Reference
2455
Fortinet Inc.

<!-- 来源页 2456 -->
Parameter
Description
Type
Size
Default
Option
Description
1083
FRODO L1.
1084
FRODO L3.
1085
FRODO L5.
1089
BIKE L1.
1090
BIKE L3.
1091
BIKE L5.
1092
HQC128.
1093
HQC192.
1094
HQC256.
addke2
phase2 ADDKE2 group.
option
-Option
Description
none
NONE.
ml-kem-512
ML-KEM-512.
ml-kem-768
ML-KEM-768.
ml-kem-1024
ML-KEM-1024.
kyber512
KYBER512.
kyber768
KYBER768.
kyber1024
KYBER1024.
frodo-l1
FRODO L1.
frodo-l3
FRODO L3.
frodo-l5
FRODO L5.
bike-l1
BIKE L1.
bike-l3
BIKE L3.
bike-l5
BIKE L5.
hqc128
HQC128.
hqc192
HQC192.
hqc256
HQC256.
0
NONE.
FortiOS 8.0.0 CLI Reference
2456
Fortinet Inc.

<!-- 来源页 2457 -->
Parameter
Description
Type
Size
Default
Option
Description
35
ML-KEM-512.
36
ML-KEM-768.
37
ML-KEM-1024.
1080
KYBER512.
1081
KYBER768.
1082
KYBER1024.
1083
FRODO L1.
1084
FRODO L3.
1085
FRODO L5.
1089
BIKE L1.
1090
BIKE L3.
1091
BIKE L5.
1092
HQC128.
1093
HQC192.
1094
HQC256.
addke3
phase2 ADDKE3 group.
option
-Option
Description
none
NONE.
ml-kem-512
ML-KEM-512.
ml-kem-768
ML-KEM-768.
ml-kem-1024
ML-KEM-1024.
kyber512
KYBER512.
kyber768
KYBER768.
kyber1024
KYBER1024.
frodo-l1
FRODO L1.
frodo-l3
FRODO L3.
frodo-l5
FRODO L5.
bike-l1
BIKE L1.
FortiOS 8.0.0 CLI Reference
2457
Fortinet Inc.

<!-- 来源页 2458 -->
Parameter
Description
Type
Size
Default
Option
Description
bike-l3
BIKE L3.
bike-l5
BIKE L5.
hqc128
HQC128.
hqc192
HQC192.
hqc256
HQC256.
0
NONE.
35
ML-KEM-512.
36
ML-KEM-768.
37
ML-KEM-1024.
1080
KYBER512.
1081
KYBER768.
1082
KYBER1024.
1083
FRODO L1.
1084
FRODO L3.
1085
FRODO L5.
1089
BIKE L1.
1090
BIKE L3.
1091
BIKE L5.
1092
HQC128.
1093
HQC192.
1094
HQC256.
addke4
phase2 ADDKE4 group.
option
-Option
Description
none
NONE.
ml-kem-512
ML-KEM-512.
ml-kem-768
ML-KEM-768.
ml-kem-1024
ML-KEM-1024.
kyber512
KYBER512.
FortiOS 8.0.0 CLI Reference
2458
Fortinet Inc.

<!-- 来源页 2459 -->
Parameter
Description
Type
Size
Default
Option
Description
kyber768
KYBER768.
kyber1024
KYBER1024.
frodo-l1
FRODO L1.
frodo-l3
FRODO L3.
frodo-l5
FRODO L5.
bike-l1
BIKE L1.
bike-l3
BIKE L3.
bike-l5
BIKE L5.
hqc128
HQC128.
hqc192
HQC192.
hqc256
HQC256.
0
NONE.
35
ML-KEM-512.
36
ML-KEM-768.
37
ML-KEM-1024.
1080
KYBER512.
1081
KYBER768.
1082
KYBER1024.
1083
FRODO L1.
1084
FRODO L3.
1085
FRODO L5.
1089
BIKE L1.
1090
BIKE L3.
1091
BIKE L5.
1092
HQC128.
1093
HQC192.
1094
HQC256.
addke5
phase2 ADDKE5 group.
option
-FortiOS 8.0.0 CLI Reference
2459
Fortinet Inc.

<!-- 来源页 2460 -->
Parameter
Description
Type
Size
Default
Option
Description
none
NONE.
ml-kem-512
ML-KEM-512.
ml-kem-768
ML-KEM-768.
ml-kem-1024
ML-KEM-1024.
kyber512
KYBER512.
kyber768
KYBER768.
kyber1024
KYBER1024.
frodo-l1
FRODO L1.
frodo-l3
FRODO L3.
frodo-l5
FRODO L5.
bike-l1
BIKE L1.
bike-l3
BIKE L3.
bike-l5
BIKE L5.
hqc128
HQC128.
hqc192
HQC192.
hqc256
HQC256.
0
NONE.
35
ML-KEM-512.
36
ML-KEM-768.
37
ML-KEM-1024.
1080
KYBER512.
1081
KYBER768.
1082
KYBER1024.
1083
FRODO L1.
1084
FRODO L3.
1085
FRODO L5.
1089
BIKE L1.
1090
BIKE L3.
1091
BIKE L5.
FortiOS 8.0.0 CLI Reference
2460
Fortinet Inc.

<!-- 来源页 2461 -->
Parameter
Description
Type
Size
Default
Option
Description
1092
HQC128.
1093
HQC192.
1094
HQC256.
addke6
phase2 ADDKE6 group.
option
-Option
Description
none
NONE.
ml-kem-512
ML-KEM-512.
ml-kem-768
ML-KEM-768.
ml-kem-1024
ML-KEM-1024.
kyber512
KYBER512.
kyber768
KYBER768.
kyber1024
KYBER1024.
frodo-l1
FRODO L1.
frodo-l3
FRODO L3.
frodo-l5
FRODO L5.
bike-l1
BIKE L1.
bike-l3
BIKE L3.
bike-l5
BIKE L5.
hqc128
HQC128.
hqc192
HQC192.
hqc256
HQC256.
0
NONE.
35
ML-KEM-512.
36
ML-KEM-768.
37
ML-KEM-1024.
1080
KYBER512.
1081
KYBER768.
1082
KYBER1024.
FortiOS 8.0.0 CLI Reference
2461
Fortinet Inc.

<!-- 来源页 2462 -->
Parameter
Description
Type
Size
Default
Option
Description
1083
FRODO L1.
1084
FRODO L3.
1085
FRODO L5.
1089
BIKE L1.
1090
BIKE L3.
1091
BIKE L5.
1092
HQC128.
1093
HQC192.
1094
HQC256.
addke7
phase2 ADDKE7 group.
option
-Option
Description
none
NONE.
ml-kem-512
ML-KEM-512.
ml-kem-768
ML-KEM-768.
ml-kem-1024
ML-KEM-1024.
kyber512
KYBER512.
kyber768
KYBER768.
kyber1024
KYBER1024.
frodo-l1
FRODO L1.
frodo-l3
FRODO L3.
frodo-l5
FRODO L5.
bike-l1
BIKE L1.
bike-l3
BIKE L3.
bike-l5
BIKE L5.
hqc128
HQC128.
hqc192
HQC192.
hqc256
HQC256.
0
NONE.
FortiOS 8.0.0 CLI Reference
2462
Fortinet Inc.

<!-- 来源页 2463 -->
Parameter
Description
Type
Size
Default
Option
Description
35
ML-KEM-512.
36
ML-KEM-768.
37
ML-KEM-1024.
1080
KYBER512.
1081
KYBER768.
1082
KYBER1024.
1083
FRODO L1.
1084
FRODO L3.
1085
FRODO L5.
1089
BIKE L1.
1090
BIKE L3.
1091
BIKE L5.
1092
HQC128.
1093
HQC192.
1094
HQC256.
auto-negotiate
Enable/disable IPsec SA auto-negotiation.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
comments
Comment.
var-string
Maximum
length: 255
dhcp-ipsec
Enable/disable DHCP-IPsec.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
dhgrp
Phase2 DH group.
option
-20
Option
Description
1
DH Group 1.
FortiOS 8.0.0 CLI Reference
2463
Fortinet Inc.

<!-- 来源页 2464 -->
Parameter
Description
Type
Size
Default
Option
Description
2
DH Group 2.
5
DH Group 5.
14
DH Group 14.
15
DH Group 15.
16
DH Group 16.
17
DH Group 17.
18
DH Group 18.
19
DH Group 19.
20
DH Group 20.
21
DH Group 21.
27
DH Group 27.
28
DH Group 28.
29
DH Group 29.
30
DH Group 30.
31
DH Group 31.
32
DH Group 32.
diffserv
Enable/disable applying DSCP value to
the IPsec tunnel outer IP header.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
diffservcode
DSCP value to be applied to the IPsec
tunnel outer IP header.
user
Not Specified
dst-addr-type
Remote proxy ID type.
option
-subnet
Option
Description
subnet
IPv4 subnet.
range
IPv4 range.
ip
IPv4 IP.
name
IPv4 firewall address or group name.
FortiOS 8.0.0 CLI Reference
2464
Fortinet Inc.

<!-- 来源页 2465 -->
Parameter
Description
Type
Size
Default
dst-end-ip
Remote proxy ID IPv4 end.
ipv4-address-any
Not Specified
0.0.0.0
dst-end-ip6
Remote proxy ID IPv6 end.
ipv6-address
Not Specified
::
dst-name
Remote proxy ID name.
string
Maximum
length: 79
dst-name6
Remote proxy ID name.
string
Maximum
length: 79
dst-port
Quick mode destination port (1 - 65535 or
0 for all).
integer
Minimum value:
0 Maximum
value: 65535
0
dst-start-ip
Remote proxy ID IPv4 start.
ipv4-address-any
Not Specified
0.0.0.0
dst-start-ip6
Remote proxy ID IPv6 start.
ipv6-address
Not Specified
::
dst-subnet
Remote proxy ID IPv4 subnet.
ipv4-classnet-any
Not Specified
0.0.0.0
0.0.0.0
dst-subnet6
Remote proxy ID IPv6 subnet.
ipv6-prefix
Not Specified
::/0
encapsulation
ESP encapsulation mode.
option
-tunnel-mode
Option
Description
tunnel-mode
Use tunnel mode encapsulation.
transport-mode
Use transport mode encapsulation.
inbound-dscp-copy
Enable/disable copying of the DSCP in the
ESP header to the inner IP header.
option
-phase1
Option
Description
phase1
copy the DCSP in the ESP header to the inner IP Header according to
the phase1 inbound_dscp_copy setting.
enable
Enable copying of the DSCP in the ESP header to the inner IP header.
disable
Disable copying of the DSCP in the ESP header to the inner IP header.
FortiOS 8.0.0 CLI Reference
2465
Fortinet Inc.

<!-- 来源页 2466 -->
Parameter
Description
Type
Size
Default
initiator-ts-narrow
Enable/disable traffic selector narrowing
for IKEv2 initiator.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
keepalive
Enable/disable keep alive.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
keylife-type
Keylife type.
option
-seconds
Option
Description
seconds
Key life in seconds.
kbs
Key life in kilobytes.
both
Key life both.
keylifekbs
Phase2 key life in number of kilobytes of
traffic (5120 - 4294967295).
integer
Minimum value:
5120 Maximum
value:
4294967295
5120
keylifeseconds
Phase2 key life in time in seconds (120 -172800).
integer
Minimum value:
120 Maximum
value: 172800
43200
l2tp
Enable/disable L2TP over IPsec.
option
-disable
Option
Description
enable
Enable L2TP over IPsec.
disable
Disable L2TP over IPsec.
name
IPsec tunnel name.
string
Maximum
length: 35
pfs
Enable/disable PFS feature.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
2466
Fortinet Inc.

<!-- 来源页 2467 -->
Parameter
Description
Type
Size
Default
phase1name
Phase 1 determines the options required
for phase 2.
string
Maximum
length: 35
proposal
Phase2 proposal.
option
-Option
Description
null-md5
null-md5
null-sha1
null-sha1
null-sha256
null-sha256
null-sha384
null-sha384
null-sha512
null-sha512
des-null
des-null
des-md5
des-md5
des-sha1
des-sha1
des-sha256
des-sha256
des-sha384
des-sha384
des-sha512
des-sha512
3des-null
3des-null
3des-md5
3des-md5
3des-sha1
3des-sha1
3des-sha256
3des-sha256
3des-sha384
3des-sha384
3des-sha512
3des-sha512
aes128-null
aes128-null
aes128-md5
aes128-md5
aes128-sha1
aes128-sha1
aes128-sha256
aes128-sha256
aes128-sha384
aes128-sha384
aes128-sha512
aes128-sha512
aes128gcm
aes128gcm
aes192-null
aes192-null
aes192-md5
aes192-md5
FortiOS 8.0.0 CLI Reference
2467
Fortinet Inc.

<!-- 来源页 2468 -->
Parameter
Description
Type
Size
Default
Option
Description
aes192-sha1
aes192-sha1
aes192-sha256
aes192-sha256
aes192-sha384
aes192-sha384
aes192-sha512
aes192-sha512
aes256-null
aes256-null
aes256-md5
aes256-md5
aes256-sha1
aes256-sha1
aes256-sha256
aes256-sha256
aes256-sha384
aes256-sha384
aes256-sha512
aes256-sha512
aes256gcm
aes256gcm
chacha20poly1305
chacha20poly1305
aria128-null
aria128-null
aria128-md5
aria128-md5
aria128-sha1
aria128-sha1
aria128-sha256
aria128-sha256
aria128-sha384
aria128-sha384
aria128-sha512
aria128-sha512
aria192-null
aria192-null
aria192-md5
aria192-md5
aria192-sha1
aria192-sha1
aria192-sha256
aria192-sha256
aria192-sha384
aria192-sha384
aria192-sha512
aria192-sha512
aria256-null
aria256-null
aria256-md5
aria256-md5
aria256-sha1
aria256-sha1
aria256-sha256
aria256-sha256
aria256-sha384
aria256-sha384
FortiOS 8.0.0 CLI Reference
2468
Fortinet Inc.

<!-- 来源页 2469 -->
Parameter
Description
Type
Size
Default
Option
Description
aria256-sha512
aria256-sha512
seed-null
seed-null
seed-md5
seed-md5
seed-sha1
seed-sha1
seed-sha256
seed-sha256
seed-sha384
seed-sha384
seed-sha512
seed-sha512
sm4-sm3
sm4-sm3
protocol
Quick mode protocol selector (1 - 255 or 0
for all).
integer
Minimum value:
0 Maximum
value: 255
0
replay
Enable/disable replay detection.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
route-overlap
Action for overlapping routes.
option
-use-new
Option
Description
use-old
Use the old route and do not add the new route.
use-new
Delete the old route and add the new route.
allow
Allow overlapping routes.
selector-match
Match type to use when comparing
selectors.
option
-auto
Option
Description
exact
Match selectors exactly.
subset
Match selectors by subset.
auto
Use subset or exact match depending on selector address type.
single-source
Enable/disable single source IP
restriction.
option
-disable
FortiOS 8.0.0 CLI Reference
2469
Fortinet Inc.

<!-- 来源页 2470 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Only single source IP will be accepted.
disable
Source IP range will be accepted.
src-addr-type
Local proxy ID type.
option
-subnet
Option
Description
subnet
IPv4 subnet.
range
IPv4 range.
ip
IPv4 IP.
name
IPv4 firewall address or group name.
src-end-ip
Local proxy ID end.
ipv4-address-any
Not Specified
0.0.0.0
src-end-ip6
Local proxy ID IPv6 end.
ipv6-address
Not Specified
::
src-name
Local proxy ID name.
string
Maximum
length: 79
src-name6
Local proxy ID name.
string
Maximum
length: 79
src-port
Quick mode source port (1 - 65535 or 0
for all).
integer
Minimum value:
0 Maximum
value: 65535
0
src-start-ip
Local proxy ID start.
ipv4-address-any
Not Specified
0.0.0.0
src-start-ip6
Local proxy ID IPv6 start.
ipv6-address
Not Specified
::
src-subnet
Local proxy ID subnet.
ipv4-classnet-any
Not Specified
0.0.0.0
0.0.0.0
src-subnet6
Local proxy ID IPv6 subnet.
ipv6-prefix
Not Specified
::/0
use-natip
Enable to use the FortiGate public IP as
the source selector when outbound NAT
is used.
option
-enable
FortiOS 8.0.0 CLI Reference
2470
Fortinet Inc.

<!-- 来源页 2471 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Replace source selector with interface IP when using outbound NAT.
disable
Do not modify source selector when using outbound NAT.
config vpn ipsec phase2-interface
Configure VPN autokey tunnel.
config vpn ipsec phase2-interface
Description: Configure VPN autokey tunnel.
edit <name>
set add-route [phase1|enable|...]
set addke1 {option1}, {option2}, ...
set addke2 {option1}, {option2}, ...
set addke3 {option1}, {option2}, ...
set addke4 {option1}, {option2}, ...
set addke5 {option1}, {option2}, ...
set addke6 {option1}, {option2}, ...
set addke7 {option1}, {option2}, ...
set auto-discovery-forwarder [phase1|enable|...]
set auto-discovery-sender [phase1|enable|...]
set auto-negotiate [enable|disable]
set comments {var-string}
set dhcp-ipsec [enable|disable]
set dhgrp {option1}, {option2}, ...
set diffserv [enable|disable]
set diffservcode {user}
set dst-addr-type [subnet|range|...]
set dst-end-ip {ipv4-address-any}
set dst-end-ip6 {ipv6-address}
set dst-name {string}
set dst-name6 {string}
set dst-port {integer}
set dst-start-ip {ipv4-address-any}
set dst-start-ip6 {ipv6-address}
set dst-subnet {ipv4-classnet-any}
set dst-subnet6 {ipv6-prefix}
set encapsulation [tunnel-mode|transport-mode]
set inbound-dscp-copy [phase1|enable|...]
set initiator-ts-narrow [enable|disable]
set keepalive [enable|disable]
set keylife-type [seconds|kbs|...]
set keylifekbs {integer}
set keylifeseconds {integer}
set l2tp [enable|disable]
set pfs [enable|disable]
FortiOS 8.0.0 CLI Reference
2471
Fortinet Inc.

<!-- 来源页 2472 -->
set phase1name {string}
set proposal {option1}, {option2}, ...
set protocol {integer}
set replay [enable|disable]
set route-overlap [use-old|use-new|...]
set single-source [enable|disable]
set src-addr-type [subnet|range|...]
set src-end-ip {ipv4-address-any}
set src-end-ip6 {ipv6-address}
set src-name {string}
set src-name6 {string}
set src-port {integer}
set src-start-ip {ipv4-address-any}
set src-start-ip6 {ipv6-address}
set src-subnet {ipv4-classnet-any}
set src-subnet6 {ipv6-prefix}
next
end
config vpn ipsec phase2-interface
Parameter
Description
Type
Size
Default
add-route
Enable/disable automatic route addition.
option
-phase1
Option
Description
phase1
Add route according to phase1 add-route setting.
enable
Add route for remote proxy ID.
disable
Do not add route for remote proxy ID.
addke1
phase2 ADDKE1 group.
option
-Option
Description
none
NONE.
ml-kem-512
ML-KEM-512.
ml-kem-768
ML-KEM-768.
ml-kem-1024
ML-KEM-1024.
kyber512
KYBER512.
kyber768
KYBER768.
kyber1024
KYBER1024.
frodo-l1
FRODO L1.
FortiOS 8.0.0 CLI Reference
2472
Fortinet Inc.

<!-- 来源页 2473 -->
Parameter
Description
Type
Size
Default
Option
Description
frodo-l3
FRODO L3.
frodo-l5
FRODO L5.
bike-l1
BIKE L1.
bike-l3
BIKE L3.
bike-l5
BIKE L5.
hqc128
HQC128.
hqc192
HQC192.
hqc256
HQC256.
0
NONE.
35
ML-KEM-512.
36
ML-KEM-768.
37
ML-KEM-1024.
1080
KYBER512.
1081
KYBER768.
1082
KYBER1024.
1083
FRODO L1.
1084
FRODO L3.
1085
FRODO L5.
1089
BIKE L1.
1090
BIKE L3.
1091
BIKE L5.
1092
HQC128.
1093
HQC192.
1094
HQC256.
addke2
phase2 ADDKE2 group.
option
-Option
Description
none
NONE.
ml-kem-512
ML-KEM-512.
FortiOS 8.0.0 CLI Reference
2473
Fortinet Inc.

<!-- 来源页 2474 -->
Parameter
Description
Type
Size
Default
Option
Description
ml-kem-768
ML-KEM-768.
ml-kem-1024
ML-KEM-1024.
kyber512
KYBER512.
kyber768
KYBER768.
kyber1024
KYBER1024.
frodo-l1
FRODO L1.
frodo-l3
FRODO L3.
frodo-l5
FRODO L5.
bike-l1
BIKE L1.
bike-l3
BIKE L3.
bike-l5
BIKE L5.
hqc128
HQC128.
hqc192
HQC192.
hqc256
HQC256.
0
NONE.
35
ML-KEM-512.
36
ML-KEM-768.
37
ML-KEM-1024.
1080
KYBER512.
1081
KYBER768.
1082
KYBER1024.
1083
FRODO L1.
1084
FRODO L3.
1085
FRODO L5.
1089
BIKE L1.
1090
BIKE L3.
1091
BIKE L5.
1092
HQC128.
1093
HQC192.
FortiOS 8.0.0 CLI Reference
2474
Fortinet Inc.

<!-- 来源页 2475 -->
Parameter
Description
Type
Size
Default
Option
Description
1094
HQC256.
addke3
phase2 ADDKE3 group.
option
-Option
Description
none
NONE.
ml-kem-512
ML-KEM-512.
ml-kem-768
ML-KEM-768.
ml-kem-1024
ML-KEM-1024.
kyber512
KYBER512.
kyber768
KYBER768.
kyber1024
KYBER1024.
frodo-l1
FRODO L1.
frodo-l3
FRODO L3.
frodo-l5
FRODO L5.
bike-l1
BIKE L1.
bike-l3
BIKE L3.
bike-l5
BIKE L5.
hqc128
HQC128.
hqc192
HQC192.
hqc256
HQC256.
0
NONE.
35
ML-KEM-512.
36
ML-KEM-768.
37
ML-KEM-1024.
1080
KYBER512.
1081
KYBER768.
1082
KYBER1024.
1083
FRODO L1.
1084
FRODO L3.
FortiOS 8.0.0 CLI Reference
2475
Fortinet Inc.

<!-- 来源页 2476 -->
Parameter
Description
Type
Size
Default
Option
Description
1085
FRODO L5.
1089
BIKE L1.
1090
BIKE L3.
1091
BIKE L5.
1092
HQC128.
1093
HQC192.
1094
HQC256.
addke4
phase2 ADDKE4 group.
option
-Option
Description
none
NONE.
ml-kem-512
ML-KEM-512.
ml-kem-768
ML-KEM-768.
ml-kem-1024
ML-KEM-1024.
kyber512
KYBER512.
kyber768
KYBER768.
kyber1024
KYBER1024.
frodo-l1
FRODO L1.
frodo-l3
FRODO L3.
frodo-l5
FRODO L5.
bike-l1
BIKE L1.
bike-l3
BIKE L3.
bike-l5
BIKE L5.
hqc128
HQC128.
hqc192
HQC192.
hqc256
HQC256.
0
NONE.
35
ML-KEM-512.
36
ML-KEM-768.
FortiOS 8.0.0 CLI Reference
2476
Fortinet Inc.

<!-- 来源页 2477 -->
Parameter
Description
Type
Size
Default
Option
Description
37
ML-KEM-1024.
1080
KYBER512.
1081
KYBER768.
1082
KYBER1024.
1083
FRODO L1.
1084
FRODO L3.
1085
FRODO L5.
1089
BIKE L1.
1090
BIKE L3.
1091
BIKE L5.
1092
HQC128.
1093
HQC192.
1094
HQC256.
addke5
phase2 ADDKE5 group.
option
-Option
Description
none
NONE.
ml-kem-512
ML-KEM-512.
ml-kem-768
ML-KEM-768.
ml-kem-1024
ML-KEM-1024.
kyber512
KYBER512.
kyber768
KYBER768.
kyber1024
KYBER1024.
frodo-l1
FRODO L1.
frodo-l3
FRODO L3.
frodo-l5
FRODO L5.
bike-l1
BIKE L1.
bike-l3
BIKE L3.
bike-l5
BIKE L5.
FortiOS 8.0.0 CLI Reference
2477
Fortinet Inc.

<!-- 来源页 2478 -->
Parameter
Description
Type
Size
Default
Option
Description
hqc128
HQC128.
hqc192
HQC192.
hqc256
HQC256.
0
NONE.
35
ML-KEM-512.
36
ML-KEM-768.
37
ML-KEM-1024.
1080
KYBER512.
1081
KYBER768.
1082
KYBER1024.
1083
FRODO L1.
1084
FRODO L3.
1085
FRODO L5.
1089
BIKE L1.
1090
BIKE L3.
1091
BIKE L5.
1092
HQC128.
1093
HQC192.
1094
HQC256.
addke6
phase2 ADDKE6 group.
option
-Option
Description
none
NONE.
ml-kem-512
ML-KEM-512.
ml-kem-768
ML-KEM-768.
ml-kem-1024
ML-KEM-1024.
kyber512
KYBER512.
kyber768
KYBER768.
kyber1024
KYBER1024.
FortiOS 8.0.0 CLI Reference
2478
Fortinet Inc.

<!-- 来源页 2479 -->
Parameter
Description
Type
Size
Default
Option
Description
frodo-l1
FRODO L1.
frodo-l3
FRODO L3.
frodo-l5
FRODO L5.
bike-l1
BIKE L1.
bike-l3
BIKE L3.
bike-l5
BIKE L5.
hqc128
HQC128.
hqc192
HQC192.
hqc256
HQC256.
0
NONE.
35
ML-KEM-512.
36
ML-KEM-768.
37
ML-KEM-1024.
1080
KYBER512.
1081
KYBER768.
1082
KYBER1024.
1083
FRODO L1.
1084
FRODO L3.
1085
FRODO L5.
1089
BIKE L1.
1090
BIKE L3.
1091
BIKE L5.
1092
HQC128.
1093
HQC192.
1094
HQC256.
addke7
phase2 ADDKE7 group.
option
-Option
Description
none
NONE.
FortiOS 8.0.0 CLI Reference
2479
Fortinet Inc.

<!-- 来源页 2480 -->
Parameter
Description
Type
Size
Default
Option
Description
ml-kem-512
ML-KEM-512.
ml-kem-768
ML-KEM-768.
ml-kem-1024
ML-KEM-1024.
kyber512
KYBER512.
kyber768
KYBER768.
kyber1024
KYBER1024.
frodo-l1
FRODO L1.
frodo-l3
FRODO L3.
frodo-l5
FRODO L5.
bike-l1
BIKE L1.
bike-l3
BIKE L3.
bike-l5
BIKE L5.
hqc128
HQC128.
hqc192
HQC192.
hqc256
HQC256.
0
NONE.
35
ML-KEM-512.
36
ML-KEM-768.
37
ML-KEM-1024.
1080
KYBER512.
1081
KYBER768.
1082
KYBER1024.
1083
FRODO L1.
1084
FRODO L3.
1085
FRODO L5.
1089
BIKE L1.
1090
BIKE L3.
1091
BIKE L5.
1092
HQC128.
FortiOS 8.0.0 CLI Reference
2480
Fortinet Inc.

<!-- 来源页 2481 -->
Parameter
Description
Type
Size
Default
Option
Description
1093
HQC192.
1094
HQC256.
auto-discovery-forwarder
Enable/disable forwarding short-cut
messages.
option
-phase1
Option
Description
phase1
Forward short-cut messages according to the phase1 auto-discovery-forwarder setting.
enable
Enable forwarding auto-discovery short-cut messages.
disable
Disable forwarding auto-discovery short-cut messages.
auto-discovery-sender
Enable/disable sending short-cut
messages.
option
-phase1
Option
Description
phase1
Send short-cut messages according to the phase1 auto-discovery-sender setting.
enable
Enable sending auto-discovery short-cut messages.
disable
Disable sending auto-discovery short-cut messages.
auto-negotiate
Enable/disable IPsec SA auto-negotiation.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
comments
Comment.
var-string
Maximum
length: 255
dhcp-ipsec
Enable/disable DHCP-IPsec.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
dhgrp
Phase2 DH group.
option
-20
FortiOS 8.0.0 CLI Reference
2481
Fortinet Inc.

<!-- 来源页 2482 -->
Parameter
Description
Type
Size
Default
Option
Description
1
DH Group 1.
2
DH Group 2.
5
DH Group 5.
14
DH Group 14.
15
DH Group 15.
16
DH Group 16.
17
DH Group 17.
18
DH Group 18.
19
DH Group 19.
20
DH Group 20.
21
DH Group 21.
27
DH Group 27.
28
DH Group 28.
29
DH Group 29.
30
DH Group 30.
31
DH Group 31.
32
DH Group 32.
diffserv
Enable/disable applying DSCP value to
the IPsec tunnel outer IP header.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
diffservcode
DSCP value to be applied to the IPsec
tunnel outer IP header.
user
Not Specified
dst-addr-type
Remote proxy ID type.
option
-subnet
Option
Description
subnet
IPv4 subnet.
range
IPv4 range.
FortiOS 8.0.0 CLI Reference
2482
Fortinet Inc.

<!-- 来源页 2483 -->
Parameter
Description
Type
Size
Default
Option
Description
ip
IPv4 IP.
name
IPv4 firewall address or group name.
subnet6
IPv6 subnet.
range6
IPv6 range.
ip6
IPv6 IP.
name6
IPv6 firewall address or group name.
dst-end-ip
Remote proxy ID IPv4 end.
ipv4-address-any
Not Specified
0.0.0.0
dst-end-ip6
Remote proxy ID IPv6 end.
ipv6-address
Not Specified
::
dst-name
Remote proxy ID name.
string
Maximum
length: 79
dst-name6
Remote proxy ID name.
string
Maximum
length: 79
dst-port
Quick mode destination port (1 - 65535 or
0 for all).
integer
Minimum value:
0 Maximum
value: 65535
0
dst-start-ip
Remote proxy ID IPv4 start.
ipv4-address-any
Not Specified
0.0.0.0
dst-start-ip6
Remote proxy ID IPv6 start.
ipv6-address
Not Specified
::
dst-subnet
Remote proxy ID IPv4 subnet.
ipv4-classnet-any
Not Specified
0.0.0.0
0.0.0.0
dst-subnet6
Remote proxy ID IPv6 subnet.
ipv6-prefix
Not Specified
::/0
encapsulation
ESP encapsulation mode.
option
-tunnel-mode
Option
Description
tunnel-mode
Use tunnel mode encapsulation.
transport-mode
Use transport mode encapsulation.
FortiOS 8.0.0 CLI Reference
2483
Fortinet Inc.

<!-- 来源页 2484 -->
Parameter
Description
Type
Size
Default
inbound-dscp-copy
Enable/disable copying of the DSCP in the
ESP header to the inner IP header.
option
-phase1
Option
Description
phase1
copy the DCSP in the ESP header to the inner IP Header according to
the phase1 inbound_dscp_copy setting.
enable
Enable copying of the DSCP in the ESP header to the inner IP header.
disable
Disable copying of the DSCP in the ESP header to the inner IP header.
initiator-ts-narrow
Enable/disable traffic selector narrowing
for IKEv2 initiator.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
keepalive
Enable/disable keep alive.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
keylife-type
Keylife type.
option
-seconds
Option
Description
seconds
Key life in seconds.
kbs
Key life in kilobytes.
both
Key life both.
keylifekbs
Phase2 key life in number of kilobytes of
traffic (5120 - 4294967295).
integer
Minimum value:
5120 Maximum
value:
4294967295
5120
keylifeseconds
Phase2 key life in time in seconds (120 -172800).
integer
Minimum value:
120 Maximum
value: 172800
43200
l2tp
Enable/disable L2TP over IPsec.
option
-disable
FortiOS 8.0.0 CLI Reference
2484
Fortinet Inc.

<!-- 来源页 2485 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable L2TP over IPsec.
disable
Disable L2TP over IPsec.
name
IPsec tunnel name.
string
Maximum
length: 35
pfs
Enable/disable PFS feature.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
phase1name
Phase 1 determines the options required
for phase 2.
string
Maximum
length: 15
proposal
Phase2 proposal.
option
-Option
Description
null-md5
null-md5
null-sha1
null-sha1
null-sha256
null-sha256
null-sha384
null-sha384
null-sha512
null-sha512
des-null
des-null
des-md5
des-md5
des-sha1
des-sha1
des-sha256
des-sha256
des-sha384
des-sha384
des-sha512
des-sha512
3des-null
3des-null
3des-md5
3des-md5
3des-sha1
3des-sha1
3des-sha256
3des-sha256
3des-sha384
3des-sha384
FortiOS 8.0.0 CLI Reference
2485
Fortinet Inc.

<!-- 来源页 2486 -->
Parameter
Description
Type
Size
Default
Option
Description
3des-sha512
3des-sha512
aes128-null
aes128-null
aes128-md5
aes128-md5
aes128-sha1
aes128-sha1
aes128-sha256
aes128-sha256
aes128-sha384
aes128-sha384
aes128-sha512
aes128-sha512
aes128gcm
aes128gcm
aes192-null
aes192-null
aes192-md5
aes192-md5
aes192-sha1
aes192-sha1
aes192-sha256
aes192-sha256
aes192-sha384
aes192-sha384
aes192-sha512
aes192-sha512
aes256-null
aes256-null
aes256-md5
aes256-md5
aes256-sha1
aes256-sha1
aes256-sha256
aes256-sha256
aes256-sha384
aes256-sha384
aes256-sha512
aes256-sha512
aes256gcm
aes256gcm
chacha20poly1305
chacha20poly1305
aria128-null
aria128-null
aria128-md5
aria128-md5
aria128-sha1
aria128-sha1
aria128-sha256
aria128-sha256
aria128-sha384
aria128-sha384
aria128-sha512
aria128-sha512
aria192-null
aria192-null
FortiOS 8.0.0 CLI Reference
2486
Fortinet Inc.

<!-- 来源页 2487 -->
Parameter
Description
Type
Size
Default
Option
Description
aria192-md5
aria192-md5
aria192-sha1
aria192-sha1
aria192-sha256
aria192-sha256
aria192-sha384
aria192-sha384
aria192-sha512
aria192-sha512
aria256-null
aria256-null
aria256-md5
aria256-md5
aria256-sha1
aria256-sha1
aria256-sha256
aria256-sha256
aria256-sha384
aria256-sha384
aria256-sha512
aria256-sha512
seed-null
seed-null
seed-md5
seed-md5
seed-sha1
seed-sha1
seed-sha256
seed-sha256
seed-sha384
seed-sha384
seed-sha512
seed-sha512
sm4-sm3
sm4-sm3
protocol
Quick mode protocol selector (1 - 255 or 0
for all).
integer
Minimum value:
0 Maximum
value: 255
0
replay
Enable/disable replay detection.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
route-overlap
Action for overlapping routes.
option
-use-new
Option
Description
use-old
Use the old route and do not add the new route.
FortiOS 8.0.0 CLI Reference
2487
Fortinet Inc.

<!-- 来源页 2488 -->
Parameter
Description
Type
Size
Default
Option
Description
use-new
Delete the old route and add the new route.
allow
Allow overlapping routes.
single-source
Enable/disable single source IP
restriction.
option
-disable
Option
Description
enable
Only single source IP will be accepted.
disable
Source IP range will be accepted.
src-addr-type
Local proxy ID type.
option
-subnet
Option
Description
subnet
IPv4 subnet.
range
IPv4 range.
ip
IPv4 IP.
name
IPv4 firewall address or group name.
subnet6
IPv6 subnet.
range6
IPv6 range.
ip6
IPv6 IP.
name6
IPv6 firewall address or group name.
src-end-ip
Local proxy ID end.
ipv4-address-any
Not Specified
0.0.0.0
src-end-ip6
Local proxy ID IPv6 end.
ipv6-address
Not Specified
::
src-name
Local proxy ID name.
string
Maximum
length: 79
src-name6
Local proxy ID name.
string
Maximum
length: 79
src-port
Quick mode source port (1 - 65535 or 0
for all).
integer
Minimum value:
0 Maximum
value: 65535
0
FortiOS 8.0.0 CLI Reference
2488
Fortinet Inc.

<!-- 来源页 2489 -->
Parameter
Description
Type
Size
Default
src-start-ip
Local proxy ID start.
ipv4-address-any
Not Specified
0.0.0.0
src-start-ip6
Local proxy ID IPv6 start.
ipv6-address
Not Specified
::
src-subnet
Local proxy ID subnet.
ipv4-classnet-any
Not Specified
0.0.0.0
0.0.0.0
src-subnet6
Local proxy ID IPv6 subnet.
ipv6-prefix
Not Specified
::/0
config vpn kmip-server
KMIP server entry configuration.
config vpn kmip-server
Description: KMIP server entry configuration.
edit <name>
set interface {string}
set interface-select-method [auto|sdwan|...]
set password {password}
set server-identity-check [enable|disable]
config server-list
Description: KMIP server list.
edit <id>
set cert {string}
set port {integer}
set server {string}
set status [enable|disable]
next
end
set source-ip {string}
set ssl-min-proto-version [default|SSLv3|...]
set username {string}
set vrf-select {integer}
next
end
config vpn kmip-server
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
FortiOS 8.0.0 CLI Reference
2489
Fortinet Inc.

<!-- 来源页 2490 -->
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
name
KMIP server entry name.
string
Maximum
length: 35
password
Password to use for connectivity to the KMIP
server.
password
Not
Specified
server-identity-check
Enable/disable KMIP server identity check (verify
server FQDN/IP address against the server
certificate).
option
-disable
Option
Description
enable
Enable server identity check.
disable
Disable server identity check.
source-ip
FortiGate IP address to be used for
communication with the KMIP server.
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
username
User name to use for connectivity to the KMIP
server.
string
Maximum
length: 63
FortiOS 8.0.0 CLI Reference
2490
Fortinet Inc.

<!-- 来源页 2491 -->
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
config server-list
Parameter
Description
Type
Size
Default
cert
Client certificate to use for connectivity to the
KMIP server.
string
Maximum
length: 35
id
ID
integer
Minimum value:
0 Maximum
value:
4294967295
0
port
KMIP server port.
integer
Minimum value:
0 Maximum
value: 65535
5696
server
KMIP server FQDN or IP address.
string
Maximum
length: 63
status
Enable/disable KMIP server.
option
-enable
Option
Description
enable
Enable server.
disable
Disable server.
config vpn l2tp
Configure L2TP.
config vpn l2tp
Description: Configure L2TP.
set compress [enable|disable]
set eip {ipv4-address}
set enforce-ipsec [enable|disable]
set hello-interval {integer}
set lcp-echo-interval {integer}
set lcp-max-echo-fails {integer}
set sip {ipv4-address}
set status [enable|disable]
set usrgrp {string}
end
FortiOS 8.0.0 CLI Reference
2491
Fortinet Inc.

<!-- 来源页 2492 -->
config vpn l2tp
Parameter
Description
Type
Size
Default
compress
Enable/disable data compression.
option
-disable
Option
Description
enable
Enable compress
disable
Disable compress
eip
End IP.
ipv4-address
Not
Specified
0.0.0.0
enforce-ipsec
Enable/disable IPsec enforcement.
option
-disable
Option
Description
enable
Enable enforce-ipsec
disable
Disable enforce-ipsec
hello-interval
L2TP hello message interval in seconds (0 - 3600
sec, default = 60).
integer
Minimum
value: 0
Maximum
value: 3600
60
lcp-echo-interval
Time in seconds between PPPoE Link Control
Protocol (LCP) echo requests.
integer
Minimum
value: 0
Maximum
value:
32767
5
lcp-max-echo-fails
Maximum number of missed LCP echo messages
before disconnect.
integer
Minimum
value: 0
Maximum
value:
32767
3
sip
Start IP.
ipv4-address
Not
Specified
0.0.0.0
status
Enable/disable FortiGate as a L2TP gateway.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
usrgrp
User group.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
2492
Fortinet Inc.

<!-- 来源页 2493 -->
config vpn pptp
Configure PPTP.
config vpn pptp
Description: Configure PPTP.
set eip {ipv4-address}
set ip-mode [range|usrgrp]
set local-ip {ipv4-address}
set sip {ipv4-address}
set status [enable|disable]
set usrgrp {string}
end
config vpn pptp
Parameter
Description
Type
Size
Default
eip
End IP.
ipv4-address
Not
Specified
0.0.0.0
ip-mode
IP assignment mode for PPTP client.
option
-range
Option
Description
range
PPTP client IP from manual config (range from sip to eip).
usrgrp
PPTP client IP from user-group defined server.
local-ip
Local IP to be used for peer's remote IP.
ipv4-address
Not
Specified
0.0.0.0
sip
Start IP.
ipv4-address
Not
Specified
0.0.0.0
status
Enable/disable FortiGate as a PPTP gateway.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
usrgrp
User group.
string
Maximum
length: 35
config vpn qkd
Configure Quantum Key Distribution servers
FortiOS 8.0.0 CLI Reference
2493
Fortinet Inc.

<!-- 来源页 2494 -->
config vpn qkd
Description: Configure Quantum Key Distribution servers
edit <name>
set certificate <name1>, <name2>, ...
set comment {var-string}
set id {string}
set peer {string}
set port {integer}
set server {string}
next
end
config vpn qkd
Parameter
Description
Type
Size
Default
certificate
<name>
Names of up to 4 certificates to offer to the KME.
Certificate name.
string
Maximum
length: 79
comment
Comment.
var-string
Maximum
length: 255
id
Quantum Key Distribution ID assigned by the KME.
string
Maximum
length: 291
name
Quantum Key Distribution configuration name.
string
Maximum
length: 35
peer
Authenticate Quantum Key Device's certificate with
the peer/peergrp.
string
Maximum
length: 35
port
Port to connect to on the KME.
integer
Minimum
value: 1
Maximum
value:
65535
0
server
IPv4, IPv6 or DNS address of the KME.
string
Maximum
length: 63
FortiOS 8.0.0 CLI Reference
2494
Fortinet Inc.

<!-- 来源页 2495 -->
config vpn ssl settings
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
FortiGate 70F, FortiGate 71F, FortiGate 800D, FortiGate 80F Bypass, FortiGate 80F DSL, FortiGate
80F Gen2, FortiGate 80F-POE, FortiGate 81F Gen2, FortiGate 81F-POE, FortiGate 900D, FortiGate
900G, FortiGate 901G, FortiGate-VM64 Aliyun, FortiGate-VM64 AWS, FortiGate-VM64 Azure,
FortiGate-VM64 GCP, FortiGate-VM64 OPC, FortiGate-VM64, FortiGateRugged 70F 3G4G,
FortiGateRugged 70F, FortiWiFi 80F 2R 3G4G DSL, FortiWiFi 80F 2R, FortiWiFi 81F 2R 3G4G DSL,
FortiWiFi 81F 2R 3G4G-POE, FortiWiFi 81F 2R-POE, FortiWiFi 81F 2R.
It is not available for: FortiGate 30G, FortiGate 31G, FortiGate 40F 3G4G, FortiGate 40F, FortiGate
50G 5G, FortiGate 50G DSL, FortiGate 50G SFP-POE, FortiGate 50G SFP, FortiGate 50G, FortiGate
51G 5G, FortiGate 51G SFP-POE, FortiGate 51G, FortiGate 60F, FortiGate 61F, FortiGate 70G-POE,
FortiGate 70G, FortiGate 71G-POE, FortiGate 71G, FortiGate 90G Gen2, FortiGate 90G, FortiGate 91G
Gen2, FortiGate 91G, FortiGateRugged 50G 5G, FortiGateRugged 60F 3G4G, FortiGateRugged 60F
Gen2, FortiGateRugged 70G 5G Dual, FortiGateRugged 70G, FortiWiFi 30G, FortiWiFi 31G, FortiWiFi
40F 3G4G, FortiWiFi 40F, FortiWiFi 50G 5G, FortiWiFi 50G DSL, FortiWiFi 50G SFP, FortiWiFi 50G,
FortiWiFi 51G, FortiWiFi 60F, FortiWiFi 61F, FortiWiFi 70G-POE, FortiWiFi 70G, FortiWiFi 71G.
Configure Agentless VPN.
config vpn ssl settings
Description: Configure Agentless VPN.
set algorithm [high|medium|...]
set auth-session-check-source-ip [enable|disable]
set auth-timeout {integer}
config authentication-rule
Description: Authentication rule for Agentless VPN.
edit <id>
set auth [any|local|...]
set cipher [any|high|...]
set client-cert [enable|disable]
set groups <name1>, <name2>, ...
set portal {string}
set realm {string}
set source-address <name1>, <name2>, ...
set source-address-negate [enable|disable]
set source-address6 <name1>, <name2>, ...
set source-address6-negate [enable|disable]
set source-interface <name1>, <name2>, ...
FortiOS 8.0.0 CLI Reference
2495
Fortinet Inc.

<!-- 来源页 2496 -->
set user-peer {string}
set users <name1>, <name2>, ...
next
end
set banned-cipher {option1}, {option2}, ...
set browser-language-detection [enable|disable]
set check-referer [enable|disable]
set ciphersuite {option1}, {option2}, ...
set client-sigalgs [no-rsa-pss|all]
set default-portal {string}
set deflate-compression-level {integer}
set deflate-min-data-size {integer}
set dns-suffix {var-string}
set dtls-heartbeat-fail-count {integer}
set dtls-heartbeat-idle-timeout {integer}
set dtls-heartbeat-interval {integer}
set dtls-hello-timeout {integer}
set dual-stack-mode [enable|disable]
set encode-2f-sequence [enable|disable]
set encrypt-and-store-password [enable|disable]
set force-two-factor-auth [enable|disable]
set header-x-forwarded-for [pass|add|...]
set hsts-include-subdomains [enable|disable]
set http-compression [enable|disable]
set http-only-cookie [enable|disable]
set http-request-body-timeout {integer}
set http-request-header-timeout {integer}
set https-redirect [enable|disable]
set idle-timeout {integer}
set login-attempt-limit {integer}
set login-block-time {integer}
set login-timeout {integer}
set port {integer}
set port-precedence [enable|disable]
set remote-https-cert-check [no-check|warn-on-error|...]
set reqclientcert [enable|disable]
set server-hostname {string}
set servercert {string}
set source-address <name1>, <name2>, ...
set source-address-negate [enable|disable]
set source-address6 <name1>, <name2>, ...
set source-address6-negate [enable|disable]
set source-interface <name1>, <name2>, ...
set ssl-client-renegotiation [disable|enable]
set ssl-insert-empty-fragment [enable|disable]
set ssl-max-proto-ver [tls1-0|tls1-1|...]
set ssl-min-proto-ver [tls1-0|tls1-1|...]
set status [enable|disable]
set tls-groups {option1}, {option2}, ...
set transform-backward-slashes [enable|disable]
set unsafe-legacy-renegotiation [enable|disable]
set url-obscuration [enable|disable]
FortiOS 8.0.0 CLI Reference
2496
Fortinet Inc.

<!-- 来源页 2497 -->
set user-peer {string}
set x-content-type-options [enable|disable]
end
config vpn ssl settings
Parameter
Description
Type
Size
Default
algorithm
Force the Agentless VPN security level.
High allows only high. Medium allows
medium and high. Low allows any.
option
-high
Option
Description
high
High algorithms.
medium
High and medium algorithms.
default
default
low
All algorithms.
auth-session-check-source-ip
Enable/disable checking of source IP for
authentication session.
option
-enable
Option
Description
enable
Enable checking of source IP for authentication session.
disable
Disable checking of source IP for authentication session.
auth-timeout
Agentless VPN authentication timeout (1 -259200 sec (3 days), 0 for no timeout).
integer
Minimum value:
0 Maximum
value: 259200
28800
banned-cipher
Select one or more cipher technologies
that cannot be used in Agentless VPN
negotiations. Only applies to TLS 1.2 and
below.
option
-SHA1 SHA256
SHA384
Option
Description
RSA
Ban the use of cipher suites using RSA key.
DHE
Ban the use of cipher suites using authenticated ephemeral DH key
agreement.
ECDHE
Ban the use of cipher suites using authenticated ephemeral ECDH key
agreement.
DSS
Ban the use of cipher suites using DSS authentication.
FortiOS 8.0.0 CLI Reference
2497
Fortinet Inc.

<!-- 来源页 2498 -->
Parameter
Description
Type
Size
Default
Option
Description
ECDSA
Ban the use of cipher suites using ECDSA authentication.
AES
Ban the use of cipher suites using either 128 or 256 bit AES.
AESGCM
Ban the use of cipher suites AES in Galois Counter Mode (GCM).
CAMELLIA
Ban the use of cipher suites using either 128 or 256 bit CAMELLIA.
3DES
Ban the use of cipher suites using triple DES
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
browser-language-detection
Enable/disable overriding the configured
system language based on the preferred
language of the browser.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
check-referer
Enable/disable verification of referer field
in HTTP request header.
option
-disable
Option
Description
enable
Enable verification of referer field in HTTP request header.
disable
Disable verification of referer field in HTTP request header.
ciphersuite
Select one or more TLS 1.3 ciphersuites to
enable. Does not affect ciphers in TLS 1.2
and below. At least one must be enabled.
To disable all, set ssl-max-proto-ver to
tls1-2 or below.
option
-TLS-AES-128-GCM-SHA256
TLS-AES-256-GCM-SHA384
TLS-CHACHA20-POLY1305-SHA256
FortiOS 8.0.0 CLI Reference
2498
Fortinet Inc.

<!-- 来源页 2499 -->
Parameter
Description
Type
Size
Default
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
client-sigalgs
Set signature algorithms related to client
authentication. Affects TLS version <= 1.2
only.
option
-all
Option
Description
no-rsa-pss
Disable RSA-PSS signature algorithms for client authentication.
all
Enable all supported signature algorithms for client authentication.
default-portal
Default Agentless VPN portal.
string
Maximum
length: 35
deflate-compression-level
Compression level (0~9).
integer
Minimum value:
0 Maximum
value: 9
6
deflate-min-data-size
Minimum amount of data that triggers
compression (200 - 65535 bytes).
integer
Minimum value:
200 Maximum
value: 65535
300
dns-suffix
DNS suffix used for Agentless VPN
clients.
var-string
Maximum
length: 253
dtls-heartbeat-fail-count
Number of missing heartbeats before the
connection is considered dropped.
integer
Minimum value:
3 Maximum
value: 10
3
dtls-heartbeat-idle-timeout
Idle timeout before DTLS heartbeat is
sent.
integer
Minimum value:
3 Maximum
value: 10
3
FortiOS 8.0.0 CLI Reference
2499
Fortinet Inc.

<!-- 来源页 2500 -->
Parameter
Description
Type
Size
Default
dtls-heartbeat-interval
Interval between DTLS heartbeat.
integer
Minimum value:
3 Maximum
value: 10
3
dtls-hello-timeout
SSLVPN maximum DTLS hello timeout (10
- 60 sec, default = 10).
integer
Minimum value:
10 Maximum
value: 60
10
dual-stack-mode
Agentless web mode: support IPv4 and
IPv6 bookmarks in the portal.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
encode-2f-sequence
Encode \2F sequence to forward slash in
URLs.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
encrypt-and-store-password
Encrypt and store user passwords for
Agentless VPN web sessions.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
force-two-factor-auth
Enable/disable only PKI users with two-factor authentication for Agentless VPNs.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
header-x-forwarded-for
Forward the same, add, or remove HTTP
header.
option
-add
Option
Description
pass
Forward the same HTTP header.
add
Add the HTTP header.
remove
Remove the HTTP header.
FortiOS 8.0.0 CLI Reference
2500
Fortinet Inc.

<!-- 来源页 2501 -->
Parameter
Description
Type
Size
Default
hsts-include-subdomains
Add HSTS includeSubDomains response
header.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
http-compression
Enable/disable to allow HTTP
compression over Agentless VPN
connections.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
http-only-cookie
Enable/disable Agentless VPN support for
HttpOnly cookies.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
http-request-body-timeout
Agentless VPN session is disconnected if
an HTTP request body is not received
within this time (1 - 60 sec, default = 20).
integer
Minimum value:
0 Maximum
value:
4294967295
30
http-request-header-timeout
Agentless VPN session is disconnected if
an HTTP request header is not received
within this time (1 - 60 sec, default = 20).
integer
Minimum value:
0 Maximum
value:
4294967295
20
https-redirect
Enable/disable redirect of port 80 to
Agentless VPN port.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
idle-timeout
Agentless VPN disconnects if idle for
specified time in seconds.
integer
Minimum value:
0 Maximum
value: 259200
300
FortiOS 8.0.0 CLI Reference
2501
Fortinet Inc.

<!-- 来源页 2502 -->
Parameter
Description
Type
Size
Default
login-attempt-limit
Agentless VPN maximum login attempt
times before block (0 - 10, default = 2, 0 =
no limit).
integer
Minimum value:
0 Maximum
value: 10
2
login-block-time
Time for which a user is blocked from
logging in after too many failed login
attempts (0 - 86400 sec, default = 60).
integer
Minimum value:
0 Maximum
value: 86400
60
login-timeout
Agentless VPN maximum login timeout (10
- 180 sec, default = 30).
integer
Minimum value:
10 Maximum
value: 180
30
port
Agentless VPN access port (1 - 65535).
integer
Minimum value:
1 Maximum
value: 65535
10443
port-precedence
Enable/disable, Enable means that if
Agentless VPN connections are allowed
on an interface admin GUI connections
are blocked on that interface.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
remote-https-cert-check
Configure how the FortiGate unit checks
and responds to the remote HTTPS
server's certificate (default = warn-on-error).
option
-warn-on-error
Option
Description
no-check
Do not check the remote HTTPS server's certificate.
warn-on-error
Display a warning when there is a certificate error.
reject-on-error
Reject connection when there is a certificate error.
reqclientcert
Enable/disable to require client
certificates for all Agentless VPN users.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
server-hostname
Server hostname for HTTPS. When set,
will be used for Agentless VPN web proxy
host header for any redirection.
string
Maximum
length: 255
FortiOS 8.0.0 CLI Reference
2502
Fortinet Inc.

<!-- 来源页 2503 -->
Parameter
Description
Type
Size
Default
servercert
Name of the server certificate to be used
for Agentless VPNs.
string
Maximum
length: 35
source-address
<name>
Source address of incoming traffic.
Address name.
string
Maximum
length: 79
source-address-negate
Enable/disable negated source address
match.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
source-address6
<name>
IPv6 source address of incoming traffic.
IPv6 address name.
string
Maximum
length: 79
source-address6-negate
Enable/disable negated source IPv6
address match.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
source-interface
<name>
Agentless VPN source interface of
incoming traffic.
Interface name.
string
Maximum
length: 35
ssl-client-renegotiation
Enable/disable to allow client
renegotiation by the server if the tunnel
goes down.
option
-disable
Option
Description
disable
Abort any SSL connection that attempts to renegotiate.
enable
Allow a SSL client to renegotiate.
ssl-insert-empty-fragment
Enable/disable insertion of empty
fragment.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
2503
Fortinet Inc.

<!-- 来源页 2504 -->
Parameter
Description
Type
Size
Default
ssl-max-proto-ver
SSL maximum protocol version.
option
-tls1-3
Option
Description
tls1-0
TLS version 1.0.
tls1-1
TLS version 1.1.
tls1-2
TLS version 1.2.
tls1-3
TLS version 1.3.
ssl-min-proto-ver
SSL minimum protocol version.
option
-tls1-2
Option
Description
tls1-0
TLS version 1.0.
tls1-1
TLS version 1.1.
tls1-2
TLS version 1.2.
tls1-3
TLS version 1.3.
status
Enable/disable Agentless VPN.
option
-enable
Option
Description
enable
Enable Agentless VPN.
disable
Disable Agentless VPN.
tls-groups
Configure the supported groups for TLS
negotiation.
option
-P-521 P-384
ML-KEM768
ML-KEM1024
P-384-MLKEM1024
P-256-MLKEM768
X25519-MLKEM768
X448
FFDHE4096
FFDHE6144
FFDHE8192
Option
Description
P-521
P-521
FortiOS 8.0.0 CLI Reference
2504
Fortinet Inc.

<!-- 来源页 2505 -->
Parameter
Description
Type
Size
Default
Option
Description
P-384
P-384
P-256
P-256
ML-KEM512
ML-KEM512
ML-KEM768
ML-KEM768
ML-KEM1024
ML-KEM1024
P-384-MLKEM1024
P-384-MLKEM1024
P-256-MLKEM768
P-256-MLKEM768
X25519-MLKEM768
X25519-MLKEM768
X448
X448
X25519
X25519
FFDHE2048
FFDHE2048
FFDHE3072
FFDHE3072
FFDHE4096
FFDHE4096
FFDHE6144
FFDHE6144
FFDHE8192
FFDHE8192
transform-backward-slashes
Transform backward slashes to forward
slashes in URLs.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
unsafe-legacy-renegotiation
Enable/disable unsafe legacy re-negotiation.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
2505
Fortinet Inc.

<!-- 来源页 2506 -->
Parameter
Description
Type
Size
Default
url-obscuration
Enable/disable to obscure the host name
of the URL of the web browser display.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
user-peer
Name of user peer.
string
Maximum
length: 35
x-content-type-options
Add HTTP X-Content-Type-Options
header.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
config authentication-rule
Parameter
Description
Type
Size
Default
auth
Agentless VPN authentication method
restriction.
option
-any
Option
Description
any
Any
local
Local
radius
RADIUS
tacacs+
TACACS+
ldap
LDAP
peer
PEER
cipher
Agentless VPN cipher strength.
option
-high
Option
Description
any
Any cipher strength.
high
High cipher strength (>= 168 bits).
medium
Medium cipher strength (>= 128 bits).
client-cert
Enable/disable Agentless VPN client certificate
restrictive.
option
-disable
FortiOS 8.0.0 CLI Reference
2506
Fortinet Inc.

<!-- 来源页 2507 -->
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
groups
<name>
User groups.
Group name.
string
Maximum
length: 79
id
ID (0 - 4294967295).
integer
Minimum value:
0 Maximum
value:
4294967295
0
portal
Agentless VPN portal.
string
Maximum
length: 35
realm
Agentless VPN realm.
string
Maximum
length: 35
source-address
<name>
Source address of incoming traffic.
Address name.
string
Maximum
length: 79
source-address-negate
Enable/disable negated source address match.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
source-address6
<name>
IPv6 source address of incoming traffic.
IPv6 address name.
string
Maximum
length: 79
source-address6-negate
Enable/disable negated source IPv6 address
match.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
source-interface
<name>
Agentless VPN source interface of incoming
traffic.
Interface name.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
2507
Fortinet Inc.

<!-- 来源页 2508 -->
Parameter
Description
Type
Size
Default
user-peer
Name of user peer.
string
Maximum
length: 35
users <name>
User name.
User name.
string
Maximum
length: 79
config vpn ssl web portal
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
FortiGate 70F, FortiGate 71F, FortiGate 800D, FortiGate 80F Bypass, FortiGate 80F DSL, FortiGate
80F Gen2, FortiGate 80F-POE, FortiGate 81F Gen2, FortiGate 81F-POE, FortiGate 900D, FortiGate
900G, FortiGate 901G, FortiGate-VM64 Aliyun, FortiGate-VM64 AWS, FortiGate-VM64 Azure,
FortiGate-VM64 GCP, FortiGate-VM64 OPC, FortiGate-VM64, FortiGateRugged 70F 3G4G,
FortiGateRugged 70F, FortiWiFi 80F 2R 3G4G DSL, FortiWiFi 80F 2R, FortiWiFi 81F 2R 3G4G DSL,
FortiWiFi 81F 2R 3G4G-POE, FortiWiFi 81F 2R-POE, FortiWiFi 81F 2R.
It is not available for: FortiGate 30G, FortiGate 31G, FortiGate 40F 3G4G, FortiGate 40F, FortiGate
50G 5G, FortiGate 50G DSL, FortiGate 50G SFP-POE, FortiGate 50G SFP, FortiGate 50G, FortiGate
51G 5G, FortiGate 51G SFP-POE, FortiGate 51G, FortiGate 60F, FortiGate 61F, FortiGate 70G-POE,
FortiGate 70G, FortiGate 71G-POE, FortiGate 71G, FortiGate 90G Gen2, FortiGate 90G, FortiGate 91G
Gen2, FortiGate 91G, FortiGateRugged 50G 5G, FortiGateRugged 60F 3G4G, FortiGateRugged 60F
Gen2, FortiGateRugged 70G 5G Dual, FortiGateRugged 70G, FortiWiFi 30G, FortiWiFi 31G, FortiWiFi
40F 3G4G, FortiWiFi 40F, FortiWiFi 50G 5G, FortiWiFi 50G DSL, FortiWiFi 50G SFP, FortiWiFi 50G,
FortiWiFi 51G, FortiWiFi 60F, FortiWiFi 61F, FortiWiFi 70G-POE, FortiWiFi 70G, FortiWiFi 71G.
Portal.
config vpn ssl web portal
Description: Portal.
edit <name>
set allow-user-access {option1}, {option2}, ...
config bookmark-group
Description: Portal bookmark group.
edit <name>
config bookmarks
Description: Bookmark table.
FortiOS 8.0.0 CLI Reference
2508
Fortinet Inc.

<!-- 来源页 2509 -->
edit <name>
set additional-params {var-string}
set apptype [ftp|rdp|...]
set color-depth [32|16|...]
set description {var-string}
set domain {var-string}
set folder {var-string}
config form-data
Description: Form data.
edit <name>
set value {var-string}
next
end
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
set sso [disable|static|...]
set sso-credential [sslvpn-login|alternative]
set sso-credential-sent-once [enable|disable]
set sso-password {password}
set sso-username {var-string}
set url {var-string}
set vnc-keyboard-layout [default|da|...]
set width {integer}
next
end
next
end
set clipboard [enable|disable]
set custom-lang {string}
set default-protocol [web|ftp|...]
set default-window-height {integer}
set default-window-width {integer}
set display-bookmark [enable|disable]
set display-connection-tools [enable|disable]
set display-history [enable|disable]
set display-status [enable|disable]
set dns-suffix {var-string}
set focus-bookmark [enable|disable]
set heading {string}
set hide-sso-credential [enable|disable]
config landing-page
Description: Landing page options.
FortiOS 8.0.0 CLI Reference
2509
Fortinet Inc.

<!-- 来源页 2510 -->
config form-data
Description: Form data.
edit <name>
set value {var-string}
next
end
set sso [disable|static|...]
set sso-credential [sslvpn-login|alternative]
set sso-password {password}
set sso-username {var-string}
set url {var-string}
end
set landing-page-mode [enable|disable]
set limit-user-logins [enable|disable]
set prefer-ipv6-dns [enable|disable]
set redir-url {var-string}
set rewrite-ip-uri-ui [enable|disable]
set smb-max-version [smbv1|smbv2|...]
set smb-min-version [smbv1|smbv2|...]
set smb-ntlmv1-auth [enable|disable]
set smbv1 [enable|disable]
set theme [jade|neutrino|...]
set use-sdwan [enable|disable]
set user-bookmark [enable|disable]
set user-group-bookmark [enable|disable]
set web-mode [enable|disable]
next
end
config vpn ssl web portal
Parameter
Description
Type
Size
Default
allow-user-access
Allow user access to Agentless VPN applications.
option
-web ftp
smb sftp
telnet ssh
vnc rdp ping
Option
Description
web
HTTP/HTTPS access.
ftp
FTP access.
smb
SMB/CIFS access.
sftp
SFTP access.
telnet
TELNET access.
ssh
SSH access.
FortiOS 8.0.0 CLI Reference
2510
Fortinet Inc.

<!-- 来源页 2511 -->
Parameter
Description
Type
Size
Default
Option
Description
vnc
VNC access.
rdp
RDP access.
ping
PING access.
clipboard
Enable to support RDP/VPC clipboard
functionality.
option
-enable
Option
Description
enable
Enable support of RDP/VNC clipboard.
disable
Disable support of RDP/VNC clipboard.
custom-lang
Change the web portal display language.
Overrides config system global set language. You
can use config system custom-language and
execute system custom-language to add custom
language files.
string
Maximum
length: 35
default-protocol
Application type that is set by default.
option
-web
Option
Description
web
HTTP/HTTPS.
ftp
FTP.
telnet
Telnet.
smb
SMB/CIFS.
vnc
VNC.
rdp
RDP.
ssh
SSH.
sftp
SFTP.
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
FortiOS 8.0.0 CLI Reference
2511
Fortinet Inc.

<!-- 来源页 2512 -->
Parameter
Description
Type
Size
Default
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
Enable to display the web portal bookmark
widget.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
display-connection-tools
Enable to display the web portal connection tools
widget.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
display-history
Enable to display the web portal user login history
widget.
option
-enable
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
dns-suffix
DNS suffix.
var-string
Maximum
length: 253
focus-bookmark
Enable to prioritize the placement of the
bookmark section over the quick-connection
section in the Agentless VPN application.
option
-disable
Option
Description
enable
Enable setting.
FortiOS 8.0.0 CLI Reference
2512
Fortinet Inc.

<!-- 来源页 2513 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable setting.
heading
Web portal heading message.
string
Maximum
length: 31
Agentless
VPN Portal
hide-sso-credential
Enable to prevent SSO credential being sent to
client.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
landing-page-mode
Enable/disable Agentless VPN landing page
mode.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
limit-user-logins
Enable to limit each user to one Agentless VPN
session at a time.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
name
Portal name.
string
Maximum
length: 35
prefer-ipv6-dns
Prefer to query IPv6 DNS server first if enabled.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
redir-url
Client login redirect URL.
var-string
Maximum
length: 255
rewrite-ip-uri-ui
Rewrite contents for URI contains IP and /ui/
(default = disable).
option
-disable
FortiOS 8.0.0 CLI Reference
2513
Fortinet Inc.

<!-- 来源页 2514 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable contents rewrite for URI contains "IP-address/ui/".
disable
Disable contents rewrite for URI contains "IP-address/ui/".
smb-max-version
SMB maximum client protocol version.
option
-smbv3
Option
Description
smbv1
SMB version 1.
smbv2
SMB version 2.
smbv3
SMB version 3.
smb-min-version
SMB minimum client protocol version.
option
-smbv2
Option
Description
smbv1
SMB version 1.
smbv2
SMB version 2.
smbv3
SMB version 3.
smb-ntlmv1-auth
Enable support of NTLMv1 for Samba
authentication.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
smbv1
SMB version 1.
option
-disable
Option
Description
enable
enable
disable
disable
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
FortiOS 8.0.0 CLI Reference
2514
Fortinet Inc.

<!-- 来源页 2515 -->
Parameter
Description
Type
Size
Default
Option
Description
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
use-sdwan
Use SD-WAN rules to get output interface.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
user-bookmark
Enable to allow web portal users to create their
own bookmarks.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
user-group-bookmark
Enable to allow web portal users to create
bookmarks for all users in the same user group.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
web-mode
Enable/disable Agentless VPN web mode.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
2515
Fortinet Inc.

<!-- 来源页 2516 -->
config bookmark-group
Parameter
Description
Type
Size
Default
name
Bookmark group name.
string
Maximum
length: 35
config bookmarks
Parameter
Description
Type
Size
Default
additional-params
Additional parameters.
var-string
Maximum
length: 128
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
FortiOS 8.0.0 CLI Reference
2516
Fortinet Inc.

<!-- 来源页 2517 -->
Parameter
Description
Type
Size
Default
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
FortiOS 8.0.0 CLI Reference
2517
Fortinet Inc.

<!-- 来源页 2518 -->
Parameter
Description
Type
Size
Default
Option
Description
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
FortiOS 8.0.0 CLI Reference
2518
Fortinet Inc.

<!-- 来源页 2519 -->
Parameter
Description
Type
Size
Default
Option
Description
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
FortiOS 8.0.0 CLI Reference
2519
Fortinet Inc.

<!-- 来源页 2520 -->
Parameter
Description
Type
Size
Default
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
static
Static SSO.
auto
Auto SSO.
sso-credential
Single sign-on credentials.
option
-sslvpn-login
Option
Description
sslvpn-login
Agentless VPN login.
alternative
Alternative.
sso-credential-sent-once
Single sign-on credentials are only sent
once to remote server.
option
-disable
Option
Description
enable
Single sign-on credentials are only sent once to remote server.
disable
Single sign-on credentials are sent to remote server for every HTTP
request.
sso-password
SSO password.
password
Not Specified
sso-username
SSO user name.
var-string
Maximum
length: 35
url
URL parameter.
var-string
Maximum
length: 128
FortiOS 8.0.0 CLI Reference
2520
Fortinet Inc.

<!-- 来源页 2521 -->
Parameter
Description
Type
Size
Default
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
config form-data
Parameter
Description
Type
Size
Default
name
Name.
string
Maximum length:
35
value
Value.
var-string
Maximum length:
63
FortiOS 8.0.0 CLI Reference
2521
Fortinet Inc.

<!-- 来源页 2522 -->
config landing-page
Parameter
Description
Type
Size
Default
sso
Single sign-on.
option
-disable
Option
Description
disable
Disable SSO.
static
Static SSO.
auto
Auto SSO.
sso-credential
Single sign-on credentials.
option
-sslvpn-login
Option
Description
sslvpn-login
Agentless VPN login.
alternative
Alternative.
sso-password
SSO password.
password
Not
Specified
sso-username
SSO user name.
var-string
Maximum
length: 35
url
Landing page URL.
var-string
Maximum
length: 511
config form-data
Parameter
Description
Type
Size
Default
name
Name.
string
Maximum length:
35
value
Value.
var-string
Maximum length:
63
FortiOS 8.0.0 CLI Reference
2522
Fortinet Inc.

<!-- 来源页 2523 -->
config vpn ssl web realm
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
FortiGate 70F, FortiGate 71F, FortiGate 800D, FortiGate 80F Bypass, FortiGate 80F DSL, FortiGate
80F Gen2, FortiGate 80F-POE, FortiGate 81F Gen2, FortiGate 81F-POE, FortiGate 900D, FortiGate
900G, FortiGate 901G, FortiGate-VM64 Aliyun, FortiGate-VM64 AWS, FortiGate-VM64 Azure,
FortiGate-VM64 GCP, FortiGate-VM64 OPC, FortiGate-VM64, FortiGateRugged 70F 3G4G,
FortiGateRugged 70F, FortiWiFi 80F 2R 3G4G DSL, FortiWiFi 80F 2R, FortiWiFi 81F 2R 3G4G DSL,
FortiWiFi 81F 2R 3G4G-POE, FortiWiFi 81F 2R-POE, FortiWiFi 81F 2R.
It is not available for: FortiGate 30G, FortiGate 31G, FortiGate 40F 3G4G, FortiGate 40F, FortiGate
50G 5G, FortiGate 50G DSL, FortiGate 50G SFP-POE, FortiGate 50G SFP, FortiGate 50G, FortiGate
51G 5G, FortiGate 51G SFP-POE, FortiGate 51G, FortiGate 60F, FortiGate 61F, FortiGate 70G-POE,
FortiGate 70G, FortiGate 71G-POE, FortiGate 71G, FortiGate 90G Gen2, FortiGate 90G, FortiGate 91G
Gen2, FortiGate 91G, FortiGateRugged 50G 5G, FortiGateRugged 60F 3G4G, FortiGateRugged 60F
Gen2, FortiGateRugged 70G 5G Dual, FortiGateRugged 70G, FortiWiFi 30G, FortiWiFi 31G, FortiWiFi
40F 3G4G, FortiWiFi 40F, FortiWiFi 50G 5G, FortiWiFi 50G DSL, FortiWiFi 50G SFP, FortiWiFi 50G,
FortiWiFi 51G, FortiWiFi 60F, FortiWiFi 61F, FortiWiFi 70G-POE, FortiWiFi 70G, FortiWiFi 71G.
Realm.
config vpn ssl web realm
Description: Realm.
edit <url-path>
set login-page {var-string}
set max-concurrent-user {integer}
set nas-ip {ipv4-address}
set radius-port {integer}
set radius-server {string}
set virtual-host {var-string}
set virtual-host-only [enable|disable]
set virtual-host-server-cert {string}
next
end
FortiOS 8.0.0 CLI Reference
2523
Fortinet Inc.

<!-- 来源页 2524 -->
config vpn ssl web realm
Parameter
Description
Type
Size
Default
login-page
Replacement HTML for Agentless VPN login page.
var-string
Maximum
length:
32768
max-concurrent-user
Maximum concurrent users (0 - 65535, 0 means
unlimited).
integer
Minimum
value: 0
Maximum
value:
65535
0
nas-ip
IP address used as a NAS-IP to communicate with
the RADIUS server.
ipv4-address
Not
Specified
0.0.0.0
radius-port
RADIUS service port number (0 - 65535, 0 means
user.radius.radius-port).
integer
Minimum
value: 0
Maximum
value:
65535
0
radius-server
RADIUS server associated with realm.
string
Maximum
length: 35
url-path
URL path to access Agentless VPN login page.
string
Maximum
length: 35
virtual-host
Virtual host name for realm.
var-string
Maximum
length: 255
virtual-host-only
Enable/disable enforcement of virtual host method
for Agentless VPN client access.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
virtual-host-server-cert
Name of the server certificate to used for this
realm.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
2524
Fortinet Inc.

<!-- 来源页 2525 -->
config vpn ssl web user-bookmark
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
FortiGate 70F, FortiGate 71F, FortiGate 800D, FortiGate 80F Bypass, FortiGate 80F DSL, FortiGate
80F Gen2, FortiGate 80F-POE, FortiGate 81F Gen2, FortiGate 81F-POE, FortiGate 900D, FortiGate
900G, FortiGate 901G, FortiGate-VM64 Aliyun, FortiGate-VM64 AWS, FortiGate-VM64 Azure,
FortiGate-VM64 GCP, FortiGate-VM64 OPC, FortiGate-VM64, FortiGateRugged 70F 3G4G,
FortiGateRugged 70F, FortiWiFi 80F 2R 3G4G DSL, FortiWiFi 80F 2R, FortiWiFi 81F 2R 3G4G DSL,
FortiWiFi 81F 2R 3G4G-POE, FortiWiFi 81F 2R-POE, FortiWiFi 81F 2R.
It is not available for: FortiGate 30G, FortiGate 31G, FortiGate 40F 3G4G, FortiGate 40F, FortiGate
50G 5G, FortiGate 50G DSL, FortiGate 50G SFP-POE, FortiGate 50G SFP, FortiGate 50G, FortiGate
51G 5G, FortiGate 51G SFP-POE, FortiGate 51G, FortiGate 60F, FortiGate 61F, FortiGate 70G-POE,
FortiGate 70G, FortiGate 71G-POE, FortiGate 71G, FortiGate 90G Gen2, FortiGate 90G, FortiGate 91G
Gen2, FortiGate 91G, FortiGateRugged 50G 5G, FortiGateRugged 60F 3G4G, FortiGateRugged 60F
Gen2, FortiGateRugged 70G 5G Dual, FortiGateRugged 70G, FortiWiFi 30G, FortiWiFi 31G, FortiWiFi
40F 3G4G, FortiWiFi 40F, FortiWiFi 50G 5G, FortiWiFi 50G DSL, FortiWiFi 50G SFP, FortiWiFi 50G,
FortiWiFi 51G, FortiWiFi 60F, FortiWiFi 61F, FortiWiFi 70G-POE, FortiWiFi 70G, FortiWiFi 71G.
Configure Agentless VPN user bookmark.
config vpn ssl web user-bookmark
Description: Configure Agentless VPN user bookmark.
edit <name>
config bookmarks
Description: Bookmark table.
edit <name>
set additional-params {var-string}
set apptype [ftp|rdp|...]
set color-depth [32|16|...]
set description {var-string}
set domain {var-string}
set folder {var-string}
config form-data
Description: Form data.
edit <name>
set value {var-string}
next
end
set height {integer}
FortiOS 8.0.0 CLI Reference
2525
Fortinet Inc.

<!-- 来源页 2526 -->
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
set sso [disable|static|...]
set sso-credential [sslvpn-login|alternative]
set sso-credential-sent-once [enable|disable]
set sso-password {password}
set sso-username {var-string}
set url {var-string}
set vnc-keyboard-layout [default|da|...]
set width {integer}
next
end
set custom-lang {string}
next
end
config vpn ssl web user-bookmark
Parameter
Description
Type
Size
Default
custom-lang
Personal language.
string
Maximum
length: 35
name
User and group name.
string
Maximum
length: 101
config bookmarks
Parameter
Description
Type
Size
Default
additional-params
Additional parameters.
var-string
Maximum
length: 128
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
FortiOS 8.0.0 CLI Reference
2526
Fortinet Inc.

<!-- 来源页 2527 -->
Parameter
Description
Type
Size
Default
Option
Description
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
FortiOS 8.0.0 CLI Reference
2527
Fortinet Inc.

<!-- 来源页 2528 -->
Parameter
Description
Type
Size
Default
Option
Description
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
FortiOS 8.0.0 CLI Reference
2528
Fortinet Inc.

<!-- 来源页 2529 -->
Parameter
Description
Type
Size
Default
Option
Description
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
FortiOS 8.0.0 CLI Reference
2529
Fortinet Inc.

<!-- 来源页 2530 -->
Parameter
Description
Type
Size
Default
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
FortiOS 8.0.0 CLI Reference
2530
Fortinet Inc.

<!-- 来源页 2531 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable SSO.
static
Static SSO.
auto
Auto SSO.
sso-credential
Single sign-on credentials.
option
-sslvpn-login
Option
Description
sslvpn-login
Agentless VPN login.
alternative
Alternative.
sso-credential-sent-once
Single sign-on credentials are only sent
once to remote server.
option
-disable
Option
Description
enable
Single sign-on credentials are only sent once to remote server.
disable
Single sign-on credentials are sent to remote server for every HTTP
request.
sso-password
SSO password.
password
Not Specified
sso-username
SSO user name.
var-string
Maximum
length: 35
url
URL parameter.
var-string
Maximum
length: 128
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
FortiOS 8.0.0 CLI Reference
2531
Fortinet Inc.

<!-- 来源页 2532 -->
Parameter
Description
Type
Size
Default
Option
Description
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
config form-data
Parameter
Description
Type
Size
Default
name
Name.
string
Maximum length:
35
value
Value.
var-string
Maximum length:
63
FortiOS 8.0.0 CLI Reference
2532
Fortinet Inc.

<!-- 来源页 2533 -->
config vpn ssl web user-group-bookmark
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
FortiGate 70F, FortiGate 71F, FortiGate 800D, FortiGate 80F Bypass, FortiGate 80F DSL, FortiGate
80F Gen2, FortiGate 80F-POE, FortiGate 81F Gen2, FortiGate 81F-POE, FortiGate 900D, FortiGate
900G, FortiGate 901G, FortiGate-VM64 Aliyun, FortiGate-VM64 AWS, FortiGate-VM64 Azure,
FortiGate-VM64 GCP, FortiGate-VM64 OPC, FortiGate-VM64, FortiGateRugged 70F 3G4G,
FortiGateRugged 70F, FortiWiFi 80F 2R 3G4G DSL, FortiWiFi 80F 2R, FortiWiFi 81F 2R 3G4G DSL,
FortiWiFi 81F 2R 3G4G-POE, FortiWiFi 81F 2R-POE, FortiWiFi 81F 2R.
It is not available for: FortiGate 30G, FortiGate 31G, FortiGate 40F 3G4G, FortiGate 40F, FortiGate
50G 5G, FortiGate 50G DSL, FortiGate 50G SFP-POE, FortiGate 50G SFP, FortiGate 50G, FortiGate
51G 5G, FortiGate 51G SFP-POE, FortiGate 51G, FortiGate 60F, FortiGate 61F, FortiGate 70G-POE,
FortiGate 70G, FortiGate 71G-POE, FortiGate 71G, FortiGate 90G Gen2, FortiGate 90G, FortiGate 91G
Gen2, FortiGate 91G, FortiGateRugged 50G 5G, FortiGateRugged 60F 3G4G, FortiGateRugged 60F
Gen2, FortiGateRugged 70G 5G Dual, FortiGateRugged 70G, FortiWiFi 30G, FortiWiFi 31G, FortiWiFi
40F 3G4G, FortiWiFi 40F, FortiWiFi 50G 5G, FortiWiFi 50G DSL, FortiWiFi 50G SFP, FortiWiFi 50G,
FortiWiFi 51G, FortiWiFi 60F, FortiWiFi 61F, FortiWiFi 70G-POE, FortiWiFi 70G, FortiWiFi 71G.
Configure Agentless VPN user group bookmark.
config vpn ssl web user-group-bookmark
Description: Configure Agentless VPN user group bookmark.
edit <name>
config bookmarks
Description: Bookmark table.
edit <name>
set additional-params {var-string}
set apptype [ftp|rdp|...]
set color-depth [32|16|...]
set description {var-string}
set domain {var-string}
set folder {var-string}
config form-data
Description: Form data.
edit <name>
set value {var-string}
next
end
set height {integer}
FortiOS 8.0.0 CLI Reference
2533
Fortinet Inc.

<!-- 来源页 2534 -->
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
set sso [disable|static|...]
set sso-credential [sslvpn-login|alternative]
set sso-credential-sent-once [enable|disable]
set sso-password {password}
set sso-username {var-string}
set url {var-string}
set vnc-keyboard-layout [default|da|...]
set width {integer}
next
end
next
end
config vpn ssl web user-group-bookmark
Parameter
Description
Type
Size
Default
name
Group name.
string
Maximum length:
64
config bookmarks
Parameter
Description
Type
Size
Default
additional-params
Additional parameters.
var-string
Maximum
length: 128
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
FortiOS 8.0.0 CLI Reference
2534
Fortinet Inc.

<!-- 来源页 2535 -->
Parameter
Description
Type
Size
Default
Option
Description
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
FortiOS 8.0.0 CLI Reference
2535
Fortinet Inc.

<!-- 来源页 2536 -->
Parameter
Description
Type
Size
Default
Option
Description
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
FortiOS 8.0.0 CLI Reference
2536
Fortinet Inc.

<!-- 来源页 2537 -->
Parameter
Description
Type
Size
Default
Option
Description
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
FortiOS 8.0.0 CLI Reference
2537
Fortinet Inc.

<!-- 来源页 2538 -->
Parameter
Description
Type
Size
Default
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
FortiOS 8.0.0 CLI Reference
2538
Fortinet Inc.

<!-- 来源页 2539 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable SSO.
static
Static SSO.
auto
Auto SSO.
sso-credential
Single sign-on credentials.
option
-sslvpn-login
Option
Description
sslvpn-login
Agentless VPN login.
alternative
Alternative.
sso-credential-sent-once
Single sign-on credentials are only sent
once to remote server.
option
-disable
Option
Description
enable
Single sign-on credentials are only sent once to remote server.
disable
Single sign-on credentials are sent to remote server for every HTTP
request.
sso-password
SSO password.
password
Not Specified
sso-username
SSO user name.
var-string
Maximum
length: 35
url
URL parameter.
var-string
Maximum
length: 128
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
FortiOS 8.0.0 CLI Reference
2539
Fortinet Inc.

<!-- 来源页 2540 -->
Parameter
Description
Type
Size
Default
Option
Description
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
config form-data
Parameter
Description
Type
Size
Default
name
Name.
string
Maximum length:
35
value
Value.
var-string
Maximum length:
63
FortiOS 8.0.0 CLI Reference
2540
Fortinet Inc.
