def montante(A, b):
    """
    Resuelve el sistema de ecuaciones Ax = b utilizando el método Montante.
    
    :param A: Matriz de coeficientes.
    :param b: Vector constante.
    :return: Vector de soluciones x.
    """

    n = len(b)
    M = [row + [val] for row, val in zip(A, b)]  # Matriz ampliada
    pivote_anterior = 1

    for k in range(n):
        pivote = M[k][k]
        for i in range(n):
            for j in range(n + 1):
                if i != k and j != k:
                    M[i][j] = (M[i][j] * pivote - M[k][j] * M[i][k]) / pivote_anterior
        for i in range(n):
            if i != k:
                M[i][k] = 0
        pivote_anterior = pivote

    sol = [row[-1] / row[i] for i, row in enumerate(M)]
    return sol

# Ejemplo de uso:
A = [
    [2, -1, 1],
    [-1, 2, -1],
    [1, -1, 2]
]

b = [1, 2, 3]

x = montante(A, b)
print(x)
