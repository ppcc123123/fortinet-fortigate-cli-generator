# 内容安全：Web过滤/DNS过滤/邮件代理/文件过滤

> 来源: FortiOS-8.0.0-CLI_Reference.pdf
> 覆盖命令/章节: webfilter, dnsfilter, web-proxy, ftp-proxy, emailfilter, file-filter
> 本文件由 extract_pdf.py 从官方 PDF 自动提取，请勿手动编辑；
> 如需修正请修改 map.json 后重跑脚本。

---


<!-- 来源页 294 -->
dnsfilter
This section includes syntax for the following commands:
l config dnsfilter domain-filter on page 294
l config dnsfilter profile on page 296
config dnsfilter domain-filter
Configure DNS domain filters.
config dnsfilter domain-filter
Description: Configure DNS domain filters.
edit <id>
set comment {var-string}
config entries
Description: DNS domain filter entries.
edit <id>
set action [block|allow|...]
set comment {var-string}
set domain {string}
set status [enable|disable]
set type [simple|regex|...]
next
end
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set name {string}
set uuid {uuid}
next
end
config dnsfilter domain-filter
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
FortiOS 8.0.0 CLI Reference
294
Fortinet Inc.

<!-- 来源页 295 -->
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
ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
name
Name of table.
string
Maximum
length: 63
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
FortiOS 8.0.0 CLI Reference
295
Fortinet Inc.

<!-- 来源页 296 -->
config entries
Parameter
Description
Type
Size
Default
action
Action to take for domain filter matches.
option
-block
Option
Description
block
Block DNS requests matching the domain filter.
allow
Allow DNS requests matching the domain filter without logging.
monitor
Allow DNS requests matching the domain filter with logging.
comment
Comment.
var-string
Maximum
length: 255
domain
Domain entries to be filtered.
string
Maximum
length: 511
id
Id.
integer
Minimum value:
0 Maximum
value:
4294967295
0
status
Enable/disable this domain filter.
option
-enable
Option
Description
enable
Enable this domain filter.
disable
Disable this domain filter.
type
DNS domain filter type.
option
-simple
Option
Description
simple
Simple domain string.
regex
Regular expression domain string.
wildcard
Wildcard domain string.
config dnsfilter profile
Configure DNS domain filter profile.
config dnsfilter profile
Description: Configure DNS domain filter profile.
edit <name>
set block-action [block|redirect|...]
set block-botnet [disable|enable]
set comment {var-string}
FortiOS 8.0.0 CLI Reference
296
Fortinet Inc.

<!-- 来源页 297 -->
config dns-translation
Description: DNS translation settings.
edit <id>
set addr-type [ipv4|ipv6]
set dst {ipv4-address}
set dst6 {ipv6-address}
set netmask {ipv4-netmask}
set prefix {integer}
set src {ipv4-address}
set src6 {ipv6-address}
set status [enable|disable]
next
end
config domain-filter
Description: Domain filter settings.
set domain-filter-table {integer}
end
set external-ip-blocklist <name1>, <name2>, ...
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
config ftgd-dns
Description: FortiGuard DNS Filter settings.
config filters
Description: FortiGuard DNS domain filters.
edit <id>
set action [block|monitor]
set category {integer}
set log [enable|disable]
next
end
set options {option1}, {option2}, ...
end
set log-all-domain [enable|disable]
set redirect-portal {ipv4-address}
set redirect-portal6 {ipv6-address}
set safe-search [disable|enable]
set sdns-domain-log [enable|disable]
set sdns-ftgd-err-log [enable|disable]
set strip-ech [disable|enable]
set transparent-dns-database <name1>, <name2>, ...
set uuid {uuid}
set youtube-restrict [strict|moderate|...]
next
end
FortiOS 8.0.0 CLI Reference
297
Fortinet Inc.

<!-- 来源页 298 -->
config dnsfilter profile
Parameter
Description
Type
Size
Default
block-action
Action to take for blocked domains.
option
-redirect
Option
Description
block
Return NXDOMAIN for blocked domains.
redirect
Redirect blocked domains to SDNS portal.
block-sevrfail
Return SERVFAIL for blocked domains.
block-botnet
Enable/disable blocking botnet C&C DNS
lookups.
option
-disable
Option
Description
disable
Disable blocking botnet C&C DNS lookups.
enable
Enable blocking botnet C&C DNS lookups.
comment
Comment.
var-string
Maximum
length: 255
external-ip-blocklist
<name>
One or more external IP block lists.
External domain block list name.
string
Maximum
length: 79
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
298
Fortinet Inc.

<!-- 来源页 299 -->
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
log-all-domain
Enable/disable logging of all domains
visited (detailed DNS logging).
option
-disable
Option
Description
enable
Enable logging of all domains visited.
disable
Disable logging of all domains visited.
name
Profile name.
string
Maximum
length: 47
redirect-portal
IPv4 address of the SDNS redirect portal.
ipv4-address
Not
Specified
0.0.0.0
redirect-portal6
IPv6 address of the SDNS redirect portal.
ipv6-address
Not
Specified
::
safe-search
Enable/disable Google, Bing, YouTube,
Qwant, DuckDuckGo safe search.
option
-disable
Option
Description
disable
Disable Google, Bing, YouTube, Qwant, DuckDuckGo safe search.
enable
Enable Google, Bing, YouTube, Qwant, DuckDuckGo safe search.
sdns-domain-log
Enable/disable domain filtering and botnet
domain logging.
option
-enable
Option
Description
enable
Enable domain filtering and botnet domain logging.
disable
Disable domain filtering and botnet domain logging.
sdns-ftgd-err-log
Enable/disable FortiGuard SDNS rating
error logging.
option
-enable
Option
Description
enable
Enable FortiGuard SDNS rating error logging.
disable
Disable FortiGuard SDNS rating error logging.
FortiOS 8.0.0 CLI Reference
299
Fortinet Inc.

<!-- 来源页 300 -->
Parameter
Description
Type
Size
Default
strip-ech
Enable/disable removal of the encrypted
client hello service parameter from
supporting DNS RRs.
option
-enable
Option
Description
disable
Disable removal of the encrypted client hello service parameter from
supporting DNS RRs.
enable
Enable removal of the encrypted client hello service parameter from
supporting DNS RRs.
transparent-dns-database
<name>
Transparent DNS database zones.
DNS database zone name.
string
Maximum
length: 79
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be manually
reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
youtube-restrict
Set safe search for YouTube restriction
level.
option
-strict
Option
Description
strict
Enable strict safe seach for YouTube.
moderate
Enable moderate safe search for YouTube.
none
Disable safe search for YouTube.
* This parameter may not exist in some models.
config dns-translation
Parameter
Description
Type
Size
Default
addr-type
DNS translation type (IPv4 or IPv6).
option
-ipv4
Option
Description
ipv4
IPv4 address type.
ipv6
IPv6 address type.
FortiOS 8.0.0 CLI Reference
300
Fortinet Inc.

<!-- 来源页 301 -->
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
dst6
IPv6 address or subnet on the external
network to substitute for the resolved
address in DNS query replies. Can be
single IP address or subnet on the
external network, but number of
addresses must equal number of
mapped IP addresses in src6.
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
netmask
If src and dst are subnets rather than
single IP addresses, enter the netmask
for both src and dst.
ipv4-netmask
Not Specified
255.255.255.255
prefix
If src6 and dst6 are subnets rather than
single IP addresses, enter the prefix for
both src6 and dst6 (1 - 128, default =
128).
integer
Minimum value:
1 Maximum
value: 128
128
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
src6
IPv6 address or subnet on the internal
network to compare with the resolved
address in DNS query replies. If the
resolved address matches, the
resolved address is substituted with
dst6.
ipv6-address
Not Specified
::
status
Enable/disable this DNS translation
entry.
option
-enable
FortiOS 8.0.0 CLI Reference
301
Fortinet Inc.

<!-- 来源页 302 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable this DNS translation.
disable
Disable this DNS translation.
config domain-filter
Parameter
Description
Type
Size
Default
domain-filter-table
DNS domain filter table ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config ftgd-dns
Parameter
Description
Type
Size
Default
options
FortiGuard DNS filter options.
option
-Option
Description
error-allow
Allow all domains when FortiGuard DNS servers fail.
ftgd-disable
Disable FortiGuard DNS domain rating.
config filters
Parameter
Description
Type
Size
Default
action
Action to take for DNS requests matching the
category.
option
-monitor
Option
Description
block
Block DNS requests matching the category.
monitor
Allow DNS requests matching the category and log the result.
category
Category number.
integer
Minimum
value: 0
Maximum
value: 255
0
FortiOS 8.0.0 CLI Reference
302
Fortinet Inc.

<!-- 来源页 303 -->
Parameter
Description
Type
Size
Default
id
ID number.
integer
Minimum
value: 0
Maximum
value: 255
0
log
Enable/disable DNS filter logging for this DNS
profile.
option
-enable
Option
Description
enable
Enable DNS filter logging.
disable
Disable DNS filter logging.
FortiOS 8.0.0 CLI Reference
303
Fortinet Inc.

---


<!-- 来源页 309 -->
emailfilter
This section includes syntax for the following commands:
l config emailfilter block-allow-list on page 309
l config emailfilter bword on page 312
l config emailfilter dnsbl on page 315
l config emailfilter fortishield on page 317
l config emailfilter iptrust on page 318
l config emailfilter mheader on page 320
l config emailfilter options on page 322
l config emailfilter profile on page 323
config emailfilter block-allow-list
Configure anti-spam block/allow list.
config emailfilter block-allow-list
Description: Configure anti-spam block/allow list.
edit <id>
set comment {var-string}
config entries
Description: Anti-spam block/allow entries.
edit <id>
set action [reject|spam|...]
set addr-type [ipv4|ipv6]
set ip4-subnet {ipv4-classnet}
set ip6-subnet {ipv6-network}
set pattern {string}
set pattern-type [wildcard|regexp]
set status [enable|disable]
set type [ip|email-to|...]
next
end
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set name {string}
set uuid {uuid}
next
end
FortiOS 8.0.0 CLI Reference
309
Fortinet Inc.

<!-- 来源页 310 -->
config emailfilter block-allow-list
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
id
ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
name
Name of table.
string
Maximum
length: 63
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
FortiOS 8.0.0 CLI Reference
310
Fortinet Inc.

<!-- 来源页 311 -->
config entries
Parameter
Description
Type
Size
Default
action
Reject, mark as spam or good email.
option
-spam
Option
Description
reject
Reject the connection.
spam
Mark as spam email.
clear
Mark as good email.
addr-type
IP address type.
option
-ipv4
Option
Description
ipv4
IPv4 Address type.
ipv6
IPv6 Address type.
id
Entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
ip4-subnet
IPv4 network address/subnet mask bits.
ipv4-classnet
Not Specified
0.0.0.0
0.0.0.0
ip6-subnet
IPv6 network address/subnet mask bits.
ipv6-network
Not Specified
::/128
pattern
Pattern to match.
string
Maximum
length: 127
pattern-type
Wildcard pattern or regular expression.
option
-wildcard
Option
Description
wildcard
Wildcard pattern.
regexp
Perl regular expression.
status
Enable/disable status.
option
-enable
Option
Description
enable
Enable status.
disable
Disable status.
type
Entry type.
option
-ip
FortiOS 8.0.0 CLI Reference
311
Fortinet Inc.

<!-- 来源页 312 -->
Parameter
Description
Type
Size
Default
Option
Description
ip
By IP address.
email-to
By email recipient.
email-from
By email sender.
subject
By email subject.
config emailfilter bword
Configure AntiSpam banned word list.
config emailfilter bword
Description: Configure AntiSpam banned word list.
edit <id>
set comment {var-string}
config entries
Description: Spam filter banned word.
edit <id>
set action [spam|clear]
set language [western|simch|...]
set pattern {string}
set pattern-type [wildcard|regexp]
set score {integer}
set status [enable|disable]
set where [subject|body|...]
next
end
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set name {string}
set uuid {uuid}
next
end
config emailfilter bword
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
FortiOS 8.0.0 CLI Reference
312
Fortinet Inc.

<!-- 来源页 313 -->
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
ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
name
Name of table.
string
Maximum
length: 63
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
FortiOS 8.0.0 CLI Reference
313
Fortinet Inc.

<!-- 来源页 314 -->
config entries
Parameter
Description
Type
Size
Default
action
Mark spam or good.
option
-spam
Option
Description
spam
Mark as spam email.
clear
Mark as good email.
id
Banned word entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
language
Language for the banned word.
option
-western
Option
Description
western
Western.
simch
Simplified Chinese.
trach
Traditional Chinese.
japanese
Japanese.
korean
Korean.
french
French.
thai
Thai.
spanish
Spanish.
pattern
Pattern for the banned word.
string
Maximum
length: 127
pattern-type
Wildcard pattern or regular expression.
option
-wildcard
Option
Description
wildcard
Wildcard pattern.
regexp
Perl regular expression.
score
Score value.
integer
Minimum value:
1 Maximum
value: 99999
10
status
Enable/disable status.
option
-enable
FortiOS 8.0.0 CLI Reference
314
Fortinet Inc.

