def sodaonguoc(n):
    while (n != 0):
        print(n % 10, end="")
        n = n // 10  
        
sodaonguoc(int(input("nhập số nguyên n cần đảo ngược: ")))