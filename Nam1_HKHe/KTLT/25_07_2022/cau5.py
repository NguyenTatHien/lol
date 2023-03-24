def viet(a, path):
    f=open(path, "a", encoding="utf-8")
    f.write(a)

viet(a = input("Nhập vào nội dung bất kỳ: "), path = input("Nhập vào đường dẫn file cần lưu: "))