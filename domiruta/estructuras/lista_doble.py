"""Lista doblemente enlazada (cabeza y cola, con puntero anterior)."""
from typing import Generic, Iterator, Optional, TypeVar

from estructuras.nodo import NodoDoble

T = TypeVar("T")


class ListaDoble(Generic[T]):
    """Lista doblemente enlazada; permite recorrer en ambos sentidos."""

    def __init__(self) -> None:
        self._cabeza: Optional[NodoDoble[T]] = None
        self._cola: Optional[NodoDoble[T]] = None
        self._tamano = 0

    @property
    def cabeza(self) -> Optional[NodoDoble[T]]:
        """Primer nodo de la lista (None si está vacía)."""
        return self._cabeza

    @property
    def cola(self) -> Optional[NodoDoble[T]]:
        """Último nodo de la lista (None si está vacía)."""
        return self._cola

    def insertar_inicio(self, dato: T) -> None:
        """Agrega un dato al inicio."""
        # O(1)
        nuevo = NodoDoble(dato, siguiente=self._cabeza)
        if self._cabeza is None:
            self._cola = nuevo
        else:
            self._cabeza.anterior = nuevo
        self._cabeza = nuevo
        self._tamano += 1

    def insertar_final(self, dato: T) -> None:
        """Agrega un dato al final."""
        # O(1)
        nuevo = NodoDoble(dato, anterior=self._cola)
        if self._cola is None:
            self._cabeza = nuevo
        else:
            self._cola.siguiente = nuevo
        self._cola = nuevo
        self._tamano += 1

    def insertar_en(self, pos: int, dato: T) -> None:
        """Inserta un dato en la posición pos (0 a len). Lanza IndexError si no es válida."""
        # O(n)
        if pos < 0 or pos > self._tamano:
            raise IndexError("Posición fuera de rango")
        if pos == 0:
            self.insertar_inicio(dato)
        elif pos == self._tamano:
            self.insertar_final(dato)
        else:
            siguiente = self._nodo_en(pos)
            previo = siguiente.anterior
            nuevo = NodoDoble(dato, siguiente=siguiente, anterior=previo)
            siguiente.anterior = nuevo
            if previo is not None:
                previo.siguiente = nuevo
            self._tamano += 1

    def eliminar(self, dato: T) -> bool:
        """Elimina la primera coincidencia. Retorna True si eliminó algo."""
        # O(n)
        actual = self._cabeza
        while actual is not None:
            if actual.dato == dato:
                if actual.anterior is None:
                    self._cabeza = actual.siguiente
                else:
                    actual.anterior.siguiente = actual.siguiente
                if actual.siguiente is None:
                    self._cola = actual.anterior
                else:
                    actual.siguiente.anterior = actual.anterior
                self._tamano -= 1
                return True
            actual = actual.siguiente
        return False

    def buscar(self, dato: T) -> int:
        """Retorna la posición de la primera coincidencia o -1 si no existe."""
        # O(n)
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
        # O(n)
        if pos < 0 or pos >= self._tamano:
            raise IndexError("Posición fuera de rango")
        return self._nodo_en(pos).dato

    def esta_vacia(self) -> bool:
        """Indica si la lista no tiene elementos."""
        # O(1)
        return self._tamano == 0

    def texto_reversa(self) -> str:
        """Retorna el texto de la lista de la cola a la cabeza."""
        # O(n): recorre con el puntero anterior.
        if self._cola is None:
            return "(vacía)"
        texto = ""
        actual = self._cola
        while actual is not None:
            texto += str(actual.dato)
            if actual.anterior is not None:
                texto += " <-> "
            actual = actual.anterior
        return texto

    def imprimir_reversa(self) -> None:
        """Imprime la lista del último al primero (del más reciente al más antiguo)."""
        # O(n)
        print(self.texto_reversa())

    def _nodo_en(self, pos: int) -> NodoDoble[T]:
        # O(n): recorre desde la cabeza (pos ya validada).
        actual = self._cabeza
        for _ in range(pos):
            actual = actual.siguiente  # type: ignore[union-attr]
        return actual  # type: ignore[return-value]

    def __iter__(self) -> Iterator[T]:
        # O(n) en total
        actual = self._cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente

    def __len__(self) -> int:
        # O(1)
        return self._tamano

    def __str__(self) -> str:
        # O(n)
        if self._cabeza is None:
            return "(vacía)"
        texto = ""
        actual = self._cabeza
        while actual is not None:
            texto += str(actual.dato)
            if actual.siguiente is not None:
                texto += " <-> "
            actual = actual.siguiente
        return texto
