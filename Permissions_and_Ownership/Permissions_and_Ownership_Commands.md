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

Owner = username or ID
Group = group name or GID
File = file or directory to modify

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-R` |         Recursively: apply to all files in subdirs 
-v.          Verbose: show what changed
—reference=RFILE
               Sets owner/group same as RFILE

### Examples
chown jake file.txt	Change owner to jake.
chown :admins file.txt	Change group to admins.
chown jake:admins file.txt	Change owner to jake, group to admins.
chown jake: file.txt	Change owner to jake, group unchanged.


# Command: chgrp

## Description:

## Syntax

- `chgrp [options] group file`

Group = target group
File = file/directory to change

### Options
- * same as chmod and chown

### Examples

chgrp staff file.txt	Change group to staff.
chgrp -R staff /project	Recursively change group to staff.

# Command: umask

## Description: sets default file permissions for newly created files and directories

## Syntax

- `umask [OPTIONS] [MASK]`

## Options

(none)	Shows the current mask in octal form.
-S	Shows the mask in symbolic form.


# Command: stat

## Description:

## Syntax

### Options

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

## Descriptions:

## Syntax

### Options

### Examples