# 运维命令 (execute)

> 来源: FortiOS-8.0.0-CLI_Reference.pdf
> 覆盖命令/章节: execute api-user, execute auto-script, execute auto-upgrade, execute azure, execute backup, execute batch, execute ble, execute bypass-mode, execute cellular-modem, execute central-mgmt, execute cfg, execute clear, execute clear-admin-password-history, execute clear-user-password-history, execute cli, execute cloud-service, execute config-transaction, execute cpu, execute date, execute device-upgrade, execute dhcp, execute dhcp6, execute digital-io, execute disconnect-admin-session, execute disk, execute ecnt-dsl, execute enter, execute erase-disk, execute ethernet, execute extender, execute fabric-vpn, execute factoryreset, execute factoryreset2, execute factoryreset-for-central-management, execute factoryreset-shutdown, execute fctems, execute federated-upgrade, execute fips, execute firewall, execute formatlogdisk, execute forticarrier-license, execute forticloud-sandbox, execute fortiguard-log, execute fortiguard-message, execute fortimanager, execute fortitoken, execute fortitoken-cloud, execute fortitoken-mobile, execute fsso, execute gen-token, execute ha, execute hscalefw-license, execute interface, execute internet-service, execute internet-service4, execute internet-service6, execute ipam, execute iscsi, execute kmip, execute log, execute lte-modem, execute mem, execute modem, execute mqtt, execute mrouter, execute mrouter6, execute nsx, execute oqs, execute ping, execute ping6, execute ping6-options, execute ping-options, execute policy-packet-capture, execute private-encryption-key, execute reboot, execute replace-device, execute report, execute report-config, execute restore, execute revision, execute router, execute sdn, execute sdn-vpn, execute send-fds-statistics, execute send-fmg-list, execute sensor, execute set, execute set-next-reboot, execute shutdown, execute speed-test, execute speed-test-custom, execute speed-test-ipsec, execute speed-test-legacy, execute speed-test-options, execute speed-test-server, execute ssh, execute ssh6, execute ssh6-options, execute ssh-options, execute ssh-regen-keys, execute switch-controller, execute sync-IPSec, execute sync-session, execute system, execute tac, execute telnet, execute telnet-options, execute test, execute time, execute traceroute, execute traceroute-options, execute tracert6, execute update-av, execute update-eip, execute update-external-resource, execute update-ffdb-on-demand, execute update-geo-ip, execute update-ips, execute update-now, execute update-sata-firmware, execute update-src-vis, execute upd-vd-license, execute upload, execute usb-device, execute usb-disk, execute vin, execute vm-license, execute vm-license-options, execute vpn, execute wake-on-lan, execute webcache, execute webfilter, execute wireless-controller
> 本文件由 extract_pdf.py 从官方 PDF 自动提取，请勿手动编辑；
> 如需修正请修改 map.json 后重跑脚本。

---


<!-- 来源页 4064 -->
CLI execute commands
l execute update-src-vis on page 4235
l execute upload on page 4235
l execute usb-device on page 4238
l execute usb-disk on page 4239
l execute vin on page 4240
l execute vm-license-options on page 4241
l execute vm-license on page 4241
l execute vpn on page 4243
l execute wake-on-lan on page 4257
l execute webcache on page 4257
l execute webfilter on page 4258
l execute wireless-controller on page 4259
execute api-user
api-user
This topic includes the following commands:
l execute api-user generate-key on page 4064
execute api-user generate-key
Generate key for API users.
execute api-user generate-key <name> <expiry>
Parameter
Description
Type
Size
<name>
API user name.
string
<expiry>
Expiry of API key in minutes from now (valid range: 1 -10080). This can only be set for Fortinet Support Tool user.
string
execute auto-script
auto-script
This topic includes the following commands:
l execute auto-script backup ftp on page 4065
l execute auto-script backup tftp on page 4065
FortiOS 8.0.0 CLI Reference
4064
Fortinet Inc.

---


<!-- 来源页 4064 -->
CLI execute commands
l execute update-src-vis on page 4235
l execute upload on page 4235
l execute usb-device on page 4238
l execute usb-disk on page 4239
l execute vin on page 4240
l execute vm-license-options on page 4241
l execute vm-license on page 4241
l execute vpn on page 4243
l execute wake-on-lan on page 4257
l execute webcache on page 4257
l execute webfilter on page 4258
l execute wireless-controller on page 4259
execute api-user
api-user
This topic includes the following commands:
l execute api-user generate-key on page 4064
execute api-user generate-key
Generate key for API users.
execute api-user generate-key <name> <expiry>
Parameter
Description
Type
Size
<name>
API user name.
string
<expiry>
Expiry of API key in minutes from now (valid range: 1 -10080). This can only be set for Fortinet Support Tool user.
string
execute auto-script
auto-script
This topic includes the following commands:
l execute auto-script backup ftp on page 4065
l execute auto-script backup tftp on page 4065
FortiOS 8.0.0 CLI Reference
4064
Fortinet Inc.

<!-- 来源页 4065 -->
CLI execute commands
l execute auto-script delete on page 4065
l execute auto-script result on page 4066
l execute auto-script start on page 4066
l execute auto-script status on page 4066
l execute auto-script stop on page 4066
l execute auto-script stopall on page 4066
execute auto-script backup ftp
Backup output file to FTP sever.
execute auto-script backup ftp <name> <ftp server>[:ftp port] <Enter>|<user> <passwd>
Parameter
Description
Type
Size
<name>
Script name.
string
<ftp server>[:ftp
port]
FTP server IPv4, IPv6, or FQDN can be attached with
port.
string
<Enter>|<user>
FTP username may be needed.
string
<passwd>
FTP password.
string
execute auto-script backup tftp
Backup output file to TFTP sever.
execute auto-script backup tftp <name> <tftp server>
Parameter
Description
Type
Size
<name>
Script name.
string
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
execute auto-script delete
Delete output of executed scripts.
execute auto-script delete <name>
Parameter
Description
Type
Size
<name>
Script name.
string
FortiOS 8.0.0 CLI Reference
4065
Fortinet Inc.

<!-- 来源页 4066 -->
CLI execute commands
execute auto-script result
Display output of executed scripts.
execute auto-script result <name>
Parameter
Description
Type
Size
<name>
Script name.
string
execute auto-script start
Start script.
execute auto-script start <name>
Parameter
Description
Type
Size
<name>
Script name.
string
execute auto-script status
List of scripts currently running or executed.
execute auto-script status
execute auto-script stop
Stop script.
execute auto-script stop <name>
Parameter
Description
Type
Size
<name>
Script name.
string
execute auto-script stopall
Stop all scripts currently running.
execute auto-script stopall
FortiOS 8.0.0 CLI Reference
4066
Fortinet Inc.

---


<!-- 来源页 4067 -->
CLI execute commands
execute auto-upgrade
auto-upgrade
This topic includes the following commands:
l execute auto-upgrade check-for-new-image on page 4067
l execute auto-upgrade delay-installation on page 4067
l execute auto-upgrade hasten-installation on page 4067
l execute auto-upgrade status on page 4067
execute auto-upgrade check-for-new-image
Manually trigger an auto-upgrade's new image check.
execute auto-upgrade check-for-new-image
execute auto-upgrade delay-installation
Delay auto-upgrade's current image installation by a week.
execute auto-upgrade delay-installation
execute auto-upgrade hasten-installation
Immediately trigger the scheduled image installation in auto-upgrade, ignoring system configurations.
execute auto-upgrade hasten-installation
execute auto-upgrade status
Display the current status of auto-upgrade.
execute auto-upgrade status
execute azure
azure
FortiOS 8.0.0 CLI Reference
4067
Fortinet Inc.

---


<!-- 来源页 4067 -->
CLI execute commands
execute auto-upgrade
auto-upgrade
This topic includes the following commands:
l execute auto-upgrade check-for-new-image on page 4067
l execute auto-upgrade delay-installation on page 4067
l execute auto-upgrade hasten-installation on page 4067
l execute auto-upgrade status on page 4067
execute auto-upgrade check-for-new-image
Manually trigger an auto-upgrade's new image check.
execute auto-upgrade check-for-new-image
execute auto-upgrade delay-installation
Delay auto-upgrade's current image installation by a week.
execute auto-upgrade delay-installation
execute auto-upgrade hasten-installation
Immediately trigger the scheduled image installation in auto-upgrade, ignoring system configurations.
execute auto-upgrade hasten-installation
execute auto-upgrade status
Display the current status of auto-upgrade.
execute auto-upgrade status
execute azure
azure
FortiOS 8.0.0 CLI Reference
4067
Fortinet Inc.

---


<!-- 来源页 4068 -->
CLI execute commands
This topic includes the following commands:
l execute azure vwan-payg-billing status on page 4068
l execute azure vwan-payg-billing usage on page 4068
l execute azure vwan-slb pull on page 4068
l execute azure vwan-slb show on page 4068
execute azure vwan-payg-billing status
Display vwan payg billing status.
execute azure vwan-payg-billing status
execute azure vwan-payg-billing usage
Display all usage events that have been posted.
execute azure vwan-payg-billing usage
execute azure vwan-slb pull
Pull the Azure vWAN SLB online setting to local cmdb.
execute azure vwan-slb pull
execute azure vwan-slb show
Display the Azure vWAN SLB online setting.
execute azure vwan-slb show
execute backup
backup
This topic includes the following commands:
l execute backup config flash on page 4069
l execute backup config ftp on page 4070
l execute backup config management-station on page 4070
FortiOS 8.0.0 CLI Reference
4068
Fortinet Inc.

<!-- 来源页 4069 -->
CLI execute commands
l execute backup config scp on page 4070
l execute backup config sftp on page 4071
l execute backup config tftp on page 4071
l execute backup config usb on page 4072
l execute backup config usb-mode on page 4072
l execute backup disk alllogs ftp on page 4072
l execute backup disk alllogs tftp on page 4072
l execute backup disk alllogs usb on page 4073
l execute backup disk ipsarchives ftp on page 4073
l execute backup disk ipsarchives tftp on page 4073
l execute backup disk ipsarchives usb on page 4073
l execute backup disk log ftp on page 4074
l execute backup disk log tftp on page 4074
l execute backup disk log usb on page 4074
l execute backup full-config ftp on page 4075
l execute backup full-config sftp on page 4075
l execute backup full-config tftp on page 4075
l execute backup full-config usb on page 4076
l execute backup full-config usb-mode on page 4076
l execute backup ipsuserdefsig ftp on page 4076
l execute backup ipsuserdefsig tftp on page 4077
l execute backup memory alllogs ftp on page 4077
l execute backup memory alllogs tftp on page 4077
l execute backup memory log ftp on page 4077
l execute backup memory log tftp on page 4078
l execute backup obfuscated-config ftp on page 4078
l execute backup obfuscated-config management-station on page 4079
l execute backup obfuscated-config sftp on page 4079
l execute backup obfuscated-config tftp on page 4079
l execute backup obfuscated-config usb on page 4079
l execute backup obfuscated-full-config ftp on page 4080
l execute backup obfuscated-full-config sftp on page 4080
l execute backup obfuscated-full-config tftp on page 4081
l execute backup obfuscated-full-config usb on page 4081
l execute backup obfuscated-yaml-config ftp on page 4081
l execute backup obfuscated-yaml-config tftp on page 4082
l execute backup yaml-config ftp on page 4082
l execute backup yaml-config tftp on page 4082
execute backup config flash
Backup config file to flash.
FortiOS 8.0.0 CLI Reference
4069
Fortinet Inc.

<!-- 来源页 4070 -->
CLI execute commands
execute backup config flash <comment>
Parameter
Description
Type
Size
<comment>
Make a comment for this config backup.
string
execute backup config ftp
Backup config file to FTP server.
execute backup config ftp <string> <ftp server>[:ftp port] <Enter>|<user> <passwd>
<Enter>|<passwd>
Parameter
Description
Type
Size
<string>
Make a file name (path) on the FTP server.
string
<ftp server>[:ftp
port]
FTP server IPv4, IPv6, or FQDN can be attached with
port.
string
<Enter>|<user>
FTP username may be needed.
string
<passwd>
FTP password.
string
<Enter>|<passwd>
Optional password to protect the backup content.
string
execute backup config management-station
Backup config file to management station.
execute backup config management-station <comment>
Parameter
Description
Type
Size
<comment>
Make a comment for this config backup.
string
execute backup config scp
Backup config file to a SCP server.
execute backup config scp <string> <scp server>[:scp port] <user> <passwd> <Enter>|<passwd>
Parameter
Description
Type
Size
<string>
Configure file name(path) on the remote scp server.
string
FortiOS 8.0.0 CLI Reference
4070
Fortinet Inc.

<!-- 来源页 4071 -->
CLI execute commands
Parameter
Description
Type
Size
<scp server>[:scp
port]
SCP server address (IPv4, [IPv6], or FQDN — port
optional) Supported formats: 192.0.2.1 (IPv4)
192.0.2.1:22 (IPv4 with port) 2001:db8::1 (Raw IPv6)
[2001:db8::1] (IPv6) [2001:db8::1]:22 (IPv6 with
port) host.example.com (FQDN, resolves to IPv4)
[host.example.com] (FQDN, resolves to IPv6)
[host.example.com]:22 (FQDN with port, resolves
to IPv6) * Use square brackets when specifying a
port with an IPv6 address or IPv6-resolving FQDN.
string
<user>
SCP username.
string
<passwd>
SCP password.
string
<Enter>|<passwd>
Password may be needed to restore/backup file.
string
execute backup config sftp
Backup config file to SFTP server.
execute backup config sftp <string> <sftp server>[:sftp port] <user> <passwd> <Enter>|<passwd>
Parameter
Description
Type
Size
<string>
Make a file name (path) on the SFTP server.
string
<sftp server>[:sftp
port]
SFTP server IPv4, IPv6 can be attached with port.
string
<user>
SFTP username.
string
<passwd>
SFTP password.
string
<Enter>|<passwd>
Optional password to protect the backup content.
string
execute backup config tftp
Backup config file to TFTP server.
execute backup config tftp <string> <tftp server> <Enter>|<passwd>
Parameter
Description
Type
Size
<string>
Make a file name (path) on the TFTP server.
string
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
<Enter>|<passwd>
Optional password to protect the backup content.
string
FortiOS 8.0.0 CLI Reference
4071
Fortinet Inc.

<!-- 来源页 4072 -->
CLI execute commands
execute backup config usb
Backup config file to USB disk.
execute backup config usb <string> <Enter>|<passwd>
Parameter
Description
Type
Size
<string>
Make a file name on the USB disk.
string
<Enter>|<passwd>
Optional password to protect the backup content.
string
execute backup config usb-mode
Backup config file for USB mode.
execute backup config usb-mode <Enter>|<passwd>
Parameter
Description
Type
Size
<Enter>|<passwd>
Optional password to protect the backup file.
string
execute backup disk alllogs ftp
Backup all log files to FTP server.
execute backup disk alllogs ftp <ftp server>[:ftp port] <Enter>|<user> <passwd> <Enter>|<string>
Parameter
Description
Type
Size
<ftp server>[:ftp
port]
FTP server IPv4, IPv6, or FQDN can be attached with
port.
string
<Enter>|<user>
FTP username may be needed.
string
<passwd>
FTP password.
string
<Enter>|<string>
Optional log file compression option
[uncompressed|compressed].
string
execute backup disk alllogs tftp
Backup all log file(s) to TFTP server.
execute backup disk alllogs tftp <tftp server>
FortiOS 8.0.0 CLI Reference
4072
Fortinet Inc.

<!-- 来源页 4073 -->
CLI execute commands
Parameter
Description
Type
Size
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
execute backup disk alllogs usb
Backup all log files to USB.
execute backup disk alllogs usb
execute backup disk ipsarchives ftp
Backup IPS archive file(s) to FTP server.
execute backup disk ipsarchives ftp <ftp server>[:ftp port] <Enter>|<user> <passwd>
Parameter
Description
Type
Size
<ftp server>[:ftp
port]
FTP server IPv4, IPv6, or FQDN can be attached with
port.
string
<Enter>|<user>
FTP username may be needed.
string
<passwd>
FTP password.
string
execute backup disk ipsarchives tftp
Backup IPS archive file(s) to TFTP server.
execute backup disk ipsarchives tftp <tftp server>
Parameter
Description
Type
Size
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
execute backup disk ipsarchives usb
Backup IPS archive file(s) to USB.
execute backup disk ipsarchives usb
FortiOS 8.0.0 CLI Reference
4073
Fortinet Inc.

<!-- 来源页 4074 -->
CLI execute commands
execute backup disk log ftp
Backup specific log file(s) to FTP server.
execute backup disk log ftp <ftp server>[:ftp port] <user> <passwd> <string> <Enter>|<string>
Parameter
Description
Type
Size
<ftp server>[:ftp
port]
FTP server IPv4, IPv6, or FQDN can be attached with
port.
string
<user>
FTP username.
string
<passwd>
FTP password.
string
<string>
, traffic, event, virus, webfilter, ips, emailfilter,
anomaly, voip, dlp, app-ctrl, waf, dns, ssh, ssl, file-filter, icap, sctp-filter, forti-switch, virtual-patch, casb,
debug, llm
string
<Enter>|<string>
Optional log file compression option
[uncompressed|compressed].
string
execute backup disk log tftp
Backup specific log file(s) to TFTP server.
execute backup disk log tftp <tftp server> <string>
Parameter
Description
Type
Size
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
<string>
, traffic, event, virus, webfilter, ips, emailfilter, anomaly,
voip, dlp, app-ctrl, waf, dns, ssh, ssl, file-filter, icap, sctp-filter, forti-switch, virtual-patch, casb, debug, llm
string
execute backup disk log usb
Backup specific log file(s) to USB.
execute backup disk log usb <string>
Parameter
Description
Type
Size
<string>
, traffic, event, virus, webfilter, ips, emailfilter, anomaly,
voip, dlp, app-ctrl, waf, dns, ssh, ssl, file-filter, icap, sctp-filter, forti-switch, virtual-patch, casb, debug, llm
string
FortiOS 8.0.0 CLI Reference
4074
Fortinet Inc.

<!-- 来源页 4075 -->
CLI execute commands
execute backup full-config ftp
Backup full config file to FTP server.
execute backup full-config ftp <string> <ftp server>[:ftp port] <Enter>|<user> <passwd>
<Enter>|<passwd>
Parameter
Description
Type
Size
<string>
Make a file name (path) on the FTP server.
string
<ftp server>[:ftp
port]
FTP server IPv4, IPv6, or FQDN can be attached with
port.
string
<Enter>|<user>
FTP username may be needed.
string
<passwd>
FTP password.
string
<Enter>|<passwd>
Optional password to protect the backup content.
string
execute backup full-config sftp
Backup full config file to SFTP server.
execute backup full-config sftp <string> <sftp server>[:sftp port] <user> <passwd>
<Enter>|<passwd>
Parameter
Description
Type
Size
<string>
Make a file name (path) on the SFTP server.
string
<sftp server>[:sftp
port]
SFTP server IPv4, IPv6 can be attached with port.
string
<user>
SFTP username.
string
<passwd>
SFTP password.
string
<Enter>|<passwd>
Optional password to protect the backup content.
string
execute backup full-config tftp
Backup full config file to TFTP server.
execute backup full-config tftp <string> <tftp server> <Enter>|<passwd>
Parameter
Description
Type
Size
<string>
Make a file name (path) on the TFTP server.
string
FortiOS 8.0.0 CLI Reference
4075
Fortinet Inc.

<!-- 来源页 4076 -->
CLI execute commands
Parameter
Description
Type
Size
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
<Enter>|<passwd>
Optional password to protect the backup content.
string
execute backup full-config usb
Backup full config file to USB disk.
execute backup full-config usb <string> <Enter>|<passwd>
Parameter
Description
Type
Size
<string>
Make a file name on the USB disk.
string
<Enter>|<passwd>
Optional password to protect the backup content.
string
execute backup full-config usb-mode
Backup full config file for USB mode.
execute backup full-config usb-mode <Enter>|<passwd>
Parameter
Description
Type
Size
<Enter>|<passwd>
Optional password to protect the backup file.
string
execute backup ipsuserdefsig ftp
Backup user defined IPS signatures to FTP server.
execute backup ipsuserdefsig ftp <string> <ftp server>[:ftp port] <Enter>|<user> <passwd>
Parameter
Description
Type
Size
<string>
Make a file name (path) on the FTP server.
string
<ftp server>[:ftp
port]
FTP server IPv4, IPv6, or FQDN can be attached with
port.
string
<Enter>|<user>
FTP username may be needed.
string
<passwd>
FTP password.
string
FortiOS 8.0.0 CLI Reference
4076
Fortinet Inc.

<!-- 来源页 4077 -->
CLI execute commands
execute backup ipsuserdefsig tftp
Backup user defined IPS signatures to TFTP server.
execute backup ipsuserdefsig tftp <string> <tftp server>
Parameter
Description
Type
Size
<string>
Make a file name (path) on the TFTP server.
string
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
execute backup memory alllogs ftp
Backup all log files to FTP server.
execute backup memory alllogs ftp <ftp server>[:ftp port] <Enter>|<user> <passwd>
Parameter
Description
Type
Size
<ftp server>[:ftp
port]
FTP server IPv4, IPv6, or FQDN can be attached with
port.
string
<Enter>|<user>
FTP username may be needed.
string
<passwd>
FTP password.
string
execute backup memory alllogs tftp
Backup all log file(s) to TFTP server.
execute backup memory alllogs tftp <tftp server>
Parameter
Description
Type
Size
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
execute backup memory log ftp
Backup specific log file(s) to FTP server.
execute backup memory log ftp <ftp server>[:ftp port] <user> <passwd> <string>
FortiOS 8.0.0 CLI Reference
4077
Fortinet Inc.

<!-- 来源页 4078 -->
CLI execute commands
Parameter
Description
Type
Size
<ftp server>
[:ftp port]
FTP server IPv4, IPv6, or FQDN can be attached with port.
string
<user>
FTP username.
string
<passwd>
FTP password.
string
<string>
, traffic, event, virus, webfilter, ips, emailfilter, anomaly,
voip, dlp, app-ctrl, waf, dns, ssh, ssl, file-filter, icap, sctp-filter, forti-switch, virtual-patch, casb, debug, llm
string
execute backup memory log tftp
Backup specific log file(s) to TFTP server.
execute backup memory log tftp <tftp server> <string>
Parameter
Description
Type
Size
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
<string>
, traffic, event, virus, webfilter, ips, emailfilter, anomaly,
voip, dlp, app-ctrl, waf, dns, ssh, ssl, file-filter, icap, sctp-filter, forti-switch, virtual-patch, casb, debug, llm
string
execute backup obfuscated-config ftp
Backup obfuscated config file to FTP server.
execute backup obfuscated-config ftp <string> <ftp server>[:ftp port] <Enter>|<user> <passwd>
<Enter>|<passwd>
Parameter
Description
Type
Size
<string>
Make a file name (path) on the FTP server.
string
<ftp server>[:ftp
port]
FTP server IPv4, IPv6, or FQDN can be attached with
port.
string
<Enter>|<user>
FTP username may be needed.
string
<passwd>
FTP password.
string
<Enter>|<passwd>
Optional password to protect the backup content.
string
FortiOS 8.0.0 CLI Reference
4078
Fortinet Inc.

<!-- 来源页 4079 -->
CLI execute commands
execute backup obfuscated-config management-station
Backup obfuscated config file to management station.
execute backup obfuscated-config management-station <comment>
Parameter
Description
Type
Size
<comment>
Make a comment for this config backup.
string
execute backup obfuscated-config sftp
Backup obfuscated config file to SFTP server.
execute backup obfuscated-config sftp <string> <sftp server>[:sftp port] <user> <passwd>
<Enter>|<passwd>
Parameter
Description
Type
Size
<string>
Make a file name (path) on the SFTP server.
string
<sftp server>[:sftp
port]
SFTP server IPv4, IPv6 can be attached with port.
string
<user>
SFTP username.
string
<passwd>
SFTP password.
string
<Enter>|<passwd>
Optional password to protect the backup content.
string
execute backup obfuscated-config tftp
Backup obfuscated config file to TFTP server.
execute backup obfuscated-config tftp <string> <tftp server> <Enter>|<passwd>
Parameter
Description
Type
Size
<string>
Make a file name (path) on the TFTP server.
string
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
<Enter>|<passwd>
Optional password to protect the backup content.
string
execute backup obfuscated-config usb
Backup obfuscated config file to USB disk.
FortiOS 8.0.0 CLI Reference
4079
Fortinet Inc.

<!-- 来源页 4080 -->
CLI execute commands
execute backup obfuscated-config usb <string> <Enter>|<passwd>
Parameter
Description
Type
Size
<string>
Make a file name on the USB disk.
string
<Enter>|<passwd>
Optional password to protect the backup content.
string
execute backup obfuscated-full-config ftp
Backup obfuscated full config file to FTP server.
execute backup obfuscated-full-config ftp <string> <ftp server>[:ftp port] <Enter>|<user> <passwd>
<Enter>|<passwd>
Parameter
Description
Type
Size
<string>
Make a file name (path) on the FTP server.
string
<ftp server>[:ftp
port]
FTP server IPv4, IPv6, or FQDN can be attached with
port.
string
<Enter>|<user>
FTP username may be needed.
string
<passwd>
FTP password.
string
<Enter>|<passwd>
Optional password to protect the backup content.
string
execute backup obfuscated-full-config sftp
Backup obfuscated full config file to SFTP server.
execute backup obfuscated-full-config sftp <string> <sftp server>[:sftp port] <user> <passwd>
<Enter>|<passwd>
Parameter
Description
Type
Size
<string>
Make a file name (path) on the SFTP server.
string
<sftp server>[:sftp
port]
SFTP server IPv4, IPv6 can be attached with port.
string
<user>
SFTP username.
string
<passwd>
SFTP password.
string
<Enter>|<passwd>
Optional password to protect the backup content.
string
FortiOS 8.0.0 CLI Reference
4080
Fortinet Inc.

<!-- 来源页 4081 -->
CLI execute commands
execute backup obfuscated-full-config tftp
Backup obfuscated full config file to TFTP server.
execute backup obfuscated-full-config tftp <string> <tftp server> <Enter>|<passwd>
Parameter
Description
Type
Size
<string>
Make a file name (path) on the TFTP server.
string
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
<Enter>|<passwd>
Optional password to protect the backup content.
string
execute backup obfuscated-full-config usb
Backup obfuscated full config file to USB disk.
execute backup obfuscated-full-config usb <string> <Enter>|<passwd>
Parameter
Description
Type
Size
<string>
Make a file name on the USB disk.
string
<Enter>|<passwd>
Optional password to protect the backup content.
string
execute backup obfuscated-yaml-config ftp
Backup obfuscated YAML config file to FTP server.
execute backup obfuscated-yaml-config ftp <string> <ftp server>[:ftp port] <Enter>|<user> <passwd>
<Enter>|<passwd>
Parameter
Description
Type
Size
<string>
Make a file name (path) on the FTP server.
string
<ftp server>[:ftp
port]
FTP server IPv4, IPv6, or FQDN can be attached with
port.
string
<Enter>|<user>
FTP username may be needed.
string
<passwd>
FTP password.
string
<Enter>|<passwd>
Optional password to protect the backup content.
string
FortiOS 8.0.0 CLI Reference
4081
Fortinet Inc.

<!-- 来源页 4082 -->
CLI execute commands
execute backup obfuscated-yaml-config tftp
Backup obfuscated YAML config file to TFTP server.
execute backup obfuscated-yaml-config tftp <string> <tftp server> <Enter>|<passwd>
Parameter
Description
Type
Size
<string>
Make a file name (path) on the TFTP server.
string
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
<Enter>|<passwd>
Optional password to protect the backup content.
string
execute backup yaml-config ftp
Backup YAML config file to FTP server.
execute backup yaml-config ftp <string> <ftp server>[:ftp port] <Enter>|<user> <passwd>
<Enter>|<passwd>
Parameter
Description
Type
Size
<string>
Make a file name (path) on the FTP server.
string
<ftp server>[:ftp
port]
FTP server IPv4, IPv6, or FQDN can be attached with
port.
string
<Enter>|<user>
FTP username may be needed.
string
<passwd>
FTP password.
string
<Enter>|<passwd>
Optional password to protect the backup content.
string
execute backup yaml-config tftp
Backup YAML config file to TFTP server.
execute backup yaml-config tftp <string> <tftp server> <Enter>|<passwd>
Parameter
Description
Type
Size
<string>
Make a file name (path) on the TFTP server.
string
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
<Enter>|<passwd>
Optional password to protect the backup content.
string
FortiOS 8.0.0 CLI Reference
4082
Fortinet Inc.

---


<!-- 来源页 4083 -->
CLI execute commands
execute batch
batch
This topic includes the following commands:
l execute batch end on page 4083
l execute batch lastlog on page 4083
l execute batch start on page 4083
l execute batch status on page 4083
execute batch end
Batch mode end.
execute batch end
execute batch lastlog
Read the result of last batch commands.
execute batch lastlog
execute batch start
Batch mode start.
execute batch start
execute batch status
Batch mode status.
execute batch status
execute ble
ble
FortiOS 8.0.0 CLI Reference
4083
Fortinet Inc.

---


<!-- 来源页 4083 -->
CLI execute commands
execute batch
batch
This topic includes the following commands:
l execute batch end on page 4083
l execute batch lastlog on page 4083
l execute batch start on page 4083
l execute batch status on page 4083
execute batch end
Batch mode end.
execute batch end
execute batch lastlog
Read the result of last batch commands.
execute batch lastlog
execute batch start
Batch mode start.
execute batch start
execute batch status
Batch mode status.
execute batch status
execute ble
ble
FortiOS 8.0.0 CLI Reference
4083
Fortinet Inc.

<!-- 来源页 4084 -->
CLI execute commands
This topic includes the following commands:
l execute ble check_default on page 4084
l execute ble check_password on page 4084
l execute ble check_registration on page 4084
l execute ble check_tp on page 4085
l execute ble check_upgrade on page 4085
l execute ble dhcp on page 4085
l execute ble hostname on page 4085
l execute ble image on page 4085
l execute ble interface on page 4086
l execute ble ip on page 4086
l execute ble matrix on page 4086
l execute ble model on page 4086
l execute ble ping on page 4086
l execute ble pppoe on page 4087
l execute ble register on page 4087
l execute ble serial on page 4087
l execute ble shutdown on page 4087
l execute ble static on page 4088
l execute ble type on page 4088
l execute ble upgrade on page 4088
l execute ble version on page 4088
execute ble check_default
Check If Factory Reset State.
execute ble check_default
execute ble check_password
Check If Pasword set.
execute ble check_password
execute ble check_registration
Check device FortiCare registeratin status.
execute ble check_registration
FortiOS 8.0.0 CLI Reference
4084
Fortinet Inc.

<!-- 来源页 4085 -->
CLI execute commands
execute ble check_tp
Check If Unit is in Transparent Mode.
execute ble check_tp
execute ble check_upgrade
Check If Upgrade Available.
execute ble check_upgrade <patch>
Parameter
Description
Type
Size
<patch>
start build patch.
string
execute ble dhcp
Interface External DHCP client mode.
execute ble dhcp <interface>
Parameter
Description
Type
Size
<interface>
Network interface to be configured.
string
execute ble hostname
Get or Set System Hostname.
execute ble hostname <name>
Parameter
Description
Type
Size
<name>
Host Name.
string
execute ble image
Download image list.
execute ble image <patch>
FortiOS 8.0.0 CLI Reference
4085
Fortinet Inc.

<!-- 来源页 4086 -->
CLI execute commands
Parameter
Description
Type
Size
<patch>
start build patch.
string
execute ble interface
List Management Interfaces.
execute ble interface
execute ble ip
Get Interface IP Address.
execute ble ip <interface>
Parameter
Description
Type
Size
<interface>
Wan Interface.
string
execute ble matrix
Download Upgrade Matrix.
execute ble matrix <patch>
Parameter
Description
Type
Size
<patch>
start build patch.
string
execute ble model
Get System Model.
execute ble model
execute ble ping
Ping IP Address or Domain Name.
execute ble ping <ip>
FortiOS 8.0.0 CLI Reference
4086
Fortinet Inc.

