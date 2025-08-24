# Linux Directory System

## Linux directory Tree Form

```
  /
       ├── bin          ← Core user commands (a branch)
       ├── sbin         ← Core admin commands
       ├── etc          ← System configuration files
       ├── var          ← Logs, mail, and changing data
       ├── home         ← Regular users' personal directories
       │    ├── jake    ← Your personal space (sub-branch)
       │    ├── alice
       ├── root         ← Superuser's home directory (a branch too!)
       ├── usr          ← User-installed software & libraries
       │    ├── bin     ← Non-essential user commands
       │    ├── sbin    ← Non-essential admin commands
       ├── opt          ← Optional, third-party apps
       ├── lib          ← Shared libraries for core programs
       ├── proc         ← Kernel & process info (virtual branch)
       ├── dev          ← Devices as files
       ├── boot         ← Kernel & bootloader (the system’s ignition)
       ├── tmp          ← Temporary scratchpad
```

# /bin

## Description: Stands for binary ( compiled programs). System directory contains essential executable programs needed to boot system and run basic commands

# /bin and /usr/bin comparison

| Chracteristic | /bin | /usr/bin |
|---------------|------|----------|
| Essential commands for startup and running the system | ✅ | ❌ |
| Non- essential programs used once the system is fully up | ❌ | ✅ |

**In modern systems, some distros symlink /bin to /usr/bin to simplify things**

## What lives in /bin

| Binary |What It Does |
|--------|--------------|
| `bash` |The Bourne Again SHell (your command interpreter) |
| `ls` | Lists directory contents |
| `cp` | Copies files and directories |
| `mv` | Moves/renames files and directories |
| `rm` | Removes files or directories |
| `cat` | Concatenates and displays file content |
| `echo` |Prints text to the terminal |
| `pwd` | Prints the current working directory |
| `chmod` | Changes file permissions |
| `ln` | Creates links (hard or symbolic) |

# /sbin
  
## Description: Stands for “system binaries”. It contains essential system administration programs that are primarily used by the root (superuser) for managing and repairing the system. These commands are needed for tasks like mounting drives, repairing filesystems, networking setup, or rebooting the system. Think of it as the “admin’s toolbox” for running and fixing the system

## What lives in /sbin

| Binary | What It Does |
|--------|--------------|
| `fsck` | Checks and repairs filesystems |
| `mount` | Mounts filesystems |
| `umount` | Unmounts filesystems |
| `ifconfig` | Configures network interfaces (deprecated for ip) |
| `reboot` | Reboots the system |
| `shutdown` |Powers down the system |
| `init` | Initializes the system (parent of all processes) |
| `iptables` | Configures firewall rules |
| `mkfs` | Builds a filesystem on a device |

# /etc

## Description:  Stands for “editable text configuration” (that’s the unofficial but easy way to remember). It’s the central hub for system-wide configuration files. This is where Linux and installed software keep their settings, preferences, and startup scripts

**Located in the root directory (/), because the system needs it even in single-user mode.**

## What lives in /etc

| File/Folder | What It Does |
|-------------|--------------|
| `passwd` | Stores user account information (but not passwords!) |
| `shadow` | Stores encrypted user passwords |
| `hosts` | Maps hostnames to IP addresses locally |
| `fstab` | Lists filesystems to mount at boot |
| `hostname` | Sets the system’s hostname |
| `resolv.conf` | Configures DNS servers |
| `network/` | Network configuration files |
| `init.d/` | Startup scripts for services (older systems) |
| `systemd/` | Service unit files for systemd (newer systems) |
| `ssh/` | SSH configuration (client & server keys/settings) |

## what happens in /etc

- `Add new users`
- `Configure networking`
- `Set which services start at boot`
- `Secure your system (like configuring SSH in /etc/ssh/sshd_config)`

**If you screw up something in /etc, your system might not boot or network correctly. That’s why experienced sysadmins back up /etc before making big changes.**

## Where does /etc fit

| Directory | Purpose | Example |
|-----------|---------|---------|
| `/bin` | Core user commands | `ls`,`mv` |
| `/sbin` | Core admin tools | `fsck`, `mount` |
| `/usr/bin` | Installed software for users | `python3`,`git` |
| `/usr/sbin` | Installed admin tools | `sshd`,`iptables` |
| `/etc` | System-wide configuration | `ssh`,`fstab`,`passwd` |

