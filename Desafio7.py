import math
import sympy as sp
def Taylor(x0, x1, f0):
    Er = 0
    h = x1 - x0
    x = sp.Symbol('x')
    fx = sp.ln(x)
    for k in range(0,5):
        fx = fx.diff(x)
        f0 = f0 + Er
        Er = fx.subs(x, 1)*h**(k+1)/math.factorial(k+1)
        print(k, f0, Er)

print("#        |       fx      |       Er")
Taylor(1, 1.2, 0)