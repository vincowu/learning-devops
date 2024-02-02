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
    3. Extended Attributes
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
The string above represents 3 different permissions for 3 different groups
First 3 characters represents 

## Extended Attributes

## User Owner

## Group Owner
