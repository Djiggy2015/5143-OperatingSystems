import os

def cd(flags,params,directs):
    if flags:
        if flags[0] == "~":
            os.chdir(os.path.expanduser("~"))

    elif params:
        dirPath = params[0]

        if len(params) ==1:
            if os.path.isdir(dirPath):    
                os.chdir(dirPath)

            else:
                print ("Path doesn't exist")
                return           
        
        else:
            print("Only one file path is accepted!") 
            return   

    else:
            os.chdir(os.path.expanduser("~"))