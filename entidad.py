# SISTEMA INTEGRAL DE GESTION SOFTWARE FJ
# ARCHIVO : entidad.py
# DESCRIPCION: Clase abstracta general del sistema.      

#Importamos las herramientas para crear clases abstractas.
from abc import ABC, abstractmethod

# Importamos la excepcion personalizada del proyecto.
from excepciones import ErrorValidacion

# Definimos la clase abstracta Entidad.
class Entidad(ABC):

    # Explicamos la finalidad de esta clase.
    """Clase base para las entidades del sistema Software FJ."""

    # Constructor que recibe el codigo identificador.
    def __init__(self, codigo):

        # Verificamos que el codigo sea un texto no vacio.
        if not isinstance(codigo, str) or not codigo.strip():

            # Lanzamos un error si el codigo es incorrecto.
            raise ErrorValidacion("El codigo no es valido")

        # Guardamos el codigo como atributo protegido.
        self._codigo = codigo.strip()

    # Permitimos consultar el codigo sin modificarlo directamente.
    @property
    def codigo(self):

        # Devolvemos el codigo registrado.
        return self._codigo

    #Indicamos que las clases hijas deben implementar este metodo.
    @abstractmethod
    def mostrar_informacion(self):
        
        # Dejamos el metodo pendiente para las clases derivadas.
        pass