## Real-World Examples

| Examples | Descriptions |
|----------|--------------|
| `Edit /etc/hostname` | Change your computer’s name |
| `Edit /etc/hosts` | Block websites (like a local ad-blocker) |
| `Edit /etc/fstab` | Automatically mount a USB drive at boot |
| `Edit /etc/ssh/sshd_config` | Harden SSH for cybersecurity |

# /etc/passwd

## Description: Stores basic information about every user

## /etc/passwd Contents

| File Contents | Descriptions |
|---------------|--------------|
| `Username` | name of user |
| `UID` | User ID |
| `GID` | Group ID |
| `Home Directory` | Directory where the user resides |
| `shell` | Default shell assigned to every user |

**Passwords are not in `/etc/passwd`they are in `/etc/shadow` which is more restricted.**

# Example

- `name: x : 1001 : 1001 : first name: /home/name:/bin/bash`

## Breakdown

| Breakdown | Description | Meaning |
|-----------|-------------|---------|
| `name` | Username | Login name, used when you type ssh name@hostname or su name |
| `X` | password placeholder | Password hashes are stored securely in `/etc/shadow` |
| `1001` | userID (UID) | Unique ID for this user. UID 0 = root, 1-999 = system users |
| `1001` | groupID (GID) | Primary group for this user ( from /etc/group) |
| `/home/name` | home directory | Path to user's home folder |
| `/bin/bash` | default shell | Default shell whwn user logs in |

# /var

## Description: Stands for “variable data." It contains files and data that change frequently while the system is running. Unlike /etc (static configs), /var is dynamic—it grows and shrinks as your system operates. Located in the root directory (/)

## What lives in /var

| Directory | What It Does |
|-----------|--------------|
| `/var/log` | System logs (kernel, authentication, errors, etc.) |
| `/var/spool` | Holds queued tasks (like print jobs and mail) |
| `/var/cache` | Application cache files |
| `/var/tmp` | Temporary files kept between reboots |
| `/var/lib` | State information for programs (databases, package info) |
| `/var/mail` | Stores user mailboxes |
| `/var/run → /run` | Holds process ID files (like services tracking info) |

## Why is /var important

## It’s where Linux keeps all its “changing state” data

- `Logs for auditing and troubleshooting`
- `Cached downloads to speed things up`
- `Queued tasks for printers or cron jobs`

# Real world examples

## See failed login attempts (great for cybersecurity)

- `Check /var/log/auth.log`

## Free up space from downloaded packages

- `Clear /var/cache/apt`

## Inspect user cron jobs

- `Look in /var/spool/cron`

## Database data lives here

- `Monitor /var/lib/mysql`

# /home

## What is it?

- `/home is where Linux stores personal files and settings for each user on the system.`
- `Every user gets their own subdirectory under /home.`
- `It’s like each user’s private workshop inside the larger house.`

## What lives in /home

| File/Folder | What It Does |
|-------------|--------------|
| `Documents/` | User’s text docs, PDFs, etc |
| `Downloads/` | Files downloaded from the internet |
| `Desktop/` | Files and shortcuts shown on the desktop environment |
| `Pictures/` | User’s images |
| `Videos/` | User’s videos |
| `Music/` | User’s audio files |
| `.bashrc` | Hidden config for bash shell customization |
| `.ssh/` | User’s SSH keys and configs |
| `.config/` | App configuration files |

**Anything with a dot (.) is hidden (like .bashrc) but critical for custom setups.**

## This is the user's world in Linux

- `Personal files and settings stay isolated.`
- `You can experiment freely without messing with the system’s core files.`
- `Great for multi-user systems—each user’s space is separate.`

## Real World Examples

- `Edit your .bashrc to customize your prompt and aliases.`
- `Store your TryHackMe reports and code projects in /home/username/Documents/cybersecurity.`
- `Place your SSH keys in /home/username/.ssh/ for secure server access.`

# /root

## What is it

