# User and Group Management

## Description: Commands involved adding, removing, and modifying groups and users

## Table of Contents

- `useradd`
- `adduser`
- `usermod`
- `passwd`
- `chage`
- `userdel`
- `deluser`
- `groupadd`
- `newgroup`
- `groupmod`
- `groupdel`
- `gpasswd`
- `groups`
- `whoami`
- `getent`
- `finger`
- `delgroup`

# Command: useradd

## Description: Creates a new user account, assigns home directories, shells, gropus and expiration settings

## Syntax

- `useradd [OPTIONS] USERNAME`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-d`or`--home DIR` | Specify custom home directory | `sudo useradd -d /srv/datauser datauser` |
| `-m`or`--create-home` | Force creation of the user's home directory | `sudo useradd -m name` |
| `-M` | Do not create a home directory | `sudo useradd -M name` |
| `-s`or`--shell SHELL` | Assign login shell | `sudo useradd -m -s /bin/bash devuser` |
| `-u`or`--uid UID` | Set custom user ID | `sudo useradd -m -u 1501 newguy` |
| `-g`or`--gid GROUP` | Assign primary group | `sudo useradd -m -g developers jane` |
| `-G`or`--groups GROUPS` | Assign supplementary groups | `sudo useradd -m -G wheel,developers opsuser` |
| `-N`or`--no-user-group` | Do not create a group with the same name as user | `sudo useradd -N tempuser` |
| `-r`or`--system` | Create a system account | `sudo useradd -r backup` |
| `-e`or`--expiredate DATE` | Set account expiration date (YYYY-MM-DD) | `sudo useradd -m -e 2025-12-31 tempstaff` |
| `-f`or`--inactive DAYS` | Set days after password expires before account is disabled | `sudo useradd -m -f 7 intern` |
| `-c`or`--comment COMMENT` | Add description (stored in /etc/passwd) | `sudo useradd -m -c "QA Tester" qauser` |
| `-k`or`--ske DIR` | Copy files from custom skeleton directory | `sudo useradd -m -k /etc/skel_custom_trainee` |
| `-o`or`--non-unique` | Allow duplicate UID (not recommended) | `sudo useradd -m -u 1001 -o cloneuser` |
| `-p`or`--password PASSWORD` | Set encrypted password (not plain text, must be hashed) | `sudo useradd -m -p "$(openssl passwd -l MyPass123)" secureuser |
| `-D` | Show or change default settings for new user | `sudo useradd -D` |

### Examples

### Create a user with default settings

```bash
sudo useradd name
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Superuser command |
| `useradd` | User command |
| `name` | New user name |

### Create user with home dir and bash shell

```bash
sudo useradd -m -s /bin/bash name
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Superuser command |
| `useradd` | User command |
| `-m` | Directs to force creation of home directory |
| `-s` | Assign login shell |
| `/bin/bash` | Assigned shell |
| `name` | New user account name |

### Create user with specific UID and comment

```bash
sudo useradd -m -u 1500 -c "name"
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Superuser command |
| `useradd` | User command |
| `-m` | Directs to force creation of home directory |
| `-u 1500` | Directs to set a custom UID of 1500 |
| `-c` | Directs to add a comment that is stored in `/etc/passwd` |
| `name` | Specified comment |

### Create user and assign to group “admins”

```bash
sudo useradd -m -G admins name
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Superuser command |
| `useradd` | User command |
| `-m` | Direct to force creation of home directory |
| `-G` | Directos to assign to admins group also |
| `admins` | Specified additional group |
| `name` | New user name |

# Command: adduser

## Description: Frontend shell script to useradd. More user-friendly, interactive than useradd. On RedHat/CentOS it links directly to useradd. Adduser prompts for passwords, full name, sets up home directory, and group memberships

## Syntax

- `adduser [Options] USERNAME`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `--home DIR` | Custom home directory | `sudo adduser --home /srv/name name` |
| `--shell SHELL` | Choose login shell | `sudo adduser --shell /bin/bash name` |
| `--uid UID` | Set custom user ID | `sudo adduser -uid 1502 name` |
| `--gid GID` | Set primary group ID | `sudo adduser --gid 1000 name` |
| `--ingroup GROUP` | Puts user in a specific existing group | `sudo adduser --ingroup developers name` |
| `--extrausers` | Use /var/lib/extrausers DB instead of /etc/passwd | `sudo adduser --extrausers name` |
| `--system` | Create a system account | `sudo adduser --system name` |
| `--disabled-password` | Account with no usable password | `sudo adduser --disabled-password name` |
| `--disabled-login` | Account completely disabled for login | `sudo adduser --disabled-login noname` |
| `--gecos "INFO" | Fill GECOS (comment) field non-interactively | `sudo adduser --gecos "QA Tester" name` |
| `--quiet` | Suppresses log messages | `sudo adduser --quiet noname` |
| `--debug` | show debug info | `sudo adduser --debug name` |
| `--force-badname` | Allow usernames that don't match the normal pattern | `sudo adduser --force-badname noname` |
| `--encrypt-home` | Encrypt user's home directory | `sudo adduser --encrypt-home noname` |


### Examples

### Create dev01 in Bash shell and add to dev groups

```bash
sudo adduser --shell /bin/bash --ingroup devs --gecos "Dev Account" dev01
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Superuser command |
| `adduser` | User command |
| `--shell` | Directs to add to specific shell |
| `/bin/bash` | Specified shell |
| `--ingroup` | Directs to add to a specific group |
| `devs` | Specified group |
| `--gecos` | Directs to add a comment |
| `"Dev Account"` | Specified comment to add |
| `dev01` | New account user name |

