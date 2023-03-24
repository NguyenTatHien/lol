def chu_so_lon_nhat_1(n):
    if n == 0:
        return
    else:
        m = n % 10
        global max
        if m > max:
            max = int(m)
    chu_so_lon_nhat_1(n/10) #Đệ qui: gọi lại chính nó

max = 0
chu_so_lon_nhat_1(int(input("Nhap vao day chu so can tim so lon nhat: ")))
print("so lon nhat la: ",max)