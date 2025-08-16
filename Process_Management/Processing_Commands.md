# Process Management

## Description: Commands involved in monitoring all processes

## Table of Contents

- `ps`
- `top`
- `htop`
- `glances`
- `iotop`
- `kill`
- `killall`
- `job`
- `bg`
- `fg`
- `nice`
- `renice`

## Command: ps

## Description: Short for 'process status'. Shows a snapshot of current processes.

## Syntax

- `ps [OPTIONS]`

### Options

| Options | Descriptions | Examples |
|---------|---------------|----------|
| `-e` or `-A` | Show all running processes | `ps -e`or`ps -A` |
| `-f` | Show Full-format listing | `ps -f` |
| `-u` | Show processes for a specific user | `ps -u username` |
| `-x` | Includes process not attached to the terminal | `ps -x` |
| `-o` | Customize output fields | `ps -eo pid,ppid,user,cmd,%mem,%cpu --sort=%cpu` |
| `--forest` | Show output in tree form | `ps -ef --forest` |
| `--sort` | Sort by field | `ps -eo pid,cmd,%mem --sort=-%mem` |
| `-p<PID>` | Display a specific process by PID | `ps -p 1234` |
| `--ppid<PID>` | Show children of a specific process | `ps ppid 1` |


### Examples

### Show all running processes

```bash
ps -e
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `ps` | Process manager command |
| `-e` | Show all running processes |

### Show full details (UID, PID, etc.)

```bash
ps -ef
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `ps` | Process manager command |
| `-e` | Show all running processes |
| `-f` | Show full-format |

### Show processes for user “username"

```bash
ps -u username
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `ps` | Process Manager command |
| `-u` | Show processes for a specific user |
| `username` | Target user |

### BSD style

```bash
ps aux
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `ps` | Process manager command |
| `a` | All users |
| `u` | Display user/owner |
| `x` | Include deamons and background tasks |

### Show only PID and COMMAND columns

```bash
ps -eo pid,cmd
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `ps` | Process manager command |
| `-e` | Show all running processes |
| `-o` | Customize output fields |
| `pid``cmd` | Target output fields |

# Command: top

## Deacription: Real-time view of processes and resource usage. It displays CPU usage,memory usage,uptime,load averages,and other things.

## Syntax

- `top [OPTIONS]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-d<seconds>` | Set refresh delay between screen updates | `top -d 2` |
| `-n<count>` | Run for a set of iterations | `top -n 5` |
| `-b` | Batch mode, when used with `-n prints output instead of interactive GUI | `top -b -n 
| `-u<username>` | Show only processes by a soecific user | `top -u username` |
| `-p<PID>` | Monitors a specific process by PID | `top -p 1234` | 

### Interactive Keystrokes

### Description: Keystrokes used within top

| Interactive Keystrokes | Description |
|------------------------|-------------|
| `h` | Help Screen |
| `p` | Sort by CPU usage |
| `M` | Sorr by memory usage |
| `T` | Sorr by time ( total CPU time used) |
| `k` | Kill a process |
| `r` | Renice a process |
| `u` | Filter by user | 
| `c` | Toggle full command-line path |
| `1` | Toggle CPU core stats |
| `z``b` | Toggle color/visual bold display |
| `q` | Quit |
| `f` | Add or remove columns |
| `W` | Save configuration |


### Examples

### Run top

```bash
top
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `top` | Process Manager command |

### Show processes for user “username"

```bash
top -u username
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `top` | Process Manager command |
| `-u` | Show processes only for username |
| `username` | Target username |

### Monitor only PID 1234

```bash
top -p 1234
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `top` | Process manager command |
| `-p` | Monitor only a specific PID |
| `1234` | Target PID |

# Command: htop

## Description: An improved, powerful, interactive process viewer.

## Syntax

- `htop [Options]

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-d<delay>` | Set delay between updates | `htop -d 20` |
| `-u` | Show only processes of a specific user | `htop -u username` |
| `-p<PID>[<PID2>]` | Show only specific PIDs | `htop -p 1234,5678` |
| `-s<column>` | Sort by a specific column name | `htop -s PERCENT_MEM` |
| `-C``--no-color` | Disable colors | `htop -C` |
| `-t` | Tree view enabled by default | `htop -t` |
| `--sort-key<column>` | Like -s, far clarify | `htop --sort-key PERCENT_CPU` |

### Interactive Keystroks

### Description: Keystrokes used within htop

| Interactive Keystrokes | Descriptions |
|------------------------|--------------|
| `F1` | Help Screen |
| `F2` | Setup Menu |
| `F3` | Search |
| `F4` | Filter |
| `F5` | Tree view |
| `F6` | change sort column |
| `F7` | Lower process priority |
| `F8` | Raise provess priority |
| `F9` | Kill selected process |
| `F10` | Quit |
| `t` | Tree view |
| `h` | Toggle help screen |
| `H` | Toggle threads view |
| `c` | Toggle command name view |
| `m` | Toggle memory meters |
| `s` | Trace system calls |
| `l` | Display open files |

### Examples

### Run htop

