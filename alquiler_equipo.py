
# SISTEMA INTEGRAL DE GESTION SOFTWARE FJ
# ARCHIVO: alquiler_equipo.py
# DESCRIPCION: Servicio de alquiler de equipos.

# Importamos herramientas para validar numeros.
import math

# Importamos la clase abstracta Servicio.
from servicio import Servicio

# Importamos las excepciones personalizadas.
from excepciones import ErrorValidacion, ServicioNoDisponible


# Creamos la clase especializada AlquilerEquipo.
class AlquilerEquipo(Servicio):

    # Recibimos la informacion del equipo.
    def __init__(self, codigo, nombre, precio_hora, disponible=True):

        # Validamos los datos generales con la clase padre.
        super().__init__(codigo, nombre, precio_hora)

        # Comprobamos que la disponibilidad sea True o False.
        if not isinstance(disponible, bool):
            raise ErrorValidacion("Disponibilidad incorrecta.")

        # Guardamos el estado de disponibilidad.
        self._disponible = disponible

    # Validamos la duracion y disponibilidad del alquiler.
    def validar_parametros(self, duracion):

        # Verificamos que la duracion sea numerica y positiva.
        if (type(duracion) not in (int, float)
                or not math.isfinite(duracion)
                or duracion <= 0):
            raise ErrorValidacion("Duracion de alquiler incorrecta.")

        # Verificamos que el equipo este disponible.
        if not self._disponible:
            raise ServicioNoDisponible("El equipo no esta disponible.")

        # Confirmamos que los parametros son validos.
        return True

    # Calculamos el costo del alquiler.
    def calcular_costo(self, duracion, descuento=0, impuesto=0):

        # Validamos primero la solicitud.
        self.validar_parametros(duracion)

        # Verificamos los porcentajes opcionales.
        for nombre, valor in (("descuento", descuento),
                              ("impuesto", impuesto)):

            # Cada porcentaje debe estar entre 0 y 100.
            if (type(valor) not in (int, float)
                    or not math.isfinite(valor)
                    or not 0 <= valor <= 100):
                raise ErrorValidacion(
                    f"Porcentaje de {nombre} incorrecto."
                )

        # Calculamos el costo inicial.
        subtotal = self._precio_hora * duracion

        # Aplicamos el descuento.
        subtotal = subtotal * (1 - descuento / 100)

        # Aplicamos el impuesto.
        total = subtotal * (1 + impuesto / 100)

        # Devolvemos el costo final.
        return round(total, 2)

    # Describimos el equipo y su disponibilidad.
    def describir_servicio(self):

        # Determinamos el estado del equipo.
        estado = "Disponible" if self._disponible else "No disponible"

        # Devolvemos la descripcion del servicio.
        return (
            f"Equipo: {self._nombre} | "
            f"Precio por hora: ${self._precio_hora} | "
            f"Estado: {estado}"
        )
