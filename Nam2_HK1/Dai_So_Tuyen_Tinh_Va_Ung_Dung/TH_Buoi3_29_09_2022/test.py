from scipy import linalg #
import numpy as np
a= np.array([1,2,3])
print(a)
b = np.array([(1+9j, 2j, 3j), (4j, 5j, 6j)]) # số phức
print(b)
c = np.array([[ (0.5, 1.5, 10), (3,2,1) ] , [(6,5,4), (7,8,9)]]) # ma trận số thực
print(c)
A = np.matrix(np.random.random( (2,2) ) )
print(A)

B = np.asmatrix(b) # Chuyển b thành dạng ma trận
print(B)
C = np.mat(np.random.random( (10,5) ) )
print(C)

D = np.mat([ [4, 3], [2, 6] ])
print(D)
F = np.eye(3, k=1) # tạo ma trận đường chéo. 3 là ma trận 3x3, k=1 là đường
#chéo nằm phía trên đường chéo chính (k = 0).
print(F)
F= np.eye(3,k=0)
print(F)
F=np.eye(3,k= -1)
print(F)
F = np.eye(3, k=0)
print(F)
F = np.eye(3, k=-1)
print(F)
f= np.linalg.matrix_rank(C)
print(f)
e= A.I
print(e)
g= linalg.inv(A)
print(g)
h= linalg.det(A)
print(h)
#Chuyen doi ma tran
l= A.T
print(l)
q=A.H
print(q)
#Giai cac loai phuong trinh tuyen tinh
n= linalg.solve(A,b)
print(n)
E= np.mat(a).T
print(E)
r= linalg.lstsq(F,E)
print(r)
#Cac ham tren ma tran
#cong hai ma tran
p= np.add(A,D)
print(p)
#tru hai ma tran
y=np.subtract(A,D)
print(y)

k= A.H
print(k)
#Giai cac loai phuong trinh tuyen tinh
o= linalg.solve(A,b)
print(o)
E= np.mat(a).T
print(E)
T= linalg.lstsq(F,E)
print(T)
#cac han na trab
e= np.add(A,D)
print(e)
#tru hai ma tran
i= np.subtract(A,D)
print(i)
#chia ma tran
y= np.divide(A,D)
print(y)
#Nhan ma tran
r= A@D
print(r)
k= np.multiply(D,A)
print(k)
l= np.dot(A,D)
print(l)
j= np.vdot(A,D)
print(j)
k=linalg.expm(A)
print(k)
g= linalg.logm(A)
print(g)
#Ma tran hoi tu
import numpy as np
A = np.array([ [0,1], [1,0]])
print(A)
temp = A.dot(A) # tính toan lần thứ 1
print(temp)
k= 6
for i in range(k-1):
    temp = temp.dot(A)
    print (temp)
    print('---')

#tinh ma tran B
B = np.array([ [0,-1], [-1,0]])
print(B)
temp = B.dot(B) #tinh toan lan 1
print(temp)
k= 5
for i in range(k-1):
    temp = temp.dot(B)
    print (temp)
    print('---')
#ma tran hoi tu
C = np.array([ [1, 0, 0], [0, 0.5, 1], [0, 0, 0.5] ])
print(C)
temp = C.dot(C) # tính toan lần thứ 1
print(temp)
k= 1000
for i in range(k-1):
    temp = temp.dot(C)
print(temp)
#ma tran Markov
M = np.array([ [0.8, 0.3], [0.2, 0.7]])
MM = M.dot(M) # tính M2, nghĩa là M2
print (MM)

MM = M.dot(M) # tính M3
print (MM)
for i in range(100): # tính các M^ khác.
    MM = MM.dot(M)
print (MM) # kết luận xu hướng của jb
#phan ra ma tran LU
M = np.array([ [0.8, 0.3], [0.2, 0.7]])
P, L, U = linalg.lu(M) # lệnh lina.lu sẽ tách ma trận M thành 3 ma trận P, L và U
print (P)
print(L)
print(U)
E= L.dot(U)
print(E)
#Bai toan loan tin
A = np.array([ [0,1,0,1],[0,0,1,0],[1,0,0,1],[1,1,0,0]])
temp = A.dot(A)# lúc này temp = A^2

print(temp)
temp = temp.dot(A) # lúc này temp = A^2

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