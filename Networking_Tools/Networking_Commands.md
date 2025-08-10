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
| `ping` | Network command. |
| `google.com` | Target location. |
  
### Send 5 packets

```bash
ping -c 5 google.com
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `ping` | Network command. |
| `-c 5` | Stop after 5 packets. |
| `google.com` | Target location. |

## Set 2-second interval between packets

```bash
ping -i 2 google.com
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `ping` | Network command. |
| `-i 2` | Interval of 2 sec in between packets. |
| `google.com` | Target location. |
  
### Check TTL value

```bash
ping -t 64 google.com
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `ping` | Network command. |
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
| `ssh` | Remote Network command. |
| `-i ~/.ssh/id_rsa` | Specific file with SSH key. |
| `sue@192.168.1.50` | Hostname with IPv4 address. |

# Command: scp

## Description: Securely copies files between systems

## Syntax

- `scp [OPTIONS] SOURCE USER@HOST:DEST`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-P <port>` | Specify port. | `scp -P 2222 file.txt name@server:/home/name/` |
| `-p` |  Preserves file attributes. | `scp -p file.txt name@server:/backup/` |
| `-r` | Copy directories recursively. | `scp -r /home/name/docs name@server:/backup/docs` |
| `-C` | Enables compression during transfer. | `scp -C bigfile.iso name@server:/backup/` |
| `-v` | Verbose mode. | `scp -v file.txt name@server:/backup/` |
| `-q` | Quiet mode. | `scp -q file.txt name@server:/backup/` |
| `-l <limit>` |  Limits bandwidth. | `scp -l 800 file.txt name@server:/backup/` |
| `-i <identify>` |  Specifies an SSH private key file for authentication. | `scp -i ~/.ssh/id_ed25519 file.txt name@server:/backup/` |
| `-0 <option>` |  Passes SSH options directly. | `scp -o StrictHostKeyChecking=no file.txt jake@server:/backup/` |
| `-4` | Forces IPv4. | `scp -4 file.txt name@server:/backup/` |
| `-6` | Forces IPv6. | `scp -6 file.txt name@server:/backup/` |

### Examples

### Copy file to remote host

