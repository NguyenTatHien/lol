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

    print("\nSo nho nhat trong danh sach la: ", min(a))

danh_sach()