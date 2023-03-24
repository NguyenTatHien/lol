def poem_read(path):
    f = open(path, "r", encoding="utf-8")
    print(f.read())

poem_read(path = input("Mời nhập đường dẫn bài thơ cần đọc: "))