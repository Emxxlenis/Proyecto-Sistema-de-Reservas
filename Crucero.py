"""
Módulo que define la clase principal Crucero para el sistema de reservas.

Este módulo implementa la clase central que coordina la gestión de habitaciones
y reservas en el sistema de gestión del crucero.
"""

from Cubiertas import Economica, Normal, Premium
from Reserva import Reserva
from Normalizar import normalizar_texto

class Crucero:
    """
    Clase principal que gestiona el sistema de reservas del crucero.
    
    Esta clase coordina la gestión de habitaciones, reservas y la interacción
    entre estos componentes en el sistema de reservas del crucero.
    
    Attributes:
        habitaciones (list): Lista de objetos de tipo Habitacion disponibles.
        reservas (list): Lista de objetos de tipo Reserva realizadas.
    """
    
    def __init__(self):
        """
        Inicializa una nueva instancia del sistema de crucero.
        
        Crea las listas de habitaciones y reservas, y realiza la inicialización
        de las habitaciones disponibles en el crucero.
        """
        self.habitaciones = []
        self.reservas = []
        self.inicializar_habitaciones()
    
    def inicializar_habitaciones(self):
        """
        Inicializa las habitaciones disponibles en el crucero.
        
        Crea 10 habitaciones para cada tipo de cubierta (Económica, Normal y Premium)
        con diferentes capacidades de acomodación (2, 3 y 4 personas).
        """
        # Crear 10 habitaciones para cada cubierta con diferentes acomodaciones
        # 3 habitaciones para 2 personas, 4 para 3 personas, 3 para 4 personas por cubierta
        
        # Habitaciones Económicas
        for i in range(1, 4):
            self.habitaciones.append(Economica(f"E{i:02d}", 2))
        for i in range(4, 8):
            self.habitaciones.append(Economica(f"E{i:02d}", 3))
        for i in range(8, 11):
            self.habitaciones.append(Economica(f"E{i:02d}", 4))
        
        # Habitaciones Normales
        for i in range(1, 4):
            self.habitaciones.append(Normal(f"N{i:02d}", 2))
        for i in range(4, 8):
            self.habitaciones.append(Normal(f"N{i:02d}", 3))
        for i in range(8, 11):
            self.habitaciones.append(Normal(f"N{i:02d}", 4))
        
        # Habitaciones Premium
        for i in range(1, 4):
            self.habitaciones.append(Premium(f"P{i:02d}", 2))
        for i in range(4, 8):
            self.habitaciones.append(Premium(f"P{i:02d}", 3))
        for i in range(8, 11):
            self.habitaciones.append(Premium(f"P{i:02d}", 4))
    
    def buscar_habitacion(self, codigo_habitacion):
        """
        Busca una habitación por su código.
        
        Args:
            codigo_habitacion (str): Código de la habitación a buscar.
            
        Returns:
            Habitacion: Objeto habitación encontrado o None si no existe.
        """
        for habitacion in self.habitaciones:
            if habitacion.codigo_habitacion == codigo_habitacion:
                return habitacion
        return None
    
    def listar_habitaciones_disponibles(self, cubierta=None, acomodacion=None):
        """
        Lista las habitaciones disponibles según los criterios especificados.
        
        Args:
            cubierta (str, optional): Tipo de cubierta a filtrar.
            acomodacion (int, optional): Capacidad de acomodación a filtrar.
            
        Returns:
            list: Lista de habitaciones que cumplen con los criterios y están disponibles.
        """
        habitaciones_disponibles = []
        
        # Normalizar la cubierta para facilitar la comparación
        cubierta_normalizada = normalizar_texto(cubierta) if cubierta else None
        
        for habitacion in self.habitaciones:
            if habitacion.disponibilidad:
                cubierta_hab_normalizada = normalizar_texto(habitacion.cubierta)
                
                # Aplicar filtros si se especificaron
                if cubierta_normalizada and cubierta_hab_normalizada != cubierta_normalizada:
                    continue
                if acomodacion and habitacion.acomodacion != acomodacion:
                    continue
                habitaciones_disponibles.append(habitacion)
        return habitaciones_disponibles
    
    def crear_reserva(self, codigos_usuarios, codigo_habitacion, dias_reserva):
        """
        Crea una nueva reserva en el sistema.
        
        Args:
            codigos_usuarios (list): Lista de códigos de usuarios para la reserva.
            codigo_habitacion (str): Código de la habitación a reservar.
            dias_reserva (int): Cantidad de días que durará la reserva.
            
        Returns:
            str: Código de la reserva creada o None si no se pudo crear.
        """
        habitacion = self.buscar_habitacion(codigo_habitacion)
        if not habitacion or not habitacion.disponibilidad:
            return None
        
        # Cambiar disponibilidad de la habitación
        habitacion.cambiar_disponibilidad(False)
        
        # Crear y registrar la reserva
        reserva = Reserva(dias_reserva, codigos_usuarios, codigo_habitacion)
        self.reservas.append(reserva)
        
        return reserva.codigo_reserva
    
    def cancelar_reserva(self, codigo_reserva):
        """
        Cancela una reserva existente.
        
        Args:
            codigo_reserva (str): Código de la reserva a cancelar.
            
        Returns:
            bool: True si se canceló correctamente, False si no se encontró.
        """
        for reserva in self.reservas:
            if reserva.codigo_reserva == codigo_reserva:
                # Liberar la habitación
                habitacion = self.buscar_habitacion(reserva.codigo_habitacion)
                if habitacion:
                    habitacion.cambiar_disponibilidad(True)
                
                # Eliminar la reserva
                self.reservas.remove(reserva)
                return True
        return False
    
    def obtener_info_reserva(self, codigo_reserva):
        """
        Obtiene información detallada de una reserva.
        
        Args:
            codigo_reserva (str): Código de la reserva a consultar.
            
        Returns:
            str: Información detallada de la reserva o mensaje de error.
        """
        for reserva in self.reservas:
            if reserva.codigo_reserva == codigo_reserva:
                return str(reserva)
        return "Reserva no encontrada."
    
    def listar_todas_reservas(self):
        """
        Lista todas las reservas activas en el sistema.
        
        Returns:
            list: Lista de strings con la información de cada reserva.
        """
        return [str(reserva) for reserva in self.reservas]
    
    def calcular_costo_reserva(self, codigo_habitacion, dias_reserva):
        """
        Calcula el costo de una reserva para una habitación específica.
        
        Args:
            codigo_habitacion (str): Código de la habitación.
            dias_reserva (int): Cantidad de días de la reserva.
            
        Returns:
            float: Costo total calculado o 0 si la habitación no existe.
        """
        habitacion = self.buscar_habitacion(codigo_habitacion)
        if habitacion:
            return habitacion.calcular_costo(habitacion.cubierta, dias_reserva, habitacion.acomodacion)
        return 0