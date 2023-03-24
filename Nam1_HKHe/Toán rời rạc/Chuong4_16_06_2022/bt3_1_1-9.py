import random
print(random.choice(['Táo', 'Lê', 'Ổi', 'Chuối']))
print(random.random())
print(random. uniform(4.9, 10.0))
print(random.randrange(6))
print(random.randrange(50, 500))
print(random.randrange(20, 100, 2))
print(random.sample(range(100), 10))
print(random.sample(range(10, 100), 15))
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
rand5_char = random.sample(chars, 5)
print(rand5_char)