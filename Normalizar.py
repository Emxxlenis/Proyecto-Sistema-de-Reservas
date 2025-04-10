"""
Módulo que proporciona funciones de normalización de texto.

Este módulo contiene funciones para normalizar texto, eliminando acentos
y convirtiendo a minúsculas para facilitar comparaciones no sensibles a
estos detalles.
"""

def normalizar_texto(texto):
    """
    Normaliza un texto eliminando acentos y convirtiéndolo a minúsculas.
    
    Esta función normaliza el texto para hacer búsquedas y comparaciones
    no sensibles a acentos y mayúsculas/minúsculas.
    
    Args:
        texto (str): Texto a normalizar.
        
    Returns:
        str: Texto normalizado (sin acentos y en minúsculas).
    """
    # Si el texto es None o vacío, devolver como está
    if not texto:
        return texto
    
    # Convertir a minúsculas
    texto = texto.lower()
    
    # Diccionario de caracteres acentuados y sus equivalentes sin acento
    acentos = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'à': 'a', 'è': 'e', 'ì': 'i', 'ò': 'o', 'ù': 'u',
        'ä': 'a', 'ë': 'e', 'ï': 'i', 'ö': 'o', 'ü': 'u',
        'â': 'a', 'ê': 'e', 'î': 'i', 'ô': 'o', 'û': 'u',
        'ã': 'a', 'ñ': 'n'
    }
    
    # Reemplazar cada caracter acentuado por su equivalente sin acento
    for acento, normal in acentos.items():
        texto = texto.replace(acento, normal)
    
    return texto