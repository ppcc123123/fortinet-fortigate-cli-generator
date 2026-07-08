# VoIP / DLP / CASB / 其他协议过滤

> 来源: FortiOS-8.0.0-CLI_Reference.pdf
> 覆盖命令/章节: voip, videofilter, dlp, casb, diameter-filter, sctp-filter, ssh-filter
> 本文件由 extract_pdf.py 从官方 PDF 自动提取，请勿手动编辑；
> 如需修正请修改 map.json 后重跑脚本。

---


<!-- 来源页 226 -->
casb
This section includes syntax for the following commands:
l config casb attribute-match on page 226
l config casb profile on page 228
l config casb saas-application on page 234
l config casb user-activity on page 237
config casb attribute-match
Configure CASB attribute match rule.
config casb attribute-match
Description: Configure CASB attribute match rule.
edit <name>
set application {string}
config match
Description: CASB tenant match rules.
edit <id>
config rule
Description: CASB attribute match rule.
edit <id>
set attribute {string}
set case-sensitive [enable|disable]
set match-pattern [simple|substr|...]
set match-value {string}
set negate [enable|disable]
next
end
set rule-strategy [and|or]
next
end
set match-strategy [or|and|...]
next
end
config casb attribute-match
Parameter
Description
Type
Size
Default
application
CASB attribute application name.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
226
Fortinet Inc.

<!-- 来源页 227 -->
Parameter
Description
Type
Size
Default
match-strategy
CASB attribute match strategy.
option
-or
Option
Description
or
Match when any rule is satisfied.
and
Match when all rules are satisfied.
subset
Match when extracted attributes are found within defined rules.
name
CASB attribute match name.
string
Maximum
length: 79
config match
Parameter
Description
Type
Size
Default
id
CASB attribute match rule ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
rule-strategy
CASB attribute match rule strategy.
option
-and
Option
Description
and
Match attribute using a logical AND operator.
or
Match attribute using a logical OR operator.
config rule
Parameter
Description
Type
Size
Default
attribute
CASB attribute match name.
string
Maximum
length: 79
case-sensitive
CASB attribute match case sensitive.
option
-disable
Option
Description
enable
Enable value case sensitive match.
disable
Disable value case sensitive match.
id
CASB attribute rule ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
FortiOS 8.0.0 CLI Reference
227
Fortinet Inc.

<!-- 来源页 228 -->
Parameter
Description
Type
Size
Default
match-pattern
CASB attribute match pattern.
option
-simple
Option
Description
simple
Exact string match pattern.
substr
Sub-string pattern.
regexp
Regular expression pattern.
match-value
CASB attribute match value.
string
Maximum
length: 1023
negate
Enable/disable what the matching strategy must
not be.
option
-disable
Option
Description
enable
Matching strategy is negated.
disable
Matching strategy is not negated.
config casb profile
Configure CASB profile.
config casb profile
Description: Configure CASB profile.
edit <name>
set comment {var-string}
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
config saas-application
Description: CASB profile SaaS application.
edit <name>
config access-rule
Description: CASB profile access rule.
edit <name>
set action [monitor|bypass|...]
config attribute-filter
Description: CASB profile attribute filter.
edit <id>
set action [monitor|bypass|...]
set attribute-match {string}
next
end
set bypass {option1}, {option2}, ...
next
FortiOS 8.0.0 CLI Reference
228
Fortinet Inc.

<!-- 来源页 229 -->
end
config advanced-tenant-control
Description: CASB profile advanced tenant control.
edit <name>
config attribute
Description: CASB advanced tenant control attribute.
edit <name>
set input <value1>, <value2>, ...
next
end
next
end
config custom-control
Description: CASB profile custom control.
edit <name>
config attribute-filter
Description: CASB attribute filter.
edit <id>
set action [monitor|bypass|...]
set attribute-match {string}
next
end
config option
Description: CASB custom control option.
edit <name>
set user-input <value1>, <value2>, ...
next
end
next
end
set domain-control [enable|disable]
set domain-control-domains <name1>, <name2>, ...
set log [enable|disable]
set safe-search [enable|disable]
set safe-search-control <name1>, <name2>, ...
set status [enable|disable]
set tenant-control [enable|disable]
set tenant-control-tenants <name1>, <name2>, ...
next
end
set uuid {uuid}
next
end
config casb profile
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
229
Fortinet Inc.

<!-- 来源页 230 -->
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
name
CASB profile name.
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
config saas-application
Parameter
Description
Type
Size
Default
domain-control
Enable/disable domain control.
option
-disable
FortiOS 8.0.0 CLI Reference
230
Fortinet Inc.

<!-- 来源页 231 -->
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
domain-control-domains
<name>
CASB profile domain control domains.
Domain control domain name.
string
Maximum
length: 79
log
Enable/disable log settings.
option
-enable
Option
Description
enable
Enable log setting.
disable
Disable log setting.
name
CASB profile SaaS application name.
string
Maximum
length: 79
safe-search
Enable/disable safe search.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
safe-search-control
<name>
CASB profile safe search control.
Safe search control name.
string
Maximum
length: 79
status
Enable/disable setting.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
tenant-control
Enable/disable tenant control.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
231
Fortinet Inc.

<!-- 来源页 232 -->
Parameter
Description
Type
Size
Default
tenant-control-tenants
<name>
CASB profile tenant control tenants.
Tenant control tenants name.
string
Maximum
length: 79
config access-rule
Parameter
Description
Type
Size
Default
action
CASB access rule action.
option
-monitor
Option
Description
monitor
Log when log is enabled.
bypass
Apply bypass options.
block
Block the request.
bypass
CASB bypass options.
option
-Option
Description
av
Exempt from AV scanning.
dlp
Exempt from data loss prevention (DLP).
web-filter
Exempt from web filter.
file-filter
Exempt from file filter.
video-filter
Exempt from video filter.
name
CASB access rule activity name.
string
Maximum
length: 79
config attribute-filter
Parameter
Description
Type
Size
Default
action
CASB access rule tenant control action.
option
-monitor
Option
Description
monitor
Log when log is enabled.
bypass
Apply bypass options.
block
Block the request.
attribute-match
CASB access rule tenant match.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
232
Fortinet Inc.

<!-- 来源页 233 -->
Parameter
Description
Type
Size
Default
id
CASB tenant control ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config advanced-tenant-control
Parameter
Description
Type
Size
Default
name
CASB advanced tenant control name.
string
Maximum
length: 79
config attribute
Parameter
Description
Type
Size
Default
input <value>
CASB extend user input value.
User input value.
string
Maximum
length: 79
name
CASB extend user input name.
string
Maximum
length: 79
config custom-control
Parameter
Description
Type
Size
Default
name
CASB custom control user activity name.
string
Maximum
length: 79
config attribute-filter
Parameter
Description
Type
Size
Default
action
CASB access rule tenant control action.
option
-monitor
Option
Description
monitor
Log when log is enabled.
bypass
Apply bypass options.
block
Block the request.
attribute-match
CASB access rule tenant match.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
233
Fortinet Inc.

<!-- 来源页 234 -->
Parameter
Description
Type
Size
Default
id
CASB tenant control ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config option
Parameter
Description
Type
Size
Default
name
CASB custom control option name.
string
Maximum
length: 79
user-input
<value>
CASB custom control user input.
user input value.
string
Maximum
length: 79
config casb saas-application
Configure CASB SaaS application.
config casb saas-application
Description: Configure CASB SaaS application.
edit <name>
set casb-name {string}
set description {string}
set domains <domain1>, <domain2>, ...
config input-attributes
Description: SaaS application input attributes.
edit <name>
set default [string|string-list]
set description {string}
set fallback-input [enable|disable]
set required [enable|disable]
set type {option}
next
end
config output-attributes
Description: SaaS application output attributes.
edit <name>
set description {string}
set optional [enable|disable]
set type [string|string-list|...]
next
end
set status [enable|disable]
set type [built-in|customized]
set uuid {string}
FortiOS 8.0.0 CLI Reference
234
Fortinet Inc.

<!-- 来源页 235 -->
next
end
config casb saas-application
Parameter
Description
Type
Size
Default
casb-name
SaaS application signature name.
string
Maximum
length: 79
description
SaaS application description.
string
Maximum
length: 63
domains
<domain>
SaaS application domain list.
Domain list separated by space.
string
Maximum
length: 127
name
SaaS application name.
string
Maximum
length: 79
status
Enable/disable setting.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
type
SaaS application type.
option
-customized
Option
Description
built-in
Built-in SaaS application.
customized
User customized SaaS appliciation.
uuid
Universally Unique Identifier (UUID;
automatically assigned but can be manually
reset).
string
Maximum
length: 36
config input-attributes
Parameter
Description
Type
Size
Default
default
CASB attribute default value.
option
-string
Option
Description
string
String type.
string-list
String list type.
FortiOS 8.0.0 CLI Reference
235
Fortinet Inc.

<!-- 来源页 236 -->
Parameter
Description
Type
Size
Default
description
CASB attribute description.
string
Maximum
length: 63
fallback-input
CASB attribute legacy input.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
name
CASB attribute name.
string
Maximum
length: 79
required
CASB input attribute required.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
type
CASB attribute format type.
option
-string
Option
Description
string
String type.
config output-attributes
Parameter
Description
Type
Size
Default
description
CASB attribute description.
string
Maximum
length: 63
name
CASB attribute name.
string
Maximum
length: 79
optional
CASB output attribute optional.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
type
CASB attribute format type.
option
-string
Option
Description
string
String type.
FortiOS 8.0.0 CLI Reference
236
Fortinet Inc.

<!-- 来源页 237 -->
Parameter
Description
Type
Size
Default
Option
Description
string-list
String list type.
integer
Integer type.
integer-list
Integer list type.
boolean
Boolean type.
config casb user-activity
Configure CASB user activity.
config casb user-activity
Description: Configure CASB user activity.
edit <name>
set application {string}
set casb-name {string}
set category [activity-control|tenant-control|...]
config control-options
Description: CASB control options.
edit <name>
config operations
Description: CASB control option operations.
edit <name>
set action [append|prepend|...]
set case-sensitive [enable|disable]
set direction [request|response]
set header-name {string}
set search-key {string}
set search-pattern [simple|substr|...]
set target [header|path|...]
set value-from-input [enable|disable]
set value-name-from-input {string}
set values <value1>, <value2>, ...
next
end
set status [enable|disable]
next
end
set description {string}
config match
Description: CASB user activity match rules.
edit <id>
config rules
Description: CASB user activity rules.
edit <id>
set body-type [json|form]
FortiOS 8.0.0 CLI Reference
237
Fortinet Inc.

<!-- 来源页 238 -->
set case-sensitive [enable|disable]
set domains <domain1>, <domain2>, ...
set header-name {string}
set jq {string}
set match-pattern [simple|substr|...]
set match-value {string}
set methods <method1>, <method2>, ...
set negate [enable|disable]
set type [domains|host|...]
next
end
set strategy [and|or]
config tenant-extraction
Description: CASB user activity tenant extraction.
config filters
Description: CASB user activity tenant extraction filters.
edit <id>
set body-type [json|form]
set direction [request|response]
set header-name {string}
set place [path|header|...]
next
end
set jq {string}
set status [disable|enable]
set type {option}
end
config tenant-session-extraction
Description: CASB user activity tenant session extraction.
config filters
Description: CASB user activity session extraction filters.
edit <id>
set body-type [json|form]
set cookie-name {string}
set direction [request|response]
set header-name {string}
set place [path|header|...]
next
end
set jq {string}
set session-match {string}
set session-source [disable|enable]
set status [disable|enable]
end
next
end
set match-strategy [and|or]
set status [enable|disable]
set type [built-in|customized]
set uuid {string}
next
end
FortiOS 8.0.0 CLI Reference
238
Fortinet Inc.

