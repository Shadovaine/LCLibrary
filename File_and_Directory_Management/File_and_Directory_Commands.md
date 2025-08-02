'# **File and Directory Management**

## Commands for manipulating files and directories

## Table of Contents
- **ls**
- **cd**
- **pwd**
- **mkdir**
- **rmdir**
- **cp**
- **mv**
- **rm**
- **touch**
- **echo**
- **find**
- **tree**
- **locate**
- **ripgrep**
- **fd**
- **fzf**
- **ranger**
- **zoxide**
- **exa**


## Command: ls 
**Descriptions:** Lists files in a directory

## **Syntax**
- ls [option] [directory]

### **Option**
- `-a`:  Show all files (include hidden ones)
- `-l`:  Long listing format
- `-h`:  Human-reachable file sizes
- `-R`:  Recursively list subdirectories
- `-S`:  Sort by file sizes

### **Example**
```bash
ls -alh /etc
```

### **Breakdown**
- `ls`:   Command to list contents 
- `-a`:   Tells ls to show all files including the hidden files
- `-l`:   Makes ls to list directory files in long listing format
- `-h`:   Converts the file's raw bites into a human readable format
- `/etc`: Target Directory


## Command: cd 
**Description:** Change Directory
 
## **Syntax**
- cd [directory]

### **Special Behaviors (cd does not have options due to it being built into the shell)**
- `cd`:    Go to home directory
- `cd ~`:  Same as above
- `cd -`:  Switch to previous directory.
- `cd ..`: Move up one level
- `cd /'path'`:  Go to a specific directory
- `cd ../..`:  Move up two levels.
- `cd ./dirname`:  Enter a directory in the current location explicitly
- `cd ~username`:  Change to another user's home directory

### **Example**
```bash
cd /var/log
```

### **Breakdown**
- `cd`:  Change directory command
- `/var/log`:  Target Directory to change to `/var/log`

   
## Command: pwd 
**Description:** Print working directory

## **Syntax**
- pwd [options]

### **Options**
- `-p`:  Shows physical path ( resolves symlink)
- `-L`:  Show the logical path.
- `--help`:  Display help for the command.
- `--version`:  Shows version information.
- 
### **Example**
```bash
pwd -p
```

### **Breakdown**
- `pwd`:   print working directory command
- `-p`:    Will print the physical path


## Command: mkdir 
**Description:** Makes a new directory

## **Syntax**
- `mkdir [options] directory_name`

### **Options**
- `-p`:  Create parent directories as needed
- `-v`:  Shows created directories (verbose)
- `-m`:  Set permissions when creating the directory
- `--help`:  Display help information.
- `--version`:  Show version information.
  
### **Example**
```bash
mkdir -pv /tmp/dragon/nest
```

### **Breakdown**
- `mkdir`:  Command to tell system to make a new directory
- `-p`:  Will create parent directories
- `-v`:  Shows all created directories 
- `/tmp/dragon/nest`:  Target directory


## Command: rmdir
**Descriptions:** Removes a directory

## **Syntax**
- `rmdir [options] directory_name`

### **Options**
- `-ignore-fail-on-non-empty`:  Ignore errors for non-empty dirs 
- `-p`:  Remove the directory and its parent directories if they become empty.
- `-v`:  Verbose mode
- `--help`:  Display help information
- `--version`:  Show version informawtion

### **Example**
```bash
rmdir empty_folder
```

### **Breakdown**
- `rmdir`:  Command to remove directory
- `empty_folder`:  Name of directory to be removed


## Command: cp 
**Description:** Makes a copy of a file or directory to destination location
                It does leave an original copy in source location

## **Syntax**
- `cp [options] source destination`

### **Options**
- `-r`:   Copy directories recursively
- `-u`:   Copy only if source is newer
- `-v`:   Verbose outpost (show what is copied)
- `-i`:   Prompt before overwriting

### **Example**
```bash
cp -ruv /source/dir /backup/dir
```

### **Breakdown**
- `-cp`:   Copy Command
- `-r`:    Causes recursive copying
- `-u`:    Says to only copy if source is newer
- `-v`:    Verbose posting
- `/source/dir`:  Source location
- `/backup/dir`:  Destination Location


## Command: mv 
**Description:** Moves a file or directory to a destination location.
                It does not leave an original copy in source location

## **Syntax**
- `mv [options] source destination`

### **Options**
- `-i`:  Prompt before overwrite
- `-v`:  Verbose output
- `-u`:  Move only if source is newer

### **Example**
```bash
mv -iv file.txt /tmp/
```

### **Breakdown**
- `mv`:  Move Command
- `-i`:  Verify with user before overwrite
- `-v`:  Verbose output
- `file.txt`:  Source file
- `/tmp/`:  Destination location
  
## Command: rm 
**Description:** Removes files or directories 

## **Syntax**
- `rm [options] target`

### **Options**
- `-r`:  Remove directories and contents recursively
- `-f`:  Force deletion (ignore errors/prompts)
- `-i`:  Prompts before each deletion.
- `-v`:  Verbose output

### **Example**
```bash
rm -rf /tmp/testdir
```

### **Breakdown**
- `rm`:  Remove command
- `-r`:  Recursive removal
- `-f`:  Forced Deletion
- `/tmp/testdir`:  Target file to be deleted
 

## Command: touch
**Description:** Creates a file

## **Syntax**
- `touch [options] file_name`

