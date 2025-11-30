# 🐍 Ejercicios de la Lección 3: Estructuras Condicionales en Python

Este `README.md` documenta los ejercicios prácticos realizados durante la Lección 3, centrada en el uso de estructuras condicionales (`if`, `elif`, `else`) en Python para la toma de decisiones.

## Tabla de Contenidos

| Nº | Tema Principal | Enunciado Breve | Archivo |
| :---: | :--- | :--- | :---: |
| 1 | Comparación de Números | Indicar si el primer número es mayor que el segundo. | `ej1.py` |
| 2 | Signo de un Número | Determinar si un número es positivo, negativo o cero. | `ej2.py` |
| 3 | Par o Impar | Determinar si un número entero es par o impar. | `ej3.py` |
| 4 | División Segura | Realizar una división solo si el divisor no es cero. | `ej4.py` |
| 5 | Login Básico | Validar un nombre de usuario ("pepe") y una contraseña ("suegra"). | `ej5.py` |
| 6 | Mayúsculas | Comprobar si una cadena (letra) es mayúscula. | `ej6.py` |
| 7 | Cálculo de Potencia | Calcular la potencia manejando exponentes positivos, cero y negativos. | `ej7.py` |
| 8 | Triple Condicional | Clasificar una persona como 'ACEPTADA', 'POSIBLE' o 'NO ACEPTADA' por nota, edad y sexo. | `ej8.py` |
| 9 | Ordenar Tres Números | Pedir tres números y mostrarlos ordenados de mayor a menor. | `ej9.py` |
| 10 | Clasificación Geométrica | Clasificar dos circunferencias según su posición (exteriores, secantes, concéntricas, etc.). | `ej10.py` |
| 11 | Tipo de Triángulo | Determinar si un triángulo es Rectángulo, Equilátero, Isósceles o Escaleno. | `ej11.py` |
| 12 | Año Bisiesto | Indicar si un año es bisiesto. | `ej12.py` |
| 13 | Validación de Fecha | Pedir día, mes y año y determinar si la fecha es correcta. | `ej13.py` |
| 14 | Ganancia de Uva | Calcular el precio final del kilo de uva según su tipo (A/B) y tamaño (1/2). | `e14.py` |
| 15 | Costo Viaje Escolar | Calcular el costo individual y total de un viaje según el número de alumnos. | `ej15.py` |
| 16 | Cobro Telefónico | Calcular el costo de una llamada por duración y aplicar impuestos según día y turno. | `ej16.py` |
| 17 | Cara Opuesta del Dado | Mostrar la cara opuesta (en letras) del resultado de un dado (1-6). | `ej17.py` |
| 18 | Día de la Semana | Pedir un número (1-7) y mostrar el día de la semana correspondiente. | `ej18.py` |
| 19 | Días del Mes | Pedir un número de mes (1-12) e imprimir la cantidad de días. | `ej19.py` |
| 20 | Costo de Envío | Calcular el costo de transporte internacional según peso y zona. | `ej20.py` |

---

## 💻 Ejercicios Detallados y Código

### 1: Comparación de Números

**Descripción:** Pide dos números por teclado e indica si el primero es mayor que el segundo.

**Algoritmo:**
1. Solicitar el primer y el segundo número.
2. Usar un `if` para comprobar si el primero es mayor que el segundo.
3. Usar un `elif` para comprobar si el segundo es mayor que el primero.
4. Usar un `else` si ninguna de las condiciones anteriores se cumple (son iguales).

```python
try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
except ValueError:
    print("Error: Ingresa solo números válidos.")
else:
    if num1 > num2:
        print(f"El primer número ({num1}) es mayor que el segundo ({num2}).")
    elif num2 > num1:
        print(f"El segundo número ({num2}) es mayor que el primero ({num1}).")
    else:
        print("Ambos números son iguales.")
```
### 2: Número Positivo, Negativo o Cero

**Descripción:** Algoritmo que pida un número y diga si es positivo, negativo o 0.

**Algoritmo:**
1. Solicitar al usuario que introduzca un número `num`.
2. Comprobar si `num` es mayor que 0. Si lo es, es positivo.
3. Si no es mayor que 0, comprobar si `num` es menor que 0. Si lo es, es negativo.
4. Si no es ni mayor ni menor que 0, por descarte, debe ser 0.

