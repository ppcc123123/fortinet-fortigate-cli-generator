# 威胁防护：防病毒 / IPS / 虚拟补丁

> 来源: FortiOS-8.0.0-CLI_Reference.pdf
> 覆盖命令/章节: antivirus, ips, virtual-patch
> 本文件由 extract_pdf.py 从官方 PDF 自动提取，请勿手动编辑；
> 如需修正请修改 map.json 后重跑脚本。

---


<!-- 来源页 142 -->
antivirus
This section includes syntax for the following commands:
l config antivirus exempt-list on page 142
l config antivirus profile on page 143
l config antivirus quarantine on page 181
l config antivirus settings on page 185
config antivirus exempt-list
Configure a list of hashes to be exempt from AV scanning.
config antivirus exempt-list
Description: Configure a list of hashes to be exempt from AV scanning.
edit <name>
set comment {var-string}
set hash {string}
set hash-type [md5|sha1|...]
set status [disable|enable]
next
end
config antivirus exempt-list
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
hash
Hash value to be matched.
string
Maximum
length: 64
hash-type
Hash type.
option
-sha1
Option
Description
md5
MD5 hash value (32 characters in length).
sha1
SHA1 hash value (40 characters in length).
sha256
SHA256 hash value (64 characters in length).
name
Table entry name.
string
Maximum
length: 35
FortiOS 8.0.0 CLI Reference
142
Fortinet Inc.

<!-- 来源页 143 -->
Parameter
Description
Type
Size
Default
status
Enable/disable table entry.
option
-enable
Option
Description
disable
Disable AV exempt-list table entry.
enable
Enable AV exempt-list table entry.
config antivirus profile
Configure AntiVirus profiles.
config antivirus profile
Description: Configure AntiVirus profiles.
edit <name>
set analytics-accept-filetype {integer}
set analytics-db [disable|enable]
set analytics-ignore-filetype {integer}
set analytics-ignore-mpip {string}
set av-virus-log [enable|disable]
config cifs
Description: Configure CIFS AntiVirus options.
set archive-block {option1}, {option2}, ...
set archive-log {option1}, {option2}, ...
set av-scan [disable|block|...]
set emulator [enable|disable]
set external-blocklist [disable|block|...]
set fortindr [disable|block|...]
set fortisandbox [disable|block|...]
set malware-stream [disable|block|...]
set outbreak-prevention [disable|block|...]
set quarantine [disable|enable]
end
set comment {var-string}
config content-disarm
Description: AV Content Disarm and Reconstruction settings.
set analytics-suspicious [disable|enable]
set cover-page [disable|enable]
set detect-only [disable|enable]
set error-action [block|log-only|...]
set office-action [disable|enable]
set office-dde [disable|enable]
set office-embed [disable|enable]
set office-hylink [disable|enable]
set office-linked [disable|enable]
set office-macro [disable|enable]
set original-file-destination [fortisandbox|quarantine|...]
set pdf-act-form [disable|enable]
set pdf-act-gotor [disable|enable]
FortiOS 8.0.0 CLI Reference
143
Fortinet Inc.

<!-- 来源页 144 -->
set pdf-act-java [disable|enable]
set pdf-act-launch [disable|enable]
set pdf-act-movie [disable|enable]
set pdf-act-sound [disable|enable]
set pdf-embedfile [disable|enable]
set pdf-hyperlink [disable|enable]
set pdf-javacode [disable|enable]
end
set ems-threat-feed [disable|enable]
set extended-log [enable|disable]
set external-blocklist <name1>, <name2>, ...
set external-blocklist-enable-all [disable|enable]
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set feature-set [flow|proxy]
set fortindr-error-action [log-only|block|...]
set fortindr-timeout-action [log-only|block|...]
set fortisandbox-destination [auto|sandbox|...]
set fortisandbox-error-action [log-only|block|...]
set fortisandbox-max-upload {integer}
set fortisandbox-mode [inline|analytics-suspicious|...]
set fortisandbox-scan-timeout {integer}
set fortisandbox-timeout-action [log-only|block|...]
config ftp
Description: Configure FTP AntiVirus options.
set archive-block {option1}, {option2}, ...
set archive-log {option1}, {option2}, ...
set av-scan [disable|block|...]
set emulator [enable|disable]
set external-blocklist [disable|block|...]
set fortindr [disable|block|...]
set fortisandbox [disable|block|...]
set malware-stream [disable|block|...]
set outbreak-prevention [disable|block|...]
set quarantine [disable|enable]
end
config http
Description: Configure HTTP AntiVirus options.
set archive-block {option1}, {option2}, ...
set archive-log {option1}, {option2}, ...
set av-scan [disable|block|...]
set content-disarm [disable|enable]
set emulator [enable|disable]
set external-blocklist [disable|block|...]
set fortindr [disable|block|...]
set fortisandbox [disable|block|...]
set malware-stream [disable|block|...]
set outbreak-prevention [disable|block|...]
set quarantine [disable|enable]
end
config imap
FortiOS 8.0.0 CLI Reference
144
Fortinet Inc.

<!-- 来源页 145 -->
Description: Configure IMAP AntiVirus options.
set archive-block {option1}, {option2}, ...
set archive-log {option1}, {option2}, ...
set av-scan [disable|block|...]
set content-disarm [disable|enable]
set emulator [enable|disable]
set executables [default|virus]
set external-blocklist [disable|block|...]
set fortindr [disable|block|...]
set fortisandbox [disable|block|...]
set malware-stream [disable|block|...]
set outbreak-prevention [disable|block|...]
set quarantine [disable|enable]
end
config mapi
Description: Configure MAPI AntiVirus options.
set archive-block {option1}, {option2}, ...
set archive-log {option1}, {option2}, ...
set av-scan [disable|block|...]
set emulator [enable|disable]
set executables [default|virus]
set external-blocklist [disable|block|...]
set fortindr [disable|block|...]
set fortisandbox [disable|block|...]
set malware-stream [disable|block|...]
set outbreak-prevention [disable|block|...]
set quarantine [disable|enable]
end
set mobile-malware-db [disable|enable]
config nac-quar
Description: Configure AntiVirus quarantine settings.
set expiry {user}
set infected [none|quar-src-ip]
set log [enable|disable]
end
config nntp
Description: Configure NNTP AntiVirus options.
set archive-block {option1}, {option2}, ...
set archive-log {option1}, {option2}, ...
set av-scan [disable|block|...]
set emulator [enable|disable]
set external-blocklist [disable|block|...]
set fortindr [disable|block|...]
set fortisandbox [disable|block|...]
set malware-stream [disable|block|...]
set outbreak-prevention [disable|block|...]
set quarantine [disable|enable]
end
set outbreak-prevention-archive-scan [disable|enable]
set outbreak-prevention-error-action [log-only|block|...]
set outbreak-prevention-timeout-action [log-only|block|...]
config pop3
FortiOS 8.0.0 CLI Reference
145
Fortinet Inc.

<!-- 来源页 146 -->
Description: Configure POP3 AntiVirus options.
set archive-block {option1}, {option2}, ...
set archive-log {option1}, {option2}, ...
set av-scan [disable|block|...]
set content-disarm [disable|enable]
set emulator [enable|disable]
set executables [default|virus]
set external-blocklist [disable|block|...]
set fortindr [disable|block|...]
set fortisandbox [disable|block|...]
set malware-stream [disable|block|...]
set outbreak-prevention [disable|block|...]
set quarantine [disable|enable]
end
set replacemsg-group {string}
set scan-mode [default|legacy]
config smtp
Description: Configure SMTP AntiVirus options.
set archive-block {option1}, {option2}, ...
set archive-log {option1}, {option2}, ...
set av-scan [disable|block|...]
set content-disarm [disable|enable]
set emulator [enable|disable]
set executables [default|virus]
set external-blocklist [disable|block|...]
set fortindr [disable|block|...]
set fortisandbox [disable|block|...]
set malware-stream [disable|block|...]
set outbreak-prevention [disable|block|...]
set quarantine [disable|enable]
end
config ssh
Description: Configure SFTP and SCP AntiVirus options.
set archive-block {option1}, {option2}, ...
set archive-log {option1}, {option2}, ...
set av-scan [disable|block|...]
set emulator [enable|disable]
set external-blocklist [disable|block|...]
set fortindr [disable|block|...]
set fortisandbox [disable|block|...]
set malware-stream [disable|block|...]
set outbreak-prevention [disable|block|...]
set quarantine [disable|enable]
end
set uuid {uuid}
config websocket
Description: Configure WEBSOCKET AntiVirus options.
set archive-block {option1}, {option2}, ...
set archive-log {option1}, {option2}, ...
set av-scan [disable|block|...]
set emulator [enable|disable]
set external-blocklist [disable|block|...]
FortiOS 8.0.0 CLI Reference
146
Fortinet Inc.

<!-- 来源页 147 -->
set fortindr [disable|block|...]
set fortisandbox [disable|block|...]
set malware-stream [disable|block|...]
set outbreak-prevention [disable|block|...]
set quarantine [disable|enable]
end
next
end
config antivirus profile
Parameter
Description
Type
Size
Default
analytics-accept-filetype
Only submit files matching this DLP
file-pattern to FortiSandbox (post-transfer scan only).
integer
Minimum value:
0 Maximum
value:
4294967295
0
analytics-db
Enable/disable using the FortiSandbox
signature database to supplement the
AV signature databases.
option
-disable
Option
Description
disable
Use only the standard AV signature databases.
enable
Also use the FortiSandbox signature database.
analytics-ignore-filetype
Do not submit files matching this DLP
file-pattern to FortiSandbox (post-transfer scan only).
integer
Minimum value:
0 Maximum
value:
4294967295
0
analytics-ignore-mpip *
Do not submit files matching this DLP
label to FortiSandbox (post-transfer
scan only).
string
Maximum
length: 35
av-virus-log
Enable/disable AntiVirus logging.
option
-enable
Option
Description
enable
Enable setting.
disable
Disable setting.
comment
Comment.
var-string
Maximum
length: 255
ems-threat-feed
Enable/disable use of EMS threat feed
when performing AntiVirus scan.
Analyzes files including the content of
archives.
option
-disable
FortiOS 8.0.0 CLI Reference
147
Fortinet Inc.

