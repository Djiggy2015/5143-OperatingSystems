from os import path

def hist(num):
    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath, "..","history.log"))
    histDict = {}
    count = 1
    with open (filepath, "r") as f:
        for line in f.readlines():
            line = line.strip()
            histDict[count] = line
            count += 1
    return (histDict[int(num)])




