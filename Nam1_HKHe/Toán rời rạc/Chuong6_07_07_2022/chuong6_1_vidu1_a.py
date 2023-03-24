def bool_xy(x, y):
    kq = 0
    if x == 1 and y == 1:
        kq = 0
    if x == 1 and y == 0: 
        kq = 1 
    if x == 0 and y == 1: 
        kq = 0 
    if x == 0 and y == 0: 
        kq = 0 
    return kq

for x in [1,0]: 
    for y in [1,0]: 
        print (bool_xy(x,y)) 