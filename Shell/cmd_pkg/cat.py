#!usr/bin/env python 3

# This command will allow the user to look at the desired file
# (or files) on their terminal. They can specify whether to have
# line numbers or not. If the file does not exist, cat will create
# it for the user.
def cat(flags, params, directs):

  # If the only parameters are files
  # just print the files out to screen.
  if not flags and not directs:
    filenum = 0
    for p in params:
      with open(params[filenum], "r") as f:
        lines = f.read().splitlines()

      for line in lines:
        print(line)

      print(" ")
      filenum += 1

  if not directs:
    # Show user the file along with line numbers
    if flags[0] == '-n':
      filenum = 0
      linenum = 1
      for p in params:
        with open(params[filenum], "r") as f:
          lines = f.read().splitlines()

        for line in lines:
          print(linenum, ":", line)
          linenum += 1

        print(" ")
        filenum += 1
        linenum = 1

    else:
      print("Invalid Operation.")

  if not flags:
    if directs[0] == '>':      
      with open(params[0], 'a') as f:
        pass

      print("File was successfully created.")

    else:
      print("Invalid operation.")


  

if __name__ == "__main__":
  cat(">", ["chunky.txt"], " ")