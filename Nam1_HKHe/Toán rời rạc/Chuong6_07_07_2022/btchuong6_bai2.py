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
D = 1
A_ = negation(A)
B_ = negation(B)
D_ = negation(D)
A_B_ = union(A_, B_)
A_B_D = union(A_B_, D)
A_B = union(A_, B)
A_BD_ = union(A_B, D_)
AB_ = union(A, B_)
AB_D_ = union(AB_, D)
AB = union(A, B)
ABD = union(AB, D)
a = choose(A_B_D, A_BD_)
b = choose(AB_D_, ABD)
print(choose(a, b))