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


