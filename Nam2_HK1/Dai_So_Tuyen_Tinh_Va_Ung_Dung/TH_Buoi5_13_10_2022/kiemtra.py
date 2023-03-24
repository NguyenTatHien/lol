#Câu 1
print("========Câu 1===========")
import numpy as np
nhucau=np.array([[6,5,3,1],[3,6,2,2],[4,4,3,1]])
giaca=np.array([[1.50,1.00],[2.00,2.50],[5.00,4.50],[16.00,17.00]])
kq=np.dot(nhucau,giaca)
print(kq)

#Câu 2
print("\n==========Câu 2==========")
print('bài 2')
x=int(input('Nhập giá trị x='))
A = np.array([[1,-2,2],[-1,1,3],[1,-1,x]])
temp = A.dot(A)
sumA=A
k = 3
sumA = sumA + temp
for i in range(1, k-1):
    temp = temp.dot(A)
    sumA = sumA + temp
print (temp)
print (sumA)

#Câu 3
print("\n=============Câu 3============\n")
import numpy as np 
A = np.array( [ [1,1], [1,0] ] ) 
b = np.array([1, 0]) 
n = 10 
for i in range(n): 
    b = A.dot(b) 
    print(b)

#Câu 4
print("\n=================Câu 4================\n")
from sympy import *
x, y, z = symbols('x y z')
MP = Matrix([[x, y, z, 1],[-1, 3, 2, 1],[0, 1, 0, 1],[-2, 0,
1, 1]])
print(MP.det())