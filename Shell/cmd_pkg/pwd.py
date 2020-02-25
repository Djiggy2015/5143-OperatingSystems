import os

# NAME
#        pwd - print name of current/working directory

# SYNOPSIS
#        pwd

# DESCRIPTION
#        Print the full filename of the current working directory.
def pwd(flags,params,directs):
    workingDir = os.getcwd()
    return print(workingDir)


