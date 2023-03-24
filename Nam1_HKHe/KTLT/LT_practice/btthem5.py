def poem(path):
    f = open(path, "w", encoding="utf-8")
    x = "done"
    while True:
        nd = input("Mời nhập nội dung bài thơ: ") 
        f.write(nd+"\n")
        if nd.lower() == x:
            break
        else:
            continue

poem(path = input("Mời nhập đường dẫn cần lưu bài thơ: "))