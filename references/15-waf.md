# WAF (Web 应用防火墙)

> 来源: FortiOS-8.0.0-CLI_Reference.pdf
> 覆盖命令/章节: waf
> 本文件由 extract_pdf.py 从官方 PDF 自动提取，请勿手动编辑；
> 如需修正请修改 map.json 后重跑脚本。

---


<!-- 来源页 2541 -->
waf
This section includes syntax for the following commands:
l config waf main-class on page 2541
l config waf profile on page 2541
l config waf signature on page 2567
l config waf sub-class on page 2567
config waf main-class
Hidden table for datasource.
config waf main-class
Description: Hidden table for datasource.
edit <id>
set name {string}
next
end
config waf main-class
Parameter
Description
Type
Size
Default
id
Main signature class ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
name
Main signature class name.
string
Maximum
length: 127
config waf profile
Configure Web application firewall configuration.
config waf profile
Description: Configure Web application firewall configuration.
edit <name>
config address-list
Description: Address block and allow lists.
set blocked-address <name1>, <name2>, ...
FortiOS 8.0.0 CLI Reference
2541
Fortinet Inc.

<!-- 来源页 2542 -->
set blocked-log [enable|disable]
set severity [high|medium|...]
set status [enable|disable]
set trusted-address <name1>, <name2>, ...
end
set comment {var-string}
config constraint
Description: WAF HTTP protocol restrictions.
config content-length
Description: HTTP content length in request.
set action [allow|block]
set length {integer}
set log [enable|disable]
set severity [high|medium|...]
set status [enable|disable]
end
config exception
Description: HTTP constraint exception.
edit <id>
set address {string}
set content-length [enable|disable]
set header-length [enable|disable]
set hostname [enable|disable]
set line-length [enable|disable]
set malformed [enable|disable]
set max-cookie [enable|disable]
set max-header-line [enable|disable]
set max-range-segment [enable|disable]
set max-url-param [enable|disable]
set method [enable|disable]
set param-length [enable|disable]
set pattern {string}
set regex [enable|disable]
set url-param-length [enable|disable]
set version [enable|disable]
next
end
config header-length
Description: HTTP header length in request.
set action [allow|block]
set length {integer}
set log [enable|disable]
set severity [high|medium|...]
set status [enable|disable]
end
config hostname
Description: Enable/disable hostname check.
set action [allow|block]
set log [enable|disable]
set severity [high|medium|...]
set status [enable|disable]
end
FortiOS 8.0.0 CLI Reference
2542
Fortinet Inc.

<!-- 来源页 2543 -->
config line-length
Description: HTTP line length in request.
set action [allow|block]
set length {integer}
set log [enable|disable]
set severity [high|medium|...]
set status [enable|disable]
end
config malformed
Description: Enable/disable malformed HTTP request check.
set action [allow|block]
set log [enable|disable]
set severity [high|medium|...]
set status [enable|disable]
end
config max-cookie
Description: Maximum number of cookies in HTTP request.
set action [allow|block]
set log [enable|disable]
set max-cookie {integer}
set severity [high|medium|...]
set status [enable|disable]
end
config max-header-line
Description: Maximum number of HTTP header line.
set action [allow|block]
set log [enable|disable]
set max-header-line {integer}
set severity [high|medium|...]
set status [enable|disable]
end
config max-range-segment
Description: Maximum number of range segments in HTTP range line.
set action [allow|block]
set log [enable|disable]
set max-range-segment {integer}
set severity [high|medium|...]
set status [enable|disable]
end
config max-url-param
Description: Maximum number of parameters in URL.
set action [allow|block]
set log [enable|disable]
set max-url-param {integer}
set severity [high|medium|...]
set status [enable|disable]
end
config method
Description: Enable/disable HTTP method check.
set action [allow|block]
set log [enable|disable]
set severity [high|medium|...]
FortiOS 8.0.0 CLI Reference
2543
Fortinet Inc.

