#!usr/bin/env python 3

import os
import shutil # Module for copying files
def cp(source, dest):

  # Make sure the source file exists before doing anything
  if os.path.exists(source):
    # If the file already exists, just copy the contents of file1 
    # to file 2
    if os.path.exists(dest):
      basepath = os.path.dirname(__file__)

      sourcepath = os.path.abspath(os.path.join(basepath, "..", source))
      destpath = os.path.abspath(os.path.join(basepath, "..", dest))

      print(sourcepath)
      print(destpath)

      shutil.copyfile(source, dest)

     # If the file does not exist, create it with the touch command and
     # then copy 
    else:
      # Create the file for writing
      with open(dest, 'a') as f:
        pass

      basepath = os.path.dirname(__file__)

      sourcepath = os.path.abspath(os.path.join(basepath, "..", source))
      destpath = os.path.abspath(os.path.join(basepath, "..", dest))

      print(sourcepath)
      print(destpath)

      shutil.copyfile(source, dest)
  
  else:
    print("Error: ", source, " does not exist.")



if __name__=="__main__":
  cp("new.txt", "file2.txt")