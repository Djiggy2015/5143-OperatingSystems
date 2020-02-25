#!usr/bin/env python 3
import os
import textwrap

# This function allows the user to read in a large file in pieces.
# They can either choose to advance the file line by line or advance
# it by a "page" or terminal size.
def less(flags,params,directs):
  # Get the size of the terminal window and insert it into rows
  # and columns.
  rows, columns = os.popen('stty size', 'r').read().split()

  # Convert these values into integers
  rows = int(rows)
  columns = int(columns)

  # This will open the file and make lines from it
  with open(params[0], "r") as f:
    file = f.read().splitlines()
  
  numlines = len(file)
  # Initialize variables
  start = 0
  end = rows
  newpage = 'p'
  
  # Display the file to user until they press q
  # Should probably use a switch statement here
  while newpage != 'q' and newpage != 'Q':

    for line in file[start : end]:
      print(line)
  
    newpage = input()

    if newpage == 'h' or newpage == 'H':
      displayhelp()

    # If the user wants to go back a line.
    if(newpage == 'b' or newpage == 'B'):

      # Makes sure user doesn't break terminal
      if(start > 0):
        start -= 1
        end -= 1

    # Lets the user skip forward a page
    elif(newpage == 'p' or newpage == 'p'):

      if(end < numlines - rows):
        start += rows
        end += rows

    # Lets the user skip back a page.
    elif(newpage == 'o' or newpage == 'O'):
      if(start >= rows):
        start -= rows
        end -= rows

    # Let the user skip to the end of the file
    elif(newpage == 'e' or newpage == 'E'):
      start = numlines - rows
      end = numlines

    # Let the user move to the beginning of the file
    elif(newpage == 's' or newpage == 's'):
      start = 0
      end = rows

    # Move the page forward on any other input.
    else:

      if(end < numlines):
        start += 1
        end += 1

  return

# This function will show the user the commands available
def displayhelp():
  choice = "h"

  while choice != 'q' and choice != 'Q':
    print("\n#################################################")
    print("Here are the available commmands:")
    print("b or B: Move back 1 line.")
    print("p or P: Skip forward 1 page (text window size).")
    print("o or O: Skip backwards 1 page (text window size).")
    print("e or E: Move to end of file.")
    print("s or S: Move to start of file.")
    print("To stop reading file: q or Q.\n\n")
    print("Press q or Q to go back to file.")
    print("###################################################")

    choice = input()

  return


if __name__ == "__main__":
  less("",["bee.txt"],"")
