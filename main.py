
# SOFTWARE FJ
# ARCHIVO: main.py
# DESCRIPCION: Menu principal de clientes, servicios y reservas.

# Importamos los gestores del sistema.
from gestor_clientes import GestorClientes
from gestor_reservas import GestorReservas

# Importamos el catalogo de servicios.
from catalogo_servicios import CatalogoServicios

# Importamos la clase Reserva.
from reservas import Reserva

# Importamos las excepciones personalizadas.
from excepciones import (
    ErrorCliente,
    ErrorServicio,
    ErrorReserva,
    ErrorValidacion,
    ServicioNoDisponible,
    OperacionNoPermitida
)

# Importamos math para validar la duracion.
import math


# Funcion que muestra las opciones del menu.
def mostrar_menu():

    print("\n===== SOFTWARE FJ =====")
    print("1. Registrar cliente")
    print("2. Consultar clientes")
    print("3. Consultar servicios")
    print("4. Crear y procesar reserva")
    print("5. Cancelar reserva")
    print("6. Consultar reservas")
    print("7. Salir")


# Funcion encargada de registrar clientes.
def registrar_cliente(gestor):

    # Solicitamos los datos del nuevo cliente.
    codigo = input("Codigo del cliente: ").strip()
    nombre = input("Nombre completo: ").strip()
    correo = input("Correo electronico: ").strip()

    try:
        # Registramos el cliente en memoria.
        cliente = gestor.registrar(codigo, nombre, correo)

    # Capturamos errores de registro.
    except (ErrorCliente, ErrorValidacion) as error:
        print("Error controlado:", error)

    else:
        # Mostramos el resultado correcto.
        print("Cliente registrado correctamente.")
        print(cliente.mostrar_informacion())


# Funcion para consultar clientes.
def consultar_clientes(gestor):

    # Obtenemos los clientes existentes.
    clientes = gestor.listar()

    # Comprobamos si la lista esta vacia.
    if not clientes:
        print("No hay clientes registrados.")
        return

    print("\n===== CLIENTES REGISTRADOS =====")

    # Mostramos cada cliente.
    for cliente in clientes:
        print(cliente.mostrar_informacion())


# Funcion para consultar los servicios del sistema.
def consultar_servicios(catalogo):

    # Obtenemos los servicios existentes.
    servicios = catalogo.listar()

    # Comprobamos si existen servicios.
    if not servicios:
        print("No hay servicios registrados.")
        return

    print("\n===== SERVICIOS DEL SISTEMA =====")

    # Aplicamos polimorfismo con cada servicio.
    for servicio in servicios:
        print(servicio.describir_servicio())


# Funcion para crear y procesar una reserva.
def crear_reserva(clientes, catalogo, reservas):

    print("\n===== CREAR RESERVA =====")

    # Solicitamos los datos necesarios.
    codigo = input("Codigo de reserva: ").strip()
    codigo_cliente = input("Codigo del cliente: ").strip()
    codigo_servicio = input("Codigo del servicio: ").strip()
    texto_duracion = input("Duracion en horas: ").strip()

    try:
        # Convertimos la duracion a numero.
        duracion = float(texto_duracion)

        # Rechazamos valores infinitos o NaN.
        if not math.isfinite(duracion):
            raise ValueError("Duracion no valida.")

        # Buscamos el cliente registrado.
        cliente = clientes.buscar(codigo_cliente)

        # Buscamos el servicio solicitado.
        servicio = catalogo.buscar(codigo_servicio)

        # Comprobamos si el codigo ya esta utilizado.
        for existente in reservas.listar():

            if existente.codigo == codigo:
                raise ErrorReserva(
                    "Ya existe una reserva con ese codigo."
                )

        # Creamos la reserva con objetos reales.
        nueva_reserva = Reserva(
            codigo, cliente, servicio, duracion
        )

        # Procesamos y calculamos el costo.
        resultado = nueva_reserva.procesar()

        # Guardamos la reserva confirmada.
        reservas.agregar(nueva_reserva)

    # Controlamos errores numericos.
    except ValueError:
        print("Error controlado: duracion numerica no valida.")

    # Controlamos las excepciones personalizadas.
    except (
        ErrorCliente,
        ErrorServicio,
        ErrorReserva,
        ErrorValidacion,
        ServicioNoDisponible,
        OperacionNoPermitida
    ) as error:
        print("Error controlado:", error)

    else:
        # Mostramos la confirmacion.
        print(resultado)
        print("Estado:", nueva_reserva.estado)


# Funcion para cancelar una reserva registrada.
def cancelar_reserva(gestor):

    print("\n===== CANCELAR RESERVA =====")

    # Solicitamos el codigo de la reserva.
    codigo = input("Codigo de reserva: ").strip()

    try:
        # Buscamos la reserva existente.
        reserva = gestor.buscar(codigo)

        # Ejecutamos el metodo de cancelacion.
        mensaje = reserva.cancelar()

    # Controlamos reservas inexistentes o ya canceladas.
    except (ErrorReserva, OperacionNoPermitida) as error:
        print("Error controlado:", error)

    else:
        # Mostramos el resultado correcto.
        print(mensaje)
        print("Estado actual:", reserva.estado)


# Funcion para consultar todas las reservas.
def consultar_reservas(gestor):

    print("\n===== RESERVAS REGISTRADAS =====")

    # Obtenemos todas las reservas almacenadas.
    reservas = gestor.listar()

    # Comprobamos si existen reservas.
    if not reservas:
        print("No hay reservas registradas.")
        return

    # Recorremos cada reserva.
    for reserva in reservas:

        # Mostramos los datos principales.
        print("\nCodigo:", reserva.codigo)
        print("Cliente:", reserva.cliente.nombre)
        print("Servicio:", reserva.servicio.describir_servicio())
        print("Duracion:", reserva.duracion, "horas")
        print("Estado:", reserva.estado)

        # Mostramos el costo si ya fue calculado.
        if hasattr(reserva, "costo_total"):
            print(f"Costo total: ${reserva.costo_total:.2f}")
        else:
            print("Costo total: pendiente de calcular")


# Funcion principal que controla el programa.
def ejecutar_programa():

    # Creamos los gestores y el catalogo.
    gestor_clientes = GestorClientes()
    gestor_reservas = GestorReservas()
    catalogo = CatalogoServicios()

    # Repetimos el menu hasta seleccionar salir.
    while True:

        # Mostramos las opciones disponibles.
        mostrar_menu()

        # Solicitamos la opcion.
        opcion = input("Seleccione una opcion: ").strip()

        # Registrar clientes.
        if opcion == "1":
            registrar_cliente(gestor_clientes)

        # Consultar clientes.
        elif opcion == "2":
            consultar_clientes(gestor_clientes)

        # Consultar servicios.
        elif opcion == "3":
            consultar_servicios(catalogo)

        # Crear y procesar reservas.
        elif opcion == "4":
            crear_reserva(
                gestor_clientes,
                catalogo,
                gestor_reservas
            )

        # Cancelar una reserva existente.
        elif opcion == "5":
            cancelar_reserva(gestor_reservas)

        # Consultar todas las reservas.
        elif opcion == "6":
            consultar_reservas(gestor_reservas)

        # Finalizar el programa.
        elif opcion == "7":
            print("Gracias por utilizar Software FJ.")
            break

        # Controlar opciones incorrectas.
        else:
            print("Opcion no valida. Intente nuevamente.")


# Punto de entrada del programa.
if __name__ == "__main__":
    ejecutar_programa()
