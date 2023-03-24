class Nut:
    def __init__(self, khoa = None) -> None:
        self.khoa = khoa
        self.trai = None
        self.phai = None
    def chen(self, khoa):
        if self is None:
            nut = Nut(khoa)
            self = nut 
            return
        if khoa < self.khoa:
            if self.trai == None:
                self.trai = Nut(khoa)
            else:
                self.trai.chen(khoa)
        elif khoa > self.khoa:
            if self.phai == None:
                self.phai = Nut(khoa)
            else:
                self.phai.chen(khoa)
        else:
            print("da co gia tri")
    
    def duyenLNR(self, goc = 0):
        nut_ht = goc
        if goc == 0:
            nut_ht = self.goc
        if nut_ht == None:
            return []
        else:
            kq = []
            kq_trai = self.duyenLNR(nut_ht.trai)
            for x in kq_trai:
                kq.append(x)
            kq.append(nut_ht.khoa)
            kq_phai = self.duyenLNR(nut_ht.phai)
            for x in kq_phai:
                kq.append(x)
            return kq