```python
try:
    num = float(input("Ingresa un número: "))
except ValueError:
    print("Error: Ingresa un número válido.")
else:
    if num > 0:
        print("El número es positivo.")
    elif num < 0:
        print("El número es negativo.")
    else:
        print("El número es cero (0).")
```
### 3: Número Par o Impar

**Descripción:** Escribe un programa que lea un número e indique si es par o impar.

**Algoritmo:**
1. Solicitar al usuario un número entero `num`.
2. Utilizar el operador módulo `%` para obtener el resto de la división de num entre 2.
3. Si el resto es 0, el número es par.
4. Si el resto es diferente de 0 (es decir, 1), el número es impar.

```python
try:
    num = float(input("Ingresa un número: "))
except ValueError:
    print("Error: Ingresa un número válido.")
else:
    if num > 0:
        print("El número es positivo.")
    elif num < 0:
        print("El número es negativo.")
    else:
        print("El número es cero (0).")
```
### 4: División con Control de Cero

**Descripción:** Crea un programa que pida al usuario dos números y muestre su división, si el segundo no es cero, o un mensaje de aviso en caso contrario.

**Algoritmo:**
1. Solicitar el dividendo ``num1`` y el divisor ``num2``.
2. Comprobar si el divisor ``num2`` es diferente de cero.
3. Si es diferente de cero, realizar la división e imprimir el resultado.
4. Si es cero, imprimir un mensaje de aviso.

```python
try:
    num1 = float(input("Ingresa el dividendo: "))
    num2 = float(input("Ingresa el divisor: "))
except ValueError:
    print("Error: Ingresa solo números válidos.")
else:
    if num2 != 0:
        resultado = num1 / num2
        print(f"El resultado de la división es: {resultado}")
    else:
        print("Aviso: No se puede dividir por cero.")
```
### 5: Login Básico

**Descripción:** Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido "pepe" y "suegra" se indica "Has entrado al sistema", sino se da un error..

**Algoritmo:**
1. Definir las credenciales correctas: usuario_ok = "pepe" y contrasena_ok = "suegra".
2. Solicitar al usuario su nombre de usuario (usuario_input) y contraseña (contrasena_input).
3. Comprobar si usuario_input es igual a usuario_ok Y si contrasena_input es igual a contrasena_ok (usando el operador and).
4. Si ambas condiciones son verdaderas, imprimir "Has entrado al sistema".
5. En caso contrario, imprimir un mensaje de error.

```python
usuario = input("Introduce el nombre de usuario: ")
contrasena = input("Introduce la contraseña: ")

# Se comprueba que AMBAS condiciones sean verdaderas
if usuario == "pepe" and contrasena == "suegra":
    print("Has entrado al sistema. ¡Bienvenido, pepe!")
else:
    print("ERROR: Credenciales incorrectas. Acceso denegado.")
```
### 6: Comprobar Letra Mayúscula

**Descripción:** Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.

**Algoritmo:**
1. Solicitar al usuario la cadena de texto ``caracter``.
2. Comprobar dos condiciones: a. Que la cadena tenga exactamente un carácter (para asegurarnos de que solo estamos comprobando una "letra"). b. Usar el método ``.isupper()`` de Python para verificar si ese carácter es una letra mayúscula.
3. Si ambas son verdaderas, el carácter es una mayúscula.
4. En caso contrario, imprimir un mensaje indicando que no lo es.

```python
cadena = input("Ingresa una cadena (ej. una letra): ")

if cadena.isupper():
    print(f"La cadena '{cadena}' está compuesta enteramente por letras mayúsculas.")
else:
    print(f"La cadena '{cadena}' contiene minúsculas, números o no es solo mayúsculas.")
```
### 7: Cálculo de Potencia con Exponente Condicional

**Descripción:** Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir tres cosas:

- El exponente sea positivo, sólo tienes que imprimir la potencia.

- El exponente sea 0, el resultado es 1.

- El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

**Algoritmo:**
1. Solicitar la base ``base`` y el exponente ``exponente``.

2. Si el exponente es 0, el resultado es 1.

3. Si el exponente es mayor que 0 ``positivo``, usar el operador ** para calcular la potencia directamente.