<!-- 来源页 4087 -->
CLI execute commands
Parameter
Description
Type
Size
<ip>
IP address
string
execute ble pppoe
Interface Static Setting.
execute ble pppoe <interface> <username> <password>
Parameter
Description
Type
Size
<interface>
Network interface to be configured.
string
<username>
Username of the PPPoE account, provided by your ISP.
string
<password>
Please input password value.
string
execute ble register
Register FortiGate.
execute ble register <email> <password> <reseller-id> <reseller>
Parameter
Description
Type
Size
<email>
Email Address.
string
<password>
Password of FortiCare Account.
string
<reseller-id>
Reseller Id.
string
<reseller>
Reseller.
string
execute ble serial
Get System Serial Number.
execute ble serial
execute ble shutdown
Shutdown Bluetooth.
execute ble shutdown
FortiOS 8.0.0 CLI Reference
4087
Fortinet Inc.

---


<!-- 来源页 4088 -->
CLI execute commands
execute ble static
Interface Static Setting.
execute ble static <interface> <class_ip> <net_netmask> <gateway_ip>
Parameter
Description
Type
Size
<interface>
Network interface to be configured.
string
<class_ip>
IP address (syntax = 192.168.11.1).
string
<net_
netmask>
subnet mask (syntax = 255.255.255.0).
string
<gateway_ip>
Gateway IP address (syntax = 192.168.11.99).
string
execute ble type
Get Device Type.
execute ble type
execute ble upgrade
Upgrade Firmware.
execute ble upgrade <version>
Parameter
Description
Type
Size
<version>
Firmware Version.
string
execute ble version
Get OS Version.
execute ble version
execute bypass-mode
bypass-mode
FortiOS 8.0.0 CLI Reference
4088
Fortinet Inc.

---


<!-- 来源页 4089 -->
CLI execute commands
This topic includes the following commands:
l execute bypass-mode disable on page 4089
l execute bypass-mode enable on page 4089
execute bypass-mode disable
disable bypass
execute bypass-mode disable <index>
Parameter
Description
Type
Size
<index>
Bypass pair index (1-16), or all
string
execute bypass-mode enable
enable bypass
execute bypass-mode enable <index>
Parameter
Description
Type
Size
<index>
Bypass pair index (1-16), or all
string
execute cellular-modem
cellular-modem
This topic includes the following commands:
l execute cellular-modem carrier-config list on page 4090
l execute cellular-modem carrier-config switch on page 4090
l execute cellular-modem cold-reboot on page 4090
l execute cellular-modem firmware-upgrade ftp on page 4090
l execute cellular-modem firmware-upgrade management-station on page 4091
l execute cellular-modem firmware-upgrade tftp on page 4091
l execute cellular-modem firmware-upgrade usb on page 4091
l execute cellular-modem reboot on page 4091
l execute cellular-modem sim-switch on page 4091
FortiOS 8.0.0 CLI Reference
4089
Fortinet Inc.

<!-- 来源页 4090 -->
CLI execute commands
execute cellular-modem carrier-config list
List all cerrier config for modem.
execute cellular-modem carrier-config list
execute cellular-modem carrier-config switch
Perform carrier config switch for modem.
execute cellular-modem carrier-config switch <carrier config index>
Parameter
Description
Type
Size
<carrier
config index>
carrier config index to switch to.
string
execute cellular-modem cold-reboot
Cold reboot cellular modem.
execute cellular-modem cold-reboot
execute cellular-modem firmware-upgrade ftp
Load image from FTP server.
execute cellular-modem firmware-upgrade ftp <string> <ftp server>[:ftp port] <Enter>|<user>
<passwd>
Parameter
Description
Type
Size
<string>
Image file name(path) on the remote server.
string
<ftp server>[:ftp
port]
FTP server IPv4, IPv6, or FQDN can be attached with
port.
string
<Enter>|<user>
FTP username may be needed.
string
<passwd>
FTP password.
string
FortiOS 8.0.0 CLI Reference
4090
Fortinet Inc.

<!-- 来源页 4091 -->
CLI execute commands
execute cellular-modem firmware-upgrade management-station
Restore image from Management station.
execute cellular-modem firmware-upgrade management-station <string>
Parameter
Description
Type
Size
<string>
firmware <version_id>.
string
execute cellular-modem firmware-upgrade tftp
Restore image from TFTP server.
execute cellular-modem firmware-upgrade tftp <string> <tftp server>
Parameter
Description
Type
Size
<string>
Image file name on the TFTP server.
string
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
execute cellular-modem firmware-upgrade usb
Restore image from USB disk.
execute cellular-modem firmware-upgrade usb <string>
Parameter
Description
Type
Size
<string>
Image file name on the USB disk.
string
execute cellular-modem reboot
Warm reboot cellular modem.
execute cellular-modem reboot
execute cellular-modem sim-switch
Perform SIM switch for modem.
FortiOS 8.0.0 CLI Reference
4091
Fortinet Inc.

---


<!-- 来源页 4092 -->
CLI execute commands
execute cellular-modem sim-switch
execute central-mgmt
central-mgmt
This topic includes the following commands:
l execute central-mgmt register-device on page 4092
l execute central-mgmt register-device-by-address on page 4092
l execute central-mgmt register-device-by-ip on page 4093
l execute central-mgmt set-mgmt-id on page 4093
l execute central-mgmt unregister-device on page 4093
execute central-mgmt register-device
Register device to FortiManager from unregistered device list.
execute central-mgmt register-device <fmg-serial-no> <fmg-register-password>
Parameter
Description
Type
Size
<fmg-serial-no>
FortiManager serial number.
string
<fmg-register-password>
Register password in to FortiManager.
string
execute central-mgmt register-device-by-address
Register device to FortiManager with token
execute central-mgmt register-device-by-address <fmg-address> <fmg-access-token> <proxy>
Parameter
Description
Type
Size
<fmg-address>
FortiManager address.
string
<fmg-access-token>
Access token
string
<proxy>
(optional)proxy
string
FortiOS 8.0.0 CLI Reference
4092
Fortinet Inc.

---


<!-- 来源页 4093 -->
CLI execute commands
execute central-mgmt register-device-by-ip
Register device to FortiManager with token
execute central-mgmt register-device-by-ip <fmg-ip> <fmg-access-token> <proxy>
Parameter
Description
Type
Size
<fmg-ip>
FortiManager IP address.
string
<fmg-access-token>
Access token
string
<proxy>
(optional)proxy
string
execute central-mgmt set-mgmt-id
Management ID of Central Management Service.
execute central-mgmt set-mgmt-id <management id>
Parameter
Description
Type
Size
<management
id>
Management ID (must be entered in encrypted format).
string
execute central-mgmt unregister-device
Remove device from its manager's device list.
execute central-mgmt unregister-device <fmg-serial-no>
Parameter
Description
Type
Size
<fmg-serial-no>
FortiManager serial number.
string
execute cfg
cfg
This topic includes the following commands:
FortiOS 8.0.0 CLI Reference
4093
Fortinet Inc.

---


<!-- 来源页 4094 -->
CLI execute commands
l execute cfg reload on page 4094
l execute cfg save on page 4094
execute cfg reload
Reboot to reload the configs.
execute cfg reload
execute cfg save
Save configs.
execute cfg save
execute clear
clear
This topic includes the following commands:
l execute clear system arp table on page 4094
execute clear system arp table
Clear system ARP table.
execute clear system arp table
execute clear-admin-password-history
Clear admin user password history.
execute clear-admin-password-history <admin user>
Parameter
Description
Type
Size
<admin user>
Name of admin user
string
FortiOS 8.0.0 CLI Reference
4094
Fortinet Inc.

---


<!-- 来源页 4094 -->
CLI execute commands
l execute cfg reload on page 4094
l execute cfg save on page 4094
execute cfg reload
Reboot to reload the configs.
execute cfg reload
execute cfg save
Save configs.
execute cfg save
execute clear
clear
This topic includes the following commands:
l execute clear system arp table on page 4094
execute clear system arp table
Clear system ARP table.
execute clear system arp table
execute clear-admin-password-history
Clear admin user password history.
execute clear-admin-password-history <admin user>
Parameter
Description
Type
Size
<admin user>
Name of admin user
string
FortiOS 8.0.0 CLI Reference
4094
Fortinet Inc.

---


<!-- 来源页 4095 -->
CLI execute commands
execute clear-user-password-history
Clear auth user password history.
execute clear-user-password-history <auth user>
Parameter
Description
Type
Size
<auth user>
Name of auth user
string
execute cli
cli
This topic includes the following commands:
l execute cli check-template-status on page 4095
l execute cli status-msg-only on page 4095
execute cli check-template-status
Check SCP script template running status.
execute cli check-template-status
execute cli status-msg-only
CLI standardized error output.
execute cli status-msg-only <enable/disable>
Parameter
Description
Type
Size
<enable/disable>
Enable/disable CLI standardized error output.
string
execute cloud-service
cloud-service
This topic includes the following commands:
FortiOS 8.0.0 CLI Reference
4095
Fortinet Inc.

---


<!-- 来源页 4095 -->
CLI execute commands
execute clear-user-password-history
Clear auth user password history.
execute clear-user-password-history <auth user>
Parameter
Description
Type
Size
<auth user>
Name of auth user
string
execute cli
cli
This topic includes the following commands:
l execute cli check-template-status on page 4095
l execute cli status-msg-only on page 4095
execute cli check-template-status
Check SCP script template running status.
execute cli check-template-status
execute cli status-msg-only
CLI standardized error output.
execute cli status-msg-only <enable/disable>
Parameter
Description
Type
Size
<enable/disable>
Enable/disable CLI standardized error output.
string
execute cloud-service
cloud-service
This topic includes the following commands:
FortiOS 8.0.0 CLI Reference
4095
Fortinet Inc.

---


<!-- 来源页 4095 -->
CLI execute commands
execute clear-user-password-history
Clear auth user password history.
execute clear-user-password-history <auth user>
Parameter
Description
Type
Size
<auth user>
Name of auth user
string
execute cli
cli
This topic includes the following commands:
l execute cli check-template-status on page 4095
l execute cli status-msg-only on page 4095
execute cli check-template-status
Check SCP script template running status.
execute cli check-template-status
execute cli status-msg-only
CLI standardized error output.
execute cli status-msg-only <enable/disable>
Parameter
Description
Type
Size
<enable/disable>
Enable/disable CLI standardized error output.
string
execute cloud-service
cloud-service
This topic includes the following commands:
FortiOS 8.0.0 CLI Reference
4095
Fortinet Inc.

<!-- 来源页 4096 -->
CLI execute commands
l execute cloud-service gen-jwt-as-token on page 4096
l execute cloud-service list on page 4096
l execute cloud-service manual-gen-jwt-as-token on page 4096
execute cloud-service gen-jwt-as-token
Generate a JSON Web Token from config to be used as bearer token.
execute cloud-service gen-jwt-as-token <string>
Parameter
Description
Type
Size
<string>
Cloud service name.
string
execute cloud-service list
List cloud service information.
execute cloud-service list <string>
Parameter
Description
Type
Size
<string>
Cloud service name.
string
execute cloud-service manual-gen-jwt-as-token
Manually generate a JSON Web Token to be used as bearer token.
execute cloud-service manual-gen-jwt-as-token <string> <string> <string> <string> <integer>
<integer>
Parameter
Description
Type
Size
<string>
keyid.
string
<string>
private key in clear text, consider quoting everything in `"`,
as `\n` needs to be transcoded as a real new line.
string
<string>
issuer.
string
<string>
subject.
string
<integer>
token in effective starting from (epoch seconds).
string
<integer>
token lifetime (seconds).
string
FortiOS 8.0.0 CLI Reference
4096
Fortinet Inc.

---


<!-- 来源页 4097 -->
CLI execute commands
execute config-transaction
config-transaction
This topic includes the following commands:
l execute config-transaction abort on page 4097
l execute config-transaction commit on page 4097
l execute config-transaction resume on page 4097
l execute config-transaction start on page 4097
execute config-transaction abort
Abort configuration transaction.
execute config-transaction abort
execute config-transaction commit
Commit configuration transaction.
execute config-transaction commit
execute config-transaction resume
Resume configuration transaction.
execute config-transaction resume <integer>
Parameter
Description
Type
Size
<integer>
Transaction ID
string
execute config-transaction start
Start configuration transaction.
execute config-transaction start <integer>
Parameter
Description
Type
Size
<integer>
Transaction timeout in minutes (1 - 60). Default value is 5.
string
FortiOS 8.0.0 CLI Reference
4097
Fortinet Inc.

---


<!-- 来源页 4098 -->
CLI execute commands
execute cpu
cpu
This topic includes the following commands:
l execute cpu add on page 4098
l execute cpu show on page 4098
execute cpu add
Activate new CPU.
execute cpu add <number>
Parameter
Description
Type
Size
<number>
New Active CPU Number.
string
execute cpu show
Show CPU number.
execute cpu show
execute date
System date.
execute date <yyyy-mm-dd>
Parameter
Description
Type
Size
<yyyy-mm-dd>
yyyy: 2001-2037, mm: 1-12, dd: 1-31.
string
execute device-upgrade
device-upgrade
FortiOS 8.0.0 CLI Reference
4098
Fortinet Inc.

---


<!-- 来源页 4098 -->
CLI execute commands
execute cpu
cpu
This topic includes the following commands:
l execute cpu add on page 4098
l execute cpu show on page 4098
execute cpu add
Activate new CPU.
execute cpu add <number>
Parameter
Description
Type
Size
<number>
New Active CPU Number.
string
execute cpu show
Show CPU number.
execute cpu show
execute date
System date.
execute date <yyyy-mm-dd>
Parameter
Description
Type
Size
<yyyy-mm-dd>
yyyy: 2001-2037, mm: 1-12, dd: 1-31.
string
execute device-upgrade
device-upgrade
FortiOS 8.0.0 CLI Reference
4098
Fortinet Inc.

---


<!-- 来源页 4098 -->
CLI execute commands
execute cpu
cpu
This topic includes the following commands:
l execute cpu add on page 4098
l execute cpu show on page 4098
execute cpu add
Activate new CPU.
execute cpu add <number>
Parameter
Description
Type
Size
<number>
New Active CPU Number.
string
execute cpu show
Show CPU number.
execute cpu show
execute date
System date.
execute date <yyyy-mm-dd>
Parameter
Description
Type
Size
<yyyy-mm-dd>
yyyy: 2001-2037, mm: 1-12, dd: 1-31.
string
execute device-upgrade
device-upgrade
FortiOS 8.0.0 CLI Reference
4098
Fortinet Inc.

---


<!-- 来源页 4099 -->
CLI execute commands
This topic includes the following commands:
l execute device-upgrade cancel on page 4099
l execute device-upgrade immediate on page 4099
execute device-upgrade cancel
Cancel a Fortinet device's upgrade by removing it from the upgrade table.
execute device-upgrade cancel <serial>
Parameter
Description
Type
Size
<serial>
Serial number of the Fortinet device to upgrade.
string
execute device-upgrade immediate
Configure a Fortinet device to upgrade immediately.
execute device-upgrade immediate <device-type> <serial> <major> <minor> <patch>
Parameter
Description
Type
Size
<device-type>
Fortinet device type to upgrade.
string
<serial>
Fortinet device serial number to upgrade.
string
<major>
Major version of the Fortinet OS image being upgraded to.
string
<minor>
Minor version of the Fortinet OS image being upgraded to.
string
<patch>
Patch version of the Fortinet OS image being upgraded to.
string
execute dhcp
dhcp
This topic includes the following commands:
l execute dhcp lease-clear on page 4100
l execute dhcp lease-list on page 4100
FortiOS 8.0.0 CLI Reference
4099
Fortinet Inc.

---


<!-- 来源页 4100 -->
CLI execute commands
execute dhcp lease-clear
Clear all DHCP leases.
execute dhcp lease-clear <IPv4 address> or <IPv4 starting address-IPv4 ending address> <all>
Parameter
Description
Type
Size
<IPv4
address> or
<IPv4 starting
address-IPv4
ending
address>
Clear lease(s) on this IP address.
string
<all>
Clear all leases.
string
execute dhcp lease-list
List all DHCP leases.
execute dhcp lease-list <interface>
Parameter
Description
Type
Size
<interface>
List leases on this interface.
string
execute dhcp6
dhcp6
This topic includes the following commands:
l execute dhcp6 lease-clear on page 4100
l execute dhcp6 lease-list on page 4101
execute dhcp6 lease-clear
Clear all DHCPv6 leases.
execute dhcp6 lease-clear <IPv6 address> or <IPv6 starting address-IPv6 ending address>
<all>
FortiOS 8.0.0 CLI Reference
4100
Fortinet Inc.

---


<!-- 来源页 4101 -->
CLI execute commands
Parameter
Description
Type
Size
<IPv6
address> or
<IPv6 starting
address-IPv6
ending
address>
Clear lease(s) on this IPv6 address.
string
<all>
Clear all leases.
string
execute dhcp6 lease-list
List all DHCPv6 leases.
execute dhcp6 lease-list <interface>
Parameter
Description
Type
Size
<interface>
List leases on this interface.
string
execute digital-io
digital-io
This topic includes the following commands:
l execute digital-io set-output alternating on page 4101
l execute digital-io set-output default on page 4101
l execute digital-io set-output opposite on page 4102
execute digital-io set-output alternating
alternates between "default" and "opposite"
execute digital-io set-output alternating
execute digital-io set-output default
NC_COM=closed & NO_COM=open
execute digital-io set-output default
FortiOS 8.0.0 CLI Reference
4101
Fortinet Inc.

---


<!-- 来源页 4102 -->
CLI execute commands
execute digital-io set-output opposite
NC_COM=open & NO_COM=closed
execute digital-io set-output opposite
execute disconnect-admin-session
Disconnect logged-in admin user.
execute disconnect-admin-session <integer>
Parameter
Description
Type
Size
<integer>
Index of user to be disconnected in logged-users table.
string
execute disk
disk
This topic includes the following commands:
l execute disk format on page 4102
l execute disk list on page 4103
l execute disk raid disable on page 4103
l execute disk raid enable on page 4103
l execute disk raid rebuild on page 4103
l execute disk raid rebuild-level on page 4103
l execute disk raid status on page 4104
l execute disk scan on page 4104
execute disk format
Format a partition.
execute disk format
FortiOS 8.0.0 CLI Reference
4102
Fortinet Inc.

---


<!-- 来源页 4102 -->
CLI execute commands
execute digital-io set-output opposite
NC_COM=open & NO_COM=closed
execute digital-io set-output opposite
execute disconnect-admin-session
Disconnect logged-in admin user.
execute disconnect-admin-session <integer>
Parameter
Description
Type
Size
<integer>
Index of user to be disconnected in logged-users table.
string
execute disk
disk
This topic includes the following commands:
l execute disk format on page 4102
l execute disk list on page 4103
l execute disk raid disable on page 4103
l execute disk raid enable on page 4103
l execute disk raid rebuild on page 4103
l execute disk raid rebuild-level on page 4103
l execute disk raid status on page 4104
l execute disk scan on page 4104
execute disk format
Format a partition.
execute disk format
FortiOS 8.0.0 CLI Reference
4102
Fortinet Inc.

<!-- 来源页 4103 -->
CLI execute commands
execute disk list
List disk devices and partitions.
execute disk list
execute disk raid disable
disable RAID
execute disk raid disable
execute disk raid enable
enable RAID
execute disk raid enable <RAID level>
Parameter
Description
Type
Size
<RAID level>
supported: Raid-0, Raid-1 (default: Raid-0)
string
execute disk raid rebuild
rebuild RAID
execute disk raid rebuild
execute disk raid rebuild-level
rebuild RAID with new level
execute disk raid rebuild-level <RAID level>
Parameter
Description
Type
Size
<RAID level>
supported: Raid-0, Raid-1
string
FortiOS 8.0.0 CLI Reference
4103
Fortinet Inc.

---


<!-- 来源页 4104 -->
CLI execute commands
execute disk raid status
show RAID status
execute disk raid status
execute disk scan
Scan a partition and fix errors.
execute disk scan
execute ecnt-dsl
ecnt-dsl
This topic includes the following commands:
l execute ecnt-dsl update on page 4104
l execute ecnt-dsl upload on page 4104
execute ecnt-dsl update
Update ECNT Firmware
execute ecnt-dsl update
execute ecnt-dsl upload
upload file
execute ecnt-dsl upload <url> <file>
Parameter
Description
Type
Size
<url>
URL of file server
string
<file>
Full path of file to be upploaded.
string
FortiOS 8.0.0 CLI Reference
4104
Fortinet Inc.

---


<!-- 来源页 4105 -->
CLI execute commands
execute enter
Select virtual domain.
execute enter <name>
Parameter
Description
Type
Size
<name>
VDOM name.
string
execute erase-disk
Erase a disk.
execute erase-disk
execute ethernet
ethernet
This topic includes the following commands:
l execute ethernet ping on page 4105
l execute ethernet ping-option cos on page 4106
l execute ethernet ping-option sender_ID on page 4106
l execute ethernet ping-option view-settings on page 4106
l execute ethernet traceroute on page 4106
l execute ethernet traceroute-option cos on page 4107
l execute ethernet traceroute-option sender_ID on page 4107
l execute ethernet traceroute-option usefdbonly on page 4107
l execute ethernet traceroute-option view-settings on page 4107
execute ethernet ping
ethernet ping.
execute ethernet ping <interface> <level> <count> <mac>
FortiOS 8.0.0 CLI Reference
4105
Fortinet Inc.

---


<!-- 来源页 4105 -->
CLI execute commands
execute enter
Select virtual domain.
execute enter <name>
Parameter
Description
Type
Size
<name>
VDOM name.
string
execute erase-disk
Erase a disk.
execute erase-disk
execute ethernet
ethernet
This topic includes the following commands:
l execute ethernet ping on page 4105
l execute ethernet ping-option cos on page 4106
l execute ethernet ping-option sender_ID on page 4106
l execute ethernet ping-option view-settings on page 4106
l execute ethernet traceroute on page 4106
l execute ethernet traceroute-option cos on page 4107
l execute ethernet traceroute-option sender_ID on page 4107
l execute ethernet traceroute-option usefdbonly on page 4107
l execute ethernet traceroute-option view-settings on page 4107
execute ethernet ping
ethernet ping.
execute ethernet ping <interface> <level> <count> <mac>
FortiOS 8.0.0 CLI Reference
4105
Fortinet Inc.

---


<!-- 来源页 4105 -->
CLI execute commands
execute enter
Select virtual domain.
execute enter <name>
Parameter
Description
Type
Size
<name>
VDOM name.
string
execute erase-disk
Erase a disk.
execute erase-disk
execute ethernet
ethernet
This topic includes the following commands:
l execute ethernet ping on page 4105
l execute ethernet ping-option cos on page 4106
l execute ethernet ping-option sender_ID on page 4106
l execute ethernet ping-option view-settings on page 4106
l execute ethernet traceroute on page 4106
l execute ethernet traceroute-option cos on page 4107
l execute ethernet traceroute-option sender_ID on page 4107
l execute ethernet traceroute-option usefdbonly on page 4107
l execute ethernet traceroute-option view-settings on page 4107
execute ethernet ping
ethernet ping.
execute ethernet ping <interface> <level> <count> <mac>
FortiOS 8.0.0 CLI Reference
4105
Fortinet Inc.

<!-- 来源页 4106 -->
CLI execute commands
Parameter
Description
Type
Size
<interface>
<interface>
string
<level>
<level>
string
<count>
<count>
string
<mac>
<mac-address>
string
execute ethernet ping-option cos
<0 - 7>
execute ethernet ping-option cos <cos>
Parameter
Description
Type
Size
<cos>
<0 - 7>.
string
execute ethernet ping-option sender_ID
<None | Hostname>
execute ethernet ping-option sender_ID <sender_ID>
Parameter
Description
Type
Size
<sender_ID>
<None | Hostname>.
string
execute ethernet ping-option view-settings
View the current options of ping.
execute ethernet ping-option view-settings
execute ethernet traceroute
ethernet traceroute.
execute ethernet traceroute <interface> <level> <mac>
FortiOS 8.0.0 CLI Reference
4106
Fortinet Inc.

<!-- 来源页 4107 -->
CLI execute commands
Parameter
Description
Type
Size
<interface>
<interface>
string
<level>
<level>
string
<mac>
<mac-address>
string
execute ethernet traceroute-option cos
<0 - 7>
execute ethernet traceroute-option cos <cos>
Parameter
Description
Type
Size
<cos>
<0 - 7>.
string
execute ethernet traceroute-option sender_ID
<None | Hostname>
execute ethernet traceroute-option sender_ID <sender_ID>
Parameter
Description
Type
Size
<sender_ID>
<None | Hostname>.
string
execute ethernet traceroute-option usefdbonly
<enable | disable>
execute ethernet traceroute-option usefdbonly <usefdbonly>
Parameter
Description
Type
Size
<usefdbonly>
<enable | disable>.
string
execute ethernet traceroute-option view-settings
View the current options of traceroute.
execute ethernet traceroute-option view-settings
FortiOS 8.0.0 CLI Reference
4107
Fortinet Inc.

---


<!-- 来源页 4108 -->
CLI execute commands
execute extender
extender
This topic includes the following commands:
l execute extender delete-fortiextender-image on page 4108
l execute extender install-forticloud-mdm-package on page 4108
l execute extender install-forticloud-os-image on page 4109
l execute extender list-fortiextender-image on page 4109
l execute extender lte-carrier add on page 4109
l execute extender lte-carrier del on page 4109
l execute extender lte-simmap add on page 4110
l execute extender lte-simmap del on page 4110
l execute extender push-fortiextender-image on page 4110
l execute extender push-fortiextender-stage-image on page 4111
l execute extender query-forticloud-mdmpkg-image on page 4111
l execute extender query-forticloud-os-image on page 4111
l execute extender reset-fortiextender on page 4111
l execute extender restart-fortiextender-daemon on page 4112
l execute extender upload-fortiextender-image ftp on page 4112
l execute extender upload-fortiextender-image tftp on page 4112
execute extender delete-fortiextender-image
Delete FortiExtender images.
execute extender delete-fortiextender-image
execute extender install-forticloud-mdm-package
Install FortiExtender modem package from Cloud.
execute extender install-forticloud-mdm-package <filename> <sn>
Parameter
Description
Type
Size
<filename>
FortiExtender Cloud modem package version.
string
<sn>
FortiExtender serial number.
string
FortiOS 8.0.0 CLI Reference
4108
Fortinet Inc.

<!-- 来源页 4109 -->
CLI execute commands
execute extender install-forticloud-os-image
Install FortiExtender OS image from Cloud.
execute extender install-forticloud-os-image <filename> <sn>
Parameter
Description
Type
Size
<filename>
FortiExtender Cloud image version.
string
<sn>
FortiExtender serial number.
string
execute extender list-fortiextender-image
List FortiExtender images.
execute extender list-fortiextender-image
execute extender lte-carrier add
Add a LTE carrier with string.
execute extender lte-carrier add <SN> <string> [<string>]
Parameter
Description
Type
Size
<SN>
FortiExtender serial number.
string
<string>
Newly added carrier name on the FEXT.
string
[<string>]
Optional and default as GENERIC. Base carrier name on the
FEXT, where the PRI and FW is referred by the newly
added carrier.
string
execute extender lte-carrier del
Delete a LTE carrier with string.
execute extender lte-carrier del <SN> <string>
Parameter
Description
Type
Size
<SN>
FortiExtender serial number.
string
<string>
Carrier name on the FEXT.
string
FortiOS 8.0.0 CLI Reference
4109
Fortinet Inc.

<!-- 来源页 4110 -->
CLI execute commands
execute extender lte-simmap add
Add a carrier based on MCC/MNC.
execute extender lte-simmap add <SN> <string> <string> <string>
Parameter
Description
Type
Size
<SN>
FortiExtender serial number.
string
<string>
MCC number.
string
<string>
MNC number.
string
<string>
Carrier name on the FEXT.
string
execute extender lte-simmap del
Delete a LTE carrier with string.
execute extender lte-simmap del <SN> <string> <string> <string>
Parameter
Description
Type
Size
<SN>
FortiExtender serial number.
string
<string>
MCC number.
string
<string>
MNC number.
string
<string>
Carrier name on the FEXT.
string
execute extender push-fortiextender-image
Push FortiExtender image to a managed FortiExtender.
execute extender push-fortiextender-image <vdom> <sn> <filename>
Parameter
Description
Type
Size
<vdom>
FortiExtender session VDOM.
string
<sn>
FortiExtender serial number.
string
<filename>
FortiExtender image filename.
string
FortiOS 8.0.0 CLI Reference
4110
Fortinet Inc.

<!-- 来源页 4111 -->
CLI execute commands
execute extender push-fortiextender-stage-image
Push FortiExtender stage image to a managed FortiExtender.
execute extender push-fortiextender-stage-image <vdom> <sn> <filename>
Parameter
Description
Type
Size
<vdom>
FortiExtender session VDOM.
string
<sn>
FortiExtender serial number.
string
<filename>
FortiExtender image filename.
string
execute extender query-forticloud-mdmpkg-image
Query FortiExtender modem packages on Cloud.
execute extender query-forticloud-mdmpkg-image <all>|<filename> <sn>
Parameter
Description
Type
Size
<all>|<filename>
FortiExtender Cloud modem packages.
string
<sn>
FortiExtender serial number.
string
execute extender query-forticloud-os-image
Query FortiExtender OS images on Cloud.
execute extender query-forticloud-os-image <all>|<filename> <sn>
Parameter
Description
Type
Size
<all>|<filename>
FortiExtender Cloud OS images.
string
<sn>
FortiExtender serial number.
string
execute extender reset-fortiextender
Restart managed FortiExtender.
execute extender reset-fortiextender <all>|<SN>
FortiOS 8.0.0 CLI Reference
4111
Fortinet Inc.

---


<!-- 来源页 4112 -->
CLI execute commands
Parameter
Description
Type
Size
<all>|<SN>
FortiExtender serial number.
string
execute extender restart-fortiextender-daemon
Restart ForExtender AC daemon.
execute extender restart-fortiextender-daemon
execute extender upload-fortiextender-image ftp
Upload FortiExtender image from FTP server.
execute extender upload-fortiextender-image ftp <string> <ftp server>[:ftp port] <Enter>|<user>
<passwd>
Parameter
Description
Type
Size
<string>
FortiExtender image file name on the remote server.
string
<ftp server>[:ftp
port]
FTP server IPv4, IPv6, or FQDN can be attached with
port.
string
<Enter>|<user>
FTP username may be needed.
string
<passwd>
FTP password.
string
execute extender upload-fortiextender-image tftp
Upload FortiExtender image from TFTP server.
execute extender upload-fortiextender-image tftp <string> <tftp server>
Parameter
Description
Type
Size
<string>
File name on the TFTP server.
string
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
execute fabric-vpn
fabric-vpn
FortiOS 8.0.0 CLI Reference
4112
Fortinet Inc.

---


<!-- 来源页 4113 -->
CLI execute commands
This topic includes the following commands:
l execute fabric-vpn flush-setup on page 4113
l execute fabric-vpn update-setup on page 4113
execute fabric-vpn flush-setup
Remove fabric VPN settings.
execute fabric-vpn flush-setup
execute fabric-vpn update-setup
Update fabric VPN setup.
execute fabric-vpn update-setup
execute factoryreset
Reset to factory default now.
execute factoryreset
execute factoryreset2
Reset to factory default except system.global.vdom-mode/system.global.long-vdom-name/VDOMS/system.virtual-switch/system.interface/system.settings/router.static/router.static6.
execute factoryreset2
execute factoryreset-for-central-management
Reset to factory default except system.central-management.serial-number/system.central-management.fmg.
execute factoryreset-for-central-management
FortiOS 8.0.0 CLI Reference
4113
Fortinet Inc.

---


