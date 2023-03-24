from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
bieuthuc = x*x - x*y + y*y
print(bieuthuc)

giatri = bieuthuc.subs({x:3, y:2})
print(giatri)
print(x)
print(y)

#Tình huống 1
giatri = bieuthuc.subs({x:3, y:x})
print(giatri)

#Tình huống 2
giatri = bieuthuc.subs({x:y, y:3})
print(giatri)

#Tình huống 3
giatri = bieuthuc.subs({y:x}).subs({x:3})
print(giatri)
