## Quien es el CEO
El CEO del Proyecto sera Mia Valentina Castañeda Maciel 

## Quien es el arquitecto
Sergio Alejandro Vironche Alvarez 

## quien es el "SD-Front-End"
Cristian Gabriel Rios Villegas
Sergio Ayon de los santos Ayon
## quien es el "SD-Back-End"
Roberto Alfonso Ambriz Garcia
Sergio Alejandro Vironche Alvarez
# Plan de Desarrollo - Boom Burger App (12 semanas / 3 meses)

Este documento describe los 12 hitos principales para el desarrollo simulado de la app Boom Burger, distribuidos en 3 meses 4 semanas cada uno.


## Mes 1: Fundamentos del Sistema (Semana 1 a 4)

### Hito 1 (Semana 1): Configuración del entorno y backlog
- Repositorio del proyecto creado (Git).
- Configuración de entorno backend (FastAPI) y frontend (React Native).
- Base de datos PostgreSQL conectada.
- Definición del backlog priorizado con tareas iniciales.

### Hito 2 (Semana 2): Registro de usuarios (1ª validación funcional)
- Formulario de registro.
- Validación de datos (correo, contraseña, campos obligatorios).
- Hash de contraseñas y almacenamiento seguro en DB.
- Confirmación visual en frontend.


### Hito 3 (Semana 3): Autenticación + mensaje de bienvenida
- Implementación de login con JWT.
- Persistencia de sesión/token.
- Pantalla de bienvenida al ingresar correctamente.

### Hito 4 (Semana 4): Diseño e integración del menú inicial
- Backend: modelo de producto con nombre, precio, descripción e imagen.
- Frontend: vista de menú con 3 productos iniciales conectados a API.


## Mes 2: Funcionalidades de pedido (Semana 5 a 8)

### Hito 5 (Semana 5): Visualización de productos con precios
- implementar API de metodo de pago         w
- Vista de detalle por producto.
- Estilos visuales jerarquizados (nombre, precio, descripción, imagen).


### Hito 6 (Semana 6): Agregar al carrito
- Lógica para añadir productos seleccionados.
- Visualización de productos en el carrito.
- Cálculo automático de precio total.


### Hito 7 (Semana 7): Ubicación y sucursal
- Visualización de ubicación en mapa (Google Maps / Leaflet).
- Selección de sucursal (simulada).
- Almacenamiento del punto de entrega en el pedido.

---

### Hito 8 (Semana 8): Solicitar pedido
- Botón "Realizar pedido" desde carrito.
- Envío de orden al backend (usuario, productos, ubicación).
- Confirmación visual de pedido generado.

---

## Mes 3: Integración de entrega (Semana 9 a 12)

### Hito 9 (Semana 9): Historial de pedidos
- Endpoint protegido `/mis-pedidos`.
- Vista para mostrar órdenes anteriores del usuario.
- Ordenados por fecha.

---

### Hito 10 (Semana 10): Ajustes de diseño y experiencia 
- Revisión visual general.
- Adaptación a diferentes dispositivos.
- Animaciones, microinteracciones y coherencia de estilo.

---

### Hito 11 (Semana 11): Pruebas funcionales y validación 
- Casos de prueba para flujo completo.
- Manejo de errores y mensajes amigables.
- Revisión de seguridad (input, token, fallos esperados).

---

### Hito 12 (Semana 12): Lanzamiento MVP
- Despliegue en plataforma (Render/Railway).
- Documentación técnica (API, instalación).
- Presentación funcional del producto mínimo viable.

---

## Notas finales
- El desarrollo es progresivo y funcional desde el primer mes.
- Se prioriza la validación del registro y experiencia de pedido como ejes centrales del MVP.
- Fases futuras pueden incluir pasarela de pago, recompensas o integraciones externas.