### Differences between useradd and adduser

| Characteristic | useradd | adduser |
|----------------|---------|---------|
| Interactive by default | ❌ | ✅ |
| Non-Interactive unless a flag is used | ✅ | ❌ |
| Performs automatic checks and setups | ❌ | ✅ |
| Writes to the file /etc/passwd,/etc/shadow | ✅ | ✅ |

# Command: usermod

## Description: Modify an existing users account

## Syntax

- `usermod [OPTIONS] USERNAME`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-c`or`--comment COMMENT` | Change the comment (GECOS field) | `sudo usermod -c "Project Manager" name` |
| `-d`or`--home HOME_DIR` | Set new home directory (does not move files by default) | `sudo usermod -d /srv/newhome name` |
| `-d`or`--home HOME_DIR -m` | Move old home to new directory | `sudo  usermod -d /srv/newhome -m name` |
| `-f`or`--inactive DAYS` | Days after password expiration until account is disabled | `sudo usermod -f 7 newname` |
| `-g`or`--gid Group` | Change primary group | `sudo usermod -g developers devname` |
| `-G`or`--groups GROUPS` | Change supplementary groups | `sudo usermod -G wheel,noname, usename` |
| `-a`or`--append` | Append to supplementary group | `sudo usermod -a -G docker noname` |
| `-l`or`--login NEW_LOGIN` | Change username | `sudo usermod -l newname oldname` |
| `-L`or`--lock` | Lock the user's password (disable login via password) | `sudo usermod -L guest` |
| `-U`or`--unlock` | Unlock user's password | `sudo usermod -U newname` |
| `-P`or`--password PASSWORD` | Set encrypted password (hash, not plain text) | `sudo usermod -p "$(openssl passwd -l NewPass123)" name` |
| `-s`or`--shell SHELL` | Change user's login shell | `sudo usermod -s /bin/bash name` |
| `-u`or`--uid UID` | Change UID | `sudo usermod -u 1595 name` |
| `-o`or`--non-unique` | Allow duplicate UID (use with -u) | `sudo usermod -u 1001 -o newname` |
| `-R`or`--root CHROOT_DIR` | Apply change inside alternate root directory (useful for chroot) | `sudo usermod -R /mnt/chroot -s /bin/bash noname` |

### Examples

### Change username from “username” to “name”

```bash
sudo usermod -l name username
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Superuser command |
| `usermod` | User command |
| `-l` | Directs to change username |
| `name` | New username |
| `username` | Old username |

### Change user’s shell to zsh

```bash
sudo usermod -s /bin/zsh name
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Superuser command |
| `usermod` | User command |
| `-s` | Change users assigned shell |
| `/bin/zsh` | New shell |
| `name` | Target user account that is getting assigned to a new shell |

# Command: passwd

## Description: Creates a new or change an existing user’s password and update authentication tokens

## Syntax

- `passwd [OPTIONS] [USERNAME]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-d`or`--delete` | Delete the user's password | `sudo passwd -d name` |
| `-e`or`--expire` | Expire the password immediately | `sudo passwd -e name` |
| `-i`or`--inactive DAYS | Set the number of inactive days after password expireation before the account is disabled | `sudo passwd -i 10 name` |
| `-k`or`--keep-token` | Keep non-expired authentication tokens | `sudo passwd -k name` |
| `-l`or`--lock` | Lock the account's password | `sudo passwd -l name` |
| `-u`or`--unlock` | Unlock a locked account | `sudo passwd -u name` |
| `-n`or`--minidays DAYS` | Sets the minimum number of days between password changes | `sudo passwd -n 3 name` |
| `-x`or`--maxdays DAYS` | Set maximum number of days a password is valid | `sudo passwd -x 90 name` |
| `-w`or`--wanrdays DAYS` | Set number of days before expireation that the user is warned | `sudo passwd -w 8 name` |
| `-S`or`--status` | Dsplay password status information for the account | `sudo paswd -S name` |

### Examples

### Change your own password

