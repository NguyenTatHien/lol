def bool_xy1(x,y): 
    kq = 0 
    if (x == 1) and (y==0): 
        kq = 1 
    return kq

for x in [1,0]: 
    for y in [1,0]: 
        print (bool_xy1(x,y))