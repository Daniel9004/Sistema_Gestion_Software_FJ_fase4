# ARCHIVO: prueba_error_controlado.py
# OBJETIVO: Comprobar el control de errores en reservas.

# Importamos la herramienta para registrar errores.
import logging

# Importamos la clase Reserva.
from reservas import Reserva

# Importamos la excepcion personalizada.
from excepciones import OperacionNoPermitida

# Configuramos el archivo donde registraremos el error.
logging.basicConfig(
    filename="eventos.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Creamos una reserva de prueba.
reserva = Reserva("R004", "Juan Perez", "Sala de reuniones", 2)

# Iniciamos el bloque de operaciones.
try:

    # Confirmamos la reserva.
    print(reserva.confirmar())

    # Cancelamos la reserva.
    print(reserva.cancelar())

    # Intentamos confirmar una reserva ya cancelada.
    print(reserva.confirmar())

# Capturamos la operacion no permitida.
except OperacionNoPermitida as error:

    # Guardamos el error y su detalle en el archivo de logs.
    logging.exception("Intento de confirmar reserva cancelada")

    # Mostramos un mensaje sin detener el programa.
    print(f"Error controlado: {error}")

# Este bloque se ejecuta si no ocurre ninguna excepcion.
else:

    # Informamos que las operaciones fueron exitosas.
    print("Operaciones realizadas sin errores.")

# Este bloque se ejecuta siempre.
finally:

    # Informamos que finalizo el procesamiento.
    print("Finalizo el procesamiento de la reserva.")

# Comprobamos que la ejecucion puede continuar.
print("El programa sigue funcionando.")