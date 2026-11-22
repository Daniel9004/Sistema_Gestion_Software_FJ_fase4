
# SOFTWARE FJ
# ARCHIVO: pruebas_finales.py
# DESCRIPCION: Diez pruebas funcionales del sistema.

# Importamos las clases principales.
from gestor_clientes import GestorClientes
from gestor_reservas import GestorReservas
from catalogo_servicios import CatalogoServicios
from reservas import Reserva

# Importamos las excepciones personalizadas.
from excepciones import (
    ErrorCliente,
    ErrorServicio,
    ErrorReserva,
    ErrorValidacion,
    OperacionNoPermitida
)


# Creamos los componentes del sistema.
clientes = GestorClientes()
reservas = GestorReservas()
catalogo = CatalogoServicios()

# Guardaremos los resultados de las pruebas.
resultados = []


# Funcion para ejecutar y evaluar cada prueba.
def comprobar(numero, descripcion, operacion, error_esperado=None):

    try:
        # Ejecutamos la operacion correspondiente.
        operacion()

    except Exception as error:

        # Comprobamos si el error era el esperado.
        if error_esperado and isinstance(error, error_esperado):
            print(f"Prueba {numero}: CORRECTA")
            print("Error controlado:", error)
            resultados.append(True)

        else:
            print(f"Prueba {numero}: FALLIDA")
            print("Error inesperado:", error)
            resultados.append(False)

    else:

        # Si no esperabamos un error, la prueba es correcta.
        if error_esperado is None:
            print(f"Prueba {numero}: CORRECTA")
            resultados.append(True)

        else:
            print(f"Prueba {numero}: FALLIDA")
            print("No se produjo el error esperado.")
            resultados.append(False)

    print("Descripcion:", descripcion)
    print("-" * 45)


# PRUEBA 1: Registrar correctamente un cliente.
comprobar(
    1,
    "Registro correcto de cliente",
    lambda: clientes.registrar(
        "C001", "Juan Perez", "juan@gmail.com"
    )
)


# PRUEBA 2: Intentar registrar un codigo duplicado.
comprobar(
    2,
    "Cliente con codigo duplicado",
    lambda: clientes.registrar(
        "C001", "Maria Lopez", "maria@gmail.com"
    ),
    ErrorCliente
)


# PRUEBA 3: Registrar un correo incorrecto.
comprobar(
    3,
    "Correo electronico invalido",
    lambda: clientes.registrar(
        "C002", "Ana Ruiz", "correo-invalido"
    ),
    ErrorValidacion
)


# PRUEBA 4: Comprobar los tres servicios.
def verificar_catalogo():

    if len(catalogo.listar()) != 3:
        raise AssertionError(
            "El catalogo debe contener tres servicios."
        )


comprobar(
    4,
    "Consulta correcta del catalogo",
    verificar_catalogo
)


# PRUEBA 5: Buscar un servicio inexistente.
comprobar(
    5,
    "Servicio inexistente",
    lambda: catalogo.buscar("Z999"),
    ErrorServicio
)


# PRUEBA 6: Verificar el calculo de una sala.
def verificar_costo():

    costo = catalogo.buscar("S001").calcular_costo(2)

    if costo != 100000:
        raise AssertionError("Costo incorrecto.")


comprobar(
    6,
    "Calculo correcto del costo",
    verificar_costo
)


# PRUEBA 7: Crear y procesar una reserva.
def procesar_reserva():

    cliente = clientes.buscar("C001")
    servicio = catalogo.buscar("S001")

    reserva = Reserva("R001", cliente, servicio, 2)

    reserva.procesar()

    if reserva.estado != "Confirmada":
        raise AssertionError("Reserva no confirmada.")

    if reserva.costo_total != 100000:
        raise AssertionError("Total incorrecto.")

    reservas.agregar(reserva)


comprobar(
    7,
    "Procesamiento correcto de reserva",
    procesar_reserva
)


# PRUEBA 8: Intentar repetir el codigo de reserva.
comprobar(
    8,
    "Codigo de reserva duplicado",
    lambda: reservas.agregar(
        Reserva(
            "R001",
            clientes.buscar("C001"),
            catalogo.buscar("S001"),
            3
        )
    ),
    ErrorReserva
)


# PRUEBA 9: Cancelar correctamente una reserva.
def verificar_cancelacion():

    reserva = reservas.buscar("R001")

    reserva.cancelar()

    if reserva.estado != "Cancelada":
        raise AssertionError("La reserva no fue cancelada.")


comprobar(
    9,
    "Cancelacion correcta de reserva",
    verificar_cancelacion
)


# PRUEBA 10: Intentar cancelar una reserva cancelada.
comprobar(
    10,
    "Cancelacion repetida",
    lambda: reservas.buscar("R001").cancelar(),
    OperacionNoPermitida
)


# Mostramos el resumen de resultados.
print("\n===== RESULTADO FINAL =====")

correctas = sum(resultados)
fallidas = len(resultados) - correctas

print("Pruebas ejecutadas:", len(resultados))
print("Pruebas correctas:", correctas)
print("Pruebas fallidas:", fallidas)

# Verificamos que todas las pruebas pasaron.
if fallidas == 0:
    print("VALIDACION SATISFACTORIA")
else:
    print("SE REQUIEREN CORRECCIONES")

print("El programa sigue funcionando.")
