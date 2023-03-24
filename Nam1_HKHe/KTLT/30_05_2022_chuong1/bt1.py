#Chuong 1/Bai 1: ktra số nguyên âm hay dương
def ktra_amduong(number):
    if number < 0:
        return False
    else:
        return True

a = int(input("Nhập vào số nguyên a: "))
kq = ktra_amduong(a)
if kq == True:
    print("Đây là số dương")
else:
    print("Đây là số âm")