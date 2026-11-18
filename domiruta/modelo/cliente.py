"""Clase Cliente."""
from dataclasses import dataclass, field

from estructuras.lista_doble import ListaDoble
from modelo.pedido import Pedido


@dataclass(order=True)
class Cliente:
    """Cliente de DomiRuta. Se compara y ordena solo por su código."""

    codigo: int
    nombre: str = field(compare=False)
    telefono: str = field(compare=False)
    barrio: str = field(compare=False)
    historial: ListaDoble[Pedido] = field(
        default_factory=ListaDoble, compare=False, repr=False
    )

    def agregar_pedido(self, pedido: Pedido) -> None:
        """Agrega un pedido al historial del cliente."""
        # O(1): se inserta al final de la lista doble.
        self.historial.insertar_final(pedido)

    def __str__(self) -> str:
        return f"[{self.codigo}] {self.nombre} - {self.telefono} ({self.barrio})"
