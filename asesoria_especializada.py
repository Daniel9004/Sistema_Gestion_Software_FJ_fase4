
# SISTEMA INTEGRAL DE GESTION SOFTWARE FJ
# ARCHIVO: asesoria_especializada.py
# DESCRIPCION: Servicio de asesorias especializadas.

# Importamos una herramienta para validar numeros.
import math

# Importamos nuestra clase abstracta Servicio.
from servicio import Servicio

# Importamos la excepcion personalizada.
from excepciones import ErrorValidacion


# Creamos la clase AsesoriaEspecializada.
# Esta clase hereda las caracteristicas de Servicio.
class AsesoriaEspecializada(Servicio):

    # Constructor que recibe los datos de la asesoria.
    def __init__(self, codigo, nombre, precio_hora,
                 especialidad, profesional):

        # Validamos codigo, nombre y precio con Servicio.
        super().__init__(codigo, nombre, precio_hora)

        # Comprobamos que la especialidad sea un texto valido.
        if (not isinstance(especialidad, str)
                or not especialidad.strip()):
            raise ErrorValidacion(
                "La especialidad no es valida."
            )

        # Comprobamos que el profesional tenga nombre.
        if (not isinstance(profesional, str)
                or not profesional.strip()):
            raise ErrorValidacion(
                "El profesional no es valido."
            )

        # Guardamos la especialidad.
        self._especialidad = especialidad.strip()

        # Guardamos el nombre del profesional.
        self._profesional = profesional.strip()

    # Implementamos la validacion de la duracion.
    def validar_parametros(self, duracion):

        # Verificamos que sea un numero positivo y finito.
        if (type(duracion) not in (int, float)
                or not math.isfinite(duracion)
                or duracion <= 0):
            raise ErrorValidacion(
                "La duracion de la asesoria no es valida."
            )

        # Confirmamos que la duracion es correcta.
        return True

    # Calculamos el costo con parametros opcionales.
    def calcular_costo(self, duracion, descuento=0, impuesto=0):

        # Validamos primero la duracion.
        self.validar_parametros(duracion)

        # Revisamos el descuento y el impuesto.
        for nombre, valor in (
            ("descuento", descuento),
            ("impuesto", impuesto)
        ):

            # Comprobamos que cada porcentaje sea valido.
            if (type(valor) not in (int, float)
                    or not math.isfinite(valor)
                    or not 0 <= valor <= 100):

                # Informamos el parametro incorrecto.
                raise ErrorValidacion(
                    f"El porcentaje de {nombre} no es valido."
                )

        # Multiplicamos el precio por las horas.
        subtotal = self._precio_hora * duracion

        # Aplicamos el descuento indicado.
        subtotal = subtotal * (1 - descuento / 100)

        # Aplicamos el impuesto indicado.
        total = subtotal * (1 + impuesto / 100)

        # Evitamos devolver resultados infinitos.
        if not math.isfinite(total):
            raise ErrorValidacion(
                "El costo calculado esta fuera de rango."
            )

        # Devolvemos el costo final con dos decimales.
        return round(total, 2)

    # Implementamos la descripcion del servicio.
    def describir_servicio(self):

        # Construimos el texto con los datos de la asesoria.
        return (
            f"Asesoria: {self._nombre} | "
            f"Especialidad: {self._especialidad} | "
            f"Profesional: {self._profesional} | "
            f"Precio por hora: ${self._precio_hora}"
        )
