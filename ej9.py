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