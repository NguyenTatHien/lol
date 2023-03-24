import numpy as np 
A = np.array( [ [1,1], [1,0] ] )
b = np.array([1, 0])
n = 10
for i in range(n): 
    b = A.dot(b) 
    print(b)