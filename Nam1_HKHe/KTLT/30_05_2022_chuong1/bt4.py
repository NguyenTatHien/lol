def timgiatri(n):
    global ds
    ds = []
    for i in range(n):
        x = int(input(f"Nhập vào số nguyên thứ {i+1}: "))
        ds.append(x)
    return ds

n = int(input("Nhập vào số phần tử n: "))
print("Danh sách của bạn: ", timgiatri(n))

def check():
    if a in ds:
        return True
    else:
        return False

a = int(input("Nhập vào số nguyên a: "))
kq = check()
if kq == a:
    print("Có trong danh sách")
else:
    print("Không có trong danh sách")