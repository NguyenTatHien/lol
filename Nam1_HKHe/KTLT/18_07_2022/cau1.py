class Cat:
    giongloai = ""
    tuoitho = ""
    mausac = ""
    gioitinh = ""

    def __init__(self):
        self.giongloai = input("Nhập giống loài: ")
        self.tuoitho = input("Nhập tuổi thọ: ")
        self.mausac = input("Nhập màu sắc: ")
        self.gioitinh = input("Nhập giới tính: ")

    def show_info(self):
        print("Giống loài: ", self.giongloai)
        print("Tuổi thọ: ", self.tuoitho)
        print("Màu sắc: ", self.mausac)
        print("Giới tính: ", self.gioitinh)

nhap = Cat()
print("================")
nhap.show_info()