- `/root is the home directory of the root user (superuser).`
- `It’s like the private lair of the dragon king—reserved only for the most powerful entity in the system.`
- `Not to be confused with / (the root of the filesystem).`

| File/Folder | What It Does |
|-------------|--------------|
| `.bashrc` | Root’s custom bash shell configuration |
| `.ssh/` | SSH keys for root-only remote access |
| `scripts/` | Admin’s personal scripts for maintenance |
| `backups/` | Critical system backup files |
| `log_check.sh` | A script for scanning logs for security breaches |

**Regular users cannot access this directory without root privileges (sudo or su).**

## Why is /root Important?

- `A safe, separate workspace from normal users`
- `A place to manage emergency system repairs`
- `Configurations isolated from regular user profiles`
- `In single and recovery mode /root is where you’ll land as the superuser`

## Root va regular users

| Feature | Regular User | Root User |
|---------|--------------|-----------|
| `Home Directory` | :heavy_check_mark: | :x: |
| `/home/jake` | :heavy_check_mark: | :x: |
| `/root` | :x: | :heavy_check_mark: |
| `Privileges Limited` | :heavy_check_mark: | :x: |
| `Full control` | :x: | :heavy_check_mark: |
| `Can Edit System Files?` | :x: | :heavy_check_mark: |
| `Can Wreck the System?` | :x: | :heavy_check_mark: |

## Real-World Examples

- `Use sudo su → Enter root’s domain`
- `Edit /root/.bashrc to set up root-specific aliases (like alias ll='ls -lah')`
- `Store sensitive system-wide scripts in /root/scripts/`

# /usr

## Description: Stands for “user system resources.”  contains user binaries—programs and commands that are not required to boot the system but are used once it’s fully operational. These are the day-to-day tools you use to work, write code, edit files, or run applications

## /usr/bin

## What lives in /usr/bin

| Binary | What It Does |
|--------|--------------|
| `python3` |  Runs Python 3 programs |
| `gcc` | GNU Compiler Collection (compiles C++ code) |
| `nano` | Simple text editor |
| `git` | Version control system |
| `tar` | Archives/compresses files |
| `wget` | Downloads files from the internet |
| `curl` | Transfers data from or to a server |

## /usr/sbin

## What is /usr/sbin

- `/usr/sbin contains system admin binaries for managing advanced system services and configurations`
- `These are non-essential at boot, but critical for configuring servers, networking, and security`
- `Usually only the root user or sudoers can run these`

## What lives in /usr/sbin

| Binary | What It Does |
|--------|--------------|
| `sshd` | Secure Shell daemon (allows SSH connections) |
| `apache2` | Apache web server binary |
| `useradd` | Adds new user accounts |
| `groupadd` | Adds new groups |
| `iptables` | Configures firewall rules |
| `tcpdump` | Captures network packets for analysis |

## If you’re setting up servers or doing cybersecurity hardening, you’ll spend a lot of time here

## How does /usr/bin and /usr/sbin fit together

| Directory | Who Uses It? | What’s Inside? |
|-----------|--------------|----------------|
| `/usr/bin` | All users | Python3, git, nano |
| `/usr/sbin` | System admins | (root) Daemons, admin tools, sshd, iptables |

| Directory Essential for Boot? | User or Root? | Example Commands |
|-------------------------------|---------------|------------------|
| `/bin` :heavy_check_mark: | All users | `ls` `cp` `mv` |
| `/sbin` | Root/admin only | `fsck` `mount` |
| `/usr/bin` | All users | `python3` `git` |
| `/usr/sbin` | Root/admin only | `sshd` `iptables` |

# /usr/local/bin

## What is /usr/local/bin

- `/usr/local/bin is for user-installed binaries (programs and scripts)`
- `This directory is not touched by the package manager (apt, yum, etc.), so it’s safe for custom installations`
- `Commands in here are typically user-level tools that don’t require root to run`
- `Located in /usr/local, which is reserved for “local” custom software on your system`

## What lives in /usr/local/bin

| Example | Binary | What It Does |
|---------|--------|--------------|
| `my_script.sh` | ❌ | A custom shell script you created |
| `node_Node.js` | ✅ | Installed manually |
| `go Golang` | ✅ | if installed from source |
| `custom-tool` | ❌ | Any utility installed outside package manager |

