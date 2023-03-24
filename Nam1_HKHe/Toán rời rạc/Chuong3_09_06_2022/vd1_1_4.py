N = 4
for i1 in range(0, N): 
    for i2 in range(i1, N): 
        for i3 in range(i2, N): 
            print (i1, i2, i3) 

N = 3 
ketqua = [] 
for i1 in range(0, N):
    for i2 in range(i1, N): 
        for i3 in range(i2, N):
            ketqua = ketqua + [(i1, i2, i3)]

print(ketqua)
print(ketqua[3])