import Sohoc
x = float(input("Nhập vào x: "))
y = float(input("Nhập vào y: "))
while True:
    n = input("Bạn muốn phép gì(cong, mu, bac3): ")
    if n.lower() == "done":
        break
    elif n == "cong":
        print("x cộng y = ",Sohoc.cong(x,y))
    elif n == "mu":
        print("x mũ y = ",Sohoc.mu(x,y))
    elif n == "bac3":
        bac3 = float(input("Nhập vào số cần căn bậc 3: "))
        print(f"Căn bậc 3 của {bac3} là {Sohoc.bac3(bac3)}")
    else:
        print("Không có trong danh sách")
        continue