<!-- 来源页 315 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable status.
disable
Disable status.
where
Component of the email to be scanned.
option
-all
Option
Description
subject
Banned word in email subject.
body
Banned word in email body.
all
Banned word in both subject and body.
config emailfilter dnsbl
Configure AntiSpam DNSBL/ORBL.
config emailfilter dnsbl
Description: Configure AntiSpam DNSBL/ORBL.
edit <id>
set comment {var-string}
config entries
Description: Spam filter DNSBL and ORBL server.
edit <id>
set action [reject|spam]
set server {string}
set status [enable|disable]
next
end
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set name {string}
set uuid {uuid}
next
end
config emailfilter dnsbl
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
FortiOS 8.0.0 CLI Reference
315
Fortinet Inc.

<!-- 来源页 316 -->
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
ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
name
Name of table.
string
Maximum
length: 63
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
FortiOS 8.0.0 CLI Reference
316
Fortinet Inc.

<!-- 来源页 317 -->
config entries
Parameter
Description
Type
Size
Default
action
Reject connection or mark as spam email.
option
-spam
Option
Description
reject
Reject the connection.
spam
Mark as spam email.
id
DNSBL/ORBL entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
server
DNSBL or ORBL server name.
string
Maximum
length: 127
status
Enable/disable status.
option
-enable
Option
Description
enable
Enable status.
disable
Disable status.
config emailfilter fortishield
Configure FortiGuard - AntiSpam.
config emailfilter fortishield
Description: Configure FortiGuard - AntiSpam.
set spam-submit-force [enable|disable]
set spam-submit-srv {string}
set spam-submit-txt2htm [enable|disable]
end
config emailfilter fortishield
Parameter
Description
Type
Size
Default
spam-submit-force
Enable/disable force insertion of a new
mime entity for the submission text.
option
-enable
Option
Description
enable
Enable setting.
FortiOS 8.0.0 CLI Reference
317
Fortinet Inc.

<!-- 来源页 318 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable setting.
spam-submit-srv
Hostname of the spam submission
server.
string
Maximum
length: 63
www.nospammer.net
spam-submit-txt2htm
Enable/disable conversion of text email
to HTML email.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
config emailfilter iptrust
Configure AntiSpam IP trust.
config emailfilter iptrust
Description: Configure AntiSpam IP trust.
edit <id>
set comment {var-string}
config entries
Description: Spam filter trusted IP addresses.
edit <id>
set addr-type [ipv4|ipv6]
set ip4-subnet {ipv4-classnet}
set ip6-subnet {ipv6-network}
set status [enable|disable]
next
end
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set name {string}
set uuid {uuid}
next
end
FortiOS 8.0.0 CLI Reference
318
Fortinet Inc.

<!-- 来源页 319 -->
config emailfilter iptrust
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
id
ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
name
Name of table.
string
Maximum
length: 63
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
FortiOS 8.0.0 CLI Reference
319
Fortinet Inc.

<!-- 来源页 320 -->
config entries
Parameter
Description
Type
Size
Default
addr-type
Type of address.
option
-ipv4
Option
Description
ipv4
IPv4 Address type.
ipv6
IPv6 Address type.
id
Trusted IP entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
ip4-subnet
IPv4 network address or network
address/subnet mask bits.
ipv4-classnet
Not Specified
0.0.0.0
0.0.0.0
ip6-subnet
IPv6 network address/subnet mask bits.
ipv6-network
Not Specified
::/128
status
Enable/disable status.
option
-enable
Option
Description
enable
Enable status.
disable
Disable status.
config emailfilter mheader
Configure AntiSpam MIME header.
config emailfilter mheader
Description: Configure AntiSpam MIME header.
edit <id>
set comment {var-string}
config entries
Description: Spam filter mime header content.
edit <id>
set action [spam|clear]
set fieldbody {string}
set fieldname {string}
set pattern-type [wildcard|regexp]
set status [enable|disable]
next
end
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
FortiOS 8.0.0 CLI Reference
320
Fortinet Inc.

<!-- 来源页 321 -->
set name {string}
set uuid {uuid}
next
end
config emailfilter mheader
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
id
ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
FortiOS 8.0.0 CLI Reference
321
Fortinet Inc.

<!-- 来源页 322 -->
Parameter
Description
Type
Size
Default
name
Name of table.
string
Maximum
length: 63
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
config entries
Parameter
Description
Type
Size
Default
action
Mark spam or good.
option
-spam
Option
Description
spam
Mark as spam email.
clear
Mark as good email.
fieldbody
Pattern for the header field body.
string
Maximum
length: 127
fieldname
Pattern for header field name.
string
Maximum
length: 63
id
Mime header entry ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
pattern-type
Wildcard pattern or regular expression.
option
-wildcard
Option
Description
wildcard
Wildcard pattern.
regexp
Perl regular expression.
status
Enable/disable status.
option
-enable
Option
Description
enable
Enable status.
disable
Disable status.
config emailfilter options
Configure AntiSpam options.
FortiOS 8.0.0 CLI Reference
322
Fortinet Inc.

<!-- 来源页 323 -->
config emailfilter options
Description: Configure AntiSpam options.
set dns-timeout {integer}
end
config emailfilter options
Parameter
Description
Type
Size
Default
dns-timeout
DNS query time out (1 - 30 sec).
integer
Minimum
value: 1
Maximum
value: 30
7
config emailfilter profile
Configure Email Filter profiles.
config emailfilter profile
Description: Configure Email Filter profiles.
edit <name>
set comment {var-string}
set external [enable|disable]
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set feature-set [flow|proxy]
config gmail
Description: Gmail.
set log-all [disable|enable]
end
config imap
Description: IMAP.
set action [pass|tag]
set log-all [disable|enable]
set tag-msg {string}
set tag-type {option1}, {option2}, ...
end
config mapi
Description: MAPI.
set action [pass|discard]
set log-all [disable|enable]
end
config msn-hotmail
Description: MSN Hotmail.
set log-all [disable|enable]
end
set options {option1}, {option2}, ...
FortiOS 8.0.0 CLI Reference
323
Fortinet Inc.

<!-- 来源页 324 -->
config other-webmails
Description: Other supported webmails.
set log-all [disable|enable]
end
config pop3
Description: POP3.
set action [pass|tag]
set log-all [disable|enable]
set tag-msg {string}
set tag-type {option1}, {option2}, ...
end
set replacemsg-group {string}
config smtp
Description: SMTP.
set action [pass|tag|...]
set hdrip [disable|enable]
set local-override [disable|enable]
set log-all [disable|enable]
set tag-msg {string}
set tag-type {option1}, {option2}, ...
end
set spam-bal-table {integer}
set spam-bword-table {integer}
set spam-bword-threshold {integer}
set spam-filtering [enable|disable]
set spam-iptrust-table {integer}
set spam-log [disable|enable]
set spam-log-fortiguard-response [disable|enable]
set spam-mheader-table {integer}
set spam-rbl-table {integer}
set uuid {uuid}
config yahoo-mail
Description: Yahoo! Mail.
set log-all [disable|enable]
end
next
end
config emailfilter profile
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
external
Enable/disable external Email
inspection.
option
-disable
FortiOS 8.0.0 CLI Reference
324
Fortinet Inc.

<!-- 来源页 325 -->
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
feature-set
Flow/proxy feature set.
option
-flow
Option
Description
flow
Flow feature set.
proxy
Proxy feature set.
name
Profile name.
string
Maximum
length: 47
options
Options.
option
-FortiOS 8.0.0 CLI Reference
325
Fortinet Inc.

<!-- 来源页 326 -->
Parameter
Description
Type
Size
Default
Option
Description
bannedword
Content block.
spambal
Block/allow list.
spamfsip
Email IP address FortiGuard AntiSpam block list check.
spamfssubmit
Add FortiGuard AntiSpam spam submission text.
spamfschksum
Email checksum FortiGuard AntiSpam check.
spamfsurl
Email content URL FortiGuard AntiSpam check.
spamhelodns
Email helo/ehlo domain DNS check.
spamraddrdns
Email return address DNS check.
spamrbl
Email DNSBL & ORBL check.
spamhdrcheck
Email mime header check.
spamfsphish
Email content phishing URL FortiGuard AntiSpam check.
replacemsg-group
Replacement message group.
string
Maximum
length: 35
spam-bal-table
Anti-spam block/allow list table ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
spam-bword-table
Anti-spam banned word table ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
spam-bword-threshold
Spam banned word threshold.
integer
Minimum value:
0 Maximum
value:
2147483647
10
spam-filtering
Enable/disable spam filtering.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
spam-iptrust-table
Anti-spam IP trust table ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
FortiOS 8.0.0 CLI Reference
326
Fortinet Inc.

<!-- 来源页 327 -->
Parameter
Description
Type
Size
Default
spam-log
Enable/disable spam logging for email
filtering.
option
-enable
Option
Description
disable
Disable spam logging for email filtering.
enable
Enable spam logging for email filtering.
spam-log-fortiguard-response
Enable/disable logging FortiGuard spam
response.
option
-disable
Option
Description
disable
Disable logging FortiGuard spam response.
enable
Enable logging FortiGuard spam response.
spam-mheader-table
Anti-spam MIME header table ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
spam-rbl-table
Anti-spam DNSBL table ID.
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
config gmail
Parameter
Description
Type
Size
Default
log-all
Enable/disable logging of all email traffic.
option
-disable
Option
Description
disable
Disable logging of all email traffic.
enable
Enable logging of all email traffic.
FortiOS 8.0.0 CLI Reference
327
Fortinet Inc.

<!-- 来源页 328 -->
config imap
Parameter
Description
Type
Size
Default
action
Action for spam email.
option
-tag
Option
Description
pass
Allow spam email to pass through.
tag
Tag spam email with configured text in subject or header.
log-all
Enable/disable logging of all email traffic.
option
-disable
Option
Description
disable
Disable logging of all email traffic.
enable
Enable logging of all email traffic.
tag-msg
Subject text or header added to spam email.
string
Maximum
length: 63
Spam
tag-type
Tag subject or header for spam email.
option
-subject
spaminfo
Option
Description
subject
Prepend text to spam email subject.
header
Append a user defined mime header to spam email.
spaminfo
Append spam info to spam email header.
config mapi
Parameter
Description
Type
Size
Default
action
Action for spam email.
option
-pass
Option
Description
pass
Allow spam email to pass through.
discard
Discard (block) spam email.
log-all
Enable/disable logging of all email traffic.
option
-disable
Option
Description
disable
Disable logging of all email traffic.
enable
Enable logging of all email traffic.
FortiOS 8.0.0 CLI Reference
328
Fortinet Inc.

<!-- 来源页 329 -->
config msn-hotmail
Parameter
Description
Type
Size
Default
log-all
Enable/disable logging of all email traffic.
option
-disable
Option
Description
disable
Disable logging of all email traffic.
enable
Enable logging of all email traffic.
config other-webmails
Parameter
Description
Type
Size
Default
log-all
Enable/disable logging of all email traffic.
option
-disable
Option
Description
disable
Disable logging of all email traffic.
enable
Enable logging of all email traffic.
config pop3
Parameter
Description
Type
Size
Default
action
Action for spam email.
option
-tag
Option
Description
pass
Allow spam email to pass through.
tag
Tag spam email with configured text in subject or header.
log-all
Enable/disable logging of all email traffic.
option
-disable
Option
Description
disable
Disable logging of all email traffic.
enable
Enable logging of all email traffic.
tag-msg
Subject text or header added to spam email.
string
Maximum
length: 63
Spam
tag-type
Tag subject or header for spam email.
option
-subject
spaminfo
Option
Description
subject
Prepend text to spam email subject.
FortiOS 8.0.0 CLI Reference
329
Fortinet Inc.

<!-- 来源页 330 -->
Parameter
Description
Type
Size
Default
Option
Description
header
Append a user defined mime header to spam email.
spaminfo
Append spam info to spam email header.
config smtp
Parameter
Description
Type
Size
Default
action
Action for spam email.
option
-discard
Option
Description
pass
Allow spam email to pass through.
tag
Tag spam email with configured text in subject or header.
discard
Discard (block) spam email.
hdrip
Enable/disable SMTP email header IP checks for
spamfsip, spamrbl, and spambal filters.
option
-disable
Option
Description
disable
Disable SMTP email header IP checks for spamfsip, spamrbl, and
spambal filters.
enable
Enable SMTP email header IP checks for spamfsip, spamrbl, and
spambal filters.
local-override
Enable/disable local filter to override SMTP remote
check result.
option
-disable
Option
Description
disable
Disable local filter to override SMTP remote check result.
enable
Enable local filter to override SMTP remote check result.
log-all
Enable/disable logging of all email traffic.
option
-disable
Option
Description
disable
Disable logging of all email traffic.
enable
Enable logging of all email traffic.
tag-msg
Subject text or header added to spam email.
string
Maximum
length: 63
Spam
FortiOS 8.0.0 CLI Reference
330
Fortinet Inc.

<!-- 来源页 331 -->
Parameter
Description
Type
Size
Default
tag-type
Tag subject or header for spam email.
option
-subject
spaminfo
Option
Description
subject
Prepend text to spam email subject.
header
Append a user defined mime header to spam email.
spaminfo
Append spam info to spam email header.
config yahoo-mail
Parameter
Description
Type
Size
Default
log-all
Enable/disable logging of all email traffic.
option
-disable
Option
Description
disable
Disable logging of all email traffic.
enable
Enable logging of all email traffic.
FortiOS 8.0.0 CLI Reference
331
Fortinet Inc.

---


