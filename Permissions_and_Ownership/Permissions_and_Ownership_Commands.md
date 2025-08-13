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

# Permission Notation Reference

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
| `-v` | Report for every file processed | `chown -v name file.txt |
| `--dereference` | Act on the referenced file | `chown --dereference name symlink.txt` |
| `-h` | Affect the symlink itself, not the target file | `chown -h name symlink.txt` |
| `-R` | Recursively: apply to all files and directories | `chown -R owner:group /project` |
| `--from=CURRENT_OWNER:CURRENT_GROUP` | Change ownership only if the current owner and group match | `chown --from=olduser:oldgroup name:newgroup file.txt` |
| `—reference=RFILE` | Sets ownership to match another file's owner/group | `chown --reference=template.txt file.txt` |

### Examples
chown jake file.txt	Change owner to jake.
chown :admins file.txt	Change group to admins.
chown jake:admins file.txt	Change owner to jake, group to admins.
chown jake: file.txt	Change owner to jake, group unchanged.


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

chgrp staff file.txt	Change group to staff.
chgrp -R staff /project	Recursively change group to staff.

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

## Description:

## Syntax

### Options

### Examples

# Command: id

## Description:

## Syntax

### Options

### Examples

# Command: groups

## Description:

## Syntax

### Options

### Examples

# Command: setfacl

## Description:

## Syntax

### Options

### Examples

# Command: getfacl

## Description:

## Syntax

### Options

### Examples

# Command: lsattr

## Description:

## Syntax

### Options

### Examples

# Command: chattr

## Description:

## Syntax

### Options

### Examples