class Student:
    mssv = ""
    dtb = ""
    tuoi = ""
    lop = ""

    def __init__(self, mssv, dtb, tuoi, lop):
        self.mssv = mssv
        self.dtb = dtb
        self.tuoi = tuoi
        self.lop = lop

    def show_info(self):
        print("Mã sinh viên: ", self.mssv)
        print("Điểm trung bình: ", self.dtb)
        print("Tuổi: ", self.tuoi)
        print("Lớp: ", self.lop)

while True:
    mssv = input("Nhập vào mã sinh viên: ")
    if len(mssv) == 8:
        break
    else:
        print("Nội dung phải có đúng 8 kí tự")
        continue
while True:
    dtb = input("Nhập vào điểm trung bình: ")
    if 0.0 <= float(dtb) <= 10.0:
        break
    else:
        print("Điểm phải từ 0.0 đến 10.0")
        continue
while True:
    tuoi = input("Nhập tuổi: ")
    if int(tuoi) >= 18:
        break
    else:
        print("Tuổi phải lớn hơn hoặc bằng 18")
while True:
    lop = input("Nhập vào lớp: ")
    if lop[0] == "A" or lop[0] == "C":
        break
    else:
        print("Phải bắt đầu bằng kí tự A hoặc C")
        continue

kq = Student(mssv, dtb, tuoi, lop)
print("=============")
kq.show_info()
print("=============")
if float(dtb) > 8:
    print("Bạn được học bổng")
else:
    print("Bạn không được học bổng")