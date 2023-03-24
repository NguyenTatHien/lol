def giaithua(n):
    if n > 0:
        giaithua = 1
        for i in range(1, n+1):
            giaithua *= i
            print(n, "Giai thừa bằng: ", giaithua)
    else:
        print("Bạn hãy nhập lại số n > 0")
    return n

n = int(input("Nhập giá trị n: "))
giaithua(n)