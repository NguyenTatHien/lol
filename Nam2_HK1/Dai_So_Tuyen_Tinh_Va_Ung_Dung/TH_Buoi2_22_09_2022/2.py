import numpy as np 
scores = np.array([-1, 1, 2, -3, 5, -4])
print(scores)

print(scores >= 0)

print(scores < 0)

print(np.select([scores >=0, scores < 0],['so duong', 'so am']))

scores = np.array([-1, 1, 2, 0, -3, 5, 0, -4])
print(np.select([scores >0, scores ==0, scores < 0],['so duong', 'so 0', 'so am']))

