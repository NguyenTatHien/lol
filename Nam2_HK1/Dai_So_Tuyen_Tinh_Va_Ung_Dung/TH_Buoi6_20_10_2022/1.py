import math

import numpy as np 
a = np.array([1,2,3]) 
b = np.array([4,5,6]) 
tich = np.inner(a,b) # tích vô hướng 
print (tich) 
print(np.dot(a,b))

import numpy as np 
a = np.array([1,2,-3]) 
print(np.linalg.norm(a)) 
a = np.array([1,2,-3])
print(np.linalg.norm(a,1))
    
def chuan(v, k):
    tong = 0
    for i in range(len(v)):
        tong = tong + abs(v[i] * k)
    ketqua = math.pow(tong, 1.0/k)
    return ketqua

import numpy as np 
a = np.array([1,2,-3]) 
print(chuan(a, 1)) 
print(np.linalg.norm(a,1)) 
print(chuan(a, 2)) 
print(np.linalg.norm(a,2)) 
print(chuan(a, 3)) 
print(np.linalg.norm(a,3)) 
print(chuan(a, 1000)) 
print(np.linalg.norm(a,1000))

from scipy import linalg 
print(linalg.norm(a)) 
print(linalg.norm(a, 100)) 
print(linalg.norm(a, 1000))

import numpy as np 
m = 10 
v1 = np.array([5,-4,3]) 
v2 = np.array([4,3,-2]) 
v3 = np.array([-4,-3,-1]) 
v4 = np.array([-9,8,6]) 
mi = np.array([2,5,2,1]) 
M = np.array([v1,v2,v3,v4]) 
MT = M.transpose() 
print(MT)
v = (1.0/m)*MT.dot(mi)
print(v)

import sympy as sym 
x, y = sym.symbols('x y') 
xy = sym.Matrix([x,y])  # khai báo vector: (x, y)T
A = sym.Matrix([[1, -68],[1,1]]) 
v = sym.Matrix([0, 1]) 
nghiem = sym.solve([A*xy-v])  # phương trình được chuyển về 1 phía 
print(sym.pretty(nghiem)) 

import sympy 
x, y, Lambda = sympy.symbols('x y Lambda') 
I = sympy.eye(2)
A = sympy.Matrix([[2,3],[3,-6]]) 
phuongtrinh = sympy.Eq(sympy.det(Lambda*I-A), 0) 
nghiem = sympy.solve(phuongtrinh) 
print([sympy.N(phantu,4) for phantu in nghiem]) 
print (sympy.pretty(nghiem))

import numpy as np 
A = np.array([[2,3],[3,-6]]) 
D = np.array([[-7,0],[0,3]]) 
P = np.array([[-1.0/3, 3],[1,1]]) 
from numpy import linalg 
from numpy import linalg as LA 
P1 = LA.inv(P) # tính giá trị nghịch đảo của P 
print (P1)
print(A.dot(P))
print(P.dot(D))
print (D **2)