"""
Módulo que define las diferentes clases de cubiertas disponibles en el crucero.

Este módulo implementa las clases específicas para cada tipo de cubierta
(Normal, Económica y Premium) que heredan de la clase base Habitacion.
"""

from Habitacion import Habitacion

class Normal(Habitacion):
    """
    Clase que representa una habitación en la cubierta Normal del crucero.
    
    Esta clase hereda de Habitacion e implementa un cálculo de costo específico
    para las habitaciones de la cubierta Normal.
    
    Attributes:
        costo_por_cubierta (float): Costo adicional por estar en la cubierta Normal.
    """
    
    def __init__(self, codigo_habitacion, acomodacion):
        """
        Inicializa una habitación de la cubierta Normal.
        
        Args:
            codigo_habitacion (str): Código único identificador de la habitación.
            acomodacion (int): Cantidad de personas que pueden alojarse.
        """
        super().__init__(codigo_habitacion, acomodacion, "Normal")
        self.costo_por_cubierta = 100000.0
    
    def calcular_costo(self, cubierta, dias_reserva, acomodacion):
        """
        Calcula el costo total de la reserva para una habitación Normal.
        
        El costo varía según la acomodación (cantidad de personas).
        
        Args:
            cubierta (str): Tipo de cubierta de la habitación.
            dias_reserva (int): Cantidad de días de la reserva.
            acomodacion (int): Cantidad de personas en la habitación.
            
        Returns:
            float: Costo total calculado para la reserva.
        """
        factor_acomodacion = 1.0
        if self.acomodacion == 3:
            factor_acomodacion = 1.2
        elif self.acomodacion == 4:
            factor_acomodacion = 1.5
            
        costo_total = (self.costo_predefinido + (self.costo_por_cubierta * factor_acomodacion)) * dias_reserva
        return costo_total

class Economica(Habitacion):
    """
    Clase que representa una habitación en la cubierta Económica del crucero.
    
    Esta clase hereda de Habitacion e implementa un cálculo de costo específico
    para las habitaciones de la cubierta Económica.
    
    Attributes:
        costo_por_cubierta (float): Costo adicional por estar en la cubierta Económica.
    """
    
    def __init__(self, codigo_habitacion, acomodacion):
        """
        Inicializa una habitación de la cubierta Económica.
        
        Args:
            codigo_habitacion (str): Código único identificador de la habitación.
            acomodacion (int): Cantidad de personas que pueden alojarse.
        """
        super().__init__(codigo_habitacion, acomodacion, "Económica")
        self.costo_por_cubierta = 80000.0
    
    def calcular_costo(self, cubierta, dias_reserva, acomodacion):
        """
        Calcula el costo total de la reserva para una habitación Económica.
        
        El costo varía según la acomodación (cantidad de personas).
        
        Args:
            cubierta (str): Tipo de cubierta de la habitación.
            dias_reserva (int): Cantidad de días de la reserva.
            acomodacion (int): Cantidad de personas en la habitación.
            
        Returns:
            float: Costo total calculado para la reserva.
        """
        factor_acomodacion = 1.0
        
        if self.acomodacion == 3:
            factor_acomodacion = 1.1
        elif self.acomodacion == 4:
            factor_acomodacion = 1.3
            
        costo_total = (self.costo_predefinido + (self.costo_por_cubierta * factor_acomodacion)) * dias_reserva
        return costo_total

class Premium(Habitacion):
    """
    Clase que representa una habitación en la cubierta Premium del crucero.
    
    Esta clase hereda de Habitacion e implementa un cálculo de costo específico
    para las habitaciones de la cubierta Premium.
    
    Attributes:
        costo_por_cubierta (float): Costo adicional por estar en la cubierta Premium.
    """
    
    def __init__(self, codigo_habitacion, acomodacion):
        """
        Inicializa una habitación de la cubierta Premium.
        
        Args:
            codigo_habitacion (str): Código único identificador de la habitación.
            acomodacion (int): Cantidad de personas que pueden alojarse.
        """
        super().__init__(codigo_habitacion, acomodacion, "Premium")
        self.costo_por_cubierta = 150000.0
    
    def calcular_costo(self, cubierta, dias_reserva, acomodacion):
        """
        Calcula el costo total de la reserva para una habitación Premium.
        
        El costo varía según la acomodación (cantidad de personas).
        
        Args:
            cubierta (str): Tipo de cubierta de la habitación.
            dias_reserva (int): Cantidad de días de la reserva.
            acomodacion (int): Cantidad de personas en la habitación.
            
        Returns:
            float: Costo total calculado para la reserva.
        """
        factor_acomodacion = 1.0
        
        if self.acomodacion == 3:
            factor_acomodacion = 1.3
        elif self.acomodacion == 4:
            factor_acomodacion = 1.7
            
        costo_total = (self.costo_predefinido + (self.costo_por_cubierta * factor_acomodacion)) * dias_reserva
        return costo_total