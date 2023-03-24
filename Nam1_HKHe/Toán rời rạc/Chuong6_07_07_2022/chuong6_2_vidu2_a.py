trang_thai = "s0"

def chuyen(tin_hieu):
    global trang_thai
    if trang_thai == "s0":
        if tin_hieu == 0:
            print("0 - s0")
            trang_thai = "s0"
        elif tin_hieu == 1:
            print("1 - s1")
            trang_thai = "s1"
    elif trang_thai == "s1":
        if tin_hieu == 0:
            print("0 - s1")
            trang_thai = "s1"
        elif tin_hieu == 1:
            print("1 - s2")
            trang_thai = "s2"
    elif trang_thai == "s2":
        if tin_hieu == 0:
            print("0 - s2")
            trang_thai = "s2"
        elif tin_hieu == 1:
            print("1 - s0")
            trang_thai = "s0"

tap_tinhieu = [1, 0, 1, 0, 1, 1, 0 , 0, 1] # thiết lập tập dữ liệu đầu vào 
for i in tap_tinhieu: 
    chuyen(i)