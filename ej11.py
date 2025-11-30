try:
    A = float(input("Ingresa la longitud del lado A: "))
    B = float(input("Ingresa la longitud del lado B: "))
    C = float(input("Ingresa la longitud del lado C: "))
except ValueError:
    print("Error: Ingresa solo valores numéricos positivos para los lados.")
else:
    # 1. Validación básica de triángulo (suma de dos lados > tercero)
    if A + B <= C or A + C <= B or B + C <= A:
        print("Los lados no forman un triángulo válido.")
        
    else:
        # Para Pitágoras, identificamos el lado más largo (hipotenusa)
        lados = sorted([A, B, C])
        a_sq = lados[0] ** 2  # Lado 1 al cuadrado
        b_sq = lados[1] ** 2  # Lado 2 al cuadrado
        c_sq = lados[2] ** 2  # Hipotenusa al cuadrado
        
        # Usamos una pequeña tolerancia (0.0001) para comparar floats
        
        # Comprobación 1: Rectángulo (A^2 + B^2 = C^2)
        if abs(a_sq + b_sq - c_sq) < 0.0001:
            print("El triángulo es RECTÁNGULO.")
        
        # Comprobación 2: Equilátero (3 lados iguales)
        elif A == B and B == C:
            print("El triángulo es EQUILÁTERO.")
        
        # Comprobación 3: Isósceles (Solo 2 lados iguales)
        elif A == B or A == C or B == C:
            print("El triángulo es ISÓSCELES.")
            
        # Comprobación 4: Escaleno (Ninguna de las anteriores)
        else:
            print("El triángulo es ESCALENO.")