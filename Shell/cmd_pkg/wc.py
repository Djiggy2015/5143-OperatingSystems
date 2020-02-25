#!usr/bin/env python 3
import re # used to get number of words

def wc(flags,params,directs):
  # If no flags were passed in, do all three
  if not flags:
    filenum = 0
    for p in params:
      with open(params[filenum], "r") as f:
        lines = f.read().splitlines()
      
      with open(params[filenum], "r") as f:
        words = f.read()

      numlines = len(lines)
      result = len(re.findall(r'\w+', words))
      chars = len(words)

      print("There are ", numlines, " lines in", params[filenum])
      print("There are ", result," words in", params[filenum])
      print("There are ", chars, "characters in the file", params[filenum])
      filenum += 1

  # If flags were passed in, do the requested action.
  else:
    # Get the number of lines in the file
    filenum = 0
    if flags[0] == "-l":
      for p in params:
        with open(params[filenum], "r") as f:
          lines = f.read().splitlines()

        numlines = len(lines)

        print("There are ", numlines, " lines in ", params[filenum])
        filenum += 1

    # Find the number of words present in the file. (Special characters are generally ignored.)
    elif flags[0] == "-w":
      filenum = 0
      for p in params:
        with open(params[filenum], "r") as f:
          words = f.read()

        result = len(re.findall(r'\w+', words))

        print("There are ", result," words in", params[filenum])
        filenum += 1

    elif flags[0] == "-m":
      filenum = 0
      for p in params:
        with open(params[filenum], "r") as f:
          chars = f.read()

        result = len(chars)

        print("There are ", result, "characters in the file ", params[filenum])
        filenum += 1

    else:
      print("Not a valid flag value. The flags are -l, -m, and -w.")


if __name__ == "__main__":
  wc(["-c"],["five.txt"]," ")