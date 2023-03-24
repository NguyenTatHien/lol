class Monhoc:
    mamonhoc = ""
    tenmonhoc = ""
    diemquatrinh = ""
    diemck = ""
    diemtong = ""
    def __init__(self):
        self.mamonhoc = input("Nhập mã môn học: ")
        self.tenmonhoc = input("Nhập tên môn học: ")
        self.diemquatrinh = float(input("Nhập điểm quá trình: "))
        self.diemck = float(input("Nhập điểm CK: "))
        self.diemtong = float(input("Nhập điểm tổng: "))
    def show_info(self):
        print("Mã môn học: ",self.mamonhoc)
        print("Tên môn học: ",self.tenmonhoc)
        print("Điểm quá trình: ",self.diemquatrinh)
        print("Điểm môn CK: ",self.diemck)
        print("Điểm tổng: ",self.diemtong)

sv = Monhoc()
sv.show_info()