<!-- 来源页 148 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable use of EMS threat feed when performing AntiVirus scan.
enable
Enable use of EMS threat feed when performing AntiVirus scan.
extended-log
Enable/disable extended logging for
antivirus.
option
-disable
Option
Description
enable
Enable setting.
disable
Disable setting.
external-blocklist <name>
One or more external malware block
lists.
External blocklist.
string
Maximum
length: 79
external-blocklist-enable-all
Enable/disable all external blocklists.
option
-disable
Option
Description
disable
Use configured external blocklists.
enable
Enable all external blocklists.
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
FortiOS 8.0.0 CLI Reference
148
Fortinet Inc.

<!-- 来源页 149 -->
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
fortindr-error-action *
Action to take if FortiNDR encounters
an error.
option
-log-only
Option
Description
log-only
Log FortiNDR error, but allow the file.
block
Block the file on FortiNDR error.
ignore
Do nothing on FortiNDR error.
fortindr-timeout-action
*
Action to take if FortiNDR encounters a
scan timeout.
option
-log-only
Option
Description
log-only
Log FortiNDR scan timeout, but allow the file.
block
Block the file on FortiNDR scan timeout.
ignore
Do nothing on FortiNDR scan timeout.
fortisandbox-destination *
FortiSandbox destination options.
option
-auto
Option
Description
auto
Auto select FortiSandbox device. If both on-premise FortiSandbox and
FortiSandbox Cloud are enabled, the default device is selected.
sandbox
Use on-premise FortiSandbox.
sandbox-cloud
Use FortiSandbox Cloud.
FortiOS 8.0.0 CLI Reference
149
Fortinet Inc.

<!-- 来源页 150 -->
Parameter
Description
Type
Size
Default
fortisandbox-error-action *
Action to take if FortiSandbox inline
scan encounters an error.
option
-log-only
Option
Description
log-only
Log FortiSandbox inline scan error, but allow the file.
block
Block the file on FortiSandbox inline scan error.
ignore
Do nothing on FortiSandbox inline scan error.
fortisandbox-max-upload
Maximum size of files that can be
uploaded to FortiSandbox in Mbytes.
integer
Minimum value:
1 Maximum
value: 1606 **
10
fortisandbox-mode
FortiSandbox scan modes.
option
-analytics-everything
Option
Description
inline
FortiSandbox inline scan.
analytics-suspicious
FortiSandbox post-transfer scan: submit supported files if heuristics
or other methods determine they are suspicious.
analytics-everything
FortiSandbox post-transfer scan: submit supported files for
inspection.
fortisandbox-scan-timeout *
FortiSandbox inline scan timeout in
seconds (30 - 180, default = 60).
integer
Minimum value:
30 Maximum
value: 180
60
fortisandbox-timeout-action
*
Action to take if FortiSandbox inline
scan encounters a scan timeout.
option
-log-only
Option
Description
log-only
Log FortiSandbox inline scan timeout, but allow the file.
block
Block the file on FortiSandbox inline scan timeout.
ignore
Do nothing on FortiSandbox inline scan timeout.
mobile-malware-db
Enable/disable using the mobile
malware signature database.
option
-enable
Option
Description
disable
Do not use the mobile malware signature database.
enable
Also use the mobile malware signature database.
FortiOS 8.0.0 CLI Reference
150
Fortinet Inc.

<!-- 来源页 151 -->
Parameter
Description
Type
Size
Default
name
Profile name.
string
Maximum
length: 47
outbreak-prevention-archive-scan
Enable/disable outbreak-prevention
archive scanning.
option
-enable
Option
Description
disable
Analyze files as sent, not the content of archives.
enable
Analyze files including the content of archives.
outbreak-prevention-error-action *
Action to take if outbreak-prevention
encounters an error
option
-log-only
Option
Description
log-only
Log outbreak-prevention errors, but allow the file.
block
Block the file on outbreak-prevention errors.
ignore
Do nothing on outbreak-prevention errors.
outbreak-prevention-timeout-action
*
Action to take if outbreak-prevention
encounters a request timeout
option
-log-only
Option
Description
log-only
Log outbreak-prevention request timeouts, but allow the file.
block
Block the file on outbreak-prevention request timeouts.
ignore
Do nothing on outbreak-prevention request timeouts.
replacemsg-group
Replacement message group
customized for this profile.
string
Maximum
length: 35
scan-mode
Configure scan mode (default or
legacy).
option
-default
Option
Description
default
On the fly decompression and scanning of certain archive files.
legacy
Scan archive files only after the entire file is received.
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be
manually reset).
uuid
Not Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
FortiOS 8.0.0 CLI Reference
151
Fortinet Inc.

<!-- 来源页 152 -->
** Values may differ between models.
config cifs
Parameter
Description
Type
Size
Default
archive-block
Select the archive types to block.
option
-Option
Description
encrypted
Block encrypted archives.
corrupted
Block corrupted archives.
partiallycorrupted
Block partially corrupted archives.
multipart
Block multipart archives.
nested
Block nested archives that exceed uncompressed nest limit.
mailbomb
Block mail bomb archives.
timeout
Block scan timeout.
unhandled
Block archives that FortiOS cannot open.
archive-log
Select the archive types to log.
option
-Option
Description
encrypted
Log encrypted archives.
corrupted
Log corrupted archives.
partiallycorrupted
Log partially corrupted archives.
multipart
Log multipart archives.
nested
Log nested archives that exceed uncompressed nest limit.
mailbomb
Log mail bomb archives.
timeout
Log scan timeout.
unhandled
Log archives that FortiOS cannot open.
av-scan
Enable/disable AntiVirus scan service.
option
-disable
Option
Description
disable
Disable.
block
Block the virus infected files.
monitor
Log the virus infected files.
emulator
Enable/disable the virus emulator.
option
-enable
FortiOS 8.0.0 CLI Reference
152
Fortinet Inc.

<!-- 来源页 153 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable the virus emulator.
disable
Disable the virus emulator.
external-blocklist
Enable/disable external-blocklist. Analyzes files
including the content of archives.
option
-disable
Option
Description
disable
Disable.
block
Block the matched files.
monitor
Log the matched files.
fortindr *
Enable/disable scanning of files by FortiNDR.
option
-disable
Option
Description
disable
Disable.
block
Block the FortiNDR detected infections.
monitor
Log the FortiNDR detected infections.
fortisandbox
Enable/disable scanning of files by FortiSandbox.
option
-disable
Option
Description
disable
Disable.
block
Block the FortiSandbox detected infections.
monitor
Log the FortiSandbox detected infections.
malware-stream
Enable/disable 0-day malware-stream scanning.
Analyzes files including the content of archives.
option
-disable
Option
Description
disable
Disable.
block
Block the matched files.
monitor
Log the matched files.
outbreak-prevention
Enable/disable virus outbreak prevention service.
option
-disable
FortiOS 8.0.0 CLI Reference
153
Fortinet Inc.

<!-- 来源页 154 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable.
block
Block the matched files.
monitor
Log the matched files.
quarantine
Enable/disable quarantine for infected files.
option
-disable
Option
Description
disable
Disable quarantine for infected files.
enable
Enable quarantine for infected files.
* This parameter may not exist in some models.
config content-disarm
Parameter
Description
Type
Size
Default
analytics-suspicious
Enable/disable using CDR as a secondary method
for determining suspicous files for analytics.
option
-enable **
Option
Description
disable
enable
cover-page
Enable/disable inserting a cover page into the
disarmed document.
option
-enable
Option
Description
disable
Disable this Content Disarm and Reconstruction feature.
enable
Enable this Content Disarm and Reconstruction feature.
detect-only
Enable/disable only detect disarmable files, do not
alter content.
option
-disable
Option
Description
disable
Disable this Content Disarm and Reconstruction feature.
enable
Enable this Content Disarm and Reconstruction feature.
error-action
Action to be taken if CDR engine encounters an
unrecoverable error.
option
-log-only
FortiOS 8.0.0 CLI Reference
154
Fortinet Inc.

<!-- 来源页 155 -->
Parameter
Description
Type
Size
Default
Option
Description
block
Block file on CDR error.
log-only
Log CDR error, but allow file.
ignore
Do nothing on CDR error.
office-action
Enable/disable stripping of PowerPoint action
events in Microsoft Office documents.
option
-enable
Option
Description
disable
Disable this Content Disarm and Reconstruction feature.
enable
Enable this Content Disarm and Reconstruction feature.
office-dde
Enable/disable stripping of Dynamic Data Exchange
events in Microsoft Office documents.
option
-enable **
Option
Description
disable
Disable this Content Disarm and Reconstruction feature.
enable
Enable this Content Disarm and Reconstruction feature.
office-embed
Enable/disable stripping of embedded objects in
Microsoft Office documents.
option
-enable
Option
Description
disable
Disable this Content Disarm and Reconstruction feature.
enable
Enable this Content Disarm and Reconstruction feature.
office-hylink
Enable/disable stripping of hyperlinks in Microsoft
Office documents.
option
-enable
Option
Description
disable
Disable this Content Disarm and Reconstruction feature.
enable
Enable this Content Disarm and Reconstruction feature.
office-linked
Enable/disable stripping of linked objects in
Microsoft Office documents.
option
-enable **
Option
Description
disable
Disable this Content Disarm and Reconstruction feature.
enable
Enable this Content Disarm and Reconstruction feature.
FortiOS 8.0.0 CLI Reference
155
Fortinet Inc.