```bash
scp file.txt name@192.168.1.50:/home/name/
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `scp` |  Secure coping command. |
| `file.txt` |  File to copy. |
| `name@192.168.1.50:/home/name/` |  hostname with IPv4 address and target location. |
  
# Command: wget

## Description: Download files from the web

## Syntax

- `wget [OPTIONS] URL`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-O <FILE>` | Write output to a specific file  | `wget -O myfile.html https://example.com` |
| `-o <FILE>` | Write log message to a file | `wget -o download.log https://example.com/file.zip` |
| `-c` | Resume incomplete download. | `wget -c https://example.com/bigfile.iso` |
| `-P <dir>` |  Save files to a specific directory. | `wget -P /tmp/downloads https://example.com/file.zip` |
| `-nv` |  Less verbose. | `wget -nv https://example.com/file.zip` |
| `-v` |  Verbose mode. | `wget -v https://example.com/file.zip` |
| `-N`| Only download if newer than local copy. | `wget -N https://example.com/file.zip` |
| `--user=<user> --password=PASS` | Autheniticate with HTTP/FTP server | `wget --user=jake --password=secret ftp://ftp.example.com/file.zip` |
| `--header="<header:value>"` |  Add custom header. | `wget --header=Authorization: Bearer MYTOKEN" https://api.example.com/data` |
| `--no-check-certificate` |  Ignore SSL certificate errors. | `wget --no-check-certificate https://selfsigned.example.com/file.zip` |
| `-r` | Recursive download. | `wget -r https://example.com/files/` |
| `-l <depth>` |  Set recursion depth. | `wget -l 2 https://example.com/` |
| `-np` |  No parent directories. | `wget -np https://example.com/files/` |
| `--accept=PATTERN` |  Accept only certain file types. | `wget --accept=*.pdf https://example.com/` |
| `--reject=PATTERN` |  Reject certain file types. | `wget --reject=*.jpg https://example.com/` |
| `--limit-rate=<rate>` |  Limit download speed. | `wget --limit-rate=200k https://example.com/file.zip` |
| `-W <seconds>` |  Wait between downloads. | `wget --wait=5 https://example.com/files/` |
| `--random-wait` |  Random delay between downloads. | `wget --randowm-wait https://example.com/files/` |
| `-b`| Run in background. | `wget -b https://example.com/bigfile.iso` |

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
| `-O` | Save file with original name. | `curl -o page.html https://example.com` |
| `-L` | Follow redirects. | `curl -L https://short.url/abcd` |
| `-u` | Use username:password authentication. | `curl -u jake:secret https://example.com/private/data.txt` |
| `-C -` | Resume a download. | `curl -C https://example.com/bigfile.iso` |
| `-s` |  Silent (no progress or errors.) | `curl -s https://example.com` |
| `-S` | Show errors even when `-s` is used. | `curl -sS https://example.com` |
| `-v` | Verbose mode. | `curl -v https://example.com/` |
| `-k` |  Ignore SSL certificate validation. | `curl -k https://selfsigned.example.com` |
| `-u  user:pass` |  HTTP Basic authentication. | `curl -u name:secret https://example.com/private/data.txt` |
| `-H "HEADER:VALUE"` |  Add a custom header. | `curl -H "Authorization: Bearer TOKEN" https://api.example.com/data` |
| `--cookie "NAME:VALUE"` | Send cookies. | `curl --cookie "sessionid=abc123" https://example.com/profile` | 
| `--cookie-jar FILE` |  Save cookie to file. | `curl --cookie-jar cookies.txt https://example.com` |
| `--compressed` |  Request compressed response. | `curl --compressed https://example.com` |
| `-X <method>` |  Specify HTTP request method. | `curl -X DELETE https://api.example.com/item/123` |
| `--data-urlencode "<data>"` |  URL-encode data before sending. | `curl --data-urlencode "search=linux commands" https://example.com/search` |
| `--limit-rate <speed>` |  Limit download speed. | `curl --limit-rate 200k -O https://example.com/file.zip` | 
  
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
| `(No arguement)` |  Show all active interfaces. | `ifconfig` |
| `ifconfig -a` |  Show all interfaces. | `ifconfig -a` |
| `ifconfig <iface>` |  Show details of a specific interface. | `ifconfig eth0` |
| `ifconfig <iface> up` |  Enable an interface. | `ifconfig eth0 up` |
| `ifconfig <iface> down` |  Disable an interface. | `ifconfig eth0 down` |
| `ifconfig <iface> <IP>` |  Assign IP address. | `ifcongig eth0 192.168.1.10` |
| `netmask <mask>` |  Set subnet mask. | `ifconfig eth0 192.168.1.50 netmask 255.255.255.0` |
| `broadcast <addr>` |  Set broadcast address. | `ifconfig eth0 broadcast 192.168.1.255` |
| `add <IP>` |  Add a secondary IP. | `ifconfig eth0:0 192.168.1.60` |`
| `hw ether <MAC>` |  Change MAC address. | `ifconfig eth0 hw ether 00:11:22:33:44:55` |
| `mtu <size>` |  Set MTU size. | `ifconfig eth0 mtu 1400` |
| `promisc` |  Enable promiscuous mode. | `ifconfig eth0 promisc` |
| `-promisc` |  Disable promiscuous mode. | `ifconfig eth0 -promisc` |

### Examples

## View all network interfaces

```bash
ifconfig
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `ifconfig` | Network Command |

## Bring up an interface

```bash
ifconfig eth0 up
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `ifconfig` |  Network Command |
| `eth0` |  Selected interface. |
| `up` |  Enable selected interface. |

### Bring down an interface

```bash
ifconfig eth0 down
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `ifconfig` | Network command |
| `eth0` |  Specific network interface to show |
| `down` | Directs to disable the eth0 network |

### Set IP address

