# 用户 / 认证 / 证书

> 来源: FortiOS-8.0.0-CLI_Reference.pdf
> 覆盖命令/章节: user, authentication, certificate
> 本文件由 extract_pdf.py 从官方 PDF 自动提取，请勿手动编辑；
> 如需修正请修改 map.json 后重跑脚本。

---


<!-- 来源页 205 -->
authentication
This section includes syntax for the following commands:
l config authentication rule on page 205
l config authentication scheme on page 208
l config authentication setting on page 212
config authentication rule
Configure Authentication Rules.
config authentication rule
Description: Configure Authentication Rules.
edit <name>
set active-auth-method {string}
set cert-auth-cookie [enable|disable]
set comments {var-string}
set cors-depth {integer}
set cors-stateful [enable|disable]
set dstaddr <name1>, <name2>, ...
set dstaddr6 <name1>, <name2>, ...
set ip-based [enable|disable]
set protocol [http|ftp|...]
set session-logout [enable|disable]
set srcaddr <name1>, <name2>, ...
set srcaddr6 <name1>, <name2>, ...
set srcintf <name1>, <name2>, ...
set sso-auth-method {string}
set status [enable|disable]
set transaction-based [enable|disable]
set web-auth-cookie [enable|disable]
set web-portal [enable|disable]
next
end
config authentication rule
Parameter
Description
Type
Size
Default
active-auth-method
Select an active authentication method.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
205
Fortinet Inc.

<!-- 来源页 206 -->
Parameter
Description
Type
Size
Default
cert-auth-cookie
Enable/disable to use device certificate as
authentication cookie (default = enable).
option
-enable
Option
Description
enable
Enable device certificate as authentication cookie.
disable
Disable device certificate as authentication cookie.
comments
Comment.
var-string
Maximum
length:
1023
cors-depth
Depth to allow CORS access (default = 3).
integer
Minimum
value: 1
Maximum
value: 8
3
cors-stateful
Enable/disable allowance of CORS access (default
= disable).
option
-disable
Option
Description
enable
Enable allowance of CORS access
disable
Disable allowance of CORS access
dstaddr
<name>
Select an IPv4 destination address from available
options. Required for web proxy authentication.
Address name.
string
Maximum
length: 79
dstaddr6
<name>
Select an IPv6 destination address from available
options. Required for web proxy authentication.
Address name.
string
Maximum
length: 79
ip-based
Enable/disable IP-based authentication. When
enabled, previously authenticated users from the
same IP address will be exempted.
option
-enable
Option
Description
enable
Enable IP-based authentication.
disable
Disable IP-based authentication.
name
Authentication rule name.
string
Maximum
length: 35
protocol
Authentication is required for the selected
protocol (default = HTTP).
option
-http
FortiOS 8.0.0 CLI Reference
206
Fortinet Inc.

<!-- 来源页 207 -->
Parameter
Description
Type
Size
Default
Option
Description
http
HTTP traffic is matched and authentication is required.
ftp
FTP traffic is matched and authentication is required.
socks
SOCKS traffic is matched and authentication is required.
ssh
SSH traffic is matched and authentication is required.
ztna-portal
ZTNA portal traffic is matched and authentication is required.
session-logout
Enable/disable logout of a user from the current
session.
option
-disable
Option
Description
enable
Enable logout of a user from the current session
disable
Disable logout of a user from the current session
srcaddr
<name>
Authentication is required for the selected IPv4
source address.
Address name.
string
Maximum
length: 79
srcaddr6
<name>
Authentication is required for the selected IPv6
source address.
Address name.
string
Maximum
length: 79
srcintf <name>
Incoming (ingress) interface.
Interface name.
string
Maximum
length: 79
sso-auth-method
Select a single-sign on (SSO) authentication
method.
string
Maximum
length: 35
status
Enable/disable this authentication rule.
option
-enable
Option
Description
enable
Enable this authentication rule.
disable
Disable this authentication rule.
transaction-based
Enable/disable transaction based authentication
(default = disable).
option
-disable
Option
Description
enable
Enable transaction based authentication.
disable
Disable transaction based authentication.
FortiOS 8.0.0 CLI Reference
207
Fortinet Inc.

<!-- 来源页 208 -->
Parameter
Description
Type
Size
Default
web-auth-cookie
Enable/disable Web authentication cookies
(default = disable).
option
-disable
Option
Description
enable
Enable Web authentication cookie.
disable
Disable Web authentication cookie.
web-portal
Enable/disable web portal for proxy transparent
policy (default = enable).
option
-enable
Option
Description
enable
Enable web-portal.
disable
Disable web-portal.
config authentication scheme
Configure Authentication Schemes.
config authentication scheme
Description: Configure Authentication Schemes.
edit <name>
set captcha [enable|disable]
set captcha-secret-key {string}
set captcha-site-key {string}
set captcha-vendor [google-recaptcha-v2-checkbox|google-recaptcha-v2-invisible|...]
set cert-http-header [enable|disable]
set digest-algo {option1}, {option2}, ...
set digest-rfc2069 [enable|disable]
set domain-controller {string}
set external-idp {string}
set fsso-agent-for-ntlm {string}
set fsso-guest [enable|disable]
set group-attr-type [display-name|external-id]
set kerberos-keytab {string}
set method {option1}, {option2}, ...
set negotiate-ntlm [enable|disable]
set oidc-server {string}
set oidc-timeout {integer}
set require-tfa [enable|disable]
set saml-server {string}
set saml-timeout {integer}
set ssh-ca {string}
set user-cert [enable|disable]
set user-database <name1>, <name2>, ...
FortiOS 8.0.0 CLI Reference
208
Fortinet Inc.

<!-- 来源页 209 -->
next
end
config authentication scheme
Parameter
Description
Type
Size
Default
captcha *
Enable/disable CAPTCHA for form authentication
(default = disable).
option
-disable
Option
Description
enable
Enable CAPTCHA for form authentication.
disable
Disable CAPTCHA for form authentication.
captcha-secret-key *
CAPTCHA secret key.
string
Maximum
length: 63
captcha-site-key *
CAPTCHA site key.
string
Maximum
length: 63
captcha-vendor *
CAPTCHA vendor (default = google-recaptcha-v2-checkbox).
option
-google-recaptcha-v2-checkbox
Option
Description
google-recaptcha-v2-checkbox
Google reCAPTCHA v2, with checkbox.
google-recaptcha-v2-invisible
Google reCAPTCHA v2, without checkbox.
google-recaptcha-v3
Google reCAPTCHA v3.
cloudflare-turnstile
Cloudflare Turnstile.
cert-http-header
Enable/disable authentication with user
certificate in Client-Cert HTTP header (default =
disable).
option
-disable
Option
Description
enable
Enable client certificate authentication with HTTP header (RFC9440).
disable
Disable client certificate authentication with HTTP header (RFC9440).
digest-algo
Digest Authentication Algorithms.
option
-md5 sha-256
FortiOS 8.0.0 CLI Reference
209
Fortinet Inc.

<!-- 来源页 210 -->
Parameter
Description
Type
Size
Default
Option
Description
md5
MD5.
sha-256
SHA-256.
digest-rfc2069
Enable/disable support for the deprecated
RFC2069 Digest Client (no cnonce field, default =
disable).
option
-disable
Option
Description
enable
Enable support for the deprecated RFC2069 Digest Client (no cnonce
field).
disable
Disable support for the deprecated RFC2069 Digest Client (no cnonce
field).
domain-controller
Domain controller setting.
string
Maximum
length: 35
external-idp
External identity provider configuration.
string
Maximum
length: 35
fsso-agent-for-ntlm
FSSO agent to use for NTLM authentication.
string
Maximum
length: 35
fsso-guest
Enable/disable user fsso-guest authentication
(default = disable).
option
-disable
Option
Description
enable
Enable user fsso-guest authentication.
disable
Disable user fsso-guest authentication.
group-attr-type
Group attribute type used to match SCIM groups
(default = display-name).
option
-display-name
Option
Description
display-name
Display name.
external-id
External ID.
kerberos-keytab
Kerberos keytab setting.
string
Maximum
length: 35
method
Authentication methods (default = basic).
option
-FortiOS 8.0.0 CLI Reference
210
Fortinet Inc.

<!-- 来源页 211 -->
Parameter
Description
Type
Size
Default
Option
Description
ntlm
NTLM authentication.
basic
Basic HTTP authentication.
digest
Digest HTTP authentication.
form
Form-based HTTP authentication.
negotiate
Negotiate authentication.
fsso
Fortinet Single Sign-On (FSSO) authentication.
rsso
RADIUS Single Sign-On (RSSO) authentication.
ssh-publickey
Public key based SSH authentication.
cert
Client certificate authentication.
saml
SAML authentication.
oidc
OpenID Connect.
entra-sso
Entra ID based Single Sign-On (SSO) authentication.
ztna-relay
ZTNA relay authentication.
name
Authentication scheme name.
string
Maximum
length: 35
negotiate-ntlm
Enable/disable negotiate authentication for
NTLM (default = disable).
option
-enable
Option
Description
enable
Enable negotiate authentication for NTLM.
disable
Disable negotiate authentication for NTLM.
oidc-server *
OpenID Connect server configuration.
string
Maximum
length: 35
oidc-timeout
*
OpenID Connect authentication timeout in
seconds.
integer
Minimum
value: 30
Maximum
value: 1200
120
require-tfa
Enable/disable two-factor authentication (default
= disable).
option
-disable
Option
Description
enable
Enable two-factor authentication.
disable
Disable two-factor authentication.
FortiOS 8.0.0 CLI Reference
211
Fortinet Inc.

<!-- 来源页 212 -->
Parameter
Description
Type
Size
Default
saml-server
SAML configuration.
string
Maximum
length: 35
saml-timeout
SAML authentication timeout in seconds.
integer
Minimum
value: 30
Maximum
value: 1200
120
ssh-ca
SSH CA name.
string
Maximum
length: 35
user-cert
Enable/disable authentication with user
certificate (default = disable).
option
-disable
Option
Description
enable
Enable client certificate field authentication.
disable
Disable client certificate field authentication.
user-database
<name>
Authentication server to contain user information;
"local-user-db" (default) or "123" (for LDAP).
Authentication server name.
string
Maximum
length: 79
* This parameter may not exist in some models.
config authentication setting
Configure authentication setting.
config authentication setting
Description: Configure authentication setting.
set active-auth-scheme {string}
set auth-https [enable|disable]
set captive-portal {string}
set captive-portal-ip {ipv4-address-any}
set captive-portal-ip6 {ipv6-address}
set captive-portal-port {integer}
set captive-portal-ssl-port {integer}
set captive-portal-type [fqdn|ip]
set captive-portal6 {string}
set cert-auth [enable|disable]
set cert-captive-portal {string}
set cert-captive-portal-ip {ipv4-address-any}
set cert-captive-portal-port {integer}
set cookie-max-age {integer}
set cookie-refresh-div {integer}
set dev-range <name1>, <name2>, ...
set ems-root-ca [enable|disable]
set ip-auth-cookie [enable|disable]
FortiOS 8.0.0 CLI Reference
212
Fortinet Inc.

<!-- 来源页 213 -->
set persistent-cookie [enable|disable]
set sso-auth-scheme {string}
set update-time {user}
set user-cert-ca <name1>, <name2>, ...
end
config authentication setting
Parameter
Description
Type
Size
Default
active-auth-scheme
Active authentication method (scheme name).
string
Maximum
length: 35
auth-https
Enable/disable redirecting HTTP user
authentication to HTTPS.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
captive-portal
Captive portal host name.
string
Maximum
length: 255
captive-portal-ip
Captive portal IP address.
ipv4-address-any
Not
Specified
0.0.0.0
captive-portal-ip6
Captive portal IPv6 address.
ipv6-address
Not
Specified
::
captive-portal-port
Captive portal port number (1 - 65535, default =
7830).
integer
Minimum
value: 1
Maximum
value:
65535
7830
captive-portal-ssl-port
Captive portal SSL port number (1 - 65535, default
= 7831).
integer
Minimum
value: 1
Maximum
value:
65535
7831
captive-portal-type
Captive portal type.
option
-fqdn
Option
Description
fqdn
Use FQDN for captive portal.
ip
Use an IP address for captive portal.
FortiOS 8.0.0 CLI Reference
213
Fortinet Inc.

<!-- 来源页 214 -->
Parameter
Description
Type
Size
Default
captive-portal6
IPv6 captive portal host name.
string
Maximum
length: 255
cert-auth
Enable/disable redirecting certificate
authentication to HTTPS portal.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
cert-captive-portal
Certificate captive portal host name.
string
Maximum
length: 255
cert-captive-portal-ip
Certificate captive portal IP address.
ipv4-address-any
Not
Specified
0.0.0.0
cert-captive-portal-port
Certificate captive portal port number (1 - 65535,
default = 7832).
integer
Minimum
value: 1
Maximum
value:
65535
7832
cookie-max-age
Persistent web portal cookie maximum age in
minutes (30 - 10080 (1 week), default = 480 (8
hours)).
integer
Minimum
value: 30
Maximum
value:
10080
480
cookie-refresh-div
Refresh rate divider of persistent web portal
cookie (default = 2). Refresh value = cookie-max-age/cookie-refresh-div.
integer
Minimum
value: 2
Maximum
value: 4
2
dev-range
<name>
Address range for the IP based device query.
Address name.
string
Maximum
length: 79
ems-root-ca
*
Enable/disable use of the EMS root CA for
FortiClient, ZTNA, and endpoint authentication
(default = enable).
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
ip-auth-cookie
Enable/disable persistent cookie on IP based web
portal authentication (default = disable).
option
-disable
FortiOS 8.0.0 CLI Reference
214
Fortinet Inc.

<!-- 来源页 215 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable persistent cookie for IP-based authentication.
disable
Disable persistent cookie for IP-based authentication.
persistent-cookie
Enable/disable persistent cookie on web portal
authentication (default = enable).
option
-enable
Option
Description
enable
Enable persistent cookie.
disable
Disable persistent cookie.
sso-auth-scheme
Single-Sign-On authentication method (scheme
name).
string
Maximum
length: 35
update-time
Time of the last update.
user
Not
Specified
user-cert-ca
<name>
CA certificate used for client certificate
verification.
CA certificate list.
string
Maximum
length: 79
* This parameter may not exist in some models.
FortiOS 8.0.0 CLI Reference
215
Fortinet Inc.

