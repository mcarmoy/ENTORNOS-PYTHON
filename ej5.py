usuario = input("Introduce el nombre de usuario: ")
contrasena = input("Introduce la contraseña: ")

# Se comprueba que AMBAS condiciones sean verdaderas
if usuario == "pepe" and contrasena == "suegra":
    print("Has entrado al sistema. ¡Bienvenido, pepe!")
else:
    print("ERROR: Credenciales incorrectas. Acceso denegado.")