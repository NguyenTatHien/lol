#Bài 3
def tim_so_lonnho1(a, b):
    if a > b:
        return a
    else:
        return b

a = int(input("Nhap vao so nguyen a: "))
b = int(input("Nhap vao so nguyen b: "))
kq = tim_so_lonnho1(a, b)
if kq == a:
    print(f"{a} la so lon nhat: ")
else:
    print(f"{b} la so lon nhat")