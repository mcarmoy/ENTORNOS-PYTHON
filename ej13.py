def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

try:
    dia = int(input("Ingresa el día: "))
    mes = int(input("Ingresa el mes: "))
    anio = int(input("Ingresa el año: "))
except ValueError:
    print("Error: Ingresa números enteros para día, mes y año.")
else:
    fecha_correcta = False
    
    # 1. Validación de rangos básicos y positivos
    if anio >= 1 and 1 <= mes <= 12 and dia >= 1:
        
        # 2. Meses con 31 días (Enero, Marzo, Mayo, Julio, Agosto, Octubre, Diciembre)
        if mes in (1, 3, 5, 7, 8, 10, 12):
            if dia <= 31:
                fecha_correcta = True
                
        # 3. Meses con 30 días (Abril, Junio, Septiembre, Noviembre)
        elif mes in (4, 6, 9, 11):
            if dia <= 30:
                fecha_correcta = True
                
        # 4. Febrero (mes 2)
        elif mes == 2:
            if es_bisiesto(anio):
                if dia <= 29:
                    fecha_correcta = True
            else:
                if dia <= 28:
                    fecha_correcta = True

    # Resultado final
    if fecha_correcta:
        print(f"La fecha {dia}/{mes}/{anio} es CORRECTA.")
    else:
        print(f"La fecha {dia}/{mes}/{anio} NO es correcta.")