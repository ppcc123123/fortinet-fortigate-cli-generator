# FortiOS CLI 基础与命令树

> 来源: FortiOS-8.0.0-CLI_Reference.pdf
> 覆盖命令/章节: Availability of commands and options, Command tree
> 本文件由 extract_pdf.py 从官方 PDF 自动提取，请勿手动编辑；
> 如需修正请修改 map.json 后重跑脚本。

---


<!-- 来源页 132 -->
FortiOS CLI reference
This document describes FortiOS 8.0.0 CLI commands used to configure and manage a FortiGate unit from the
command line interface (CLI). For information on using the CLI, see the FortiOS 8.0.0 Administration Guide,
which contains information such as:
l Connecting to the CLI
l CLI basics
l Command syntax
l Subcommands
l Permissions
Availability of commands and options
Some FortiOS CLI commands and options are not available on all FortiGate units. The CLI displays an error
message if you attempt to enter a command or option that is not available. You can use the question mark ‘?’ to
verify the commands and options that are available.
Commands and options may not be available for the following reasons:
FortiGate model
All commands are not available on all FortiGate models. For example, a hardware switch can be configured only
on models which have the corresponding hardware switch chipset.
Hardware configuration
For example, settings like mediatype would only be available on units with SFPs.
FortiOS Carrier, FortiGate 5K/6K/7K, FortiGate with LTE, etc.
Commands for extended functionality are not available on all FortiGate models. The CLI Reference may not
include all commands.
Command tree
Enter tree to display the entire FortiOS CLI command tree. To capture the full output, connect to your device
using a terminal emulation program, such as PuTTY, and capture the output to a log file.
l To view all available commands, enter tree.
l To view a specific configuration branch of a tree, enter tree <branch>, for example: tree system.
FortiOS 8.0.0 CLI Reference
132
Fortinet Inc.

---


<!-- 来源页 132 -->
FortiOS CLI reference
This document describes FortiOS 8.0.0 CLI commands used to configure and manage a FortiGate unit from the
command line interface (CLI). For information on using the CLI, see the FortiOS 8.0.0 Administration Guide,
which contains information such as:
l Connecting to the CLI
l CLI basics
l Command syntax
l Subcommands
l Permissions
Availability of commands and options
Some FortiOS CLI commands and options are not available on all FortiGate units. The CLI displays an error
message if you attempt to enter a command or option that is not available. You can use the question mark ‘?’ to
verify the commands and options that are available.
Commands and options may not be available for the following reasons:
FortiGate model
All commands are not available on all FortiGate models. For example, a hardware switch can be configured only
on models which have the corresponding hardware switch chipset.
Hardware configuration
For example, settings like mediatype would only be available on units with SFPs.
FortiOS Carrier, FortiGate 5K/6K/7K, FortiGate with LTE, etc.
Commands for extended functionality are not available on all FortiGate models. The CLI Reference may not
include all commands.
Command tree
Enter tree to display the entire FortiOS CLI command tree. To capture the full output, connect to your device
using a terminal emulation program, such as PuTTY, and capture the output to a log file.
l To view all available commands, enter tree.
l To view a specific configuration branch of a tree, enter tree <branch>, for example: tree system.
FortiOS 8.0.0 CLI Reference
132
Fortinet Inc.

<!-- 来源页 133 -->
FortiOS CLI reference
l To view all available diagnose commands, enter tree diagnose.
l To view all available execute commands, enter tree execute.
FortiOS 8.0.0 CLI Reference
133
Fortinet Inc.
