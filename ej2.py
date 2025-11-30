# 2.Algoritmo que pida un número y diga si es positivo, negativo o 0.

valor = int(input("Indicame un número: "))

if valor > 0:
    print(f"El número {valor} es psitivo")
elif valor == 0:
    print(f"El número {valor} es 0")
else:
    print(f"El número {valor} es negativo")