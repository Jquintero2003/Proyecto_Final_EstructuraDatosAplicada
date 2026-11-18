"""Casos de prueba mínimos. Ejecutar con: python pruebas.py"""
import io
import unittest
from contextlib import redirect_stdout

from estructuras.lista_doble import ListaDoble
from estructuras.lista_enlazada import ListaEnlazada
from modelo.cliente import Cliente
from modelo.pedido import Pedido
from util.recursion import (
    buscar_recursivo,
    contar_urgentes,
    imprimir_reversa_recursivo,
    invertir_lista,
    sumar_valores,
)


def _texto_desde(nodo) -> str:
    """Recorre nodos y arma el texto 'a -> b -> c' (ayuda para las pruebas)."""
    texto = ""
    while nodo is not None:
        texto += str(nodo.dato)
        if nodo.siguiente is not None:
            texto += " -> "
        nodo = nodo.siguiente
    return texto


def _pedido(id_: int, valor: float, urgente: bool = False) -> Pedido:
    return Pedido(id_, 1, "prueba", valor, "Centro", urgente)


class PruebasFase1(unittest.TestCase):
    # ---- Casos mínimos del enunciado ----
    def test_01_eliminar_de_lista_vacia(self):
        lista = ListaEnlazada()
        self.assertFalse(lista.eliminar(5))

    def test_02_invertir_recursivamente(self):
        lista = ListaEnlazada()
        for n in range(1, 5):
            lista.insertar_final(n)
        nueva_cabeza = invertir_lista(lista.cabeza)
        self.assertEqual(_texto_desde(nueva_cabeza), "4 -> 3 -> 2 -> 1")

    # ---- Lista simple ----
    def test_insertar_y_orden(self):
        lista = ListaEnlazada()
        lista.insertar_final(2)
        lista.insertar_inicio(1)
        lista.insertar_final(4)
        lista.insertar_en(2, 3)
        self.assertEqual(str(lista), "1 -> 2 -> 3 -> 4")
        self.assertEqual(len(lista), 4)

    def test_buscar_obtener_y_errores(self):
        lista = ListaEnlazada()
        lista.insertar_final("a")
        lista.insertar_final("b")
        self.assertEqual(lista.buscar("b"), 1)
        self.assertEqual(lista.buscar("z"), -1)
        self.assertEqual(lista.obtener(0), "a")
        with self.assertRaises(IndexError):
            lista.obtener(2)
        with self.assertRaises(IndexError):
            lista.insertar_en(5, "x")

    def test_eliminar_cola_actualiza_referencia(self):
        lista = ListaEnlazada()
        lista.insertar_final(1)
        lista.insertar_final(2)
        self.assertTrue(lista.eliminar(2))
        lista.insertar_final(3)  # si la cola quedó mal, esto se pierde
        self.assertEqual(str(lista), "1 -> 3")

    # ---- Lista doble ----
    def test_lista_doble_reversa_y_eliminar(self):
        lista = ListaDoble()
        for n in range(1, 5):
            lista.insertar_final(n)
        self.assertEqual(lista.texto_reversa(), "4 <-> 3 <-> 2 <-> 1")
        self.assertTrue(lista.eliminar(4))
        self.assertTrue(lista.eliminar(1))
        self.assertEqual(str(lista), "2 <-> 3")
        self.assertEqual(lista.texto_reversa(), "3 <-> 2")
        self.assertFalse(ListaDoble().eliminar(1))

    def test_lista_doble_insertar_en(self):
        lista = ListaDoble()
        lista.insertar_final(1)
        lista.insertar_final(3)
        lista.insertar_en(1, 2)
        self.assertEqual(str(lista), "1 <-> 2 <-> 3")
        self.assertEqual(lista.texto_reversa(), "3 <-> 2 <-> 1")

    # ---- Recursión ----
    def test_sumar_y_contar(self):
        historial = ListaDoble()
        historial.insertar_final(_pedido(1, 10000, True))
        historial.insertar_final(_pedido(2, 5000))
        historial.insertar_final(_pedido(3, 7500, True))
        self.assertEqual(sumar_valores(historial.cabeza), 22500)
        self.assertEqual(contar_urgentes(historial.cabeza), 2)
        self.assertEqual(sumar_valores(None), 0)

    def test_buscar_recursivo(self):
        lista = ListaEnlazada()
        lista.insertar_final(7)
        lista.insertar_final(8)
        self.assertTrue(buscar_recursivo(lista.cabeza, 8))
        self.assertFalse(buscar_recursivo(lista.cabeza, 9))

    def test_imprimir_reversa_recursivo(self):
        lista = ListaEnlazada()
        for n in range(1, 4):
            lista.insertar_final(n)
        salida = io.StringIO()
        with redirect_stdout(salida):
            imprimir_reversa_recursivo(lista.cabeza)
        self.assertEqual(salida.getvalue(), "3\n2\n1\n")

    # ---- Modelo ----
    def test_cliente_se_compara_por_codigo(self):
        self.assertEqual(Cliente(5, "Ana", "300", "Centro"), Cliente(5, "Otro", "1", "X"))
        self.assertTrue(Cliente(1, "A", "1", "X") < Cliente(2, "B", "2", "Y"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
