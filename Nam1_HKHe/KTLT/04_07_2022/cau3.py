def doc_tho(path):
    f = open(path, "r", encoding="utf-8")
    r = f.read()
    return print(r)

doc_tho(path = input("Mời nhập vào đường dẫn thơ cần đọc: "))