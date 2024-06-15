import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def f(x):
  return (9.42667*x)*((20*x)/(2*x+20))**(2/3) - 5
def biseccion(a, b, tol):
  res = pd.DataFrame(columns=['a', 'b', 'm', 'f(a)', 'f(b)', 'f(m)', 'error'])
  i=0
  while(True):
    m = (a+b)/2
    res.loc[i] = [a, b, m, f(a), f(b), f(m), abs(f(m))]
    i+=1
    if(f(a)*f(m)<0):
      b=m
    elif(f(b)*f(m)<0):
      a=m
    else:
      print("Solucion encontrada: ", m)
      break
    if(abs(f(m))<=tol):
      break
  print(res)
  print("Solucion aproximada ", m, "con error ", abs(f(m)))

  x = np.linspace(-20, 20, 100)
  y = f(x)

  plt.axhline(0)
  plt.axvline(0)
  plt.plot(x, y, color="blue")
  plt.plot(m, f(m), 'o', color="red")
  plt.xlim(-10, 20)
  plt.ylim(-10, 20)
  plt.show()

biseccion(0, 1, 0.0005)