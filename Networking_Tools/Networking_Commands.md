Networking Commands

ping
- check connectivity to another host

ping [OPTIONS] DESTINATION

Options

-c N	Stop after sending N packets.
-i S	Interval between packets (in seconds).
-t N	Set time-to-live (TTL).

Ex:

Ping google.com until stopped:
ping google.com

Send 5 packets:
ping -c 5 google.com

Set 2-second interval between packets:
ping -i 2 google.com

Check TTL value:
ping -t 64 google.com

ssh

Secure remote login

ssh [OPTIONS] [USER@]HOST

Options

-p	Specify port.
-i	Use identity file (SSH key).
-L	Local port forwarding.

Ex:

ssh -i ~/.ssh/id_rsa jake@192.168.1.50
Login with a specific key.



scp 

Securely copy files between systems

scp [OPTIONS] SOURCE [USER@]HOST:DEST

Options

-P	Specify port.
-r	Copy directories recursively.

Ex:

scp file.txt jake@192.168.1.50:/home/jake/
Copy file to remote host.



wget

Download files from the web

wget [OPTIONS] URL

Options

	Description
-O FILE	Save as specified filename.
-c	Resume incomplete download.
--limit-rate	Limit download speed.

Ex:

wget -O ubuntu.iso http://example.com/ubuntu.iso



curl 

Transfer data from/to server

curl [OPTIONS] URL

Options

-O	Save file with original name.
-L	Follow redirects.
-u	Use username:password authentication.
-X	Specify HTTP request method.
-d	Send data in POST request.

Ex:

curl -O http://example.com/file.txt
curl -u user:pass https://api.example.com/data

ifconfig

Displays or configures network interfaces. (Legacy tool—ip replaces it in modern systems)

ifconfig [INTERFACE] [OPTIONS]

Options

(no args)	Show all active interfaces.
up	Enable a network interface.
down	Disable a network interface.
inet ADDRESS	Assign IP address to interface.

Ex:

View all interfaces:
ifconfig

Bring up an interface:
ifconfig eth0 up

 Bring down an interface:
ifconfig eth0 down

Set IP address:
ifconfig eth0 192.168.1.100

ip

The modern replacement for ifconfig and route.

ip [OBJECT] [OPTIONS]

Options

addr	Show/modify IP addresses.
link	Show/modify interfaces.
route	Show/modify routing table.

Ex:

 Show all IP addresses:
ip addr

Bring up interface:
ip link set eth0 up

Add default route:
ip route add default via 192.168.1.1

View routes:
ip route show

taskwarrior – Terminal task/project manager
 Syntax: 
task [command]

Ex:
task add "Finish Linux+ drills"
task list

Options:
	•	add, list, done, delete, modify
	•	Supports due dates, priorities, tags

🧠 Great for tracking recon, post-exploit steps, or learning goals in CLI-only setups

ts – Task spooler (run background jobs and queue them)
	•	Category: Job Queueing
syntax:
ts [command]

Ex:
echo 'nmap -sV 192.168.1.0/24' | ts
ts -l         # list jobs
ts -c         # clear all

Use case: Queue multiple scans, backups, or cracking jobs without screen or tmux.

error – CLI error message explainer
	•	Category: Developer Helper / Debugging

Syntax: error [error-message]

Ex:
error "permission denied"

Function: Searches known forums and docs to explain common Linux, Bash, or language errors.

🧠 IR Use: Explain odd messages during breach recovery or system misbehavior.


systemd-analyze – Diagnose boot performance
	•	Category: Performance / System Boot Analysis

Syntax:
systems-analyze

Ex:
systemd-analyze blame


Options:
	•	blame → Show which services delayed boot
	•	critical-chain → Dependency tree and timing

🧠 Use case: Optimize startup or spot malicious services delaying boot.

lazydocker – TUI for Docker management

Syntax: lazydocker
Ex:
lazydocker

Function: View running containers, images, logs, volumes in a slick terminal interface.

fabric – Python-based remote shell & deployment tool
	•	Category: Automation / DevOps / Red Teaming

Syntax:

fab [task]

Ex: (in fabfile.py)
def deploy():
    run("git pull")
    run("systemctl restart webapp")

