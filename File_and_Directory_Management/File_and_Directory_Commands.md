# File and Directory Management

## Commands for manipulating files and directories

## Table of Contents

- `ls`
- `cd`
- `pwd`
- `mkdir`
- `rmdir`
- `cp`
- `mv`
- `rm`
- `touch`
- `echo`
- `find`
- `tree`
- `locate`
- `ripgrep`
- `fd`
- `fzf`
- `ranger`
- `zoxide`
- `exa`
- `shred`
- `vidir`



## Command: ls 

## Descriptions: Lists files in a directory

## Syntax

- `ls [option] [directory]`

### Option

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-a` | Show all files (include hidden ones). | `ls -a` |
| `-l` | Long listing format. | `ls -l` |
| `-h` | Human-readable file sizes. | `ls -h` |
| `-R` | Recursively list subdirectories. | `ls -R` |
| `-S` | Sort by file sizes. | `ls -S` |
| `-A` | Show all files except `.` and `..`. | `ls -A` |
| `-d` | List directories themselves. | `ls -d` |
| `-F` | Append `/` to directories, `*` to executables, `@` to symlinks. | `ls -F` |
| `-t` | Sort by modification time. | `ls -t` |
| `-r` | Reverse the sort order. | `ls -r` |
| `-1` | Force one entry per line. | `ls -1` |
| `-i` | Show the inode number of each file. | `ls -i` |
| `-p` | Append `/` to directories similar to `-F`. | `ls -p` |
| `-g` | Long listing format without showing owner. | `ls -g` |
| `-G` | Suppress group information in long listing format. | `ls -G` |
| `-q` | Show non-printable characters as `?`. | `ls -q` |
| `-X` | Sort by file extension. | `ls -X` |
| `--color` |  Colorize the output. | `ls --color` |
| `--group-directories-first` |  List directories before files. | `ls --group-directories-first` |

### Examples

### List all files in detail in readable format

```bash
ls -alh /etc
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `ls` | Command to list contents. |
| `-a` | Tells ls to show all files including the hidden files. |
| `-l` | Makes ls to list directory files in long listing format. |
| `-h` | Converts the file's raw bites into a human readable format. |
| `/etc` | Target Directory. |

### List all files in detail in readable form sorting them by file size.

```bash
ls -alhS /etc
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `ls` | List command. |
| `-a` | Directs ls to list all files including hidden ones. |
| `-l` | Directs list to be in detailed form. |
| `-h` | Outputs list in readable form. |
| `-S` | Directs to sort files by size. |
| `/etc` | Target directory to list. |

## Command: cd

## Description: Change Directory

## Syntax

- `cd [directory]`

### Special Behaviors (cd does not have options due to it being built into the shell)

| Special Behaviors | Description |
|-------------------|-------------|
| `cd` | Go to home directory. |
| `cd ~` | Same as above. |
| cd -` | Switch to previous directory. |
| `cd ..` | Move up one level. |
| `cd /'path'` | Go to a specific directory. |
| `cd ../..` | Move up two levels. |
| `cd ./dirname` | Enter a directory in the current location explicitly. |
| `cd ~username` | Change to another user's home directory. |

### Example

### Change to a specific file

```bash
cd ~/Desktop/profile
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `cd` | Change directory command. |
| `~` | Home directory. |
| `/Desktop/profile` | Target Directory to change to `/Desktop/profile`. |

## Command: pwd

## Description: Print working directory

## Syntax

- `pwd [options]`

### Options

| Options | Descriptions | Examples|
|---------|--------------|---------|
| `-p` | Shows physical path ( resolves symlink). | `pwd -p` |
| `-L` | Show the logical path. | `pwd -L` |
| `--help` | Display help for the command. | `pwd --help` |
| `--version` | Shows version information. | `pwd --version` |
  
### Example

### Show the physical path of the current working directory

```bash
pwd -p
```

### Breakdown

| Breakdown | Description |
|-----------|--------------|
| `pwd` | Print working directory command. |
| `-p` | Will print the physical path. |

## Command: mkdir

## Description: Makes a new directory

## Syntax

- `mkdir [options] directory_name`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-p` | Create parent directories as needed. | `mkdir -p backup/projects/place` |
| `-v` | Shows created directories (verbose). | `mkdir -v backups` |
| `-m` | Set permissions when creating the directory. | `mkdir -m 700 backups` |
| `--help` | Display help information.| `mkdir --help` |
| `--version` |Show version information. | `mkdir --version` |
  
