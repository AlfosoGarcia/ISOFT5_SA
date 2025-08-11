# Importación de librerías
import hashlib  # (aunque no se está usando aún, podrías usarlo para encriptar contraseñas)

# --- Módulo 1: Registro de usuarios ---
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
                    continue
                if datos[0] == usuario or datos[1] == correo:
                    print("El nombre de usuario o correo ya está registrado.")
                    return
    except FileNotFoundError:
        pass  # El archivo no existe, se creará luego

    # Guardar usuario
    with open("usuarios.txt", "a") as archivo:
        archivo.write(f"{usuario},{correo},{contraseña}\n")
        print(f"¡Usuario registrado correctamente! Bienvenido a Boom Burger, {usuario}.")

# --- Módulo 2: Inicio de sesión ---
def INICIAR_SESION():
    print("--- Inicio de Sesión en Boom Burger ---")

    usuario = input("Nombre de usuario: ").strip()
    contraseña = input("Contraseña: ").strip()

    try:
        with open("usuarios.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                if len(datos) < 3:
                    continue
                if datos[0] == usuario and datos[2] == contraseña:
                    print(f"¡Bienvenido de nuevo, {usuario}!")
                    return usuario
        print("Nombre de usuario o contraseña incorrectos.")
    except FileNotFoundError:
        print("No hay usuarios registrados aún.")
    return None

# --- Módulo 3: Realizar pedido ---
def REALIZAR_PEDIDO(usuario):
    print("--- Realizar Pedido ---")
    menu = {
        "1": ("Hamburguesa Clásica", 5.99),
        "2": ("Hamburguesa Doble", 7.99),
        "3": ("Papas Fritas", 2.49),
        "4": ("Refresco", 1.99)
    }

    total = 0
    pedido = []

    while True:
        print("\nMenú:")
        for clave, (producto, precio) in menu.items():
            print(f"{clave}. {producto} - ${precio:.2f}")

        opcion = input("Selecciona el número del producto (o '0' para finalizar): ")
        if opcion == "0":
            break
        elif opcion in menu:
            pedido.append(menu[opcion][0])
            total += menu[opcion][1]
            print(f"{menu[opcion][0]} agregado al pedido.")
        else:
            print("Opción no válida.")

    if pedido:
        with open("pedidos.txt", "a") as archivo:
            archivo.write(f"{usuario}: {', '.join(pedido)} - Total: ${total:.2f}\n")
        print(f"Pedido realizado con éxito. Total: ${total:.2f}")
    else:
        print("No se realizó ningún pedido.")

# --- Función principal ---
if __name__ == "__main__":
    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrarse")
        print("2. Iniciar Sesión")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            REGISTRAR_USUARIOS()
        elif opcion == "2":
            usuario = INICIAR_SESION()
            if usuario:
                REALIZAR_PEDIDO(usuario)
        elif opcion == "3":
            print("Gracias por visitar Boom Burger.")
            break
        else:
            print("Opción inválida.")