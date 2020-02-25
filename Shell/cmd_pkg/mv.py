# NAME
#        mv 

# SYNOPSIS
#        mv

# DESCRIPTION
#        - mv command moves files or directories from one place 
#          to another and/ or renames files.


#                       IMPORTS                                         #     
from shutil import move        # imports move module from shutil
import os

def mv(cmd,flags,params,direct):
    try:
        move(params[0],params[1])
    except IOError:
        print(" Destination: (" + params[1] + " ) not writable")
    return