<!-- 来源页 156 -->
Parameter
Description
Type
Size
Default
office-macro
Enable/disable stripping of macros in Microsoft
Office documents.
option
-enable
Option
Description
disable
Disable this Content Disarm and Reconstruction feature.
enable
Enable this Content Disarm and Reconstruction feature.
original-file-destination
Destination to send original file if active content is
removed.
option
-discard
Option
Description
fortisandbox
Send original file to configured FortiSandbox.
quarantine
Send original file to quarantine.
discard
Original file will be discarded after content disarm.
pdf-act-form
Enable/disable stripping of PDF document actions
that submit data to other targets.
option
-enable **
Option
Description
disable
Disable this Content Disarm and Reconstruction feature.
enable
Enable this Content Disarm and Reconstruction feature.
pdf-act-gotor
Enable/disable stripping of PDF document actions
that access other PDF documents.
option
-enable
Option
Description
disable
Disable this Content Disarm and Reconstruction feature.
enable
Enable this Content Disarm and Reconstruction feature.
pdf-act-java
Enable/disable stripping of PDF document actions
that execute JavaScript code.
option
-enable **
Option
Description
disable
Disable this Content Disarm and Reconstruction feature.
enable
Enable this Content Disarm and Reconstruction feature.
pdf-act-launch
Enable/disable stripping of PDF document actions
that launch other applications.
option
-enable **
FortiOS 8.0.0 CLI Reference
156
Fortinet Inc.

<!-- 来源页 157 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable this Content Disarm and Reconstruction feature.
enable
Enable this Content Disarm and Reconstruction feature.
pdf-act-movie
Enable/disable stripping of PDF document actions
that play a movie.
option
-enable **
Option
Description
disable
Disable this Content Disarm and Reconstruction feature.
enable
Enable this Content Disarm and Reconstruction feature.
pdf-act-sound
Enable/disable stripping of PDF document actions
that play a sound.
option
-enable **
Option
Description
disable
Disable this Content Disarm and Reconstruction feature.
enable
Enable this Content Disarm and Reconstruction feature.
pdf-embedfile
Enable/disable stripping of embedded files in PDF
documents.
option
-enable
Option
Description
disable
Disable this Content Disarm and Reconstruction feature.
enable
Enable this Content Disarm and Reconstruction feature.
pdf-hyperlink
Enable/disable stripping of hyperlinks from PDF
documents.
option
-enable **
Option
Description
disable
Disable this Content Disarm and Reconstruction feature.
enable
Enable this Content Disarm and Reconstruction feature.
pdf-javacode
Enable/disable stripping of JavaScript code in PDF
documents.
option
-enable **
Option
Description
disable
Disable this Content Disarm and Reconstruction feature.
enable
Enable this Content Disarm and Reconstruction feature.
** Values may differ between models.
FortiOS 8.0.0 CLI Reference
157
Fortinet Inc.

<!-- 来源页 158 -->
config ftp
Parameter
Description
Type
Size
Default
archive-block
Select the archive types to block.
option
-Option
Description
encrypted
Block encrypted archives.
corrupted
Block corrupted archives.
partiallycorrupted
Block partially corrupted archives.
multipart
Block multipart archives.
nested
Block nested archives that exceed uncompressed nest limit.
mailbomb
Block mail bomb archives.
timeout
Block scan timeout.
unhandled
Block archives that FortiOS cannot open.
archive-log
Select the archive types to log.
option
-Option
Description
encrypted
Log encrypted archives.
corrupted
Log corrupted archives.
partiallycorrupted
Log partially corrupted archives.
multipart
Log multipart archives.
nested
Log nested archives that exceed uncompressed nest limit.
mailbomb
Log mail bomb archives.
timeout
Log scan timeout.
unhandled
Log archives that FortiOS cannot open.
av-scan
Enable/disable AntiVirus scan service.
option
-disable
Option
Description
disable
Disable.
block
Block the virus infected files.
monitor
Log the virus infected files.
emulator
Enable/disable the virus emulator.
option
-enable
FortiOS 8.0.0 CLI Reference
158
Fortinet Inc.

<!-- 来源页 159 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable the virus emulator.
disable
Disable the virus emulator.
external-blocklist
Enable/disable external-blocklist. Analyzes files
including the content of archives.
option
-disable
Option
Description
disable
Disable.
block
Block the matched files.
monitor
Log the matched files.
fortindr *
Enable/disable scanning of files by FortiNDR.
option
-disable
Option
Description
disable
Disable.
block
Block the FortiNDR detected infections.
monitor
Log the FortiNDR detected infections.
fortisandbox
Enable/disable scanning of files by FortiSandbox.
option
-disable
Option
Description
disable
Disable.
block
Block the FortiSandbox detected infections.
monitor
Log the FortiSandbox detected infections.
malware-stream
Enable/disable 0-day malware-stream scanning.
Analyzes files including the content of archives.
option
-disable
Option
Description
disable
Disable.
block
Block the matched files.
monitor
Log the matched files.
outbreak-prevention
Enable/disable virus outbreak prevention service.
option
-disable
FortiOS 8.0.0 CLI Reference
159
Fortinet Inc.

<!-- 来源页 160 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable.
block
Block the matched files.
monitor
Log the matched files.
quarantine
Enable/disable quarantine for infected files.
option
-disable
Option
Description
disable
Disable quarantine for infected files.
enable
Enable quarantine for infected files.
* This parameter may not exist in some models.
config http
Parameter
Description
Type
Size
Default
archive-block
Select the archive types to block.
option
-Option
Description
encrypted
Block encrypted archives.
corrupted
Block corrupted archives.
partiallycorrupted
Block partially corrupted archives.
multipart
Block multipart archives.
nested
Block nested archives that exceed uncompressed nest limit.
mailbomb
Block mail bomb archives.
timeout
Block scan timeout.
unhandled
Block archives that FortiOS cannot open.
archive-log
Select the archive types to log.
option
-Option
Description
encrypted
Log encrypted archives.
corrupted
Log corrupted archives.
partiallycorrupted
Log partially corrupted archives.
multipart
Log multipart archives.
FortiOS 8.0.0 CLI Reference
160
Fortinet Inc.

<!-- 来源页 161 -->
Parameter
Description
Type
Size
Default
Option
Description
nested
Log nested archives that exceed uncompressed nest limit.
mailbomb
Log mail bomb archives.
timeout
Log scan timeout.
unhandled
Log archives that FortiOS cannot open.
av-scan
Enable/disable AntiVirus scan service.
option
-disable
Option
Description
disable
Disable.
block
Block the virus infected files.
monitor
Log the virus infected files.
content-disarm
Enable/disable Content Disarm and Reconstruction
when performing AntiVirus scan.
option
-disable
Option
Description
disable
Disable Content Disarm and Reconstruction when performing AntiVirus
scan.
enable
Enable Content Disarm and Reconstruction when performing AntiVirus
scan.
emulator
Enable/disable the virus emulator.
option
-enable
Option
Description
enable
Enable the virus emulator.
disable
Disable the virus emulator.
external-blocklist
Enable/disable external-blocklist. Analyzes files
including the content of archives.
option
-disable
Option
Description
disable
Disable.
block
Block the matched files.
monitor
Log the matched files.
fortindr *
Enable/disable scanning of files by FortiNDR.
option
-disable
FortiOS 8.0.0 CLI Reference
161
Fortinet Inc.

<!-- 来源页 162 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable.
block
Block the FortiNDR detected infections.
monitor
Log the FortiNDR detected infections.
fortisandbox
Enable/disable scanning of files by FortiSandbox.
option
-disable
Option
Description
disable
Disable.
block
Block the FortiSandbox detected infections.
monitor
Log the FortiSandbox detected infections.
malware-stream
Enable/disable 0-day malware-stream scanning.
Analyzes files including the content of archives.
option
-disable
Option
Description
disable
Disable.
block
Block the matched files.
monitor
Log the matched files.
outbreak-prevention
Enable/disable virus outbreak prevention service.
option
-disable
Option
Description
disable
Disable.
block
Block the matched files.
monitor
Log the matched files.
quarantine
Enable/disable quarantine for infected files.
option
-disable
Option
Description
disable
Disable quarantine for infected files.
enable
Enable quarantine for infected files.
* This parameter may not exist in some models.
FortiOS 8.0.0 CLI Reference
162
Fortinet Inc.

<!-- 来源页 163 -->
config imap
Parameter
Description
Type
Size
Default
archive-block
Select the archive types to block.
option
-Option
Description
encrypted
Block encrypted archives.
corrupted
Block corrupted archives.
partiallycorrupted
Block partially corrupted archives.
multipart
Block multipart archives.
nested
Block nested archives that exceed uncompressed nest limit.
mailbomb
Block mail bomb archives.
timeout
Block scan timeout.
unhandled
Block archives that FortiOS cannot open.
archive-log
Select the archive types to log.
option
-Option
Description
encrypted
Log encrypted archives.
corrupted
Log corrupted archives.
partiallycorrupted
Log partially corrupted archives.
multipart
Log multipart archives.
nested
Log nested archives that exceed uncompressed nest limit.
mailbomb
Log mail bomb archives.
timeout
Log scan timeout.
unhandled
Log archives that FortiOS cannot open.
av-scan
Enable/disable AntiVirus scan service.
option
-disable
Option
Description
disable
Disable.
block
Block the virus infected files.
monitor
Log the virus infected files.
content-disarm
Enable/disable Content Disarm and Reconstruction
when performing AntiVirus scan.
option
-disable
FortiOS 8.0.0 CLI Reference
163
Fortinet Inc.

