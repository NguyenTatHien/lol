trang_thai = "s0"
trangthai_ke = {
    's0': ['s0', 's1'], 
    's1': ['s1', 's2'], 
    's2': ['s2', 's0']
                }
ket_qua = { 
    's0': [ 0, 1], 
    's1': [ 0, 1], 
    's2': [ 0, 1]
            }

def chuyen_trangthai(tin_hieu):
    global trang_thai
    chuoi_in = str(ket_qua[trang_thai][tin_hieu])
    chuoi_in = chuoi_in + " - " + trangthai_ke[trang_thai][tin_hieu]
    print(chuoi_in)
    trang_thai = trangthai_ke[trang_thai][tin_hieu]

tap_tinhieu = [1, 0, 1, 0, 1, 1, 0 , 0, 1] 
for i in tap_tinhieu: 
    chuyen_trangthai(i) 