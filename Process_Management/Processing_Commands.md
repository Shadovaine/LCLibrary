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

## Description: Short for process status. Shows a snapshot of current processes

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
| `pid`or `cmd` | Target output fields |

# Command: top

## Deacription: Real-time view of processes and resource usage. It displays CPU usage,memory usage,uptime,load averages,and other things.

## Syntax

- `top [OPTIONS]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-d<seconds>` | Set refresh delay between screen updates | `top -d 2` |
| `-n<count>` | Run for a set of iterations | `top -n 5` |
| `-b` | Batch mode, when used with `-n prints output instead of interactive GUI | `top -b -n` |
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
| `z`or`b` | Toggle color/visual bold display |
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

## Description: Send a signal to kill a process

## Syntax

- `kill [OPTIONS] PID`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-s<SIGKILL>` or `-9` | Directs to send SIGKILL to terminate a process | `kill -s SIGKILL 1234` `kill -9 1111` |
| `-s<SIGHUP>` or `-1` | Directs to send SIGHUP to reload a process | `kill -s SIGHUP 1111` `kill -1 1111` |
| `-l` | Lists all available signals by name | `kill -l` |
| `-L` | List all available signals in a table format | `kill -L` |

### Examples

### Gracefully terminate PID 1234

```bash
kill 1234
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `kill` | Process command |
| `1234` | Target process |

### Force kill PID 1234

```bash
kill -9 1234
```

### Breakdown 

| Breakdown | Description |
|-----------|-------------|
| `kill` | Process command |
| `-9` | Directs to send SIGKILL to target process |
| `1234` | Target Process |

### List signals

```bash
kill -l
```

### Breakdown 

| Breakdown | Description |
|-----------|-------------|
| `kill` | Process command |
| `-l` | Lists all processes by name |

# Command: killall

## Description:  Kills processes by name instead of PID

## Syntax

- `killall [OPTIONS] PROCESS_NAME`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-s` | Sends a specific signal | `killall -s SIGKILL process` |
| `-e` | Exact name match | `killall -e ssh` |
| `-I` | Case-insensitive matching | `killall -i -I process` |
| `-g` | Kills the process group of each matched process | `killall -g process` |
| `-i` | Asks for confirmation before killing process | `killall -i process` |
| `-n` or `--ns<PID>` | Restricts matching to the namespace of PID | `killall -n 1234 bash` |
| `-w` | Waits until all killed processes are dead before exiting | `killall -w process` |
| `-V` | Shows current working version | `killall -V` |
| `-v` | Verbose mode | `killall -v process` |
| `-u` | kills only processess owned by user | `killall -u name process` |
| `-r` | Matches processes using a regular expression | `killall -r 'process.*'` |
| `-y` | Kills only processes younger than 5 minutes | `killall -y 5m process` |
| `-o` or `--older-than<time>` | Kills only processes older than one hour | `killall -o 1h process` |

### Examples

### Kill all processes named “firefox”

```bash
killall firefox
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `killall` | Process Command |
| `firefox` | process to be killed |

### Prompt before killing

```bash
killall -i python3
```

### Breakdown

| Breakdown | Description | 
|-----------|-------------|
| `killall` | Process command |
| `-i` | Directs to prompt user before killing process |
| `python3` | Process to be killed |

# Command: jobs

## Description: Lists background jobs in the current shell session. 

## Syntax

- `jobs [OPTIONS][job_spec ..]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-l` | Shows PIDs along with numbers | `jobs -l` |
| `-n` | Shows only jobs whose status has changed since the last `jobs` call | `jobs -n` |
| `-p` | Prints just the PIDs | `jobs -p` |
| `-r` | Lists only jobs that are currently running | `jobs -r` |
| `-r` | Lists only jobs that are stopped/suspended | `jobs -s` |
| `-s` | Show only stopped jobs | `jobs -s` |

### Examples

### List currently working jobs

```bash
jobs -r
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `jobs` | Process command |
| `-r` | Directs to only list currently running jobs |

### List jobs with PID

```bash
jobs -l
```

### Breakdown 

