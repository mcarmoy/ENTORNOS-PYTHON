cadena = input("Ingresa una cadena (ej. una letra): ")

if cadena.isupper():
    print(f"La cadena '{cadena}' está compuesta enteramente por letras mayúsculas.")
else:
    print(f"La cadena '{cadena}' contiene minúsculas, números o no es solo mayúsculas.")