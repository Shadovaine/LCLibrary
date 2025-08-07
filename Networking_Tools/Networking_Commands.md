# Networking Commands

## Commands used in network communications, diagnostics, system monitoring, and remote file transfer

## Table of Contents
- `ping`
- `ssh`
- `scp`
- `wget`
- `curl`
- `ifconfig`
- `ip`
- `taskwarrior`
- `ts`
- `error`
- `systemd-analyze`
- `lazydocker`
- `fabric`
- `asciinema`
- `netstat`
- `ss`
- `rsync`
- `ftp`
- `mtr`
- `mosh`
- `dog`
- `termshark`
- `lsof`
- `ipcalc`
- `wormhole`

## Command: ping
## Description Check connectivity to another host.

## Syntax
- `ping [OPTIONS] DESTINATION`

### Options
| Options | Descriptions | Example |
|---------|--------------|---------|
| `-c <NUM>` | Stop after sending N packets. |
| `-i <interval>` | Interval between packets (in seconds). |
| `-t <ttl>` | Set time-to-live (TTL). |
| `-s <size>` | Set the size of the packet payload. |
| `-W <timeout>` | Set timeout to wait for a reply. |
| `-q` | Quiet output. |
| `-v` | Verbose mode. |
| `-f` | Flood ping (root required). |
| `-D` | Print timestamps for each reply. |
| `-I <iface>` | Specify network interface to use. |
| `-4` | Force IPv4 ping. |
| `-6` | Force IPv6 ping. |

### Examples

## Ping google.com until stopped:
```bash  
ping google.com
```

### Breakdown
| Breakdown | Description |
|-----------|-------------|
| `ping` | Check connectivity command. |
| `google.com` | Target location. |
  
### Send 5 packets:
```bash
ping -c 5 google.com
```

### Breakdown
| Breakdown | Description |
|-----------|-------------|
| `ping` | Check connectivity command. |
| `-c 5` | Stop after 5 packets. |
| `google.com` | Target location. |

### Set 2-second interval between packets:
```bash
ping -i 2 google.com
```

### Breakdown
| Breakdown | Description |
|-----------|-------------|
| `ping` | Check connectivity command. |
| `-i 2` | Interval of 2 sec in between packets. |
| `google.com` | Target location. |
  
### Check TTL value:
```bash
ping -t 64 google.com
```

### Breakdown
| Breakdown | Description |
|-----------|-------------|
| `ping` | Check connectivity command. |
| `-t 2` | Time to live value of 2. |
| `google.com` | Target location. |

  
## Command: ssh
## Description Secure remote login:

## Syntax
- ssh [OPTIONS] [USER@]HOST

### Options
| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-p <port>` | Specify port. |
| `-i <identity>` | Use identity file (SSH key). |
| `-L [bind:]port:host:hostport` | Local port forwarding. |
| `-l <user>` | Log in as a specific user. |
| `-v` | Verbose mode. |
| `-C` | Enable compression. |
| `-x` | Enable X11 forwarding. |
| `-R [bind:]port:host:hostpost`| Remote port forwarding. |
| `-D <port>` |  Dynamic port forwarding. |
| `-N` | No remote command execution. |
| `-T` | Disable pseudo-terminal allocation. |
| `-o <option>` | Pass custom SSH client option. |
| `-4` | Force IPv4. |
| `-6` | Force IPv6. |
| `-q` | Quiet mode. |

### Examples

### Login with a specific key.
```bash
ssh -i ~/.ssh/id_rsa jake@192.168.1.50`
```

### Breakdown
| Breakdown | Description |
|-----------|-------------|
| `ssh` | Secure shell command. |
| `-i ~/.ssh/id_rsa` | Specific file with SSH key. |
| `sue@192.168.1.50` | Hostname with IPv4 address. |


  
## Command: scp
## Description: Securely copies files between systems.

## Syntax
- `scp [OPTIONS] SOURCE [USER@]HOST:DEST`

