# **Sistema de Gestión de Reservas de Crucero** 🚢  

Un sistema de reservas para cruceros desarrollado en Python, que permite gestionar habitaciones, usuarios y reservas con diferentes tipos de cubiertas (Económica, Normal, Premium).  

---

## **📌 Características**  
✅ **Gestión de Habitaciones:**  
- Tres tipos de cubiertas: **Económica, Normal, Premium**.  
- Capacidad para **2, 3 o 4 personas** por habitación.  
- Cálculo automático de costos según días de reserva y tipo de cubierta.  

✅ **Registro de Usuarios:**  
- Códigos únicos generados automáticamente (ej. `U01`).  
- Un usuario solo puede tener **una reserva activa**.  

✅ **Reservas:**  
- Códigos de reserva únicos (ej. `R001`).  
- Cancelación de reservas con liberación automática de habitaciones.  
- Consulta de reservas por código.  

✅ **Interfaz de Consola:**  
- Menú interactivo con emojis.  
- Búsqueda filtrada por cubierta y capacidad.  

---

## **⚙️ Estructura del Proyecto**  

```plaintext
📦crucero/
├── 📜main.py               # Interfaz principal del sistema
├── 📜Crucero.py            # Clase principal que gestiona reservas y habitaciones
├── 📜Habitacion.py         # Clase base para habitaciones
├── 📜Cubiertas.py          # Subclases de habitaciones (Económica, Normal, Premium)
├── 📜Usuario.py            # Clase para gestionar usuarios
├── 📜Reserva.py            # Clase para manejar reservas
├── 📜Normalizar.py         # Funciones para normalizar texto
└── 📜README.md             # Este archivo
```

---

## **🚀 Instalación y Ejecución**  

1. **Clonar el repositorio:**  
   ```bash
   git clone https://github.com/tu-usuario/reservas-crucero.git
   cd reservas-crucero
   ```

2. **Ejecutar el programa:**  
   ```bash
   python main.py
   ```

3. **Seguir las instrucciones del menú:**  
   ```
   🚢 SISTEMA DE RESERVAS DE CRUCERO 🚢
   ========================================
   1️⃣  Listar habitaciones disponibles
   2️⃣  Buscar habitaciones por cubierta/acomodación 🔍
   3️⃣  Realizar una reserva 📝
   4️⃣  Cancelar una reserva ❌
   5️⃣  Consultar reserva por código 🔎
   6️⃣  Listar todas las reservas 📋
   7️⃣  Salir 🚪
   ========================================
   ```

---

## **📝 Ejemplo de Uso**  

### **1. Realizar una reserva**  
1. Seleccionar opción **3** en el menú.  
2. Ingresar el código de habitación (ej. `E01`).  
3. Registrar usuarios (nombre y código opcional).  
4. Ingresar días de reserva.  
5. Confirmar y obtener código de reserva (ej. `R001`).  

### **2. Cancelar una reserva**  
1. Seleccionar opción **4** en el menú.  
2. Ingresar código de usuario (ej. `U01`).  
3. Confirmar cancelación.  

---

## **🛠️ Tecnologías Utilizadas**  
- **Python 3.9+**  
- **POO (Programación Orientada a Objetos)**  
- **Manejo de fechas (`datetime`)**  
- **Normalización de texto para búsquedas**  

---

## **📌 Requisitos**  
- Python 3 instalado.  
- No se requieren librerías externas.  

---

## **📜 Licencia**  
Este proyecto está bajo la licencia **MIT**.  

---

## **💡 Contribuciones**  
¡Las contribuciones son bienvenidas! Si deseas mejorar el código:  
1. Haz un **fork** del repositorio.  
2. Crea una rama con tu mejora (`git checkout -b feature/nueva-funcionalidad`).  
3. Envía un **Pull Request**.  

---

¡Gracias por usar el **Sistema de Reservas de Crucero**! ⚓
