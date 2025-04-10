"""
Módulo que define la clase Reserva para el sistema de reservas de crucero.

Este módulo implementa la clase que maneja las reservas de habitaciones
en el sistema de gestión del crucero.
"""

from datetime import datetime

class Reserva:
    """
    Clase que representa una reserva de habitación en el crucero.
    
    Esta clase maneja la información relacionada con una reserva específica,
    incluyendo los usuarios, habitación, días y fecha de la reserva.
    
    Attributes:
        dias_reserva (int): Cantidad de días que dura la reserva.
        fecha_reserva (datetime): Fecha en que se realizó la reserva.
        codigos_usuarios (list): Lista de códigos de usuarios asignados a la reserva.
        codigo_habitacion (str): Código de la habitación reservada.
        codigo_reserva (str): Código único identificador de la reserva.
        contador_reservas (int): Contador de clase para generar códigos únicos.
    """
  
    contador_reservas = 1
    
    def __init__(self, dias_reserva, codigos_usuarios, codigo_habitacion, fecha_reserva=None):
        """
        Inicializa una nueva instancia de reserva.
        
        Args:
            dias_reserva (int): Cantidad de días que dura la reserva.
            codigos_usuarios (list): Lista de códigos de usuarios asignados a la reserva.
            codigo_habitacion (str): Código de la habitación reservada.
            fecha_reserva (datetime, optional): Fecha de la reserva. Si es None,
                se establece la fecha actual.
        """
        self.dias_reserva = dias_reserva
        
        # Asignar fecha actual si no se proporciona una
        if fecha_reserva is None:
            self.fecha_reserva = datetime.now()
        else:
            self.fecha_reserva = fecha_reserva
        
        # Guardar información de usuarios y habitación
        self.codigos_usuarios = codigos_usuarios
        self.codigo_habitacion = codigo_habitacion
        
        # Generar código único para la reserva
        self.codigo_reserva = f"R{Reserva.contador_reservas:03d}"
        Reserva.contador_reservas += 1
    
    def __str__(self):
        """
        Devuelve una representación en cadena de la reserva.
        
        Returns:
            str: Representación detallada de la reserva, incluyendo usuarios,
                habitación, días y fecha.
        """
        usuarios_str = ", ".join([str(u) if u else "Vacante" for u in self.codigos_usuarios])
        return f"Reserva: {self.codigo_reserva} | Usuarios: {usuarios_str} | Habitación: {self.codigo_habitacion} | Días: {self.dias_reserva} | Fecha: {self.fecha_reserva.strftime('%Y-%m-%d')}"