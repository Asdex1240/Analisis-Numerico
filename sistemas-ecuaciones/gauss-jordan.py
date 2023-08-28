
# ... [Las funciones se mantienen igual que antes]

def buscar_maximo_en_columna(matriz, columna, desde_fila):
    """Encuentra la fila con el valor máximo en una columna específica a partir de una fila dada.
    
    Args:
    - matriz (list): La matriz en la que buscar.
    - columna (int): La columna en la que buscar.
    - desde_fila (int): La fila a partir de la cual comenzar la búsqueda.
    
    Returns:
    - int: El índice de la fila con el valor máximo en la columna especificada.
    """
    max_val = abs(matriz[desde_fila][columna])
    max_fila = desde_fila
    for i in range(desde_fila + 1, len(matriz)):
        if abs(matriz[i][columna]) > max_val:
            max_val = abs(matriz[i][columna])
            max_fila = i
    return max_fila

def intercambiar_filas(matriz, fila1, fila2):
    """Intercambia dos filas en una matriz.
    
    Args:
    - matriz (list): La matriz en la que se intercambiarán las filas.
    - fila1, fila2 (int): Los índices de las filas a intercambiar.
    """
    matriz[fila1], matriz[fila2] = matriz[fila2], matriz[fila1]

def multiplicar_fila(matriz, fila, factor):
    """Multiplica una fila por un factor.
    
    Args:
    - matriz (list): La matriz que contiene la fila a multiplicar.
    - fila (int): El índice de la fila a multiplicar.
    - factor (float): El factor por el que se multiplicará la fila.
    """
    matriz[fila] = [elemento * factor for elemento in matriz[fila]]

def sumar_filas(matriz, fila_destino, fila_fuente, factor=1):
    """Suma una fila fuente multiplicada por un factor a una fila destino.
    
    Args:
    - matriz (list): La matriz que contiene las filas.
    - fila_destino (int): El índice de la fila a la que se sumará.
    - fila_fuente (int): El índice de la fila que se sumará.
    - factor (float): El factor por el que se multiplicará la fila fuente.
    """
    matriz[fila_destino] = [dest + factor * src for dest, src in zip(matriz[fila_destino], matriz[fila_fuente])]

# ... [Resto del código se mantiene igual]


def gauss_jordan(matriz, b):
    """Aplica el método Gauss-Jordan a una matriz y su vector de términos independientes.
    
    Args:
    - matriz (list): Lista de listas que representa la matriz.
    - b (list): Vector de términos independientes.
    
    Returns:
    - list: Matriz en su forma reducida de fila escalonada.
    - list: Vector de soluciones.
    """
    n = len(matriz)
    # Creamos la matriz aumentada uniendo matriz y b
    matriz_aumentada = [matriz[i] + [b[i]] for i in range(n)]
    
    for i in range(n):
        max_fila = buscar_maximo_en_columna(matriz_aumentada, i, i)
        intercambiar_filas(matriz_aumentada, i, max_fila)
        pivot = matriz_aumentada[i][i]
        if pivot == 0:
            print("El pivote es cero, lo que puede indicar que el sistema no tiene solución única.")
        multiplicar_fila(matriz_aumentada, i, 1/pivot)

        for j in range(n):
            if j != i:
                factor = -matriz_aumentada[j][i]
                sumar_filas(matriz_aumentada, j, i, factor)
    
    # Separamos la matriz y el vector solución
    matriz_reducida = [fila[:-1] for fila in matriz_aumentada]
    soluciones = [fila[-1] for fila in matriz_aumentada]
    return matriz_reducida, soluciones

if __name__ == "__main__":
    n = int(input("Introduce el tamaño de la matriz nxn (ingresa n): "))
    A = []
    b = []
    
    # Solicita los valores de la matriz y el vector b
    print("Introduce los valores de la matriz:")
    for i in range(n):
        fila = []
        for j in range(n):
            valor = float(input(f"Elemento A({i+1}, {j+1}): "))
            fila.append(valor)
        A.append(fila)
        
        valor_b = float(input(f"Valor b para la ecuación {i+1}: "))
        b.append(valor_b)
    
    matriz_reducida, soluciones = gauss_jordan(A, b)
    print("\nMatriz en su forma reducida de fila escalonada:")
    for fila in matriz_reducida:
        print(fila)
        
    print("\nSoluciones del sistema:")
    for i, sol in enumerate(soluciones):
        print(f"Variable {i+1} = {round(sol, 4)}")

