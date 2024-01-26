# Accessing Linux Systems
Need to access server with proper credentials
Methods of accessing Linux Systems:
1. Console Login
    - since we don't know the ip address, might need to install web console
    Note to access
2. su command
    - become other user and execute commands as that user
    - example of command su - userName (su - root or su -)
3. sudo command
    - allows user to become another user and execute commands as another
    - sudo -i
4. SSH command
    - ssh suite of commands allow secure remote loginx, remote command execution, connection tunneling and file transfers
    ````
    ssh-keygen
    ssh-copy-id web_user@other-server
    ssh web_user@other-server 
    ````
To view the version of redhat, you would check the /etc/redhat-release file

### Securely Transfering Files
When transferring data you can use scp or sftp, both the files and password are encrypted so that anyone peering into the traffic won't be able to view data.
can find out more [here](https://linuxize.com/post/how-to-use-scp-command-to-securely-transfer-files/)
How the STP command will look:
````
scp [OPTION] [user@SRC_HOST:]file1 [user@DEST_HOST:}file2
````
to view more options check man pages (man scp)

SFTP(SSH File Transfer Protocol) is another secure file protocol that transfers files over encrypted SSH transport and is secure.
Unlike SCP (only supports file transfers), SFTP lets you perform a bunch of operations on remote files.

````
sftp remote_username@server_ip

sftp> mget filename.zip
Fetching /home/remote_username/filename.zip to filename.zip
/home/remote_username/filename.zip                           100%   24MB   1.8MB/s   00:13

# to view commands use help
````
The commands above will allow us to download the files to our local.



