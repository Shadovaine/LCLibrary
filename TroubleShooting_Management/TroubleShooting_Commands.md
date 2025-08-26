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

## Description: - Captures and analyzes network packets. It can inspect headers, apply filters, and save to `.pcap` files

## Syntax

- `tcpdump [OPTIONS] [FILTER]`

## Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-i <interface>` | Select interface to capture on | `sudo tcpdump -i eth0` |
| `-n` | Do not resolve hostnames | `sudo tcpdump -nn -i eth0` |
| `-c <count>` | Capture only N packets | `sudo tcpdump -c 10 -i eth0` |
| `-w <file>` | Write packets to file | `sudo tcpdump -w capture.pcap -i eth0` |
| `-r <file>` | Read from pcap file instead of live capture | `tcpdump -r capture.pcap` |
| `-v`,`-vv`,`-vvv` | Increase verbosity | `sudo tcpdump -vvv -i eth0` |
| `-X` | show packet contents in hex and ASCII | `sudp tcpdump -X -i eth0` |
| `-xx` | Show packet contents in hex | `sudo tcpdump -xx -i eth0` |
| `-nni <iface>` | Shortcut for numeric + interface | `sudo tcpdump -nni eth0` |
| `-K` | Disable checksum validation | `sudo tcpdump -K -i eth0` |
| `-C <file_size>` | Rotate files by size | `sudo tcpdump -C 10 -w cap.pcap -i eth0` |
| `-G <seconds> + -w <file>` | Rotate capture files by time | `sudo tcpdump -G 60 -w 'cap-%Y%m%d%H%M%S.pcap' -i eth0` |
| `-U` | Write packets to file as they arrive | `sudo tcpdump -U -w stream.pcap -i eth0` |
| `-D` | List available interfaces | `tcpdump -D` |
| `-Z <user>` | Drop privileges to user after starting capture | `sudo tcpdump -Z name -i eth0` |
| `-e` | Print link-level headers | `sudo tcpdump -e -i eth0` |
| `-tt` | Timestamps - absolute time | `sudo tcpdump -tt -i eth0` |
| `-ttt` | Timestamps - relative time between packets | `sudo tcpdump -ttt -i eth0` |
| `-q` | Quiet mode | `sudo tcpdump -q -i eth0` |
| `-s <snaplen>` | Set capture size per packet | `sudo tcpdump -s 0 -w fullcap.pcap` |
| `-A` | Print packet payload in ASCII | `sudo tcpdump -A -i eth0 port 80` |

### Examples

## Capture packets on eth0

```bash
sudo tcpdump -i eth0
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Superuser command |
| `tcpdump` | Packet command |
| `-i` | Direct to specific network adapter |
| `eth0` | Specified adapter |

## Capture and save to file

```bash
sudo tcpdump -i eth0 -w capture.pcap
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Superuser command |
| `tcpdump` | packet command |
| `-i` | Directs to a specific network adapter |
| `eth0` | Specified adapter |
| `-w` | Directs to write packet output to a file |
| `capture.pcap` | Specified file |

## Read from capture file


```bash
sudo tcpdump -r capture.pcap
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Superuser command |
| `tcpdump` | Packet command | 
| `-r` | Directs to read from specified file |
| `capture.pcap` | Specified file |

# Command: nmap (Network Mapper)

## Description: A network scanning tool used to discover hosts and services. it can identify open ports, running services, OS details, and vulnerabilities

## Syntax

- `nmap [OPTIONS] TARGET`

## Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-sS` | TCP SYN scan | `nmap -sS 192.168.1.1` |
| `-sT` | TCP connect scan | `nmap -sT 192.168.1.1` |
| `-sU` | UDP scan | `nmap -sU 192.168.1.1` |
| `-sA` | ACK scan | `nmap -sA 192.168.1.1` |
| `-sW` | Window scan | `nmap -sW 192.168.1.1` |
| `-sM` | TCP Maimon scan | `nmap -sM 192.168.1.1` |
| `-sN` | Null scan | `nmap -sN 192.168.1.1` |
| `-sF` | FIN scan | `nmap -sF 192.168.1.1` |
| `-sX` | Xmas scan | `nmap -sX 192.168.1.1` |
| `-p <port>` | Scans specified port only | `nmap -p 22` |
| `-p 1-1000` | Scans a specified range | `nmap -p 1-1000` |
| `-p U:53,T:80` | Specific UDP and TCP ports to scan | `nmap -p U:53,T:80` |
| `-F` | Fast scan | `nmap -F 192.168.1.1` |
| `-p-` | Scan all 65535 ports | `nmap -p` |
| `-sV` | Detect service version | `nmap -sV 192.168.1.1` |
| `-O` | Detect operating system | `nmap -O 192.168.1.1` |
| `-T0` | Paranoid - very slow, avoids detection | `nmap -T0 192.168.1.1` |
| `-T3` | Normal Performance | `nmap -T3 192.168.1.1` |
| `-T4` | Aggressive - faster, more noticeable | `nmap -T4 192.168.1.1` |
| `-T5` | Insane - super fast and noisy | `nmap -T5 192.168.1.1` |
| `-sn` | Ping scan | `nmap -sn 192.168.1.1` |
| `-Pn` | Treat all hosts as online | `nmap -Pn 192.168.1.1` |
| `-PE` | ICMP echo request discovery | `nmap -PE 192.168.1.1` |
| `-v` | Verbose mode | `nmap -v 192.168.1.1` |
| `--reason` | Show why ports are in a specific state | `nmap --reason 22` |
| `--open` | Show only open ports | `nmap --open 192.168.1.1` |
| `--top-ports 20` | Scan the 20 most common ports | `nmap --top-ports 20 192.168.1.1` | 
| `--traceroute` | Trace the path to target | `nmap --traceroute 192.168.1.1` |

