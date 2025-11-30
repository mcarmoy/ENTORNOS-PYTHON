import math

try:
    peso_gramos = float(input("Ingresa el peso del paquete en gramos: "))
    zona = int(input("Ingresa la zona de destino (1=Norteamérica, 2=Centroamérica, 3=Sudamérica, 4=Europa, 5=Asia): "))
except ValueError:
    print("ERROR: Ingresa valores numéricos válidos para peso y zona.")
else:
    costo_gramo = 0.0
    recargo_kilo = 0.0
    
    # 1. Validación de peso y zona
    if peso_gramos <= 0:
        print("ERROR: El peso debe ser positivo.")
    elif zona < 1 or zona > 5:
        print("ERROR: La zona de destino debe ser un número entre 1 y 5.")
        
    else:
        # 2. Asignación de tarifas según la ZONA
        if zona == 1:
            costo_gramo = 0.02
            recargo_kilo = 10.00
        elif zona == 2:
            costo_gramo = 0.05
            recargo_kilo = 15.00
        elif zona == 3:
            costo_gramo = 0.10
            recargo_kilo = 20.00
        elif zona == 4:
            costo_gramo = 0.15
            recargo_kilo = 25.00
        elif zona == 5:
            costo_gramo = 0.20
            recargo_kilo = 30.00

        # 3. Cálculo del costo base y recargo por kilo
        
        # El peso en kilos se usa para el recargo. math.ceil() asegura que fracciones de kilo cuenten como un kilo completo.
        peso_kilos_facturable = math.ceil(peso_gramos / 1000)
        
        costo_total = (costo_gramo * peso_gramos) + (recargo_kilo * peso_kilos_facturable)

        print("\n--- Resultado del Envío ---")
        print(f"Peso facturable (kilos): {peso_kilos_facturable}")
        print(f"Costo base ({costo_gramo:.2f} €/g): {costo_gramo * peso_gramos:.2f} €")
        print(f"Recargo por kilo: {recargo_kilo * peso_kilos_facturable:.2f} €")
        print(f"Costo Total del Servicio: {costo_total:.2f} €")