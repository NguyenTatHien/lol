class QLSinhvien:
    def __init__(self, HoTen, MSSV, Diemtb, next=None):
        self.HoTen = HoTen
        self.MSSV = MSSV
        self.Diemtb = float(Diemtb)
        self.next = next
    def __str__(self):
        return "==================\n" + "MSSV: " + str(self.MSSV) + "\n" + "Họ và tên: " + str(self.HoTen) + "\n" + "Điểm tb: " + str(self.Diemtb)
    

def ThemSV():
    global node
    node = QLSinhvien("Nguyen Tat Hien", "23sedf", 9)
    node1 = QLSinhvien("Tuan", "545", 8)
    node2 = QLSinhvien("Lo", "222", 7)
    node3 = QLSinhvien(input("Nhập Họ và tên: "), input("Nhập mssv: "), float(input("Nhập vào điểm tb: ")))
    node.next = node1
    node1.next = node2
    node2.next = node3

# def XoaSV():


def InDSSV(node):
    while node:
        print(node)
        node = node.next
        list.append(node)
        # print

InDSSV(node)
