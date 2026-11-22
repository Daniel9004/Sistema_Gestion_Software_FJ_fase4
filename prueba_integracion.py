
# SISTEMA INTEGRAL DE GESTION SOFTWARE FJ
# ARCHIVO: prueba_integracion.py
# DESCRIPCION: Prueba de integracion de los modulos.

# Importamos la clase Cliente.
from cliente import Cliente

# Importamos el servicio de salas de reuniones.
from sala_reuniones import SalaReuniones

# Importamos la clase Reserva del compañero.
from reservas import Reserva


# Creamos un cliente con datos validos.
cliente = Cliente("C001", "Juan Perez", "juan@gmail.com")

# Creamos una sala con precio de 50000 por hora.
sala = SalaReuniones("S001", "Sala de reuniones", 50000, 10)

# Creamos una reserva para el cliente y la sala.
reserva = Reserva("R006", cliente, sala, 2)

# Mostramos los datos del cliente.
print(cliente.mostrar_informacion())

# Mostramos la descripcion de la sala.
print(sala.describir_servicio())

# Calculamos el costo usando la duracion de la reserva.
costo = sala.calcular_costo(reserva.duracion)

# Mostramos el costo total.
print(f"Costo total: ${costo:.2f}")

# Verificamos que la reserva contiene el cliente correcto.
print("Cliente conectado:", reserva.cliente is cliente)

# Verificamos que la reserva contiene el servicio correcto.
print("Servicio conectado:", reserva.servicio is sala)

# Confirmamos la reserva.
print(reserva.confirmar())

# Consultamos el estado final.
print("Estado final:", reserva.estado)
