import os
n = input("Nhập vào tên file cần sao chép: ")
if os.path.exists(n):
    f = open(n, "r", encoding="utf-8")
    r = f.read()
    print("Đây là dữ liệu của file: \n", r)
    n2 = input("Nhập nơi cần paste: ")
    p = open(n2, "a", encoding="utf-8")
    p.write(r)
else:
    print("Tập tin không tồn tại")