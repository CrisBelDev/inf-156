import math

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def f(x):
  return 5 - 20*(math.e**(-0.15*x)-math.e**(-0.5*x))

def df(x):
  return 3*math.e**(-0.15*x)-10*math.e**(-0.5*x)


def newton(x, tol):
  res = pd.DataFrame(columns=['x', 'f(x)', 'df(x)', 'error'])
  i=0
  while True:
    res.loc[i]=[x, f(x), df(x), abs(f(x))]
    i+=1
    x = x - (f(x)/df(x))
    if abs(f(x))<tol:
      break
  print(res)
  print("Solucion aproximada ", x," con error ", abs(f(x)))
  xi = np.linspace(-20, 20, 100)
  yi = f(xi)

  plt.axhline(0)
  plt.axvline(0)
  plt.plot(xi, yi, color="blue")
  plt.plot(x, f(x), 'o', color="red")
  plt.xlim(0, 5)
  plt.ylim(-3, 3)
  plt.show()

newton(0, 0.0005)