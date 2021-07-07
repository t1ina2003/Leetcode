import os
import shutil

allEntryinDir = os.scandir("./") 
allFileEntryinDir = [ entry for entry in allEntryinDir if entry.is_file() ]
# get list of problem number of filename in the base folder.
filenames = [ fileEntry.name for fileEntry in allFileEntryinDir ]
problemFiles = [ pf for pf in filenames if pf.split('.')[0]!='' and pf.split('.')[0].isnumeric()]
folderNamse = [ fn.split('.')[0] for fn in problemFiles ]
# # try create folders base on the list.
for foldername in set(folderNamse):
    try:
        os.mkdir("./"+foldername)
        print("Directory " + foldername + " created.")
    except FileExistsError:
        print("Directory " + foldername + " already existed.")
# try move files into folders.
for file in problemFiles:
    try:
        shutil.move("./"+file, "./"+file.split('.')[0]+"/"+file)
        print("File " + file + " move succeed.")
    except FileExistsError:
        print("File " + file + " move failed.")