<!-- 来源页 4113 -->
CLI execute commands
This topic includes the following commands:
l execute fabric-vpn flush-setup on page 4113
l execute fabric-vpn update-setup on page 4113
execute fabric-vpn flush-setup
Remove fabric VPN settings.
execute fabric-vpn flush-setup
execute fabric-vpn update-setup
Update fabric VPN setup.
execute fabric-vpn update-setup
execute factoryreset
Reset to factory default now.
execute factoryreset
execute factoryreset2
Reset to factory default except system.global.vdom-mode/system.global.long-vdom-name/VDOMS/system.virtual-switch/system.interface/system.settings/router.static/router.static6.
execute factoryreset2
execute factoryreset-for-central-management
Reset to factory default except system.central-management.serial-number/system.central-management.fmg.
execute factoryreset-for-central-management
FortiOS 8.0.0 CLI Reference
4113
Fortinet Inc.

---


<!-- 来源页 4113 -->
CLI execute commands
This topic includes the following commands:
l execute fabric-vpn flush-setup on page 4113
l execute fabric-vpn update-setup on page 4113
execute fabric-vpn flush-setup
Remove fabric VPN settings.
execute fabric-vpn flush-setup
execute fabric-vpn update-setup
Update fabric VPN setup.
execute fabric-vpn update-setup
execute factoryreset
Reset to factory default now.
execute factoryreset
execute factoryreset2
Reset to factory default except system.global.vdom-mode/system.global.long-vdom-name/VDOMS/system.virtual-switch/system.interface/system.settings/router.static/router.static6.
execute factoryreset2
execute factoryreset-for-central-management
Reset to factory default except system.central-management.serial-number/system.central-management.fmg.
execute factoryreset-for-central-management
FortiOS 8.0.0 CLI Reference
4113
Fortinet Inc.

---


<!-- 来源页 4114 -->
CLI execute commands
execute factoryreset-shutdown
Reset to factory default and shutdown.
execute factoryreset-shutdown
execute fctems
fctems
This topic includes the following commands:
l execute fctems is-verified on page 4114
l execute fctems unverify on page 4114
l execute fctems verify on page 4114
execute fctems is-verified
Check if Configured EMS server has a verified certificate.
execute fctems is-verified <fctems>
Parameter
Description
Type
Size
<fctems>
FortiClient EMS table entry id in CMDB.
string
execute fctems unverify
Unverify FortiClient EMS server.
execute fctems unverify <fctems>
Parameter
Description
Type
Size
<fctems>
FortiClient EMS table entry id in CMDB.
string
execute fctems verify
Verify FortiClient EMS server.
FortiOS 8.0.0 CLI Reference
4114
Fortinet Inc.

---


<!-- 来源页 4114 -->
CLI execute commands
execute factoryreset-shutdown
Reset to factory default and shutdown.
execute factoryreset-shutdown
execute fctems
fctems
This topic includes the following commands:
l execute fctems is-verified on page 4114
l execute fctems unverify on page 4114
l execute fctems verify on page 4114
execute fctems is-verified
Check if Configured EMS server has a verified certificate.
execute fctems is-verified <fctems>
Parameter
Description
Type
Size
<fctems>
FortiClient EMS table entry id in CMDB.
string
execute fctems unverify
Unverify FortiClient EMS server.
execute fctems unverify <fctems>
Parameter
Description
Type
Size
<fctems>
FortiClient EMS table entry id in CMDB.
string
execute fctems verify
Verify FortiClient EMS server.
FortiOS 8.0.0 CLI Reference
4114
Fortinet Inc.

---


<!-- 来源页 4115 -->
CLI execute commands
execute fctems verify <fctems>
Parameter
Description
Type
Size
<fctems>
FortiClient EMS table entry id in CMDB.
string
execute federated-upgrade
federated-upgrade
This topic includes the following commands:
l execute federated-upgrade cancel on page 4115
l execute federated-upgrade initialize on page 4115
l execute federated-upgrade quick-fortigate-upgrade on page 4115
l execute federated-upgrade quick-full-upgrade on page 4116
l execute federated-upgrade restart on page 4116
l execute federated-upgrade safe-cancel on page 4116
l execute federated-upgrade status on page 4117
execute federated-upgrade cancel
Cancel the currently configured upgrade.
execute federated-upgrade cancel
execute federated-upgrade initialize
Set up a federated upgrade.
execute federated-upgrade initialize
execute federated-upgrade quick-fortigate-upgrade
Set up a 15 minute immediate mode upgrade for all FortiGates in the CSF tree.
execute federated-upgrade quick-fortigate-upgrade <major> <minor> <patch> <delay-minutes> <max-minutes>
FortiOS 8.0.0 CLI Reference
4115
Fortinet Inc.

<!-- 来源页 4116 -->
CLI execute commands
Parameter
Description
Type
Size
<major>
Major version of the Fortinet OS image being upgraded to.
string
<minor>
Minor version of the Fortinet OS image being upgraded to.
string
<patch>
Patch version of the Fortinet OS image being upgraded to.
string
<delay-minutes>
Minutes to delay before starting the upgrade setup.
string
<max-minutes>
Number of minutes allowed for upgrade preparation.
string
execute federated-upgrade quick-full-upgrade
Set up a 15 minute immediate mode upgrade for all CSF devices.
execute federated-upgrade quick-full-upgrade <major> <minor> <patch> <delay-minutes> <max-minutes>
Parameter
Description
Type
Size
<major>
Major version of the Fortinet OS image being upgraded to.
string
<minor>
Minor version of the Fortinet OS image being upgraded to.
string
<patch>
Patch version of the Fortinet OS image being upgraded to.
string
<delay-minutes>
Minutes to delay before starting the upgrade setup.
string
<max-minutes>
Number of minutes allowed for upgrade preparation.
string
execute federated-upgrade restart
Restart the currently configured federated upgrade.
execute federated-upgrade restart
execute federated-upgrade safe-cancel
Cancel the currently configured upgrade via the safe cancel API. Only cancels user-created upgrades.
execute federated-upgrade safe-cancel
FortiOS 8.0.0 CLI Reference
4116
Fortinet Inc.

---


<!-- 来源页 4117 -->
CLI execute commands
execute federated-upgrade status
Show the current status of federated upgrade.
execute federated-upgrade status
execute fips
fips
This topic includes the following commands:
l execute fips tftp-drbg-entropy-source on page 4117
l execute fips tftp-test-vectors on page 4117
execute fips tftp-drbg-entropy-source
tftp files and generate drbg entropy source samples
execute fips tftp-drbg-entropy-source <ip> <dir> <number> <number>
Parameter
Description
Type
Size
<ip>
IP address of the tftp server
string
<dir>
directory for the entropy sample files
string
<number>
samples size.
string
<number>
total number of samples.
string
execute fips tftp-test-vectors
tftp files and generate test vector results
execute fips tftp-test-vectors <ip> <dir> <file name>
Parameter
Description
Type
Size
<ip>
IP address of the tftp server
string
<dir>
directory of the test files
string
<file name>
The JSON file to test.
string
FortiOS 8.0.0 CLI Reference
4117
Fortinet Inc.

---


<!-- 来源页 4118 -->
CLI execute commands
execute firewall
firewall
This topic includes the following commands:
l execute firewall ssh generate local-ca on page 4118
l execute firewall ssh generate local-key on page 4118
execute firewall ssh generate local-ca
Generate the default ssh local key.
execute firewall ssh generate local-ca <string>
Parameter
Description
Type
Size
<string>
Local CA name.
string
execute firewall ssh generate local-key
Generate the default ssh local key.
execute firewall ssh generate local-key <string>
Parameter
Description
Type
Size
<string>
Local key name.
string
execute formatlogdisk
Format log disk.
execute formatlogdisk
execute forticarrier-license
forticarrier-license
FortiOS 8.0.0 CLI Reference
4118
Fortinet Inc.

---


<!-- 来源页 4118 -->
CLI execute commands
execute firewall
firewall
This topic includes the following commands:
l execute firewall ssh generate local-ca on page 4118
l execute firewall ssh generate local-key on page 4118
execute firewall ssh generate local-ca
Generate the default ssh local key.
execute firewall ssh generate local-ca <string>
Parameter
Description
Type
Size
<string>
Local CA name.
string
execute firewall ssh generate local-key
Generate the default ssh local key.
execute firewall ssh generate local-key <string>
Parameter
Description
Type
Size
<string>
Local key name.
string
execute formatlogdisk
Format log disk.
execute formatlogdisk
execute forticarrier-license
forticarrier-license
FortiOS 8.0.0 CLI Reference
4118
Fortinet Inc.

---


<!-- 来源页 4118 -->
CLI execute commands
execute firewall
firewall
This topic includes the following commands:
l execute firewall ssh generate local-ca on page 4118
l execute firewall ssh generate local-key on page 4118
execute firewall ssh generate local-ca
Generate the default ssh local key.
execute firewall ssh generate local-ca <string>
Parameter
Description
Type
Size
<string>
Local CA name.
string
execute firewall ssh generate local-key
Generate the default ssh local key.
execute firewall ssh generate local-key <string>
Parameter
Description
Type
Size
<string>
Local key name.
string
execute formatlogdisk
Format log disk.
execute formatlogdisk
execute forticarrier-license
forticarrier-license
FortiOS 8.0.0 CLI Reference
4118
Fortinet Inc.

---


<!-- 来源页 4119 -->
CLI execute commands
execute forticarrier-license <activation-code>
Parameter
Description
Type
Size
<activation-code>
Format:0000-0000-0000-0000-0001 or <license-key>
Format:0000-0000-0000-0000-0000-0000-00
string
execute forticloud-sandbox
forticloud-sandbox
This topic includes the following commands:
l execute forticloud-sandbox region on page 4119
l execute forticloud-sandbox update on page 4119
execute forticloud-sandbox region
Get FortiCloud sandbox region.
execute forticloud-sandbox region
execute forticloud-sandbox update
Update FortiCloud sandbox contract.
execute forticloud-sandbox update
execute fortiguard-log
fortiguard-log
This topic includes the following commands:
l execute fortiguard-log certificate-activation on page 4120
l execute fortiguard-log migration on page 4120
l execute fortiguard-log update on page 4120
FortiOS 8.0.0 CLI Reference
4119
Fortinet Inc.

---


<!-- 来源页 4119 -->
CLI execute commands
execute forticarrier-license <activation-code>
Parameter
Description
Type
Size
<activation-code>
Format:0000-0000-0000-0000-0001 or <license-key>
Format:0000-0000-0000-0000-0000-0000-00
string
execute forticloud-sandbox
forticloud-sandbox
This topic includes the following commands:
l execute forticloud-sandbox region on page 4119
l execute forticloud-sandbox update on page 4119
execute forticloud-sandbox region
Get FortiCloud sandbox region.
execute forticloud-sandbox region
execute forticloud-sandbox update
Update FortiCloud sandbox contract.
execute forticloud-sandbox update
execute fortiguard-log
fortiguard-log
This topic includes the following commands:
l execute fortiguard-log certificate-activation on page 4120
l execute fortiguard-log migration on page 4120
l execute fortiguard-log update on page 4120
FortiOS 8.0.0 CLI Reference
4119
Fortinet Inc.

---


<!-- 来源页 4120 -->
CLI execute commands
execute fortiguard-log certificate-activation
Activate FortiCloud certification.
execute fortiguard-log certificate-activation <code>
Parameter
Description
Type
Size
<code>
Activation code.
string
execute fortiguard-log migration
Migrate standalone FortiGate Cloud account to FortiCloud.
execute fortiguard-log migration <password>
Parameter
Description
Type
Size
<password>
Password.
string
execute fortiguard-log update
Update FortiCloud Contract.
execute fortiguard-log update
execute fortiguard-message
fortiguard-message
This topic includes the following commands:
l execute fortiguard-message add on page 4120
l execute fortiguard-message info on page 4121
l execute fortiguard-message update on page 4121
execute fortiguard-message add
Add FortiGuard Message Service activation code.
execute fortiguard-message add <activation code>
FortiOS 8.0.0 CLI Reference
4120
Fortinet Inc.

---


<!-- 来源页 4121 -->
CLI execute commands
Parameter
Description
Type
Size
<activation
code>
Activation code for FortiGuard Message Service.
string
execute fortiguard-message info
Show info about FortiGuard Message Service.
execute fortiguard-message info
execute fortiguard-message update
Force to update FortiGuard Message Service.
execute fortiguard-message update
execute fortimanager
fortimanager
This topic includes the following commands:
l execute fortimanager fetch on page 4121
l execute fortimanager register on page 4121
execute fortimanager fetch
Fetch and verify the FortiManager certificate
execute fortimanager fetch
execute fortimanager register
Register Fortigate to Fortimanager
execute fortimanager register <ip>
Parameter
Description
Type
Size
<ip>
Fortimanager's ip that Fortigate will register to
string
FortiOS 8.0.0 CLI Reference
4121
Fortinet Inc.

---


<!-- 来源页 4122 -->
CLI execute commands
execute fortitoken
fortitoken
This topic includes the following commands:
l execute fortitoken activate on page 4122
l execute fortitoken import ftp on page 4123
l execute fortitoken import tftp on page 4123
l execute fortitoken import usb on page 4123
l execute fortitoken import-sn-file on page 4124
l execute fortitoken sync on page 4124
execute fortitoken activate
Activate FortiToken(s) with FortiGuard.
execute fortitoken activate <id> <id> <id> <id> <id> <id> <id> <id> <id> <id> <id> <id> <id> <id>
<id> <id> <id> <id> <id> <id>
Parameter
Description
Type
Size
<id>
FortiToken ID.
string
<id>
FortiToken ID.
string
<id>
FortiToken ID.
string
<id>
FortiToken ID.
string
<id>
FortiToken ID.
string
<id>
FortiToken ID.
string
<id>
FortiToken ID.
string
<id>
FortiToken ID.
string
<id>
FortiToken ID.
string
<id>
FortiToken ID.
string
<id>
FortiToken ID.
string
<id>
FortiToken ID.
string
<id>
FortiToken ID.
string
<id>
FortiToken ID.
string
<id>
FortiToken ID.
string
<id>
FortiToken ID.
string
FortiOS 8.0.0 CLI Reference
4122
Fortinet Inc.

<!-- 来源页 4123 -->
CLI execute commands
Parameter
Description
Type
Size
<id>
FortiToken ID.
string
<id>
FortiToken ID.
string
<id>
FortiToken ID.
string
<id>
FortiToken ID.
string
execute fortitoken import ftp
Import FortiToken seeds file from FTP server.
execute fortitoken import ftp <file name> <ftp server>[:ftp port] <Enter>|<user> <passwd>
Parameter
Description
Type
Size
<file name>
FortiToken seeds file name.
string
<ftp server>[:ftp
port]
FTP server IPv4, IPv6, or FQDN can be attached with
port.
string
<Enter>|<user>
FTP username may be needed.
string
<passwd>
FTP password.
string
execute fortitoken import tftp
Import FortiToken seeds file from TFTP server.
execute fortitoken import tftp <file name> <tftp server>
Parameter
Description
Type
Size
<file name>
FortiToken seeds file name.
string
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
execute fortitoken import usb
Import FortiToken seeds file from USB drive.
execute fortitoken import usb <file name>
Parameter
Description
Type
Size
<file name>
FortiToken seeds file name.
string
FortiOS 8.0.0 CLI Reference
4123
Fortinet Inc.

---


<!-- 来源页 4124 -->
CLI execute commands
execute fortitoken import-sn-file
Import FTK_200 serial number from FortiCare.
execute fortitoken import-sn-file <FTK_200 Serial Number>
Parameter
Description
Type
Size
<FTK_200
Serial
Number>
FTK_200 serial number.
string
execute fortitoken sync
Synchronize FortiToken by adjusting for drift of internal clock.
execute fortitoken sync <id> <code> <next code>
Parameter
Description
Type
Size
<id>
FortiToken ID.
string
<code>
FortiToken code.
string
<next code>
Next FortiToken code.
string
execute fortitoken-cloud
fortitoken-cloud
This topic includes the following commands:
l execute fortitoken-cloud migrate-ftm on page 4125
l execute fortitoken-cloud new on page 4125
l execute fortitoken-cloud region-info on page 4125
l execute fortitoken-cloud region-reset on page 4125
l execute fortitoken-cloud show on page 4125
l execute fortitoken-cloud sync on page 4126
l execute fortitoken-cloud trial on page 4126
l execute fortitoken-cloud update on page 4126
FortiOS 8.0.0 CLI Reference
4124
Fortinet Inc.

<!-- 来源页 4125 -->
CLI execute commands
execute fortitoken-cloud migrate-ftm
Migrate FortiToken service to FortiToken Cloud.
execute fortitoken-cloud migrate-ftm <license number> <vdom>
Parameter
Description
Type
Size
<license
number>
FortiToken mobile license number.
string
<vdom>
VDOM name.
string
execute fortitoken-cloud new
Send new activation code for a user.
execute fortitoken-cloud new <user name> <user type> <vdom>
Parameter
Description
Type
Size
<user name>
User name for new token.
string
<user type>
Enter admin, local or remote.
string
<vdom>
VDOM name.
string
execute fortitoken-cloud region-info
Show regional service information.
execute fortitoken-cloud region-info
execute fortitoken-cloud region-reset
Reset regional service to none.
execute fortitoken-cloud region-reset
execute fortitoken-cloud show
Show service status of this FortiGate.
execute fortitoken-cloud show
FortiOS 8.0.0 CLI Reference
4125
Fortinet Inc.

---


<!-- 来源页 4126 -->
CLI execute commands
execute fortitoken-cloud sync
Synchronize users to FortiToken Cloud.
execute fortitoken-cloud sync <user type>
Parameter
Description
Type
Size
<user type>
Enter <return>, all, local or remote.
string
execute fortitoken-cloud trial
Activate free license.
execute fortitoken-cloud trial
execute fortitoken-cloud update
Update VDOM list to FortiToken Cloud.
execute fortitoken-cloud update
execute fortitoken-mobile
fortitoken-mobile
This topic includes the following commands:
l execute fortitoken-mobile import on page 4126
l execute fortitoken-mobile poll on page 4127
l execute fortitoken-mobile provision on page 4127
l execute fortitoken-mobile renew on page 4127
l execute fortitoken-mobile update-regid on page 4127
execute fortitoken-mobile import
Import a list of tokens from FortiGuard to the FortiGate unit.
execute fortitoken-mobile import <code>
FortiOS 8.0.0 CLI Reference
4126
Fortinet Inc.

---


<!-- 来源页 4127 -->
CLI execute commands
Parameter
Description
Type
Size
<code>
Software Token Redemption Certificate.
string
execute fortitoken-mobile poll
Poll soft token states.
execute fortitoken-mobile poll
execute fortitoken-mobile provision
Provision a soft token.
execute fortitoken-mobile provision <sn>
Parameter
Description
Type
Size
<sn>
MobileToken serial number.
string
execute fortitoken-mobile renew
Renew a locked mobile FortiToken.
execute fortitoken-mobile renew <sn>
Parameter
Description
Type
Size
<sn>
MobileToken serial number.
string
execute fortitoken-mobile update-regid
Update the reg ID after a user re-install the FTM app on the mobile phone.
execute fortitoken-mobile update-regid
execute fsso
fsso
FortiOS 8.0.0 CLI Reference
4127
Fortinet Inc.

---


<!-- 来源页 4128 -->
CLI execute commands
This topic includes the following commands:
l execute fsso refresh on page 4128
execute fsso refresh
Refresh FSSO groups.
execute fsso refresh
execute gen-token
Generate bearer token.
execute gen-token <Type> <string> <Algorithm> <Expire>
Parameter
Description
Type
Size
<Type>
Type for token generation, by certificate or by pre-shared
key. Available types: cert, key
string
<string>
Certificate or preshared-key for token generation.
Available certificates:
string
<Algorithm>
Algorithm for token generation. Please ensure that the
signing algorithm matches the type of certificate and its
corresponding private key. Available Algorithms: RS256,
RS384, RS512, ES256, ES384, ES512 for cert. HS256,
HS384, HS512 for key.
string
<Expire>
Expire interval in hours, 0 for long live token.
string
execute ha
ha
This topic includes the following commands:
l execute ha disconnect on page 4129
l execute ha failover set on page 4129
l execute ha failover status on page 4129
l execute ha failover unset on page 4130
l execute ha ignore-hardware-revision disable on page 4130
l execute ha ignore-hardware-revision enable on page 4130
FortiOS 8.0.0 CLI Reference
4128
Fortinet Inc.

---


<!-- 来源页 4128 -->
CLI execute commands
This topic includes the following commands:
l execute fsso refresh on page 4128
execute fsso refresh
Refresh FSSO groups.
execute fsso refresh
execute gen-token
Generate bearer token.
execute gen-token <Type> <string> <Algorithm> <Expire>
Parameter
Description
Type
Size
<Type>
Type for token generation, by certificate or by pre-shared
key. Available types: cert, key
string
<string>
Certificate or preshared-key for token generation.
Available certificates:
string
<Algorithm>
Algorithm for token generation. Please ensure that the
signing algorithm matches the type of certificate and its
corresponding private key. Available Algorithms: RS256,
RS384, RS512, ES256, ES384, ES512 for cert. HS256,
HS384, HS512 for key.
string
<Expire>
Expire interval in hours, 0 for long live token.
string
execute ha
ha
This topic includes the following commands:
l execute ha disconnect on page 4129
l execute ha failover set on page 4129
l execute ha failover status on page 4129
l execute ha failover unset on page 4130
l execute ha ignore-hardware-revision disable on page 4130
l execute ha ignore-hardware-revision enable on page 4130
FortiOS 8.0.0 CLI Reference
4128
Fortinet Inc.

<!-- 来源页 4129 -->
CLI execute commands
l execute ha ignore-hardware-revision status on page 4130
l execute ha manage on page 4130
l execute ha synchronize on page 4131
execute ha disconnect
Disconnect from HA cluster.
execute ha disconnect <string> <string> <ip> <netmask>
Parameter
Description
Type
Size
<string>
Serial number.
string
<string>
Interface name.
string
<ip>
IP or subnet of the interface.
string
<netmask>
Netmask of the interface.
string
execute ha failover set
Set the given virtual cluster as secondary and trigger failover. Argument optional; if argument omitted, all virtual
clusters are affected.
execute ha failover set [integer]
Parameter
Description
Type
Size
[integer]
Virtual cluster ID. Optional; if not given, all virtual clusters
are affected.
string
execute ha failover status
Display whether the given virtual cluster has been set as secondary for failover. Argument optional; if no
argument given, display statuses of all virtual clusters.
execute ha failover status [integer]
Parameter
Description
Type
Size
[integer]
Virtual cluster ID. Optional; if not given, all virtual clusters
are affected.
string
FortiOS 8.0.0 CLI Reference
4129
Fortinet Inc.

<!-- 来源页 4130 -->
CLI execute commands
execute ha failover unset
If the given virtual cluster has been set as secondary before, unset it so HA will use normal criteria to decide the
primary. May trigger a failover. Argument optional; if argument not given, all virtual clusters are affected.
execute ha failover unset [integer]
Parameter
Description
Type
Size
[integer]
Virtual cluster ID. Optional; if not given, all virtual clusters
are affected.
string
execute ha ignore-hardware-revision disable
disable HA ignore hardware revision mode
execute ha ignore-hardware-revision disable
execute ha ignore-hardware-revision enable
enable HA ignore hardware revision mode
execute ha ignore-hardware-revision enable
execute ha ignore-hardware-revision status
display HA ignore hardware revision mode
execute ha ignore-hardware-revision status
execute ha manage
HA cluster index.
execute ha manage <string> <string>
Parameter
Description
Type
Size
<string>
HA cluster index.
string
<string>
Login admin name.
string
FortiOS 8.0.0 CLI Reference
4130
Fortinet Inc.

---


<!-- 来源页 4131 -->
CLI execute commands
execute ha synchronize
HA synchronize commands.
execute ha synchronize <string>
Parameter
Description
Type
Size
<string>
File type.
string
execute hscalefw-license
hscalefw-license
execute hscalefw-license <activation-code>
Parameter
Description
Type
Size
<activation-code>
Format:0000-0000-0000-0000-0001 or <license-key>
Format:0000-0000-0000-0000-0000-0000-00
string
execute interface
interface
This topic includes the following commands:
l execute interface dhcp6client-renew on page 4131
l execute interface dhcpclient-renew on page 4132
l execute interface pppoe-reconnect on page 4132
execute interface dhcp6client-renew
Renew DHCPv6 lease.
execute interface dhcp6client-renew <interface>
Parameter
Description
Type
Size
<interface>
Renew DHCPv6 lease on this interface.
string
FortiOS 8.0.0 CLI Reference
4131
Fortinet Inc.

---


<!-- 来源页 4131 -->
CLI execute commands
execute ha synchronize
HA synchronize commands.
execute ha synchronize <string>
Parameter
Description
Type
Size
<string>
File type.
string
execute hscalefw-license
hscalefw-license
execute hscalefw-license <activation-code>
Parameter
Description
Type
Size
<activation-code>
Format:0000-0000-0000-0000-0001 or <license-key>
Format:0000-0000-0000-0000-0000-0000-00
string
execute interface
interface
This topic includes the following commands:
l execute interface dhcp6client-renew on page 4131
l execute interface dhcpclient-renew on page 4132
l execute interface pppoe-reconnect on page 4132
execute interface dhcp6client-renew
Renew DHCPv6 lease.
execute interface dhcp6client-renew <interface>
Parameter
Description
Type
Size
<interface>
Renew DHCPv6 lease on this interface.
string
FortiOS 8.0.0 CLI Reference
4131
Fortinet Inc.

---


<!-- 来源页 4132 -->
CLI execute commands
execute interface dhcpclient-renew
Renew DHCP lease.
execute interface dhcpclient-renew <interface>
Parameter
Description
Type
Size
<interface>
Renew DHCP lease on this interface.
string
execute interface pppoe-reconnect
Reconnect to PPPoE server.
execute interface pppoe-reconnect <interface>
Parameter
Description
Type
Size
<interface>
Reconnect PPPoE on this interface.
string
execute internet-service
internet-service
This topic includes the following commands:
l execute internet-service restore on page 4132
execute internet-service restore
Restore Backup Internet Service DataBase.
execute internet-service restore
execute internet-service4
internet-service4
This topic includes the following commands:
l execute internet-service4 refresh on page 4133
FortiOS 8.0.0 CLI Reference
4132
Fortinet Inc.

---


<!-- 来源页 4132 -->
CLI execute commands
execute interface dhcpclient-renew
Renew DHCP lease.
execute interface dhcpclient-renew <interface>
Parameter
Description
Type
Size
<interface>
Renew DHCP lease on this interface.
string
execute interface pppoe-reconnect
Reconnect to PPPoE server.
execute interface pppoe-reconnect <interface>
Parameter
Description
Type
Size
<interface>
Reconnect PPPoE on this interface.
string
execute internet-service
internet-service
This topic includes the following commands:
l execute internet-service restore on page 4132
execute internet-service restore
Restore Backup Internet Service DataBase.
execute internet-service restore
execute internet-service4
internet-service4
This topic includes the following commands:
l execute internet-service4 refresh on page 4133
FortiOS 8.0.0 CLI Reference
4132
Fortinet Inc.

---


<!-- 来源页 4133 -->
CLI execute commands
execute internet-service4 refresh
Refresh Internet Service Database(IPV4).
execute internet-service4 refresh
execute internet-service6
internet-service6
This topic includes the following commands:
l execute internet-service6 refresh on page 4133
execute internet-service6 refresh
Refresh Internet Service Database(IPV6).
execute internet-service6 refresh
execute ipam
ipam
This topic includes the following commands:
l execute ipam create-dhcp-server on page 4133
execute ipam create-dhcp-server
Create a DHCP server managed by IPAM.
execute ipam create-dhcp-server <interface>
Parameter
Description
Type
Size
<interface>
Interface for the DHCP server.
string
FortiOS 8.0.0 CLI Reference
4133
Fortinet Inc.

---


<!-- 来源页 4133 -->
CLI execute commands
execute internet-service4 refresh
Refresh Internet Service Database(IPV4).
execute internet-service4 refresh
execute internet-service6
internet-service6
This topic includes the following commands:
l execute internet-service6 refresh on page 4133
execute internet-service6 refresh
Refresh Internet Service Database(IPV6).
execute internet-service6 refresh
execute ipam
ipam
This topic includes the following commands:
l execute ipam create-dhcp-server on page 4133
execute ipam create-dhcp-server
Create a DHCP server managed by IPAM.
execute ipam create-dhcp-server <interface>
Parameter
Description
Type
Size
<interface>
Interface for the DHCP server.
string
FortiOS 8.0.0 CLI Reference
4133
Fortinet Inc.

---


<!-- 来源页 4134 -->
CLI execute commands
execute iscsi
iscsi
This topic includes the following commands:
l execute iscsi login on page 4134
l execute iscsi logout on page 4134
l execute iscsi show on page 4134
execute iscsi login
Login to iSCSI.
execute iscsi login <name>
Parameter
Description
Type
Size
<name>
iSCSI name.
string
execute iscsi logout
Logout from iSCSI.
execute iscsi logout <name>
Parameter
Description
Type
Size
<name>
iSCSI name.
string
execute iscsi show
Show iSCSI info.
execute iscsi show <name>
Parameter
Description
Type
Size
<name>
iSCSI name.
string
FortiOS 8.0.0 CLI Reference
4134
Fortinet Inc.

---


<!-- 来源页 4135 -->
CLI execute commands
execute kmip
kmip
This topic includes the following commands:
l execute kmip create on page 4135
l execute kmip destroy on page 4135
l execute kmip get on page 4135
l execute kmip locate on page 4136
l execute kmip rekey on page 4136
execute kmip create
Create Symmetric key(s) in KMIP server
execute kmip create <kmip server> <algo> <keylen> <name>
Parameter
Description
Type
Size
<kmip server>
KMIP server name.
string
<algo>
Cryptographic Algorithm.
string
<keylen>
Key size (in bits).
string
<name>
Key name (separate with '|' or '*' for multiple items).
string
execute kmip destroy
Destroy Symmetric key(s) in KMIP server
execute kmip destroy <kmip server> <keyid>
Parameter
Description
Type
Size
<kmip server>
KMIP server name.
string
<keyid>
Key ID (in hex string, separate with '|' or '*' for multiple
items).
string
execute kmip get
Get Symmetric key(s) from KMIP server
FortiOS 8.0.0 CLI Reference
4135
Fortinet Inc.

---


<!-- 来源页 4136 -->
CLI execute commands
execute kmip get
execute kmip locate
locate Symmetric key(s) in KMIP server
execute kmip locate <kmip server> <name>
Parameter
Description
Type
Size
<kmip server>
KMIP server name.
string
<name>
Key name (separate with '|' or '*' for multiple items).
string
execute kmip rekey
Rekey Symmetric key(s) from KMIP server
execute kmip rekey <kmip server> <keyid>
Parameter
Description
Type
Size
<kmip server>
KMIP server name.
string
<keyid>
Key ID (in hex string, separate with '|' or '*' for multiple
items).
string
execute log
log
This topic includes the following commands:
l execute log backup ftp on page 4137
l execute log backup local on page 4138
l execute log backup tftp on page 4138
l execute log chroot on page 4138
l execute log delete on page 4138
l execute log delete-all on page 4138
l execute log detail on page 4139
l execute log display on page 4139
l execute log filter category on page 4139
l execute log filter device on page 4139
FortiOS 8.0.0 CLI Reference
4136
Fortinet Inc.

<!-- 来源页 4137 -->
CLI execute commands
l execute log filter dump on page 4139
l execute log filter field on page 4140
l execute log filter free-style on page 4140
l execute log filter ha-member on page 4140
l execute log filter local-search-mode on page 4141
l execute log filter max-checklines on page 4141
l execute log filter pre-fetch-pages on page 4141
l execute log filter reset on page 4141
l execute log filter start-line on page 4141
l execute log filter view-lines on page 4142
l execute log flush-cache on page 4142
l execute log flush-cache-all on page 4142
l execute log fortianalyzer manual-failover on page 4142
l execute log fortianalyzer test-connectivity on page 4142
l execute log fortianalyzer-cloud test-connectivity on page 4143
l execute log fortianalyzer2 manual-failover on page 4143
l execute log fortianalyzer3 manual-failover on page 4143
l execute log fortiguard test-connectivity on page 4143
l execute log list on page 4143
l execute log raw-backup ftp on page 4143
l execute log raw-backup tftp on page 4144
l execute log restore on page 4144
l execute log roll on page 4144
l execute log shift-time on page 4144
l execute log upload on page 4145
l execute log upload-progress on page 4145
execute log backup ftp
Backup logs and report databases to remote FTP server.
execute log backup ftp <filename> <ftp server>[:ftp port] <user> <passwd>
Parameter
Description
Type
Size
<filename>
Make file name on the remote FTP server
string
<ftp server>
[:ftp port]
FTP server IPv4, IPv6, or FQDN can be attached with port.
string
<user>
FTP username.
string
<passwd>
FTP password.
string
FortiOS 8.0.0 CLI Reference
4137
Fortinet Inc.

