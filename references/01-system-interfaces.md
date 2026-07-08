# 系统：接口 / Zone / 隧道 / VDOM

> 来源: FortiOS-8.0.0-CLI_Reference.pdf
> 覆盖命令/章节: config system interface, config system zone, config system physical-switch, config system virtual-switch, config system virtual-wire-pair, config system switch-interface, config system vdom, config system vdom-link, config system vdom-dns, config system vdom-netflow, config system vdom-property, config system vdom-radius-server, config system vdom-sflow, config system vdom-exception, config system gre-tunnel, config system ipip-tunnel, config system ipv6-tunnel, config system sit-tunnel, config system geneve, config system pppoe-interface, config system vxlan, config system wccp
> 本文件由 extract_pdf.py 从官方 PDF 自动提取，请勿手动编辑；
> 如需修正请修改 map.json 后重跑脚本。

---


<!-- 来源页 1631 -->
Parameter
Description
Type
Size
Default
server-port
Port to communicate with FortiToken Mobile push
services server (1 - 65535, default = 4433).
integer
Minimum
value: 1
Maximum
value:
65535
4433
status
Enable/disable the use of FortiToken Mobile push
services.
option
-disable
Option
Description
enable
Enable FortiToken Mobile push services.
disable
Disable FortiToken Mobile push services.
config system geneve
Configure GENEVE devices.
config system geneve
Description: Configure GENEVE devices.
edit <name>
set dstport {integer}
set interface {string}
set ip-version [ipv4-unicast|ipv6-unicast]
set remote-ip {ipv4-address}
set remote-ip6 {ipv6-address}
set type [ethernet|ppp]
set vni {integer}
next
end
config system geneve
Parameter
Description
Type
Size
Default
dstport
GENEVE destination port (1 - 65535, default =
6081).
integer
Minimum
value: 1
Maximum
value:
65535
6081
interface
Outgoing interface for GENEVE encapsulated
traffic.
string
Maximum
length: 15
FortiOS 8.0.0 CLI Reference
1631
Fortinet Inc.

---


<!-- 来源页 1685 -->
Parameter
Description
Type
Size
Default
Option
Description
client
Wireless client mode.
fwfap
Obsolete wireless AP mode.
* This parameter may not exist in some models.
** Values may differ between models.
config split-port-mode
Parameter
Description
Type
Size
Default
interface
Split port interface.
string
Maximum
length: 15
split-mode
The configuration mode for the split port interface.
option
-disable
Option
Description
disable
Disable split.
4x10G
Split the port into four 10G ports.
4x25G
Split the port into four 25G ports.
4x50G
Split the port into four 50G ports.
8x50G
Split the port into eight 50G ports.
4x100G
Split the port into four 100G ports.
2x200G
Split the port into two 200G ports.
config system gre-tunnel
Configure GRE tunnel.
config system gre-tunnel
Description: Configure GRE tunnel.
edit <name>
set auto-asic-offload [enable|disable]
set checksum-reception [disable|enable]
set checksum-transmission [disable|enable]
set diffservcode {user}
set dscp-copying [disable|enable]
set interface {string}
set ip-version [4|6]
set keepalive-failtimes {integer}
set keepalive-interval {integer}
FortiOS 8.0.0 CLI Reference
1685
Fortinet Inc.

<!-- 来源页 1686 -->
set key-inbound {integer}
set key-outbound {integer}
set local-gw {ipv4-address-any}
set local-gw6 {ipv6-address}
set loopback-ecmp-offload [disable|enable]
set remote-gw {ipv4-address}
set remote-gw6 {ipv6-address}
set sequence-number-reception [disable|enable]
set sequence-number-transmission [disable|enable]
set use-sdwan [disable|enable]
next
end
config system gre-tunnel
Parameter
Description
Type
Size
Default
auto-asic-offload *
Enable/disable automatic ASIC offloading.
option
-enable
Option
Description
enable
Enable automatic ASIC offloading.
disable
Disable automatic ASIC offloading.
checksum-reception *
Enable/disable validating checksums in
received GRE packets.
option
-disable
Option
Description
disable
Do not validate checksums in received GRE packets.
enable
Validate checksums in received GRE packets.
checksum-transmission *
Enable/disable including checksums in
transmitted GRE packets.
option
-disable
Option
Description
disable
Do not include checksums in transmitted GRE packets.
enable
Include checksums in transmitted GRE packets.
diffservcode
DiffServ setting to be applied to GRE tunnel
outer IP header.
user
Not Specified
dscp-copying
Enable/disable DSCP copying.
option
-disable
Option
Description
disable
Disable DSCP copying.
FortiOS 8.0.0 CLI Reference
1686
Fortinet Inc.

<!-- 来源页 1687 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable DSCP copying.
interface
Interface name.
string
Maximum
length: 15
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
keepalive-failtimes
Number of consecutive unreturned keepalive
messages before a GRE connection is
considered down (1 - 255).
integer
Minimum value:
1 Maximum
value: 255
10
keepalive-interval
Keepalive message interval (0 - 32767, 0 =
disabled).
integer
Minimum value:
0 Maximum
value: 32767
0
key-inbound *
Require received GRE packets contain this key
(0 - 4294967295).
integer
Minimum value:
0 Maximum
value:
4294967295
0
key-outbound
*
Include this key in transmitted GRE packets (0
- 4294967295).
integer
Minimum value:
0 Maximum
value:
4294967295
0
local-gw
IP address of the local gateway.
ipv4-address-any
Not Specified
0.0.0.0
local-gw6
IPv6 address of the local gateway.
ipv6-address
Not Specified
::
loopback-ecmp-offload
*
Enable/disable tunnel over loopback ecmp
offloading support.
option
-disable
Option
Description
disable
Disable multi-tunnel offloading support.
enable
Enable multi-tunnel offloading support.
name
Tunnel name.
string
Maximum
length: 15
FortiOS 8.0.0 CLI Reference
1687
Fortinet Inc.

---


<!-- 来源页 1724 -->
Parameter
Description
Type
Size
Default
Option
Description
software
Prefer CPU to perform Diffie-Hellman calculations.
hardware
Prefer CPX to perform Diffie-Hellman calculations.
global
Use global dh-mode setting.
config dh-group-5
Parameter
Description
Type
Size
Default
keypair-cache
Configure custom key pair cache size for this
Diffie-Hellman group.
option
-global
Option
Description
global
Use global Diffie-Hellman key pair cache setting.
custom
Use custom Diffie-Hellman key pair cache setting.
keypair-count
Number of key pairs to pre-generate for this Diffie-Hellman group (per-worker).
integer
Minimum
value: 0
Maximum
value:
50000
0
mode
Use software (CPU) or hardware (CPX) to perform
calculations for this Diffie-Hellman group.
option
-global
Option
Description
software
Prefer CPU to perform Diffie-Hellman calculations.
hardware
Prefer CPX to perform Diffie-Hellman calculations.
global
Use global dh-mode setting.
config system interface
Configure interfaces.
config system interface
Description: Configure interfaces.
edit <name>
set ac-name {string}
set aggregate {string}
set aggregate-type [physical|vxlan]
set algorithm [L2|L3|...]
FortiOS 8.0.0 CLI Reference
1724
Fortinet Inc.

<!-- 来源页 1725 -->
set alias {string}
set allowaccess {option1}, {option2}, ...
set annex [a|b|...]
set ap-discover [enable|disable]
set arp-egress-cos [cos0|cos1|...]
set arpforward [enable|disable]
set atm-protocol [none|ipoa]
set auth-cert {string}
set auth-portal-addr {string}
set auth-type [auto|pap|...]
set auto-auth-extension-device [enable|disable]
set bandwidth-measure-time {integer}
set bfd [global|enable|...]
set bfd-desired-min-tx {integer}
set bfd-detect-mult {integer}
set bfd-required-min-rx {integer}
set broadcast-forward [enable|disable]
set cli-conn-status {integer}
config client-options
Description: DHCP client options.
edit <id>
set code {integer}
set ip {user}
set type [hex|string|...]
set value {string}
next
end
set color {integer}
set dedicated-to [none|management]
set default-purdue-level [1|1.5|...]
set defaultgw [enable|disable]
set description {var-string}
set detected-peer-mtu {integer}
set detectprotocol {option1}, {option2}, ...
set detectserver {user}
set device-identification [enable|disable]
set device-user-identification [enable|disable]
set devindex {integer}
set dhcp-broadcast-flag [disable|enable]
set dhcp-classless-route-addition [enable|disable]
set dhcp-client-identifier {string}
set dhcp-egress-cos [cos0|cos1|...]
set dhcp-relay-agent-option [enable|disable]
set dhcp-relay-allow-no-end-option [disable|enable]
set dhcp-relay-circuit-id {string}
set dhcp-relay-interface {string}
set dhcp-relay-interface-select-method [auto|sdwan|...]
set dhcp-relay-ip {user}
set dhcp-relay-link-selection {ipv4-address}
set dhcp-relay-request-all-server [disable|enable]
set dhcp-relay-service [disable|enable]
set dhcp-relay-source-ip {ipv4-address}
FortiOS 8.0.0 CLI Reference
1725
Fortinet Inc.

<!-- 来源页 1726 -->
set dhcp-relay-type [regular|ipsec]
set dhcp-relay-vrf-select {integer}
set dhcp-renew-time {integer}
set dhcp-smart-relay [disable|enable]
config dhcp-snooping-server-list
Description: Configure DHCP server access list.
edit <name>
set server-ip {ipv4-address}
next
end
set disc-retry-timeout {integer}
set distance {integer}
set dns-server-override [enable|disable]
set dns-server-protocol {option1}, {option2}, ...
set drop-fragment [enable|disable]
set eap-ca-cert {string}
set eap-identity {string}
set eap-method [tls|peap]
set eap-password {password}
set eap-supplicant [enable|disable]
set eap-user-cert {string}
set egress-cos [disable|cos0|...]
config egress-queues
Description: Configure queues of NP port on egress path.
set cos0 {string}
set cos1 {string}
set cos2 {string}
set cos3 {string}
set cos4 {string}
set cos5 {string}
set cos6 {string}
set cos7 {string}
end
set egress-shaping-profile {string}
set eip {ipv4-address-any}
set estimated-downstream-bandwidth {integer}
set estimated-upstream-bandwidth {integer}
set exclude-signatures {option1}, {option2}, ...
set explicit-ftp-proxy [enable|disable]
set explicit-web-proxy [enable|disable]
set external [enable|disable]
set fail-action-on-extender [soft-restart|hard-restart|...]
set fail-alert-interfaces <name1>, <name2>, ...
set fail-alert-method [link-failed-signal|link-down]
set fail-detect [enable|disable]
set fail-detect-option {option1}, {option2}, ...
set fortilink [enable|disable]
set fortilink-backup-link {integer}
set fortilink-neighbor-detect [lldp|fortilink]
set fortilink-split-interface [enable|disable]
set forward-domain {integer}
set forward-error-correction [none|disable|...]
FortiOS 8.0.0 CLI Reference
1726
Fortinet Inc.

<!-- 来源页 1727 -->
set gateway-address {ipv4-address}
set gwaddr {ipv4-address}
set gwdetect [enable|disable]
set ha-priority {integer}
set icmp-accept-redirect [enable|disable]
set icmp-send-redirect [enable|disable]
set ident-accept [enable|disable]
set idle-timeout {integer}
set ike-saml-server {string}
set inbandwidth {integer}
set inbandwidth-source [default|measured]
set ingress-cos [disable|cos0|...]
set ingress-shaping-profile {string}
set ingress-spillover-threshold {integer}
set interconnect-profile [default|profile1|...]
set interface {string}
set internal {integer}
set ip {ipv4-classnet-host}
set ip-managed-by-fortiipam [inherit-global|enable|...]
set ipam-conflicts [enable|disable]
set ipmac [enable|disable]
set ips-sniffer-mode [enable|disable]
set ipunnumbered {ipv4-address}
config ipv6
Description: IPv6 of interface.
set autoconf [enable|disable]
set cli-conn6-status {integer}
config client-options
Description: DHCP6 client options.
edit <id>
set code {integer}
set ip6 {user}
set type [hex|string|...]
set value {string}
next
end
set dhcp6-client-options {option1}, {option2}, ...
set dhcp6-egress-cos [cos0|cos1|...]
config dhcp6-iapd-list
Description: DHCPv6 IA-PD list.
edit <iaid>
set prefix-hint {ipv6-network}
set prefix-hint-plt {integer}
set prefix-hint-vlt {integer}
next
end
set dhcp6-information-request [enable|disable]
set dhcp6-prefix-delegation [enable|disable]
set dhcp6-relay-interface-id {string}
set dhcp6-relay-ip {user}
set dhcp6-relay-service [disable|enable]
set dhcp6-relay-source-interface [disable|enable]
FortiOS 8.0.0 CLI Reference
1727
Fortinet Inc.

<!-- 来源页 1728 -->
set dhcp6-relay-source-ip {ipv6-address}
set dhcp6-relay-type {option}
set icmp6-send-redirect [enable|disable]
set interface-identifier {ipv6-address}
set ip6-address {ipv6-prefix}
set ip6-adv-rio [enable|disable]
set ip6-allowaccess {option1}, {option2}, ...
set ip6-default-life {integer}
set ip6-delegated-prefix-iaid {integer}
config ip6-delegated-prefix-list
Description: Advertised IPv6 delegated prefix list.
edit <prefix-id>
set autonomous-flag [enable|disable]
set delegated-prefix-iaid {integer}
set dnssl-service [enable|disable]
set onlink-flag [enable|disable]
set rdnss {user}
set rdnss-service [delegated|default|...]
set subnet {ipv6-network}
set upstream-interface {string}
next
end
set ip6-dns-server-override [enable|disable]
config ip6-dnssl-list
Description: Advertised IPv6 DNSS list.
edit <domain>
set dnssl-life-time {integer}
next
end
config ip6-extra-addr
Description: Extra IPv6 address prefixes of interface.
edit <prefix>
next
end
set ip6-hop-limit {integer}
set ip6-link-local {ipv6-prefix}
set ip6-link-mtu {integer}
set ip6-manage-flag [enable|disable]
set ip6-max-interval {integer}
set ip6-mgmt-address {ipv6-prefix}
set ip6-min-interval {integer}
set ip6-mode [static|dhcp|...]
set ip6-other-flag [enable|disable]
config ip6-prefix-list
Description: Advertised prefix list.
edit <prefix>
set autonomous-flag [enable|disable]
set onlink-flag [enable|disable]
set preferred-life-time {integer}
set valid-life-time {integer}
next
end
FortiOS 8.0.0 CLI Reference
1728
Fortinet Inc.

<!-- 来源页 1729 -->
set ip6-prefix-mode [dhcp6|ra]
config ip6-rdnss-list
Description: Advertised IPv6 RDNSS list.
edit <rdnss>
set rdnss-life-time {integer}
next
end
set ip6-reachable-time {integer}
set ip6-retrans-time {integer}
config ip6-route-list
Description: Advertised route list.
edit <route>
set route-life-time {integer}
set route-pref [medium|high|...]
next
end
set ip6-route-pref [medium|high|...]
set ip6-send-adv [enable|disable]
set ip6-subnet {ipv6-prefix}
set ip6-upstream-interface {string}
set nd-cert {string}
set nd-cga-modifier {user}
set nd-mode [basic|SEND-compatible]
set nd-security-level {integer}
set nd-timestamp-delta {integer}
set nd-timestamp-fuzz {integer}
set ra-send-mtu [enable|disable]
set unique-autoconf-addr [enable|disable]
set vrip6_link_local {ipv6-address}
set vrrp-virtual-mac6 [enable|disable]
config vrrp6
Description: IPv6 VRRP configuration.
edit <vrid>
set accept-mode [enable|disable]
set adv-interval {integer}
set ignore-default-route [enable|disable]
set preempt [enable|disable]
set priority {integer}
set start-time {integer}
set status [enable|disable]
set vrdst-priority {integer}
set vrdst6 {ipv6-address}
set vrgrp {integer}
set vrip6 {ipv6-address}
next
end
end
set l2forward [enable|disable]
set l2tp-client [enable|disable]
config l2tp-client-settings
Description: L2TP client settings.
set auth-type [auto|pap|...]
FortiOS 8.0.0 CLI Reference
1729
Fortinet Inc.

<!-- 来源页 1730 -->
set defaultgw [enable|disable]
set distance {integer}
set hello-interval {integer}
set ip {ipv4-classnet-host}
set mtu {integer}
set password {password}
set peer-host {string}
set peer-mask {ipv4-netmask}
set peer-port {integer}
set priority {integer}
set user {string}
end
set lacp-ha-secondary [enable|disable]
set lacp-mode [static|passive|...]
set lacp-speed [slow|fast]
set lcp-echo-interval {integer}
set lcp-max-echo-fails {integer}
set link-up-delay {integer}
set lldp-network-policy {string}
set lldp-reception [enable|disable|...]
set lldp-transmission [enable|disable|...]
set macaddr {mac-address}
set managed-subnetwork-size [4|8|...]
set management-ip {ipv4-classnet-host}
set measured-downstream-bandwidth {integer}
set measured-upstream-bandwidth {integer}
set mediatype [serdes-sfp|sgmii-sfp|...]
set member <interface-name1>, <interface-name2>, ...
set min-links {integer}
set min-links-down [operational|administrative]
set mirroring-direction {option}
config mirroring-filter
Description: Mirroring filter.
set filter-dport {integer}
set filter-dstip {ipv4-classnet-host}
set filter-protocol {integer}
set filter-sport {integer}
set filter-srcip {ipv4-classnet-host}
end
set mirroring-port {string}
set mode [static|dhcp|...]
set monitor-bandwidth [enable|disable]
set mrru {integer}
set mtu {integer}
set mtu-override [enable|disable]
set multilink [enable|disable]
set mux-type [llc-encaps|vc-encaps]
set ndiscforward [enable|disable]
set netbios-forward [disable|enable]
set netflow-sample-rate {integer}
set netflow-sampler [disable|tx|...]
set netflow-sampler-id {integer}
FortiOS 8.0.0 CLI Reference
1730
Fortinet Inc.

<!-- 来源页 1731 -->
set np-qos-profile {integer}
set outbandwidth {integer}
set outbandwidth-source [default|measured]
set padt-retry-timeout {integer}
set password {password}
set phy-mode [vdsl|auto|...]
config phy-setting
Description: PHY settings
set signal-ok-threshold {integer}
end
set ping-serv-status {integer}
set poe [enable|disable]
set polling-interval {integer}
set port-mirroring [disable|enable]
set pppoe-egress-cos [cos0|cos1|...]
set pppoe-unnumbered-negotiate [enable|disable]
set pptp-auth-type [auto|pap|...]
set pptp-client [enable|disable]
set pptp-password {password}
set pptp-server-ip {ipv4-address}
set pptp-timeout {integer}
set pptp-user {string}
set preserve-session-route [enable|disable]
set priority {integer}
set priority-override [enable|disable]
set profiles {option1}, {option2}, ...
set proxy-captive-portal [enable|disable]
set pvc-atm-qos [cbr|rt-vbr|...]
set pvc-chan {integer}
set pvc-crc {integer}
set pvc-pcr {integer}
set pvc-scr {integer}
set pvc-vlan-id {integer}
set pvc-vlan-rx-id {integer}
set pvc-vlan-rx-op [pass-through|replace|...]
set pvc-vlan-tx-id {integer}
set pvc-vlan-tx-op [pass-through|replace|...]
set reachable-time {integer}
set redundant-interface {string}
set remote-ip {ipv4-classnet-host}
set replacemsg-override-group {string}
set retransmission [disable|enable]
set ring-rx {integer}
set ring-tx {integer}
set role [lan|wan|...]
set sample-direction [tx|rx|...]
set sample-rate {integer}
set secondary-IP [enable|disable]
config secondaryip
Description: Second IP address of interface.
edit <id>
set allowaccess {option1}, {option2}, ...
FortiOS 8.0.0 CLI Reference
1731
Fortinet Inc.

