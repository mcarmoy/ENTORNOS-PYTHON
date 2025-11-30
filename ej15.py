try:
    num_alumnos = int(input("Ingresa el número total de alumnos para el viaje: "))
except ValueError:
    print("Error: Ingresa un número entero positivo.")
else:
    costo_compania = 0
    costo_por_alumno = 0
    
    if num_alumnos <= 0:
        print("El número de alumnos debe ser positivo para organizar el viaje.")
        
    # Caso 1: 100 alumnos o más
    elif num_alumnos >= 100:
        costo_por_alumno = 65
        costo_compania = num_alumnos * costo_por_alumno
        
    # Caso 2: 50 a 99 alumnos
    elif num_alumnos >= 50:  # Implica (num_alumnos >= 50 AND num_alumnos <= 99)
        costo_por_alumno = 70
        costo_compania = num_alumnos * costo_por_alumno
        
    # Caso 3: 30 a 49 alumnos
    elif num_alumnos >= 30:  # Implica (num_alumnos >= 30 AND num_alumnos <= 49)
        costo_por_alumno = 95
        costo_compania = num_alumnos * costo_por_alumno
        
    # Caso 4: Menos de 30 alumnos
    else:  # Implica (num_alumnos < 30 AND num_alumnos > 0)
        costo_compania = 4000
        # El costo individual es el total dividido entre el número de alumnos
        costo_por_alumno = costo_compania / num_alumnos
        
    # Mostrar resultados
    if num_alumnos > 0:
        print(f"\nNúmero de alumnos: {num_alumnos}")
        print(f"Pago total a la compañía de autobuses: {costo_compania:.2f} euros")
        print(f"Costo individual que debe pagar cada alumno: {costo_por_alumno:.2f} euros")