# SOFTWARE FJ
# ARCHIVO: prueba_flujo_reservas.py
# DESCRIPCION: Pruebas de procesamiento de reservas.

# Importamos los gestores necesarios.
from gestor_clientes import GestorClientes
from gestor_reservas import GestorReservas

# Importamos el catalogo y la clase Reserva.
from catalogo_servicios import CatalogoServicios
from reservas import Reserva

# Importamos las excepciones personalizadas.
from excepciones import ErrorReserva, OperacionNoPermitida


# Creamos los gestores y el catalogo.
clientes = GestorClientes()
reservas = GestorReservas()
catalogo = CatalogoServicios()

# Registramos un cliente valido.
cliente = clientes.registrar(
    "C101", "Juan Perez", "juan@gmail.com"
)

# Obtenemos una sala del catalogo.
servicio = catalogo.buscar("S001")

# PRUEBA 1: Procesar una reserva correcta.
reserva = Reserva("R101", cliente, servicio, 2)

print("PRUEBA 1:")
print(reserva.procesar())

# Guardamos la reserva procesada.
reservas.agregar(reserva)

# PRUEBA 2: Intentar registrar el mismo codigo.
print("\nPRUEBA 2:")

try:
    reservas.agregar(reserva)

except ErrorReserva as error:
    print("Error controlado:", error)

# PRUEBA 3: Intentar procesar una reserva confirmada.
print("\nPRUEBA 3:")

try:
    reserva.procesar()

except OperacionNoPermitida as error:
    print("Error controlado:", error)

# Comprobamos que las fallas no detuvieron el programa.
print("\nReservas registradas:", len(reservas.listar()))
print("El programa sigue funcionando.")