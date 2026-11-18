"""DomiRuta Manizales - menú principal (Fase 1: listas y recursión)."""
import unittest

from estructuras.lista_enlazada import ListaEnlazada
from modelo.cliente import Cliente
from modelo.pedido import Pedido
from util.recursion import contar_urgentes, sumar_valores

# Fase 1: los clientes viven temporalmente en una lista enlazada (luego, tabla hash).
clientes: ListaEnlazada[Cliente] = ListaEnlazada()
_siguiente_id_pedido = 1


def leer_entero(mensaje: str) -> int:
    """Pide un entero por consola hasta que sea válido."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Ingrese un número entero válido.")


def leer_decimal(mensaje: str) -> float:
    """Pide un número decimal por consola hasta que sea válido."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Ingrese un número válido.")


def buscar_cliente(codigo: int) -> Cliente | None:
    """Busca un cliente por código con búsqueda lineal."""
    pos = clientes.buscar(Cliente(codigo, "", "", ""))
    return None if pos == -1 else clientes.obtener(pos)


def registrar_cliente() -> None:
    codigo = leer_entero("Código: ")
    if buscar_cliente(codigo) is not None:
        print("Ya existe un cliente con ese código.")
        return
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    barrio = input("Barrio: ")
    clientes.insertar_final(Cliente(codigo, nombre, telefono, barrio))
    print("Cliente registrado.")


def crear_pedido() -> None:
    global _siguiente_id_pedido
    cliente = buscar_cliente(leer_entero("Código del cliente: "))
    if cliente is None:
        print("Cliente no encontrado.")
        return
    descripcion = input("Descripción: ")
    valor = leer_decimal("Valor: ")
    barrio = input("Barrio destino: ")
    urgente = input("¿Urgente? (s/n): ").strip().lower() == "s"
    pedido = Pedido(_siguiente_id_pedido, cliente.codigo, descripcion, valor, barrio, urgente)
    _siguiente_id_pedido += 1
    cliente.agregar_pedido(pedido)
    print(f"Pedido creado: {pedido}")


def ver_historial() -> None:
    cliente = buscar_cliente(leer_entero("Código del cliente: "))
    if cliente is None:
        print("Cliente no encontrado.")
        return
    print(f"Historial de {cliente.nombre}")
    print("Orden normal (antiguo -> reciente):")
    for pedido in cliente.historial:
        print("  ", pedido)
    print("Orden reverso (reciente -> antiguo):")
    cliente.historial.imprimir_reversa()
    print(f"Total de pedidos: ${sumar_valores(cliente.historial.cabeza):,.0f}")
    print(f"Pedidos urgentes: {contar_urgentes(cliente.historial.cabeza)}")


def ejecutar_pruebas() -> None:
    import pruebas

    suite = unittest.defaultTestLoader.loadTestsFromModule(pruebas)
    unittest.TextTestRunner(verbosity=2).run(suite)


def menu() -> None:
    opciones = (
        "\n=== DomiRuta Manizales ===\n"
        "1. Registrar cliente\n"
        "2. Crear pedido\n"
        "3. Ver historial de un cliente\n"
        "4. Ejecutar pruebas\n"
        "0. Salir\n"
        "Opción: "
    )
    while True:
        opcion = input(opciones).strip()
        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            crear_pedido()
        elif opcion == "3":
            ver_historial()
        elif opcion == "4":
            ejecutar_pruebas()
        elif opcion == "0":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