### Options
| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-P <port>` | Specify port. |
| `-P` | Preserves file attributes. |
| `-r` | Copy directories recursively. |
| `-C` | Enables compression during transfer. |
| `-v` | Verbose mode. |
| `-q` | Quiet mode. |
| `-l <limit>` | Limits bandwidth. |
| `-1 <identify>` | Specifies an SSH private key file for authentication. |
| `-0 <option>` | Passes SSH options directly. |
| `-S<program>` | Use a different SSH program. |
| `-4` | Forces IPv4. |
| `-6` | Forces IPv6. |
| `-B` | Batch mode. |
| `-T` | Disable strict filename escaping. |

### Examples

### Copy file to remote host:
```bash
scp file.txt sue@192.168.1.50:/home/sue/
```

### Breakdown
| Breakdown | Description |
|-----------|-------------|
| `scp` | Secure coping command.|
| `file.txt` | File to copy. |
| `sue@192.168.1.50:/home/sue/` | hostname with IPv4 address and target location. |
  

## Command: wget
## Description: Download files from the web.

## Syntax
- `wget [OPTIONS] URL`

### Options
| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-O <FILE>` | Save as specified filename. |
| `-c` | Resume incomplete download. |
| `-P <dir>` | Save files to a specific directory. |
| `-q` | Quiet mode. |
| `-nv` | Less verbose. |
| `-v` | Verbose mode. |
| `-N` | Only download if newer than local copy. |
| `--user=<user>` | Set HTTP/FTP username. |
| `--password=<pass>` | Set HTTP/FTP password. |
| `--header="<header>"` | Add custom header. |
| `--no-check-certificate` | Ignore SSL certificate errors. |
- `-r`:  Recursive download.
- `-l`:  <depth>`:  Set recursion depth.
- `-np`:  No parent directories.
- `-nd`:  No directory structure.
- `-A <list>`:  Accept only certain file types.
- `-R <list>`:  Reject certain file types.
- `--limit-rate=<rate>`:  Limit download speed.
- `-W <seconds>`:  Wait between downloads.
- `--random-wait`:  Random delay between downloads.
- `--tries=<n>`:  Retry download N times.
- `--timeout=<seconds>`:  Set timeout.
- `--retry-connrefused`:  Retry if connection is refused.
- `-b`:  Run in background.
- `-S`:  Show server response headers.
- `-d`:  Debug output.
- `-e robots=off`:  Ignore robots.txt.
- `--mirror`:  Mirro an entire website.

### **Example**

**Download a file and rename it**

```bash
wget -O ubuntu.iso http://example.com/ubuntu.iso
```

### **Breakdown**
- `wget`:  Download command.
- `-O ubuntu.iso`:  Directs to save as a specific filename.
- `http://example.com/ubuntu.iso`:  Target web location.
  

## **Command: curl**
**Description** Transfer data from/to server

## **Syntax**
- curl [OPTIONS] URL

### **Options**
- `-O`:  Save file with original name.
- `-L`:  Follow redirects.
- `-u`: Use username:password authentication.
- `-C -`:  Resume a download.
- `-s`:  Silent (no progress or errors.)
- `-S`:  Show errors even when `-s` is used.
- `-v`:  Verbose mode.
- `-k`:  Ignore SSL certificate validation.
- `-u  user:pass`:  HTTP Basic authentication.
- `-H "<header>"`:  Add a custom header.
- `-b <cookie>`:  Send cookie.
- `-c <cookie-file>`:  Save cookie to file.
- `--compressed`:  Request compressed response.
- `-X <method>`:  Specify HTTP request method.
- `-d @file.json`:  Send JSON from file.
- `--data-urlencode "<data>"`:  URL-encode data before sending.
- `-F "field=@file"`:  File upload.
- `--limit-rate <speed>`:  Limit download speed.
- `-r <range>`:  Download byte range.
- `--max-time <seconds>`:  Set a timeout.
- `-D <file>`:  Save response headers to a file.
- `-W "<format>"`:  Custom output formatting.
- `-I`:  Fetch only headers.
- `--resolve`:  Manually resolve domain to an IP.
- `--interface <iface>`:  Use specific network interface.
- `--socks5 <host:port>`:  Route through SOCKS5 proxy.
- `--retry <n>`:  Retry failed requests.
- `--retry-all-errors`:  Retry on all errors.
  
### **Examples**

**Save file with original name:**

```bash
curl -O http://example.com/file.txt
```

### **Breakdown**
- `curl`:  Transfer file command.
- `-O`:  Directs to save file with original name.
- `http://example.com/file.txt`:  Target file.

**Authenticating with username and password:**

```bash
curl -u user:pass https://api.example.com/data
```

