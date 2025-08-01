# **File Permission and Ownership**

## **chmod**

## **Syntax**
- chmod [options] mode file

### **Mode**
Mode = the permissions you want to set
Symbolic
        u(user), g(group), o(owner), a(all)
        + add, - remove, = set exactly
        r read, w write, x execute

Numeric
        Each number is a sum of permissions
                4 = read
                2 = write
                1 = execute

rwx = 7, rw- = 6, r— = 4, —- = 0
Ex: u=rwx, g=rx, o=rx

#### **Options**
-R.         Recursive: change permissions in all subdirs.
-v.          Verbose: show what is being changed.
— reference=RFILE.             
                Set permissions as same as RFILE.


## **chown**

## **Syntax**
- chown [options] [owner] [:[group]] file

Owner = username or ID
Group = group name or GID
File = file or directory to modify

### **Options**
-R.         Recursively: apply to all files in subdirs 
-v.          Verbose: show what changed
—reference=RFILE
               Sets owner/group same as RFILE

####**Examples**
chown jake file.txt	Change owner to jake.
chown :admins file.txt	Change group to admins.
chown jake:admins file.txt	Change owner to jake, group to admins.
chown jake: file.txt	Change owner to jake, group unchanged.


## **chgrp**

## **Syntax**
-chgrp [options] group file

Group = target group
File = file/directory to change

### **Options**
- * same as chmod and chown

#### **Examples**
chgrp staff file.txt	Change group to staff.
chgrp -R staff /project	Recursively change group to staff.

## **umask**
- sets default file permissions for newly created files and directories

## **Syntax**
- umask [OPTIONS] [MASK]

## **Options**
(none)	Shows the current mask in octal form.
-S	Shows the mask in symbolic form.

