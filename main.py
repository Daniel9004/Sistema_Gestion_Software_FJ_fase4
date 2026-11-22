
# SOFTWARE FJ
# ARCHIVO: main.py
# DESCRIPCION: Menu principal del sistema de gestion.

# Importamos el gestor de clientes.
from gestor_clientes import GestorClientes

# Importamos el catalogo de servicios.
from catalogo_servicios import CatalogoServicios

# Importamos las excepciones personalizadas.
from excepciones import ErrorCliente, ErrorValidacion


# Funcion para mostrar las opciones del programa.
def mostrar_menu():

    print("\n===== SOFTWARE FJ =====")
    print("1. Registrar cliente")
    print("2. Consultar clientes")
    print("3. Consultar servicios")
    print("4. Salir")


# Funcion para registrar clientes.
def registrar_cliente(gestor):

    # Solicitamos los datos del cliente.
    codigo = input("Codigo del cliente: ").strip()
    nombre = input("Nombre completo: ").strip()
    correo = input("Correo electronico: ").strip()

    # Intentamos registrar los datos.
    try:
        cliente = gestor.registrar(codigo, nombre, correo)

    # Capturamos los errores de registro.
    except (ErrorCliente, ErrorValidacion) as error:
        print("Error controlado:", error)

    # Si el registro es correcto, mostramos el cliente.
    else:
        print("Cliente registrado correctamente.")
        print(cliente.mostrar_informacion())


# Funcion para consultar los clientes registrados.
def consultar_clientes(gestor):

    # Obtenemos los clientes almacenados.
    clientes = gestor.listar()

    # Verificamos si existen clientes.
    if not clientes:
        print("No hay clientes registrados.")
        return

    # Mostramos la informacion de cada cliente.
    print("\n===== CLIENTES REGISTRADOS =====")

    for cliente in clientes:
        print(cliente.mostrar_informacion())


# Funcion para consultar los servicios.
def consultar_servicios(catalogo):

    # Obtenemos los servicios del catalogo.
    servicios = catalogo.listar()

    # Comprobamos si existen servicios.
    if not servicios:
        print("No hay servicios registrados.")
        return

    # Mostramos el encabezado.
    print("\n===== SERVICIOS DISPONIBLES =====")

    # Recorremos los servicios registrados.
    for servicio in servicios:

        # Aplicamos polimorfismo para describir cada servicio.
        print(servicio.describir_servicio())


# Funcion principal que controla el sistema.
def ejecutar_programa():

    # Creamos el gestor que almacenara clientes.
    gestor = GestorClientes()

    # Creamos el catalogo de servicios.
    catalogo = CatalogoServicios()

    # Mantenemos el programa activo.
    while True:

        # Mostramos el menu principal.
        mostrar_menu()

        # Solicitamos una opcion al usuario.
        opcion = input("Seleccione una opcion: ").strip()

        # Opcion 1: Registrar cliente.
        if opcion == "1":
            registrar_cliente(gestor)

        # Opcion 2: Consultar clientes.
        elif opcion == "2":
            consultar_clientes(gestor)

        # Opcion 3: Consultar servicios.
        elif opcion == "3":
            consultar_servicios(catalogo)

        # Opcion 4: Salir del programa.
        elif opcion == "4":
            print("Gracias por utilizar Software FJ.")
            break

        # Controlamos una opcion incorrecta.
        else:
            print("Opcion no valida. Intente nuevamente.")


# Punto de entrada de la aplicacion.
if __name__ == "__main__":
    ejecutar_programa()
