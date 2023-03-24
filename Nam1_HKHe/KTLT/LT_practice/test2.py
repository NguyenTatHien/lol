class Employee:
    """Đây là chương trình hiển thị thông tin sinh viên"""
    ID = 2174802010458
    Name = "Nguyen Tat Hien"
    DeptName = "CNTT"
    def show_info(self):
        print("ID: ", self.ID)
        print("Name: ", self.Name)
        print("DeptName: ", self.DeptName)

print(Employee.__doc__)
print(Employee.show_info)