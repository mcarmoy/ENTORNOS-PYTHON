try:
    precio_inicial = float(input("Ingresa el precio inicial por kg de uva (€): "))
    tipo = input("Ingresa el tipo de uva (A o B): ").upper()
    tamano = int(input("Ingresa el tamaño de la uva (1 o 2): "))
except ValueError:
    print("Error: Asegúrate de ingresar números válidos para precio y tamaño.")
else:
    precio_final = precio_inicial
    
    # Comprobación principal por TIPO de uva
    if tipo == 'A':
        # Condicional anidado por TAMAÑO para TIPO A
        if tamano == 1:
            precio_final += 0.20 # Cargo de 20 céntimos
        elif tamano == 2:
            precio_final += 0.30 # Cargo de 30 céntimos
        else:
            print("Error: Tamaño no válido para Tipo A.")
    
    elif tipo == 'B':
        # Condicional anidado por TAMAÑO para TIPO B
        if tamano == 1:
            precio_final -= 0.30 # Rebaja de 30 céntimos
        elif tamano == 2:
            precio_final -= 0.50 # Rebaja de 50 céntimos
        else:
            print("Error: Tamaño no válido para Tipo B.")
            
    else:
        print("Error: Tipo de uva no válido. Debe ser 'A' o 'B'.")

    # Muestra el resultado solo si el tipo y tamaño eran válidos
    if tipo in ('A', 'B') and tamano in (1, 2):
        print(f"El precio final por kg de uva es: {precio_final:.2f} €")