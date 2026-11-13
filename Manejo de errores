# ARCHIVO: manejo de errores

import logging

from excepciones import (
    ErrorValidacion,
    ErrorReserva,
    ServicioNoDisponible,
    OperacionNoPermitida
)

# Configuracion del archivo de registros
logging.basicConfig(
    filename="eventos.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

logger = logging.getLogger(__name__)

# Funcion para registrar eventos del sistema
def registrar_evento(mensaje):
    logger.info(mensaje)

# Funcion para registrar errores
def registrar_error(mensaje):
    logger.error(mensaje)

# Funcion para ejecutar operaciones de una reserva
def ejecutar_operacion_reserva(reserva, operacion, disponible=True):

    logger.info("Inicio de la operacion: %s", operacion)

    try:

        if operacion == "confirmar":
            resultado = reserva.confirmar(disponible)

        elif operacion == "cancelar":
            resultado = reserva.cancelar()

        else:
            raise OperacionNoPermitida("La operacion solicitada no es valida.")

    except (
        ErrorValidacion,
        ErrorReserva,
        ServicioNoDisponible,
        OperacionNoPermitida
    ) as error:

        logger.exception("Error controlado durante la operacion.")

        return f"No fue posible completar la operacion: {error}"

    except Exception as error:

        logger.exception("Se presento un error inesperado.")

        # Encadenamiento de excepciones
        raise ErrorReserva("Ocurrio un error inesperado al procesar la reserva.") from error

    else:

        logger.info("Operacion realizada correctamente: %s",resultado)

        return resultado

    finally:

        logger.info("Finalizo la operacion: %s", operacion)
