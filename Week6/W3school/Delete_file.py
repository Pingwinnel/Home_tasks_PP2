#Delete a File

import os
os.remove("demofile.txt")

#Check if File exist:
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
  
#Delete Folder
import os
os.rmdir("myfolder")