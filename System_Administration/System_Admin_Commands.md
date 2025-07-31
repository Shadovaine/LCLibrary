System Administration

sudo (Superuser Do)

Run a command as another user (usually root).

sudo [OPTIONS] COMMAND

Options
-u USER	Run as specified user (default is root).
-k	Forget cached credentials.
-l	List allowed commands for current user.

Ex:

Run command as root:
sudo apt update

Run as another user:
sudo -u jake ls /home/jake

List your sudo privileges:
sudo -l

 Clear cached credentials:
sudo -k


su (Substitute User)

Switch to another user account (default: root).

su [OPTIONS] [USERNAME]

Options
-	Simulate a full login (load user’s environment).

Ex:

Switch to root:
su

Switch to user “jake”:
su jake

Full login shell for root:
su -

Exit su session:
Exit



visudo

Safely edit the sudoers file to manage sudo privileges.

sudo visudo

Why use visudo?

✅ It checks for syntax errors before saving to prevent locking yourself out.

Options

 Add user “jake” to sudoers:
sudo visudo

Then add:

jake ALL=(ALL) ALL

 Allow “jake” to run only shutdown:
jake ALL=(ALL) /sbin/shutdown



systemctl (Systemd Control)

Manages systemd services and units on modern Linux distros.

systemctl [OPTIONS] COMMAND [SERVICE]

Options

start	Start a service.
stop	Stop a service.
restart	Restart a service.
enable	Enable service at boot.
disable	Disable service at boot.
status	Show service status.
is-active	Check if service is active.

Ex:

 Start Apache service:
sudo systemctl start apache2

Enable Apache to run at boot:
sudo systemctl enable apache2

Check status:
sudo systemctl status apache2

List all services:
sudo systemctl list-units --type=service



service (SysVinit Service Control)

Manages SysVinit services (legacy tool; still works on many systems).

service [SERVICE] COMMAND

Options

start	Start a service.
stop	Stop a service.
restart	Restart a service.
status	Show service status.

Ex:

Start Apache service:
sudo service apache2 start

Restart service:
sudo service ssh restart

Check service status:
sudo service cron status


