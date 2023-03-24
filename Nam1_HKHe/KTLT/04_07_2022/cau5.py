def tong(chuoi):
    kq = 0
    a = chuoi.split()
    for i in a:
        try:
            kq += float(i)
        except:
            continue
    return kq

def file_sum():
    dulieu = open("tinhtong.txt", "r")
    kq = open("tinhtong1.txt", "w")
    dem = 1
    for i in dulieu:
        kq.write("chuoi" + str(dem) + ":" + str(tong(i)) + "\n")
        dem += 1

file_sum()