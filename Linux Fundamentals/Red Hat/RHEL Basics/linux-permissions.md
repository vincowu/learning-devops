# Linux File Permissions
Linux file permissions are a integral part of security in linux systems. By setting permssions on a file/directory level, it allows access to be limited based on the user.

To view linux file permissions:
````
$ ls -l

drwxr-xr-x. 4 root root    68 Jun 13 20:25 tuned
-rw-r--r--. 1 root root  4017 Feb 24  2022 vimrc

````
The metadata is split up and informs you about 5 different things:
    1. File type
    2. Permission Settings
    3. Extended Attributes (This is the . at the end of the string)
    4. User owner
    5. Group owner
## File Type (represented in beginning of metadata string)
There are 3 type of file types: regular files (-), directory files (d) and special files (5 types). More info can be found [here](https://www.bogotobogo.com/Linux/linux_File_Types.php)
    Special files:
    1. Block File (B)
        These are hardware files and mostly present in the /dev and are created usually by fdisk command
    2. Character device file(c)
        Provides a serial stream of input or output
    3. Named pipe file (p)
    4. Symbolic link file (l)
    5. Socket file (s)
        Used to pass info between apps
## Permission Settings 
This is represented by the 9 character string after the file type (ex. rw-r--r--)
r means read, w means write and x means execute
The string above represents 3 different permissions for 3 different groups
- First 3 characters (rw-) represents permissions for the owner of the file
- Next 3 characters (r--) represents permissions for the user group that owns the file
- Last 3 characters (r--) represents permissions for others
### Symbolic Mode
This can also be written in symbolic mode: u (user owner), g(group owner) and o(other)

### Numeric Mode (Octal Values)
- r (read): 4
- w (write): 2
- x (execute): 1
This would be represented by 3 numbers. 744 for example would mean that the owner has 4(read) + 2(write) + 1(execute) permissions, group would have 4(read) permissions and other would also ahve 4(read) permissions

When a linux system looks at the file permissions, the steps it takes to determine whether you can interact with the file is
1. Checks if you own the file. If so, you are granted the permissions from the first 3 characters.
2. If you don't own the file, it then checcks for group membership to see if you belong to the group that matches the group owner. If so, you will be granted permissions in the next 3 characters
3. Finally if you aren't the owner and don't belong in the same group as the owner, then the other permissions are granted to you.

To change the linux permissions of a file, you would use the chmod command
````
# Numeric 
chmod 744 file-name

or
# Symbolic
chmod ug+rwx file-name
chmod o+r file-name

# This means that all the files in the directory will be recursively set
chmod -R o+r directoty/

````
Note when adding permissions using symbolic permissions, different operators mean different things.
the + operator means add specified permission modes
the - operator means remove specified permission modes
the = operator means make the specified permissions exactly as whats specified 

To change the actual user owenr itself you would use the chown command.
To change the group you can use chgrp command

Note to check groups that a user is in command is 
````
groups user_name
````
## umask
File creation mask (umask) sets permissions for new files/directories.
Default permissions for files is 666 and for directories is 777
Umask is subtractive therefore by setting umask of 002, the new files permission would be 663
````
learning-devops % whoami
vincowu
learning-devops % umask
022
# To change the default umask, you would need to:
learning-devops % echo 'umask 0027' >> ~/.bashrc
````