**If you install software manually with `make && make install`, it usually ends up here**

# /usr/local/sbin

## What is /usr/local/sbin

- `/usr/local/sbin is the admin-only version of /usr/local/bin`
- `Used for system administrator programs that you’ve compiled  or installed yourself`
- `Commands in here usually require root or sudo to run`

## What is in /usr/local/sbin

| Example | Binary | What It Does |
|---------|--------|--------------|
| `custom-daemon` | :x: | A custom service you compiled and installed |
| `vpn-setup-tool` | :x: | A manually installed VPN admin utility |
| `my_backup_tool` | :x: | Your own backup script running as root |

# The big picture

| Directory | Managed By? | Who Uses It? | What’s Inside? |
|-----------|-------------|--------------|----------------|
| `/bin` | OS |All users |Core commands (ls, cp, etc.) |
| `/sbin` | OS | Root/admin only | Core admin tools (fsck, mount) |
| `/usr/bin` | Package Manager |All users | Installed software (python3, nano) |
| `/usr/sbin` | Package Manager | Root/admin only | Installed admin tools (sshd, apache2) |
| `/usr/local/bin` | You (manual install) | All users |Custom binaries/scripts |
| `/usr/local/sbin` | You (manual install) |Root/admin only | custom-made admin script tools |

# /opt

## What is it?

- `/opt stands for “optional"`
- `It’s a directory designed to hold add-on application software packages that aren’t part of the base OS`
- `Think of it like the “VIP room” for third-party apps`

**Located at the root level `/`, separate from system binaries and configs**

## What lives in /opt

| Example | What It Does |
|---------|--------------|
| `/opt/google/` | Google Chrome installed manually |
| `/opt/vmware/` | VMware Workstation binaries and libraries |
| `/opt/zoom/` | Zoom client installed outside package manager |
| `/opt/myapp/` | Your custom app installed manually |

**Packages installed here often come with their own binaries, libraries, and configs, keeping them isolated from system files**

## Why Use /opt?

- `For third-party or custom software`
- `Keeps your system’s core directories (/bin, /usr/bin) clean`
- `Prevents conflicts with OS updates or package manager upgrades`
- `Useful for enterprise apps and manual installations`

**Sysadmins love this directory for managing large, self-contained software suites**

## Real-World Examples

- `You download a .tar.gz of a custom security tool, extract it, and install it in /opt/mytool/`
- `A company installs Oracle software in /opt/oracle/`
- `Games like Steam (if manually installed) often go here`

## Pro Tips on /opt

- `Good for cybersecurity tools: Pen-testing apps like Burp Suite, Nessus, or custom scripts often live here when installed manually`
- `Avoids “dependency hell”: Since apps in /opt bring their own dependencies, they don’t break when you update the system`

# /lib

## What is /lib?

- `/lib stands for “library”`
- `It holds shared libraries and kernel modules needed by programs in /bin and /sbin to run`
- `These libraries are like the magical incantations that make your commands actually work`
- `Located in the root filesystem (/), because it’s essential for system booting`
- `Shared libraries here usually have names like LibXYZ.so."1"`

## What lives in /lib?

| Directory/File | What It Does |
|----------------|--------------|
| `libc.so.*` | The GNU C library (the core library for Linux) |
| `ld-linux.so.*` | Dynamic linker/loader |
| `modules/` | Kernel modules (*.ko files) |
| `systemd/` | Libraries needed for system initialization |
| `libm.so.*` | Math library |





## Why is /lib important?

It’s critical for system booting and running basic binaries.
 • Without /lib, binaries in /bin and /sbin wouldn’t work because they rely on these libraries.
 • Kernel modules here let Linux interact with hardware (drivers for devices like USB, networking, etc.).

🛡️ If you accidentally delete /lib, your system becomes unbootable.

## Real-World Examples

- `Dynamic Linking: When you run ls, it calls libraries in /lib (like libc.so)`
- `Kernel Modules: Load extra hardware support by pulling modules from /lib/modules/`

## Troubleshooting

- `if a program complains about “missing shared library,” check /lib`

## On 64-bit systems, you’ll also see

