# System Information and Monitoring Management

## Description:

## Table of Contents

- `uname`
- `uptime`
- `blkid`
- `file`
- `free`
- `df`
- `du`
- `dmesg`
- `findmnt`
- `fsck`
- `lsblk`
- `lscpu`
- `mount`
- `umount`
- `iostat`
- `vmstat`
- `dstat`
- `w`
- `who`
- `watch`
- `progress`

# Command: uname

## Description: Shows system information (kernel, architecture, etc.)

## Synatax

- `uname [OPTIONS]`

## Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-s` | Prints the kernel name | `uname -s`|
| `-n` | Prints the node name | `uname-n` |
| `-r` | Prints the kernel version | `uname -v` |
| `-m` | Prints the. machine hardware name | `uname -m` |
| `-p` | Prints the processor type | `uname -p` |
| `-i` | Prints the hardware platform | `uname -i` |
| `-o` | Prints the operating system | `uname -o` |
| `-a` | Prints all available system information | `uname -a` |

## Examples

## Show kernel name

```bash
uname 
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `uname` | Monitoring command |

## Show all system details

```bash
uname -a
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `uname` | Monitoring command |
| `-a` | Directs to display all system information |

# Command: uptime

## Description: Displays how long the system has been running, how many users are logged in, and system load averages. It is used hy sysadmins to check system stability and performance trends

## Syntax

- `uptime`

## Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `(none)` | Default output of current time, uptime, users, load averages | `uptime` |
| `-p` | Shows output in human friendly form | `uptime -p` |
| `-s` | Shows wxact time system was booted | `uptime -s` |

## Examples

## Show uptime and load averages

```bash
uptime
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `uptime` | Monitoring command |

# Command: blkid

## Description: Is used to locate and print block device attributes. It is used to find UUIDs, filesystem types, labels, and other metadata of partition of drives

## Syntax

- `blkid [Options] [Device..]`

## Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-c <cachefile>` | Specify a cache file for device attributes | `blkid -c /dev/null` |
| `-o <format>` | Set output format (Full, value, list, and udev) | `blkid -o list` |
| `-s <tag0>` | Show only a specific attribute | `blkid -s UUID /dev/sda1` |
| `-t <token>` | Search for devices that match a specific attribute | `blkid -t TYPE=ext4` |
| `-L <label>` | Search for a partition by filesystem | `blkid -L mydata` |
| `-U <UUID>` | Search for a partition by UUID | `blkid -U <number>` |
| `-g` | Garbage collect the blkid cache file | `sudo blkid -g` |
| `-k` | list all known filesystem and partition types `blkid` can recognize | `blkid -k` |
| `-i` | Display I/O limits | `blkid -i /dev/sda` |
| `-p` | probe a device directly, even if not in cache | `sudo blkid -p /dev/sdb1` |
| `-w <cachefile>` | Write results to a custom cache file instead of default | `blkid -w /tmp/myblkid.tab` |

## Examples

## Find which device has the label `backup`

```bash
blkid -L backup
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `blkid` | System command |
| `-L` | Directs to find a device with a specific label |
| `backup` | Specified Label |

# Command: file

## Description: Used to identify the type of a file by examining its contents rather than just relying on its extension

## Syntax

- `file [Options] file...`

## Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-b` | Do not show the filename in output | `file -b /bin/ls` |
| `-i` | Pring the MIME type instead of descriptive text | `file -i picture.jpg` |
| `-e <test>` | Excludes certain tests | `file -e compress archive.gz` |
| `-f <namefile>` | Read filenames to examine from a file | `file -f filelist.txt` |
| `-F <separator>` | Use a custom separator instead of `:` after filenames | `file -F " -> " /bin/ls` |
| `-h` | Do not follow symlink | `file -h symlink_to_file` |
| `-k` | Keep going after the first match | `file -k script.sh` |
| `-Z` | Output SELinux security context | `file -Z /bin/ls` |
| `-z` | Try to look inside compressed file | `file -z archive.gz` |
| `-s` | Read block/character devices | `sudo file -s /dev/sda` |

## Examples

## Quickly check file type without filename

```bash
file -b document.pdf`
```

### Breakdown

| Breakdown | Description | 
|-----------|-------------|
| `file` | Monitoring command |
| `-b` | Directs to not show filename in output |
| `document.pdf` | Specified file |

# Command: free

## Description: Shows RAM and swap usage

## Syntax

- `free [OPTIONS]`

## Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-b`,`-k`,`-m`,`-g` | Displays in the selected byte size | `free -m` |
| `-h` | Human readablw format | `free -h` |
| `--kilo`,`--mega`,`--giga`,`--tera` | Forces specified units | `free --mega` |
| `--si` | Use powers of 1000 instead of 1024 | `free -si` |
| `-t` | Shows totals | `free -t` |
| `-l` | Show low and high memory statistics | `free -l` |
| `-c<count>` | Repeat output NUM times | `free -c 5` |
| `-s<seconds>` | Update output continuously every specified seconds | `free -s 4` |
| `--wide` | Wider output to avoid column truncation | `free --wide` |