<!-- 来源页 1732 -->
set detectprotocol {option1}, {option2}, ...
set detectserver {user}
set gwdetect [enable|disable]
set ha-priority {integer}
set ip {ipv4-classnet-host}
set ping-serv-status {integer}
set secip-relay-ip {user}
next
end
set security-8021x-dynamic-vlan-id {integer}
set security-8021x-master {string}
set security-8021x-member-mode [switch|disable]
set security-8021x-mode [default|dynamic-vlan|...]
set security-exempt-list {string}
set security-external-logout {string}
set security-external-web {var-string}
set security-groups <name1>, <name2>, ...
set security-ip-auth-bypass [enable|disable]
set security-mac-auth-bypass [mac-auth-only|enable|...]
set security-mode [none|captive-portal|...]
set security-redirect-url {var-string}
set select-profile-30a-35b [30a|35b]
set service-name {string}
set sflow-sampler [enable|disable]
set sfp-dsl [disable|enable]
set sfp-dsl-adsl-fallback [disable|enable]
set sfp-dsl-autodetect [disable|enable]
set sfp-dsl-mac {mac-address}
set snmp-index {integer}
set speed [auto|10full|...]
set spillover-threshold {integer}
set src-check [enable|disable]
set status [up|down]
set stp [disable|enable]
set stp-edge [disable|enable]
set stp-ha-secondary [disable|enable|...]
set stpforward [enable|disable]
set stpforward-mode [rpl-all-ext-id|rpl-bridge-ext-id|...]
set subst [enable|disable]
set substitute-dst-mac {mac-address}
set sw-algorithm [l2|l3|...]
set swc-first-create {integer}
set swc-vlan {integer}
set switch {string}
set switch-controller-access-vlan [enable|disable]
set switch-controller-arp-inspection [enable|disable|...]
set switch-controller-dhcp-snooping [enable|disable]
set switch-controller-dhcp-snooping-option82 [enable|disable]
set switch-controller-dhcp-snooping-verify-mac [enable|disable]
set switch-controller-dynamic {string}
set switch-controller-feature [none|default-vlan|...]
set switch-controller-fortilink-settings {string}
FortiOS 8.0.0 CLI Reference
1732
Fortinet Inc.

<!-- 来源页 1733 -->
set switch-controller-igmp-snooping [enable|disable]
set switch-controller-igmp-snooping-fast-leave [enable|disable]
set switch-controller-igmp-snooping-proxy [enable|disable]
set switch-controller-iot-scanning [enable|disable]
set switch-controller-learning-limit {integer}
set switch-controller-mgmt-vlan {integer}
set switch-controller-nac {string}
set switch-controller-netflow-collect [disable|enable]
set switch-controller-offload [enable|disable]
set switch-controller-offload-gw [enable|disable]
set switch-controller-offload-ip {ipv4-address}
set switch-controller-rspan-mode [disable|enable]
set switch-controller-source-ip [outbound|fixed]
set switch-controller-traffic-policy {string}
set system-id {mac-address}
set system-id-type [auto|user]
config tagging
Description: Config object tagging.
edit <name>
set category {string}
set tags <name1>, <name2>, ...
next
end
set tc-mode [ptm|atm]
set tcp-mss {integer}
set telemetry-discover [enable|disable]
set trunk [enable|disable]
set trust-ip-1 {ipv4-classnet-any}
set trust-ip-2 {ipv4-classnet-any}
set trust-ip-3 {ipv4-classnet-any}
set trust-ip6-1 {ipv6-prefix}
set trust-ip6-2 {ipv6-prefix}
set trust-ip6-3 {ipv6-prefix}
set tx-queue-len {integer}
set type [physical|vlan|...]
set username {string}
set vci {integer}
set vdom {string}
set vectoring [disable|enable]
set vindex {integer}
set virtual-mac {mac-address}
set vlan-id {integer}
set vlan-op-mode [tag|untag|...]
set vlan-protocol [8021q|8021ad]
set vlanforward [enable|disable]
set vlanid {integer}
set vpi {integer}
set vrf {integer}
config vrrp
Description: VRRP configuration.
edit <vrid>
set accept-mode [enable|disable]
FortiOS 8.0.0 CLI Reference
1733
Fortinet Inc.

<!-- 来源页 1734 -->
set adv-interval {integer}
set ignore-default-route [enable|disable]
set preempt [enable|disable]
set priority {integer}
config proxy-arp
Description: VRRP Proxy ARP configuration.
edit <id>
set ip {user}
next
end
set start-time {integer}
set status [enable|disable]
set version [2|3]
set vrdst {ipv4-address-any}
set vrdst-priority {integer}
set vrgrp {integer}
set vrip {ipv4-address-any}
next
end
set vrrp-virtual-mac [enable|disable]
set wccp [enable|disable]
set weight {integer}
set wifi-5g-threshold {string}
set wifi-acl [allow|deny]
set wifi-ap-band [any|5g-preferred|...]
set wifi-auth [PSK|radius|...]
set wifi-auto-connect [enable|disable]
set wifi-auto-save [enable|disable]
set wifi-broadcast-ssid [enable|disable]
set wifi-dns-server1 {ipv4-address}
set wifi-dns-server2 {ipv4-address}
set wifi-encrypt [TKIP|AES]
set wifi-fragment-threshold {integer}
set wifi-gateway {ipv4-address}
set wifi-key {password}
set wifi-keyindex {integer}
set wifi-mac-filter [enable|disable]
config wifi-mac-list
Description: MAC filter list.
edit <id>
set mac {mac-address}
next
end
config wifi-networks
Description: WiFi network table.
edit <id>
set wifi-ca-certificate {string}
set wifi-client-certificate {string}
set wifi-eap-type [both|tls|...]
set wifi-encrypt [TKIP|AES]
set wifi-key {password}
set wifi-keyindex {integer}
FortiOS 8.0.0 CLI Reference
1734
Fortinet Inc.

<!-- 来源页 1735 -->
set wifi-passphrase {password}
set wifi-private-key {string}
set wifi-private-key-password {password}
set wifi-security [open|wep64|...]
set wifi-ssid {string}
set wifi-username {string}
next
end
set wifi-passphrase {password}
set wifi-radius-server {string}
set wifi-rts-threshold {integer}
set wifi-security [open|wep64|...]
set wifi-ssid {string}
set wifi-usergroup {string}
set wins-ip {ipv4-address}
next
end
config system interface
Parameter
Description
Type
Size
Default
ac-name
PPPoE server name.
string
Maximum
length: 63
aggregate
Aggregate interface. Read-only.
string
Maximum
length: 15
aggregate-type
Type of aggregation.
option
-physical
Option
Description
physical
Physical interface aggregation.
vxlan
VXLAN interface aggregation.
algorithm
Frame distribution algorithm.
option
-L4
Option
Description
L2
Use layer 2 address for distribution.
L3
Use layer 3 address for distribution.
L4
Use layer 4 information for distribution.
NPU-GRE
Use L4 and GRE inner header information for distribution.
Source-MAC
Use source MAC address for distribution.
alias
Alias will be displayed with the
interface name to make it easier
to distinguish.
string
Maximum
length: 25
FortiOS 8.0.0 CLI Reference
1735
Fortinet Inc.

<!-- 来源页 1736 -->
Parameter
Description
Type
Size
Default
allowaccess
Permitted types of management
access to this interface.
option
-Option
Description
ping
PING access.
https
HTTPS access.
ssh
SSH access.
snmp
SNMP access.
http
HTTP access.
telnet
TELNET access.
fgfm
FortiManager access.
radius-acct
RADIUS accounting access.
probe-response
Probe access.
fabric
Security Fabric access.
ftm
FTM access.
speed-test
Speed test access.
scim
System for Cross-domain Identity Management (SCIM) access.
dnp
DNP access.
icond
Industrial Connectivity service access.
mqtt
MQTT access.
annex *
Set xDSL annex type.
option
-a
Option
Description
a
xDSL Annex A
b
xDSL Annex B
i
xDSL Annex I
j
xDSL Annex J
m
xDSL Annex M
al
xDSL Annex AL
bj
xDSL Annex BJ
aijlm
xDSL Annex AIJLM
FortiOS 8.0.0 CLI Reference
1736
Fortinet Inc.

<!-- 来源页 1737 -->
Parameter
Description
Type
Size
Default
ap-discover
Enable/disable automatic
registration of unknown FortiAP
devices.
option
-enable
Option
Description
enable
Enable automatic registration of unknown FortiAP devices.
disable
Disable automatic registration of unknown FortiAP devices.
arp-egress-cos *
CoS in VLAN tag for outgoing
ARP packets.
option
-cos0
Option
Description
cos0
CoS 0.
cos1
CoS 1.
cos2
CoS 2.
cos3
CoS 3.
cos4
CoS 4.
cos5
CoS 5.
cos6
CoS 6.
cos7
CoS 7.
arpforward
Enable/disable ARP forwarding.
option
-enable
Option
Description
enable
Enable ARP forwarding.
disable
Disable ARP forwarding.
atm-protocol *
ATM protocol.
option
-none
Option
Description
none
Not over ATM.
ipoa
IPoA RFC2684.
auth-cert
HTTPS server certificate.
string
Maximum
length: 35
auth-portal-addr
Address of captive portal.
string
Maximum
length: 63
auth-type
PPP authentication type to use.
option
-auto
FortiOS 8.0.0 CLI Reference
1737
Fortinet Inc.

<!-- 来源页 1738 -->
Parameter
Description
Type
Size
Default
Option
Description
auto
Automatically choose authentication.
pap
PAP authentication.
chap
CHAP authentication.
mschapv1
MS-CHAPv1 authentication.
mschapv2
MS-CHAPv2 authentication.
auto-auth-extension-device
Enable/disable automatic
authorization of dedicated
Fortinet extension device on this
interface.
option
-disable
Option
Description
enable
Enable automatic authorization of dedicated Fortinet extension
device on this interface.
disable
Disable automatic authorization of dedicated Fortinet extension
device on this interface.
bandwidth-measure-time
Bandwidth measure time.
integer
Minimum value:
0 Maximum
value:
4294967295
0
bfd
Bidirectional Forwarding
Detection (BFD) settings.
option
-global
Option
Description
global
BFD behavior of this interface will be based on global configuration.
enable
Enable BFD on this interface and ignore global configuration.
disable
Disable BFD on this interface and ignore global configuration.
bfd-desired-min-tx
BFD desired minimal transmit
interval.
integer
Minimum value:
1 Maximum
value: 100000
250
bfd-detect-mult
BFD detection multiplier.
integer
Minimum value:
1 Maximum
value: 50
3
bfd-required-min-rx
BFD required minimal receive
interval.
integer
Minimum value:
1 Maximum
value: 100000
250
FortiOS 8.0.0 CLI Reference
1738
Fortinet Inc.

<!-- 来源页 1739 -->
Parameter
Description
Type
Size
Default
broadcast-forward
Enable/disable broadcast
forwarding.
option
-disable
Option
Description
enable
Enable broadcast forwarding.
disable
Disable broadcast forwarding.
cli-conn-status
CLI connection status. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
color
Color of icon on the GUI.
integer
Minimum value:
0 Maximum
value: 32
0
dedicated-to
Configure interface for single
purpose.
option
-none
Option
Description
none
Interface not dedicated for any purpose.
management
Dedicate this interface for management purposes only.
default-purdue-level
default purdue level of device
detected on this interface.
option
-3
Option
Description
1
Level 1 - Basic Control
1.5
Level 1.5
2
Level 2 - Area Supervisory Control
2.5
Level 2.5
3
Level 3 - Operations & Control
3.5
Level 3.5
4
Level 4 - Business Planning & Logistics
5
Level 5 - Enterprise Network
5.5
Level 5.5
defaultgw
Enable to get the gateway IP from
the DHCP or PPPoE server.
option
-enable
FortiOS 8.0.0 CLI Reference
1739
Fortinet Inc.

<!-- 来源页 1740 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable default gateway.
disable
Disable default gateway.
description
Description.
var-string
Maximum
length: 255
detected-peer-mtu
MTU of detected peer (0 -4294967295). Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
detectprotocol
Protocols used to detect the
server.
option
-ping
Option
Description
ping
PING.
tcp-echo
TCP echo.
udp-echo
UDP echo.
detectserver
Gateway's ping server for this IP.
user
Not Specified
device-identification
Enable/disable passively
gathering of device identity
information about the devices on
the network connected to this
interface.
option
-disable
Option
Description
enable
Enable passive gathering of identity information about hosts.
disable
Disable passive gathering of identity information about hosts.
device-user-identification
Enable/disable passive gathering
of user identity information about
users on this interface.
option
-enable
Option
Description
enable
Enable passive gathering of user identity information about users.
disable
Disable passive gathering of user identity information about users.
FortiOS 8.0.0 CLI Reference
1740
Fortinet Inc.

<!-- 来源页 1741 -->
Parameter
Description
Type
Size
Default
devindex
Device Index. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
dhcp-broadcast-flag
Enable/disable setting of the
broadcast flag in messages sent
by the DHCP client (default =
enable).
option
-enable
Option
Description
disable
Disable broadcast flag.
enable
Enable broadcast flag.
dhcp-classless-route-addition
Enable/disable addition of
classless static routes retrieved
from DHCP server.
option
-disable **
Option
Description
enable
Enable addition of classless static routes retrieved from DHCP server.
disable
Disable addition of classless static routes retrieved from DHCP
server.
dhcp-client-identifier
DHCP client identifier.
string
Maximum
length: 48
dhcp-egress-cos *
CoS in VLAN tag for outgoing
DHCP packets.
option
-cos0
Option
Description
cos0
CoS 0.
cos1
CoS 1.
cos2
CoS 2.
cos3
CoS 3.
cos4
CoS 4.
cos5
CoS 5.
cos6
CoS 6.
cos7
CoS 7.
dhcp-relay-agent-option
Enable/disable DHCP relay agent
option.
option
-enable
FortiOS 8.0.0 CLI Reference
1741
Fortinet Inc.

<!-- 来源页 1742 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable DHCP relay agent option.
disable
Disable DHCP relay agent option.
dhcp-relay-allow-no-end-option
Enable/disable relaying DHCP
messages with no end option.
option
-disable
Option
Description
disable
Disable relaying DHCP messages with no end option.
enable
Enable relaying DHCP messages with no end option.
dhcp-relay-circuit-id
DHCP relay circuit ID.
string
Maximum
length: 64
dhcp-relay-interface
Specify outgoing interface to
reach server.
string
Maximum
length: 15
dhcp-relay-interface-select-method
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
dhcp-relay-ip
DHCP relay IP address.
user
Not Specified
dhcp-relay-link-selection
DHCP relay link selection.
ipv4-address
Not Specified
0.0.0.0
dhcp-relay-request-all-server
Enable/disable sending of DHCP
requests to all servers.
option
-disable
Option
Description
disable
Send DHCP requests only to a matching server.
enable
Send DHCP requests to all servers.
dhcp-relay-service
Enable/disable allowing this
interface to act as a DHCP relay.
option
-disable
FortiOS 8.0.0 CLI Reference
1742
Fortinet Inc.

<!-- 来源页 1743 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
None.
enable
DHCP relay agent.
dhcp-relay-source-ip
IP address used by the DHCP
relay as its source IP.
ipv4-address
Not Specified
0.0.0.0
dhcp-relay-type
DHCP relay type (regular or
IPsec).
option
-regular
Option
Description
regular
Regular DHCP relay.
ipsec
DHCP relay for IPsec.
dhcp-relay-vrf-select
VRF ID used for connection to
server.
integer
Minimum value:
0 Maximum
value: 511
-1
dhcp-renew-time
DHCP renew time in seconds
(300-604800), 0 means use the
renew time provided by the
server.
integer
Minimum value:
300 Maximum
value: 604800
0
dhcp-smart-relay
Enable/disable DHCP smart relay.
option
-disable
Option
Description
disable
Disable DHCP smart relay.
enable
Enable DHCP smart relay.
disc-retry-timeout
Time in seconds to wait before
retrying to start a PPPoE
discovery, 0 means no timeout.
integer
Minimum value:
0 Maximum
value:
4294967295
1
distance
Distance for routes learned
through PPPoE or DHCP, lower
distance indicates preferred
route.
integer
Minimum value:
1 Maximum
value: 255
5
dns-server-override
Enable/disable use DNS acquired
by DHCP or PPPoE.
option
-enable
FortiOS 8.0.0 CLI Reference
1743
Fortinet Inc.

<!-- 来源页 1744 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Use DNS acquired by DHCP or PPPoE.
disable
No not use DNS acquired by DHCP or PPPoE.
dns-server-protocol
DNS transport protocols.
option
-cleartext
Option
Description
cleartext
DNS over UDP/53, DNS over TCP/53.
dot
DNS over TLS/853.
doh
DNS over HTTPS/443.
drop-fragment
Enable/disable drop fragment
packets.
option
-disable
Option
Description
enable
Enable/disable drop fragment packets.
disable
Do not drop fragment packets.
eap-ca-cert
EAP CA certificate name.
string
Maximum
length: 79
eap-identity
EAP identity.
string
Maximum
length: 35
eap-method
EAP method.
option
-Option
Description
tls
TLS.
peap
PEAP.
eap-password
EAP password.
password
Not Specified
eap-supplicant
Enable/disable EAP-Supplicant.
option
-disable
Option
Description
enable
Enable EAP Supplicant.
disable
Disable EAP Supplicant.
eap-user-cert
EAP user certificate name.
string
Maximum
length: 35
egress-cos *
Override outgoing CoS in user
VLAN tag.
option
-disable
FortiOS 8.0.0 CLI Reference
1744
Fortinet Inc.

<!-- 来源页 1745 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable.
cos0
CoS 0.
cos1
CoS 1.
cos2
CoS 2.
cos3
CoS 3.
cos4
CoS 4.
cos5
CoS 5.
cos6
CoS 6.
cos7
CoS 7.
egress-shaping-profile
Outgoing traffic shaping profile.
string
Maximum
length: 35
eip *
External IP. Read-only.
ipv4-address-any
Not Specified
0.0.0.0
estimated-downstream-bandwidth
Estimated maximum downstream
bandwidth (kbps). Used to
estimate link utilization.
integer
Minimum value:
0 Maximum
value:
4294967295
0
estimated-upstream-bandwidth
Estimated maximum upstream
bandwidth (kbps). Used to
estimate link utilization.
integer
Minimum value:
0 Maximum
value:
4294967295
0
exclude-signatures
Exclude IOT or OT application
signatures.
option
-Option
Description
iot
Exclude IOT appctrl signatures.
ot
Exclude OT appctrl signatures.
explicit-ftp-proxy
Enable/disable the explicit FTP
proxy on this interface.
option
-disable
Option
Description
enable
Enable explicit FTP proxy on this interface.
disable
Disable explicit FTP proxy on this interface.
FortiOS 8.0.0 CLI Reference
1745
Fortinet Inc.

