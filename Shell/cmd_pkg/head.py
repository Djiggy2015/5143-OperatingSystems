#!usr/bin/env python 3
from os import path, getcwd

# This function will display the first few lines of a file
# The user can specify how many lines they want, but the 
# default is 10.
def head(flags,params,directs):

  if not flags:
    end = 10
    with open(params[0], "r") as f:
      lines = f.read().splitlines()


  elif flags[0] == '-n':
    end = params[0]
    end = int(end)

    # Open the file and read it line per line
    with open(params[1], "r") as f:
      lines = f.read().splitlines()

  # Print out the first few lines of the file
  for line in lines[: end]:
    print(line)


if __name__ == "__main__":

  head("","bee.txt","")