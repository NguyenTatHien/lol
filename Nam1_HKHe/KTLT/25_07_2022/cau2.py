def dem_soluong(n):
    if n == 0:
        return 0
    else:         
         return 1 + dem_soluong(int(n/10))
    

# TEST
dem = 0
dem = dem_soluong(int(input("Nhập vào dãy số nguyên dương cần đếm: ")))
print(dem)
