from os import path

def help(cmd):
    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath, "..", f"help/{cmd}.txt"))
    with open(filepath,"r") as f:
        text = f.read()
    print(text)
