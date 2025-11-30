try:
    num = int(input("Ingresa un número entero: "))
except ValueError:
    print("Error: Ingresa un número entero.")
else:
    if num % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")