### **Breakdown**
- `curl`:  Transfile file command.
- `-u`:  Directs to authenticate with username and password.
- `user:pass`:  username and password to authenticate.
- `https://api.example.com/data`:  Target location.


## **Command: ifconfig**
**Descriptions** Displays or configures network interfaces. (Legacy tool—ip replaces it in modern systems)

## **Syntax**
- ifconfig [INTERFACE] [OPTIONS]

### **Options**
- `(No arguement)`:  Show all active interfaces.
- `ifconfig -a`:  Show all interfaces.
- `ifconfig <iface>`:  Show details of a specific interface.
- `ifconfig <iface> up`:  Enable an interface.
- `ifconfig <iface> down`:  Disable an interface.
- `ifconfig <iface> <IP>`:  Assign IP address.
- `netmask <mask>`:  Set subnet mask.
- `broadcast <addr>`:  Set broadcast address.
- `add <IP>`:  Add a secondary IP.
- `del <IP>`:  Remove an IP address.
- `hw ether <MAC>`:  Change MAC address.
- `mtu <size>`:  Set MTU size.
- `promisc`:  Enable promiscuous mode.
- `-promisc`:  Disable promiscuous mode.
- `allmulti`:  Enable all-multicast mode.
- `-allmulti`:  Disable all-multicast mode.
- `debug`:  Enable debugging on the interface.
- `-debug`:  Disable debugging on the interface. 

### **Examples**

**View all interfaces:**
```bash
ifconfig
```

### **Breakdown**
- `ifconfig`:  Shows all interfaces.

**Bring up an interface:**
```bash
ifconfig eth0 up
```

### **Breakdown**
- `ifcongig`:  Show interface.
- `eth0`:  Selected interface.
- `up`:  Enable selected interface. 
**Bring down an interface:**

```bash
ifconfig eth0 down
```

**Set IP address:**

```bash
ifconfig eth0 192.168.1.100
```


## **ip**
- The modern replacement for ifconfig and route.

## **Syntax**
- ip [OBJECT] [OPTIONS]

### **Options**
addr	Show/modify IP addresses.
link	Show/modify interfaces.
route	Show/modify routing table.

### **Examples**
 Show all IP addresses:
ip addr

Bring up interface:
ip link set eth0 up

Add default route:
ip route add default via 192.168.1.1

View routes:
ip route show

## **taskwarrior**
– Terminal task/project manager
- Great for tracking recon, post-exploit steps, or learning goals in CLI-only setups

## **Syntax:** 
- task [command]

### **Examples**
- task add "Finish Linux+ drills"
- task list

### **Options**
- add, list, done, delete, modify
- Supports due dates, priorities, tags


## **ts – Task spooler (run background jobs and queue them)**

## **syntax**
- ts [command]

### **Examples**
- echo 'nmap -sV 192.168.1.0/24' | ts
- ts -l         # list jobs
- ts -c         # clear all

Use case: Queue multiple scans, backups, or cracking jobs without screen or tmux.

## **error – CLI error message explainer**

## **Syntax**
- error [error-message]

### **Example**
- error "permission denied"

Function: Searches known forums and docs to explain common Linux, Bash, or language errors.

🧠 IR Use: Explain odd messages during breach recovery or system misbehavior.


## **systemd-analyze – Diagnose boot performance**

## **Syntax**
- systemd-analyze

## **Example**
- systems-analyze blame

### **Options**
- blame Show which services delayed boot
- critical-chain Dependency tree and timing

🧠 Use case: Optimize startup or spot malicious services delaying boot.

## **lazydocker – TUI for Docker management**

## **Syntax** 
- lazydocker

## **Example**
- lazydocker

View running containers, images, logs, volumes in a slick terminal interface.

## **fabric – Python-based remote shell & deployment tool**
	•	Category: Automation / DevOps / Red Teaming

## **Syntax**
- fab [task]

Ex: (in fabfile.py)
def deploy():
    run("git pull")
    run("systemctl restart webapp")

Then:
fab deploy

Think of it as a programmable SSH runner across multiple servers — great for ops or mass remote changes.

## **asciinema – Record and share terminal sessions**

## **Syntax**
- asciinema rec [filename]

### **Examples**
asciinema rec install_hardened_linux.cast

