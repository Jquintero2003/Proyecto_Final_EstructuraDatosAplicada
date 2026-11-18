"""Clase Operacion: registro de una acción del operador (para deshacer)."""
from dataclasses import dataclass
from typing import Any


@dataclass
class Operacion:
    """Operación realizada: tipo, dato afectado y su estado anterior."""

    tipo: str
    dato_afectado: Any
    estado_anterior: Any