<!-- 来源页 390 -->
file-filter
This section includes syntax for the following commands:
l config file-filter profile on page 390
config file-filter profile
Configure file-filter profiles.
config file-filter profile
Description: Configure file-filter profiles.
edit <name>
set comment {var-string}
set extended-log [disable|enable]
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set feature-set [flow|proxy]
set log [disable|enable]
set replacemsg-group {string}
config rules
Description: File filter rules.
edit <name>
set action [log-only|block|...]
set comment {var-string}
set direction [incoming|outgoing|...]
set file-type <name1>, <name2>, ...
set password-protected [yes|any]
set protocol {option1}, {option2}, ...
next
end
set scan-archive-contents [disable|enable]
set uuid {uuid}
next
end
config file-filter profile
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
390
Fortinet Inc.

<!-- 来源页 391 -->
Parameter
Description
Type
Size
Default
extended-log
Enable/disable file-filter extended logging.
option
-disable
Option
Description
disable
Disable extended logging.
enable
Enable extended logging.
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
feature-set
Flow/proxy feature set.
option
-flow
Option
Description
flow
Flow feature set.
proxy
Proxy feature set.
log
Enable/disable file-filter logging.
option
-enable
FortiOS 8.0.0 CLI Reference
391
Fortinet Inc.

<!-- 来源页 392 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable logging.
enable
Enable logging.
name
Profile name.
string
Maximum
length: 47
replacemsg-group
Replacement message group.
string
Maximum
length: 35
scan-archive-contents
Enable/disable archive contents scan.
option
-enable
Option
Description
disable
Disable scanning archive contents.
enable
Enable scanning archive contents.
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be manually
reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
config rules
Parameter
Description
Type
Size
Default
action
Action taken for matched file.
option
-log-only
Option
Description
log-only
Allow the content and write a log message.
block
Block the content and write a log message.
warning
Allow content after warning the user. Access is logged. Applies only to
incoming HTTP traffic. Outgoing HTTP traffic and other protocols are
log-only.
comment
Comment.
var-string
Maximum
length: 255
direction
Traffic direction (HTTP, FTP, SSH, WEBSOCKET,
CIFS, and MAPI only).
option
-any
FortiOS 8.0.0 CLI Reference
392
Fortinet Inc.

<!-- 来源页 393 -->
Parameter
Description
Type
Size
Default
Option
Description
incoming
Match files transmitted in the session's reply direction.
outgoing
Match files transmitted in the session's originating direction.
any
Match files transmitted in the session's originating and reply directions.
file-type
<name>
Select file type.
File type name.
string
Maximum
length: 39
name
File-filter rule name.
string
Maximum
length: 35
password-protected
Match password-protected files.
option
-any
Option
Description
yes
Match only password-protected files.
any
Match any file.
protocol
Protocols to apply rule to.
option
-http ftp smtp
imap pop3
mapi cifs ssh
websocket
**
Option
Description
http
Filter on HTTP.
ftp
Filter on FTP.
smtp
Filter on SMTP.
imap
Filter on IMAP.
pop3
Filter on POP3.
mapi
Filter on MAPI. (Proxy mode only.)
cifs
Filter on CIFS.
ssh
Filter on SFTP and SCP. (Proxy mode only.)
websocket
Filter on WEBSOCKET. (Proxy mode only.)
** Values may differ between models.
FortiOS 8.0.0 CLI Reference
393
Fortinet Inc.

---


<!-- 来源页 835 -->
ftp-proxy
This section includes syntax for the following commands:
l config ftp-proxy explicit on page 835
config ftp-proxy explicit
Configure explicit FTP proxy settings.
config ftp-proxy explicit
Description: Configure explicit FTP proxy settings.
set incoming-ip {ipv4-address-any}
set incoming-port {user}
set outgoing-ip {ipv4-address-any}
set sec-default-action [accept|deny]
set server-data-mode [client|passive]
set ssl [enable|disable]
set ssl-algorithm [high|medium|...]
set ssl-cert <name1>, <name2>, ...
set ssl-dh-bits [768|1024|...]
set status [enable|disable]
end
config ftp-proxy explicit
Parameter
Description
Type
Size
Default
incoming-ip
Accept incoming FTP requests from this IP
address. An interface must have this IP address.
ipv4-address-any
Not
Specified
0.0.0.0
incoming-port
Accept incoming FTP requests on one or more
ports.
user
Not
Specified
outgoing-ip
Outgoing FTP requests will leave from this IP
address. An interface must have this IP address.
ipv4-address-any
Not
Specified
sec-default-action
Accept or deny explicit FTP proxy sessions when
no FTP proxy firewall policy exists.
option
-deny
FortiOS 8.0.0 CLI Reference
835
Fortinet Inc.

<!-- 来源页 836 -->
Parameter
Description
Type
Size
Default
Option
Description
accept
Accept requests. All explicit FTP proxy traffic is accepted whether there
is an explicit FTP proxy policy or not
deny
Deny requests unless there is a matching explicit FTP proxy policy.
server-data-mode
Determine mode of data session on FTP server
side.
option
-client
Option
Description
client
Use the same transmission mode for client and server data sessions.
passive
Use passive mode on server data session.
ssl
Enable/disable the explicit FTPS proxy.
option
-disable
Option
Description
enable
Enable the explicit FTPS proxy.
disable
Disable the explicit FTPS proxy.
ssl-algorithm
Relative strength of encryption algorithms
accepted in negotiation.
option
-high
Option
Description
high
High encryption. Allow only AES and ChaCha
medium
Medium encryption. Allow AES, ChaCha, 3DES, and RC4.
low
Low encryption. Allow AES, ChaCha, 3DES, RC4, and DES.
ssl-cert
<name>
List of certificate names to use for SSL connections
to this server.
Certificate list.
string
Maximum
length: 79
ssl-dh-bits
Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA negotiation (default = 2048).
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
status
Enable/disable the explicit FTP proxy.
option
-disable
FortiOS 8.0.0 CLI Reference
836
Fortinet Inc.

<!-- 来源页 837 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable the explicit FTP proxy.
disable
Disable the explicit FTP proxy.
FortiOS 8.0.0 CLI Reference
837
Fortinet Inc.

---


<!-- 来源页 2596 -->
web-proxy
This section includes syntax for the following commands:
l config web-proxy debug-url on page 2596
l config web-proxy explicit on page 2597
l config web-proxy fast-fallback on page 2605
l config web-proxy forward-server-group on page 2609
l config web-proxy forward-server on page 2606
l config web-proxy global on page 2611
l config web-proxy isolator-server on page 2616
l config web-proxy profile on page 2618
l config web-proxy url-match on page 2624
l config web-proxy wisp on page 2626
config web-proxy debug-url
Configure debug URL addresses.
config web-proxy debug-url
Description: Configure debug URL addresses.
edit <name>
set exact [enable|disable]
set status [enable|disable]
set url-pattern {string}
next
end
config web-proxy debug-url
Parameter
Description
Type
Size
Default
exact
Enable/disable matching the exact path.
option
-enable
Option
Description
enable
Enable matching the exact path.
disable
Disable matching the exact path.
name
Debug URL name.
string
Maximum
length: 63
FortiOS 8.0.0 CLI Reference
2596
Fortinet Inc.

<!-- 来源页 2597 -->
Parameter
Description
Type
Size
Default
status
Enable/disable this URL exemption.
option
-enable
Option
Description
enable
Enable this URL exemption.
disable
Disable this URL exemption.
url-pattern
URL exemption pattern.
string
Maximum
length: 511
config web-proxy explicit
Configure explicit Web proxy settings.
config web-proxy explicit
Description: Configure explicit Web proxy settings.
set client-cert [disable|enable]
set client-certificate-blocklist [enable|disable]
set empty-cert-action [accept|block|...]
set ftp-incoming-port {user}
set ftp-over-http [enable|disable]
set http-connection-mode [static|multiplex|...]
set http-incoming-port {user}
set https-incoming-port {user}
set https-replacement-message [enable|disable]
set incoming-ip {ipv4-address-any}
set incoming-ip6 {ipv6-address}
set interface {string}
set interface-select-method [sdwan|specify]
set ipv6-status [enable|disable]
set message-upon-server-error [enable|disable]
set outgoing-ip {ipv4-address-any}
set outgoing-ip6 {ipv6-address}
set pac-file-data {user}
set pac-file-name {string}
set pac-file-server-port {user}
set pac-file-server-status [enable|disable]
set pac-file-through-https [enable|disable]
set pac-file-url {user}
config pac-policy
Description: PAC policies.
edit <policyid>
set comments {var-string}
set dstaddr <name1>, <name2>, ...
set pac-file-data {user}
set pac-file-name {string}
set srcaddr <name1>, <name2>, ...
set srcaddr6 <name1>, <name2>, ...
FortiOS 8.0.0 CLI Reference
2597
Fortinet Inc.

<!-- 来源页 2598 -->
set status [enable|disable]
next
end
set pref-dns-result [ipv4|ipv6|...]
set realm {string}
set sec-default-action [accept|deny]
set secure-web-proxy [disable|enable|...]
set secure-web-proxy-cert <name1>, <name2>, ...
set socks [enable|disable]
set socks-incoming-port {user}
set ssl-algorithm [high|medium|...]
set ssl-dh-bits [768|1024|...]
set status [enable|disable]
set strict-guest [enable|disable]
set trace-auth-no-rsp [enable|disable]
set unknown-http-version [reject|best-effort]
set user-agent-detect [disable|enable]
set vrf-select {integer}
end
config web-proxy explicit
Parameter
Description
Type
Size
Default
client-cert
Enable/disable to request client certificate.
option
-disable
Option
Description
disable
Disable client certificate request.
enable
Enable client certificate request.
client-certificate-blocklist *
Enable/disable blocking client malicious
certificates list by FortiGuard during TLS
handshake.
option
-enable
Option
Description
enable
Enable client certificate blocklist during TLS handshake.
disable
Disable client certificate blocklist during TLS handshake.
empty-cert-action
Action of an empty client certificate.
option
-block
Option
Description
accept
Accept the SSL handshake if the client certificate is empty.
block
Block the SSL handshake if the client certificate is empty.
FortiOS 8.0.0 CLI Reference
2598
Fortinet Inc.

<!-- 来源页 2599 -->
Parameter
Description
Type
Size
Default
Option
Description
accept-unmanageable
Accept the SSL handshake only if the end-point is unmanageable.
ftp-incoming-port
Accept incoming FTP-over-HTTP requests on
one or more ports (0 - 65535, default = 0; use
the same as HTTP).
user
Not
Specified
ftp-over-http
Enable to proxy FTP-over-HTTP sessions sent
from a web browser.
option
-disable
Option
Description
enable
Enable FTP-over-HTTP sessions.
disable
Disable FTP-over-HTTP sessions.
http-connection-mode
HTTP connection mode (default = static).
option
-static
Option
Description
static
Only one server connection exists during the proxy session.
multiplex
Established connections are held until the proxy session ends.
serverpool
Established connections are shared with other proxy sessions.
http-incoming-port
Accept incoming HTTP requests on one or more
ports (0 - 65535, default = 8080).
user
Not
Specified
https-incoming-port
Accept incoming HTTPS requests on one or
more ports (0 - 65535, default = 0, use the
same as HTTP).
user
Not
Specified
https-replacement-message
Enable/disable sending the client a replacement
message for HTTPS requests.
option
-enable
Option
Description
enable
Display a replacement message for HTTPS requests.
disable
Do not display a replacement message for HTTPS requests.
incoming-ip
Restrict the explicit HTTP proxy to only accept
sessions from this IP address. An interface must
have this IP address.
ipv4-address-any
Not
Specified
0.0.0.0
FortiOS 8.0.0 CLI Reference
2599
Fortinet Inc.

<!-- 来源页 2600 -->
Parameter
Description
Type
Size
Default
incoming-ip6
Restrict the explicit web proxy to only accept
sessions from this IPv6 address. An interface
must have this IPv6 address.
ipv6-address
Not
Specified
::
interface
Specify outgoing interface to reach server.
string
Maximum
length: 15
interface-select-method
Specify how to select outgoing interface to
reach server.
option
-sdwan
Option
Description
sdwan
Set outgoing interface by SD-WAN or policy routing rules.
specify
Set outgoing interface manually.
ipv6-status
Enable/disable allowing an IPv6 web proxy
destination in policies and all IPv6 related
entries in this command.
option
-disable
Option
Description
enable
Enable allowing an IPv6 web proxy destination.
disable
Disable allowing an IPv6 web proxy destination.
message-upon-server-error
Enable/disable displaying a replacement
message when a server error is detected.
option
-enable
Option
Description
enable
Display a replacement message when a server error is detected.
disable
Do not display a replacement message when a server error is
detected.
outgoing-ip
Outgoing HTTP requests will have this IP
address as their source address. An interface
must have this IP address.
ipv4-address-any
Not
Specified
outgoing-ip6
Outgoing HTTP requests will leave this IPv6.
Multiple interfaces can be specified. Interfaces
must have these IPv6 addresses.
ipv6-address
Not
Specified
pac-file-data
PAC file contents enclosed in quotes (maximum
of 256K bytes).
user
Not
Specified
pac-file-name
Pac file name.
string
Maximum
length: 63
proxy.pac
FortiOS 8.0.0 CLI Reference
2600
Fortinet Inc.

