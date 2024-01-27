# System Documentation
3 ways to find more details on different linux commands
    1. Man Pages (man command)
        - Traditional Unix documentation (uses vim keybindings)
    2. Info Pages (info command)
        - Default dormat for documentation for GNU (uses emacs keybindings)
    3. System Docs 
        - System documentation located in the /usr/share/doc directory.
        ````
        ls /usr/share/doc | grep -i "httpd"
        ````
Examples using man and installing
````
#!/bin/bash

# installing httpd and mariadb using dnf package manager
sudo dnf -y install httpd mariadb

# checking mariadb for help docs
mariadb --help

# will return man pages to httpd now after installing packages
man httpd

# will return command name and manpage number plus brief description
whatis httpd
# will return even more info
apropos httpd
````
