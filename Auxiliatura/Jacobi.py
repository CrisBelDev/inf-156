import numpy as np

def jacobi(a, b, tol):
    tam = len(a)
    m = np.zeros((tam, tam))
    c = []
    for i in range(tam):
        for j in range(tam):
            if i != j:
                m[i][j] = -a[i][j] / a[i][i]
        c.append(b[i] / a[i][i])
    x = [0] * tam
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
            suma = 0
            error[i] = abs(x1[i] - x[i])

        max_error = 0
        for i in error:
            if i > max_error:
                max_error = i

        if max_error < tol:
            break
        print("iteracion ", nro_ite, )
        print(x)
        x = x1.copy()
        nro_ite += 1
    return x, nro_ite

a = [[-8, 1, -2],
     [2, -6, -1],
     [-3, -1, 7]]

b = [-20, -38, -34]
tol = 0.00001
x, nro_ite = jacobi(a, b, tol)
print(nro_ite)
print(x)