try:
    base = float(input("Ingresa la base (número a elevar): "))
    exponente = int(input("Ingresa el exponente (número entero): "))
except ValueError:
    print("Entrada inválida. Por favor, asegúrate de ingresar números.")
else:
    # Caso 1: Exponente positivo
    if exponente > 0:
        resultado = base ** exponente
        print(f"La potencia de {base} elevado a {exponente} es: {resultado}")

    # Caso 2: Exponente cero
    elif exponente == 0:
        # Cualquier número elevado a 0 es 1 (excepto 0^0, que es indefinido, pero aquí asumimos 1)
        resultado = 1
        print(f"La potencia de {base} elevado a {exponente} es: {resultado}")

    # Caso 3: Exponente negativo
    else: 
        # Si el exponente es negativo (ej. -2), calculamos 1 / (base ** exponente_positivo)
        # exponente_positivo se obtiene multiplicando por -1
        exponente_positivo = -exponente
        
        # Calculamos 1 / (base ^ |exponente|)
        resultado = 1 / (base ** exponente_positivo)
        print(f"La potencia de {base} elevado a {exponente} es 1 / ({base}^{exponente_positivo}), que es: {resultado}")