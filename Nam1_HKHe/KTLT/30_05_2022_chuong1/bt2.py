from matplotlib.pyplot import flag


def check_prime_number(n):
    flag = 1
    if n < 2:
        flag = 0
        return flag
    for p in range(2, n):
        if n % p == 0:
            flag = 0
            break
    return flag

n = int(input("Nhập số tự nhiên: "))
check = check_prime_number(n)
if check == 1:
    print(n, "Là số nguyên tố")
else:
    print(n, "Không phải là số nguyên tố")