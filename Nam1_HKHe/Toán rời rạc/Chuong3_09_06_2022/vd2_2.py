A = [0, 1, 2, 3, 4, 5, 6, 7]
B = [2, 4, 6, 8, 10]
def intersection(A, B):
    ketqua = []
    for x in A:
        if x in B:
            ketqua = ketqua + [x]

print(intersection(A, B))