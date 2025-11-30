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