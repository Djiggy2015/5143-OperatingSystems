
# NAME
#        touch - change file access and modification times

# SYNOPSIS
#        touch

# DESCRIPTION
#       change file access and modification times.

#                              IMPORTS                                              #

import os              # imports os module
import sys             # import sys module -functions relevant to system of computer.
import datetime        # import datetime module
from os import utime
import time 
import stat

#                            TOUCH METHOD                                             #

def touch(flags, params, directs):    # passing in filename

 if os.path.exists(params[0]):
    os.utime(params[0])
    stinfo = os.stat()
    print(stinfo)
 else:
    f = open(params[0],"w+")
    print(stinfo)
    f.close()

    
#                             DEBUGGING CODE                                         #
 
if __name__ == "__main__":
    if os.path.exists():
        os.utime("OperatingSystem.txt")
        stinfo = os.stat()
        print (stinfo)
    else:
        with open ("OperatingSystem.txt", 'a') as f:
            pass
        