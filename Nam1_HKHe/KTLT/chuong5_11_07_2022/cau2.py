class NhanVien:
    ten = ""
    tuoi = ""
    diachi = ""
    tienluong = ""
    tongsogiolam = ""

    def __init__(self, ten, tuoi, diachi, tienluong, tongsogiolam):
        self.ten = ten
        self.tuoi = tuoi
        self.diachi = diachi
        self.tienluong = tienluong
        self.tongsogiolam = tongsogiolam

    def printInfo(self):
        print("Tên: ",self.ten)
        print("Tuổi: ",self.tuoi)
        print("Địa chỉ: ",self.diachi)
        print("Tiền lương: ",self.tienluong)
        print("Tổng số giờ làm: ",self.tongsogiolam)
    
    def tinhThuong(self):
        if float(self.tongsogiolam) >= 200:
            print("Tiền thưởng thêm vào lương là: ",float(self.tienluong) * 0.2)
        elif float(self.tienluong) < 200 and float(self.tienluong) >= 100:
            print("Tiền thưởng thêm vào lương là: ",float(self.tienluong) * 0.1)
        else:
            print("Tiền thưởng thêm vào lương là: ", float(self.tienluong))

nhap = NhanVien(ten = input("Nhập vào Tên: "), tuoi = input("Nhập vào tuổi: "), diachi = input("Nhập vào địa chỉ: "), tienluong = input("Nhập vào tiền lương: "), tongsogiolam = input("Nhập vào tổng số giờ làm: "))

while True:
    yeucau = input("bạn muốn object nào(in, tiền thưởng): ")
    if yeucau.lower() == "in":
        nhap.printInfo()
    elif yeucau.lower() == "tiền thưởng":
        nhap.tinhThuong()
    else:
        print("Không có trong object")
        break