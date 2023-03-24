from sympy import Symbol

x = Symbol('x')
y = Symbol('y')

from sympy import factor

bieuthuc = x**3 - y**3
print(factor(bieuthuc))

from sympy import expand

bieuthuc = (x - y)*(x**2 + x*y + y**2)
print(expand(bieuthuc))