```bash
passwd
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `passwd` | password command |

### Set password for user "name"

```bash
sudo passwd name
```

### Breakdown

|Breakdown | Description |
|----------|-------------|
| `sudo` | Superuser command |
| `passwd` | password command |
| `name` | specified User Account |

# Command: chage

## Description: Allows user to set minimum and maximum days between password changes, expiration dates, waring periods, and it can display current settings

## Syntax

- `chage [Options] USERNAME`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-d`or`--lastday LAST_DAY` | Sets the date of the last password change | `sudo chage -d 2025-08-22 name` |
| `-E`or`--expiredate DATE` | Sets account expiration date | `suod chage -E 2025-12-31 name` |
| `-I`or`--inactive DAYS` | Sets number of days of inactivity after password expires before the account is locked | `sudo chage -I 4 name` |
| `-m`or`--minidays DAYS` | Sets minimum number of days between password changes | `sudo chage -m 2 name` |
| `-M`or`--maxdays DAYS` | Sets maximum number of days a password is valid | `sudo chage -M 99 name` |
| `-W`or`--warndays DAYS` | Sets number of days before expireation that the user is warned | `sudo chage -W 8 name` |
| `-l`or`--list` | Lists current password aging settings | `chage -l name` |

### Examples

### Reset the clock 

```bash
sudo chage -d 2025-08-23 name
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Superuser command |
| `chage` | Password command |
| `-d` | Directs to set the date for the last password change |
| `2025-08-23` | Specified date |
| `name` | Target user account |

### User Account expires at the end of 2025

```bash
sudo chage -E 2025-12-31 name
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Superuser command |
| `chage` | password command |
| `-E` | Sets account expiration date |
| `2025-12-31` | Specified expiration date |
| `name` | User account |

# Command: userdel

## Description: Delets user account and related files

## Syntax

- `userdel [Options] USERNAME`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-r`or`--remove` | Removes the user's home directory and mail spool in addition to the account | `sudo userdel -r name` |
| `-f`or`--force` | Force removal of the account, kills processes, removes account if user is still logged in | `sudo userdel -f name` |

### Examples

### Delete name's account, home directory, and mail spool

```bash
sudo userdel -r name
```

### Breakdown

| Breakdown | Description | Examples |
|-----------|-------------|----------|
| `sudo` | Superuser command |
| `userdel` | User command |
| `-r` | Directs to remove account, home directory, and mail spool |
| `name` | Specified user account |

# Command: deluser

## Description: Interactive account removal tool. It has more features compared to userdel like removing user from groups, deleting home, purging configs, and other features

## Syntax

- `deluser [Options] USERNAME`
- `deluser [Options] USERNAME GROUP`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `--remove-home` | Deletes the user's home directory and mail spool | `sudo deluser --remove-home name` |
| `--remove-all-files` | Remove all files owned by the user on the system | `sudo deluser --remove-all-files name` |
| `--backup` | Backup user files before deletion | `suod deluser --remove-hom --backup --backup-to /backups name` |
| `--backup-to DIR` | Specifies to backup destination directory | `sudo deluser --remove-all-files --backup --backups name` |
| `--system` | Remove a system user | `sudo deluser --system www-data` |

### Examples

### Remove name and delete name's home directory

```bash
sudo deluser --remove-home name
```

### Breakdown

| Breakdown | Description | 
|-----------|-------------|
| `sudo` | Superuser command |
| `deluser` | User command |
| `--remove-home` | Directs to remove home |
| `name` | Specified user account |

### Remove name and all files across system

```bash
sudo deluser --remove-all-files name
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Superuser command |
| `deluser` | User command | 
| `--remove-all-files` | Directs to remove all files from system |
| `name` | Specified user account |

# Command: groupadd

## Description: Create a new group on system. Used when setting up new teams or assigning users to project groups

## Syntax

- `groupadd [OPTIONS] GROUPNAME`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-f`or`--force` | Does not return error if group already exists | `sudo groupadd -f developers` |
| `-g`or`--gid GID` | Specifies a custom Group ID instead of auto-assigning | `sudo groupadd -g 1500 projectx` |
| `-K`or`--key KEY=VALUE` | Override defaults from `/etc/login.defs` | `sudo groupadd -K GID_MIN=2000 specialgroup` |
| `-o`or`--non-unique` | Allow creation of group with duplicate GID | `sudo groupadd -g 1001 -o dubgroup` |
| `-p`or`--password ENCRYPTED` | Assigns an encrypted password for the group | `sudo groupadd -p "$(openssl passwd -l MyGroupPass)" securegroup` |

### Examples

### Create a group called “admins”

```bash
sudo groupadd admins
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Superuser command |
| `groupadd` | Group command |
| `admins` | Specified group name |

### Create group with specific GID

