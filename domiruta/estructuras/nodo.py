"""Nodos enlazados: bloque base de toda la biblioteca de estructuras."""
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class Nodo(Generic[T]):
    """Nodo simple: guarda un dato y la referencia al siguiente nodo."""

    def __init__(self, dato: T, siguiente: Optional["Nodo[T]"] = None) -> None:
        self._dato = dato
        self._siguiente = siguiente

    @property
    def dato(self) -> T:
        """Dato almacenado en el nodo."""
        return self._dato

    @dato.setter
    def dato(self, valor: T) -> None:
        self._dato = valor

    @property
    def siguiente(self) -> Optional["Nodo[T]"]:
        """Nodo siguiente (None si es el último)."""
        return self._siguiente

    @siguiente.setter
    def siguiente(self, nodo: Optional["Nodo[T]"]) -> None:
        self._siguiente = nodo


class NodoDoble(Generic[T]):
    """Nodo doble: dato, referencia al siguiente y al anterior."""

    def __init__(
        self,
        dato: T,
        siguiente: Optional["NodoDoble[T]"] = None,
        anterior: Optional["NodoDoble[T]"] = None,
    ) -> None:
        self._dato = dato
        self._siguiente = siguiente
        self._anterior = anterior

    @property
    def dato(self) -> T:
        """Dato almacenado en el nodo."""
        return self._dato

    @dato.setter
    def dato(self, valor: T) -> None:
        self._dato = valor

    @property
    def siguiente(self) -> Optional["NodoDoble[T]"]:
        """Nodo siguiente (None si es el último)."""
        return self._siguiente

    @siguiente.setter
    def siguiente(self, nodo: Optional["NodoDoble[T]"]) -> None:
        self._siguiente = nodo

    @property
    def anterior(self) -> Optional["NodoDoble[T]"]:
        """Nodo anterior (None si es el primero)."""
        return self._anterior

    @anterior.setter
    def anterior(self, nodo: Optional["NodoDoble[T]"]) -> None:
        self._anterior = nodo
