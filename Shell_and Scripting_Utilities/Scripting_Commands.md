# **Shell and Scripting Utilities**

## +*echo**
- Print text or variables to the terminal.

## **Syntax**
- echo [OPTIONS] [STRING...]

### **Options**
-n	Do not output the trailing newline.
-e	Enable interpretation of backslash escapes.

#### **Examples**
 Print text:
echo "Hello, dragon rider!"

 Print without newline:
echo -n "Enter your name: "

Print with escape characters:
echo -e "Line 1\nLine 2\tTabbed"

Print environment variable:
echo $HOME


## **read**
- Read a line of input from the user

## ** Syntax**
- read [OPTIONS] VARIABLE

## **Options**
-p PROMPT	Display a prompt before reading input.
-s	Silent mode (hide input, e.g., passwords).

### **Examples**
Read user input:
read name
echo "Hello, $name!"

Prompt for input:
read -p "Enter your username: " username

Silent read (for passwords):
read -sp "Enter password: " password



## **export**
- Set environment variables for the current session.

## **Syntax**
- export VARIABLE=VALUE

### **Examples**
Set a variable:
export EDITOR=nano

Set PATH:
export PATH=$PATH:/opt/myapp/bin

Make a variable available to child processes:
export LANG=en_US.UTF-8



## **alias**
- Create shortcuts for commands.

## **Syntax**
- alias NAME='COMMAND'

### **Examples**
Make ll list with details:
alias ll='ls -la'

Shorten a long command:
alias gs='git status'

Remove an alias:
unalias ll

List all aliases:
alias



## **history**
- Show command history.

## **Syntax**
- history [OPTIONS]

## **Options**
(no args)	List command history.
-c	Clear the history.
!N	Run command number N from history.

#### ** Examples**
 Show last 10 commands:
history | tail -10

 Re-run command #42:
!42

Clear history:
history -c



## **cron**
- Runs scheduled tasks repeatedly at specified times.
- You use crontab to manage your cron jobs.

## **Syntax**
- crontab [OPTIONS]

### **Options**
-e	Edit the crontab file.
-l	List current user’s cron jobs.
-r	Remove current user’s crontab.

#### **Examples**
Edit cron jobs:
crontab -e

List cron jobs:
crontab -l

Example cron job (run backup.sh daily at 2AM):
0 2 * * * /home/jake/scripts/backup.sh



## **at**
- Schedule a one-time task to run in the future.
## **Syntax**
- at TIME

### **Options**
-l	List pending at jobs.
-c JOB	View commands for a scheduled job.
-r JOB	Remove a scheduled job.

#### **Examples**
Schedule task to run at 5 PM:
at 17:00

List scheduled tasks:
atq

Remove job #2:
atrm 2

# **zi – Fast, modular Zsh plugin manager**
	•	Category: Shell Enhancement / Zsh Plugin Loader

## **Syntax**
- zi load username/repo

## **Examples**
- zi load zsh-users/zsh-autosuggestions

# unalias

# which

# type

# set

# bash

# exit