| Breakdown | Description |
|-----------|-------------|
| `jobs` | Process command |
| `-l` | Directs to list jobs by PID |

# Command: bg

## Description: Resumes a supspended job in the background in the current shell session

## Syntax

- `bg [JOB_SPEC]`

## Options

| Options | Description | Examples |
|---------|-------------|----------|
| `default` | Resume the most recent job | `bg` |
| `%%` | Brings the latest stopped job back into the background | `bg %%` |
| `%1` | Resume a specific job by number | `bg %1` |
| `%+` or `%%` | Resume the current job | `bg %+` |
| `%-` | Resume the previous job | `bg %-` |
| `%na` | Resume by partial job name | `bg %na` |
| `%?sleep` | Job whose command contains a string | `bg %?sleep` |

### Examples

### Resume job #1 in background

```bash
bg %1
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `bg` | process command |
| `%1` | Directs to resume a specific job by number |

### Resume most recent stopped job

```bash
bg
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `bg` | Process command when along automatically resumes the most recent stopped job |

# Command: fg

## Description: Brings a background job to the foreground running in current shell session

## Syntax

- `fg [JOB_SPEC]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `(none)` | Bring the most recent job to the foreground | `fg` |
| `%1` | Bring a specific job by number | `fg %1` |
| `%%` | Bring the current job | `fg %%` |
| `%-` | Bring the previous job | `fg %-` |
| `%string` | Bring a job by partial command name | `fg %string` |
| `%?string` | Bring a job by substring match | `fg %?1000` |


### Examples

### Bring job #1 to foreground

```bash
fg %1
```

### Breakdown

| Breakdown | Desription |
|-----------|------------|
| `fg` | Process command |
| `%1` | Bring a specific job by number | 

### Bring most recent background job

```bash
fg
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `fg` | Process command and by itself will bring most recent background job to foreground |

# Command: nice

## Description: Starts a process with a specific priority (lower is higher priority)

## Syntax

- `nice [OPTIONS] [COMMAND [ARG]...]`

## Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-n` | Set the nice value adjustment (Range is -20 = Highest to 19 = lowest) | `nice -n 5 sleep 60` |
| `--help` | Prints usage help | `nice --help` |
| `--version` | Prints version of nice | `nice --version` |

### Examples

### Run a script with lower priority

```bash
nice -n 10 ./backup.sh
```

### Breakdown 

| Breakdown | Description |
|-----------|-------------|
| `nice` | Process Command |
| `-n` | Directs to set value adjustment |
| `10` | Priority Value to assign to target file |
| `./backup.sh` | Target file |

### Run with highest priority (requires sudo)

```bash
sudo nice -n -20 ./critical_task.sh
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Temporary Superuser command |
| `nice` | Process command | 
| `-n` | Directs to set priority value |
| `-20` | Exact priority value to assign |
| `./critical_task.sh` | Target file |

# Command: renice

## Description: Changes the priority of an already running process

## Syntax

- `renice [Options] priority [PID]`

| Syntax Component | Description |
|------------------|-------------|
| `Priority` | The new nice value (between -20 = highest priority and 19 = lowest) |
| `PID` | One or more process IDs |

## Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-n` | Changes the nice value relative to the current one | `renice -n +5 -p 1234` |
| `-p` | Explicitly says you're renicing a process by PID | `renice 10 -p 1234` |
| `-u` | Changes priority of all processes owned by a user | `renice -n +5 -u name` | 
| `-g` | Changes priority for a whole process group | `renice -n -5 -g 1234` | 

### Examples

### Change priority of PID 1234

```bash
renice 5 -p 1234
```

### Breakdown

| Breakdown | Description|
|-----------|------------|
| `renice` | Process Manager command |
| `5` | Amount the nice value is changing |
| `-p` | Directs to only change target PID |
| `1234` | Target PID |

### Make PID 5678 highest priority

```bash
sudo renice -20 -p 5678
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Temporary Superuser command |
| `renice` | Process Manager command |
| `-20` | Specific nice value to change to |
| `-p` | Directs to only make changes to specific PID |
| `5678` | Specific PID |