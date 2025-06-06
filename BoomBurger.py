# Importación de librerías
import hashlib

def REGISTRAR_USUARIOS():
    print("--- Bienvenido a Boom Burger ---")

    usuario = input("Nombre de usuario: ").strip()
    correo = input("Correo electrónico: ").strip()
    contraseña = input("Ingrese contraseña: ").strip()
    confirmar = input("Confirme su contraseña: ").strip()

    if contraseña != confirmar:
        print("Las contraseñas no coinciden.")
        return

    # Verificar si el usuario o correo ya existen
    try:
        with open("usuarios.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                if len(datos) < 3:
                    continue  # Saltar líneas mal formateadas
                if datos[0] == usuario or datos[1] == correo:
                    print("El nombre de usuario o correo ya está registrado.")
                    return
    except FileNotFoundError:
        pass  # El archivo no existe, se creará luego

    # Guardar usuario
    with open("usuarios.txt", "a") as archivo:
        archivo.write(f"{usuario},{correo},{contraseña}\n")
        print(f"¡Usuario registrado correctamente! Bienvenido a Boom Burger, {usuario}.")

# Ejecutar registro
REGISTRAR_USUARIOS()

