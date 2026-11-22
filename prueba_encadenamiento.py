# SOFTWARE FJ
# ARCHIVO: prueba_encadenamiento.py
# DESCRIPCION: Validacion del encadenamiento de errores.

# Importamos la funcion de manejo de operaciones.
from manejo_de_errores import ejecutar_operacion_reserva

# Importamos nuestra excepcion personalizada.
from excepciones import ErrorReserva


# Creamos una clase que simula un fallo inesperado.
class ReservaPrueba:

    # Metodo que simula la confirmacion.
    def confirmar(self, disponible=True):

        # Provocamos intencionalmente un error.
        raise ValueError("Error de prueba simulado.")


# Creamos el objeto utilizado en la prueba.
reserva = ReservaPrueba()

# Intentamos ejecutar la operacion.
try:

    ejecutar_operacion_reserva(reserva, "confirmar")

# Capturamos la excepcion personalizada.
except ErrorReserva as error:

    print("Error controlado:", error)

    # Comprobamos que conserva el error original.
    if isinstance(error.__cause__, ValueError):

        print("Encadenamiento de excepciones: CORRECTO")
        print("Error original:", error.__cause__)

    else:

        print("Encadenamiento de excepciones: FALLIDO")
        raise AssertionError(
            "No se conservo el error original."
        )

# Comprobamos que finaliza correctamente.
print("El programa sigue funcionando.")