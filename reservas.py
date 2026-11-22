# Importamos la clase Cliente para verificar los clientes.
from cliente import Cliente

# Importamos la clase Servicio para verificar los servicios.
from servicio import Servicio

# DESCRIPCION: Gestion de reservas de clientes y servicios

# Importacion de excepciones personalizadas
from excepciones import (
    ErrorValidacion,
    ErrorReserva,
    ServicioNoDisponible,
    OperacionNoPermitida
)

# Clase para gestionar las reservas
class Reserva:

    def __init__(self, codigo, cliente, servicio, duracion):

        # Validacion del codigo de reserva
        if not isinstance(codigo, str) or not codigo.strip():
            raise ErrorValidacion("El codigo de reserva no es valido.")

        # Validacion del cliente
        if cliente is None:
            raise ErrorValidacion("La reserva debe tener un cliente asociado.")

        # Validacion del servicio
        if servicio is None:
            raise ErrorValidacion("La reserva debe tener un servicio asociado.")

        # Validacion de la duracion
        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)):
            raise ErrorValidacion("La duracion debe ser un valor numerico.")

        if duracion <= 0:
            raise ErrorValidacion("La duracion debe ser mayor que cero.")

        # Inicializacion de los atributos
        self.codigo = codigo
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    # Metodo para confirmar una reserva
    def confirmar(self, disponible=True):

        if self.estado == "Cancelada":
            raise OperacionNoPermitida("No se puede confirmar una reserva cancelada.")

        if self.estado == "Confirmada":
            raise OperacionNoPermitida("La reserva ya esta confirmada.")

        if not disponible:
            raise ServicioNoDisponible("El servicio no se encuentra disponible.")

        self.estado = "Confirmada"

        return f"Reserva {self.codigo} confirmada correctamente."

    # Metodo para cancelar una reserva
    def cancelar(self):

        if self.estado == "Cancelada":
            raise OperacionNoPermitida("La reserva ya esta cancelada.")

        self.estado = "Cancelada"

        return f"Reserva {self.codigo} cancelada correctamente."
 # Metodo para procesar una reserva y calcular su costo.
    def procesar(self, descuento=0, impuesto=0):

        # Solo permitimos procesar reservas pendientes.
        if self.estado != "Pendiente":
            raise OperacionNoPermitida(
                "Solo se pueden procesar reservas pendientes."
            )

        # Comprobamos que el cliente sea un objeto Cliente.
        if not isinstance(self.cliente, Cliente):
            raise ErrorReserva(
                "La reserva debe tener un cliente valido."
            )

        # Comprobamos que el servicio sea un objeto Servicio.
        if not isinstance(self.servicio, Servicio):
            raise ErrorReserva(
                "La reserva debe tener un servicio valido."
            )

        # Calculamos el costo y validamos los parametros del servicio.
        total = self.servicio.calcular_costo(
            self.duracion, descuento, impuesto
        )

        # Confirmamos la reserva despues de las validaciones.
        self.confirmar()

        # Guardamos el costo calculado.
        self.costo_total = total

        # Devolvemos un mensaje con el resultado.
        return (
            f"Reserva {self.codigo} procesada correctamente. "
            f"Total: ${total:.2f}"
        ) 

    # Metodo para consultar los datos de la reserva
    def consultar_reserva(self):

        return {
            "codigo": self.codigo,
            "cliente": self.cliente,
            "servicio": self.servicio,
            "duracion": self.duracion,
            "estado": self.estado
        }

    # Metodo para mostrar la informacion de la reserva
    def __str__(self):

        return (
            f"Reserva: {self.codigo} | "
            f"Duracion: {self.duracion} | "
            f"Estado: {self.estado}"
        )
