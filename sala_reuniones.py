
# SISTEMA INTEGRAL DE GESTION SOFTWARE FJ
# ARCHIVO: sala_reuniones.py
# DESCRIPCION: Gestion del servicio de reserva de salas.

# Importamos herramientas para validar numeros.
import math

# Importamos la clase abstracta Servicio.
from servicio import Servicio

# Importamos nuestra excepcion personalizada.
from excepciones import ErrorValidacion


# Creamos la clase SalaReuniones que hereda de Servicio.
class SalaReuniones(Servicio):

    # Constructor que recibe los datos de la sala.
    def __init__(self, codigo, nombre, precio_hora, capacidad):

        # Validamos los datos generales mediante Servicio.
        super().__init__(codigo, nombre, precio_hora)

        # Verificamos que la capacidad sea un entero positivo.
        if type(capacidad) is not int or capacidad <= 0:
            raise ErrorValidacion(
                "La capacidad debe ser un entero positivo."
            )

        # Guardamos la capacidad de la sala.
        self._capacidad = capacidad

    # Sobrescribimos el metodo para validar la duracion.
    def validar_parametros(self, duracion):

        # Comprobamos que la duracion sea numerica y positiva.
        if (isinstance(duracion, bool)
                or not isinstance(duracion, (int, float))
                or not math.isfinite(duracion)
                or duracion <= 0):

            # Generamos una excepcion si es incorrecta.
            raise ErrorValidacion(
                "La duracion debe ser mayor que cero."
            )

        # Indicamos que la duracion es valida.
        return True

    # Calculamos el costo con descuento e impuesto opcionales.
    def calcular_costo(self, duracion, descuento=0, impuesto=0):

        # Verificamos primero la duracion solicitada.
        self.validar_parametros(duracion)

        # Revisamos los porcentajes recibidos.
        for nombre, porcentaje in (
            ("descuento", descuento),
            ("impuesto", impuesto)
        ):

            # Los porcentajes deben estar entre 0 y 100.
            if (isinstance(porcentaje, bool)
                    or not isinstance(porcentaje, (int, float))
                    or not math.isfinite(porcentaje)
                    or not 0 <= porcentaje <= 100):

                # Informamos el parametro incorrecto.
                raise ErrorValidacion(
                    f"El {nombre} debe estar entre 0 y 100."
                )

        # Calculamos el precio inicial de la reserva.
        subtotal = self._precio_hora * duracion

        # Aplicamos el descuento porcentual.
        subtotal = subtotal * (1 - descuento / 100)

        # Aplicamos el impuesto porcentual.
        total = subtotal * (1 + impuesto / 100)

        # Devolvemos el resultado con dos decimales.
        return round(total, 2)

    # Sobrescribimos el metodo para describir el servicio.
    def describir_servicio(self):

        # Devolvemos los datos principales de la sala.
        return (
            f"Sala: {self._nombre} | "
            f"Capacidad: {self._capacidad} personas | "
            f"Precio por hora: ${self._precio_hora}"
        )