## Examples

## Scan a single host

```bash
nmap 192.168.1.1
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `nmap` | Network command |
| `192.168.1.1` | Target host to scan |

## Scan for open ports on host

```bash
nmap -p 22,80,443 192.168.1.1
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `nmap` | Networkd command |
| `-p` | Directs to scan specified ports |
| `22,80,443` | Specified ports |
| `192.168.1.1` | Specified host |


# Command: iptables (Linux Firewall Rules)

## Description: Manages packet filtering rules for IPv4.

## Syntax

- `sudo iptables [OPTIONS] COMMAND`

## Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-A` | Append a rule | `sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT` |
| `-I` | Insert a rule | `sudo iptables -I INPUT -p icmp -j DROP` |
| `-D` | Delete a rule | `sudo iptables -D INPUT -p tcp --dport 22 -j ACCEPT` |
| `-R` | Replace a current rule with a new one | `sudo intables -R INPUT 2 -p tcp --dport 80 -j DROP` |
| `-L` | List current rules | `Sudo iptables -L -n -v` |
| `-N` | Flush all rules | `sudo iptables -F INPUT` |
| `-X` | Creat a new chain | `sudo iptables -N LOGGING` |
| `-P` | Set policy | `sudo iptables -P INPUT DROP` |


## Examples

## List current firewall rules

```bash
sudo iptables -L
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Superuser command |
| `iptables` | Firewall command |
| `-L` | Directs to list all current rules |

## Flush all rules

```bash
sudo iptables -F
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Superuser command |
| `iptables` | Firewall command |
| `-F` | Directs to flush all rules |

# Command: ufw

## Description: Is a front-end for `iptables` which provides a simple CLI for managing netfilter firewall rules in Linux. It supports IPv4, IPv6, profiles, logging, rate-limiting, and app-based rule sets

## Syntax

- `ufw [Options] [Command]`

## Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `enable` | Turns firewall on | `sudo ufw enable` |
| `disable` | Turns firewall off | `sudo ufw disable` |
| `status` | Shows current firewall rules | `sudo ufw status` |
| `allow <port>` | Allows specified port | `sudo ufw allow 22` |
| `reject` | Actively responds with responds with `ICMP` | `sudo ufw reject 445` |
| `delete` | Removes an allowed rule | `sudo ufw delete allow 22` |
| `limit` | Protects a port/protocol by rate-limiting | `sudo ufw limit ssh` |
| `--dry-run` | Simulates change | `sudo ufw --dry-run enable` |
| `reset` | Disables `ufw` and deletes all rules | `sudo ufw reset` |

## Examples

## Secure SSH

```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 22/tcp
sudo ufw enable
```

# Command: dig

## Description: Stands for Domain Information Groper. It queries name servers for information. More modern and script-friendly than `nslookup`. It will return specific record types, query different servers , trace delegation paths, and format results for automation.

## Syntax

- `dig [@server] [name] [type] [class] [options]`

| Syntax Component | Description |
|------------------|-------------|
| `@server` | DNS server to query |
| `name` | Domain name |
| `type` | Record type |
| `class` | usually `IN` for internet |
| `options` | Control output and query style |

## Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `@server` | Query a specific DNS server | `dig @1.1.1.1 example.com` |
| `+short` | Minimal output | `dig +short example.com` |
| `+noall +answer` | Show only the answer section | `dig example.com +noall +answer` |
| `+trace` | Trace delegation from root servers | `dig example.com +trace` |
| `+dnssec` | Request DNSSEC records | `dig example.com +dnssec` |
| `+multi` | Print multiple results per line | `dig +multi example.com` |
| `+stats` | Show query statistics | `dig example.com +stats` |
| `+nocomments` | Suppress comments in output | `dig example.com +nocomments` |
| `+nocmd` | Suppress the initial `dig` header line | `dig example.com +nocmd +noall +answer` |
| `+search` | Use `/etc/resolv.conf` search list | `dig +search host1` |
| `+time=<sec>` | Set query timeout | `dig example.com +time` | 
| `+tries=<NUM>` | Retry attempts before failing | `dig -x 8.8.8.8` |
| `-p<port>` | Query on a custom port | `dig @127.0.0.1 -p 1100 example.com` |
| `-t <type>` | Explicitly set query type | `dig -t MX example.com` |
| `-f <file>` | Batch mode | `dig -f example.txt` |
| `-4` | Forces IPv4 transport | `dig -4 example.com` |
| `-6` | Forces IPv6 transport | `dig -6 example.com` |
| `+tcp` | Forces TCP use instead of UDP | `dig +tcp example.com` |
| `+ignore` | Ignore truncation errors | `dig +ignore example.com` |

