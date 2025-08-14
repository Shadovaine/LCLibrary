# File Permission and Ownership

## Description: Commands involved in viewing, setting, and modifying permissions and ownership

## Table of Contents

- `Permmission Notation Reference`
- `chmod`
- `chown`
- `chgrp`
- `umask`
- `stat`
- `namei`
- `id`
- `groups`
- `setfacl`
- `getfacl`
- `lsattr`
- `chattr`

## MODE Description: persmission you want to set (symbolic or numeric)

## Symbolic Notation

## Format: [ugoa][+0=][rwx]

| Symbol | Meaning |
|--------|---------|
| `u` | User (owner of the file) |
| `g` | Group(users in the file's group) |
| `o` | Others(all other users) |
| `a` | All (u+g+o) |
| `+` | Add permission |
| `-` | Remove permission |
| `=` | Set exactly these permissions |
| `r` | Read |
| `w` | Write |
| `x` | Execute |

## Octal (Numeric) Notation

## Format: [owner][group][others]

| Number | Permission | Binary Equivalent |
|--------|------------|-------------------|
| `4` | Read(r) | `100` |
| `2` | Write(w) | `010` |
| `1` | Execute(x) | `001` |
| `0` | No permission | `000` |
| `7` | Read + Write + Execute | `111` |
| `6` | Read + Write | `110` |
| `5` | Read + Execute | `101` |
| `3` | Write + Execute | `011` |

# Command: chmod

## Description: Used to set or modify who can read, write, or execute a file

## Syntax

- `chmod [options] MODE file`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-R` | Recursively change permissions for directories and their contents | `chmod -R 755 /var/www` |
| `-v` | Verbose output- shows changes made | `chmod -v 644 file.txt` |
| `-c` | Like `-v`, but only reports changes actually made | `chmod -c 600 secret.txt` |
| `—reference=RFILE | Set permissions to match another file | `chmod --reference-template.txt newfile.txt` |
| `--preserve-root` | Do not operate recursively on / | `chmod --preserve-root -R 755 /` |

### Examples

```bash
chmod u+s myprog
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `chmod` | Permission command |
| `u+s` | Setuid command |
| `myprog` | specified directory to set user ID |

# Command: chown

## Description: Command to set, view and modify ownership of a file

## Syntax

- `chown [options] [owner] [:[group]] file`

## chown Syntax Breakdown

| Breakdown | Description |
|-----------|-------------|
| `Owner` | New file owner (username or UID) |
| `Group` | New group (group name or GID) |
| `:group` | If only group is given, only the group changes |
| `Owner:` | If only owner is given, only the owner changes |

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-c` | Report when a change is made | `chown -c name file.txt` |
| `-f` | Suppress most error messages | `chown -f name file.txt` |
| `-v` | Report for every file processed | `chown -v name file.txt` |
| `--dereference` | Act on the referenced file | `chown --dereference name symlink.txt` |
| `-h` | Affect the symlink itself, not the target file | `chown -h name symlink.txt` |
| `-R` | Recursively: apply to all files and directories | `chown -R owner:group /project` |
| `--from=CURRENT_OWNER:CURRENT_GROUP` | Change ownership only if the current owner and group match | `chown --from=olduser:oldgroup name:newgroup file.txt` |
| `—reference=RFILE` | Sets ownership to match another file's owner/group | `chown --reference=template.txt file.txt` |

### Examples

### Change owner to name

```bash
chown name file.txt
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `chown` | Perm and Owner Command |
| `name` | New name for file |
| `file.txt` | Target file being changed |

# Command: chgrp

## Description: Command to set, view, or modify group settings

## Syntax

- `chgrp [options] group file`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-c` | Report only when a change actually occurs | `chgrp -c name file.txt` |
| `-f` | Suppress most error messages | `chgrp -f name file.txt` |
| `-v` | Report every file processed every if no change was made | `chgrp -v name file.txt` |
| `-R` | Change group ownership for directories and their contents recursively | `chgrp -R name /project` |
| `-H` | Follow symbolic links given on the command line when using -R | `chgrp -RH name /project` |
| `-h` | Affect the symlink iteself instead of the it points to | `chgrp -h name symlink.txt` |
| `-L` | Follow all symbolic links when using -R | `chgrp -RL name /project` |
| `-P` | Never follow symbolic links when using -R | `chgrp -RP name /project` |
| `-reference=RFILE` | Set group ownership to match another file's group | `chgrp --reference=template.txt file.txt` |

### Examples

### Change group to staff

```bash
chgrp staff file.txt 
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `chgrp` | Perm and Owner Command | 
| `staff` | New name for file |
| `file.txt` | Target file |

# Command: umask

## Description: sets default file permissions for newly created files and directories

## Common umask Values

| Umask | File Perms | Dir Perms | Description |
|-------|------------|-----------|-------------|
| `000` | `666` | `777` | Everyone has full access (umask default) |
| `022` | `644` | `755` | Default for most systems |
| `027` | `640` | `750` | No access for others |
| `077` | `600` | `700` | Owner-only access |

## Syntax

- `umask [OPTIONS] [MASK]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `(none)` | Shows the current umask in octal form | `umask` |
| `-S` | Shows the current umask in symbolic form | `umask -S` |
| `Set umask (octal)` | Sets the umask directly using octal numbers | `umask 0022` |
| `Set umask (symbolic)` | Sets the umask using symbolic notation | `umask u=rwx,g=rx,o=rx` |
| `Temporary umask` | Used in the same shell session; resets after logout | `umask 0007` |
| `Persisenet umask` | No direct flag - set it in shell startup files to make it permanent | `echo "umask 0027" >> ~/.bashrc source ~/.bashrc` |

### Examples

# Command: stat

## Description: Display detailed file/filesystem information. It shows metadata such as size, permissions, ownership, timestamps, nad more

## Syntax

- `stat [OPTIONS] FILE`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `no options` | Returns the default output | `stat file.txt` |
| `-L` | Follow symlinks and show info about the target file | `stat -L symlink.txt` |
| `-f` | Display filesystem infomation | `stat -f /home` |
| `-c` | custom output format | `stat -c "%n %s" file.txt` |
| `--print=FORMAT` | like `--format` but without automatically adding a newline | `stat --print="Size: %s bytes" file.txt` |

### Common Format Sequences

| Code | Meaning |
|------|---------|
| `%n` | File name |
| `%s` | Size in bytes |
| `%F` | File type |
| `%a` | Access rights in octal |
| `%A` | Access rights in human-readable |
| `%u` | User ID of owner |
| `%U` | User name of owner |
| `%g` | Group ID of owner |
| `%G` | Group name of owner |
| `%x` | Last access time |
| `%y` | last modification time |
| `%z` | Last change time |
| `%d` | Birth time |
| `%i` | Inode Number |
| `%h` | Number of hard links |

### Examples

# Command: namei

## Description: Resolves and displays each component of a file path, it shows how the system interprets directories, symlinks, and files along the path

## Syntax

- `namei [Options] [File path]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-l` | Show long listing | `namei -l /etc/passwd` |
| `-m` | Show mode bits for each component | `namei -m /etc/passwd` |
| `-o` | Show owner and group for each component | `namei -o /etc/passwd` |
| `-v` | Vebose Output | `namei -v /etc/passwd` |
| `-x` | Show mount points | `namei -x /etc/passwd` |
| `-n` | Do not follow symlinks | `namei -n /etc/passwd` |
| `-a` | Show all components including `.` and `..` | `namei -a /etc/passwd` |

### Examples

### Show owner and group for each component

```bash
namei -o /tmp/test
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `namei` | Perm and Owner Command |
| `-o` | Show owner and group for each component |
| `/tmp/test` | Specified location |

# Command: id

## Description: Displays user and group identity information for the current or specified user, including user ID (UID), group ID (GID), and group memberships

## Syntax

- `id [options] [username]`

### Options

| Option      | Description                                      | Example                      |
|-------------|--------------------------------------------------|------------------------------|
| (none)      | Show user and group info for current user        | `id`                         |
| `username`  | Show info for specified user                     | `id jake`                    |
| `-u`        | Show only the user ID                            | `id -u`                      |
| `-g`        | Show only the group ID                           | `id -g`                      |
| `-G`        | Show all group IDs                               | `id -G`                      |
| `-n`        | Print name instead of number (use with -u, -g, -G)| `id -un`                     |
| `-r`        | Print real ID instead of effective ID (use with -u, -g, -G) | `id -ur`            |
| `-Z`        | Show SELinux security context                    | `id -Z`                      |
| `-a`        | (Obsolete, ignored)                              | `id -a`                      |

### Examples

```bash
id name
```

### Breakdown 

| Breakdown | Description |
|-----------|-------------|
| `id` | Perm and Owner command |
| `name` | Target user |

# Command: groups

## Description: Displays the group memberships for the current user or a specified user

## Syntax

- `groups [username]`

### Options

| Option      | Description                                 | Example           |
|-------------|---------------------------------------------|-------------------|
| (none)      | Show groups for current user                | `groups`          |
| `username`  | Show groups for specified user              | `groups jake`     |

### Examples

```bash
groups name
```

### Breakdown 

| Breakdown | Description |
|-----------|-------------|
| `groups` | Perm and Owner Command |
| `name` | Target user |

# Command: setfacl

## Description: Sets Access Control Lists (ACLs) for files and directories, allowing fine-grained permission management beyond standard Unix permissions

## Syntax

- `setfacl [options] [acl] file`

### Options

| Option | Description | Examples |
|--------|-------------|----------|
| `-m`| Modify ACL by adding or changing permissions | `setfacl -m u:jake:rwx file.txt` |
| `-x` | Remove an entry from the ACL | `setfacl -x u:jake file.txt` |
| `-b` | Remove all ACL entries (reset to default) | `setfacl -b file.txt` |
| `-k` | Remove default ACLs | `setfacl -k dir/` |
| `-R` | Apply changes recursively to directories | `setfacl -R -m u:jake:rwx dir/`|
| `-d` | Set default ACLs for directories | `setfacl -m d:u:jake:rwx dir/`|
| `--set` | Set ACLs from a string, replacing existing entries  | `setfacl --set u::rw-,g::r--,o::r-- file.txt` |
| `--set-file`| Set ACLs from a file | `setfacl --set-file=acls.txt file.txt`  |

### Examples

### Remove a user from the ACL

```bash
setfacl -x u:name file.txt
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `setfacl` | Perm and Owner Command |
| `-x` | Removes a user from the ACL |
| `u:name` | Target user to remove |
| `file.txt` | Target file |

# Command: getfacl

## Description: Displays the Access Control Lists (ACLs) for files and directories, showing detailed permissions for each user and group

## Syntax

- `getfacl [options] file`

### Options

| Option      | Description                                         | Example                       |
|-------------|-----------------------------------------------------|-------------------------------|
| (none)      | Show ACLs for a file or directory                   | `getfacl file.txt`            |
| `-R`        | Recursively list ACLs for directories and contents   | `getfacl -R dir/`             |
| `--absolute-names` | Print absolute pathnames                      | `getfacl --absolute-names file.txt` |
| `--tabular` | Output in tabular format (if supported)             | `getfacl --tabular file.txt`   |

### Examples

### Show ACLs for target directory

```bash
getfacl file.txt
```

### List ACLs for specified directory

```bash
getfacl -R /var/log
```

# Command: lsattr

## Description: Lists file attributes on a Linux filesystem, showing special flags such as immutable, append-only, and others

## Syntax

- `lsattr [options] [files]`

### Options

| Option      | Description                                         | Example                       |
|-------------|-----------------------------------------------------|-------------------------------|
| (none)      | List attributes for files in current directory      | `lsattr`                      |
| `-a`        | List all files, including hidden files              | `lsattr -a`                   |
| `-R`        | Recursively list attributes in directories          | `lsattr -R /home/user`        |
| `-d`        | List attributes of directories themselves           | `lsattr -d /home/user`        |
| `-v`        | List file version/generation number                 | `lsattr -v file.txt`          |
| `-V`        | Show program version                                | `lsattr -V`                   |

### Examples

### List all files including hidden files

```bash
lsattr -a
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `lsattr` | Perm and Owner Command |
| `-a` | List all files, including hidden files |

# Command: chattr

## Description: Change file attributes on a Linux filesystem, such as making files immutable, append-only, or setting other special flags

## Syntax

- `chattr [options] [attributes] file`

### Options

| Option      | Description                                         | Example                       |
|-------------|-----------------------------------------------------|-------------------------------|
| (none)      | Change attributes for a file                        | `chattr +i file.txt`          |
| `-R`        | Recursively change attributes in directories         | `chattr -R +a /var/log`       |
| `-V`        | Show program version                                | `chattr -V`                   |
| `-f`        | Suppress most error messages                        | `chattr -f +i file.txt`       |
| `-v version`| Set the file's version/generation number            | `chattr -v 2 file.txt`        |

### Examples

### make file immutable

```bash
chattr +i file.txt
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `chattr` | Perm and Owner Command |
| `+i` | Directs to make file immutable |
| `file.txt` | Target file |

### Make all files in /var/log append-only

```bash
chattr -R +a /var/log
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `chattr` | Perm and Owner Command |
| `-R` | Directs to make changes recursively |
| `+a` | Directs to make file append-only |
| `/var/log` | Target location |


