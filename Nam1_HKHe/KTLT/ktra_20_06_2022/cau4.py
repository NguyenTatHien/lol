ds = [5, 7, 8, 1, 3]
def timkiem(x):
    if x in ds:
        return x
    else:
        return 0
x = float(input("Nhập vào số cần tìm: "))
if x == timkiem(x):
    print("Có trong danh sách")
else:
    print("Không có trong danh sách")