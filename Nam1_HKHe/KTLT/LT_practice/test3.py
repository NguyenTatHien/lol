class Employee:
    """Đây là chương trình hiển thị thông tin sinh viên"""
    ID = int
    Name = ""
    DeptName = ""
    def __init__(self, ID, Name, DeptName):
        self.ID = ID
        self.Name = Name
        self.DeptName = DeptName

    def show_info(self):
        print("ID: ", self.ID)
        print("Name: ", self.Name)
        print("DeptName: ", self.DeptName)

while True:
    try:
        sv = Employee(int(input("Nhap vao mssv: ")), input("Name: "), input("Phong ban: "))
        check = input("Bạn muốn tiếp tục không(Y/N): ")
        if check == "N":
            sv.show_info()
            break
        else:
            continue
    except ValueError:
        print("Vui long nhap so nguyen")
        continue