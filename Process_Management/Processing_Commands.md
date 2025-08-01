# **Process Management**

## **ps**
- Shows a snapshot of current processes.

##** Syntax**
- ps [OPTIONS]

## **Options**
	Show all processes (alias for -A).
-f	Full-format listing.
-u USER	Show processes for a specific user.
-o	Customize output format.
aux	BSD style: show all processes with details.

#### **Examples**
Show all running processes:
ps -e

Show full details (UID, PID, etc.):
ps -ef

 Show processes for user “jake”:
ps -u jake

 BSD style:
ps aux

Show only PID and COMMAND columns:
ps -eo pid,comm

## **top**
Real-time view of processes and resource usage.

## **Syntax**
-top [OPTIONS]

## **Options**
-u USER	Show processes for a specific user.
-p PID	Monitor only the given PID.
-n N	Update screen N times then exit.

####**Examples**
Run top:
top

 Show processes for user “jake”:
top -u jake

Monitor only PID 1234:
top -p 1234

## **htop**
An improved, interactive version of top. (If not installed, use sudo apt install htop)


htop

Ex:

Run htop:
htop

Use arrow keys to navigate and F9 to kill a process.
✅ Press F6 to sort by a column (e.g., CPU usage).


glances – System Monitor (like top/htop but on steroids)

Syntax

glances 

Ex:

glances -w

Options

	-w → Run web server mode
	•	-t → Set refresh time

iotop – Monitor disk I/O per process

Syntax
Sudo iotop 

Ex:
sudo iotop -o

Options

	-o → Show only processes doing I/O
	•	-a → Accumulate I/O over time



kill

Send a signal (default: TERM) to a process.

kill [OPTIONS] PID

Options
-l	List all available signals.
-9	Send SIGKILL (force kill).
-15	Send SIGTERM (default).

Ex:

Gracefully terminate PID 1234:
kill 1234

Force kill PID 1234:
kill -9 1234

List signals:
kill -l


killall

Kills processes by name instead of PID.

killall [OPTIONS] PROCESS_NAME

Options
-i	Prompt before killing.
-v	Verbose (show what was killed).

Ex:

Kill all processes named “firefox”:
killall firefox

Prompt before killing:
killall -i python3

jobs

Lists background jobs in the current shell session.

jobs [OPTIONS]

Options
-l	Show PIDs of background jobs.

Ex:

List background jobs:
jobs

List jobs with PID:
jobs -l

bg

Resumes a stopped job in the background.

bg [JOB_SPEC]

Ex:

Resume job #1 in background:
bg %1

Resume most recent stopped job:
bg


fg

Brings a background job to the foreground.

fg [JOB_SPEC]

Ex:

Bring job #1 to foreground:
fg %1

Bring most recent background job:
fg


nice

Starts a process with a specific priority (lower is higher priority).

nice [OPTIONS] COMMAND

Options
-n VALUE	Set priority adjustment (-20 to 19).

Ex:

 Run a script with lower priority:
nice -n 10 ./backup.sh

 Run with highest priority (requires sudo):
sudo nice -n -20 ./critical_task.sh


nice
-Set the priority of a process at startup
-When launching a new process

Syntax:
nice -n 10 command

	-n: Nice value (range: -20 to 19)
	•	Lower = higher priority (e.g., -5 = more CPU time)
	•	Higher = lower priority (e.g., 10 = gets CPU when available)

Ex:
nice -n 15 tar -czf backup.tar.gz /home/jake
Starts the tar process with low priority (15 = nice to others).




renice

Changes the priority of an already running process.
After the process has started

renice PRIORITY -p PID

 Change priority of PID 1234:
renice 5 -p 1234

Make PID 5678 highest priority:
sudo renice -20 -p 5678

