"""
Módulo principal para el sistema de gestión de reservas de crucero.

Este módulo implementa la interfaz de usuario del sistema, permitiendo
realizar operaciones como listar habitaciones, buscar por criterios,
realizar reservas, cancelarlas y consultar información.
"""

from Crucero import Crucero
from Usuario import Usuario
from Normalizar import normalizar_texto

def mostrar_menu():
    """
    Muestra el menú principal del sistema de gestión de crucero.
    
    Presenta las opciones disponibles para el usuario utilizando
    emojis para una mejor experiencia visual.
    """
    print("\n" + "=" * 40)
    print(" 🚢 SISTEMA DE RESERVAS DE CRUCERO 🚢 ")
    print("=" * 40)
    print(" 1️⃣  Listar habitaciones disponibles")
    print(" 2️⃣  Buscar habitaciones por cubierta/acomodación 🔍")
    print(" 3️⃣  Realizar una reserva 📝")
    print(" 4️⃣  Cancelar una reserva ❌")
    print(" 5️⃣  Consultar reserva por código 🔎")
    print(" 6️⃣  Listar todas las reservas 📋")
    print(" 7️⃣  Salir 🚪")
    print("=" * 40)

def main():
    """
    Función principal que maneja la lógica del sistema de crucero.
    
    Esta función inicializa el sistema, muestra el menú y procesa
    las opciones seleccionadas por el usuario, realizando las
    operaciones correspondientes.
    """
    crucero = Crucero()
    usuarios = []
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            # Listar todas las habitaciones disponibles
            habitaciones = crucero.listar_habitaciones_disponibles()
            if habitaciones:
                print("\nHabitaciones disponibles:")
                for habitacion in habitaciones:
                    print(habitacion)
            else:
                print("\nNo hay habitaciones disponibles.")
        
        elif opcion == "2":
            # Buscar habitaciones por cubierta y/o acomodación
            print("\nOpciones de cubierta: Económica, Normal, Premium")
            cubierta = input("Ingrese la cubierta (deje en blanco para todas): ")
            
            if cubierta:
                cubierta_normalizada = normalizar_texto(cubierta)
                if cubierta_normalizada == "economica":
                    cubierta = "Económica"
                elif cubierta_normalizada == "normal":
                    cubierta = "Normal"
                elif cubierta_normalizada == "premium":
                    cubierta = "Premium"
                else:
                    print("Cubierta no válida. Utilizando todas las cubiertas.")
                    cubierta = None
            else:
                cubierta = None
            
            try:
                acomodacion = input("Ingrese la acomodación (2, 3 o 4 personas, deje en blanco para todas): ")
                if acomodacion == "":
                    acomodacion = None
                else:
                    acomodacion = int(acomodacion)
                    if acomodacion not in [2, 3, 4]:
                        print("Acomodación no válida. Debe ser 2, 3 o 4.")
                        continue
            except ValueError:
                print("Valor inválido para acomodación.")
                continue
            
            habitaciones = crucero.listar_habitaciones_disponibles(cubierta, acomodacion)
            if habitaciones:
                print("\nHabitaciones que cumplen con los criterios:")
                for habitacion in habitaciones:
                    print(habitacion)
            else:
                print("\nNo hay habitaciones que cumplan con los criterios.")
        
        elif opcion == "3":
            # Realizar una reserva
            codigo_habitacion = input("\nIngrese el código de la habitación a reservar: ")
            habitacion = crucero.buscar_habitacion(codigo_habitacion)
            
            if not habitacion or not habitacion.disponibilidad:
                print("Habitación no disponible o no existe.")
                continue
            
            capacidad = habitacion.acomodacion
            print(f"\nLa habitación seleccionada tiene capacidad para {capacidad} personas.")
            
            codigos_usuarios = []
            
            # Registrar usuarios para la reserva
            for i in range(1, capacidad + 1):
                print(f"\nRegistro de Usuario {i}/{capacidad}:")
                registrar = input(f"¿Desea registrar al usuario {i}? (S/N, N para dejar vacante): ").upper()
                
                if registrar == "S":
                    nombre = input("Ingrese el nombre del usuario: ")
                    
                    codigo_input = input("Ingrese el número de usuario (deje en blanco para asignar automáticamente): ")
                    
                    if codigo_input.strip() == "":
                        codigo = None  # Se asignará automáticamente
                    else:
                        try:
                            numero = int(codigo_input)
                            codigo = f"U{numero:02d}"
                        except ValueError:
                            print("Número de usuario inválido, se asignará automáticamente.")
                            codigo = None
                    
                    # Verificar si el usuario ya existe
                    usuario_existente = None
                    for u in usuarios:
                        if codigo and u.codigo == codigo:
                            usuario_existente = u
                            break
                    
                    if usuario_existente:
                        usuario = usuario_existente
                        print(f"Usuario existente encontrado: {usuario}")
                    else:
                        usuario = Usuario(nombre, codigo)
                        usuarios.append(usuario)
                        print(f"Nuevo usuario registrado: {usuario}")
                    
                    # Verificar si el usuario ya tiene una reserva
                    if usuario.obtener_reserva():
                        print(f"El usuario ya tiene una reserva: {usuario.obtener_reserva()}")
                        opciones = input("¿Desea seleccionar otro usuario? (S/N): ").upper()
                        if opciones == "S":
                            i -= 1  # Repetir este ciclo
                            continue
                        else:
                            print("Reserva cancelada.")
                            break
                    
                    codigos_usuarios.append(usuario.codigo)
                else:
                    codigos_usuarios.append(None)  # Vacante
            
            # Verificar que haya al menos un usuario registrado
            if not any(codigos_usuarios):
                print("No se registró ningún usuario. Reserva cancelada.")
                continue
            
            # Solicitar días de reserva
            try:
                dias_reserva = int(input("\nIngrese la cantidad de días de reserva: "))
                if dias_reserva <= 0:
                    print("La cantidad de días debe ser mayor a 0.")
                    continue
            except ValueError:
                print("Valor inválido para días de reserva.")
                continue
            
            # Mostrar costo y confirmar reserva
            costo = habitacion.calcular_costo(habitacion.cubierta, dias_reserva, habitacion.acomodacion)
            print(f"\nCosto de la reserva: ${costo}")
            
            confirmacion = normalizar_texto(input("¿Confirmar reserva? (S/N): "))
            if confirmacion == "s" or confirmacion == "si":
                codigo_reserva = crucero.crear_reserva(codigos_usuarios, codigo_habitacion, dias_reserva)
                if codigo_reserva:
                    # Asociar la reserva a los usuarios registrados
                    for codigo_usuario in codigos_usuarios:
                        if codigo_usuario:  # No asociar vacantes
                            for u in usuarios:
                                if u.codigo == codigo_usuario:
                                    u.agregar_reserva(codigo_reserva)
                                    break
                    print(f"\nReserva realizada con éxito. Código: {codigo_reserva}")
                else:
                    print("\nNo se pudo realizar la reserva.")
            else:
                print("\nReserva cancelada.")
        
        elif opcion == "4":
            # Cancelar una reserva
            codigo = input("\nIngrese el código del usuario (ejemplo: U01): ")
            
            # Asegurar formato correcto del código
            if not codigo.upper().startswith('U'):
                codigo = f"U{codigo}"
            
            # Buscar el usuario
            usuario = None
            for u in usuarios:
                if u.codigo == codigo:
                    usuario = u
                    break
            
            if not usuario:
                print("Usuario no encontrado.")
                continue
            
            # Verificar si tiene reserva
            codigo_reserva = usuario.obtener_reserva()
            if not codigo_reserva:
                print("El usuario no tiene reservas activas.")
                continue
            
            # Confirmar cancelación
            confirmacion = normalizar_texto(input(f"¿Confirmar cancelación de la reserva {codigo_reserva}? (S/N): "))
            if confirmacion == "s" or confirmacion == "si":
                if crucero.cancelar_reserva(codigo_reserva):
                    usuario.cancelar_reserva()
                    print("\nReserva cancelada con éxito.")
                else:
                    print("\nNo se pudo cancelar la reserva.")
            else:
                print("\nCancelación abortada.")
        
        elif opcion == "5":
            # Consultar reserva por código
            codigo_reserva = input("\nIngrese el código de la reserva (ejemplo: R001): ")
            info_reserva = crucero.obtener_info_reserva(codigo_reserva)
            print(f"\n{info_reserva}")
        
        elif opcion == "6":
            # Listar todas las reservas activas
            reservas = crucero.listar_todas_reservas()
            if reservas:
                print("\nReservas activas:")
                for reserva in reservas:
                    print(reserva)
            else:
                print("\nNo hay reservas activas.")
        
        elif opcion == "7":
            # Salir del sistema
            print("\nGracias por usar el sistema de reservas de crucero.")
            break
        
        else:
            print("\nOpción no válida.")

if __name__ == "__main__":
    main()