<!-- 来源页 2544 -->
set status [enable|disable]
end
config param-length
Description: Maximum length of parameter in URL, HTTP POST request or HTTP body.
set action [allow|block]
set length {integer}
set log [enable|disable]
set severity [high|medium|...]
set status [enable|disable]
end
config url-param-length
Description: Maximum length of parameter in URL.
set action [allow|block]
set length {integer}
set log [enable|disable]
set severity [high|medium|...]
set status [enable|disable]
end
config version
Description: Enable/disable HTTP version check.
set action [allow|block]
set log [enable|disable]
set severity [high|medium|...]
set status [enable|disable]
end
end
set extended-log [enable|disable]
set external [disable|enable]
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
config method
Description: Method restriction.
set default-allowed-methods {option1}, {option2}, ...
set log [enable|disable]
config method-policy
Description: HTTP method policy.
edit <id>
set address {string}
set allowed-methods {option1}, {option2}, ...
set pattern {string}
set regex [enable|disable]
next
end
set severity [high|medium|...]
set status [enable|disable]
end
config signature
Description: WAF signatures.
set credit-card-detection-threshold {integer}
config custom-signature
Description: Custom signature.
FortiOS 8.0.0 CLI Reference
2544
Fortinet Inc.

<!-- 来源页 2545 -->
edit <name>
set action [allow|block|...]
set case-sensitivity [disable|enable]
set direction [request|response]
set log [enable|disable]
set pattern {string}
set severity [high|medium|...]
set status [enable|disable]
set target {option1}, {option2}, ...
next
end
set disabled-signature <id1>, <id2>, ...
set disabled-sub-class <id1>, <id2>, ...
config main-class
Description: Main signature class. Read-only.
edit <id>
set action [allow|block|...]
set log [enable|disable]
set severity [high|medium|...]
set status [enable|disable]
next
end
end
config url-access
Description: URL access list.
edit <id>
config access-pattern
Description: URL access pattern.
edit <id>
set negate [enable|disable]
set pattern {string}
set regex [enable|disable]
set srcaddr {string}
next
end
set action [bypass|permit|...]
set address {string}
set log [enable|disable]
set severity [high|medium|...]
next
end
set uuid {uuid}
next
end
FortiOS 8.0.0 CLI Reference
2545
Fortinet Inc.

<!-- 来源页 2546 -->
config waf profile
Parameter
Description
Type
Size
Default
comment
Comment.
var-string
Maximum
length:
1023
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
external
Disable/Enable external HTTP Inspection.
option
-disable
Option
Description
disable
Disable external inspection.
enable
Enable external inspection.
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
FortiOS 8.0.0 CLI Reference
2546
Fortinet Inc.

<!-- 来源页 2547 -->
Parameter
Description
Type
Size
Default
Option
Description
local
Source of truth for this object is this security fabric member.
root
Source of truth for this object is the root of the fabric.
name
WAF Profile name.
string
Maximum
length: 47
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be manually
reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
config address-list
Parameter
Description
Type
Size
Default
blocked-address
<name>
Blocked address.
Address name.
string
Maximum
length: 79
blocked-log
Enable/disable logging on blocked addresses.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
severity
Severity.
option
-medium
Option
Description
high
High severity.
medium
Medium severity.
low
Low severity.
status
Status.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
trusted-address
<name>
Trusted address.
Address name.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
2547
Fortinet Inc.

<!-- 来源页 2548 -->
config content-length
Parameter
Description
Type
Size
Default
action
Action.
option
-allow
Option
Description
allow
Allow.
block
Block.
length
Length of HTTP content in bytes (0 to
2147483647).
integer
Minimum
value: 0
Maximum
value:
2147483647
67108864
log
Enable/disable logging.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
severity
Severity.
option
-medium
Option
Description
high
High severity.
medium
Medium severity.
low
Low severity.
status
Enable/disable the constraint.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
config exception
Parameter
Description
Type
Size
Default
address
Host address.
string
Maximum
length: 79
content-length
HTTP content length in request.
option
-disable
FortiOS 8.0.0 CLI Reference
2548
Fortinet Inc.

<!-- 来源页 2549 -->
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
header-length
HTTP header length in request.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
hostname
Enable/disable hostname check.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
id
Exception ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
line-length
HTTP line length in request.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
malformed
Enable/disable malformed HTTP request check.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
max-cookie
Maximum number of cookies in HTTP request.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
2549
Fortinet Inc.