Playback: asciinema play install_hardened_linux.cast

Perfect for: creating tutorials, logging incident response steps, or leaving a trail for blue teams or audits.


## **netstat**
- Displays network connections, routing tables, and interface stats. (Legacy—ss replaces it in modern systems)

## **Syntax**
- netstat [OPTIONS]

### **Options**
-t	Show TCP connections only.
-u	Show UDP connections only.
-l	Show listening ports.
-n	Show numerical addresses (don’t resolve DNS).
-p	Show process using the socket.

### **Examples**
 Show all connections:
netstat -a

Show only listening ports:
netstat -l

Show TCP connections
netstat -t

Show process names:
netstat -tulpn


## **ss**
- A faster, more modern replacement for netstat.

## **Syntax**
- ss [OPTIONS]

### **Options**
-t	Show TCP connections.
-u	Show UDP connections.
-l	Show listening sockets.
-n	Show numerical addresses.
-p	Show processes using sockets.

### **Examples**
 Show all TCP connections:
ss -t

 Show listening sockets:
ss -l

 Show processes using sockets:
ss -tunap

 Show UDP connections:
ss -u

## **rsync**
- Efficiently syncs files/directories between locations.

## **Syntax**
- rsync [OPTIONS] SOURCE DEST

### **Options**
-a	Archive mode (preserve permissions, symlinks).
-v	Verbose output.
-z	Compress data during transfer.
--delete	Delete files in dest not present in source.
-P	Show progress and keep partially transferred files.

### **Examples**
 Sync two directories:
rsync -av /home/jake/ /mnt/backup/

Sync over SSH:
rsync -avz /home/jake user@server:/backup/

Mirror source to destination (delete extras):
rsync -av --delete /source/ /dest/


## **ftp**
- Connect to an FTP server and transfer files.

## **Syntax**
- ftp [OPTIONS] HOST

### **Options**
get	Download a file.
put	Upload a file.
ls	List files on server.
cd	Change directory on server.
mget	Download multiple files.
mput	Upload multiple files.

### **Wxamples**
 Connect to an FTP server:
ftp ftp.example.com

Login and download a file:
Name: user
Password: ****
ftp> get file.zip

Upload a file:
ftp> put myfile.txt

Exit FTP:
ftp> bye

## **mtr – Combine traceroute + ping into real-time network map**

## **Syntax**
mtr [options] [host]

### **Examples**
- mtr google.com

### **Options**
	•	-r → Report mode (non-interactive)
	•	-c [n] → Number of pings
	•	-b → Show both IPs and hostnames
	•	-w → Wide report mode

## **mosh – Mobile Shell (better ssh for flaky networks)**
	•	Category: Remote Connectivity

## **Syntax**
-mosh  user@host

## **Example**
mosh jake@192.168.1.50

Benefits:
	•	Works even if your IP changes
	•	Auto-reconnects after drops
	•	Uses UDP instead of TCP

## **dog – Modern replacement for dig (DNS queries)**
	•	Category: DNS Tool
	•	Syntax: dog [domain]

### **Example**
- dog chat.openai.com

### **Options**
	•	@1.1.1.1 → Query a specific DNS server
	•	-t A → Query record type (e.g., A, MX, TXT, etc.)

## **termshark – Wireshark in your terminal**

## **Syntax**
- termshark -i [interface]

### **Example**
- sudo termshark -i eth0

### **Options**
	•	Navigate packet layers with arrow keys
	•	Filters work like tcpdump (ip.addr==192.168.0.5)


## **lsof - List network connections and the programs using them**

## **Syntax**
- sudo lsof -i

### ** Examples**
sudo lsof -i :22          # Who’s using SSH  
sudo lsof -i tcp@localhost:8080

## **ipcalc – IP calculator for CIDR, subnetting, broadcast, etc.**

## **Syntax**
- ipcalc [ip-address/cidr]

### **Example**
- ipcalc 192.168.1.5/24

Output:
	•	Network address
	•	Netmask
	•	Broadcast address
	•	Host range


## **wormhole**( – Encrypted file transfer between systems

## **Syntax**
- wormhole send [filename]
- wormhole receive

### **Example**
wormhole send secrets.tar.gz

Features:
Uses PAKE (Password-Authenticated Key Exchange)
No server required — transfers peer-to-peer
 Must be installed on both systems



