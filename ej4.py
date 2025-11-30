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