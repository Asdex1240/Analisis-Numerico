def gauss_seidel(A, b, tol=1e-10, max_iter=1000):
    """
    Resuelve el sistema de ecuaciones Ax = b utilizando el método de Gauss-Seidel.
    
    :param A: Matriz de coeficientes.
    :param b: Vector constante.
    :param tol: Tolerancia para el criterio de parada.
    :param max_iter: Número máximo de iteraciones.
    :return: Vector de soluciones x.
    """
    
    n = len(b)
    x = [0.0 for i in range(n)]  # Asume la solución inicial como [0, 0, ... , 0]
    for it in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]
        
        # Criterio de parada basado en la diferencia relativa
        if all(abs(x_new[i] - x[i]) < tol for i in range(n)):
            return x_new
        x = x_new
    
    print("El método no convergió después de", max_iter, "iteraciones.")
    return x

# Ejemplo de uso:
A = [
    [2, -1, 1],
    [-1, 2, -1],
    [-1, 2, -1],
    [1,-1, 2]
]

b = [1, 2, 3]

x = gauss_seidel(A, b)
print(x)
