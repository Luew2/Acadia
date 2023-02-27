import os

path = r"./Sticker_Generator/data/"
print(path)
for file_name in os.listdir(path):
    # construct full file path
    file = path + file_name
    print(file)
    if os.path.isfile(file):
        print("Deleting file:", file)
        os.remove(file)
