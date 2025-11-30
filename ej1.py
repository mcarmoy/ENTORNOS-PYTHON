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

