import numpy as np
from scipy import linalg, sparse 
D = np.mat([[3,4], [5,6]])
print(D) 

C = np.mat(np.random.random((5,7))) 
print(C)

A = np.mat(np.random.random((2,2)))
print(A)

b = np.array([(1+5j, 2j, 3j),(4, 5, 6)])
B = np.asmatrix(b)
print(b)
print(B)

print(A.T)

print(A.I)

print(linalg.inv(A))

M = np.array([[-1,3,2],[0,-2,1],[1,5,-2]])
M_lower = np.tril(M)
print(M_lower) 

M = np.array([[-1,3,2],[0,-2,1],[1,5,-2]])
M_upper = np.triu(M) 
print(M_upper)

M = np.array([[-1,3,2],[0,-2,1],[1,5,-2]]) 
v_diag = np.diag(M) 
print(v_diag)
M_diag = np.diag(v_diag)
print(M_diag)

import sympy as sp
x = sp.Symbol('x')
y = sp.Symbol('y')
z = sp.Symbol('z')
print(sp.solve([x*x+2-6, y-1-6, x+z-1, 2*x*x-8, z*z+4-5, y-z-8], [x, y, z]))

x = [1,2,3]
y = [1,2,3]
print(all([x[i] == y[i] for i in range(len(x))]))

y = [1,2,4]
print(all([x[i] == y[i] for i in range(len(x))]))

import numpy as np
print(np.array_equal([1,2],[1,2]))
print(np.array_equal(np.array([1,2]), np.array([1,2])))

import numpy as np
A = np.reshape(np.arange(36.0), (6,6))
print(A)

I6 = np.identity(6)
print(I6)

print(A.size)

print(np.matrix.diagonal(A))

A = A + I6
print(A)

vecB = np.array([1., 2., 3., 4., 5., 6.]) 
C = A.dot(vecB)
print(C)

D = np.array([[1., 2., 3., 4., 5., 6.], [1., 0., 1., 0., 1., 0.]]) 
print(D)

# E = A.dot(D)

F = np.array([[1., 1.], [2., 0.], [3., 1.], [4., 0], [5., 1], [6., 0.]])
G = A.dot(F)
print(F)
print(G)
print(np.linalg.inv(A))
print(np.linalg.inv(np.linalg.inv(A)))