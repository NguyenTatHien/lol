n1 = input("Nhập vào tên tập tin nguồn: ")
n2 = input("Nhập vào tên tập tin đích: ")
o = open(n1, "r", encoding="utf-8")
o2 = open(n2, "w", encoding="utf-8")
dem = 1
for i in o.readlines():
    o2.write(str(dem) +".\t"+  i)
    dem+=1