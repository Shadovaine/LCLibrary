# User and Group Management

## Description: Commands involved adding, removing, and modifying groups and users

## Table of Contents

- `useradd`
- `adduser`
- `usermod`
- `passwd`
- `chage`
- `userdel`
- `groupadd`
- `groupmod`
- `groupdel`
- `gpasswd`
- `groups`
- `id`
- `whoami`
- `getent`
- `finger`
- `user`
- `chmod`
- `chown`
- `chgrp`
- `newgrp`
- `deluser`
- `delgroup`

# Command: useradd

## Description: Creates a new user

## Syntax

- `useradd [OPTIONS] USERNAME`

### Options

-m	Create the user’s home directory.
-d DIR	Specify custom home directory.
-s SHELL	Specify login shell (e.g., /bin/bash).
-u UID	Assign specific user ID.
-g GROUP	Set primary group.
-G GROUPS	Add to supplementary groups (comma-separated).
-c COMMENT	Set user description/comment (GECOS field).

### Examples

### Create a user with default settings

sudo useradd name

### Create user with home dir and bash shell

sudo useradd -m -s /bin/bash name

### Create user with specific UID and comment

sudo useradd -m -u 1500 -c "name"

### Create user and assign to group “admins”

sudo useradd -m -G admins name

# Command: adduser

## Description: Command to add a user to an existing folder

## Syntax

### Options

### Examples

# Command: usermod

## Description: Modify an existing users account

## Syntax

- `usermod [OPTIONS] USERNAME`

### Options

-l NEWNAME	Change the username.
-d DIR	Change home directory.
-m	Move existing files to new home directory.
-s SHELL	Change login shell.
-g GROUP	Change primary group.
-G GROUPS	Set supplementary groups.
-a -G GROUPS	Add user to supplementary groups (append).

### Examples

### Change username from “username” to “name”

sudo usermod -l name username

### Change user’s shell to zsh

sudo usermod -s /bin/zsh name

### Move user’s home directory

sudo usermod -d /home/dragon -m name

### Add user to “sudo” group (append)

sudo usermod -a -G sudo jake

# Command: passwd

## Description: Creates a new or change an existing user’s password

## Syntax

- `passwd [OPTIONS] [USERNAME]`

### Options

- (no args)	Change the current user’s password.
- USERNAME	Change password for another user.
-l USERNAME	Lock user account.
-u USERNAME	Unlock user account.
-e USERNAME	Expire user’s password (force change on next login).

### Examples

### Change your password

passwd

### Set password for user "name"

sudo passwd name

### Lock user account

sudo passwd -l name

### Unlock user account

sudo passwd -u jake

# Command: chage

## Description:

## Syntax

### Options

### Examples

# Command: userdel

## Description:

## Syntax

### Options

### Examples

# Command: groupadd

## Description: Create a new group

## Syntax

- `groupadd [OPTIONS] GROUPNAME`

### Options

- -g GID	Specify a group ID.

### Examples

### Create a group called “admins”

sudo groupadd admins

### Create group with specific GID

sudo groupadd -g 1001 developers

# Command: groupmod

## Description:

## Syntax

### Options

### Examples

# Command: groupdel

## Description:

## Syntax

### Options

### Examples

# Command: gpasswd

## Description:

## Syntax

### Options

### Examples

# Command: groups

## Description: Show which groups a user belongs to

## Syntax

- `groups [USERNAME]`

### Options

### Examples

### Show your groups

groups

### Show groups for user "name"

groups name

# Command: id

## Description: Show a user’s UID, GID, and group memberships.

## Syntax

- `id [OPTIONS] [USERNAME]`

### Options

-u	Show only the UID.
-g	Show only the GID.
-G	Show all group IDs.
-n	Show names instead of numeric IDs.

### Examples

### Show your user and group IDs

id

### Show IDs for user "name"

id name

### Show only UID for user "name"

id -u name

### Show only GID for user "name"

id -g name

# Command: whoami

## Description:

## Syntax

### Options

### Examples

# Command: getent

## Description:

## Syntax

### Options

### Examples

# Command: finger

## Description:

## Syntax

### Options

### Examples

# Command: user

## Description:

## Syntax

### Options

### Examples

# Command: chmod

## Description:

## Syntax

### Options

### Examples

# Command: chown

## Description:

## Syntax

### Options

### Examples

# Command: chgrp

## Description:

## Syntax

### Options

### Examples

# Command: newgrp

## Description:

## Syntax

### Options

### Examples

# Command: deluser

## Description:

## Syntax

### Options

### Examples

# Command: delgroup

## Description:

## Syntax

### Options

### Examples