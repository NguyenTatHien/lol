def scale(a, v): 
    return [a*vi for vi in v] 
v = [3,5,7] 
print(scale(10, v))

def sumvector(v, w): 
    return [vi+wi for (vi, wi) in zip(v, w)] 
v = [3,5,7] 
w = [2,4,6] 
print(sumvector(v, w))

def dotvector(v, w): 
    return sum([vi*wi for (vi, wi) in zip(v, w)]) 
print(dotvector(v, w))

def lenvector(v): 
    return dotvector(v,v) 
print(lenvector(w))

