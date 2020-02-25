# NAME
#        sort
# DESCRIPTION
#        - sorts or merge records(lines) of text (and binary) files.
#                       IMPORTS                                         #    
from numbers import Number 
def sort(flags, params, directs):
    lines =[]
    if not directs: 
       with open(params[0], "r+") as f:
        type(lines)
        lines = f.read().splitlines()
        lines.sort()
        print(lines)
    else: 
        with open(directs[2],directs[1]) as wf:
            with open(params[0],"r+") as rf:
                s_lines = rf.read().splitlines()
                s_lines.sort()
                for line in s_lines:
                    wf.write(line)
    return