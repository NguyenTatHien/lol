import math
g = lambda n:[[1 if (j+1==i or j==i+1) else 0 if(i==n/2) else math.sqrt(2) for j in range(n)] for i in range(n)] 
print(g(3))