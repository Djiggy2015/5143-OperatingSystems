#!usr/bin/env python 3
import os
import shutil # for recursive deletion

# Remove function for shell
# Parameters: filename
# This function will remove the requested file if it exists.

def rm(flags,params,directs):

  if flags:

    # Delete a directory and all of its contents
    if flags[0] == '-r':
      shutil.rmtree(params[0]) # Recursivel delete a directory
      print(params[0], "was deleted.")

  else:

    # If the user did not enter a filename, return an error message
    if not params:
      print("Error: Please enter a file name after rm.")

    # If the user entered a file name, see if it exists and remove it if it does
    else:
      filename = params[0]
      basepath = os.getcwd()

      # Used for wildcard deletion of files.
      if "*" in filename:
        substring = filename[1 :]

        for file in os.listdir(basepath):
          if file.endswith(substring):
            os.remove(os.path.join(basepath,file))
            print(file, "was deleted")
      

      else:
        index = 0
        for p in params:
          if os.path.exists(params[index]):
            os.remove(params[index])
          else:
            print("Error: The file does not exist.")
        index += 1
  return


if __name__=="__main__":

  rm([" "],["file"],[" "])
