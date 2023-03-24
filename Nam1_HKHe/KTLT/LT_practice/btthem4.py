def tb_cong(path, path2):
    global f2, tbcong
    f = open(path, "r")
    f2 = open(path2, "w", encoding="utf-8")
    dem = 0
    tong = 0
    for i in f:
        chia = i.split()
        for j in chia:
            tong += float(j)
            dem += 1
            tbcong = tong / dem
        
tb_cong(path = input("Mời nhập đường dẫn cần tính trung bình cộng: "), path2 = input("Mời nhập đường dẫn ket qua: "))
f2.write("Trung bình cộng là: "+str(tbcong))