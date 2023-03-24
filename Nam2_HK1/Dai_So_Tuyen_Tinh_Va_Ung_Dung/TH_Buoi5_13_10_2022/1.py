import numpy as np
D = np.array([[1,2],[3,4]]) 
E = np.array([[1,2],[3,5]]) 
np.copyto(E, D) 
print(E) 
B = np.matrix("[1 2 3; 4 5 6]") 
x = np.array([['a','b'],['c','d']]) 
y = 'x'
C = np.matrix([[x,y],[1, 2]] )
print (C) 
A = np.matrix([[[1,2],[3,4]],[[5,6],[7,8]]]) 
A = np.array([[[1,2],[3,4]],[[5,6],[7,8]]]) 
print(A) 
from numpy import matlib
G = matlib.identity(5) 
print (G) 
H = matlib.randn(3,2)
print(H)
K = matlib.zeros([4,4])
print(K) 
c = [3, 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14, 2]
M = np.mat([[1,2],[3,4]])
for i in range(len(c)): 
    ci = np.mat([[1,1],[1,0]]) 
    ci[0, 0] = c[i] 
    if (i==0): 
        M = ci 
    else: 
        M = M.dot(ci)
print(M)
print (M[0,0]/M[1,0])