<!-- 来源页 4138 -->
CLI execute commands
execute log backup local
Backup logs and report databases to local storage device.
execute log backup local <path>
Parameter
Description
Type
Size
<path>
Path to store logs and report databases.
string
execute log backup tftp
Backup logs and report databases to remote TFTP server.
execute log backup tftp <filename> <tftp server>
Parameter
Description
Type
Size
<filename>
Make file name on the remote TFTP server
string
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
execute log chroot
Drop/Gain CLI root privilege.
execute log chroot
execute log delete
Delete local logs of one category.
execute log delete
execute log delete-all
Delete all local logs and recreate report database.
execute log delete-all
FortiOS 8.0.0 CLI Reference
4138
Fortinet Inc.

<!-- 来源页 4139 -->
CLI execute commands
execute log detail
Display utm log entries for a particular traffic log.
execute log detail <category> <utmref>
Parameter
Description
Type
Size
<category>
Category for UTM logs
string
<utmref>
You can copy and paste it from log display result by tuning
on it using 'exec log filter show-utm-ref 1'
string
execute log display
Display filtered log entries.
execute log display
execute log filter category
Category.
execute log filter category <category>
Parameter
Description
Type
Size
<category>
Category name, press enter for options.
string
execute log filter device
Device to get log from.
execute log filter device <device>
Parameter
Description
Type
Size
<device>
Device name, press enter for options.
string
execute log filter dump
Dump current filter settings.
FortiOS 8.0.0 CLI Reference
4139
Fortinet Inc.

<!-- 来源页 4140 -->
CLI execute commands
execute log filter dump
execute log filter field
Filter by field.
execute log filter field <name> <argument 1> <argument 2> <argument 3> <argument 4> <argument 5>
<argument 6> <argument 7>
Parameter
Description
Type
Size
<name>
Field name, press enter for options.
string
<argument 1>
Field search argument 1, press enter for more help.
string
<argument 2>
Optional arguments, press enter to save.
string
<argument 3>
Optional arguments, press enter to save.
string
<argument 4>
Optional arguments, press enter to save.
string
<argument 5>
Optional arguments, press enter to save.
string
<argument 6>
Optional arguments, press enter to save.
string
<argument 7>
Optional arguments, press enter to save.
string
execute log filter free-style
Filter by free-style expression.
execute log filter free-style <expression>
Parameter
Description
Type
Size
<expression>
Log filter expression.
string
execute log filter ha-member
HA member.
execute log filter ha-member <sn>
Parameter
Description
Type
Size
<sn>
Serial number of HA member.
string
FortiOS 8.0.0 CLI Reference
4140
Fortinet Inc.

<!-- 来源页 4141 -->
CLI execute commands
execute log filter local-search-mode
local log search mode
execute log filter local-search-mode <mode>
Parameter
Description
Type
Size
<mode>
Local log search mode, press enter for options.
string
execute log filter max-checklines
Maximum number of lines to check.
execute log filter max-checklines <number>
Parameter
Description
Type
Size
<number>
0 or (100 - 1000000).
string
execute log filter pre-fetch-pages
Number of pages to check in advance under on-demand log search mode.
execute log filter pre-fetch-pages <number>
Parameter
Description
Type
Size
<number>
(2 - 10).
string
execute log filter reset
Reset filter.
execute log filter reset <enter|all|field>
Parameter
Description
Type
Size
<enter|all|field>
<enter|all> to reset all, <field> to reset field only.
string
execute log filter start-line
Start line to display.
FortiOS 8.0.0 CLI Reference
4141
Fortinet Inc.

<!-- 来源页 4142 -->
CLI execute commands
execute log filter start-line <number>
Parameter
Description
Type
Size
<number>
>=1
string
execute log filter view-lines
Lines per view.
execute log filter view-lines <number>
Parameter
Description
Type
Size
<number>
Number of lines to view (5 - 1000).
string
execute log flush-cache
Write disk log cache of current category to disk in compressed format.
execute log flush-cache
execute log flush-cache-all
Write disk log cache of all categories to disk in compressed format.
execute log flush-cache-all
execute log fortianalyzer manual-failover
Manually failover to use the other server.
execute log fortianalyzer manual-failover
execute log fortianalyzer test-connectivity
Query FortiAnalyzer connection status.
execute log fortianalyzer test-connectivity
FortiOS 8.0.0 CLI Reference
4142
Fortinet Inc.

<!-- 来源页 4143 -->
CLI execute commands
execute log fortianalyzer-cloud test-connectivity
Query FortiAnalyzer Cloud connection status.
execute log fortianalyzer-cloud test-connectivity
execute log fortianalyzer2 manual-failover
Manually failover to use the other server.
execute log fortianalyzer2 manual-failover
execute log fortianalyzer3 manual-failover
Manually failover to use the other server.
execute log fortianalyzer3 manual-failover
execute log fortiguard test-connectivity
Query FortiGuard connection status.
execute log fortiguard test-connectivity
execute log list
List current and rolled log files info.
execute log list <category>
Parameter
Description
Type
Size
<category>
Category name, press enter for options.
string
execute log raw-backup ftp
Backup raw logs to remote FTP server.
execute log raw-backup ftp <remotedir> <ftp server>[:ftp port] <user> <passwd>
FortiOS 8.0.0 CLI Reference
4143
Fortinet Inc.

<!-- 来源页 4144 -->
CLI execute commands
Parameter
Description
Type
Size
<remotedir>
Remote directory on FTP server
string
<ftp server>
[:ftp port]
FTP server IPv4, IPv6, or FQDN can be attached with port.
string
<user>
FTP username.
string
<passwd>
FTP password.
string
execute log raw-backup tftp
Backup raw logs to remote TFTP server.
execute log raw-backup tftp <remotedir> <tftp server>
Parameter
Description
Type
Size
<remotedir>
Existing remote directory on TFTP server
string
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
execute log restore
Restore logs and report databases from local storage device.
execute log restore <path>
Parameter
Description
Type
Size
<path>
Path to restore logs and report databases.
string
execute log roll
Roll log files now.
execute log roll
execute log shift-time
Shift log time stamps.
execute log shift-time <hours>
FortiOS 8.0.0 CLI Reference
4144
Fortinet Inc.

---


<!-- 来源页 4145 -->
CLI execute commands
Parameter
Description
Type
Size
<hours>
Hours to shift log and report time stamps by.
string
execute log upload
Upload log and archives to FortiAnalyzer/FortiCloud.
execute log upload
execute log upload-progress
Check FortiCloud upload progress.
execute log upload-progress
execute lte-modem
lte-modem
This topic includes the following commands:
l execute lte-modem PLMN-profile change-password on page 4146
l execute lte-modem PLMN-profile delete on page 4146
l execute lte-modem PLMN-profile list on page 4146
l execute lte-modem PLMN-profile lock on page 4147
l execute lte-modem PLMN-profile modify on page 4147
l execute lte-modem PLMN-profile show-password on page 4147
l execute lte-modem PLMN-profile unlock on page 4147
l execute lte-modem cold-reboot on page 4147
l execute lte-modem get-modem-firmware ftp on page 4148
l execute lte-modem get-modem-firmware management-station on page 4148
l execute lte-modem get-modem-firmware tftp on page 4148
l execute lte-modem get-modem-firmware usb on page 4148
l execute lte-modem get-pri-firmware ftp on page 4149
l execute lte-modem get-pri-firmware management-station on page 4149
l execute lte-modem get-pri-firmware tftp on page 4149
l execute lte-modem get-pri-firmware usb on page 4150
l execute lte-modem power-off on page 4150
l execute lte-modem power-on on page 4150
l execute lte-modem purge-billing-data on page 4150
FortiOS 8.0.0 CLI Reference
4145
Fortinet Inc.

<!-- 来源页 4146 -->
CLI execute commands
l execute lte-modem reboot on page 4150
l execute lte-modem set-operation-mode on page 4150
l execute lte-modem set-usb-mode on page 4151
l execute lte-modem sim-switch on page 4151
l execute lte-modem start-upgrade on page 4151
l execute lte-modem start-upgrade-remote on page 4151
l execute lte-modem wireless-profile create on page 4151
l execute lte-modem wireless-profile delete on page 4152
l execute lte-modem wireless-profile list on page 4152
l execute lte-modem wireless-profile modify on page 4152
l execute lte-modem wireless-profile test on page 4153
execute lte-modem PLMN-profile change-password
Change PLMN-Profile Setting password.
execute lte-modem PLMN-profile change-password <new password> <password confirm>
Parameter
Description
Type
Size
<new
password>
New PLMN lock password (0-24 characters).
string
<password
confirm>
Confirm new PLMN password.
string
execute lte-modem PLMN-profile delete
Delete a PLMN profile.
execute lte-modem PLMN-profile delete <(0-9)>
Parameter
Description
Type
Size
<(0-9)>
PLMN profile ID.
string
execute lte-modem PLMN-profile list
List all the PLMN profiles in the Modem.
execute lte-modem PLMN-profile list
FortiOS 8.0.0 CLI Reference
4146
Fortinet Inc.

<!-- 来源页 4147 -->
CLI execute commands
execute lte-modem PLMN-profile lock
Lock PLMN-Profile Setting.
execute lte-modem PLMN-profile lock
execute lte-modem PLMN-profile modify
Create a PLMN profile.
execute lte-modem PLMN-profile modify <(0-9)> <code>
Parameter
Description
Type
Size
<(0-9)>
PLMN profile ID.
string
<code>
PLMN profile code (1 to 9 characters).
string
execute lte-modem PLMN-profile show-password
Show current PLMN-Profile lock password.
execute lte-modem PLMN-profile show-password
execute lte-modem PLMN-profile unlock
Unlock PLMN-Profile Setting.
execute lte-modem PLMN-profile unlock <password>
Parameter
Description
Type
Size
<password>
PLMN lock password (0-24 characters).
string
execute lte-modem cold-reboot
Cold reboot LTE Modem.
execute lte-modem cold-reboot
FortiOS 8.0.0 CLI Reference
4147
Fortinet Inc.

<!-- 来源页 4148 -->
CLI execute commands
execute lte-modem get-modem-firmware ftp
Load image from FTP server.
execute lte-modem get-modem-firmware ftp <string> <ftp server>[:ftp port] <Enter>|<user> <passwd>
Parameter
Description
Type
Size
<string>
Image file name(path) on the remote server.
string
<ftp server>[:ftp
port]
FTP server IPv4, IPv6, or FQDN can be attached with
port.
string
<Enter>|<user>
FTP username may be needed.
string
<passwd>
FTP password.
string
execute lte-modem get-modem-firmware management-station
Restore image from Management station.
execute lte-modem get-modem-firmware management-station <string>
Parameter
Description
Type
Size
<string>
Image ID on the server.
string
execute lte-modem get-modem-firmware tftp
Restore image from TFTP server.
execute lte-modem get-modem-firmware tftp <string> <tftp server>
Parameter
Description
Type
Size
<string>
Image file name on the TFTP server.
string
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
execute lte-modem get-modem-firmware usb
Restore image from USB disk.
execute lte-modem get-modem-firmware usb <string>
FortiOS 8.0.0 CLI Reference
4148
Fortinet Inc.

<!-- 来源页 4149 -->
CLI execute commands
Parameter
Description
Type
Size
<string>
Image file name on the USB disk.
string
execute lte-modem get-pri-firmware ftp
Load image from FTP server.
execute lte-modem get-pri-firmware ftp <string> <ftp server>[:ftp port] <Enter>|<user> <passwd>
Parameter
Description
Type
Size
<string>
Image file name(path) on the remote server.
string
<ftp server>[:ftp
port]
FTP server IPv4, IPv6, or FQDN can be attached with
port.
string
<Enter>|<user>
FTP username may be needed.
string
<passwd>
FTP password.
string
execute lte-modem get-pri-firmware management-station
Restore image from Management station.
execute lte-modem get-pri-firmware management-station <string>
Parameter
Description
Type
Size
<string>
Image ID on the server.
string
execute lte-modem get-pri-firmware tftp
Restore image from TFTP server.
execute lte-modem get-pri-firmware tftp <string> <tftp server>
Parameter
Description
Type
Size
<string>
Image file name on the TFTP server.
string
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
FortiOS 8.0.0 CLI Reference
4149
Fortinet Inc.

<!-- 来源页 4150 -->
CLI execute commands
execute lte-modem get-pri-firmware usb
Restore image from USB disk.
execute lte-modem get-pri-firmware usb <string>
Parameter
Description
Type
Size
<string>
Image file name on the USB disk.
string
execute lte-modem power-off
Power off LTE Modem.
execute lte-modem power-off
execute lte-modem power-on
Power on LTE Modem.
execute lte-modem power-on
execute lte-modem purge-billing-data
Purge all existing LTE Modem billing data.
execute lte-modem purge-billing-data
execute lte-modem reboot
Warm reboot LTE Modem.
execute lte-modem reboot
execute lte-modem set-operation-mode
Set LTE Modem operation mode.
execute lte-modem set-operation-mode <( 0, 1)>
FortiOS 8.0.0 CLI Reference
4150
Fortinet Inc.

<!-- 来源页 4151 -->
CLI execute commands
Parameter
Description
Type
Size
<( 0, 1)>
Operation mode. 0 - Online 1 - Low Power
string
execute lte-modem set-usb-mode
Set LTE Modem USB speed mode.
execute lte-modem set-usb-mode <(0, 1)>
Parameter
Description
Type
Size
<(0, 1)>
Operation mode. 0 - High speed 1 - Super high speed
string
execute lte-modem sim-switch
Perform sim switch to the other sim-slot.
execute lte-modem sim-switch
execute lte-modem start-upgrade
Start LTE Modem firmware upgrade.
execute lte-modem start-upgrade
execute lte-modem start-upgrade-remote
Start LTE Modem firmware upgrade now via forticloud service
execute lte-modem start-upgrade-remote
execute lte-modem wireless-profile create
Create a wireless profile.
execute lte-modem wireless-profile create <name> <profile type> <(0 - 4)> <name> <(0 - 3)>
<name>|<Enter> <password>
FortiOS 8.0.0 CLI Reference
4151
Fortinet Inc.

<!-- 来源页 4152 -->
CLI execute commands
Parameter
Description
Type
Size
<name>
Wireless profile name 1 to 16 characters.
string
<profile type>
Wireless profile type. 0 - 3GPP
string
<(0 - 4)>
Wireless profile PDP type. 0 - IPV4 1 - PPP 2 - IPV6 3 -IPV4V6
string
<name>
Wireless profile APN name 0 to 32 characters.
string
<(0 - 3)>
Wireless profile authentication type. 0 - None 1 - PAP 2
- CHAP 3 - PAP and CHAP
string
<name>|<Enter>
Wireless profile user Name 1 to 32 characters, or
<Enter> if authentication is none.
string
<password>
Wireless profile password 1 to 32 characters.
string
execute lte-modem wireless-profile delete
Delete a wireless profile from the Modem.
execute lte-modem wireless-profile delete <(1-16)>
Parameter
Description
Type
Size
<(1-16)>
Wireless profile ID.
string
execute lte-modem wireless-profile list
List all the wireless profiles in the Modem.
execute lte-modem wireless-profile list
execute lte-modem wireless-profile modify
Modify a wireless profile.
execute lte-modem wireless-profile modify <(1-16)> <name> <profile type> <(0 - 4)> <name> <(0 -3)> <name>|<Enter> <password>
Parameter
Description
Type
Size
<(1-16)>
Wireless profile ID.
string
<name>
Wireless profile name 1 to 16 characters.
string
FortiOS 8.0.0 CLI Reference
4152
Fortinet Inc.

---


<!-- 来源页 4153 -->
CLI execute commands
Parameter
Description
Type
Size
<profile type>
Wireless profile type. 0 - 3GPP
string
<(0 - 4)>
Wireless profile PDP type. 0 - IPV4 1 - PPP 2 - IPV6 3 -IPV4V6
string
<name>
Wireless profile APN name 0 to 32 characters.
string
<(0 - 3)>
Wireless profile authentication type. 0 - None 1 - PAP 2
- CHAP 3 - PAP and CHAP
string
<name>|<Enter>
Wireless profile user name 1 to 32 characters, or
<Enter> if authentication is none.
string
<password>
Wireless profile password 1 to 32 characters.
string
execute lte-modem wireless-profile test
Test wireless profiles.
execute lte-modem wireless-profile test <(1-16)|<Enter>>
Parameter
Description
Type
Size
<(1-16)|<Enter>>
Wireless profile ID.
string
execute mem
mem
This topic includes the following commands:
l execute mem add on page 4153
execute mem add
Online new memory blocks.
execute mem add
FortiOS 8.0.0 CLI Reference
4153
Fortinet Inc.

---


<!-- 来源页 4154 -->
CLI execute commands
execute modem
modem
This topic includes the following commands:
l execute modem dial on page 4154
l execute modem hangup on page 4154
l execute modem trigger on page 4154
execute modem dial
Manually dial the MODEM.
execute modem dial
execute modem hangup
Manually hang up the MODEM.
execute modem hangup
execute modem trigger
Trigger the MODEM if it is stuck.
execute modem trigger
execute mqtt
mqtt
This topic includes the following commands:
l execute mqtt restart on page 4154
execute mqtt restart
restart mqtt-broker.
FortiOS 8.0.0 CLI Reference
4154
Fortinet Inc.

---


<!-- 来源页 4154 -->
CLI execute commands
execute modem
modem
This topic includes the following commands:
l execute modem dial on page 4154
l execute modem hangup on page 4154
l execute modem trigger on page 4154
execute modem dial
Manually dial the MODEM.
execute modem dial
execute modem hangup
Manually hang up the MODEM.
execute modem hangup
execute modem trigger
Trigger the MODEM if it is stuck.
execute modem trigger
execute mqtt
mqtt
This topic includes the following commands:
l execute mqtt restart on page 4154
execute mqtt restart
restart mqtt-broker.
FortiOS 8.0.0 CLI Reference
4154
Fortinet Inc.

---


<!-- 来源页 4155 -->
CLI execute commands
execute mqtt restart
execute mrouter
mrouter
This topic includes the following commands:
l execute mrouter clear dense-routes on page 4155
l execute mrouter clear igmp-group on page 4155
l execute mrouter clear igmp-interface on page 4156
l execute mrouter clear multicast-routes on page 4156
l execute mrouter clear sparse-mode-bsr on page 4156
l execute mrouter clear sparse-routes on page 4156
l execute mrouter clear statistics on page 4157
execute mrouter clear dense-routes
Clear PIM dense mode routes.
execute mrouter clear dense-routes <xxx.xxx.xxx.xxx> <xxx.xxx.xxx.xxx>
Parameter
Description
Type
Size
<xxx.xxx.xxx.xxx>
Group IP address.
string
<xxx.xxx.xxx.xxx>
Source IP address.
string
execute mrouter clear igmp-group
Clear all IGMP entries for one or all groups.
execute mrouter clear igmp-group <xxx.xxx.xxx.xxx> <string>
Parameter
Description
Type
Size
<xxx.xxx.xxx.xxx>
Group IP address.
string
<string>
Interface name.
string
FortiOS 8.0.0 CLI Reference
4155
Fortinet Inc.

<!-- 来源页 4156 -->
CLI execute commands
execute mrouter clear igmp-interface
Clear all IGMP entries from one interface.
execute mrouter clear igmp-interface <string>
Parameter
Description
Type
Size
<string>
Interface name.
string
execute mrouter clear multicast-routes
Clear all PIM dense mode and sparse mode routes.
execute mrouter clear multicast-routes <xxx.xxx.xxx.xxx>|<0-511> <xxx.xxx.xxx.xxx>|<0-511> <0-511>
Parameter
Description
Type
Size
<xxx.xxx.xxx.xxx>|<0-511>
Group IP address or VRF ID.
string
<xxx.xxx.xxx.xxx>|<0-511>
Source IP address or VRF ID.
string
<0-511>
VRF ID.
string
execute mrouter clear sparse-mode-bsr
Clear PIM-SM RP sets learned from the BSR.
execute mrouter clear sparse-mode-bsr <0-511>
Parameter
Description
Type
Size
<0-511>
VRF ID.
string
execute mrouter clear sparse-routes
Clear PIM sparse mode routes.
execute mrouter clear sparse-routes <xxx.xxx.xxx.xxx>|<0-511> <xxx.xxx.xxx.xxx>|<0-511> <0-511>
Parameter
Description
Type
Size
<xxx.xxx.xxx.xxx>|<0-511>
Group IP address or VRF ID.
string
FortiOS 8.0.0 CLI Reference
4156
Fortinet Inc.

---


<!-- 来源页 4157 -->
CLI execute commands
Parameter
Description
Type
Size
<xxx.xxx.xxx.xxx>|<0-511>
Source IP address or VRF ID.
string
<0-511>
VRF ID.
string
execute mrouter clear statistics
Clear PIM routing statistics.
execute mrouter clear statistics <xxx.xxx.xxx.xxx>|<0-511> <xxx.xxx.xxx.xxx>|<0-511> <0-511>
Parameter
Description
Type
Size
<xxx.xxx.xxx.xxx>|<0-511>
Group IP address or VRF ID.
string
<xxx.xxx.xxx.xxx>|<0-511>
Source IP address or VRF ID.
string
<0-511>
VRF ID.
string
execute mrouter6
mrouter6
This topic includes the following commands:
l execute mrouter6 clear mld on page 4157
l execute mrouter6 clear mld group on page 4158
l execute mrouter6 clear mld interface on page 4158
l execute mrouter6 clear mld vrf on page 4158
l execute mrouter6 clear sparse-routes on page 4158
execute mrouter6 clear mld
Clear PIM6 MLD group cache entries.
execute mrouter6 clear mld <X:X::X:X> <string>
Parameter
Description
Type
Size
<X:X::X:X>
Group IPv6 address.
string
<string>
Interface name.
string
FortiOS 8.0.0 CLI Reference
4157
Fortinet Inc.

<!-- 来源页 4158 -->
CLI execute commands
execute mrouter6 clear mld group
Clear PIM6 MLD group cache entries.
execute mrouter6 clear mld group <X:X::X:X> <string>|<0-511>
Parameter
Description
Type
Size
<X:X::X:X>
Group IPv6 address.
string
<string>|<0-511>
VRF ID (optional) or interface (optional).
string
execute mrouter6 clear mld interface
Clear PIM6 MLD group cache entries by interface.
execute mrouter6 clear mld interface <string>
Parameter
Description
Type
Size
<string>
Interface name.
string
execute mrouter6 clear mld vrf
Clear PIM6 MLD group cache entries by VRF.
execute mrouter6 clear mld vrf <0-511>
Parameter
Description
Type
Size
<0-511>
VRF ID.
string
execute mrouter6 clear sparse-routes
Clear PIM6 sparse mode routes.
execute mrouter6 clear sparse-routes <X:X::X:X> <X:X::X:X> <X:X::X:X>|<0-511> <X:X::X:X>|<0-511>
<0-511>
Parameter
Description
Type
Size
<X:X::X:X>
Group IPv6 address.
string
<X:X::X:X>
Source IPv6 address.
string
FortiOS 8.0.0 CLI Reference
4158
Fortinet Inc.

---


<!-- 来源页 4159 -->
CLI execute commands
Parameter
Description
Type
Size
<X:X::X:X>|<0-511>
Group IPv6 address or VRF ID.
string
<X:X::X:X>|<0-511>
Source IPv6 address or VRF ID.
string
<0-511>
VRF ID.
string
execute nsx
nsx
This topic includes the following commands:
l execute nsx group delete on page 4159
l execute nsx group import on page 4159
l execute nsx group list on page 4160
execute nsx group delete
Delete NSX Security Groups.
execute nsx group delete <vdom> <filter>
Parameter
Description
Type
Size
<vdom>
VDOM.
string
<filter>
Name Filter.
string
execute nsx group import
Import NSX Security Groups.
execute nsx group import <name> <vdom> <filter>
Parameter
Description
Type
Size
<name>
SDN connector.
string
<vdom>
VDOM.
string
<filter>
Name Filter.
string
FortiOS 8.0.0 CLI Reference
4159
Fortinet Inc.

---


<!-- 来源页 4160 -->
CLI execute commands
execute nsx group list
List NSX Security Groups.
execute nsx group list <name> <filter>
Parameter
Description
Type
Size
<name>
SDN connector.
string
<filter>
Name Filter.
string
execute oqs
OQS command to see available PQC KEM algorithms and generate test data.
execute oqs
execute ping
PING command.
execute ping <ip>
Parameter
Description
Type
Size
<ip>
IP address or domain name.
string
execute ping6
PINGv6 command.
execute ping6
FortiOS 8.0.0 CLI Reference
4160
Fortinet Inc.

---


<!-- 来源页 4160 -->
CLI execute commands
execute nsx group list
List NSX Security Groups.
execute nsx group list <name> <filter>
Parameter
Description
Type
Size
<name>
SDN connector.
string
<filter>
Name Filter.
string
execute oqs
OQS command to see available PQC KEM algorithms and generate test data.
execute oqs
execute ping
PING command.
execute ping <ip>
Parameter
Description
Type
Size
<ip>
IP address or domain name.
string
execute ping6
PINGv6 command.
execute ping6
FortiOS 8.0.0 CLI Reference
4160
Fortinet Inc.

---


<!-- 来源页 4160 -->
CLI execute commands
execute nsx group list
List NSX Security Groups.
execute nsx group list <name> <filter>
Parameter
Description
Type
Size
<name>
SDN connector.
string
<filter>
Name Filter.
string
execute oqs
OQS command to see available PQC KEM algorithms and generate test data.
execute oqs
execute ping
PING command.
execute ping <ip>
Parameter
Description
Type
Size
<ip>
IP address or domain name.
string
execute ping6
PINGv6 command.
execute ping6
FortiOS 8.0.0 CLI Reference
4160
Fortinet Inc.

---


<!-- 来源页 4161 -->
CLI execute commands
execute ping6-options
ping6-options
This topic includes the following commands:
l execute ping6-options adaptive-ping on page 4161
l execute ping6-options data-size on page 4161
l execute ping6-options interface on page 4162
l execute ping6-options interval on page 4162
l execute ping6-options pattern on page 4162
l execute ping6-options repeat-count on page 4162
l execute ping6-options reset on page 4162
l execute ping6-options source6 on page 4163
l execute ping6-options timeout on page 4163
l execute ping6-options tos on page 4163
l execute ping6-options ttl on page 4163
l execute ping6-options use-sdwan on page 4164
l execute ping6-options validate-reply on page 4164
l execute ping6-options view-settings on page 4164
l execute ping6-options vrf on page 4164
execute ping6-options adaptive-ping
Adaptive ping <enable|disable>.
execute ping6-options adaptive-ping <string>
Parameter
Description
Type
Size
<string>
<enable|disable>.
string
execute ping6-options data-size
Integer value to specify datagram size in bytes.
execute ping6-options data-size <integer>
Parameter
Description
Type
Size
<integer>
Integer value [0,65507].
string
FortiOS 8.0.0 CLI Reference
4161
Fortinet Inc.

<!-- 来源页 4162 -->
CLI execute commands
execute ping6-options interface
Auto | <outgoing interface>.
execute ping6-options interface <string>
Parameter
Description
Type
Size
<string>
Auto | <outgoing interface>.
string
execute ping6-options interval
Integer value to specify seconds to wait between two pings.
execute ping6-options interval <integer>
Parameter
Description
Type
Size
<integer>
Integer value [1, 2147483647]
string
execute ping6-options pattern
Hex format of pattern, e.g. 00ffaabb.
execute ping6-options pattern <string>
Parameter
Description
Type
Size
<string>
Hex format of pattern, e.g. 00ffaabb.
string
execute ping6-options repeat-count
Integer value to specify how many times to repeat PING.
execute ping6-options repeat-count <string>
Parameter
Description
Type
Size
<string>
Integer value [1, 2147483647]
string
execute ping6-options reset
Reset settings.
FortiOS 8.0.0 CLI Reference
4162
Fortinet Inc.

<!-- 来源页 4163 -->
CLI execute commands
execute ping6-options reset
execute ping6-options source6
Auto | <source interface IPv6>.
execute ping6-options source6 <xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx>
Parameter
Description
Type
Size
<xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx>
<source interface IPv6> | Auto
string
execute ping6-options timeout
Integer value to specify timeout in seconds.
execute ping6-options timeout <integer>
Parameter
Description
Type
Size
<integer>
Integer value [0, 2147483647]
string
execute ping6-options tos
IPv6 type-of-service (traffic class) value.
execute ping6-options tos <integer>
Parameter
Description
Type
Size
<integer>
Hex number [0x00, 0xFF]
string
execute ping6-options ttl
Integer value to specify time-to-live.
execute ping6-options ttl <integer>
Parameter
Description
Type
Size
<integer>
Integer value [1,255]
string
FortiOS 8.0.0 CLI Reference
4163
Fortinet Inc.

---


<!-- 来源页 4164 -->
CLI execute commands
execute ping6-options use-sdwan
Use SD-WAN rules to get output interface <yes | no>.
execute ping6-options use-sdwan <string>
Parameter
Description
Type
Size
<string>
<yes | no>.
string
execute ping6-options validate-reply
Validate reply data <yes | no>.
execute ping6-options validate-reply <string>
Parameter
Description
Type
Size
<string>
<yes | no>.
string
execute ping6-options view-settings
View the current settings for PING option.
execute ping6-options view-settings
execute ping6-options vrf
VRF ID.
execute ping6-options vrf <interger>
Parameter
Description
Type
Size
<interger>
<0-511>
string
execute ping-options
ping-options
This topic includes the following commands:
FortiOS 8.0.0 CLI Reference
4164
Fortinet Inc.

<!-- 来源页 4165 -->
CLI execute commands
l execute ping-options adaptive-ping on page 4165
l execute ping-options data-size on page 4165
l execute ping-options df-bit on page 4165
l execute ping-options interface on page 4166
l execute ping-options interval on page 4166
l execute ping-options pattern on page 4166
l execute ping-options repeat-count on page 4166
l execute ping-options reset on page 4167
l execute ping-options source on page 4167
l execute ping-options timeout on page 4167
l execute ping-options tos on page 4167
l execute ping-options ttl on page 4167
l execute ping-options use-sdwan on page 4168
l execute ping-options validate-reply on page 4168
l execute ping-options view-settings on page 4168
l execute ping-options vrf on page 4168
execute ping-options adaptive-ping
Adaptive ping <enable|disable>.
execute ping-options adaptive-ping <string>
Parameter
Description
Type
Size
<string>
<enable|disable>.
string
execute ping-options data-size
Integer value to specify datagram size in bytes.
execute ping-options data-size <integer>
Parameter
Description
Type
Size
<integer>
Integer value [0,65507].
string
execute ping-options df-bit
Set DF bit in IP header <yes | no>.
execute ping-options df-bit <string>
FortiOS 8.0.0 CLI Reference
4165
Fortinet Inc.

<!-- 来源页 4166 -->
CLI execute commands
Parameter
Description
Type
Size
<string>
<yes | no>.
string
execute ping-options interface
Auto | <outgoing interface>.
execute ping-options interface <string>
Parameter
Description
Type
Size
<string>
Auto | <outgoing interface>.
string
execute ping-options interval
Integer value to specify seconds between two pings.
execute ping-options interval <integer>
Parameter
Description
Type
Size
<integer>
Integer value [1, 2147483647]
string
execute ping-options pattern
Hex format of pattern, e.g. 00ffaabb.
execute ping-options pattern <string>
Parameter
Description
Type
Size
<string>
Hex format of pattern, e.g. 00ffaabb.
string
execute ping-options repeat-count
Integer value to specify how many times to repeat PING.
execute ping-options repeat-count <integer>
Parameter
Description
Type
Size
<integer>
Integer value [1, 2147483647]
string
FortiOS 8.0.0 CLI Reference
4166
Fortinet Inc.

