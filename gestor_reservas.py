# SOFTWARE FJ
# ARCHIVO: gestor_reservas.py
# DESCRIPCION: Registro y consulta de reservas en memoria.

# Importamos la clase Reserva.
from reservas import Reserva

# Importamos la excepcion de reservas.
from excepciones import ErrorReserva


# Creamos la clase para administrar reservas.
class GestorReservas:

    # Constructor de la clase.
    def __init__(self):

        # Lista donde guardaremos las reservas.
        self._reservas = []

    # Metodo para agregar una reserva.
    def agregar(self, reserva):

        # Verificamos que recibimos un objeto Reserva.
        if not isinstance(reserva, Reserva):
            raise ErrorReserva(
                "Se requiere un objeto Reserva valido."
            )

        # Verificamos que el codigo no este duplicado.
        for existente in self._reservas:

            if existente.codigo == reserva.codigo:
                raise ErrorReserva(
                    "Ya existe una reserva con ese codigo."
                )

        # Guardamos la reserva en la lista.
        self._reservas.append(reserva)

        # Devolvemos la reserva guardada.
        return reserva

    # Metodo para buscar una reserva.
    def buscar(self, codigo):

        # Recorremos las reservas registradas.
        for reserva in self._reservas:

            # Comparamos el codigo.
            if reserva.codigo == codigo:
                return reserva

        # Informamos si no encontramos la reserva.
        raise ErrorReserva("Reserva no encontrada.")

    # Metodo para consultar todas las reservas.
    def listar(self):

        # Devolvemos una copia de la lista.
        return list(self._reservas)