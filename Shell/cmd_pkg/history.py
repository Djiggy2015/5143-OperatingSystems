from os import path

def history(flags, params, directs):
    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath, "..","history.log"))
    histDict = {}
    count =1 
    with open (filepath, "r") as f:
        for line in f.readlines():
            histDict[count] = line
            print(f"{count}   {line}",end='')
            count+=1
    return histDict