<!-- 来源页 4167 -->
CLI execute commands
execute ping-options reset
Reset settings.
execute ping-options reset
execute ping-options source
Auto | <source interface IP>.
execute ping-options source <xxx.xxx.xxx.xxx>
Parameter
Description
Type
Size
<xxx.xxx.xxx.xxx>
<source interface IP> | Auto
string
execute ping-options timeout
Integer value to specify timeout in seconds.
execute ping-options timeout <integer>
Parameter
Description
Type
Size
<integer>
Integer value [0, 2147483647]
string
execute ping-options tos
IP type-of-service option.
execute ping-options tos <string>
Parameter
Description
Type
Size
<string>
default IP TOS defaults to 0 lowcost IP TOS minimize cost
lowdelay IP TOS minimize delay reliability IP TOS maximize
reliability throughput IP TOS maximize throughput
string
execute ping-options ttl
Integer value to specify time-to-live.
FortiOS 8.0.0 CLI Reference
4167
Fortinet Inc.

<!-- 来源页 4168 -->
CLI execute commands
execute ping-options ttl <integer>
Parameter
Description
Type
Size
<integer>
Integer value [1,255].
string
execute ping-options use-sdwan
Use SD-WAN rules to get output interface <yes | no>.
execute ping-options use-sdwan <string>
Parameter
Description
Type
Size
<string>
<yes | no>.
string
execute ping-options validate-reply
Validate reply data <yes | no>.
execute ping-options validate-reply <string>
Parameter
Description
Type
Size
<string>
<yes | no>.
string
execute ping-options view-settings
View the current settings for PING option.
execute ping-options view-settings
execute ping-options vrf
VRF ID.
execute ping-options vrf <interger>
Parameter
Description
Type
Size
<interger>
<0-511>
string
FortiOS 8.0.0 CLI Reference
4168
Fortinet Inc.

---


<!-- 来源页 4169 -->
CLI execute commands
execute policy-packet-capture
policy-packet-capture
This topic includes the following commands:
l execute policy-packet-capture delete-all on page 4169
execute policy-packet-capture delete-all
Delete all captured packet.
execute policy-packet-capture delete-all
execute private-encryption-key
private-encryption-key
This topic includes the following commands:
l execute private-encryption-key sample on page 4169
l execute private-encryption-key verify on page 4169
execute private-encryption-key sample
Generate base64 clear text and its HMAC signature encrypted by private key.
execute private-encryption-key sample
execute private-encryption-key verify
Verify if the input base64 HMAC is encrypted by private key.
execute private-encryption-key verify <string> <string>
Parameter
Description
Type
Size
<string>
base64-clear-text.
string
<string>
base64-hmac-signature.
string
FortiOS 8.0.0 CLI Reference
4169
Fortinet Inc.

---


<!-- 来源页 4169 -->
CLI execute commands
execute policy-packet-capture
policy-packet-capture
This topic includes the following commands:
l execute policy-packet-capture delete-all on page 4169
execute policy-packet-capture delete-all
Delete all captured packet.
execute policy-packet-capture delete-all
execute private-encryption-key
private-encryption-key
This topic includes the following commands:
l execute private-encryption-key sample on page 4169
l execute private-encryption-key verify on page 4169
execute private-encryption-key sample
Generate base64 clear text and its HMAC signature encrypted by private key.
execute private-encryption-key sample
execute private-encryption-key verify
Verify if the input base64 HMAC is encrypted by private key.
execute private-encryption-key verify <string> <string>
Parameter
Description
Type
Size
<string>
base64-clear-text.
string
<string>
base64-hmac-signature.
string
FortiOS 8.0.0 CLI Reference
4169
Fortinet Inc.

---


<!-- 来源页 4170 -->
CLI execute commands
execute reboot
Reboot now.
execute reboot <comment> <string>
Parameter
Description
Type
Size
<comment>
comment
string
<string>
Reboot comments.
string
execute replace-device
replace-device
This topic includes the following commands:
l execute replace-device fortiap on page 4170
l execute replace-device fortiextender on page 4170
l execute replace-device fortiswitch on page 4171
execute replace-device fortiap
FortiAP.
execute replace-device fortiap <fortiap-id> <fortiap-id>
Parameter
Description
Type
Size
<fortiap-id>
Old FortiAP serial number.
string
<fortiap-id>
New FortiAP serial number.
string
execute replace-device fortiextender
FortiExtender.
execute replace-device fortiextender <fortiextender-id> <fortiextender-id>
FortiOS 8.0.0 CLI Reference
4170
Fortinet Inc.

---


<!-- 来源页 4170 -->
CLI execute commands
execute reboot
Reboot now.
execute reboot <comment> <string>
Parameter
Description
Type
Size
<comment>
comment
string
<string>
Reboot comments.
string
execute replace-device
replace-device
This topic includes the following commands:
l execute replace-device fortiap on page 4170
l execute replace-device fortiextender on page 4170
l execute replace-device fortiswitch on page 4171
execute replace-device fortiap
FortiAP.
execute replace-device fortiap <fortiap-id> <fortiap-id>
Parameter
Description
Type
Size
<fortiap-id>
Old FortiAP serial number.
string
<fortiap-id>
New FortiAP serial number.
string
execute replace-device fortiextender
FortiExtender.
execute replace-device fortiextender <fortiextender-id> <fortiextender-id>
FortiOS 8.0.0 CLI Reference
4170
Fortinet Inc.

---


<!-- 来源页 4171 -->
CLI execute commands
Parameter
Description
Type
Size
<fortiextender-id>
Old FortiExtender serial number.
string
<fortiextender-id>
New FortiExtender serial number.
string
execute replace-device fortiswitch
FortiSwitch.
execute replace-device fortiswitch <fortiswitch-id> <fortiswitch-id>
Parameter
Description
Type
Size
<fortiswitch-id>
Existing FortiSwitch serial number.
string
<fortiswitch-id>
New FortiSwitch serial number.
string
execute report
report
This topic includes the following commands:
l execute report flush-cache on page 4171
l execute report recreate-db on page 4171
l execute report run on page 4172
l execute report sandbox-status on page 4172
execute report flush-cache
Flush report caches
execute report flush-cache
execute report recreate-db
Recreate the report database
execute report recreate-db
FortiOS 8.0.0 CLI Reference
4171
Fortinet Inc.

---


<!-- 来源页 4172 -->
CLI execute commands
execute report run
generate a report, only last 7-days data available
execute report run [layout name] [Start Time] [End Time]
Parameter
Description
Type
Size
[layout name]
Layout name for a report. If not provided, the default layout
will be used.
string
[Start Time]
Start time of the report time period ("yyyy-mm-dd hh").
string
[End Time]
End time of the report time period ("yyyy-mm-dd hh").
string
execute report sandbox-status
sending sandbox status for testing
execute report sandbox-status [status] [sha256]
Parameter
Description
Type
Size
[status]
The status of sandbox returning result
string
[sha256]
SHA256 checksum
string
execute report-config
report-config
This topic includes the following commands:
l execute report-config reset on page 4172
execute report-config reset
Reset report templates to the factory default
execute report-config reset
FortiOS 8.0.0 CLI Reference
4172
Fortinet Inc.

---


<!-- 来源页 4173 -->
CLI execute commands
execute restore
restore
This topic includes the following commands:
l execute restore av ftp on page 4174
l execute restore av tftp on page 4174
l execute restore config dhcp on page 4174
l execute restore config flash on page 4175
l execute restore config ftp on page 4175
l execute restore config management-station normal on page 4175
l execute restore config management-station script on page 4175
l execute restore config management-station template on page 4176
l execute restore config scp on page 4176
l execute restore config tftp on page 4176
l execute restore config usb on page 4177
l execute restore config usb-mode on page 4177
l execute restore image flash on page 4177
l execute restore image ftp on page 4177
l execute restore image management-station on page 4178
l execute restore image scp on page 4178
l execute restore image tftp on page 4178
l execute restore image url on page 4179
l execute restore image usb on page 4179
l execute restore ips ftp on page 4179
l execute restore ips tftp on page 4180
l execute restore ipsuserdefsig ftp on page 4180
l execute restore ipsuserdefsig tftp on page 4180
l execute restore manual-license ftp on page 4181
l execute restore manual-license scp on page 4181
l execute restore manual-license tftp on page 4181
l execute restore other-objects ftp on page 4182
l execute restore other-objects tftp on page 4182
l execute restore script ftp on page 4182
l execute restore script lastlog on page 4183
l execute restore script scp on page 4183
l execute restore script tftp on page 4183
l execute restore secondary-image ftp on page 4184
l execute restore secondary-image tftp on page 4184
l execute restore secondary-image url on page 4184
l execute restore secondary-image usb on page 4185
l execute restore vmlicense ftp on page 4185
FortiOS 8.0.0 CLI Reference
4173
Fortinet Inc.

<!-- 来源页 4174 -->
CLI execute commands
l execute restore vmlicense tftp on page 4185
execute restore av ftp
Restore antivirus database from FTP server.
execute restore av ftp <string> <ftp server>[:ftp port] <Enter>|<user> <passwd>
Parameter
Description
Type
Size
<string>
Antivirus data base file name (path) on the remote
server.
string
<ftp server>[:ftp
port]
FTP server IPv4, IPv6, or FQDN can be attached with
port.
string
<Enter>|<user>
FTP username may be needed.
string
<passwd>
FTP password.
string
execute restore av tftp
Restore antivirus database from TFTP server.
execute restore av tftp <string> <tftp server>
Parameter
Description
Type
Size
<string>
Antivirus database file name on the TFTP server.
string
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
execute restore config dhcp
Load config file via DHCP.
execute restore config dhcp <port> <Enter> | <vlanid>
Parameter
Description
Type
Size
<port>
Port to be DHCP client.
string
<Enter> |
<vlanid>
Enter or specify VLAN ID to create a VLAN on the <port>.
string
FortiOS 8.0.0 CLI Reference
4174
Fortinet Inc.

<!-- 来源页 4175 -->
CLI execute commands
execute restore config flash
Load config file from flash to firewall.
execute restore config flash <revision>
Parameter
Description
Type
Size
<revision>
Revision ID on the flash.
string
execute restore config ftp
Load config file from FTP server.
execute restore config ftp <string> <ftp server>[:ftp port] <Enter>|<user> <passwd>
<Enter>|<passwd>
Parameter
Description
Type
Size
<string>
Configure file name(path) on the remote server.
string
<ftp server>[:ftp
port]
FTP server IPv4, IPv6, or FQDN can be attached with
port.
string
<Enter>|<user>
FTP username may be needed.
string
<passwd>
FTP password.
string
<Enter>|<passwd>
Password may be needed to restore.
string
execute restore config management-station normal
Load normal config file from management station to firewall.
execute restore config management-station normal <revision>
Parameter
Description
Type
Size
<revision>
Revision to retrieve, or enter '0' to get latest revision list.
string
execute restore config management-station script
Load script config file from management station to firewall.
execute restore config management-station script <revision>
FortiOS 8.0.0 CLI Reference
4175
Fortinet Inc.

<!-- 来源页 4176 -->
CLI execute commands
Parameter
Description
Type
Size
<revision>
Revision to retrieve, or enter '0' to get latest revision list.
string
execute restore config management-station template
Load template config file from management station to firewall.
execute restore config management-station template <revision>
Parameter
Description
Type
Size
<revision>
Revision to retrieve, or enter '0' to get latest revision list.
string
execute restore config scp
Restore config file from a SCP server.
execute restore config scp <string> <scp server>[:scp port] <user> <passwd> <Enter>|<passwd>
Parameter
Description
Type
Size
<string>
Configure file name(path) on the remote scp server.
string
<scp server>[:scp
port]
SCP server address (IPv4, [IPv6], or FQDN — port
optional) Supported formats: 192.0.2.1 (IPv4)
192.0.2.1:22 (IPv4 with port) 2001:db8::1 (Raw IPv6)
[2001:db8::1] (IPv6) [2001:db8::1]:22 (IPv6 with
port) host.example.com (FQDN, resolves to IPv4)
[host.example.com] (FQDN, resolves to IPv6)
[host.example.com]:22 (FQDN with port, resolves
to IPv6) * Use square brackets when specifying a
port with an IPv6 address or IPv6-resolving FQDN.
string
<user>
SCP username.
string
<passwd>
SCP password.
string
<Enter>|<passwd>
Password may be needed to restore/backup file.
string
execute restore config tftp
Load config file from TFTP server to firewall.
execute restore config tftp <string> <tftp server> <Enter>|<passwd>
FortiOS 8.0.0 CLI Reference
4176
Fortinet Inc.

<!-- 来源页 4177 -->
CLI execute commands
Parameter
Description
Type
Size
<string>
File name on the TFTP server.
string
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
<Enter>|<passwd>
Password may be needed to restore.
string
execute restore config usb
Load config file from USB disk to firewall.
execute restore config usb <string> <Enter>|<passwd>
Parameter
Description
Type
Size
<string>
File name on USB disk.
string
<Enter>|<passwd>
Password may be needed to restore.
string
execute restore config usb-mode
Load config file from USB disk and reboot.
execute restore config usb-mode <Enter>|<passwd>
Parameter
Description
Type
Size
<Enter>|<passwd>
Optional password to protect.
string
execute restore image flash
Restore image from flash.
execute restore image flash <revision>
Parameter
Description
Type
Size
<revision>
Image revision ID on flash.
string
execute restore image ftp
Load image from FTP server.
execute restore image ftp <string> <ftp server>[:ftp port] <Enter>|<user> <passwd>
FortiOS 8.0.0 CLI Reference
4177
Fortinet Inc.

<!-- 来源页 4178 -->
CLI execute commands
Parameter
Description
Type
Size
<string>
Image file name(path) on the remote server.
string
<ftp server>[:ftp
port]
FTP server IPv4, IPv6, or FQDN can be attached with
port.
string
<Enter>|<user>
FTP username may be needed.
string
<passwd>
FTP password.
string
execute restore image management-station
Restore image from Management station.
execute restore image management-station <string>
Parameter
Description
Type
Size
<string>
Image ID on the server.
string
execute restore image scp
Restore system image from a SCP server.
execute restore image scp <string> <scp server>[:scp port] <user> <passwd>
Parameter
Description
Type
Size
<string>
Configure file name(path) on the remote scp server.
string
<scp server>
[:scp port]
SCP server address (IPv4, [IPv6], or FQDN — port optional)
Supported formats: 192.0.2.1 (IPv4) 192.0.2.1:22 (IPv4
with port) 2001:db8::1 (Raw IPv6) [2001:db8::1] (IPv6)
[2001:db8::1]:22 (IPv6 with port) host.example.com
(FQDN, resolves to IPv4) [host.example.com] (FQDN,
resolves to IPv6) [host.example.com]:22 (FQDN with port,
resolves to IPv6) * Use square brackets when specifying a
port with an IPv6 address or IPv6-resolving FQDN.
string
<user>
SCP username.
string
<passwd>
SCP password.
string
execute restore image tftp
Restore image from TFTP server.
FortiOS 8.0.0 CLI Reference
4178
Fortinet Inc.

<!-- 来源页 4179 -->
CLI execute commands
execute restore image tftp <string> <tftp address>
Parameter
Description
Type
Size
<string>
Image file name on the TFTP server.
string
<tftp
address>
TFTP server IPv4, IPv6, or FQDN.
string
execute restore image url
Restore image from URL with HTTP/HTTPS protocols. Decrypt image if needed.
execute restore image url <string> <Enter>|<passwd>|<force> <Enter>|<force>
Parameter
Description
Type
Size
<string>
URL string with protocol prefix. e.g:
https://example.com/image.aes
string
<Enter>|<passwd>|<force>
Image encryption passphrase.
string
<Enter>|<force>
Bypass signature and validity checking.
string
execute restore image usb
Restore image from USB disk.
execute restore image usb <string>
Parameter
Description
Type
Size
<string>
Image file name on the USB disk.
string
execute restore ips ftp
Restore IPS database from FTP server.
execute restore ips ftp <string> <ftp server>[:ftp port] <Enter>|<user> <passwd>
Parameter
Description
Type
Size
<string>
IPS data base file name (path) on the remote server.
string
FortiOS 8.0.0 CLI Reference
4179
Fortinet Inc.

<!-- 来源页 4180 -->
CLI execute commands
Parameter
Description
Type
Size
<ftp server>[:ftp
port]
FTP server IPv4, IPv6, or FQDN can be attached with
port.
string
<Enter>|<user>
FTP username may be needed.
string
<passwd>
FTP password.
string
execute restore ips tftp
Restore IPS database from TFTP server.
execute restore ips tftp <string> <tftp server>
Parameter
Description
Type
Size
<string>
IPS database file name on the TFTP server.
string
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
execute restore ipsuserdefsig ftp
Restore user-defined ips signatures file from FTP server.
execute restore ipsuserdefsig ftp <string> <ftp server>[:ftp port] <Enter>|<user> <passwd>
Parameter
Description
Type
Size
<string>
User-defined ips signatures file on the remote server.
string
<ftp server>[:ftp
port]
FTP server IPv4, IPv6, or FQDN can be attached with
port.
string
<Enter>|<user>
FTP username may be needed.
string
<passwd>
FTP password.
string
execute restore ipsuserdefsig tftp
Restore user defined IPS signatures file from TFTP server.
execute restore ipsuserdefsig tftp <string> <tftp server>
Parameter
Description
Type
Size
<string>
File name on the TFTP server.
string
FortiOS 8.0.0 CLI Reference
4180
Fortinet Inc.

<!-- 来源页 4181 -->
CLI execute commands
Parameter
Description
Type
Size
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
execute restore manual-license ftp
Restore Manual License from FTP server.
execute restore manual-license ftp <string> <ftp server>[:ftp port] <Enter>|<user> <passwd>
Parameter
Description
Type
Size
<string>
FortiGuard Contract License file name on the FTP
server.
string
<ftp server>[:ftp
port]
FTP server IPv4, IPv6, or FQDN can be attached with
port.
string
<Enter>|<user>
FTP username may be needed.
string
<passwd>
FTP password.
string
execute restore manual-license scp
Restore Manual License from SCP server.
execute restore manual-license scp <string> <scp server>[:scp port] <user> <passwd>
Parameter
Description
Type
Size
<string>
Configure file name(path) on the remote scp server.
string
<scp server>
[:scp port]
SCP server address (IPv4, [IPv6], or FQDN — port optional)
Supported formats: 192.0.2.1 (IPv4) 192.0.2.1:22 (IPv4
with port) 2001:db8::1 (Raw IPv6) [2001:db8::1] (IPv6)
[2001:db8::1]:22 (IPv6 with port) host.example.com
(FQDN, resolves to IPv4) [host.example.com] (FQDN,
resolves to IPv6) [host.example.com]:22 (FQDN with port,
resolves to IPv6) * Use square brackets when specifying a
port with an IPv6 address or IPv6-resolving FQDN.
string
<user>
SCP username.
string
<passwd>
SCP password.
string
execute restore manual-license tftp
Restore Manual License from TFTP server.
FortiOS 8.0.0 CLI Reference
4181
Fortinet Inc.

<!-- 来源页 4182 -->
CLI execute commands
execute restore manual-license tftp <string> <tftp server>
Parameter
Description
Type
Size
<string>
Fortiguard Contract License file name on the TFTP server.
string
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
execute restore other-objects ftp
Restore other FortiGuard packages from FTP server. Current support: Internet-service Database Apps/Maps,
URL Allow List, DLP signatures and CASB signatures.
execute restore other-objects ftp <string> <ftp server>[:ftp port] <Enter>|<user> <passwd>
Parameter
Description
Type
Size
<string>
Other FortiGuard package file name on the FTP server.
string
<ftp server>[:ftp
port]
FTP server IPv4, IPv6, or FQDN can be attached with
port.
string
<Enter>|<user>
FTP username may be needed.
string
<passwd>
FTP password.
string
execute restore other-objects tftp
Restore other FortiGuard packages from TFTP server. Current support: Internet-service Database Apps/Maps,
URL Allow List, DLP signatures and CASB signatures.
execute restore other-objects tftp <string> <tftp server>
Parameter
Description
Type
Size
<string>
Other FortiGuard package file name on the TFTP server.
string
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
execute restore script ftp
Load script from FTP server.
execute restore script ftp <string> <ftp server>[:ftp port] <Enter>|<user> <passwd>
FortiOS 8.0.0 CLI Reference
4182
Fortinet Inc.

<!-- 来源页 4183 -->
CLI execute commands
Parameter
Description
Type
Size
<string>
Script on the remote server.
string
<ftp server>[:ftp
port]
FTP server IPv4, IPv6, or FQDN can be attached with
port.
string
<Enter>|<user>
FTP username may be needed.
string
<passwd>
FTP password.
string
execute restore script lastlog
Read the result of last restored script.
execute restore script lastlog
execute restore script scp
Load script from SCP server to firewall.
execute restore script scp <string> <ip> <user> <Enter>|<passwd>
Parameter
Description
Type
Size
<string>
File name on the SCP server.
string
<ip>
IP address.
string
<user>
User name.
string
<Enter>|<passwd>
Enter or input password.
string
execute restore script tftp
Load script from TFTP server to firewall.
execute restore script tftp <string> <tftp server> <Enter>|<passwd>
Parameter
Description
Type
Size
<string>
File name on the TFTP server.
string
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
<Enter>|<passwd>
Password may be needed to restore.
string
FortiOS 8.0.0 CLI Reference
4183
Fortinet Inc.

<!-- 来源页 4184 -->
CLI execute commands
execute restore secondary-image ftp
Load image from FTP server.
execute restore secondary-image ftp <string> <ftp server>[:ftp port] <Enter>|<user> <passwd>
Parameter
Description
Type
Size
<string>
Image file name(path) on the remote server.
string
<ftp server>[:ftp
port]
FTP server IPv4, IPv6, or FQDN can be attached with
port.
string
<Enter>|<user>
FTP username may be needed.
string
<passwd>
FTP password.
string
execute restore secondary-image tftp
Restore image from TFTP server.
execute restore secondary-image tftp <string> <tftp address>
Parameter
Description
Type
Size
<string>
Image file name on the TFTP server.
string
<tftp
address>
TFTP server IPv4, IPv6, or FQDN.
string
execute restore secondary-image url
Restore image from URL with HTTP/HTTPS protocols. Decrypt image if needed.
execute restore secondary-image url <string> <Enter>|<passwd>|<force> <Enter>|<force>
Parameter
Description
Type
Size
<string>
URL string with protocol prefix. e.g:
https://example.com/image.aes
string
<Enter>|<passwd>|<force>
Image encryption passphrase.
string
<Enter>|<force>
Bypass signature and validity checking.
string
FortiOS 8.0.0 CLI Reference
4184
Fortinet Inc.

---


<!-- 来源页 4185 -->
CLI execute commands
execute restore secondary-image usb
Restore image from USB disk.
execute restore secondary-image usb <string>
Parameter
Description
Type
Size
<string>
Image file name on the USB disk.
string
execute restore vmlicense ftp
Restore VM license from FTP server.
execute restore vmlicense ftp <string> <ftp server>[:ftp port] <Enter>|<user> <passwd>
Parameter
Description
Type
Size
<string>
VM license file name(path) on the remote server.
string
<ftp server>[:ftp
port]
FTP server IPv4, IPv6, or FQDN can be attached with
port.
string
<Enter>|<user>
FTP username may be needed.
string
<passwd>
FTP password.
string
execute restore vmlicense tftp
restore VM license from tftp server
execute restore vmlicense tftp <string> <tftp server>
Parameter
Description
Type
Size
<string>
VM license file name on the tftp server
string
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
execute revision
revision
This topic includes the following commands:
FortiOS 8.0.0 CLI Reference
4185
Fortinet Inc.

<!-- 来源页 4186 -->
CLI execute commands
l execute revision delete config on page 4186
l execute revision delete image on page 4186
l execute revision list config on page 4186
l execute revision list image on page 4186
execute revision delete config
Delete config revision on local disk.
execute revision delete config <revision> <rev_id>
Parameter
Description
Type
Size
<revision>
Revision ID(s) on local disk. Eg. 1 3-6 8
string
<rev_id>
place holder for multiple Revision IDs, at most 10 a time.
string
execute revision delete image
Delete image revision on local disk.
execute revision delete image <revision> <rev_id>
Parameter
Description
Type
Size
<revision>
Revision ID(s) on local disk. Eg. 1 3-6 8
string
<rev_id>
place holder for multiple Revision IDs, at most 10 a time.
string
execute revision list config
List config revision on local disk.
execute revision list config
execute revision list image
List image revision on local disk.
execute revision list image
FortiOS 8.0.0 CLI Reference
4186
Fortinet Inc.

---


<!-- 来源页 4187 -->
CLI execute commands
execute router
router
This topic includes the following commands:
l execute router clear bfd session on page 4187
l execute router clear bgp all on page 4187
l execute router clear bgp as on page 4187
l execute router clear bgp dampening on page 4188
l execute router clear bgp external on page 4188
l execute router clear bgp flap-statistics on page 4188
l execute router clear bgp group on page 4188
l execute router clear bgp ip on page 4188
l execute router clear bgp ipv6 on page 4188
l execute router clear ospf process on page 4189
l execute router clear ospf6 process on page 4189
l execute router restart on page 4189
execute router clear bfd session
Clear BFD session.
execute router clear bfd session <xxx.xxx.xxx.xxx> <xxx.xxx.xxx.xxx> <string>
Parameter
Description
Type
Size
<xxx.xxx.xxx.xxx>
Source IP address.
string
<xxx.xxx.xxx.xxx>
Destination IP address.
string
<string>
Interface name.
string
execute router clear bgp all
Clear all BGP peers.
execute router clear bgp all
execute router clear bgp as
Clear BGP peer by AS number.
FortiOS 8.0.0 CLI Reference
4187
Fortinet Inc.

<!-- 来源页 4188 -->
CLI execute commands
execute router clear bgp as
execute router clear bgp dampening
Clear route flap dampening information.
execute router clear bgp dampening
execute router clear bgp external
Clear all external peers.
execute router clear bgp external
execute router clear bgp flap-statistics
Clear route flap statistics.
execute router clear bgp flap-statistics
execute router clear bgp group
Clear BGP peer by group.
execute router clear bgp group
execute router clear bgp ip
Clear BGP peer by IP address.
execute router clear bgp ip
execute router clear bgp ipv6
Clear BGP peer by IPv6 address.
execute router clear bgp ipv6
FortiOS 8.0.0 CLI Reference
4188
Fortinet Inc.

---


<!-- 来源页 4189 -->
CLI execute commands
execute router clear ospf process
Clear and restart OSPF router.
execute router clear ospf process
execute router clear ospf6 process
Clear and restart OSPF6 router.
execute router clear ospf6 process
execute router restart
Restart routing software.
execute router restart
execute sdn
sdn
This topic includes the following commands:
l execute sdn tag add nsx on page 4189
l execute sdn tag remove nsx on page 4190
execute sdn tag add nsx
NSX tag VM.
execute sdn tag add nsx <name> <ip-addr> <tagname> <0/1>
Parameter
Description
Type
Size
<name>
NSX SDN connector name.
string
<ip-addr>
VM IP address.
string
<tagname>
Tag name.
string
<0/1>
Disable/enable use of Spoofguard.
string
FortiOS 8.0.0 CLI Reference
4189
Fortinet Inc.

---


<!-- 来源页 4190 -->
CLI execute commands
execute sdn tag remove nsx
NSX remove VM from tag.
execute sdn tag remove nsx <name> <ip-addr> <tagname> <0/1>
Parameter
Description
Type
Size
<name>
NSX SDN connector name.
string
<ip-addr>
VM IP address.
string
<tagname>
Tag name.
string
<0/1>
Disable/enable use of Spoofguard.
string
execute sdn-vpn
sdn-vpn
This topic includes the following commands:
l execute sdn-vpn discover aws-tgw on page 4190
l execute sdn-vpn discover aws-vgw on page 4190
execute sdn-vpn discover aws-tgw
Discover AWS virtual private gateways.
execute sdn-vpn discover aws-tgw <name>
Parameter
Description
Type
Size
<name>
SDN Connector name.
string
execute sdn-vpn discover aws-vgw
Discover AWS virtual private gateways.
execute sdn-vpn discover aws-vgw <name>
Parameter
Description
Type
Size
<name>
SDN Connector name.
string
FortiOS 8.0.0 CLI Reference
4190
Fortinet Inc.

---


<!-- 来源页 4191 -->
CLI execute commands
execute send-fds-statistics
Send FortiGuard statistics.
execute send-fds-statistics
execute send-fmg-list
Send connected FortiManager list to FortiGuard.
execute send-fmg-list
execute sensor
sensor
This topic includes the following commands:
l execute sensor detail on page 4191
l execute sensor list on page 4191
execute sensor detail
List detailed sensors and readings
execute sensor detail
execute sensor list
List sensors and readings
execute sensor list
FortiOS 8.0.0 CLI Reference
4191
Fortinet Inc.

---


<!-- 来源页 4191 -->
CLI execute commands
execute send-fds-statistics
Send FortiGuard statistics.
execute send-fds-statistics
execute send-fmg-list
Send connected FortiManager list to FortiGuard.
execute send-fmg-list
execute sensor
sensor
This topic includes the following commands:
l execute sensor detail on page 4191
l execute sensor list on page 4191
execute sensor detail
List detailed sensors and readings
execute sensor detail
execute sensor list
List sensors and readings
execute sensor list
FortiOS 8.0.0 CLI Reference
4191
Fortinet Inc.

---


<!-- 来源页 4191 -->
CLI execute commands
execute send-fds-statistics
Send FortiGuard statistics.
execute send-fds-statistics
execute send-fmg-list
Send connected FortiManager list to FortiGuard.
execute send-fmg-list
execute sensor
sensor
This topic includes the following commands:
l execute sensor detail on page 4191
l execute sensor list on page 4191
execute sensor detail
List detailed sensors and readings
execute sensor detail
execute sensor list
List sensors and readings
execute sensor list
FortiOS 8.0.0 CLI Reference
4191
Fortinet Inc.

---


<!-- 来源页 4192 -->
CLI execute commands
execute set
set
This topic includes the following commands:
l execute set system session filter clear all on page 4192
l execute set system session filter clear dport on page 4193
l execute set system session filter clear dst on page 4193
l execute set system session filter clear duration on page 4193
l execute set system session filter clear expire on page 4193
l execute set system session filter clear policy on page 4193
l execute set system session filter clear proto on page 4193
l execute set system session filter clear sport on page 4194
l execute set system session filter clear src on page 4194
l execute set system session filter clear vd on page 4194
l execute set system session filter dport on page 4194
l execute set system session filter dst on page 4194
l execute set system session filter duration on page 4195
l execute set system session filter expire on page 4195
l execute set system session filter list on page 4195
l execute set system session filter negate dport on page 4195
l execute set system session filter negate dst on page 4195
l execute set system session filter negate duration on page 4196
l execute set system session filter negate expire on page 4196
l execute set system session filter negate policy on page 4196
l execute set system session filter negate proto on page 4196
l execute set system session filter negate sport on page 4196
l execute set system session filter negate src on page 4196
l execute set system session filter negate vd on page 4197
l execute set system session filter policy on page 4197
l execute set system session filter proto on page 4197
l execute set system session filter sport on page 4197
l execute set system session filter src on page 4198
l execute set system session filter vd on page 4198
execute set system session filter clear all
Clear session filter.
execute set system session filter clear all
FortiOS 8.0.0 CLI Reference
4192
Fortinet Inc.

