def luythua(x, n):
    ketqua = 1
    for i in range(n):
        ketqua = ketqua * x
    return ketqua

print(luythua(2, 1))
print(luythua(2, 0))