### Examples

### Create a new directory along with parent directories and output the detailed locations

```bash
mkdir -pv /tmp/dragonnest
```

## Breakdown

| Breakdown | Description |
|-----------|-------------|
| `mkdir` | Command to tell system to make a new directory. |
| `-p` | Will create parent directories. |
| `-v` | Shows all created directories. |
| `/tmp/dragonnest` | Target directory. |

## Command: rmdir

## Descriptions: Removes a directory

## Syntax

- `rmdir [options] directory_name`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-ignore-fail-on-non-empty` | Ignore errors for non-empty dirs. | `rmdir -ignore-fail-on-non-empty project` |
| `-p` | Remove the directory and its parent directories if they become empty. | `rmdir -p project` |
| `-v` | Verbose mode. | `rmdir -v project` |
| `--help` | Display help information. | `rmdir --help` |
| `--version` | Show version informawtion. | `rmdir --version` |

### Example

### Remove a directory

```bash
rmdir empty_folder
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `rmdir` | Command to remove directory. |
| `empty_folder` | Name of directory to be removed. |



## Command: cp

## Description: Makes a copy of a file or directory to destination location. It leaves an original copy in source location

## Syntax

- `cp [options] source destination`

### Options

| Option | Description | Example |
|--------|-------------|---------|
| `-r`   | Copy directories recursively. | `cp -r folder/ backup/` |
| `-u`   | Copy only if source is newer  | `cp -u folder/ backup/` |
| `-v`   | Verbose mode | `cp -v folder/ backup/` |
| `-i`   | Prompt before overwriting | `cp -i folder/ backup/` |
| `-a`   | Archive mode | `cp -a folder/ backup/` |
| `-f`   | Force overwrite | `cp -f folder/ backup/` |
| `-n`   | No overwrite skip files thar already exist at destination. | `cp -n folder/ backup/` |
| `-p`   | Preserve file attributes. | `cp -p folder/ backup/` |
| `-d`   |  Preserve symlinks. | `cp -d folder/ backup/` |
| `-L`   |  Dereference symlinks | `cp -L folder/ backup/` |
| `-P`   |  Never dereference symlinks. | `cp -P folder/ backup/` |
| `--parents` | Preserve full path of source when copying to destination. | `cp --parents folder/ backup/` |
| `--remove-destination` | Remove destination before copying. | `cp --remove-destination folder/ backup/` |
| `--backup` | Create a backup of each existing destination file before copying. | `cp --backup folder/ backup/` | 

### Examples

### Copy a file into another directory

```bash
cp file.txt backup/
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `cp` | Copy command. |
| `file.txt` | Source file to copy. |
| `backup/` | Destination location for new copy. |
  
### Copy a directory recursively with verbose output

```bash
cp -rv project /backup/
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `cp` | Copy Command. |
| `-r` | Causes recursive copying. |
| `-v` | Verbose posting. |
| `project/` | Source location. |
| `backup/` | Destination Location. |

### Prompt before overwriting a file

```bash
cp -i file.txt backup/
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `-cp` | Copy command. |
| `-i` | Displays a prompt for user before overwriting. |
| `file.txt`:  Source file. |
| `backup/` | Destination location. |

## Command: mv

## Description: Moves a file or directory to a destination location. It does not leave an original copy in source location.

## Syntax

- `mv [options] source destination`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-i` | Prompt before overwrite. | `mv -i project.txt backup/` |
| `-v` | Verbose output. | `mv -v project.txt backup/` |
| `-u` | Move only if source is newer. | `mv -u project.txt backup/` |
| `-f` | Force move. | `mv -f project.txt backup/` |
| `-n` | Never overwrite an existing file. | `mv -n project.txt backup/` |
| `-t <dir>` | Specify the target directory explicitly. | `mv -t backup/ project.txt project1.txt project2.txt` |
| `--backup[=CONTROL]` | Make a backup of each destination file. | `mv --backup=simple project.txt backup/` |
| `--strip-trailing-slashes` | Removes trailing slashes from source arguments. | `mv --strip-trailing-slashes project/ backup/` |

