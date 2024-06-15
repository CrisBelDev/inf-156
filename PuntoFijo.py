import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def f(x):
    return np.exp(-x)-x

def g(x):
    return np.exp(-x)

def PuntoFijo(xi, tol):
    res = pd.DataFrame(columns=['x' ,'f(x)', 'g(x)','error'])
    error = np.abs(g(xi)-xi)
    i = 0
    while (error > tol):
        res.loc[i] = [xi, f(xi), g(xi), abs(f(xi))]
        if  i > 0:
            error = np.abs(g(xi)-xi)
        xi = g(xi)
        i+=1
    print(res)
    print("El valor de x, tal que f(x) = 0 es: ", xi, "\nCon error: ", error)

    x = np.linspace(0, 1.5, 100)
    plt.title('Método del punto fijo')
    plt.plot(x, f(x), label='f(x)')
    plt.plot(x, g(x), label='g(x)')
    plt.plot(x,x,label = 'f(x) = x')
    plt.axvline(xi, label = f"f(x) = 0, x = {xi:.5f}", color = "black")
    plt.axhline(0, color = "black")
    plt.legend(loc = 'upper right')
    plt.grid()
    plt.show()

PuntoFijo(0,0.0005)
