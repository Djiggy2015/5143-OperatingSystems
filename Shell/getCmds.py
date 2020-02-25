# This may be useful for the "wc" and "split" commands as well

def getCmds():
    with open("cmd_pkg/__init__.py", "r") as f:
        # Makes a list of lines that aren't blank and don't start with "#", then
        # removes preceeding and proceeding whitespace and newlines from the line.
        # Finally, it splits each line into a list of the words that make it up
            
        # lines = [line.strip() for line in f.readlines() if not line.startswith(("#","\n"))]
        # words = [line.split() for line in lines]
        
        # Shorter version
        lines = [line.strip().split() for line in f.readlines() if not line.startswith(("#","\n"))]

    # Creates a dictionary with the format <commandName>:<cp.commandName> 
    cmdDict = {}
    for line in lines:
        key = line[3]
        val = "cp." + key
        cmdDict[key] = val

    return (cmdDict)


    
