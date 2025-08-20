# System Administration

## Description: Commands commonly used for system administration duties

## Table of Contents

- `sudo`
- `su`
- `visudo`
- `systemctl`
- `service`

# Command: sudo (Superuser Do)

## Description: Permits user to run a command with elevated privileges

## Syntax

- `sudo [OPTIONS] COMMAND`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-h` | Show help | `sudo -h` |
| `-V` | Display the version and exit | `sudo -V` |
| `-v` | Update the user's cached credentials (keeps you from having to re-enter your password soon) | `sudo -v` |
| `-k` | Invalidate the timestamp (force password re-entry next time) | `sudo -k` |
| `-K` | Remove the cached credentials entirely | `sudo -K` |
| `-l` | List allowed (and forbidden) commands for the current user | `sudo -l` |
| `-L` | List all sudoers options and defaults | `sudo -L` |
| `-u<user>` | Run commands as another user | `sudo -u www-data whoami` |
| `-g<group>` | Run the command with the primary group set to `<group>` | `sudo -g developers id -gn` |
| `-U<user>` | List privileges for another user | `sudo -U alice -l` |
| `-s` | Run the command in the user's default shell | `sudo -s` |
| `-i` | Run login shell as root (like logging in as root) | `sudo -i` |
| `-E` | Preserve the user's environment variables | `sudo -E env` |
| `-H` | Set `HOME` to the target user's home directory | `sudo -H pip install some-package` |
| `-b` | run the command in the background | `sudo -b apt update` |
| `-n` | Non-interacrtive - do not prompt for password (fail if password required) | `sudo -n ls /root` |
| `-p<prompt>` | List a custom password prompt | `sudo -p "Enter your passcode: " ls /root` |
| `-S` | Read password from standard input | `sudo -S ls /root` |
| `-A` | Use an external program for the password prompt | `sudo -A ls /root` |

### Examples

### Run command as root

```bash
sudo apt update
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Superuser Command |
| `apt` | Package manager |
| `update` | directs to update all installed packages |

### Run as another user

```bash
sudo -u name ls /home/name
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | Superuser command |
| `-u name` | Directs to use a different user |
| ` ls` | list command |
| `/home/name` | file to list |


# Command: su (Substitute User)

## Description: Allows changes to user identity mid-session

## Syntax

- `su [OPTIONS] [-] [USERNAME [ARG]...]`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `(none)` | Switches to root account | `su` |
| `-<username>` or `-l<username>` | Start a login shell as the target user | `su - name` |
| `-c<command>` | run a single command as another user | `su -c "ls /root" root` |
| `-s<shell>` | Specify which shell to use when switching users | `su -s /bin/bash name` |
| `m` or `-p` | Preserve the current user's environment | `su -m name` |
| `-(shortcut for full login shell)` | this is the same as `-l` | `su -` |

### Examples

### Switch to root

```bash
su
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `su` | switches user to root |

### Switch to user **name**

```bash
su name
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `su` | superuser command |
| `name` | target user |

# Command: visudo

## Description: Safely edit the sudoers file to manage sudo privileges

## Syntax

- `sudo visudo`

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `-c` | Check the `sudoers` file for syntax errors | `sudo visudo -c` |
| `-f<file>` | Specify an alternative sudoers file instead of /etc/sudoers | `sudo visudo -f /etc/sudoers.d/webadmins` |
| `-s` | Enable strict checking mode | `sudo visudo -s` |
| `-x` | Export the parsed `sudoers` file in JSON format | `sudo visudo -x` |
| `-q` | Quiet mode | `sudo visudo -q` |

### Examples

### Add user “nane" to sudoers

```bash
sudo visudo
name ALL=(ALL) ALL
```

### Breakdown

| Breakdown | Description |
|-----------|-------------|
| `sudo` | superdoer command |
| `visudo` | system admin command |
| `name` | target user |
| `ALL' | who it applies to |
| `=(ALL)` | who u can impersonate |
| `ALL` | what commands u can run |

### Allow “name” to run only shutdown

```bash
name ALL=(ALL) /sbin/shutdown
```

# Command: systemctl (Systemd Control)

## Description: Manages systemd services, units, targets, and the system state also

## Syntax

systemctl [OPTIONS] COMMAND [SERVICE]

### Options

| Options | Descriptions | Examples |
|---------|--------------|----------|
| `start<service>` | Start a service | `sudo systemctl start nginx` |
| `stop<service>` | Stop a service | `sudo systemctl stop nginx` |
| `reload<service>` | Reload configuration without restarting | `sudo systemctl reload nginx` |
| `reload-or-restart<service>` | Reload if supported, else restart | `sudo systemctl reload-or-restart nginx` |
| `enable<service>` | Enable service at boot | `sudo systemctl enable docker` |
| `disable<service>` | disable service from starting at boot | `sudo systemctl disable bluetooth` |
| `mask<service>` | Prevent any manual or automatic start | `sudo systemctl mask telnet` |
| `unmask<service>` | Unlock a masked service | `sudo systemctl unmask telnet` |
| `status<service>` | Show detailed status | `systemctl status sshd` |
| `is-active<service>` | Check if service is active | `systemctl is-active nginx` |
| `is-enabled<services>` | Check if service starts at boot | `systemctl is-enabled service` |
| `is-failed<services>` | Check if service has failed | `systemctl is-failed service` |



### Examples

### Start Apache service

sudo systemctl start apache2

### Enable Apache to run at boot

sudo systemctl enable apache2

### Check status

sudo systemctl status apache2

### List all services

sudo systemctl list-units --type=service

# Command: service (SysVinit Service Control)

## Description: Manages SysVinit services (legacy tool; still works on many systems).

## Syntax

service [SERVICE] COMMAND

### Options

start	Start a service.
stop	Stop a service.
restart	Restart a service.
status	Show service status.

### Examples

### Start Apache service

sudo service apache2 start

### Restart service

sudo service ssh restart

### Check service status

sudo service cron status