<!-- 来源页 2601 -->
Parameter
Description
Type
Size
Default
pac-file-server-port
Port number that PAC traffic from client web
browsers uses to connect to the explicit web
proxy (0 - 65535, default = 0; use the same as
HTTP).
user
Not
Specified
pac-file-server-status
Enable/disable Proxy Auto-Configuration (PAC)
for users of this explicit proxy profile.
option
-disable
Option
Description
enable
Enable Proxy Auto-Configuration (PAC).
disable
Disable Proxy Auto-Configuration (PAC).
pac-file-through-https
Enable/disable to get Proxy Auto-Configuration
(PAC) through HTTPS.
option
-disable
Option
Description
enable
Enable to get Proxy Auto-Configuration (PAC) through HTTPS.
disable
Disable to get Proxy Auto-Configuration (PAC) through HTTPS.
pac-file-url
PAC file access URL. Read-only.
user
Not
Specified
pref-dns-result
Prefer resolving addresses using the configured
IPv4 or IPv6 DNS server (default = ipv4).
option
-ipv4
Option
Description
ipv4
Send the IPv4 request first and then the IPv6 request. Use the DNS
response that returns to the FortiGate first.
ipv6
Send the IPv6 request first and then the IPv4 request. Use the DNS
response that returns to the FortiGate first.
ipv4-strict
Use the IPv4 DNS response. If the IPv6 DNS response arrives first,
wait 50ms for the IPv4 response and then use the IPv4 response,
otherwise the IPv6.
ipv6-strict
Use the IPv6 DNS response. If the IPv4 DNS response arrives first,
wait 50ms for the IPv6 response and then use the IPv6 response,
otherwise the IPv4.
realm
Authentication realm used to identify the
explicit web proxy (maximum of 63 characters).
string
Maximum
length: 63
default
sec-default-action
Accept or deny explicit web proxy sessions
when no web proxy firewall policy exists.
option
-deny
FortiOS 8.0.0 CLI Reference
2601
Fortinet Inc.

<!-- 来源页 2602 -->
Parameter
Description
Type
Size
Default
Option
Description
accept
Accept requests. All explicit web proxy traffic is accepted whether
there is an explicit web proxy policy or not.
deny
Deny requests unless there is a matching explicit web proxy policy.
secure-web-proxy
Enable/disable/require the secure web proxy for
HTTP and HTTPS session.
option
-disable
Option
Description
disable
Disable secure webproxy.
enable
Enable secure webproxy access.
secure
Require secure webproxy access.
secure-web-proxy-cert
<name>
Name of certificates for secure web proxy.
Certificate list.
string
Maximum
length: 79
socks
Enable/disable the SOCKS proxy.
option
-disable
Option
Description
enable
Enable the SOCKS proxy.
disable
Disable the SOCKS proxy.
socks-incoming-port
Accept incoming SOCKS proxy requests on one
or more ports (0 - 65535, default = 0; use the
same as HTTP).
user
Not
Specified
ssl-algorithm
Relative strength of encryption algorithms
accepted in HTTPS deep scan: high, medium, or
low.
option
-low
Option
Description
high
High encrption. Allow only AES and ChaCha.
medium
Medium encryption. Allow AES, ChaCha, 3DES, and RC4.
low
Low encryption. Allow AES, ChaCha, 3DES, RC4, and DES.
ssl-dh-bits
Bit-size of Diffie-Hellman (DH) prime used in
DHE-RSA negotiation (default = 2048).
option
-2048
Option
Description
768
768-bit Diffie-Hellman prime.
FortiOS 8.0.0 CLI Reference
2602
Fortinet Inc.

<!-- 来源页 2603 -->
Parameter
Description
Type
Size
Default
Option
Description
1024
1024-bit Diffie-Hellman prime.
1536
1536-bit Diffie-Hellman prime.
2048
2048-bit Diffie-Hellman prime.
status
Enable/disable the explicit Web proxy for HTTP
and HTTPS session.
option
-disable
Option
Description
enable
Enable the explicit web proxy.
disable
Disable the explicit web proxy.
strict-guest
Enable/disable strict guest user checking by the
explicit web proxy.
option
-disable
Option
Description
enable
Enable strict guest user checking.
disable
Disable strict guest user checking.
trace-auth-no-rsp
Enable/disable logging timed-out
authentication requests.
option
-disable
Option
Description
enable
Enable logging timed-out authentication requests.
disable
Disable logging timed-out authentication requests.
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
best-effort
Assume all HTTP sessions comply with HTTP 0.9, 1.0, or 1.1. If a
session uses a different HTTP version, it may not parse correctly and
the connection may be lost.
user-agent-detect
Enable/disable to detect device type by HTTP
user-agent if no client certificate provided.
option
-enable
FortiOS 8.0.0 CLI Reference
2603
Fortinet Inc.

<!-- 来源页 2604 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable to detect unknown device by HTTP user-agent if no client
certificate provided.
enable
Enable to detect unknown device by HTTP user-agent if no client
certificate provided.
vrf-select
VRF ID used for connection to server.
integer
Minimum
value: 0
Maximum
value: 511
-1
* This parameter may not exist in some models.
config pac-policy
Parameter
Description
Type
Size
Default
comments
Optional comments.
var-string
Maximum
length:
1023
dstaddr
<name>
Destination address objects.
Address name.
string
Maximum
length: 79
pac-file-data
PAC file contents enclosed in quotes (maximum of
256K bytes).
user
Not
Specified
pac-file-name
Pac file name.
string
Maximum
length: 63
proxy.pac
policyid
Policy ID.
integer
Minimum
value: 1
Maximum
value: 100
0
srcaddr
<name>
Source address objects.
Address name.
string
Maximum
length: 79
srcaddr6
<name>
Source address6 objects.
Address name.
string
Maximum
length: 79
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
FortiOS 8.0.0 CLI Reference
2604
Fortinet Inc.

<!-- 来源页 2605 -->
config web-proxy fast-fallback
Proxy destination connection fast-fallback.
config web-proxy fast-fallback
Description: Proxy destination connection fast-fallback.
edit <name>
set connection-mode [sequentially|simultaneously]
set connection-timeout {integer}
set protocol [IPv4-first|IPv6-first|...]
set status [enable|disable]
next
end
config web-proxy fast-fallback
Parameter
Description
Type
Size
Default
connection-mode
Connection mode for multiple destinations.
option
-sequentially
Option
Description
sequentially
Connect the different destinations sequentially.
simultaneously
Connect the different destinations simultaneously.
connection-timeout
Number of milliseconds to wait before starting
another connection (200 - 1800000, default =
200). For sequential connection-mode only.
integer
Minimum
value: 200
Maximum
value:
1800000
200
name
Configure a name for the fast-fallback entry.
string
Maximum
length: 63
protocol
Connection protocols for multiple destinations.
option
-IPv4-first
Option
Description
IPv4-first
Connect IPv4 destinations first.
IPv6-first
Connect IPv6 destinations first.
IPv4-only
Connect IPv4 destinations only.
IPv6-only
Connect IPv6 destinations only.
status
Enable/disable the fast-fallback entry.
option
-enable
FortiOS 8.0.0 CLI Reference
2605
Fortinet Inc.

<!-- 来源页 2606 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable Status of the entry.
disable
Disable Status of the entry.
config web-proxy forward-server
Configure forward-server addresses.
config web-proxy forward-server
Description: Configure forward-server addresses.
edit <name>
set addr-type [ip|ipv6|...]
set comment {string}
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set fqdn {string}
set healthcheck [disable|enable]
set interface {string}
set interface-select-method [sdwan|specify]
set ip {ipv4-address-any}
set ipv6 {ipv6-address}
set masquerade [enable|disable]
set monitor {string}
set password {password}
set port {integer}
set server-down-option [block|pass]
set username {string}
set uuid {uuid}
set vrf-select {integer}
next
end
config web-proxy forward-server
Parameter
Description
Type
Size
Default
addr-type
Address type of the forwarding proxy
server: IP or FQDN.
option
-ip
Option
Description
ip
Use an IPv4 address for the forwarding proxy server.
FortiOS 8.0.0 CLI Reference
2606
Fortinet Inc.

<!-- 来源页 2607 -->
Parameter
Description
Type
Size
Default
Option
Description
ipv6
Use an IPv6 address for the forwarding proxy server.
fqdn
Use the FQDN for the forwarding proxy server.
comment
Comment.
string
Maximum
length: 63
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
fqdn
Forward server Fully Qualified Domain
Name (FQDN).
string
Maximum
length: 255
healthcheck
Enable/disable forward server health
checking. Attempts to connect through
the remote forwarding server to a
destination to verify that the forwarding
server is operating normally.
option
-disable
FortiOS 8.0.0 CLI Reference
2607
Fortinet Inc.

<!-- 来源页 2608 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable health checking.
enable
Enable health checking.
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
-sdwan
Option
Description
sdwan
Set outgoing interface by SD-WAN or policy routing rules.
specify
Set outgoing interface manually.
ip
Forward proxy server IP address.
ipv4-address-any
Not
Specified
0.0.0.0
ipv6
Forward proxy server IPv6 address.
ipv6-address
Not
Specified
::
masquerade
Enable/disable use of the IP address of
the outgoing interface as the client IP
address (default = enable)
option
-enable
Option
Description
enable
Enable use of the IP address of the outgoing interface as the client IP
address.
disable
Disable use of the IP address of the outgoing interface as the client IP
address.
monitor
URL for forward server health check
monitoring (default = www.google.com).
string
Maximum
length: 255
www.google.com
name
Server name.
string
Maximum
length: 63
password
HTTP authentication password.
password
Not
Specified
port
Port number that the forwarding server
expects to receive HTTP sessions on (1 -65535, default = 3128).
integer
Minimum
value: 1
Maximum
value:
65535
3128
FortiOS 8.0.0 CLI Reference
2608
Fortinet Inc.

<!-- 来源页 2609 -->
Parameter
Description
Type
Size
Default
server-down-option
Action to take when the forward server
is found to be down: block sessions until
the server is back up or pass sessions to
their destination.
option
-block
Option
Description
block
Block sessions until the server is back up.
pass
Pass sessions to their destination bypassing the forward server.
username
HTTP authentication user name.
string
Maximum
length: 64
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
vrf-select
VRF ID used for connection to server.
integer
Minimum
value: 0
Maximum
value: 511
-1
* This parameter may not exist in some models.
config web-proxy forward-server-group
Configure a forward server group consisting or multiple forward servers. Supports failover and load balancing.
config web-proxy forward-server-group
Description: Configure a forward server group consisting or multiple forward servers. Supports
failover and load balancing.
edit <name>
set affinity [enable|disable]
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set group-down-option [block|pass]
set ldb-method [weighted|least-session|...]
config server-list
Description: Add web forward servers to a list to form a server group. Optionally
assign weights to each server.
edit <name>
set weight {integer}
next
end
set uuid {uuid}
next
end
FortiOS 8.0.0 CLI Reference
2609
Fortinet Inc.

<!-- 来源页 2610 -->
config web-proxy forward-server-group
Parameter
Description
Type
Size
Default
affinity
Enable/disable affinity, attaching a source-ip's traffic to the assigned forwarding server
until the forward-server-affinity-timeout is
reached (under web-proxy global).
option
-enable
Option
Description
enable
Enable affinity.
disable
Disable affinity.
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
group-down-option
Action to take when all of the servers in the
forward server group are down: block
sessions until at least one server is back up
or pass sessions to their destination.
option
-block
FortiOS 8.0.0 CLI Reference
2610
Fortinet Inc.

<!-- 来源页 2611 -->
Parameter
Description
Type
Size
Default
Option
Description
block
Block sessions until at least one server in the group is back up.
pass
Pass sessions to their destination bypassing servers in the forward
server group.
ldb-method
Load balance method: weighted or least-session.
option
-weighted
Option
Description
weighted
Load balance traffic to forward servers based on assigned weights.
Weights are ratios of total number of sessions.
least-session
Send new sessions to the server with lowest session count.
active-passive
Send new sessions to the next active server in the list. Servers are
selected with highest weight first and then in order as they are
configured. Traffic switches back to the first server upon failure
recovery.
name
Configure a forward server group consisting
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
Forward server name.
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
config web-proxy global
Configure Web proxy global settings.
FortiOS 8.0.0 CLI Reference
2611
Fortinet Inc.

<!-- 来源页 2612 -->
config web-proxy global
Description: Configure Web proxy global settings.
set always-learn-client-ip [enable|disable]
set auth-sign-timeout {integer}
set fast-policy-match [enable|disable]
set forward-proxy-auth [enable|disable]
set forward-server-affinity-timeout {integer}
set http2-client-window-size {integer}
set http2-server-window-size {integer}
set ldap-user-cache [enable|disable]
set learn-client-ip [enable|disable]
set learn-client-ip-from-header {option1}, {option2}, ...
set learn-client-ip-srcaddr <name1>, <name2>, ...
set learn-client-ip-srcaddr6 <name1>, <name2>, ...
set log-app-id [enable|disable]
set log-forward-server [enable|disable]
set log-policy-pending [enable|disable]
set max-message-length {integer}
set max-request-length {integer}
set max-waf-body-cache-length {integer}
set policy-partial-match [enable|disable]
set proxy-fqdn {string}
set proxy-transparent-cert-inspection [enable|disable]
set request-obs-fold [replace-with-sp|block|...]
set src-affinity-exempt-addr {ipv4-address-any}
set src-affinity-exempt-addr6 {ipv6-address}
set ssl-ca-cert {string}
set ssl-cert {string}
set strict-web-check [enable|disable]
set webproxy-profile {string}
end
config web-proxy global
Parameter
Description
Type
Size
Default
always-learn-client-ip
Enable/disable learning the client's IP
address from headers for every request.
option
-disable
Option
Description
enable
Enable learning the client's IP address from headers for every request.
disable
Disable learning the client's IP address from headers for every request.
auth-sign-timeout
Proxy auth query sign timeout in seconds
(30 - 3600, default = 120).
integer
Minimum
value: 30
Maximum
value: 3600
120
FortiOS 8.0.0 CLI Reference
2612
Fortinet Inc.

