'''''''''''
Safe Float Comparison
Implement def almost_equal(a, b, rel_tol=1e-9, 
abs_tol=0.0) reproducing math.isclose without using the module.


'''''''''

from math import isclose

a = 56.7
b = 56.6

res = isclose(a, b)
print(res)

#https://docs.python.org/3/library/math.html#math.isclose

#control - you can control how strict or loose the comparison is.
print(isclose(1000, 1001, rel_tol=0.01))
print(isclose(0, 0.0000001, abs_tol=1e-6))