```bash
sudo groupadd -g 1001 developers
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Superuser command |
| `groupadd` | Group command |
| `-g` | Directs to assign a specific GID |
| `1001` | Selected GID |
| `developers` | Specified group name |

# Command: newgrp

## Description: Allows a user for temporarily switching from one group to another group on the "fly"

## Syntax

- `newgrp [Options] [Group]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-` | Starts a new login shell | `newgrp - developers` |

### Examples

### Switch to another group

```bash
group name
newgrp newname
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `group name` | Login group |
| `newgrp newname` | New group user switched to |

# Command: groupmod

## Description: Modifies existing group's name, change its GID, or update its password

## Syntax

- `groupmod [Options] GROUP`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-g` | Change the group's numeric Group ID | `sudo groupmod -g 1000 developers` |
| `-n`or`--new-name NEW_GROUP` | Rename a group | `sudo groupmod -n devs developers` |
| `-o`or`--non-unique` | Allow a duplicate GID | `sudo groupmod -g 1001 -o duplicategroup` |
| `-p`or`--password ENCRYPTED` | "$(openssl passwd -l GroupPass123)" admins` |

### Examples

### Rename group qa to quality

```bash
sudo groupmod -n quality qa
```

### Breakdown

| Breakdown | Descriptions | Examples |
|-----------|--------------|----------|
| `sudo` | Superuser command |
| `groupmod` | User command |
| `-n` | Rename a group |
| `quality` | New Group name |
| `qa` | Old group name |

### Change GID of staff group to 2000

```bash
sudo groupmod -g 2000 staff
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Superuser command |
| `groupmod` | User command |
| `-g` | Directs to change the group's ID |
| `2000` | New Group ID |
| `staff` | Group name |

# Command: groupdel

## Description: Deletes a group from the system by removing the entry from `/etc/group` and `/etc/shadow`. Does not delete user

## Syntax

- `groupdel [Options] GROUP`

### Options

- `No options for groupdel`

### Examples

### Delete a group

```bash
sudo groupdel testers
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Superuser command |
| `groupdel` | Group command |
| `testers` | Specified group |

# Command: gpasswd

## Description: It handles group passwords and memberships directly. It can set or change passwords, add or remove users from groups, set group administrators, and lock or unlock groups. It uses the `/etc/group` and `/etc/gshadow` files

## Syntax

- `gpasswd [Options] GROUP`
- `gpasswd [Options] -a USER GROUP`
- `gpasswd [Options] -d USER GROUP`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-a USER` | Add user to group | `sudo gpasswd -a name newname` |
| `-d USER` | Remove user from group | `sudo gpasswd -d name newname` |
| `-r` | Remove group password | `sudo gpasswd -r name` |
| `-R` | Restrict group access to members only | `sudo gpasswd -R name` |
| `-A USER1,USER2` | Set group administrators | `sudo gpasswd -A name,oldname newnamex` |
| `-M USER1,USER2 | Define group members | `sudo gpasswd -M name,oldnane newnames` |

### Examples

### Add user name to docker group

```bash
sudo gpasswd -a name docker
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Superuser command |
| `gpasswd` | Group command |
| `-a` | Add a user to a group |
| `name` | Name of a new user |
| `docker` | Specified group to add new user |

### Assign admins name and oldname to group qa

```bash
sudo gpasswd -A name, oldname qa
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Superuser command |
| `gpasswd` | Group command |
| `-A` | Directs to add specified users as admin to group |
| `name, oldname` | Specified users to be admin |
| `qa` | Specified group |


# Command: whoami

## Description: Displays the current effective username of the shell or process running the command. It is a shortcut for `id -un`

## Syntax

- `whoami [Options]`

### Options

- `no options`

### Examples

### Check current username

```bash
whoami
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `whoami` | User command |

# Command: getent

## Description: Retrieves entries from administrative databases configured in `/etc/nsswitch.conf`. It can pull user accounts, groups, hosts, network services, protocols, and more

## Syntax

- `getent [Options] DATABASE [Keyword...]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `(none)` | Dumps all user accounts | `getent passwd` |
| `with KEY` | Returns only name's entry from passwd database | `getent passwd name` |
| `hosts` | Queries from hosts database | `getent hosts localhosts` |
| `service` | Queries from service database | `getent services ssh` |
| `protocols` | Queries from protocols database | `getent protocols tcp` |
| `networks` | Queries from networks database | `getent networks loopback` |
| `ahosts` | Outputs IPv4 and IPv6 addresses | `getent ahosts google.com` |
| `alias` | Queries mail alias if configured | `getent aliases mail |

### Examples

### List all groups

```bash
getent group
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `getent` | Database command |
| `group` | Specified target to query |

# Command: finger

## Description:

## Syntax

### Options

### Examples







# Command: delgroup

## Description:

## Syntax

### Options

### Examples