### **Options**
- `-c` or `--no-create`:  Don’t create file if it doesn’t exist
- `-a`:  Change only the access time of the file.
- `-m`:  Changes only the modification time of the file.
- `-d`:  Set a specific date/time instead of using the current time
- `-t`:  Set a specific timestamp
- `-r`:  Use the timestamp from another file instead of the current time.

### **Example**
- `touch dragon.txt`

### **Breakdown**
- `touch`:  Create a file Command
- `dragon.txt`:  Name of new file


## **Command: echo
**Description:** Print what is in the string" "

## **Syntax**
-`echo [options] [string]`

### **Options**
- `-n`:  Don’t print newline at end
- `-e`:  Enable interpretation of escapes

### **Example**
 - `echo -e “Watcher\nmode”`

### **Breakdown**
- `echo`:  Print Command
- `-e`:  Don't print newline at end
- `"Watcher/nmode"`:  String to be printed


## Command: find
**Description** Searches files and directories

## **Syntax**
- `find [PATH] [OPTIONS] [EXPRESSION]`

### **Options**
- `-name`:  Match filenames
- `-type`:  Specify type (f for file, d for dir)
- `-size`:  Search by size ( e.g +10m, -1G)
- `-exec`:  Execute a command on found items
- `-mtime`:  Modified in last N days
- `-atime`:  Accessed in last N days
- `-print`:  Print full path of each file
- `-perm`:  World writable (others have permission to write)

### **Examples**
- `find /var/log -name "*.log" -exec rm {} \;`

### **Breakdown**
- `-find`:  Search Command
- `/var/log`:  Path to file
- `-name`:  Directs to match a filename
- `"*.log"`:  portion of file name to be searched for
- `-exec`:  Says to execute the following command
- `rm`:  Command to be executed
- `{}`:  A placeholder for each file as find command searches each file
- `\;`:  The end of the -exec command
   
## Command: tree
**Description:** Displays directory structure in a tree like form

## **Syntax**
- `tree [OPTIONS] [DIRECTORY]`

### **OPTIONS**
- `-a`:  Show all hidden files

### **Example**
```bash
tree -a /home
```
  
### **Breakdown**
- `tree`:  Command to create tree form
- `-a`:  Show all hidden files
- `/home`:  Target directory


## Command: Locate
**Description:** Searches filesystem

## **Syntax**
- `locate [OPTIONS] PATTERN`

### **Options**
- `-i`:  Case-insensitive search
- `-c`:  Prints out the number of matches instead of listing them.
- `-n NUM`:  Will only print out the desired amount inputed.
- `-r REGEX`:  Searches using regular expression.
- `-w`:  Matches whole words.
- `-b`:  Matches only the basename.
- `-1 NUM`:  Limits results to stated amount.
- `-0`:  outputs results sepersted by a null character instead of a new line.
- `-q`:  Quiet mode.
- `-d DBPATH`:  Uses a specific database and not the default database.
- `-e`:  only prints existing files.
- `-S`: Shows database statistics.
- `-V`:  Shows version information.

### **Example**
```bash
locate passwd find all files named passwd
```


## Command: ripgrep(rg)
**Descriptions:** Lightning-fast file search Command

## **Syntax**
- `rg [pattern] [path]`

### **Options**
- `-i`:  Case-insensitive
- `-n`:  Show line numbers
- `-l`:  List filenames only

### **Example**
```bash
rg "sudo" /etc
```

### **Breakdown**
- `rg`:  `rg` command
- `"sudo"`:  Selected pattern.
- `/etc`:  Targeted location.


## Command: fd
**Description** `find` command alternative

## **Syntax**
- `fd [pattern] [path]`

### **Options**
- `-e`:  File extension filter (e.g., -e txt)
- `-H`:  Include hidden files
- `-t f|d`:  Search for files or directories

### **Example**
```bash
fd passwd /etc
```

### **Breakdown**
- `fd`:  'fd' command
- `passwd`:  target pattern
- `/etc`:  target location to find pattern.


## Command: fzf
**Description:** Interactive fuzzy file finder

## **Syntax**
- `fzf`

### **Example**
```bash
find -type f | fzf
```

### **Breakdown**
- `find`:  `find` command
- `-type f`:  directs `find` command to loook in files
- `|`:  `pipe` command thats say it takes output from `find` and will send it through `fzf`
- `fzf`: Fuzzy file finder.


## Command: ranger
**Description** File manager

## **Syntax**
- `ranger`

### **Example**
```bash
ranger /etc
```

### **Breakdown**
- `ranger`:  Command
- `/etc`:  Target location

## Command: zoxide
**Description:** A smarter `cd` command

## **Syntax** 
- `zoxide [dir]`
- 
### **Example**
```bash
z /etc
```

### **Breakdown**
- `z`:  `zoxide` command
- `/etc`: target location.

## Command: exa 
**Description** Modern `ls` command

## **Syntax**
- exa [options] [path]

### **Options**
- `-l`:  Long format
- `-a`:  Show hidden files
- `-la` or `-al`:  Combine long format and hidden files.
- `-1`:  list one file per line.
- `-s`:  Sort by the file size.
- `-s name`:  Sort by name.
- `-s modified`:  Sort by modification time.
- `-r`:  Reverse the sort order.
- `-T`:  Display a tree view of directories.
- `-L <num>`:  Limit depth of recursion in tree view.
- `--git`:  Show Git status for files.
- `-@`:  Show extended attributes.
- `--icons`:  Show file-type icons 

### **Example**
```bash
exa -la -T /etc
```

### **Breakdown**
- `exa`:  exa command
- `-l`:  Long format
- `-a`:  Show hidden files.
- `-T`:  Put in tree viewing form
- `/etc`:  Target directory





