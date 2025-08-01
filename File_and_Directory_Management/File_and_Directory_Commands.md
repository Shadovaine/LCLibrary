# **File and Directory Management**

## Commands for manipulating files and directories

## **ls - list**

### **Syntax**
- ls [option][directory]

#### **Option**
- **-a**:     Show all files (include hidden ones)
- **-l**:     Long listing format
- **-h**:     Human-reachable file sizes
- **-R**:     Recursively list subdirectories
- **-S**:     Sort by file sizes

##### **Example**
- ls -alh /etc

##### **Breakdown**
- **ls**:   Command to list contents 
- **-a**:   Tells ls to show all files including the hidden files
- **-l**:   Makes ls to list directory files in long listing format
- **-h**:   Converts the file's raw bites into a human readable format
- **/etc**: Target Directory
'''

## **cd - Change Directory**

### **Syntax**
- cd [directory]

#### **Options**
- **cd**:    Go to home directory
- **cd ~**:  Same as above
- **cd -**:  Switch to previous directory.
- **cd ..**: Move up one level

##### **Example**
- cd /var/log

##### **Breakdown**
- **cd**:       Change directory command
- **/var/log**: Target Directory to change to
'''
   
## **pwd - print working directory**

### **Syntax**
- pwd [options]

#### **Options**
- **-p**:    Shows physical path ( resolves symlink)

#### **Example**
- pwd -p

##### **Breakdown**
- **pwd**:   print working directory command
- **-p**:    Will print the physical path

## **mkdir - make a new directory**

### **Syntax**
- mkdir [options] directory_name

### **Options**
- **-p**:   Create parent directories as needed
- **-v**:   Shows created directories (verbose)

#### **Example**
- mkdir -pv /tmp/dragon/nest

##### **Breakdown**
- **mkdir**: Command to tell system to make a new directory
- **-p**:    Will create parent directories
- **-v**:    Shows all created directories 

## **rmdir - remove a directory**

### **Syntax**
- rmdir [options] directory_name

### **Options**
- **-ignore-fail-on-non-empty**:      Ignore errors for non-empty dirs 

#### **Example**
- rmdir empty_folder

##### **Breakdown**
- **rmdir**:    Command to remove directory
- **empty_folder**: name of directory to be removed

## **cp** 

### **Syntax**
- cp [options] source destination

### **Options**
- **-r**:   Copy directories recursively
- **-u**:   Copy only if source is newer
- **-v**:   Verbose outpost (show what is copied)
- **-i**:   Prompt before overwriting

#### **Example**
- cp -ruv /source/dir /backup/dir

##### **Breakdown**
- **-cp**:   Copy Command
- **-r**:    Causes recursive copying
- **-u**:    Says to only copy if source is newer
- **-v**:    Verbose posting
- **/source/dir**:  Source location
- **/backup/dir**:  Destination Location

## **mv - moves a file** 

## **Syntax**
mv [options] source destination

### **Options**
- **-i**:  Prompt before overwrite
- **-v**:  Verbose output
- **-u**:  Move only if source is newer

#### **Example**
 - mv -iv file.txt /tmp/

##### **Breakdown**
- **mv**:   Move Command
- **-i**:   Verify with user before overwrite
- **-v**:   Verbose output
- **file.txt**:  Source file
- **/tmp/**:     Destination location
  
## **rm - removes files** 

## **Syntax**
rm [options] target

### **Options**
- **-r**:   Remove directories and contents recursively
- **-f**:   Force deletion (ignore errors/prompts)
- **-i**:   Prompts before each deletion.
- **-v**:   Verbose output

#### **Example**
- rm -rf /tmp/testdir

##### **Breakdown**
- **rm**:   Remove command
- **-r**:   Recursive removal
- **-f**:   Forced Deletion
- **/tmp/testdir**:   Target file to be deleted
 
## **touch - create a file**

## **Syntax**
- touch [options] file_name

### **Options**
- **-c**:   Don’t create file if it doesn’t exist

#### **Example**
- touch dragon.txt

##### **Breakdown**
- **touch**:  Create a file Command
- **dragon.txt**:  Name of new file


## **Echo - Print what is in string""**

## **Syntax**
- echo [options] [string]

### **Options**
- **-n**:   Don’t print newline at end
- **-e**:   Enable interpretation of escapes

#### **Example**
 - echo -e “Watcher\nmode”

##### **Breakdown**
- **echo**:  Print Command
- **-e**:    Don't print newline at end
- **"Watcher/nmode"**: String to be printed

## **Find - Searches files and directories**

## **Syntax**
- find [PATH] [OPTIONS] [EXPRESSION]

### **Options**
- **-name**:   Match filenames
- **-type**:   Specify type (f for file, d for dir)
- **-size**:   Search by size ( e.g +10m, -1G)
- **-exec**:   Execute a command on found items
- **-mtime**:  Modified in last N days
- **-atime**:  Accessed in last N days
- **-print**:  Print full path of each file
- **-perm**:   World writable (others have permission to write)

#### **Examples**
- find /var/log -name "*.log" -exec rm {} \;

##### **Breakdown**
- **-find**:    Search Command
- **/var/log**: path to file
- **-name**:    Directs to match a filename
- **"*.log"**:  portion of file name to be searched for
- **-exec**:    says to execute the following command
- **rm**:       Command to be executed
- **{}**:       A placeholder for each file as find command searches each file
- **\;**:       The end of the -exec command
   
## **tree - displays directory structure in a tree like form**

## **Syntax**
- tree [OPTIONS] [DIRECTORY]

### **OPTIONS**
- **-a**:  Show all hidden files

#### **Example**
- tree -a /home
- 
##### **Breakdown**
- **tree**:   Command to create tree form
- **-a**:     show all hidden files
- **/home**:  target directory

## **Locate - Searches filesystem**

## **Syntax**
- locate [OPTIONS] PATTERN

### **Example**
- locate passwd find all files named passwd

## **ripgrep(rg) - Lightning-fast file search Command**

## **Syntax**
- rg [pattern] [path]

### **Options**
- **-i**:      Case-insensitive
- **-n**:      Show line numbers
- **-l**:      List filenames only

#### **Example**
- rg "sudo" /etc

## **fd - find command alternative**

## **Syntax**
- fd [pattern] [path]

### **Options**
- **-e**:   File extension filter (e.g., -e txt)
- **-H**:   Include hidden files
- **-t f|d**:  Search for files or directories

#### **Example**
- fd passwd /etc

## **fzf-Interactive fuzzy file finder**

## **Syntax**
- fzf

### **Example**
- find -type f | fzf

## **ranger - file manager**

## **Syntax**
- ranger

### **Example**
- ranger /etc

## **zoxide - a smarter cd command*

## **Syntax** 
- zoxide [dir]

### **Example**
- z /etc


## **exa - Modern ls command**

## **Syntax**
- exa [options] [path]

### **Options**
- **-l**: Long format
- **-a**: Show hidden files

#### **Example**
- exa -la --tree /etc







