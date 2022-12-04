import shutil
import os
  
# Define the source and destination path
PATH = os.getcwd()
source = PATH
destination = PATH+"/dest_folder"

if destination.exists():
    next
else:
    os.mkdir(PATH+"/dest_folder")
  
# code to move the files from sub-folder to main folder.
files = os.listdir(source)
for dirs, subdirs,files in os.walk(source):
    for file in files:
        file_name = os.path.join(source, dirs, file)
        if file_name == file_name:
            next
        print(file_name)
        shutil.copy(file_name, destination)
print("Files Moved")
