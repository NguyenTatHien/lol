setA = {n for n in range(100) if n % 2 == 1}
setB = {n for n in range(100) if n % 2 == 1}
print(setA | setB)
print(setA & setB)
print(setA - setB)
print(setA < setB)
print(setA <= setB)
print(10 in setA)
print(setA.add(0))
print(setA > setB)