<!-- 来源页 2613 -->
Parameter
Description
Type
Size
Default
fast-policy-match
Enable/disable fast matching algorithm for
explicit and transparent proxy policy.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
forward-proxy-auth
Enable/disable forwarding proxy
authentication headers.
option
-disable
Option
Description
enable
Enable forwarding proxy authentication headers.
disable
Disable forwarding proxy authentication headers.
forward-server-affinity-timeout
Period of time before the source IP's traffic
is no longer assigned to the forwarding
server (6 - 60 min, default = 30).
integer
Minimum
value: 6
Maximum
value: 60
30
http2-client-window-size
HTTP/2 client initial window size in bytes
(65535 - 2147483647, default = 1048576
(1MB)).
integer
Minimum
value: 65535
Maximum
value:
2147483647
1048576
http2-server-window-size
HTTP/2 server initial window size in bytes
(65535 - 2147483647, default = 1048576
(1MB)).
integer
Minimum
value: 65535
Maximum
value:
2147483647
1048576
ldap-user-cache
Enable/disable LDAP user cache for explicit
and transparent proxy user.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
learn-client-ip
Enable/disable learning the client's IP
address from headers.
option
-disable
Option
Description
enable
Enable learning the client's IP address from headers.
disable
Disable learning the client's IP address from headers.
FortiOS 8.0.0 CLI Reference
2613
Fortinet Inc.

<!-- 来源页 2614 -->
Parameter
Description
Type
Size
Default
learn-client-ip-from-header
Learn client IP address from the specified
headers.
option
-Option
Description
true-client-ip
Learn the client IP address from the True-Client-IP header.
x-real-ip
Learn the client IP address from the X-Real-IP header.
x-forwarded-for
Learn the client IP address from the X-Forwarded-For header.
learn-client-ip-srcaddr
<name>
Source address name (srcaddr or srcaddr6
must be set).
Address name.
string
Maximum
length: 79
learn-client-ip-srcaddr6
<name>
IPv6 Source address name (srcaddr or
srcaddr6 must be set).
Address name.
string
Maximum
length: 79
log-app-id
Enable/disable always log application type
in traffic log.
option
-disable
Option
Description
enable
Enable logging application type in traffic log.
disable
Disable logging application type in traffic log.
log-forward-server
Enable/disable forward server name
logging in forward traffic log.
option
-disable
Option
Description
enable
Enable logging forward server name in forward traffic log.
disable
Disable logging forward server name in forward traffic log.
log-policy-pending
Enable/disable logging sessions that are
pending on policy matching.
option
-disable
Option
Description
enable
Enable logging sessions that are pending on policy matching.
disable
Disable logging sessions that are pending on policy matching.
max-message-length
Maximum length of HTTP message, not
including body (16 - 256 Kbytes, default =
32).
integer
Minimum
value: 16
Maximum
value: 256
32
FortiOS 8.0.0 CLI Reference
2614
Fortinet Inc.

<!-- 来源页 2615 -->
Parameter
Description
Type
Size
Default
max-request-length
Maximum length of HTTP request line (2 -64 Kbytes, default = 8).
integer
Minimum
value: 2
Maximum
value: 64
8
max-waf-body-cache-length
Maximum length of HTTP messages
processed by Web Application Firewall
(WAF) (1 - 1024 Kbytes, default = 1).
integer
Minimum
value: 1
Maximum
value: 1024
1
policy-partial-match
Enable/disable policy partial matching.
option
-enable
Option
Description
enable
Enable policy partial matching.
disable
Disable policy partial matching.
proxy-fqdn
Fully Qualified Domain Name of the explicit
web proxy (default = default.fqdn) that
clients connect to.
string
Maximum
length: 255
default.fqdn
proxy-transparent-cert-inspection
Enable/disable transparent proxy
certificate inspection.
option
-disable
Option
Description
enable
Enable proxying certificate inspection in transparent mode.
disable
Disable proxying certificate inspection in transparent mode.
request-obs-fold
Action when HTTP/1.x request header
contains obs-fold (default = keep).
option
-keep
Option
Description
replace-with-sp
Replace CRLF in obs-fold with SP in the request header for HTTP/1.x.
block
Block HTTP/1.x request with obs-fold.
keep
Keep obs-fold in the request header for HTTP/1.x. There are known
security risks.
src-affinity-exempt-addr
IPv4 source addresses to exempt proxy
affinity.
ipv4-address-any
Not Specified
FortiOS 8.0.0 CLI Reference
2615
Fortinet Inc.

<!-- 来源页 2616 -->
Parameter
Description
Type
Size
Default
src-affinity-exempt-addr6
IPv6 source addresses to exempt proxy
affinity.
ipv6-address
Not Specified
ssl-ca-cert
SSL CA certificate for SSL interception.
string
Maximum
length: 35
Fortinet_CA_
SSL
ssl-cert
SSL certificate for SSL interception.
string
Maximum
length: 35
Fortinet_
Factory **
strict-web-check
Enable/disable strict web checking to block
web sites that send incorrect headers that
don't conform to HTTP.
option
-disable
Option
Description
enable
Enable strict web checking.
disable
Disable strict web checking.
webproxy-profile
Name of the web proxy profile to apply
when explicit proxy traffic is allowed by
default and traffic is accepted that does
not match an explicit proxy policy.
string
Maximum
length: 63
** Values may differ between models.
config web-proxy isolator-server
Configure forward-server addresses.
config web-proxy isolator-server
Description: Configure forward-server addresses.
edit <name>
set addr-type [ip|ipv6|...]
set comment {string}
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set fqdn {string}
set interface {string}
set interface-select-method [sdwan|specify]
set ip {ipv4-address-any}
set ipv6 {ipv6-address}
set masquerade [enable|disable]
set port {integer}
set uuid {uuid}
set vrf-select {integer}
next
end
FortiOS 8.0.0 CLI Reference
2616
Fortinet Inc.

<!-- 来源页 2617 -->
config web-proxy isolator-server
Parameter
Description
Type
Size
Default
addr-type
Address type of the forwarding proxy
server: IP or FQDN.
option
-ip
Option
Description
ip
Use an IPv4 address for the forwarding proxy server.
ipv6
Use an IPv6 address for the forwarding proxy server.
fqdn
Use the FQDN for the forwarding proxy server.
comment
Comment.
string
Maximum
length: 63
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
fqdn
Forward server Fully Qualified Domain
Name (FQDN).
string
Maximum
length: 255
interface
Specify outgoing interface to reach server.
string
Maximum
length: 15
FortiOS 8.0.0 CLI Reference
2617
Fortinet Inc.

<!-- 来源页 2618 -->
Parameter
Description
Type
Size
Default
interface-select-method
Specify how to select outgoing interface to
reach server.
option
-sdwan
Option
Description
sdwan
Set outgoing interface by SD-WAN or policy routing rules.
specify
Set outgoing interface manually.
ip
Forward proxy server IP address.
ipv4-address-any
Not
Specified
0.0.0.0
ipv6
Forward proxy server IPv6 address.
ipv6-address
Not
Specified
::
masquerade
Enable/disable use of the IP address of the
outgoing interface as the client IP address
(default = enable)
option
-enable
Option
Description
enable
Enable use of the IP address of the outgoing interface as the client IP
address.
disable
Disable use of the IP address of the outgoing interface as the client IP
address.
name
Server name.
string
Maximum
length: 63
port
Port number that the forwarding server
expects to receive HTTP sessions on (1 -65535, default = 3128).
integer
Minimum
value: 1
Maximum
value:
65535
3128
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
vrf-select
VRF ID used for connection to server.
integer
Minimum
value: 0
Maximum
value: 511
-1
* This parameter may not exist in some models.
config web-proxy profile
Configure web proxy profiles.
FortiOS 8.0.0 CLI Reference
2618
Fortinet Inc.

<!-- 来源页 2619 -->
config web-proxy profile
Description: Configure web proxy profiles.
edit <name>
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set header-client-cert [pass|add|...]
set header-client-ip [pass|add|...]
set header-front-end-https [pass|add|...]
set header-via-request [pass|add|...]
set header-via-response [pass|add|...]
set header-x-authenticated-groups [pass|add|...]
set header-x-authenticated-user [pass|add|...]
set header-x-forwarded-client-cert [pass|add|...]
set header-x-forwarded-for [pass|add|...]
config headers
Description: Configure HTTP forwarded requests headers.
edit <id>
set action [add-to-request|add-to-response|...]
set add-option [append|new-on-not-found|...]
set base64-encoding [disable|enable]
set content {var-string}
set dstaddr <name1>, <name2>, ...
set dstaddr6 <name1>, <name2>, ...
set name {string}
set protocol {option1}, {option2}, ...
next
end
set log-header-change [enable|disable]
set strip-encoding [enable|disable]
set uuid {uuid}
next
end
config web-proxy profile
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
FortiOS 8.0.0 CLI Reference
2619
Fortinet Inc.

<!-- 来源页 2620 -->
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
header-client-cert
Action to take on the HTTP Client-Cert/Client-Cert-Chain headers in
forwarded responses: forwards (pass),
adds, or removes the HTTP header.
option
-pass
Option
Description
pass
Forward the same HTTP header.
add
Add the HTTP header.
remove
Remove the HTTP header.
header-client-ip
Action to take on the HTTP client-IP
header in forwarded requests: forwards
(pass), adds, or removes the HTTP
header.
option
-pass
Option
Description
pass
Forward the same HTTP header.
add
Add the HTTP header.
remove
Remove the HTTP header.
FortiOS 8.0.0 CLI Reference
2620
Fortinet Inc.

<!-- 来源页 2621 -->
Parameter
Description
Type
Size
Default
header-front-end-https
Action to take on the HTTP front-end-HTTPS header in forwarded requests:
forwards (pass), adds, or removes the
HTTP header.
option
-pass
Option
Description
pass
Forward the same HTTP header.
add
Add the HTTP header.
remove
Remove the HTTP header.
header-via-request
Action to take on the HTTP via header in
forwarded requests: forwards (pass),
adds, or removes the HTTP header.
option
-pass
Option
Description
pass
Forward the same HTTP header.
add
Add the HTTP header.
remove
Remove the HTTP header.
header-via-response
Action to take on the HTTP via header in
forwarded responses: forwards (pass),
adds, or removes the HTTP header.
option
-pass
Option
Description
pass
Forward the same HTTP header.
add
Add the HTTP header.
remove
Remove the HTTP header.
header-x-authenticated-groups
Action to take on the HTTP x-authenticated-groups header in
forwarded requests: forwards (pass),
adds, or removes the HTTP header.
option
-pass
Option
Description
pass
Forward the same HTTP header.
add
Add the HTTP header.
remove
Remove the HTTP header.
FortiOS 8.0.0 CLI Reference
2621
Fortinet Inc.

<!-- 来源页 2622 -->
Parameter
Description
Type
Size
Default
header-x-authenticated-user
Action to take on the HTTP x-authenticated-user header in forwarded
requests: forwards (pass), adds, or
removes the HTTP header.
option
-pass
Option
Description
pass
Forward the same HTTP header.
add
Add the HTTP header.
remove
Remove the HTTP header.
header-x-forwarded-client-cert
Action to take on the HTTP x-forwarded-client-cert header in forwarded requests:
forwards (pass), adds, or removes the
HTTP header.
option
-pass
Option
Description
pass
Forward the same HTTP header.
add
Add the HTTP header.
remove
Remove the HTTP header.
header-x-forwarded-for
Action to take on the HTTP x-forwarded-for header in forwarded requests:
forwards (pass), adds, or removes the
HTTP header.
option
-pass
Option
Description
pass
Forward the same HTTP header.
add
Add the HTTP header.
remove
Remove the HTTP header.
log-header-change
Enable/disable logging HTTP header
changes.
option
-disable
Option
Description
enable
Enable Enable/disable logging HTTP header changes.
disable
Disable Enable/disable logging HTTP header changes.
name
Profile name.
string
Maximum
length: 63
strip-encoding
Enable/disable stripping unsupported
encoding from the request header.
option
-disable
FortiOS 8.0.0 CLI Reference
2622
Fortinet Inc.

<!-- 来源页 2623 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable stripping of unsupported encoding from the request header.
disable
Disable stripping of unsupported encoding from the request header.
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
config headers
Parameter
Description
Type
Size
Default
action
Configure adding, removing, or logging of the
HTTP header entry in HTTP requests and
responses.
option
-add-to-request
Option
Description
add-to-request
Add the HTTP header to request.
add-to-response
Add the HTTP header to response.
remove-from-request
Remove the HTTP header from request.
remove-from-response
Remove the HTTP header from response.
monitor-request
Record the HTTP header in utm-webfilter log.
monitor-response
Record the HTTP header in utm-webfilter log.
add-option
Configure options to append content to existing
HTTP header or add new HTTP header.
option
-new
Option
Description
append
Append content to existing HTTP header or create new header if HTTP
header is not found.
new-on-not-found
Create new header only if existing HTTP header is not found.
new
Create new header regardless if existing HTTP header is found or not.
FortiOS 8.0.0 CLI Reference
2623
Fortinet Inc.

