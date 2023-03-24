def kiemtra_nuocsoi(nhiet_do):
    if nhiet_do < 100:
        return "Nuoc chua soi!"
    else:
        return "Nuoc da soi!"

print(kiemtra_nuocsoi(100))
print(kiemtra_nuocsoi(99))

def kiemtra_nuocsoi1(nhiet_do):
    return 'Nuoc ' + ('da soi!' if nhiet_do == 100 else 'chua soi.')

print(kiemtra_nuocsoi1(100))
print(kiemtra_nuocsoi1(99))

ds_dau = []
for diem_so in range(10):
    if diem_so > 5:
        ds_dau.append(str(diem_so))
print(ds_dau)

ds_dau = [str(diem_so) for diem_so in range(10) if diem_so > 5]
print(ds_dau)