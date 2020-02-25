#!usr/bin/env python 3

def grep(flags,params,directs):

  with open(params[1], "r") as f:
    lines = f.read().splitlines()

  # Used for testing parameters
  choice = flags[0]

  # Budget switch statment
  switcher = {
    '-c': count,
    '-n': getlines,
    '-i': nocase,
    '-v': nomatch
  }

  func = switcher.get(choice, lambda: "Error: enter a valid parameter")
  func(params[0], lines)

# Find the number of times the word appears in file
def count(word, lines):
  foundnum = 0
  # Count the number of times the word appears in file
  for line in lines:
    if line.find(word) > 0:
      foundnum += 1
    
  print(word, "was found ", foundnum, " times.")


# Show what lines contain the specified word.
def getlines(word, lines):
  linenum = 0
  # Show the lines in which the word appears.
  for line in lines:
    if line.find(word) > 0:
      print(linenum, line)

    linenum += 1

# Allows user to search for a word, ignoring its case
def nocase(word, lines):
  # Create an uppercase version of word
  upperword = word.upper()

  for line in lines:
    if line.find(word) > 0 or line.find(upperword) > 0:
      print(line)

# Prints out the lines that do not contain the word
def nomatch(word, lines):

  for line in lines:
    if line.find(word) < 0:
      print(line)


if __name__ == "__main__":
  grep("-c", "bee.txt", " ")