<!-- 来源页 2624 -->
Parameter
Description
Type
Size
Default
Option
Description
replace
Replace content to existing HTTP header or create new header if HTTP
header is not found.
replace-when-match
Replace content to existing HTTP header.
base64-encoding
Enable/disable use of base64 encoding of HTTP
content.
option
-disable
Option
Description
disable
Disable use of base64 encoding of HTTP content.
enable
Enable use of base64 encoding of HTTP content.
content
HTTP header content (0 - 16383).
var-string
**
Maximum
length: 16383
**
dstaddr
<name>
Destination address and address group names.
Address name.
string
Maximum
length: 79
dstaddr6
<name>
Destination address and address group names
(IPv6).
Address name.
string
Maximum
length: 79
id
HTTP forwarded header id.
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
protocol
Configure protocol(s) to take add-option action
on (HTTP, HTTPS, or both).
option
-https http
Option
Description
https
Perform add-option action on HTTPS.
http
Perform add-option action on HTTP.
** Values may differ between models.
config web-proxy url-match
Exempt URLs from web proxy forwarding, caching and fast-fallback.
FortiOS 8.0.0 CLI Reference
2624
Fortinet Inc.

<!-- 来源页 2625 -->
config web-proxy url-match
Description: Exempt URLs from web proxy forwarding, caching and fast-fallback.
edit <name>
set cache-exemption [enable|disable]
set comment {var-string}
set fast-fallback {string}
set forward-server {string}
set status [enable|disable]
set url-pattern {string}
next
end
config web-proxy url-match
Parameter
Description
Type
Size
Default
cache-exemption
Enable/disable exempting this URL pattern from
caching.
option
-disable
Option
Description
enable
Enable exempting this URL pattern from caching.
disable
Disable exempting this URL pattern from caching.
comment
Comment.
var-string
Maximum
length: 255
fast-fallback
Fast fallback configuration entry name.
string
Maximum
length: 63
forward-server
Forward server name.
string
Maximum
length: 63
name
Configure a name for the URL to be exempted.
string
Maximum
length: 63
status
Enable/disable exempting the URLs matching the
URL pattern from web proxy forwarding, caching
and fast-fallback.
option
-enable
Option
Description
enable
Enable exempting the matching URLs.
disable
Disable exempting the matching URLs.
url-pattern
URL pattern to be exempted from web proxy
forwarding, caching and fast-fallback.
string
Maximum
length: 511
FortiOS 8.0.0 CLI Reference
2625
Fortinet Inc.

<!-- 来源页 2626 -->
config web-proxy wisp
Configure Websense Integrated Services Protocol (WISP) servers.
config web-proxy wisp
Description: Configure Websense Integrated Services Protocol (WISP) servers.
edit <name>
set comment {var-string}
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set max-connections {integer}
set outgoing-ip {ipv4-address-any}
set server-ip {ipv4-address-any}
set server-port {integer}
set timeout {integer}
set uuid {uuid}
next
end
config web-proxy wisp
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
2626
Fortinet Inc.

<!-- 来源页 2627 -->
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
max-connections
Maximum number of web proxy WISP
connections (4 - 4096, default = 64).
integer
Minimum
value: 4
Maximum
value: 4096
64
name
Server name.
string
Maximum
length: 35
outgoing-ip
WISP outgoing IP address.
ipv4-address-any
Not
Specified
0.0.0.0
server-ip
WISP server IP address.
ipv4-address-any
Not
Specified
0.0.0.0
server-port
WISP server port (1 - 65535, default =
15868).
integer
Minimum
value: 1
Maximum
value:
65535
15868
timeout
Period of time before WISP requests time
out (1 - 15 sec, default = 5).
integer
Minimum
value: 1
Maximum
value: 15
5
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
FortiOS 8.0.0 CLI Reference
2627
Fortinet Inc.

---


<!-- 来源页 2628 -->
webfilter
This section includes syntax for the following commands:
l config webfilter content-header on page 2630
l config webfilter content on page 2628
l config webfilter fortiguard on page 2632
l config webfilter ftgd-local-cat on page 2634
l config webfilter ftgd-local-rating on page 2635
l config webfilter ftgd-local-risk on page 2636
l config webfilter ftgd-risk-level on page 2637
l config webfilter ips-urlfilter-cache-setting on page 2637
l config webfilter ips-urlfilter-setting on page 2638
l config webfilter ips-urlfilter-setting6 on page 2639
l config webfilter override on page 2639
l config webfilter profile on page 2641
l config webfilter search-engine on page 2659
l config webfilter urlfilter on page 2660
config webfilter content
Configure Web filter banned word table.
config webfilter content
Description: Configure Web filter banned word table.
edit <id>
set comment {var-string}
config entries
Description: Configure banned word entries.
edit <name>
set action [block|exempt]
set pattern-type [wildcard|regexp]
set score {integer}
set status [enable|disable]
next
end
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set name {string}
set uuid {uuid}
next
end
FortiOS 8.0.0 CLI Reference
2628
Fortinet Inc.

<!-- 来源页 2629 -->
config webfilter content
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
id
ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
name
Name of table.
string
Maximum
length: 63
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
FortiOS 8.0.0 CLI Reference
2629
Fortinet Inc.

<!-- 来源页 2630 -->
config entries
Parameter
Description
Type
Size
Default
action
Block or exempt word when a match is found.
option
-block
Option
Description
block
Block matches.
exempt
Exempt matches.
name
Banned word.
string
Maximum
length: 127
pattern-type
Banned word pattern type: wildcard pattern or
Perl regular expression.
option
-wildcard
Option
Description
wildcard
Wildcard pattern.
regexp
Perl regular expression.
score
Score, to be applied every time the word
appears on a web page (0 - 4294967295,
default = 10).
integer
Minimum value:
0 Maximum
value:
4294967295
10
status
Enable/disable banned word.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
config webfilter content-header
Configure content types used by Web filter.
config webfilter content-header
Description: Configure content types used by Web filter.
edit <id>
set comment {var-string}
config entries
Description: Configure content types used by web filter.
edit <pattern>
set action [block|allow|...]
set category {user}
next
end
FortiOS 8.0.0 CLI Reference
2630
Fortinet Inc.

<!-- 来源页 2631 -->
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set name {string}
set uuid {uuid}
next
end
config webfilter content-header
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
2631
Fortinet Inc.

<!-- 来源页 2632 -->
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
Name of table.
string
Maximum
length: 63
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
config entries
Parameter
Description
Type
Size
Default
action
Action to take for this content type.
option
-allow
Option
Description
block
Block content type.
allow
Allow content type.
exempt
Exempt content type.
category
Categories that this content type applies to.
user
Not
Specified
all
pattern
Content type (regular expression).
string
Maximum
length: 31
config webfilter fortiguard
Configure FortiGuard Web Filter service.
config webfilter fortiguard
Description: Configure FortiGuard Web Filter service.
set cache-mem-permille {integer}
set cache-mode [ttl|db-ver]
set cache-prefix-match [enable|disable]
set close-ports [enable|disable]
set embed-image [enable|disable]
set ovrd-auth-https [enable|disable]
set ovrd-auth-port-http {integer}
set ovrd-auth-port-https {integer}
set ovrd-auth-port-https-flow {integer}
FortiOS 8.0.0 CLI Reference
2632
Fortinet Inc.

<!-- 来源页 2633 -->
set ovrd-auth-port-warning {integer}
set request-packet-size-limit {integer}
set warn-auth-https [enable|disable]
end
config webfilter fortiguard
Parameter
Description
Type
Size
Default
cache-mem-permille
Maximum permille of available memory allocated to
caching (1 - 150).
integer
Minimum
value: 1
Maximum
value: 150
1
cache-mode
Cache entry expiration mode.
option
-ttl
Option
Description
ttl
Expire cache items by time-to-live.
db-ver
Expire cache items when the server DB version changes.
cache-prefix-match
Enable/disable prefix matching in the cache.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
close-ports
Close ports used for HTTP/HTTPS override
authentication and disable user overrides.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
embed-image
Enable/disable embedding images into
replacement messages (default = enable).
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
ovrd-auth-https
Enable/disable use of HTTPS for override
authentication.
option
-enable
FortiOS 8.0.0 CLI Reference
2633
Fortinet Inc.

<!-- 来源页 2634 -->
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
ovrd-auth-port-http
Port to use for FortiGuard Web Filter HTTP override
authentication.
integer
Minimum
value: 0
Maximum
value:
65535
8008
ovrd-auth-port-https
Port to use for FortiGuard Web Filter HTTPS
override authentication in proxy mode.
integer
Minimum
value: 0
Maximum
value:
65535
8010
ovrd-auth-port-https-flow
Port to use for FortiGuard Web Filter HTTPS
override authentication in flow mode.
integer
Minimum
value: 0
Maximum
value:
65535
8015
ovrd-auth-port-warning
Port to use for FortiGuard Web Filter Warning
override authentication.
integer
Minimum
value: 0
Maximum
value:
65535
8020
request-packet-size-limit
Limit size of URL request packets sent to
FortiGuard server (0 for default).
integer
Minimum
value: 576
Maximum
value:
10000
0
warn-auth-https
Enable/disable use of HTTPS for warning and
authentication.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
config webfilter ftgd-local-cat
Configure FortiGuard Web Filter local categories.
FortiOS 8.0.0 CLI Reference
2634
Fortinet Inc.

<!-- 来源页 2635 -->
config webfilter ftgd-local-cat
Description: Configure FortiGuard Web Filter local categories.
edit <desc>
set id {integer}
set status [enable|disable]
set urlfilter-table {integer}
next
end
config webfilter ftgd-local-cat
Parameter
Description
Type
Size
Default
desc
Local category description.
string
Maximum
length: 79
id
Local category ID.
integer
Minimum value:
140 Maximum
value: 191
0
status
Enable/disable the local category.
option
-enable
Option
Description
enable
Enable the local category.
disable
Disable the local category.
urlfilter-table
*
Local URL list.
integer
Minimum value:
0 Maximum
value:
4294967295
0
* This parameter may not exist in some models.
config webfilter ftgd-local-rating
Configure local FortiGuard Web Filter local ratings.
config webfilter ftgd-local-rating
Description: Configure local FortiGuard Web Filter local ratings.
edit <url>
set comment {var-string}
set rating {user}
set status [enable|disable]
next
end
FortiOS 8.0.0 CLI Reference
2635
Fortinet Inc.

<!-- 来源页 2636 -->
config webfilter ftgd-local-rating
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
rating
Local rating.
user
Not
Specified
status
Enable/disable local rating.
option
-enable
Option
Description
enable
Enable local rating.
disable
Disable local rating.
url
URL to rate locally.
string
Maximum
length: 511
config webfilter ftgd-local-risk
Configure FortiGuard Web Filter local risk score.
config webfilter ftgd-local-risk
Description: Configure FortiGuard Web Filter local risk score.
edit <url>
set comment {var-string}
set risk-score {integer}
set status [enable|disable]
next
end
config webfilter ftgd-local-risk
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
risk-score
Local risk score.
integer
Minimum
value: 0
Maximum
value: 100
0
status
Enable/disable local risk score.
option
-enable
FortiOS 8.0.0 CLI Reference
2636
Fortinet Inc.

<!-- 来源页 2637 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable local risk level.
disable
Disable local risk level.
url
URL to rate locally.
string
Maximum
length: 511
config webfilter ftgd-risk-level
Configure FortiGuard Web Filter risk level.
config webfilter ftgd-risk-level
Description: Configure FortiGuard Web Filter risk level.
edit <name>
set high {integer}
set low {integer}
next
end
config webfilter ftgd-risk-level
Parameter
Description
Type
Size
Default
high
Risk level high.
integer
Minimum
value: 0
Maximum
value: 100
0
low
Risk level low.
integer
Minimum
value: 0
Maximum
value: 100
0
name
Risk level name.
string
Maximum
length: 35
config webfilter ips-urlfilter-cache-setting
Configure IPS URL filter cache settings.
config webfilter ips-urlfilter-cache-setting
Description: Configure IPS URL filter cache settings.
set dns-retry-interval {integer}
FortiOS 8.0.0 CLI Reference
2637
Fortinet Inc.

<!-- 来源页 2638 -->
set extended-ttl {integer}
end
config webfilter ips-urlfilter-cache-setting
Parameter
Description
Type
Size
Default
dns-retry-interval
Retry interval. Refresh DNS faster than TTL to
capture multiple IPs for hosts. 0 means use DNS
server's TTL only.
integer
Minimum
value: 0
Maximum
value:
2147483
0
extended-ttl
Extend time to live beyond reported by DNS. Use
of 0 means use DNS server's TTL.
integer
Minimum
value: 0
Maximum
value:
2147483
0
config webfilter ips-urlfilter-setting
Configure IPS URL filter settings.
config webfilter ips-urlfilter-setting
Description: Configure IPS URL filter settings.
set device {string}
set distance {integer}
set gateway {ipv4-address}
set geo-filter {var-string}
end
config webfilter ips-urlfilter-setting
Parameter
Description
Type
Size
Default
device
Interface for this route.
string
Maximum
length: 35
distance
Administrative distance (1 - 255) for this route.
integer
Minimum
value: 1
Maximum
value: 255
1
gateway
Gateway IP address for this route.
ipv4-address
Not
Specified
0.0.0.0
FortiOS 8.0.0 CLI Reference
2638
Fortinet Inc.

