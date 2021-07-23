# import the os module
import os

ROOT_DIR = "C:/Users/harpern/Box/BI254 Donor Scans/bi-254-isolated-muscle-animations/Blender Projects"

OUTPUT_FOLDER = "D:/GIT/python-development/Utilities/Blender Template Utility/output"

# get path to TEMPLATE.blend file
TEMPLATE_FILE = os.path.join(ROOT_DIR, "TEMPLATE.blend")


# make a list of each folder name in ROOT_DIR
FOLDERS = os.listdir(ROOT_DIR)

# make a folder for each item in folders list in OUTPUT_FOLDER and put a copy of the TEMPLATE_FILE in each
for FOLDER in FOLDERS:
    FOLDER_PATH = os.path.join(OUTPUT_FOLDER, FOLDER)
    os.mkdir(FOLDER_PATH)
    os.system("copy " + TEMPLATE_FILE + " " + FOLDER_PATH)


# for folder in folders:
#     FOLDER_PATH = os.path.join(OUTPUT_FOLDER, folder)
#     os.mkdir(FOLDER_PATH)
