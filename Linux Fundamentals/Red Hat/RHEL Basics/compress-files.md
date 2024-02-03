# Compressing and Decompressing Files
Archiving is a process of collecting and storing one or more files/directories in a single file
- tar and star are commands used for this purpose

Compressing is reducing size of a file
- gzip and bzip are tools sued for compression in Linux


````
# Archiving
tar [OPTIONS] [ARCHIVE-FILE] [FILE OR DIRECTORY TO BE ARCHIVED]
tar cvf /home/archives/user1.tar user1

# Can add z flag to use gzip in the tar command
tar cvfz /home/archives/user2.tar.gz

# Will list the archive
tar tvf archives/user1.tar

# To zip archive file
gzip archives/user1.tar 

bzip2 archives/user1.star 

# star archiving
star -cv file=/home/archives/user1.star user1

# Can also use star archiving together with bzip
star -cv -bz file=/home/archives/user2.star.bz


# to view archives
star -tv file=/home/archives/user1.star
````