<!-- 来源页 2639 -->
Parameter
Description
Type
Size
Default
geo-filter
Filter based on geographical location. Route will
NOT be installed if the resolved IP address belongs
to the country in the filter.
var-string
Maximum
length: 255
config webfilter ips-urlfilter-setting6
Configure IPS URL filter settings for IPv6.
config webfilter ips-urlfilter-setting6
Description: Configure IPS URL filter settings for IPv6.
set device {string}
set distance {integer}
set gateway6 {ipv6-address}
set geo-filter {var-string}
end
config webfilter ips-urlfilter-setting6
Parameter
Description
Type
Size
Default
device
Interface for this route.
string
Maximum
length: 35
distance
Administrative distance (1 - 255) for this route.
integer
Minimum
value: 1
Maximum
value: 255
1
gateway6
Gateway IPv6 address for this route.
ipv6-address
Not
Specified
::
geo-filter
Filter based on geographical location. Route will
NOT be installed if the resolved IPv6 address
belongs to the country in the filter.
var-string
Maximum
length: 255
config webfilter override
Configure FortiGuard Web Filter administrative overrides.
config webfilter override
Description: Configure FortiGuard Web Filter administrative overrides.
edit <id>
set expires {user}
set initiator {string}
set ip {ipv4-address}
FortiOS 8.0.0 CLI Reference
2639
Fortinet Inc.

<!-- 来源页 2640 -->
set ip6 {ipv6-address}
set new-profile {string}
set old-profile {string}
set scope [user|user-group|...]
set status [enable|disable]
set user {string}
set user-group {string}
next
end
config webfilter override
Parameter
Description
Type
Size
Default
expires
Override expiration date and time, from 5
minutes to 365 from now (format:
yyyy/mm/dd hh:mm:ss).
user
Not Specified
1969/12/31
16:00:00 **
id
Override rule ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
initiator
Initiating user of override (read-only setting).
string
Maximum
length: 64
ip
IPv4 address which the override applies.
ipv4-address
Not Specified
0.0.0.0
ip6
IPv6 address which the override applies.
ipv6-address
Not Specified
::
new-profile
Name of the new web filter profile used by the
override.
string
Maximum
length: 47
old-profile
Name of the web filter profile which the
override applies.
string
Maximum
length: 47
scope
Override either the specific user, user group,
IPv4 address, or IPv6 address.
option
-user
Option
Description
user
Override the specified user.
user-group
Override the specified user group.
ip
Override the specified IP address.
ip6
Override the specified IPv6 address.
status
Enable/disable override rule.
option
-disable
FortiOS 8.0.0 CLI Reference
2640
Fortinet Inc.

<!-- 来源页 2641 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable override rule.
disable
Disable override rule.
user
Name of the user which the override applies.
string
Maximum
length: 64
user-group
Specify the user group for which the override
applies.
string
Maximum
length: 63
** Values may differ between models.
config webfilter profile
Configure Web filter profiles.
config webfilter profile
Description: Configure Web filter profiles.
edit <name>
config antiphish
Description: AntiPhishing profile.
set authentication [domain-controller|ldap]
set check-basic-auth [enable|disable]
set check-uri [enable|disable]
set check-username-only [enable|disable]
config custom-patterns
Description: Custom username and password regex patterns.
edit <pattern>
set category [username|password]
set type [regex|literal]
next
end
set default-action [exempt|log|...]
set domain-controller {string}
config inspection-entries
Description: AntiPhishing entries.
edit <name>
set action [exempt|log|...]
set fortiguard-category {user}
next
end
set ldap {string}
set max-body-len {integer}
set status [enable|disable]
end
set comment {var-string}
set extended-log [enable|disable]
FortiOS 8.0.0 CLI Reference
2641
Fortinet Inc.

<!-- 来源页 2642 -->
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set feature-set [flow|proxy]
config ftgd-wf
Description: FortiGuard Web Filter settings.
set exempt-quota {user}
config filters
Description: FortiGuard filters.
edit <id>
set action [block|authenticate|...]
set auth-usr-grp <name1>, <name2>, ...
set category {integer}
set log [enable|disable]
set override-replacemsg {string}
set warn-duration {user}
set warning-duration-type [session|timeout]
set warning-prompt [per-domain|per-category]
next
end
set max-quota-timeout {integer}
set options {option1}, {option2}, ...
set ovrd {user}
config quota
Description: FortiGuard traffic quota settings.
edit <id>
set category {user}
set duration {user}
set override-replacemsg {string}
set type [time|traffic]
set unit [B|KB|...]
set value {integer}
next
end
set rate-crl-urls [disable|enable]
set rate-css-urls [disable|enable]
set rate-javascript-urls [disable|enable]
config risk
Description: FortiGuard risk level settings.
edit <id>
set action [block|monitor]
set log [enable|disable]
set risk-level {string}
next
end
end
set https-replacemsg [enable|disable]
set log-all-url [enable|disable]
set options {option1}, {option2}, ...
config override
Description: Web Filter override settings.
set ovrd-cookie [allow|deny]
FortiOS 8.0.0 CLI Reference
2642
Fortinet Inc.

<!-- 来源页 2643 -->
set ovrd-dur {user}
set ovrd-dur-mode [constant|ask]
set ovrd-scope [user|user-group|...]
set ovrd-user-group <name1>, <name2>, ...
set profile <name1>, <name2>, ...
set profile-attribute [User-Name|NAS-IP-Address|...]
set profile-type [list|radius]
end
set ovrd-perm {option1}, {option2}, ...
set post-action [normal|block]
set replacemsg-group {string}
set uuid {uuid}
config web
Description: Web content filtering settings.
set allowlist {option1}, {option2}, ...
set blocklist [enable|disable]
set bword-table {integer}
set bword-threshold {integer}
set content-header-list {integer}
set keyword-match <pattern1>, <pattern2>, ...
set log-search [enable|disable]
set safe-search {option1}, {option2}, ...
set urlfilter-table {integer}
set vimeo-restrict {string}
set youtube-restrict [none|strict|...]
end
set web-antiphishing-log [enable|disable]
set web-content-log [enable|disable]
set web-extended-all-action-log [enable|disable]
set web-filter-activex-log [enable|disable]
set web-filter-applet-log [enable|disable]
set web-filter-command-block-log [enable|disable]
set web-filter-cookie-log [enable|disable]
set web-filter-cookie-removal-log [enable|disable]
set web-filter-js-log [enable|disable]
set web-filter-jscript-log [enable|disable]
set web-filter-referer-log [enable|disable]
set web-filter-unknown-log [enable|disable]
set web-filter-vbs-log [enable|disable]
set web-flow-log-encoding [utf-8|punycode]
set web-ftgd-err-log [enable|disable]
set web-ftgd-quota-usage [enable|disable]
set web-invalid-domain-log [enable|disable]
set web-url-log [enable|disable]
set wisp [enable|disable]
set wisp-algorithm [primary-secondary|round-robin|...]
set wisp-servers <name1>, <name2>, ...
next
end
FortiOS 8.0.0 CLI Reference
2643
Fortinet Inc.

<!-- 来源页 2644 -->
config webfilter profile
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
extended-log
Enable/disable extended logging for web
filtering.
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
Option
Description
member
Source of truth for this object is a non-root member of fabric.
local
Source of truth for this object is this security fabric member.
root
Source of truth for this object is the root of the fabric.
feature-set
Flow/proxy feature set.
option
-flow
Option
Description
flow
Flow feature set.
proxy
Proxy feature set.
FortiOS 8.0.0 CLI Reference
2644
Fortinet Inc.

<!-- 来源页 2645 -->
Parameter
Description
Type
Size
Default
https-replacemsg
Enable replacement messages for HTTPS.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
log-all-url
Enable/disable logging all URLs visited.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
name
Profile name.
string
Maximum
length: 47
options
Options.
option
-Option
Description
activexfilter
ActiveX filter.
cookiefilter
Cookie filter.
javafilter
Java applet filter.
block-invalid-url
Block sessions contained an invalid domain name.
jscript
Javascript block.
js
JS block.
vbs
VB script block.
unknown
Unknown script block.
intrinsic
Intrinsic script block.
wf-referer
Referring block.
wf-cookie
Cookie block.
per-user-bal
Per-user block/allow list filter
ovrd-perm
Permitted override types.
option
-Option
Description
bannedword-override
Banned word override.
FortiOS 8.0.0 CLI Reference
2645
Fortinet Inc.

<!-- 来源页 2646 -->
Parameter
Description
Type
Size
Default
Option
Description
urlfilter-override
URL filter override.
fortiguard-wf-override
FortiGuard Web Filter override.
contenttype-check-override
Content-type header override.
post-action
Action taken for HTTP POST traffic.
option
-normal
Option
Description
normal
Normal, POST requests are allowed.
block
POST requests are blocked.
replacemsg-group
Replacement message group.
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
web-antiphishing-log
Enable/disable logging of AntiPhishing
checks.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
web-content-log
Enable/disable logging logging blocked
web content.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
web-extended-all-action-log
Enable/disable extended any filter action
logging for web filtering.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
2646
Fortinet Inc.

<!-- 来源页 2647 -->
Parameter
Description
Type
Size
Default
web-filter-activex-log
Enable/disable logging ActiveX.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
web-filter-applet-log
Enable/disable logging Java applets.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
web-filter-command-block-log
Enable/disable logging blocked
commands.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
web-filter-cookie-log
Enable/disable logging cookie filtering.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
web-filter-cookie-removal-log
Enable/disable logging blocked cookies.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
web-filter-js-log
Enable/disable logging Java scripts.
option
-enable
FortiOS 8.0.0 CLI Reference
2647
Fortinet Inc.

<!-- 来源页 2648 -->
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
web-filter-jscript-log
Enable/disable logging JScripts.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
web-filter-referer-log
Enable/disable logging referrers.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
web-filter-unknown-log
Enable/disable logging unknown scripts.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
web-filter-vbs-log
Enable/disable logging VBS scripts.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
web-flow-log-encoding
Log encoding in flow mode.
option
-utf-8
Option
Description
utf-8
UTF-8 encoding.
punycode
Punycode encoding.
web-ftgd-err-log
Enable/disable logging rating errors.
option
-enable
FortiOS 8.0.0 CLI Reference
2648
Fortinet Inc.

<!-- 来源页 2649 -->
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
web-ftgd-quota-usage
Enable/disable logging daily quota usage.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
web-invalid-domain-log
Enable/disable logging invalid domain
names.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
web-url-log
Enable/disable logging URL filtering.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
wisp
Enable/disable web proxy WISP.
option
-disable
Option
Description
enable
Enable web proxy WISP.
disable
Disable web proxy WISP.
wisp-algorithm
WISP server selection algorithm.
option
-auto-learning
Option
Description
primary-secondary
Select the first healthy server in order.
round-robin
Select the next healthy server.
auto-learning
Select the lightest loading healthy server.
wisp-servers
<name>
WISP servers.
Server name.
string
Maximum
length: 79
* This parameter may not exist in some models.
FortiOS 8.0.0 CLI Reference
2649
Fortinet Inc.

<!-- 来源页 2650 -->
config antiphish
Parameter
Description
Type
Size
Default
authentication
Authentication methods.
option
-domain-controller
Option
Description
domain-controller
Domain Controller to verify user credential.
ldap
LDAP to verify user credential.
check-basic-auth
Enable/disable checking of HTTP Basic Auth
field for known credentials.
option
-disable
Option
Description
enable
Enable checking of HTTP Basic Auth field for known credentials.
disable
Disable checking of HTTP Basic Auth field for known credentials.
check-uri
Enable/disable checking of GET URI
parameters for known credentials.
option
-disable
Option
Description
enable
Enable checking of GET URI for username and password fields.
disable
Disable checking of GET URI for username and password fields.
check-username-only
Enable/disable username only matching of
credentials. Action will be taken for valid
usernames regardless of password validity.
option
-disable
Option
Description
enable
Enable username only credential matches.
disable
Disable username only credential matches.
default-action
Action to be taken when there is no matching
rule.
option
-exempt
Option
Description
exempt
Exempt requests from matching.
log
Log all matched requests.
block
Block all matched requests.
domain-controller
Domain for which to verify received
credentials against.
string
Maximum
length: 63
FortiOS 8.0.0 CLI Reference
2650
Fortinet Inc.

<!-- 来源页 2651 -->
Parameter
Description
Type
Size
Default
ldap
LDAP server for which to verify received
credentials against.
string
Maximum
length: 63
max-body-len
Maximum size of a POST body to check for
credentials.
integer
Minimum value:
0 Maximum
value:
4294967295
1024
status
Toggle AntiPhishing functionality.
option
-disable
Option
Description
enable
Enable AntiPhishing functionality.
disable
Disable AntiPhishing functionality.
config custom-patterns
Parameter
Description
Type
Size
Default
category
Category that the pattern matches.
option
-username
Option
Description
username
Pattern matches username fields.
password
Pattern matches password fields.
pattern
Target pattern.
string
Maximum
length: 255
type
Pattern will be treated either as a regex pattern or
literal string.
option
-regex
Option
Description
regex
Pattern will be treated as a regex pattern.
literal
Pattern will be treated as a literal string.
config inspection-entries
Parameter
Description
Type
Size
Default
action
Action to be taken upon an AntiPhishing match.
option
-exempt
Option
Description
exempt
Exempt requests from matching.
log
Log all matched requests.
FortiOS 8.0.0 CLI Reference
2651
Fortinet Inc.

