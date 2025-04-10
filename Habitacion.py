"""
Módulo que define la clase base Habitacion para el sistema de reservas de crucero.

Este módulo implementa la clase base que será heredada por los diferentes tipos
de habitaciones disponibles en el crucero.
"""

class Habitacion:
    """
    Clase base que representa una habitación genérica en el crucero.
    
    Esta clase define los atributos y métodos comunes a todos los tipos de
    habitaciones disponibles en el sistema de reservas del crucero.
    
    Attributes:
        codigo_habitacion (str): Código único identificador de la habitación.
        acomodacion (int): Cantidad de personas que pueden alojarse en la habitación.
        cubierta (str): Tipo de cubierta donde se encuentra la habitación.
        disponibilidad (bool): Indica si la habitación está disponible para reservar.
        costo_predefinido (float): Costo base de la habitación por día.
    """
    
    def __init__(self, codigo_habitacion, acomodacion, cubierta, disponibilidad=True):
        """
        Inicializa una instancia de la clase Habitacion.
        
        Args:
            codigo_habitacion (str): Código único identificador de la habitación.
            acomodacion (int): Cantidad de personas que pueden alojarse.
            cubierta (str): Tipo de cubierta donde se encuentra la habitación.
            disponibilidad (bool, optional): Indica si la habitación está disponible. 
                Por defecto es True.
        """
        self.codigo_habitacion = codigo_habitacion
        self.acomodacion = acomodacion
        self.cubierta = cubierta
        self.disponibilidad = disponibilidad
        self.costo_predefinido = 100000.0
    
    def mostrar_habitacion(self):
        """
        Genera una representación en texto de la habitación incluyendo su costo.
        
        Returns:
            str: Cadena con los detalles de la habitación.
        """
        costo = self.calcular_costo(self.cubierta, 1, self.acomodacion)
        return f"{self.codigo_habitacion} - {self.cubierta} - {self.acomodacion} personas - {'Disponible' if self.disponibilidad else 'No disponible'} - ${costo}"
    
    def calcular_costo(self, cubierta, dias_reserva, acomodacion):
        """
        Calcula el costo de la habitación para la reserva.
        
        Método que debe ser sobrescrito por las clases derivadas para 
        implementar el cálculo específico según el tipo de habitación.
        
        Args:
            cubierta (str): Tipo de cubierta de la habitación.
            dias_reserva (int): Cantidad de días de la reserva.
            acomodacion (int): Cantidad de personas en la habitación.
            
        Returns:
            float: Costo total calculado para la reserva.
        """
        return self.costo_predefinido * dias_reserva
    
    def cambiar_disponibilidad(self, estado):
        """
        Cambia el estado de disponibilidad de la habitación.
        
        Args:
            estado (bool): Nuevo estado de disponibilidad (True = disponible).
            
        Returns:
            bool: True para confirmar que el cambio se realizó.
        """
        self.disponibilidad = estado
        return True
    
    def __str__(self):
        """
        Devuelve una representación en cadena de la habitación.
        
        Returns:
            str: Representación detallada de la habitación.
        """
        return self.mostrar_habitacion()