"""Lista enlazada simple con referencia a la cola."""
from typing import Generic, Iterator, Optional, TypeVar

from estructuras.nodo import Nodo

T = TypeVar("T")


class ListaEnlazada(Generic[T]):
    """Lista enlazada simple construida con nodos (sin colecciones de Python)."""

    def __init__(self) -> None:
        self._cabeza: Optional[Nodo[T]] = None
        self._cola: Optional[Nodo[T]] = None
        self._tamano = 0

    @property
    def cabeza(self) -> Optional[Nodo[T]]:
        """Primer nodo de la lista (None si está vacía)."""
        return self._cabeza

    def insertar_inicio(self, dato: T) -> None:
        """Agrega un dato al inicio."""
        # O(1): solo se reasigna la cabeza.
        nuevo = Nodo(dato, self._cabeza)
        self._cabeza = nuevo
        if self._cola is None:
            self._cola = nuevo
        self._tamano += 1

    def insertar_final(self, dato: T) -> None:
        """Agrega un dato al final usando la referencia a la cola."""
        # O(1): la cola evita recorrer la lista.
        nuevo = Nodo(dato)
        if self._cola is None:
            self._cabeza = nuevo
        else:
            self._cola.siguiente = nuevo
        self._cola = nuevo
        self._tamano += 1

    def insertar_en(self, pos: int, dato: T) -> None:
        """Inserta un dato en la posición pos (0 a len). Lanza IndexError si no es válida."""
        # O(n): hay que recorrer hasta la posición anterior.
        if pos < 0 or pos > self._tamano:
            raise IndexError("Posición fuera de rango")
        if pos == 0:
            self.insertar_inicio(dato)
        elif pos == self._tamano:
            self.insertar_final(dato)
        else:
            previo = self._nodo_en(pos - 1)
            previo.siguiente = Nodo(dato, previo.siguiente)
            self._tamano += 1

    def eliminar(self, dato: T) -> bool:
        """Elimina la primera coincidencia. Retorna True si eliminó algo."""
        # O(n): puede requerir recorrer toda la lista.
        previo: Optional[Nodo[T]] = None
        actual = self._cabeza
        while actual is not None:
            if actual.dato == dato:
                if previo is None:
                    self._cabeza = actual.siguiente
                else:
                    previo.siguiente = actual.siguiente
                if actual is self._cola:
                    self._cola = previo
                self._tamano -= 1
                return True
            previo = actual
            actual = actual.siguiente
        return False

    def buscar(self, dato: T) -> int:
        """Retorna la posición de la primera coincidencia o -1 si no existe."""
        # O(n): búsqueda lineal.
        actual = self._cabeza
        pos = 0
        while actual is not None:
            if actual.dato == dato:
                return pos
            actual = actual.siguiente
            pos += 1
        return -1

    def obtener(self, pos: int) -> T:
        """Retorna el dato en la posición pos. Lanza IndexError si no es válida."""
        # O(n): recorre hasta la posición.
        if pos < 0 or pos >= self._tamano:
            raise IndexError("Posición fuera de rango")
        return self._nodo_en(pos).dato

    def esta_vacia(self) -> bool:
        """Indica si la lista no tiene elementos."""
        # O(1)
        return self._tamano == 0

    def _nodo_en(self, pos: int) -> Nodo[T]:
        # O(n): recorre desde la cabeza (pos ya validada).
        actual = self._cabeza
        for _ in range(pos):
            actual = actual.siguiente  # type: ignore[union-attr]
        return actual  # type: ignore[return-value]

    def __iter__(self) -> Iterator[T]:
        # O(n) en total: recorre la lista de cabeza a cola.
        actual = self._cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente

    def __len__(self) -> int:
        # O(1): el tamaño se mantiene como contador.
        return self._tamano

    def __str__(self) -> str:
        # O(n): recorre la lista para armar el texto.
        if self._cabeza is None:
            return "(vacía)"
        texto = ""
        actual = self._cabeza
        while actual is not None:
            texto += str(actual.dato)
            if actual.siguiente is not None:
                texto += " -> "
            actual = actual.siguiente
        return texto
