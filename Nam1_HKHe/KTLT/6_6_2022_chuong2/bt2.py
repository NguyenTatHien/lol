
def DIEMSO(n):
    if n == 0:
        return 0
    else:
        return 1 + DIEMSO(int(n/10))

dem = 0
dem = DIEMSO(int(input("Nhap day chu so can dem: ")))
print(f"Dãy số trên có {dem} số")