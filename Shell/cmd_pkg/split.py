#!usr/bin/env python 3
import math
import os

def split(flags,params,directs):

  if flags[0] == "-l":
    splitmore(flags, params, directs)

  elif flags[0] == "-b":
    bytesplit(flags,params,directs)

  else:
    # Open the file so we can determine its length in number
    # of lines.
    with open(params[0], "r") as f:
      file = f.read().splitlines()

    # This basic version splits the file into two pieces
    numlines = len(file)

    chunk = numlines / 2
    chunk = int(chunk)

    str1 = " "
    str2 = " "
    for line in file[: chunk]:
      str1 += line

    for line in file[chunk : numlines]:
      str2 += line

    file1 = open("xaa", "w")
    file1.write(str1)
    file1.close()

    file2 = open("xbb", "w")
    file2.write(str2)
    file2.close()
  

def splitmore(flags, params, directs):
  with open(params[0], "r") as f:
    file = f.read().splitlines()

  numlines = len(file)
  print("There are ", numlines, "in this file.")
  flines = input("How many lines do you want in each smaller file?")
  flines = int(flines)

  # This will tell us how many files to make
  divided = numlines / flines
  divided = math.ceil(divided) + 1 # Round it up to a whole number if necessary

  start = 0
  end = flines
  str1 = " "
  name = " "

  # Start creating the smaller files
  for n in range(1 , divided):
    for line in file[start : end]:
      str1 += line
      str1 += "\n"

    name = 'Xx' + str(n)

    filex = open(name, "w")
    filex.write(str1)
    filex.close()

    # Increment to the next lines to be read
    start += flines

    if(end + flines > numlines):
      end = numlines

    else:
      end += flines

    str1 = " "

# Splits a file into smaller files of specified size(in bytes)
def bytesplit(flags,params,directs):
  with open(params[0], "r") as f:
    file = f.read().splitlines()

   # Get the size of that file
  size = os.path.getsize(params[0])

  print("File size is", size)
  choice = input("How large do you want your files to be? (in bytes): ")
  choice = int(choice)

  # Idiot proof it (Speaking from experience here...)
  if(size / choice > 10):
    print("No. Your computer does NOT want that.")
  
  else:

    index = 1
    name = "file1.txt"

    # Print data out to smaller files until they become full,
    # then switch to a new one.
    for line in file:
      with open(name, "a") as f:
        f.write(line)

        # Once the file has become full, start writing to a new
        # file.
        if int(os.path.getsize(name)) > choice:
          index += 1
          name = "file" + str(index) + ".txt"
  






  
if __name__ == "__main__":
  split("-b", "starwars.txt", " ")