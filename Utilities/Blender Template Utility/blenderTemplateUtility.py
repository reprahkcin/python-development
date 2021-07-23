import os

TEMPLATE_FILE = os.getcwd()+"\\Utilities\\Blender Template Utility\\TEMPLATE.blend"
print(TEMPLATE_FILE)
ROOT_DIRECTORY = os.getcwd()+"\\Utilities\\Blender Template Utility\\Blender Projects"

# Copy TEMPLATE_FILE to every subdirectory in ROOT_DIRECTORY
# for directory in os.listdir(ROOT_DIRECTORY):
#     if os.path.isdir(ROOT_DIRECTORY+"\\"+directory):
#         print("Copying TEMPLATE_FILE to "+directory)
#         os.system("copy "+TEMPLATE_FILE+" "+ROOT_DIRECTORY+"\\"+directory)
