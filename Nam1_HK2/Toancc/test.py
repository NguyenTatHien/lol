from numpy import append


list_ = ["2174802010458","2174802010499", "2174802010468"]
khoa_ = ["k27", "k26", "k25"]
ten_ = ["nguyen tat hien", "tran thi ai", "nguyen tat vinh"]
sit = ['1A','2A','3A','4A','5A','1B','2B','3B','4B','5B','1C','2C','3C','4C','5C']
dachon = []
while True:
    mssv = input("Nhập vào MSSV: ")
    khoa = input("Nhập vào khóa học: ")
    ten = input("Họ và tên: ")
    if mssv in list_ and khoa.lower() in khoa_ and ten.lower() in ten_:
        print("access")
        break
    else:
        them = input("Không có thông tin của bạn\nBạn có muốn thêm vào thông tin của bạn không?(Y/N): ")
        if them.upper() == "Y":
            themmssv = input("Nhập mssv cần thêm: ")
            list_.append(themmssv)
            themten = input("Nhập tên cần thêm: ")
            ten_.append(themten)
            print("Mời bạn nhập lại để kiểm tra")
            continue
        else:
            exit()
sach = {"1":"NGUỒN SỐNG", "2":"KHÁM PHÁ", "3":"LÀM VIỆC", "4":"THỬ THÁCH", "5":"THÁCH ĐẤU", "6":"VÕ SĨ ĐƯỜNG PHỐ"}
while True:
    print(sach)
    nhap = input("Nhập vào sách hoặc số kệ sách muốn đọc: ")
    if nhap.upper() in sach.values() or nhap in sach.keys():
        print(f"Đây là danh sách kệ mời bạn đến số kệ tương ứng với sách đã chọn\n========================\n\n{sach}\n\n========================\n")
        break
    else:
        print("Thư viện chưa có loại sách này mời bạn chọn sách khác")
        print("========================\n")
        continue
while True:
    ngoi = input("Mời bạn chọn chỗ ngồi: ")
    if ngoi.upper() in sit:
        print("chọn chỗ thành công")
        dachon.append(ngoi.upper())
        continue
    if ngoi.upper() not in sit:
        print("Chọn chỗ không thành công")
        print("Mời chọn lại")
        continue
while True:
    ngoi = input("Mời bạn chọn chỗ ngồi: ")
    if ngoi.upper() in dachon:
        print("Chỗ ngồi đã có người")
        print("Mời bạn chọn vị trí khác")
        continue
    elif ngoi.upper() not in sit:
        print("Chọn chỗ không thành công")
        continue
    else:
        print("Chọn chỗ thành công")
        dachon.append(ngoi.upper())
        continue