## Examples

## Show memory in MB

```bash
free -m
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `free` | Monitoring command |
| `-m` | Directs to show memory in MB |

### Human-readable format

```bash
free -h
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `free` | Monitoring Command |
| `-h` | Directs to output in human-readable format |

# Command: df

## Description: Shows disk usage of file systems

## Syntax

- `df [OPTIONS] [FILESYSTEM]`

## Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-h` | Human-readable sizes | `df -h` |
| `-i` | Inodes instead of blocks | `df -i` |
| `-a` | All file systems | `df -a` |
| `-k`,`-m`,`-BG`,`-B` | Block size control | `df -k` |
| `-p` | POSIX compliance | `df -p` |
| `-l` | Local file system only | `df -l` |
| `-t <file>` | File system type filter | `df -t ext4` |
| `--total` | Grand total | `df --total` |

## Examples

## Show disk usage in human-readable format

```bash
df -h
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `df` | System command |
| `-h` | Directs to show output in human-readable format |

## Show filesystem types

```bash
df -T
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `df` | System command |
| `-T` | Directs to show filesystem types |

# Command: du

## Description: Stands for Disk Usage. It used yo estimate and display the amount of disk space

## Syntax
- `du [Options] [file...]`

## Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-a` | Displays sizes of all files and directories | `du -a /home/name` |
| `-h` | Prints sizes in human-friendly units (K,M,G) | `du -h /var/log` |
| `-s` | Shows only the total size for each argument | `du -sh /home/name` |
| `-c` | Produces a grand total wt the end | `du -ch /etc` |
| `-d <Num>` | Limut recursion to NUM levels deep | `du -h -d 1 /home/name` |
| `--max-depth=N` | Same as `-d N` | `du -h --max-depth=2 /var` |
| `-x` | Skips directories on different filesystems | `du -xh /` |
| `--apparent-size` | Report the actual size instead of disk blocks | `du --apparent-size -h bigfile` |
| `-k,m` | Forces sizes to be in kilobytes or megabytes | `du -k /usr` |
| `-B <SIZE>` | Show sizes in specific block size | `du -B M /home/name` |
| `--time` | Show the last modification time of each f/d | `du --time -h /var/log` |
| `--exclude=PATTERN` | Exclude matching files | `du -h --exclude="*.log" /var/log` |
| `--inodes` | List inodes usage instead of block sizes | `du --inodes /home` |

## Examples

## Find the file size of home directory

```bash
du -sh ~
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `du` | System command |
| `-sh` | Shows only in human readable form and only displays the total size of specified f/d |
| `~` | Spwcified location |

## Check a specific file's disk usage

```bash
du -h /var/log/syslog
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `du` | System command |
| `-h` | Prints sizes in himan readable form |
| `/var/log/syslog` | Specified location |

# Command: dmesg

## Description: Stands for diagnostic message. Prints kernel ring buffer messages (boot logs, driver info). A key tool for troubleshooting hardware, drivers, networking, and system startup issues

## Syntax

- `dmesg [OPTIONS]`

## Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-C` | Clear the kernel ring buffer | `sudo dmesg -C` |
| `-c` | Print then clear the ring buffer | `sudo dmesg -c` |
| `-D` | Disables printing message to the console | `sudo dmesg -D` |
| `-E` | Re-enable messages to the console | `sudo dmesg -E` |
| `-d` | Shows only messages added since the last `dmesg` | `dmesg -e` |
| `-e` | Interpret the timesyamps onyo human readable formats | `dmesg -e` |
| `-H` | Human-readable output | `dmesg -H` |
| `-k` | Print only kernel messages | `dmesg -k` |

## Examples

## Show boot logs

```bash
dmesg | less
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `dmesg` | Monitoring command |
| `less | Output is piped through `less` to show only one page at a time |

### Show with timestamps

