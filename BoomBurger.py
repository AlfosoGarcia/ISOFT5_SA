# Importación de librerías
import hashlib  # (aunque no se está usando aún, podrías usarlo para encriptar contraseñas)

#funcion singleton: Clase que gestiona el menú como una única instancia compartida
class MenuSingleton:
    _instancia = None  #funcion singleton: Variable de clase que guarda la única instancia

    def __new__(cls):
        #funcion singleton: Si no existe instancia, se crea; si ya existe, se reutiliza
        if cls._instancia is None:
            cls._instancia = super(MenuSingleton, cls).__new__(cls)
            cls._instancia.menu = {
                "1": ("Hamburguesa Clásica", 5.99),
                "2": ("Hamburguesa Doble", 7.99),
                "3": ("Papas Fritas", 2.49),
                "4": ("Refresco", 1.99)
            }
        return cls._instancia

    def obtener_menu(self):
        #funcion singleton: Devuelve el menú almacenado en la instancia única
        return self.menu

#funcion singleton: Clase que gestiona el archivo de usuarios como una única instancia
class GestorUsuariosSingleton:
    _instancia = None  #funcion singleton: Variable de clase que guarda la única instancia

    def __new__(cls):
        #funcion singleton: Crea la instancia única si no existe
        if cls._instancia is None:
            cls._instancia = super(GestorUsuariosSingleton, cls).__new__(cls)
            cls._instancia.archivo = "usuarios.txt"
        return cls._instancia

    def leer_usuarios(self):
        #funcion singleton: Lee el archivo de usuarios desde la instancia única
        try:
            with open(self.archivo, "r") as archivo:
                return archivo.readlines()
        except FileNotFoundError:
            return []

    def guardar_usuario(self, usuario, correo, contraseña):
        #funcion singleton: Guarda un nuevo usuario en el archivo desde la instancia única
        with open(self.archivo, "a") as archivo:
            archivo.write(f"{usuario},{correo},{contraseña}\n")

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

    gestor = GestorUsuariosSingleton()  #funcion singleton: Se obtiene la instancia única del gestor de usuarios
    usuarios = gestor.leer_usuarios()  #funcion singleton: Se leen los usuarios desde la instancia única

    for linea in usuarios:
        datos = linea.strip().split(",")
        if len(datos) < 3:
            continue
        if datos[0] == usuario or datos[1] == correo:
            print("El nombre de usuario o correo ya está registrado.")
            return

    gestor.guardar_usuario(usuario, correo, contraseña)  #funcion singleton: Se guarda el usuario usando la instancia única
    print(f"¡Usuario registrado correctamente! Bienvenido a Boom Burger, {usuario}.")

# --- Módulo 2: Inicio de sesión ---
def INICIAR_SESION():
    print("--- Inicio de Sesión en Boom Burger ---")

    usuario = input("Nombre de usuario: ").strip()
    contraseña = input("Contraseña: ").strip()

    gestor = GestorUsuariosSingleton()  #funcion singleton: Se obtiene la instancia única del gestor de usuarios
    usuarios = gestor.leer_usuarios()  #funcion singleton: Se leen los usuarios desde la instancia única

    for linea in usuarios:
        datos = linea.strip().split(",")
        if len(datos) < 3:
            continue
        if datos[0] == usuario and datos[2] == contraseña:
            print(f"¡Bienvenido de nuevo, {usuario}!")
            return usuario
    print("Nombre de usuario o contraseña incorrectos.")
    return None

# --- Módulo 3: Realizar pedido ---
def REALIZAR_PEDIDO(usuario):
    print("--- Realizar Pedido ---")
    menu = MenuSingleton().obtener_menu()  #funcion singleton: Se obtiene el menú desde la instancia única

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
    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        REGISTRAR_USUARIOS()
    elif opcion == "2":
        usuario = INICIAR_SESION()
        if usuario:
            REALIZAR_PEDIDO(usuario)
    else:
        print("Opción no válida.")
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


#COMPROBAR QUE ESTA FUNCIONADO            
a = MenuSingleton()
b = MenuSingleton()
print(a is b)  # True