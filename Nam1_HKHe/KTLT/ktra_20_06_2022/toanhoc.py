def tongphantu():
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
    
        print("\nTổng các phần tử trong danh sách là: ", sum(a))

    danh_sach()


def canbac3():
    x = float(input("Nhập vào x muốn tính căn bậc 3: "))
    bac3 = x ** 1/3
    print(f"Căn bậc 3 của x là: {bac3}")
