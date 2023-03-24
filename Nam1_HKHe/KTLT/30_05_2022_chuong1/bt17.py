def trung_binh_cong():
    l = []
    tong = 0
    solan = 0
    for i in range(nhap): 
        solan += 1
        n = i + 1
        print("Số nguyên thứ", n,"là: ", end=" ")
        l.append(int(input()))
        tong += n
    print("Số vừa nhập là: ")
    for i in l:
        print("\t", i, end=" ")
    print("\nTrung bình cộng của các số trên là: ",tong / solan)

nhap = int(input("Nhập vào số phần tử cần tính tbc: "))
trung_binh_cong()