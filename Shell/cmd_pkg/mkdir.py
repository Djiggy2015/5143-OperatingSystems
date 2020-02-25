# NAME
#        mkdir (mkdir.py)

# SYNOPSIS
#        mkdir

# DESCRIPTION
#        - creates a directory named path with a specific numeric mode.


#        IMPORTS                     #         
import os          # imports os module 


#              MKDIR METHOD           #

def mkdir(flags,params,directs): #every function takes three arguments- flags, params and directs

    os.mkdir(params[0])             # working with params[0]
 
#                              Debugging Code                                           #
if __name__ == "__main__":
                                    #   def mkdir (params):
                                    #   hard coding just for example and testing method #
    pd = "C:/Users/Ladelle/"        #   pd = parent directory 
    cd = "mkdirTestDirectory"       #   cd = created directory
    path = os.path.abspath(os.path.join(pd,cd))        #   path = joined pd to cd.
    print(path)
    try:
        os.mkdir(path)                        #calling os.mkdir with hardcode path
        print (f"Directory Created {cd}")
    except OSError as error:              # printing error using os error message 
        print(error)                      # prints out error message
                                          # print("cannot create " cd "directory")

