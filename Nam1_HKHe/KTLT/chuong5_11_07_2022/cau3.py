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

    def showInfo(self):
        print("Mã sinh viên: ",self.mssv)
        print("Điểm trung bình: ",self.dtb)
        print("Tuổi: ",self.tuoi)
        print("Lớp: ",self.lop)


while True:
    mssv = input("Nhập mã sinh viên: ")
    if len(mssv) == 8:
        break
    else:
        print("Mã sinh viên phải có đúng 8 ký tự")
        continue

while True:
    dtb = input("Nhập điểm trung bình: ")
    if 0.0 <= float(dtb) <= 10.0:
        break
    else:
        print("Điểm phải từ 0.0 - 10.0")
        continue

while True:
    tuoi = input("Nhập vào tuổi: ")
    if int(tuoi) >= 18:
        break
    else:
        print("Tuổi phải lớn hơn hoặc bằng 18")
        continue

while True:
    lop = input("Nhập vào lớp: ")
    if lop[0] == "A" or lop[0] == "C":
        break
    else:
        print("Lớp phải bắt đầu bằng kí tự A hoặc C (phải ghi hoa)")
        continue

nhap = Student(mssv, dtb, tuoi, lop)
check = input("Bạn có muốn hiển thị thông tin vừa nhập không?(Y/N): ")
if check.upper() == "Y":
    print("================")
    nhap.showInfo()
    print("================")
else:
    print("================")

if float(dtb) >= 8:
    print("Bạn được xét học bổng")
else:
    print("Bạn không được xét học bổng do điểm trung bình < 8")