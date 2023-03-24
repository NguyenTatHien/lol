class Person:
    name = ""
    def __init__(self, name):
        self.name = name
    
    def xinchao(self):
        print("Hello, tôi tên là: ",self.name)
    
nhap = Person(name = input("Nhập vào tên: "))
nhap.xinchao()