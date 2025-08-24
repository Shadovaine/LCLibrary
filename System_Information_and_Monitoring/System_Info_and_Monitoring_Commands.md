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

uname 

## Show all system details

uname -a

## Show only architecture

uname -m

# Command: uptime

## Description: Displays how long the system has been running

## Syntax

- `uptime`

### Options

### Examples

- Show uptime and load averages:
uptime

Output: 14:36:29 up 3 days, 5:42, 3 users, load average: 0.08, 0.05, 0.01)

# Command: free

## Description: Shows RAM and swap usage

## Syntax

- `free [OPTIONS]`

### Options

-h	Human-readable (MB, GB).
-m	Show output in MB.
-g	Show output in GB.
-t	Show totals.

### Examples

### Show memory in MB

- free -m

### Human-readable format

free -h

# Command: df

## Description: Shows disk usage of file systems

## Syntax

- `df [OPTIONS] [FILESYSTEM]`

### Options

-h	Human-readable sizes.
-T	Show filesystem type.
-a	Include pseudo, duplicate, and inaccessible file systems.

### Examples

### Show disk usage in human-readable format

df -h

### Show filesystem types

df -T

# Command: dmesg

## Description: Prints kernel ring buffer messages (boot logs, driver info)

## Syntax

- `dmesg [OPTIONS]`

### Options

-T	Print human-readable timestamps.
-k	Only show kernel messages.
 
### Examples

### Show boot logs

dmesg | less

### Show with timestamps

dmesg -T

### Filter for USB events

dmesg | grep usb

# Command: lsblk

## Description: Lists block devices (disks, partitions, etc.)

## Syntax

- `lsblk [OPTIONS]`

### Options

-f	Show filesystem info.
-a	Show all devices.

### Examples

### Show block devices tree

lsblk

### Show with filesystem info

lsblk -f

# Command: lscpu

## Description: Displays CPU architecture info

## Syntax

### Options

### Examples

- `lscpu`

### Show CPU details

lscpu

Outputs info like cores, threads, architecture, etc.)

# Command: iostat

## Description: Shows CPU and disk I/O statistics. (Requires sysstat package)

## Syntax

- `iostat [OPTIONS] [INTERVAL [COUNT]]`

### Options

-c	CPU utilization only.
-d	Device utilization only.

### Examples

### Show CPU and disk stats

iostat

### Update every 2 sec, 3 times

iostat 2 3

### Show only CPU stats

iostat -c

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