<!-- 来源页 4193 -->
CLI execute commands
execute set system session filter clear dport
Clear destination port.
execute set system session filter clear dport
execute set system session filter clear dst
Clear destination IP.
execute set system session filter clear dst
execute set system session filter clear duration
Clear duration.
execute set system session filter clear duration
execute set system session filter clear expire
Clear expire.
execute set system session filter clear expire
execute set system session filter clear policy
Clear policy ID.
execute set system session filter clear policy
execute set system session filter clear proto
Clear protocol.
execute set system session filter clear proto
FortiOS 8.0.0 CLI Reference
4193
Fortinet Inc.

<!-- 来源页 4194 -->
CLI execute commands
execute set system session filter clear sport
Clear source port.
execute set system session filter clear sport
execute set system session filter clear src
Clear source IP.
execute set system session filter clear src
execute set system session filter clear vd
Clear virtual domain.
execute set system session filter clear vd
execute set system session filter dport
Destination port.
execute set system session filter dport <xxxx> <xxxx>
Parameter
Description
Type
Size
<xxxx>
<0-65535> (from).
string
<xxxx>
<0-65535> (to).
string
execute set system session filter dst
Destination IP address.
execute set system session filter dst <xxx.xxx.xxx.xxx> <xxx.xxx.xxx.xxx>
Parameter
Description
Type
Size
<xxx.xxx.xxx.xxx>
Destination IP (from).
string
<xxx.xxx.xxx.xxx>
Destination IP (to).
string
FortiOS 8.0.0 CLI Reference
4194
Fortinet Inc.

<!-- 来源页 4195 -->
CLI execute commands
execute set system session filter duration
duration
execute set system session filter duration <xxx> <xxx>
Parameter
Description
Type
Size
<xxx>
Duration (from).
string
<xxx>
Duration (to).
string
execute set system session filter expire
expire
execute set system session filter expire <xxx> <xxx>
Parameter
Description
Type
Size
<xxx>
Expire (from).
string
<xxx>
Expire (to).
string
execute set system session filter list
List system session filter.
execute set system session filter list
execute set system session filter negate dport
Inverse destination port.
execute set system session filter negate dport
execute set system session filter negate dst
Inverse destination IP.
execute set system session filter negate dst
FortiOS 8.0.0 CLI Reference
4195
Fortinet Inc.

<!-- 来源页 4196 -->
CLI execute commands
execute set system session filter negate duration
Inverse duration.
execute set system session filter negate duration
execute set system session filter negate expire
Inverse expire.
execute set system session filter negate expire
execute set system session filter negate policy
Inverse policy ID.
execute set system session filter negate policy
execute set system session filter negate proto
Inverse protocol.
execute set system session filter negate proto
execute set system session filter negate sport
Inverse source port.
execute set system session filter negate sport
execute set system session filter negate src
Inverse source IP.
execute set system session filter negate src
FortiOS 8.0.0 CLI Reference
4196
Fortinet Inc.

<!-- 来源页 4197 -->
CLI execute commands
execute set system session filter negate vd
Inverse virtual domain.
execute set system session filter negate vd
execute set system session filter policy
Policy ID.
execute set system session filter policy <xxx> <xxx>
Parameter
Description
Type
Size
<xxx>
Policy ID (from).
string
<xxx>
Policy ID (to).
string
execute set system session filter proto
Protocol number.
execute set system session filter proto <xx> <xx>
Parameter
Description
Type
Size
<xx>
<0-255> (from).
string
<xx>
<0-255> (to).
string
execute set system session filter sport
Source port.
execute set system session filter sport <xxxx> <xxxx>
Parameter
Description
Type
Size
<xxxx>
<0-65535> (from).
string
<xxxx>
<0-65535> (to).
string
FortiOS 8.0.0 CLI Reference
4197
Fortinet Inc.

---


<!-- 来源页 4198 -->
CLI execute commands
execute set system session filter src
Source IP address.
execute set system session filter src <xxx.xxx.xxx.xxx> <xxx.xxx.xxx.xxx>
Parameter
Description
Type
Size
<xxx.xxx.xxx.xxx>
Source IP (from).
string
<xxx.xxx.xxx.xxx>
Source IP (to).
string
execute set system session filter vd
Index of virtual domain. -1 matches all.
execute set system session filter vd <xxx>
Parameter
Description
Type
Size
<xxx>
Index of virtual domain. -1 matches all.
string
execute set-next-reboot
set-next-reboot
This topic includes the following commands:
l execute set-next-reboot primary on page 4198
l execute set-next-reboot secondary on page 4198
execute set-next-reboot primary
partition
execute set-next-reboot primary
execute set-next-reboot secondary
partition
execute set-next-reboot secondary
FortiOS 8.0.0 CLI Reference
4198
Fortinet Inc.

---


<!-- 来源页 4199 -->
CLI execute commands
execute shutdown
Shutdown now.
execute shutdown <comment> <string>
Parameter
Description
Type
Size
<comment>
comment
string
<string>
Shutdown comments.
string
execute speed-test
A bandwidth measuring tool.
execute speed-test <interface> <mode> <max-up> <min-up> <max-down> <min-down>
Parameter
Description
Type
Size
<interface>
Testing interface name.
string
<mode>
optional, Auto(default), TCP or UDP.
string
<max-up>
interger, Expected maximum outbandwidth(kpbs).
string
<min-up>
interger, Expected minimum outbandwidth(kpbs).
string
<max-down>
interger, Expected maximum inbandwidth(kpbs).
string
<min-down>
interger, Expected minimum inbandwidth(kpbs).
string
execute speed-test-custom
Run speed test to a custom server.
execute speed-test-custom <interface> <server>
Parameter
Description
Type
Size
<interface>
Speed test interface.
string
<server>
Server address.
string
FortiOS 8.0.0 CLI Reference
4199
Fortinet Inc.

---


<!-- 来源页 4199 -->
CLI execute commands
execute shutdown
Shutdown now.
execute shutdown <comment> <string>
Parameter
Description
Type
Size
<comment>
comment
string
<string>
Shutdown comments.
string
execute speed-test
A bandwidth measuring tool.
execute speed-test <interface> <mode> <max-up> <min-up> <max-down> <min-down>
Parameter
Description
Type
Size
<interface>
Testing interface name.
string
<mode>
optional, Auto(default), TCP or UDP.
string
<max-up>
interger, Expected maximum outbandwidth(kpbs).
string
<min-up>
interger, Expected minimum outbandwidth(kpbs).
string
<max-down>
interger, Expected maximum inbandwidth(kpbs).
string
<min-down>
interger, Expected minimum inbandwidth(kpbs).
string
execute speed-test-custom
Run speed test to a custom server.
execute speed-test-custom <interface> <server>
Parameter
Description
Type
Size
<interface>
Speed test interface.
string
<server>
Server address.
string
FortiOS 8.0.0 CLI Reference
4199
Fortinet Inc.

---


<!-- 来源页 4199 -->
CLI execute commands
execute shutdown
Shutdown now.
execute shutdown <comment> <string>
Parameter
Description
Type
Size
<comment>
comment
string
<string>
Shutdown comments.
string
execute speed-test
A bandwidth measuring tool.
execute speed-test <interface> <mode> <max-up> <min-up> <max-down> <min-down>
Parameter
Description
Type
Size
<interface>
Testing interface name.
string
<mode>
optional, Auto(default), TCP or UDP.
string
<max-up>
interger, Expected maximum outbandwidth(kpbs).
string
<min-up>
interger, Expected minimum outbandwidth(kpbs).
string
<max-down>
interger, Expected maximum inbandwidth(kpbs).
string
<min-down>
interger, Expected minimum inbandwidth(kpbs).
string
execute speed-test-custom
Run speed test to a custom server.
execute speed-test-custom <interface> <server>
Parameter
Description
Type
Size
<interface>
Speed test interface.
string
<server>
Server address.
string
FortiOS 8.0.0 CLI Reference
4199
Fortinet Inc.

---


<!-- 来源页 4200 -->
CLI execute commands
execute speed-test-ipsec
Measure the bandwidth of the underlay of a IPSec tunnel.
execute speed-test-ipsec <interface> <tunnel_name>
Parameter
Description
Type
Size
<interface>
ipsec phase1 interface.
string
<tunnel_
name>
all | <specific tunnel name>.
string
execute speed-test-legacy
A bandwidth measuring tool.
execute speed-test-legacy <interface> <server> <mode>
Parameter
Description
Type
Size
<interface>
auto | <outgoing interface name>.
string
<server>
server name.
string
<mode>
optional, TCP or UDP.
string
execute speed-test-options
speed-test-options
This topic includes the following commands:
l execute speed-test-options blksize on page 4201
l execute speed-test-options burst on page 4201
l execute speed-test-options ctrl-port on page 4201
l execute speed-test-options duration on page 4201
l execute speed-test-options get-token on page 4202
l execute speed-test-options max-down on page 4202
l execute speed-test-options max-up on page 4202
l execute speed-test-options num-stream on page 4202
l execute speed-test-options protocol on page 4203
FortiOS 8.0.0 CLI Reference
4200
Fortinet Inc.

---


<!-- 来源页 4200 -->
CLI execute commands
execute speed-test-ipsec
Measure the bandwidth of the underlay of a IPSec tunnel.
execute speed-test-ipsec <interface> <tunnel_name>
Parameter
Description
Type
Size
<interface>
ipsec phase1 interface.
string
<tunnel_
name>
all | <specific tunnel name>.
string
execute speed-test-legacy
A bandwidth measuring tool.
execute speed-test-legacy <interface> <server> <mode>
Parameter
Description
Type
Size
<interface>
auto | <outgoing interface name>.
string
<server>
server name.
string
<mode>
optional, TCP or UDP.
string
execute speed-test-options
speed-test-options
This topic includes the following commands:
l execute speed-test-options blksize on page 4201
l execute speed-test-options burst on page 4201
l execute speed-test-options ctrl-port on page 4201
l execute speed-test-options duration on page 4201
l execute speed-test-options get-token on page 4202
l execute speed-test-options max-down on page 4202
l execute speed-test-options max-up on page 4202
l execute speed-test-options num-stream on page 4202
l execute speed-test-options protocol on page 4203
FortiOS 8.0.0 CLI Reference
4200
Fortinet Inc.

---


<!-- 来源页 4200 -->
CLI execute commands
execute speed-test-ipsec
Measure the bandwidth of the underlay of a IPSec tunnel.
execute speed-test-ipsec <interface> <tunnel_name>
Parameter
Description
Type
Size
<interface>
ipsec phase1 interface.
string
<tunnel_
name>
all | <specific tunnel name>.
string
execute speed-test-legacy
A bandwidth measuring tool.
execute speed-test-legacy <interface> <server> <mode>
Parameter
Description
Type
Size
<interface>
auto | <outgoing interface name>.
string
<server>
server name.
string
<mode>
optional, TCP or UDP.
string
execute speed-test-options
speed-test-options
This topic includes the following commands:
l execute speed-test-options blksize on page 4201
l execute speed-test-options burst on page 4201
l execute speed-test-options ctrl-port on page 4201
l execute speed-test-options duration on page 4201
l execute speed-test-options get-token on page 4202
l execute speed-test-options max-down on page 4202
l execute speed-test-options max-up on page 4202
l execute speed-test-options num-stream on page 4202
l execute speed-test-options protocol on page 4203
FortiOS 8.0.0 CLI Reference
4200
Fortinet Inc.

<!-- 来源页 4201 -->
CLI execute commands
l execute speed-test-options reset on page 4203
l execute speed-test-options reset-token on page 4203
l execute speed-test-options server-port on page 4203
l execute speed-test-options set-shaper on page 4203
l execute speed-test-options show on page 4204
l execute speed-test-options tos on page 4204
execute speed-test-options blksize
Set blksize.
execute speed-test-options blksize <blksize>
Parameter
Description
Type
Size
<blksize>
0-2147483647
string
execute speed-test-options burst
Set number of burst packet in UDP test.
execute speed-test-options burst <burst>
Parameter
Description
Type
Size
<burst>
0-2147483647
string
execute speed-test-options ctrl-port
Set test controller port.
execute speed-test-options ctrl-port <port>
Parameter
Description
Type
Size
<port>
0-65535
string
execute speed-test-options duration
Set test duration in seconds.
execute speed-test-options duration <duration>
FortiOS 8.0.0 CLI Reference
4201
Fortinet Inc.

<!-- 来源页 4202 -->
CLI execute commands
Parameter
Description
Type
Size
<duration>
5-2147483647
string
execute speed-test-options get-token
Obtain test token via ipsec tunnel.
execute speed-test-options get-token
execute speed-test-options max-down
Set maximum downloading rate (kbps).
execute speed-test-options max-down <max-down>
Parameter
Description
Type
Size
<max-down>
0-2147483647
string
execute speed-test-options max-up
Set maximum uploading rate (kbps).
execute speed-test-options max-up <max-up>
Parameter
Description
Type
Size
<max-up>
0-2147483647
string
execute speed-test-options num-stream
Set number of streams in TCP test.
execute speed-test-options num-stream <num_stream>
Parameter
Description
Type
Size
<num_
stream>
1-100
string
FortiOS 8.0.0 CLI Reference
4202
Fortinet Inc.

<!-- 来源页 4203 -->
CLI execute commands
execute speed-test-options protocol
Set protocol.
execute speed-test-options protocol <protocol>
Parameter
Description
Type
Size
<protocol>
TCP or UDP
string
execute speed-test-options reset
Reset options to default.
execute speed-test-options reset
execute speed-test-options reset-token
Reset saved token.
execute speed-test-options reset-token
execute speed-test-options server-port
Set test server port.
execute speed-test-options server-port <port>
Parameter
Description
Type
Size
<port>
0-65535
string
execute speed-test-options set-shaper
Notify server to set egress shaper based on test results.
execute speed-test-options set-shaper <enable | disable>
Parameter
Description
Type
Size
<enable |
disable>
<enable | disable>
string
FortiOS 8.0.0 CLI Reference
4203
Fortinet Inc.

---


<!-- 来源页 4204 -->
CLI execute commands
execute speed-test-options show
Show options.
execute speed-test-options show
execute speed-test-options tos
Set TOS.
execute speed-test-options tos <tos>
Parameter
Description
Type
Size
<tos>
TOS
string
execute speed-test-server
speed-test-server
This topic includes the following commands:
l execute speed-test-server download on page 4204
l execute speed-test-server list on page 4204
execute speed-test-server download
Download server list from FortiGate Cloud.
execute speed-test-server download
execute speed-test-server list
List all available servers.
execute speed-test-server list
FortiOS 8.0.0 CLI Reference
4204
Fortinet Inc.

---


<!-- 来源页 4205 -->
CLI execute commands
execute ssh
Simple SSH client.
execute ssh <user@host> <port>
Parameter
Description
Type
Size
<user@host>
User-name @ IP address or domain name.
string
<port>
port.
string
execute ssh6
Simple IPv6 SSH client.
execute ssh6 <user@host> <port>
Parameter
Description
Type
Size
<user@host>
User-name @ IPv6 address or domain name.
string
<port>
port.
string
execute ssh6-options
ssh6-options
This topic includes the following commands:
l execute ssh6-options interface on page 4205
l execute ssh6-options reset on page 4206
l execute ssh6-options source6 on page 4206
l execute ssh6-options view-settings on page 4206
execute ssh6-options interface
Auto | <outgoing interface>.
execute ssh6-options interface <string>
FortiOS 8.0.0 CLI Reference
4205
Fortinet Inc.

---


<!-- 来源页 4205 -->
CLI execute commands
execute ssh
Simple SSH client.
execute ssh <user@host> <port>
Parameter
Description
Type
Size
<user@host>
User-name @ IP address or domain name.
string
<port>
port.
string
execute ssh6
Simple IPv6 SSH client.
execute ssh6 <user@host> <port>
Parameter
Description
Type
Size
<user@host>
User-name @ IPv6 address or domain name.
string
<port>
port.
string
execute ssh6-options
ssh6-options
This topic includes the following commands:
l execute ssh6-options interface on page 4205
l execute ssh6-options reset on page 4206
l execute ssh6-options source6 on page 4206
l execute ssh6-options view-settings on page 4206
execute ssh6-options interface
Auto | <outgoing interface>.
execute ssh6-options interface <string>
FortiOS 8.0.0 CLI Reference
4205
Fortinet Inc.

---


<!-- 来源页 4205 -->
CLI execute commands
execute ssh
Simple SSH client.
execute ssh <user@host> <port>
Parameter
Description
Type
Size
<user@host>
User-name @ IP address or domain name.
string
<port>
port.
string
execute ssh6
Simple IPv6 SSH client.
execute ssh6 <user@host> <port>
Parameter
Description
Type
Size
<user@host>
User-name @ IPv6 address or domain name.
string
<port>
port.
string
execute ssh6-options
ssh6-options
This topic includes the following commands:
l execute ssh6-options interface on page 4205
l execute ssh6-options reset on page 4206
l execute ssh6-options source6 on page 4206
l execute ssh6-options view-settings on page 4206
execute ssh6-options interface
Auto | <outgoing interface>.
execute ssh6-options interface <string>
FortiOS 8.0.0 CLI Reference
4205
Fortinet Inc.

---


<!-- 来源页 4206 -->
CLI execute commands
Parameter
Description
Type
Size
<string>
Auto | <outgoing interface>.
string
execute ssh6-options reset
Reset settings.
execute ssh6-options reset
execute ssh6-options source6
Auto | <source interface IPv6>.
execute ssh6-options source6 <xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx>
Parameter
Description
Type
Size
<xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx>
<source interface IPv6> | Auto
string
execute ssh6-options view-settings
View current settings for SSH (IPv6) option.
execute ssh6-options view-settings
execute ssh-options
ssh-options
This topic includes the following commands:
l execute ssh-options interface on page 4206
l execute ssh-options reset on page 4207
l execute ssh-options source on page 4207
l execute ssh-options view-settings on page 4207
execute ssh-options interface
Auto | <outgoing interface>.
FortiOS 8.0.0 CLI Reference
4206
Fortinet Inc.

---


<!-- 来源页 4207 -->
CLI execute commands
execute ssh-options interface <string>
Parameter
Description
Type
Size
<string>
Auto | <outgoing interface>.
string
execute ssh-options reset
Reset settings.
execute ssh-options reset
execute ssh-options source
Auto | <source interface IP>.
execute ssh-options source <xxx.xxx.xxx.xxx>
Parameter
Description
Type
Size
<xxx.xxx.xxx.xxx>
<source interface IP> | Auto
string
execute ssh-options view-settings
View the current settings for SSH option.
execute ssh-options view-settings
execute ssh-regen-keys
Regenerate SSH server keys.
execute ssh-regen-keys
execute switch-controller
switch-controller
FortiOS 8.0.0 CLI Reference
4207
Fortinet Inc.

---


<!-- 来源页 4207 -->
CLI execute commands
execute ssh-options interface <string>
Parameter
Description
Type
Size
<string>
Auto | <outgoing interface>.
string
execute ssh-options reset
Reset settings.
execute ssh-options reset
execute ssh-options source
Auto | <source interface IP>.
execute ssh-options source <xxx.xxx.xxx.xxx>
Parameter
Description
Type
Size
<xxx.xxx.xxx.xxx>
<source interface IP> | Auto
string
execute ssh-options view-settings
View the current settings for SSH option.
execute ssh-options view-settings
execute ssh-regen-keys
Regenerate SSH server keys.
execute ssh-regen-keys
execute switch-controller
switch-controller
FortiOS 8.0.0 CLI Reference
4207
Fortinet Inc.

<!-- 来源页 4208 -->
CLI execute commands
This topic includes the following commands:
l execute switch-controller custom-command on page 4209
l execute switch-controller diagnose-connection on page 4210
l execute switch-controller diagnose-connection-v6 on page 4210
l execute switch-controller dsl reset on page 4210
l execute switch-controller dsl update ftp on page 4210
l execute switch-controller dsl update tftp on page 4211
l execute switch-controller flapguard reset on page 4211
l execute switch-controller get-component-status on page 4211
l execute switch-controller get-conn-status on page 4212
l execute switch-controller get-physical-conn dot on page 4212
l execute switch-controller get-physical-conn standard on page 4212
l execute switch-controller get-sync-status all on page 4212
l execute switch-controller get-sync-status group on page 4213
l execute switch-controller get-sync-status serial on page 4213
l execute switch-controller get-sync-status switch-id on page 4213
l execute switch-controller get-upgrade-status on page 4213
l execute switch-controller ssh on page 4213
l execute switch-controller switch-action 802-1X clear-auth-mac on page 4214
l execute switch-controller switch-action 802-1X clear-auth-port on page 4214
l execute switch-controller switch-action bpdu-guard reset on page 4214
l execute switch-controller switch-action cable-diag on page 4215
l execute switch-controller switch-action factory-reset on page 4215
l execute switch-controller switch-action flow-tracking delete-flows-all on page 4215
l execute switch-controller switch-action flow-tracking expire-flows-all on page 4215
l execute switch-controller switch-action igmp-snoop clear-learned on page 4216
l execute switch-controller switch-action loop-guard reset on page 4216
l execute switch-controller switch-action mac-device-reset dynamic on page 4216
l execute switch-controller switch-action mac-device-reset nac on page 4216
l execute switch-controller switch-action mac-limit-violation reset all on page 4217
l execute switch-controller switch-action mac-limit-violation reset interface on page 4217
l execute switch-controller switch-action mac-limit-violation reset vlan on page 4217
l execute switch-controller switch-action mclag stats clear icl on page 4218
l execute switch-controller switch-action mclag stats clear mlag on page 4218
l execute switch-controller switch-action physical-ports led-flash switch-group on page 4218
l execute switch-controller switch-action physical-ports led-flash switch-id on page 4219
l execute switch-controller switch-action physical-ports led-flash tier1 on page 4219
l execute switch-controller switch-action physical-ports led-flash tier2plus on page 4219
l execute switch-controller switch-action poe reset on page 4219
l execute switch-controller switch-action restart delay all on page 4220
l execute switch-controller switch-action restart delay switch-group on page 4220
l execute switch-controller switch-action restart delay switch-id on page 4220
FortiOS 8.0.0 CLI Reference
4208
Fortinet Inc.

<!-- 来源页 4209 -->
CLI execute commands
l execute switch-controller switch-action restart swtp all on page 4220
l execute switch-controller switch-action restart swtp switch-group on page 4221
l execute switch-controller switch-action restart swtp switch-id on page 4221
l execute switch-controller switch-action set-standalone on page 4221
l execute switch-controller switch-action sticky-mac delete-unsaved all on page 4221
l execute switch-controller switch-action sticky-mac delete-unsaved interface on page 4222
l execute switch-controller switch-action sticky-mac save all on page 4222
l execute switch-controller switch-action sticky-mac save interface on page 4222
l execute switch-controller switch-software cancel all on page 4223
l execute switch-controller switch-software cancel switch-group on page 4223
l execute switch-controller switch-software cancel switch-id on page 4223
l execute switch-controller switch-software delete on page 4223
l execute switch-controller switch-software list-available on page 4224
l execute switch-controller switch-software stage all on page 4224
l execute switch-controller switch-software stage switch-group on page 4224
l execute switch-controller switch-software stage switch-id on page 4224
l execute switch-controller switch-software upgrade on page 4225
l execute switch-controller switch-software upload ftp on page 4225
l execute switch-controller switch-software upload tftp on page 4225
l execute switch-controller virtual-port-pool request on page 4225
l execute switch-controller virtual-port-pool return on page 4226
l execute switch-controller virtual-port-pool show on page 4226
l execute switch-controller virtual-port-pool show-by-pool on page 4226
l execute switch-controller virtual-port-pool show-by-property on page 4226
l execute switch-controller virtual-port-pool show-by-tag on page 4227
execute switch-controller custom-command
Push a FortiSwitch custom command to a FortiSwitch device.
execute switch-controller custom-command <cmd-name> <target-switch>
Parameter
Description
Type
Size
<cmd-name>
Names of commands to be pushed to this FortiSwitch
device, as configured under config switch-controller
custom-command.
string
<target-switch>
FortiSwitch device to push the custom command to.
string
FortiOS 8.0.0 CLI Reference
4209
Fortinet Inc.

<!-- 来源页 4210 -->
CLI execute commands
execute switch-controller diagnose-connection
Get FortiSwitch connection diagnostics.
execute switch-controller diagnose-connection <switch>
Parameter
Description
Type
Size
<switch>
FortiSwitch device ID.
string
execute switch-controller diagnose-connection-v6
Get FortiSwitch IPv6 connection diagnostics.
execute switch-controller diagnose-connection-v6 <switch>
Parameter
Description
Type
Size
<switch>
FortiSwitch device ID.
string
execute switch-controller dsl reset
Reset DSL module on port of FortiSwitch.
execute switch-controller dsl reset <switch> <port>
Parameter
Description
Type
Size
<switch>
FortiSwitch device ID.
string
<port>
FortiSwitch port.
string
execute switch-controller dsl update ftp
Upload a DSL image from FTP server.
execute switch-controller dsl update ftp <string> <ftp server>[:ftp port] <Enter>|<user> <passwd>
<switch> <port>
Parameter
Description
Type
Size
<string>
DSL image name on the FTP server.
string
FortiOS 8.0.0 CLI Reference
4210
Fortinet Inc.

<!-- 来源页 4211 -->
CLI execute commands
Parameter
Description
Type
Size
<ftp server>[:ftp
port]
FTP server IPv4, IPv6, or FQDN can be attached with
port.
string
<Enter>|<user>
FTP username may be needed.
string
<passwd>
FTP password.
string
<switch>
FortiSwitch device ID.
string
<port>
FortiSwitch port.
string
execute switch-controller dsl update tftp
Upload a DSL image from TFTP server.
execute switch-controller dsl update tftp <string> <tftp server> <switch> <port>
Parameter
Description
Type
Size
<string>
DSL image name on the TFTP server.
string
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
<switch>
FortiSwitch device ID.
string
<port>
FortiSwitch port.
string
execute switch-controller flapguard reset
Reset flapguard on port.
execute switch-controller flapguard reset
<switch-name> <port>
Parameter
Description
Type
Size
<switch-name>
Name.
string
<port>
FortiSwitch port.
string
execute switch-controller get-component-status
Get FortiSwitch component status.
execute switch-controller get-component-status <switch>
FortiOS 8.0.0 CLI Reference
4211
Fortinet Inc.

<!-- 来源页 4212 -->
CLI execute commands
Parameter
Description
Type
Size
<switch>
FortiSwitch device ID.
string
execute switch-controller get-conn-status
Get FortiSwitch connection status.
execute switch-controller get-conn-status <switch>
Parameter
Description
Type
Size
<switch>
FortiSwitch device ID.
string
execute switch-controller get-physical-conn dot
Get FortiLink connectivity graph in dot output format.
execute switch-controller get-physical-conn dot <fortilink-name>
Parameter
Description
Type
Size
<fortilink-name>
FortiLink name.
string
execute switch-controller get-physical-conn standard
Get FortiLink connectivity graph in standard output format.
execute switch-controller get-physical-conn standard <fortilink-name>
Parameter
Description
Type
Size
<fortilink-name>
FortiLink name.
string
execute switch-controller get-sync-status all
Get FortiSwitch sync status.
execute switch-controller get-sync-status all
FortiOS 8.0.0 CLI Reference
4212
Fortinet Inc.

<!-- 来源页 4213 -->
CLI execute commands
execute switch-controller get-sync-status group
Get FortiSwitch sync status by group.
execute switch-controller get-sync-status group
<group>
Parameter
Description
Type
Size
<group>
Group Name.
string
execute switch-controller get-sync-status serial
Get FortiSwitch sync status by switch serial number.
execute switch-controller get-sync-status serial
<switch-serial-number>
Parameter
Description
Type
Size
<switch-serial-number>
Serial Number.
string
execute switch-controller get-sync-status switch-id
Get FortiSwitch sync status by switch.
execute switch-controller get-sync-status switch-id <switch>
Parameter
Description
Type
Size
<switch>
FortiSwitch device ID.
string
execute switch-controller get-upgrade-status
Get FortiSwitch upgrade status.
execute switch-controller get-upgrade-status
execute switch-controller ssh
SSH to FortiSwitch.
FortiOS 8.0.0 CLI Reference
4213
Fortinet Inc.

<!-- 来源页 4214 -->
CLI execute commands
execute switch-controller ssh <user> <switch>
Parameter
Description
Type
Size
<user>
user.
string
<switch>
FortiSwitch device ID.
string
execute switch-controller switch-action 802-1X clear-auth-mac
Clear FortiSwitch MAC entry.
execute switch-controller switch-action 802-1X clear-auth-mac <switch> <mac>
Parameter
Description
Type
Size
<switch>
FortiSwitch device ID.
string
<mac>
MAC address.
string
execute switch-controller switch-action 802-1X clear-auth-port
Clear FortiSwitch MAC entries on a single interface.
execute switch-controller switch-action 802-1X clear-auth-port <switch> <port>
Parameter
Description
Type
Size
<switch>
FortiSwitch device ID.
string
<port>
FortiSwitch port.
string
execute switch-controller switch-action bpdu-guard reset
Reset BPDU guard on switch-interface.
execute switch-controller switch-action bpdu-guard reset <switch> <port>
Parameter
Description
Type
Size
<switch>
FortiSwitch device ID.
string
<port>
FortiSwitch port.
string
FortiOS 8.0.0 CLI Reference
4214
Fortinet Inc.

<!-- 来源页 4215 -->
CLI execute commands
execute switch-controller switch-action cable-diag
Run a TDR diagnostic test on the specified FortiSwitch port.
execute switch-controller switch-action cable-diag <switch> <port>
Parameter
Description
Type
Size
<switch>
FortiSwitch device ID.
string
<port>
FortiSwitch port.
string
execute switch-controller switch-action factory-reset
Set FortiSwitch to factory default settings.
execute switch-controller switch-action factory-reset <switch>
Parameter
Description
Type
Size
<switch>
FortiSwitch device ID.
string
execute switch-controller switch-action flow-tracking
delete-flows-all
Delete all flows in the FortiSwitch.
execute switch-controller switch-action flow-tracking delete-flows-all <switch>
Parameter
Description
Type
Size
<switch>
FortiSwitch device ID.
string
execute switch-controller switch-action flow-tracking
expire-flows-all
Expire all flows in the FortiSwitch.
execute switch-controller switch-action flow-tracking expire-flows-all <switch>
Parameter
Description
Type
Size
<switch>
FortiSwitch device ID.
string
FortiOS 8.0.0 CLI Reference
4215
Fortinet Inc.

<!-- 来源页 4216 -->
CLI execute commands
execute switch-controller switch-action igmp-snoop
clear-learned
Clear FortiSwitch IGMP snooping multicast Groups and Queriers.
execute switch-controller switch-action igmp-snoop clear-learned <switch>
Parameter
Description
Type
Size
<switch>
FortiSwitch device ID.
string
execute switch-controller switch-action loop-guard reset
Reset loop-guard on switch-interface.
execute switch-controller switch-action loop-guard reset <switch> <port>
Parameter
Description
Type
Size
<switch>
FortiSwitch device ID.
string
<port>
FortiSwitch port.
string
execute switch-controller switch-action mac-device-reset dynamic
Remove specific or all DPP devices.
execute switch-controller switch-action mac-device-reset dynamic <mac>
Parameter
Description
Type
Size
<mac>
MAC address of the DPP device.
string
execute switch-controller switch-action mac-device-reset nac
Remove NAC devices and return MAC to onboarding VLAN.
execute switch-controller switch-action mac-device-reset nac <mac>
FortiOS 8.0.0 CLI Reference
4216
Fortinet Inc.

<!-- 来源页 4217 -->
CLI execute commands
Parameter
Description
Type
Size
<mac>
MAC address of the NAC device.
string
execute switch-controller switch-action mac-limit-violation reset all
Reset all MAC learning limit violations in FortiSwitch.
execute switch-controller switch-action mac-limit-violation reset all <switch>
Parameter
Description
Type
Size
<switch>
FortiSwitch device ID.
string
execute switch-controller switch-action mac-limit-violation reset interface
Reset MAC learning limit violations on a FortiSwitch interface.
execute switch-controller switch-action mac-limit-violation reset interface <switch> <port>
Parameter
Description
Type
Size
<switch>
FortiSwitch device ID.
string
<port>
FortiSwitch ports.
string
execute switch-controller switch-action mac-limit-violation reset vlan
Reset MAC learning limit violations on a FortiSwitch VLAN.
execute switch-controller switch-action mac-limit-violation reset vlan <switch> <vlan-id>
Parameter
Description
Type
Size
<switch>
FortiSwitch device ID.
string
<vlan-id>
FortiSwitch VLAN ID.
string
FortiOS 8.0.0 CLI Reference
4217
Fortinet Inc.