- `/lib64: Libraries specifically for 64-bit binaries`

## Pro Tips on /lib

- `It’s the system’s magic: Without it, binaries are useless shells`
- `Cybersecurity tip: Attackers sometimes replace /lib libraries with malicious ones (called library hijacking)`

# /proc 

## What is /proc?

- `/proc stands for “process.”`
- `It’s a virtual filesystem (not stored on disk) that provides a window into the kernel and running processes`
- `Think of it as the control room where Linux displays real-time information about the system`
- `Mounted automatically at boot under: `/proc`` 

## What lives in /proc?

| File/Folder | What It Represents |
|-------------|--------------------|
| `cpuinfo` | Details about the CPU (model, cores, speed) |
| `meminfo` | RAM usage statistics |
| `uptime` | How long the system has been running |
| `version` | Kernel version information |
| `mounts` | Mounted filesystems |
| `cmdline| Kernel boot parameters |
| `[PID]/` | Subdirectories for each running process by their PID |
| `kallsyms` | Kernel symbol table |
| `sys/` | Kernel tunables (used by sysctl) |

## What’s So Special About /proc?

- `It’s dynamic: Data in /proc is generated on-the-fly by the kernel every time you access it`
- `It’s read-only for most files, but some files (like /proc/sys) can be modified to change kernel parameters in real-time`
- `This is why /proc is vital for system monitoring, debugging, and tuning`

## Real world examples

## See CPU Details

- `cat /proc/cpuinfo`

## Check Memory Usage:

- `cat /proc/meminfo`

## List all running processes (by PID)

- `ls /proc | grep '^[0-9]`

## Tweak Kernel Settings (as root)

- `echo 1 > /proc/sys/net/ipv4/ip_forward`

## View Kernel Version

- `cat /proc/version`

## How /proc Powers Cybersecurity

- `Monitor system activity: Watch process behavior during an incident`
- `Forensics: Inspect /proc/[PID]/cmdline to see what commands a process ran`
- `Hardening: Adjust kernel security flags via /proc/sys`

## Pro Tips on /proc

- `It’s like reading the system’s live neural network`
- `Some files in /proc/sys can literally change system behavior—so handle with care`
- `As a cybersecurity pro, you’ll visit /proc often to monitor or control processes`

# /dev

## Description: /dev is the directory that contains device files (also called special files)

## What is /dev?

- `In Linux, everything is a file – even hardware like disks, terminals, and printers`
- `The files in /dev are interfaces to kernel drivers that let you interact with hardware or virtual devices`
- `You don’t directly “open” these files to edit them, but commands and programs can use them to send or receive data to/from hardware`

## 2 main types of device files in /dev

## Character Devices (c)

- `Data is handled one character at a time`
- `Example: keyboards, mice, serial ports, terminals`
- `Found with ls -l showing a c at the start`
- `crw-rw-rw- 1 root root 1, 3 Jul 16 10:12 /dev/null`

## Block Devices (b)

- `Data is handled in blocks (like disks)`
- `Example: hard drives, SSDs, USB drives`
- `Found with ls -l showing a b at the start`
- `brw-rw---- 1 root disk 8, 0 Jul 16 10:12 /dev/sda`

## Key Special Files in /dev

|File | What It Represents |
|-----|--------------------|
| `/dev/null` | A “black hole” – data written here is discarded (used to suppress output) |
| `/dev/zero` | Infinite stream of zeros. Useful for overwriting or allocating space |
| `/dev/random` | Generates random data (good for cryptography) |
| `/dev/random` | Like /dev/random, but faster and less “truly random” |
| `/dev/tty` | The terminal currently in use |
| `/dev/sda` | The first hard disk (block device). Subsequent disks are /dev/sdb, /dev/sdc, etc |
| `/dev/sr0` | First CD/DVD-ROM drive |
| `/dev/loop0` | A loopback device (lets you mount a file as if it were a disk) |
| `/dev/fd0` | First floppy disk (mostly historical now) |

## Why is /dev special?

- `Dynamic: Modern Linux uses udev, which populates /dev automatically as devices are added/removed`
- `Virtual Filesystem: /dev isn’t a real directory on disk. It’s provided by the devtmpfs filesystem mounted at boot`

