from sympy import Symbol
x = Symbol('x')
f = x + x + x + 2
print(f)

a = Symbol('Noi')
b = Symbol('Chim')
print(3*b + 7*a)

print(a.name)
print(b.name)