<!-- 来源页 2550 -->
Parameter
Description
Type
Size
Default
max-header-line
Maximum number of HTTP header line.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
max-range-segment
Maximum number of range segments in HTTP
range line.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
max-url-param
Maximum number of parameters in URL.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
method
Enable/disable HTTP method check.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
param-length
Maximum length of parameter in URL, HTTP
POST request or HTTP body.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
pattern
URL pattern.
string
Maximum
length: 511
regex
Enable/disable regular expression based pattern
match.
option
-disable
FortiOS 8.0.0 CLI Reference
2550
Fortinet Inc.

<!-- 来源页 2551 -->
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
url-param-length
Maximum length of parameter in URL.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
version
Enable/disable HTTP version check.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
config header-length
Parameter
Description
Type
Size
Default
action
Action.
option
-allow
Option
Description
allow
Allow.
block
Block.
length
Length of HTTP header in bytes (0 to
2147483647).
integer
Minimum
value: 0
Maximum
value:
2147483647
8192
log
Enable/disable logging.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
severity
Severity.
option
-medium
FortiOS 8.0.0 CLI Reference
2551
Fortinet Inc.

<!-- 来源页 2552 -->
Parameter
Description
Type
Size
Default
Option
Description
high
High severity.
medium
Medium severity.
low
Low severity.
status
Enable/disable the constraint.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
config hostname
Parameter
Description
Type
Size
Default
action
Action.
option
-allow
Option
Description
allow
Allow.
block
Block.
log
Enable/disable logging.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
severity
Severity.
option
-medium
Option
Description
high
High severity.
medium
Medium severity.
low
Low severity.
status
Enable/disable the constraint.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
2552
Fortinet Inc.

<!-- 来源页 2553 -->
config line-length
Parameter
Description
Type
Size
Default
action
Action.
option
-allow
Option
Description
allow
Allow.
block
Block.
length
Length of HTTP line in bytes (0 to 2147483647).
integer
Minimum
value: 0
Maximum
value:
2147483647
1024
log
Enable/disable logging.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
severity
Severity.
option
-medium
Option
Description
high
High severity.
medium
Medium severity.
low
Low severity.
status
Enable/disable the constraint.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
config malformed
Parameter
Description
Type
Size
Default
action
Action.
option
-allow
Option
Description
allow
Allow.
block
Block.
FortiOS 8.0.0 CLI Reference
2553
Fortinet Inc.

<!-- 来源页 2554 -->
Parameter
Description
Type
Size
Default
log
Enable/disable logging.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
severity
Severity.
option
-medium
Option
Description
high
High severity.
medium
Medium severity.
low
Low severity.
status
Enable/disable the constraint.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
config max-cookie
Parameter
Description
Type
Size
Default
action
Action.
option
-allow
Option
Description
allow
Allow.
block
Block.
log
Enable/disable logging.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
max-cookie
Maximum number of cookies in HTTP request (0
to 2147483647).
integer
Minimum
value: 0
Maximum
value:
2147483647
16
severity
Severity.
option
-medium
FortiOS 8.0.0 CLI Reference
2554
Fortinet Inc.

<!-- 来源页 2555 -->
Parameter
Description
Type
Size
Default
Option
Description
high
High severity.
medium
Medium severity.
low
Low severity.
status
Enable/disable the constraint.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
config max-header-line
Parameter
Description
Type
Size
Default
action
Action.
option
-allow
Option
Description
allow
Allow.
block
Block.
log
Enable/disable logging.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
max-header-line
Maximum number HTTP header lines (0 to
2147483647).
integer
Minimum
value: 0
Maximum
value:
2147483647
32
severity
Severity.
option
-medium
Option
Description
high
High severity.
medium
Medium severity.
low
Low severity.
status
Enable/disable the constraint.
option
-disable
FortiOS 8.0.0 CLI Reference
2555
Fortinet Inc.

<!-- 来源页 2556 -->
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
config max-range-segment
Parameter
Description
Type
Size
Default
action
Action.
option
-allow
Option
Description
allow
Allow.
block
Block.
log
Enable/disable logging.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
max-range-segment
Maximum number of range segments in HTTP
range line (0 to 2147483647).
integer
Minimum
value: 0
Maximum
value:
2147483647
5
severity
Severity.
option
-medium
Option
Description
high
High severity.
medium
Medium severity.
low
Low severity.
status
Enable/disable the constraint.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
2556
Fortinet Inc.