<!-- 来源页 164 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable Content Disarm and Reconstruction when performing AntiVirus
scan.
enable
Enable Content Disarm and Reconstruction when performing AntiVirus
scan.
emulator
Enable/disable the virus emulator.
option
-enable
Option
Description
enable
Enable the virus emulator.
disable
Disable the virus emulator.
executables
Treat Windows executable files as viruses for the
purpose of blocking or monitoring.
option
-default
Option
Description
default
Perform standard AntiVirus scanning of Windows executable files.
virus
Treat Windows executables as viruses.
external-blocklist
Enable/disable external-blocklist. Analyzes files
including the content of archives.
option
-disable
Option
Description
disable
Disable.
block
Block the matched files.
monitor
Log the matched files.
fortindr *
Enable/disable scanning of files by FortiNDR.
option
-disable
Option
Description
disable
Disable.
block
Block the FortiNDR detected infections.
monitor
Log the FortiNDR detected infections.
fortisandbox
Enable/disable scanning of files by FortiSandbox.
option
-disable
Option
Description
disable
Disable.
block
Block the FortiSandbox detected infections.
FortiOS 8.0.0 CLI Reference
164
Fortinet Inc.

<!-- 来源页 165 -->
Parameter
Description
Type
Size
Default
Option
Description
monitor
Log the FortiSandbox detected infections.
malware-stream
Enable/disable 0-day malware-stream scanning.
Analyzes files including the content of archives.
option
-disable
Option
Description
disable
Disable.
block
Block the matched files.
monitor
Log the matched files.
outbreak-prevention
Enable/disable virus outbreak prevention service.
option
-disable
Option
Description
disable
Disable.
block
Block the matched files.
monitor
Log the matched files.
quarantine
Enable/disable quarantine for infected files.
option
-disable
Option
Description
disable
Disable quarantine for infected files.
enable
Enable quarantine for infected files.
* This parameter may not exist in some models.
config mapi
Parameter
Description
Type
Size
Default
archive-block
Select the archive types to block.
option
-Option
Description
encrypted
Block encrypted archives.
corrupted
Block corrupted archives.
partiallycorrupted
Block partially corrupted archives.
multipart
Block multipart archives.
nested
Block nested archives that exceed uncompressed nest limit.
FortiOS 8.0.0 CLI Reference
165
Fortinet Inc.

<!-- 来源页 166 -->
Parameter
Description
Type
Size
Default
Option
Description
mailbomb
Block mail bomb archives.
timeout
Block scan timeout.
unhandled
Block archives that FortiOS cannot open.
archive-log
Select the archive types to log.
option
-Option
Description
encrypted
Log encrypted archives.
corrupted
Log corrupted archives.
partiallycorrupted
Log partially corrupted archives.
multipart
Log multipart archives.
nested
Log nested archives that exceed uncompressed nest limit.
mailbomb
Log mail bomb archives.
timeout
Log scan timeout.
unhandled
Log archives that FortiOS cannot open.
av-scan
Enable/disable AntiVirus scan service.
option
-disable
Option
Description
disable
Disable.
block
Block the virus infected files.
monitor
Log the virus infected files.
emulator
Enable/disable the virus emulator.
option
-enable
Option
Description
enable
Enable the virus emulator.
disable
Disable the virus emulator.
executables
Treat Windows executable files as viruses for the
purpose of blocking or monitoring.
option
-default
Option
Description
default
Perform standard AntiVirus scanning of Windows executable files.
virus
Treat Windows executables as viruses.
FortiOS 8.0.0 CLI Reference
166
Fortinet Inc.

<!-- 来源页 167 -->
Parameter
Description
Type
Size
Default
external-blocklist
Enable/disable external-blocklist. Analyzes files
including the content of archives.
option
-disable
Option
Description
disable
Disable.
block
Block the matched files.
monitor
Log the matched files.
fortindr *
Enable/disable scanning of files by FortiNDR.
option
-disable
Option
Description
disable
Disable.
block
Block the FortiNDR detected infections.
monitor
Log the FortiNDR detected infections.
fortisandbox
Enable/disable scanning of files by FortiSandbox.
option
-disable
Option
Description
disable
Disable.
block
Block the FortiSandbox detected infections.
monitor
Log the FortiSandbox detected infections.
malware-stream
Enable/disable 0-day malware-stream scanning.
Analyzes files including the content of archives.
option
-disable
Option
Description
disable
Disable.
block
Block the matched files.
monitor
Log the matched files.
outbreak-prevention
Enable/disable virus outbreak prevention service.
option
-disable
Option
Description
disable
Disable.
block
Block the matched files.
monitor
Log the matched files.
quarantine
Enable/disable quarantine for infected files.
option
-disable
FortiOS 8.0.0 CLI Reference
167
Fortinet Inc.

<!-- 来源页 168 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable quarantine for infected files.
enable
Enable quarantine for infected files.
* This parameter may not exist in some models.
config nac-quar
Parameter
Description
Type
Size
Default
expiry
Duration of quarantine.
user
Not
Specified
5m
infected
Enable/Disable quarantining infected hosts to the
banned user list.
option
-none
Option
Description
none
Do not quarantine infected hosts.
quar-src-ip
Quarantine all traffic from the infected hosts source IP.
log
Enable/disable AntiVirus quarantine logging.
option
-disable
Option
Description
enable
Enable AntiVirus quarantine logging.
disable
Disable AntiVirus quarantine logging.
config nntp
Parameter
Description
Type
Size
Default
archive-block
Select the archive types to block.
option
-Option
Description
encrypted
Block encrypted archives.
corrupted
Block corrupted archives.
partiallycorrupted
Block partially corrupted archives.
multipart
Block multipart archives.
nested
Block nested archives that exceed uncompressed nest limit.
mailbomb
Block mail bomb archives.
FortiOS 8.0.0 CLI Reference
168
Fortinet Inc.

<!-- 来源页 169 -->
Parameter
Description
Type
Size
Default
Option
Description
timeout
Block scan timeout.
unhandled
Block archives that FortiOS cannot open.
archive-log
Select the archive types to log.
option
-Option
Description
encrypted
Log encrypted archives.
corrupted
Log corrupted archives.
partiallycorrupted
Log partially corrupted archives.
multipart
Log multipart archives.
nested
Log nested archives that exceed uncompressed nest limit.
mailbomb
Log mail bomb archives.
timeout
Log scan timeout.
unhandled
Log archives that FortiOS cannot open.
av-scan
Enable/disable AntiVirus scan service.
option
-disable
Option
Description
disable
Disable.
block
Block the virus infected files.
monitor
Log the virus infected files.
emulator
Enable/disable the virus emulator.
option
-enable
Option
Description
enable
Enable the virus emulator.
disable
Disable the virus emulator.
external-blocklist
Enable/disable external-blocklist. Analyzes files
including the content of archives.
option
-disable
Option
Description
disable
Disable.
block
Block the matched files.
monitor
Log the matched files.
FortiOS 8.0.0 CLI Reference
169
Fortinet Inc.

<!-- 来源页 170 -->
Parameter
Description
Type
Size
Default
fortindr *
Enable/disable scanning of files by FortiNDR.
option
-disable
Option
Description
disable
Disable.
block
Block the FortiNDR detected infections.
monitor
Log the FortiNDR detected infections.
fortisandbox
Enable/disable scanning of files by FortiSandbox.
option
-disable
Option
Description
disable
Disable.
block
Block the FortiSandbox detected infections.
monitor
Log the FortiSandbox detected infections.
malware-stream
Enable/disable 0-day malware-stream scanning.
Analyzes files including the content of archives.
option
-disable
Option
Description
disable
Disable.
block
Block the matched files.
monitor
Log the matched files.
outbreak-prevention
Enable/disable virus outbreak prevention service.
option
-disable
Option
Description
disable
Disable.
block
Block the matched files.
monitor
Log the matched files.
quarantine
Enable/disable quarantine for infected files.
option
-disable
Option
Description
disable
Disable quarantine for infected files.
enable
Enable quarantine for infected files.
* This parameter may not exist in some models.
FortiOS 8.0.0 CLI Reference
170
Fortinet Inc.

<!-- 来源页 171 -->
config pop3
Parameter
Description
Type
Size
Default
archive-block
Select the archive types to block.
option
-Option
Description
encrypted
Block encrypted archives.
corrupted
Block corrupted archives.
partiallycorrupted
Block partially corrupted archives.
multipart
Block multipart archives.
nested
Block nested archives that exceed uncompressed nest limit.
mailbomb
Block mail bomb archives.
timeout
Block scan timeout.
unhandled
Block archives that FortiOS cannot open.
archive-log
Select the archive types to log.
option
-Option
Description
encrypted
Log encrypted archives.
corrupted
Log corrupted archives.
partiallycorrupted
Log partially corrupted archives.
multipart
Log multipart archives.
nested
Log nested archives that exceed uncompressed nest limit.
mailbomb
Log mail bomb archives.
timeout
Log scan timeout.
unhandled
Log archives that FortiOS cannot open.
av-scan
Enable/disable AntiVirus scan service.
option
-disable
Option
Description
disable
Disable.
block
Block the virus infected files.
monitor
Log the virus infected files.
content-disarm
Enable/disable Content Disarm and Reconstruction
when performing AntiVirus scan.
option
-disable
FortiOS 8.0.0 CLI Reference
171
Fortinet Inc.

