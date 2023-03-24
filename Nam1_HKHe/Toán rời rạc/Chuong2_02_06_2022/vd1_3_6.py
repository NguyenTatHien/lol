from functools import reduce


ds = [20, 25, 50, 103, 13, 19]
f = lambda a,b: a if a>b else b
print(reduce(f,ds))