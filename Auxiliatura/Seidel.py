import numpy as np

def seidel(a, b, tol):
    tam = len(a)
    m = np.zeros((tam, tam))
    c = []
    for i in range(tam):
        for j in range(tam):
            if i != j:
                m[i][j] = -a[i][j] / a[i][i]
        c.append(b[i] / a[i][i])

    x = [0] * tam
    x0 = [0] * tam
    error = [0] * tam
    nro_ite = 0
    while True:
        x1 = []
        suma = 0
        for i in range(tam):
            for j in range(tam):
                suma += m[i][j] * x[j]
            suma += c[i]
            x1.append(suma)
            x[i] = suma
            suma = 0
            error[i] = abs(x1[i] - x0[i])

        max_error = 0
        for i in error:
            if i > max_error:
                max_error = i

        if max_error < tol:
            break
        print("iteracion ", nro_ite, )
        print(x)
        x0 = x1.copy()
        nro_ite += 1
    return x, nro_ite


a = [[10, 2, -1],
     [-3, -6, 2],
     [1, 1, 5]]

b = [27, -61.5, -21.5]
tol = 0.05
x, nro_ite = seidel(a, b, tol)
print("iteracion ", nro_ite)
print(x)