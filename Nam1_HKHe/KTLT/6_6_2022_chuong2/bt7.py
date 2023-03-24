def day_so():
    tong = 0
    n = 0
    
    n = int(input("Hãy nhập vào số n: "))
    
    for i in range(1, n + 1) :
        tong += i ** 2
    
    print("Tổng số là: ", tong)
    day_so()
day_so()