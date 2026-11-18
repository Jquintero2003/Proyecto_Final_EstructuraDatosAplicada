"""Funciones recursivas sobre listas enlazadas (sin ciclos).

Nota: Python limita la recursión a ~1000 llamadas (sys.getrecursionlimit()),
por eso estas funciones fallan con RecursionError en listas muy largas.
"""
from typing import Any, Optional, Union

from estructuras.nodo import Nodo, NodoDoble

NodoCualquiera = Union[Nodo[Any], NodoDoble[Any], None]


def sumar_valores(nodo: NodoCualquiera) -> float:
    """Suma el valor de todos los pedidos desde el nodo dado."""
    # Recursión lineal (no de cola): queda una suma pendiente tras cada llamada. O(n)
    if nodo is None:  # caso base: lista vacía o fin de la lista
        return 0.0
    # caso recursivo: valor actual + suma del resto
    return nodo.dato.valor + sumar_valores(nodo.siguiente)


def contar_urgentes(nodo: NodoCualquiera) -> int:
    """Cuenta los pedidos urgentes desde el nodo dado."""
    # Recursión lineal (no de cola): queda una suma pendiente. O(n)
    if nodo is None:  # caso base
        return 0
    # caso recursivo: 1 si el actual es urgente + urgentes del resto
    actual = 1 if nodo.dato.urgente else 0
    return actual + contar_urgentes(nodo.siguiente)


def buscar_recursivo(nodo: NodoCualquiera, dato: Any) -> bool:
    """Indica si el dato está en la lista a partir del nodo dado."""
    # Recursión de cola: la llamada recursiva es lo último que se hace. O(n)
    if nodo is None:  # caso base: se acabó la lista sin encontrarlo
        return False
    if nodo.dato == dato:  # caso base: encontrado
        return True
    return buscar_recursivo(nodo.siguiente, dato)  # caso recursivo


def imprimir_reversa_recursivo(nodo: Optional[Nodo[Any]]) -> None:
    """Imprime una lista simple al revés (un dato por línea), sin lista doble."""
    # Recursión lineal (no de cola): primero se recorre el resto y luego se imprime. O(n)
    if nodo is None:  # caso base
        return
    imprimir_reversa_recursivo(nodo.siguiente)  # caso recursivo: primero el resto
    print(nodo.dato)  # al regresar de la recursión se imprime el actual


def invertir_lista(nodo: Optional[Nodo[Any]]) -> Optional[Nodo[Any]]:
    """Invierte físicamente la lista simple y retorna la nueva cabeza."""
    # Recursión lineal (no de cola): se re-enlaza después de la llamada. O(n)
    if nodo is None or nodo.siguiente is None:  # caso base: vacía o un solo nodo
        return nodo
    nueva_cabeza = invertir_lista(nodo.siguiente)  # caso recursivo: invertir el resto
    nodo.siguiente.siguiente = nodo  # el siguiente ahora apunta de vuelta al actual
    nodo.siguiente = None  # el actual pasa a ser el último
    return nueva_cabeza
