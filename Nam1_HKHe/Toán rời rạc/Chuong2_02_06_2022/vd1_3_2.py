def thue(phan_tram):
    return lambda x: x*phan_tram
hcm = thue(0.012)
hn = thue(0.01)
print(hcm(1000000))