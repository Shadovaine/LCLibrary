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
- `w`
- `who`
- `user`
- `chmod`
- `chown`
- `chgrp`
- `newgrp`
- `deluser`
- `delgroup`


## **useradd**
- creates a new user

## **Syntax**
-useradd [OPTIONS] USERNAME

### **Options**
-m	Create the user’s home directory.
-d DIR	Specify custom home directory.
-s SHELL	Specify login shell (e.g., /bin/bash).
-u UID	Assign specific user ID.
-g GROUP	Set primary group.
-G GROUPS	Add to supplementary groups (comma-separated).
-c COMMENT	Set user description/comment (GECOS field).

#### **Examples**
Create a user with default settings:
sudo useradd jake

Create user with home dir and bash shell:
sudo useradd -m -s /bin/bash jake

Create user with specific UID and comment:
sudo useradd -m -u 1500 -c "Dragon Rider" jake

Create user and assign to group “admins”:
sudo useradd -m -G admins jake


## **usermod**
- Modify an existing user account.

## **Syntax**
- usermod [OPTIONS] USERNAME

## **Options**
-l NEWNAME	Change the username.
-d DIR	Change home directory.
-m	Move existing files to new home directory.
-s SHELL	Change login shell.
-g GROUP	Change primary group.
-G GROUPS	Set supplementary groups.
-a -G GROUPS	Add user to supplementary groups (append).

### **Examples**
Change username from “jake” to “shadow”:
sudo usermod -l shadow jake

Change user’s shell to zsh:
sudo usermod -s /bin/zsh jake

 Move user’s home directory:
sudo usermod -d /home/dragon -m jake

 Add user to “sudo” group (append):
sudo usermod -a -G sudo jake


## **passwd**
- Set or change a user’s password.

## **Syntax**
- passwd [OPTIONS] [USERNAME]

## **Options**
- (no args)	Change the current user’s password.
- USERNAME	Change password for another user.
-l USERNAME	Lock user account.
-u USERNAME	Unlock user account.
-e USERNAME	Expire user’s password (force change on next login).

## **Examples**
Change your password:
passwd

Set password for user “jake”:
sudo passwd jake

Lock user account:
sudo passwd -l jake

Unlock user account:
sudo passwd -u jake



## **groupadd**
- Create a new group.

## **Syntax**
groupadd [OPTIONS] GROUPNAME

## **Options**
- -g GID	Specify a group ID.

### **Examples**
 Create a group called “admins”:
sudo groupadd admins

Create group with specific GID:
sudo groupadd -g 1001 developers



## **groups**
- Show which groups a user belongs to.

## **Syntax**
- groups [USERNAME]

### **Options**
 Show your groups:
groups

 Show groups for user “jake”:
groups jake



## **id**
- Show a user’s UID, GID, and group memberships.

## **Syntax**
- id [OPTIONS] [USERNAME]

## **Options**
-u	Show only the UID.
-g	Show only the GID.
-G	Show all group IDs.
-n	Show names instead of numeric IDs.

## **Examples**
Show your user and group IDs:
id

Show IDs for user “jake”:
id jake

 Show only UID for user “jake”:
id -u jake

Show only GID for user “jake”:
id -g jake
