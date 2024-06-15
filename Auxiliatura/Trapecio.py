import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (2.7182**x)/x


def trapecio(a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    suma = 0

    for i in range(1, n):
        suma += y[i]

    I = (h / 2) * (y[0] + 2 * suma + y[n])

    xi = np.linspace(a, b, 60)
    yi = f(xi)

    plt.plot(x, y, label='Trapecio', color='blue')
    plt.plot(x, y, 'o', label='Trapecio', color='red')

    plt.plot(xi, yi, label='Integral', color='green')
    plt.legend()
    plt.show()

    print("El area aproximada de la integral es: ", I)

trapecio(1, 2, 8)