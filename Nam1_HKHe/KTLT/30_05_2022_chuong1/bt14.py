def du_doan_mua(thang):
    if 1 <= thang <= 3:
        return 3
    elif 4 <= thang <= 6:
        return 6
    elif 7 <= thang <= 9:
        return 9
    elif 10 <= thang <= 12:
        return 12
    elif thang < 0 or thang > 12:
        return 0

thang = int(input("Nhập vào tháng: "))
kq = du_doan_mua(thang)
if kq == 3:
    print("Mùa xuân")
elif kq == 6:
    print("Mùa Hạ")
elif kq == 9:
    print("Mùa Thu")
elif kq == 12:
    print("Mùa Đông")
else:
    print("Tháng ko hợp lệ")
