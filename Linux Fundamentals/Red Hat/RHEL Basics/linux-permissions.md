# Linux File Permissions
Linux file permissions are a integral part of security in linux systems. By setting permssions on a file/directory level, it allows access to be limited based on the user.

To view linux file permissions:
````
$ ls -l

drwxr-xr-x. 4 root root    68 Jun 13 20:25 tuned
-rw-r--r--. 1 root root  4017 Feb 24  2022 vimrc

````
The metadata is split up and informs you about 5 different things:
    1. File type: 
    2. Permission Settings
    3. Extended Attributes
    4. User owner
    5. Group owner