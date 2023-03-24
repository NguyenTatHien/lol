def dem_(path):
    global dem
    dem = 0
    f = open(path,"r")
    for i in f:
        t = i.split(";")
        for e in t:
            dem += 1

path = input("Nhập vào đường dẫn cần đếm: ")
dem_(path)
print("Số lượng của file là: ",dem)