<!-- 来源页 239 -->
config casb user-activity
Parameter
Description
Type
Size
Default
application
CASB SaaS application name.
string
Maximum
length: 79
casb-name
CASB user activity signature name.
string
Maximum
length: 79
category
CASB user activity category.
option
-activity-control
Option
Description
activity-control
Activity control.
tenant-control
Tenant control.
domain-control
Domain control.
safe-search-control
Safe search control.
advanced-tenant-control
Advanced tenant control.
other
User customized category.
description
CASB user activity description.
string
Maximum
length: 63
match-strategy
CASB user activity match strategy.
option
-or
Option
Description
and
Match user activity using a logical AND operator.
or
Match user activity using a logical OR operator.
name
CASB user activity name.
string
Maximum
length: 79
status
CASB user activity status.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
type
CASB user activity type.
option
-customized
FortiOS 8.0.0 CLI Reference
239
Fortinet Inc.

<!-- 来源页 240 -->
Parameter
Description
Type
Size
Default
Option
Description
built-in
Built-in CASB user-activity.
customized
User customized CASB user-activity.
uuid
Universally Unique Identifier (UUID;
automatically assigned but can be manually
reset).
string
Maximum
length: 36
config control-options
Parameter
Description
Type
Size
Default
name
CASB control option name.
string
Maximum
length: 79
status
CASB control option status.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
config operations
Parameter
Description
Type
Size
Default
action
CASB operation action.
option
-append
Option
Description
append
Append the values after the target.
prepend
Prepend the values before the target.
replace
Replace the target by the value.
new
Create a new header regardless if existing header is found or not.
new-on-not-found
Create new header only if existing HTTP header is not found.
delete
Delete the target.
case-sensitive
CASB operation search case sensitive.
option
-disable
FortiOS 8.0.0 CLI Reference
240
Fortinet Inc.

<!-- 来源页 241 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable case sensitive search.
disable
Disable case sensitive search.
direction
CASB operation direction.
option
-request
Option
Description
request
Request.
response
Response.
header-name
CASB operation header name to search.
string
Maximum
length: 255
name
CASB control option operation name.
string
Maximum
length: 79
search-key
CASB operation key to search.
string
Maximum
length:
1023
search-pattern
CASB operation search pattern.
option
-simple
Option
Description
simple
Exact string match pattern.
substr
Sub-string pattern.
regexp
Regular expression pattern.
target
CASB operation target.
option
-header
Option
Description
header
Header.
path
Path.
body
Body.
value-from-input
Enable/disable value from user input.
option
-disable
Option
Description
enable
Enable value from input.
disable
Disable value from input.
FortiOS 8.0.0 CLI Reference
241
Fortinet Inc.

<!-- 来源页 242 -->
Parameter
Description
Type
Size
Default
value-name-from-input
CASB operation value name from user input.
string
Maximum
length: 79
values
<value>
CASB operation new values.
Operation value.
string
Maximum
length: 79
config match
Parameter
Description
Type
Size
Default
id
CASB user activity match rules ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
strategy
CASB user activity rules strategy.
option
-and
Option
Description
and
Match user activity using a logical AND operator.
or
Match user activity using a logical OR operator.
config rules
Parameter
Description
Type
Size
Default
body-type
CASB user activity match rule body type.
option
-json
Option
Description
json
JSON body type.
form
Form body type.
case-sensitive
CASB user activity match case sensitive.
option
-disable
Option
Description
enable
Enable value case sensitive match.
disable
Disable value case sensitive match.
domains
<domain>
CASB user activity domain list.
Domain list separated by space.
string
Maximum
length: 127
header-name
CASB user activity rule header name.
string
Maximum
length: 255
FortiOS 8.0.0 CLI Reference
242
Fortinet Inc.

<!-- 来源页 243 -->
Parameter
Description
Type
Size
Default
id
CASB user activity rule ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
jq
CASB user activity rule match jq script.
string
Maximum
length: 255
match-pattern
CASB user activity rule match pattern.
option
-simple
Option
Description
simple
Exact string match pattern.
substr
Sub-string pattern.
regexp
Regular expression pattern.
match-value
CASB user activity rule match value.
string
Maximum
length: 1023
methods
<method>
CASB user activity method list.
User activity method.
string
Maximum
length: 79
negate
Enable/disable what the matching strategy must
not be.
option
-disable
Option
Description
enable
Matching strategy is negated.
disable
Matching strategy is not negated.
type
CASB user activity rule type.
option
-host
Option
Description
domains
Domains.
host
Host.
path
Path.
header
HTTP header.
header-value
HTTP header and value.
method
HTTP method.
body
HTTP body.
FortiOS 8.0.0 CLI Reference
243
Fortinet Inc.

<!-- 来源页 244 -->
config tenant-extraction
Parameter
Description
Type
Size
Default
jq
CASB user activity tenant extraction jq script.
string
Maximum
length:
1023
status
Enable/disable CASB tenant extraction.
option
-disable
Option
Description
disable
Disable tenant extraction.
enable
Enable tenant extraction.
type
CASB user activity tenant extraction type.
option
-json-query
Option
Description
json-query
HTTP JSON body extraction.
config filters
Parameter
Description
Type
Size
Default
body-type
CASB content extraction filter body type.
option
-json
Option
Description
json
JSON body type.
form
Form body type.
direction
CASB content extraction filter direction.
option
-request
Option
Description
request
Request.
response
Response.
header-name
CASB content extraction filter header name.
string
Maximum
length: 255
id
CASB content extraction filter ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
place
CASB content extraction filter place type.
option
-header
FortiOS 8.0.0 CLI Reference
244
Fortinet Inc.

<!-- 来源页 245 -->
Parameter
Description
Type
Size
Default
Option
Description
path
Path.
header
HTTP header.
body
HTTP body.
config tenant-session-extraction
Parameter
Description
Type
Size
Default
jq
CASB user activity session extraction jq script.
string
Maximum
length:
1023
session-match
CASB user activity session match name.
string
Maximum
length: 79
session-source
Enable/disable CASB session extraction source
flag.
option
-disable
Option
Description
disable
Disable session extraction source flag.
enable
Enable session extraction source flag.
status
Enable/disable CASB session extraction.
option
-disable
Option
Description
disable
Disable session extraction.
enable
Enable session extraction.
config filters
Parameter
Description
Type
Size
Default
body-type
CASB content extraction filter body type.
option
-json
Option
Description
json
JSON body type.
form
Form body type.
cookie-name
CASB content extraction filter cookie name.
string
Maximum
length: 255
FortiOS 8.0.0 CLI Reference
245
Fortinet Inc.

<!-- 来源页 246 -->
Parameter
Description
Type
Size
Default
direction
CASB content extraction filter direction.
option
-request
Option
Description
request
Request.
response
Response.
header-name
CASB content extraction filter header name.
string
Maximum
length: 255
id
CASB content extraction filter ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
place
CASB content extraction filter place type.
option
-header
Option
Description
path
Path.
header
HTTP header.
cookie
HTTP cookie.
body
HTTP body.
FortiOS 8.0.0 CLI Reference
246
Fortinet Inc.

---


<!-- 来源页 261 -->
diameter-filter
This section includes syntax for the following commands:
l config diameter-filter profile on page 261
config diameter-filter profile
Configure Diameter filter profiles.
config diameter-filter profile
Description: Configure Diameter filter profiles.
edit <name>
set cmd-flags-reserve-set [allow|block|...]
set command-code-invalid [allow|block|...]
set command-code-range {user}
set comment {var-string}
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set log-packet [disable|enable]
set message-length-invalid [allow|block|...]
set missing-request-action [allow|block|...]
set monitor-all-messages [disable|enable]
set protocol-version-invalid [allow|block|...]
set request-error-flag-set [allow|block|...]
set track-requests-answers [disable|enable]
set uuid {uuid}
next
end
config diameter-filter profile
Parameter
Description
Type
Size
Default
cmd-flags-reserve-set
Action to be taken for messages with cmd
flag reserve bits set.
option
-block
Option
Description
allow
Allow or pass matching traffic.
block
Block or drop matching traffic.
FortiOS 8.0.0 CLI Reference
261
Fortinet Inc.

<!-- 来源页 262 -->
Parameter
Description
Type
Size
Default
Option
Description
reset
Reset sessions for matching traffic.
monitor
Allow and log matching traffic.
command-code-invalid
Action to be taken for messages with invalid
command code.
option
-block
Option
Description
allow
Allow or pass matching traffic.
block
Block or drop matching traffic.
reset
Reset sessions for matching traffic.
monitor
Allow and log matching traffic.
command-code-range
Valid range for command codes (0-16777215).
user
Not
Specified
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
FortiOS 8.0.0 CLI Reference
262
Fortinet Inc.

<!-- 来源页 263 -->
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
log-packet
Enable/disable packet log for triggered
diameter settings.
option
-disable
Option
Description
disable
Disable.
enable
Enable.
message-length-invalid
Action to be taken for invalid message
length.
option
-block
Option
Description
allow
Allow or pass matching traffic.
block
Block or drop matching traffic.
reset
Reset sessions for matching traffic.
monitor
Allow and log matching traffic.
missing-request-action
Action to be taken for answers without
corresponding request.
option
-block
Option
Description
allow
Allow or pass matching traffic.
block
Block or drop matching traffic.
reset
Reset sessions for matching traffic.
monitor
Allow and log matching traffic.
monitor-all-messages
Enable/disable logging for all User Name and
Result Code AVP messages.
option
-disable
Option
Description
disable
Disable.
enable
Enable.
name
Profile name.
string
Maximum
length: 47
FortiOS 8.0.0 CLI Reference
263
Fortinet Inc.

<!-- 来源页 264 -->
Parameter
Description
Type
Size
Default
protocol-version-invalid
Action to be taken for invalid protocol
version.
option
-block
Option
Description
allow
Allow or pass matching traffic.
block
Block or drop matching traffic.
reset
Reset sessions for matching traffic.
monitor
Allow and log matching traffic.
request-error-flag-set
Action to be taken for request messages
with error flag set.
option
-block
Option
Description
allow
Allow or pass matching traffic.
block
Block or drop matching traffic.
reset
Reset sessions for matching traffic.
monitor
Allow and log matching traffic.
track-requests-answers
Enable/disable validation that each answer
has a corresponding request.
option
-enable
Option
Description
disable
Disable.
enable
Enable.
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be manually
reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
FortiOS 8.0.0 CLI Reference
264
Fortinet Inc.

---


