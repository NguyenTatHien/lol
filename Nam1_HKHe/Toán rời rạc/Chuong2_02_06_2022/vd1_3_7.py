imatrix = lambda n: [[1 if j==i else 0 for j in range(n)] for i in range(n)] 
print(imatrix(3))
import numpy
list_eye = lambda n: numpy.eye(n).tolist()
print(list_eye(4))