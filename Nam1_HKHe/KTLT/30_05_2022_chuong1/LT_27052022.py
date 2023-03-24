# def print_name(full_name):
#     print("Xin chao", full_name)

# print_name("Nguyen Tat Hien")
# dict_ = {"555":"nguyen tat hien", "123":"nguyen sksk li", "565":"lj ki lo"}
# def in_thong_tin(mssv, ho_ten):
#     print("Mssv: ", mssv)
#     print("Ho va ten: ", ho_ten)

# a = int(input("Moi nhap mssv: "))
# b = input("Moi nhap ten: ")

# if a not in dict_.keys() and b.lower() not in dict_.values():
#     print("Unavailable")
# else:
#     print("Available")
#     in_thong_tin(a, b)

# def thong_tin_cuoc_goi(*call_info):
#     print("from: ", call_info[0])
#     print("To: ", call_info[1])
#     print("Time: ", call_info[2])

# thong_tin_cuoc_goi(56546546,787987,150)



def add_number(n1, n2, n3):
    t = n1 + n2 + n3
    v = n1 * n2 + n3
    c = n3 - n1 + n2
    return (t, v, c)

total = add_number(13, 25, 40)
print(total)