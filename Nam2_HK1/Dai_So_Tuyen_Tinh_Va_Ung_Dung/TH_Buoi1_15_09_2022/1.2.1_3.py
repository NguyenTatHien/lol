import itertools
tap_sinh = list(itertools.chain(range(4), range(5, 10), range(15, 20) ))
print(tap_sinh)

print(list(zip(range(4), range(7, 12), reversed(range(11)))))