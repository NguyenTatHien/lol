def tinh_tong(n):
    if n**3 == 1**3:
        return 1**3
    return n**3 + tinh_tong(n - 1**3)
 
print("Hãy nhập vào số n: ")
n = int(input())
tong = tinh_tong(n)
print("Tổng là: ", tong)