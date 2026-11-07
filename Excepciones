# SISTEMA INTEGRAL DE GESTION SOFTWARE FJ
# DESCRIPCION: Excepciones personalizadas del sistema

# Clase base para las excepciones del sistema
class ErrorSistema(Exception):
    """Controla los errores generales del sistema."""
    pass
    
# Excepcion para errores de validacion
class ErrorValidacion(ErrorSistema):
    """Controla los datos que no cumplen las validaciones."""
    pass

# Excepcion relacionada con los clientes
class ErrorCliente(ErrorSistema):
    """Controla los errores relacionados con los clientes."""
    pass

# Excepcion relacionada con los servicios
class ErrorServicio(ErrorSistema):
    """Controla los errores relacionados con los servicios."""
    pass

# Excepcion para servicios no disponibles
class ServicioNoDisponible(ErrorServicio):
    """Controla los servicios que no estan disponibles."""
    pass

# Excepcion relacionada con las reservas
class ErrorReserva(ErrorSistema):
    """Controla los errores relacionados con las reservas."""
    pass

# Excepcion para operaciones no permitidas
class OperacionNoPermitida(ErrorSistema):
    """Controla las operaciones que no estan permitidas."""
    pass
