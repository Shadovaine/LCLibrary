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

# Command: ping

## Description: Check connectivity to another host

## Syntax

- `ping [OPTIONS] DESTINATION`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-c <NUM>` | Stop after sending N packets. | `ping -c 4 google.com` |
| `-i <interval>`| Interval between packets (in seconds). | `ping -i 3 google.com` |
| `-t <ttl>` | Set time-to-live (TTL). | `ping -t 3 google.com` |
| `-s <size>` |  Set the size of the packet payload. | `ping -s 128 google.com` |
| `-W <timeout>` | Set timeout to wait for a reply. | `ping -W 10 google.com` |
| `-q` | Quiet output. | `ping -q google.com` |
| `-v` | Verbose mode. | `ping -v google.com` |
| `-f` |  Flood ping (root required). | `sudo ping -f google.com` |
| `-D` |  Print timestamps for each reply. | `ping -D google.com` |
| `-I <iface>` | Specify network interface to use. | `ping -I eth0 8.8.8.8` |
| `-4` |  Force IPv4 ping. | `ping -4 google.com` |
| `-6` | Force IPv6 ping. | `ping -6 google.com` |

### Examples

### Ping google.com until stopped

```bash  
ping google.com
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `ping` | Check connectivity command. |
| `google.com` | Target location. |
  
### Send 5 packets

```bash
ping -c 5 google.com
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `ping` | Check connectivity command. |
| `-c 5` | Stop after 5 packets. |
| `google.com` | Target location. |

## Set 2-second interval between packets

```bash
ping -i 2 google.com
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `ping` | Check connectivity command. |
| `-i 2` | Interval of 2 sec in between packets. |
| `google.com` | Target location. |
  
### Check TTL value

```bash
ping -t 64 google.com
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `ping` | Check connectivity command. |
| `-t 2` | Time to live value of 2. |
| `google.com` | Target location. |

# Command: ssh

## Description: Secure remote login

## Syntax

- `ssh [OPTIONS] USER@HOST`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-p <port>` |  Specify port. | `ssh -p 2222 test@10.1.0.33` |
| `-i <identity>` |  Use identity file (SSH key). | `ssh -i ~/.ssh/id_ed25519 test@testserver.com` |
|  `-L <local_port>:<remote_host>:<remote_port>` |  Local port forwarding. | `ssh -L 8080:localhost:80 test@testserver.com` |
| `-l <user>` | Log in as a specific user. | `ssh -l "testname" test@1.1.1.1` |
| `-v` |  Verbose mode. | `ssh -v test@1.1.1.1` |
| `-x` |  Enable X11 forwarding. | `ssh -x test@ubuntu.u` |
| `-R <remote_port>:<local_host>:<local_port>` | Remote port forwarding. | `ssh -R 8000:local_host:3333 test@testhost` |
| `-D <port>` |  Dynamic port forwarding. | `ssh -D 3333 test@testhost` |
| `-N` |  No remote command execution. | `ssh -N -L 8080:localhost:80 test@testhost.com` |
| `-T` |  Disable pseudo-terminal allocation. | `ssh -T test@testhost 'uptime'` |
| `-o <option>` |  Pass custom SSH client option. | `ssh -o Testhostkeychecking=no test@1.1.1.1` |
| `-4` |  Force IPv4. | `ssh -4 test@1.1.1.1` |
| `-6` |  Force IPv6. |`ssh -6 test@1.1.1.1` |
| `-q` |  Quiet mode. | `ssh -q test@1.1.1.1` |

### Examples

### Login with a specific key

```bash
ssh -i ~/.ssh/id_rsa jake@192.168.1.50
```

### Breakdown

|Breakdown | Description |
|----------|-------------|
| `ssh` | Secure shell command. |
| `-i ~/.ssh/id_rsa` | Specific file with SSH key. |
| `sue@192.168.1.50` | Hostname with IPv4 address. |

# Command: scp

## Description: Securely copies files between systems

## Syntax

