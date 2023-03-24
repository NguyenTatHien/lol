systlic = float(input("Mời nhập tâm thu: "))
diatolic = float(input("Mời nhập tâm trương: "))
if systlic < 90 and diatolic < 60 :
    print("Hypotension")
elif systlic < 120 and diatolic < 80:
    print("Optimal")
elif 120 < systlic < 129 and 80 < diatolic < 84:
    print("Normal")
elif 130 < systlic < 139 and 85 < diatolic < 89:
    print("High normal")
elif 140 < systlic < 159 and 90 < diatolic < 99:
    print("THA 1 (Nhe)") 
elif 160 < systlic < 179 and 100 < diatolic < 109:
    print("THA 2 (Trung binh)")
elif systlic >= 180 and diatolic >= 110:
    print("THA do 3 (Nang)")
elif systlic >= 140 and diatolic < 90:
    print("THA tam thu don doc")
else:
    print("Không có trong danh sách hiểu biết của chúng tôi")