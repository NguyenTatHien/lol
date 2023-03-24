def De(n):
    D = (n-1)*(5*D[n-1] + 2*D[n-2])
    if n == 1:
        D[n] = (n-1)*(5*D[n-1] + 2*D[n-2])
        print(D)
    elif n == 2:
        D[n] = (n-1)*(5*D[n-1] + 2*D[n-2])
        print(D[n])
    else:
        return D

De(float(input("Nhap n: ")))