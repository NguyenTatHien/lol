mon_hoc = ["ToanCC", "DSTT", "ToanRR", "LaptrinhCB"]
thu_tu = [2, 3, 4, 1]
diem_so = [10, 9, 8, 7]
anh_xa = zip(thu_tu, mon_hoc, diem_so)
print(anh_xa)

tap_hop = set(anh_xa)
print(tap_hop)

lay_TT, lay_monhoc , lay_diem = zip(*anh_xa)
print(lay_monhoc)