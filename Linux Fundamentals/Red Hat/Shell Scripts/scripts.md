# Shell Scripts
Anatomy of a Shell script
````
#!/bin/bash                       Header

# What the script does, etc       Comments

USERFILE=$1                       Variables

if [ "$Userfile" = "" ]           Main Body
then
    echo "Please specify input!"
    exit 10
elif test -e $USERFILE
then
    for user in `cat $USERFILE
    do
        echo "Creating the "$user" user..."
        useradd -m $user
    done
    exit 20
else
    echo "invalid input"
    exit 30
fi
````

# For Loops
````
for user in billy bob joe ; do useradd -m $user ; done
grep -E 'billy|bob|joe' /etc/passwd

````

More examples of shell scripts
