import os
import getpass
import subprocess

def who(cmd, flags, params, direct):
    if not direct:
        print(subprocess.check_output("who"))
    else:                                           # checking which ones to use not sure yet
        with open(direct[0], 'w') as outfile:
            outfile.write(subprocess.check_output("who"))
            print("USER with os.getuid:",os.getuid())
            print ("USER using getpass",getpass.getuser()) 
        
    return
