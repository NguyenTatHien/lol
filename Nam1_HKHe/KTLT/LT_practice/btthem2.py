import os, shutil
def check(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    else:
        print("Folder not found")

check(path = input("Nhập đường dẫn: "))