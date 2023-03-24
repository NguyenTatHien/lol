def dientich_hcn():
    d = float(input("Nhập vào chiều dài: "))
    r = float(input("Nhập vào chiều rộng: "))
    s = d * r
    return print("Diện tích HCN là: ",s)
def chuvi_hcn():
    d = float(input("Nhập vào chiều dài: "))
    r = float(input("Nhập vào chiều rộng: "))
    p = (d + r)*2
    return print("Chu vi HCN là: ",p)
def dientich_tamgiac():
    day = float(input("Nhập vào độ dài đáy: "))
    h = float(input("Nhập vào chiều cao h: "))
    s = 1/2*day*h
    return print("Diện tích tam giác là: ",s)
def chuvi_tamgiac():
    a = float(input("Nhập vào cạnh a: "))
    b = float(input("Nhập vào cạnh b: "))
    c = float(input("Nhập vào cạnh c: "))
    p = a + b + c
    return print("Chu vi tam giác là: ",p)
def dientich_hinhtron():
    r = float(input("Nhập vào bán kính r: "))
    s = r * r * 3.14
    return print("Diện tích hình tròn là: ", s)
def chuvi_hinhtron():
    r = float(input("Nhập vào bán kính hình tròn: "))
    p = r * 2 * 3.14
    return print("Chu vi hình tròn là: ", p)