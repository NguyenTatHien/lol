import numpy as np
from scipy import linalg #
A = np.array([ [0,1], [1,0]])
print(A) 
temp = A.dot(A) 
print(temp) 
k= 6
for i in range(k-1): 
    temp = temp.dot(A) 
    print (temp) 
    print('---')

B = np.array([ [0,-1], [-1,0]])
print(B)
temp = B.dot(B)
print(temp)
k= 5 
for i in range(k-1):
    temp = temp.dot(B) 
    print (temp) 
    print('---')

C = np.array([ [1, 0, 0], [0, 0.5, 1], [0, 0, 0.5] ])
print(C) 
temp = C.dot(C)
print(temp) 
k= 1000
for i in range(k-1): 
    temp = temp.dot(C)
print(temp)
k= 1000
for i in range(k-1): 
    temp = temp.dot(C)
print(temp)

M = np.array([ [0.8, 0.3], [0.2, 0.7]]) 
MM = M.dot(M)
print (MM)
MM = M.dot(M)
print(MM)
for i in range(100):
    MM = MM.dot(M)
print(MM)

M = np.array([ [0.8, 0.3], [0.2, 0.7]]) 
P, L, U = linalg.lu(M)
print (P) 
print (L)
print (L)
print (U)
print(L.dot(U))

A = np.array([ [0,1,0,1],[0,0,1,0],[1,0,0,1],[1,1,0,0]]) 
temp = A.dot(A) 
print(temp)
temp = temp.dot(A) 
print(temp) 
A = np.array([ [0,1,0,1],[0,0,1,0],[1,0,0,1],[1,1,0,0]])
sumA = A
temp = A.dot(A)
k = 3
sumA = sumA + temp 
for i in range(1, k-1):
    temp = temp.dot(A) 
    sumA = sumA + temp
print (temp) 
print (sumA)