<!-- 来源页 1746 -->
Parameter
Description
Type
Size
Default
explicit-web-proxy
Enable/disable the explicit web
proxy on this interface.
option
-disable
Option
Description
enable
Enable explicit Web proxy on this interface.
disable
Disable explicit Web proxy on this interface.
external
Enable/disable identifying the
interface as an external interface
(which usually means it's
connected to the Internet).
option
-disable
Option
Description
enable
Enable identifying the interface as an external interface.
disable
Disable identifying the interface as an external interface.
fail-action-on-extender
Action on FortiExtender when
interface fail.
option
-soft-restart
Option
Description
soft-restart
Soft-restart-on-extender.
hard-restart
Hard-restart-on-extender.
reboot
Reboot-on-extender.
fail-alert-interfaces
<name>
Names of the FortiGate
interfaces to which the link failure
alert is sent.
Names of the non-virtual
interface.
string
Maximum
length: 15
fail-alert-method
Select link-failed-signal or link-down method to alert about a
failed link.
option
-link-down
Option
Description
link-failed-signal
Link-failed-signal.
link-down
Link-down.
fail-detect
Enable/disable fail detection
features for this interface.
option
-disable
FortiOS 8.0.0 CLI Reference
1746
Fortinet Inc.

<!-- 来源页 1747 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable interface failed option status.
disable
Disable interface failed option status.
fail-detect-option
Options for detecting that this
interface has failed.
option
-link-down
Option
Description
detectserver
Use a ping server to determine if the interface has failed.
link-down
Use port detection to determine if the interface has failed.
fortilink
Enable FortiLink to dedicate this
interface to manage other
Fortinet devices.
option
-disable
Option
Description
enable
Enable FortiLink to dedicated interface for managing FortiSwitch
devices.
disable
Disable FortiLink to dedicated interface for managing FortiSwitch
devices.
fortilink-backup-link
FortiLink split interface backup
link. Read-only.
integer
Minimum value:
0 Maximum
value: 255
0
fortilink-neighbor-detect
Protocol for FortiGate neighbor
discovery.
option
-lldp
Option
Description
lldp
Detect FortiLink neighbors using LLDP protocol.
fortilink
Detect FortiLink neighbors using FortiLink protocol.
fortilink-split-interface
Enable/disable FortiLink split
interface to connect member link
to different FortiSwitch in stack
for uplink redundancy.
option
-enable
Option
Description
enable
Enable FortiLink split interface to connect member link to different
FortiSwitch in stack for uplink redundancy.
disable
Disable FortiLink split interface.
FortiOS 8.0.0 CLI Reference
1747
Fortinet Inc.

<!-- 来源页 1748 -->
Parameter
Description
Type
Size
Default
forward-domain
Transparent mode forward
domain.
integer
Minimum value:
0 Maximum
value:
2147483647
0
forward-error-correction *
Enable/disable forward error
correction (FEC).
option
-none
Option
Description
none
none
disable
Disable forward error correction (FEC).
cl91-rs-fec
Reed-Solomon (FEC CL91).
cl74-fc-fec
Fire-Code (FEC CL74).
rs-fec544
Reed-Solomon(544, 514).
auto
Negotaite forward error correction (FEC).
default
Default FEC for mediatype: disable for LR4/DR, CL91 for other modes
gateway-address *
Gateway address.
ipv4-address
Not Specified
0.0.0.0
gwaddr *
Gateway address.
ipv4-address
Not Specified
0.0.0.0
gwdetect
Enable/disable detect gateway
alive for first.
option
-disable
Option
Description
enable
Enable detect gateway alive for first.
disable
Disable detect gateway alive for first.
ha-priority
HA election priority for the PING
server.
integer
Minimum value:
1 Maximum
value: 50
1
icmp-accept-redirect
Enable/disable ICMP accept
redirect.
option
-enable
Option
Description
enable
Enable ICMP accept redirect.
disable
Disable ICMP accept redirect.
icmp-send-redirect
Enable/disable sending of ICMP
redirects.
option
-enable
FortiOS 8.0.0 CLI Reference
1748
Fortinet Inc.

<!-- 来源页 1749 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable sending of ICMP redirects.
disable
Disable sending of ICMP redirects.
ident-accept
Enable/disable authentication for
this interface.
option
-disable
Option
Description
enable
Enable determining a user's identity from packet identification.
disable
Disable determining a user's identity from packet identification.
idle-timeout
PPPoE auto disconnect after idle
timeout seconds, 0 means no
timeout.
integer
Minimum value:
0 Maximum
value: 32767
0
ike-saml-server
Configure IKE authentication
SAML server.
string
Maximum
length: 35
inbandwidth
Bandwidth limit for incoming
traffic (0 - 80000000 kbps), 0
means unlimited.
integer
Minimum value:
0 Maximum
value:
80000000 **
0
inbandwidth-source *
Determine which inbandwidth
values to use for setting shaper.
option
-default
Option
Description
default
Use manually configured bandwidth as inbandwidth source.
measured
Use speedtest measured bandwidth as inbandwidth source.
ingress-cos *
Override incoming CoS in user
VLAN tag on VLAN interface or
assign a priority VLAN tag on
physical interface.
option
-disable
Option
Description
disable
Disable.
cos0
CoS 0.
cos1
CoS 1.
cos2
CoS 2.
cos3
CoS 3.
FortiOS 8.0.0 CLI Reference
1749
Fortinet Inc.

<!-- 来源页 1750 -->
Parameter
Description
Type
Size
Default
Option
Description
cos4
CoS 4.
cos5
CoS 5.
cos6
CoS 6.
cos7
CoS 7.
ingress-shaping-profile
Incoming traffic shaping profile.
string
Maximum
length: 35
ingress-spillover-threshold
Ingress Spillover threshold (0 -16776000 kbps), 0 means
unlimited.
integer
Minimum value:
0 Maximum
value:
16776000
0
interconnect-profile *
Set interconnect profile.
option
-default
Option
Description
default
default interconnect profile
profile1
interconnect profile1 [(10G & IC > 7m/20db-loss) or (25G/27G & IC <
1m)]
profile2
interconnect profile2 [(27G in AP (106G) Auto Profile)]
interface
Interface name.
string
Maximum
length: 15
internal
Implicitly created.
integer
Minimum value:
0 Maximum
value: 255
0
ip
Interface IPv4 address and
subnet mask, syntax: X.X.X.X/24.
ipv4-classnet-host
Not Specified
0.0.0.0 0.0.0.0
ip-managed-by-fortiipam
Enable/disable automatic IP
address assignment of this
interface by FortiIPAM.
option
-inherit-global
Option
Description
inherit-global
Control automatic IP address assignment status using the central
FortiIPAM config.
enable
Enable automatic IP address assignment of this interface by
FortiIPAM.
FortiOS 8.0.0 CLI Reference
1750
Fortinet Inc.

<!-- 来源页 1751 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable automatic IP address assignment of this interface by
FortiIPAM.
ipam-conflicts *
Configure behavior for this
interface on how to handle IPAM
conflict detections.
option
-disable
Option
Description
enable
Ignore this interface when IPAM conflicts are detected.
disable
Do not ignore this interface when IPAM conflicts are detected.
ipmac
Enable/disable IP/MAC binding.
option
-disable
Option
Description
enable
Enable IP/MAC binding.
disable
Disable IP/MAC binding.
ips-sniffer-mode
Enable/disable the use of this
interface as a one-armed sniffer.
option
-disable
Option
Description
enable
Enable IPS sniffer mode.
disable
Disable IPS sniffer mode.
ipunnumbered
Unnumbered IP used for PPPoE
interfaces for which no unique
local address is provided.
ipv4-address
Not Specified
0.0.0.0
l2forward
Enable/disable l2 forwarding.
option
-disable
Option
Description
enable
Enable L2 forwarding.
disable
Disable L2 forwarding.
l2tp-client *
Enable/disable this interface as a
Layer 2 Tunnelling Protocol
(L2TP) client.
option
-disable
Option
Description
enable
Enable L2TP client.
disable
Disable L2TP client.
FortiOS 8.0.0 CLI Reference
1751
Fortinet Inc.

<!-- 来源页 1752 -->
Parameter
Description
Type
Size
Default
lacp-ha-secondary
LACP HA secondary member.
option
-enable
Option
Description
enable
Allow HA secondary member to send/receive LACP messages.
disable
Block HA secondary member from sending/receiving LACP
messages.
lacp-mode
LACP mode.
option
-active
Option
Description
static
Use static aggregation, do not send and ignore any LACP messages.
passive
Passively use LACP to negotiate 802.3ad aggregation.
active
Actively use LACP to negotiate 802.3ad aggregation.
lacp-speed
How often the interface sends
LACP messages.
option
-slow
Option
Description
slow
Send LACP message every 30 seconds.
fast
Send LACP message every second.
lcp-echo-interval
Time in seconds between PPPoE
Link Control Protocol (LCP) echo
requests.
integer
Minimum value:
0 Maximum
value: 32767
5
lcp-max-echo-fails
Maximum missed LCP echo
messages before disconnect.
integer
Minimum value:
0 Maximum
value: 32767
3
link-up-delay
Number of milliseconds to wait
before considering a link is up.
integer
Minimum value:
50 Maximum
value:
3600000
50
lldp-network-policy
LLDP-MED network policy profile.
string
Maximum
length: 35
lldp-reception
Enable/disable Link Layer
Discovery Protocol (LLDP)
reception.
option
-vdom
Option
Description
enable
Enable reception of Link Layer Discovery Protocol (LLDP).
FortiOS 8.0.0 CLI Reference
1752
Fortinet Inc.

<!-- 来源页 1753 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable reception of Link Layer Discovery Protocol (LLDP).
vdom
Use VDOM Link Layer Discovery Protocol (LLDP) reception
configuration setting.
lldp-transmission
Enable/disable Link Layer
Discovery Protocol (LLDP)
transmission.
option
-vdom
Option
Description
enable
Enable transmission of Link Layer Discovery Protocol (LLDP).
disable
Disable transmission of Link Layer Discovery Protocol (LLDP).
vdom
Use VDOM Link Layer Discovery Protocol (LLDP) transmission
configuration setting.
macaddr
Change the interface's MAC
address.
mac-address
Not Specified
00:00:00:00:00:00
**
managed-subnetwork-size
Number of IP addresses to be
allocated by FortiIPAM and used
by this FortiGate unit's DHCP
server settings.
option
-256
Option
Description
4
Allocate a subnet with 4 IP addresses.
8
Allocate a subnet with 8 IP addresses.
16
Allocate a subnet with 16 IP addresses.
32
Allocate a subnet with 32 IP addresses.
64
Allocate a subnet with 64 IP addresses.
128
Allocate a subnet with 128 IP addresses.
256
Allocate a subnet with 256 IP addresses.
512
Allocate a subnet with 512 IP addresses.
1024
Allocate a subnet with 1024 IP addresses.
2048
Allocate a subnet with 2048 IP addresses.
4096
Allocate a subnet with 4096 IP addresses.
8192
Allocate a subnet with 8192 IP addresses.
FortiOS 8.0.0 CLI Reference
1753
Fortinet Inc.

<!-- 来源页 1754 -->
Parameter
Description
Type
Size
Default
Option
Description
16384
Allocate a subnet with 16384 IP addresses.
32768
Allocate a subnet with 32768 IP addresses.
65536
Allocate a subnet with 65536 IP addresses.
131072
Allocate a subnet with 131072 IP addresses.
262144
Allocate a subnet with 262144 IP addresses.
524288
Allocate a subnet with 524288 IP addresses.
1048576
Allocate a subnet with 1048576 IP addresses.
2097152
Allocate a subnet with 2097152 IP addresses.
4194304
Allocate a subnet with 4194304 IP addresses.
8388608
Allocate a subnet with 8388608 IP addresses.
16777216
Allocate a subnet with 16777216 IP addresses.
management-ip
High Availability in-band
management IP address of this
interface.
ipv4-classnet-host
Not Specified
0.0.0.0 0.0.0.0
measured-downstream-bandwidth
Measured downstream
bandwidth (kbps).
integer
Minimum value:
0 Maximum
value:
4294967295
0
measured-upstream-bandwidth
Measured upstream bandwidth
(kbps).
integer
Minimum value:
0 Maximum
value:
4294967295
0
mediatype *
Select SFP media interface type
option
-serdes-sfp **
Option
Description
serdes-sfp
SFP using SerDes Media Interface
sgmii-sfp
SFP using SGMII Media Interface
serdes-copper-sfp
Copper SFP using SerDes media Interface.
none
none
gmii
Use GMII transceiver
sgmii
Use SGMII Interface
FortiOS 8.0.0 CLI Reference
1754
Fortinet Inc.

<!-- 来源页 1755 -->
Parameter
Description
Type
Size
Default
Option
Description
sr
Use Short Range transceiver
lr
Use Long Range transceiver
cr
Use Copper transceiver
sr-lr
Use SFP/SFP+ transceiver
kr
Use DAC transceiver
sr2
Use Short Range transceiver(2 lane)
lr2
Use Long Range transceiver(2 lane)
cr2
Use Copper transceiver(2 lane)
sr4
Use Short Range transceiver(4 lane)
lr4
Use Long Range transceiver(4 lane)
cr4
Use Copper transceiver(4 lane)
dr
Use Depot Reach transceiver
sr8
Use Short Range transceiver(8 lane)
lr8
Use Long Range transceiver(8 lane)
cr8
Use Copper transceiver(8 lane)
member
<interface-name>
Physical interfaces that belong to
the aggregate or redundant
interface.
Physical interface name.
string
Maximum
length: 79
min-links
Minimum number of aggregated
ports that must be up.
integer
Minimum value:
1 Maximum
value: 32
1
min-links-down
Action to take when less than the
configured minimum number of
links are active.
option
-operational
Option
Description
operational
Set the aggregate operationally down.
administrative
Set the aggregate administratively down.
mirroring-direction *
Port mirroring direction.
option
-FortiOS 8.0.0 CLI Reference
1755
Fortinet Inc.

<!-- 来源页 1756 -->
Parameter
Description
Type
Size
Default
Option
Description
rx
Port mirroring receive direction only.
mirroring-port *
Mirroring port.
string
Maximum
length: 15
mode
Addressing mode (static, DHCP,
PPPoE).
option
-static
Option
Description
static
Static setting.
dhcp
External DHCP client mode.
pppoe
External PPPoE mode.
pppoa
External PPPoATM mode.
monitor-bandwidth
Enable monitoring bandwidth on
this interface.
option
-disable
Option
Description
enable
Enable monitoring bandwidth on this interface.
disable
Disable monitoring bandwidth on this interface.
mrru
PPP MRRU (296 - 65535, default
= 1500).
integer
Minimum value:
296 Maximum
value: 65535
1500
mtu
MTU value for this interface.
integer
Minimum value:
0 Maximum
value:
4294967295
1500
mtu-override
Enable to set a custom MTU for
this interface.
option
-disable
Option
Description
enable
Override default MTU.
disable
Use default MTU.
multilink
Enable/disable PPP multilink
support.
option
-disable
FortiOS 8.0.0 CLI Reference
1756
Fortinet Inc.

<!-- 来源页 1757 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable PPP multilink support.
disable
Disable PPP multilink support.
mux-type *
Multiplexer type.
option
-llc-encaps
Option
Description
llc-encaps
LLC encapsulation.
vc-encaps
VC encapsulation.
name
Name.
string
Maximum
length: 15
ndiscforward
Enable/disable NDISC
forwarding.
option
-enable
Option
Description
enable
Enable NDISC forwarding.
disable
Disable NDISC forwarding.
netbios-forward
Enable/disable NETBIOS
forwarding.
option
-disable
Option
Description
disable
Disable NETBIOS forwarding.
enable
Enable NETBIOS forwarding.
netflow-sample-rate
NetFlow sample rate. Sample one
packet every configured number
of packets (1 - 65535, default = 1,
which means standard NetFlow
where all packets are sampled).
integer
Minimum value:
1 Maximum
value: 65535
1
netflow-sampler
Enable/disable NetFlow on this
interface and set the data that
NetFlow collects (rx, tx, or both).
option
-disable
Option
Description
disable
Disable NetFlow protocol on this interface.
tx
Monitor transmitted traffic on this interface.
rx
Monitor received traffic on this interface.
both
Monitor transmitted/received traffic on this interface.
FortiOS 8.0.0 CLI Reference
1757
Fortinet Inc.

<!-- 来源页 1758 -->
Parameter
Description
Type
Size
Default
netflow-sampler-id
Netflow sampler ID.
integer
Minimum value:
1 Maximum
value: 254
0
np-qos-profile *
NP QoS profile ID.
integer
Minimum value:
0 Maximum
value: 15
0
outbandwidth
Bandwidth limit for outgoing
traffic (0 - 80000000 kbps).
integer
Minimum value:
0 Maximum
value:
80000000 **
0
outbandwidth-source *
Determine which outbandwidth
values to use for setting shaper.
option
-default
Option
Description
default
Use manually configured bandwidth as outbandwidth source.
measured
Use speedtest measured bandwidth as outbandwidth source.
padt-retry-timeout
PPPoE Active Discovery
Terminate (PADT) used to
terminate sessions after an idle
time.
integer
Minimum value:
0 Maximum
value:
4294967295
1
password
PPPoE account's password.
password
Not Specified
phy-mode *
DSL physical mode.
option
-vdsl
Option
Description
vdsl
VDSL.
auto
Auto Sync-Up.
adsl-auto
ADSL Auto Sync-Up.
vdsl2
VDSL2.
adsl2+
ADSL2+.
adsl2
ADSL2.
g-dmt
G.DMT.
t1-413
T1.413.
g-lite
G.lite.
ping-serv-status
PING server status. Read-only.
integer
Minimum value:
0 Maximum
value: 255
0
FortiOS 8.0.0 CLI Reference
1758
Fortinet Inc.

<!-- 来源页 1759 -->
Parameter
Description
Type
Size
Default
poe *
Enable/disable PoE status.
option
-enable
Option
Description
enable
Enable PoE status.
disable
Disable PoE status.
polling-interval
sFlow polling interval in seconds
(1 - 255).
integer
Minimum value:
1 Maximum
value: 255
20
port-mirroring *
Enable/disable NP port mirroring.
option
-disable
Option
Description
disable
Disable NP port mirroring.
enable
Enable NP port mirroring.
pppoe-egress-cos
CoS in VLAN tag for outgoing
PPPoE/PPP packets.
option
-cos0
Option
Description
cos0
CoS 0.
cos1
CoS 1.
cos2
CoS 2.
cos3
CoS 3.
cos4
CoS 4.
cos5
CoS 5.
cos6
CoS 6.
cos7
CoS 7.
pppoe-unnumbered-negotiate
Enable/disable PPPoE
unnumbered negotiation.
option
-enable
Option
Description
enable
Enable IP address negotiating for unnumbered.
disable
Disable IP address negotiating for unnumbered.
pptp-auth-type
PPTP authentication type.
option
-auto
FortiOS 8.0.0 CLI Reference
1759
Fortinet Inc.

<!-- 来源页 1760 -->
Parameter
Description
Type
Size
Default
Option
Description
auto
Automatically choose authentication.
pap
PAP authentication.
chap
CHAP authentication.
mschapv1
MS-CHAPv1 authentication.
mschapv2
MS-CHAPv2 authentication.
pptp-client
Enable/disable PPTP client.
option
-disable
Option
Description
enable
Enable PPTP client.
disable
Disable PPTP client.
pptp-password
PPTP password.
password
Not Specified
pptp-server-ip
PPTP server IP address.
ipv4-address
Not Specified
0.0.0.0
pptp-timeout
Idle timer in minutes (0 for
disabled).
integer
Minimum value:
0 Maximum
value: 65535
0
pptp-user
PPTP user name.
string
Maximum
length: 64
preserve-session-route
Enable/disable preservation of
session route when dirty.
option
-disable
Option
Description
enable
Enable preservation of session route when dirty.
disable
Disable preservation of session route when dirty.
priority
Priority of learned routes.
integer
Minimum value:
1 Maximum
value: 65535
1
priority-override
Enable/disable fail back to higher
priority port once recovered.
option
-enable
Option
Description
enable
Enable fail back to higher priority port once recovered.
disable
Disable fail back to higher priority port once recovered.
FortiOS 8.0.0 CLI Reference
1760
Fortinet Inc.

