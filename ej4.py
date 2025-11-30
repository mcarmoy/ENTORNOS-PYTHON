try:
    num1 = float(input("Ingresa el dividendo (primer número): "))
    num2 = float(input("Ingresa el divisor (segundo número): "))
except ValueError:
    print("Entrada inválida. Por favor, ingresa solo números.")
else:
    # Condición para evitar la división por cero
    if num2 != 0:
        resultado = num1 / num2
        print(f"El resultado de la división es: {resultado}")
    else:
        print("¡ADVERTENCIA! No se puede dividir por cero. Por favor, ingresa un divisor diferente de cero.")