<!-- 来源页 265 -->
dlp
This section includes syntax for the following commands:
l config dlp data-type on page 265
l config dlp dictionary on page 267
l config dlp exact-data-match on page 269
l config dlp filepattern on page 270
l config dlp fp-doc-source on page 275
l config dlp label on page 279
l config dlp profile on page 281
l config dlp sensitivity on page 288
l config dlp sensor on page 289
l config dlp settings on page 291
config dlp data-type
Configure predefined data type used by DLP blocking.
config dlp data-type
Description: Configure predefined data type used by DLP blocking.
edit <name>
set comment {var-string}
set look-ahead {integer}
set look-back {integer}
set match-ahead {integer}
set match-around {string}
set match-back {integer}
set pattern {string}
set transform {string}
set verify {string}
set verify-transformed-pattern [enable|disable]
set verify2 {string}
next
end
FortiOS 8.0.0 CLI Reference
265
Fortinet Inc.

<!-- 来源页 266 -->
config dlp data-type
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
look-ahead
Number of characters to obtain in advance for
verification (1 - 255, default = 1).
integer
Minimum
value: 1
Maximum
value: 255
1
look-back
Number of characters required to save for
verification (1 - 255, default = 1).
integer
Minimum
value: 1
Maximum
value: 255
1
match-ahead
Number of characters behind for match-around (1
- 4096, default = 1).
integer
Minimum
value: 1
Maximum
value: 4096
1
match-around
Dictionary to check whether it has a match
around (Only support match-any and basic types,
no repeat supported).
string
Maximum
length: 35
match-back
Number of characters in front for match-around
(1 - 4096, default = 1).
integer
Minimum
value: 1
Maximum
value: 4096
1
name
Name of table containing the data type.
string
Maximum
length: 35
pattern
Regular expression pattern string without look
around.
string
Maximum
length: 255
transform
Template to transform user input to a pattern
using capture group from 'pattern'.
string
Maximum
length: 255
verify
Regular expression pattern string used to verify
the data type.
string
Maximum
length: 255
verify-transformed-pattern
Enable/disable verification for transformed
pattern.
option
-disable
Option
Description
enable
Enable verification for transformed pattern.
disable
Disable verification for transformed pattern.
verify2
Extra regular expression pattern string used to
verify the data type.
string
Maximum
length: 255
FortiOS 8.0.0 CLI Reference
266
Fortinet Inc.

<!-- 来源页 267 -->
config dlp dictionary
Configure dictionaries used by DLP blocking.
config dlp dictionary
Description: Configure dictionaries used by DLP blocking.
edit <name>
set comment {var-string}
config entries
Description: DLP dictionary entries.
edit <id>
set comment {var-string}
set ignore-case [enable|disable]
set pattern {string}
set repeat [enable|disable]
set status [enable|disable]
set type {string}
next
end
set match-around [enable|disable]
set match-type [match-all|match-any]
set uuid {uuid}
next
end
config dlp dictionary
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
match-around
Enable/disable match-around support.
option
-disable
Option
Description
enable
Enable match-around support.
disable
Disable match-around support.
match-type
Logical relation between entries (default =
match-any).
option
-match-any
Option
Description
match-all
Match all entries.
match-any
Match any entries.
FortiOS 8.0.0 CLI Reference
267
Fortinet Inc.

