# Bono de Programación — Problemas Generales de Conteo
**Matemáticas Discretas I — Universidad Nacional de Colombia**  
Docente: Jhoan Sebastian Tenjo García

---

## Descripción

Este repositorio contiene la solución a dos problemas de combinatoria del bono de programación del segundo corte. El objetivo es construir herramientas generales que calculen correctamente para distintos valores de entrada, no solo un caso fijo.

---

## Problemas resueltos

### Problema 1 — Calculadora general de permutaciones P(n, r)

Una permutación P(n, r) cuenta el número de formas de ordenar r objetos distintos tomados de un conjunto de n objetos distintos. En las permutaciones **el orden sí importa**.

**Fórmula:**

```
P(n, r) = n! / (n - r)!
```

**El programa permite:**
- Calcular n! de forma iterativa y recursiva
- Comparar ambas implementaciones del factorial
- Calcular P(n, r) para cualquier entrada válida
- Ver casos de ejemplo predefinidos: P(4,2), P(5,3), P(6,0), P(10,3), P(20,5)

**Eficiencia:**  
El factorial iterativo es O(n) en tiempo y O(1) en espacio. El recursivo es O(n) en tiempo y O(n) en espacio por la pila de llamadas. Para n muy grande, el recursivo puede superar el límite de recursión de Python (~1000 llamadas).

---

### Problema 9 — Coeficientes multinomiales y palabras con letras repetidas

Cuando se tienen elementos repetidos, no todas las permutaciones son distintas. Este problema calcula cuántas palabras o arreglos diferentes pueden formarse.

**Fórmula:**

```
n! / (n1! * n2! * ... * nk!)

donde n = n1 + n2 + ... + nk
```

**Ejemplo:** BANANA tiene 6 letras (A×3, N×2, B×1):
```
6! / (3! * 2! * 1!) = 720 / 12 = 60 palabras distintas
```

**El programa permite:**
- Ingresar una palabra y calcular sus arreglos distintos
- Ingresar una lista de cantidades directamente
- Ver ejemplos predefinidos (BANANA y [4,3,2])
- Generar y listar todas las permutaciones distintas para palabras pequeñas

**Eficiencia:**  
El cálculo del coeficiente multinomial es O(n) donde n es el total de caracteres. La generación manual de permutaciones es O(n!) en tiempo y espacio, por lo que se limita a palabras de máximo 12 letras.

---

## Requisitos

- Python 3.x
- No requiere librerías externas

---

## Instalación y ejecución

```bash
# Clonar el repositorio
git clone https://github.com/gonzaleztsebas-blip/bono_combinatoria.git
cd bono_combinatoria

# Ejecutar
python main.py
```

---

## Estructura del proyecto

```
bono_combinatoria/
├── main.py     # Interfaz de usuario y menús
├── math1.py    # Funciones matemáticas de ambos problemas
└── README.md
```

---

## Ejemplos de entrada y salida

### Problema 1 — Calcular P(10, 3)

```
Ingrese n: 10
Ingrese r: 3

----- RESULTADOS -----
10! (iterativo) = 3628800
10! (recursivo) = 3628800

Comparacion de implementaciones:
Iterativo : 3628800
Recursivo : 3628800
Coinciden : True

Permutacion:
P(10,3) = 720
```

### Problema 1 — Casos de ejemplo

```
----- CASOS DE EJEMPLO -----
P(4,2) = 12
P(5,3) = 60
P(6,0) = 1
P(10,3) = 720
P(20,5) = 1860480
```

### Problema 9 — Palabra BANANA

```
Opcion: 1
Ingrese la palabra: BANANA

Frecuencias encontradas:
{'b': 1, 'a': 3, 'n': 2}

Total de arreglos distintos:
60
```

### Problema 9 — Lista de cantidades [4, 3, 2]

```
Opcion: 2
Ingrese cantidades separadas por comas (ej: 4,3,2): 4,3,2

Cantidades ingresadas:
[4, 3, 2]

Total de arreglos distintos:
1260
```

---

## Validación de casos especiales

| Entrada | Comportamiento |
|---|---|
| n o r negativos | Mensaje de error, vuelve a pedir |
| r > n | Mensaje de error, vuelve a pedir |
| Texto en lugar de número | Mensaje de error, vuelve a pedir |
| P(n, 0) | Retorna 1 correctamente |
| P(n, n) | Retorna n! correctamente |
| Palabra vacía | Mensaje de error |
| Palabra > 12 letras (opción manual) | Mensaje de error |
| Lista con valores no numéricos | Mensaje de error |
