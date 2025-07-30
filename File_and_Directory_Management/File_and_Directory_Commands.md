# **File and Directory Management**

## Commands for manipulating files and directories

**ls**

**Syntax**
ls [option][directory]

**Option**
-a     Show all files (include hidden ones)
-l     Long listing format
-h     Human-reachable file sizes
-R     Recursively list subdirectories
-S     Sort by file sizes

**Example**
 ls -alh /etc

**cd**

**Syntax**
cd [directory]

**Options**
cd         Go to home directory
cd ~       Same as above
cd -       Switch to previous directory.
cd ..      Move up one level


**Example**
cd /var/log

**pwd**

**Syntax**
pwd [options]

**Options**
-p      Shows physical path ( resolves symlink)

**Example**
pwd -p

**mkdir**

**Syntax**
mkdir [options] directory_name

**Options**
-p      Create parent directories as needed
-v      Shows created directories (verbose)

**Example**
 mkdir -pv /tmp/dragon/nest

**rmdir**

**Syntax**
rmdir [options] directory_name

**Options**
—ignore-fail-on-non-empty      Ignore errors for non-empty dirs 

**Example**
rmdir empty_folder

**cp** 

**Syntax**
cp [options] source destination

**Options**
-r      Copy directories recursively
-u      Copy only if source is newer
-v      Verbose outpost (show what is copied)
-i      Prompt before overwriting

**Example**
cp -ruv /source/dir /backup/dir

**mv** 

**Syntax**
mv [options] source destination

**Options**
-i      Prompt before overwrite
-v      Verbose output
-u      Move only if source is newer

**Example**
 mv -iv file.txt /tmp/

**rm** 

rm [options] target

**Options**
-r      Remove directories and contents recursively
-f      Force deletion (ignore errors/prompts)
-i      Prompts before each deletion.
-v      Verbose output

**Example**
rm -rf /tmp/testdir

**touch**

**Syntax**
touch [options] file_name

**Options**
-c      Don’t create file if it doesn’t exist

**Example**
touch dragon.txt

**Echo**

**Syntax**
echo [options] [string]

**Options**
-n      Don’t print newline at end
-e      Enable interpretation of escapes

**Example**
 echo -e “Watcher\nmode”

**Find**
Search files and directories

**Syntax**
find [PATH] [OPTIONS] [EXPRESSION]

**Options**
-name   Match filenames
-type   Specify type (f for file, d for dir)
-size   Search by size ( e.g +10m, -1G)
-exec   Execute a command on found items
-mtime  Modified in last N days
-atime  Accessed in last N days
-print  Print full path of each file
-perm   World writable (others have permission to write)

**Examples**
find /var/log -name "*.log" -exec rm {} \;

**tree**
shows directory structure in a tree like form

**Syntax**
tree [OPTIONS] [DIRECTORY]

OPTIONS] → Modify the output (like depth, showing hidden files, etc.)
	•	[DIRECTORY] → The directory you want to view. If omitted, defaults to current directory (.).

tree
shows current directory

tree -a
shows all hidden files also


**Locate**
Searches filesystem

**Syntax**
locate [OPTIONS] PATTERN

**Example**
locate passwd find all files named passwd

**ripgrep - aka rg**
Lightning-fast file search

**Syntax**
rg [pattern] [path]

**Options**
-i      Case-insensitive
-n      Show line numbers
-l      List filenames only

**Example**
rg "sudo" /etc

**fd**
 Modern find alternative

**Syntax**
fd [pattern] [path]

**Options**
-e      File extension filter (e.g., -e txt)
-H      Include hidden files
-t f|d  Search for files or directories

**Example**
fd passwd /etc


**fzf**
Interactive fuzzy file finder
Can integrate with vim, tmux, bash or zsh key bindings
Default: pipes input and lets you search interactively

**Syntax**
fzf

**Example**
find -type f | fzf
	
**ranger**
Terminal file manager with previews

**Syntax**
ranger

**Example**
ranger /etc

**zoxide**
Smarter cd command

**Syntax** 
zoxide [dir]

**Example**
z /etc
-	Learns your habits

**exa**
Modern ls replacement with colors & icons
	•	Category: File Listing

 **Syntax**
 exa [options] [path]

**Options**
	•	-l → Long format
	•	-a → Show hidden files
	•	--tree → Directory tree view 

**Example**
exa -la --tree /etc







