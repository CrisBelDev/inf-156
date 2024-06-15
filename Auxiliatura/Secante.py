import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

def f(x):
  return x**3 + 2*x**2 + 10*x - 20

def secante(x0, x, tol):
  res = pd.DataFrame(columns=['x', 'f(x)', 'error'])
  i=2
  res.loc[0]=[x0, f(x0), abs(f(x))]
  res.loc[1]=[x, f(x), abs(f(x))]
  while(abs(f(x))>=tol):
    x1=x
    x = x1 - ((f(x1))*(x0-x1)/(f(x0)-f(x1)))
    x0=x1
    res.loc[i]=[x, f(x), abs(f(x))]
    i+=1

  print(res)
  print("Solucion aproximada ", x, "con un error de ", abs(f(x)))

  xi = np.linspace(-20, 20, 20)
  yi = f(xi)

  plt.axhline(0)
  plt.axvline(0)
  plt.plot(xi, yi, color="blue")
  plt.plot(x, f(x), 'o', color="red")
  plt.show()

secante(0, 1, 0.0001)