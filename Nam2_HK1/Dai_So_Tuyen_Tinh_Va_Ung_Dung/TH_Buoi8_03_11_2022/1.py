import numpy as np 
u = np.array([2,-1,5,0]) 
v = np.array([4,3,1,-1]) 
w = np.array([-6,2,0,3]) 
x = 2*u-(v+3*w) 
print (x) 
x = 0.5*(2*u-v-3*w)
print (x)
from numpy import linalg 
A = np.matrix([[0, -1, 3],[1, 1, 1],[4, 2, 2]]) 
B = np.array([-1, -2, -2]) 
X = np.linalg.solve(A, B)
print (X)
A = np.matrix([[1,0],[0,0]])
B = np.matrix([[0,0],[0,1]]) 
from numpy import linalg as LA
# print(LA.inv(A))
# print(LA.inv(B))
print(LA.inv(A+B))
print(LA.det(A))
print(LA.det(B))
print(LA.det(A+B))
import sympy as sp 
x, y = sp.symbols('x y') # khai báo 2 biến x và y 
A = sp.Matrix([[x, y],[y, x]]) # lưu ý: kiểu ma trận của sympy là ‘Matrix’ (viết hoa) 
x1, y1 = sp.symbols('x1 y1') 
A1 = sp.Matrix([[x1, y1],[y1, x1]]) 
x2, y2 = sp.symbols('x2 y2') 
A2 = sp.Matrix([[x2, y2],[y2, x2]]) 
print(A1.T)
print((A1+A2).T)
print(((A1+A2).T).equals(A1+A2))
c = sp.symbols('c') 
print (c*A)
print(((c*A).T).equals(c*A))
import sympy as sp 
c1, c2, c3 = sp.symbols('c1 c2 c3')
print(sp.solve([c1-2*c3, 2*c1+c2, 3*c1+2*c2+c3], [c1, c2, c3]))
import sympy as sp 
c1, c2 = sp.symbols('c1 c2')
u1, u2 = sp.symbols('u1 u2')
print(sp.solve([c1+c2-u1,c1-c2-u2]))
u1 = 0
u2 = 0
print(sp.solve([c1+c2-u1,c1-c2-u2]))

import numpy as np 
P = np.array([[0,0,3,3,1,1,2,2,1,1],[0,5,5,4,4,3,3,2,2,0]]) 
vecdelta = np.array([4,2]) 
P_caua = (P.T + vecdelta).T
print (P_caua)
import numpy as np 
P = np.array([[0,0,3,3,1,1,2,2,1,1],[0,5,5,4,4,3,3,2,2,0]]) 
vecdelta = np.array([4,-2]) 
matran_biendoi = np.array([[1.0, 0.0], 
 [0.0, 2.0]]) 
P_caub = (P.T @ matran_biendoi + vecdelta).T 
print (P_caub)

import sympy as sp 
from sympy import lambdify
x1, x2, x3 = sp.symbols('x1 x2 x3') 
bieuthuc1 = x1 - x2 + x3 
f1 = lambdify([x1, x2, x3], bieuthuc1, 'numpy') 
a, b, c = sp.symbols('a b c') # khai báo thêm 3 biến a, b, c giả định X = (a, b, c) 
d, e, f = sp.symbols('d e f') # khai báo thêm 3 biến d, e, f giả định Y = (e, d, f) 
print(f1(a, b, c))
print(f1(d, e, f))
print(f1(a+d, b+e, c+f))
print(f1(a,b,c) + f1(d,e,f) == f1(a+d, b+e, c+f))
print((f1(a,b,c) + f1(d,e,f)).equals( f1(a+d, b+e, c+f)))
q = sp.symbols('q')
print((q*f1(a,b,c) + f1(d,e,f)).equals(f1(q*a+d, q*b+e, q*c+f).expand()))
bieuthuc2 = 2*x2 + 3* x3 
f2 = lambdify([x1, x2, x3], bieuthuc2, 'numpy') 
print((q*f2(a,b,c) + f2(d,e,f)).equals(f2(q*a+d, q*b+e, q*c+f).expand()))
import sympy as sp 
a, b = sp.symbols('a b') 
x, y = sp.symbols('x y') 
print(sp.solve([a+3*b-x, 2*a+5*b-y],[a,b]))
fu1 = np.array([1,1,2]) 
fu2 = np.array([4,2,1]) 
fu = a*fu1 + b*fu2 
print (fu)
fu = a.subs(a, -5*x + 3*y)*fu1 + b.subs(b, 2*x - y)*fu2 # thay giá trị tìm được ở trên vào 
print (fu)
x1, x2, x3 = sp.symbols('x1 x2 x3')
print(sp.solve([x1+x2-x3, 2*x1+3*x2-x3, 3*x1+5*x2-x3],[x1, x2, x3]))
import numpy as np 
import math 
from scipy import linalg as LA 
B = np.matrix([[1.0/math.sqrt(2), 1.0/math.sqrt(2)], 
 [-1.0/math.sqrt(2),1.0/math.sqrt(2)]]) # cos(pi/4) 
print(LA.orth(B))
print(np.array([[-0.70710678, 0.70710678], [ 0.70710678, 0.70710678]]))