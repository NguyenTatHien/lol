def tongduong():
    _tong = 0
    _n = 0
    _n = int(input("Nhap vao so n: "))
    for _i in range(1,_n+1):
        _tong = _tong + (2*_i +1)
    print("Tong so la: ",_tong)

tongduong()