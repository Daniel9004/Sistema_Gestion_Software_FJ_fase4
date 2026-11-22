
# SOFTWARE FJ
# Prueba de validacion de clientes duplicados.

# Importamos el gestor y la excepcion.
from gestor_clientes import GestorClientes
from excepciones import ErrorCliente

# Creamos el gestor de clientes.
gestor = GestorClientes()

# Registramos el primer cliente.
gestor.registrar("C001", "Juan Perez", "juan@gmail.com")
print("Primer cliente registrado correctamente.")

# Intentamos registrar otro cliente con el mismo codigo.
try:
    gestor.registrar("C001", "Maria Lopez", "maria@gmail.com")

# Capturamos el error sin detener el programa.
except ErrorCliente as error:
    print("Error controlado:", error)

# Comprobamos cuantos clientes quedaron registrados.
print("Total de clientes:", len(gestor.listar()))

# Verificamos que el programa continua funcionando.
print("El programa sigue funcionando.")