<!-- 来源页 1761 -->
Parameter
Description
Type
Size
Default
profiles *
Set allowed VDSL profiles.
option
-17a 30a
Option
Description
8a
Enable VDSL Profile 8A.
8b
Enable VDSL Profile 8B.
8c
Enable VDSL Profile 8C.
8d
Enable VDSL Profile 8D.
12a
Enable VDSL Profile 12A.
12b
Enable VDSL Profile 12B.
17a
Enable VDSL Profile 17A.
30a
Enable VDSL Profile 30A.
35b
Enable VDSL Profile 35B.
proxy-captive-portal
Enable/disable proxy captive
portal on this interface.
option
-disable
Option
Description
enable
Enable proxy captive portal on this interface.
disable
Disable proxy captive portal on this interface.
pvc-atm-qos *
SFP-DSL ADSL Fallback PVC
ATM QoS.
option
-ubr
Option
Description
cbr
ATM QoS CBR.
rt-vbr
ATM QoS rt-VBR.
nrt-vbr
ATM QoS nrt-VBR.
ubr
ATM QoS CCBR.
pvc-chan *
SFP-DSL ADSL Fallback PVC
Channel.
integer
Minimum value:
0 Maximum
value: 7
0
pvc-crc *
SFP-DSL ADSL Fallback PVC CRC
Option: bit0: sar LLC preserve,
bit1: ream LLC preserve, bit2:
ream VC-MUX has crc.
integer
Minimum value:
0 Maximum
value: 7
2
FortiOS 8.0.0 CLI Reference
1761
Fortinet Inc.

<!-- 来源页 1762 -->
Parameter
Description
Type
Size
Default
pvc-pcr *
SFP-DSL ADSL Fallback PVC
Packet Cell Rate in cells (0 -5500).
integer
Minimum value:
0 Maximum
value: 5500
0
pvc-scr *
SFP-DSL ADSL Fallback PVC
Sustainable Cell Rate in cells (0 -5500).
integer
Minimum value:
0 Maximum
value: 5500
0
pvc-vlan-id *
SFP-DSL ADSL Fallback PVC
VLAN ID.
integer
Minimum value:
1 Maximum
value: 4094
7
pvc-vlan-rx-id *
SFP-DSL ADSL Fallback PVC
VLANID RX.
integer
Minimum value:
1 Maximum
value: 4094
7
pvc-vlan-rx-op *
SFP-DSL ADSL Fallback PVC
VLAN RX op.
option
-pass-through
Option
Description
pass-through
PVC VLAN Tag Passthrough.
replace
PVC VLAN Tag Replace.
remove
PVC VLAN Tag Remove.
pvc-vlan-tx-id *
SFP-DSL ADSL Fallback PVC
VLAN ID TX.
integer
Minimum value:
1 Maximum
value: 4094
7
pvc-vlan-tx-op *
SFP-DSL ADSL Fallback PVC
VLAN TX op.
option
-remove
Option
Description
pass-through
PVC VLAN Tag Passthrough.
replace
PVC VLAN Tag Replace.
remove
PVC VLAN Tag Remove.
reachable-time
IPv4 reachable time in
milliseconds (30000 - 3600000,
default = 30000).
integer
Minimum value:
30000
Maximum
value:
3600000
30000
redundant-interface
Redundant interface. Read-only.
string
Maximum
length: 15
FortiOS 8.0.0 CLI Reference
1762
Fortinet Inc.

<!-- 来源页 1763 -->
Parameter
Description
Type
Size
Default
remote-ip
Remote IP address of tunnel.
ipv4-classnet-host
Not Specified
0.0.0.0 0.0.0.0
replacemsg-override-group
Replacement message override
group.
string
Maximum
length: 35
retransmission *
Enable/disable DSL
retransmission.
option
-enable
Option
Description
disable
Disable retransmission.
enable
Enable retransmission.
ring-rx *
RX ring size.
integer
Minimum value:
0 Maximum
value:
4294967295
0
ring-tx *
TX ring size.
integer
Minimum value:
0 Maximum
value:
4294967295
0
role
Interface role.
option
-undefined
Option
Description
lan
Connected to local network of endpoints.
wan
Connected to Internet.
dmz
Connected to server zone.
undefined
Interface has no specific role.
sample-direction
Data that NetFlow collects (rx, tx,
or both).
option
-both
Option
Description
tx
Monitor transmitted traffic on this interface.
rx
Monitor received traffic on this interface.
both
Monitor transmitted/received traffic on this interface.
sample-rate
sFlow sample rate (10 - 99999).
integer
Minimum value:
10 Maximum
value: 99999
2000
FortiOS 8.0.0 CLI Reference
1763
Fortinet Inc.

<!-- 来源页 1764 -->
Parameter
Description
Type
Size
Default
secondary-IP
Enable/disable adding a
secondary IP to this interface.
option
-disable
Option
Description
enable
Enable secondary IP.
disable
Disable secondary IP.
security-8021x-dynamic-vlan-id
*
VLAN ID for virtual switch.
integer
Minimum value:
0 Maximum
value: 4094
0
security-8021x-master *
802.1X master virtual-switch.
string
Maximum
length: 15
security-8021x-member-mode *
802.1X member mode.
option
-switch
Option
Description
switch
This member will use switch 802.1X configuration.
disable
This member will disable 802.1X configuration.
security-8021x-mode *
802.1X mode.
option
-default
Option
Description
default
802.1X default mode.
dynamic-vlan
802.1X dynamic VLAN (master) mode.
fallback
802.1X fallback (master) mode.
slave
802.1X slave mode.
security-exempt-list
Name of security-exempt-list.
string
Maximum
length: 35
security-external-logout
URL of external authentication
logout server.
string
Maximum
length: 127
security-external-web
URL of external authentication
web server.
var-string
Maximum
length: 1023
security-groups
<name>
User groups that can
authenticate with the captive
portal.
Names of user groups that can
authenticate with the captive
portal.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
1764
Fortinet Inc.

<!-- 来源页 1765 -->
Parameter
Description
Type
Size
Default
security-ip-auth-bypass
Enable/disable IP authentication
bypass.
option
-disable
Option
Description
enable
Enable IP authentication bypass.
disable
Disable IP authentication bypass.
security-mac-auth-bypass
Enable/disable MAC
authentication bypass.
option
-disable
Option
Description
mac-auth-only
Enable MAC authentication bypass without EAP.
enable
Enable MAC authentication bypass.
disable
Disable MAC authentication bypass.
security-mode
Turn on captive portal
authentication for this interface.
option
-none
Option
Description
none
No security option.
captive-portal
Captive portal authentication.
802.1X
802.1X port-based authentication.
security-redirect-url
URL redirection after
disclaimer/authentication.
var-string
Maximum
length: 1023
select-profile-30a-35b *
Select VDSL Profile 30a or 35b.
option
-35b
Option
Description
30a
Enable VDSL Profile 30A.
35b
Enable VDSL Profile 35B.
service-name
PPPoE service name.
string
Maximum
length: 63
sflow-sampler
Enable/disable sFlow on this
interface.
option
-disable
Option
Description
enable
Enable sFlow protocol on this interface.
disable
Disable sFlow protocol on this interface.
FortiOS 8.0.0 CLI Reference
1765
Fortinet Inc.

<!-- 来源页 1766 -->
Parameter
Description
Type
Size
Default
sfp-dsl *
Enable/disable SFP DSL.
option
-disable
Option
Description
disable
Disable SFP DSL.
enable
Enable SFP DSL.
sfp-dsl-adsl-fallback *
Enable/disable SFP DSL ADSL
fallback.
option
-disable
Option
Description
disable
Disable SFP DSL ADSL fallback.
enable
Enable SFP DSL ADSL fallback.
sfp-dsl-autodetect *
Enable/disable SFP DSL MAC
address autodetect.
option
-enable
Option
Description
disable
Disable SFP DSL MAC address autodetect.
enable
Enable SFP DSL MAC address autodetect.
sfp-dsl-mac *
SFP DSL MAC address.
mac-address
Not Specified
00:00:00:00:00:00
snmp-index
Permanent SNMP Index of the
interface.
integer
Minimum value:
0 Maximum
value:
2147483647
0
speed
Interface speed. The default
setting and the options available
depend on the interface
hardware.
option
-auto
Option
Description
auto
Automatically adjust speed.
10full
10M full-duplex.
10half
10M half-duplex.
100full
100M full-duplex.
100half
100M half-duplex.
100auto
100M auto-negotiation.
FortiOS 8.0.0 CLI Reference
1766
Fortinet Inc.

<!-- 来源页 1767 -->
Parameter
Description
Type
Size
Default
Option
Description
1000full
1000M full-duplex.
1000auto
1000M auto adjust.
10000full
10G full-duplex.
10000auto
10G auto-negotiation.
2500auto
2500M auto-negotiation.
5000auto
5000M auto-negotiation.
25000full
25G full-duplex.
25000auto
25G auto-negotiation.
40000full
40G full-duplex.
40000auto
40G auto-negotiation.
50000full
50G full-duplex.
50000auto
50G auto-negotiation.
100Gfull
100G full-duplex.
100Gauto
100G auto-negotiation.
200Gfull
200G full-duplex.
200Gauto
200G auto-negotiation.
400Gfull
400G full-duplex.
400Gauto
400G auto-negotiation.
sgmii-auto
Serial Gigabit Media Independent Interface (SGMII), automatically
adjust speed.
sgmii-100full
Serial Gigabit Media Independent Interface (SGMII), forced 100M full-duplex.
spillover-threshold
Egress Spillover threshold (0 -16776000 kbps), 0 means
unlimited.
integer
Minimum value:
0 Maximum
value:
16776000
0
src-check
Enable/disable source IP check.
option
-enable
Option
Description
enable
Enable source IP check.
disable
Disable source IP check.
FortiOS 8.0.0 CLI Reference
1767
Fortinet Inc.

<!-- 来源页 1768 -->
Parameter
Description
Type
Size
Default
status
Bring the interface up or shut the
interface down.
option
-up
Option
Description
up
Bring the interface up.
down
Shut the interface down.
stp *
Enable/disable STP.
option
-disable
Option
Description
disable
Disable STP.
enable
Enable STP.
stp-edge *
Enable/disable as STP edge port.
option
-disable
Option
Description
disable
Disable STP edge port.
enable
Enable STP edge port.
stp-ha-secondary *
Control STP behavior on HA
secondary.
option
-priority-adjust
Option
Description
disable
Disable STP negotiation on HA secondary.
enable
Enable STP negotiation on HA secondary.
priority-adjust
Enable STP negotiation on HA secondary and make priority lower
than HA primary.
stpforward
Enable/disable STP forwarding.
option
-disable
Option
Description
enable
Enable STP forwarding.
disable
Disable STP forwarding.
stpforward-mode
Configure STP forwarding mode.
option
-rpl-all-ext-id
Option
Description
rpl-all-ext-id
Replace all extension IDs (root, bridge).
FortiOS 8.0.0 CLI Reference
1768
Fortinet Inc.

<!-- 来源页 1769 -->
Parameter
Description
Type
Size
Default
Option
Description
rpl-bridge-ext-id
Replace the bridge extension ID only.
rpl-nothing
Replace nothing.
subst
Enable to always send packets
from this interface to a
destination MAC address.
option
-disable
Option
Description
enable
Send packets from this interface.
disable
Do not send packets from this interface.
substitute-dst-mac
Destination MAC address that all
packets are sent to from this
interface.
mac-address
Not Specified
00:00:00:00:00:00
sw-algorithm *
Frame distribution algorithm for
switch.
option
-default
Option
Description
l2
Use layer 2 address for distribution.
l3
Use layer 3 address for distribution.
eh
Use enhanced hashing for distribution.
default
Use the hashing that the driver selects during initialization for
distribution.
swc-first-create
Initial create for switch-controller
VLANs. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
swc-vlan
Creation status for switch-controller VLANs. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
switch
Contained in switch. Read-only.
string
Maximum
length: 15
switch-controller-access-vlan
Block FortiSwitch port-to-port
traffic.
option
-disable
FortiOS 8.0.0 CLI Reference
1769
Fortinet Inc.

<!-- 来源页 1770 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Block FortiSwitch port-to-port traffic on the VLAN, only permitting
traffic to and from the FortiGate.
disable
Allow normal VLAN traffic.
switch-controller-arp-inspection
Enable/disable/Monitor
FortiSwitch ARP inspection.
option
-disable
Option
Description
enable
Enable ARP inspection for FortiSwitch devices.
disable
Disable ARP inspection for FortiSwitch devices.
monitor
Monitor ARP traffic and update DHCP client database with MAC-VLAN-IP.
switch-controller-dhcp-snooping
Switch controller DHCP
snooping.
option
-disable
Option
Description
enable
Enable DHCP snooping for FortiSwitch devices.
disable
Disable DHCP snooping for FortiSwitch devices.
switch-controller-dhcp-snooping-option82
Switch controller DHCP snooping
option82.
option
-disable
Option
Description
enable
Enable DHCP snooping insert option82 for FortiSwitch devices.
disable
Disable DHCP snooping insert option82 for FortiSwitch devices.
switch-controller-dhcp-snooping-verify-mac
Switch controller DHCP snooping
verify MAC.
option
-disable
Option
Description
enable
Enable DHCP snooping verify source MAC for FortiSwitch devices.
disable
Disable DHCP snooping verify source MAC for FortiSwitch devices.
FortiOS 8.0.0 CLI Reference
1770
Fortinet Inc.

<!-- 来源页 1771 -->
Parameter
Description
Type
Size
Default
switch-controller-dynamic
Integrated FortiLink settings for
managed FortiSwitch.
string
Maximum
length: 35
switch-controller-feature
Interface's purpose when
assigning traffic (read only).
option
-none
Option
Description
none
VLAN for generic purpose.
default-vlan
Default VLAN (native) assigned to all switch ports upon discovery.
quarantine
VLAN for quarantined traffic.
rspan
VLAN for RSPAN/ERSPAN mirrored traffic.
voice
VLAN dedicated for voice devices.
video
VLAN dedicated for camera devices.
nac
VLAN dedicated for NAC onboarding devices.
nac-segment
VLAN dedicated for NAC segment devices.
switch-controller-fortilink-settings
*
Integrated FortiLink settings for
managed FortiSwitch.
string
Maximum
length: 35
switch-controller-igmp-snooping
Switch controller IGMP snooping.
option
-disable
Option
Description
enable
Enable IGMP snooping.
disable
Disable IGMP snooping.
switch-controller-igmp-snooping-fast-leave
Switch controller IGMP snooping
fast-leave.
option
-disable
Option
Description
enable
Enable IGMP snooping fast-leave.
disable
Disable IGMP snooping fast-leave.
FortiOS 8.0.0 CLI Reference
1771
Fortinet Inc.

<!-- 来源页 1772 -->
Parameter
Description
Type
Size
Default
switch-controller-igmp-snooping-proxy
Switch controller IGMP snooping
proxy.
option
-disable
Option
Description
enable
Enable IGMP snooping proxy.
disable
Disable IGMP snooping proxy.
switch-controller-iot-scanning
Enable/disable managed
FortiSwitch IoT scanning.
option
-disable
Option
Description
enable
Enable IoT scanning for managed FortiSwitch devices.
disable
Disable IoT scanning for managed FortiSwitch devices.
switch-controller-learning-limit
Limit the number of dynamic
MAC addresses on this VLAN (1 -128, 0 = no limit, default).
integer
Minimum value:
0 Maximum
value: 128
0
switch-controller-mgmt-vlan
VLAN to use for FortiLink
management purposes.
integer
Minimum value:
1 Maximum
value: 4094
4094
switch-controller-nac
Integrated FortiLink settings for
managed FortiSwitch.
string
Maximum
length: 35
switch-controller-netflow-collect
NetFlow collection and
processing.
option
-disable
Option
Description
disable
Disable NetFlow collection.
enable
Enable NetFlow collection.
switch-controller-offload
Enable/disable managed
FortiSwitch routing offload.
option
-disable
Option
Description
enable
Enable routing offload to managed FortiSwitch devices.
disable
Disable routing offload to managed FortiSwitch devices.
FortiOS 8.0.0 CLI Reference
1772
Fortinet Inc.

<!-- 来源页 1773 -->
Parameter
Description
Type
Size
Default
switch-controller-offload-gw
Enable/disable managed
FortiSwitch routing offload
gateway.
option
-disable
Option
Description
enable
Enable routing offload gateway to managed FortiSwitch devices.
disable
Disable routing offload gateway to managed FortiSwitch devices.
switch-controller-offload-ip
IP for routing offload on
FortiSwitch.
ipv4-address
Not Specified
0.0.0.0
switch-controller-rspan-mode
Stop Layer2 MAC learning and
interception of BPDUs and other
packets on this interface.
option
-disable
Option
Description
disable
Disable RSPAN passthrough mode on this VLAN interface.
enable
Enable RSPAN passthrough mode on this VLAN interface.
switch-controller-source-ip
Source IP address used in
FortiLink over L3 connections.
option
-outbound
Option
Description
outbound
Source IP address is that of the outbound interface.
fixed
Source IP address is that of the FortiLink interface.
switch-controller-traffic-policy
Switch controller traffic policy for
the VLAN.
string
Maximum
length: 63
system-id
Define a system ID for the
aggregate interface.
mac-address
Not Specified
00:00:00:00:00:00
system-id-type
Method in which system ID is
generated.
option
-auto
Option
Description
auto
Use the MAC address of the first member.
user
User-defined system ID.
tc-mode *
DSL transfer mode.
option
-ptm
FortiOS 8.0.0 CLI Reference
1773
Fortinet Inc.

<!-- 来源页 1774 -->
Parameter
Description
Type
Size
Default
Option
Description
ptm
Packet transfer mode.
atm
Asynchronous transfer mode.
tcp-mss
TCP maximum segment size. 0
means do not change segment
size.
integer
Minimum value:
48 Maximum
value: 65535
0
telemetry-discover *
Enable/disable automatic
registration of unknown
FortiTelemetry agents.
option
-enable
Option
Description
enable
Enable automatic registration of unknown FortiTelemetry agents.
disable
Disable automatic registration of unknown FortiTelemetry agents.
trunk *
Enable/disable VLAN trunk.
option
-disable
Option
Description
enable
Enable VLAN trunk on this interface.
disable
Disable VLAN trunk on this interface.
trust-ip-1
Trusted host for dedicated
management traffic (0.0.0.0/24
for all hosts).
ipv4-classnet-any
Not Specified
0.0.0.0 0.0.0.0
trust-ip-2
Trusted host for dedicated
management traffic (0.0.0.0/24
for all hosts).
ipv4-classnet-any
Not Specified
0.0.0.0 0.0.0.0
trust-ip-3
Trusted host for dedicated
management traffic (0.0.0.0/24
for all hosts).
ipv4-classnet-any
Not Specified
0.0.0.0 0.0.0.0
trust-ip6-1
Trusted IPv6 host for dedicated
management traffic (::/0 for all
hosts).
ipv6-prefix
Not Specified
::/0
trust-ip6-2
Trusted IPv6 host for dedicated
management traffic (::/0 for all
hosts).
ipv6-prefix
Not Specified
::/0
trust-ip6-3
Trusted IPv6 host for dedicated
management traffic (::/0 for all
hosts).
ipv6-prefix
Not Specified
::/0
FortiOS 8.0.0 CLI Reference
1774
Fortinet Inc.