<!-- 来源页 172 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable Content Disarm and Reconstruction when performing AntiVirus
scan.
enable
Enable Content Disarm and Reconstruction when performing AntiVirus
scan.
emulator
Enable/disable the virus emulator.
option
-enable
Option
Description
enable
Enable the virus emulator.
disable
Disable the virus emulator.
executables
Treat Windows executable files as viruses for the
purpose of blocking or monitoring.
option
-default
Option
Description
default
Perform standard AntiVirus scanning of Windows executable files.
virus
Treat Windows executables as viruses.
external-blocklist
Enable/disable external-blocklist. Analyzes files
including the content of archives.
option
-disable
Option
Description
disable
Disable.
block
Block the matched files.
monitor
Log the matched files.
fortindr *
Enable/disable scanning of files by FortiNDR.
option
-disable
Option
Description
disable
Disable.
block
Block the FortiNDR detected infections.
monitor
Log the FortiNDR detected infections.
fortisandbox
Enable/disable scanning of files by FortiSandbox.
option
-disable
Option
Description
disable
Disable.
block
Block the FortiSandbox detected infections.
FortiOS 8.0.0 CLI Reference
172
Fortinet Inc.

<!-- 来源页 173 -->
Parameter
Description
Type
Size
Default
Option
Description
monitor
Log the FortiSandbox detected infections.
malware-stream
Enable/disable 0-day malware-stream scanning.
Analyzes files including the content of archives.
option
-disable
Option
Description
disable
Disable.
block
Block the matched files.
monitor
Log the matched files.
outbreak-prevention
Enable/disable virus outbreak prevention service.
option
-disable
Option
Description
disable
Disable.
block
Block the matched files.
monitor
Log the matched files.
quarantine
Enable/disable quarantine for infected files.
option
-disable
Option
Description
disable
Disable quarantine for infected files.
enable
Enable quarantine for infected files.
* This parameter may not exist in some models.
config smtp
Parameter
Description
Type
Size
Default
archive-block
Select the archive types to block.
option
-Option
Description
encrypted
Block encrypted archives.
corrupted
Block corrupted archives.
partiallycorrupted
Block partially corrupted archives.
multipart
Block multipart archives.
nested
Block nested archives that exceed uncompressed nest limit.
FortiOS 8.0.0 CLI Reference
173
Fortinet Inc.

<!-- 来源页 174 -->
Parameter
Description
Type
Size
Default
Option
Description
mailbomb
Block mail bomb archives.
timeout
Block scan timeout.
unhandled
Block archives that FortiOS cannot open.
archive-log
Select the archive types to log.
option
-Option
Description
encrypted
Log encrypted archives.
corrupted
Log corrupted archives.
partiallycorrupted
Log partially corrupted archives.
multipart
Log multipart archives.
nested
Log nested archives that exceed uncompressed nest limit.
mailbomb
Log mail bomb archives.
timeout
Log scan timeout.
unhandled
Log archives that FortiOS cannot open.
av-scan
Enable/disable AntiVirus scan service.
option
-disable
Option
Description
disable
Disable.
block
Block the virus infected files.
monitor
Log the virus infected files.
content-disarm
Enable/disable Content Disarm and Reconstruction
when performing AntiVirus scan.
option
-disable
Option
Description
disable
Disable Content Disarm and Reconstruction when performing AntiVirus
scan.
enable
Enable Content Disarm and Reconstruction when performing AntiVirus
scan.
emulator
Enable/disable the virus emulator.
option
-enable
Option
Description
enable
Enable the virus emulator.
FortiOS 8.0.0 CLI Reference
174
Fortinet Inc.

<!-- 来源页 175 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable the virus emulator.
executables
Treat Windows executable files as viruses for the
purpose of blocking or monitoring.
option
-default
Option
Description
default
Perform standard AntiVirus scanning of Windows executable files.
virus
Treat Windows executables as viruses.
external-blocklist
Enable/disable external-blocklist. Analyzes files
including the content of archives.
option
-disable
Option
Description
disable
Disable.
block
Block the matched files.
monitor
Log the matched files.
fortindr *
Enable/disable scanning of files by FortiNDR.
option
-disable
Option
Description
disable
Disable.
block
Block the FortiNDR detected infections.
monitor
Log the FortiNDR detected infections.
fortisandbox
Enable/disable scanning of files by FortiSandbox.
option
-disable
Option
Description
disable
Disable.
block
Block the FortiSandbox detected infections.
monitor
Log the FortiSandbox detected infections.
malware-stream
Enable/disable 0-day malware-stream scanning.
Analyzes files including the content of archives.
option
-disable
Option
Description
disable
Disable.
block
Block the matched files.
monitor
Log the matched files.
FortiOS 8.0.0 CLI Reference
175
Fortinet Inc.

<!-- 来源页 176 -->
Parameter
Description
Type
Size
Default
outbreak-prevention
Enable/disable virus outbreak prevention service.
option
-disable
Option
Description
disable
Disable.
block
Block the matched files.
monitor
Log the matched files.
quarantine
Enable/disable quarantine for infected files.
option
-disable
Option
Description
disable
Disable quarantine for infected files.
enable
Enable quarantine for infected files.
* This parameter may not exist in some models.
config ssh
Parameter
Description
Type
Size
Default
archive-block
Select the archive types to block.
option
-Option
Description
encrypted
Block encrypted archives.
corrupted
Block corrupted archives.
partiallycorrupted
Block partially corrupted archives.
multipart
Block multipart archives.
nested
Block nested archives that exceed uncompressed nest limit.
mailbomb
Block mail bomb archives.
timeout
Block scan timeout.
unhandled
Block archives that FortiOS cannot open.
archive-log
Select the archive types to log.
option
-Option
Description
encrypted
Log encrypted archives.
corrupted
Log corrupted archives.
partiallycorrupted
Log partially corrupted archives.
FortiOS 8.0.0 CLI Reference
176
Fortinet Inc.

<!-- 来源页 177 -->
Parameter
Description
Type
Size
Default
Option
Description
multipart
Log multipart archives.
nested
Log nested archives that exceed uncompressed nest limit.
mailbomb
Log mail bomb archives.
timeout
Log scan timeout.
unhandled
Log archives that FortiOS cannot open.
av-scan
Enable/disable AntiVirus scan service.
option
-disable
Option
Description
disable
Disable.
block
Block the virus infected files.
monitor
Log the virus infected files.
emulator
Enable/disable the virus emulator.
option
-enable
Option
Description
enable
Enable the virus emulator.
disable
Disable the virus emulator.
external-blocklist
Enable/disable external-blocklist. Analyzes files
including the content of archives.
option
-disable
Option
Description
disable
Disable.
block
Block the matched files.
monitor
Log the matched files.
fortindr *
Enable/disable scanning of files by FortiNDR.
option
-disable
Option
Description
disable
Disable.
block
Block the FortiNDR detected infections.
monitor
Log the FortiNDR detected infections.
fortisandbox
Enable/disable scanning of files by FortiSandbox.
option
-disable
FortiOS 8.0.0 CLI Reference
177
Fortinet Inc.

<!-- 来源页 178 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable.
block
Block the FortiSandbox detected infections.
monitor
Log the FortiSandbox detected infections.
malware-stream
Enable/disable 0-day malware-stream scanning.
Analyzes files including the content of archives.
option
-disable
Option
Description
disable
Disable.
block
Block the matched files.
monitor
Log the matched files.
outbreak-prevention
Enable/disable virus outbreak prevention service.
option
-disable
Option
Description
disable
Disable.
block
Block the matched files.
monitor
Log the matched files.
quarantine
Enable/disable quarantine for infected files.
option
-disable
Option
Description
disable
Disable quarantine for infected files.
enable
Enable quarantine for infected files.
* This parameter may not exist in some models.
config websocket
Parameter
Description
Type
Size
Default
archive-block
Select the archive types to block.
option
-Option
Description
encrypted
Block encrypted archives.
corrupted
Block corrupted archives.
partiallycorrupted
Block partially corrupted archives.
FortiOS 8.0.0 CLI Reference
178
Fortinet Inc.

<!-- 来源页 179 -->
Parameter
Description
Type
Size
Default
Option
Description
multipart
Block multipart archives.
nested
Block nested archives that exceed uncompressed nest limit.
mailbomb
Block mail bomb archives.
timeout
Block scan timeout.
unhandled
Block archives that FortiOS cannot open.
archive-log
Select the archive types to log.
option
-Option
Description
encrypted
Log encrypted archives.
corrupted
Log corrupted archives.
partiallycorrupted
Log partially corrupted archives.
multipart
Log multipart archives.
nested
Log nested archives that exceed uncompressed nest limit.
mailbomb
Log mail bomb archives.
timeout
Log scan timeout.
unhandled
Log archives that FortiOS cannot open.
av-scan
Enable/disable AntiVirus scan service.
option
-disable
Option
Description
disable
Disable.
block
Block the virus infected files.
monitor
Log the virus infected files.
emulator
Enable/disable the virus emulator.
option
-enable
Option
Description
enable
Enable the virus emulator.
disable
Disable the virus emulator.
external-blocklist
Enable/disable external-blocklist. Analyzes files
including the content of archives.
option
-disable
FortiOS 8.0.0 CLI Reference
179
Fortinet Inc.

