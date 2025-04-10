"""
Módulo que define la clase Usuario para el sistema de reservas de crucero.

Este módulo implementa la clase que maneja los datos de los usuarios
que realizan reservas en el sistema de gestión del crucero.
"""

from datetime import datetime

class Usuario:
    """
    Clase que representa a un usuario del sistema de reservas de crucero.
    
    Esta clase maneja la información de los usuarios que pueden hacer reservas
    en el sistema, incluyendo su información personal y las reservas asociadas.
    
    Attributes:
        nombre (str): Nombre del usuario.
        codigo (str): Código único identificador del usuario.
        fecha_registro (datetime): Fecha en que el usuario se registró.
        fecha_salida (datetime): Fecha en que el usuario terminó su estancia (si aplica).
        reserva (str): Código de la reserva asociada al usuario (si tiene).
        contador_usuarios (int): Contador de clase para generar códigos únicos.
    """

    contador_usuarios = 1
    
    def __init__(self, nombre, codigo=None, fecha_registro=None):
        """
        Inicializa una nueva instancia de usuario.
        
        Args:
            nombre (str): Nombre del usuario.
            codigo (str, optional): Código del usuario. Si es None, se genera automáticamente.
            fecha_registro (datetime, optional): Fecha de registro. Si es None,
                se establece la fecha actual.
        """
        self.nombre = nombre
        
        # Asignar código automático o procesar el código proporcionado
        if codigo is None:
            self.codigo = f"U{Usuario.contador_usuarios:03d}"
            Usuario.contador_usuarios += 1
        else:
            # Asegurar formato correcto del código
            if not str(codigo).upper().startswith('U'):
                self.codigo = f"U{int(codigo):03d}"
            else:
                self.codigo = codigo
        
        # Asignar fecha actual si no se proporciona una
        if fecha_registro is None:
            self.fecha_registro = datetime.now()
        else:
            self.fecha_registro = fecha_registro
        
        self.fecha_salida = None
        self.reserva = None
    
    def agregar_reserva(self, codigo_reserva):
        """
        Asocia una reserva al usuario.
        
        Args:
            codigo_reserva (str): Código de la reserva a asociar.
            
        Returns:
            bool: True si se agregó correctamente, False si ya tenía una reserva.
        """
        if self.reserva:
            return False
        self.reserva = codigo_reserva
        return True
    
    def cancelar_reserva(self):
        """
        Cancela la reserva asociada al usuario.
        
        Returns:
            bool: True si se canceló correctamente, False si no tenía reserva.
        """
        if not self.reserva:
            return False
        self.reserva = None
        return True
    
    def obtener_reserva(self):
        """
        Obtiene el código de la reserva asociada al usuario.
        
        Returns:
            str: Código de la reserva o None si no tiene.
        """
        return self.reserva
    
    def __str__(self):
        """
        Devuelve una representación en cadena del usuario.
        
        Returns:
            str: Representación detallada del usuario.
        """
        return f"{self.nombre} - ID: {self.codigo} - Registro: {self.fecha_registro.strftime('%Y-%m-%d')}"