<!-- 来源页 1775 -->
Parameter
Description
Type
Size
Default
tx-queue-len *
TX queue length.
integer
Minimum value:
0 Maximum
value: 65536
0
type
Interface type.
option
-vlan
Option
Description
physical
Physical interface.
vlan
VLAN interface.
aggregate
Aggregate interface.
redundant
Redundant interface.
tunnel
Tunnel interface.
vdom-link
VDOM link interface.
loopback
Loopback interface.
switch
Software switch interface.
vap-switch
VAP interface.
wl-mesh
WLAN mesh interface.
fext-wan
FortiExtender interface.
vxlan
VXLAN interface.
geneve
GENEVE interface.
switch-vlan
Switch VLAN interface.
emac-vlan
EMAC VLAN interface.
lan-extension
LAN extension interface.
hard-switch
Hardware switch interface.
wireless
Wireless interface.
username
Username of the PPPoE account,
provided by your ISP.
string
Maximum
length: 64
vci *
Virtual Channel ID.
integer
Minimum value:
0 Maximum
value: 65535
35
vdom
Interface is in this virtual domain
(VDOM).
string
Maximum
length: 31
vectoring *
Enable/disable DSL vectoring.
option
-enable
FortiOS 8.0.0 CLI Reference
1775
Fortinet Inc.

<!-- 来源页 1776 -->
Parameter
Description
Type
Size
Default
Option
Description
disable
Disable vectoring.
enable
Enable vectoring.
vindex
Switch control interface VLAN ID.
Read-only.
integer
Minimum value:
0 Maximum
value: 65535
0
virtual-mac
Change the interface's virtual
MAC address.
mac-address
Not Specified
00:00:00:00:00:00
vlan-id *
Vlan ID.
integer
Minimum value:
0 Maximum
value: 4095
1
vlan-op-mode *
Configure DSL 802.1q mode.
option
-passthrough
Option
Description
tag
802.1q Tagged.
untag
802.1q Un-Tagged.
passthrough
802.1q Passthrough.
vlan-protocol
Ethernet protocol of VLAN.
option
-8021q
Option
Description
8021q
IEEE 802.1Q.
8021ad
IEEE 802.1AD.
vlanforward
Enable/disable traffic forwarding
between VLANs on this interface.
option
-disable
Option
Description
enable
Enable traffic forwarding.
disable
Disable traffic forwarding.
vlanid
VLAN ID (1 - 4094).
integer
Minimum value:
1 Maximum
value: 4094
0
vpi *
Virtual Path ID.
integer
Minimum value:
0 Maximum
value: 255
0
FortiOS 8.0.0 CLI Reference
1776
Fortinet Inc.

<!-- 来源页 1777 -->
Parameter
Description
Type
Size
Default
vrf
Virtual Routing Forwarding ID.
integer
Minimum value:
0 Maximum
value: 511
0
vrrp-virtual-mac
Enable/disable use of virtual MAC
for VRRP.
option
-disable
Option
Description
enable
Enable use of virtual MAC for VRRP.
disable
Disable use of virtual MAC for VRRP.
wccp
Enable/disable WCCP on this
interface. Used for encapsulated
WCCP communication between
WCCP clients and servers.
option
-disable
Option
Description
enable
Enable WCCP protocol on this interface.
disable
Disable WCCP protocol on this interface.
weight
Default weight for static routes (if
route has no weight configured).
integer
Minimum value:
0 Maximum
value: 255
0
wifi-5g-threshold *
Minimal signal strength to be
considered as a good 5G AP.
string
Maximum
length: 7
-78
wifi-acl *
Access control for MAC
addresses in the MAC list.
option
-deny
Option
Description
allow
Allow.
deny
Deny.
wifi-ap-band *
How to select the AP to connect.
option
-any
Option
Description
any
Connect to the best 2G or 5G AP.
5g-preferred
Connect to the 5G AP if a good 5G AP exists.
5g-only
Only connect to the 5G AP.
wifi-auth *
WiFi authentication.
option
-PSK
FortiOS 8.0.0 CLI Reference
1777
Fortinet Inc.

<!-- 来源页 1778 -->
Parameter
Description
Type
Size
Default
Option
Description
PSK
PSK.
radius
RADIUS.
usergroup
User group.
wifi-auto-connect *
Enable/disable WiFi network auto
connect.
option
-enable
Option
Description
enable
Enable WiFi network auto connect.
disable
Disable WiFi network auto connect.
wifi-auto-save *
Enable/disable WiFi network
automatic save.
option
-disable
Option
Description
enable
Enable WiFi network automatic save.
disable
Disable WiFi network automatic save.
wifi-broadcast-ssid *
Enable/disable SSID broadcast in
the beacon.
option
-enable
Option
Description
enable
Enable SSID broadcast in the beacon.
disable
Disable SSID broadcast in the beacon.
wifi-dns-server1
*
DNS server 1.
ipv4-address
Not Specified
0.0.0.0
wifi-dns-server2
*
DNS server 2.
ipv4-address
Not Specified
0.0.0.0
wifi-encrypt *
Data encryption.
option
-AES
Option
Description
TKIP
TKIP.
AES
AES.
wifi-fragment-threshold *
WiFi fragment threshold (800 -2346).
integer
Minimum value:
800 Maximum
value: 2346
2346
FortiOS 8.0.0 CLI Reference
1778
Fortinet Inc.

<!-- 来源页 1779 -->
Parameter
Description
Type
Size
Default
wifi-gateway *
IPv4 default gateway IP address.
ipv4-address
Not Specified
0.0.0.0
wifi-key *
WiFi WEP Key.
password
Not Specified
wifi-keyindex *
WEP key index (1 - 4).
integer
Minimum value:
1 Maximum
value: 4
1
wifi-mac-filter *
Enable/disable MAC filter status.
option
-disable
Option
Description
enable
Enable MAC filter.
disable
Disable MAC filter.
wifi-passphrase
*
WiFi pre-shared key for WPA.
password
Not Specified
wifi-radius-server *
WiFi RADIUS server for WPA.
string
Maximum
length: 35
wifi-rts-threshold *
WiFi RTS threshold (256 - 2346).
integer
Minimum value:
256 Maximum
value: 2346
2346
wifi-security *
Wireless access security of SSID.
option
-wpa-personal
Option
Description
open
Open.
wep64
WEP64.
wep128
WEP128.
wpa-personal
WPA personal.
wpa-enterprise
WPA enterprise.
wpa-only-personal
WPA personal only.
wpa-only-enterprise
WPA enterprise only.
wpa2-only-personal
WPA2 personal only.
wpa2-only-enterprise
WPA2 enterprise only.
wifi-ssid *
IEEE 802.11 Service Set Identifier.
string
Maximum
length: 32
fortinet
FortiOS 8.0.0 CLI Reference
1779
Fortinet Inc.

<!-- 来源页 1780 -->
Parameter
Description
Type
Size
Default
wifi-usergroup *
WiFi user group for WPA.
string
Maximum
length: 35
wins-ip
WINS server IP.
ipv4-address
Not Specified
0.0.0.0
* This parameter may not exist in some models.
** Values may differ between models.
config client-options
Parameter
Description
Type
Size
Default
code
DHCP client option code.
integer
Minimum value:
0 Maximum
value: 255
0
id
ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
ip
DHCP option IPs.
user
Not Specified
type
DHCP client option type.
option
-hex
Option
Description
hex
DHCP option in hex.
string
DHCP option in string.
ip
DHCP option in IP.
fqdn
DHCP option in domain search option format.
value
DHCP client option value.
string
Maximum
length: 312
config dhcp-snooping-server-list
Parameter
Description
Type
Size
Default
name
DHCP server name.
string
Maximum
length: 35
default
server-ip
IP address for DHCP server.
ipv4-address
Not
Specified
0.0.0.0
FortiOS 8.0.0 CLI Reference
1780
Fortinet Inc.

<!-- 来源页 1781 -->
config egress-queues
Parameter
Description
Type
Size
Default
cos0
CoS profile name for CoS 0.
string
Maximum
length: 35
cos1
CoS profile name for CoS 1.
string
Maximum
length: 35
cos2
CoS profile name for CoS 2.
string
Maximum
length: 35
cos3
CoS profile name for CoS 3.
string
Maximum
length: 35
cos4
CoS profile name for CoS 4.
string
Maximum
length: 35
cos5
CoS profile name for CoS 5.
string
Maximum
length: 35
cos6
CoS profile name for CoS 6.
string
Maximum
length: 35
cos7
CoS profile name for CoS 7.
string
Maximum
length: 35
config ipv6
Parameter
Description
Type
Size
Default
autoconf
Enable/disable address auto config.
option
-disable
Option
Description
enable
Enable auto-configuration.
disable
Disable auto-configuration.
cli-conn6-status
CLI IPv6 connection status. Read-only.
integer
Minimum value:
0 Maximum
value:
4294967295
0
dhcp6-client-options
DHCPv6 client options. Read-only.
option
-Option
Description
rapid
Send rapid commit option.
iapd
Send including IA-PD option.
iana
Send including IA-NA option.
FortiOS 8.0.0 CLI Reference
1781
Fortinet Inc.

<!-- 来源页 1782 -->
Parameter
Description
Type
Size
Default
dhcp6-egress-cos *
CoS in VLAN tag for outgoing DHCPv6 packets.
option
-cos0
Option
Description
cos0
CoS 0.
cos1
CoS 1.
cos2
CoS 2.
cos3
CoS 3.
cos4
CoS 4.
cos5
CoS 5.
cos6
CoS 6.
cos7
CoS 7.
dhcp6-information-request
Enable/disable DHCPv6 information request.
option
-disable
Option
Description
enable
Enable DHCPv6 information request.
disable
Disable DHCPv6 information request.
dhcp6-prefix-delegation
Enable/disable DHCPv6 prefix delegation.
option
-disable
Option
Description
enable
Enable DHCPv6 prefix delegation.
disable
Disable DHCPv6 prefix delegation.
dhcp6-relay-interface-id
DHCP6 relay interface ID.
string
Maximum
length: 64
dhcp6-relay-ip
DHCPv6 relay IP address.
user
Not Specified
dhcp6-relay-service
Enable/disable DHCPv6 relay.
option
-disable
Option
Description
disable
Disable DHCPv6 relay
enable
Enable DHCPv6 relay.
FortiOS 8.0.0 CLI Reference
1782
Fortinet Inc.

<!-- 来源页 1783 -->
Parameter
Description
Type
Size
Default
dhcp6-relay-source-interface
Enable/disable use of address on this interface
as the source address of the relay message.
option
-disable
Option
Description
disable
Use address of the egress interface as source address of the relay
message.
enable
Use address of this interface as source address of the relay message.
dhcp6-relay-source-ip
IPv6 address used by the DHCP6 relay as its
source IP.
ipv6-address
Not Specified
::
dhcp6-relay-type
DHCPv6 relay type.
option
-regular
Option
Description
regular
Regular DHCP relay.
icmp6-send-redirect
Enable/disable sending of ICMPv6 redirects.
option
-enable
Option
Description
enable
Enable sending of ICMPv6 redirects.
disable
Disable sending of ICMPv6 redirects.
interface-identifier
IPv6 interface identifier.
ipv6-address
Not Specified
::
ip6-address
Primary IPv6 address prefix. Syntax:
xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xxx.
ipv6-prefix
Not Specified
::/0
ip6-adv-rio
Enable/disable sending advertisements with
route information option.
option
-disable
Option
Description
enable
Enable sending advertisements with route information option.
disable
Disable sending advertisements with route information option.
ip6-allowaccess
Allow management access to the interface.
option
-Option
Description
ping
PING access.
FortiOS 8.0.0 CLI Reference
1783
Fortinet Inc.

<!-- 来源页 1784 -->
Parameter
Description
Type
Size
Default
Option
Description
https
HTTPS access.
ssh
SSH access.
snmp
SNMP access.
http
HTTP access.
telnet
TELNET access.
fgfm
FortiManager access.
fabric
Security Fabric access.
probe-response
Probe access.
scim
System for Cross-domain Identity Management (SCIM) access.
ip6-default-life
Default life (sec).
integer
Minimum value:
0 Maximum
value: 9000
1800
ip6-delegated-prefix-iaid
IAID of obtained delegated-prefix from the
upstream interface.
integer
Minimum value:
0 Maximum
value:
4294967295
0
ip6-dns-server-override
Enable/disable using the DNS server acquired by
DHCP.
option
-enable
Option
Description
enable
Enable using the DNS server acquired by DHCP.
disable
Disable using the DNS server acquired by DHCP.
ip6-hop-limit
Hop limit (0 means unspecified).
integer
Minimum value:
0 Maximum
value: 255
0
ip6-link-local *
IPv6 link-local address of interface.
ipv6-prefix
Not Specified
::/0
ip6-link-mtu
IPv6 link MTU.
integer
Minimum value:
1280 Maximum
value: 16000
0
ip6-manage-flag
Enable/disable the managed flag.
option
-disable
FortiOS 8.0.0 CLI Reference
1784
Fortinet Inc.

<!-- 来源页 1785 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable the managed IPv6 flag.
disable
Disable the managed IPv6 flag.
ip6-max-interval
IPv6 maximum interval (4 to 1800 sec).
integer
Minimum value:
4 Maximum
value: 1800
600
ip6-mgmt-address *
High Availability in-band management IPv6
address of this interface and should be in the
same subnet with primary IPv6 address
ipv6-prefix
Not Specified
::/0
ip6-min-interval
IPv6 minimum interval (3 to 1350 sec).
integer
Minimum value:
3 Maximum
value: 1350
198
ip6-mode
Addressing mode (static, DHCP, delegated).
option
-static
Option
Description
static
Static setting.
dhcp
DHCPv6 client mode.
pppoe
IPv6 over PPPoE mode.
delegated
IPv6 address with delegated prefix.
ip6-other-flag
Enable/disable the other IPv6 flag.
option
-disable
Option
Description
enable
Enable the other IPv6 flag.
disable
Disable the other IPv6 flag.
ip6-prefix-mode
Assigning a prefix from DHCP or RA.
option
-dhcp6
Option
Description
dhcp6
Use delegated prefix from a DHCPv6 client to form a delegated IPv6
address.
ra
Use prefix from RA to form a delegated IPv6 address.
ip6-reachable-time
IPv6 reachable time (milliseconds; 0 means
unspecified).
integer
Minimum value:
0 Maximum
value:
3600000
0
FortiOS 8.0.0 CLI Reference
1785
Fortinet Inc.

<!-- 来源页 1786 -->
Parameter
Description
Type
Size
Default
ip6-retrans-time
IPv6 retransmit time (milliseconds; 0 means
unspecified).
integer
Minimum value:
0 Maximum
value:
4294967295
0
ip6-route-pref
Set route preference to the interface (default =
medium).
option
-medium
Option
Description
medium
Medium route preferences in RA packet.
high
High route preferences in RA packet.
low
Low route preferences in RA packet.
ip6-send-adv
Enable/disable sending advertisements about
the interface.
option
-disable
Option
Description
enable
Enable sending advertisements about this interface.
disable
Disable sending advertisements about this interface.
ip6-subnet
Subnet to routing prefix. Syntax:
xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xxx.
ipv6-prefix
Not Specified
::/0
ip6-upstream-interface
Interface name providing delegated information.
string
Maximum
length: 15
nd-cert
Neighbor discovery certificate.
string
Maximum
length: 35
nd-cga-modifier
Neighbor discovery CGA modifier.
user
Not Specified
nd-mode
Neighbor discovery mode.
option
-basic
Option
Description
basic
Do not support SEND.
SEND-compatible
Support SEND.
nd-security-level
Neighbor discovery security level (0 - 7; 0 =
least secure, default = 0).
integer
Minimum value:
0 Maximum
value: 7
0
nd-timestamp-delta
Neighbor discovery timestamp delta value (1 -3600 sec; default = 300).
integer
Minimum value:
1 Maximum
value: 3600
300
FortiOS 8.0.0 CLI Reference
1786
Fortinet Inc.

<!-- 来源页 1787 -->
Parameter
Description
Type
Size
Default
nd-timestamp-fuzz
Neighbor discovery timestamp fuzz factor (1 -60 sec; default = 1).
integer
Minimum value:
1 Maximum
value: 60
1
ra-send-mtu
Enable/disable sending link MTU in RA packet.
option
-enable
Option
Description
enable
Enable sending link MTU in RA packet.
disable
Disable sending link MTU in RA packet.
unique-autoconf-addr
Enable/disable unique auto config address.
option
-disable
Option
Description
enable
Enable unique auto-configuration address.
disable
Disable unique auto-configuration address.
vrip6_link_
local
Link-local IPv6 address of virtual router.
ipv6-address
Not Specified
::
vrrp-virtual-mac6
Enable/disable virtual MAC for VRRP.
option
-disable
Option
Description
enable
Enable virtual MAC for VRRP.
disable
Disable virtual MAC for VRRP.
* This parameter may not exist in some models.
config client-options
Parameter
Description
Type
Size
Default
code
DHCPv6 option code.
integer
Minimum value:
0 Maximum
value: 255
0
id
ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
ip6
DHCP option IP6s.
user
Not Specified
type
DHCPv6 option type.
option
-hex
FortiOS 8.0.0 CLI Reference
1787
Fortinet Inc.

<!-- 来源页 1788 -->
Parameter
Description
Type
Size
Default
Option
Description
hex
DHCPv6 option in hex.
string
DHCPv6 option in string.
ip6
DHCPv6 option in IP6.
fqdn
DHCPv6 option in domain search option format.
value
DHCPv6 option value (hexadecimal value must
be even).
string
Maximum
length: 312
config dhcp6-iapd-list
Parameter
Description
Type
Size
Default
iaid
Identity association identifier.
integer
Minimum value:
0 Maximum
value:
4294967295
0
prefix-hint
DHCPv6 prefix that will be used as a hint to the
upstream DHCPv6 server.
ipv6-network
Not Specified
::/0
prefix-hint-plt
DHCPv6 prefix hint preferred life time (sec), 0
means unlimited lease time.
integer
Minimum value:
0 Maximum
value:
4294967295
604800
prefix-hint-vlt
DHCPv6 prefix hint valid life time (sec).
integer
Minimum value:
0 Maximum
value:
4294967295
2592000
config ip6-delegated-prefix-list
Parameter
Description
Type
Size
Default
autonomous-flag
Enable/disable the autonomous flag.
option
-enable
Option
Description
enable
Enable the autonomous flag.
disable
Disable the autonomous flag.
FortiOS 8.0.0 CLI Reference
1788
Fortinet Inc.

<!-- 来源页 1789 -->
Parameter
Description
Type
Size
Default
delegated-prefix-iaid
IAID of obtained delegated-prefix from the
upstream interface.
integer
Minimum value:
0 Maximum
value:
4294967295
0
dnssl-service
Enable/disable use of domain from delegated
prefix for DNSSL.
option
-enable
Option
Description
enable
Enable use of domain from delegated prefix for DNSSL.
disable
Disable use of domain from delegated prefix for DNSSL.
onlink-flag
Enable/disable the onlink flag.
option
-enable
Option
Description
enable
Enable the onlink flag.
disable
Disable the onlink flag.
prefix-id
Prefix ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
rdnss
Recursive DNS server option.
user
Not Specified
rdnss-service
Recursive DNS service option.
option
-specify
Option
Description
delegated
Delegated RDNSS settings.
default
System RDNSS settings.
specify
Specify recursive DNS servers.
subnet
Add subnet ID to routing prefix.
ipv6-network
Not Specified
::/0
upstream-interface
Name of the interface that provides delegated
information.
string
Maximum
length: 15
config ip6-dnssl-list
Parameter
Description
Type
Size
Default
dnssl-life-time
DNS search list time in seconds (0 -4294967295, default = 1800).
integer
Minimum value:
0 Maximum
value:
4294967295
1800
FortiOS 8.0.0 CLI Reference
1789
Fortinet Inc.