### Example

### Prompt user before moving file then show detailed path of new location

```bash
mv -iv file.txt /tmp/
```

### Breakdown

| Breakdown | Description |
| `mv` | Move Command.
| `-i` | Verify with user if a file already exists before overwriting. |
| `-v` | Verbose mode. |
| `file.txt` | Source file.
| `/tmp/` | Destination location. |
  
## Command: rm

## Description: Removes files or directories

## Syntax

- `rm [options] target`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-r` | Remove directories and contents recursively. | `rm -r project/` |
| `-f` | Force deletion (ignore errors/prompts). | `rm -f project/` |
| `-i` | Prompts before each deletion. | `rm -i project` |
| `-v` | Verbose mode. | `rm -v project` |
| `-I` | Less intrusive interactive mode. | `rm -I project` |
| `-d` | Remove empty directories. | `rm -d /backup/` |
| `--preserve-root` | Prevents rm from operating recursively. | `rm --preserve-root backup/` |
| `--no-preserve-root` | Removes the protection from \. | `rm --no-preserve-root backup` |
| `--one-file-system` | When deleting recursively, skip files on other file systems. | `rm -r --one-file-system backup/` |

### Example

### Remove all directories and contents and force deletion on target directory

```bash
rm -rf /tmp/testdir
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `rm` | Remove command. |
| `-r` | Recursive removal. |
| `-f` | Forced Deletion. |
| `/tmp/testdir` | Target file to be deleted. |

## Command: touch

## Description: Creates a file

## Syntax

- `touch [options] file_name`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-c` or `--no-create` | Don’t create file if it doesn’t exist. | `touch -c backup` |
| `-a` | Change only the access time of the file. | `touch -a backup` |
| `-m` | Changes only the modification time of the file. | `touch -m backup` |
| `-d <time>` | Set a specific date/time instead of using the current time. | `touch -d <0000> backup` |
| `-t <stamp>` | Set a specific timestamp. | `touch -t <1300> backup` |
| `-r <file>` | Use the timestamp from another file instead of the current time. | `rm -r <backup> backup1` |

### Example

### Create a file

```bash
touch dragon.txt
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `-touch` | Create a file Command. |
| `dragon.txt` | Name of new file. |

## Command: echo

## Description: Print what is in the string" "

## Syntax

-`echo [options] [string]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-n` | Don’t print newline at end. | `echo -n "back up"` |
| `-e` | Enable interpretation of escapes. | `echo -e "back\nup"` |
| `-E` | Disable interpretation of escape sequence. | `echo -E "back up"` |

### Escape sequences (paired with -e)

| Escape Sequences | Descriptions |
|------------------|--------------|
| `\n` | Newline. |
| `\t` | Horizontal tab. |
| `\v` | Vertical tab. |
| '\r` | Carriage return. |
| `\b` | Backspace. |
| `\a` | Alert. |
| `\\` | Backslash. |
| `\c` | Suppress further output. |

### Example

