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



## Command: ls 
## Descriptions: Lists files in a directory

## Syntax
- `ls [option] [directory]`

### Option
| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-a` | Show all files (include hidden ones). |
| `-l` | Long listing format. |
| `-h` | Human-readable file sizes. |
| `-R` | Recursively list subdirectories. |
| `-S` | Sort by file sizes. |
| `-A` | Show all files except `.` and `..`. |
| `-d` | List directories themselves. |
| `-F` | Append `/` to directories, `*` to executables, `@` to symlinks. |
| `-t` | Sort by modification time. |
| `-r` | Reverse the sort order. | 
| `-1` | Force one entry per line. |
| `-i` | Show the inode number of each file. |
| `-p` | Append `/` to directories similar to `-F`. |
| `-g` | Long listing format without showing owner. |
| `-G` | Suppress group information in long listing format. |
| `-q` | Show non-printable characters as `?`. |
| `-X` | Sort by file extension. |
| `--color`:  Colorize the output. |
| `--group-directories-first`:  List directories before files. |

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
| `/Desktop/profile` | Target Directory to change to `/var/log`. |


   
## Command: pwd 
## Description: Print working directory

## Syntax
- `pwd [options]`

### Options
| Options | Descriptions | Examples|
|---------|--------------|---------|
| `p` | Shows physical path ( resolves symlink). |
| `-L` | Show the logical path. |
| `--help` | Display help for the command. |
| `--version` | Shows version information. |
  
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
| `-p` | Create parent directories as needed. |
| `-v` | Shows created directories (verbose). |
| `-m` | Set permissions when creating the directory. |
| `--help` | Display help information.|
| `--version` |Show version information. |
  
### Examples

### Create a new directory along with parent directories and output the detailed locations.
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

### **Options**
| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-ignore-fail-on-non-empty` | Ignore errors for non-empty dirs. |
| `p` | Remove the directory and its parent directories if they become empty. |
| `-v` | Verbose mode. |
| `--help` | Display help information. |
| `--version` | Show version informawtion. |

### **Example**

### **Remove a directory**
```bash
rmdir empty_folder
```

### **Breakdown**
| Breakdown | Description |
|-----------|-------------|
| `rmdir` | Command to remove directory. |
| `empty_folder` | Name of directory to be removed. |



## Command: cp 
## Description: Makes a copy of a file or directory to destination location. It leaves an original copy in source location.

## Syntax
```bash
cp [options] source destination
```

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

### Copy a file into another directory:
```bash
cp file.txt backup/
```

### Breakdown
| Breakdown | Description |
|-----------|-------------|
| `cp` | Copy command. |
| `file.txt' | Source file to copy. |
| `backup/` | Destination location for new copy. |
  
### Copy a directory recursively with verbose output:
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

### Prompt before overwriting a file:
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
| `-i` | Prompt before overwrite. |
| `-v` | Verbose output. |
| `-u` | Move only if source is newer. |
| `-f` | Force move. |
| `-n` | Never overwrite an existing file. |
| `-t <dir>` | Specify the target directory explicitly. |
| `--backup[CONTROL]` | Make a backup of each destination file. |
| `--strip-trailing-slashes` | Removes trailing slashes from source arguments. |

### Example

### Prompt user before moving file then show detailed path of new location.
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
## Description: Removes files or directories. 

## Syntax
- `rm [options] target`

### Options
| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-r` | Remove directories and contents recursively. |
| `-f` | Force deletion (ignore errors/prompts). |
| `-i` | Prompts before each deletion. |
| `-v` | Verbose mode. |
| `-I` | Less intrusive interactive mode. |
| `-d` | Remove empty directories. |
| `--preserve-root` | Prevents rm from operating recursively. |
| `--no-preserve-root` | Removes the protection from \. |
| `--one-file-system` | When deleting recursively, skip files on other file systems. |

### Example

