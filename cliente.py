# SISTEMA INTEGRAL DE GESTION SOFTWARE FJ
# ARCHIVO : cliente.py
# DESCRIPCION: Registro y validacion de clientes.

#Importamos la herramienta para validar correos.
import re

# Importamos la clase abstracta que creamos anteriormente.
from entidad import Entidad

# Importamos la excepcion personalizada del proyecto.
from excepciones import ErrorValidacion


# Creamos la clase Cliente que hereda de Entidad.
class Cliente(Entidad): 

    # Explicamos la fnalidad de nuestra clase.
    """Representa un cliente registrado en Software FJ."""

    # Recibimos el codigo, el nombre y el correo del cliente.
    def __init__(self, codigo, nombre, correo):

        # Utilizamos el constructor de la clase Entidad.
        # Este se encarga de validar y guardar el codigo.
        super().__init__(codigo)

        # Comprobamos que el nombre sea un texto valido.
        if not isinstance(nombre, str) or len(nombre.strip()) < 3:

            # Generamos una excepcion si el nombre es incorrecto.
            raise ErrorValidacion(
                "El nombre no es valido"
            )
        # Comprobamos que el correo sea un texto.
        if not isinstance(correo, str):

            # Informamos que el correo es incorrecto.
            raise ErrorValidacion("El correo no es valido")

        # Quitamos los espacios al iniciio y al final.
        correo = correo.strip()

        # Verificamos la estructura basica del correo.
        patron = r"[^@\s]+@[^@\s]+\.[^@\s]+"

        # Comprobamos que el correo cumpla el patron.
        if not re.fullmatch(patron, correo):

            # Generamos un error si el formato es incorrecto.
            raise ErrorValidacion("El correo no es valido")

        # Guardamos el nombre como atributo privado.
        self.__nombre = nombre.strip()

        # Guardamos el correo privado en minusculas.
        self.__correo = correo.lower()

    # Permitimos consultar el nombre del cliente.
    @property
    def nombre(self):

        # Devolvemos el nombre registrado.
        return self.__nombre

    # Permitimos consultar el correo del cliente.
    @property
    def correo(self):

        # Devolvemos el correo registrado.
        return self.__correo

    # Implementamos el metodo abstracto de la clase Entidad.
    def mostrar_informacion(self):

        # Devolvemos los datos del cliente.
        return (
            f"Codigo: {self.codigo} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo}"
        )

