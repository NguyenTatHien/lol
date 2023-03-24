import os
def ktra_file(path):
    if os.path.exists(path):
        return True

path = input("Mời nhập đường dẫn file cần kiểm tra: ")
if ktra_file(path) == True:
    os.remove(path)
else:
    print("Tập tin không tồn tại")