---


<!-- 来源页 247 -->
certificate
This section includes syntax for the following commands:
l config certificate ca on page 247
l config certificate crl on page 249
l config certificate hsm-local on page 250
l config certificate local on page 254
l config certificate remote on page 259
config certificate ca
CA certificate.
config certificate ca
Description: CA certificate.
edit <name>
set auto-update-days {integer}
set auto-update-days-warning {integer}
set ca {user}
set ca-identifier {string}
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
config certificate ca
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
FortiOS 8.0.0 CLI Reference
247
Fortinet Inc.

<!-- 来源页 248 -->
Parameter
Description
Type
Size
Default
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
range
Either global or VDOM IP address range for the
CA certificate.
option
-global
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
FortiOS 8.0.0 CLI Reference
248
Fortinet Inc.

<!-- 来源页 249 -->
Parameter
Description
Type
Size
Default
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
config certificate crl
Certificate Revocation List as a PEM file.
config certificate crl
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
set source-ip {ipv4-address}
set update-interval {integer}
set update-vdom {string}
next
end
config certificate crl
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
FortiOS 8.0.0 CLI Reference
249
Fortinet Inc.

<!-- 来源页 250 -->
Parameter
Description
Type
Size
Default
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
-global
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
config certificate hsm-local
Local certificates whose keys are stored on HSM.
config certificate hsm-local
Description: Local certificates whose keys are stored on HSM.
edit <name>
FortiOS 8.0.0 CLI Reference
250
Fortinet Inc.

<!-- 来源页 251 -->
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
config certificate hsm-local
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
FortiOS 8.0.0 CLI Reference
251
Fortinet Inc.

<!-- 来源页 252 -->
Para
met
er
Description
Ty
pe
Size
Def
ault
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
rsa-sign-pkcs1-4096-sha512
4096 bit RSA - PKCS#1 v1.5 padding - SHA512 Digest.
rsa-sign-pss-2048-sha256
2048 bit RSA - PSS padding - SHA256 Digest.
rsa-sign-pss-3072-sha256
3072 bit RSA - PSS padding - SHA256 Digest.
rsa-sign-pss-4096-sha256
4096 bit RSA - PSS padding - SHA256 Digest.
FortiOS 8.0.0 CLI Reference
252
Fortinet Inc.

<!-- 来源页 253 -->
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
FortiOS 8.0.0 CLI Reference
253
Fortinet Inc.

<!-- 来源页 254 -->
Para
met
er
Description
Ty
pe
Size
Def
ault
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
-glo
bal
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
Option
Description
unknown
Unknown type of HSM.
gch
Google Cloud HSM.
config certificate local
Local keys and certificates.
FortiOS 8.0.0 CLI Reference
254
Fortinet Inc.

<!-- 来源页 255 -->
config certificate local
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
set range [global|vdom]
set scep-password {password}
set scep-url {string}
set source [factory|user|...]
set source-ip {ipv4-address}
set state {user}
next
end
FortiOS 8.0.0 CLI Reference
255
Fortinet Inc.

<!-- 来源页 256 -->
config certificate local
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
FortiOS 8.0.0 CLI Reference
256
Fortinet Inc.

<!-- 来源页 257 -->
Parameter
Description
Type
Size
Default
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
FortiOS 8.0.0 CLI Reference
257
Fortinet Inc.

<!-- 来源页 258 -->
Parameter
Description
Type
Size
Default
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
FortiOS 8.0.0 CLI Reference
258
Fortinet Inc.

<!-- 来源页 259 -->
Parameter
Description
Type
Size
Default
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
-global
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
config certificate remote
Remote certificate as a PEM file.
FortiOS 8.0.0 CLI Reference
259
Fortinet Inc.

<!-- 来源页 260 -->
config certificate remote
Description: Remote certificate as a PEM file.
edit <name>
set range [global|vdom]
set remote {user}
set source [factory|user|...]
next
end
config certificate remote
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
-global
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
user
User generated certificate.
bundle
Bundle file certificate.
FortiOS 8.0.0 CLI Reference
260
Fortinet Inc.

---


<!-- 来源页 2223 -->
user
This section includes syntax for the following commands:
l config user adgrp on page 2223
l config user certificate on page 2225
l config user domain-controller on page 2226
l config user exchange on page 2230
l config user external-identity-provider on page 2232
l config user fortitoken on page 2234
l config user fsso-polling on page 2240
l config user fsso on page 2235
l config user group on page 2242
l config user krb-keytab on page 2249
l config user ldap on page 2250
l config user local on page 2259
l config user nac-policy on page 2264
l config user oidc on page 2268
l config user password-policy on page 2270
l config user peer on page 2272
l config user peergrp on page 2274
l config user pop3 on page 2275
l config user quarantine on page 2276
l config user radius on page 2278
l config user saml on page 2294
l config user scim on page 2300
l config user security-exempt-list on page 2302
l config user setting on page 2303
l config user tacacs+ on page 2308
config user adgrp
Configure FSSO groups.
config user adgrp
Description: Configure FSSO groups.
edit <name>
set connector-source {string}
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
FortiOS 8.0.0 CLI Reference
2223
Fortinet Inc.

<!-- 来源页 2224 -->
set fabric-object-source [member|local|...]
set id {integer}
set server-name {string}
set uuid {uuid}
next
end
config user adgrp
Parameter
Description
Type
Size
Default
connector-source
FSSO connector source.
string
Maximum
length: 35
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
2224
Fortinet Inc.

<!-- 来源页 2225 -->
Parameter
Description
Type
Size
Default
id
Group ID. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
name
Name.
string
Maximum
length: 511
server-name
FSSO agent name.
string
Maximum
length: 35
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
config user certificate
Configure certificate users.
config user certificate
Description: Configure certificate users.
edit <name>
set common-name {string}
set id {integer}
set issuer {string}
set status [enable|disable]
set type [single-certificate|trusted-issuer]
next
end
config user certificate
Parameter
Description
Type
Size
Default
common-name
Certificate common name.
string
Maximum
length: 64
id
User ID. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
issuer
CA certificate used for client certificate
verification.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
2225
Fortinet Inc.

<!-- 来源页 2226 -->
Parameter
Description
Type
Size
Default
name
User name.
string
Maximum
length: 64
status
Enable/disable allowing the certificate user to
authenticate with the FortiGate unit.
option
-enable
Option
Description
enable
Enable user.
disable
Disable user.
type
Type of certificate authentication method.
option
-single-certificate
Option
Description
single-certificate
Single certificate.
trusted-issuer
Trusted CA issuer.
config user domain-controller
Configure domain controller entries.
config user domain-controller
Description: Configure domain controller entries.
edit <name>
set ad-mode [none|ds|...]
set adlds-dn {string}
set adlds-ip-address {ipv4-address}
set adlds-ip6 {ipv6-address}
set adlds-port {integer}
set change-detection [enable|disable]
set change-detection-period {integer}
set dns-srv-lookup [enable|disable]
set domain-name {string}
config extra-server
Description: Extra servers.
edit <id>
set ip-address {ipv4-address}
set port {integer}
set source-ip-address {ipv4-address}
set source-port {integer}
next
end
set hostname {string}
set interface {string}
FortiOS 8.0.0 CLI Reference
2226
Fortinet Inc.

<!-- 来源页 2227 -->
set interface-select-method [auto|sdwan|...]
set ip-address {ipv4-address}
set ip6 {ipv6-address}
set ldap-server <name1>, <name2>, ...
set password {password}
set port {integer}
set replication-port {integer}
set source-ip-address {ipv4-address}
set source-ip6 {ipv6-address}
set source-port {integer}
set username {string}
next
end
config user domain-controller
Parameter
Description
Type
Size
Default
ad-mode
Set Active Directory mode.
option
-none
Option
Description
none
The server is not configured as an Active Directory Domain Server (AD
DS).
ds
The server is configured as an Active Directory Domain Server (AD DS).
lds
The server is an Active Directory Lightweight Domain Server (AD LDS).
adlds-dn
AD LDS distinguished name.
string
Maximum
length: 255
adlds-ip-address
AD LDS IPv4 address.
ipv4-address
Not
Specified
0.0.0.0
adlds-ip6
AD LDS IPv6 address.
ipv6-address
Not
Specified
::
adlds-port
Port number of AD LDS service (default = 389).
integer
Minimum
value: 0
Maximum
value:
65535
389
change-detection
Enable/disable detection of a configuration
change in the Active Directory server.
option
-disable
Option
Description
enable
Enable detection of a configuration change in the Active Directory
server.
FortiOS 8.0.0 CLI Reference
2227
Fortinet Inc.

<!-- 来源页 2228 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable detection of a configuration change in the Active Directory
server.
change-detection-period
Minutes to detect a configuration change in the
Active Directory server (5 - 10080 minutes (7
days), default = 60).
integer
Minimum
value: 5
Maximum
value:
10080
60
dns-srv-lookup
Enable/disable DNS service lookup.
option
-disable
Option
Description
enable
Enable DNS service lookup.
disable
Disable DNS service lookup.
domain-name
Domain DNS name.
string
Maximum
length: 255
hostname
Hostname of the server to connect to.
string
Maximum
length: 255
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
ip-address
Domain controller IPv4 address.
ipv4-address
Not
Specified
0.0.0.0
ip6
Domain controller IPv6 address.
ipv6-address
Not
Specified
::
ldap-server
<name>
LDAP server name(s).
LDAP server name.
string
Maximum
length: 79
name
Domain controller entry name.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
2228
Fortinet Inc.

<!-- 来源页 2229 -->
Parameter
Description
Type
Size
Default
password
Password for specified username.
password
Not
Specified
port
Port to be used for communication with the
domain controller (default = 445).
integer
Minimum
value: 0
Maximum
value:
65535
445
replication-port
Port to be used for communication with the
domain controller for replication service. Port
number 0 indicates automatic discovery.
integer
Minimum
value: 0
Maximum
value:
65535
0
source-ip-address
FortiGate IPv4 address to be used for
communication with the domain controller.
ipv4-address
Not
Specified
0.0.0.0
source-ip6
FortiGate IPv6 address to be used for
communication with the domain controller.
ipv6-address
Not
Specified
::
source-port
Source port to be used for communication with the
domain controller.
integer
Minimum
value: 0
Maximum
value:
65535
0
username
User name to sign in with. Must have proper
permissions for service.
string
Maximum
length: 64
config extra-server
Parameter
Description
Type
Size
Default
id
Server ID.
integer
Minimum
value: 1
Maximum
value: 100
0
ip-address
Domain controller IP address.
ipv4-address
Not
Specified
0.0.0.0
port
Port to be used for communication with the domain
controller (default = 445).
integer
Minimum
value: 0
Maximum
value:
65535
445
source-ip-address
FortiGate IPv4 address to be used for
communication with the domain controller.
ipv4-address
Not
Specified
0.0.0.0
FortiOS 8.0.0 CLI Reference
2229
Fortinet Inc.

<!-- 来源页 2230 -->
Parameter
Description
Type
Size
Default
source-port
Source port to be used for communication with the
domain controller.
integer
Minimum
value: 0
Maximum
value:
65535
0
config user exchange
Configure MS Exchange server entries.
config user exchange
Description: Configure MS Exchange server entries.
edit <name>
set auth-level [connect|call|...]
set auth-type [spnego|ntlm|...]
set auto-discover-kdc [enable|disable]
set connect-protocol [rpc-over-tcp|rpc-over-http|...]
set domain-name {string}
set http-auth-type [basic|ntlm]
set ip {ipv4-address-any}
set kdc-ip <ipv41>, <ipv42>, ...
set password {password}
set server-name {string}
set ssl-min-proto-version [default|SSLv3|...]
set username {string}
set validate-server-certificate [disable|enable]
next
end
config user exchange
Parameter
Description
Type
Size
Default
auth-level
Authentication security level used for the RPC
protocol layer.
option
-privacy
Option
Description
connect
RPC authentication level 'connect'.
call
RPC authentication level 'call'.
packet
RPC authentication level 'packet'.
integrity
RPC authentication level 'integrity'.
privacy
RPC authentication level 'privacy'.
FortiOS 8.0.0 CLI Reference
2230
Fortinet Inc.

<!-- 来源页 2231 -->
Parameter
Description
Type
Size
Default
auth-type
Authentication security type used for the RPC
protocol layer.
option
-kerberos
Option
Description
spnego
Negotiate authentication.
ntlm
NTLM authentication.
kerberos
Kerberos authentication.
auto-discover-kdc
Enable/disable automatic discovery of KDC IP
addresses.
option
-enable
Option
Description
enable
Enable automatic discovery of KDC IP addresses.
disable
Disable automatic discovery of KDC IP addresses.
connect-protocol
Connection protocol used to connect to MS
Exchange service.
option
-rpc-over-https
Option
Description
rpc-over-tcp
Connect using RPC-over-TCP. Use for MS Exchange 2010 and earlier
versions. Supported in MS Exchange 2013.
rpc-over-http
Connect using RPC-over-HTTP. Use for MS Exchange 2016 and later
versions. Supported in MS Exchange 2013.
rpc-over-https
Connect using RPC-over-HTTPS. Use for MS Exchange 2016 and later
versions. Supported in MS Exchange 2013.
domain-name
MS Exchange server fully qualified domain name.
string
Maximum
length: 79
http-auth-type
Authentication security type used for the HTTP
transport.
option
-ntlm
Option
Description
basic
Basic HTTP authentication.
ntlm
NTLM HTTP authentication.
ip
Server IPv4 address.
ipv4-address-any
Not
Specified
0.0.0.0
kdc-ip
<ipv4>
KDC IPv4 addresses for Kerberos authentication.
KDC IPv4 addresses for Kerberos authentication.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
2231
Fortinet Inc.

