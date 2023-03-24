def selection_sort(arr):
    for i in range(len(arr)):
        min = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[min], arr[i] = arr[i], arr[min]
    return arr

arr = [65, 27, 16, 24, 3]
n = selection_sort(arr)
print(n)