### Remove all directories and contents and force deletion on target directory.
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
| `-c` or `--no-create` | Don’t create file if it doesn’t exist. |
| `-a` | Change only the access time of the file. |
| `-m` | Changes only the modification time of the file. |
| `-d <time>` | Set a specific date/time instead of using the current time. |
| `-t <stamp>` | Set a specific timestamp.
| `-r <file>` | Use the timestamp from another file instead of the current time. |

### Example

### Create a file.
```bash
touch dragon.txt
```

### Breakdown
| Breakdown | Description |
| `-touch` | Create a file Command. |
| `dragon.txt` | Name of new file. |


## Command: echo
## Description: Print what is in the string" ".

## Syntax
-`echo [options] [string]`

### Options
| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-n` | Don’t print newline at end. |
| `-e` | Enable interpretation of escapes. |
| `-E` | Disable interpretation of escape sequence. |

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
| `"Watcher" | Prints this part of the string on first line. |
| `\n` | Directs everything after it to print on a new line. |
| `"mode"` | Rest of string prints on a new line. |



## Command: find
## Description: Searches files and directories.

## Syntax
- `find [PATH] [OPTIONS] [EXPRESSION]`

### Options
| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-name` | Match filenames. |
| `-type` | Specify type (f for file, d for dir). |
| `-size` | Search by size ( e.g +10m, -1G). |
| `-exec` | Execute a command on found items. |
| `-mtime` | Modified in last N days. |
| `-atime` | Accessed in last N days. |
| `-print` | Print full path of each file. |
| `-perm` | World writable (others have permission to write). |

### Examples

### Remove all log files found in /var/log:
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
## Description: Displays directory structure in a tree like form.

## Syntax
- `tree [OPTIONS] [DIRECTORY]`

### OPTIONS
| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-a` | Show all hidden files. |
| `-d` | List directories. |
| `-L <num>` | Limit display to a specific number of directory levels. |
| `-f` | Print full path prefix for each file. |
| `-F` | Append `/` to directories, `*` to executables, @ to symlinks. |
| `-p` | Print file permissions. |
| `-u` | Print the username of the file owner. |
| `-g` | Print the group name of the file owner. |
| `-s` | Print file sizes in bytes. |
| `-h` | Print file sizes in human readable format. |
| `-P <pattern>` | Display only files matching a wildcard pattern. |
| `-I <pattern>` | Exclude files or directories matching a wildcard pattern. |
| `-C` | Enable colorized output. |
| `-n` | Disable colorized output. |
| `-q` | Print non-printable characters as `?`. |
| `--du` | Print directory sizes. |
| `--prune` | Prune empty directories from the output. |
| `--dirsfirst` | List directories before files. |
  
### Example

### Show all files including hisden ones in a tree structure.
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
| `-i` | Case-insensitive search. |
| `-c` | Prints out the number of matches instead of listing them. |
| `-n NUM` | Will only print out the desired amount inputed. |
| `-r REGEX` | Searches using regular expression. |
| `-w` | Matches whole words. |
| `-b` | Matches only the basename. |
| `-1 NUM` | Limits results to stated amount. |
| `-0` | Output results separated by a null character instead of a new line.
| `-q` | Quiet mode.
| `-d DBPATH` | Uses a specific database and not the default database. |
| `-e` | Only prints existing files. |
| `-S` | Shows database statistics. |
| `-V`:  Shows version information. |

### Example

### Print out the top 10 results and make the search case-insensitive.
```bash
locate -i -n 10 readme
```

### Breakdown
| Breakdown | Description |
| `locate` | `locate` command. |
| `-i` | Make the search case-insensitive. |
| `-n 10` | Sets the amount of lines to print out to 10 lines. |
| `readme` | target pattern. |


## Command: ripgrep(rg)
## Descriptions: Lightning-fast file search Command.

## Syntax
- `rg [pattern] [path]`

