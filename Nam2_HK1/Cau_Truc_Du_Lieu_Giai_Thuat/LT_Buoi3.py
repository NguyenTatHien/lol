def BubbleSort(a, n):
    for i in range(0, i<n-1, 1):
        for j in range(n-1, j>i, -1):
            if a[j] < a[j-1]:
                print(a[j], a[j-1])

BubbleSort(input("Nhap a: "), int(input("Nhap n: ")))
