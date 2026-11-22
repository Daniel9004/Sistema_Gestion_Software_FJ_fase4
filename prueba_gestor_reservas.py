# SOFTWARE FJ
# Prueba de validacion de reservas duplicadas.

# Importamos las clases necesarias.
from gestor_reservas import GestorReservas
from reservas import Reserva
from excepciones import ErrorReserva

# Creamos el gestor de reservas.
gestor = GestorReservas()

# Creamos y guardamos la primera reserva.
reserva1 = Reserva("R010", "Juan Perez", "Sala de reuniones", 2)
gestor.agregar(reserva1)

print("Primera reserva registrada correctamente.")

# Creamos otra reserva con el mismo codigo.
reserva2 = Reserva("R010", "Maria Lopez", "Sala de reuniones", 3)

# Intentamos agregar la segunda reserva.
try:
    gestor.agregar(reserva2)

# Capturamos el error de codigo duplicado.
except ErrorReserva as error:
    print("Error controlado:", error)

# Consultamos el numero de reservas registradas.
print("Total de reservas:", len(gestor.listar()))

# Verificamos que el programa continua funcionando.
print("El programa sigue funcionando.")