<!-- 来源页 2557 -->
config max-url-param
Parameter
Description
Type
Size
Default
action
Action.
option
-allow
Option
Description
allow
Allow.
block
Block.
log
Enable/disable logging.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
max-url-param
Maximum number of parameters in URL (0 to
2147483647).
integer
Minimum
value: 0
Maximum
value:
2147483647
16
severity
Severity.
option
-medium
Option
Description
high
High severity.
medium
Medium severity.
low
Low severity.
status
Enable/disable the constraint.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
config method
Parameter
Description
Type
Size
Default
action
Action.
option
-allow
Option
Description
allow
Allow.
block
Block.
FortiOS 8.0.0 CLI Reference
2557
Fortinet Inc.

<!-- 来源页 2558 -->
Parameter
Description
Type
Size
Default
log
Enable/disable logging.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
severity
Severity.
option
-medium
Option
Description
high
High severity.
medium
Medium severity.
low
Low severity.
status
Enable/disable the constraint.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
config param-length
Parameter
Description
Type
Size
Default
action
Action.
option
-allow
Option
Description
allow
Allow.
block
Block.
length
Maximum length of parameter in URL, HTTP
POST request or HTTP body in bytes (0 to
2147483647).
integer
Minimum
value: 0
Maximum
value:
2147483647
8192
log
Enable/disable logging.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
severity
Severity.
option
-medium
FortiOS 8.0.0 CLI Reference
2558
Fortinet Inc.

<!-- 来源页 2559 -->
Parameter
Description
Type
Size
Default
Option
Description
high
High severity.
medium
Medium severity.
low
Low severity.
status
Enable/disable the constraint.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
config url-param-length
Parameter
Description
Type
Size
Default
action
Action.
option
-allow
Option
Description
allow
Allow.
block
Block.
length
Maximum length of URL parameter in bytes (0 to
2147483647).
integer
Minimum
value: 0
Maximum
value:
2147483647
8192
log
Enable/disable logging.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
severity
Severity.
option
-medium
Option
Description
high
High severity.
medium
Medium severity.
low
Low severity.
status
Enable/disable the constraint.
option
-disable
FortiOS 8.0.0 CLI Reference
2559
Fortinet Inc.

<!-- 来源页 2560 -->
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
config version
Parameter
Description
Type
Size
Default
action
Action.
option
-allow
Option
Description
allow
Allow.
block
Block.
log
Enable/disable logging.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
severity
Severity.
option
-medium
Option
Description
high
High severity.
medium
Medium severity.
low
Low severity.
status
Enable/disable the constraint.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
config method
Parameter
Description
Type
Size
Default
default-allowed-methods
Methods.
option
-FortiOS 8.0.0 CLI Reference
2560
Fortinet Inc.

<!-- 来源页 2561 -->
Parameter
Description
Type
Size
Default
Option
Description
get
HTTP GET method.
post
HTTP POST method.
put
HTTP PUT method.
head
HTTP HEAD method.
connect
HTTP CONNECT method.
trace
HTTP TRACE method.
options
HTTP OPTIONS method.
delete
HTTP DELETE method.
others
Other HTTP methods.
log
Enable/disable logging.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
severity
Severity.
option
-medium
Option
Description
high
High severity
medium
medium severity
low
low severity
status
Status.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
config method-policy
Parameter
Description
Type
Size
Default
address
Host address.
string
Maximum
length: 79
allowed-methods
Allowed Methods.
option
-FortiOS 8.0.0 CLI Reference
2561
Fortinet Inc.