## Real-World Examples

## Suppressing Output

```bash
command > /dev/null 2>&1
```

**(Send all output and errors to the void.)**

## Wiping a Drive

```bash
sudo dd if=/dev/zero of=/dev/sdb bs=1M
```

**(Overwrite /dev/sdb with zeros.)**

## Testing Randomness

```bash
head -c 100 /dev/random | od -t x1
```

## Checking USB Device

```bash
dmesg | grep sdb
ls -l /dev/sd*
```

# /boot

## Description: Contains the statis files needed to boot the operating system

## What lives in /boot

| File/Directory | What It Does |
|----------------|--------------|
| `vmlinuz-*` | Compressed Linux kernel (the core OS) |
| `initrd.img-*` | Initial RAM disk (used during early boot stages) |
| `grub` | GRUB bootloader configs and modules |
| `System.map-*` | Kernel symbol table (for debugging and crash analysis) |
| `config` | Kernel build configuration |

**The asterisks (*) represent the kernel version (e.g., vmlinuz-5.15.0-1051)**

## Why is /boot Important?

- `It load the kernel`
- `Initialize hardware drivers`
- `Hands control to user space`

## Real-World Examples

## View the kernel version loaded

```bash
uname -r
```

## Inspect GRUB configuration (bootloader)

```bash
cat /boot/grub/grub.cfg
```

## Check available kernels

```bash
grep menuentry /boot/grub/grub.cfg
```

## Update GRUB after kernel upgrade

```bash
sudo update-grub
```

# /tmp

## Description: Is a temporary directory where programs and users can store files that are only needed for a short time. Think of it as Linux’s scratchpad or a sandbox for temp files

## Key Properties of /tmp

- `Ephemeral: Anything here is not meant to last. Don’t save important files here`
- `World-Writable: Any user can write here, but files are protected from other users by the sticky bit`
- `Any user or program can write here (with some restrictions)`
- `It’s cleared out automatically, either: On reboot or by tmpwatch / systemd-tmpfiles if a file is unused for too long`

## Example

## Long Listing format

```bash
ls -ld /tmp

drwxrwxrwt 10 root root 4096 Jul 16 09:42 /tmp
```

## Breakdown

| Breakdown | Description |
|-----------|-------------|
| `drwxrwxrw` | Permission settings for users, groups, and others |
| `---------t` | t stands for sticky bit which means users can not delete files they do not own |
| `10` | Number of hard links to this directory |
| `root` | Owner is the user who owns this directory |
| `root` | Group that owns this directory |
| `4096` | Size of directory in bytes |
| `Jul 15 09:42` | Last modfication time for the directory |
| `/tmp` | The directory's path name |

## What Goes in /tmp

- `Temporary data while running`
- `Socket files for inter-process communication (IPC)`
- `Lock files`
- `Cache files during installations`

## File Purpose Examples

## User-created temp file

- `/tmp/tmp1234.txt`

## Sockets for X Window system

- `/tmp/.X11-unix`

## Audio server (PulseAudio) socket folder

- `/tmp/pulse-PKdhtXMmr18n`

## Temporary directory for SSH keys

- `/tmp/ssh-XXXXXX/`

## Sticky Bit in Action

```bash
ls -ld /tmp

drwxrwxrwt 10 root root 4096 Jul 16 09:42 /tmp
```

## The t at the end means

- `Users can’t delete files they don’t own`
- `Without sticky bit? Any user could delete anyone else’s temp files`

## Security Notes

- `Modern Linux mounts /tmp with noexec and nosuid to prevent abuse`
- `noexec: Stops programs from running directly from /tmp`
- `nosuid: Stops set-user-ID programs from escalating privileges`

## Real-World Examples

## Quick Scratch File

```bash
cd /tmp
echo "test" > testfile.txt
```

## Temporary Download

```bash
wget -O /tmp/testfile.zip <http://example.com/file.zip>
```

## /tmp vs /var/tmp

| Directory | Cleared When? | Use Case |
|-----------|---------------|----------|
| `/tmp` | On reboot | Short-lived temp files |
| `/var/tmp` | Sticks around between reboots | Longer-lived temp files |
