def danh_sach():
    a = []
    n = int(input("Nhap vao so luong phan tu: n = "))

    print("Nhap vao cac phan tu cho danh sach:")
    for i in range(n):
        print("\tPhan tu thu", i+1 ,"la:", end=" ")
        a.append(int(input()))

    print("Danh sach vua nhap la:")
    for i in a:
        print("\t", i, end="")

    for i in range(0, n-1):
        for j in range(i+1, n):
            if a[i] > a[j]:
                tg = a[i]
                a[i] = a[j]
                a[j] = tg

    print("\nDanh sach sau khi sap xep tang dan la:")
    for i in a:
        print("\t", i, end="")

danh_sach()