<!-- 来源页 2652 -->
Parameter
Description
Type
Size
Default
Option
Description
block
Block all matched requests.
fortiguard-category
FortiGuard category to match.
user
Not
Specified
0
name
Inspection target name.
string
Maximum
length: 63
config ftgd-wf
Parameter
Description
Type
Size
Default
exempt-quota
Do not stop quota for these categories.
user
Not
Specified
17
max-quota-timeout
Maximum FortiGuard quota used by single page
view in seconds (excludes streams).
integer
Minimum
value: 1
Maximum
value:
86400
300
options
Options for FortiGuard Web Filter.
option
-ftgd-disable
Option
Description
error-allow
Allow web pages with a rating error to pass through.
rate-server-ip
Rate the server IP in addition to the domain name.
connect-request-bypass
Bypass connection which has CONNECT request.
ftgd-disable
Disable FortiGuard scanning.
ovrd
Allow web filter profile overrides.
user
Not
Specified
rate-crl-urls
Enable/disable rating CRL by URL.
option
-enable
Option
Description
disable
Disable rating CRL by URL.
enable
Enable rating CRL by URL.
rate-css-urls
Enable/disable rating CSS by URL.
option
-enable
FortiOS 8.0.0 CLI Reference
2652
Fortinet Inc.

<!-- 来源页 2653 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable rating CSS by URL.
enable
Enable rating CSS by URL.
rate-javascript-urls
Enable/disable rating JavaScript by URL.
option
-enable
Option
Description
disable
Disable rating JavaScript by URL.
enable
Enable rating JavaScript by URL.
config filters
Parameter
Description
Type
Size
Default
action
Action to take for matches.
option
-monitor
Option
Description
block
Block access.
authenticate
Authenticate user before allowing access.
monitor
Allow access while logging the action.
warning
Allow access after warning the user.
auth-usr-grp
<name>
Groups with permission to authenticate.
User group name.
string
Maximum
length: 79
category
Categories and groups the filter examines.
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
value: 255
0
log
Enable/disable logging.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
2653
Fortinet Inc.

<!-- 来源页 2654 -->
Parameter
Description
Type
Size
Default
override-replacemsg
Override replacement message.
string
Maximum
length: 28
warn-duration
Duration of warnings.
user
Not
Specified
5m
warning-duration-type
Re-display warning after closing browser or after a
timeout.
option
-timeout
Option
Description
session
After session ends.
timeout
After timeout occurs.
warning-prompt
Warning prompts in each category or each domain.
option
-per-category
Option
Description
per-domain
Per-domain warnings.
per-category
Per-category warnings.
config quota
Parameter
Description
Type
Size
Default
category
FortiGuard categories to apply quota to
(category action must be set to monitor).
user
Not Specified
duration
Duration of quota.
user
Not Specified
5m
id
ID number.
integer
Minimum value:
0 Maximum
value:
4294967295
0
override-replacemsg
Override replacement message.
string
Maximum
length: 28
type
Quota type.
option
-time
Option
Description
time
Use a time-based quota.
traffic
Use a traffic-based quota.
unit
Traffic quota unit of measurement.
option
-MB
FortiOS 8.0.0 CLI Reference
2654
Fortinet Inc.

<!-- 来源页 2655 -->
Parameter
Description
Type
Size
Default
Option
Description
B
Quota in bytes.
KB
Quota in kilobytes.
MB
Quota in megabytes.
GB
Quota in gigabytes.
value
Traffic quota value.
integer
Minimum value:
1 Maximum
value:
4294967295
1024
config risk
Parameter
Description
Type
Size
Default
action
Action to take for matches.
option
-monitor
Option
Description
block
Block access.
monitor
Allow access while logging the action.
id
ID number.
integer
Minimum
value: 0
Maximum
value: 255
0
log
Enable/disable logging.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
risk-level
Risk level to be examined.
string
Maximum
length: 35
config override
Parameter
Description
Type
Size
Default
ovrd-cookie
Allow/deny browser-based (cookie) overrides.
option
-deny
FortiOS 8.0.0 CLI Reference
2655
Fortinet Inc.

<!-- 来源页 2656 -->
Parameter
Description
Type
Size
Default
Option
Description
allow
Allow browser-based (cookie) override.
deny
Deny browser-based (cookie) override.
ovrd-dur
Override duration.
user
Not
Specified
15m
ovrd-dur-mode
Override duration mode.
option
-constant
Option
Description
constant
Constant mode.
ask
Prompt for duration when initiating an override.
ovrd-scope
Override scope.
option
-user
Option
Description
user
Override for the user.
user-group
Override for the user's group.
ip
Override for the initiating IP.
browser
Create browser-based (cookie) override.
ask
Prompt for scope when initiating an override.
ovrd-user-group <name>
User groups with permission to use the override.
User group name.
string
Maximum
length: 79
profile <name>
Web filter profile with permission to create
overrides.
Web profile.
string
Maximum
length: 79
profile-attribute
Profile attribute to retrieve from the RADIUS server.
option
-Login-LAT-Service
Option
Description
User-Name
Use this attribute.
NAS-IP-Address
Use this attribute.
Framed-IP-Address
Use this attribute.
FortiOS 8.0.0 CLI Reference
2656
Fortinet Inc.

<!-- 来源页 2657 -->
Parameter
Description
Type
Size
Default
Option
Description
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
Framed-AppleTalk-Zone
Use this attribute.
Acct-Session-Id
Use this attribute.
Acct-Multi-Session-Id
Use this attribute.
profile-type
Override profile type.
option
-list
Option
Description
list
Profile chosen from list.
radius
Profile determined by RADIUS server.
FortiOS 8.0.0 CLI Reference
2657
Fortinet Inc.

<!-- 来源页 2658 -->
config web
Parameter
Description
Type
Size
Default
allowlist
FortiGuard allowlist settings.
option
-Option
Description
exempt-av
Exempt antivirus.
exempt-webcontent
Exempt web content.
exempt-activex-java-cookie
Exempt ActiveX-JAVA-Cookie.
exempt-dlp
Exempt DLP.
exempt-rangeblock
Exempt RangeBlock.
extended-log-others
Support extended log.
blocklist
Enable/disable automatic addition of URLs
detected by FortiSandbox to blocklist.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
bword-table
Banned word table ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
bword-threshold
Banned word score threshold.
integer
Minimum value:
0 Maximum
value:
2147483647
10
content-header-list
Content header list.
integer
Minimum value:
0 Maximum
value:
4294967295
0
keyword-match
<pattern>
Search keywords to log when match is found.
Pattern/keyword to search for.
string
Maximum
length: 79
**
log-search
Enable/disable logging all search phrases.
option
-disable
FortiOS 8.0.0 CLI Reference
2658
Fortinet Inc.

<!-- 来源页 2659 -->
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
safe-search
Safe search type.
option
-Option
Description
url
Insert safe search string into URL.
header
Insert safe search header.
urlfilter-table
URL filter table ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
vimeo-restrict
Set Vimeo-restrict ("7" = don't show mature
content, "134" = don't show unrated and mature
content). A value of cookie "content_rating".
string
Maximum
length: 63
youtube-restrict
YouTube EDU filter level.
option
-none
Option
Description
none
Full access for YouTube.
strict
Strict access for YouTube.
moderate
Moderate access for YouTube.
config webfilter search-engine
Configure web filter search engines.
config webfilter search-engine
Description: Configure web filter search engines.
edit <name>
set charset [utf-8|gb2312]
set hostname {string}
set query {string}
set safesearch [disable|url|...]
set safesearch-str {string}
set url {string}
next
end
FortiOS 8.0.0 CLI Reference
2659
Fortinet Inc.

<!-- 来源页 2660 -->
config webfilter search-engine
Parameter
Description
Type
Size
Default
charset
Search engine charset.
option
-utf-8
Option
Description
utf-8
UTF-8 encoding.
gb2312
GB2312 encoding.
hostname
Hostname (regular expression).
string
Maximum
length: 127
name
Search engine name.
string
Maximum
length: 35
query
Code used to prefix a query (must end with an
equals character).
string
Maximum
length: 15
safesearch
Safe search method. You can disable safe search,
add the safe search string to URLs, or insert a safe
search header.
option
-disable
Option
Description
disable
Site does not support safe search.
url
Safe search selected with a parameter in the URL.
header
Safe search selected by search header (i.e. youtube.edu).
translate
Perform URL FortiGuard check on translated URL.
yt-pattern
Pattern to match YouTube channel ID.
yt-scan
Perform IPS scan.
yt-video
Pattern to match YouTube video name.
yt-channel
Pattern to match YouTube channel name.
safesearch-str
Safe search parameter used in the URL in URL
mode. In translate mode, it provides either the
regex to translate the URL or the special case to
translate the URL.
string
Maximum
length: 255
url
URL (regular expression).
string
Maximum
length: 127
config webfilter urlfilter
Configure URL filter lists.
FortiOS 8.0.0 CLI Reference
2660
Fortinet Inc.

<!-- 来源页 2661 -->
config webfilter urlfilter
Description: Configure URL filter lists.
edit <id>
set comment {var-string}
config entries
Description: URL filter entries.
edit <id>
set action [exempt|block|...]
set antiphish-action [block|log]
set comment {var-string}
set dns-address-family [ipv4|ipv6|...]
set exempt {option1}, {option2}, ...
set referrer-host {string}
set status [enable|disable]
set type [simple|regex|...]
set url {string}
set web-proxy-profile {string}
next
end
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set include-subdomains [enable|disable]
set ip-addr-block [enable|disable]
set ip4-mapped-ip6 [enable|disable]
set name {string}
set one-arm-ips-urlfilter [enable|disable]
set type [profile|category]
set uuid {uuid}
next
end
config webfilter urlfilter
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
FortiOS 8.0.0 CLI Reference
2661
Fortinet Inc.

<!-- 来源页 2662 -->
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
id
ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
include-subdomains
Enable/disable matching subdomains.
Applies only to simple type (default =
enable).
option
-enable
Option
Description
enable
Enable matching subdomains. Applies only to simple type.
disable
Disable matching subdomains. Applies only to simple type.
ip-addr-block
Enable/disable blocking URLs when the
hostname appears as an IP address.
option
-disable
Option
Description
enable
Enable blocking URLs when the hostname appears as an IP address.
disable
Disable blocking URLs when the hostname appears as an IP address.
ip4-mapped-ip6
Enable/disable matching of IPv4 mapped
IPv6 URLs.
option
-disable
FortiOS 8.0.0 CLI Reference
2662
Fortinet Inc.

<!-- 来源页 2663 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable matching IPv4 mapped IPv6 URLs.
disable
Disable matching IPv4 mapped IPv6 URLs.
name
Name of URL filter list.
string
Maximum
length: 63
one-arm-ips-urlfilter
Enable/disable DNS resolver for one-arm
IPS URL filter operation.
option
-disable
Option
Description
enable
Enable DNS resolver for one-arm IPS URL filter operation.
disable
Disable DNS resolver for one-arm IPS URL filter operation.
type *
Type of URL filter table (profile or
category).
option
-profile
Option
Description
profile
URL list for webfilter profile.
category
URL list for local web category override.
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
config entries
Parameter
Description
Type
Size
Default
action
Action to take for URL filter matches.
option
-exempt
Option
Description
exempt
Exempt matches.
block
Block matches.
allow
Allow matches (no log).
monitor
Allow matches (with log).
antiphish-action
Action to take for AntiPhishing matches.
option
-block
FortiOS 8.0.0 CLI Reference
2663
Fortinet Inc.

<!-- 来源页 2664 -->
Parameter
Description
Type
Size
Default
Option
Description
block
Block matches.
log
Allow matches with log.
comment
Comment.
var-string
Maximum
length: 255
dns-address-family
Resolve IPv4 address, IPv6 address, or both
from DNS server.
option
-ipv4
Option
Description
ipv4
Resolve IPv4 address from DNS server.
ipv6
Resolve IPv6 address from DNS server.
both
Resolve both IPv4 and IPv6 addresses from DNS server.
exempt
If action is set to exempt, select the security
profile operations that exempt URLs skip.
Separate multiple options with a space.
option
-av web-content
activex-java-cookie
dlp
fortiguard
range-block
antiphish all
Option
Description
av
AntiVirus scanning.
web-content
Web filter content matching.
activex-java-cookie
ActiveX, Java, and cookie filtering.
dlp
DLP scanning.
fortiguard
FortiGuard web filtering.
range-block
Range block feature.
pass
Pass single connection from all.
antiphish
AntiPhish credential checking.
all
Exempt from all security profiles.
FortiOS 8.0.0 CLI Reference
2664
Fortinet Inc.

<!-- 来源页 2665 -->
Parameter
Description
Type
Size
Default
id
Id.
integer
Minimum value:
0 Maximum
value:
4294967295
0
referrer-host
Referrer host name.
string
Maximum
length: 255
status
Enable/disable this URL filter.
option
-enable
Option
Description
enable
Enable this URL filter.
disable
Disable this URL filter.
type
Filter type (simple or wildcard). If table type
'profile', regex also supported.
option
-simple
Option
Description
simple
Simple URL string.
regex
Regular expression URL string.
wildcard
Wildcard URL string.
url
URL to be filtered.
string
Maximum
length: 511
web-proxy-profile
Web proxy profile.
string
Maximum
length: 63
FortiOS 8.0.0 CLI Reference
2665
Fortinet Inc.
