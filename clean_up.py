import os

path = r"./Sticker_Generator/data/"
print("Deleting files in " + path + "...")
for file_name in os.listdir(path):
    # construct full file path
    file = path + file_name
    if os.path.isfile(file):
        os.remove(file)
