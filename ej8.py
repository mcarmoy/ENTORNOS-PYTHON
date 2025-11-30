try:
    nota = float(input("Introduce la nota (0-10): "))
    edad = int(input("Introduce la edad: "))
    sexo = input("Introduce el sexo ('F' o 'M'): ").upper() # Convertimos a mayúsculas para simplificar la comprobación
except ValueError:
    print("Entrada inválida. Asegúrate de ingresar números para nota y edad.")
else:
    # 1. Comprobamos las condiciones comunes de Nota y Edad
    if nota >= 5 and edad >= 18:
        
        # 2. Si se cumplen, comprobamos el Sexo para determinar ACEPTADA o POSIBLE
        if sexo == 'F':
            print("ACEPTADA")
        elif sexo == 'M':
            print("POSIBLE")
        else:
            # Si nota y edad OK, pero el sexo no es 'F' ni 'M'
            print("NO ACEPTADA (Sexo inválido)") 
    
    # 3. Si no se cumplen las condiciones comunes (Nota < 5 o Edad < 18)
    else:
        print("NO ACEPTADA")