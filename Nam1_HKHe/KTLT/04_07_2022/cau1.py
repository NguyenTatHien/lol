import os 
def ktra_file(path):
    if os.path.exists(path):
        return True

path = input("Mời nhập đường dẫn vào thư mục: ")
if ktra_file(path) == True:
    print("Thư mục đã tồn tại")
else:
    os.mkdir(path)