#!/usr/bin/env python3

import threading
import sys
import cmd_pkg as cp
from getCmds import getCmds
import cmd_pkg.fDict
import shlex
import re
import os

class CommandHelper(object):
    def __init__(self):

        # Automatically generates the commands dictionary
        self.commands = getCmds()        
        self.flagList=cp.fDict.flags()
        self.directsList=cp.fDict.direct()
        self.flagsDict = cp.fDict.fDict()
        
        # Makes the string value from self.commands a callable object
        for key in self.commands:
            self.commands[key] = eval(self.commands[key]) 

     
    def exists(self, cmd):  # Checks that a command exists
        return cmd in self.commands


    def parseit(self,cmd_in):               
        flags=[]
        params=[]
        directs=[]
        cmd = cmd_in[0]

        if cmd_in[1:]:
            args = cmd_in[1:] 
            
            for item, i in zip(args, range(0, len(args))):
                if item in self.flagsDict[cmd]:
                    flags.append(item)
                
                elif item in self.directsList:  # ex ['c:/user/2.txt', '<', 'c:/user/1.txt']

                    if item == '>':
                        item = "w+"
                    elif item == '>>':
                        item = "a+"
                    elif item == '<':
                        item = "r+"
                    if i > 0 and not (str.isdigit(args[i-1])): #i >0 and the previous argument isn't a number
                        directs.append(args[i-1])   # typically the read file (this won't always be used)
                    directs.append(item)            # the mode to open the writefile in
                    directs.append(args[i+1])       # the writefile
                else:
                    params.append(item)
        else: 
            args = None

        self.runit(cmd=cmd, flags=flags, params=params, directs=directs )


    def runit(self, **kwargs):
   
        if 'cmd' in kwargs:
            cmd = kwargs['cmd']

        else:
            print("How did you mess this up?")

        if kwargs['flags']:
            flags = kwargs['flags']         
        else:
            flags = []

        if kwargs['params']:
            params = kwargs['params']            
        else:
            params = []

        if kwargs['directs']:
            for item in kwargs['directs']:
                if item == '>':
                    item = "w+"     #write
                elif item == '>>':
                    item = "a+"     #append
                elif item == '<':
                    item = "r+"     #read (but it will make a file if one does not exist)
            directs = kwargs['directs']  
            print(directs)                     
        else:
            directs = []

        self.commands[cmd](flags=flags, params=params, directs=directs)


if __name__ == "__main__":
    ch = CommandHelper()
    
    basepath = os.path.dirname(__file__)
    filepath = os.path.abspath(os.path.join(basepath, "history.log"))

    while True:
        skip = False
        ch.runit(cmd='pwd', flags=None, params=None, directs=None)  #Print working dir above the cmd prompt ##DISABLE WHEN DEBUGGING
        cmd_in = input("% ")

        while len(cmd_in.rstrip()) < 1: # Check for empty lines
            print("Error: no command entered") 
            cmd_in = input("% ")
        
        cmd = cmd_in.split()[0] # First word is the command

        if cmd == "exit":  # This should be right after we pass input to history.py
            sys.exit(0)
        
        # Help
        if cmd == "help":
            cmd = cmd_in.split()[1]
            if cmd == "!":
                cmd = "hist"
            if ch.exists(cmd):
                print(cp.help(cmd))
                skip = True
            else:
                print("Invalid command")
        
       # History 
        num = 0    
        if cmd[0] == "!":
            if len(cmd)>1 and (str.isdigit(cmd[1:])):
                num =cmd[1:]
                cmd = 'hist'
                cmd_in = cp.hist(num)
            else:
                print("Invaild entry")        
                
        with open(filepath,"a+") as log:    
            log.write(f"{cmd_in}\n")

        if skip == False:
            if ch.exists(cmd):
                cmd_in = shlex.split(cmd_in,posix=True) # Split user input into multiple strings
                ch.parseit(cmd_in) # Parses the user input
            else:
                print("Invalid command")
        else:
            pass

