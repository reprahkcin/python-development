from ntpath import join
import os

folderList = open(
    join(os.getcwd(), "Utilities/Folder Creator/folderNames.txt"), "r")

folders = [line.split() for line in folderList]


consolidated = []

for names in folders:
    ready = '-'.join(names)
    consolidated.append(ready)

for path in consolidated:
    os.mkdir(path.lower())
