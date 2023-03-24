def tong(chuoi):
    kq = 0
    a = chuoi.split(",")
    for i in a:
        kq += int(i)
    return kq

def file_sum():
    n = input("Nhập vào đường link cần tính: ")
    n2 = input("Nhập vào đường link để xuất kết quả: ")
    dulieu = open(n,"r")
    kq = open(n2, "w")
    for i in dulieu:
        kq.write(str(tong(i)))

file_sum()