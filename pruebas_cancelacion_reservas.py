# SOFTWARE FJ
# ARCHIVO: prueba_cancelacion_reservas.py
# DESCRIPCION: Validacion de cancelaciones.

# Importamos los gestores del sistema.
from gestor_clientes import GestorClientes
from gestor_reservas import GestorReservas

# Importamos las clases de servicios y reservas.
from catalogo_servicios import CatalogoServicios
from reservas import Reserva

# Importamos las excepciones personalizadas.
from excepciones import ErrorReserva, OperacionNoPermitida


# Creamos los gestores.
clientes = GestorClientes()
reservas = GestorReservas()
catalogo = CatalogoServicios()

# Registramos un cliente.
cliente = clientes.registrar(
    "C201", "Maria Lopez", "maria@gmail.com"
)

# Buscamos una sala.
servicio = catalogo.buscar("S001")

# Creamos una reserva.
reserva = Reserva("R201", cliente, servicio, 2)

# Procesamos y guardamos la reserva.
reserva.procesar()
reservas.agregar(reserva)


# PRUEBA 1: Cancelacion correcta.
print("PRUEBA 1:")

print(reserva.cancelar())
print("Estado:", reserva.estado)


# PRUEBA 2: Intento de cancelar nuevamente.
print("\nPRUEBA 2:")

try:
    reserva.cancelar()

except OperacionNoPermitida as error:
    print("Error controlado:", error)


# PRUEBA 3: Buscar una reserva inexistente.
print("\nPRUEBA 3:")

try:
    reservas.buscar("R999")

except ErrorReserva as error:
    print("Error controlado:", error)


# PRUEBA 4: Comprobar continuidad del programa.
print("\nPRUEBA 4:")

print("Reservas registradas:", len(reservas.listar()))
print("El programa sigue funcionando.")