<!-- 来源页 1790 -->
Parameter
Description
Type
Size
Default
domain
Domain name.
string
Maximum
length: 79
config ip6-extra-addr
Parameter
Description
Type
Size
Default
prefix
IPv6 address prefix.
ipv6-prefix
Not Specified
::/0
config ip6-prefix-list
Parameter
Description
Type
Size
Default
autonomous-flag
Enable/disable the autonomous flag.
option
-enable
Option
Description
enable
Enable the autonomous flag.
disable
Disable the autonomous flag.
onlink-flag
Enable/disable the onlink flag.
option
-enable
Option
Description
enable
Enable the onlink flag.
disable
Disable the onlink flag.
preferred-life-time
Preferred life time (sec).
integer
Minimum value:
0 Maximum
value:
4294967295
604800
prefix
IPv6 prefix.
ipv6-network
Not Specified
::/0
valid-life-time
Valid life time (sec).
integer
Minimum value:
0 Maximum
value:
4294967295
2592000
FortiOS 8.0.0 CLI Reference
1790
Fortinet Inc.

<!-- 来源页 1791 -->
config ip6-rdnss-list
Parameter
Description
Type
Size
Default
rdnss
Recursive DNS server option.
ipv6-address
Not Specified
::
rdnss-life-time
Recursive DNS server life time in seconds (0 -4294967295, default = 1800).
integer
Minimum value:
0 Maximum
value:
4294967295
1800
config ip6-route-list
Parameter
Description
Type
Size
Default
route
IPv6 route.
ipv6-network
Not
Specified
::/0
route-life-time
Route life time in seconds (0 - 65535, default =
1800).
integer
Minimum
value: 0
Maximum
value:
65535
1800
route-pref
Set route preference to the interface (default =
medium).
option
-medium
Option
Description
medium
Medium route preferences in RA packet.
high
High route preferences in RA packet.
low
Low route preferences in RA packet.
config vrrp6
Parameter
Description
Type
Size
Default
accept-mode
Enable/disable accept mode.
option
-enable
Option
Description
enable
Enable accept mode.
disable
Disable accept mode.
FortiOS 8.0.0 CLI Reference
1791
Fortinet Inc.

<!-- 来源页 1792 -->
Parameter
Description
Type
Size
Default
adv-interval
Advertisement interval (250 - 255000
milliseconds).
integer
Minimum
value: 250
Maximum
value:
255000
1000
ignore-default-route
Enable/disable ignoring of default route when
checking destination.
option
-disable
Option
Description
enable
Ignore default route when checking destination.
disable
Do not ignore default route when checking destination.
preempt
Enable/disable preempt mode.
option
-enable
Option
Description
enable
Enable preempt mode.
disable
Disable preempt mode.
priority
Priority of the virtual router (1 - 255).
integer
Minimum
value: 1
Maximum
value: 255
100
start-time
Startup time (1 - 255 seconds).
integer
Minimum
value: 1
Maximum
value: 255
3
status
Enable/disable VRRP.
option
-enable
Option
Description
enable
Enable VRRP.
disable
Disable VRRP.
vrdst-priority
Priority of the virtual router when the virtual router
destination becomes unreachable (0 - 254).
integer
Minimum
value: 0
Maximum
value: 254
0
vrdst6
Monitor the route to this destination.
ipv6-address
Not
Specified
FortiOS 8.0.0 CLI Reference
1792
Fortinet Inc.

<!-- 来源页 1793 -->
Parameter
Description
Type
Size
Default
vrgrp
VRRP group ID (1 - 65535).
integer
Minimum
value: 1
Maximum
value:
65535
0
vrid
Virtual router identifier (1 - 255).
integer
Minimum
value: 1
Maximum
value: 255
0
vrip6
IPv6 address of the virtual router.
ipv6-address
Not
Specified
::
config l2tp-client-settings
Parameter
Description
Type
Size
Default
auth-type
L2TP authentication type.
option
-auto
Option
Description
auto
Automatically choose authentication.
pap
PAP authentication.
chap
CHAP authentication.
mschapv1
MS-CHAPv1 authentication.
mschapv2
MS-CHAPv2 authentication.
defaultgw
Enable/disable default gateway.
option
-disable
Option
Description
enable
Enable default gateway.
disable
Disable default gateway.
distance
Distance of learned routes.
integer
Minimum
value: 1
Maximum
value: 255
2
hello-interval
L2TP hello message interval in seconds (0
- 3600 sec, default = 60).
integer
Minimum
value: 0
Maximum
value: 3600
60
FortiOS 8.0.0 CLI Reference
1793
Fortinet Inc.

<!-- 来源页 1794 -->
Parameter
Description
Type
Size
Default
ip
IP. Read-only.
ipv4-classnet-host
Not
Specified
0.0.0.0 0.0.0.0
mtu
L2TP MTU.
integer
Minimum
value: 40
Maximum
value:
65535
1460
password
L2TP password.
password
Not
Specified
peer-host
L2TP peer host address.
string
Maximum
length: 255
peer-mask
L2TP peer mask.
ipv4-netmask
Not
Specified
255.255.255.255
peer-port
L2TP peer port number.
integer
Minimum
value: 1
Maximum
value:
65535
1701
priority
Priority of learned routes.
integer
Minimum
value: 1
Maximum
value:
65535
1
user
L2TP user name.
string
Maximum
length: 127
config mirroring-filter
Parameter
Description
Type
Size
Default
filter-dport
Destinatin port of mirroring filter.
integer
Minimum
value: 0
Maximum
value:
65535
0
filter-dstip
Destinatin IP and mask of mirroring filter.
ipv4-classnet-host
Not
Specified
0.0.0.0
0.0.0.0
FortiOS 8.0.0 CLI Reference
1794
Fortinet Inc.

<!-- 来源页 1795 -->
Parameter
Description
Type
Size
Default
filter-protocol
Protocol of mirroring filter.
integer
Minimum
value: 0
Maximum
value: 255
0
filter-sport
Source port of mirroring filter.
integer
Minimum
value: 0
Maximum
value:
65535
0
filter-srcip
Source IP and mask of mirroring filter.
ipv4-classnet-host
Not
Specified
0.0.0.0
0.0.0.0
config phy-setting
Parameter
Description
Type
Size
Default
signal-ok-threshold
Configure the signal strength value at which the
FortiGate unit detects that the receiving signal is
idle or that data is not being received. Zero means
idle detection is disabled. Higher values mean the
signal strength must be higher in order for the
FortiGate unit to consider the interface is not idle
(0 - 12, default = 0).
integer
Minimum
value: 0
Maximum
value: 12
0
config secondaryip
Parameter
Description
Type
Size
Default
allowaccess
Management access settings for the
secondary IP address.
option
-Option
Description
ping
PING access.
https
HTTPS access.
ssh
SSH access.
snmp
SNMP access.
http
HTTP access.
telnet
TELNET access.
fgfm
FortiManager access.
FortiOS 8.0.0 CLI Reference
1795
Fortinet Inc.

<!-- 来源页 1796 -->
Parameter
Description
Type
Size
Default
Option
Description
radius-acct
RADIUS accounting access.
probe-response
Probe access.
fabric
Security Fabric access.
ftm
FTM access.
speed-test
Speed test access.
scim
System for Cross-domain Identity Management (SCIM) access.
detectprotocol
Protocols used to detect the server.
option
-ping
Option
Description
ping
PING.
tcp-echo
TCP echo.
udp-echo
UDP echo.
detectserver
Gateway's ping server for this IP.
user
Not Specified
gwdetect
Enable/disable detect gateway alive for
first.
option
-disable
Option
Description
enable
Enable detect gateway alive for first.
disable
Disable detect gateway alive for first.
ha-priority
HA election priority for the PING server.
integer
Minimum value:
1 Maximum
value: 50
1
id
ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
ip
Secondary IP address of the interface.
ipv4-classnet-host
Not Specified
0.0.0.0
0.0.0.0
ping-serv-status
PING server status. Read-only.
integer
Minimum value:
0 Maximum
value: 255
0
secip-relay-ip
DHCP relay IP address.
user
Not Specified
FortiOS 8.0.0 CLI Reference
1796
Fortinet Inc.

<!-- 来源页 1797 -->
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
config vrrp
Parameter
Description
Type
Size
Default
accept-mode
Enable/disable accept mode.
option
-enable
Option
Description
enable
Enable accept mode.
disable
Disable accept mode.
adv-interval
Advertisement interval (250 - 255000
milliseconds).
integer
Minimum
value: 250
Maximum
value:
255000
1000
ignore-default-route
Enable/disable ignoring of default route when
checking destination.
option
-disable
Option
Description
enable
Ignore default route when checking destination.
disable
Do not ignore default route when checking destination.
preempt
Enable/disable preempt mode.
option
-enable
Option
Description
enable
Enable preempt mode.
disable
Disable preempt mode.
priority
Priority of the virtual router (1 - 255).
integer
Minimum
value: 1
Maximum
value: 255
100
FortiOS 8.0.0 CLI Reference
1797
Fortinet Inc.

<!-- 来源页 1798 -->
Parameter
Description
Type
Size
Default
start-time
Startup time (1 - 255 seconds).
integer
Minimum
value: 1
Maximum
value: 255
3
status
Enable/disable this VRRP configuration.
option
-enable
Option
Description
enable
Enable this VRRP configuration.
disable
Disable this VRRP configuration.
version
VRRP version.
option
-2
Option
Description
2
VRRP version 2.
3
VRRP version 3.
vrdst
Monitor the route to this destination.
ipv4-address-any
Not
Specified
vrdst-priority
Priority of the virtual router when the virtual router
destination becomes unreachable (0 - 254).
integer
Minimum
value: 0
Maximum
value: 254
0
vrgrp
VRRP group ID (1 - 65535).
integer
Minimum
value: 1
Maximum
value:
65535
0
vrid
Virtual router identifier (1 - 255).
integer
Minimum
value: 1
Maximum
value: 255
0
vrip
IP address of the virtual router.
ipv4-address-any
Not
Specified
0.0.0.0
FortiOS 8.0.0 CLI Reference
1798
Fortinet Inc.

<!-- 来源页 1799 -->
config proxy-arp
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
ip
Set IP addresses of proxy ARP.
user
Not Specified
config wifi-mac-list
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
mac
MAC address.
mac-address
Not Specified
00:00:00:00:00:00
config wifi-networks
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
wifi-ca-certificate
CA certificate for WPA2/WPA3-ENTERPRISE.
string
Maximum
length: 79
wifi-client-certificate
Client certificate for WPA2/WPA3-ENTERPRISE.
string
Maximum
length: 35
wifi-eap-type
WPA2/WPA3-ENTERPRISE EAP Method.
option
-peap
Option
Description
both
EAP PEAP and TLS.
tls
EAP TLS.
peap
EAP PEAP.
wifi-encrypt
Data encryption.
option
-AES
FortiOS 8.0.0 CLI Reference
1799
Fortinet Inc.

<!-- 来源页 1800 -->
Parameter
Description
Type
Size
Default
Option
Description
TKIP
TKIP.
AES
AES.
wifi-key
WiFi WEP Key.
password
Not Specified
wifi-keyindex
WEP key index (1 - 4).
integer
Minimum value:
1 Maximum
value: 4
1
wifi-passphrase
WiFi pre-shared key for WPA-PSK or
password for WPA3-SAE and WPA2/WPA3-ENTERPRISE.
password
Not Specified
wifi-private-key
Private key for WPA2/WPA3-ENTERPRISE.
string
Maximum
length: 35
wifi-private-key-password
Password for private key file for WPA2/WPA3-ENTERPRISE.
password
Not Specified
wifi-security
Wireless access security of SSID.
option
-wpa-personal
Option
Description
open
Open.
wep64
WEP64.
wep128
WEP128.
wpa-personal
WPA personal.
wpa-only-personal
WPA personal only.
wpa2-only-personal
WPA2 personal only.
wpa3-sae
WPA3 SAE.
owe
OWE.
wpa-enterprise
WPA2/WPA3 ENTERPRISE.
wifi-ssid
IEEE 802.11 Service Set Identifier.
string
Maximum
length: 32
fortinet
wifi-username
Username for WPA2/WPA3-ENTERPRISE.
string
Maximum
length: 64
fortinet
FortiOS 8.0.0 CLI Reference
1800
Fortinet Inc.

---


<!-- 来源页 1804 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable DHCP server on matched IPAM interface.
disable
Disable DHCP server on matched IPAM interface.
dhcp-template *
DHCP template for assingned interface.
string
Maximum
length: 79
item-name
<name> *
Configure name or wildcard of item to match.
Name or wildcard.
string
Maximum
length: 79
item-type *
Configure whether item is an interface or an
address.
option
-interface
Option
Description
interface
interface
address
address
name
IPAM rule name.
string
Maximum
length: 79
pool <name>
Configure name of IPAM pool to use.
IPAM pool name.
string
Maximum
length: 79
role
Configure role of interface to match.
option
-any
Option
Description
any
Match any interface role.
lan
Match interface role lan.
wan
Match interface role wan.
dmz
Match interface role dmz.
undefined
Match interface role undefined.
vdom <name>
*
Configure which VDOMs have access to this IPAM
rule.
VDOM or wildcard.
string
Maximum
length: 79
* This parameter may not exist in some models.
config system ipip-tunnel
Configure IP in IP Tunneling.
FortiOS 8.0.0 CLI Reference
1804
Fortinet Inc.

---


<!-- 来源页 1809 -->
next
end
config system ipv6-neighbor-cache
Parameter
Description
Type
Size
Default
id
Unique integer ID of the entry.
integer
Minimum
value: 0
Maximum
value:
4294967295
0
interface
Select the associated interface name from
available options.
string
Maximum
length: 15
ipv6
IPv6 address (format:
xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx).
ipv6-address
Not Specified
::
mac
MAC address (format: xx:xx:xx:xx:xx:xx).
mac-address
Not Specified
00:00:00:00:00:00
config system ipv6-tunnel
Configure IPv6/IPv4 in IPv6 tunnel.
config system ipv6-tunnel
Description: Configure IPv6/IPv4 in IPv6 tunnel.
edit <name>
set auto-asic-offload [enable|disable]
set destination {ipv6-address}
set interface {string}
set source {ipv6-address}
set use-sdwan [disable|enable]
next
end
config system ipv6-tunnel
Parameter
Description
Type
Size
Default
auto-asic-offload *
Enable/disable tunnel ASIC offloading.
option
-enable
FortiOS 8.0.0 CLI Reference
1809
Fortinet Inc.

<!-- 来源页 1810 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable auto ASIC offloading.
disable
Disable ASIC offloading.
destination
Remote IPv6 address of the tunnel.
ipv6-address
Not
Specified
::
interface
Interface name.
string
Maximum
length: 15
name
IPv6 tunnel name.
string
Maximum
length: 15
source
Local IPv6 address of the tunnel.
ipv6-address
Not
Specified
::
use-sdwan
Enable/disable use of SD-WAN to reach remote
gateway.
option
-disable
Option
Description
disable
Disable use of SD-WAN to reach remote gateway.
enable
Enable use of SD-WAN to reach remote gateway.
* This parameter may not exist in some models.
FortiOS 8.0.0 CLI Reference
1810
Fortinet Inc.

---


<!-- 来源页 1999 -->
config system physical-switch
This command is available for model(s): FortiGate 1000F, FortiGate 1001F, FortiGate 100F, FortiGate
101F Gen2, FortiGate 1100E, FortiGate 1101E, FortiGate 120G, FortiGate 121G, FortiGate 1800F,
FortiGate 1801F, FortiGate 200F, FortiGate 200G, FortiGate 201F, FortiGate 201G, FortiGate 2600F,
FortiGate 2601F, FortiGate 3000F, FortiGate 3001F, FortiGate 300E, FortiGate 301E, FortiGate 30G,
FortiGate 31G, FortiGate 3200F, FortiGate 3201F Gen2, FortiGate 3500F Gen2, FortiGate 3501F
Gen2, FortiGate 3700F, FortiGate 3701F, FortiGate 400E Bypass, FortiGate 400E, FortiGate 400F,
FortiGate 401E, FortiGate 401F, FortiGate 40F 3G4G, FortiGate 40F, FortiGate 4200F, FortiGate
4201F Gen2, FortiGate 4400F, FortiGate 4401F Gen2, FortiGate 4800F, FortiGate 4801F, FortiGate
50G 5G, FortiGate 50G DSL, FortiGate 50G SFP-POE, FortiGate 50G SFP, FortiGate 50G, FortiGate
51G 5G, FortiGate 51G SFP-POE, FortiGate 51G, FortiGate 600F, FortiGate 601F, FortiGate 60F,
FortiGate 61F, FortiGate 70F, FortiGate 70G-POE, FortiGate 70G, FortiGate 71F, FortiGate 71G-POE,
FortiGate 71G, FortiGate 80F Bypass, FortiGate 80F DSL, FortiGate 80F Gen2, FortiGate 80F-POE,
FortiGate 81F Gen2, FortiGate 81F-POE, FortiGate 900G, FortiGate 901G, FortiGate 90G Gen2,
FortiGate 90G, FortiGate 91G Gen2, FortiGate 91G, FortiGateRugged 50G 5G, FortiGateRugged 60F
3G4G, FortiGateRugged 60F Gen2, FortiGateRugged 70F 3G4G, FortiGateRugged 70F,
FortiGateRugged 70G 5G Dual, FortiGateRugged 70G, FortiWiFi 30G, FortiWiFi 31G, FortiWiFi 40F
3G4G, FortiWiFi 40F, FortiWiFi 50G 5G, FortiWiFi 50G DSL, FortiWiFi 50G SFP, FortiWiFi 50G,
FortiWiFi 51G, FortiWiFi 60F, FortiWiFi 61F, FortiWiFi 70G-POE, FortiWiFi 70G, FortiWiFi 71G, FortiWiFi
80F 2R 3G4G DSL, FortiWiFi 80F 2R, FortiWiFi 81F 2R 3G4G DSL, FortiWiFi 81F 2R 3G4G-POE,
FortiWiFi 81F 2R-POE, FortiWiFi 81F 2R.
It is not available for: FortiGate 1000D, FortiGate 2000E, FortiGate 200E, FortiGate 201E, FortiGate
2200E, FortiGate 2201E, FortiGate 2500E, FortiGate 3300E, FortiGate 3301E, FortiGate 3400E,
FortiGate 3401E, FortiGate 3600E, FortiGate 3601E, FortiGate 3960E, FortiGate 3980E, FortiGate
500E, FortiGate 501E, FortiGate 600E, FortiGate 601E, FortiGate 800D, FortiGate 900D, FortiGate-VM64 Aliyun, FortiGate-VM64 AWS, FortiGate-VM64 Azure, FortiGate-VM64 GCP, FortiGate-VM64
OPC, FortiGate-VM64.
Configure physical switches.
config system physical-switch
Description: Configure physical switches.
edit <name>
set age-enable [enable|disable]
set age-val {integer}
next
end
config system physical-switch
Parameter
Description
Type
Size
Default
age-enable
Enable/disable layer 2 age timer.
option
-disable
FortiOS 8.0.0 CLI Reference
1999
Fortinet Inc.

---


<!-- 来源页 2000 -->
Parameter
Description
Type
Size
Default
Option
Description
enable
Enable layer 2 ageing timer.
disable
Disable layer 2 ageing timer.
age-val
Layer 2 table age timer value.
integer
Minimum value:
0 Maximum
value:
4294967295
3158067
name
Name.
string
Maximum
length: 15
config system pppoe-interface
Configure the PPPoE interfaces.
config system pppoe-interface
Description: Configure the PPPoE interfaces.
edit <name>
set ac-name {string}
set auth-type [auto|pap|...]
set device {string}
set dial-on-demand [enable|disable]
set disc-retry-timeout {integer}
set idle-timeout {integer}
set ipunnumbered {ipv4-address}
set ipv6 [enable|disable]
set lcp-echo-interval {integer}
set lcp-max-echo-fails {integer}
set mrru {integer}
set multilink [enable|disable]
set padt-retry-timeout {integer}
set password {password}
set pppoe-egress-cos [cos0|cos1|...]
set pppoe-unnumbered-negotiate [enable|disable]
set service-name {string}
set username {string}
next
end
FortiOS 8.0.0 CLI Reference
2000
Fortinet Inc.

