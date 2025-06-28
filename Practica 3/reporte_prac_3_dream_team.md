# Reporte de practica 3 

Este documento explica detalladamente que hace cada seccion del codigo que simula las acciones de un grupo de personas en una fiesta.
### integrantes del equipo:
- Sergio Alejandro Vironche Alvarez.
- Mia Valentina Castañeda Maciel.
- Christian Gabriel Rios Villegas.
- Roberto Alfonso Ambriz Garcia.
- Sergio Jehosua De Los Santos Ayón.

  ---

## 1. Importaciónes

```python
import time
import random
```

**Función:**  
Importa los módulos necesarios:
- `time`: permite pausar la ejecucion y ver mas en detalle que se esta ejecutando.
- `random`: permite seleccionar acciones aleatorias.

---

## 2. Definición de funciones (acciones posibles)

```python
def tomar(nombre): ...
def usar_baño(nombre): ...
def llamar_ex(nombre): ...
def cantar(nombre): ...
```

**Función:**  
Cada una simula una acción específica:
- `tomar`: beber cerveza.
- `usar_baño`: orinar y salir del baño.
- `llamar_ex`: llamar a su ex y ser rechazado.
- `cantar`: cantar canciones de Jose Jose.

Todas las funciones incluyen una pausa con `time.sleep(0.5)`.

---

## 3.  Lista de participantes

```python
Dream_team = ["Vironche", "Mia", "Alfonso", "Checo", "Chris"]
```

**Función:**  
Define los nombres de los participantes en la simulacion en un arreglo de cadena.

---

## 4. Lista de acciones

```python
acciones = [tomar, usar_baño, llamar_ex, cantar]
```

**Función:**  
Agrupa todas las acciones disponibles para que se puedan seleccionar aleatoriamente, se guardan en un arreglo para poder llamarlas facilmente.

---

## 5. Ciclo principal

```python
i = 0
while True:
    ...
    if i > 3:
        break
```

**Función:**  
Ejecuta la simulación en ciclos (4 veces en total). Controlado por una variable `i`, que seria lo que es nuestro indice.

---

## 6. Inicio de cada ciclo

```python
i += 1
print(f"--- Ciclo {i} ---")
acc_disp = acciones.copy()
```

**Función:**  
- Incrementa el ciclo.
- Muestra el numero del ciclo.
- Copia las acciones para no repetirlas en ese mismo ciclo, para esto usamos una variable auxiliar (acc_disp) para guardar las acciones.

---

## 7. Acciones de los participantes

```python
for nombre in Dream_team:
    if not acc_disp:
        acc_disp = acciones.copy()
    accion = random.choice(acc_disp)
    acc_disp.remove(accion)
    accion(nombre)
```

**Función:**  
- Recorre todos los participantes del `Dream_team`.
- Antes de asignar una accion, verifica si `acc_disp` (acciones disponibles) está vacía.
- Si está vacía, **vuelve a llenar la lista con todas las acciones** para permitir continuar.
- Esto es necesario porque hay más participantes (5) que acciones únicas (4), por lo tanto se permite la repetición de acciones una vez que se han agotado en ese ciclo.
- Luego, se selecciona una accion aleatoria, se elimina de la lista y se ejecuta.

---

## 8. Fin del ciclo

```python
print("--- Fin de un ciclo ---")
```

**Función:**  
Muestra un mensaje indicando que el ciclo ha terminado.

---

## 9. Cierre de la simulación

```python
print("Chris esta vomitando en el balcon")
```

**Función:**  
Muestra un mensaje final tras la simulación de los 4 ciclos.

---

## 10. Conclusiones
**Sergio Jehosua De Los Santos Ayón:**
Esta actividad nos dejo como aprendizale la gestion de recursos, ya que mientras una persona este usando el recurso puede saturar el programa ya que varios van a esperar el mismo recurso.

**Sergio Alejandro Vironche Alvarez:**
esta actividad la verdad estuvo super entretenida y chistosa y pues dentro de todo eso se obtuvo un gran aprendizaje.

**Mia Valentina Castañeda Maciel:**
Se logró el objetivo de la actividad, haciendo que todos los participantes tuvieran una actividad diferente en cada ciclo.


**Roberto Alfonso Ambriz Garcia:**
En esta actividad se muestra como el uso de listas y una estructura modular nos ayuda a un mejor orden y entendimiento, añadiendo un gran toque para finalizar la simulación.


**Rios Villegas Christian Gabriel:**
Se logró el objetivo de la actividad, igual se busco la forma de hacerlo mas dinámico 
asi que utilizamos ciertas funciones que lo hicieron mas sencillo y dinamico 