```bash
dmesg -T
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `dmesg` | Monitoring command |
| `-T` | Directs to print human readable timestamps |

# Command: findmnt

## Description: Displays a tree of mounted file systems, finds a particular mount point/device. Its the modern way to query mount information

## Syntax

- `findmnt [Options] [Device] [Mountpoint]`

## Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `(default)` | findmnt | `findmnt` |
| `-l` | List view | `findmnt -l` |
| `-t` | Specfiy file system type | `findmnt -t ext4` |
| `-x` | Exclude a type | `findmnt -x tmpfs` |
| `-o` | Output format | `findmnt -o ...` |
| `-J` | JSON or fstab-style | `findmnt -J` |
| `-r` | Mounted vs not yet mounted | `findmnt -r` |
| `-m` | Show only mounted file systems | `findmnt -m` |
| `-p` | Poll for changes | `findmnt -p` |
| `-s` | Shows `fstab`- style format | `findmnt -s` |
## Examples

## Print mount info to JSON for auditing

```bash
findmnt -s
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `findmnt` | Monitoring command |
| `-s` | Directs to show output in `fstab` format |

# Command: fsck

## Description: It stands for `File System Consistency Check`. It checks and optionally repairs inconsistencies in file systems. Never run `fsck` on a mounted, active file system. Boot from a rescue/live system, or remount read-only if you need to check it safely

## Syntax

- `fsck [Options] [Filesystem...]`

## Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-A` | Check all file systems | `fsck -A` |
| `-y` | Automatic repair | `fsck -y /dev/sda1` |
| `-r` | Interactive mode | `fsck -r /dev/sda1` |
| `-f` | Force a check | `fsck -f /dev/sda1` |
| `-v` | Verbose output | `fsck -v /dev/sda1` |
| `-C` | Check root partition on boot | `fsck -C -y /` |
| `-t` | Specify file system type | `fsck -t ext4 /dev/sda1` |
| `-N` | No action taken, check only | `fsck -N /dev/sda1` |
| `-M` | Skip mounted partitions | `fsck -M -A` |

## Examples

## Auto-check all fstab entries at boot safely

```bash
fsck -AR -y
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `fsck` | Monitoring command |
| `-A` | Directs to check all files from `/etc/fstab` |
| `-R` | Directs to skip root file system |
| `-y` | Directs to fix corrupted files automatically |

# Command: lsblk

## Description: Lists block devices (disks, partitions, etc.). It pulls info from `/sys`. It shows devices in tree form

## Syntax

- `lsblk [OPTIONS] [Device...]`

## Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-h` | Human-readable sizes | `lsblk -h` |
| `-a` | List all devices | `lsblk -a` |
| `-f` | Prints file system info | `lsblk -f` | 
| `-o` | Output all details | `lsblk -o <column details>` |
| `-l` | Output in list form | `lsblk -l` |
| `-n` | Show kernel major:minor numbers | `lsblk -n` |
| `-p` | Prints device path instead of names | `lsblk -p` |
| `-t` | Show topology information | `lsblk -t` |
| `-r` | Show dependencies | `lsblk -r` |
| `-J` | JSON or tree output | `lsblk -J` |
| `-d` | Filter by device type | `lsblk -d` |

## Examples

## Show block devices tree

```bash
lsblk
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `lsblk` | System command |

### Show with filesystem info

```bash
lsblk -f
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `lsblk` | System command |
| `-f` | Directs to show filesystem information |

# Command: lscpu

## Description: Displays detailed CPU architecture info. It pulls from `/proc/cpuinfo`. Used for hardware inventory, performance tuning, and security checks

## Syntax

- `lscpu [Options]`

## Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `(Default)` | Dumps everything in a readable key | `lscpu` |
| `-J` | JSON output | `lscpu -J` |
| `-e=<Column headings>` | Ouput specific columns | `lscpu -e=CPU,CORE,SOCKET,NODE` |
| `-e=ALL` | Prints all available columns | `lscpu -e=ALL` |
| `-p` | Specify output format | `lscpu -p` |
| `-e=CPU,ONLINE` | Shows which logical CPUs are online vs offline | `lscpu -e=CPU,ONLINE` |
| `--extended=CPU,SOCKET,NODE,ONLINE` | Shows CPU hotplug states | `lscpu --extended=CPU,SOCKET,NODe, ONLINE` |

## Examples

## Display CPU architecture information

```bash
lscpu
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `lscpu` | System command |

## Show CPU details

```bash
lscpu
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `lscpu` | system command |

# Command: mount

## Description: Attaches a filesystem to the system's directory tree. Once mounted, contents of device appear at the specified mount point

## Syntax

- `mount [Options] DEVICE DIR`

## Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `(default)` | View mounted file systems | `mount` |
| `-t <filetype>` | Specify filesystem type | `sudo mount -t ext4 /dev/sda1 /mnt/data` |
| `-o ro` | Mount read-only | `sudo mount -o ro /dev/sda1 /mnt/usb` |
| `--make-private` | Make mount private | `sudo mount --make-private /mnt/usb` |
| `--make-shared` | Make mount shared | `sudo mount --make-shared /mnt/usb` |
| `--move` | Move a mount point | `sudo mount --move /mnt/usb /media/usb` |
| `--bind` | Bind mount | `sudo mount --bind /var/www /mnt/www` |

## Examples

## Mount USB read-only for forensic analysis

```bash
sudo mount -o ro,noload /dev/sdb1 /mnt/usb
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Superuser command |
| `mount` | System command |
| `-o ro` | Directs to mount with read-only permissions |
| `/dev/sdb1` | Specified file |
| `/mnt/usb` | Targeted file |

# Command: umount

## Description: This command is used to unmount a filesystem from the directory tree

## Syntax

- `umount [options] <target>`

## Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-a` | Unmount all mounted filesystems mentioned in `/etc/mtab` | `umount -a` |
| `-r`, `--read-only` | If unmounted fails, remount the filesystem read-only | `umount -r /mnt/data` |
| `-f`,`--force` | Force unmount | `umount -f /mnt/nfs` |
| `-f`,`--lazy` | Lazy unmount | `unmount -l /mnt/usb` |
| `-d` | `When unmounting a loop device, also free the loop device | `umount -d /mnt/loop` |
| `--types<type>`,`-t<type>` | Unmount only filesystems of the given type | `umount -a -t nfs` |
| `--fake`, `-n` | Fake unmount | `umount --fake /mnt/test` |

## Examples

## Unmount USB drive by mount point

```bash
umount /mnt/usb
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `umount` | System command |
| `/mnt/usb` | Specified file to unmount |

# Command: iostat

## Description: Shows CPU and disk I/O statistics. (Requires sysstat package)

## Syntax

- `iostat [OPTIONS] [INTERVAL [COUNT]]`

## Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-c` | Show CPU stats only | `iostat -c 2 5` |
| `-d` | Show device stats only | `iostat -d` |
| `-x` | Show extended stats | `iostat -x 1 3` |
| `-h` | Show human-readable units | `iostat -h -d` |
| `-k` | Report in KB/sec | `iostat -d -k` |
| `-m` | Report in MB/sec | `iostat -d -m` |
| `-t` | Prints timestamp with each line | `iostat -t 2` |

## Examples

## Show CPU and disk stats

```bash
iostat
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `iostat` | System command |

### Show only CPU stats

```bash
iostat -c
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `iostat` | System command |
| `-c` | Directs to show CPU utilization only |

# Command: vmstat

## Description: Reports virtual memory, CPU activity, I/O stats

## Syntax

- `vmstat [OPTIONS] [DELAY [COUNT]]`

## Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-a` | Show memory in active/inactive pages instead of just free/buffer/cache | `vmstat -a 2 5` |
| `-s` | Display a table of memory-related event counters | `vmstat -s` |
| `-d` | Show disk statistics | `vmstat -d` |
| `-D` | Show disk summary statistics | `vmstat -D` |
| `-p<partition>` | Show detailed stats for a specific partition | `vmstat -p sda1` |
| `-f` | Show number of forks since boot | `vmstat -f` |
| `-m` | Display `slabinfo` (kernel memory caches) | `vmstat -m` |
| `-t` | Show timestamp with each line | `vmstat -t 1 5` |
| `-w` | Wide output | `vmstat -w` |
| `-V` | Show version and exit | `vmstat -V` |

## Examples

## One-shot report

```bash
vmstat
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `vmstat` | Monitoring command |

## Update every 2 seconds, 5 times

```bash
vmstat 2 5
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `vmstat` | Monitoring command |
| `2` | Directs to update every 2 seconds |
| `5` | Directs to update a total of 5 times |

# Command: dstat

## Description: It is vmstat, iostat, netstat, and ifstat all rolled into one tool. It is a versatile real-time system resource monitor

## Syntax

- `dstat [options] [delay [count]]`

## Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-c` | Shows CPU stats | `dstat -c` |
| `-m` | Show memory usage | `dstat -m` |
| `-d` | Show disk I/O | `dstat -d` |
| `-n` | Show network traffic | `dstat -n` |
| `-g` | Show page stats | `dstat -g` |
| `-y` | Show system stats | `dstat -y` |
| `-p` | Show process stats | `dstat -p` |

## Examples

## Mix multiple options together

