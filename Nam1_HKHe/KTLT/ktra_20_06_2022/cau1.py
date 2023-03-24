from datetime import date
today = date.today()
if today.weekday() == 0:
    print("Hôm nay là thứ hai trong tuần")
elif today.weekday() == 1:
    print("Hôm nay là thứ ba trong tuần")
elif today.weekday() == 2:
    print("Hôm nay là thứ tư trong tuần")
elif today.weekday() == 3:
    print("Hôm nay là ngày thứ năm trong tuần")
elif today.weekday() == 4:
    print("Hôm nay là ngày thứ sáu trong tuần")
elif today.weekday() == 5:
    print("Hôm nay là ngày thứ bảy trong tuần")
else:
    print("Hôm nay là ngày chủ nhật trong tuần")