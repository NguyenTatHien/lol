class StateMachine: 
    def __init__(self): 
        self.tap_xuly = {} 
        self.trangthaiBatdau = None 
        self.trangthaiKetThuc = [] 
    def them_Trangthai(self, trangthai, xuly, trangthai_ketthuc = 0): 
        trangthai = trangthai.upper() 
        self.tap_xuly[trangthai] = xuly 
        if trangthai_ketthuc: 
            self.trangthaiKetThuc.append(trangthai)

def thietlap_TrangthaiBatdau(self, trangthai): 
    self.trangthaiBatdau = trangthai.upper() 
def thucthi(self, dauvao): 
    try: 
        xuly = self.tap_xuly[self.trangthaiBatdau] 
    except: 
        raise IndentationError("Phai gÍi .thietlap_TrangthaiBatdau() truoc khi goi .thucthi() ") 
    if not self.trangthaiKetThuc: 
        raise IndentationError("It nhat 1 trang thai phai la trang thai ket thuc") 
    while True: 
        (TrangThaiMoi, dauvao) = xuly(dauvao) 
        if TrangThaiMoi.upper() in self.trangthaiKetThuc: 
            print ("Den dich! ", TrangThaiMoi) 
            break 
        else: 
            xuly = self.tap_xuly[TrangThaiMoi.upper()]

from statemachine import StateMachine