```bash
htop
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `htop` | Starts the program |


# Command: glances

## Description: System Process Monitoring package

## Syntax

- `glances`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-h` | Show help | `glances -h` |
| `-V` | shows the current version | `glances -V` |
| `-t<seconds>` | Sets refresh rate | `glances -t 5` |
| `-w` | Start in Web UI mode | `glances -w` |
| `-s` | Start in server mode | `glances -s` | 
| `-c` | connect as client to remote server | `glances -c 192.168.1.50` |
| `-C` | Use custom config file | `glances -C /etc/glances/glances.conf` |
| `-o<type>` | Set your output mode | `glances -o html` |
| `-export<backend>` | Exports stats to DB/Monitoring tool | `glances --export influxdb2` |
| `--diable-logs` | Disable logs | `glances --disable-logs` |
| `--disable-check-update` | Disable auto update check | `glances --disable-check-update` |
| `--disable-rest` | Disable RESTful API | `glance --disable-rest` |
| `--enable-plugin<name>``--disable-plugin<name>` | Control plugins | `glances --disable-plugin gpu` |
| `-p<port>` | Set server/webserver port | `glances -w -p 8080` |
| `--username<user>--password<pwd>` | Set basic auth for web UI | `glance -w --username admin --password secret` |
| `-f<MB>` | Minimum free space alert threshold | `glances -f 500` |
| `--process filter<regex>` | Only show processes matching regex | `glances --process-filter python` |
| `-B` | No bold text | `glances -B` |
| `-q` | Only critical messages | `glances -q` |

### Interactive Keystrokes

| Interactive Keystrokes | Description |
|------------------------|-------------|
| `h` | Help |
| `q` | Quit |
| `1` | Per CPU stats toggle |
| `m` | Sort Processes by CPU |
| `c` | Sort porcesses by CPU |
| `i` | Sort by I/O |
| `t` | Sort by time |
| `p` | Sort by process name |
| `u` | Show processes by user |
| `f` | Toggle filesystem stats | 
| `n` | Toggle network stats |
| `d` | Toggle disk I/O stats |
| `s` | Toggle sensors |
| `l` | toggle logs |

### Examples

```bash
glances -w
```

### Breakdown 

| Breakdown | Description |
|-----------|-------------|
| `glances` | Process manager command |
| `-w` | Show in Web UI mode |

# Command: iotop

## Description: Monitor disk I/O per process

## Syntax

- `sudo iotop`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-o` | Show only provesses or threads actually doing I/O | `sudo iotop -o` |
| `-a` | Show total I/O since iotop started | `sudo iotop -a` |
| `-b` | Run in non-interactive mode, suitable for logging | `sudo iotop -b -n 10 > io_log.txt` |
| `-n<NUM>` | Number of iterations to run(use with -b) | `sudo iotop -b -n 2` |
| `-d<SECONDS>` | Delay between updates | `sudo iotop -d 2` |
| -p<PID>` | Monitor only specific process by PID | `sudo iotop -p 1234` | 
| `-u<USER>` | Show only processes for a given user | `sudo iotop -u user` |
| `-k` | Show I/O in KB instead of bytes | `sudo iotop -k` |
| `-q` | Suppress header lines | `sudo iotop -b -qqq > io_only.txt` |

### Examples

-sudo iotop -o

# Command: kill

## Description: Send a signal (default: TERM) to a process

## Syntax

- `kill [OPTIONS] PID`

### Options

-l	List all available signals.
-9	Send SIGKILL (force kill).
-15	Send SIGTERM (default).

### Example

Gracefully terminate PID 1234:
kill 1234

Force kill PID 1234:
kill -9 1234

List signals:
kill -l

# Command: killall

## Description:  Kills processes by name instead of PID

## Syntax

- `killall [OPTIONS] PROCESS_NAME`

### Options

-i	Prompt before killing.
-v	Verbose (show what was killed).

### Examples

Kill all processes named “firefox”:
killall firefox

Prompt before killing:
killall -i python3

# Command: jobs

## Description: Lists background jobs in the current shell session

## Syntax

- `jobs [OPTIONS]`

### Options

-l	Show PIDs of background jobs.

### Examples

List background jobs:
jobs

List jobs with PID:
jobs -l

# Command: bg

## Description: Resumes a stopped job in the background

## Syntax

- `bg [JOB_SPEC]`

### Examples

Resume job #1 in background:
bg %1

Resume most recent stopped job:
bg


# Command: fg

## Description: Brings a background job to the foreground

## Syntax

- `fg [JOB_SPEC]`

### Examples

Bring job #1 to foreground:
fg %1

Bring most recent background job:
fg


# Command: nice

## Description: Starts a process with a specific priority (lower is higher priority)

## Syntax

- `nice [OPTIONS] COMMAND`

## Options

-n VALUE	Set priority adjustment (-20 to 19).

### Examples

 Run a script with lower priority:
nice -n 10 ./backup.sh

 Run with highest priority (requires sudo):
sudo nice -n -20 ./critical_task.sh

# Command: renice

## Description: Changes the priority of an already running process.

renice PRIORITY -p PID

 Change priority of PID 1234:
renice 5 -p 1234

Make PID 5678 highest priority:
sudo renice -20 -p 5678