```bash
ifconfig eth0 192.168.1.100
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `ifconfig` | Network command |
| `eth0` | Specific network interface |
| `192.168.1.100` | Specific IP address to set to eth0 |

# Command: ip

## Description: The modern replacement for ifconfig

## Syntax

- `ip [OPTIONS] OBJECT { COMMAND | help}`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `addr` | Show/modify IP addresses | `ip addr` |
| `link` | Show/modify interfaces | `ip link set eth0 up or down` |
| `show` | Show specific interface | `ip addr show dev eth0` |
| `add` | Add an IP address | `ip addr add 192.168.1.50/24 dev eth0` |
| `del` | Remove an IP address | `ip addr del 192.168.1.50/24 dev eth0` |
| `route` | Show/modify routing table | `ip route show` |
| `neigh` | Show or modify ARP cache | `ip neigh show` |
| `rule` | Routing policy rules | `ip route show` |
| `monitor` | Watch changes to netlink | `ip monitor all` |
| `help` | Show help | `ip help` |

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

## Syntax

- `task <Filter> <command> [<modification> | <args>]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `--debug` | Show debug output | `task diagnostic` |
| `--verbose` | More detailed output | `task --verbose list` |
| `--quiet` | Suppress output | `task --quiet list` |
| `--force` | Ignore warnings | `task --force list` |
| `rc:<name>=<value>` | Temporarily overside config settings | `task rc.data.location=/tmp/mytasks list` |
| `+<tag>` | Filter: has this tag | `task +home list` |
| `-<tag>` | Filter: does NOT have this tag | `task -home list` |
| `add` | Add a new task | `task add "Finish Library"` |
| `list` | Show pending tasks | `task list` |
| `done` | Mark task as done | `task 23 done` |
| `delete` | Delete task | `task 22 delete` |
| `start` | Mark task as started | `task 10 start` |
| `stop` | Stop task tracking | ` task 11 stop` |
| `mod` | Modify task | `task 15 modify priority: H due:Fri +review` |
| `edit` | Edit task in $editor | `task 33 edit` |
| `annotate` | Add note to task | `task router list` |
| `denotate` | Remove note | `task 42 denotate "name-222"` |
| `project` | Set or view project structure | `task project:work list` |
| `undo` | Revert last change | `task undo` |
| `status` | View summary of tasks | `task status:pending list` |
| `summary` | Project summary report | `task summary` |
| `log` | Show completed tasks | `task log "Rotated VPN keys" end: 2025-01-01 project:Security` |
| `info` | Show full details of a task | `task 11 info` |
| `export` | Export task list in JSON | `task +pending export > pending.json` |
| `import` | Import tasks from JSON | `task import pending.json` |
| `sync` | Sync with taskserver | `task sync` |

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
| `-S <NUM>` | Sets the maximum number of jobs that run simultaneously | `ts -S 4` |
| `-r <ID>` | To remove a job | `ts -r 2` |
| `-s <ID>` | Show status of a job | `ts -s 2` |
| `-n` | No output file, send output to stdout/stderr | `ts -n echo "Hello World"` |
| `-g` | Compress output with gzip (use with -n) | `ts -ng echo "Large output here "` |
| `-f` | Run in foreground, wait until done | `ts -f sleep 5` |
| `-m` | Email results when done | `TS_MAIL_TO="name@example.com" ts -m echo "Job completed"` |
| `-L <label>` | Archive and compress a file | ts -L backup tar -czf backup.tar.gz /home/name` |
| `-K` | Kill Task Spooler | `ts -K` |
| `-C` | Clear finished jobs from list | `ts -C` |
| `-U <id-id>` | Swap positions of two jobs | `ts -U 2-4` |
| `-u` | Move job up in queue | `ts -u 2` |
| `-w <ID> | Wait for job to finish | `ts -w 2` |
| `-o <ID> | Show output file path | `ts -o 2` |
| `-p <ID> | Show PID of job | `ts -p 2` |
| `-c <ID> | Show full job output | `ts -c 2` |
| `-t <ID> | Tail last 10 lines of job output | `ts -t 2` |
| `-l` | List jobs | `ts -l` |
| `-N <NUM>` | Requires <NUM> free slots to run | `ts -N 2 echo "Free Slots"` |
| `-E` | Separate stdout and stderr files | `ts -E bash -c "echo 'out' ; echo 'err' ?&2"` |
| `-B` | Do not block when queue is full | `ts -B echo "Non-blocking job"` |
| `-D <ID>` | Run only if specific job ID succeeded | `ts echo "Step 1" / ts -D 1 echo "Step 2"` |
| `-d` | Run only if last job succeeded | `ts -d echo "Step 2"` |

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

# Command: systemd-analyze

## Description: Diagnose boot performance

## Syntax

