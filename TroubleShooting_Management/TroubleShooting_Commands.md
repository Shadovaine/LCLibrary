# Troubleshooting Tools

## Description: Debugging/Network Security

## Table of Contents

- `strace`
- `traceroute`
- `tracepath`
- `lsof`
- `tcpdump`
- `nmap`
- `iptables`
- `ufw`
- `dig`
- `nslookup`
- `nc` or `netcat`

# Command: strace (System Trace)

## Description: Traces system calls and signals made by a process

## Syntax

- `strace [OPTIONS] COMMAND`

### Options

-p PID	Attach to a running process by PID.
-o FILE	Write trace output to FILE.
-e	Filter system calls (e.g., -e open,read,write).
-c	Count calls and display summary.

### Examples

### Trace a command

strace ls

### Trace only open calls

strace -e open ls

### Attach to a process by PID

sudo strace -p 1234

### Write trace to file

strace -o trace.log ls

### Summary of system call counts

strace -c ls

# Command: tracepath

## Description:

## Syntax

### Options

### Examples

# Command: lsof (List Open Files)

## Description: Lists open files and the processes using them

## Syntax

- `lsof [OPTIONS]`

### Options

-u USER	Show files opened by a specific user.
-p PID	Show files opened by a specific process.
-i	Show network connections.
+D DIR	Show files opened in a directory

### Examples

### List all open files

sudo lsof

### Show files for user “name"

sudo lsof -u name

### List network connections

sudo lsof -i

### List files opened in /var/log

sudo lsof +D /var/log

### Show files opened by PID 1234

sudo lsof -p 1234

# Command: tcpdump (Packet Sniffer)

## Description: - Captures and analyzes network packets.

## Syntax

- `tcpdump [OPTIONS] [FILTER]`

### Options

-i IFACE	Specify network interface (e.g., eth0).
-w FILE	Write packets to a file.
-r FILE	Read packets from a file.
-nn	Don’t resolve names (show raw IPs/ports).
-c COUNT	Stop after capturing COUNT packets.

### Examples

### Capture packets on eth0

sudo tcpdump -i eth0

###Capture and save to file

sudo tcpdump -i eth0 -w capture.pcap

### Read from capture file

sudo tcpdump -r capture.pcap

### Capture only HTTP traffic

sudo tcpdump -i eth0 port 80

sudo tcpdump -i eth0 port 80
sudo tcpdump -c 10 -i eth0

# Command: nmap (Network Mapper)

## Description: Scans networks for hosts, ports, and vulnerabilities

## Syntax

- `nmap [OPTIONS] TARGET`

### Options

-sS	TCP SYN scan (stealth).
-sV	Detect service versions.
-O	Detect OS of target.
-p PORTS	Scan specific ports.
-Pn	Skip host discovery (treat all as online).

### Examples

### Scan a single host

nmap 192.168.1.1

### Scan for open ports on host

nmap -p 22,80,443 192.168.1.1

### Service and version detection

nmap -sV 192.168.1.1

### OS detection

sudo nmap -O 192.168.1.1

### Scan a subnet

nmap 192.168.1.0/24

# Command: iptables (Linux Firewall Rules)

## Description: Manages packet filtering rules for IPv4.

## Syntax

- `sudo iptables [OPTIONS] COMMAND`

### Options

L	List current rules.
-A	Append a rule to a chain.
-D	Delete a rule from a chain.
-F	Flush all rules.

### Examples

### List current firewall rules

sudo iptables -L

### Allow incoming SSH (port 22)

sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT

### Block all incoming HTTP (port 80)

sudo iptables -A INPUT -p tcp --dport 80 -j DROP

### Flush all rules

sudo iptables -F

### Delete SSH allow rule

sudo iptables -D INPUT -p tcp --dport 22 -j ACCEPT

# Command: ufw

## Description:

## Syntax

### Options

### Examples

# Command: dig

## Description:

## Syntax

### Options

### Examples

# Command: nslookup

## Description:

## Syntax

### Options

### Examples

# Command: nc

## Description:

## Syntax

### Options

### Examples





## **lazygit – TUI interface for Git inside terminal**
	•	Category: Git / Dev Tooling
	•	Syntax: lazygit
	•	Features:
	•	View branches, diffs, stashes
	•	Commit & push without typing Git CLI



## **zellij – Terminal multiplexer (like tmux, but modular)**
	•	Category: Workflow / DevOps Enhancement
	•	Syntax: zellij
	•	Features:
	•	Tabbed terminal interface
	•	Resize panes, plugins, floating windows
	•	Beginner-friendly, config file is sane

Bonus: AI CLI Tools (Mentioned in your list as “AI custom commands”)

This space is rapidly growing. Here are a few to explore:

Tool	Description
aicommits	Auto-generates commit messages using OpenAI
continue	CLI coding assistant from the terminal
codellama	Run LLMs locally for code/infra help
chatblade	GPT wrapper for terminal use (secure prompt shell)