```bash
echo -e “Watcher\nmode”
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `echo` | Print Command. |
| `-e` | Activates the following escape sequence. |
| `"Watcher"` | Prints this part of the string on first line. |
| `\n` | Directs everything after it to print on a new line. |
| `"mode"` | Rest of string prints on a new line. |

## Command: find

## Description: Searches files and directories

## Syntax

- `find [PATH] [OPTIONS] [EXPRESSION] [ACTION]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-name` | Match filenames. | `find /home/path -name "*.backup"` | 
| `-type` | Specify type (f for file, d for dir). | `find /home -type f "*.backup"` |
| `-size` | Search by size ( e.g +10m, -1G). | `find . -size +10k` |
| `-exec` | Execute a command on found items. | `find . -name "*.log" -exec rm {} \;` |
| `-mtime` | Modified in last N days. | `find /home -mtime 2` |
| `-atime` | Accessed in last N days. | `find /home -atime 3` |
| `-print` | Print full path of each file. | `find /home  -type f -print` |
| `-perm` | World writable (others have permission to write). | `find /home -perm 644` |

### Examples

### Remove all log files found in /var/log

```bash
find /var/log -name "*.log" -exec rm {} \;
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `-find` | Search Command. |
| `/var/log` | Path to file. |
| `-name` | Directs to match a filename. |
| `*.log"` | Portion of file name to be searched for. |
| `-exec` | Says to execute the following command. |
| `rm` | Command to be executed. |
| `{}` | A placeholder for each file as find command searches each file. |
| `\;` | The end of the -exec command. |

## Command: tree

## Description: Displays directory structure in a tree like form

## Syntax

- `tree [OPTIONS] [DIRECTORY]`

### OPTIONS

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-a` | Show all hidden files. | `tree -a` |
| `-d` | List directories. | `tree -d` |
| `-L <num>` | Limit display to a specific number of directory levels. | `tree -L 2 /home` |
| `-f` | Print full path prefix for each file. | `tree -f` |
| `-F` | Append `/` to directories, `*` to executables, @ to symlinks. | `tree -F` |
| `-p` | Print file permissions. | `tree -p` |
| `-u` | Print the username of the file owner. | `tree -u` |
| `-g` | Print the group name of the file owner. | `tree -g` |
| `-s` | Print file sizes in bytes. | `tree -s` |
| `-h` | Print file sizes in human readable format. | `tree -h` |
| `-P <pattern>` | Display only files matching a wildcard pattern. | `tree -P "*.sh"` |
| `-I <pattern>` | Exclude files or directories matching a wildcard pattern. | `tree -P "*.log"` |
| `-C` | Enable colorized output. | `tree -C` |
| `-n` | Disable colorized output. | `tree -n` |
| `-q` | Print non-printable characters as `?`. | `tree -q` |
| `--du` | Print directory sizes. | `tree --du` |
| `--prune` | Prune empty directories from the output. | `tree --prune` |
| `--dirsfirst` | List directories before files. | `tree --dirsfirst` |
  
### Example

### Show all files including hisden ones in a tree structure

```bash
tree -a /home
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `tree` | Command to create tree form. |
| `-a` | Show all hidden files. |
| `/home` | Target directory. |

## Command: Locate

## Description: Searches filesystem

## Syntax

- `locate [OPTIONS] PATTERN`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-i` | Case-insensitive search. | `locate -i backup` |
| `-c` | Prints out the number of matches instead of listing them. | `locate -c .log` |
| `-n NUM` | Will only print out the desired amount inputed. | `locate -n 9 backup` |
| `-r REGEX` | Searches using regular expression. | `locate -r "\.log$"` |
| `-w` | Matches whole words. | `locate -w backup` |
| `-b` | Matches only the basename. | `locate -b backup` |
| `-1 NUM` | Limits results to stated amount. | `locate -l 4 hosts` |
| `-0` | Output results separated by a null character instead of a new line. | `locate -0 backup` |
| `-q` | Quiet mode. | `locate -q backup` |
| `-d DBPATH` | Uses a specific database and not the default database. | `locate -d /home/path` |
| `-e` | Only prints existing files. | `locate -e backup` |
| `-S` | Shows database statistics. | `locate -S backup` |
| `-V`: |  Shows version information. | `locate -V backup` |

### Example

### Print out the top 10 results and make the search case-insensitive

```bash
locate -i -n 10 readme
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `locate` | `locate` command. |
| `-i` | Make the search case-insensitive. |
| `-n 10` | Sets the amount of lines to print out to 10 lines. |
| `readme` | target pattern. |

## Command: ripgrep(rg)

