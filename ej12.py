try:
    anio = int(input("Ingresa un año: "))
except ValueError:
    print("Error: Ingresa un número entero para el año.")
else:
    # (Divisible por 4 Y no divisible por 100) O (Divisible por 400)
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        print(f"El año {anio} ES bisiesto.")
    else:
        print(f"El año {anio} NO es bisiesto.")