### Options
| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-i` | Case-insensitive. |
| `-n` | Show line numbers. |
| `-l` | List filenames only. |
| `-S` | Smart case: case-insensitive unless the oattern has upper cass letters. |
| `-F` | Treat the pattern as a literal string. |
| `-e <pattern>` | Explicitly specific a search pattern. |
| `-w` | Match whole words only. |
| `-x` | Match the entire line. |
| `-g <glob>` | Includes only files matching the glob pattern. |
| `-T <ext>` | Excludes a certain file type. |
| `t <type>` | Searches only files of a certain type. |
| `u` | Search hidden and ignored files. |
| `uu` | Seach hidden and ifnored files. |
| `iglob <pattern>` | Case-insensitive glob matching. |
| `-hidden` | Include hidden files or directories. |
| `-n` | Show line numbers. |
| `H` | Always show the filename in results. |
| `l` | Print only filenames with matches. |
| `-L` | Print only filenames without matches. |
| `-o` | Show onlythe matching part of each line. |
| `-v` | Invert match. |
| `-c`:  Show the count of matches per file. |
| `--stats | Show search statistics. |
| `-r <replacements>` | Use regex replacements. |
| `-m <NUM>` | Limit the number of matches. |
| `--max-columns <NUM>` | Truncate long lines to the column width in the output. |
| `--max-depth <NUM>` | Limit search depth. |
| `follow` | Follow symlink. |
| `-no-messages` | Suppress error messages. |
| `--color <when>` | Control color. always, never, auto. |
| '--heading` | Shows file names as headings. |
| `--no-heading` | Disables headings. |
| `--json` | Output results in JSON format. |
| `--pretty` | Pretty print results with colors and context. |
| `-A <NUM>` |Show NUM lines after each match. |
| `-B <NUM>` | Show NUM lines before each match. |
|`-C <NUM>` | Show NUM lines of context. |

### Example

```bash
rg "sudo" /etc
```

### Breakdown
- `rg`:  `rg` command
- `"sudo"`:  Selected pattern.
- `/etc`:  Targeted location.



## Command: fd
## Description: `find` command alternative

## Syntax
- `fd [pattern] [path]`

### Options
| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-e` | File extension filter (e.g., -e txt). |
| `-H` | Include hidden files. 
| `-t f|d` | Search for files or directories. |
| `-I` | Include ignored files. |
| `-u` | Search unrestricted files including hidden and ignored files. |
| `-e <ext>` | Search only files with the spwcific extension. |
| `-g <glob>` | Search using glob patterns not regex patterns. |
| `-t <type>` | Filter by type. f(file, d(directory), 1(symlink), x(excutable), e(empty). |
| `-E <pattern>` | Exclude file, directories matching the pattern. |
| `-l` | long form format. |
| `-0` | Separate results with a null character instead of new line. |
| `-x <cmd>` | Execute a command on each search result. |
| `-X <cmd>` | Similar to `-x`, but passes all results to command at once. |
| `-j <num>` | Limit the numberof threads used for searching. |
| `-d <depth>` | limit the maximum search depth. 
| `-p` | Search only given path with no aearch in subdirectories. |
| `-a` | Print absolute paths instead of relative ones. |
| `-c <color>` | Control color output. auto, never, always. |
| `-s` | Show symlink instead of resolving them. |
| `-i` | Case-insensitive search. |
| `-s` | Case-sensitive search. |
| `-F` | Treat the pattern as a literal string. |

### Example

### Find passwd within the directory /etc.
```bash
fd passwd /etc
```

### Breakdown
| Breakdown | Description |
|-----------|-------------|
| `fd` | `fd' command. |
| `passwd` | Target pattern. |
| `/etc` | Target location to find pattern. |



## Command: fzf
## Description: Interactive fuzzy file finder

## Syntax
- `fzf`