- `systemd-analyze [OPTIONS] COMMAND [COMMAND OPTIONS]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `time` | Overall boot Breakdown | `systemd-analyze time` |
| `blame` | Slowest units first | `systemd-analyze blame` |
| `critical-chain` | Why startup was slow | `systemd-analyze critical-chain` |
| `plot` | Boot timeline SVG | `systemd-analyze plot > boot.svg` |
| `dot` | Dependency Graph | `systemd-analyze dot | dot -Tsvg > deps.svg` |
| `verify` | verify unit files | `systemd-analyze verify /etc/systemd/system/myapp.service` |
| `dump` | Dump Manager State | `systemd-analyze dump | less` |
| `security` | Security posture for all services | `systemd-analyze security | less` |


### Example

```bash
systemd-analyze blame
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `systemd-analyze` | Network Command |
| `blame` | Shows slowest unit first |

# Command: lazydocker

## Description:  TUI for Docker management

## Syntax

- `lazydocker`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `--debug` | Log internal debug into for troubleshooting | `lazydocker --debug` |
| `--config` | Loads a custom config file instead of default one | `lazydocker --config ~/.config/lazydocker/custom-config.yml` |
| `f` | Points to a different docker compose file | `lazydocker -f ./docker-compose.dev.yml` |
| `-p` | Override the Project Name | `lazydocker -p myproject` |
| `--help` | Prints the built in help text | `lazydocker --help` |
| `--version` | Displays the current version | `lazydocker --version` |

### Example

### View running containers, images, logs, and volumes

```bash
lazydocker
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `lazydocker` | Opens the TUI for managin Docker |

# Command: fabric

## Description: Python-based remote shell & deployment tool

## Syntax

- `fab [task]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `deploy` | Deploys task | `fab deploy` |
| `cleanup` | Cleanups tasks | `fab cleanup` |
| `-H` | Specifies a host | `fab -H server1, server2 restart_service` |
| `-i` | Overrides the SSH key, and uses a targeted authentication | `fab -H prod.server.com -i ~/.ssh/prod_key deploy` |
| `--prompt-for-passphrase` | Prompts user to enter password | fab -H host1 --prompt-for-login-password deploy` |
| `--list` | lists all the defined tasks | `fab --list` |
| `-R` | Dry run, just echos with no execution | `fab -H host1 -R test_deploy` |
| `-P` | Run tasks in parallel | `fab -H host1, host2 -P backup_db` |
| `-f` | Instructs to fun custom fab.py files instead of default ones | `fab -f custom_fabfile.py deploy` |
| `--connect-timeout, --command-timeout` | Sets timeouts | `fab -H host1 --connect-timeout=10 --command-timeout=30 deploy` |

### Examples

### Specify a host

```bash
fab -H server1, server2 restart_service
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `fab` | Fabric command |
| `-H` | Directs to specify a host |
| `server1` | the original server1 |
| `server2` | the specified location for server1 |
| `restart_service` | restarting server service |

# Command: asciinema

## Description: Record and share terminal sessions. Perfect for: creating tutorials, logging incident response steps, or leaving a trail for blue teams or audits

## Syntax

- `asciinema rec [filename]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
|  `-c` | Records a specific command | `asciinema -c "htop" htop-demo.cast` |
| `-i` | Compresses long idle time so viewers do not snooze | `asciinema -i 5 quick-demo.cast` |
| `rec <filename>` | Record a session | `asciinema rec demo.cast` |
| `--stdin` | Records your keystrokes along with terminal output | `asciinema rec --stdin with-keystrokes.cast` |
| `--append` | Adds to existing file | `asciinema rec --append session.cast` |
| `--overwrite` | Overwrites the existing file | `asciinema rec --overwrite session.cast` |
| `-t` | Adds a descriptive title when uploading | `asciinema rec -t "Linux Firewall Setup" Firewall.cast` |
| `-q` | Suppresses non-essential messages | `asciinema rec -q silent.cast` |
| `-y` | Automatically answers yes to prompts | `asciinema rec -y auto.cast` |
| `play` | Plays a recording | `asciinema play demo.cast` |
| `-s` | Allows you to change the playback speed | `asciinema play -s 1.5 demo.cast` |
| `cat` | Dumps the recorded session output to your terminal without timing | `asciinema cat demo.cast` |
| `upload` | pushes file to asciinema.org | `asciinema upload demo.cast` |
| `auth` | Links local client to online account for uploads and management | `asciinema auth` |

### Examples

### Start a recording

```bash
asciinema rec install_hardened_linux.cast
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `asciinema` | Recording manager command |
| `rec` | Directs to start recording |
| `install_hardened_linux.cast` | name of file |

