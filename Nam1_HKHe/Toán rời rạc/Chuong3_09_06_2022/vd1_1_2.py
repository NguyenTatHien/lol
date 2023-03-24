N = 4
for i1 in range(0, N):
    for i2 in range(0, N):
        for i3 in range(0, N):
            if i1 != i2 and i2 != i3 and i1 != i3:
                print (i1, i2, i3)