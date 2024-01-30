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
    -s will specifiy that this will be a symbolic link, otherwise it will be a hard link

## Unlinking
To unlink a symlink, you can use:
````
rm linked_file.format

or

unlink linked_file.format
````