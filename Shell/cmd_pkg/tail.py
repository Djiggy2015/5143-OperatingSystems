from os import path

def tail(flags,params,directs):
    # basepath = path.dirname(__file__)
    # filepath = path.abspath(path.join(basepath, "..","history.log"))
    print (params)
    print(directs)

    if not directs: #no directs

        #no directs, with flags
        if '-n' in flags:
            filename = params[1]
            num = int(params[0])  # print the last <num> lines
            
            with open(filename, "r") as f:
                lines = f.read().splitlines()
                numLines = len(lines)
                for line in lines[(numLines-num): ]:
                    print (line)

        else:   #no directs, no flags
            filename = params[0]
            num = 10
            with open(filename, "r") as f:
                lines = f.read().splitlines()
                numLines = len(lines)
                for line in lines[(numLines-num): ]:
                    print (line)

#consider the command "tail -n 30 headTailtest.txt >> file.txt" 
# flags = ['-n']
# params = ['30', 'headTailtest.txt', 'file.txt']
# directs = ['headTailtest.txt', 'a+', 'file.txt']     
# 
    elif (directs or '&' in directs):   # there are directs or & is in directs (tells a program to run in the background)
        ls = []
        if '-n' in flags:   #directs and flags
            mode = directs[1]   # file open mode ( >> = a+, > = w+, < = r+)
            readfilename = directs[0]   # file to read from (to the left of >> or >)
            writefilename = directs[2] # file to write to (file on the right of >> or >)
            num = int(params[0])  

            with open (readfilename, "r") as rf: #open the read file
                lines = rf.read().splitlines()  # make a list with all the lines from the read file
                numLines = len(lines)           # count the the total number of lines
                for line in lines[(numLines-num): ]: #picks out only the last X lines we want
                    ls.append(line)                 # appends them to a list
            with open (writefilename, mode) as wf:     # open the write file
                for line in ls:                    
                    wf.write(f"{line}\n")     # write the lines from out list to the file      


        else: # directs and no flags
            mode = directs[1]
            readfilename = directs[0]
            writefilename = directs[2]
            num = 10

            with open(readfilename, "r") as rf:   #dir[1] is the filename, dir[0] is the mode (read, write, append, etc)":
                lines = rf.read().splitlines()
                numLines = len(lines)
                for line in lines[(numLines-num): ]:    
                    ls.append(line)

            with open (writefilename, mode) as wf:
                for line in ls:
                    wf.write(f"{line}\n")



if __name__ == "__main__":
    from os import path, getcwd     
    workingdir = getcwd()
    basepath = path.dirname(__file__)
    print (workingdir)
    print(basepath)

    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath, "..","headTailtest.txt"))

    with open(filepath, "w+") as f:
        f.write("FIRST LINE\n")
        
        for i in range(2,50): 
            f.write(str(i) + "\n")
        
        f.write("LAST LINE")     
        f.seek(0)
        lines = f.read().splitlines()
    
    numLines = len(lines)
    first = lines[ :10]
    last = lines[(numLines-10): ]

    for i in lines[ :10]:
        print(i)

    for i in lines[(numLines-10): ]:
        print(i)



        