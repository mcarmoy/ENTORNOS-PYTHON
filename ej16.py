try:
    duracion = int(input("Ingresa la duración de la llamada en minutos: "))
    dia = input("Ingresa el día de la semana (ej. Domingo, Lunes, etc.): ").lower()
    turno = input("Ingresa el turno (Mañana o Tarde): ").lower()
except ValueError:
    print("Error: La duración de la llamada debe ser un número entero.")
else:
    costo_base = 0.0
    
    # 1. Cálculo del COSTO BASE por duración
    
    # Primeros 5 minutos (Costo: 1.00 €)
    if duracion <= 5:
        costo_base = duracion * 0.20 # 1.00 / 5 = 0.20 por minuto
    
    # Minutos 6 a 8 (3 minutos siguientes) (Costo: 0.80 €)
    elif duracion <= 8:
        costo_base = 1.00  # Costo de los primeros 5 min
        minutos_extra = duracion - 5
        costo_base += minutos_extra * (0.80 / 3) # 0.80 € / 3 min
        
    # Minutos 9 y 10 (2 minutos siguientes) (Costo: 0.70 €)
    elif duracion <= 10:
        costo_base = 1.00 + 0.80 # Costo de los primeros 8 min
        minutos_extra = duracion - 8
        costo_base += minutos_extra * (0.70 / 2) # 0.70 € / 2 min
        
    # A partir del minuto 11 (Costo: 0.50 € por minuto)
    else: 
        costo_base = 1.00 + 0.80 + 0.70 # Costo de los primeros 10 min (2.50 €)
        minutos_extra = duracion - 10
        costo_base += minutos_extra * 0.50
        
    # 2. Cálculo del IMPUESTO
    
    impuesto = 0.0
    
    if dia == 'domingo':
        impuesto = 0.03 # 3%
    else:
        if turno == 'mañana':
            impuesto = 0.15 # 15%
        elif turno == 'tarde':
            impuesto = 0.10 # 10%
        else:
            print("Error: Turno no válido.")
    
    # 3. Cálculo del costo final
    
    monto_impuesto = costo_base * impuesto
    costo_final = costo_base + monto_impuesto
    
    if impuesto > 0.0:
        print("\n--- Desglose de Cobro ---")
        print(f"Costo Base por Duración: {costo_base:.2f} €")
        print(f"Impuesto ({impuesto * 100:.0f}%): {monto_impuesto:.2f} €")
        print(f"Total a Pagar: {costo_final:.2f} €")