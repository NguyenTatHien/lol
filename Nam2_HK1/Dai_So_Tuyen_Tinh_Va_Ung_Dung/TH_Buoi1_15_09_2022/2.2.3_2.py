from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
bieuthuc = x*x - x*y + y*y
print(bieuthuc)

bieuthuc_moi = bieuthuc.subs({x:1-y})
print(bieuthuc_moi)

from sympy import simplify
dongian = simplify(bieuthuc_moi)
print(dongian)