<!-- 来源页 180 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable.
block
Block the matched files.
monitor
Log the matched files.
fortindr *
Enable/disable scanning of files by FortiNDR.
option
-disable
Option
Description
disable
Disable.
block
Block the FortiNDR detected infections.
monitor
Log the FortiNDR detected infections.
fortisandbox
Enable/disable scanning of files by FortiSandbox.
option
-disable
Option
Description
disable
Disable.
block
Block the FortiSandbox detected infections.
monitor
Log the FortiSandbox detected infections.
malware-stream
Enable/disable 0-day malware-stream scanning.
Analyzes files including the content of archives.
option
-disable
Option
Description
disable
Disable.
block
Block the matched files.
monitor
Log the matched files.
outbreak-prevention
Enable/disable virus outbreak prevention service.
option
-disable
Option
Description
disable
Disable.
block
Block the matched files.
monitor
Log the matched files.
quarantine
Enable/disable quarantine for infected files.
option
-disable
FortiOS 8.0.0 CLI Reference
180
Fortinet Inc.

<!-- 来源页 181 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable quarantine for infected files.
enable
Enable quarantine for infected files.
* This parameter may not exist in some models.
config antivirus quarantine
Configure quarantine options.
config antivirus quarantine
Description: Configure quarantine options.
set agelimit {integer}
set destination [NULL|disk|...]
set drop-infected {option1}, {option2}, ...
set drop-machine-learning {option1}, {option2}, ...
set lowspace [drop-new|ovrw-old]
set maxfilesize {integer}
set quarantine-quota {integer}
set store-infected {option1}, {option2}, ...
set store-machine-learning {option1}, {option2}, ...
end
config antivirus quarantine
Parameter
Description
Type
Size
Default
agelimit
Age limit for quarantined files (0 - 479 hours, 0
means forever).
integer
Minimum value:
0 Maximum
value: 479
0
destination
Choose whether to quarantine files to the
FortiGate disk or to FortiAnalyzer or to delete
them instead of quarantining them.
option
-disk **
Option
Description
NULL
Files that would be quarantined are deleted.
disk
Quarantine files to the FortiGate hard disk.
FortiAnalyzer
FortiAnalyzer
FortiOS 8.0.0 CLI Reference
181
Fortinet Inc.

<!-- 来源页 182 -->
Parameter
Description
Type
Size
Default
drop-infected
Do not quarantine infected files found in
sessions using the selected protocols. Dropped
files are deleted instead of being quarantined.
option
-Option
Description
imap
IMAP.
smtp
SMTP.
pop3
POP3.
http
HTTP.
ftp
FTP.
nntp
NNTP.
imaps
IMAPS.
smtps
SMTPS.
pop3s
POP3S.
https
HTTPS.
ftps
FTPS.
mapi
MAPI.
cifs
CIFS.
ssh
SSH.
drop-machine-learning
Do not quarantine files detected by machine
learning found in sessions using the selected
protocols. Dropped files are deleted instead of
being quarantined.
option
-Option
Description
imap
IMAP.
smtp
SMTP.
pop3
POP3.
http
HTTP.
ftp
FTP.
nntp
NNTP.
imaps
IMAPS.
smtps
SMTPS.
FortiOS 8.0.0 CLI Reference
182
Fortinet Inc.

<!-- 来源页 183 -->
Parameter
Description
Type
Size
Default
Option
Description
pop3s
POP3S.
https
HTTPS.
ftps
FTPS.
mapi
MAPI.
cifs
CIFS.
ssh
SSH.
lowspace
Select the method for handling additional files
when running low on disk space.
option
-ovrw-old
Option
Description
drop-new
Drop (delete) the most recently quarantined files.
ovrw-old
Overwrite the oldest quarantined files. That is, the files that are closest
to being deleted from the quarantine.
maxfilesize
Maximum file size to quarantine (0 - 500
Mbytes, 0 means unlimited).
integer
Minimum value:
0 Maximum
value: 500
0
quarantine-quota
The amount of disk space to reserve for
quarantining files (0 - 4294967295 Mbytes, 0
means unlimited and depends on disk space).
integer
Minimum value:
0 Maximum
value:
4294967295
0
store-infected
Quarantine infected files found in sessions
using the selected protocols.
option
-imap smtp
pop3 http
ftp nntp
imaps
smtps
pop3s
https ftps
mapi cifs
ssh
Option
Description
imap
IMAP.
smtp
SMTP.
pop3
POP3.
http
HTTP.
FortiOS 8.0.0 CLI Reference
183
Fortinet Inc.

<!-- 来源页 184 -->
Parameter
Description
Type
Size
Default
Option
Description
ftp
FTP.
nntp
NNTP.
imaps
IMAPS.
smtps
SMTPS.
pop3s
POP3S.
https
HTTPS.
ftps
FTPS.
mapi
MAPI.
cifs
CIFS.
ssh
SSH.
store-machine-learning
Quarantine files detected by machine learning
found in sessions using the selected protocols.
option
-imap smtp
pop3 http
ftp nntp
imaps
smtps
pop3s
https ftps
mapi cifs
ssh
Option
Description
imap
IMAP.
smtp
SMTP.
pop3
POP3.
http
HTTP.
ftp
FTP.
nntp
NNTP.
imaps
IMAPS.
smtps
SMTPS.
pop3s
POP3S.
https
HTTPS.
ftps
FTPS.
FortiOS 8.0.0 CLI Reference
184
Fortinet Inc.

<!-- 来源页 185 -->
Parameter
Description
Type
Size
Default
Option
Description
mapi
MAPI.
cifs
CIFS.
ssh
SSH.
** Values may differ between models.
config antivirus settings
Configure AntiVirus settings.
config antivirus settings
Description: Configure AntiVirus settings.
set cache-infected-result [enable|disable]
set grayware [enable|disable]
set machine-learning-detection [enable|monitor|...]
set override-timeout {integer}
set use-extreme-db [enable|disable]
end
config antivirus settings
Parameter
Description
Type
Size
Default
cache-infected-result
Enable/disable cache of infected scan results
(default = enable).
option
-enable
Option
Description
enable
Enable cache of infected scan results.
disable
Disable cache of infected scan results.
grayware
Enable/disable grayware detection when an
AntiVirus profile is applied to traffic.
option
-disable
Option
Description
enable
Enable grayware detection.
disable
Disable grayware detection.
FortiOS 8.0.0 CLI Reference
185
Fortinet Inc.

<!-- 来源页 186 -->
Parameter
Description
Type
Size
Default
machine-learning-detection
Use machine learning based malware detection.
option
-enable
Option
Description
enable
Enable machine learning based malware detection.
monitor
Enable machine learning based malware detection for monitoring only.
disable
Disable machine learning based malware detection.
override-timeout
Override the large file scan timeout value in
seconds (30 - 3600). Zero is the default value and
is used to disable this command. When disabled,
the daemon adjusts the large file scan timeout
based on the file size.
integer
Minimum
value: 30
Maximum
value: 3600
0
use-extreme-db
Enable/disable the use of Extreme AVDB.
option
-disable
Option
Description
enable
Enable extreme AVDB.
disable
Disable extreme AVDB.
FortiOS 8.0.0 CLI Reference
186
Fortinet Inc.

---


<!-- 来源页 851 -->
ips
This section includes syntax for the following commands:
l config ips custom on page 851
l config ips decoder on page 853
l config ips global on page 853
l config ips rule-settings on page 860
l config ips rule on page 858
l config ips sensor on page 860
l config ips settings on page 867
l config ips view-map on page 868
config ips custom
Configure IPS custom signature.
config ips custom
Description: Configure IPS custom signature.
edit <tag>
set action [pass|block]
set application {user}
set comment {string}
set location {user}
set log [disable|enable]
set log-packet [disable|enable]
set os {user}
set protocol {user}
set rule-id {integer}
set severity {user}
set signature {var-string}
set status [disable|enable]
next
end
config ips custom
Parameter
Description
Type
Size
Default
action
Default action (pass or block) for this signature.
option
-pass
FortiOS 8.0.0 CLI Reference
851
Fortinet Inc.

<!-- 来源页 852 -->
Parameter
Description
Type
Size
Default
Option
Description
pass
Pass or allow matching traffic.
block
Block or drop matching traffic.
application
Applications to be protected. Blank for all
applications.
user
Not Specified
comment
Comment.
string
Maximum
length: 63
location
Protect client or server traffic.
user
Not Specified
log
Enable/disable logging.
option
-enable
Option
Description
disable
Disable logging.
enable
Enable logging.
log-packet
Enable/disable packet logging.
option
-disable
Option
Description
disable
Disable packet logging.
enable
Enable packet logging.
os
Operating system(s) that the signature protects.
Blank for all operating systems.
user
Not Specified
protocol
Protocol(s) that the signature scans. Blank for all
protocols.
user
Not Specified
rule-id
Signature ID. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
severity
Relative severity of the signature, from info to
critical. Log messages generated by the
signature include the severity.
user
Not Specified
signature
Custom signature enclosed in single quotes.
var-string
Maximum
length: 4095
status
Enable/disable this signature.
option
-enable
Option
Description
disable
Disable status.
FortiOS 8.0.0 CLI Reference
852
Fortinet Inc.

<!-- 来源页 853 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable status.
tag
Signature tag.
string
Maximum
length: 63
config ips decoder
Configure IPS decoder. Read-only.
config ips decoder
Description: Configure IPS decoder. Read-only.
edit <name>
config parameter
Description: IPS group parameters. Read-only.
edit <name>
set value {string}
next
end
next
end
config ips decoder
Parameter
Description
Type
Size
Default
name
Decoder name.
string
Maximum length:
63
config parameter
Parameter
Description
Type
Size
Default
name
Parameter name.
string
Maximum length: 31
value
Parameter value.
string
Maximum length:
199
config ips global
Configure IPS global parameter.
FortiOS 8.0.0 CLI Reference
853
Fortinet Inc.

