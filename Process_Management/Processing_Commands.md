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

### Interactive Commands

### Description: Commands used within top

| Interactive Command | Description |
|---------------------|-------------|
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

## Description: An improved, interactive version of top.

## Syntax

- `htop [Options]

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|

### Examples
Run htop:
htop

Use arrow keys to navigate and F9 to kill a process.
✅ Press F6 to sort by a column (e.g., CPU usage).


## **glances – System Monitor (like top/htop but on steroids)**

## **Syntax**
glances 

### **Examples**
glances -w

#### **Options**
	-w → Run web server mode
	•	-t → Set refresh time

## **iotop – Monitor disk I/O per process**

## **Syntax**
-Sudo iotop 

### **Examples**
-sudo iotop -o

#### **Options**
	-o → Show only processes doing I/O
	•	-a → Accumulate I/O over time



## **kill**
- Send a signal (default: TERM) to a process.

## **Syntax**
- kill [OPTIONS] PID

### **Options**
-l	List all available signals.
-9	Send SIGKILL (force kill).
-15	Send SIGTERM (default).

#### **Example**
Gracefully terminate PID 1234:
kill 1234

Force kill PID 1234:
kill -9 1234

List signals:
kill -l


## **killall**
- Kills processes by name instead of PID.

## **Syntax**
- killall [OPTIONS] PROCESS_NAME

### **Options**
-i	Prompt before killing.
-v	Verbose (show what was killed).

#### **Examples**
Kill all processes named “firefox”:
killall firefox

Prompt before killing:
killall -i python3

## **jobs**
- Lists background jobs in the current shell session.

## **Syntax**
- jobs [OPTIONS]

### **Options**
-l	Show PIDs of background jobs.

#### **Examples**
List background jobs:
jobs

List jobs with PID:
jobs -l

## **bg**
- Resumes a stopped job in the background.

## **Syntax**
- bg [JOB_SPEC]

*** **Examples**
Resume job #1 in background:
bg %1

Resume most recent stopped job:
bg


## **fg**
- Brings a background job to the foreground.

## ** Syntax**
- fg [JOB_SPEC]

## **Examples**
Bring job #1 to foreground:
fg %1

Bring most recent background job:
fg


## **nice**
- Starts a process with a specific priority (lower is higher priority).

## **Syntax**
- nice [OPTIONS] COMMAND

## **Options**
-n VALUE	Set priority adjustment (-20 to 19).

### **Examples**
 Run a script with lower priority:
nice -n 10 ./backup.sh

 Run with highest priority (requires sudo):
sudo nice -n -20 ./critical_task.sh


## **nice**
-Set the priority of a process at startup
-When launching a new process

## **Syntax**
- nice -n 10 command

## **Options**
	-n: Nice value (range: -20 to 19)
	•	Lower = higher priority (e.g., -5 = more CPU time)
	•	Higher = lower priority (e.g., 10 = gets CPU when available)

Ex:
nice -n 15 tar -czf backup.tar.gz /home/jake
Starts the tar process with low priority (15 = nice to others).




## **renice**
- Changes the priority of an already running process.
- After the process has started

renice PRIORITY -p PID

 Change priority of PID 1234:
renice 5 -p 1234

Make PID 5678 highest priority:
sudo renice -20 -p 5678

