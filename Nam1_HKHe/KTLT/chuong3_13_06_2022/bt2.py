import math
def add():
    a = float(input("Nhập vào a: "))
    b = float(input("Nhập vào b: "))
    s = a + b
    return print(s)
def sub():
    a = float(input("Nhập vào a: "))
    b = float(input("Nhập vào b: "))
    sub = a - b
    return print(sub)
def multiple():
    a = float(input("Nhập vào a: "))
    b = float(input("Nhập vào b: "))
    multiple = a * b
    return print(multiple)
def divide():
    a = float(input("Nhập vào a: "))
    b = float(input("Nhập vào b: "))
    divide = a / b
    return print(divide)
def can_bac_hai():
    a = float(input("Nhập vào a: "))
    return print(math.sqrt(a))
