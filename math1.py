# ============================================================
# PROBLEMA 1: Calculadora general de permutaciones P(n, r)
# ============================================================
# Una permutacion P(n, r) cuenta el numero de formas de ordenar
# r objetos distintos tomados de un conjunto de n objetos distintos.
#
# En las permutaciones el orden SI importa:
# (A, B) y (B, A) representan arreglos diferentes.
#
# Formula:
#
#           P(n, r) = n! / (n-r)!
#
# Ejemplo:
#
# P(4, 2) = 4! / (4-2)!
#         = 24 / 2
#         = 12
#
# Es decir, existen 12 formas distintas de ordenar
# 2 objetos seleccionados de un conjunto de 4.
#
# El programa implementa herramientas relacionadas con
# el calculo de permutaciones:
#
# - Calculo iterativo del factorial
#
# - Calculo recursivo del factorial
#
# - Comparacion entre ambas implementaciones
#
# - Calculo general de P(n,r)
#
# - Casos de prueba predefinidos para validar resultados
#
# Observacion:
# Las permutaciones aparecen frecuentemente en problemas
# de ordenamientos, asignaciones, distribuciones y
# arreglos donde la posicion de los elementos afecta
# el resultado final.
# ============================================================


def factorial_iterativo(n):
    """
    Calcula n! de forma iterativa usando un ciclo for.
    Multiplica secuencialmente: 1 x 2 x 3 x ... x n

    Ventaja: eficiente en memoria, no apila llamadas.
    Complejidad: O(n) en tiempo, O(1) en espacio.

    Parametros:
        n (int): numero entero no negativo

    Retorna:
        int: el valor de n!
    """
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


def factorial_recursivo(n):
    """
    Calcula n! de forma recursiva: la funcion se llama a si misma
    reduciendo n en 1 cada vez hasta llegar al caso base.

    Definicion matematica:
        0! = 1            (caso base)
        n! = n x (n-1)!  (caso recursivo)

    Desventaja: para n muy grandes puede superar el limite de
    recursion de Python (por defecto ~1000 llamadas).
    Complejidad: O(n) en tiempo, O(n) en espacio (pila de llamadas).

    Parametros:
        n (int): numero entero no negativo

    Retorna:
        int: el valor de n!
    """
    if n == 0 or n == 1:   # Caso base: detiene la recursion
        return 1
    return n * factorial_recursivo(n - 1)  # Llamada recursiva


def calcular_permutacion(n, r):
    """
    Calcula P(n, r) = n! / (n - r)! usando factorial_iterativo.

    Parametros:
        n (int): total de objetos disponibles (n >= 0)
        r (int): objetos a ordenar (0 <= r <= n)

    Retorna:
        int: numero de permutaciones P(n, r)
    """
    return factorial_iterativo(n) // factorial_iterativo(n - r)


def comparar_factoriales(n):
    """
    Compara los resultados de ambas implementaciones del factorial
    para verificar que producen el mismo resultado.

    Parametros:
        n (int): numero a evaluar

    Retorna:
        dict con los resultados de ambas implementaciones y si coinciden
    """
    iter_result = factorial_iterativo(n)
    rec_result  = factorial_recursivo(n)
    return {
        "iterativo": iter_result,
        "recursivo": rec_result,
        "son_iguales": iter_result == rec_result
    }


def casos_de_ejemplo_1():
    """
    Retorna una lista de casos predefinidos para mostrar en la interfaz.
    Incluye los casos P(10,3) y P(20,5) solicitados por el enunciado,
    mas casos pequenos verificables manualmente.

    Retorna:
        lista de tuplas: [(n, r, P(n,r)), ...]
    """
    casos = [(4, 2), (5, 3), (6, 0), (10, 3), (20, 5)]
    return [(n, r, calcular_permutacion(n, r)) for n, r in casos]

# ============================================================
# PROBLEMA 9: Coeficientes multinomiales y palabras
# con letras repetidas
# ============================================================
# Este problema calcula cuantas palabras, cadenas o arreglos
# distintos pueden formarse cuando algunos elementos aparecen
# repetidos.
#
# Cuando existen repeticiones, NO todas las permutaciones son
# diferentes. Por ejemplo:
#
# BANANA
#
# contiene:
#
# 3 letras A
# 2 letras N
# 1 letra B
#
# Formula general:
#
#                 n!
# ------------------------------
# n1! * n2! * ... * nk!
#
# donde:
#
# n  = numero total de elementos
# n1, n2, ..., nk = cantidad de repeticiones
#
# Ejemplo:
#
# BANANA tiene 6 letras:
#
#         6!
# ---------------- = 60
# 3! * 2! * 1!
#
# Por tanto, existen 60 palabras distintas.
#
# El programa implementa:
#
# - Conteo de palabras con letras repetidas
#
# - Calculo general de coeficientes multinomiales
#
# - Entrada mediante palabras o cantidades
#
# - Casos de prueba predefinidos
#
# Observacion:
# Los coeficientes multinomiales aparecen frecuentemente
# en problemas de conteo, distribucion, arreglos con
# repeticiones y expansion multinomial.
# ============================================================

def calcular_repeticiones_en_cadena(palabra):
    palabra = palabra.lower()  # Convertir a minusculas para uniformidad
    lista_caracteres = list(palabra)
    conteo = {}
    
    for caracter in lista_caracteres:
        if caracter in conteo:
            conteo[caracter] += 1
        else:
            conteo[caracter] = 1
    return conteo

def calcular_permutacion_con_repeticion_str(conteo):
    total_caracteres = sum(conteo.values())
    total = factorial_iterativo(total_caracteres)
    
    for repeticiones in conteo.values():
        total = total // factorial_iterativo(repeticiones)
        
    return total

def calcular_repeticiones_en_lista(lista):
    try:
        lista_num_str = lista.split(",")
        lista_num_int = []
        
        for elemento in lista_num_str:
            lista_num_int.append(int(elemento))
            
        return lista_num_int
    except ValueError:
        print("inserte una lista de NUMEROS separados por comas ejm:(1,2,3..)")

def calcular_permutacion_con_repeticion_list(lista):
    total_suma_rep = sum(lista)
    total = factorial_iterativo(total_suma_rep)
    
    for repeticiones in lista:
        total = total // factorial_iterativo(repeticiones)
        
    return total

def permutaciones_manuales(palabra):
    if len(palabra) <= 1:
        return {palabra}
    
    resultado = set()
    
    for i in range(len(palabra)):
        letra_actual = palabra[i]
        # El resto de la palabra sin la letra actual
        resto_palabra = palabra[:i] + palabra[i+1:]
        
        # Llamada recursiva para mezclar el resto de las letras
        for p in permutaciones_manuales(resto_palabra):
            resultado.add(letra_actual + p)
            
    return resultado