<!-- 来源页 2232 -->
Parameter
Description
Type
Size
Default
name
MS Exchange server entry name.
string
Maximum
length: 35
password
Password for the specified username.
password
Not
Specified
server-name
MS Exchange server hostname.
string
Maximum
length: 63
ssl-min-proto-version
Minimum SSL/TLS protocol version for HTTPS
transport (default is to follow system global
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
User name used to sign in to the server. Must
have proper permissions for service.
string
Maximum
length: 64
validate-server-certificate
Enable/disable exchange server certificate
validation.
option
-disable
Option
Description
disable
Disable validation of server certificate.
enable
Enable validation of server certificate.
config user external-identity-provider
Configure external identity provider.
config user external-identity-provider
Description: Configure external identity provider.
edit <name>
set group-attr-name {string}
set interface {string}
set interface-select-method [auto|sdwan|...]
set port {integer}
set server-identity-check [disable|enable]
FortiOS 8.0.0 CLI Reference
2232
Fortinet Inc.

<!-- 来源页 2233 -->
set source-ip {string}
set timeout {integer}
set type {option}
set url {string}
set user-attr-name {string}
set version [v1.0|beta]
set vrf-select {integer}
next
end
config user external-identity-provider
Parameter
Description
Type
Size
Default
group-attr-name
Group attribute name in authentication
query.
string
Maximum
length: 63
id
interface
Specify outgoing interface to reach
server.
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
name
External identity provider name.
string
Maximum
length: 35
port
External identity provider service port
number (0 to use default).
integer
Minimum
value: 0
Maximum
value:
65535
0
server-identity-check
Enable/disable server's identity check
against its certificate and subject
alternative name(s).
option
-enable
Option
Description
disable
Do not check server's identity against its certificate and subject
alternative name(s).
enable
Check server's identity against its certificate and subject alternative
name(s).
FortiOS 8.0.0 CLI Reference
2233
Fortinet Inc.

<!-- 来源页 2234 -->
Parameter
Description
Type
Size
Default
source-ip
Use this IPv4/v6 address to connect to the
external identity provider.
string
Maximum
length: 63
timeout
Connection timeout value in seconds
(default=5).
integer
Minimum
value: 1
Maximum
value: 60
5
type
External identity provider type.
option
-Option
Description
ms-graph
Microsoft Graph server.
url
External identity provider URL (e.g.
"https://example.com:8080/api/v1").
Read-only.
string
Maximum
length: 127
user-attr-name
User attribute name in authentication
query.
string
Maximum
length: 63
userPrincipalName
version
External identity API version.
option
-Option
Description
v1.0
MS Graph REST API v1.0.
beta
MS Graph REST API beta (debug build only).
vrf-select
VRF ID used for connection to server.
integer
Minimum
value: 0
Maximum
value: 511
0
config user fortitoken
Configure FortiToken.
config user fortitoken
Description: Configure FortiToken.
edit <serial-number>
set activation-code {string}
set activation-expire {integer}
set comments {var-string}
set license {string}
set os-ver {string}
set reg-id {string}
set seed {string}
set status [active|lock]
FortiOS 8.0.0 CLI Reference
2234
Fortinet Inc.

<!-- 来源页 2235 -->
next
end
config user fortitoken
Parameter
Description
Type
Size
Default
activation-code
Mobile token user activation-code.
string
Maximum
length: 32
activation-expire
Mobile token user activation-code expire time.
integer
Minimum value:
0 Maximum
value:
4294967295
0
comments
Comment.
var-string
Maximum
length: 255
license
Mobile token license.
string
Maximum
length: 31
os-ver
Device Mobile Version.
string
Maximum
length: 15
reg-id
Device Reg ID.
string
Maximum
length: 256
seed
Token seed.
string
Maximum
length: 208
serial-number
Serial number.
string
Maximum
length: 16
status
Status.
option
-active
Option
Description
active
Activate FortiToken.
lock
Lock FortiToken.
config user fsso
Configure Fortinet Single Sign On (FSSO) agents.
config user fsso
Description: Configure Fortinet Single Sign On (FSSO) agents.
edit <name>
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
FortiOS 8.0.0 CLI Reference
2235
Fortinet Inc.

<!-- 来源页 2236 -->
set group-poll-interval {integer}
set interface {string}
set interface-select-method [auto|sdwan|...]
set ldap-poll [enable|disable]
set ldap-poll-filter {string}
set ldap-poll-interval {integer}
set ldap-server {string}
set logon-timeout {integer}
set password {password}
set password2 {password}
set password3 {password}
set password4 {password}
set password5 {password}
set port {integer}
set port2 {integer}
set port3 {integer}
set port4 {integer}
set port5 {integer}
set server {string}
set server2 {string}
set server3 {string}
set server4 {string}
set server5 {string}
set sni {string}
set source-ip {ipv4-address}
set source-ip6 {ipv6-address}
set ssl [enable|disable]
set ssl-server-host-ip-check [enable|disable]
set ssl-trusted-cert {string}
set type [default|fortinac]
set user-info-server {string}
set uuid {uuid}
set vrf-select {integer}
next
end
config user fsso
Parameter
Description
Type
Size
Default
fabric-force-sync *
Enable/disable forced
synchronization of configuration
objects from the root FortiGate
unit to the downstream devices.
Configuration conflict check is
skipped.
option
-disable
FortiOS 8.0.0 CLI Reference
2236
Fortinet Inc.

<!-- 来源页 2237 -->
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
*
Security Fabric global object
setting.
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
group-poll-interval
Interval in minutes within to fetch
groups from FSSO server, or unset
to disable.
integer
Minimum
value: 1
Maximum
value: 2880
0
interface
Specify outgoing interface to
reach server.
string
Maximum
length: 15
interface-select-method
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
ldap-poll
Enable/disable automatic fetching
of groups from LDAP server.
option
-disable
FortiOS 8.0.0 CLI Reference
2237
Fortinet Inc.

<!-- 来源页 2238 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable automatic fetching of groups from LDAP server.
disable
Disable automatic fetching of groups from LDAP server.
ldap-poll-filter
Filter used to fetch groups.
string
Maximum
length:
2047
(objectCategory=group)
ldap-poll-interval
Interval in minutes within to fetch
groups from LDAP server.
integer
Minimum
value: 1
Maximum
value: 2880
180
ldap-server
LDAP server to get group
information.
string
Maximum
length: 35
logon-timeout
Interval in minutes to keep logons
after FSSO server down.
integer
Minimum
value: 1
Maximum
value: 2880
5
name
Name.
string
Maximum
length: 35
password
Password of the first FSSO
collector agent.
password
Not
Specified
password2
Password of the second FSSO
collector agent.
password
Not
Specified
password3
Password of the third FSSO
collector agent.
password
Not
Specified
password4
Password of the fourth FSSO
collector agent.
password
Not
Specified
password5
Password of the fifth FSSO
collector agent.
password
Not
Specified
port
Port of the first FSSO collector
agent.
integer
Minimum
value: 1
Maximum
value:
65535
8000
port2
Port of the second FSSO collector
agent.
integer
Minimum
value: 1
Maximum
value:
65535
8000
FortiOS 8.0.0 CLI Reference
2238
Fortinet Inc.

<!-- 来源页 2239 -->
Parameter
Description
Type
Size
Default
port3
Port of the third FSSO collector
agent.
integer
Minimum
value: 1
Maximum
value:
65535
8000
port4
Port of the fourth FSSO collector
agent.
integer
Minimum
value: 1
Maximum
value:
65535
8000
port5
Port of the fifth FSSO collector
agent.
integer
Minimum
value: 1
Maximum
value:
65535
8000
server
Domain name or IP address of the
first FSSO collector agent.
string
Maximum
length: 63
server2
Domain name or IP address of the
second FSSO collector agent.
string
Maximum
length: 63
server3
Domain name or IP address of the
third FSSO collector agent.
string
Maximum
length: 63
server4
Domain name or IP address of the
fourth FSSO collector agent.
string
Maximum
length: 63
server5
Domain name or IP address of the
fifth FSSO collector agent.
string
Maximum
length: 63
sni
Server Name Indication.
string
Maximum
length: 255
source-ip
Source IP for communications to
FSSO agent.
ipv4-address
Not
Specified
0.0.0.0
source-ip6
IPv6 source for communications to
FSSO agent.
ipv6-address
Not
Specified
::
ssl
Enable/disable use of SSL.
option
-disable
Option
Description
enable
Enable use of SSL.
disable
Disable use of SSL.
ssl-server-host-ip-check
Enable/disable server host/IP
verification.
option
-disable
FortiOS 8.0.0 CLI Reference
2239
Fortinet Inc.

<!-- 来源页 2240 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable server host/IP verification.
disable
Disable server host/IP verification.
ssl-trusted-cert
Trusted server certificate or CA
certificate.
string
Maximum
length: 79
type
Server type.
option
-default
Option
Description
default
All other unspecified types of servers.
fortinac
FortiNAC server.
user-info-server
LDAP server to get user
information.
string
Maximum
length: 35
uuid *
Universally Unique Identifier
(UUID; automatically assigned but
can be manually reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
vrf-select
VRF ID used for connection to
server.
integer
Minimum
value: 0
Maximum
value: 511
0
* This parameter may not exist in some models.
config user fsso-polling
Configure FSSO active directory servers for polling mode.
config user fsso-polling
Description: Configure FSSO active directory servers for polling mode.
edit <id>
config adgrp
Description: LDAP Group Info.
edit <name>
next
end
set default-domain {string}
set ldap-server {string}
set logon-history {integer}
set password {password}
set polling-frequency {integer}
set port {integer}
set server {string}
FortiOS 8.0.0 CLI Reference
2240
Fortinet Inc.

<!-- 来源页 2241 -->
set smb-ntlmv1-auth [enable|disable]
set smbv1 [enable|disable]
set status [enable|disable]
set user {string}
next
end
config user fsso-polling
Parameter
Description
Type
Size
Default
default-domain
Default domain managed by this Active
Directory server.
string
Maximum
length: 35
id
Active Directory server ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
ldap-server
LDAP server name used in LDAP connection
strings.
string
Maximum
length: 35
logon-history
Number of hours of logon history to keep, 0
means keep all history.
integer
Minimum value:
0 Maximum
value: 48
8
password
Password required to log into this Active
Directory server.
password
Not Specified
polling-frequency
Polling frequency (every 1 to 30 seconds).
integer
Minimum value:
1 Maximum
value: 30
10
port
Port to communicate with this Active Directory
server.
integer
Minimum value:
0 Maximum
value: 65535
0
server
Host name or IP address of the Active Directory
server.
string
Maximum
length: 63
smb-ntlmv1-auth
Enable/disable support of NTLMv1 for Samba
authentication.
option
-disable
Option
Description
enable
Enable support of NTLMv1 for Samba authentication.
disable
Disable support of NTLMv1 for Samba authentication.
smbv1
Enable/disable support of SMBv1 for Samba.
option
-disable
FortiOS 8.0.0 CLI Reference
2241
Fortinet Inc.

<!-- 来源页 2242 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable support of SMBv1 for Samba.
disable
Disable support of SMBv1 for Samba.
status
Enable/disable polling for the status of this
Active Directory server.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
user
User name required to log into this Active
Directory server.
string
Maximum
length: 35
config adgrp
Parameter
Description
Type
Size
Default
name
Name.
string
Maximum length:
511
config user group
Configure user groups.
config user group
Description: Configure user groups.
edit <name>
set auth-concurrent-override [enable|disable]
set auth-concurrent-value {integer}
set authtimeout {integer}
set company [optional|mandatory|...]
set email [disable|enable]
set expire {integer}
set expire-type [immediately|first-successful-login]
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set group-type [firewall|fsso-service|...]
config guest
Description: Guest User.
edit <id>
set comment {var-string}
set company {string}
FortiOS 8.0.0 CLI Reference
2242
Fortinet Inc.

<!-- 来源页 2243 -->
set email {string}
set expiration {user}
set mobile-phone {string}
set name {string}
set password {password}
set sponsor {string}
set user-id {string}
next
end
set http-digest-realm {string}
set id {integer}
config match
Description: Group matches.
edit <id>
set group-name {string}
set server-name {string}
next
end
set max-accounts {integer}
set member <name1>, <name2>, ...
set mobile-phone [disable|enable]
set multiple-guest-add [disable|enable]
set password [auto-generate|specify|...]
set scim-group-attr-type [display-name|external-id]
set scim-groups <name1>, <name2>, ...
set scim-user-attr-type [user-name|display-name|...]
set scim-users <name1>, <name2>, ...
set sms-custom-server {string}
set sms-server [fortiguard|custom]
set sponsor [optional|mandatory|...]
set sso-attribute-value {string}
set user-id [email|auto-generate|...]
set user-name [disable|enable]
set uuid {uuid}
next
end
config user group
Parameter
Description
Type
Size
Default
auth-concurrent-override
Enable/disable overriding the global
number of concurrent authentication
sessions for this user group.
option
-disable
Option
Description
enable
Enable auth-concurrent-override.
disable
Disable auth-concurrent-override.
FortiOS 8.0.0 CLI Reference
2243
Fortinet Inc.

<!-- 来源页 2244 -->
Parameter
Description
Type
Size
Default
auth-concurrent-value
Maximum number of concurrent
authenticated connections per user (0 -100).
integer
Minimum value:
0 Maximum
value: 100
0
authtimeout
Authentication timeout in minutes for
this user group. 0 to use the global user
setting auth-timeout.
integer
Minimum value:
0 Maximum
value: 43200
0
company
Set the action for the company guest
user field.
option
-optional
Option
Description
optional
Optional.
mandatory
Mandatory.
disabled
Disabled.
email
Enable/disable the guest user email
address field.
option
-enable
Option
Description
disable
Disable setting.
enable
Enable setting.
expire
Time in seconds before guest user
accounts expire (1 - 31536000).
integer
Minimum value:
1 Maximum
value:
31536000
14400
expire-type
Determine when the expiration
countdown begins.
option
-immediately
Option
Description
immediately
Immediately.
first-successful-login
First successful login.
fabric-force-sync *
Enable/disable forced synchronization of
configuration objects from the root
FortiGate unit to the downstream
devices. Configuration conflict check is
skipped.
option
-disable
FortiOS 8.0.0 CLI Reference
2244
Fortinet Inc.

<!-- 来源页 2245 -->
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
group-type
Set the group to be for firewall
authentication, FSSO, RSSO, SCIM, or
guest users.
option
-firewall
Option
Description
firewall
Firewall.
fsso-service
Fortinet Single Sign-On Service.
rsso
RADIUS based Single Sign-On Service.
guest
Guest.
scim
SCIM based Authorization.
http-digest-realm
Realm attribute for MD5-digest
authentication.
string
Maximum
length: 35
id
Group ID. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
FortiOS 8.0.0 CLI Reference
2245
Fortinet Inc.

<!-- 来源页 2246 -->
Parameter
Description
Type
Size
Default
max-accounts
Maximum number of guest accounts that
can be created for this group (0 means
unlimited).
integer
Minimum value:
0 Maximum
value: 1024 **
0
member
<name>
Names of users, peers, LDAP severs,
RADIUS servers, SCIM client or external
idp servers to add to the user group.
Group member name.
string
Maximum
length: 511
mobile-phone
Enable/disable the guest user mobile
phone number field.
option
-disable
Option
Description
disable
Disable setting.
enable
Enable setting.
multiple-guest-add
Enable/disable addition of multiple
guests.
option
-disable
Option
Description
disable
Disable setting.
enable
Enable setting.
name
Group name.
string
Maximum
length: 35
password
Guest user password type.
option
-auto-generate
Option
Description
auto-generate
Automatically generate.
specify
Specify.
disable
Disable.
scim-group-attr-type *
Group attribute type used to match
SCIM groups (default = display-name).
option
-display-name
Option
Description
display-name
Display name.
external-id
External ID.
scim-groups
<name> *
Names of SCIM groups.
Names of SCIM groups.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
2246
Fortinet Inc.

<!-- 来源页 2247 -->
Parameter
Description
Type
Size
Default
scim-user-attr-type *
User attribute type used to match SCIM
users (default = user-name).
option
-user-name
Option
Description
user-name
User name.
display-name
Display name.
external-id
External ID.
email
Email.
scim-users
<name> *
Names of SCIM users.
Names of SCIM users.
string
Maximum
length: 79
sms-custom-server
SMS server.
string
Maximum
length: 35
sms-server
Send SMS through FortiGuard or other
external server.
option
-fortiguard
Option
Description
fortiguard
Send SMS by FortiGuard.
custom
Send SMS by custom server.
sponsor
Set the action for the sponsor guest user
field.
option
-optional
Option
Description
optional
Optional.
mandatory
Mandatory.
disabled
Disabled.
sso-attribute-value
RADIUS attribute value.
string
Maximum
length: 511
user-id
Guest user ID type.
option
-email
Option
Description
email
Email address.
auto-generate
Automatically generate.
specify
Specify.
user-name
Enable/disable the guest user name
entry.
option
-disable
FortiOS 8.0.0 CLI Reference
2247
Fortinet Inc.

<!-- 来源页 2248 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable setting.
enable
Enable setting.
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
** Values may differ between models.
config guest
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
company
Set the action for the company guest user
field.
string
Maximum
length: 35
email
Email.
string
Maximum
length: 64
expiration
Expire time.
user
Not Specified
id
Guest ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
mobile-phone
Mobile phone.
string
Maximum
length: 35
name
Guest name.
string
Maximum
length: 64
password
Guest password.
password
Not Specified
sponsor
Set the action for the sponsor guest user field.
string
Maximum
length: 35
user-id
Guest ID.
string
Maximum
length: 64
FortiOS 8.0.0 CLI Reference
2248
Fortinet Inc.

<!-- 来源页 2249 -->
config match
Parameter
Description
Type
Size
Default
group-name
Name of matching user or group on remote
authentication server or SCIM.
string
Maximum
length: 511
id
ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
server-name
Name of remote auth server.
string
Maximum
length: 35
config user krb-keytab
Configure Kerberos keytab entries.
config user krb-keytab
Description: Configure Kerberos keytab entries.
edit <name>
set keytab {user}
set ldap-server <name1>, <name2>, ...
set pac-data [enable|disable]
set principal {string}
next
end
config user krb-keytab
Parameter
Description
Type
Size
Default
keytab
Base64 coded keytab file containing a pre-shared
key.
user **
Not
Specified **
ldap-server
<name>
LDAP server name(s).
LDAP server name.
string
Maximum
length: 79
name
Kerberos keytab entry name.
string
Maximum
length: 35
pac-data
Enable/disable parsing PAC data in the ticket.
option
-enable
Option
Description
enable
Enable parsing PAC data in the ticket.
disable
Disable parsing PAC data in the ticket.
FortiOS 8.0.0 CLI Reference
2249
Fortinet Inc.

<!-- 来源页 2250 -->
Parameter
Description
Type
Size
Default
principal
Kerberos service principal. For example,
HTTP/myfgt.example.com@example.com.
string
Maximum
length: 511
** Values may differ between models.
config user ldap
Configure LDAP server entries.
config user ldap
Description: Configure LDAP server entries.
edit <name>
set account-key-cert-field [othername|rfc822name|...]
set account-key-filter {string}
set account-key-processing [same|strip]
set antiphish [enable|disable]
set ca-cert {string}
set client-cert {string}
set client-cert-auth [enable|disable]
set cnid {string}
set dn {string}
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set group-filter {string}
set group-member-check [user-attr|group-object|...]
set group-object-filter {string}
set group-search-base {string}
set interface {string}
set interface-select-method [auto|sdwan|...]
set member-attr {string}
set obtain-user-info [enable|disable]
set password {password}
set password-attr {string}
set password-expiry-warning [enable|disable]
set password-renewal [enable|disable]
set port {integer}
set search-type {option1}, {option2}, ...
set secondary-server {string}
set secure [disable|starttls|...]
set server {string}
set server-identity-check [enable|disable]
set source-ip {string}
set source-ip-interface {string}
set source-port {integer}
set ssl-min-proto-version [default|SSLv3|...]
set status-ttl {integer}
set tertiary-server {string}
FortiOS 8.0.0 CLI Reference
2250
Fortinet Inc.

<!-- 来源页 2251 -->
set two-factor [disable|fortitoken-cloud]
set two-factor-authentication [fortitoken|email|...]
set two-factor-filter {string}
set two-factor-notification [email|sms]
set type [simple|anonymous|...]
set user-info-exchange-server {string}
set username {string}
set uuid {uuid}
set vrf-select {integer}
next
end
config user ldap
Parameter
Description
Type
Size
Default
account-key-cert-field
Define subject
identity field in
certificate for
user access
right checking.
option
-othername
Option
Description
othername
Other name in SAN.
rfc822name
RFC822 email address in SAN.
dnsname
DNS name in SAN.
cn
CN in subject.
account-key-filter
Account key
filter, using the
UPN as the
search filter.
string
Maximum
length:
2047
(&(userPrincipalName=%s)(!
(UserAccountControl:1.2.840.113556.1.4.803:=
2)))
account-key-processing
Account key
processing
operation. The
FortiGate will
keep either the
whole domain
or strip the
domain from
the subject
identity.
option
-same
FortiOS 8.0.0 CLI Reference
2251
Fortinet Inc.

<!-- 来源页 2252 -->
Parameter
Description
Type
Size
Default
Option
Description
same
Same as subject identity field.
strip
Strip domain string from subject identity field.
antiphish
Enable/disable
AntiPhishing
credential
backend.
option
-disable
Option
Description
enable
Enable AntiPhishing credential backend.
disable
Disable AntiPhishing credential backend.
ca-cert
CA certificate
name.
string
Maximum
length: 79
client-cert
Client
certificate
name.
string
Maximum
length: 79
client-cert-auth
Enable/disable
using client
certificate for
TLS
authentication.
option
-disable
Option
Description
enable
Enable using client certificate for TLS authentication.
disable
Disable using client certificate for TLS authentication.
cnid
Common name
identifier for the
LDAP server.
The common
name identifier
for most LDAP
servers is "cn".
string
Maximum
length: 20
cn
dn
Distinguished
name used to
look up entries
on the LDAP
server.
string
Maximum
length:
511
FortiOS 8.0.0 CLI Reference
2252
Fortinet Inc.

<!-- 来源页 2253 -->
Parameter
Description
Type
Size
Default
fabric-force-sync *
Enable/disable
forced
synchronization
of configuration
objects from
the root
FortiGate unit to
the
downstream
devices.
Configuration
conflict check is
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
Security Fabric
global object
setting.
option
-disable
Option
Description
enable
Object is set as a security fabric-wide global object.
disable
Object is local to this security fabric member.
fabric-object-source *
Source of truth
for fabric
object.
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
group-filter
Filter used for
group
matching.
string
Maximum
length:
2047
group-member-check
Group member
checking
methods.
option
-user-attr
FortiOS 8.0.0 CLI Reference
2253
Fortinet Inc.

<!-- 来源页 2254 -->
Parameter
Description
Type
Size
Default
Option
Description
user-attr
User attribute checking.
group-object
Group object checking.
posix-group-object
POSIX group object checking.
group-object-filter
Filter used for
group
searching.
string
Maximum
length:
2047
(&(objectcategory=group)(member=*))
group-search-base
Search base
used for group
searching.
string
Maximum
length:
511
interface
Specify
outgoing
interface to
reach server.
string
Maximum
length: 15
interface-select-method
Specify how to
select outgoing
interface to
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
member-attr
Name of
attribute from
which to get
group
membership.
string
Maximum
length: 63
memberOf
name
LDAP server
entry name.
string
Maximum
length: 35
obtain-user-info
Enable/disable
obtaining of
user
information.
option
-enable
FortiOS 8.0.0 CLI Reference
2254
Fortinet Inc.

<!-- 来源页 2255 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable obtaining of user information.
disable
Disable obtaining of user information.
password
Password for
initial binding.
password
Not
Specified
password-attr
Name of
attribute to get
password hash.
string
Maximum
length: 35
userPassword
password-expiry-warning
Enable/disable
password
expiry
warnings.
option
-disable
Option
Description
enable
Enable password expiry warnings.
disable
Disable password expiry warnings.
password-renewal
Enable/disable
online
password
renewal.
option
-disable
Option
Description
enable
Enable online password renewal.
disable
Disable online password renewal.
port
Port to be used
for
communication
with the LDAP
server (default
= 389).
integer
Minimum
value: 1
Maximum
value:
65535
389
search-type
Search type.
option
-Option
Description
recursive
Recursively retrieve the user-group chain information of a user in a
particular Microsoft AD domain.
FortiOS 8.0.0 CLI Reference
2255
Fortinet Inc.

<!-- 来源页 2256 -->
Parameter
Description
Type
Size
Default
secondary-server
Secondary
LDAP server CN
domain name or
IP.
string
Maximum
length: 63
secure
Port to be used
for
authentication.
option
-disable
Option
Description
disable
No SSL.
starttls
Use StartTLS.
ldaps
Use LDAPS.
server
LDAP server CN
domain name or
IP.
string
Maximum
length: 63
server-identity-check
Enable/disable
LDAP server
identity check
(verify server
domain name/IP
address against
the server
certificate).
option
-enable
Option
Description
enable
Enable server identity check.
disable
Disable server identity check.
source-ip
FortiGate IP
address to be
used for
communication
with the LDAP
server.
string
Maximum
length: 63
source-ip-interface
Source
interface for
communication
with the LDAP
server.
string
Maximum
length: 15
FortiOS 8.0.0 CLI Reference
2256
Fortinet Inc.

<!-- 来源页 2257 -->
Parameter
Description
Type
Size
Default
source-port
Source port to
be used for
communication
with the LDAP
server.
integer
Minimum
value: 0
Maximum
value:
65535
0
ssl-min-proto-version
Minimum
supported
protocol version
for SSL/TLS
connections
(default is to
follow system
global setting).
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
status-ttl
Time for which
server
reachability is
cached so that
when a server is
unreachable, it
will not be
retried for at
least this period
of time (0 =
cache disabled,
default = 300).
integer
Minimum
value: 0
Maximum
value: 600
300
tertiary-server
Tertiary LDAP
server CN
domain name or
IP.
string
Maximum
length: 63
two-factor
Enable/disable
two-factor
authentication.
option
-disable
FortiOS 8.0.0 CLI Reference
2257
Fortinet Inc.

<!-- 来源页 2258 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
disable two-factor authentication.
fortitoken-cloud
FortiToken Cloud Service.
two-factor-authentication
Authentication
method by
FortiToken
Cloud.
option
-Option
Description
fortitoken
FortiToken authentication.
email
Email one time password.
sms
SMS one time password.
two-factor-filter
Filter used to
synchronize
users to
FortiToken
Cloud.
string
Maximum
length:
2047
two-factor-notification
Notification
method for user
activation by
FortiToken
Cloud.
option
-Option
Description
email
Email notification for activation code.
sms
SMS notification for activation code.
type
Authentication
type for LDAP
searches.
option
-simple
Option
Description
simple
Simple password authentication without search.
anonymous
Bind using anonymous user search.
regular
Bind using username/password and then search.
FortiOS 8.0.0 CLI Reference
2258
Fortinet Inc.

<!-- 来源页 2259 -->
Parameter
Description
Type
Size
Default
user-info-exchange-server
MS Exchange
server from
which to fetch
user
information.
string
Maximum
length: 35
username
Username (full
DN) for initial
binding.
string
Maximum
length:
511
uuid *
Universally
Unique
Identifier (UUID;
automatically
assigned but
can be manually
reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
vrf-select
VRF ID used for
connection to
server.
integer
Minimum
value: 0
Maximum
value: 511
0
* This parameter may not exist in some models.
config user local
Configure local users.
config user local
Description: Configure local users.
edit <name>
set auth-concurrent-override [enable|disable]
set auth-concurrent-value {integer}
set authtimeout {integer}
set email-to {string}
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set fortitoken {string}
set id {integer}
set ldap-server {string}
set passwd {password}
set passwd-policy {string}
set passwd-time {user}
set ppk-identity {string}
set ppk-secret {password-3}
set qkd-profile {string}
set radius-server {string}
FortiOS 8.0.0 CLI Reference
2259
Fortinet Inc.

<!-- 来源页 2260 -->
set saml-server {string}
set sms-custom-server {string}
set sms-phone {string}
set sms-server [fortiguard|custom]
set status [enable|disable]
set tacacs+-server {string}
set two-factor [disable|fortitoken|...]
set two-factor-authentication [fortitoken|email|...]
set two-factor-notification [email|sms]
set type [password|radius|...]
set username-sensitivity [disable|enable]
set uuid {uuid}
set workstation {string}
next
end
config user local
Parameter
Description
Type
Size
Default
auth-concurrent-override
Enable/disable overriding the
policy-auth-concurrent under
config system global.
option
-disable
Option
Description
enable
Enable auth-concurrent-override.
disable
Disable auth-concurrent-override.
auth-concurrent-value
Maximum number of concurrent
logins permitted from the same
user.
integer
Minimum value:
0 Maximum
value: 100
0
authtimeout
Time in minutes before the
authentication timeout for a user is
reached.
integer
Minimum value:
0 Maximum
value: 1440
0
email-to
Two-factor recipient's email
address.
string
Maximum
length: 63
fabric-force-sync *
Enable/disable forced
synchronization of configuration
objects from the root FortiGate unit
to the downstream devices.
Configuration conflict check is
skipped.
option
-disable
FortiOS 8.0.0 CLI Reference
2260
Fortinet Inc.

<!-- 来源页 2261 -->
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
fabric-object *
Security Fabric global object
setting.
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
fortitoken
Two-factor recipient's FortiToken
serial number.
string
Maximum
length: 16
id
User ID. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
ldap-server
Name of LDAP server with which
the user must authenticate.
string
Maximum
length: 35
name
Local user name.
string
Maximum
length: 64
passwd
User's password.
password
Not Specified
passwd-policy
Password policy to apply to this
user, as defined in config user
password-policy.
string
Maximum
length: 35
passwd-time
Time of the last password update.
user
Not Specified
ppk-identity
IKEv2 Postquantum Preshared Key
Identity.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
2261
Fortinet Inc.

<!-- 来源页 2262 -->
Parameter
Description
Type
Size
Default
ppk-secret
IKEv2 Postquantum Preshared Key
(ASCII string or hexadecimal
encoded with a leading 0x).
password-3
Not Specified
qkd-profile
Quantum Key Distribution (QKD)
profile.
string
Maximum
length: 35
radius-server
Name of RADIUS server with which
the user must authenticate.
string
Maximum
length: 35
saml-server
Name of SAML server with which
the user must authenticate.
string
Maximum
length: 35
sms-custom-server
Two-factor recipient's SMS server.
string
Maximum
length: 35
sms-phone
Two-factor recipient's mobile
phone number.
string
Maximum
length: 15
sms-server
Send SMS through FortiGuard or
other external server.
option
-fortiguard
Option
Description
fortiguard
Send SMS by FortiGuard.
custom
Send SMS by custom server.
status
Enable/disable allowing the local
user to authenticate with the
FortiGate unit.
option
-enable
Option
Description
enable
Enable user.
disable
Disable user.
tacacs+-server
Name of TACACS+ server with
which the user must authenticate.
string
Maximum
length: 35
two-factor
Enable/disable two-factor
authentication.
option
-disable
Option
Description
disable
disable
fortitoken
FortiToken
fortitoken-cloud
FortiToken Cloud Service.
email
Email authentication code.
FortiOS 8.0.0 CLI Reference
2262
Fortinet Inc.

<!-- 来源页 2263 -->
Parameter
Description
Type
Size
Default
Option
Description
sms
SMS authentication code.
two-factor-authentication
Authentication method by
FortiToken Cloud.
option
-Option
Description
fortitoken
FortiToken authentication.
email
Email one time password.
sms
SMS one time password.
two-factor-notification
Notification method for user
activation by FortiToken Cloud.
option
-Option
Description
email
Email notification for activation code.
sms
SMS notification for activation code.
type
Authentication method.
option
-password
Option
Description
password
Password authentication.
radius
RADIUS server authentication.
tacacs+
TACACS+ server authentication.
ldap
LDAP server authentication.
saml
SAML server authentication.
username-sensitivity
Enable/disable case and accent
sensitivity when performing
username matching (accents are
stripped and case is ignored when
disabled).
option
-disable **
Option
Description
disable
Ignore case and accents. Username at prompt not required to match
case or accents.
enable
Do not ignore case and accents. Username at prompt must be an
exact match.
FortiOS 8.0.0 CLI Reference
2263
Fortinet Inc.

<!-- 来源页 2264 -->
Parameter
Description
Type
Size
Default
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not Specified
00000000-0000-0000-0000-000000000000
workstation
Name of the remote user
workstation, if you want to limit the
user to authenticate only from a
particular workstation.
string
Maximum
length: 35
* This parameter may not exist in some models.
** Values may differ between models.
config user nac-policy
Configure NAC policy matching pattern to identify matching NAC devices.
config user nac-policy
Description: Configure NAC policy matching pattern to identify matching NAC devices.
edit <name>
set category [device|firewall-user|...]
set description {string}
set ems-tag {string}
set family {string}
set firewall-address {string}
set fortivoice-tag {string}
set host {string}
set hw-vendor {string}
set hw-version {string}
set mac {string}
set match-period {integer}
set match-remove [default|link-down]
set match-type [dynamic|override]
set os {string}
set port-setting-override [disable|enable]
set qos-policy {string}
set severity <severity-num1>, <severity-num2>, ...
set src {string}
set ssid-policy {string}
set status [enable|disable]
set sw-version {string}
set switch-fortilink {string}
set switch-group <name1>, <name2>, ...
set switch-mac-policy {string}
set type {string}
set user {string}
set user-group {string}
next
end
FortiOS 8.0.0 CLI Reference
2264
Fortinet Inc.

<!-- 来源页 2265 -->
config user nac-policy
Parameter
Description
Type
Size
Default
category
Category of NAC policy.
option
-device
Option
Description
device
Device category.
firewall-user
Firewall user category.
ems-tag
EMS Tag category.
fortivoice-tag
FortiVoice Tag category.
vulnerability
Vulnerability category.
description
Description for the NAC policy matching pattern.
string
Maximum
length: 63
ems-tag
NAC policy matching EMS tag.
string
Maximum
length: 79
family
NAC policy matching family.
string
Maximum
length: 31
firewall-address
Dynamic firewall address to associate MAC which
match this policy.
string
Maximum
length: 79
fortivoice-tag
NAC policy matching FortiVoice tag.
string
Maximum
length: 79
host
NAC policy matching host.
string
Maximum
length: 64
hw-vendor
NAC policy matching hardware vendor.
string
Maximum
length: 15
hw-version
NAC policy matching hardware version.
string
Maximum
length: 15
mac
NAC policy matching MAC address.
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
FortiOS 8.0.0 CLI Reference
2265
Fortinet Inc.

<!-- 来源页 2266 -->
Parameter
Description
Type
Size
Default
Option
Description
default
Remove the matched override devices based on the match period.
link-down
Remove the matched override devices based on switch port link down
event.
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
NAC policy name.
string
Maximum
length: 63
os
NAC policy matching operating system.
string
Maximum
length: 31
port-setting-override *
Enable/disable port setting action on the NAC
policy.
option
-disable
Option
Description
disable
Disable port setting action on the nac-policy.
enable
Enable port setting action and apply if matched device is the only device
on the port.
qos-policy *
Switch Port qos-policy action to be applied on the
matched NAC policy.
string
Maximum
length: 63
severity
<severity-num>
NAC policy matching devices vulnerability severity
lists.
Enter multiple severity levels, where 0 = Info, 1 =
Low, ..., 4 = Critical
integer
Minimum
value: 0
Maximum
value: 4
src
NAC policy matching source.
string
Maximum
length: 15
ssid-policy
SSID policy to be applied on the matched NAC
policy.
string
Maximum
length: 35
status
Enable/disable NAC policy.
option
-enable
Option
Description
enable
Enable NAC policy.
disable
Disable NAC policy.
FortiOS 8.0.0 CLI Reference
2266
Fortinet Inc.

<!-- 来源页 2267 -->
Parameter
Description
Type
Size
Default
sw-version
NAC policy matching software version.
string
Maximum
length: 15
switch-fortilink
FortiLink interface for which this NAC policy
belongs to.
string
Maximum
length: 15
switch-group
<name>
List of managed FortiSwitch groups on which NAC
policy can be applied.
Managed FortiSwitch group name from available
options.
string
Maximum
length: 79
switch-mac-policy
Switch MAC policy action to be applied on the
matched NAC policy.
string
Maximum
length: 63
type
NAC policy matching type.
string
Maximum
length: 15
user
NAC policy matching user.
string
Maximum
length: 64
user-group
NAC policy matching user group.
string
Maximum
length: 35
* This parameter may not exist in some models.
** Values may differ between models.
FortiOS 8.0.0 CLI Reference
2267
Fortinet Inc.

<!-- 来源页 2268 -->
config user oidc
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
OpenID Connect server entry configuration.
config user oidc
Description: OpenID Connect server entry configuration.
edit <name>
set authorization-url {string}
set client-id {string}
set client-secret {password}
set clock-tolerance {integer}
set discovery-url {string}
set domain-hint {string}
set issuer {string}
set jwks-uri {string}
set ldap-server <name1>, <name2>, ...
set token-url {string}
set type [discovery|manual]
set user-attr-name [email|sub|...]
set user-regex {string}
set verify-issuer [enable|disable]
FortiOS 8.0.0 CLI Reference
2268
Fortinet Inc.

<!-- 来源页 2269 -->
next
end
config user oidc
Parameter
Description
Type
Size
Default
authorization-url
OpenID Connect server authorization URL.
string
Maximum
length: 255
client-id
OpenID Connect server client ID.
string
Maximum
length: 127
client-secret
OpenID Connect server client secret.
password
Not
Specified
clock-tolerance
Clock skew tolerance in seconds (0 - 300,
default = 15, 0 = no tolerance).
integer
Minimum
value: 0
Maximum
value: 300
15
discovery-url
OpenID Connect server discovery URL.
string
Maximum
length: 255
domain-hint
Domain Hint.
string
Maximum
length: 255
issuer
OpenID Connect server issuer.
string
Maximum
length: 255
jwks-uri
URL of the OP's JWK Set document.
string
Maximum
length: 255
ldap-server
<name>
LDAP server name(s).
LDAP server name.
string
Maximum
length: 79
name
OpenID Connect server entry name.
string
Maximum
length: 35
token-url
OpenID Connect server token URL.
string
Maximum
length: 255
type
Type of OpenID Connect config.
option
-discovery
Option
Description
discovery
Use discovery URL to get configuration.
manual
Use manual configuration.
user-attr-name
Which field in ID token is username.
option
-email
FortiOS 8.0.0 CLI Reference
2269
Fortinet Inc.

<!-- 来源页 2270 -->
Parameter
Description
Type
Size
Default
Option
Description
email
Use email in ID token as username.
sub
Use sub in ID token as username.
preferred_
username
Use preferred_username in ID token as username.
user-regex
username must match this regex (case
insensitive).
string
Maximum
length: 255
verify-issuer
Verify issuer in ID token (default = enable).
option
-enable
Option
Description
enable
Enable verification of issuer in ID token (default).
disable
Disable verification of issuer in ID token.
config user password-policy
Configure user password policy.
config user password-policy
Description: Configure user password policy.
edit <name>
set expire-days {integer}
set expire-status [enable|disable]
set expired-password-renewal [enable|disable]
set min-change-characters {integer}
set min-lower-case-letter {integer}
set min-non-alphanumeric {integer}
set min-number {integer}
set min-upper-case-letter {integer}
set minimum-length {integer}
set reuse-password [enable|disable]
set reuse-password-limit {integer}
set warn-days {integer}
next
end
FortiOS 8.0.0 CLI Reference
2270
Fortinet Inc.

<!-- 来源页 2271 -->
config user password-policy
Parameter
Description
Type
Size
Default
expire-days
Time in days before the user's password expires.
integer
Minimum
value: 0
Maximum
value: 999
180
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
expired-password-renewal
Enable/disable renewal of a password that
already is expired.
option
-disable
Option
Description
enable
Enable renewal of a password that already is expired.
disable
Disable renewal of a password that already is expired.
min-change-characters
Minimum number of unique characters in new
password which do not exist in old password (0 -128, default = 0. This attribute overrides reuse-password if both are enabled).
integer
Minimum
value: 0
Maximum
value: 128
0
min-lower-case-letter
Minimum number of lowercase characters in
password (0 - 128, default = 0).
integer
Minimum
value: 0
Maximum
value: 128
0
min-non-alphanumeric
Minimum number of non-alphanumeric
characters in password (0 - 128, default = 0).
integer
Minimum
value: 0
Maximum
value: 128
0
min-number
Minimum number of numeric characters in
password (0 - 128, default = 0).
integer
Minimum
value: 0
Maximum
value: 128
0
min-upper-case-letter
Minimum number of uppercase characters in
password (0 - 128, default = 0).
integer
Minimum
value: 0
Maximum
value: 128
0
FortiOS 8.0.0 CLI Reference
2271
Fortinet Inc.

<!-- 来源页 2272 -->
Parameter
Description
Type
Size
Default
minimum-length
Minimum password length (8 - 128, default = 8).
integer
Minimum
value: 8
Maximum
value: 128
8
name
Password policy name.
string
Maximum
length: 35
reuse-password
Enable/disable reuse of password. If both reuse-password and min-change-characters are
enabled, min-change-characters overrides.
option
-enable
Option
Description
enable
Users are allowed to reuse the same password up to a limit.
disable
Users must create a new password.
reuse-password-limit
Number of times passwords can be reused (0 -20, default = 0. If set to 0, can reuse password an
unlimited number of times.).
integer
Minimum
value: 0
Maximum
value: 20
0
warn-days
Time in days before a password expiration
warning message is displayed to the user upon
login.
integer
Minimum
value: 0
Maximum
value: 30
15
config user peer
Configure peer users.
config user peer
Description: Configure peer users.
edit <name>
set ca {string}
set checkemail {string}
set checkhost {string}
set checkip {user}
set cn {string}
set cn-type [string|email|...]
set mandatory-ca-verify [enable|disable]
set mfa-mode [none|password|...]
set mfa-password {password}
set mfa-server {string}
set mfa-username {string}
set ocsp-override-server {string}
set passwd {password}
set subject {string}
FortiOS 8.0.0 CLI Reference
2272
Fortinet Inc.

<!-- 来源页 2273 -->
set two-factor [enable|disable]
next
end
config user peer
Parameter
Description
Type
Size
Default
ca
Name of the CA certificate.
string
Maximum
length: 127
checkemail *
Peer certificate email address. Check passes if
the certificate SAN matches the specified email
address. If the certificate has no email-type SAN,
the emailAddress DN in the Subject is checked
instead.
string
Maximum
length: 127
checkhost *
Peer certificate hostname. Check passes if the
certificate SAN matches the specified hostname,
and the client IP matches the hostname's resolved
IP. If the certificate has no DNS-type SAN, CN is
checked instead.
string
Maximum
length: 255
checkip *
Peer certificate IP address. Check passes if the
certificate SAN and the client IP both match the
specified IP.
user
Not
Specified
cn
Peer certificate common name.
string
Maximum
length: 255
cn-type *
Peer certificate common name type.
option
-string
Option
Description
string
Normal string.
email
Email address.
FQDN
Fully Qualified Domain Name.
ipv4
IPv4 address.
ipv6
IPv6 address.
mandatory-ca-verify
Determine what happens to the peer if the CA
certificate is not installed. Disable to automatically
consider the peer certificate as valid.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
2273
Fortinet Inc.

<!-- 来源页 2274 -->
Parameter
Description
Type
Size
Default
mfa-mode
MFA mode for remote peer
authentication/authorization.
option
-none
Option
Description
none
None.
password
Specified username/password.
subject-identity
Subject identity extracted from certificate.
mfa-password
Unified password for remote authentication. This
field may be left empty when RADIUS
authentication is used, in which case the
FortiGate will use the RADIUS username as a
password.
password
Not
Specified
mfa-server
Name of a remote authenticator. Performs client
access right check.
string
Maximum
length: 35
mfa-username
Unified username for remote authentication.
string
Maximum
length: 35
name
Peer name.
string
Maximum
length: 35
ocsp-override-server
Online Certificate Status Protocol (OCSP) server
for certificate retrieval.
string
Maximum
length: 35
passwd
Peer's password used for two-factor
authentication.
password
Not
Specified
subject
Peer certificate name constraints.
string
Maximum
length: 255
two-factor
Enable/disable two-factor authentication,
applying certificate and password-based
authentication.
option
-disable
Option
Description
enable
Enable 2-factor authentication.
disable
Disable 2-factor authentication.
* This parameter may not exist in some models.
config user peergrp
Configure peer groups.
FortiOS 8.0.0 CLI Reference
2274
Fortinet Inc.

<!-- 来源页 2275 -->
config user peergrp
Description: Configure peer groups.
edit <name>
set member <name1>, <name2>, ...
next
end
config user peergrp
Parameter
Description
Type
Size
Default
member
<name>
Peer group members.
Peer group member name.
string
Maximum
length: 35
name
Peer group name.
string
Maximum
length: 35
config user pop3
POP3 server entry configuration.
config user pop3
Description: POP3 server entry configuration.
edit <name>
set port {integer}
set secure [none|starttls|...]
set server {string}
set ssl-min-proto-version [default|SSLv3|...]
next
end
config user pop3
Parameter
Description
Type
Size
Default
name
POP3 server entry name.
string
Maximum
length: 35
port
POP3 service port number.
integer
Minimum
value: 0
Maximum
value:
65535
0
secure
SSL connection.
option
-starttls
FortiOS 8.0.0 CLI Reference
2275
Fortinet Inc.

<!-- 来源页 2276 -->
Parameter
Description
Type
Size
Default
Option
Description
none
None.
starttls
Use StartTLS.
pop3s
Use POP3 over SSL.
server
Server domain name or IP address.
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
config user quarantine
Configure quarantine support.
config user quarantine
Description: Configure quarantine support.
set firewall-groups {string}
set quarantine [enable|disable]
config targets
Description: Quarantine entry to hold multiple MACs.
edit <entry>
set description {string}
config macs
Description: Quarantine MACs.
edit <mac>
set description {string}
set drop [disable|enable]
set parent {string}
next
end
next
end
FortiOS 8.0.0 CLI Reference
2276
Fortinet Inc.

<!-- 来源页 2277 -->
set traffic-policy {string}
end
config user quarantine
Parameter
Description
Type
Size
Default
firewall-groups
Firewall address group which includes all
quarantine MAC address.
string
Maximum
length: 79
quarantine
Enable/disable quarantine.
option
-enable
Option
Description
enable
Enable quarantine.
disable
Disable quarantine.
traffic-policy
Traffic policy for quarantined MACs.
string
Maximum
length: 63
config targets
Parameter
Description
Type
Size
Default
description
Description for the quarantine entry.
string
Maximum
length: 63
entry
Quarantine entry name.
string
Maximum
length: 63
config macs
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
drop
Enable/disable dropping of quarantined
device traffic.
option
-disable
Option
Description
disable
Sends quarantined device traffic to FortiGate.
enable
Blocks quarantined device traffic to FortiGate.
mac
Quarantine MAC.
mac-address
Not
Specified
00:00:00:00:00:00
parent
Parent entry name. Read-only.
string
Maximum
length: 63
FortiOS 8.0.0 CLI Reference
2277
Fortinet Inc.

<!-- 来源页 2278 -->
config user radius
Configure RADIUS server entries.
config user radius
Description: Configure RADIUS server entries.
edit <name>
set account-key-cert-field [othername|rfc822name|...]
set account-key-processing [same|strip]
config accounting-server
Description: Additional accounting servers.
edit <id>
set interface {string}
set interface-select-method [auto|sdwan|...]
set port {integer}
set secret {password}
set server {string}
set source-ip {string}
set status [enable|disable]
set vrf-select {integer}
next
end
set acct-all-servers [enable|disable]
set acct-interim-interval {integer}
set all-usergroup [disable|enable]
set auth-type [auto|ms_chap_v2|...]
set ca-cert {string}
set call-station-id-type [legacy|IP|...]
set class <name1>, <name2>, ...
set client-cert {string}
set delimiter [plus|comma]
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set group-override-attr-type [filter-Id|class]
set h3c-compatibility [enable|disable]
set interface {string}
set interface-select-method [auto|sdwan|...]
set mac-case [uppercase|lowercase]
set mac-password-delimiter [hyphen|single-hyphen|...]
set mac-username-delimiter [hyphen|single-hyphen|...]
set nas-id {string}
set nas-id-type [legacy|custom|...]
set nas-ip {ipv4-address}
set password-encoding [auto|ISO-8859-1]
set password-renewal [enable|disable]
set radius-coa [enable|disable]
set radius-port {integer}
set require-message-authenticator [enable|disable]
set rsso [enable|disable]
set rsso-context-timeout {integer}
FortiOS 8.0.0 CLI Reference
2278
Fortinet Inc.

<!-- 来源页 2279 -->
set rsso-endpoint-attribute [User-Name|NAS-IP-Address|...]
set rsso-endpoint-block-attribute [User-Name|NAS-IP-Address|...]
set rsso-ep-one-ip-only [enable|disable]
set rsso-flush-ip-session [enable|disable]
set rsso-log-flags {option1}, {option2}, ...
set rsso-log-period {integer}
set rsso-radius-response [enable|disable]
set rsso-radius-server-port {integer}
set rsso-secret {password}
set rsso-validate-request-secret [enable|disable]
set secondary-secret {password}
set secondary-server {string}
set secret {password}
set server {string}
set server-identity-check [enable|disable]
set source-ip {string}
set source-ip-interface {string}
set sso-attribute [User-Name|NAS-IP-Address|...]
set sso-attribute-key {string}
set sso-attribute-value-override [enable|disable]
set status-ttl {integer}
set switch-controller-acct-fast-framedip-detect {integer}
set switch-controller-nas-ip-dynamic [enable|disable]
set switch-controller-service-type {option1}, {option2}, ...
set tertiary-secret {password}
set tertiary-server {string}
set timeout {integer}
set tls-min-proto-version [default|SSLv3|...]
set transport-protocol [udp|tcp|...]
set use-management-vdom [enable|disable]
set username-case-sensitive [enable|disable]
set uuid {uuid}
set vrf-select {integer}
next
end
config user radius
Parameter
Description
Type
Size
Default
account-key-cert-field
Define subject identity field in
certificate for user access right
checking.
option
-othername
Option
Description
othername
Other name in SAN.
rfc822name
RFC822 email address in SAN.
dnsname
DNS name in SAN.
FortiOS 8.0.0 CLI Reference
2279
Fortinet Inc.

<!-- 来源页 2280 -->
Parameter
Description
Type
Size
Default
Option
Description
cn
CN in subject.
account-key-processing
Account key processing operation.
The FortiGate will keep either the
whole domain or strip the domain
from the subject identity.
option
-same
Option
Description
same
Same as subject identity field.
strip
Strip domain string from subject identity field.
acct-all-servers
Enable/disable sending of
accounting messages to all
configured servers (default =
disable).
option
-disable
Option
Description
enable
Send accounting messages to all configured servers.
disable
Send accounting message only to servers that are confirmed to be
reachable.
acct-interim-interval
Time in seconds between each
accounting interim update message.
integer
Minimum value:
60 Maximum
value: 86400
0
all-usergroup
Enable/disable automatically
including this RADIUS server in all
user groups.
option
-disable
Option
Description
disable
Do not automatically include this server in a user group.
enable
Include this RADIUS server in every user group.
auth-type
Authentication methods/protocols
permitted for this RADIUS server.
option
-auto
Option
Description
auto
Use PAP, MSCHAP_v2, and CHAP (in that order).
ms_chap_v2
Microsoft Challenge Handshake Authentication Protocol version 2.
ms_chap
Microsoft Challenge Handshake Authentication Protocol.
FortiOS 8.0.0 CLI Reference
2280
Fortinet Inc.

<!-- 来源页 2281 -->
Parameter
Description
Type
Size
Default
Option
Description
chap
Challenge Handshake Authentication Protocol.
pap
Password Authentication Protocol.
ca-cert
CA of server to trust under TLS.
string
Maximum
length: 79
call-station-id-type
Calling & Called station identifier type
configuration (default = legacy), this
option is not available for 802.1x
authentication.
option
-legacy
Option
Description
legacy
Calling & Called station identifier is the value previously used by each
daemon.
IP
Calling & Called station identifier is the value of IP address.
MAC
Calling & Called station identifier is the value of MAC address.
class <name>
Class attribute name(s).
Class name.
string
Maximum
length: 79
client-cert
Client certificate to use under TLS.
string
Maximum
length: 35
delimiter
Configure delimiter to be used for
separating profile group names in the
SSO attribute (default = plus
character "+").
option
-plus
Option
Description
plus
Plus character "+".
comma
Comma character ",".
fabric-force-sync *
Enable/disable forced
synchronization of configuration
objects from the root FortiGate unit
to the downstream devices.
Configuration conflict check is
skipped.
option
-disable
Option
Description
enable
Enable forced synchronization of configuration objects from the root
FortiGate unit to the downstream devices.
FortiOS 8.0.0 CLI Reference
2281
Fortinet Inc.

<!-- 来源页 2282 -->
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
group-override-attr-type
RADIUS attribute type to override
user group information.
option
-Option
Description
filter-Id
Filter-Id
class
Class
h3c-compatibility
Enable/disable compatibility with the
H3C, a mechanism that performs
security checking for authentication.
option
-disable
Option
Description
enable
Enable H3C compatibility.
disable
Disable H3C compatibility.
interface
Specify outgoing interface to reach
server.
string
Maximum
length: 15
interface-select-method
Specify how to select outgoing
interface to reach server.
option
-auto
Option
Description
auto
Set outgoing interface automatically.
FortiOS 8.0.0 CLI Reference
2282
Fortinet Inc.

<!-- 来源页 2283 -->
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
mac-case
MAC authentication case (default =
lowercase).
option
-lowercase
Option
Description
uppercase
Use uppercase MAC.
lowercase
Use lowercase MAC.
mac-password-delimiter
MAC authentication password
delimiter (default = hyphen).
option
-hyphen
Option
Description
hyphen
Use hyphen as delimiter for MAC authentication password.
single-hyphen
Use single hyphen as delimiter for MAC authentication password.
colon
Use colon as delimiter for MAC authentication password.
none
No delimiter for MAC authentication password.
mac-username-delimiter
MAC authentication username
delimiter (default = hyphen).
option
-hyphen
Option
Description
hyphen
Use hyphen as delimiter for MAC authentication username.
single-hyphen
Use single hyphen as delimiter for MAC authentication username.
colon
Use colon as delimiter for MAC authentication username.
none
No delimiter for MAC authentication username.
name
RADIUS server entry name.
string
Maximum
length: 35
nas-id
Custom NAS identifier.
string
Maximum
length: 255
nas-id-type
NAS identifier type configuration
(default = legacy).
option
-legacy
Option
Description
legacy
NAS-ID value is the value previously used by each daemon.
FortiOS 8.0.0 CLI Reference
2283
Fortinet Inc.

<!-- 来源页 2284 -->
Parameter
Description
Type
Size
Default
Option
Description
custom
NAS-ID value is customized.
hostname
NAS-ID value is hostname or HA group name if applicable.
nas-ip
IP address used to communicate with
the RADIUS server and used as NAS-IP-Address and Called-Station-ID
attributes.
ipv4-address
Not Specified
0.0.0.0
password-encoding
Password encoding.
option
-auto
Option
Description
auto
Use original password encoding.
ISO-8859-1
Use ISO-8859-1 password encoding.
password-renewal
Enable/disable password renewal.
option
-enable
Option
Description
enable
Enable password renewal.
disable
Disable password renewal.
radius-coa
Enable to allow a mechanism to
change the attributes of an
authentication, authorization, and
accounting session after it is
authenticated.
option
-disable
Option
Description
enable
Enable RADIUS CoA.
disable
Disable RADIUS CoA.
radius-port
RADIUS service port number.
integer
Minimum value:
0 Maximum
value: 65535
0
require-message-authenticator
Require message authenticator in
authentication response.
option
-enable
FortiOS 8.0.0 CLI Reference
2284
Fortinet Inc.

<!-- 来源页 2285 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Make the validation of message authenticator mandatory in
authentication response.
disable
Make the validation of message authenticator optional in
authentication response.
rsso
Enable/disable RADIUS based single
sign on feature.
option
-disable
Option
Description
enable
Enable RADIUS based single sign on feature.
disable
Disable RADIUS based single sign on feature.
rsso-context-timeout
Time in seconds before the logged
out user is removed from the "user
context list" of logged on users.
integer
Minimum value:
0 Maximum
value:
4294967295
28800
rsso-endpoint-attribute
RADIUS attributes used to extract
the user end point identifier from the
RADIUS Start record.
option
-Calling-Station-Id
Option
Description
User-Name
Use this attribute.
NAS-IP-Address
Use this attribute.
Framed-IP-Address
Use this attribute.
Framed-IP-Netmask
Use this attribute.
Filter-Id
Use this attribute.
Login-IP-Host
Use this attribute.
Reply-Message
Use this attribute.
Callback-Number
Use this attribute.
Callback-Id
Use this attribute.
Framed-Route
Use this attribute.
Framed-IPX-Network
Use this attribute.
FortiOS 8.0.0 CLI Reference
2285
Fortinet Inc.

<!-- 来源页 2286 -->
Parameter
Description
Type
Size
Default
Option
Description
Class
Use this attribute.
Called-Station-Id
Use this attribute.
Calling-Station-Id
Use this attribute.
NAS-Identifier
Use this attribute.
Proxy-State
Use this attribute.
Login-LAT-Service
Use this attribute.
Login-LAT-Node
Use this attribute.
Login-LAT-Group
Use this attribute.
Framed-AppleTalk-Zone
Use this attribute.
Acct-Session-Id
Use this attribute.
Acct-Multi-Session-Id
Use this attribute.
rsso-endpoint-block-attribute
RADIUS attributes used to block a
user.
option
-Option
Description
User-Name
Use this attribute.
NAS-IP-Address
Use this attribute.
Framed-IP-Address
Use this attribute.
Framed-IP-Netmask
Use this attribute.
Filter-Id
Use this attribute.
Login-IP-Host
Use this attribute.
Reply-Message
Use this attribute.
FortiOS 8.0.0 CLI Reference
2286
Fortinet Inc.

<!-- 来源页 2287 -->
Parameter
Description
Type
Size
Default
Option
Description
Callback-Number
Use this attribute.
Callback-Id
Use this attribute.
Framed-Route
Use this attribute.
Framed-IPX-Network
Use this attribute.
Class
Use this attribute.
Called-Station-Id
Use this attribute.
Calling-Station-Id
Use this attribute.
NAS-Identifier
Use this attribute.
Proxy-State
Use this attribute.
Login-LAT-Service
Use this attribute.
Login-LAT-Node
Use this attribute.
Login-LAT-Group
Use this attribute.
Framed-AppleTalk-Zone
Use this attribute.
Acct-Session-Id
Use this attribute.
Acct-Multi-Session-Id
Use this attribute.
rsso-ep-one-ip-only
Enable/disable the replacement of
old IP addresses with new ones for
the same endpoint on RADIUS
accounting Start messages.
option
-disable
Option
Description
enable
Enable replacement of old IP address with new IP address for the
same endpoint on RADIUS accounting start.
FortiOS 8.0.0 CLI Reference
2287
Fortinet Inc.

<!-- 来源页 2288 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable replacement of old IP address with new IP address for the
same endpoint on RADIUS accounting start.
rsso-flush-ip-session
Enable/disable flushing user IP
sessions on RADIUS accounting Stop
messages.
option
-disable
Option
Description
enable
Enable flush user IP sessions on RADIUS accounting stop.
disable
Disable flush user IP sessions on RADIUS accounting stop.
rsso-log-flags
Events to log.
option
-protocol-error
profile-missing
accounting-stop-missed
accounting-event
endpoint-block
radiusd-other
Option
Description
protocol-error
Enable this log type.
profile-missing
Enable this log type.
accounting-stop-missed
Enable this log type.
accounting-event
Enable this log type.
endpoint-block
Enable this log type.
radiusd-other
Enable this log type.
none
Disable all logging.
rsso-log-period
Time interval in seconds that group
event log messages will be
generated for dynamic profile
events.
integer
Minimum value:
0 Maximum
value:
4294967295
0
rsso-radius-response
Enable/disable sending RADIUS
response packets after receiving
Start and Stop records.
option
-disable
FortiOS 8.0.0 CLI Reference
2288
Fortinet Inc.

<!-- 来源页 2289 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable sending RADIUS response packets.
disable
Disable sending RADIUS response packets.
rsso-radius-server-port
UDP port to listen on for RADIUS
Start and Stop records.
integer
Minimum value:
0 Maximum
value: 65535
1813
rsso-secret
RADIUS secret used by the RADIUS
accounting server.
password
Not Specified
rsso-validate-request-secret
Enable/disable validating the RADIUS
request shared secret in the Start or
End record.
option
-disable
Option
Description
enable
Enable validating RADIUS request shared secret.
disable
Disable validating RADIUS request shared secret.
secondary-secret
Secret key to access the secondary
server.
password
Not Specified
secondary-server
Secondary RADIUS CN domain name
or IP address.
string
Maximum
length: 63
secret
Pre-shared secret key used to
access the primary RADIUS server.
password
Not Specified
server
Primary RADIUS server CN domain
name or IP address.
string
Maximum
length: 63
server-identity-check
Enable/disable RADIUS server
identity check (verify server domain
name/IP address against the server
certificate).
option
-enable
Option
Description
enable
Enable server identity check.
disable
Disable server identity check.
source-ip
Source IP address for
communications to the RADIUS
server.
string
Maximum
length: 63
source-ip-interface
Source interface for communication
with the RADIUS server.
string
Maximum
length: 15
FortiOS 8.0.0 CLI Reference
2289
Fortinet Inc.

<!-- 来源页 2290 -->
Parameter
Description
Type
Size
Default
sso-attribute
RADIUS attribute that contains the
profile group name to be extracted
from the RADIUS Start record.
option
-Class
Option
Description
User-Name
Use this attribute.
NAS-IP-Address
Use this attribute.
Framed-IP-Address
Use this attribute.
Framed-IP-Netmask
Use this attribute.
Filter-Id
Use this attribute.
Login-IP-Host
Use this attribute.
Reply-Message
Use this attribute.
Callback-Number
Use this attribute.
Callback-Id
Use this attribute.
Framed-Route
Use this attribute.
Framed-IPX-Network
Use this attribute.
Class
Use this attribute.
Called-Station-Id
Use this attribute.
Calling-Station-Id
Use this attribute.
NAS-Identifier
Use this attribute.
Proxy-State
Use this attribute.
Login-LAT-Service
Use this attribute.
Login-LAT-Node
Use this attribute.
Login-LAT-Group
Use this attribute.
FortiOS 8.0.0 CLI Reference
2290
Fortinet Inc.

<!-- 来源页 2291 -->
Parameter
Description
Type
Size
Default
Option
Description
Framed-AppleTalk-Zone
Use this attribute.
Acct-Session-Id
Use this attribute.
Acct-Multi-Session-Id
Use this attribute.
sso-attribute-key
Key prefix for SSO group value in the
SSO attribute.
string
Maximum
length: 35
sso-attribute-value-override
Enable/disable override old attribute
value with new value for the same
endpoint.
option
-enable
Option
Description
enable
Enable override old attribute value with new value for the same
endpoint.
disable
Disable override old attribute value with new value for the same
endpoint.
status-ttl
Time for which server reachability is
cached so that when a server is
unreachable, it will not be retried for
at least this period of time (0 = cache
disabled, default = 300).
integer
Minimum value:
0 Maximum
value: 600
300
switch-controller-acct-fast-framedip-detect
Switch controller accounting
message Framed-IP detection from
DHCP snooping (seconds,
default=2).
integer
Minimum value:
2 Maximum
value: 600
2
switch-controller-nas-ip-dynamic
Enable/Disable switch-controller
nas-ip dynamic to dynamically set
nas-ip.
option
-disable
Option
Description
enable
Enable dynamic NAS-IP setting.
disable
Disable dynamic NAS-IP setting.
switch-controller-service-type
RADIUS service type.
option
-FortiOS 8.0.0 CLI Reference
2291
Fortinet Inc.

<!-- 来源页 2292 -->
Parameter
Description
Type
Size
Default
Option
Description
login
User should be connected to a host.
framed
User use Framed Protocol.
callback-login
User disconnected and called back.
callback-framed
User disconnected and called back, then a Framed Protocol.
outbound
User granted access to outgoing devices.
administrative
User granted access to the administrative unsigned interface.
nas-prompt
User provided a command prompt on the NAS.
authenticate-only
Authentication requested, and no auth info needs to be returned.
callback-nas-prompt
User disconnected and called back, then provided a command
prompt.
call-check
Used by the NAS in an Access-Request packet, Access-Accept to
answer the call.
callback-administrative
User disconnected and called back, granted access to the admin
unsigned interface.
tertiary-secret
Secret key to access the tertiary
server.
password
Not Specified
tertiary-server
Tertiary RADIUS CN domain name or
IP address.
string
Maximum
length: 63
timeout
Time in seconds to retry connecting
server.
integer
Minimum value:
1 Maximum
value: 300
5
tls-min-proto-version
Minimum supported protocol version
for TLS connections (default is to
follow system global setting).
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
2292
Fortinet Inc.

<!-- 来源页 2293 -->
Parameter
Description
Type
Size
Default
transport-protocol
Transport protocol to be used
(default = udp).
option
-udp
Option
Description
udp
UDP.
tcp
TCP.
tls
TLS over TCP.
use-management-vdom
Enable/disable using management
VDOM to send requests.
option
-disable
Option
Description
enable
Send requests using the management VDOM.
disable
Send requests using the current VDOM.
username-case-sensitive
Enable/disable case sensitive user
names.
option
-disable
Option
Description
enable
Enable username case-sensitive.
disable
Disable username case-sensitive.
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not Specified
00000000-0000-0000-0000-000000000000
vrf-select
VRF ID used for connection to server.
integer
Minimum value:
0 Maximum
value: 511
0
* This parameter may not exist in some models.
config accounting-server
Parameter
Description
Type
Size
Default
id
ID (0 - 4294967295).
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
FortiOS 8.0.0 CLI Reference
2293
Fortinet Inc.

<!-- 来源页 2294 -->
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
port
RADIUS accounting port number.
integer
Minimum value:
0 Maximum
value: 65535
0
secret
Secret key.
password
Not Specified
server
Server CN domain name or IP address.
string
Maximum
length: 63
source-ip
Source IP address for communications to the
RADIUS server.
string
Maximum
length: 63
status
Status.
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
Minimum value:
0 Maximum
value: 511
0
config user saml
SAML server entry configuration.
config user saml
Description: SAML server entry configuration.
edit <name>
set adfs-claim [enable|disable]
set cert {string}
set clock-tolerance {integer}
set digest-method [sha1|sha256]
set entity-id {string}
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
FortiOS 8.0.0 CLI Reference
2294
Fortinet Inc.

<!-- 来源页 2295 -->
set group-claim-type [email|given-name|...]
set group-name {string}
set idp-cert {string}
set idp-entity-id {string}
set idp-single-logout-url {string}
set idp-single-sign-on-url {string}
set limit-relaystate [enable|disable]
set realm {string}
set reauth [enable|disable]
set require-signed-resp-and-asrt [enable|disable]
set scim-client {string}
set scim-group-attr-type [display-name|external-id]
set scim-user-attr-type [user-name|display-name|...]
set service-provider-address {string}
set single-logout-url {string}
set single-sign-on-url {string}
set type [custom|fortiidentity-cloud]
set user-claim-type [email|given-name|...]
set user-name {string}
set user-source {string}
set uuid {uuid}
next
end
config user saml
Parameter
Description
Type
Size
Default
adfs-claim
Enable/disable ADFS Claim for user/group
attribute in assertion statement (default =
disable).
option
-disable
Option
Description
enable
Enable ADFS Claim for user/group attribute in assertion statement.
disable
Disable ADFS Claim for user/group attribute in assertion statement.
cert
Certificate to sign SAML messages.
string
Maximum
length: 35
clock-tolerance
Clock skew tolerance in seconds (0 - 300,
default = 15, 0 = no tolerance).
integer
Minimum
value: 0
Maximum
value: 300
15
digest-method
Digest method algorithm.
option
-sha256 **
FortiOS 8.0.0 CLI Reference
2295
Fortinet Inc.

<!-- 来源页 2296 -->
Parameter
Description
Type
Size
Default
Option
Description
sha1
Digest Method Algorithm is SHA1.
sha256
Digest Method Algorithm is SHA256.
entity-id
SP entity ID.
string
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
group-claim-type
Group claim in assertion statement.
option
-group
Option
Description
email
E-mail address of the user.
given-name
Given name of the user.
FortiOS 8.0.0 CLI Reference
2296
Fortinet Inc.

<!-- 来源页 2297 -->
Parameter
Description
Type
Size
Default
Option
Description
name
Unique name of the user.
upn
User principal name (UPN) of the user.
common-name
Common name of the user.
email-adfs-1x
E-mail address of the user when interoperating with AD FS 1.1 or ADFS
1.0.
group
Group that the user is a member of.
upn-adfs-1x
User principal name (UPN) of the user.
role
Role that the user has.
sur-name
Surname of the user
ppid
Private identifier of the user.
name-identifier
SAML name identifier of the user.
authentication-method
Method used to authenticate the user.
deny-only-group-sid
Deny-only group SID of the user.
deny-only-primary-sid
Deny-only primary SID of the user.
deny-only-primary-group-sid
Deny-only primary group SID of the user.
group-sid
Group SID of the user.
primary-group-sid
Primary group SID of the user.
primary-sid
Primary SID of the user.
windows-account-name
Domain account name of the user in the form of <domain>\<user>.
group-name
Group name in assertion statement.
string
Maximum
length: 255
idp-cert
IDP Certificate name.
string
Maximum
length: 35
idp-entity-id
IDP entity ID.
string
Maximum
length: 255
FortiOS 8.0.0 CLI Reference
2297
Fortinet Inc.

<!-- 来源页 2298 -->
Parameter
Description
Type
Size
Default
idp-single-logout-url
IDP single logout url.
string
Maximum
length: 255
idp-single-sign-on-url
IDP single sign-on URL.
string
Maximum
length: 255
limit-relaystate
Enable/disable limiting of relay-state
parameter when it exceeds SAML 2.0
specification limits (80 bytes).
option
-disable
Option
Description
enable
Enable limiting of relay-state parameter when it exceeds SAML 2.0
specification limits (80 bytes).
disable
Disable limiting of relay-state parameter when it exceeds SAML 2.0
specification limits (80 bytes).
name
SAML server entry name.
string
Maximum
length: 35
realm *
FortiIdentity cloud realm.
string
Maximum
length: 35
default
reauth
Enable/disable signalling of IDP to force
user re-authentication (default = disable).
option
-disable
Option
Description
enable
Enable signalling of IDP to force user re-authentication.
disable
Disable signalling of IDP to force user re-authentication.
require-signed-resp-and-asrt
Require both response and assertion from
IDP to be signed when FGT acts as SP
(default = disable).
option
-disable
Option
Description
enable
Both response and assertion must be signed and valid.
disable
At least one of response or assertion must be signed and valid.
scim-client
SCIM client name.
string
Maximum
length: 35
scim-group-attr-type
Group attribute type used to match SCIM
groups (default = display-name).
option
-display-name
Option
Description
display-name
Display name.
FortiOS 8.0.0 CLI Reference
2298
Fortinet Inc.

<!-- 来源页 2299 -->
Parameter
Description
Type
Size
Default
Option
Description
external-id
External ID.
scim-user-attr-type
User attribute type used to match SCIM
users (default = user-name).
option
-user-name
Option
Description
user-name
User name.
display-name
Display name.
external-id
External ID.
email
Email.
service-provider-address *
The address to handle SAML auth request.
To include a port, append it after a colon.
string
Maximum
length: 255
single-logout-url
SP single logout URL.
string
Maximum
length: 255
single-sign-on-url
SP single sign-on URL.
string
Maximum
length: 255
type *
SAML type.
option
-custom
Option
Description
custom
Manually configure SAML.
fortiidentity-cloud
Automatically create a new SSO app on FortiIdentity cloud and setup it
up
user-claim-type
User name claim in assertion statement.
option
-upn
Option
Description
email
E-mail address of the user.
given-name
Given name of the user.
name
Unique name of the user.
upn
User principal name (UPN) of the user.
common-name
Common name of the user.
email-adfs-1x
E-mail address of the user when interoperating with AD FS 1.1 or ADFS
1.0.
FortiOS 8.0.0 CLI Reference
2299
Fortinet Inc.

<!-- 来源页 2300 -->
Parameter
Description
Type
Size
Default
Option
Description
group
Group that the user is a member of.
upn-adfs-1x
User principal name (UPN) of the user.
role
Role that the user has.
sur-name
Surname of the user
ppid
Private identifier of the user.
name-identifier
SAML name identifier of the user.
authentication-method
Method used to authenticate the user.
deny-only-group-sid
Deny-only group SID of the user.
deny-only-primary-sid
Deny-only primary SID of the user.
deny-only-primary-group-sid
Deny-only primary group SID of the user.
group-sid
Group SID of the user.
primary-group-sid
Primary group SID of the user.
primary-sid
Primary SID of the user.
windows-account-name
Domain account name of the user in the form of <domain>\<user>.
user-name
User name in assertion statement.
string
Maximum
length: 255
user-source *
FortiIdentity cloud user souce.
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
** Values may differ between models.
config user scim
Configure SCIM client entries.
FortiOS 8.0.0 CLI Reference
2300
Fortinet Inc.

<!-- 来源页 2301 -->
config user scim
Description: Configure SCIM client entries.
edit <name>
set auth-method [token|base]
set base-url {string}
set cascade [disable|enable]
set certificate {string}
set client-identity-check [enable|disable]
set id {integer}
set secret {password}
set status [enable|disable]
set token-certificate {string}
next
end
config user scim
Parameter
Description
Type
Size
Default
auth-method
TLS client authentication methods (default =
bearer token).
option
-token
Option
Description
token
Bearer token.
base
Base.
base-url
Server URL to receive SCIM create, read,
update, delete (CRUD) requests.
string
Maximum
length: 127
cascade
Enable/disable to follow SCIM users/groups
changes in IDP.
option
-disable
Option
Description
disable
Disable setting.
enable
Enable setting.
certificate
Certificate for client verification during TLS
handshake.
string
Maximum
length: 79
client-identity-check
Enable/disable client identity check.
option
-enable
Option
Description
enable
Enable client identity check.
disable
Disable client identity check.
FortiOS 8.0.0 CLI Reference
2301
Fortinet Inc.

<!-- 来源页 2302 -->
Parameter
Description
Type
Size
Default
id
SCIM client ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
name
SCIM client name.
string
Maximum
length: 35
secret
Secret for token verification or base
authentication.
password
Not Specified
status
Enable/disable System for Cross-domain
Identity Management (SCIM).
option
-disable
Option
Description
enable
Enable System for Cross-domain Identity Management (SCIM).
disable
Disable System for Cross-domain Identity Management (SCIM).
token-certificate
Certificate for token verification.
string
Maximum
length: 79
config user security-exempt-list
Configure security exemption list.
config user security-exempt-list
Description: Configure security exemption list.
edit <name>
set description {string}
config rule
Description: Configure rules for exempting users from captive portal authentication.
edit <id>
set dstaddr <name1>, <name2>, ...
set service <name1>, <name2>, ...
set srcaddr <name1>, <name2>, ...
next
end
next
end
FortiOS 8.0.0 CLI Reference
2302
Fortinet Inc.

<!-- 来源页 2303 -->
config user security-exempt-list
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
Name of the exempt list.
string
Maximum
length: 35
config rule
Parameter
Description
Type
Size
Default
dstaddr
<name>
Destination addresses or address groups.
Address or group name.
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
service
<name>
Destination services.
Service name.
string
Maximum
length: 79
srcaddr
<name>
Source addresses or address groups.
Address or group name.
string
Maximum
length: 79
config user setting
Configure user authentication setting.
config user setting
Description: Configure user authentication setting.
set auth-blackout-time {integer}
set auth-ca-cert {string}
set auth-cert {string}
set auth-http-basic [enable|disable]
set auth-invalid-max {integer}
set auth-lockout-duration {integer}
set auth-lockout-threshold {integer}
set auth-on-demand [always|implicitly]
set auth-portal-timeout {integer}
config auth-ports
Description: Set up non-standard ports for authentication with HTTP, HTTPS, FTP, and
TELNET.
edit <id>
set port {integer}
set type [http|https|...]
FortiOS 8.0.0 CLI Reference
2303
Fortinet Inc.

<!-- 来源页 2304 -->
next
end
set auth-secure-http [enable|disable]
set auth-src-mac [enable|disable]
set auth-ssl-allow-renegotiation [enable|disable]
set auth-ssl-max-proto-version [sslv3|tlsv1|...]
set auth-ssl-min-proto-version [default|SSLv3|...]
set auth-ssl-sigalgs [no-rsa-pss|all]
set auth-timeout {integer}
set auth-timeout-type [idle-timeout|hard-timeout|...]
set auth-type {option1}, {option2}, ...
set cors [disable|enable]
set cors-allowed-origins <name1>, <name2>, ...
set default-user-password-policy {string}
set per-policy-disclaimer [enable|disable]
set radius-ses-timeout-act [hard-timeout|ignore-timeout]
end
config user setting
Parameter
Description
Type
Size
Default
auth-blackout-time
Time in seconds an IP address is denied
access after failing to authenticate five times
within one minute.
integer
Minimum value:
0 Maximum
value: 3600
0
auth-ca-cert
HTTPS CA certificate for policy
authentication.
string
Maximum
length: 35
auth-cert
HTTPS server certificate for policy
authentication.
string
Maximum
length: 35
auth-http-basic
Enable/disable use of HTTP basic
authentication for identity-based firewall
policies.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
auth-invalid-max
Maximum number of failed authentication
attempts before the user is blocked.
integer
Minimum value:
1 Maximum
value: 100
5
auth-lockout-duration
Lockout period in seconds after too many
login failures.
integer
Minimum value:
0 Maximum
value:
4294967295
0
FortiOS 8.0.0 CLI Reference
2304
Fortinet Inc.

<!-- 来源页 2305 -->
Parameter
Description
Type
Size
Default
auth-lockout-threshold
Maximum number of failed login attempts
before login lockout is triggered.
integer
Minimum value:
1 Maximum
value: 10
3
auth-on-demand
Always/implicitly trigger firewall
authentication on demand.
option
-implicitly
Option
Description
always
Always trigger firewall authentication on demand.
implicitly
Implicitly trigger firewall authentication on demand.
auth-portal-timeout
Time in minutes before captive portal user
have to re-authenticate (1 - 30 min, default 3
min).
integer
Minimum value:
1 Maximum
value: 30
3
auth-secure-http
Enable/disable redirecting HTTP user
authentication to more secure HTTPS.
option
-enable **
Option
Description
enable
Enable setting.
disable
Disable setting.
auth-src-mac
Enable/disable source MAC for user identity.
option
-enable
Option
Description
enable
Enable source MAC for user identity.
disable
Disable source MAC for user identity.
auth-ssl-allow-renegotiation
Allow/forbid SSL re-negotiation for HTTPS
authentication.
option
-disable
Option
Description
enable
Allow SSL re-negotiation.
disable
Forbid SSL re-negotiation.
auth-ssl-max-proto-version
Maximum supported protocol version for
SSL/TLS connections (default is no limit).
option
-Option
Description
sslv3
SSLv3.
tlsv1
TLSv1.
FortiOS 8.0.0 CLI Reference
2305
Fortinet Inc.

<!-- 来源页 2306 -->
Parameter
Description
Type
Size
Default
Option
Description
tlsv1-1
TLSv1.1.
tlsv1-2
TLSv1.2.
tlsv1-3
TLSv1.3.
auth-ssl-min-proto-version
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
auth-ssl-sigalgs
Set signature algorithms related to HTTPS
authentication (affects TLS version <= 1.2
only, default is to enable all).
option
-all
Option
Description
no-rsa-pss
Disable RSA-PSS signature algorithms for HTTPS authentication.
all
Enable all supported signature algorithms for HTTPS authentication.
auth-timeout
Time in minutes before the firewall user
authentication timeout requires the user to re-authenticate.
integer
Minimum value:
1 Maximum
value: 1440
5
auth-timeout-type
Control if authenticated users have to login
again after a hard timeout, after an idle
timeout, or after a session timeout.
option
-idle-timeout
Option
Description
idle-timeout
Idle timeout.
hard-timeout
Hard timeout.
new-session
New session timeout.
auth-type
Supported firewall policy authentication
protocols/methods.
option
-http **
FortiOS 8.0.0 CLI Reference
2306
Fortinet Inc.

<!-- 来源页 2307 -->
Parameter
Description
Type
Size
Default
Option
Description
http
Allow HTTP authentication.
https
Allow HTTPS authentication.
ftp
Allow FTP authentication.
telnet
Allow TELNET authentication.
cors
Enable/disable allowed origins white list for
CORS.
option
-disable
Option
Description
disable
Disable allowed origins white list for CORS.
enable
Enable allowed origins white list for CORS.
cors-allowed-origins <name>
Allowed origins white list for CORS.
Allowed origin for CORS.
string
Maximum
length: 79
default-user-password-policy
Default password policy to apply to all local
users unless otherwise specified, as defined
in config user password-policy.
string
Maximum
length: 35
per-policy-disclaimer
Enable/disable per policy disclaimer.
option
-disable
Option
Description
enable
Enable per policy disclaimer.
disable
Disable per policy disclaimer.
radius-ses-timeout-act
Set the RADIUS session timeout to a hard
timeout or to ignore RADIUS server session
timeouts.
option
-hard-timeout
Option
Description
hard-timeout
Use session timeout from RADIUS as hard-timeout.
ignore-timeout
Ignore session timeout from RADIUS.
** Values may differ between models.
FortiOS 8.0.0 CLI Reference
2307
Fortinet Inc.

<!-- 来源页 2308 -->
config auth-ports
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
port
Non-standard port for firewall user
authentication.
integer
Minimum value:
1 Maximum
value: 65535
1024
type
Service type.
option
-http
Option
Description
http
HTTP service.
https
HTTPS service.
ftp
FTP service.
telnet
TELNET service.
config user tacacs+
Configure TACACS+ server entries.
config user tacacs+
Description: Configure TACACS+ server entries.
edit <name>
set authen-type [mschap|chap|...]
set authorization [enable|disable]
set interface {string}
set interface-select-method [auto|sdwan|...]
set key {password}
set port {integer}
set secondary-key {password}
set secondary-server {string}
set server {string}
set source-ip {string}
set status-ttl {integer}
set tertiary-key {password}
set tertiary-server {string}
set vrf-select {integer}
next
end
FortiOS 8.0.0 CLI Reference
2308
Fortinet Inc.

<!-- 来源页 2309 -->
config user tacacs+
Parameter
Description
Type
Size
Default
authen-type
Allowed authentication protocols/methods.
option
-auto
Option
Description
mschap
MSCHAP.
chap
CHAP.
pap
PAP.
ascii
ASCII.
auto
Use PAP, MSCHAP, and CHAP (in that order).
authorization
Enable/disable TACACS+ authorization.
option
-disable
Option
Description
enable
Enable TACACS+ authorization.
disable
Disable TACACS+ authorization.
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
key
Key to access the primary server.
password
Not
Specified
name
TACACS+ server entry name.
string
Maximum
length: 35
port
Port number of the TACACS+ server.
integer
Minimum
value: 1
Maximum
value:
65535
49
secondary-key
Key to access the secondary server.
password
Not
Specified
FortiOS 8.0.0 CLI Reference
2309
Fortinet Inc.

<!-- 来源页 2310 -->
Parameter
Description
Type
Size
Default
secondary-server
Secondary TACACS+ server CN domain name or
IP address.
string
Maximum
length: 63
server
Primary TACACS+ server CN domain name or IP
address.
string
Maximum
length: 63
source-ip
Source IP address for communications to
TACACS+ server.
string
Maximum
length: 63
status-ttl
Time for which server reachability is cached so
that when a server is unreachable, it will not be
retried for at least this period of time (0 = cache
disabled, default = 300).
integer
Minimum
value: 0
Maximum
value: 600
300
tertiary-key
Key to access the tertiary server.
password
Not
Specified
tertiary-server
Tertiary TACACS+ server CN domain name or IP
address.
string
Maximum
length: 63
vrf-select
VRF ID used for connection to server.
integer
Minimum
value: 0
Maximum
value: 511
0
FortiOS 8.0.0 CLI Reference
2310
Fortinet Inc.
