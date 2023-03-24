import os
def check_folder(path):
    if os.path.exists(path):
        print("Folder don't exist")
    else:
        os.mkdir(path)
        print("Folder was created!")

check_folder(path = input("Write the path: "))