4. Si el exponente es menor que 0 ``negativo``, calcular la potencia de la base con el exponente positivo ``-exponente``, y luego dividir 1 por ese resultado.

```python
try:
    base = float(input("Ingresa la base (número a elevar): "))
    exponente = int(input("Ingresa el exponente (número entero): "))
except ValueError:
    print("Entrada inválida. Por favor, asegúrate de ingresar números.")
else:
    # Caso 1: Exponente positivo
    if exponente > 0:
        resultado = base ** exponente
        print(f"La potencia de {base} elevado a {exponente} es: {resultado}")

    # Caso 2: Exponente cero
    elif exponente == 0:
        # Cualquier número elevado a 0 es 1 (excepto 0^0, que es indefinido, pero aquí asumimos 1)
        resultado = 1
        print(f"La potencia de {base} elevado a {exponente} es: {resultado}")

    # Caso 3: Exponente negativo
    else: 
        # Si el exponente es negativo (ej. -2), calculamos 1 / (base ** exponente_positivo)
        # exponente_positivo se obtiene multiplicando por -1
        exponente_positivo = -exponente
        
        # Calculamos 1 / (base ^ |exponente|)
        resultado = 1 / (base ** exponente_positivo)
        print(f"La potencia de {base} elevado a {exponente} es 1 / ({base}^{exponente_positivo}), que es: {resultado}")
```
### 8: Criterio de Admisión

**Descripción:** Algoritmo que pida dos números 'nota' y 'edad' y un carácter 'sexo' y muestre el mensaje 'ACEPTADA' si la nota es mayor o igual a cinco, la edad es mayor o igual a dieciocho y el sexo es 'F'. En caso de que se cumpla lo mismo, pero el sexo sea 'M', debe imprimir 'POSIBLE'. Si no se cumplen dichas condiciones se debe mostrar 'NO ACEPTADA'.Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir tres cosas:

**Algoritmo:**
1. Solicitar la nota ``nota``, la edad ``edad`` y el sexo ``sexo``.

2. Definir las condiciones base: ``nota >= 5`` Y ``edad >= 18``.

3. Si las condiciones base son verdaderas: a. Comprobar si ``sexo`` es 'F'. Si lo es, imprimir 'ACEPTADA'. b. Si ``sexo`` es 'M', imprimir 'POSIBLE'. c. Si no es 'F' ni 'M', se puede considerar 'NO ACEPTADA' (o manejar como error).

4. Si las condiciones base son falsas, imprimir 'NO ACEPTADA'.

```python
try:
    nota = float(input("Introduce la nota (0-10): "))
    edad = int(input("Introduce la edad: "))
    sexo = input("Introduce el sexo ('F' o 'M'): ").upper() # Convertimos a mayúsculas para simplificar la comprobación
except ValueError:
    print("Entrada inválida. Asegúrate de ingresar números para nota y edad.")
else:
    # 1. Comprobamos las condiciones comunes de Nota y Edad
    if nota >= 5 and edad >= 18:
        
        # 2. Si se cumplen, comprobamos el Sexo para determinar ACEPTADA o POSIBLE
        if sexo == 'F':
            print("ACEPTADA")
        elif sexo == 'M':
            print("POSIBLE")
        else:
            # Si nota y edad OK, pero el sexo no es 'F' ni 'M'
            print("NO ACEPTADA (Sexo inválido)") 
    
    # 3. Si no se cumplen las condiciones comunes (Nota < 5 o Edad < 18)
    else:
        print("NO ACEPTADA")
```
### 9: Ordenar Tres Números

**Descripción:** Algoritmo que pida tres números y los muestre ordenados (de mayor a menor).

**Algoritmo:**
1. Solicitar los tres números (``a``, ``b``, ``c``).

2. Utilizar condicionales anidadas o múltiples ``elif`` para cubrir todas las 6 posibles combinaciones de orden.

3. Por ejemplo, si ``a`` es el mayor, luego comparamos ``b`` y ``c`` para el orden de los dos restantes.

