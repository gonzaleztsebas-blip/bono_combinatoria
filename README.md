# Bono de Programación — Problemas Generales de Conteo
## Descripción

Solución a los problemas 1 y 9 del bono de programación del segundo corte. Cada problema está implementado como una herramienta general — no resuelve un único caso fijo sino que recibe parámetros del usuario y calcula para cualquier entrada válida.

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

## Uso de Inteligencia Artificial

Durante el desarrollo se utilizó Claude (Anthropic) como apoyo puntual.
El modelado matemático, la lógica de todas las funciones implementadas
y la estructura general del programa fueron desarrollados manualmente.

En cuanto a la interfaz, elementos como la estructura de los menús,
los mensajes al usuario y la navegación entre opciones fueron
realizados de forma manual.

Considero que el uso de estas herramientas fue complementario al
proceso de desarrollo, utilizándose como apoyo técnico y no como
sustituto del razonamiento o la implementación principal.

**Uso específico de IA:**
- Detección de bugs en la validación de entradas
- Reestructuración de los menús anidados
- Revisión y mejora de comentarios y documentación
- Apoyo en la redacción del README

---

## Validación de casos especiales

- Si n o r son negativos, el programa muestra un error y vuelve a pedir la entrada
- Si r > n, mismo comportamiento
- Si se ingresa texto en lugar de número, no explota — pide de nuevo
- P(n, 0) retorna 1 y P(n, n) retorna n!, ambos correctos
- Palabra vacía en el problema 9 muestra error
- Palabras de más de 12 letras en la generación manual están bloqueadas para evitar que el programa se cuelgue
- Lista con valores no numéricos en el problema 9 muestra error