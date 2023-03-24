import random, string
while True:
    print('#{:06x}'.format(random.randint(0, 0xFFFFFF)))
    a = random.choice(string.ascii_letters)
    b = random.randint(0, 10) * 7
    print(a)
    print(b)