## Descriptions: Lightning-fast file search Command

## Syntax

- `rg [pattern] [path]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-i` | Case-insensitive. | `rg -i "error"` |
| `-n` | Show line numbers. | `rg -n "error"` |
| `-l` | List filenames only. | `rg -l "error"` |
| `-S` | Smart case: case-insensitive unless the oattern has upper cass letters. | `rg -S "error"` |
| `-F` | Treat the pattern as a literal string. | `rg -F "error"` |
| `-e <pattern>` | Explicitly specific a search pattern. | `rg -e "TOO" -e "HARD"` |
| `-w` | Match whole words only. | `rg -w "error"` |
| `-x` | Match the entire line. | `rg -x "error"` |
| `-g <glob>` | Includes only files matching the glob pattern. | `rg -g "*.sh"` |
| `-T <ext>` | Excludes a certain file type. | `rg -T "*.log"` |
| `-t <type>` | Searches only files of a certain type. | `rg -t "*.sh"` |
| `-u` | Search hidden and ignored files. | `rg -u /etc` |
| `-iglob <pattern>` | Case-insensitive glob matching. | `-ig "TOO" |
| `--hidden` | Include hidden files or directories. | `rg --hidden "error"` |
| `-H` | Always show the filename in results. | `rg -H "error"` |
| `-L` | Print only filenames without matches. | `rg -L "error"` |
| `-o` | Show only the matching part of each line. | `rg -o "error"` |
| `-v` | Invert match. | `rg -v "error"` |
| `-c` |  Show the count of matches per file. | `rg -c "error"` |
| `--stats` | Show search statistics. | `rg --stats "error"` |
| `-r <replacements>` | Use regex replacements. | `rg -r "error"` |
| `-m <NUM>` | Limit the number of matches. | `rg -m 3 "error"` |
| `--max-columns <NUM>` | Truncate long lines to the column width in the output. | `rg --max-columns 3 "error"` |
| `--max-depth <NUM>` | Limit search depth. | `rg --max-depth 3 "error"` |
| `--follow` | Follow symlink. | `rg --follow "error"` |
| `--no-messages` | Suppress error messages. | `rg --no-messages "error"` |
| `--color <when>` | Control color. always, never, auto. | `rg --color "always" "error"` |
| `--heading` | Shows file names as headings. | `rg --heading "error"` |
| `--no-heading` | Disables headings. | `rg --no-heading "error"` |
| `--json` | Output results in JSON format. | `rg --json "error"` |
| `--pretty` | Pretty print results with colors and context. | `rg --pretty "error"` |
| `-A <NUM>` |Show NUM lines after each match. | `rg -A 2 "error"` |
| `-B <NUM>` | Show NUM lines before each match. | `rg -B 2 "error"` |
| `-C <NUM>` | Show NUM lines of context. | `rg -C 2 "error"` |

### Example

### Search for sudo in all of /etc directory

```bash
rg "sudo" /etc
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `rg` | `rg` command. |
| `"sudo"` | Selected pattern. |
| `/etc` | Targeted location. |

## Command: fd

## Description: `find` command alternative

## Syntax

