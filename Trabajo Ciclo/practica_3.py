import time
import random

def tomar(nombre):
    print(f"{nombre} esta tomando cerveza...")
    time.sleep(0.5)

def usar_baño(nombre):
    print(f"{nombre} esta orinando...")
    time.sleep(0.5)
    print(f"{nombre} salio del baño.")

def llamar_ex(nombre):
    print(f"{nombre} esta llamando a su ex...")
    time.sleep(0.5)
    print(f"{nombre} fue bateado :(")

def cantar(nombre):
    print(f"{nombre} esta cantando canciones de Jose Jose...")
    time.sleep(0.5)


Dream_team = ["Vironche", "Mia", "Alfonso", "Checo", "Chris"]


acciones = [tomar, usar_baño, llamar_ex, cantar]

    
i = 0
while True:
    i += 1
    print(f"\n--- Ciclo {i} ---\n")

    # Copia de acciones para no repetirlas en el mismo ciclo
    acc_disp = acciones.copy()

    for nombre in Dream_team:
        if not acc_disp:
            acc_disp = acciones.copy()  # Reponer acciones si se acaban

        accion = random.choice(acc_disp)
        acc_disp.remove(accion)
        accion(nombre)

    print("\n--- Fin de un ciclo ---\n")
    if i > 3:
        break

print("Chris esta vomitando en el balcon")
