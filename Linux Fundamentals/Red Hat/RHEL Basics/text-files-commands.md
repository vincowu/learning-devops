# Common Commands used on text files

## Touch command
creates a zero byte file
````
touch [option][file]
````

## Tree command
tells you the tree structure of a folder
````
tree [options]
````
## Grep command
Will search file for the string you input. Command is called global regular expression print (used for searching and matching text patterns in files)

````
grep "string" filename 

# will return string in the file and 5 lines after that 
grep "string" filename -A 5
````
FLAGS
- v will exclude anything containing the "string"
## Input/output redirection
Redirection is a way in linux to change the standard input/output devices. Anytime a linux command is run, it takes an input and returns an output.
In most cases standard input device is the keyboard and output device is the screen. More info can be found [here](https://www.guru99.com/linux-redirection.html)
Symbols used:
- The ">" will redirect the command output to the file found after the ">". If said file doesn't exist it will create a new file with the name listed, else it will overwrite.
- The ">>" operator will perform same function but will not overwrite an existing file. Instead it will append it to the back of the file 
Example of output redirection is 
````
# will rewrite listings file
ls -al > listings

# will append ls -al output to listings file
ls -al >> listings
````

### Error redirection
Whenever a program/command is executed in the terminal, there are 3 files always open.
1. Standard input (0)
2. Standard output (1)
3. Standard error (2)

Error redirection is very common feature used because lots of commands in Unix/Linux will retrun lots of errors. A solution to prevent erros from cluttering up a normal program output would be to redirect all standard error to another file, leaving only the output of the command to be redirected to another file.
Example of this would be
````
ls Documents ABC> dirlist 2>&1

````
In the command above, the error output is also redirected to standard output. Standard output is alraeady being re-directed to file >dirlist so both error and stard output are written to file [dirlist](https://www.guru99.com/linux-redirection.html).

Note: ">&" redirects output of one file to another.

## Word Count
Will return the number of lines found in a file.
````
wc -l file.yaml
````