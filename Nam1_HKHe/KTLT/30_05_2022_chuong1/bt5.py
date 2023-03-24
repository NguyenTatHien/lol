def timgiatri(n):
    global ds
    ds = []
    for i in range(n):
        x = int(input(f"Nhập vào số nguyên thứ {i+1}: "))
        ds.append(x)
    return ds

n = int(input("Nhập vào số phần tử n: "))
print("Danh sách của bạn: ", timgiatri(n))

def countX(ds,x):
    return ds.count(x)
x = int(input("Mời nhập số cần đếm: "))
print("Số {} có {} lần". format(x,countX(ds,x)))