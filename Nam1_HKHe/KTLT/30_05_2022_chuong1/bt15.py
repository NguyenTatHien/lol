def kiem_tra_nam_nhuan(nam):
    if nam % 400 == 0 or nam % 4 == 0 and nam % 100 != 0:
        return nam
    else:
        return 0
        
nam = int(input("Nhap vao nam: "))
kq = kiem_tra_nam_nhuan(nam)
if kq == nam:
    print("Đây là năm nhuận")
else:
    print("Đây ko phải năm nhuận")