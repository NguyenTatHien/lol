def tongdayso():
    tich = 0
    n = 0
    
    n = int(input("Hãy nhập vào số n: "))
    
    for i in range(1, n + 1) :
        tich += 1/(2*i*i)
    print("Tich la: ",tich)
tongdayso()
