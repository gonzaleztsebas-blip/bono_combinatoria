from math1 import *


# ==================================================
# MENU PRINCIPAL
# ==================================================

while True:

    print("\n====================================")
    print(" CALCULADORA DE COMBINATORIA")
    print("====================================")
    print("1. Permutaciones P(n,r)")
    print("2. Coeficientes multinomiales")
    print("3. Salir")

    opcion_principal = input("\nOpcion: ")

    # --------------------------------------------------
    # PROBLEMA 1: Permutaciones P(n,r)
    # --------------------------------------------------
    if opcion_principal == "1":

        while True:

            print("\n====================================")
            print(" PERMUTACIONES P(n,r)")
            print("====================================")
            print("1. Calcular P(n,r)")
            print("2. Ver casos de ejemplo")
            print("3. Volver al menu principal")

            opcion = input("\nOpcion: ")

            # CALCULAR P(n,r)
            if opcion == "1":

                while True:
                    try:
                        n = int(input("Ingrese n: "))
                        r = int(input("Ingrese r: "))

                        if n < 0 or r < 0:
                            print("Error: n y r deben ser no negativos")
                        elif r > n:
                            print("Error: debe cumplirse r <= n")
                        else:
                            break
                    except ValueError:
                        print("Error: ingrese un numero entero")

                print("\n----- RESULTADOS -----")

                # Factoriales
                print(f"{n}! (iterativo) =", factorial_iterativo(n))
                print(f"{n}! (recursivo) =", factorial_recursivo(n))

                # Comparacion factoriales
                comparacion = comparar_factoriales(n)

                print("\nComparacion de implementaciones:")
                print("Iterativo :", comparacion["iterativo"])
                print("Recursivo :", comparacion["recursivo"])
                print("Coinciden :", comparacion["son_iguales"])

                # Permutacion
                perm = calcular_permutacion(n, r)

                print("\nPermutacion:")
                print(f"P({n},{r}) =", perm)

            # CASOS DE EJEMPLO
            elif opcion == "2":

                print("\n----- CASOS DE EJEMPLO -----")
                for n_ej, r_ej, resultado in casos_de_ejemplo_1():
                    print(f"P({n_ej},{r_ej}) = {resultado}")

            # VOLVER AL MENU PRINCIPAL
            elif opcion == "3":
                break

            else:
                print("\nOpcion invalida.")

    # --------------------------------------------------
    # PROBLEMA 9: Coeficientes multinomiales
    # --------------------------------------------------
    elif opcion_principal == "2":

        while True:

            print("\n==========================================")
            print(" PERMUTACIONES CON REPETICION")
            print(" COEFICIENTES MULTINOMIALES")
            print("==========================================")
            print("\nSeleccione una opcion:")
            print("1. Ingresar una palabra/cadena")
            print("2. Ingresar lista de cantidades")
            print("3. Mostrar ejemplos")
            print("4. Generar permutaciones manuales")
            print("5. Volver al menu principal")

            opcion = input("\nOpcion: ")

            # CASO 1: PALABRA
            if opcion == "1":

                palabra = input("Ingrese la palabra: ")

                if not palabra:
                    print("Error: la palabra no puede estar vacia")
                    continue

                conteo = calcular_repeticiones_en_cadena(palabra)
                resultado = calcular_permutacion_con_repeticion_str(conteo)

                print("\nFrecuencias encontradas:")
                print(conteo)

                print("\nTotal de arreglos distintos:")
                print(resultado)

            # CASO 2: LISTA DE CANTIDADES
            elif opcion == "2":

                lista = input(
                    "Ingrese cantidades separadas por comas (ej: 4,3,2): "
                )

                cantidades = calcular_repeticiones_en_lista(lista)

                if cantidades:
                    resultado = calcular_permutacion_con_repeticion_list(
                        cantidades
                    )

                    print("\nCantidades ingresadas:")
                    print(cantidades)

                    print("\nTotal de arreglos distintos:")
                    print(resultado)

            # CASOS DE EJEMPLO
            elif opcion == "3":

                print("\nBANANA:")
                conteo = calcular_repeticiones_en_cadena("BANANA")
                print(calcular_permutacion_con_repeticion_str(conteo))

                print("\n[4,3,2]:")
                print(calcular_permutacion_con_repeticion_list([4, 3, 2]))

            # GENERAR PERMUTACIONES MANUALMENTE
            elif opcion == "4":

                palabra = input(
                    "Ingrese palabra (recomendado <=8 letras): "
                )

                if not palabra:
                    print("Error: la palabra no puede estar vacia")
                    continue

                if len(palabra) > 12:
                    print("Error: palabra demasiado larga (max 12 letras)")
                    continue

                resultado = sorted(list(permutaciones_manuales(palabra)))

                print("\nCantidad generada:")
                print(len(resultado))

                print("\nPermutaciones:")
                for p in resultado:
                    print(p)

            # VOLVER AL MENU PRINCIPAL
            elif opcion == "5":
                break

            else:
                print("\nOpcion invalida.")

    # --------------------------------------------------
    # SALIR
    # --------------------------------------------------
    elif opcion_principal == "3":

        print("\nPrograma finalizado.")
        break

    else:
        print("\nOpcion invalida.")