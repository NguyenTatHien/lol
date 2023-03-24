path = input("Mời nhập đường dẫn cần tính trung bình cộng: ")
path2 = input("Mời nhập đường dẫn ket qua: ")
f = open(path, "r")
f2 = open(path2, "a")
dem = 0
tong = 0
for i in f:
    chia = i.split()
    for j in chia:
        tong += float(j)
        dem += 1
        tbcong = tong / dem
        
print("Trung bình cộng là: ",f2.write(str(tbcong)))