import numpy as np
n = 4
X = np.array(range(1,n+1))
sigma = np.array([4,3,2,1])
def sgn_by_def(sigma):
    ket_qua=1.0
    for i in range(len(X)-1):
        for j in range(i+1,len(X)):
            ket_qua=ket_qua*((X[i]-X[j])/(sigma[i]-sigma[j]))
    return int(ket_qua)
sigma=np.array([2,1,3,4])
print(sgn_by_def(sigma))

# -----------------------------
# B1
from itertools import permutations
n=3
X=[]
for i in range(1,n+1):
    X.append(i)
Sn=list(permutations(X))
print(Sn)
# B2
det = 0
# B3
def phatsinh_dinhthuc (n):
    X=[]
    for i in range (1, n+1):
        X.append (i)
    Sn= list (permutations (X) )
    dinhthuc = ""
    for sn in Sn:
       sigma= np.array ( [1])
       sigma.resize ( [n])
       product = ""
       for i in range (1,n+1) :
           sigma [sn.index (i) ] = i
           product= product +"a"+str (i) +str (sn. index (i) +1)
           dau = sgn_by_def (sigma)
           if (dau != 1):
              product= "-" +product
           else:
               product = " +" + product
           dinhthuc = dinhthuc + product 
    return dinhthuc
phatsinh_dinhthuc(2)
# -----------------------------------

def tinhtoan_dinhthuc (A) :
    X=[]
    import math
    n=int (math.sqrt (A. size) ) 
    for i in range (1, n+1):
        X.append (i)
    Sn=list (permutations (X))
    dinhthuc = 0
    for sn in Sn:
       sigma= np.array ([1])
       sigma.resize ( [n])
       product = 1
       for i in range (1, n+1) :
           sigma[ sn.index (i)] = i
           product= product* A[i-1] [sn. index (i) ]
           dau = sgn_by_def (sigma)
           if (dau != 1):
              product = product*(-1)
           dinhthuc = dinhthuc + product
    return dinhthuc

import numpy as np
A = np.array([[4, -2],[3, -5]]) 
A1 = np.array([[10, -2],[11, -5]])
A2 = np.array([[4, 10],[3, 11]])
from scipy import linalg 
detA = linalg.det(A) 
detA1 = linalg.det(A1) 

detA2 = linalg.det(A2)
print (detA, detA1, detA2)
if (detA != 0):
 x1 = detA1 / detA
 x2 = detA2 / detA
print ("Hai nghiệm của phương trình là: ", x1, x2) 

import sympy as sp
TG = sp.Matrix([[1, 0, 1],[4, 3, 1], [2, 2, 1]])
print("Dien tich tam giac la:",1/2*TG.det())

from sympy import * # lúc này ta sử dụng trực tiếp thư viện
x, y, z = symbols('x y z')
MP = Matrix([[x, y, z, 1],[-1, 3, 2, 1],[0, 1, 0, 1],[-2, 0, 1, 1]])
print(MP.det())