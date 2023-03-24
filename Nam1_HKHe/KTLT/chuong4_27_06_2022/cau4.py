import os
n = input("Nhập vào đường dẫn có tên tập tin: ")
if os.path.exists(n):
    f = open(n, "r", encoding="utf-8")
    print(f.read())
else:
    print("Tập tin không tồn tại")