# Command: netstat

## Description: Displays network connections, routing tables, and interface stats. (Legacy—ss replaces it in modern systems)

## Syntax

- `netstat [OPTIONS]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-a` | Show all sockets | `netstat -a` |
| `-t` | Show TCP connections only | `netstat -t` |
| `-u` | Show UDP connections only | `netstat -u` |
| `-l` | Show listening sockets only | `netstat -l` |
| `-p` | Show the PID and program name of each connection | `sudo netstat -p` |
| `-n` | Show address numerically | `netstat -n` |
| `-r` | Show the routing table | `netstat -r` |
| `-i` | Show network interfaces | `netstat -i` |
| `-s` | Show per-protocol statistics | `netstat -s` |
| `-c` | Continuous output | `netstat -c` |
| `-e` | Show extended information | `netstat -e` |
| `-g` | Show multicast group membership | `netstat -g` |
| `-o` | Show timers for connections | `netstat -o` |

### Examples

### Show all connections

```bash
netstat -a
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `netstat` | Network command|
| `-a` | Show all networks |

### Show only listening ports

```bash
netstat -l
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `netstat` | Network command |
| `-l` | Show listening ports only |

### Show TCP connections

```bash
netstat -t
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `netstat` | Network Command |
| `-t` | Show TCP connections only |

### Show process names

```bash
netstat -tulpn
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `netstate` | Network Command |
| `-t` | Show TCP connections |
| `-u` | Show UDP connections |
| `-l` | Show listening ports |
| `-p` | Show the PID and Program name |
| `-n` | Show addresses numberically |

# Command: ss

## Description: A faster, more modern replacement for netstat

## Syntax

- `ss [OPTIONS] [FILTER]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-t` | Show TCP sockets only | `ss -t` |
| `-u` | Show UDP sockets only | `ss -u` |
| `-l` | Show listening sockets only | `ss -l` |
| `-a` | Show all sockets | `ss -a` |
| `-n` | Do not resolve service names or hostnames | `ss -n` |
| `-p` | Show PID and process using the socket | `ss -p` |
| `-4/-6` | Show only IPv4 or IPv6 sockets | `ss -4 or ss -6` |
| `-r` | Resolve service names | `ss -r` |
| `-o` | Show timer information | `ss -o` |
| `-s` | Show summary statistics | `ss-s` |
| `-i` | Show internal TCP info | `ss -ti` |
| `-m` | Show memory usage for sockets | `ss -m` |
| `-K` | Kill a socket | `ss -K dst 192.168.1.100 dport = 22` |
| `-f` | Specify socket family | `ss -f inet` |
| `-H` | No header line in output | `ss -H -t` |

### Examples

### Show all TCP connections

```bash
ss -t
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `ss` | Network Command |
| `-t` | Show TCP connections |

### Show listening sockets

```bash
ss -l
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `ss` | Network command |
| `-l` | Show listening sockets |

### Show processes using sockets

