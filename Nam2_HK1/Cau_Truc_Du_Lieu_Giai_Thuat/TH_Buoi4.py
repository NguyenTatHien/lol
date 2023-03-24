from winreg import DeleteValue
class QLSinhvien:
    Diemtb = 0
    list_ = {}
    def __init__(self, MSSV, Hoten, Diemtb):
        self.MSSV = MSSV
        self.Hoten = Hoten
        self.Diemtb = Diemtb
    def ThemSinhvien(self):
        self.MSSV = input("Nhập vào MSSV: ")
        self.list_.keys.append(self.MSSV)
        self.Hoten = input("Nhập Họ và tên: ")
        self.list_.values.append(self.Hoten)
        try:
            self.Diemtb = input("Nhập vào điểm trung bình: ")
            self.list_.values.append(self.Diemtb)
        except:
            return self.Diemtb
    def XoaSinhvien(self):
        xoa = input("Nhập vào mã sinh viên cần xóa: ")
        if xoa in self.list_.keys:
            self.list_.keys.DeleteValue(xoa)
        else:
            print("MSSV không tồn tại!")
    def InDSSV(self):
        for i in self.list_:
            print(i)

QL = QLSinhvien("2174802010458", "Nguyen Tat Hien", "0")
print(QL.InDSSV())