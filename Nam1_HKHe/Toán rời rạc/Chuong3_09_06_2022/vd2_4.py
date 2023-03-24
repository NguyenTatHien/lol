def isSubSet(A, B): 
    ketqua = True # DUNG 
    for x in A: 
        if x not in B: 
            ketqua = False # SAI 
    return ketqua 
A = [0, 1, 2, 3, 4, 5, 6, 7] 
B = [2, 4, 6, 8, 10] 
print(isSubSet(A, B))
B = [1, 3, 5, 7]
print(isSubSet(A, B))
print(isSubSet(B, A))
def equalSets(A, B): 
    return isSubSet(A, B) and isSubSet(B, A) 
print(equalSets([1, 3, 5, 7], [7, 3, 1, 5]))