```bash
ss -tunap
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `ss` | Network Command |
| `-t` | Show TCP connections |
| `-u` | Show UDP connections |
| `-n` | Do not resolve service names or hostnames |
| `-a` | Show all sockets |
| `-p` | Show PID and program names |

# Command: rsync

## Description: Efficiently syncs files/directories between locations

## Syntax

- `rsync [OPTIONS] SOURCE DEST`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-v` | Verbose mode | `rsync -v file.txt /backup/` |
| `-a` | Archive mode | `rsync -a /home/name/ /backup/name/` |
| `-r` | Copy directories recursively | `rsync -r doc/ /backup/docs/` |
| `-l` | Copy symlinks as symlinks | `rsync -l source/ target/` |
| `-p` | Preserve permissions | `rsync -p file.txt /backup/ |
| `-t` | Preserve modification times | `rsync -t file.txt /backup/` |
| `-g` | Preserve group ownership | `rsync -g file.txt /backup/` |
| `-o` | Preserve owner | `rsync -o file.txt /backup/` |
| `-D` | Preserve device files and special files | `rsync -aD /dev/ /backup/dev/` |
| `-u` | Skip files new on the destination | `rsync -u /src/ /dest/` |
| `-n` | Show what would be done, without doing it | `rsync -an /src/ /dest/` |
| `-z` | Compress file data during transfer | `rsync -az /src/ remote:/dest/` |
| `-P` | Show progress and keep partially transferred files | `rsync -aP big-iso /backup/` |
| `--progress` | Show progress during transfer | `rsync --progress file.txt /backup/` |
| `--partial` | Keep partially transferre*d files | `rsync --partial bigfile /backup/` |
| `--rsync-path=PATH` | Specify remote rsync path | `rsync -a --rsync-path="/usr/local/bin/rsync" /src/ remote:/dest/` |
| `--chown=USER:GROUP` | Change ownership on transferred files | `rsync -a --chown=root:root /src/ /dest/` |
| `--chmod=CHMOD` | Change permissions on transferred files | `rsync -a --chmod=755 /src/script.sh /dest/` |
| `--size-only` | Skip files matching in size, ignore timestamp | `rsync -a --size-only /src/ /dest/` |
| `--ignore-existing` | skip updating existing files | `rsync -a --ignore-existing /src/ /dest` |
| `--remove-source-files` | Delete source files after successful transfer | `rsync -a --remove-source-files /src/ /dest/` |
| `--delete` | Delete extraneous files from the destination | `rsync -a --delete /src/ /dest/` |
| `--exclude=PATTERN` | Exclude certain files | `rsync -a --exclude="*.tmp" /src/ /dest/` |
| `--exclude-from=FILE` | Read exclude patterns from file | `rsync -a --exclude-from=exclude.txt /src/ /dest/` |
| `--include=PATTERN` | Force inclusion of specific files | `rsynce -a --include="*.jpg" --exclude="*" /src/ /dest/` |
| `--bwlimit=KBPS` | limit bandwidth usage | `rsync -a --bwlimit=500 /src/ /dest/` |
| `--checksum` | Skip files with same checksum | `rsync -a --checksum /src/ /dest/` |
| `--append` | Append data to partially transferred files | `rsync --append bigfile /backup/` |
| `--apend-verify` | Append and verify checksum | `rsync --append-verify bigfile /backup/` |

### Examples

### Sync two directories

```bash
rsync -av /home/name/ /mnt/backup/
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `rsync` | Network Commdand |
| `-a` | Archive mode |
| `-v` | Verbose mode |
| `/home/name/` | Source location |
| `/mnt/backup/` | Target location |

### Sync over SSH

```bash
rsync -avz /home/name user@server:/backup/
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `rsync` | Network Command |
| `-a` | Archive mode |
| `-v` | Verbose mode |
| `-z` | Compress files during transfer |
| `/home/name/` | Source lcoation |
| `user@server:/backup/` | Destination location |

### Mirror source to destination (delete extras)

```bash
rsync -av --delete /source/ /dest/
```

### Breakdown

| Breakdown | Destination |
|-----------|-------------|
| `rsync` | Network Command |
| `-a` | Archive mode |
| `-v` | Verbose mode |
| `--delete` | Directs to delete extra files at destination |
| `/source/` | source location |
| `/dest/` | Destination Location |

# Command: ftp

## Description: Connect to an FTP server and transfer files

## Syntax

- `ftp [OPTIONS] HOSTNAME`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-p` | Eable passive mode | `ftp -p ftp.example.com` |
| `-i` | Turns off interactive prompting when using multiple file transfers | `ftp -i ftp.example.com` |
| `-n` | Do not auto-login when connecting | `ftp -n ftp.example.com` |
| `-g` | Disables filename globbing | `ftp -g ftp.example.com` |
| `-v` | Enable verbose mode | `ftp -v ftp.example.com` |
| `-d` | Enable debugging messages | `ftp -d ftp.example.com` |
| `-u user[,pass]` | Specify username and optional password on the command line | `ftp -u name, password ftp.example.com` |

### Examples

### Connect to an FTP server

