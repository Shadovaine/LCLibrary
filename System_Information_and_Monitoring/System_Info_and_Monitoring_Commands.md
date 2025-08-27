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

-h	Human-readable sizes.
-T	Show filesystem type.
-a	Include pseudo, duplicate, and inaccessible file systems.

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
| `-I 

-T	Print human-readable timestamps.
-k	Only show kernel messages.
 
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

<<<<<<< HEAD

=======
# Command: findmnt

## Syntax

## Description

## Options

## Examples

# Command: fsck

## Description:

## Syntax

## Options

## Examples
>>>>>>> 92ea0f6203aaafb48631556e43e9fd106a53637b
# Command: lsblk

## Description: Lists block devices (disks, partitions, etc.)

## Syntax

- `lsblk [OPTIONS]`

## Options

-f	Show filesystem info.
-a	Show all devices.

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

## Description: Displays CPU architecture info

## Syntax

## Options

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

## Description:

## Syntax

## Options

## Examples

# Command: umount

## Description:

## Syntax

## Options

## Examples

# Command: iostat

## Description: Shows CPU and disk I/O statistics. (Requires sysstat package)

## Syntax

- `iostat [OPTIONS] [INTERVAL [COUNT]]`

## Options

-c	CPU utilization only.
-d	Device utilization only.

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
| `-c` | 
# Command: vmstat

## Description: Reports virtual memory, CPU activity, I/O stats

## Syntax

- `vmstat [OPTIONS] [DELAY [COUNT]]`

### Options

-s	Show memory stats in table form.

### Examples

### One-shot report

vmstat

### Update every 2 seconds, 5 times

vmstat 2 5

### Memory stats summary

vmstat -s

# Command: dstat

## Description: All-in-one performance viewer

## Syntax

- `dstat [options]`

### Options

### Examples

dstat -cdngyt

### **Options**
	•	-c → CPU
	•	-d → Disk
	•	-n → Network
	•	-g → Page stats
	•	-y → System stats
	•	-t → Time


# Command: w

## Description: Shows who is logged in and what they’re doing

## Syntax

- `w [OPTIONS] [USER]`

### Options

-h	Don’t print header.

### Examples

### Show active users and processes

w

### Show only user “name"

w name

# Command: who

## Description: Shows who is logged in

## Syntax

- `*who [OPTIONS]`

### Options

H	Print column headers.
-u	Include idle time.

### Examples

### List logged-in users

who

### Show with headers

who -H

# Command: watch

## Description: Repeat a command at intervals

## Syntax

- `watch [option] command`

### Options

	•	-n → Interval in seconds
	•	-d → Highlight changes

### Examples

-watch -n 1 'df -h'

# Command: progress

## Description: Show progress of common commands (cp, mv, etc.)

## Syntax

- `progress`

### Options

	•	-w → Watch mode (auto-refreshing)
	•	-c → Compact output
### Examples

- progress -w
