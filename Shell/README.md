# 5143-OS-Shell
## Shell Project
#### Operating Systems Spring 2020

#### Group Members

| Name                          | Email       | Github Username |
| ----------------------------- | ----------- | --------------- |
| [Ben Diekhoff](https://github.com/BenDiekhoff/5143-OS-Diekhoff) | ben.diekhoff@gmail.com   | BenDiekhoff    |
| [Ladelle Augustine](https://github.com/Ladelle/5143-OS-Augustine) | ladelle2016@gmail.com   | Ladelle    |
| [Matthew Stanley](https://github.com/Djiggy2015/5143-OperatingSystems) | fiddlebum1@gmail.com | Djiggy2015  |

#### Project Files

:x: = not started
:black_square_button: = work in progress
:white_check_mark: = finished and working

| Command | Flags/Params | FileName                        | Author  | Works                 | Description/Notes                                         |                 
| ------- | ------------ | ------------------------------- | ------- | -------               | --------------------------------------------------------- |                 
|         |              |[README.md](#shell-project)      | Ben     | :white_check_mark: |                                                           |                    
|         |              |[shell.py](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/shell.py)       | Ben     | :white_check_mark: |                                                           |
|         |              |[getCmds.py](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/getCmds.py)       | Ben     | :white_check_mark: |  *NOT A SHELL COMMAND* Automtically generates command dictionary for shell.py                      |
|          |              |[fDict.py](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/cmd_pkg/fDict.py)       | Ben     | :white_check_mark: |  *NOT A SHELL COMMAND* Lists and dicts used for parsing by shell.py                    |
| [cat](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/help/cat.txt )     | file             |[cat.py](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/cmd_pkg/cd.py)         |  Matt    | :white_check_mark:                   | Concatenates a file(s) and displays results to std out    |
|         | file1,file2,fileN             |                                 |		|							|	Display each of the files as if they were concatenated				|
| [cd](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/help/cd.txt )      | directory |[cd.py](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/cmd_pkg/cd.py)          | Ben     | :white_check_mark:                   | Change directory                                          |
|         |              |                                 |		|							| change to home dir |
|         |    ~        |                                 |		|							| change to home dir														|
|         |    ..        |                                 |		|							| change to parent dir															|		
| [chmod](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/help/chmod.txt )   |              |[chmod.py](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/cmd_pkg/chmod.py)       | Matt       | :white_check_mark:                   | Change file mode                                          |
| [cp](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/help/cp.txt )      | file1 file2             |[cp.py](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/cmd_pkg/cp.py)          |  Matt       | :white_check_mark:                   | Copy a file and call it file 2                                             |
| [grep](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/help/grep.txt )   | 'keyword' file |[grep.py](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/cmd_pkg/grep.py)        |  Matt       | :white_check_mark:                   | Search a file(s) for keywords and print lines where pattern is found |
|         |  -l            |                                 |		|							|	only return file names where the word or pattern is found																|
| [head](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/help/head.txt )    | file            |[head.py](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/cmd_pkg/head.py)        |  Matt       | :white_check_mark:                   | Display first 10 lines of a file                          |
|         | -n             |                                 |		|							|	display the first few lines of a file																| 
| [history](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/help/history.txt ) |              |[history.py](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/cmd_pkg/history.py)     | Ben     | :white_check_mark:                   | Shows all your previous commands                          |
| [less](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/help/less.txt )    | file             |[less.py](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/cmd_pkg/less.py)        | Matt        | :white_check_mark:                   | Display a file a page at a time                           |
| [ls](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/help/ls.txt )      |              |[ls.py](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/cmd_pkg/ls.py)          | Ladelle    |:white_check_mark:    | List files and folders in working directory               |
|         | -a             |                                 |		|							| Show hidden files	as well																|
|         | -l             |                                 |		|							| long listing format																	|
|         | -h             |                                 |		|							| human readable format																		|
| [mkdir](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/help/mkdir.txt )   | directory              |[mkdir.py](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/cmd_pkg/mkdir.py)       | Ladelle    |:white_check_mark:  | Create a directory                                        |
| [mv](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/help/mv.txt )     | file1 file2              |[mv.py](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/cmd_pkg/mv.py)          | Ladelle      | :white_check_mark:     | Move or rename file1 to file2                                     |
| [pwd](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/help/pwd.txt )     |              |[pwd.py](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/cmd_pkg/pwd.py)         | Ben     | :white_check_mark:    | Print working directory                                   | 
| [rm](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/help/rm.txt )      | file             |[rm.py](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/cmd_pkg/rm.py)          |  Matt      | :white_check_mark:                   | Remove file                                               |
|         | -r             |                                 |		|							| recurses into non-empty folder to delete all		|
|         | fil*e or *file or `file*`             |                                 |		|							| removes files that match a wildcard			|
| [split](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/help/sort.txt )   |              |[split.py](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/cmd_pkg/split.py)       |  Matt    | :white_check_mark:                   | Split a file into pieces                                  |
|         | -b             |                                 |		|							| Create smaller files byte_count bytes in length					|
|         | -l             |                                 |		|							| Create smaller files n lines in length					|
| [sort](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/help/split.txt )    |              |[sort.py](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/cmd_pkg/sort.py)        |  Ladelle |:white_check_mark:  |Sort or merge records (lines) of text (and binary) files
| [tail](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/help/tail.txt )    | file             |[tail.py](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/cmd_pkg/tail.py)        | Ben     | :white_check_mark:                   | Display the last 10 lines of a file                       |
|         | -n             |                                 |		|							|	display the last few lines of a file																|
| [touch](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/help/touch.txt )   |              |[touch.py](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/cmd_pkg/touch.py)       |Ladelle         |:white_check_mark:     | Change file access and modification times                 |
|         | -m             |                                 |		|							| change the modification time of the file					|
|         | -a             |                                 |		|							| change the access time of the file												|
| [wc](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/help/wc.txt )      |              |[wc.py](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/cmd_pkg/wc.py)          | Matt     | :white_check_mark:    | Count number of lines/words/characters in a file          |
|         | -l             |                                 |		|							| count number of lines in file																	|
|         | -m            |                                 |		|							| count number of characters in file																	|
|         | -w             |                                 |		|							| count number of words in file																	|
| [!x](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/help/hist.txt )      |              |[hist.py](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/cmd_pkg/hist.py)          | Ben     | :white_check_mark:                   | Load command `x` from your history so you can run it again |
| [who](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/help/wc.txt )     |              |[who.py](https://github.com/BenDiekhoff/5143-OS-Shell/blob/master/cmd_pkg/who.py)         |   Ladelle      |:white_check_mark:                    | Lists users currently logged in                           	|
|         |              |                                 |		|							|																	|

#### Directory Structure

```
/5143-OS-Shell
│   .gitignore
│   bees.txt
│   binary.dat
│   file.txt
│   getCmds.py
│   headTailtest.txt
│   ls.txt
│   README.md
│   shell.py
│   sort.py
│   sortTest.txt
│   sorttofile.txt
│   splitfile.txt
│   starwars.txt
│   test.txt
│
├───cmd_pkg
│   │   bee.txt
│   │   cat.py
│   │   cd.py
│   │   chmod.py
│   │   cp.py
│   │   fDict.py
│   │   grep.py
│   │   head.py
│   │   help.py
│   │   hist.py
│   │   history.py
│   │   less.py
│   │   ls.py
│   │   mkdir.py
│   │   mv.py
│   │   pwd.py
│   │   rm.py
│   │   sort.py
│   │   split.py
│   │   tail.py
│   │   touch.py
│   │   wc.py
│   │   who.py
│   │   __init__.py
│   │
│   └───__pycache__
│           cd.cpython-38.pyc
│           ls.cpython-38.pyc
│           pwd.cpython-38.pyc
│           rm.cpython-38.pyc
│           touch.cpython-38.pyc
│           __init__.cpython-38.pyc
│
├───help
│       cat.txt
│       cd.txt
│       chmod.txt
│       cp.txt
│       grep.txt
│       head.txt
│       help.txt
│       hist.txt
│       history.txt
│       less.txt
│       ls.txt
│       mkdir.txt
│       mv.txt
│       pwd.txt
│       rm.txt
│       sort.txt
│       split.txt
│       tail.txt
│       touch.txt
│       wc.txt
│       who.txt
│
└───__pycache__
        getCmds.cpython-38.pyc
```