- scp [OPTIONS] SOURCE USER@HOST:DEST

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-P <port>` | Specify port. |
| `-P` |  Preserves file attributes. |
| `-r` | Copy directories recursively. |
| `-C` | Enables compression during transfer. |
| `-v` | Verbose mode. |
| `-q` | Quiet mode. |
| `-l <limit>` |  Limits bandwidth. |
| `-1 <identify>` |  Specifies an SSH private key file for authentication. |
| `-0 <option>` |  Passes SSH options directly. |
| `-S <program>` |  Use a different SSH program. |
| `-4` | Forces IPv4. |
| `-6` | Forces IPv6. |
| `-B` | Batch mode. |
| `-T` |  Disable strict filename escaping. |

### Examples

### Copy file to remote host

```bash
scp file.txt sue@192.168.1.50:/home/sue/
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `scp` |  Secure coping command. |
| `file.txt` |  File to copy. |
| `sue@192.168.1.50:/home/sue/` |  hostname with IPv4 address and target location. |
  
# Command: wget

## Description: Download files from the web

## Syntax

- `wget [OPTIONS] URL`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-O <FILE>` | Save as specified filename. | 
| `-c` | Resume incomplete download. |
| `-P <dir>` |  Save files to a specific directory. |
| `-nv` |  Less verbose. |
| `-v` |  Verbose mode. |
| `-N`| Only download if newer than local copy. |
| `--user=<user>` | Set HTTP/FTP username. |
| `--password=<pass>` |  Set HTTP/FTP password. |
| `--header="<header11>"` |  Add custom header. |
| `--no-check-certificate` |  Ignore SSL certificate errors. |
| `-r` | Recursive download. |
| `-l <depth>` |  Set recursion depth. |
| `-np` |  No parent directories. |
| `-nd` |  No directory structure. |
| `-A <list>` |  Accept only certain file types. |
| `-R <list>` |  Reject certain file types. |
| `--limit-rate=<rate>` |  Limit download speed. |
| `-W <seconds>` |  Wait between downloads. |
| `--random-wait` |  Random delay between downloads. |
| `--tries=<n>` |  Retry download N times. |
| `--timeout=<seconds>` |  Set timeout. |
| `--retry-connrefused` |  Retry if connection is refused. |
| `-b`| Run in background. |
| `-S` |  Show server response headers. |
| `-d` | Debug output. |
| `-e robots=off` |  Ignore robots.txt, |
| `--mirror` | Mirro an entire website. |

### Example

### Download a file and rename it

```bash
wget -O ubuntu.iso http://example.com/ubuntu.iso
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `wget` |  Download command |
| `-O ubuntu.iso` | Directs to save as a specific filename. |
| `http://example.com/ubuntu.iso` |  Target web location. |
  
# Command: curl

## Description: Transfer data from/to server

## Syntax

- `curl [OPTIONS] URL`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-O` | Save file with original name. |
| `-L` | Follow redirects. |
| `-u` | Use username:password authentication. |
| `-C -` | Resume a download. |
| `-s` |  Silent (no progress or errors.) |
| `-S` | Show errors even when `-s` is used. |
| `-v` | Verbose mode. |
| `-k` |  Ignore SSL certificate validation. |
| `-u  user:pass` |  HTTP Basic authentication. |
| `-H "<header>"` |  Add a custom header. |
| `-b <cookie>` | Send cookie. |
| `-c <cookie-file>` |  Save cookie to file. |
| `--compressed` |  Request compressed response. |
| `-X <method>` |  Specify HTTP request method. |
| `-d @file.json` |  Send JSON from file. |
| `--data-urlencode "<data>"` |  URL-encode data before sending. |
| `-1 `-F "field=@file"` | File upload. |
| `--limit-rate <speed>` |  Limit download speed. |
| `-r <range>` | Download byte range. |
| `--max-time <seconds>` |  Set a timeout. |
| `-D <file>` |  Save response headers to a file. |
| `-W "<format>"` |  Custom output formatting. |
| `-I` | Fetch only headers. |
| `--resolve` |  Manually resolve domain to an IP. |
| `--interface <iface>` |  Use specific network interface. |
| `--socks5 <host:port>`|  Route through SOCKS5 proxy. |
| `--retry <n>` |  Retry failed requests. |
| `--retry-all-errors` |  Retry on all errors. |
  
### ##Examples

### Save file with original name

```bash
curl -O http://example.com/file.txt
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `curl` | Transfer file command. |
| `-O` | Directs to save file with original name. |
| `http://example.com/file.txt` | Target file. |