<!-- 来源页 854 -->
config ips global
Description: Configure IPS global parameter.
set anomaly-mode [periodical|continuous]
set av-mem-limit {integer}
set cp-accel-mode [none|basic|...]
set database [regular|extended]
set deep-app-insp-db-limit {integer}
set deep-app-insp-timeout {integer}
set engine-count {integer}
set exclude-signatures [none|ot]
set fail-open [enable|disable]
set ips-reserve-cpu [disable|enable]
set machine-learning-detection [enable|disable]
set ngfw-max-scan-range {integer}
set np-accel-mode [none|basic]
set packet-log-queue-depth {integer}
set session-limit-mode [accurate|heuristic]
set socket-size {integer}
set sync-session-ttl [enable|disable]
config tls-active-probe
Description: TLS active probe configuration.
set interface {string}
set interface-select-method [auto|sdwan|...]
set source-ip {ipv4-address}
set source-ip6 {ipv6-address}
set vdom {string}
end
set traffic-submit [enable|disable]
end
config ips global
Parameter
Description
Type
Size
Default
anomaly-mode
Global blocking mode for rate-based
anomalies.
option
-continuous
Option
Description
periodical
After an anomaly is detected, allow the number of packets per second
according to the anomaly configuration.
continuous
Block packets once an anomaly is detected. Overrides individual
anomaly settings.
av-mem-limit
Maximum percentage of system memory
allowed for use on AV scanning (10 - 50,
default = zero). To disable set to zero. When
disabled, there is no limit on the AV memory
usage.
integer
Minimum value:
10 Maximum
value: 50
0
FortiOS 8.0.0 CLI Reference
854
Fortinet Inc.

<!-- 来源页 855 -->
Parameter
Description
Type
Size
Default
cp-accel-mode *
IPS Pattern matching acceleration/offloading
to CPx processors.
option
-advanced **
Option
Description
none
CPx acceleration/offloading disabled.
basic
Offload basic pattern matching to CPx processors.
advanced
Offload more types of pattern matching resulting in higher throughput
than basic mode.
database
Regular or extended IPS database. Regular
protects against the latest common and in-the-wild attacks. Extended includes
protection from legacy attacks.
option
-extended **
Option
Description
regular
IPS regular database package.
extended
IPS extended database package.
deep-app-insp-db-limit
Limit on number of entries in deep application
inspection database (1 - 2147483647, use
recommended setting = 0).
integer
Minimum value:
0 Maximum
value:
2147483647
0
deep-app-insp-timeout
Timeout for Deep application inspection (1 -2147483647 sec., 0 = use recommended
setting).
integer
Minimum value:
0 Maximum
value:
2147483647
0
engine-count
Number of IPS engines running. If set to the
default value of 0, FortiOS sets the number to
optimize performance depending on the
number of CPU cores.
integer
Minimum value:
0 Maximum
value: 255
0
exclude-signatures
Excluded signatures.
option
-ot
Option
Description
none
No signatures excluded.
ot
Exclude ot signatures.
fail-open
Enable to allow traffic if the IPS buffer is full.
Default is disable and IPS traffic is blocked
when the IPS buffer is full.
option
-disable
FortiOS 8.0.0 CLI Reference
855
Fortinet Inc.

<!-- 来源页 856 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable IPS fail open.
disable
Disable IPS fail open.
ips-reserve-cpu *
Enable/disable IPS daemon's use of CPUs
other than CPU 0.
option
-disable
Option
Description
disable
Disable IPS daemon's use of CPUs other than CPU 0 (all daemons run on
all CPUs).
enable
Enable IPS daemon's use of CPUs other than CPU 0.
machine-learning-detection
Enable/disable machine learning detection.
option
-enable
Option
Description
enable
Enable ML detection.
disable
Disable ML detection.
ngfw-max-scan-range
NGFW policy-mode app detection threshold.
integer
Minimum value:
0 Maximum
value:
4294967295
4096
np-accel-mode *
Acceleration mode for IPS processing by NPx
processors.
option
-basic
Option
Description
none
NPx acceleration disabled.
basic
NPx acceleration enabled.
packet-log-queue-depth
Packet/pcap log queue depth per IPS engine.
integer
Minimum value:
128 Maximum
value: 4096
128
session-limit-mode
Method of counting concurrent sessions
used by session limit anomalies. Choose
between greater accuracy (accurate) or
improved performance (heuristics).
option
-heuristic
FortiOS 8.0.0 CLI Reference
856
Fortinet Inc.

<!-- 来源页 857 -->
Parameter
Description
Type
Size
Default
Option
Description
accurate
Accurately count concurrent sessions, demands more resources.
heuristic
Use heuristics to estimate the number of concurrent sessions.
Acceptable in most cases.
socket-size
IPS socket buffer size. Max and default value
depend on available memory. Can be
changed to tune performance.
integer
Minimum value:
0 Maximum
value: 256 **
128 **
sync-session-ttl
Enable/disable use of kernel session TTL for
IPS sessions.
option
-enable
Option
Description
enable
Enable use of kernel session TTL for IPS sessions.
disable
Disable use of kernel session TTL for IPS sessions.
traffic-submit
Enable/disable submitting attack data found
by this FortiGate to FortiGuard.
option
-disable
Option
Description
enable
Enable traffic submit.
disable
Disable traffic submit.
* This parameter may not exist in some models.
** Values may differ between models.
config tls-active-probe
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
FortiOS 8.0.0 CLI Reference
857
Fortinet Inc.

<!-- 来源页 858 -->
Parameter
Description
Type
Size
Default
source-ip
Source IP address used for TLS active probe.
ipv4-address
Not
Specified
0.0.0.0
source-ip6
Source IPv6 address used for TLS active probe.
ipv6-address
Not
Specified
::
vdom
Virtual domain name for TLS active probe.
string
Maximum
length: 31
config ips rule
Configure IPS rules. Read-only.
config ips rule
Description: Configure IPS rules. Read-only.
edit <name>
set action [pass|block]
set application {user}
set date {integer}
set group {string}
set location {user}
set log [disable|enable]
set log-packet [disable|enable]
config metadata
Description: Meta data. Read-only.
edit <id>
set metaid {integer}
set valueid {integer}
next
end
set os {user}
set rev {integer}
set rule-id {integer}
set service {user}
set severity {user}
next
end
config ips rule
Parameter
Description
Type
Size
Default
action
Action. Read-only.
option
-pass
FortiOS 8.0.0 CLI Reference
858
Fortinet Inc.

<!-- 来源页 859 -->
Parameter
Description
Type
Size
Default
Option
Description
pass
Pass or allow matching traffic.
block
Block or drop matching traffic.
application
Vulnerable applications. Read-only.
user
Not Specified
date
Date. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
group
Group. Read-only.
string
Maximum
length: 63
location
Vulnerable location. Read-only.
user
Not Specified
log
Enable/disable logging. Read-only.
option
-enable
Option
Description
disable
Disable logging.
enable
Enable logging.
log-packet
Enable/disable packet logging. Read-only.
option
-disable
Option
Description
disable
Disable packet logging.
enable
Enable packet logging.
name
Rule name.
string
Maximum
length: 63
os
Vulnerable operation systems. Read-only.
user
Not Specified
rev
Revision. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
rule-id
Rule ID. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
service
Vulnerable service. Read-only.
user
Not Specified
severity
Severity. Read-only.
user
Not Specified
FortiOS 8.0.0 CLI Reference
859
Fortinet Inc.

<!-- 来源页 860 -->
config metadata
Parameter
Description
Type
Size
Default
id
ID. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
metaid
Meta ID. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
valueid
Value ID. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
config ips rule-settings
Configure IPS rule setting. Read-only.
config ips rule-settings
Description: Configure IPS rule setting. Read-only.
edit <id>
next
end
config ips rule-settings
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
config ips sensor
Configure IPS sensor.
config ips sensor
Description: Configure IPS sensor.
edit <name>
set block-malicious-url [disable|enable]
FortiOS 8.0.0 CLI Reference
860
Fortinet Inc.

<!-- 来源页 861 -->
set comment {var-string}
config entries
Description: IPS sensor filter.
edit <id>
set action [pass|block|...]
set application {user}
set cve <cve-entry1>, <cve-entry2>, ...
set default-action [all|pass|...]
set default-status [all|enable|...]
config exempt-ip
Description: Traffic from selected source or destination IP addresses is
exempt from this signature.
edit <id>
set dst-ip {ipv4-classnet}
set src-ip {ipv4-classnet}
next
end
set last-modified {user}
set location {user}
set log [disable|enable]
set log-attack-context [disable|enable]
set log-packet [disable|enable]
set os {user}
set protocol {user}
set quarantine [none|attacker]
set quarantine-expiry {user}
set quarantine-log [disable|enable]
set rate-count {integer}
set rate-duration {integer}
set rate-mode [periodical|continuous]
set rate-track [none|src-ip|...]
set rule <id1>, <id2>, ...
set severity {user}
set status [disable|enable|...]
set vuln-type <id1>, <id2>, ...
next
end
set extended-log [enable|disable]
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set replacemsg-group {string}
set scan-botnet-connections [disable|block|...]
set uuid {uuid}
next
end
FortiOS 8.0.0 CLI Reference
861
Fortinet Inc.

