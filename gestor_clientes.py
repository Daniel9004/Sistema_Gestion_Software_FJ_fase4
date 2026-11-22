
# SOFTWARE FJ
# ARCHIVO: gestor_clientes.py
# DESCRIPCION: Registro y consulta de clientes en memoria.

# Importamos la clase Cliente.
from cliente import Cliente

# Importamos la excepcion para errores de clientes.
from excepciones import ErrorCliente


# Creamos la clase encargada de administrar clientes.
class GestorClientes:

    # Constructor del gestor.
    def __init__(self):

        # Creamos una lista vacia para guardar clientes.
        self._clientes = []

    # Metodo para registrar un nuevo cliente.
    def registrar(self, codigo, nombre, correo):

        # Recorremos los clientes existentes.
        for cliente in self._clientes:

            # Verificamos que el codigo no este repetido.
            if cliente.codigo == codigo:
                raise ErrorCliente(
                    "Ya existe un cliente con ese codigo."
                )

        # Creamos el cliente usando su clase.
        nuevo_cliente = Cliente(codigo, nombre, correo)

        # Guardamos el objeto en la lista.
        self._clientes.append(nuevo_cliente)

        # Devolvemos el cliente registrado.
        return nuevo_cliente

    # Metodo para buscar un cliente por su codigo.
    def buscar(self, codigo):

        # Recorremos la lista de clientes.
        for cliente in self._clientes:

            # Comparamos el codigo solicitado.
            if cliente.codigo == codigo:
                return cliente

        # Informamos si el cliente no existe.
        raise ErrorCliente("Cliente no encontrado.")

    # Metodo para consultar todos los clientes.
    def listar(self):

        # Devolvemos una copia de la lista.
        return list(self._clientes)
