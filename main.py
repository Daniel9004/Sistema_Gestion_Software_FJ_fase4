
# SOFTWARE FJ
# ARCHIVO: main.py
# DESCRIPCION: Menu principal del sistema.

# Importamos el modulo encargado de gestionar clientes.
from gestor_clientes import GestorClientes

# Importamos las excepciones personalizadas.
from excepciones import ErrorCliente, ErrorValidacion


# Funcion para mostrar las opciones del programa.
def mostrar_menu():

    print("\n===== SOFTWARE FJ =====")
    print("1. Registrar cliente")
    print("2. Consultar clientes")
    print("3. Salir")


# Funcion para registrar un nuevo cliente.
def registrar_cliente(gestor):

    # Solicitamos la informacion al usuario.
    codigo = input("Codigo del cliente: ").strip()
    nombre = input("Nombre completo: ").strip()
    correo = input("Correo electronico: ").strip()

    # Intentamos registrar el cliente.
    try:
        cliente = gestor.registrar(codigo, nombre, correo)

    # Controlamos los errores de validacion.
    except (ErrorCliente, ErrorValidacion) as error:
        print("Error controlado:", error)

    # Mostramos el resultado cuando todo funciona.
    else:
        print("Cliente registrado correctamente.")
        print(cliente.mostrar_informacion())


# Funcion para consultar los clientes registrados.
def consultar_clientes(gestor):

    # Obtenemos todos los clientes de la lista.
    clientes = gestor.listar()

    # Verificamos si la lista esta vacia.
    if not clientes:
        print("No hay clientes registrados.")
        return

    # Mostramos los clientes existentes.
    print("\nCLIENTES REGISTRADOS")

    for cliente in clientes:
        print(cliente.mostrar_informacion())


# Funcion que controla la ejecucion principal.
def ejecutar_programa():

    # Creamos el gestor que conservara los clientes.
    gestor = GestorClientes()

    # Mantenemos el menu activo hasta que se elija salir.
    while True:

        # Mostramos las opciones disponibles.
        mostrar_menu()

        # Leemos la opcion seleccionada.
        opcion = input("Seleccione una opcion: ").strip()

        # Opcion para registrar un cliente.
        if opcion == "1":
            registrar_cliente(gestor)

        # Opcion para consultar clientes.
        elif opcion == "2":
            consultar_clientes(gestor)

        # Opcion para finalizar el programa.
        elif opcion == "3":
            print("Gracias por utilizar Software FJ.")
            break

        # Controlamos las opciones incorrectas.
        else:
            print("Opcion no valida. Intente nuevamente.")


# Punto de entrada del programa.
if __name__ == "__main__":
    ejecutar_programa()