- `fd [options] [pattern] [path]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-e` | File extension filter (e.g., -e txt). | `fd -e md` |
| `-H` | Include hidden files. | `fd -H` |
| `-t f/d` | Search for files or directories. | `fd -t file.txt` |
| `-I` | Include ignored files. | `fd -I` |
| `-u` | Search unrestricted files including hidden and ignored files. | `fd -u` |
| `-e <ext>` | Search only files with the spwcific extension. | `fd -e "*.log"` |
| `-g <glob>` | Search using glob patterns not regex patterns. | `fd -g "*.sh"` |
| `-t <type>` | Filter by type. f(file, d(directory), 1(symlink), x(excutable), e(empty). | `fd -t 1` |
| `-E <pattern>` | Exclude file, directories matching the pattern. | `fd -E "*.log"` |
| `-l` | long form format. | `fd -l` |
| `-0` | Separate results with a null character instead of new line. | `fd -0` |
| `-x <cmd>` | Execute a command on each search result. | `fd -x rm` |
| `-X <cmd>` | Similar to `-x`, but passes all results to command at once. | `fd -X mv` |
| `-j <num>` | Limit the numberof threads used for searching. | `fd -j 3` |
| `-d <depth>` | limit the maximum search depth. | `fd -d 3` |
| `-p` | Search only given path with no search in subdirectories. | `fd -p` |
| `-a` | Print absolute paths instead of relative ones. | `fd -a` |
| `-c <color>` | Control color output. auto, never, always. | `fd -c auto` |
| `-s` | Show symlink instead of resolving them. | `fd -s` |
| `-i` | Case-insensitive search. | `fd -i` |
| `-s` | Case-sensitive search. | `fd -s` |
| `-F` | Treat the pattern as a literal string. | `fd -F` |

### Example

### Find passwd within the directory /etc

```bash
fd passwd /etc
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `fd` | `fd` command. |
| `passwd` | Target pattern. |
| `/etc` | Target location to find pattern. |

## Command: fzf

## Description: Interactive fuzzy file finder

## Syntax

- `fzf`

## Options

| Options | Descriptions | Examples |
|---------|---------------|----------|
| `-q <query>` | Starts with a preloaded query. | `fzf -q "config"` |
| `-e` | Exact match mode. | `fzf -e` |
| `--nth <range>` | Restricts search to specific fields in the UI. | `fzf --nth 2` |
| `--delimiter <str>`| Define a custom field delimiter. | `fzf --delimiter ":"` |
| `-m` | Multi-select mode. | `fzf -m` |
| `-no-sort` | Preserve input order. | `fzf -no-sort` |
| `--no-mouse` | Disable mouse support. | `fzf --no-mouse` |
| `--height <size>` | Show the UI in the smaller window. | `fzf --height 20` |
| `--layout <style>` | Control layout. | `fzf --layout=reverse` |
| `--preview <command>` | Shows a preview window of the command. | `fzf --preview cat {}` |
| `--preview-window <opts>` | Control preview window position and size. | `fzf --preview head -50 {}` |
| `--ansi` | Enable ANSI color codes. | `fzf --ansi` |

### Example

### Finds all files and send them through the fuzzy file finder

```bash
find -type f | fzf
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `find` | `find` command. |
| `-type f` | Directs `find` command to loook in files. |
| `fzf` | Piped Outputs results in the Fuzzy file finder. |

## Command: ranger

## Description Terminal-based file manager that lets you navigate, preview, and manage files efficiently

## Syntax

- `ranger [options] [path]`

### Options

| Options | Descriptions | Examples|
|---------|--------------|---------|
| `-d` or `--debug` | Debug mode. | `ranger -d /etc` |
| `-c` or `--clean` | Start ranger without loading any configuration files. | `ranger -c /etc` |
| `-r` or `--confdir` | Specify an alternate configuration directory. | `ranger -r /etc` |
| `--copy-config` | Copy default config files to config directory for customization. | `ranger --copy-config ~/home/backup` |
| `-f` or `--fail-unless-cd` | Exit if the initial directory chosen is invalid. | `ranger -f /backup` |
| `-p` or `--profile` | Enable profiling. | `ranger -p /backup` |
| `-s` or `--selectfile` | Select a file in the given directory when launching. | `ranger -s /backup` |
| `-w` or `--choosefiles` | Output the chosen file paths to a file instead of running ranger normally. | `ranger -w /backup` |
| `-t` or `--choosefile` | Same as `--choosefiles`, but for a single file. | `ranger -t /backup` |
| `-m` or `--choosefile-multiple` | Same as `--choosefile` but allows multiple files. | `ranger -m /backup` |
| `-q` or `--list-unused-keys` | List all keybindings that aren't mapped in the current configuration. | `ranger -q /backup` |

### Keybindings

| Keybindings | Descriptions |
|-------------|--------------|
| `h` | Go to parent directory. |
| `l` or `Enter` | Enter directory. |
| `j` | Move down. |
| `k` | Move up. |
| `/` | Search. |
| `y` | Yank file path. |
| `p` | Paste. |
| `d` | Delete. |
| `r` | Rename. |
| `:` | Command mode. |
| `q` | Quit. |
  
### Example

### Show a specific file

```bash
ranger -t file1.txt
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `ranger` | File Manager Command. |
| `-t` | Directs output to a specific file. |
| `file1.txt` | Target file. |

# Command: zoxide

## Description: A smarter `cd` command. Aliases include `z` and `zi`

## Syntax

- `z [OPTIONS] [KEYWORD]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `z [query]` | Jumps to the highest-rainked directory that matches your search. | `z projects` |
| `-i` or `--interactive` | Opens fuzzy selector loop. | `z -i projects` |
| `-l` or `--list` | Show all matching paths instead of jumping. | `z -l projects` |
| `-s` or `--score` | Along with list, display frequency. | `z -s projects` |
| `-t` or `--type<dir/file>` | Filter by directory or file type. | `z -t f projects` |
  
### Example

### Show frequency of projects

```bash
z -s projects
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `z` | `zoxide` command. |
| `-s` | To show the frequency of usage. |
| `projects` | Queried keyword. |

## Command: exa

## Description: Modern `ls` command

## Syntax

- `exa [options] [path]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-l` | Long format. | `exa -l` |
| `-a` | Show hidden files. | `exa -a` |
| `-la` or `-al` | Combine long format and hidden files. | `exa -la` |
| `-1` | List one file per line. | `exa -l` |
| `-s` | Sort by the file size. | `exa -s` |
| `-s name` | Sort by name. | `exa -s backup` |
| `-s modified` | Sort by modification time. | `exa -s` |
| `-r` | Reverse the sort order. | `exa -r` |
| `-T` | Display a tree view of directories. | `exa -T` |
| `-L <num>` | Limit depth of recursion in tree view. | `exa -L 4` |
| `--git` | Show Git status for files. | `exa --git` |
| `-@` | Show extended attributes. | `exa -@` |
| `--icons` | Show file-type icons.| `exa --icons` |

### Example

### Show long form with hidden files in a tree structure of directory

```bash
exa -la -T /etc
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `exa` | exa command. |
| `-l` | Long format. |
| `-a` | Show hidden files. |
| `-T` | Put in tree viewing form. |
| `/etc` | Target directory. |

# Command: shred

## Description: Secure file deletion (overwrite before delete)

## Syntax

- `shred [options] [file]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-f` | Change Permissions if neccessary to allow writing | `shred -f secret.txt` |
| `-n<iterations>`or`--iterations=<iterations>` | Number of overwrite passes (default is 3) | `shred -n 5 password_list.txt` |
| `-z`or`--zero` | Add a final overwrite with zeros to hide shredding (makes file look "empty") | `shred -z secret.txt` |
| `s<size>`or`--size=<size>` | Shred only part of a file (useful if you know sensitive data only lives in a segment) | `shred -s 1M bigfile.log` |
| `-u`or`--remove[=HOW]` | Remove file after shredding | `shred -u secret.txt` |
| `-v` | Verbose mode | `shred -v -n 7 secret.txt` |
| `--random-source=<file>` | Specify a source of random data(default = /dev/urandom/) | `shred --random-source=/dev/random secret.txt` |

### Examples

```bash
shred -u -n 5 secrets.txt
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `shred` | File deletion command |
| `-u` | Remove file after shredding it | 
| -n 5` | Directs to do 5 shred passes over the file |
| `secrets.txt` | Target file to shred |

# Command: vidir

## Description: Edit directory filenames in bulk using your editor

## Syntax

- `vidir [Options] [directory] [file...]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------}
| `-v` | Verbose mode | `vidir -v /home/name/projects |
| `-c` | Create mode | `vidir -c /tmp` |

### Examples

```bash
vidir ~/Downloads
```

| Breakdown | Description |
|-----------|-------------|
| `vidir` | File manipulator command |
| `~/Downloads` | Target Directory |