<!-- 来源页 2001 -->
config system pppoe-interface
Parameter
Description
Type
Size
Default
ac-name
PPPoE AC name.
string
Maximum
length: 63
auth-type
PPP authentication type to use.
option
-auto
Option
Description
auto
Automatically choose the authentication method.
pap
PAP authentication.
chap
CHAP authentication.
mschapv1
MS-CHAPv1 authentication.
mschapv2
MS-CHAPv2 authentication.
device
Name for the physical interface.
string
Maximum
length: 15
dial-on-demand
Enable/disable dial on demand to dial the
PPPoE interface when packets are routed to
the PPPoE interface.
option
-disable
Option
Description
enable
Enable dial on demand.
disable
Disable dial on demand.
disc-retry-timeout
PPPoE discovery init timeout value in (0-4294967295 sec).
integer
Minimum value:
0 Maximum
value:
4294967295
1
idle-timeout
PPPoE auto disconnect after idle timeout (0-4294967295 sec).
integer
Minimum value:
0 Maximum
value:
4294967295
0
ipunnumbered
PPPoE unnumbered IP.
ipv4-address
Not Specified
0.0.0.0
ipv6
Enable/disable IPv6 Control Protocol
(IPv6CP).
option
-disable
Option
Description
enable
Enable IPv6CP.
disable
Disable IPv6CP.
FortiOS 8.0.0 CLI Reference
2001
Fortinet Inc.

<!-- 来源页 2002 -->
Parameter
Description
Type
Size
Default
lcp-echo-interval
Time in seconds between PPPoE Link
Control Protocol (LCP) echo requests.
integer
Minimum value:
0 Maximum
value: 32767
5
lcp-max-echo-fails
Maximum missed LCP echo messages
before disconnect.
integer
Minimum value:
0 Maximum
value: 32767
3
mrru
PPP MRRU (296 - 65535, default = 1500).
integer
Minimum value:
296 Maximum
value: 65535
1500
multilink
Enable/disable PPP multilink support.
option
-disable
Option
Description
enable
Enable PPP multilink support.
disable
Disable PPP multilink support.
name
Name of the PPPoE interface.
string
Maximum
length: 15
padt-retry-timeout
PPPoE terminate timeout value in (0-4294967295 sec).
integer
Minimum value:
0 Maximum
value:
4294967295
1
password
Enter the password.
password
Not Specified
pppoe-egress-cos
CoS in VLAN tag for outgoing PPPoE/PPP
packets.
option
-cos0
Option
Description
cos0
CoS 0.
cos1
CoS 1.
cos2
CoS 2.
cos3
CoS 3.
cos4
CoS 4.
cos5
CoS 5.
cos6
CoS 6.
cos7
CoS 7.
pppoe-unnumbered-negotiate
Enable/disable PPPoE unnumbered
negotiation.
option
-enable
FortiOS 8.0.0 CLI Reference
2002
Fortinet Inc.

---


<!-- 来源页 2123 -->
config collectors
Parameter
Description
Type
Size
Default
collector-ip
IP addresses of the sFlow collectors that sFlow
agents added to interfaces in this VDOM send
sFlow datagrams to.
ipv4-address
Not Specified
0.0.0.0
collector-port
UDP port number used for sending sFlow
datagrams (configure only if required by your
sFlow collector or your network configuration)
(0 - 65535, default = 6343).
integer
Minimum value:
0 Maximum
value: 65535
6343
id
ID.
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
source-ip
Source IP address for sFlow agent.
ipv4-address
Not Specified
0.0.0.0
config system sit-tunnel
Configure IPv6 tunnel over IPv4.
config system sit-tunnel
Description: Configure IPv6 tunnel over IPv4.
edit <name>
set auto-asic-offload [enable|disable]
set destination {ipv4-address}
set interface {string}
set ip6 {ipv6-prefix}
set source {ipv4-address}
set use-sdwan [disable|enable]
next
end
FortiOS 8.0.0 CLI Reference
2123
Fortinet Inc.

<!-- 来源页 2124 -->
config system sit-tunnel
Parameter
Description
Type
Size
Default
auto-asic-offload *
Enable/disable tunnel ASIC offloading.
option
-enable
Option
Description
enable
Enable auto ASIC offloading.
disable
Disable ASIC offloading.
destination
Destination IP address of the tunnel.
ipv4-address
Not
Specified
0.0.0.0
interface
Interface name.
string
Maximum
length: 15
ip6
IPv6 address of the tunnel.
ipv6-prefix
Not
Specified
::/0
name
Tunnel name.
string
Maximum
length: 15
source
Source IP address of the tunnel.
ipv4-address
Not
Specified
0.0.0.0
use-sdwan
Enable/disable use of SD-WAN to reach remote
gateway.
option
-disable
Option
Description
disable
Disable use of SD-WAN to reach remote gateway.
enable
Enable use of SD-WAN to reach remote gateway.
* This parameter may not exist in some models.
FortiOS 8.0.0 CLI Reference
2124
Fortinet Inc.

---


<!-- 来源页 2173 -->
Parameter
Description
Type
Size
Default
Option
Description
24576
24576
28672
28672
32768
32768
36864
36864
40960
40960
45056
45056
49152
49152
53248
53248
57344
57344
config system switch-interface
Configure software switch interfaces by grouping interfaces.
config system switch-interface
Description: Configure software switch interfaces by grouping interfaces.
edit <name>
set intra-switch-policy [implicit|explicit]
set mac-ttl {integer}
set member <interface-name1>, <interface-name2>, ...
set span [disable|enable]
set span-dest-port {string}
set span-direction [rx|tx|...]
set span-source-port <interface-name1>, <interface-name2>, ...
set type [switch|hub]
set vdom {string}
next
end
config system switch-interface
Parameter
Description
Type
Size
Default
intra-switch-policy
Allow any traffic between switch interfaces or
require firewall policies to allow traffic between
switch interfaces.
option
-implicit
FortiOS 8.0.0 CLI Reference
2173
Fortinet Inc.

<!-- 来源页 2174 -->
Parameter
Description
Type
Size
Default
Option
Description
implicit
Traffic between switch members is implicitly allowed.
explicit
Traffic between switch members must match firewall policies.
mac-ttl
Duration for which MAC addresses are held in the
ARP table (300 - 8640000 sec, default = 300).
integer
Minimum
value: 300
Maximum
value:
8640000
300
member
<interface-name>
Names of the interfaces that belong to the
software switch.
Interface name.
string
Maximum
length: 79
name
Interface name (name cannot be in use by any
other interfaces, VLANs, or inter-VDOM links).
string
Maximum
length: 15
span
Enable/disable port spanning. Port spanning
echoes traffic received by the software switch to
the span destination port.
option
-disable
Option
Description
disable
Disable port spanning.
enable
Enable port spanning.
span-dest-port
SPAN destination port name. All traffic on the
SPAN source ports is echoed to the SPAN
destination port.
string
Maximum
length: 15
span-direction
The direction in which the SPAN port operates,
either: rx, tx, or both.
option
-both
Option
Description
rx
Copies only received packets from source SPAN ports to the
destination SPAN port.
tx
Copies only transmitted packets from source SPAN ports to the
destination SPAN port.
both
Copies both received and transmitted packets from source SPAN ports
to the destination SPAN port.
span-source-port
<interface-name>
Physical interface name. Port spanning echoes all
traffic on the SPAN source ports to the SPAN
destination port.
Physical interface name.
string
Maximum
length: 79
FortiOS 8.0.0 CLI Reference
2174
Fortinet Inc.

---


<!-- 来源页 2179 -->
config system tos-based-priority
Configure Type of Service (ToS) based priority table to set network traffic priorities.
config system tos-based-priority
Description: Configure Type of Service (ToS) based priority table to set network traffic
priorities.
edit <id>
set priority [low|medium|...]
set tos {integer}
next
end
config system tos-based-priority
Parameter
Description
Type
Size
Default
id
Item ID.
integer
Minimum value:
0 Maximum
value:
4294967295
0
priority
ToS based priority level to low, medium or high
(these priorities match firewall traffic shaping
priorities) (default = medium).
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
tos
Value of the ToS byte in the IP datagram header
(0-15, 8: minimize delay, 4: maximize
throughput, 2: maximize reliability, 1: minimize
monetary cost, and 0: default service).
integer
Minimum value:
0 Maximum
value: 15
0
config system vdom
Configure virtual domain.
config system vdom
Description: Configure virtual domain.
edit <name>
set flag {integer}
set short-name {string}
FortiOS 8.0.0 CLI Reference
2179
Fortinet Inc.

---


<!-- 来源页 2180 -->
set vcluster-id {integer}
next
end
config system vdom
Parameter
Description
Type
Size
Default
flag
Flag.
integer
Minimum value:
0 Maximum
value:
4294967295
0
name
VDOM name.
string
Maximum
length: 31
short-name
VDOM short name.
string
Maximum
length: 11
vcluster-id
Virtual cluster ID (0 - 4294967295).
integer
Minimum value:
0 Maximum
value:
4294967295
0
config system vdom-dns
Configure DNS servers for a non-management VDOM.
config system vdom-dns
Description: Configure DNS servers for a non-management VDOM.
set alt-primary {ipv4-address}
set alt-secondary {ipv4-address}
set interface {string}
set interface-select-method [auto|sdwan|...]
set ip6-primary {ipv6-address}
set ip6-secondary {ipv6-address}
set primary {ipv4-address}
set protocol {option1}, {option2}, ...
set secondary {ipv4-address}
set server-hostname <hostname1>, <hostname2>, ...
set server-select-method [least-rtt|failover]
set source-ip {ipv4-address}
set source-ip-interface {string}
set ssl-certificate {string}
set vdom-dns [enable|disable]
set vrf-select {integer}
end
FortiOS 8.0.0 CLI Reference
2180
Fortinet Inc.

<!-- 来源页 2181 -->
config system vdom-dns
Parameter
Description
Type
Size
Default
alt-primary
Alternate primary DNS server. This is not used as a
failover DNS server.
ipv4-address
Not
Specified
0.0.0.0
alt-secondary
Alternate secondary DNS server. This is not used
as a failover DNS server.
ipv4-address
Not
Specified
0.0.0.0
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
ip6-primary
Primary IPv6 DNS server IP address for the VDOM.
ipv6-address
Not
Specified
::
ip6-secondary
Secondary IPv6 DNS server IP address for the
VDOM.
ipv6-address
Not
Specified
::
primary
Primary DNS server IP address for the VDOM.
ipv4-address
Not
Specified
0.0.0.0
protocol
DNS transport protocols.
option
-cleartext
Option
Description
cleartext
DNS over UDP/53, DNS over TCP/53.
dot
DNS over TLS/853.
doh
DNS over HTTPS/443.
secondary
Secondary DNS server IP address for the VDOM.
ipv4-address
Not
Specified
0.0.0.0
server-hostname
<hostname>
DNS server host name list.
DNS server host name list separated by space
(maximum 4 domains).
string
Maximum
length: 127
server-select-method
Specify how configured servers are prioritized.
option
-least-rtt
FortiOS 8.0.0 CLI Reference
2181
Fortinet Inc.

---


<!-- 来源页 2182 -->
Parameter
Description
Type
Size
Default
Option
Description
least-rtt
Select servers based on least round trip time.
failover
Select servers based on the order they are configured.
source-ip
Source IP for communications with the DNS server.
ipv4-address
Not
Specified
0.0.0.0
source-ip-interface
IP address of the specified interface as the source
IP address.
string
Maximum
length: 15
ssl-certificate
Name of local certificate for SSL connections.
string
Maximum
length: 35
vdom-dns
Enable/disable configuring DNS servers for the
current VDOM.
option
-disable
Option
Description
enable
Enable configuring DNS servers for the current VDOM.
disable
Disable configuring DNS servers for the current VDOM.
vrf-select
VRF ID used for connection to server.
integer
Minimum
value: 0
Maximum
value: 511
0
config system vdom-exception
Global configuration objects that can be configured independently across different ha peers for all VDOMs or for
the defined VDOM scope.
config system vdom-exception
Description: Global configuration objects that can be configured independently across
different ha peers for all VDOMs or for the defined VDOM scope.
edit <id>
set object [log.fortianalyzer.setting|log.fortianalyzer.override-setting|...]
set scope [all|inclusive|...]
set vdom <name1>, <name2>, ...
next
end
FortiOS 8.0.0 CLI Reference
2182
Fortinet Inc.

<!-- 来源页 2183 -->
config system vdom-exception
Parameter
Description
Type
Size
Default
id
Index (1 - 4096).
integer
Minimum value:
1 Maximum
value: 4096
0
object
Name of the configuration object
that can be configured
independently for all VDOMs.
option
-Option
Description
log.fortianalyzer.setting
log.fortianalyzer.setting
log.fortianalyzer.override-setting
log.fortianalyzer.override-setting
log.fortianalyzer2.setting
log.fortianalyzer2.setting
log.fortianalyzer2.override-setting
log.fortianalyzer2.override-setting
log.fortianalyzer3.setting
log.fortianalyzer3.setting
log.fortianalyzer3.override-setting
log.fortianalyzer3.override-setting
log.fortianalyzer-cloud.setting
log.fortianalyzer-cloud.setting
log.fortianalyzer-cloud.override-setting
log.fortianalyzer-cloud.override-setting
log.syslogd.setting
log.syslogd.setting
log.syslogd.override-setting
log.syslogd.override-setting
log.syslogd2.setting
log.syslogd2.setting
log.syslogd2.override-setting
log.syslogd2.override-setting
log.syslogd3.setting
log.syslogd3.setting
log.syslogd3.override-setting
log.syslogd3.override-setting
log.syslogd4.setting
log.syslogd4.setting
log.syslogd4.override-setting
log.syslogd4.override-setting
system.gre-tunnel
system.gre-tunnel
system.central-management
system.central-management
system.csf
system.csf
FortiOS 8.0.0 CLI Reference
2183
Fortinet Inc.

<!-- 来源页 2184 -->
Parameter
Description
Type
Size
Default
Option
Description
user.radius
user.radius
system.interface
system.interface
firewall.address
firewall.address
system.snmp.sysinfo
system.snmp.sysinfo
system.standalone-cluster
system.standalone-cluster
vpn.ipsec.phase1-interface
vpn.ipsec.phase1-interface
vpn.ipsec.phase2-interface
vpn.ipsec.phase2-interface
router.bgp
router.bgp
router.route-map
router.route-map
router.prefix-list
router.prefix-list
firewall.ippool
firewall.ippool
firewall.ippool6
firewall.ippool6
router.static
router.static
router.static6
router.static6
firewall.vip
firewall.vip
firewall.vip6
firewall.vip6
system.sdwan
system.sdwan
system.saml
system.saml
router.policy
router.policy
router.policy6
router.policy6
system.vin-alarm
system.vin-alarm
scope
Determine whether the
configuration object can be
configured separately for all
VDOMs or if some VDOMs share
the same configuration.
option
-all
Option
Description
all
Object configuration independent for all VDOMs.
inclusive
Object configuration independent for the listed VDOMs. Other VDOMs
use the global configuration.
FortiOS 8.0.0 CLI Reference
2184
Fortinet Inc.

---


<!-- 来源页 2185 -->
Parameter
Description
Type
Size
Default
Option
Description
exclusive
Use the global object configuration for the listed VDOMs. Other VDOMs
can be configured independently.
vdom <name>
Names of the VDOMs.
VDOM name.
string
Maximum
length: 79
config system vdom-link
Configure VDOM links.
config system vdom-link
Description: Configure VDOM links.
edit <name>
set type [ppp|ethernet|...]
set vcluster [vcluster1|vcluster2]
next
end
config system vdom-link
Parameter
Description
Type
Size
Default
name
VDOM link name (maximum = 11 characters).
string
Maximum
length: 11
type
VDOM link type: PPP or Ethernet.
option
-ppp
Option
Description
ppp
PPP VDOM link.
ethernet
Ethernet VDOM link.
npupair
NPU VDOM link.
vcluster
Virtual cluster.
option
-vcluster1
Option
Description
vcluster1
Virtual cluster 1.
vcluster2
Virtual cluster 2.
FortiOS 8.0.0 CLI Reference
2185
Fortinet Inc.

---


<!-- 来源页 2186 -->
config system vdom-netflow
Configure NetFlow per VDOM.
config system vdom-netflow
Description: Configure NetFlow per VDOM.
config collectors
Description: Netflow collectors.
edit <id>
set collector-ip {string}
set collector-port {integer}
set interface {string}
set interface-select-method [auto|sdwan|...]
set source-ip {string}
set source-ip-interface {string}
set vrf-select {integer}
next
end
set vdom-netflow [enable|disable]
end
config system vdom-netflow
Parameter
Description
Type
Size
Default
vdom-netflow
Enable/disable NetFlow per VDOM.
option
-disable
Option
Description
enable
Enable NetFlow per VDOM.
disable
Disable NetFlow per VDOM.
config collectors
Parameter
Description
Type
Size
Default
collector-ip
Collector IP.
string
Maximum
length: 63
collector-port
NetFlow collector port number.
integer
Minimum
value: 0
Maximum
value:
65535
2055
FortiOS 8.0.0 CLI Reference
2186
Fortinet Inc.

---


<!-- 来源页 2187 -->
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
value: 6
0
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
source-ip
Source IP address for communication with the
NetFlow agent.
string
Maximum
length: 63
source-ip-interface
Name of the interface used to determine the source
IP for exporting packets.
string
Maximum
length: 15
vrf-select
VRF ID used for connection to server.
integer
Minimum
value: 0
Maximum
value: 511
0
config system vdom-property
Configure VDOM property.
config system vdom-property
Description: Configure VDOM property.
edit <name>
set custom-service {user}
set description {string}
set dialup-tunnel {user}
set firewall-address {user}
set firewall-addrgrp {user}
set firewall-policy {user}
set ipsec-phase1 {user}
set ipsec-phase1-interface {user}
set ipsec-phase2 {user}
set ipsec-phase2-interface {user}
set log-disk-quota {user}
set onetime-schedule {user}
FortiOS 8.0.0 CLI Reference
2187
Fortinet Inc.

<!-- 来源页 2188 -->
set proxy {user}
set recurring-schedule {user}
set service-group {user}
set session {user}
set snmp-index {integer}
set sslvpn {user}
set user {user}
set user-group {user}
next
end
config system vdom-property
Parameter
Description
Type
Size
Default
custom-service
Maximum guaranteed number of firewall custom
services.
user
Not Specified
description
Description.
string
Maximum
length: 127
dialup-tunnel
Maximum guaranteed number of dial-up tunnels.
user
Not Specified
firewall-address
Maximum guaranteed number of firewall
addresses (IPv4, IPv6, multicast).
user
Not Specified
firewall-addrgrp
Maximum guaranteed number of firewall address
groups (IPv4, IPv6).
user
Not Specified
firewall-policy
Maximum guaranteed number of firewall policies
(policy, DoS-policy4, DoS-policy6, multicast).
user
Not Specified
ipsec-phase1
Maximum guaranteed number of VPN IPsec
phase 1 tunnels.
user
Not Specified
ipsec-phase1-interface
Maximum guaranteed number of VPN IPsec
phase1 interface tunnels.
user
Not Specified
ipsec-phase2
Maximum guaranteed number of VPN IPsec
phase 2 tunnels.
user
Not Specified
ipsec-phase2-interface
Maximum guaranteed number of VPN IPsec
phase2 interface tunnels.
user
Not Specified
log-disk-quota
Log disk quota in megabytes (MB). Range
depends on how much disk space is available.
user
Not Specified
name
VDOM name.
string
Maximum
length: 31
FortiOS 8.0.0 CLI Reference
2188
Fortinet Inc.