```python
try:
    a = float(input("Ingresa el primer número (A): "))
    b = float(input("Ingresa el segundo número (B): "))
    c = float(input("Ingresa el tercer número (C): "))
except ValueError:
    print("Entrada inválida. Asegúrate de ingresar solo números.")
else:
    # Mostramos los números ordenados de Mayor a Menor

    # Caso 1: A es el mayor de todos
    if a >= b and a >= c:
        if b >= c:
            print(f"Orden: {a}, {b}, {c}")
        else: # c > b
            print(f"Orden: {a}, {c}, {b}")

    # Caso 2: B es el mayor de todos
    elif b >= a and b >= c:
        if a >= c:
            print(f"Orden: {b}, {a}, {c}")
        else: # c > a
            print(f"Orden: {b}, {c}, {a}")

    # Caso 3: C es el mayor de todos (o si son todos iguales, se resuelve en los casos anteriores pero esta es la alternativa)
    else: 
        if a >= b:
            print(f"Orden: {c}, {a}, {b}")
        else: # b > a
            print(f"Orden: {c}, {b}, {a}")
```
### 10: Clasificación de Circunferencias

**Descripción:** Algoritmo que pida los puntos centrales x1 ,y1 ,x2 ,y2 y los radios r1 ,r2 de dos circunferencias y las clasifique en uno de estos estados:

- exteriores

- tangentes exteriores

- secantes

- tangentes interiores

- interiores

- concéntricas

**Algoritmo:**
1. CÁLCULO:

- D: Distancia entre los dos centros.

- Suma de Radios (R_suma): La suma del Radio 1 más el Radio 2.

- Diferencia de Radios (R_diferencia): La diferencia entre el Radio mayor y el Radio menor.

2. COMPARACIÓN (Relación de D):

- Si D es mayor que R_suma: Las circunferencias son Exteriores.

- Si D es igual a R_suma: Las circunferencias son Tangentes Exteriores.

- Si D es menor que R_suma y D es mayor que R_diferencia: Las circunferencias son Secantes (se cruzan).

- Si D es igual a R_diferencia (y D no es cero): Las circunferencias son Tangentes Interiores.

- Si D es menor que R_diferencia: Las circunferencias son Interiores.

- Si D es igual a cero:

- Si los Radios son iguales: Coincidentes.

- Si los Radios son diferentes: Concéntricas.

```python
import math

try:
    # Solicitar coordenadas y radios
    x1 = float(input("Centro Circunferencia 1 - Coordenada x1: "))
    y1 = float(input("Centro Circunferencia 1 - Coordenada y1: "))
    r1 = float(input("Radio Circunferencia 1 (r1): "))
    
    x2 = float(input("Centro Circunferencia 2 - Coordenada x2: "))
    y2 = float(input("Centro Circunferencia 2 - Coordenada y2: "))
    r2 = float(input("Radio Circunferencia 2 (r2): "))
    
except ValueError:
    print("Error: Ingresa valores numéricos válidos.")
else:
    # Aseguramos que los radios sean positivos
    if r1 <= 0 or r2 <= 0:
        print("Error: Los radios deben ser mayores que cero.")
    else:
        # Calcular la distancia entre los centros (d)
        d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        
        # Calcular la suma de radios (suma_r) y la diferencia de radios (resta_r)
        suma_r = r1 + r2
        resta_r = abs(r1 - r2)
        
        # Clasificar la posición de las circunferencias
        # Se añaden comentarios breves solo para claridad de la clasificación geométrica
        
        # Caso 1: Concéntricas (Centros iguales)
        if d == 0:
            # Si los radios son iguales y los centros son iguales, son la misma circunferencia (implícitamente concéntricas)
            if r1 == r2:
                print("CONCÉNTRICAS (Iguales)")
            else:
                print("CONCÉNTRICAS (Diferentes radios)")
        
        # Caso 2: Exteriores (d > r1 + r2)
        elif d > suma_r:
            print("EXTERIORES")

        # Caso 3: Tangentes Exteriores (d = r1 + r2)
        elif d == suma_r:
            print("TANGENTES EXTERIORES")

        # Caso 4: Secantes (resta_r < d < suma_r)
        elif d > resta_r and d < suma_r:
            print("SECANTES")

        # Caso 5: Tangentes Interiores (d = |r1 - r2|)
        elif d == resta_r:
            print("TANGENTES INTERIORES")

        # Caso 6: Interiores (d < |r1 - r2|)
        elif d < resta_r:
            print("INTERIORES")

        else:
            print("Clasificación no cubierta (error lógico o radios superpuestos).")
```
