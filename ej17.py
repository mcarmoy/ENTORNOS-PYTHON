try:
    dado = int(input("Ingresa el resultado del dado (1 a 6): "))
except ValueError:
    print("ERROR: La entrada debe ser un número entero.")
else:
    cara_opuesta = 0
    nombre_opuesto = ""
    
    # Comprobación principal y asignación de la cara opuesta
    if dado == 1:
        cara_opuesta = 6
    elif dado == 2:
        cara_opuesta = 5
    elif dado == 3:
        cara_opuesta = 4
    elif dado == 4:
        cara_opuesta = 3
    elif dado == 5:
        cara_opuesta = 2
    elif dado == 6:
        cara_opuesta = 1
    else:
        print("ERROR: número incorrecto.")
        # Salimos del programa si hay error para evitar el siguiente bloque
        exit()

    # Mapeo de la cara opuesta a su nombre en letras
    if cara_opuesta == 1:
        nombre_opuesto = "Uno"
    elif cara_opuesta == 2:
        nombre_opuesto = "Dos"
    elif cara_opuesta == 3:
        nombre_opuesto = "Tres"
    elif cara_opuesta == 4:
        nombre_opuesto = "Cuatro"
    elif cara_opuesta == 5:
        nombre_opuesto = "Cinco"
    elif cara_opuesta == 6:
        nombre_opuesto = "Seis"
        
    print(f"La cara opuesta al {dado} es el {cara_opuesta} ({nombre_opuesto}).")