# Troubleshooting Tools

## Description: Debugging/Network Security

## Table of Contents

- `strace`
- `lsof`
- `tcpdump`
- `nmap`
- `iptables`
- `ufw`
## strace (System Trace)**
-Traces system calls and signals made by a process.

## **Syntax**
strace [OPTIONS] COMMAND
strace [OPTIONS] -p PID

### **Options**
-p PID	Attach to a running process by PID.
-o FILE	Write trace output to FILE.
-e	Filter system calls (e.g., -e open,read,write).
-c	Count calls and display summary.

## **Examples**
Trace a command:
strace ls

 Trace only open calls:
strace -e open ls

Attach to a process by PID:
sudo strace -p 1234

Write trace to file:
strace -o trace.log ls

Summary of system call counts:
strace -c ls


## **lsof (List Open Files)**
- Lists open files and the processes using them.

## **Syntax**
- lsof [OPTIONS]

### **Options**
-u USER	Show files opened by a specific user.
-p PID	Show files opened by a specific process.
-i	Show network connections.
+D DIR	Show files opened in a directory

##### **Examples**
 List all open files:
sudo lsof

Show files for user “jake”:
sudo lsof -u jake

 List network connections:
sudo lsof -i

List files opened in /var/log:
sudo lsof +D /var/log

Show files opened by PID 1234:
sudo lsof -p 1234



## **tcpdump (Packet Sniffer)**
- Captures and analyzes network packets.

## ** Syntax**
- tcpdump [OPTIONS] [FILTER]

## **Options**
-i IFACE	Specify network interface (e.g., eth0).
-w FILE	Write packets to a file.
-r FILE	Read packets from a file.
-nn	Don’t resolve names (show raw IPs/ports).
-c COUNT	Stop after capturing COUNT packets.

### **Examples**
Capture packets on eth0:
sudo tcpdump -i eth0

Capture and save to file:
sudo tcpdump -i eth0 -w capture.pcap

 Read from capture file:
sudo tcpdump -r capture.pcap

Capture only HTTP traffic:
sudo tcpdump -i eth0 port 80

sudo tcpdump -i eth0 port 80
sudo tcpdump -c 10 -i eth0



## **nmap (Network Mapper)**
- Scans networks for hosts, ports, and vulnerabilities.

## **Syntax**
- nmap [OPTIONS] TARGET

## **Options**
-sS	TCP SYN scan (stealth).
-sV	Detect service versions.
-O	Detect OS of target.
-p PORTS	Scan specific ports.
-Pn	Skip host discovery (treat all as online).

Ex:

Scan a single host:
nmap 192.168.1.1

Scan for open ports on host:
nmap -p 22,80,443 192.168.1.1

Service and version detection:
nmap -sV 192.168.1.1

OS detection:
sudo nmap -O 192.168.1.1

Scan a subnet:
nmap 192.168.1.0/24


## **iptables (Linux Firewall Rules)**
- Manages packet filtering rules for IPv4.

## **Syntax**
- sudo iptables [OPTIONS] COMMAND

## **Options**
L	List current rules.
-A	Append a rule to a chain.
-D	Delete a rule from a chain.
-F	Flush all rules.

### **Examples##
List current firewall rules:
sudo iptables -L

 Allow incoming SSH (port 22):
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT

Block all incoming HTTP (port 80):
sudo iptables -A INPUT -p tcp --dport 80 -j DROP

Flush all rules:
sudo iptables -F

Delete SSH allow rule:
sudo iptables -D INPUT -p tcp --dport 22 -j ACCEPT


## **shred – Secure file deletion (overwrite before delete)**

## **Syntax**
- shred [options] [file]

### **Examples**
- shred -u -n 5 secrets.txt

#### **Options**
	•	-u → Truncate and remove file after overwriting
	•	-n → Number of overwrite passes (default: 3)
	•	-z → Final overwrite with zeroes (stealthy)

🧠 Use case: Securely delete sensitive data so it can’t be recovered with forensic tools.

## **vipe – Edit stdin input in your $EDITOR (usually nano or vim)**

## **Syntax**
- some_command | vipe | another_command

### **Examples**
- echo "classified content" | vipe | gpg -c > encrypted.gpg

Use case: Intercept CLI data to review/modify securely before sending it along a pipeline.

## **vidir – Edit directory filenames in bulk using your editor**

## **Syntax**
- vidir [directory]

### **Examples**
- vidir ~/Downloads

You’ll see a list of files and can edit names in bulk (great for obfuscating data dumps or renaming malicious payloads).

## **unp – Smart extractor for multiple compressed file formats**
	•	Category: File Handling / Forensics

## **Syntax**
- unp [archive]

### **Examples**
- unp secrets.tar.gz

Supported formats: .zip, .tar, .gz, .bz2, .7z, .rar, etc.

## **jg – JSON grepping / parsing tool**
	•	Category: Privacy Auditing / Data Extraction

## **Syntax**
- jg [query] < file.json

## **Examples**
- cat authlog.json | jg "user.name == 'jake'"

Useful for analyzing logs or leaked dumps in structured formats.


## **dog (revisited) – DNS tool**

Mentioned earlier in Networking but deserves a second mention here for recon / OSINT / DNS leaks.

IR Pro Tip: Combine these tools during incident response:

shred -u -z -n 7 /tmp/backdoor
vidir /tmp/loot
gpg -c secrets.log

## **progress – Show progress of common commands (cp, mv, etc.)**

## **Syntax**
- progress

## **Examples**
- progress -w

## **Options**
	•	-w → Watch mode (auto-refreshing)
	•	-c → Compact output

🧠 Shows live byte transfer progress for background file copy/move jobs — a nice visibility hack.

## **procs – Supercharged ps alternative with colors and extras**
	•	Category: Process Management

Syntax:
procs

Ex:
procs --watch

Features:
	•	Color-coded CPU/mem usage
	•	Shows user, start time, I/O
	•	--tree view like pstree

## **agg – Aggregate and visualize logs or command output**
	•	Category: Data Visualization
	•	Syntax: agg [options]

Ex:
journalctl -b | agg -f user.name

Features:
	•	Parses structured logs
	•	Outputs charts or breakdowns

🧠 Perfect for turning large CLI data (logs, JSON, etc.) into summaries or bar charts.

error – (revisited) Helps explain error messages in CLI tools

Worth another look in combo with other output-heavy tools like agg, journalctl, dstat.

## **vipe & vidir – Terminal editing power tools**
	•	Mentioned earlier under privacy, but especially useful when:
	•	Batch-editing log entries (vipe)
	•	Renaming payloads or decoys (vidir)
	•	Rewriting scripts on the fly

## **lazygit – TUI interface for Git inside terminal**
	•	Category: Git / Dev Tooling
	•	Syntax: lazygit
	•	Features:
	•	View branches, diffs, stashes
	•	Commit & push without typing Git CLI

## **btop – Blinged-out, interactive system monitor**
	•	Category: System Health / Dashboard
	•	Syntax: btop
	•	Example: Just run btop
	•	Shows:
	•	CPU, memory, disks, temps, processes — all in a colorful interface

🧠 Great for demoing system status during training or incident reviews.

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