Then:
fab deploy

Think of it as a programmable SSH runner across multiple servers — great for ops or mass remote changes.

asciinema – Record and share terminal sessions

Syntax:
asciinema rec [filename]

Ex:
asciinema rec install_hardened_linux.cast

Playback: asciinema play install_hardened_linux.cast

Perfect for: creating tutorials, logging incident response steps, or leaving a trail for blue teams or audits.



netstat

Displays network connections, routing tables, and interface stats. (Legacy—ss replaces it in modern systems)

netstat [OPTIONS]

Options

-t	Show TCP connections only.
-u	Show UDP connections only.
-l	Show listening ports.
-n	Show numerical addresses (don’t resolve DNS).
-p	Show process using the socket.

Ex:

 Show all connections:
netstat -a

Show only listening ports:
netstat -l

Show TCP connections
netstat -t

Show process names:
netstat -tulpn


ss

A faster, more modern replacement for netstat.

ss [OPTIONS]

-t	Show TCP connections.
-u	Show UDP connections.
-l	Show listening sockets.
-n	Show numerical addresses.
-p	Show processes using sockets.

Ex:

 Show all TCP connections:
ss -t

 Show listening sockets:
ss -l

 Show processes using sockets:
ss -tunap

 Show UDP connections:
ss -u



rsync

Efficiently syncs files/directories between locations.

rsync [OPTIONS] SOURCE DEST

Options
-a	Archive mode (preserve permissions, symlinks).
-v	Verbose output.
-z	Compress data during transfer.
--delete	Delete files in dest not present in source.
-P	Show progress and keep partially transferred files.

Ex:

 Sync two directories:
rsync -av /home/jake/ /mnt/backup/

Sync over SSH:
rsync -avz /home/jake user@server:/backup/

Mirror source to destination (delete extras):
rsync -av --delete /source/ /dest/


ftp

Connect to an FTP server and transfer files.

ftp [OPTIONS] HOST

Options

get	Download a file.
put	Upload a file.
ls	List files on server.
cd	Change directory on server.
mget	Download multiple files.
mput	Upload multiple files.

Ex:

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

mtr – Combine traceroute + ping into real-time network map

Syntax:
mtr [options] [host]

Ex:
mtr google.com

Options:
	•	-r → Report mode (non-interactive)
	•	-c [n] → Number of pings
	•	-b → Show both IPs and hostnames
	•	-w → Wide report mode

mosh – Mobile Shell (better ssh for flaky networks)
	•	Category: Remote Connectivity

Syntax:
mosh  user@host

Ex:
mosh jake@192.168.1.50

Benefits:
	•	Works even if your IP changes
	•	Auto-reconnects after drops
	•	Uses UDP instead of TCP

dog – Modern replacement for dig (DNS queries)
	•	Category: DNS Tool
	•	Syntax: dog [domain]
Ex:
dog chat.openai.com

Options:
	•	@1.1.1.1 → Query a specific DNS server
	•	-t A → Query record type (e.g., A, MX, TXT, etc.)

termshark – Wireshark in your terminal
	•	Category: Packet Analysis

Syntax:
termshark -i [interface]

Ex:
sudo termshark -i eth0

Options:
	•	Navigate packet layers with arrow keys
	•	Filters work like tcpdump (ip.addr==192.168.0.5)


lsof -i – List network connections and the programs using them
	•	Category: Network / Process Mapping

Syntax:
sudo lsof -i

Ex:
sudo lsof -i :22          # Who’s using SSH  
sudo lsof -i tcp@localhost:8080

ipcalc – IP calculator for CIDR, subnetting, broadcast, etc.

Syntax:
ipcalc [ip-address/cidr]

Ex:
ipcalc 192.168.1.5/24

Output:
	•	Network address
	•	Netmask
	•	Broadcast address
	•	Host range


wormhole – Encrypted file transfer between systems

Syntax:
wormhole send [filename]
wormhole receive

Ex:
wormhole send secrets.tar.gz

Features:
	•	Uses PAKE (Password-Authenticated Key Exchange)
	•	No server required — transfers peer-to-peer
	•	Must be installed on both systems



