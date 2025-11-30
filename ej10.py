import math

try:
    # Solicitar coordenadas y radios
    x1 = float(input("Centro Circunferencia 1 - Coordenada x1: "))
    y1 = float(input("Centro Circunferencia 1 - Coordenada y1: "))
    r1 = float(input("Radio Circunferencia 1 (r1): "))
    
    x2 = float(input("Centro Circunferencia 2 - Coordenada x2: "))
    y2 = float(input("Centro Circunferencia 2 - Coordenada y2: "))
    r2 = float(input("Radio Circunferencia 2 (r2): "))
    
except ValueError:
    print("Error: Ingresa valores numéricos válidos.")
else:
    # Aseguramos que los radios sean positivos
    if r1 <= 0 or r2 <= 0:
        print("Error: Los radios deben ser mayores que cero.")
    else:
        # Calcular la distancia entre los centros (d)
        d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        
        # Calcular la suma de radios (suma_r) y la diferencia de radios (resta_r)
        suma_r = r1 + r2
        resta_r = abs(r1 - r2)
        
        # Clasificar la posición de las circunferencias
        # Se añaden comentarios breves solo para claridad de la clasificación geométrica
        
        # Caso 1: Concéntricas (Centros iguales)
        if d == 0:
            # Si los radios son iguales y los centros son iguales, son la misma circunferencia (implícitamente concéntricas)
            if r1 == r2:
                print("CONCÉNTRICAS (Iguales)")
            else:
                print("CONCÉNTRICAS (Diferentes radios)")
        
        # Caso 2: Exteriores (d > r1 + r2)
        elif d > suma_r:
            print("EXTERIORES")

        # Caso 3: Tangentes Exteriores (d = r1 + r2)
        elif d == suma_r:
            print("TANGENTES EXTERIORES")

        # Caso 4: Secantes (resta_r < d < suma_r)
        elif d > resta_r and d < suma_r:
            print("SECANTES")

        # Caso 5: Tangentes Interiores (d = |r1 - r2|)
        elif d == resta_r:
            print("TANGENTES INTERIORES")

        # Caso 6: Interiores (d < |r1 - r2|)
        elif d < resta_r:
            print("INTERIORES")

        else:
            print("Clasificación no cubierta (error lógico o radios superpuestos).")