```bash
ftp ftp.example.com
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `ftp` | file transfer protocol command |
| `ftp.example.com` | target server |

# Command: mtr

## Description: Combines traceroute + ping into real-time network map

## Syntax

- `mtr [options] [host]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-4` | Forces IPv4 | `mtr -4 google.com` |
| `-6` | Forces IPv6 | `mtr -6 google.com` |
| `-r` | Report mode | `mtr -r google.com` |
| `-c` | counts number of cycles to run | `mtr -r -c 10 google.com` |
| `-n` | Say to not resolve hostnames | `mtr -n google.com` |
| `-b` | Show both hostname and IP addresses | `mtr -b google.com` |
| `-a` | Binds to a specific source address | `mtr -a 192.168.1.100 google.com` |
| `-f` | Set the first TTL hop to probe | `mtr -f 5 google.com` |
| `-m` | Set the maximum TTL | `mtr -m 15 google.com` |
| `-p` | Displays the actual packet path | `mtr -p google.com` |
| `-z` | Shows ASN info | `mtr -z google.com` |
| `-i` | Time between pings | `mtr -i 2 google.com` |
| `-w` | Wide report format | `mtr -w google.com` |
| `-t` | Enable TCP mode | `mtr -t google.com` |
| `-u` | Use UDP mode | `mtr -u google.com` |
| `--json` | Output results in JSON format | `mtr --JSON google.com` |

### Examples

### Show both hostname and IP addresses

```bash
mtr -b google.com
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `mtr` | Network Command |
| `-b` | Directs to show both hostname and IP address |
| `google.com` | Target site |

# Command: mosh

## Description: Mobile Shell (better ssh for flaky networks)

## Syntax

- `mosh [Options] [--] [user@host] [Command]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-p` or `--port=PORT:PORT2` | Specifies UDP port | `mosh -p 60000 user@server.example.com` |
| `--ssh=SSH-COMMAND` | Connects via SSH on port 2222 | `mosh --ssh"ssh -p 2222 -i ~/ssh/id_rsa" user@server.example.com` |
| `-4` or `--family=inet` | Forces IPv4 | `mosh -4 user@server.example.com` |
| `-6` or `--family=inet6` | Forces IPv6 | `mosh -6 user@server.example.com` |
| `--predict=adaptive/always/never` | Controls predictive echo | `mosh --predict=always user@server.example.com` |
| `--no-init` | Disables terminal initialization on startup | `mosh --no-init user@server.example.com` |
| `--local` | Forces Mosh to run in local-only mode | `mosh --local` |
| `--help` | Shows help menu | `mosh --help` |
| `--version | Shows working version | `mosh --version` |

### Example

### connecting using a specific port

```bash
mosh -p 60000:60010 \
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `mosh` | special shell command |
| `-p` | Specifies a specific port to use |
| `60000:60010` | Specified ports |

# Command: dog

## Description: Modern replacement for dig (DNS queries)

## Syntax

-`dog [ query Options] [Domain]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-q` or `--query=HOST` | Domain to query | `dog -q example.com` |
| `-t` or `--type=TYPE` | specify the DNS record type | `dog -q example.com -t MX` |
| `-n` or `--nameserver=ADDR` | Query a specific nameserver | `dog -q example.com -t A -n 8.8.8.8` |
| `--class=CLASS` | Sets DNS class | `dog -q example.com --class=IN` |

### Example

```bash
dog -q example.com
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `dog` | Network command |
| `-q` | Directs to query a domain |
| `example.com` | domain to query |

# Command: termshark

## Description: Wireshark in your terminal

## Syntax

- `termshark [Options] [<capture filter>]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `r <file>` | Read and analyze a file offline | `termshark -r sample.pcap` |
| `-i` | Capture live traffic from the specified interface | `sudo termshark -i wlan0` |
| `D` | Dump a list of available network interfaces and exit | `termshark -D` |
| `-f` | Apply a BPF-style filter during capture | `termshark -i eth0 -f "port 53"` |
| `-Y` | Apply a Wireshark-style display filter | `termshark -r sample.pcap -Y "tcp.port == 8080"` |
| `-P` | Only packets addressed to your host are captured | `termshark -p` |
| `-s <snaplen>` | Set the snapshot length | `termshark -s 128` |
| `-l` | Launch directly into live capture mode | `termshark -l` |

### Example

