# Linking Linux Files
Linking files in linux can be split into 2 categories.
1. Soft Links
    - Soft Link will point to the original file on your system
2. Hard Links
    - Hard link will create a copy of the file
One difference between soft and hard links are that soft links can point to other files/directories on another file system while hard links can't do [that](https://www.freecodecamp.org/news/linux-ln-how-to-create-a-symbolic-link-in-linux-example-bash-command/)

## Linking Syntax
````
ln -FLAGS SOURCE_FILE OPTION_SYMBOLIC_LINK
````
Some key flag would be:
    -s will specify that this will be a symbolic link, otherwise it will be a hard link

## Unlinking
To unlink a symlink, you can use:
````
rm linked_file.format

or

unlink linked_file.format
````

## Key differences between hardlink and soft link
- Hard Link has an additonal name for existing file while special link points to another file
- Hard Link can't be created for directories while soft lnik can
- Hard Link can't cross file system boundaries or partiions while softlink can
- Hard Link has same inode(unique value for each file) number and permissions as original file while soft link has different inode and file 
- Soft Link doesn't contain file data