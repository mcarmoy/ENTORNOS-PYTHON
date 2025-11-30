def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

try:
    mes = int(input("Ingresa el número del mes (1 a 12): "))
    
    if mes == 2:
        # Se pide el año solo si el mes es febrero, para dar una respuesta precisa.
        anio = int(input("Ingresa el año para la comprobación de febrero: "))
    else:
        anio = 0 # No usado, pero necesario para la estructura.
        
except ValueError:
    print("ERROR: Ingresa solo números enteros.")
else:
    dias = 0
    
    # Comprobación de que el mes está en el rango correcto
    if 1 <= mes <= 12:
        
        # Meses con 31 días (Enero, Marzo, Mayo, Julio, Agosto, Octubre, Diciembre)
        if mes in (1, 3, 5, 7, 8, 10, 12):
            dias = 31
            
        # Meses con 30 días (Abril, Junio, Septiembre, Noviembre)
        elif mes in (4, 6, 9, 11):
            dias = 30
            
        # Febrero
        elif mes == 2:
            if es_bisiesto(anio):
                dias = 29
            else:
                dias = 28
        
        print(f"El mes {mes} tiene {dias} días.")
    else:
        print("ERROR: Número incorrecto. El mes debe ser un número entre 1 y 12.")