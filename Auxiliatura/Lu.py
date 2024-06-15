import numpy as np

def matrizLu(a):
    m = []
    tam = len(a)
    L = np.zeros((tam, tam))
    for i in range(tam):
        L[i][i] = 1
    fil = 1
    aux = a.copy()
    col = 0
    while (fil < tam):
        cont = 1
        for i in range(fil, tam):
            div = float(aux[i][col]) / float(aux[i - cont][col])  # division
            L[i][col] = div

            for j in range(tam):
                aux[i][j] = (-div) * aux[i - cont][j] + aux[i][j]
            cont += 1
        col += 1
        fil += 1
    return np.array(aux), L


def LU(a, b):
    U, L = matrizLu(a)
    invl = np.linalg.inv(L)
    d = np.matmul(invl, b)
    invu = np.linalg.inv(U)
    x = np.matmul(invu, d)
    print(x)


a = [[10, 2, -1],
     [-3, -6, -2],
     [1, 2, 5]]

b = [27, -61.5, -21.5]
LU(a, b)