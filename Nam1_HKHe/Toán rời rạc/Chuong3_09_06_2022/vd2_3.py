def difference(A,B):
    ketqua = []
    for x in A:
        if x not in B:
            ketqua = [x]
    return ketqua

A = [0, 1, 2, 3, 4, 5, 6, 7]
B = [2, 4, 6, 8, 10]
print(difference(A,B))