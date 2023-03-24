# import random
# def BubbleSort1(a):
#     n = len(a)
#     for i in range(n-1):
#         for j in range(n-1, i-1, -1):
#             if a[j] < a[j-1]:
#                 a[j], a[j-1] = a[j-1], a[j]
                

# def BubbleSort2(a):
#     n = len(a) - 1
#     for i in range(n, 0, -1):
#         for j in range(0, i):
#             if a[j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]

def SelectionSort(a):
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min=j
        arr[min],arr[i]=arr[i],arr[min]
    return arr
arr=[65,27,16,24,3]
print(SelectionSort(arr))

# def InputData(n):
#     a = []
#     for i in range(n):
#         a = a + [random.randint(-30, 50)]
#     return a

# def OutputData(a):
#     return a

# def Main():
#     n = int(input("Nhap so phan tu: "))
#     a = InputData(n)
#     print("Mang phat sinh ngau nhien: ", OutputData(a))
#     BubbleSort1(a)
#     print("Mảng sau khi sắp xếp tăng dần: ", OutputData(a))
#     BubbleSort2(a)
#     print("Mảng sau khi sắp xếp giảm dần: ", OutputData(a))


# if __name__ == "__main__":
#     Main()