<!-- 来源页 2562 -->
Parameter
Description
Type
Size
Default
Option
Description
get
HTTP GET method.
post
HTTP POST method.
put
HTTP PUT method.
head
HTTP HEAD method.
connect
HTTP CONNECT method.
trace
HTTP TRACE method.
options
HTTP OPTIONS method.
delete
HTTP DELETE method.
others
Other HTTP methods.
id
HTTP method policy ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
pattern
URL pattern.
string
Maximum
length: 511
regex
Enable/disable regular expression based pattern
match.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
config signature
Parameter
Description
Type
Size
Default
credit-card-detection-threshold
The minimum number of Credit cards to detect
violation.
integer
Minimum value:
0 Maximum
value: 128
3
disabled-signature
<id>
Disabled signatures.
Signature ID.
integer
Minimum value:
0 Maximum
value:
4294967295
disabled-sub-class
<id>
Disabled signature subclasses.
Signature subclass ID.
integer
Minimum value:
0 Maximum
value:
4294967295
FortiOS 8.0.0 CLI Reference
2562
Fortinet Inc.

<!-- 来源页 2563 -->
config custom-signature
Parameter
Description
Type
Size
Default
action
Action.
option
-allow
Option
Description
allow
Allow.
block
Block.
erase
Erase credit card numbers.
case-sensitivity
Case sensitivity in pattern.
option
-disable
Option
Description
disable
Case insensitive in pattern.
enable
Case sensitive in pattern.
direction
Traffic direction.
option
-request
Option
Description
request
Match HTTP request.
response
Match HTTP response.
log
Enable/disable logging.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
name
Signature name.
string
Maximum
length: 35
pattern
Match pattern.
string
Maximum
length: 511
severity
Severity.
option
-medium
Option
Description
high
High severity.
medium
Medium severity.
low
Low severity.
status
Status.
option
-disable
FortiOS 8.0.0 CLI Reference
2563
Fortinet Inc.

<!-- 来源页 2564 -->
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
target
Match HTTP target.
option
-Option
Description
arg
HTTP arguments.
arg-name
Names of HTTP arguments.
req-body
HTTP request body.
req-cookie
HTTP request cookies.
req-cookie-name
HTTP request cookie names.
req-filename
HTTP request file name.
req-header
HTTP request headers.
req-header-name
HTTP request header names.
req-raw-uri
Raw URI of HTTP request.
req-uri
URI of HTTP request.
resp-body
HTTP response body.
resp-hdr
HTTP response headers.
resp-status
HTTP response status.
config main-class
Parameter
Description
Type
Size
Default
action
Action.
option
-allow
Option
Description
allow
Allow.
block
Block.
erase
Erase credit card numbers.
FortiOS 8.0.0 CLI Reference
2564
Fortinet Inc.

<!-- 来源页 2565 -->
Parameter
Description
Type
Size
Default
id
Main signature class ID.
integer
Minimum value:
0 Maximum
value:
4294967295
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
severity
Severity.
option
-medium
Option
Description
high
High severity.
medium
Medium severity.
low
Low severity.
status
Status.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
config url-access
Parameter
Description
Type
Size
Default
action
Action.
option
-permit
Option
Description
bypass
Allow the HTTP request, also bypass further WAF scanning.
permit
Allow the HTTP request, and continue further WAF scanning.
block
Block HTTP request.
address
Host address.
string
Maximum
length: 79
id
URL access ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
FortiOS 8.0.0 CLI Reference
2565
Fortinet Inc.

<!-- 来源页 2566 -->
Parameter
Description
Type
Size
Default
log
Enable/disable logging.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
severity
Severity.
option
-medium
Option
Description
high
High severity.
medium
Medium severity.
low
Low severity.
config access-pattern
Parameter
Description
Type
Size
Default
id
URL access pattern ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
negate
Enable/disable match negation.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
pattern
URL pattern.
string
Maximum
length: 511
regex
Enable/disable regular expression based pattern
match.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
srcaddr
Source address.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
2566
Fortinet Inc.

<!-- 来源页 2567 -->
config waf signature
Hidden table for datasource.
config waf signature
Description: Hidden table for datasource.
edit <id>
set desc {string}
next
end
config waf signature
Parameter
Description
Type
Size
Default
desc
Signature description.
string
Maximum
length: 511
id
Signature ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config waf sub-class
Hidden table for datasource.
config waf sub-class
Description: Hidden table for datasource.
edit <id>
set name {string}
next
end
config waf sub-class
Parameter
Description
Type
Size
Default
id
Signature subclass ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
name
Signature subclass name.
string
Maximum
length: 127
FortiOS 8.0.0 CLI Reference
2567
Fortinet Inc.
