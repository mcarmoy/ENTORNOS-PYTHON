try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
except ValueError:
    print("Entrada inválida. Por favor, ingresa solo números.")
else:
    if num1 > num2:
        print(f"El número mayor es: {num1}")
    elif num2 > num1:
        print(f"El número mayor es: {num2}")
    else:
        print("Ambos números son iguales.")