```bash
- sudo termshark -i eth0
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Temporary superuser command |
| `termshark` | Activates termshark |
| `-i` | Captures live  traffic from specified interface |
| `eth0` | Specified interface |

# Command: lsof

## Description: List network connections and the programs using them. Stands for "list open files"

## Syntax

- `lsof [Options] [names]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-u <users>` | Shows files opened by a specific user | `lsof -u  username` |
| `-p <PID>` | Shows files opened by a specific user | `lsof -p 1234` |
| `-i` | Show network connections | `lsof -i` |
| `-i <port> | show processes using a specific port | `lsof -i :80` |
| `-i tcp/-i udp` | filter bhy protocol | `lsof -i tcp` |
| `-i @<ip>` | Filter by host/IP | `lsof -i username@192.168.1.20` |
| `-c <string>` | Show processes whose command starts with string | `lsof -c ssh` |
| `-a` | Combine multiple filters | `lsof -i tcp -a -u username` |
| `-P` | Dont resolve port numbers to service names | `lsof -P -i` |
| `-n` | Do not resolve hostnames | `lsof -t -i :22` |
| `-t` | Output only process IDs | `lsof -t -i :443` |
| `+d <dir>` | List files opened in a specific directory | `sudo lsof +d /etc` |
| `+D <dir>` | Recursively list files opened under a directory | `sudo lsof +D /var/log` |

### Examples

### Who’s using SSH

```bash
sudo lsof -i :22            
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Temporary superuser command |
| `lsof` | List open files command |
| `-i :22` | Directs to list processes using port 22 |

### Filter by host and IP address

```bash
lsof -i @192.168.1.10
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `lsof` | List open files command |
| `-i @192.168.1.10` | Filter by host/IP |

# Command: ipcalc

## Description: IP calculator for CIDR, subnetting, broadcast, etc

## Syntax

- `ipcalc [ip-address/cidr]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-c` | Validate if the IP is legit | `ipcalc -c 192.16.1.256` |
| `-i` | Show readable network info | `ipcalc -i 192.168.1.10/24` |
| `--all-info` | Verbose human-readable output | `ipcalc --all-info 193.92.15.2/24` |
| `-S` | Cut a network into smaller chunks using specified prefixes | `ipcalc -S 26 192.168.1.23` |
| `-d` | Split a range into covering networks | `ipcalc -d 192.168.1.3-192.168.1.23` |
| `-r` | Create a random private IP given mask | `ipcalc -r \24` |
| `-h` | Give me the possible hostname for that IP | `ipcalc --hostname 8.8.8.8` |
| `-j` | Output results as JSON | `ipcalc -j --all-info 192.168.1.10/24` |
| `--no-decorate` | Raw output with no fluff | ipcalc -S 26 192.168.1.0/24` |
| `--addrspace` | Info about address space category | `ipcalc --addrspace 192.168.1.0/24` |
| `-p` | Show the CIDR prefix | `ipcalc --prefix 192.168.1.10 255.255.255.0` |
| `--class-prefix` | Use classful defaults for netmask | `ipcalc --class-prefix 10.0.0.1` |\
| `-n` | Just show the network address | `ipcalc --network 192.168.1.10/24` |
| `--addresses` | Show number of hosts | `ipcalc --addresses 192.168.1.0/24` |
| `--minaddr` | Lowest usable host IP in the network | `ipcalc --minaddr 192.168.1.0/24` |
| `--maxaddr` | Highest usable host IP | `ipcalc --maxaddr 192.168.1.0/24` |

### Example

### Validate if the IP is legit

```bash
ipcalc -c 192.168.1.5/24
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `ipcalc` | Network Command |
| `-c` | Directs to validate IP |
| `192.168.1.5/24` | IP address

# Command: wormhole

## Description: Encrypted file transfer between systems. Must be installed on both systems. No server required

## Syntax

- `wormhole [OPTIONS] COMMAND [ARGUEMENT]`

### Options

| Options | Description | Examples |
|---------|-------------|----------|
| `send[f or d]` | Kicks off a transfer, spits out a code | `wormhole send backup` |
| `receive` | Waits for someone to punch in that code | `wormhole receive` |

### Example

```bash
wormhole send secrets.tar.gz
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `wormhole` | File transfer command |
| `send` | Directs to kick off the transfer |
| `secret.tar.gz` | file to be transferred |
