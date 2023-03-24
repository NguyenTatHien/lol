def giaithua(x):
    if x == 0 or x == 1:
        return 1
    else:
        return giaithua(x-1) * x

x = int(input("Bạn muốn tính giai thừa của số?: "))
kq = giaithua(x)
print(f"Giai thừa của số {x} là: {kq}")

#x! = (x-1)! * x
#2! = (2-1)! * 2
#3! = (3-1)! * 3
#4! = 3! * 4