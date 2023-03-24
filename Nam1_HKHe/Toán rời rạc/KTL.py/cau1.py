from functools import reduce

ds = [5,3,9,12,15,4,20,6] 
f = lambda a,b: a if (a>b) else b 
print (reduce(f, ds))