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

- `strace [OPTIONS] COMMAND [args...]`

## Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-o<FILE>` | Write a trace output to a file | `strace -o trace.log ls` |
| `-p<PID>` | Attach to an already running process | `strace -p 1234` |
| `-c` | Count syscalls | `strace -c ls` |
| `-f` | Follow forks | `strace -f firefox` |
| `-ff` | Follow forks and write separate trace files | `strace -ff -o trace firefox` |
| `-t` | Add timestamp to each line | `strace -t ls` |
| `-tt` | Microsecond timestamps | `strace -tt ls` |
| `-ttt` | Prints UNIX epoch timestamps | `strace -ttt ls` |
| `-T` | Show syscall time | `strace -T ls` |
| `-r` | Relative timestamp | `strace -r ls` |
| `-i` | Show syscall instruction pointer | `strace -i ls` |
| `-k` | Print kernel stack trace for each syscall | `strace -k ls` |
| `-E VAR=VAL` `-E VAR` `-E VAR-` | Modify environment variables | `strace -E HOME=/tmp ls` |
| `-u <username>` | Run command as another user | `sudo strace -u nobody ls` |
| `-P <path>` | Trace only syscalls that access a specific path | `strace -P /etc/passwd cat /etc/passwd` |
| `-yy` | Pring file descriptor paths | `strace -yy ls` |
| `-v` | Verbose mode | `strace -v ls` |
| `-s <size>` | Increase maximum string size shown | `strace -s 200 ls` |
| `-e <trace=<set>` `-e signal=<set>` `-e status=<set>` | Trace only specified sets | `strace -e trace=file ls` |

## Syscall Categories

| Syscall Categories | Specific Names |
|--------------------|----------------|
| `file` | File-related syscalls |
| `network` | Networking syscalls |
| `process` | Process mgmt |
| `ipc` | inter-process communication |
| `signal` | Signal-related |
| `desc` | File Descriptor |

## Examples

## Trace a command

```bash
strace ls
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `strace` | Troubleshooting command |
| `ls` | Specific file |

## Trace only open calls

```bash
strace -e open ls
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `strace` | Troubleshooting command |
| `-e` | Directs to a status command |
| `open` | Status command |
| `ls` | Specified file |

## Attach to a process by PID

```bash
sudo strace -p 1234
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Superuser Command |
| `strace` | Troubleshooting command |
| `-p` | Directs to use specific PID |
| `1234` | Specified PID |

## Write trace to file

```bash
strace -o trace.log ls
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `strace` | Troubleshooting command |
| `-o` | Directs to write a trace file |
| `trace.log` | Specified trace file |
| `ls` | Specifed command to trace |

# Command: tracepath

## Description: Traces the path packets take to a destination host

## Syntax

- `tracepath [Options] <destination> [Port]`

## Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-n` | Do not resolve hostname, show numeric IPs | `tracepath -n google.com` |
| `-b` | Show both IP addresses and hostnames | `tracepath -b google.com` |
| `-m<max_hops>` | Set maximum hop limit | `tracepath -m 15 google.com` |
| `-l <pktlen>` | Set packet length in bytes | `tracepath -l 1200 google.com` |
| `-p<port>` | Set base destination port | `tracepath -p 4444 google.com` |
| `-4` | Force IPv4 | `tracepath -4 google.com` |
| `-6` | Force IPv6 | `tracepath -6 ipv6.google.com` |
| `-V` | Print version information | `tracepath -V` |

## Examples

## Trace without DNS resolution

```bash
tracepath -n 8.8.8.8
```
### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `tracepath` | Troubleshooting command |
| `-n` | Directs to not resolve DNS | 
| `8.8.8.8` | IPv4 address |

# Command: lsof (List Open Files)

## Description: Lists open files and the processes using them

## Syntax

- `lsof [OPTIONS] [names...]`

## Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-p <pid>` | List open files for a specific process ID | `lsof -p 1234` |
| `-c <command>` | Show files opened by processes whose command starts with `<command>` | `lsof -c ssh` |
| `-u <user>` | Show files opened by a specific user | `lsof -u name` |
| `-i` | Show network connections | `lsof -i` |
| `-F` | Machine-reachable output | `lsof -F -p 1234` |
| `-r <intervals>` | Repeat listing at a time interval | `lsof -r -i:80` |
| `-d <fd>` | Filter by file descriptor | `lsof -d 0,1,2` |
| `-g <gid>` | Show processes using specific group ID | `lsof -g 1000` |
| `-a` | Logical AND when combining multiple options | `lsof -u name -a -i` |
| `-P` | Do not resolve port numbers to service names | `lsof -nP -i` |
| `-n` | Do not resolve hostname | `lsof -n -i` |
| `-t` | Print only PID | `lsof -t -i:80` |
| `+D <directory>` | Show all open files under a directory | `sudo lsof +D /var/log` |
| `+d <directory>` | Same as +D but non-recursive | `sudo lsof +d /tmp` |

## Examples

## List all open files

```bash
sudo lsof
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Superuser command |
| `lsof` | Lists all open files |

## Show files for user “name"

```bash
sudo lsof -u name
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Superuser command |
| `lsof` | Lists all open files |
| `-u` | Directs to a specific user |
| `name` | Specified user |

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

## Description: A versatile networking utility that reads and writes data across network connections using TCP or UDP. It is a useful debugging, testing, file transfer, and port scanning.

## Syntax

- `nc [Options] host port

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| 
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