<!-- 来源页 268 -->
Parameter
Description
Type
Size
Default
name
Name of table containing the dictionary.
string
Maximum
length: 35
uuid
Universally Unique Identifier (UUID;
automatically assigned but can be manually
reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
config entries
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
id
ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
ignore-case
Enable/disable ignore case.
option
-disable
Option
Description
enable
Enable ignore case.
disable
Disable ignore case.
pattern
Pattern to match.
string
Maximum
length: 255
repeat
Enable/disable repeat match.
option
-disable
Option
Description
enable
Enable repeat match.
disable
Disable repeat match.
status
Enable/disable this pattern.
option
-enable
Option
Description
enable
Enable this pattern.
disable
Disable this pattern.
type
Pattern type to match.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
268
Fortinet Inc.

<!-- 来源页 269 -->
config dlp exact-data-match
Configure exact-data-match template used by DLP scan.
config dlp exact-data-match
Description: Configure exact-data-match template used by DLP scan.
edit <name>
config columns
Description: DLP exact-data-match column types.
edit <index>
set optional [enable|disable]
set type {string}
next
end
set data {string}
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set optional {integer}
set uuid {uuid}
next
end
config dlp exact-data-match
Parameter
Description
Type
Size
Default
data
External resource for exact data match.
string
Maximum
length: 35
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
FortiOS 8.0.0 CLI Reference
269
Fortinet Inc.

<!-- 来源页 270 -->
Parameter
Description
Type
Size
Default
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
name
Name of table containing the exact-data-match template.
string
Maximum
length: 35
optional
Number of optional columns need to match.
integer
Minimum
value: 0
Maximum
value: 32
0 **
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
config columns
Parameter
Description
Type
Size
Default
index
Column index.
integer
Minimum
value: 1
Maximum
value: 32
0
optional
Enable/disable optional match.
option
-disable
Option
Description
enable
Enable optional match.
disable
Disable optional match.
type
Data-type for this column.
string
Maximum
length: 35
config dlp filepattern
Configure file patterns used by DLP blocking.
FortiOS 8.0.0 CLI Reference
270
Fortinet Inc.

<!-- 来源页 271 -->
config dlp filepattern
Description: Configure file patterns used by DLP blocking.
edit <id>
set comment {var-string}
config entries
Description: Configure file patterns used by DLP blocking.
edit <pattern>
set file-type [7z|arj|...]
set filter-type [pattern|type]
next
end
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set name {string}
set uuid {uuid}
next
end
config dlp filepattern
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
FortiOS 8.0.0 CLI Reference
271
Fortinet Inc.

<!-- 来源页 272 -->
Parameter
Description
Type
Size
Default
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
Name of table containing the file pattern
list.
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
file-type
Select a file type.
option
-unknown
Option
Description
7z
Match 7-zip files.
arj
Match arj compressed files.
cab
Match Windows cab files.
lzh
Match lzh compressed files.
rar
Match rar archives.
tar
Match tar files.
zip
Match zip files.
bzip
Match bzip files.
gzip
Match gzip files.
bzip2
Match bzip2 files.
FortiOS 8.0.0 CLI Reference
272
Fortinet Inc.

<!-- 来源页 273 -->
Parameter
Description
Type
Size
Default
Option
Description
xz
Match xz files.
bat
Match Windows batch files.
uue
Match uue files.
mime
Match mime files.
base64
Match base64 files.
binhex
Match binhex files.
elf
Match elf files.
exe
Match Windows executable files.
dll
Match dll files.
jnlp
Match jnlp files.
hta
Match hta files.
html
Match html files.
jad
Match jad files.
class
Match class files.
cod
Match cod files.
javascript
Match javascript files.
msoffice
Match legacy MS-Office files. doc, ppt, and xls.
msofficex
Match MS-Office XML files. docm, docx, pptm, pptx, xlsm, and xlsx.
fsg
Match fsg files.
upx
Match upx files.
petite
Match petite files.
aspack
Match aspack files.
sis
Match sis files.
hlp
Match Windows help files.
activemime
Match activemime files.
jpeg
Match jpeg files.
gif
Match gif files.
tiff
Match tiff files.
png
Match png files.
FortiOS 8.0.0 CLI Reference
273
Fortinet Inc.

<!-- 来源页 274 -->
Parameter
Description
Type
Size
Default
Option
Description
bmp
Match bmp files.
unknown
Match unknown files.
mpeg
Match mpeg files.
mov
Match mov files.
mp3
Match mp3 files.
wma
Match wma files.
wav
Match wav files.
pdf
Match Acrobat PDF files.
avi
Match avi files.
rm
Match rm files.
torrent
Match torrent files.
hibun
Match special-file-23-support files.
msi
Match Windows Installer msi files.
mach-o
Match Mach object files.
dmg
Match Apple disk image files.
.net
Match .NET files.
xar
Match xar archive files.
chm
Match Windows compiled HTML help files.
iso
Match ISO archive files.
crx
Match Chrome extension files.
flac
Match flac files.
registry
Match registry files.
hwp
Match hwp files.
rpm
Match rpm files.
genscript
Match generic script files.
python
Match python files.
c/cpp
Match c/cpp files.
pfile
Match pfile files.
lzip
Match lzip files.
FortiOS 8.0.0 CLI Reference
274
Fortinet Inc.

<!-- 来源页 275 -->
Parameter
Description
Type
Size
Default
Option
Description
wasm
Match WebAssembly files.
sylk
Match Microsoft symbolic link files.
shellscript
Match shell script files.
filter-type
Filter by file name pattern or by file type.
option
-pattern
Option
Description
pattern
Filter by file name pattern.
type
Filter by file type.
pattern
Add a file name pattern.
string
Maximum
length: 79
config dlp fp-doc-source
This command is available for model(s): FortiGate 1000D, FortiGate 1001F, FortiGate 101F Gen2,
FortiGate 1101E, FortiGate 121G, FortiGate 1801F, FortiGate 2000E, FortiGate 201E, FortiGate 201F,
FortiGate 201G, FortiGate 2201E, FortiGate 2500E, FortiGate 2600F, FortiGate 2601F, FortiGate
3001F, FortiGate 301E, FortiGate 3201F Gen2, FortiGate 3301E, FortiGate 3401E, FortiGate 3501F
Gen2, FortiGate 3601E, FortiGate 3701F, FortiGate 401E, FortiGate 401F, FortiGate 4201F Gen2,
FortiGate 4401F Gen2, FortiGate 4801F, FortiGate 501E, FortiGate 601E, FortiGate 601F, FortiGate
70F, FortiGate 70G-POE, FortiGate 70G, FortiGate 71F, FortiGate 71G-POE, FortiGate 71G, FortiGate
800D, FortiGate 80F Bypass, FortiGate 81F Gen2, FortiGate 81F-POE, FortiGate 900D, FortiGate
901G, FortiGate 91G Gen2, FortiGate 91G, FortiGate-VM64 Aliyun, FortiGate-VM64 AWS, FortiGate-VM64 Azure, FortiGate-VM64 GCP, FortiGate-VM64 OPC, FortiGate-VM64, FortiGateRugged 70F
3G4G, FortiGateRugged 70F, FortiGateRugged 70G 5G Dual, FortiGateRugged 70G, FortiWiFi 70G-POE, FortiWiFi 70G, FortiWiFi 71G, FortiWiFi 80F 2R 3G4G DSL, FortiWiFi 80F 2R, FortiWiFi 81F 2R
3G4G DSL, FortiWiFi 81F 2R 3G4G-POE, FortiWiFi 81F 2R-POE, FortiWiFi 81F 2R.
It is not available for: FortiGate 1000F, FortiGate 100F, FortiGate 1100E, FortiGate 120G, FortiGate
1800F, FortiGate 200E, FortiGate 200F, FortiGate 200G, FortiGate 2200E, FortiGate 3000F,
FortiGate 300E, FortiGate 30G, FortiGate 31G, FortiGate 3200F, FortiGate 3300E, FortiGate 3400E,
FortiGate 3500F Gen2, FortiGate 3600E, FortiGate 3700F, FortiGate 3960E, FortiGate 3980E,
FortiGate 400E Bypass, FortiGate 400E, FortiGate 400F, FortiGate 40F 3G4G, FortiGate 40F,
FortiGate 4200F, FortiGate 4400F, FortiGate 4800F, FortiGate 500E, FortiGate 50G 5G, FortiGate
50G DSL, FortiGate 50G SFP-POE, FortiGate 50G SFP, FortiGate 50G, FortiGate 51G 5G, FortiGate
51G SFP-POE, FortiGate 51G, FortiGate 600E, FortiGate 600F, FortiGate 60F, FortiGate 61F,
FortiGate 80F DSL, FortiGate 80F Gen2, FortiGate 80F-POE, FortiGate 900G, FortiGate 90G Gen2,
FortiGate 90G, FortiGateRugged 50G 5G, FortiGateRugged 60F 3G4G, FortiGateRugged 60F Gen2,
FortiWiFi 30G, FortiWiFi 31G, FortiWiFi 40F 3G4G, FortiWiFi 40F, FortiWiFi 50G 5G, FortiWiFi 50G
DSL, FortiWiFi 50G SFP, FortiWiFi 50G, FortiWiFi 51G, FortiWiFi 60F, FortiWiFi 61F.
FortiOS 8.0.0 CLI Reference
275
Fortinet Inc.

<!-- 来源页 276 -->
Create a DLP fingerprint database by allowing the FortiGate to access a file server containing files from which to
create fingerprints.
config dlp fp-doc-source
Description: Create a DLP fingerprint database by allowing the FortiGate to access a file
server containing files from which to create fingerprints.
edit <name>
set date {integer}
set file-path {string}
set file-pattern {string}
set keep-modified [enable|disable]
set password {password}
set period [none|daily|...]
set remove-deleted [enable|disable]
set scan-on-creation [enable|disable]
set scan-subdirectories [enable|disable]
set sensitivity {string}
set server {string}
set server-type {option}
set tod-hour {integer}
set tod-min {integer}
set username {string}
set uuid {uuid}
set vdom [mgmt|current]
set weekday [sunday|monday|...]
next
end
config dlp fp-doc-source
Parameter
Description
Type
Size
Default
date
Day of the month on which to scan the
server (1 - 31).
integer
Minimum
value: 1
Maximum
value: 31
1
file-path
Path on the server to the fingerprint files
(max 119 characters).
string
Maximum
length: 119
file-pattern
Files matching this pattern on the server
are fingerprinted. Optionally use the *
and ? wildcards.
string
Maximum
length: 35
*
keep-modified
Enable so that when a file is changed on
the server the FortiGate keeps the old
fingerprint and adds a new fingerprint to
the database.
option
-enable
FortiOS 8.0.0 CLI Reference
276
Fortinet Inc.

<!-- 来源页 277 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Keep the old fingerprint and add a new fingerprint when a file is
changed on the server.
disable
Replace the old fingerprint with the new fingerprint when a file is
changed on the server.
name
Name of the DLP fingerprint database.
string
Maximum
length: 35
password
Password required to log into the file
server.
password
Not
Specified
period
Frequency for which the FortiGate
checks the server for new or changed
files.
option
-none
Option
Description
none
Check the server when the FortiGate starts up.
daily
Check the server once a day.
weekly
Check the server once a week.
monthly
Check the server once a month.
remove-deleted
Enable to keep the fingerprint database
up to date when a file is deleted from the
server.
option
-enable
Option
Description
enable
Keep the fingerprint database up to date when a file is deleted from
the server.
disable
Do not check for deleted files on the server. Saves system resources.
scan-on-creation
Initiate an immediate update of the
fingerprint database after creating this
fp-doc-source entry.
option
-enable
Option
Description
enable
Immediately scan the file server after creating this entry.
disable
Disable immediate scan of the file server. Files will be scanned at the
scheduled interval.
scan-subdirectories
Enable/disable scanning subdirectories
to find files to create fingerprints from.
option
-enable
FortiOS 8.0.0 CLI Reference
277
Fortinet Inc.

<!-- 来源页 278 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Scan subdirectories.
disable
Do not scan subdirectories.
sensitivity
Select a sensitivity or threat level for
matches with this fingerprint database.
Add sensitivities using sensitivity.
string
Maximum
length: 35
server
IPv4 or IPv6 address of the server.
string
Maximum
length: 63
**
server-type
Protocol used to communicate with the
file server. Currently only Samba (SMB)
servers are supported.
option
-samba
Option
Description
samba
SAMBA server.
tod-hour
Hour of the day on which to scan the
server (0 - 23, default = 1).
integer
Minimum
value: 0
Maximum
value: 23
1
tod-min
Minute of the hour on which to scan the
server (0 - 59).
integer
Minimum
value: 0
Maximum
value: 59
0
username
User name required to log into the file
server.
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
vdom
Select the VDOM that can communicate
with the file server.
option
-mgmt
Option
Description
mgmt
Communicate with the file server through the management VDOM.
current
Communicate with the file server through the VDOM containing this
DLP fingerprint database configuration.
weekday
Day of the week on which to scan the
server.
option
-sunday
FortiOS 8.0.0 CLI Reference
278
Fortinet Inc.

<!-- 来源页 279 -->
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
* This parameter may not exist in some models.
** Values may differ between models.
config dlp label
Configure labels used by DLP blocking.
config dlp label
Description: Configure labels used by DLP blocking.
edit <name>
set comment {var-string}
set connector {string}
config entries
Description: DLP label entries.
edit <id>
set fortidata-label-name {string}
set guid {string}
set mpip-label-name {string}
next
end
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set mpip-type [remote|local]
set type [mpip|fortidata]
set uuid {uuid}
next
end
FortiOS 8.0.0 CLI Reference
279
Fortinet Inc.

<!-- 来源页 280 -->
config dlp label
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
connector
Name of SDN connector.
string
Maximum
length: 35
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
mpip-type
MPIP label type.
option
-remote
Option
Description
remote
Remotely fetched MPIP labels.
local
Locally configured MPIP labels.
name
Name of table containing the label.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
280
Fortinet Inc.

<!-- 来源页 281 -->
Parameter
Description
Type
Size
Default
type
Label type.
option
-mpip
Option
Description
mpip
Microsoft Purview Information Protection.
fortidata
FortiData.
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be manually
reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
config entries
Parameter
Description
Type
Size
Default
fortidata-label-name
Name of FortiData label
string
Maximum
length: 127
guid
MPIP label guid.
string
Maximum
length: 36
id
ID.
integer
Minimum
value: 1
Maximum
value: 32
0
mpip-label-name
Name of MPIP label.
string
Maximum
length: 127
config dlp profile
Configure DLP profiles.
config dlp profile
Description: Configure DLP profiles.
edit <name>
set comment {var-string}
set dlp-log [enable|disable]
set extended-log [enable|disable]
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set feature-set [flow|proxy]
set fortidata-error-action [log-only|block|...]
set fortidata-scan-timeout {integer}
set full-archive-proto {option1}, {option2}, ...
FortiOS 8.0.0 CLI Reference
281
Fortinet Inc.

<!-- 来源页 282 -->
set nac-quar-log [enable|disable]
set replacemsg-group {string}
config rule
Description: Set up DLP rules for this profile.
edit <id>
set action [allow|log-only|...]
set archive [disable|enable]
set expiry {user}
set file-size {integer}
set file-type {integer}
set filter-by [sensor|label|...]
set label {string}
set match-percentage {integer}
set name {string}
set proto {option1}, {option2}, ...
set sensitivity <name1>, <name2>, ...
set sensor <name1>, <name2>, ...
set severity [info|low|...]
set type [file|message]
next
end
set summary-proto {option1}, {option2}, ...
set uuid {uuid}
next
end
config dlp profile
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
dlp-log
Enable/disable DLP logging.
option
-enable
Option
Description
enable
Enable DLP logging.
disable
Disable DLP logging.
extended-log
Enable/disable extended logging for data
loss prevention.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
FortiOS 8.0.0 CLI Reference
282
Fortinet Inc.

<!-- 来源页 283 -->
Parameter
Description
Type
Size
Default
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
fortidata-error-action
Action to take if FortiData query fails.
option
-block
Option
Description
log-only
Log failure, but allow the file.
block
Block the file.
ignore
Behave as if FortiData returned no match.
FortiOS 8.0.0 CLI Reference
283
Fortinet Inc.

<!-- 来源页 284 -->
Parameter
Description
Type
Size
Default
fortidata-scan-timeout *
FortiData inline scan timeout in seconds (10
- 30, default = 15).
integer
Minimum
value: 10
Maximum
value: 30
15
full-archive-proto
Protocols to always content archive.
option
-Option
Description
smtp
SMTP.
pop3
POP3.
imap
IMAP.
http-get
HTTP GET.
http-post
HTTP POST.
ftp
FTP.
nntp
NNTP.
mapi
MAPI.
ssh
SFTP and SCP.
cifs
CIFS.
websocket
WEBSOCKET.
nac-quar-log
Enable/disable NAC quarantine logging.
option
-disable
Option
Description
enable
Enable NAC quarantine logging.
disable
Disable NAC quarantine logging.
name
Name of the DLP profile.
string
Maximum
length: 47
replacemsg-group
Replacement message group used by this
DLP profile.
string
Maximum
length: 35
summary-proto
Protocols to always log summary.
option
-Option
Description
smtp
SMTP.
pop3
POP3.
FortiOS 8.0.0 CLI Reference
284
Fortinet Inc.

<!-- 来源页 285 -->
Parameter
Description
Type
Size
Default
Option
Description
imap
IMAP.
http-get
HTTP GET.
http-post
HTTP POST.
ftp
FTP.
nntp
NNTP.
mapi
MAPI.
ssh
SFTP and SCP.
cifs
CIFS.
websocket
WEBSOCKET.
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be manually
reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
config rule
Parameter
Description
Type
Size
Default
action
Action to take with content that this DLP profile
matches.
option
-allow
Option
Description
allow
Allow the content to pass through the FortiGate and do not create a log
message.
log-only
Allow the content to pass through the FortiGate, but write a log
message.
block
Block the content and write a log message.
quarantine-ip
Quarantine all traffic from the IP address and write a log message.
archive
Enable/disable DLP archiving.
option
-disable
Option
Description
disable
No DLP archiving.
enable
Enable full DLP archiving.
FortiOS 8.0.0 CLI Reference
285
Fortinet Inc.

<!-- 来源页 286 -->
Parameter
Description
Type
Size
Default
expiry
Quarantine duration in days, hours, minutes
(format = dddhhmm).
user
Not Specified
5m
file-size
Match files greater than or equal to this size
(KB).
integer
Minimum value:
0 Maximum
value: 1644544
**
0
file-type
Select the number of a DLP file pattern table to
match.
integer
Minimum value:
0 Maximum
value:
4294967295
0
filter-by
Select the type of content to match.
option
-none
Option
Description
sensor
Use DLP sensors to match content.
label
Use DLP labels to match content.
fingerprint
Match against a fingerprint sensitivity.
encrypted
Look for encrypted files.
none
No content scan.
id
ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
label
Select DLP label.
string
Maximum
length: 35
match-percentage *
Percentage of fingerprints in the fingerprint
databases designated with the selected
sensitivity to match.
integer
Minimum value:
1 Maximum
value: 100
10
name
Filter name.
string
Maximum
length: 35
proto
Check messages or files over one or more of
these protocols.
option
-Option
Description
smtp
SMTP.
pop3
POP3.
imap
IMAP.
FortiOS 8.0.0 CLI Reference
286
Fortinet Inc.

<!-- 来源页 287 -->
Parameter
Description
Type
Size
Default
Option
Description
http-get
HTTP GET.
http-post
HTTP POST.
ftp
FTP.
nntp
NNTP.
mapi
MAPI.
ssh
SFTP and SCP.
cifs
CIFS.
websocket
WEBSOCKET.
sensitivity
<name> *
Select a DLP file pattern sensitivity to match.
Select a DLP sensitivity.
string
Maximum
length: 35
sensor
<name>
Select DLP sensors.
Sensor name.
string
Maximum
length: 35
severity
Select the severity or threat level that matches
this filter.
option
-medium
Option
Description
info
Informational.
low
Low.
medium
Medium.
high
High.
critical
Critical.
type
Select whether to check the content of
messages (an email message) or files
(downloaded files or email attachments).
option
-file
Option
Description
file
Check the contents of downloaded or attached files.
message
Check the contents of email messages, web pages, etc.
* This parameter may not exist in some models.
** Values may differ between models.
FortiOS 8.0.0 CLI Reference
287
Fortinet Inc.

<!-- 来源页 288 -->
config dlp sensitivity
This command is available for model(s): FortiGate 1000D, FortiGate 1001F, FortiGate 101F Gen2,
FortiGate 1101E, FortiGate 121G, FortiGate 1801F, FortiGate 2000E, FortiGate 201E, FortiGate 201F,
FortiGate 201G, FortiGate 2201E, FortiGate 2500E, FortiGate 2600F, FortiGate 2601F, FortiGate
3001F, FortiGate 301E, FortiGate 3201F Gen2, FortiGate 3301E, FortiGate 3401E, FortiGate 3501F
Gen2, FortiGate 3601E, FortiGate 3701F, FortiGate 401E, FortiGate 401F, FortiGate 4201F Gen2,
FortiGate 4401F Gen2, FortiGate 4801F, FortiGate 501E, FortiGate 601E, FortiGate 601F, FortiGate
70F, FortiGate 70G-POE, FortiGate 70G, FortiGate 71F, FortiGate 71G-POE, FortiGate 71G, FortiGate
800D, FortiGate 80F Bypass, FortiGate 81F Gen2, FortiGate 81F-POE, FortiGate 900D, FortiGate
901G, FortiGate 91G Gen2, FortiGate 91G, FortiGate-VM64 Aliyun, FortiGate-VM64 AWS, FortiGate-VM64 Azure, FortiGate-VM64 GCP, FortiGate-VM64 OPC, FortiGate-VM64, FortiGateRugged 70F
3G4G, FortiGateRugged 70F, FortiGateRugged 70G 5G Dual, FortiGateRugged 70G, FortiWiFi 70G-POE, FortiWiFi 70G, FortiWiFi 71G, FortiWiFi 80F 2R 3G4G DSL, FortiWiFi 80F 2R, FortiWiFi 81F 2R
3G4G DSL, FortiWiFi 81F 2R 3G4G-POE, FortiWiFi 81F 2R-POE, FortiWiFi 81F 2R.
It is not available for: FortiGate 1000F, FortiGate 100F, FortiGate 1100E, FortiGate 120G, FortiGate
1800F, FortiGate 200E, FortiGate 200F, FortiGate 200G, FortiGate 2200E, FortiGate 3000F,
FortiGate 300E, FortiGate 30G, FortiGate 31G, FortiGate 3200F, FortiGate 3300E, FortiGate 3400E,
FortiGate 3500F Gen2, FortiGate 3600E, FortiGate 3700F, FortiGate 3960E, FortiGate 3980E,
FortiGate 400E Bypass, FortiGate 400E, FortiGate 400F, FortiGate 40F 3G4G, FortiGate 40F,
FortiGate 4200F, FortiGate 4400F, FortiGate 4800F, FortiGate 500E, FortiGate 50G 5G, FortiGate
50G DSL, FortiGate 50G SFP-POE, FortiGate 50G SFP, FortiGate 50G, FortiGate 51G 5G, FortiGate
51G SFP-POE, FortiGate 51G, FortiGate 600E, FortiGate 600F, FortiGate 60F, FortiGate 61F,
FortiGate 80F DSL, FortiGate 80F Gen2, FortiGate 80F-POE, FortiGate 900G, FortiGate 90G Gen2,
FortiGate 90G, FortiGateRugged 50G 5G, FortiGateRugged 60F 3G4G, FortiGateRugged 60F Gen2,
FortiWiFi 30G, FortiWiFi 31G, FortiWiFi 40F 3G4G, FortiWiFi 40F, FortiWiFi 50G 5G, FortiWiFi 50G
DSL, FortiWiFi 50G SFP, FortiWiFi 50G, FortiWiFi 51G, FortiWiFi 60F, FortiWiFi 61F.
Create self-explanatory DLP sensitivity levels to be used when setting sensitivity under config fp-doc-source.
config dlp sensitivity
Description: Create self-explanatory DLP sensitivity levels to be used when setting
sensitivity under config fp-doc-source.
edit <name>
next
end
config dlp sensitivity
Parameter
Description
Type
Size
Default
name
DLP Sensitivity Levels.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
288
Fortinet Inc.

<!-- 来源页 289 -->
config dlp sensor
Configure sensors used by DLP blocking.
config dlp sensor
Description: Configure sensors used by DLP blocking.
edit <name>
set comment {var-string}
config entries
Description: DLP sensor entries.
edit <id>
set count {integer}
set dictionary {string}
set status [enable|disable]
next
end
set eval {string}
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set match-type [match-all|match-any|...]
set uuid {uuid}
next
end
config dlp sensor
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
eval
Expression to evaluate.
string
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
FortiOS 8.0.0 CLI Reference
289
Fortinet Inc.

<!-- 来源页 290 -->
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
match-type
Logical relation between entries (default =
match-any).
option
-match-any
Option
Description
match-all
Match all entries.
match-any
Match any entries.
match-eval
Match an expression evaluation.
name
Name of table containing the sensor.
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
config entries
Parameter
Description
Type
Size
Default
count
Count of dictionary matches to trigger sensor entry
match (Dictionary might not be able to trigger more
than once based on its 'repeat' option, 1 - 255,
default = 1).
integer
Minimum
value: 1
Maximum
value: 255
1
dictionary
Select a DLP dictionary or exact-data-match.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
290
Fortinet Inc.

<!-- 来源页 291 -->
Parameter
Description
Type
Size
Default
id
ID.
integer
Minimum
value: 1
Maximum
value: 32
0
status
Enable/disable this entry.
option
-enable
Option
Description
enable
Enable this entry.
disable
Disable this entry.
config dlp settings
Configure settings for DLP.
config dlp settings
Description: Configure settings for DLP.
set cache-mem-percent {integer}
set chunk-size {integer}
set config-builder-timeout {integer}
set db-mode [stop-adding|remove-modified-then-oldest|...]
config ocr
Description: Configure settings for optical character recognition (OCR) conversion.
set confidence {integer}
set filetype-ignore-list <name1>, <name2>, ...
set max-file-size {integer}
set scan [enable|disable]
end
set size {integer}
set storage-device {string}
end
config dlp settings
Parameter
Description
Type
Size
Default
cache-mem-percent *
Maximum percentage of available memory
allocated to caching DLP fingerprints (1 - 15).
integer
Minimum value:
1 Maximum
value: 15
2
chunk-size *
Maximum fingerprint chunk size. Caution,
changing this setting will flush the entire
database.
integer
Minimum value:
100 Maximum
value: 100000
2800
FortiOS 8.0.0 CLI Reference
291
Fortinet Inc.

<!-- 来源页 292 -->
Parameter
Description
Type
Size
Default
config-builder-timeout
Maximum time allowed for building a single DLP
profile (default 60 seconds).
integer
Minimum value:
10 Maximum
value: 100000
60
db-mode *
Behavior when the maximum size is reached in
the DLP fingerprint database.
option
-stop-adding
Option
Description
stop-adding
Stop adding entries.
remove-modified-then-oldest
Remove modified chunks first, then oldest file entries.
remove-oldest
Remove the oldest files first.
size *
Maximum total size of files within the DLP
fingerprint database (MB).
integer
Minimum value:
16 Maximum
value:
4294967295
16
storage-device *
Storage device name.
string
Maximum
length: 35
* This parameter may not exist in some models.
config ocr
Parameter
Description
Type
Size
Default
confidence
Minimum confidence threshold for the OCR
converted content to be scanned (0 - 100, default
= 80).
integer
Minimum
value: 0
Maximum
value: 100
80
filetype-ignore-list
<name>
List of file types to be exempt from OCR scanning.
File type name.
string
Maximum
length: 39
max-file-size
Maximum file size for an image to be a candidate
for OCR conversion in kilobytes (0 - 1644544, 0 =
unlimited).
integer
Minimum
value: 0
Maximum
value:
1644544 **
0
scan
Enable/disable OCR conversion of images for DLP
content scanning.
option
-enable
FortiOS 8.0.0 CLI Reference
292
Fortinet Inc.

<!-- 来源页 293 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable OCR conversion during DLP scan.
disable
Disable OCR conversion during DLP scan.
** Values may differ between models.
FortiOS 8.0.0 CLI Reference
293
Fortinet Inc.

---


<!-- 来源页 1303 -->
sctp-filter
This section includes syntax for the following commands:
l config sctp-filter profile on page 1303
config sctp-filter profile
Configure SCTP filter profiles.
config sctp-filter profile
Description: Configure SCTP filter profiles.
edit <name>
set comment {var-string}
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
config ppid-filters
Description: PPID filters list.
edit <id>
set action [pass|reset|...]
set comment {var-string}
set ppid {integer}
next
end
set uuid {uuid}
next
end
config sctp-filter profile
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
FortiOS 8.0.0 CLI Reference
1303
Fortinet Inc.

<!-- 来源页 1304 -->
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
name
Profile name.
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
config ppid-filters
Parameter
Description
Type
Size
Default
action
Action taken when PPID is matched.
option
-reset
Option
Description
pass
Pass data chunk.
reset
Reset SCTP session.
replace
Replace data chunk.
FortiOS 8.0.0 CLI Reference
1304
Fortinet Inc.

<!-- 来源页 1305 -->
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
id
ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
ppid
Payload protocol identifier.
integer
Minimum value:
0 Maximum
value:
4294967295
FortiOS 8.0.0 CLI Reference
1305
Fortinet Inc.

---


<!-- 来源页 1306 -->
ssh-filter
This section includes syntax for the following commands:
l config ssh-filter profile on page 1306
config ssh-filter profile
Configure SSH filter profile.
config ssh-filter profile
Description: Configure SSH filter profile.
edit <name>
set block {option1}, {option2}, ...
set default-command-log [enable|disable]
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set log {option1}, {option2}, ...
config shell-commands
Description: SSH command filter.
edit <id>
set action [block|allow]
set alert [enable|disable]
set log [enable|disable]
set pattern {string}
set severity [low|medium|...]
set type [simple|regex]
next
end
set uuid {uuid}
next
end
config ssh-filter profile
Parameter
Description
Type
Size
Default
block
SSH blocking options.
option
-Option
Description
x11
X server forwarding.
FortiOS 8.0.0 CLI Reference
1306
Fortinet Inc.

<!-- 来源页 1307 -->
Parameter
Description
Type
Size
Default
Option
Description
shell
SSH shell.
exec
SSH execution.
port-forward
Port forwarding.
tun-forward
Tunnel forwarding.
sftp
SFTP.
scp
SCP.
unknown
Unknown channel.
default-command-log
Enable/disable logging unmatched shell
commands.
option
-disable
Option
Description
enable
Enable log unmatched shell commands.
disable
Disable log unmatched shell commands.
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
FortiOS 8.0.0 CLI Reference
1307
Fortinet Inc.

<!-- 来源页 1308 -->
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
log
SSH logging options.
option
-Option
Description
x11
X server forwarding.
shell
SSH shell.
exec
SSH execution.
port-forward
Port forwarding.
tun-forward
Tunnel forwarding.
sftp
SFTP.
scp
SCP.
unknown
Unknown channel.
name
SSH filter profile name.
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
config shell-commands
Parameter
Description
Type
Size
Default
action
Action to take for SSH shell command matches.
option
-block
Option
Description
block
Block the SSH shell command.
allow
Allow the SSH shell command.
alert
Enable/disable alert.
option
-disable
FortiOS 8.0.0 CLI Reference
1308
Fortinet Inc.

<!-- 来源页 1309 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable alert.
disable
Disable alert.
id
Id.
integer
Minimum value:
0 Maximum
value:
4294967295
0
log
Enable/disable logging.
option
-disable
Option
Description
enable
Enable logging.
disable
Disable logging.
pattern
SSH shell command pattern.
string
Maximum
length: 128
severity
Log severity.
option
-medium
Option
Description
low
Severity low.
medium
Severity medium.
high
Severity high.
critical
Severity critical.
type
Matching type.
option
-simple
Option
Description
simple
Match single command.
regex
Match command line using regular expression.
FortiOS 8.0.0 CLI Reference
1309
Fortinet Inc.

---


<!-- 来源页 2311 -->
videofilter
This section includes syntax for the following commands:
l config videofilter keyword on page 2311
l config videofilter profile on page 2312
l config videofilter youtube-key on page 2315
config videofilter keyword
Configure video filter keywords.
config videofilter keyword
Description: Configure video filter keywords.
edit <id>
set comment {var-string}
set match [or|and]
set name {string}
config word
Description: List of keywords.
edit <name>
set comment {var-string}
set pattern-type [wildcard|regex]
set status [enable|disable]
next
end
next
end
config videofilter keyword
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
id
ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
match
Keyword matching logic.
option
-or
FortiOS 8.0.0 CLI Reference
2311
Fortinet Inc.

<!-- 来源页 2312 -->
Parameter
Description
Type
Size
Default
Option
Description
or
Match any keyword.
and
Match all keywords.
name
Name.
string
Maximum
length: 35
config word
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
Name.
string
Maximum
length: 79
pattern-type
Pattern type.
option
-wildcard
Option
Description
wildcard
Wildcard pattern.
regex
Perl regular expression.
status
Enable(consider)/disable(ignore) this keyword.
option
-enable
Option
Description
enable
Consider this keyword.
disable
Ignore this keyword.
config videofilter profile
Configure VideoFilter profile.
config videofilter profile
Description: Configure VideoFilter profile.
edit <name>
set comment {var-string}
set dailymotion [enable|disable]
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
config filters
Description: YouTube filter entries.
FortiOS 8.0.0 CLI Reference
2312
Fortinet Inc.

<!-- 来源页 2313 -->
edit <id>
set action [allow|monitor|...]
set category {string}
set channel {string}
set comment {var-string}
set keyword {integer}
set log [enable|disable]
set type [category|channel|...]
next
end
set replacemsg-group {string}
set uuid {uuid}
set vimeo [enable|disable]
set youtube [enable|disable]
next
end
config videofilter profile
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
dailymotion *
Enable/disable Dailymotion video source.
option
-enable
Option
Description
enable
Enable Dailymotion source.
disable
Disable Dailymotion source.
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
FortiOS 8.0.0 CLI Reference
2313
Fortinet Inc.

<!-- 来源页 2314 -->
Parameter
Description
Type
Size
Default
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
name
Name.
string
Maximum
length: 47
replacemsg-group
Replacement message group.
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
vimeo *
Enable/disable Vimeo video source.
option
-enable
Option
Description
enable
Enable Vimeo source.
disable
Disable Vimeo source.
youtube *
Enable/disable YouTube video source.
option
-enable
Option
Description
enable
Enable YouTube source.
disable
Disable YouTube source.
* This parameter may not exist in some models.
config filters
Parameter
Description
Type
Size
Default
action
Video filter action.
option
-monitor
Option
Description
allow
Allow videos to be accessed. The traffic is allowed by videofilter,
bypasses webfilter, and continues with other types of UTM scans.
monitor
Monitor videos. The traffic continues with other types of UTM scans.
block
Block videos. The traffic is blocked immediately.
FortiOS 8.0.0 CLI Reference
2314
Fortinet Inc.

<!-- 来源页 2315 -->
Parameter
Description
Type
Size
Default
category
FortiGuard category ID.
string
Maximum
length: 7
channel
Channel ID.
string
Maximum
length: 255
comment
Comment.
var-string
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
keyword
Video filter keyword ID.
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
Enable logging.
disable
Disable logging.
type
Filter type.
option
-category
Option
Description
category
Filter videos by FortiGuard category.
channel
Filter videos by channel ID.
title
Filter videos by title.
description
Filter videos by description.
config videofilter youtube-key
Configure YouTube API keys.
config videofilter youtube-key
Description: Configure YouTube API keys.
edit <id>
set key {string}
next
end
FortiOS 8.0.0 CLI Reference
2315
Fortinet Inc.

<!-- 来源页 2316 -->
config videofilter youtube-key
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
key
Key.
string
Maximum
length: 47
FortiOS 8.0.0 CLI Reference
2316
Fortinet Inc.

---


<!-- 来源页 2320 -->
voip
This section includes syntax for the following commands:
l config voip profile on page 2320
config voip profile
Configure VoIP profiles.
config voip profile
Description: Configure VoIP profiles.
edit <name>
set comment {var-string}
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set feature-set [ips|voipd]
config msrp
Description: MSRP.
set log-violations [disable|enable]
set max-msg-size {integer}
set max-msg-size-action [pass|block|...]
set status [disable|enable]
end
config sccp
Description: SCCP.
set block-mcast [disable|enable]
set log-call-summary [disable|enable]
set log-violations [disable|enable]
set max-calls {integer}
set status [disable|enable]
set verify-header [disable|enable]
end
config sip
Description: SIP.
set ack-rate {integer}
set ack-rate-track [none|src-ip|...]
set block-ack [disable|enable]
set block-bye [disable|enable]
set block-cancel [disable|enable]
set block-geo-red-options [disable|enable]
set block-info [disable|enable]
set block-invite [disable|enable]
set block-long-lines [disable|enable]
set block-message [disable|enable]
FortiOS 8.0.0 CLI Reference
2320
Fortinet Inc.

<!-- 来源页 2321 -->
set block-notify [disable|enable]
set block-options [disable|enable]
set block-prack [disable|enable]
set block-publish [disable|enable]
set block-refer [disable|enable]
set block-register [disable|enable]
set block-subscribe [disable|enable]
set block-unknown [disable|enable]
set block-update [disable|enable]
set bye-rate {integer}
set bye-rate-track [none|src-ip|...]
set call-id-regex {var-string}
set call-keepalive {integer}
set cancel-rate {integer}
set cancel-rate-track [none|src-ip|...]
set contact-fixup [disable|enable]
set content-type-regex {var-string}
set hnt-restrict-source-ip [disable|enable]
set hosted-nat-traversal [disable|enable]
set info-rate {integer}
set info-rate-track [none|src-ip|...]
set invite-rate {integer}
set invite-rate-track [none|src-ip|...]
set ips-rtp [disable|enable]
set log-call-summary [disable|enable]
set log-violations [disable|enable]
set malformed-header-allow [discard|pass|...]
set malformed-header-call-id [discard|pass|...]
set malformed-header-contact [discard|pass|...]
set malformed-header-content-length [discard|pass|...]
set malformed-header-content-type [discard|pass|...]
set malformed-header-cseq [discard|pass|...]
set malformed-header-expires [discard|pass|...]
set malformed-header-from [discard|pass|...]
set malformed-header-max-forwards [discard|pass|...]
set malformed-header-no-proxy-require [discard|pass|...]
set malformed-header-no-require [discard|pass|...]
set malformed-header-p-asserted-identity [discard|pass|...]
set malformed-header-rack [discard|pass|...]
set malformed-header-record-route [discard|pass|...]
set malformed-header-route [discard|pass|...]
set malformed-header-rseq [discard|pass|...]
set malformed-header-sdp-a [discard|pass|...]
set malformed-header-sdp-b [discard|pass|...]
set malformed-header-sdp-c [discard|pass|...]
set malformed-header-sdp-i [discard|pass|...]
set malformed-header-sdp-k [discard|pass|...]
set malformed-header-sdp-m [discard|pass|...]
set malformed-header-sdp-o [discard|pass|...]
set malformed-header-sdp-r [discard|pass|...]
set malformed-header-sdp-s [discard|pass|...]
set malformed-header-sdp-t [discard|pass|...]
FortiOS 8.0.0 CLI Reference
2321
Fortinet Inc.

<!-- 来源页 2322 -->
set malformed-header-sdp-v [discard|pass|...]
set malformed-header-sdp-z [discard|pass|...]
set malformed-header-to [discard|pass|...]
set malformed-header-via [discard|pass|...]
set malformed-request-line [discard|pass|...]
set max-body-length {integer}
set max-dialogs {integer}
set max-idle-dialogs {integer}
set max-line-length {integer}
set message-rate {integer}
set message-rate-track [none|src-ip|...]
set nat-port-range {user}
set nat-trace [disable|enable]
set no-sdp-fixup [disable|enable]
set notify-rate {integer}
set notify-rate-track [none|src-ip|...]
set open-contact-pinhole [disable|enable]
set open-record-route-pinhole [disable|enable]
set open-register-pinhole [disable|enable]
set open-via-pinhole [disable|enable]
set options-rate {integer}
set options-rate-track [none|src-ip|...]
set prack-rate {integer}
set prack-rate-track [none|src-ip|...]
set preserve-override [disable|enable]
set provisional-invite-expiry-time {integer}
set publish-rate {integer}
set publish-rate-track [none|src-ip|...]
set refer-rate {integer}
set refer-rate-track [none|src-ip|...]
set register-contact-trace [disable|enable]
set register-rate {integer}
set register-rate-track [none|src-ip|...]
set rfc2543-branch [disable|enable]
set rtp [disable|enable]
set ssl-algorithm [high|medium|...]
set ssl-auth-client {string}
set ssl-auth-server {string}
set ssl-client-certificate {string}
set ssl-client-renegotiation [allow|deny|...]
set ssl-max-version [ssl-3.0|tls-1.0|...]
set ssl-min-version [ssl-3.0|tls-1.0|...]
set ssl-mode [off|full]
set ssl-pfs [require|deny|...]
set ssl-send-empty-frags [enable|disable]
set ssl-server-certificate {string}
set status [disable|enable]
set strict-register [disable|enable]
set subscribe-rate {integer}
set subscribe-rate-track [none|src-ip|...]
set unknown-header [discard|pass|...]
set update-rate {integer}
FortiOS 8.0.0 CLI Reference
2322
Fortinet Inc.

<!-- 来源页 2323 -->
set update-rate-track [none|src-ip|...]
end
set uuid {uuid}
next
end
config voip profile
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
feature-set
IPS or voipd (SIP-ALG) inspection feature
set.
option
-voipd
FortiOS 8.0.0 CLI Reference
2323
Fortinet Inc.

<!-- 来源页 2324 -->
Parameter
Description
Type
Size
Default
Option
Description
ips
IPS Engine feature set for ips-voip-filter.
voipd
SIP ALG feature set for voip-profile.
name
Profile name.
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
config msrp
Parameter
Description
Type
Size
Default
log-violations
Enable/disable logging of MSRP violations.
option
-enable
Option
Description
disable
Disable status.
enable
Enable status.
max-msg-size
Maximum allowable MSRP message size (1-65535).
integer
Minimum
value: 0
Maximum
value:
65535
0
max-msg-size-action
Action for violation of max-msg-size.
option
-pass
Option
Description
pass
Pass or allow matching traffic.
block
Block or drop matching traffic.
reset
Reset sessions for matching traffic.
monitor
Pass and log matching traffic.
status
Enable/disable MSRP.
option
-enable
Option
Description
disable
Disable status.
enable
Enable status.
FortiOS 8.0.0 CLI Reference
2324
Fortinet Inc.

<!-- 来源页 2325 -->
config sccp
Parameter
Description
Type
Size
Default
block-mcast
Enable/disable block multicast RTP connections.
option
-disable
Option
Description
disable
Disable status.
enable
Enable status.
log-call-summary
Enable/disable log summary of SCCP calls.
option
-disable
Option
Description
disable
Disable status.
enable
Enable status.
log-violations
Enable/disable logging of SCCP violations.
option
-disable
Option
Description
disable
Disable status.
enable
Enable status.
max-calls
Maximum calls per minute per SCCP client (max
65535).
integer
Minimum
value: 0
Maximum
value:
65535
0
status
Enable/disable SCCP.
option
-enable
Option
Description
disable
Disable status.
enable
Enable status.
verify-header
Enable/disable verify SCCP header content.
option
-disable
Option
Description
disable
Disable status.
enable
Enable status.
FortiOS 8.0.0 CLI Reference
2325
Fortinet Inc.

<!-- 来源页 2326 -->
config sip
Parameter
Description
Type
Size
Default
ack-rate
ACK request rate limit (per second, per policy).
integer
Minimum value:
0 Maximum
value:
4294967295
0
ack-rate-track
Track the packet protocol field.
option
-none
Option
Description
none
None.
src-ip
Source IP.
dest-ip
Destination IP.
block-ack
Enable/disable block ACK requests.
option
-disable
Option
Description
disable
Disable status.
enable
Enable status.
block-bye
Enable/disable block BYE requests.
option
-disable
Option
Description
disable
Disable status.
enable
Enable status.
block-cancel
Enable/disable block CANCEL requests.
option
-disable
Option
Description
disable
Disable status.
enable
Enable status.
block-geo-red-options
Enable/disable block OPTIONS requests, but
OPTIONS requests still notify for redundancy.
option
-disable
Option
Description
disable
Disable status.
enable
Enable status.
block-info
Enable/disable block INFO requests.
option
-disable
FortiOS 8.0.0 CLI Reference
2326
Fortinet Inc.

<!-- 来源页 2327 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable status.
enable
Enable status.
block-invite
Enable/disable block INVITE requests.
option
-disable
Option
Description
disable
Disable status.
enable
Enable status.
block-long-lines
Enable/disable block requests with headers
exceeding max-line-length.
option
-enable
Option
Description
disable
Disable status.
enable
Enable status.
block-message
Enable/disable block MESSAGE requests.
option
-disable
Option
Description
disable
Disable status.
enable
Enable status.
block-notify
Enable/disable block NOTIFY requests.
option
-disable
Option
Description
disable
Disable status.
enable
Enable status.
block-options
Enable/disable block OPTIONS requests and
no OPTIONS as notifying message for
redundancy either.
option
-disable
Option
Description
disable
Disable status.
enable
Enable status.
block-prack
Enable/disable block prack requests.
option
-disable
FortiOS 8.0.0 CLI Reference
2327
Fortinet Inc.

<!-- 来源页 2328 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable status.
enable
Enable status.
block-publish
Enable/disable block PUBLISH requests.
option
-disable
Option
Description
disable
Disable status.
enable
Enable status.
block-refer
Enable/disable block REFER requests.
option
-disable
Option
Description
disable
Disable status.
enable
Enable status.
block-register
Enable/disable block REGISTER requests.
option
-disable
Option
Description
disable
Disable status.
enable
Enable status.
block-subscribe
Enable/disable block SUBSCRIBE requests.
option
-disable
Option
Description
disable
Disable status.
enable
Enable status.
block-unknown
Block unrecognized SIP requests (enabled by
default).
option
-enable
Option
Description
disable
Disable status.
enable
Enable status.
block-update
Enable/disable block UPDATE requests.
option
-disable
FortiOS 8.0.0 CLI Reference
2328
Fortinet Inc.

<!-- 来源页 2329 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable status.
enable
Enable status.
bye-rate
BYE request rate limit (per second, per policy).
integer
Minimum value:
0 Maximum
value:
4294967295
0
bye-rate-track
Track the packet protocol field.
option
-none
Option
Description
none
None.
src-ip
Source IP.
dest-ip
Destination IP.
call-id-regex
Validate PCRE regular expression for Call-Id
header value.
var-string
Maximum
length: 511
call-keepalive
Continue tracking calls with no RTP for this
many minutes.
integer
Minimum value:
0 Maximum
value: 10080
0
cancel-rate
CANCEL request rate limit (per second, per
policy).
integer
Minimum value:
0 Maximum
value:
4294967295
0
cancel-rate-track
Track the packet protocol field.
option
-none
Option
Description
none
None.
src-ip
Source IP.
dest-ip
Destination IP.
contact-fixup
Fixup contact anyway even if contact's IP:port
doesn't match session's IP:port.
option
-enable
Option
Description
disable
Disable status.
enable
Enable status.
FortiOS 8.0.0 CLI Reference
2329
Fortinet Inc.

<!-- 来源页 2330 -->
Parameter
Description
Type
Size
Default
content-type-regex
Validate PCRE regular expression for Content-Type header value.
var-string
Maximum
length: 511
hnt-restrict-source-ip
Enable/disable restrict RTP source IP to be the
same as SIP source IP when HNT is enabled.
option
-disable
Option
Description
disable
Disable status.
enable
Enable status.
hosted-nat-traversal
Hosted NAT Traversal (HNT).
option
-disable
Option
Description
disable
Disable status.
enable
Enable status.
info-rate
INFO request rate limit (per second, per
policy).
integer
Minimum value:
0 Maximum
value:
4294967295
0
info-rate-track
Track the packet protocol field.
option
-none
Option
Description
none
None.
src-ip
Source IP.
dest-ip
Destination IP.
invite-rate
INVITE request rate limit (per second, per
policy).
integer
Minimum value:
0 Maximum
value:
4294967295
0
invite-rate-track
Track the packet protocol field.
option
-none
Option
Description
none
None.
src-ip
Source IP.
dest-ip
Destination IP.
ips-rtp
Enable/disable allow IPS on RTP.
option
-enable
FortiOS 8.0.0 CLI Reference
2330
Fortinet Inc.

<!-- 来源页 2331 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable status.
enable
Enable status.
log-call-summary
Enable/disable logging of SIP call summary.
option
-enable
Option
Description
disable
Disable status.
enable
Enable status.
log-violations
Enable/disable logging of SIP violations.
option
-disable
Option
Description
disable
Disable status.
enable
Enable status.
malformed-header-allow
Action for malformed Allow header.
option
-pass
Option
Description
discard
Discard malformed messages.
pass
Bypass malformed messages.
respond
Respond with error code.
malformed-header-call-id
Action for malformed Call-ID header.
option
-pass
Option
Description
discard
Discard malformed messages.
pass
Bypass malformed messages.
respond
Respond with error code.
malformed-header-contact
Action for malformed Contact header.
option
-pass
Option
Description
discard
Discard malformed messages.
pass
Bypass malformed messages.
FortiOS 8.0.0 CLI Reference
2331
Fortinet Inc.

<!-- 来源页 2332 -->
Parameter
Description
Type
Size
Default
Option
Description
respond
Respond with error code.
malformed-header-content-length
Action for malformed Content-Length header.
option
-pass
Option
Description
discard
Discard malformed messages.
pass
Bypass malformed messages.
respond
Respond with error code.
malformed-header-content-type
Action for malformed Content-Type header.
option
-pass
Option
Description
discard
Discard malformed messages.
pass
Bypass malformed messages.
respond
Respond with error code.
malformed-header-cseq
Action for malformed CSeq header.
option
-pass
Option
Description
discard
Discard malformed messages.
pass
Bypass malformed messages.
respond
Respond with error code.
malformed-header-expires
Action for malformed Expires header.
option
-pass
Option
Description
discard
Discard malformed messages.
pass
Bypass malformed messages.
respond
Respond with error code.
malformed-header-from
Action for malformed From header.
option
-pass
FortiOS 8.0.0 CLI Reference
2332
Fortinet Inc.

<!-- 来源页 2333 -->
Parameter
Description
Type
Size
Default
Option
Description
discard
Discard malformed messages.
pass
Bypass malformed messages.
respond
Respond with error code.
malformed-header-max-forwards
Action for malformed Max-Forwards header.
option
-pass
Option
Description
discard
Discard malformed messages.
pass
Bypass malformed messages.
respond
Respond with error code.
malformed-header-no-proxy-require
Action for malformed SIP messages without
Proxy-Require header.
option
-pass
Option
Description
discard
Discard malformed messages.
pass
Bypass malformed messages.
respond
Respond with error code.
malformed-header-no-require
Action for malformed SIP messages without
Require header.
option
-pass
Option
Description
discard
Discard malformed messages.
pass
Bypass malformed messages.
respond
Respond with error code.
malformed-header-p-asserted-identity
Action for malformed P-Asserted-Identity
header.
option
-pass
Option
Description
discard
Discard malformed messages.
FortiOS 8.0.0 CLI Reference
2333
Fortinet Inc.

<!-- 来源页 2334 -->
Parameter
Description
Type
Size
Default
Option
Description
pass
Bypass malformed messages.
respond
Respond with error code.
malformed-header-rack
Action for malformed RAck header.
option
-pass
Option
Description
discard
Discard malformed messages.
pass
Bypass malformed messages.
respond
Respond with error code.
malformed-header-record-route
Action for malformed Record-Route header.
option
-pass
Option
Description
discard
Discard malformed messages.
pass
Bypass malformed messages.
respond
Respond with error code.
malformed-header-route
Action for malformed Route header.
option
-pass
Option
Description
discard
Discard malformed messages.
pass
Bypass malformed messages.
respond
Respond with error code.
malformed-header-rseq
Action for malformed RSeq header.
option
-pass
Option
Description
discard
Discard malformed messages.
pass
Bypass malformed messages.
respond
Respond with error code.
malformed-header-sdp-a
Action for malformed SDP a line.
option
-pass
FortiOS 8.0.0 CLI Reference
2334
Fortinet Inc.

<!-- 来源页 2335 -->
Parameter
Description
Type
Size
Default
Option
Description
discard
Discard malformed messages.
pass
Bypass malformed messages.
respond
Respond with error code.
malformed-header-sdp-b
Action for malformed SDP b line.
option
-pass
Option
Description
discard
Discard malformed messages.
pass
Bypass malformed messages.
respond
Respond with error code.
malformed-header-sdp-c
Action for malformed SDP c line.
option
-pass
Option
Description
discard
Discard malformed messages.
pass
Bypass malformed messages.
respond
Respond with error code.
malformed-header-sdp-i
Action for malformed SDP i line.
option
-pass
Option
Description
discard
Discard malformed messages.
pass
Bypass malformed messages.
respond
Respond with error code.
malformed-header-sdp-k
Action for malformed SDP k line.
option
-pass
Option
Description
discard
Discard malformed messages.
pass
Bypass malformed messages.
respond
Respond with error code.
malformed-header-sdp-m
Action for malformed SDP m line.
option
-pass
FortiOS 8.0.0 CLI Reference
2335
Fortinet Inc.

<!-- 来源页 2336 -->
Parameter
Description
Type
Size
Default
Option
Description
discard
Discard malformed messages.
pass
Bypass malformed messages.
respond
Respond with error code.
malformed-header-sdp-o
Action for malformed SDP o line.
option
-pass
Option
Description
discard
Discard malformed messages.
pass
Bypass malformed messages.
respond
Respond with error code.
malformed-header-sdp-r
Action for malformed SDP r line.
option
-pass
Option
Description
discard
Discard malformed messages.
pass
Bypass malformed messages.
respond
Respond with error code.
malformed-header-sdp-s
Action for malformed SDP s line.
option
-pass
Option
Description
discard
Discard malformed messages.
pass
Bypass malformed messages.
respond
Respond with error code.
malformed-header-sdp-t
Action for malformed SDP t line.
option
-pass
Option
Description
discard
Discard malformed messages.
pass
Bypass malformed messages.
respond
Respond with error code.
malformed-header-sdp-v
Action for malformed SDP v line.
option
-pass
FortiOS 8.0.0 CLI Reference
2336
Fortinet Inc.

<!-- 来源页 2337 -->
Parameter
Description
Type
Size
Default
Option
Description
discard
Discard malformed messages.
pass
Bypass malformed messages.
respond
Respond with error code.
malformed-header-sdp-z
Action for malformed SDP z line.
option
-pass
Option
Description
discard
Discard malformed messages.
pass
Bypass malformed messages.
respond
Respond with error code.
malformed-header-to
Action for malformed To header.
option
-pass
Option
Description
discard
Discard malformed messages.
pass
Bypass malformed messages.
respond
Respond with error code.
malformed-header-via
Action for malformed VIA header.
option
-pass
Option
Description
discard
Discard malformed messages.
pass
Bypass malformed messages.
respond
Respond with error code.
malformed-request-line
Action for malformed request line.
option
-pass
Option
Description
discard
Discard malformed messages.
pass
Bypass malformed messages.
respond
Respond with error code.
FortiOS 8.0.0 CLI Reference
2337
Fortinet Inc.

<!-- 来源页 2338 -->
Parameter
Description
Type
Size
Default
max-body-length
Maximum SIP message body length (0
meaning no limit).
integer
Minimum value:
0 Maximum
value:
4294967295
0
max-dialogs
Maximum number of concurrent calls/dialogs
(per policy).
integer
Minimum value:
0 Maximum
value:
4294967295
0
max-idle-dialogs
Maximum number established but idle dialogs
to retain (per policy).
integer
Minimum value:
0 Maximum
value:
4294967295
0
max-line-length
Maximum SIP header line length (78-4096).
integer
Minimum value:
78 Maximum
value: 4096
998
message-rate
MESSAGE request rate limit (per second, per
policy).
integer
Minimum value:
0 Maximum
value:
4294967295
0
message-rate-track
Track the packet protocol field.
option
-none
Option
Description
none
None.
src-ip
Source IP.
dest-ip
Destination IP.
nat-port-range
RTP NAT port range.
user
Not Specified
5117-65533
nat-trace
Enable/disable preservation of original IP in
SDP i line.
option
-enable
Option
Description
disable
Disable status.
enable
Enable status.
no-sdp-fixup
Enable/disable no SDP fix-up.
option
-disable
Option
Description
disable
Disable status.
FortiOS 8.0.0 CLI Reference
2338
Fortinet Inc.

<!-- 来源页 2339 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable status.
notify-rate
NOTIFY request rate limit (per second, per
policy).
integer
Minimum value:
0 Maximum
value:
4294967295
0
notify-rate-track
Track the packet protocol field.
option
-none
Option
Description
none
None.
src-ip
Source IP.
dest-ip
Destination IP.
open-contact-pinhole
Enable/disable open pinhole for non-REGISTER
Contact port.
option
-enable
Option
Description
disable
Disable status.
enable
Enable status.
open-record-route-pinhole
Enable/disable open pinhole for Record-Route
port.
option
-enable
Option
Description
disable
Disable status.
enable
Enable status.
open-register-pinhole
Enable/disable open pinhole for REGISTER
Contact port.
option
-enable
Option
Description
disable
Disable status.
enable
Enable status.
open-via-pinhole
Enable/disable open pinhole for Via port.
option
-disable
FortiOS 8.0.0 CLI Reference
2339
Fortinet Inc.

<!-- 来源页 2340 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable status.
enable
Enable status.
options-rate
OPTIONS request rate limit (per second, per
policy).
integer
Minimum value:
0 Maximum
value:
4294967295
0
options-rate-track
Track the packet protocol field.
option
-none
Option
Description
none
None.
src-ip
Source IP.
dest-ip
Destination IP.
prack-rate
PRACK request rate limit (per second, per
policy).
integer
Minimum value:
0 Maximum
value:
4294967295
0
prack-rate-track
Track the packet protocol field.
option
-none
Option
Description
none
None.
src-ip
Source IP.
dest-ip
Destination IP.
preserve-override
Override i line to preserve original IPs (default:
append).
option
-disable
Option
Description
disable
Disable status.
enable
Enable status.
provisional-invite-expiry-time
Expiry time (10-3600, in seconds) for
provisional INVITE.
integer
Minimum value:
10 Maximum
value: 3600
210
FortiOS 8.0.0 CLI Reference
2340
Fortinet Inc.

<!-- 来源页 2341 -->
Parameter
Description
Type
Size
Default
publish-rate
PUBLISH request rate limit (per second, per
policy).
integer
Minimum value:
0 Maximum
value:
4294967295
0
publish-rate-track
Track the packet protocol field.
option
-none
Option
Description
none
None.
src-ip
Source IP.
dest-ip
Destination IP.
refer-rate
REFER request rate limit (per second, per
policy).
integer
Minimum value:
0 Maximum
value:
4294967295
0
refer-rate-track
Track the packet protocol field.
option
-none
Option
Description
none
None.
src-ip
Source IP.
dest-ip
Destination IP.
register-contact-trace
Enable/disable trace original IP/port within the
contact header of REGISTER requests.
option
-disable
Option
Description
disable
Disable status.
enable
Enable status.
register-rate
REGISTER request rate limit (per second, per
policy).
integer
Minimum value:
0 Maximum
value:
4294967295
0
register-rate-track
Track the packet protocol field.
option
-none
Option
Description
none
None.
FortiOS 8.0.0 CLI Reference
2341
Fortinet Inc.

<!-- 来源页 2342 -->
Parameter
Description
Type
Size
Default
Option
Description
src-ip
Source IP.
dest-ip
Destination IP.
rfc2543-branch
Enable/disable support via branch compliant
with RFC 2543.
option
-disable
Option
Description
disable
Disable status.
enable
Enable status.
rtp
Enable/disable create pinholes for RTP traffic
to traverse firewall.
option
-enable
Option
Description
disable
Disable status.
enable
Enable status.
ssl-algorithm
Relative strength of encryption algorithms
accepted in negotiation.
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
ssl-auth-client
Require a client certificate and authenticate it
with the peer/peergrp.
string
Maximum
length: 35
ssl-auth-server
Authenticate the server's certificate with the
peer/peergrp.
string
Maximum
length: 35
ssl-client-certificate
Name of Certificate to offer to server if
requested.
string
Maximum
length: 35
ssl-client-renegotiation
Allow/block client renegotiation by server.
option
-allow
Option
Description
allow
Allow a SSL client to renegotiate.
deny
Abort any SSL connection that attempts to renegotiate.
FortiOS 8.0.0 CLI Reference
2342
Fortinet Inc.

<!-- 来源页 2343 -->
Parameter
Description
Type
Size
Default
Option
Description
secure
Reject any SSL connection that does not offer a RFC 5746 Secure
Renegotiation Indication.
ssl-max-version
Highest SSL/TLS version to negotiate.
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
Lowest SSL/TLS version to negotiate.
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
ssl-mode
SSL/TLS mode for encryption & decryption of
traffic.
option
-off
Option
Description
off
No SSL.
full
Client to FortiGate and FortiGate to Server SSL.
ssl-pfs
SSL Perfect Forward Secrecy.
option
-allow
Option
Description
require
PFS mandatory.
deny
PFS rejected.
allow
PFS allowed.
FortiOS 8.0.0 CLI Reference
2343
Fortinet Inc.

<!-- 来源页 2344 -->
Parameter
Description
Type
Size
Default
ssl-send-empty-frags
Send empty fragments to avoid attack on CBC
IV (SSL 3.0 & TLS 1.0 only).
option
-enable
Option
Description
enable
Send empty fragments.
disable
Do not send empty fragments.
ssl-server-certificate
Name of Certificate return to the client in every
SSL connection.
string
Maximum
length: 35
status
Enable/disable SIP.
option
-enable
Option
Description
disable
Disable status.
enable
Enable status.
strict-register
Enable/disable only allow the registrar to
connect.
option
-enable
Option
Description
disable
Disable status.
enable
Enable status.
subscribe-rate
SUBSCRIBE request rate limit (per second, per
policy).
integer
Minimum value:
0 Maximum
value:
4294967295
0
subscribe-rate-track
Track the packet protocol field.
option
-none
Option
Description
none
None.
src-ip
Source IP.
dest-ip
Destination IP.
unknown-header
Action for unknown SIP header.
option
-pass
Option
Description
discard
Discard malformed messages.
FortiOS 8.0.0 CLI Reference
2344
Fortinet Inc.

<!-- 来源页 2345 -->
Parameter
Description
Type
Size
Default
Option
Description
pass
Bypass malformed messages.
respond
Respond with error code.
update-rate
UPDATE request rate limit (per second, per
policy).
integer
Minimum value:
0 Maximum
value:
4294967295
0
update-rate-track
Track the packet protocol field.
option
-none
Option
Description
none
None.
src-ip
Source IP.
dest-ip
Destination IP.
FortiOS 8.0.0 CLI Reference
2345
Fortinet Inc.
