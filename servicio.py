
# SISTEMA INTEGRAL DE GESTION SOFTWARE FJ
# ARCHIVO: servicio.py
# DESCRIPCION: Clase abstracta para los servicios.

# Importamos las herramientas para crear clases abstractas.
from abc import ABC, abstractmethod

# Importamos una herramienta para validar numeros.
import math

# Importamos la excepcion personalizada.
from excepciones import ErrorValidacion


# Creamos la clase abstracta Servicio.
class Servicio(ABC):

    # Este metodo recibe los datos generales del servicio.
    def __init__(self, codigo, nombre, precio_hora):

        # Verificamos que el codigo sea un texto valido.
        if not isinstance(codigo, str) or not codigo.strip():
            raise ErrorValidacion("El codigo no es valido.")

        # Verificamos que el nombre sea correcto.
        if not isinstance(nombre, str) or not nombre.strip():
            raise ErrorValidacion("El nombre no es valido.")

        # Comprobamos que el precio sea numerico y positivo.
        if (isinstance(precio_hora, bool)
                or not isinstance(precio_hora, (int, float))
                or not math.isfinite(precio_hora)
                or precio_hora <= 0):
            raise ErrorValidacion("El precio debe ser positivo.")

        # Guardamos los datos generales del servicio.
        self._codigo = codigo.strip()
        self._nombre = nombre.strip()
        self._precio_hora = precio_hora

    # Obligamos a validar los parametros del servicio.
    @abstractmethod
    def validar_parametros(self, duracion):
        pass

    # Obligamos a implementar el calculo de costos.
    @abstractmethod
    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        pass

    # Obligamos a describir el servicio.
    @abstractmethod
    def describir_servicio(self):
        pass
