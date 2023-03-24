def tuyen_tinh(array, n, x):
    for i in range(0, n):
        if array[i] == x:
            return i

    return -1

array = [20, 30, 15, 5, 10, 40]
x = float(input("Nhap x: "))
n = len(array)
result = tuyen_tinh(array, n, x)
if result in array:
    print("Co trong danh sach")
print("Phan tu tim thay tai vi tri la: ", result)

def tim(self, x):
    vi_tri = 0
    hien_tai = hien_tai.self
    