<!-- 来源页 4218 -->
CLI execute commands
execute switch-controller switch-action mclag stats clear
icl
Clears MCLAG inter-chassis-link statistics.
execute switch-controller switch-action mclag stats clear icl <switch>
Parameter
Description
Type
Size
<switch>
FortiSwitch device ID.
string
execute switch-controller switch-action mclag stats clear
mlag
Clears MCLAGs statistics for MCLAG enabled trunk.
execute switch-controller switch-action mclag stats clear mlag <switch> <mclag-trunk-name>
Parameter
Description
Type
Size
<switch>
FortiSwitch device ID.
string
<mclag-trunk-name>
MCLAG's trunk name.
string
execute switch-controller switch-action physical-ports
led-flash switch-group
Enable LED flash mode on FortiSwitches in the switch-group.
execute switch-controller switch-action physical-ports led-flash switch-group <switch-group ID>
<time>
Parameter
Description
Type
Size
<switch-group ID>
FortiSwitch group ID.
string
<time>
FortiSwitch LED flash mode in minutes < disable | 5 | 15 |
30 | 60 >.
string
FortiOS 8.0.0 CLI Reference
4218
Fortinet Inc.

<!-- 来源页 4219 -->
CLI execute commands
execute switch-controller switch-action physical-ports
led-flash switch-id
Enable FortiSwitch LED flash mode by switch name.
execute switch-controller switch-action physical-ports led-flash switch-id <switch> <time>
Parameter
Description
Type
Size
<switch>
FortiSwitch device ID.
string
<time>
FortiSwitch LED flash mode in minutes < disable | 5 | 15 |
30 | 60 >.
string
execute switch-controller switch-action physical-ports
led-flash tier1
Enable LED flash mode on all tier 1 FortiSwitch units.
execute switch-controller switch-action physical-ports led-flash tier1 <time>
Parameter
Description
Type
Size
<time>
FortiSwitch LED flash mode in minutes < disable | 5 | 15 |
30 | 60 >.
string
execute switch-controller switch-action physical-ports
led-flash tier2plus
Enable LED flash mode on all tier 2 and lower FortiSwitch units.
execute switch-controller switch-action physical-ports led-flash tier2plus <time>
Parameter
Description
Type
Size
<time>
FortiSwitch LED flash mode in minutes < disable | 5 | 15 |
30 | 60 >.
string
execute switch-controller switch-action poe reset
Reset PoE port on FortiSwitch.
FortiOS 8.0.0 CLI Reference
4219
Fortinet Inc.

<!-- 来源页 4220 -->
CLI execute commands
execute switch-controller switch-action poe reset <switch> <port>
Parameter
Description
Type
Size
<switch>
FortiSwitch device ID.
string
<port>
FortiSwitch port.
string
execute switch-controller switch-action restart delay all
Restart delay all FortiSwitch devices.
execute switch-controller switch-action restart delay all
execute switch-controller switch-action restart delay
switch-group
Restart delay FortiSwitch devices belonging to switch-group.
execute switch-controller switch-action restart delay switch-group <switch-group ID>
Parameter
Description
Type
Size
<switch-group ID>
Switch group ID.
string
execute switch-controller switch-action restart delay
switch-id
Restart delay FortiSwitch device identified by switch name.
execute switch-controller switch-action restart delay switch-id <switch>
Parameter
Description
Type
Size
<switch>
FortiSwitch device ID.
string
execute switch-controller switch-action restart swtp all
Restart all FortiSwitch devices.
execute switch-controller switch-action restart swtp all
FortiOS 8.0.0 CLI Reference
4220
Fortinet Inc.

<!-- 来源页 4221 -->
CLI execute commands
execute switch-controller switch-action restart swtp
switch-group
Restart FortiSwitch devices belonging to switch-group.
execute switch-controller switch-action restart swtp switch-group <switch-group ID>
Parameter
Description
Type
Size
<switch-group ID>
Switch group ID.
string
execute switch-controller switch-action restart swtp
switch-id
Restart FortiSwitch device identified by switch name.
execute switch-controller switch-action restart swtp switch-id <switch>
Parameter
Description
Type
Size
<switch>
FortiSwitch device ID.
string
execute switch-controller switch-action set-standalone
Set FortiSwitch to local/non-FortiLink mode.
execute switch-controller switch-action set-standalone <switch>
Parameter
Description
Type
Size
<switch>
FortiSwitch device ID.
string
execute switch-controller switch-action sticky-mac
delete-unsaved all
Delete all unsync Sticky MAC entries on FSW.
execute switch-controller switch-action sticky-mac delete-unsaved all <switch>
FortiOS 8.0.0 CLI Reference
4221
Fortinet Inc.

<!-- 来源页 4222 -->
CLI execute commands
Parameter
Description
Type
Size
<switch>
FortiSwitch device ID.
string
execute switch-controller switch-action sticky-mac
delete-unsaved interface
Delete specific interface's unsync Sticky MAC entries on FSW.
execute switch-controller switch-action sticky-mac delete-unsaved interface <switch> <port>
Parameter
Description
Type
Size
<switch>
FortiSwitch device ID.
string
<port>
Delete unsaved Sticky MAC entries for the specified
interface.
string
execute switch-controller switch-action sticky-mac save
all
Sync and save all Sticky MAC entries to config file (loads entries on boot).
execute switch-controller switch-action sticky-mac save all <switch>
Parameter
Description
Type
Size
<switch>
FortiSwitch device ID.
string
execute switch-controller switch-action sticky-mac save
interface
Sync and save specific interface Sticky MAC entries to config file (loads entries on boot).
execute switch-controller switch-action sticky-mac save interface <switch> <port>
Parameter
Description
Type
Size
<switch>
FortiSwitch device ID.
string
<port>
Save Sticky MAC entries for the specified interface.
string
FortiOS 8.0.0 CLI Reference
4222
Fortinet Inc.

<!-- 来源页 4223 -->
CLI execute commands
execute switch-controller switch-software cancel all
Cancel staged image to all FortiSwitch devices.
execute switch-controller switch-software cancel all
execute switch-controller switch-software cancel switch-group
Cancel staged image to FortiSwitch devices belonging to switch-group.
execute switch-controller switch-software cancel switch-group <switch-group ID>
Parameter
Description
Type
Size
<switch-group ID>
Switch group ID.
string
execute switch-controller switch-software cancel switch-id
Cancel staged image to FortiSwitch device identified by switch name.
execute switch-controller switch-software cancel switch-id <switch>
Parameter
Description
Type
Size
<switch>
FortiSwitch device ID.
string
execute switch-controller switch-software delete
Delete FortiSwitch image.
execute switch-controller switch-software delete <all>|<image-name>
Parameter
Description
Type
Size
<all>|<image-name>
Delete all images or specific image.
string
FortiOS 8.0.0 CLI Reference
4223
Fortinet Inc.

<!-- 来源页 4224 -->
CLI execute commands
execute switch-controller switch-software list-available
List FortiSwitch image(s) available on FortiGate.
execute switch-controller switch-software list-available
execute switch-controller switch-software stage all
Stage image to all FortiSwitch devices.
execute switch-controller switch-software stage all <filename>
Parameter
Description
Type
Size
<filename>
FortiSwitch image filename.
string
execute switch-controller switch-software stage switch-group
Stage image to FortiSwitch devices belonging to switch-group.
execute switch-controller switch-software stage switch-group <switch-group ID> <filename>
Parameter
Description
Type
Size
<switch-group ID>
Switch group ID.
string
<filename>
FortiSwitch image filename.
string
execute switch-controller switch-software stage switch-id
Stage image to FortiSwitch device identified by switch name.
execute switch-controller switch-software stage switch-id <switch> <filename>
Parameter
Description
Type
Size
<switch>
FortiSwitch device ID.
string
<filename>
FortiSwitch image filename.
string
FortiOS 8.0.0 CLI Reference
4224
Fortinet Inc.

<!-- 来源页 4225 -->
CLI execute commands
execute switch-controller switch-software upgrade
Upgrade FortiSwitch image to a managed FortiSwitch device.
execute switch-controller switch-software upgrade <switch> <filename>
Parameter
Description
Type
Size
<switch>
FortiSwitch device ID.
string
<filename>
FortiSwitch image filename.
string
execute switch-controller switch-software upload ftp
Upload a FortiSwitch image from FTP server.
execute switch-controller switch-software upload ftp <string> <ftp server>[:ftp port]
<Enter>|<user> <passwd>
Parameter
Description
Type
Size
<string>
FortiSwitch image name on the FTP server.
string
<ftp server>[:ftp
port]
FTP server IPv4, IPv6, or FQDN can be attached with
port.
string
<Enter>|<user>
FTP username may be needed.
string
<passwd>
FTP password.
string
execute switch-controller switch-software upload tftp
Upload a FortiSwitch image from TFTP server.
execute switch-controller switch-software upload tftp <string> <tftp server>
Parameter
Description
Type
Size
<string>
FortiSwitch image name on the TFTP server.
string
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
execute switch-controller virtual-port-pool request
Request virtual port from pool.
execute switch-controller virtual-port-pool request <switch> <port>
FortiOS 8.0.0 CLI Reference
4225
Fortinet Inc.

<!-- 来源页 4226 -->
CLI execute commands
Parameter
Description
Type
Size
<switch>
FortiSwitch device ID.
string
<port>
FortiSwitch port.
string
execute switch-controller virtual-port-pool return
Return virtual port to pool.
execute switch-controller virtual-port-pool return <switch> <port>
Parameter
Description
Type
Size
<switch>
FortiSwitch device ID.
string
<port>
FortiSwitch port.
string
execute switch-controller virtual-port-pool show
Show details of virtual ports in pool.
execute switch-controller virtual-port-pool show
execute switch-controller virtual-port-pool show-by-pool
Show details of virtual ports in pool by pool name.
execute switch-controller virtual-port-pool show-by-pool <pool>
Parameter
Description
Type
Size
<pool>
Pool Name.
string
execute switch-controller virtual-port-pool show-by-property
Show details of virtual ports in pool by property name.
execute switch-controller virtual-port-pool show-by-property <property>
FortiOS 8.0.0 CLI Reference
4226
Fortinet Inc.

---


<!-- 来源页 4227 -->
CLI execute commands
Parameter
Description
Type
Size
<property>
Property Name.
string
execute switch-controller virtual-port-pool show-by-tag
Show details of virtual ports in pool by tag name.
execute switch-controller virtual-port-pool show-by-tag <tag>
Parameter
Description
Type
Size
<tag>
Tag Name.
string
execute sync-IPSec
Sync all IPSec from peers.
execute sync-IPSec
execute sync-session
Sync all sessions from peers.
execute sync-session
execute system
system
This topic includes the following commands:
l execute system custom-language import on page 4228
l execute system fortisandbox test-connectivity on page 4228
FortiOS 8.0.0 CLI Reference
4227
Fortinet Inc.

---


<!-- 来源页 4227 -->
CLI execute commands
Parameter
Description
Type
Size
<property>
Property Name.
string
execute switch-controller virtual-port-pool show-by-tag
Show details of virtual ports in pool by tag name.
execute switch-controller virtual-port-pool show-by-tag <tag>
Parameter
Description
Type
Size
<tag>
Tag Name.
string
execute sync-IPSec
Sync all IPSec from peers.
execute sync-IPSec
execute sync-session
Sync all sessions from peers.
execute sync-session
execute system
system
This topic includes the following commands:
l execute system custom-language import on page 4228
l execute system fortisandbox test-connectivity on page 4228
FortiOS 8.0.0 CLI Reference
4227
Fortinet Inc.

---


<!-- 来源页 4227 -->
CLI execute commands
Parameter
Description
Type
Size
<property>
Property Name.
string
execute switch-controller virtual-port-pool show-by-tag
Show details of virtual ports in pool by tag name.
execute switch-controller virtual-port-pool show-by-tag <tag>
Parameter
Description
Type
Size
<tag>
Tag Name.
string
execute sync-IPSec
Sync all IPSec from peers.
execute sync-IPSec
execute sync-session
Sync all sessions from peers.
execute sync-session
execute system
system
This topic includes the following commands:
l execute system custom-language import on page 4228
l execute system fortisandbox test-connectivity on page 4228
FortiOS 8.0.0 CLI Reference
4227
Fortinet Inc.

---


<!-- 来源页 4228 -->
CLI execute commands
execute system custom-language import
Import a custom language from the TFTP server.
execute system custom-language import <string> <string> <ip>
Parameter
Description
Type
Size
<string>
The language name.
string
<string>
The file name on the TFTP server.
string
<ip>
IP address of the TFTP server.
string
execute system fortisandbox test-connectivity
Query FortiSandbox connection status.
execute system fortisandbox test-connectivity <device-name>
Parameter
Description
Type
Size
<device-name>
test fortisandbox connectivity
string
execute tac
tac
This topic includes the following commands:
l execute tac report on page 4228
execute tac report
Debug report.
execute tac report
FortiOS 8.0.0 CLI Reference
4228
Fortinet Inc.

---


<!-- 来源页 4229 -->
CLI execute commands
execute telnet
Simple telnet client.
execute telnet <dest> <port>
Parameter
Description
Type
Size
<dest>
IP address or domain name.
string
<port>
port
string
execute telnet-options
telnet-options
This topic includes the following commands:
l execute telnet-options interface on page 4229
l execute telnet-options reset on page 4229
l execute telnet-options source on page 4230
l execute telnet-options view-settings on page 4230
execute telnet-options interface
Auto | <outgoing interface>.
execute telnet-options interface <string>
Parameter
Description
Type
Size
<string>
Auto | <outgoing interface>.
string
execute telnet-options reset
Reset settings.
execute telnet-options reset
FortiOS 8.0.0 CLI Reference
4229
Fortinet Inc.

---


<!-- 来源页 4229 -->
CLI execute commands
execute telnet
Simple telnet client.
execute telnet <dest> <port>
Parameter
Description
Type
Size
<dest>
IP address or domain name.
string
<port>
port
string
execute telnet-options
telnet-options
This topic includes the following commands:
l execute telnet-options interface on page 4229
l execute telnet-options reset on page 4229
l execute telnet-options source on page 4230
l execute telnet-options view-settings on page 4230
execute telnet-options interface
Auto | <outgoing interface>.
execute telnet-options interface <string>
Parameter
Description
Type
Size
<string>
Auto | <outgoing interface>.
string
execute telnet-options reset
Reset settings.
execute telnet-options reset
FortiOS 8.0.0 CLI Reference
4229
Fortinet Inc.

---


<!-- 来源页 4230 -->
CLI execute commands
execute telnet-options source
Auto | <source interface IP>.
execute telnet-options source <xxx.xxx.xxx.xxx>
Parameter
Description
Type
Size
<xxx.xxx.xxx.xxx>
<source interface IP> | Auto
string
execute telnet-options view-settings
View the current settings for TELNET option.
execute telnet-options view-settings
execute test
test
This topic includes the following commands:
l execute test tftp-analytics-report on page 4230
execute test tftp-analytics-report
tftp analytics report.
execute test tftp-analytics-report <ip> <dir> <checksum>
Parameter
Description
Type
Size
<ip>
IP address of the TFTP server.
string
<dir>
Directory for the analytics report.
string
<checksum>
Checksum for the analytics report.
string
execute time
System time.
FortiOS 8.0.0 CLI Reference
4230
Fortinet Inc.

---


<!-- 来源页 4230 -->
CLI execute commands
execute telnet-options source
Auto | <source interface IP>.
execute telnet-options source <xxx.xxx.xxx.xxx>
Parameter
Description
Type
Size
<xxx.xxx.xxx.xxx>
<source interface IP> | Auto
string
execute telnet-options view-settings
View the current settings for TELNET option.
execute telnet-options view-settings
execute test
test
This topic includes the following commands:
l execute test tftp-analytics-report on page 4230
execute test tftp-analytics-report
tftp analytics report.
execute test tftp-analytics-report <ip> <dir> <checksum>
Parameter
Description
Type
Size
<ip>
IP address of the TFTP server.
string
<dir>
Directory for the analytics report.
string
<checksum>
Checksum for the analytics report.
string
execute time
System time.
FortiOS 8.0.0 CLI Reference
4230
Fortinet Inc.

---


<!-- 来源页 4231 -->
CLI execute commands
execute time <hh:mm:ss>
Parameter
Description
Type
Size
<hh:mm:ss>
hh: 0-23, mm: 0-59, ss: 0-59.
string
execute traceroute
Traceroute {IP|hostname}.
execute traceroute <dest>
Parameter
Description
Type
Size
<dest>
IP address or hostname.
string
execute traceroute-options
traceroute-options
This topic includes the following commands:
l execute traceroute-options device on page 4231
l execute traceroute-options queries on page 4232
l execute traceroute-options reset on page 4232
l execute traceroute-options source on page 4232
l execute traceroute-options use-sdwan on page 4232
l execute traceroute-options view-settings on page 4232
l execute traceroute-options vrf on page 4233
execute traceroute-options device
Auto | <ifname>.
execute traceroute-options device <string>
Parameter
Description
Type
Size
<string>
Auto | <ifname>
string
FortiOS 8.0.0 CLI Reference
4231
Fortinet Inc.

---


<!-- 来源页 4231 -->
CLI execute commands
execute time <hh:mm:ss>
Parameter
Description
Type
Size
<hh:mm:ss>
hh: 0-23, mm: 0-59, ss: 0-59.
string
execute traceroute
Traceroute {IP|hostname}.
execute traceroute <dest>
Parameter
Description
Type
Size
<dest>
IP address or hostname.
string
execute traceroute-options
traceroute-options
This topic includes the following commands:
l execute traceroute-options device on page 4231
l execute traceroute-options queries on page 4232
l execute traceroute-options reset on page 4232
l execute traceroute-options source on page 4232
l execute traceroute-options use-sdwan on page 4232
l execute traceroute-options view-settings on page 4232
l execute traceroute-options vrf on page 4233
execute traceroute-options device
Auto | <ifname>.
execute traceroute-options device <string>
Parameter
Description
Type
Size
<string>
Auto | <ifname>
string
FortiOS 8.0.0 CLI Reference
4231
Fortinet Inc.

<!-- 来源页 4232 -->
CLI execute commands
execute traceroute-options queries
Integer value to specify number of queries per hop.
execute traceroute-options queries <integer>
Parameter
Description
Type
Size
<integer>
Integer value [1, 10].
string
execute traceroute-options reset
Reset settings.
execute traceroute-options reset
execute traceroute-options source
Auto | <source interface IP>.
execute traceroute-options source <string>
Parameter
Description
Type
Size
<string>
Auto | <source interface IP>.
string
execute traceroute-options use-sdwan
Use SD-WAN rules to get output interface <yes | no>.
execute traceroute-options use-sdwan <string>
Parameter
Description
Type
Size
<string>
<yes | no>.
string
execute traceroute-options view-settings
View the current options of traceroute.
execute traceroute-options view-settings
FortiOS 8.0.0 CLI Reference
4232
Fortinet Inc.

---


<!-- 来源页 4233 -->
CLI execute commands
execute traceroute-options vrf
VRF ID.
execute traceroute-options vrf <interger>
Parameter
Description
Type
Size
<interger>
<0-511>
string
execute tracert6
Traceroute for IPv6.
execute tracert6
execute update-av
Update AV engine/definitions.
execute update-av
execute update-eip
Update external IP.
execute update-eip
execute update-external-resource
Download external resource.
execute update-external-resource <name>
FortiOS 8.0.0 CLI Reference
4233
Fortinet Inc.

---


<!-- 来源页 4233 -->
CLI execute commands
execute traceroute-options vrf
VRF ID.
execute traceroute-options vrf <interger>
Parameter
Description
Type
Size
<interger>
<0-511>
string
execute tracert6
Traceroute for IPv6.
execute tracert6
execute update-av
Update AV engine/definitions.
execute update-av
execute update-eip
Update external IP.
execute update-eip
execute update-external-resource
Download external resource.
execute update-external-resource <name>
FortiOS 8.0.0 CLI Reference
4233
Fortinet Inc.

---


<!-- 来源页 4233 -->
CLI execute commands
execute traceroute-options vrf
VRF ID.
execute traceroute-options vrf <interger>
Parameter
Description
Type
Size
<interger>
<0-511>
string
execute tracert6
Traceroute for IPv6.
execute tracert6
execute update-av
Update AV engine/definitions.
execute update-av
execute update-eip
Update external IP.
execute update-eip
execute update-external-resource
Download external resource.
execute update-external-resource <name>
FortiOS 8.0.0 CLI Reference
4233
Fortinet Inc.

---


<!-- 来源页 4233 -->
CLI execute commands
execute traceroute-options vrf
VRF ID.
execute traceroute-options vrf <interger>
Parameter
Description
Type
Size
<interger>
<0-511>
string
execute tracert6
Traceroute for IPv6.
execute tracert6
execute update-av
Update AV engine/definitions.
execute update-av
execute update-eip
Update external IP.
execute update-eip
execute update-external-resource
Download external resource.
execute update-external-resource <name>
FortiOS 8.0.0 CLI Reference
4233
Fortinet Inc.

---


<!-- 来源页 4234 -->
CLI execute commands
Parameter
Description
Type
Size
<name>
External resource name
string
execute update-ffdb-on-demand
Update ondemand FFDB from FDS.
execute update-ffdb-on-demand
execute update-geo-ip
Update IP Geography DB.
execute update-geo-ip
execute update-ips
Update IPS engine/definitions.
execute update-ips
execute update-now
Update now.
execute update-now
execute update-sata-firmware
Update SATA firmware.
execute update-sata-firmware
FortiOS 8.0.0 CLI Reference
4234
Fortinet Inc.

---


<!-- 来源页 4234 -->
CLI execute commands
Parameter
Description
Type
Size
<name>
External resource name
string
execute update-ffdb-on-demand
Update ondemand FFDB from FDS.
execute update-ffdb-on-demand
execute update-geo-ip
Update IP Geography DB.
execute update-geo-ip
execute update-ips
Update IPS engine/definitions.
execute update-ips
execute update-now
Update now.
execute update-now
execute update-sata-firmware
Update SATA firmware.
execute update-sata-firmware
FortiOS 8.0.0 CLI Reference
4234
Fortinet Inc.

---


<!-- 来源页 4234 -->
CLI execute commands
Parameter
Description
Type
Size
<name>
External resource name
string
execute update-ffdb-on-demand
Update ondemand FFDB from FDS.
execute update-ffdb-on-demand
execute update-geo-ip
Update IP Geography DB.
execute update-geo-ip
execute update-ips
Update IPS engine/definitions.
execute update-ips
execute update-now
Update now.
execute update-now
execute update-sata-firmware
Update SATA firmware.
execute update-sata-firmware
FortiOS 8.0.0 CLI Reference
4234
Fortinet Inc.

---


<!-- 来源页 4234 -->
CLI execute commands
Parameter
Description
Type
Size
<name>
External resource name
string
execute update-ffdb-on-demand
Update ondemand FFDB from FDS.
execute update-ffdb-on-demand
execute update-geo-ip
Update IP Geography DB.
execute update-geo-ip
execute update-ips
Update IPS engine/definitions.
execute update-ips
execute update-now
Update now.
execute update-now
execute update-sata-firmware
Update SATA firmware.
execute update-sata-firmware
FortiOS 8.0.0 CLI Reference
4234
Fortinet Inc.

---


<!-- 来源页 4234 -->
CLI execute commands
Parameter
Description
Type
Size
<name>
External resource name
string
execute update-ffdb-on-demand
Update ondemand FFDB from FDS.
execute update-ffdb-on-demand
execute update-geo-ip
Update IP Geography DB.
execute update-geo-ip
execute update-ips
Update IPS engine/definitions.
execute update-ips
execute update-now
Update now.
execute update-now
execute update-sata-firmware
Update SATA firmware.
execute update-sata-firmware
FortiOS 8.0.0 CLI Reference
4234
Fortinet Inc.

---


<!-- 来源页 4235 -->
CLI execute commands
execute update-src-vis
Update src-vis object.
execute update-src-vis
execute upd-vd-license
Update VDOM license.
execute upd-vd-license <license key>
Parameter
Description
Type
Size
<license key>
VDOM license key.
string
execute upload
upload
This topic includes the following commands:
l execute upload config ftp on page 4235
l execute upload config tftp on page 4236
l execute upload config usb on page 4236
l execute upload image ftp on page 4236
l execute upload image tftp on page 4237
l execute upload image usb on page 4237
l execute upload report-img ftp on page 4237
l execute upload report-img tftp on page 4238
execute upload config ftp
Load config file from FTP server.
execute upload config ftp <string> <comment> <ftp server>[:ftp port] <Enter>|<user> <passwd>
<Enter>|<passwd>
FortiOS 8.0.0 CLI Reference
4235
Fortinet Inc.

---


<!-- 来源页 4235 -->
CLI execute commands
execute update-src-vis
Update src-vis object.
execute update-src-vis
execute upd-vd-license
Update VDOM license.
execute upd-vd-license <license key>
Parameter
Description
Type
Size
<license key>
VDOM license key.
string
execute upload
upload
This topic includes the following commands:
l execute upload config ftp on page 4235
l execute upload config tftp on page 4236
l execute upload config usb on page 4236
l execute upload image ftp on page 4236
l execute upload image tftp on page 4237
l execute upload image usb on page 4237
l execute upload report-img ftp on page 4237
l execute upload report-img tftp on page 4238
execute upload config ftp
Load config file from FTP server.
execute upload config ftp <string> <comment> <ftp server>[:ftp port] <Enter>|<user> <passwd>
<Enter>|<passwd>
FortiOS 8.0.0 CLI Reference
4235
Fortinet Inc.

---


<!-- 来源页 4235 -->
CLI execute commands
execute update-src-vis
Update src-vis object.
execute update-src-vis
execute upd-vd-license
Update VDOM license.
execute upd-vd-license <license key>
Parameter
Description
Type
Size
<license key>
VDOM license key.
string
execute upload
upload
This topic includes the following commands:
l execute upload config ftp on page 4235
l execute upload config tftp on page 4236
l execute upload config usb on page 4236
l execute upload image ftp on page 4236
l execute upload image tftp on page 4237
l execute upload image usb on page 4237
l execute upload report-img ftp on page 4237
l execute upload report-img tftp on page 4238
execute upload config ftp
Load config file from FTP server.
execute upload config ftp <string> <comment> <ftp server>[:ftp port] <Enter>|<user> <passwd>
<Enter>|<passwd>
FortiOS 8.0.0 CLI Reference
4235
Fortinet Inc.

<!-- 来源页 4236 -->
CLI execute commands
Parameter
Description
Type
Size
<string>
Configure file name(path) on the remote server.
string
<comment>
comments
string
<ftp server>[:ftp
port]
FTP server IPv4, IPv6, or FQDN can be attached with
port.
string
<Enter>|<user>
FTP username may be needed.
string
<passwd>
FTP password.
string
<Enter>|<passwd>
Password may be needed to restore.
string
execute upload config tftp
Load config from TFTP server to local disk.
execute upload config tftp <string> <comment> <tftp server>
Parameter
Description
Type
Size
<string>
File name on the TFTP server.
string
<comment>
comments
string
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
execute upload config usb
Load config from USB to local disk.
execute upload config usb <string> <comment>
Parameter
Description
Type
Size
<string>
File name on USB disk.
string
<comment>
comments
string
execute upload image ftp
Load image from FTP server.
execute upload image ftp <string> <comment> <ftp server>[:ftp port] <Enter>|<user> <passwd>
FortiOS 8.0.0 CLI Reference
4236
Fortinet Inc.

<!-- 来源页 4237 -->
CLI execute commands
Parameter
Description
Type
Size
<string>
Image file name(path) on the remote server.
string
<comment>
comments
string
<ftp server>[:ftp
port]
FTP server IPv4, IPv6, or FQDN can be attached with
port.
string
<Enter>|<user>
FTP username may be needed.
string
<passwd>
FTP password.
string
execute upload image tftp
Load image from TFTP server to local disk.
execute upload image tftp <string> <comment> <tftp server>
Parameter
Description
Type
Size
<string>
File name on the TFTP server.
string
<comment>
comments
string
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
execute upload image usb
Load image from USB to local disk.
execute upload image usb <string> <comment>
Parameter
Description
Type
Size
<string>
File name on USB disk.
string
<comment>
comments
string
execute upload report-img ftp
upload report image file from ftp server
execute upload report-img ftp <string> <ftp server>[:ftp port] <Enter>|<user> <passwd> <Enter>
FortiOS 8.0.0 CLI Reference
4237
Fortinet Inc.

---


<!-- 来源页 4238 -->
CLI execute commands
Parameter
Description
Type
Size
<string>
Image file name(path) on the remote server.
string
<ftp server>[:ftp
port]
FTP server IPv4, IPv6, or FQDN can be attached with
port.
string
<Enter>|<user>
FTP username may be needed.
string
<passwd>
FTP password.
string
<Enter>
string
execute upload report-img tftp
upload report image file from tftp server
execute upload report-img tftp <string> <tftp server> <Enter>
Parameter
Description
Type
Size
<string>
File name on the TFTP server.
string
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
<Enter>
string
execute usb-device
usb-device
This topic includes the following commands:
l execute usb-device disconnect on page 4238
l execute usb-device list on page 4239
l execute usb-device modeswitch on page 4239
execute usb-device disconnect
Disconnect a USB device.
execute usb-device disconnect
FortiOS 8.0.0 CLI Reference
4238
Fortinet Inc.

---


<!-- 来源页 4239 -->
CLI execute commands
execute usb-device list
Display the lists of the USB device.
execute usb-device list
execute usb-device modeswitch
Perform usb device mode switch
execute usb-device modeswitch <argument string>
Parameter
Description
Type
Size
<argument
string>
usb_modeswitch arguments. e.g: usb_modeswitch '-v
0x12d1 -p 0x1f01 -V 0x12d1 -P 0x14dc'
string
execute usb-disk
usb-disk
This topic includes the following commands:
l execute usb-disk delete on page 4239
l execute usb-disk eject on page 4240
l execute usb-disk format on page 4240
l execute usb-disk list on page 4240
l execute usb-disk rename on page 4240
execute usb-disk delete
Delete file from the USB disk.
execute usb-disk delete <filename>
Parameter
Description
Type
Size
<filename>
File in the USB disk.
string
FortiOS 8.0.0 CLI Reference
4239
Fortinet Inc.

---


<!-- 来源页 4240 -->
CLI execute commands
execute usb-disk eject
Eject the USB disk.
execute usb-disk eject
execute usb-disk format
Format the USB disk.
execute usb-disk format
execute usb-disk list
Display the contents of the USB disk.
execute usb-disk list
execute usb-disk rename
Rename file in the USB disk.
execute usb-disk rename <old> <new>
Parameter
Description
Type
Size
<old>
Old file in the USB disk.
string
<new>
New file in the USB disk.
string
execute vin
vin
This topic includes the following commands:
l execute vin show on page 4241
FortiOS 8.0.0 CLI Reference
4240
Fortinet Inc.

---


<!-- 来源页 4241 -->
CLI execute commands
execute vin show
Show vin status.
execute vin show
execute vm-license
Download VM license from FortiCare.
execute vm-license <token> <proxy>
Parameter
Description
Type
Size
<token>
VM License Token.
string
<proxy>
HTTP Proxy URL.
string
execute vm-license-options
vm-license-options
This topic includes the following commands:
l execute vm-license-options account-id on page 4241
l execute vm-license-options account-password on page 4242
l execute vm-license-options count on page 4242
l execute vm-license-options government on page 4242
l execute vm-license-options interval on page 4242
l execute vm-license-options proxy on page 4243
l execute vm-license-options reset on page 4243
l execute vm-license-options show on page 4243
l execute vm-license-options token on page 4243
execute vm-license-options account-id
Account ID.
execute vm-license-options account-id <string>
FortiOS 8.0.0 CLI Reference
4241
Fortinet Inc.

