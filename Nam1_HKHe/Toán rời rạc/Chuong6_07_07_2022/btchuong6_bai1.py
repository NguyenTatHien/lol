def union(x , y):
    kq = 0 
    if x == 1 and y == 1:
        kq = 1
    return kq

def choose(x, y):
    kq = 1
    if x == 0 and y == 0:
        kq = 0
    return kq 

def negation(x):
    if x == 0:
        return 1
    return 0

A = 1
B = 1 
A_ = negation(A)
B_ = negation(B)
A_B = union(A_, B)
AB_ = union(A, B_)

print(choose(A_B, AB_))