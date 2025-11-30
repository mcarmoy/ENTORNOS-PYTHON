try:
    dia_num = int(input("Ingresa un número del 1 al 7 para el día de la semana: "))
except ValueError:
    print("ERROR: Ingresa solo un número entero.")
else:
    if dia_num == 1:
        print("El día correspondiente es: Lunes")
    elif dia_num == 2:
        print("El día correspondiente es: Martes")
    elif dia_num == 3:
        print("El día correspondiente es: Miércoles")
    elif dia_num == 4:
        print("El día correspondiente es: Jueves")
    elif dia_num == 5:
        print("El día correspondiente es: Viernes")
    elif dia_num == 6:
        print("El día correspondiente es: Sábado")
    elif dia_num == 7:
        print("El día correspondiente es: Domingo")
    else:
        print("ERROR: Número incorrecto. Debe ser un número del 1 al 7.")