<!-- 来源页 862 -->
config ips sensor
Parameter
Description
Type
Size
Default
block-malicious-url
Enable/disable malicious URL blocking.
option
-disable
Option
Description
disable
Disable malicious URL blocking.
enable
Enable malicious URL blocking.
comment
Comment.
var-string
Maximum
length: 255
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
FortiOS 8.0.0 CLI Reference
862
Fortinet Inc.

<!-- 来源页 863 -->
Parameter
Description
Type
Size
Default
name
Sensor name.
string
Maximum
length: 47
replacemsg-group
Replacement message group.
string
Maximum
length: 35
scan-botnet-connections
Block or monitor connections to Botnet
servers, or disable Botnet scanning.
option
-disable
Option
Description
disable
Do not scan connections to botnet servers.
block
Block connections to botnet servers.
monitor
Log connections to botnet servers.
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
action
Action taken with traffic in which signatures
are detected.
option
-default
Option
Description
pass
Pass or allow matching traffic.
block
Block or drop matching traffic.
reset
Reset sessions for matching traffic.
default
Pass or drop matching traffic, depending on the default action of the
signature.
application
Operating systems to be protected. Use all for
every application and other for unlisted
application.
user
Not Specified
all
cve <cve-entry>
List of CVE IDs of the signatures to add to the
sensor.
CVE IDs or CVE wildcards.
string
Maximum
length: 19
default-action
Signature default action filter.
option
-all
FortiOS 8.0.0 CLI Reference
863
Fortinet Inc.

<!-- 来源页 864 -->
Parameter
Description
Type
Size
Default
Option
Description
all
Selects signatures with any default action.
pass
Selects signatures with default action 'pass'.
block
Selects signatures with default action 'block'.
default-status
Signature default status filter.
option
-all
Option
Description
all
Selects signatures with any default status.
enable
Selects signatures enabled by default.
disable
Selects signatures disabled by default.
id
Rule ID in IPS database (0 - 4294967295).
integer
Minimum value:
0 Maximum
value:
4294967295
0
last-modified
Filter by signature last modified date.
Formats: before <date>, after <date>,
between <start-date> <end-date>.
user
Not Specified
location
Protect client or server traffic.
user
Not Specified
all
log
Enable/disable logging of signatures included
in filter.
option
-enable
Option
Description
disable
Disable logging of selected rules.
enable
Enable logging of selected rules.
log-attack-context
Enable/disable logging of attack context: URL
buffer, header buffer, body buffer, packet
buffer.
option
-disable
Option
Description
disable
Disable logging of detailed attack context.
enable
Enable logging of detailed attack context.
log-packet
Enable/disable packet logging. Enable to save
the packet that triggers the filter. You can
download the packets in pcap format for
diagnostic use.
option
-disable
FortiOS 8.0.0 CLI Reference
864
Fortinet Inc.

<!-- 来源页 865 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable packet logging of selected rules.
enable
Enable packet logging of selected rules.
os
Operating systems to be protected. Use all for
every operating system and other for unlisted
operating systems.
user
Not Specified
all
protocol
Protocols to be examined. Use all for every
protocol and other for unlisted protocols.
user
Not Specified
all
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
Duration of quarantine. (Format
###d##h##m, minimum 1m, maximum
364d23h59m, default = 5m). Requires
quarantine set to attacker.
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
rate-count
Count of the rate.
integer
Minimum value:
0 Maximum
value: 65535
0
rate-duration
Duration (sec) of the rate.
integer
Minimum value:
1 Maximum
value: 65535
60
rate-mode
Rate limit mode.
option
-continuous
Option
Description
periodical
Allow configured number of packets every rate-duration.
continuous
Block packets once the rate is reached.
FortiOS 8.0.0 CLI Reference
865
Fortinet Inc.

<!-- 来源页 866 -->
Parameter
Description
Type
Size
Default
rate-track
Track the packet protocol field.
option
-none
Option
Description
none
none
src-ip
Source IP.
dest-ip
Destination IP.
dhcp-client-mac
DHCP client.
dns-domain
DNS domain.
rule <id>
Identifies the predefined or custom IPS
signatures to add to the sensor.
Rule IPS.
integer
Minimum value:
0 Maximum
value:
4294967295
severity
Relative severity of the signature, from info to
critical. Log messages generated by the
signature include the severity.
user
Not Specified
all
status
Status of the signatures included in filter. Only
those filters with a status to enable are used.
option
-default
Option
Description
disable
Disable status of selected rules.
enable
Enable status of selected rules.
default
Default.
vuln-type
<id>
List of signature vulnerability types to filter
by.
Vulnerability type ID.
integer
Minimum value:
0 Maximum
value:
4294967295
config exempt-ip
Parameter
Description
Type
Size
Default
dst-ip
Destination IP address and netmask (applies to
packet matching the signature).
ipv4-classnet
Not Specified
0.0.0.0
0.0.0.0
id
Exempt IP ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
src-ip
Source IP address and netmask (applies to
packet matching the signature).
ipv4-classnet
Not Specified
0.0.0.0
0.0.0.0
FortiOS 8.0.0 CLI Reference
866
Fortinet Inc.

<!-- 来源页 867 -->
config ips settings
Configure IPS VDOM parameter.
config ips settings
Description: Configure IPS VDOM parameter.
set ha-session-pickup [connectivity|security]
set ips-packet-quota {integer}
set packet-log-history {integer}
set packet-log-memory {integer}
set packet-log-post-attack {integer}
set proxy-inline-ips [disable|enable]
end
config ips settings
Parameter
Description
Type
Size
Default
ha-session-pickup
IPS HA failover session pickup preference.
option
-connectivity
Option
Description
connectivity
Prefer session continuity.
security
Prefer session complete security.
ips-packet-quota
Maximum amount of disk space in MB for
logged packets when logging to disk. Range
depends on disk size.
integer
Minimum value:
0 Maximum
value:
4294967295
0
packet-log-history
Number of packets to capture before and
including the one in which the IPS signature
is detected (1 - 255).
integer
Minimum value:
1 Maximum
value: 255
1
packet-log-memory
Maximum memory can be used by packet log
(64 - 8192 kB).
integer
Minimum value:
64 Maximum
value: 8192
256
packet-log-post-attack
Number of packets to log after the IPS
signature is detected (0 - 255).
integer
Minimum value:
0 Maximum
value: 255
0
proxy-inline-ips
Enable/disable proxy-mode policy inline IPS
support.
option
-disable **
Option
Description
disable
Do not allow inline IPS in proxy-mode policy.
enable
Allow inline IPS in proxy-mode policy.
FortiOS 8.0.0 CLI Reference
867
Fortinet Inc.

<!-- 来源页 868 -->
** Values may differ between models.
config ips view-map
Configure IPS view-map. Read-only.
config ips view-map
Description: Configure IPS view-map. Read-only.
edit <id>
set id-policy-id {integer}
set policy-id {integer}
set vdom-id {integer}
set which [firewall|interface|...]
next
end
config ips view-map
Parameter
Description
Type
Size
Default
id
View ID. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
id-policy-id
ID-based policy ID. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
policy-id
Policy ID. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
vdom-id
VDOM ID. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
which
Policy. Read-only.
option
-firewall
Option
Description
firewall
Firewall policy.
interface
Interface policy.
interface6
Interface policy6.
FortiOS 8.0.0 CLI Reference
868
Fortinet Inc.

<!-- 来源页 869 -->
Parameter
Description
Type
Size
Default
Option
Description
sniffer
Sniffer policy.
sniffer6
Sniffer policy6.
explicit
explicit proxy policy.
FortiOS 8.0.0 CLI Reference
869
Fortinet Inc.

---


<!-- 来源页 2317 -->
virtual-patch
This section includes syntax for the following commands:
l config virtual-patch profile on page 2317
config virtual-patch profile
Configure virtual-patch profile.
config virtual-patch profile
Description: Configure virtual-patch profile.
edit <name>
set action [pass|block]
set comment {var-string}
config exemption
Description: Exempt devices or rules.
edit <id>
set device <mac1>, <mac2>, ...
set rule <id1>, <id2>, ...
set status [enable|disable]
next
end
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set log [enable|disable]
set severity {option1}, {option2}, ...
set uuid {uuid}
next
end
config virtual-patch profile
Parameter
Description
Type
Size
Default
action
Action (pass/block).
option
-block
Option
Description
pass
Allows session that match the profile.
block
Blocks sessions that match the profile.
FortiOS 8.0.0 CLI Reference
2317
Fortinet Inc.

<!-- 来源页 2318 -->
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
log
Enable/disable logging of detection.
option
-enable
Option
Description
enable
Enable logging.
disable
Disable logging.
name
Profile name.
string
Maximum
length: 47
severity
Relative severity of the signature (low,
medium, high, critical).
option
-info low medium
high critical
FortiOS 8.0.0 CLI Reference
2318
Fortinet Inc.

<!-- 来源页 2319 -->
Parameter
Description
Type
Size
Default
Option
Description
info
info
low
low
medium
medium
high
high
critical
critical
uuid *
Universally Unique Identifier (UUID;
automatically assigned but can be manually
reset).
uuid
Not
Specified
00000000-0000-0000-0000-000000000000
* This parameter may not exist in some models.
config exemption
Parameter
Description
Type
Size
Default
device <mac>
Device MAC addresses.
Device MAC address.
mac-address
Not Specified
id
IDs.
integer
Minimum value:
0 Maximum
value:
4294967295
0
rule <id>
Patch signature rule IDs.
Rule IDs.
integer
Minimum value:
0 Maximum
value:
4294967295
status
Enable/disable exemption.
option
-enable
Option
Description
enable
Enable exemption.
disable
Disable exemption.
FortiOS 8.0.0 CLI Reference
2319
Fortinet Inc.