### Authenticating with username and password

```bash
curl -u user:pass https://api.example.com/data
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `curl` | Transfile file command. |
| `-u` | Directs to authenticate with username and password. |
| `user:pass` | username and password to authenticate. |
| `https://api.example.com/data` | Target location. |

# Command: ifconfig

## Descriptions: Displays or configures network interfaces. (Legacy tool—ip replaces it in modern systems)

## Syntax

- `ifconfig [INTERFACE] [OPTIONS]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `(No arguement)` |  Show all active interfaces. |
| `ifconfig -a` |  Show all interfaces. |
| `ifconfig <iface>` |  Show details of a specific interface. |
| `ifconfig <iface> up` |  Enable an interface. |
| `ifconfig <iface> down` |  Disable an interface. |
| `ifconfig <iface> <IP>` |  Assign IP address. |
| `netmask <mask>` |  Set subnet mask. |
| `broadcast <addr>` |  Set broadcast address. |
| `add <IP>` |  Add a secondary IP. |
| `del <IP>` |  Remove an IP address. |
| `hw ether <MAC>` |  Change MAC address. |
| `mtu <size>` |  Set MTU size. |
| `promisc` |  Enable promiscuous mode. |
| `-promisc` |  Disable promiscuous mode. |
| `allmulti` |  Enable all-multicast mode. |
| `-allmulti` |  Disable all-multicast mode. |
| `debug` |  Enable debugging on the interface. |
| `-debug` | Disable debugging on the interface. |


### Examples

## View all network interfaces

```bash
ifconfig
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `ifconfig` | Shows all network interfaces. |

## Bring up an interface

```bash
ifconfig eth0 up
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `ifconfig` |  Show network interface. |
| `eth0` |  Selected interface. |
| `up` |  Enable selected interface. |

### Bring down an interface

```bash
ifconfig eth0 down
```

### Breakdown
| Breakdown | Description |
|-----------|-------------|
| `ifconfig` | Show network interface command |
| `eth0` |  Specific network interface to show |
| `down` | Directs to disable the eth0 network |

### Set IP address

```bash
ifconfig eth0 192.168.1.100
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `ifconfig` | Show network interface command |
| `eth0` | Specific network interface |
| ` 192.168.1.100` | Specific IP address to set to eth0 |

# Command: ip

## Description: The modern replacement for ifconfig

## Syntax

- `ip [OPTIONS] OBJECT { COMMAND | help}`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `addr` | Show/modify IP addresses |
| `link` | Show/modify interfaces |
| `route` | Show/modify routing table |
| `neigh` | Show or modify ARP cache |
| `rule` | Routing policy rules |
| `maddr` | Multicast addresses |
| `monitor ` | Watch changes to netlink |
| `help` | Show help |

### Examples

### Show all IP addresses

```bash
ip addr
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `ip` | Network command |
| `addr` | Directs to show all IP addresses |

### Enable eth0 network interface

```bash
ip link set eth0 up
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `ip` | Network command |
| `link` | Directs to set up specific interface |
| `set eth0` | Specific interface. |
| `up` | enables specific interface |

### Add default route

```bash
ip route add default via 192.168.1.1
```

### Breakdown
| Breakdown | Description |
|-----------|-------------|
| `ip` | Network command |
| `route` | Show routing table |
| `add default via 192.168.1.1` | Add a default route at IP address |

### View routes