---


<!-- 来源页 4241 -->
CLI execute commands
execute vin show
Show vin status.
execute vin show
execute vm-license
Download VM license from FortiCare.
execute vm-license <token> <proxy>
Parameter
Description
Type
Size
<token>
VM License Token.
string
<proxy>
HTTP Proxy URL.
string
execute vm-license-options
vm-license-options
This topic includes the following commands:
l execute vm-license-options account-id on page 4241
l execute vm-license-options account-password on page 4242
l execute vm-license-options count on page 4242
l execute vm-license-options government on page 4242
l execute vm-license-options interval on page 4242
l execute vm-license-options proxy on page 4243
l execute vm-license-options reset on page 4243
l execute vm-license-options show on page 4243
l execute vm-license-options token on page 4243
execute vm-license-options account-id
Account ID.
execute vm-license-options account-id <string>
FortiOS 8.0.0 CLI Reference
4241
Fortinet Inc.

<!-- 来源页 4242 -->
CLI execute commands
Parameter
Description
Type
Size
<string>
Account ID.
string
execute vm-license-options account-password
Account password.
execute vm-license-options account-password <string>
Parameter
Description
Type
Size
<string>
Account password.
string
execute vm-license-options count
FortiFlex license download count (default=1, 0 means infinite).
execute vm-license-options count <integer>
Parameter
Description
Type
Size
<integer>
API call count.
string
execute vm-license-options government
For government use <yes | no>.
execute vm-license-options government <string>
Parameter
Description
Type
Size
<string>
<yes | no>.
string
execute vm-license-options interval
FortiFlex license download interval (1-3600 sec, default=60).
execute vm-license-options interval <integer>
Parameter
Description
Type
Size
<integer>
API call interval.
string
FortiOS 8.0.0 CLI Reference
4242
Fortinet Inc.

---


<!-- 来源页 4243 -->
CLI execute commands
execute vm-license-options proxy
HTTP proxy URL.
execute vm-license-options proxy <string>
Parameter
Description
Type
Size
<string>
HTTP proxy URL.
string
execute vm-license-options reset
Reset options.
execute vm-license-options reset
execute vm-license-options show
Show options.
execute vm-license-options show
execute vm-license-options token
Token.
execute vm-license-options token <string>
Parameter
Description
Type
Size
<string>
Token.
string
execute vpn
vpn
This topic includes the following commands:
l execute vpn certificate ca export tftp on page 4244
l execute vpn certificate ca import auto on page 4245
l execute vpn certificate ca import bundle on page 4245
FortiOS 8.0.0 CLI Reference
4243
Fortinet Inc.

<!-- 来源页 4244 -->
CLI execute commands
l execute vpn certificate ca import est on page 4245
l execute vpn certificate ca import tftp on page 4246
l execute vpn certificate crl import auto on page 4246
l execute vpn certificate ems_ca import tftp on page 4246
l execute vpn certificate hsm-local gch-get-versions on page 4247
l execute vpn certificate hsm-local status on page 4247
l execute vpn certificate hsm-local verify on page 4247
l execute vpn certificate local export scp on page 4247
l execute vpn certificate local export tftp on page 4248
l execute vpn certificate local generate cmp-ec on page 4248
l execute vpn certificate local generate cmp-rsa on page 4249
l execute vpn certificate local generate default-gui-mgmt-cert on page 4250
l execute vpn certificate local generate default-ssl-ca on page 4250
l execute vpn certificate local generate default-ssl-ca-untrusted on page 4250
l execute vpn certificate local generate default-ssl-key-certs on page 4250
l execute vpn certificate local generate default-ssl-serv-key on page 4250
l execute vpn certificate local generate ec on page 4250
l execute vpn certificate local generate est on page 4251
l execute vpn certificate local generate rsa on page 4252
l execute vpn certificate local import scp on page 4253
l execute vpn certificate local import tftp on page 4254
l execute vpn certificate local verify on page 4254
l execute vpn certificate remote export tftp on page 4254
l execute vpn certificate remote import tftp on page 4254
l execute vpn ikecrypt dhperf compute on page 4255
l execute vpn ikecrypt dhperf generate on page 4255
l execute vpn ipsec tunnel down on page 4255
l execute vpn ipsec tunnel up on page 4255
l execute vpn sslvpn del-all on page 4256
l execute vpn sslvpn del-tunnel on page 4256
l execute vpn sslvpn del-web on page 4256
l execute vpn sslvpn list on page 4256
execute vpn certificate ca export tftp
Export CA certificate to a TFTP server.
execute vpn certificate ca export tftp <string> <string> <ip>
Parameter
Description
Type
Size
<string>
CA certificate name.
string
FortiOS 8.0.0 CLI Reference
4244
Fortinet Inc.

<!-- 来源页 4245 -->
CLI execute commands
Parameter
Description
Type
Size
<string>
File name on the TFTP server.
string
<ip>
IP address of TFTP server.
string
execute vpn certificate ca import auto
Import CA certificate via SCEP.
execute vpn certificate ca import auto <string> <string> <ip> <fingerprint>
Parameter
Description
Type
Size
<string>
URL of the CA server.
string
<string>
CA Identifier (optional).
string
<ip>
Source-IP for communications to the CA server (optional).
string
<fingerprint>
Fingerprint for authenticating CA certificate from server
(optional).
string
execute vpn certificate ca import bundle
Import certificate bundle from a TFTP server.
execute vpn certificate ca import bundle <string> <ip>
Parameter
Description
Type
Size
<string>
File name on the TFTP server.
string
<ip>
IP address of TFTP server.
string
execute vpn certificate ca import est
Import CA certificate via EST.
execute vpn certificate ca import est <string> <string> <string> <string> <ip> <string> <string>
<string> <string>
Parameter
Description
Type
Size
<string>
URL of the CA server. (e.g. https://example.com:1234).
string
<string>
CA Identifier (optional).
string
FortiOS 8.0.0 CLI Reference
4245
Fortinet Inc.

<!-- 来源页 4246 -->
CLI execute commands
Parameter
Description
Type
Size
<string>
Verify CA server using this certificate (optional).
string
<string>
Client certificate (optional).
string
<ip>
Source-IP for communications to the CA server (optional).
string
<string>
TLS-SRP Username (optional).
string
<string>
TLS-SRP Password (optional).
string
<string>
HTTP Authentication Username (optional).
string
<string>
HTTP Authentication Password (optional).
string
execute vpn certificate ca import tftp
Import CA certificate from a TFTP server.
execute vpn certificate ca import tftp <string> <tftp server>
Parameter
Description
Type
Size
<string>
File name on the TFTP server.
string
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
execute vpn certificate crl import auto
Update CRL.
execute vpn certificate crl import auto <string>
Parameter
Description
Type
Size
<string>
CRL name.
string
execute vpn certificate ems_ca import tftp
Import Testing EMS CA certificate from a TFTP server.
execute vpn certificate ems_ca import tftp <string> <tftp server>
Parameter
Description
Type
Size
<string>
File name on the TFTP server.
string
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
FortiOS 8.0.0 CLI Reference
4246
Fortinet Inc.

<!-- 来源页 4247 -->
CLI execute commands
execute vpn certificate hsm-local gch-get-versions
List available crypto-key-versions.
execute vpn certificate hsm-local gch-get-versions <string> <string>
Parameter
Description
Type
Size
<string>
hsm-local certificate name.
string
<string>
Access token or JSON Web Token to be used as bearer
token in request.
string
execute vpn certificate hsm-local status
Status check for an hsm-local certificate.
execute vpn certificate hsm-local status <string> <string>
Parameter
Description
Type
Size
<string>
hsm-local certificate name.
string
<string>
Access token or JSON Web Token to be used as bearer
token in request.
string
execute vpn certificate hsm-local verify
Verify between hsm-local certificate and its private key.
execute vpn certificate hsm-local verify <string> <string>
Parameter
Description
Type
Size
<string>
hsm-local certificate name.
string
<string>
Access token or JSON Web Token to be used as bearer
token in request.
string
execute vpn certificate local export scp
Export local certificate or request to a SCP server.
execute vpn certificate local export scp <string> <string> <string> <scp server> <user> <passwd>
FortiOS 8.0.0 CLI Reference
4247
Fortinet Inc.

<!-- 来源页 4248 -->
CLI execute commands
Parameter
Description
Type
Size
<string>
Local certificate name.
string
<string>
Certificate file type ('cer'|'p12'|'csr').
string
<string>
File name on the SCP server.
string
<scp server>
SCP server address (IPv4, [IPv6], or FQDN — port optional)
Supported formats: 192.0.2.1 (IPv4) 192.0.2.1:22 (IPv4
with port) 2001:db8::1 (Raw IPv6) [2001:db8::1] (IPv6)
[2001:db8::1]:22 (IPv6 with port) host.example.com
(FQDN, resolves to IPv4) [host.example.com] (FQDN,
resolves to IPv6) [host.example.com]:22 (FQDN with port,
resolves to IPv6) * Use square brackets when specifying a
port with an IPv6 address or IPv6-resolving FQDN.
string
<user>
SCP username.
string
<passwd>
SCP password.
string
execute vpn certificate local export tftp
Export local certificate or certificate request to a TFTP server.
execute vpn certificate local export tftp <string> <string> <string> <tftp server>
Parameter
Description
Type
Size
<string>
Local certificate name.
string
<string>
Certificate file type ('cer'|'p12'|'csr').
string
<string>
File name on the TFTP server.
string
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
execute vpn certificate local generate cmp-ec
Generate a ECDSA certificate request over CMPv2.
execute vpn certificate local generate cmp-ec <string> <string> <string> <string> <string>
<string> <string> <string> <string> <string> <ip>
Parameter
Description
Type
Size
<string>
Local certificate name.
string
<string>
Elliptic curve name: secp256r1, secp384r1 and secp521r1.
string
FortiOS 8.0.0 CLI Reference
4248
Fortinet Inc.

<!-- 来源页 4249 -->
CLI execute commands
Parameter
Description
Type
Size
<string>
Server ('ADDRESS:PORT' for CMP server).
string
<string>
Path (Path location inside CMP server)
string
<string>
SrvCert (CMDB name of CMP server's certificate/root-CA)
string
<string>
AuthCert (CMDB name of client's current certificate)
string
<string>
User (Username for doing the IR with a pre-shared key)
string
<string>
Password (Password for doing the IR with a pre-shared
key)
string
<string>
Subject (optional, e.g. "CN=User,O=Org,OU=Unit").
string
<string>
Subject alternative name (optional, e.g.
"DNS:dns1.com,IP:192.168.1.99").
string
<ip>
Source-IP for communications to the CMP server
(optional).
string
execute vpn certificate local generate cmp-rsa
Generate a RSA certificate request over CMPv2.
execute vpn certificate local generate cmp-rsa <string> <number> <string> <string> <string>
<string> <string> <string> <string> <string> <ip>
Parameter
Description
Type
Size
<string>
Local certificate name.
string
<number>
Key size: 1024, 1536, 2048, 4096.
string
<string>
Server ('ADDRESS:PORT' for CMP server, add 'https://'
before address to enable ssl/tls).
string
<string>
Path (Path location inside CMP server)
string
<string>
SrvCert (CMDB name of CMP server's certificate/root-CA)
string
<string>
AuthCert (CMDB name of client's current certificate)
string
<string>
User (Username for doing the IR with a pre-shared key)
string
<string>
Password (Password for doing the IR with a pre-shared
key)
string
<string>
Subject (optional, e.g. "CN=User,O=Org,OU=Unit").
string
<string>
Subject alternative name (optional, e.g.
"DNS:dns1.com,IP:192.168.1.99").
string
<ip>
Source-IP for communications to the CMP server
(optional).
string
FortiOS 8.0.0 CLI Reference
4249
Fortinet Inc.

<!-- 来源页 4250 -->
CLI execute commands
execute vpn certificate local generate default-gui-mgmt-cert
Generate the default GUI mgmt admin-server certificate.
execute vpn certificate local generate default-gui-mgmt-cert
execute vpn certificate local generate default-ssl-ca
Generate the default CA certificate used by SSL Inspection.
execute vpn certificate local generate default-ssl-ca
execute vpn certificate local generate default-ssl-ca-untrusted
Generate the default untrusted CA certificate used by SSL Inspection.
execute vpn certificate local generate default-ssl-ca-untrusted
execute vpn certificate local generate default-ssl-key-certs
Generate the default RSA, DSA and ECDSA key certs for ssl resign.
execute vpn certificate local generate default-ssl-key-certs
execute vpn certificate local generate default-ssl-serv-key
Generate the default server key used by SSL Inspection.
execute vpn certificate local generate default-ssl-serv-key
execute vpn certificate local generate ec
Generate an elliptic curve certificate request.
FortiOS 8.0.0 CLI Reference
4250
Fortinet Inc.

<!-- 来源页 4251 -->
CLI execute commands
execute vpn certificate local generate ec <string> <string> <string> <string> <string> <string>
<string> <string> <string> <string> <string> <string> <ip> <string> <string> <string> <string>
Parameter
Description
Type
Size
<string>
Local certificate name.
string
<string>
Elliptic curve name: secp256r1, secp384r1 and secp521r1.
string
<string>
Common Name.
string
<string>
Country name (e.g. Canada) or country code (e.g. ca).
string
<string>
State.
string
<string>
City.
string
<string>
Org.
string
<string>
Unit(s); ',' as delimiter.
string
<string>
Email.
string
<string>
Subject alternative name (optional).
string
<string>
URL of the CA server for signing via SCEP (optional).
string
<string>
Challenge password for signing via SCEP (optional).
string
<ip>
Source-IP for communications to the CA server (optional).
string
<string>
CA identifier of the CA server for signing via SCEP
(optional).
string
<string>
Password for private-key (optional).
string
<string>
Installed CA certificate for generating fingerprint for
validating CA from SCEP server (optional).
string
<string>
Fingerprint for authenticating CA certificate from SCEP
server. Ignored if valid CA for generating fingerprint is
specified (optional).
string
execute vpn certificate local generate est
Generate an certificate via Enrollment over Secure Transport.
execute vpn certificate local generate est <string> <string> <string> <string> <string> <string>
<string> <string> <string> <string> <string> <ip> <string> <string>
Parameter
Description
Type
Size
<string>
Local certificate name.
string
FortiOS 8.0.0 CLI Reference
4251
Fortinet Inc.

<!-- 来源页 4252 -->
CLI execute commands
Parameter
Description
Type
Size
<string>
Cryptography algorithm: rsa-1024, rsa-1536, rsa-2048,
rsa-4096, ec-secp256r1, ec-secp384r1, ec-secp521r1
string
<string>
URL of the CA server. (e.g. https://example.com:1234).
string
<string>
Subject (optional, e.g. "CN=User,O=Org,OU=Unit").
string
<string>
Subject alternative name (optional, e.g.
"DNS:dns1.com,IP:192.168.1.99").
string
<string>
HTTP Authentication Username (optional).
string
<string>
HTTP Authentication Password (optional).
string
<string>
CA Identifier (optional).
string
<string>
CA Server certificate (optional).
string
<string>
Password for private-key (optional).
string
<string>
Client certificate (optional).
string
<ip>
Source-IP for communications to the CA server (optional).
string
<string>
TLS-SRP Username (optional).
string
<string>
TLS-SRP Password (optional).
string
execute vpn certificate local generate rsa
Generate a RSA certificate request.
execute vpn certificate local generate rsa <string> <number> <string> <string> <string> <string>
<string> <string> <string> <string> <string> <string> <ip> <string> <string> <string> <string>
Parameter
Description
Type
Size
<string>
Local certificate name.
string
<number>
Key size: 1024, 1536, 2048, 4096.
string
<string>
Common Name.
string
<string>
Country name (e.g. Canada) or country code (e.g. ca).
string
<string>
State.
string
<string>
City.
string
<string>
Org.
string
<string>
Unit(s); ',' as delimiter.
string
<string>
Email.
string
FortiOS 8.0.0 CLI Reference
4252
Fortinet Inc.

<!-- 来源页 4253 -->
CLI execute commands
Parameter
Description
Type
Size
<string>
Subject alternative name (optional).
string
<string>
URL of the CA server for signing via SCEP (optional).
string
<string>
Challenge password for signing via SCEP (optional).
string
<ip>
Source-IP for communications to the CA server (optional).
string
<string>
CA identifier of the CA server for signing via SCEP
(optional).
string
<string>
Password for private-key (optional).
string
<string>
Installed CA certificate for generating fingerprint for
validating CA from SCEP server (optional).
string
<string>
Fingerprint for authenticating CA certificate from SCEP
server. Ignored if valid CA for generating fingerprint is
specified (optional).
string
execute vpn certificate local import scp
Import the signed certificate from a SCP server.
execute vpn certificate local import scp <scp server>[:scp port] <user> <passwd> <string> <string>
<Enter>|<passwd>
Parameter
Description
Type
Size
<scp server>[:scp
port]
SCP server address (IPv4, [IPv6], or FQDN — port
optional) Supported formats: 192.0.2.1 (IPv4)
192.0.2.1:22 (IPv4 with port) 2001:db8::1 (Raw IPv6)
[2001:db8::1] (IPv6) [2001:db8::1]:22 (IPv6 with
port) host.example.com (FQDN, resolves to IPv4)
[host.example.com] (FQDN, resolves to IPv6)
[host.example.com]:22 (FQDN with port, resolves
to IPv6) * Use square brackets when specifying a
port with an IPv6 address or IPv6-resolving FQDN.
string
<user>
SCP username.
string
<passwd>
SCP password.
string
<string>
File name on the SCP server.
string
<string>
Certificate file type ('cer'|'p12').
string
<Enter>|<passwd>
Password for PKCS12 file.
string
FortiOS 8.0.0 CLI Reference
4253
Fortinet Inc.

<!-- 来源页 4254 -->
CLI execute commands
execute vpn certificate local import tftp
Import the signed certificate from a TFTP server.
execute vpn certificate local import tftp <string> <tftp server> <string> <Enter>|<passwd>
Parameter
Description
Type
Size
<string>
File name on the TFTP server.
string
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
<string>
Certificate file type ('cer'|'p12').
string
<Enter>|<passwd>
Password for PKCS12 file.
string
execute vpn certificate local verify
Verify certificate and private key files match and regenerate if mismatched.
execute vpn certificate local verify <string>
Parameter
Description
Type
Size
<string>
Local certificate name.
string
execute vpn certificate remote export tftp
Export REMOTE certificate to a TFTP server.
execute vpn certificate remote export tftp <string> <string> <tftp server>
Parameter
Description
Type
Size
<string>
REMOTE certificate name.
string
<string>
File name on the TFTP server.
string
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
execute vpn certificate remote import tftp
Import REMOTE certificate from a TFTP server.
execute vpn certificate remote import tftp <string> <tftp server>
FortiOS 8.0.0 CLI Reference
4254
Fortinet Inc.

<!-- 来源页 4255 -->
CLI execute commands
Parameter
Description
Type
Size
<string>
File name on the TFTP server.
string
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
execute vpn ikecrypt dhperf compute
Run DH generate and compute benchmark.
execute vpn ikecrypt dhperf compute <rounds>
Parameter
Description
Type
Size
<rounds>
Number of DH generate and compute rounds to perform
per group <1-100000>.
string
execute vpn ikecrypt dhperf generate
Run DH generate benchmark.
execute vpn ikecrypt dhperf generate <rounds>
Parameter
Description
Type
Size
<rounds>
Number of DH generate rounds to perform per group <1-100000>.
string
execute vpn ipsec tunnel down
Shut down the specified IPsec tunnel.
execute vpn ipsec tunnel down <phase2> <phase1> <serial>
Parameter
Description
Type
Size
<phase2>
Phase2 name.
string
<phase1>
Phase1 name.
string
<serial>
Phase2 serial number.
string
execute vpn ipsec tunnel up
Activate the specified IPsec tunnel.
FortiOS 8.0.0 CLI Reference
4255
Fortinet Inc.

<!-- 来源页 4256 -->
CLI execute commands
execute vpn ipsec tunnel up <phase2> <phase1> <serial>
Parameter
Description
Type
Size
<phase2>
Phase2 name.
string
<phase1>
Phase1 name.
string
<serial>
Phase2 serial number.
string
execute vpn sslvpn del-all
Delete all connections under current VDOM.
execute vpn sslvpn del-all <tunnel>
Parameter
Description
Type
Size
<tunnel>
Press <Enter> to delete all or type "tunnel" to delete
sesison only.
string
execute vpn sslvpn del-tunnel
Delete session connection.
execute vpn sslvpn del-tunnel <index>
Parameter
Description
Type
Size
<index>
Session index.
string
execute vpn sslvpn del-web
Delete web connection.
execute vpn sslvpn del-web <index>
Parameter
Description
Type
Size
<index>
Web index.
string
execute vpn sslvpn list
List connections.
FortiOS 8.0.0 CLI Reference
4256
Fortinet Inc.

---


<!-- 来源页 4257 -->
CLI execute commands
execute vpn sslvpn list <web|tunnel>
Parameter
Description
Type
Size
<web|tunnel>
Web or session.
string
execute wake-on-lan
Wake On LAN command.
execute wake-on-lan <interface> <host-mac> <protocol> <port> <ip> <password>
Parameter
Description
Type
Size
<interface>
Network interface to send out WoL packets.
string
<host-mac>
Host MAC address to be woken up.
string
<protocol>
Protocol used by WoL packets (1-WoL, 2-UDP, default =
2).
string
<port>
Port used by UDP WoL packets, (0, 7, or 9, default = 9).
string
<ip>
Broadcast IP used by UDP WoL packets.
string
<password>
Password of the destination host if SecureOn is enabled.
string
execute webcache
webcache
This topic includes the following commands:
l execute webcache delete regular-expression on page 4257
l execute webcache delete simple-string on page 4258
l execute webcache delete status on page 4258
l execute webcache delete wildcard on page 4258
execute webcache delete regular-expression
Delete objects matching a regular expression in webcache.
execute webcache delete regular-expression <pattern>
FortiOS 8.0.0 CLI Reference
4257
Fortinet Inc.

---


<!-- 来源页 4257 -->
CLI execute commands
execute vpn sslvpn list <web|tunnel>
Parameter
Description
Type
Size
<web|tunnel>
Web or session.
string
execute wake-on-lan
Wake On LAN command.
execute wake-on-lan <interface> <host-mac> <protocol> <port> <ip> <password>
Parameter
Description
Type
Size
<interface>
Network interface to send out WoL packets.
string
<host-mac>
Host MAC address to be woken up.
string
<protocol>
Protocol used by WoL packets (1-WoL, 2-UDP, default =
2).
string
<port>
Port used by UDP WoL packets, (0, 7, or 9, default = 9).
string
<ip>
Broadcast IP used by UDP WoL packets.
string
<password>
Password of the destination host if SecureOn is enabled.
string
execute webcache
webcache
This topic includes the following commands:
l execute webcache delete regular-expression on page 4257
l execute webcache delete simple-string on page 4258
l execute webcache delete status on page 4258
l execute webcache delete wildcard on page 4258
execute webcache delete regular-expression
Delete objects matching a regular expression in webcache.
execute webcache delete regular-expression <pattern>
FortiOS 8.0.0 CLI Reference
4257
Fortinet Inc.

---


<!-- 来源页 4258 -->
CLI execute commands
Parameter
Description
Type
Size
<pattern>
Pattern.
string
execute webcache delete simple-string
Delete objects matching a simple string in webcache.
execute webcache delete simple-string <pattern>
Parameter
Description
Type
Size
<pattern>
Pattern.
string
execute webcache delete status
Query pattern deletion status.
execute webcache delete status
execute webcache delete wildcard
Delete objects matching a wildcard in webcache.
execute webcache delete wildcard <pattern>
Parameter
Description
Type
Size
<pattern>
Pattern.
string
execute webfilter
webfilter
This topic includes the following commands:
l execute webfilter quota-reset on page 4258
execute webfilter quota-reset
Reset the WF quota for a given user.
FortiOS 8.0.0 CLI Reference
4258
Fortinet Inc.

---


<!-- 来源页 4259 -->
CLI execute commands
execute webfilter quota-reset <wf-profile> <endpoint>
Parameter
Description
Type
Size
<wf-profile>
Web filter profile.
string
<endpoint>
Authenticated user or IP address.
string
execute wireless-controller
wireless-controller
This topic includes the following commands:
l execute wireless-controller create-sae-pk on page 4259
l execute wireless-controller delete-wtp-image on page 4260
l execute wireless-controller hs20-icon backup-icon ftp on page 4260
l execute wireless-controller hs20-icon backup-icon tftp on page 4260
l execute wireless-controller hs20-icon delete-hs-icon on page 4261
l execute wireless-controller hs20-icon list-hs-icon on page 4261
l execute wireless-controller hs20-icon upload-icon ftp on page 4261
l execute wireless-controller hs20-icon upload-icon tftp on page 4261
l execute wireless-controller led-blink on page 4262
l execute wireless-controller list-wtp-image on page 4262
l execute wireless-controller mpsk-key create-keys on page 4262
l execute wireless-controller push-wtp-image on page 4262
l execute wireless-controller reset-wtp on page 4263
l execute wireless-controller restart-acd on page 4263
l execute wireless-controller restart-stad on page 4263
l execute wireless-controller restart-wtpd on page 4263
l execute wireless-controller rolling-wtp-upgrade on page 4263
l execute wireless-controller spectral-scan on page 4264
l execute wireless-controller upload-wtp-image ftp on page 4264
l execute wireless-controller upload-wtp-image tftp on page 4264
execute wireless-controller create-sae-pk
Create SAE PK keys.
execute wireless-controller create-sae-pk <string> <string>
FortiOS 8.0.0 CLI Reference
4259
Fortinet Inc.

<!-- 来源页 4260 -->
CLI execute commands
Parameter
Description
Type
Size
<string>
SSID.
string
<string>
Curve: prime256v1|secp384r1|secp521r1.
string
execute wireless-controller delete-wtp-image
Delete WTP images.
execute wireless-controller delete-wtp-image <all>|<all-pushing>|<image-name>
Parameter
Description
Type
Size
<all>|<all-pushing>|<image-name>
Delete all images or specific image.
string
execute wireless-controller hs20-icon backup-icon ftp
Backup a hotspot icon to FTP server.
execute wireless-controller hs20-icon backup-icon ftp <string> <ftp server>[:ftp port]
<Enter>|<user> <passwd>
Parameter
Description
Type
Size
<string>
Icon file name on AC.
string
<ftp server>[:ftp
port]
FTP server IPv4, IPv6, or FQDN can be attached with
port.
string
<Enter>|<user>
FTP username may be needed.
string
<passwd>
FTP password.
string
execute wireless-controller hs20-icon backup-icon tftp
Backup a hotspot icon to TFTP server.
execute wireless-controller hs20-icon backup-icon tftp <string> <tftp server>
Parameter
Description
Type
Size
<string>
Icon file name on AC.
string
<tftp server>
IP/IPv6 or FQDN address of TFTP server.
string
FortiOS 8.0.0 CLI Reference
4260
Fortinet Inc.

<!-- 来源页 4261 -->
CLI execute commands
execute wireless-controller hs20-icon delete-hs-icon
Delete hotspot icons.
execute wireless-controller hs20-icon delete-hs-icon
execute wireless-controller hs20-icon list-hs-icon
List hotspot icons.
execute wireless-controller hs20-icon list-hs-icon
execute wireless-controller hs20-icon upload-icon ftp
Upload a hotspot icon from FTP server.
execute wireless-controller hs20-icon upload-icon ftp <string> <ftp server>[:ftp port]
<Enter>|<user> <passwd>
Parameter
Description
Type
Size
<string>
Icon file name on the remote server.
string
<ftp server>[:ftp
port]
FTP server IPv4, IPv6, or FQDN can be attached with
port.
string
<Enter>|<user>
FTP username may be needed.
string
<passwd>
FTP password.
string
execute wireless-controller hs20-icon upload-icon tftp
Upload a hotspot icon from TFTP server.
execute wireless-controller hs20-icon upload-icon tftp <string> <tftp server>
Parameter
Description
Type
Size
<string>
Icon file name on the TFTP server.
string
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
FortiOS 8.0.0 CLI Reference
4261
Fortinet Inc.

<!-- 来源页 4262 -->
CLI execute commands
execute wireless-controller led-blink
Blink status LED or power LED of managed FortiAP.
execute wireless-controller led-blink <wtp-id> <mode> <duration>
Parameter
Description
Type
Size
<wtp-id>
WTP ID.
string
<mode>
[on | off]
string
<duration>
Blink duration in seconds (0 = unlimited).
string
execute wireless-controller list-wtp-image
List WTP images.
execute wireless-controller list-wtp-image
execute wireless-controller mpsk-key create-keys
Create random MPSK keys.
execute wireless-controller mpsk-key create-keys <string> <string> <string> <string> <int> <int>
Parameter
Description
Type
Size
<string>
VDOM.
string
<string>
MPSK profile name.
string
<string>
MPSK group name.
string
<string>
Key prefix.
string
<int>
Key count.
string
<int>
Key length.
string
execute wireless-controller push-wtp-image
Push WTP image to a managed WTP.
execute wireless-controller push-wtp-image <vdom> <wtp-id> <filename>
FortiOS 8.0.0 CLI Reference
4262
Fortinet Inc.

<!-- 来源页 4263 -->
CLI execute commands
Parameter
Description
Type
Size
<vdom>
WTP session VDOM.
string
<wtp-id>
WTP ID.
string
<filename>
WTP image filename.
string
execute wireless-controller reset-wtp
Restart managed WTP.
execute wireless-controller reset-wtp <all>|<SN>|<wtp-group>
Parameter
Description
Type
Size
<all>|<SN>|<wtp-group>
WTP serial number or WTP group.
string
execute wireless-controller restart-acd
Restart wireless controller daemon.
execute wireless-controller restart-acd
execute wireless-controller restart-stad
Restart sta daemon.
execute wireless-controller restart-stad
execute wireless-controller restart-wtpd
Restart local WTP daemon.
execute wireless-controller restart-wtpd
execute wireless-controller rolling-wtp-upgrade
Rolling upgrade managed WTP.
execute wireless-controller rolling-wtp-upgrade <all>|<SN>|<wtp-group>
FortiOS 8.0.0 CLI Reference
4263
Fortinet Inc.

<!-- 来源页 4264 -->
CLI execute commands
Parameter
Description
Type
Size
<all>|<SN>|<wtp-group>
WTP serial number or WTP group.
string
execute wireless-controller spectral-scan
Enable/disable spectral scan.
execute wireless-controller spectral-scan <wtp-id> <radio-id> <mode> <duration> <channel> <report-interval>
Parameter
Description
Type
Size
<wtp-id>
WTP ID.
string
<radio-id>
Radio ID
string
<mode>
[on | off | scan-only | keep-alive | clear]
string
<duration>
Spectrum scan duration in seconds (0 = unlimited).
string
<channel>
Spectrum scan channels separated by commas. (0 or
empty = all supported channels).
string
<report-interval>
Time between two spectral reports from the AP in
millisecond (<min> - <max>, 0 or empty = 1000ms).
string
execute wireless-controller upload-wtp-image ftp
Upload a WTP image from FTP server.
execute wireless-controller upload-wtp-image ftp <string> <ftp server>[:ftp port] <Enter>|<user>
<passwd>
Parameter
Description
Type
Size
<string>
WTP image file name on the remote server.
string
<ftp server>[:ftp
port]
FTP server IPv4, IPv6, or FQDN can be attached with
port.
string
<Enter>|<user>
FTP username may be needed.
string
<passwd>
FTP password.
string
execute wireless-controller upload-wtp-image tftp
Upload a WTP image from TFTP server.
FortiOS 8.0.0 CLI Reference
4264
Fortinet Inc.

<!-- 来源页 4265 -->
CLI execute commands
execute wireless-controller upload-wtp-image tftp <string> <tftp server>
Parameter
Description
Type
Size
<string>
File name on the TFTP server.
string
<tftp server>
TFTP server IPv4, IPv6, or FQDN.
string
FortiOS 8.0.0 CLI Reference
4265
Fortinet Inc.
