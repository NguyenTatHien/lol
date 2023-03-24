import hinhhoc
while True:
    n = input("Bạn muốn tính công thức nào(chuvitamgiac, dientichtamgiac): ")
    if n.lower() == "done":
        break
    elif n == "chuvitamgiac":
        a = input("Nhập vào chiều dài a: ")
        b = input("Nhập vào chiều dài b: ")
        c = input("Nhập vào chiều dài c: ")
        print("Chu vi tam giác là: ",hinhhoc.chuvi_tamgiac(a,b,c))
    elif n == "dientichtamgiac":
        day = input("Nhập vào chiều dài đáy: ")
        h = input("Nhập vào chiều cao: ")
        print("Diện tích tam giác là: ",hinhhoc.dientich_tamgiac(day, h))
    else:
        print("Không có trong danh sách")
        continue