## Options
| Options | Descriptions | Examples |
|---------|---------------|----------|
| `-q <query>` | Starts with a preloaded query. |
| `-e` | Exact match mode. |
| `--nth <range>` | Restricts search to specific fields in the UI. |
| `--width-nth <range> | Display only specific fields in the UI. |
| `--delimiter <str> | Define a custom field delimiter. |
| `-m` | Multi-select mode. |
| `-no-sort` | Preserve input order. |
| `--no-mouse` | Disable mouse support. |
| `--height <size> | Show the UI in the smaller window. |
| `--layout <style> | Control layout. |
| `--preview <command>` | Shows a preview window of the command. |
| `--preview-window <opts> | Control preview window position and size. |
| `ansi` | Enable ANSI color codes. |
| `--no-clear` | Don't clear the screen when fzf exits. |
| `--print-query` | Print the sesrch query on exit. |
| `--print0` | Output selected items seperated by a null character. |
|`--bind <key:action> | Create custom key bindings. |
| `-toggle-sort` | Keybinding to toggle sort. |
| `--expect <keys>` | Returned the key pressed before selection. |

### Example

### Fins all files and send them through the fuzzy file finder.
```bash
find -type f | fzf
```

### Breakdown
| Breakdown | Description |
|-----------|-------------|
| `find` | `find` command. |
| `-type f` | Directs `find` command to loook in files. |
| `|` | `pipe` command thats say it takes output from `find` and will send it through `fzf`.
| `fzf` |  Outputs results in the Fuzzy file finder. |



## Command: ranger
## Description Terminal-based file manager that lets you navigate, preview, and manage files efficiently.

## Syntax
- `ranger [options] [path]`

### Options
| Options | Descriptions | Examples|
| `-d` or `--debug` | Debug mode. |
| `-c` or `--clean` | Start ranger without loading any configuration files. |
| `-r` or `--confdir` | Specify an alternate configuration directory. |
| `--copy-config` | Copy default config files to config directory for customization. |
| `-f` or `--fail-unless-cd` | Exit if the initial directory chosen is invalid. |
| `-p` or `--profile` | Enable profiling. |
| `-s` or `--selectfile` | Select a file in the given directory when launching. |
| `-w` or `--choosefiles` | Output the chosen file paths to a file instead of running ranger normally. |
| `-t` or `--choosefile` | Same as `--choosefiles`, but for a single file. |
| `-m` or `--choosefile-multiple` | Same as `--choosefile` but allows multiple files. |
| `-q` or `--list-unused-keys` | List all keybindings that aren't mapped in the current configuration. |

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

### Show a specific file.
```bash
ranger -t file1.txt
```

### Breakdown
| Breakdown | Description |
|-----------|-------------|
| `ranger` | File Manager Command. |
| `-t` | Directs output to a specific file. |
| `file1.txt` | Target file. |


## Command: zoxide
## Description: A smarter `cd` command. Aliases include `z` and `zi`. 

## Syntax
- `z [OPTIONS] [KEYWORD]`

### Options
| Options | Descriptions | Examples |
|---------|--------------|----------|
| `z [query]` | Jumps to the highest-rainked directory that matches your search. |
| `-i` or `--interactive` | Opens fuzzy selector loop. |
| `-l` or `--list` | Show all matching paths instead of jumping. |
| `-s` or `--score` | Along with list, display frecency. |
| `-t` or `--type <dir|file>` | Filter by directory or file type. |
  
### Example

### Show 
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
| `-l` | Long format. 
| `-a` | Show hidden files. |
| `-la` or `-al` | Combine long format and hidden files. |
| `-1` | List one file per line. |
| `-s` | Sort by the file size. |
| `-s name` | Sort by name. |
| `-s modified` | Sort by modification time. |
| `-r` | Reverse the sort order. |
| `-T` | Display a tree view of directories. |
| `-L <num>` | Limit depth of recursion in tree view. |
| `--git` | Show Git status for files. |
| `-@` | Show extended attributes. |
| `--icons` | Show file-type icons.|

### Example

### Show long form with hidden files in a tree structure of directory.
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





