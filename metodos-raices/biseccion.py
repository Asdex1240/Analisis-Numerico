def crear_polinomio():
    max_exponente = int(input("Ingrese el máximo exponente: "))
    
    terminos = []

    for exponente in range(max_exponente, -1, -1):
        constante = float(input(f"Ingrese constante de x^{exponente}: "))
        if constante != 0:
            terminos.append((constante, exponente))

    if not terminos:
        return []

    polinomio_str = ' + '.join([f"{c}x^{e}" if e > 0 else str(c) for c, e in terminos])
    print(f"Polinomio resultante: {polinomio_str}")

    return terminos

def evaluar_polinomio(terminos, x_valor):
    resultado = sum(coef * (x_valor ** exp) for coef, exp in terminos)
    return resultado

def evaluar_raiz(terminos, xi, xu):
    #Primera iteracion para saber si existen raices en el intervalo
    resultado_xi = evaluar_polinomio(terminos, xi)
    resultado_xr = evaluar_polinomio(terminos, xu)
    return resultado_xi * resultado_xr < 0

def evaluar_raiz_con_promedio(terminos, xi, xu, error):
    error_relativo = 100  # Inicializar el error relativo
    iteracion = 1  # Contador de iteraciones
    
    while error_relativo > error:
        xr = (xi + xu) / 2  # Calcular la nueva aproximación de la raíz
        
        resultado_xi = evaluar_polinomio(terminos, xi)
        resultado_xr = evaluar_polinomio(terminos, xr)
        evaluacion = resultado_xi * resultado_xr
        
        if evaluacion < 0:
            xu = xr
        elif evaluacion > 0:
            xi = xr
        else:
            # La raíz es exacta, no es necesario continuar
            break
        
        error_relativo = abs((xr - xi) / xr) * 100  # Calcular el nuevo error relativo
        
        print(f"Iteración {iteracion}:")
        print(f"xr: {xr}")
        print(f"Evaluación: {evaluacion}")
        print(f"Error relativo: {error_relativo}\n")
        
        iteracion += 1
    
    print("Raiz encontrada")
    print(f"Una raiz es {xr}")



def main():
    terminos = crear_polinomio()

    if not terminos:
        return

    xi = float(input("Ingrese el primer numero del intervalo: "))
    xu = float(input("Ingrese el segundo numero del intervalo: "))
    error = float(input("Ingrese el error deseado: "))

    if evaluar_raiz(terminos, xi, xu):
        eror_relativo = 100
        print("Hay raices")
        evaluar_raiz_con_promedio(terminos, xi, xu, error)
    else:
        print("No hay raices")

if __name__ == "__main__":
    main()
