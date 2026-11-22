
# SISTEMA INTEGRAL DE GESTION SOFTWARE FJ
# ARCHIVO: prueba_polimorfismo.py
# DESCRIPCION: Comprobacion del polimorfismo.

# Importamos el servicio de reserva de salas.
from sala_reuniones import SalaReuniones

# Importamos el servicio de alquiler de equipos.
from alquiler_equipo import AlquilerEquipo

# Importamos el servicio de asesorias especializadas.
from asesoria_especializada import AsesoriaEspecializada


# Creamos una sala de reuniones.
sala = SalaReuniones("S001", "Sala principal", 50000, 10)

# Creamos un equipo disponible para alquiler.
equipo = AlquilerEquipo("E001", "Portatil", 20000, True)

# Creamos una asesoria especializada.
asesoria = AsesoriaEspecializada(
    "A001", "Asesoria Python", 80000,
    "Programacion", "Ingeniero de sistemas"
)

# Agrupamos los tres servicios en una lista.
servicios = [sala, equipo, asesoria]

# Recorremos cada servicio de la lista.
for servicio in servicios:

    # Calculamos dos horas mediante el mismo metodo.
    costo = servicio.calcular_costo(2)

    # Mostramos el tipo de servicio y su costo.
    print(f"{type(servicio).__name__}: ${costo:.2f}")
