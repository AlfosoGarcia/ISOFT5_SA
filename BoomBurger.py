#importacion de librerias
import hashlib

def REGISTRAR_USUARIOS():
    print("---REGISTRAR USUARIOS---")
    usuario = input("Nombre de usuario: ").strip()
    contraseña = input("Ingrese Contraseña: ").strip()
    confirmar = input("Confirme su contraseña: ").strip()

    if contraseña != confirmar:
        print("Las contraseñas no coinciden")
        return
    
    #verificar si el usuario existe
    try:
        with open("usuarios.txt","r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                if datos[0] == usuario:
                    print("El nombre de usuario ya se encuentra registrado")
                    return
    except FileNotFoundError:
        pass #EL ARCHIVO NO EXISTE SE CREADA DESPUES

    #GUARDAR USUARIO 
    with open("usuarios.txt" ,"a") as archivo:
        archivo.write(f"{usuario},{contraseña}\n")
        print("usuario registrado correctamente")
#ejecutar registro
REGISTRAR_USUARIOS()