```bash
dstat -cdngyt
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `dstat` | Monitoring command |
| `-cdngyt` | Directs to monitor the CPU, I/O, network, page, system, and print a timestamp along with all the selected stats |

# Command: w

## Description: Shows who is logged in and their running processes. It displays current time, how long the system has been running, number of users logged in, load averages, and detailed information on user sessions

## Syntax

- `w [OPTIONS] [USER]`

## Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-h` | Do not print the header | `w -h` |
| `-u` | Ignore the username when figuring out idle time | `w -u` |
| `-s` | Short format | `w -s` |
| `-f` | Toggle form/to showing the FROM field | `w -f` |
| `[user]` | Specify a username to limit the display | `w name` |

## Examples

## Show all active users and their activity

```bash
w
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `w` | Monitoring command |

# Command: who

## Description: Displays information about users currently logged in th the system. It pulls information from `/var/run/utmp` file

## Syntax

- `*who [OPTIONS] [file]`

## Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-a`,`--all` | Show all available information | `who -a` |
| `-b`,`--boot` | Show last system boot time | `who -b` |
| `-d`,`--dead` | Show dead processes | `who -d` |
| `-H`,`--heading` | Print column headers | `who -H` |
| `-l`,`--login` | Show login processes | `who -l` |
| `-m` | Show only the current terminal session. Same as `whoami` | `who -m` |
| `-p`,`--process` | Show active processes spawned by init | `who -p` |
| `-q`,`--count` | Quick list of usernames + total numbers of users | `who -q` |
| `-r`,`--runlevel` | Show current runlevel | `who -r` |
| `-s`,`--short` | Default output-username,terminal,login time | `who -s` |
| `-T`,~--mesg`,`-w`,`--write` | Show users message permission status | `who -T` |
| `-u`,`--user` | Show idle time of users | `who -u` |
| `--ips` | Show IP addresses instead of hostnames | `who --ips` |

## Examples

## List logged-in users

```bash
who
```

## Breakdown

| Breakdown | Description |
|-----------|-------------|
| `who` | System command |

## Show with headers

```bash
who -H
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `who` | System command |
| `-H` | Directs to print column headers |

# Command: watch

## Description: Repeatedly runs a specified command at a fixed interval and displays the output fullscreen in the terminal

## Syntax

- `watch [option] command`

## Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-n`,`--interval<seconds>` | Sets the refresh interval in seconds | `watch -n 4 ls -l` |
| `-d`,`--differences[=permanent]` | Highlight the differences between updates, if `=permanent` is added, changes remain highlighted permanently | `watch -d free -m` |
| `-t`,`--no-title` | Removes the header showing interval, command, and timestamp | `watch -t date` |
| `-g`,`--chgexit` | Exit when the output of the command changes | `watch -g ls /tmp` |
| `-e`,`--errexit` | Exit if the command returns a non-zero exit code | `watch -e systemctl is-actie ssh` |
| `-c`,`--color` | Interpret ANSI color codes so colored output displays properly | `watch -c ls --color=always` |
| `-b`,`--beep` | Beep if the command has non-zero exit code | `watch -b systemctl is-active apache2` |
| `-p`,`--precise` | Try to run the command at precise intervals, accounting for drift | `watch -n 1 -p date` |

## Examples

## Monitor disk usage every 10 seconds

```bash
watch -n 10 df -h
```

### Breakdown 

| Breakdown | Description |
|-----------|-------------|
| `watch` | Monitoring command |
| `-n 10` | Sets the refresh interval in seconds |
| `df` | Directs to display disk usage for each file system |
| `-h` | Directs to make all output in human readable format |

# Command: progress

## Description: Displays how much data has been processed, gives percentage completion, and estimated time remaining 

## Syntax

- `progress [Options]`

## Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-q`,`--quiet` | Suppresses messages, silent mode | `progress -q` |
| `-d`,`--debug` | Show debug and warning messages | `progress -d` |
| `-w`,`--wait` | Estimate I/O throughput + time remaining | `progress -w` |
| `-W secs`,`--wait-delay secs` | Delay before calculating throughput | `progress -W` |
| `-m`,`--monitor` | Loop while monitored throughput | `progress -m` |
| `-M`,`--monitor-continously` | Monitor indefinitely | `progress -M` |
| `-c cmd`,`--command cmd` | Only monitor processes named cmd | `progress -c firefox` |
| `-a cmd`,`--command cmd` | Add cmd to default monitored list | `progress -a rsync` |
| `-p pid`,`--pid id` | Monitor only a specific process id | `progress -p 1234` |
| `-i file`,`--ignore-file file` | Do not report processes handling file | `progress -i example.txt` |

## Example

## Monitor continuously

```bash
progress -m
```

### Breakdown

| Breakdown | Description | 
|-----------|-------------|
| `progress` | Monitoring command |
| `-m` | Loop while monitoring throughput |
