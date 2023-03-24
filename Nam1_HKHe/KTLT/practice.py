def giai_thua(n):
    if n == 0:
        return 1
    else:
        return giai_thua(n-1) * n

print(giai_thua(n = int(input("Giai thua cua: "))))