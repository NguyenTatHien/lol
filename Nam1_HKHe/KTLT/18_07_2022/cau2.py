class HocVien:
    mssv = ""
    hoten = ""
    hocky = ""
    gioitinh = ""
    mon1 = ""
    mon2 = ""

    def __init__(self):
        self.mssv = input("Nhập mã sinh viên: ")
        self.hoten = input("Nhập họ và tên: ") 
        self.hocky = input("Nhập học kỳ: ")
        self.gioitinh = input("Nhập giới tính: ")
        self.mon1 = input("Nhập môn 1: ")
        self.mon2 = input("Nhập môn 2: ")

    def show_info(self):
        print("Mã sinh viên: ", self.mssv)
        print("Họ tên: ", self.hoten)
        print("Học kỳ: ", self.hocky)
        print("Giới tính: ", self.gioitinh)
        print("Môn 1: ", self.mon1)
        print("Môn 2: ", self.mon2)

nhap = HocVien()
print("==============")
nhap.show_info()