---


<!-- 来源页 2189 -->
Parameter
Description
Type
Size
Default
onetime-schedule
Maximum guaranteed number of firewall one-time schedules.
user
Not Specified
proxy *
Maximum guaranteed number of concurrent
proxy users.
user
Not Specified
recurring-schedule
Maximum guaranteed number of firewall
recurring schedules.
user
Not Specified
service-group
Maximum guaranteed number of firewall service
groups.
user
Not Specified
session
Maximum guaranteed number of sessions.
user
Not Specified
snmp-index
Permanent SNMP Index of the virtual domain (1 -2147483647).
integer
Minimum
value: 1
Maximum
value:
2147483647
0
sslvpn *
Maximum guaranteed number of Agentless
VPNs.
user
Not Specified
user
Maximum guaranteed number of local users.
user
Not Specified
user-group
Maximum guaranteed number of user groups.
user
Not Specified
* This parameter may not exist in some models.
config system vdom-radius-server
Configure a RADIUS server to use as a RADIUS Single Sign On (RSSO) server for this VDOM.
config system vdom-radius-server
Description: Configure a RADIUS server to use as a RADIUS Single Sign On (RSSO) server for
this VDOM.
edit <name>
set radius-server-vdom {string}
set status [enable|disable]
next
end
config system vdom-radius-server
Parameter
Description
Type
Size
Default
name
Name of the VDOM that you are adding the RADIUS
server to.
string
Maximum
length: 31
FortiOS 8.0.0 CLI Reference
2189
Fortinet Inc.

---


<!-- 来源页 2190 -->
Parameter
Description
Type
Size
Default
radius-server-vdom
Use this option to select another VDOM containing
a VDOM RSSO RADIUS server to use for the current
VDOM.
string
Maximum
length: 31
status
Enable/disable the RSSO RADIUS server for this
VDOM.
option
-disable
Option
Description
enable
Enable the RSSO RADIUS server for this VDOM.
disable
Disable the RSSO RADIUS server for this VDOM.
config system vdom-sflow
Configure sFlow per VDOM to add or change the IP address and UDP port that FortiGate sFlow agents in this
VDOM use to send sFlow datagrams to an sFlow collector.
config system vdom-sflow
Description: Configure sFlow per VDOM to add or change the IP address and UDP port that
FortiGate sFlow agents in this VDOM use to send sFlow datagrams to an sFlow collector.
config collectors
Description: sFlow collectors.
edit <id>
set collector-ip {ipv4-address}
set collector-port {integer}
set interface {string}
set interface-select-method [auto|sdwan|...]
set source-ip {ipv4-address}
next
end
set vdom-sflow [enable|disable]
end
config system vdom-sflow
Parameter
Description
Type
Size
Default
vdom-sflow
Enable/disable the sFlow configuration for the
current VDOM.
option
-disable
Option
Description
enable
Enable sFlow for this VDOM.
disable
Disable sFlow for this VDOM.
FortiOS 8.0.0 CLI Reference
2190
Fortinet Inc.

<!-- 来源页 2191 -->
config collectors
Parameter
Description
Type
Size
Default
collector-ip
IP addresses of the sFlow collectors that sFlow
agents added to interfaces in this VDOM send
sFlow datagrams to.
ipv4-address
Not Specified
0.0.0.0
collector-port
UDP port number used for sending sFlow
datagrams (configure only if required by your
sFlow collector or your network configuration)
(0 - 65535, default = 6343).
integer
Minimum value:
0 Maximum
value: 65535
6343
id
ID.
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
source-ip
Source IP address for sFlow agent.
ipv4-address
Not Specified
0.0.0.0
FortiOS 8.0.0 CLI Reference
2191
Fortinet Inc.

---


<!-- 来源页 2194 -->
config system virtual-switch
This command is available for model(s): FortiGate 1000F, FortiGate 1001F, FortiGate 100F, FortiGate
101F Gen2, FortiGate 1100E, FortiGate 1101E, FortiGate 120G, FortiGate 121G, FortiGate 1800F,
FortiGate 1801F, FortiGate 200F, FortiGate 200G, FortiGate 201F, FortiGate 201G, FortiGate 2600F,
FortiGate 2601F, FortiGate 3000F, FortiGate 3001F, FortiGate 300E, FortiGate 301E, FortiGate 30G,
FortiGate 31G, FortiGate 3200F, FortiGate 3201F Gen2, FortiGate 3500F Gen2, FortiGate 3501F
Gen2, FortiGate 3700F, FortiGate 3701F, FortiGate 400E Bypass, FortiGate 400E, FortiGate 400F,
FortiGate 401E, FortiGate 401F, FortiGate 40F 3G4G, FortiGate 40F, FortiGate 4200F, FortiGate
4201F Gen2, FortiGate 4400F, FortiGate 4401F Gen2, FortiGate 4800F, FortiGate 4801F, FortiGate
50G 5G, FortiGate 50G DSL, FortiGate 50G SFP-POE, FortiGate 50G SFP, FortiGate 50G, FortiGate
51G 5G, FortiGate 51G SFP-POE, FortiGate 51G, FortiGate 600F, FortiGate 601F, FortiGate 60F,
FortiGate 61F, FortiGate 70F, FortiGate 70G-POE, FortiGate 70G, FortiGate 71F, FortiGate 71G-POE,
FortiGate 71G, FortiGate 80F Bypass, FortiGate 80F DSL, FortiGate 80F Gen2, FortiGate 80F-POE,
FortiGate 81F Gen2, FortiGate 81F-POE, FortiGate 900G, FortiGate 901G, FortiGate 90G Gen2,
FortiGate 90G, FortiGate 91G Gen2, FortiGate 91G, FortiGateRugged 50G 5G, FortiGateRugged 60F
3G4G, FortiGateRugged 60F Gen2, FortiGateRugged 70F 3G4G, FortiGateRugged 70F,
FortiGateRugged 70G 5G Dual, FortiGateRugged 70G, FortiWiFi 30G, FortiWiFi 31G, FortiWiFi 40F
3G4G, FortiWiFi 40F, FortiWiFi 50G 5G, FortiWiFi 50G DSL, FortiWiFi 50G SFP, FortiWiFi 50G,
FortiWiFi 51G, FortiWiFi 60F, FortiWiFi 61F, FortiWiFi 70G-POE, FortiWiFi 70G, FortiWiFi 71G, FortiWiFi
80F 2R 3G4G DSL, FortiWiFi 80F 2R, FortiWiFi 81F 2R 3G4G DSL, FortiWiFi 81F 2R 3G4G-POE,
FortiWiFi 81F 2R-POE, FortiWiFi 81F 2R.
It is not available for: FortiGate 1000D, FortiGate 2000E, FortiGate 200E, FortiGate 201E, FortiGate
2200E, FortiGate 2201E, FortiGate 2500E, FortiGate 3300E, FortiGate 3301E, FortiGate 3400E,
FortiGate 3401E, FortiGate 3600E, FortiGate 3601E, FortiGate 3960E, FortiGate 3980E, FortiGate
500E, FortiGate 501E, FortiGate 600E, FortiGate 601E, FortiGate 800D, FortiGate 900D, FortiGate-VM64 Aliyun, FortiGate-VM64 AWS, FortiGate-VM64 Azure, FortiGate-VM64 GCP, FortiGate-VM64
OPC, FortiGate-VM64.
Configure virtual hardware switch interfaces.
config system virtual-switch
Description: Configure virtual hardware switch interfaces.
edit <name>
set physical-switch {string}
config port
Description: Configure member ports.
edit <name>
set alias {string}
next
end
set span [disable|enable]
set span-dest-port {string}
set span-direction [rx|tx|...]
set span-source-port {string}
set vlan {integer}
next
end
FortiOS 8.0.0 CLI Reference
2194
Fortinet Inc.

<!-- 来源页 2195 -->
config system virtual-switch
Parameter
Description
Type
Size
Default
name
Name of the virtual switch.
string
Maximum
length: 15
physical-switch
Physical switch parent.
string
Maximum
length: 15
span *
Enable/disable SPAN.
option
-disable
Option
Description
disable
Disable SPAN.
enable
Enable SPAN.
span-dest-port *
SPAN destination port.
string
Maximum
length: 15
span-direction *
SPAN direction.
option
-both
Option
Description
rx
SPAN receive direction only.
tx
SPAN transmit direction only.
both
SPAN both directions.
span-source-port *
SPAN source port.
string
Maximum
length: 15
vlan *
VLAN.
integer
Minimum value:
0 Maximum
value:
4294967295
0
* This parameter may not exist in some models.
config port
Parameter
Description
Type
Size
Default
alias
Alias.
string
Maximum
length: 25
name
Physical interface name.
string
Maximum
length: 15
FortiOS 8.0.0 CLI Reference
2195
Fortinet Inc.

---


<!-- 来源页 2196 -->
config system virtual-wire-pair
Configure virtual wire pairs.
config system virtual-wire-pair
Description: Configure virtual wire pairs.
edit <name>
set member <interface-name1>, <interface-name2>, ...
set outer-vlan-id <vlanid1>, <vlanid2>, ...
set poweroff-bypass [enable|disable]
set poweron-bypass [enable|disable]
set vlan-filter {user}
set wildcard-vlan [enable|disable]
next
end
config system virtual-wire-pair
Parameter
Description
Type
Size
Default
member
<interface-name>
Interfaces belong to the virtual-wire-pair.
Interface name.
string
Maximum
length: 79
name
Virtual-wire-pair name. Must be a unique interface
name.
string
Maximum
length: 11
outer-vlan-id
<vlanid> *
Outer VLAN ID.
VLAN ID (1 - 4094).
integer
Minimum
value: 1
Maximum
value: 4094
poweroff-bypass *
Enable/disable interface bypass state when power
off.
option
-disable
Option
Description
enable
Enable bypass when power off.
disable
Disable bypass when power off.
poweron-bypass *
Enable/disable interface bypass state when power
on.
option
-disable
Option
Description
enable
Enable bypass when power on.
disable
Disable bypass when power on.
FortiOS 8.0.0 CLI Reference
2196
Fortinet Inc.

---


<!-- 来源页 2200 -->
Parameter
Description
Type
Size
Default
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
config system vxlan
Configure VXLAN devices.
config system vxlan
Description: Configure VXLAN devices.
edit <name>
set dstport {integer}
set evpn-id {integer}
set interface {string}
set ip-version [ipv4-unicast|ipv6-unicast|...]
set learn-from-traffic [enable|disable]
set local-ip {ipv4-address}
set local-ip6 {ipv6-address}
set multicast-ttl {integer}
set remote-ip <ip1>, <ip2>, ...
set remote-ip6 <ip61>, <ip62>, ...
set vni {integer}
next
end
config system vxlan
Parameter
Description
Type
Size
Default
dstport
VXLAN destination port (1 - 65535, default =
4789).
integer
Minimum
value: 1
Maximum
value:
65535
4789
FortiOS 8.0.0 CLI Reference
2200
Fortinet Inc.

<!-- 来源页 2201 -->
Parameter
Description
Type
Size
Default
evpn-id
EVPN instance.
integer
Minimum
value: 1
Maximum
value:
65535
0
interface
Outgoing interface for VXLAN encapsulated traffic.
string
Maximum
length: 15
ip-version
IP version to use for the VXLAN interface and so for
communication over the VXLAN. IPv4 or IPv6
unicast or multicast.
option
-ipv4-unicast
Option
Description
ipv4-unicast
Use IPv4 unicast addressing over the VXLAN.
ipv6-unicast
Use IPv6 unicast addressing over the VXLAN.
ipv4-multicast
Use IPv4 multicast addressing over the VXLAN.
ipv6-multicast
Use IPv6 multicast addressing over the VXLAN.
learn-from-traffic
Enable/disable VXLAN MAC learning from traffic.
option
-disable
Option
Description
enable
Enable VXLAN MAC learning from traffic.
disable
Disable VXLAN MAC learning from traffic.
local-ip
IPv4 address to use as the source address for
egress VXLAN packets.
ipv4-address
Not
Specified
0.0.0.0
local-ip6
IPv6 address to use as the source address for
egress VXLAN packets.
ipv6-address
Not
Specified
::
multicast-ttl
VXLAN multicast TTL (1-255, default = 0).
integer
Minimum
value: 1
Maximum
value: 255
0
name
VXLAN device or interface name. Must be a unique
interface name.
string
Maximum
length: 15
remote-ip
<ip>
IPv4 address of the VXLAN interface on the device
at the remote end of the VXLAN.
IPv4 address.
string
Maximum
length: 15
remote-ip6
<ip6>
IPv6 IP address of the VXLAN interface on the
device at the remote end of the VXLAN.
IPv6 address.
string
Maximum
length: 45
FortiOS 8.0.0 CLI Reference
2201
Fortinet Inc.

---


<!-- 来源页 2202 -->
Parameter
Description
Type
Size
Default
vni
VXLAN network ID.
integer
Minimum
value: 1
Maximum
value:
16777215
0
config system wccp
Configure WCCP.
config system wccp
Description: Configure WCCP.
edit <service-id>
set assignment-bucket-format [wccp-v2|cisco-implementation]
set assignment-dstaddr-mask {ipv4-netmask-any}
set assignment-method [HASH|MASK|...]
set assignment-srcaddr-mask {ipv4-netmask-any}
set assignment-weight {integer}
set authentication [enable|disable]
set cache-engine-method [GRE|L2]
set cache-id {ipv4-address}
set forward-method [GRE|L2|...]
set group-address {ipv4-address-multicast}
set password {password}
set ports {user}
set ports-defined [source|destination]
set primary-hash {option1}, {option2}, ...
set priority {integer}
set protocol {integer}
set return-method [GRE|L2|...]
set router-id {ipv4-address}
set router-list {user}
set server-list {user}
set server-type [forward|proxy]
set service-type [auto|standard|...]
next
end
config system wccp
Parameter
Description
Type
Size
Default
assignment-bucket-format
Assignment bucket format for the WCCP
cache engine.
option
-cisco-implementation
FortiOS 8.0.0 CLI Reference
2202
Fortinet Inc.

<!-- 来源页 2203 -->
Parameter
Description
Type
Size
Default
Option
Description
wccp-v2
WCCP-v2 bucket format.
cisco-implementation
Cisco bucket format.
assignment-dstaddr-mask
Assignment destination address mask.
ipv4-netmask-any
Not
Specified
0.0.0.0
assignment-method
Hash key assignment preference.
option
-HASH
Option
Description
HASH
HASH assignment method.
MASK
MASK assignment method.
any
HASH or MASK.
assignment-srcaddr-mask
Assignment source address mask.
ipv4-netmask-any
Not
Specified
0.0.23.65
assignment-weight
Assignment of hash weight/ratio for the
WCCP cache engine.
integer
Minimum
value: 0
Maximum
value: 255
0
authentication
Enable/disable MD5 authentication.
option
-disable
Option
Description
enable
Enable MD5 authentication.
disable
Disable MD5 authentication.
cache-engine-method
Method used to forward traffic to the
routers or to return to the cache engine.
option
-GRE
Option
Description
GRE
GRE encapsulation.
L2
L2 rewrite.
cache-id
IP address known to all routers. If the
addresses are the same, use the default
0.0.0.0.
ipv4-address
Not
Specified
0.0.0.0
forward-method
Method used to forward traffic to the
cache servers.
option
-GRE
FortiOS 8.0.0 CLI Reference
2203
Fortinet Inc.

<!-- 来源页 2204 -->
Parameter
Description
Type
Size
Default
Option
Description
GRE
GRE encapsulation.
L2
L2 rewrite.
any
GRE or L2.
group-address
IP multicast address used by the cache
routers. For the FortiGate to ignore
multicast WCCP traffic, use the default
0.0.0.0.
ipv4-address-multicast
Not
Specified
0.0.0.0
password
Password for MD5 authentication.
password
Not
Specified
ports
Service ports.
user
Not
Specified
ports-defined
Match method.
option
-Option
Description
source
Source port match.
destination
Destination port match.
primary-hash
Hash method.
option
-dst-ip
Option
Description
src-ip
Source IP hash.
dst-ip
Destination IP hash.
src-port
Source port hash.
dst-port
Destination port hash.
priority
Service priority.
integer
Minimum
value: 0
Maximum
value: 255
0
protocol
Service protocol.
integer
Minimum
value: 0
Maximum
value: 255
0
return-method
Method used to decline a redirected
packet and return it to the FortiGate unit.
option
-GRE
FortiOS 8.0.0 CLI Reference
2204
Fortinet Inc.

<!-- 来源页 2205 -->
Parameter
Description
Type
Size
Default
Option
Description
GRE
GRE encapsulation.
L2
L2 rewrite.
any
GRE or L2.
router-id
IP address known to all cache engines. If
all cache engines connect to the same
FortiGate interface, use the default
0.0.0.0.
ipv4-address
Not
Specified
0.0.0.0
router-list
IP addresses of one or more WCCP
routers.
user
Not
Specified
server-list
IP addresses and netmasks for up to four
cache servers.
user
Not
Specified
server-type
Cache server type.
option
-forward
Option
Description
forward
Forward server.
proxy
Proxy server.
service-id
Service ID.
string
Maximum
length: 3
service-type
WCCP service type used by the cache
server for logical interception and
redirection of traffic.
option
-auto
Option
Description
auto
auto
standard
Standard service.
dynamic
Dynamic service.
FortiOS 8.0.0 CLI Reference
2205
Fortinet Inc.

---


<!-- 来源页 2210 -->
Parameter
Description
Type
Size
Default
power-level
Power level (0 - 17).
integer
Minimum value:
0 Maximum
value: 17
17
rogue-scan *
Enable/disable rogue scan.
option
-disable
Option
Description
enable
Enable rogue scan.
disable
Disable rogue scan.
rogue-scan-mac-adjacency *
MAC adjacency (0-31).
integer
Minimum value:
0 Maximum
value: 31
7
short-guard-interval
Enable/disable short guard interval.
option
-disable
Option
Description
enable
400 ns long guard interval.
disable
800 ns short guard interval.
* This parameter may not exist in some models.
config system zone
Configure zones to group two or more interfaces. When a zone is created you can configure policies for the
zone instead of individual interfaces in the zone.
config system zone
Description: Configure zones to group two or more interfaces. When a zone is created you can
configure policies for the zone instead of individual interfaces in the zone.
edit <name>
set description {string}
set fabric-force-sync [enable|disable]
set fabric-object [enable|disable]
set fabric-object-source [member|local|...]
set interface <interface-name1>, <interface-name2>, ...
set intrazone [allow|deny]
config tagging
Description: Config object tagging.
edit <name>
set category {string}
set tags <name1>, <name2>, ...
next
end
set uuid {uuid}
FortiOS 8.0.0 CLI Reference
2210
Fortinet Inc.

<!-- 来源页 2211 -->
next
end
config system zone
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
interface
<interface-name>
Names of the interfaces that belong to this
zone. Interfaces must not be assigned to
another zone or have firewall policies
defined.
Select interfaces to add to the zone.
string
Maximum
length: 79
intrazone
Allow or deny traffic routing between
different interfaces in the same zone
(default = deny).
option
-deny
FortiOS 8.0.0 CLI Reference
2211
Fortinet Inc.

<!-- 来源页 2212 -->
Parameter
Description
Type
Size
Default
Option
Description
allow
Allow traffic between interfaces in the zone.
deny
Deny traffic between interfaces in the zone.
name
Zone name.
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
FortiOS 8.0.0 CLI Reference
2212
Fortinet Inc.
