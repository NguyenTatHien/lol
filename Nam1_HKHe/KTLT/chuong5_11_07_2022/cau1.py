class SoHoc:
    number1 = ""
    number2 = ""
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def printInfo(self):
        print("Number1: ", self.number1)
        print("Number2: ", self.number2)

    def addition(self):
        print("Phép cộng của 2 số trên là: ",float(self.number1) + float(self.number2))

    def subtract(self):
        print("Phép trừ của 2 số trên là: ",float(self.number1) - float(self.number2))

    def multi(self):
        print("Phép nhân của 2 số trên là: ",float(self.number1) * float(self.number2))

    def division(self):
        print("Phép chia của 2 số trên là: ",float(self.number1) / float(self.number2))

nhap = SoHoc(number1=input("Nhập vào number1: "), number2 = input("Nhập vào number2: "))

while True: 
    xuat = input("Bạn muốn sao(in, cộng, trừ, nhân, chia): ")
    if xuat.lower() == "in":
        nhap.printInfo()
    elif xuat.lower() == "cộng":
        nhap.addition()
    elif xuat.lower() == "trừ":    
        nhap.subtract()
    elif xuat.lower() == "nhân":
        nhap.multi()
    elif xuat.lower() == "chia":
        nhap.division()
    else:
        print("Không có phép tính!!Shutdown!!")
        break