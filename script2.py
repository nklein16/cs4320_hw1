__author__ = 'Nathaniel Klein - Coded on my MBPro - 06/04/15'

from polynomial import bisection
from polynomial import eval

a = 1
b = 7
poly = [-119, 3, -4, 0, 7]
tolerance = 1e-12

# Prints the value of the root
print(bisection(a, b, poly, tolerance))

# Stores the returned value of the root in rootval
rootval = (bisection(a, b, poly, tolerance))

# Evaluates the polynomial at the value of the root
print(eval(rootval,poly))