```bash
ip route show
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `ip` | Network command |
| `route show` | Directs to show routes |

# Command: taskwarrior

## Description: Terminal task/project manager. Great for tracking recon, post-exploit steps, or learning goals in CLI-only setups

## Syntax:

- `task [options] [filter] [commands] [modifications]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `--debug ` | Show debug output |
| `--verbose` | More detailed output |
| `--quiet` | Suppress output |
| `--force` | Ignore warnings |
| `--` | Stop option parsing |
| `rc:<name>=<value>` | Temporarily overside config settings |
| `+<tag>` | Filter: has this tag |
| `-<tag>` | Filter: does NOT have this tag |
| `<attribute>:<value> | Filter: Matches specific attribute |
| `add` | Add a new task |
| `list` | Show pending tasks |
| `done` | Mark task as done |
| `delete` | Delete task |
| `start` | Mark task as started |
| `stop` | Stop task tracking |
| `mod` | Modify task |
| `edit` | Edit task in $editor |
| `annotate` | Add note to task |
| `denotate` | Remove note |
| `project` | Set or view project structure |
| `tags` | Add/remove tags |
| `undo` | Revert last change |
| `status` | View summary of tasks |
| `summary` | Project summary report |
| `log` | Show completed tasks |
| `info` | Show full details of a task |
| `export` | Export task list in JSON |
| `import` | Import tasks from JSON |
| `diagnostic` | View diagnostic info |
| `gc` | Garbage collect orphaned data |
| `sync` | Sync with taskserver |

### Examples

### Add a task

```bash
task add "Finish Linux+ drills"
```

### Breakdown

|Breakdwon | Description |
|----------|-------------|
| `task` | Task manager command |
| `add` | Directs to add a task |
| `Finish Linux+ drills` | task to add |

### Show list of tasks

```bash
task list
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `task` | task manager command |
| `list` | Directs to list all tasks |

# Command: ts 

## Description Task spooler (run background jobs and queue them)

## syntax

- `ts [OPTION] ... [Format]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-i` | Show interval instead of timestamp |
| `-r` | Show relative timestamp |
| `-s` | Use strftime format string instead of default |

### Examples


### Prefix with timestamps

```bash
echo -e "Line 1\nLine 2" | ts
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `echo` | Print command |
| `-e` | Allow the use of escape sequence |
| `"Line 1/nLine 2"` | String that will be printed |
| `ts` | task spool command |

# Command: error 

## Description: CLI error message explainer

## Syntax

- `error [error-message]`

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

 • Category: Automation / DevOps / Red Teaming

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

-t Show TCP connections only.
-u Show UDP connections only.
-l Show listening ports.
-n Show numerical addresses (don’t resolve DNS).
-p Show process using the socket.

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

-t Show TCP connections.
-u Show UDP connections.
-l Show listening sockets.
-n Show numerical addresses.
-p Show processes using sockets.

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

-a Archive mode (preserve permissions, symlinks).
-v Verbose output.
-z Compress data during transfer.
--delete Delete files in dest not present in source.
-P Show progress and keep partially transferred files.

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

get Download a file.
put Upload a file.
ls List files on server.
cd Change directory on server.
mget Download multiple files.
mput Upload multiple files.

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

 • -r → Report mode (non-interactive)
 • -c [n] → Number of pings
 • -b → Show both IPs and hostnames
 • -w → Wide report mode

## **mosh – Mobile Shell (better ssh for flaky networks)**

 • Category: Remote Connectivity

## **Syntax**

-mosh  user@host

## **Example**

mosh jake@192.168.1.50

Benefits:
 • Works even if your IP changes
 • Auto-reconnects after drops
 • Uses UDP instead of TCP

## **dog – Modern replacement for dig (DNS queries)**

 • Category: DNS Tool
 • Syntax: dog [domain]

### **Example**

- dog chat.openai.com

### **Options**

 • @1.1.1.1 → Query a specific DNS server
 • -t A → Query record type (e.g., A, MX, TXT, etc.)

## **termshark – Wireshark in your terminal**

## **Syntax**

- termshark -i [interface]

### **Example**

- sudo termshark -i eth0

### **Options**

 • Navigate packet layers with arrow keys
 • Filters work like tcpdump (ip.addr==192.168.0.5)

## **lsof - List network connections and the programs using them**

## **Syntax**

- sudo lsof -i

### **Examples**

sudo lsof -i :22          # Who’s using SSH  
sudo lsof -i tcp@localhost:8080

## **ipcalc – IP calculator for CIDR, subnetting, broadcast, etc.**

## **Syntax**

- ipcalc [ip-address/cidr]

### **Example**

- ipcalc 192.168.1.5/24

Output:
 • Network address
 • Netmask
 • Broadcast address
 • Host range

# Command: wormhole

## Description: Encrypted file transfer between systems

## Syntax

- wormhole send [filename]
- wormhole receive

### Example

wormhole send secrets.tar.gz

Features:
Uses PAKE (Password-Authenticated Key Exchange)
No server required — transfers peer-to-peer
 Must be installed on both systems