## DNS Records

| DNS Record | Description |
|------------|-------------|
| `A` | IPv4 address |
| `AAAA` | IPv6 address |
| `MX` | Mail Exchange |
| `NS` | Name servers |
| `CNAME` | Canonical name |
| `SOA` | Start of Authority |
| `TXT` | Text(SPF/DKIM) |
| `ANY` | All records |


## Examples

## Quick IP lookup

```bash
dig +short example.com
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `dig` | Network command |
| `+short` | Directs to produce a minimal output |
| `example.com` | Specific Domain |

# Command: nslookup

## Description: Queries DNS servers for information about hostnames, IP addresses, or other DNS records. It can run in interactive mode or non-interactive mode

## Syntax

- `nslookup [Options] [Hostname] [Server]`

- `[Hostname]` = Domain name or IP address to look up
- `[Server]` = Optional DNS server to query (default is system reslover)

## Options

|Options | Descriptions | Examples |
|--------|--------------|----------|
| `nslookup <hostname>` | Basic query | `nslookup google.com` |
| `nslookup <IP>` | Reverse lookup | `nslookup 8.8.8.8` |
| `nslookup <hostname> <server>` | Query a specific DNS server | `nslookup example.com 8.8.8.8` |
| `-debug` | Enable debug mode | `nslookup -debug google.com` |
| `-timeout-<seconds>` | Set query timeout | `nslookup -timeout=5 example.com` |
| `-retry=<NUM>` | Number of retries before giving up | `nslookup -retry=2 example.com` |
| `-port=<NUM>` | Use a specific DNS server port (default is 53) | `nslookup -port=5353 example.com` |
| `-class=<class>` | Specify DNS class | `nslookup -class=IN example.com` | `nslookup -class=IN example.com` |
| `-sil` | Silent mode | `nslookup -sil example.com` |

## DNS Records

| DNS Record | Description |
|------------|-------------|
| `A` | IPv4 address |
| `AAAA` | IPv6 address |
| `MX` | Mail exchange |
| `NS` | Name servers |
| `CNAME` | canonical name |
| `SOA` | Start of authority |
| `TXT` | Text records |

## Examples

## Find domain name of an IP

```bash
nslookup 8.8.8.8
```

### Breakdown 

| Breakdown | Description |
|-----------|-------------|
| `nslookup` | Network command |
| `8.8.8.8` | Specified IP |

# Command: nc

## Description: A versatile networking utility that reads and writes data across network connections using TCP or UDP. It is a useful debugging, testing, file transfer, and port scanning.

## Syntax

- `nc [Options] host port`

## Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-q<sec>` | Quit after EOF on `stdin` and delay | `nc -q 1 192.168.1.10 1234` |
| `-X <proxy version>` | Specify proxy protocol (4,5, connect) | `nc -X 5 -x 127.0.0.1:8080 example.com 22` |
| `-x <proxy:port>` | Specify SOCKS4 proxy | `nc -x 127.0.0.1: 9050 -X 5 example.com 80` |
| `-o <file>` | Hex dump traffic into file | `nc -o dump.txt example.com 80` |
| `-c <program>` | Run command via shell after connection | `nc -l -p 5555 -c /bin/bash` |
| `-e <program>` | Execute a program after connection | `nc -l -p 4444 -e /bin/bash` |
| `-k` | Keep listening after client disconnects | `nc -lk 1234` |
| `-w <secs>` | Timeout for connects and final net reads | `nc -w 5 google.com 80` |
| `-n` | Do not resolve DNS (use raw IPs) | `nc -n 192.168.1.1 80` |
| `-vv` | Extra verbose mode | `nc -vv example.com 22` |
| `-v` | Verbose mode | `nc -v google.com 80` |
| `-z` | Zero-I/O mode(useful for scanning) | `nc -zv 192.168.1.1 20-80` |
| `-u` | Use UDP instead of TCP | `nc -u 1234` |
| `-p <port>` | Specify source port | `nc -p 1234 example.com 80` |
| `-l` | Listen mode | `nc -l 1234` |

## Examples

## Simple chat server/client

- Listener

```bash
nc -l 1234
```

- Client

```bash
nc 192.168.1.1 1234
```

### Breakdown for Listener

| Breakdown | Description |
|-----------|-------------|
| `nc` | Troubleshooting command |
| `-l` | Directs to listen |
| `1234` | Specified port to listen for |

### Breakdown for Client

| Breakdown | Description |
|-----------|-------------|
| `nc` | Troubleshooting command |
| `192.168.1.1 1234` | Specified IPv4 address with port number |
