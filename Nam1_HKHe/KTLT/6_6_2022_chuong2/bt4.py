def tinhtong():
    tong = 0
    n = 0
    n = int(input("Hãy nhập vào số n: "))
    for i in range(1, n + 1) :
        tong += 1 / i
    print("Tong so la: ", tong)

tinhtong()
