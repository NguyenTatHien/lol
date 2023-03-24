from functools import reduce


day_so = range(1, 11)
print(reduce(lambda x, y: x + y, day_so))