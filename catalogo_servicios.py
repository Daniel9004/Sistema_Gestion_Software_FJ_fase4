# SOFTWARE FJ
# ARCHIVO: catalogo_servicios.py
# DESCRIPCION: Administracion del catalogo de servicios.

# Importamos las clases de servicios especializados.
from sala_reuniones import SalaReuniones
from alquiler_equipo import AlquilerEquipo
from asesoria_especializada import AsesoriaEspecializada

# Importamos la excepcion personalizada.
from excepciones import ErrorServicio


# Clase encargada del catalogo de servicios.
class CatalogoServicios:

    # Constructor que se ejecuta al crear el catalogo.
    def __init__(self):

        # Creamos una sala de reuniones.
        sala = SalaReuniones(
            "S001", "Sala principal", 50000, 10
        )

        # Creamos un equipo disponible.
        equipo = AlquilerEquipo(
            "E001", "Portatil", 20000, True
        )

        # Creamos una asesoria especializada.
        asesoria = AsesoriaEspecializada(
            "A001", "Asesoria Python", 80000,
            "Programacion", "Ingeniero de sistemas"
        )

        # Guardamos los tres servicios en un diccionario.
        self._servicios = {
            "S001": sala,
            "E001": equipo,
            "A001": asesoria
        }

    # Metodo para consultar todos los servicios.
    def listar(self):

        # Obtenemos los servicios guardados.
        return list(self._servicios.values())

    # Metodo para buscar un servicio por codigo.
    def buscar(self, codigo):

        # Verificamos si existe el codigo solicitado.
        if codigo not in self._servicios:

            # Generamos un error cuando no existe.
            raise ErrorServicio("Servicio no encontrado.")

        # Devolvemos el servicio encontrado.
        return self._servicios[codigo]