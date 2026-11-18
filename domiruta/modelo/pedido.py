"""Clase Pedido y su estado."""
from dataclasses import dataclass
from enum import Enum


class EstadoPedido(Enum):
    """Estados posibles de un pedido."""

    EN_ESPERA = "EN_ESPERA"
    ASIGNADO = "ASIGNADO"
    ENTREGADO = "ENTREGADO"
    CANCELADO = "CANCELADO"


@dataclass
class Pedido:
    """Pedido de un cliente de DomiRuta."""

    id: int
    codigo_cliente: int
    descripcion: str
    valor: float
    barrio_destino: str
    urgente: bool = False
    estado: EstadoPedido = EstadoPedido.EN_ESPERA

    def __str__(self) -> str:
        prioridad = "URGENTE" if self.urgente else "normal"
        return (
            f"#{self.id} {self.descripcion} ${self.valor:,.0f} "
            f"-> {self.barrio_destino} [{prioridad}, {self.estado.value}]"
        )
