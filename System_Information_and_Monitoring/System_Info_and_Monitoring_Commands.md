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

-a	Show all system information.
-r	Show kernel release.
-s	Show kernel name.
-n	Show network hostname.
-m	Show machine hardware name (arch).

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

## Description: Displays how long the system has been running

## Syntax

- `uptime`

## Options

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

- `[Options] [Device..]`

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

# Command: free

## Description: Shows RAM and swap usage

## Syntax

- `free [OPTIONS]`

## Options

-h	Human-readable (MB, GB).
-m	Show output in MB.
-g	Show output in GB.
-t	Show totals.

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

## Description:

## Syntax

## Options

## Examples

# Command: dmesg

## Description: Prints kernel ring buffer messages (boot logs, driver info)

## Syntax

- `dmesg [OPTIONS]`

## Options

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
