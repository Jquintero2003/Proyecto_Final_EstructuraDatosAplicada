# ANALISIS.md — DomiRuta Manizales

## Fase 1: listas y recursión

### Complejidad de las listas

| Método | ListaEnlazada | ListaDoble | Por qué |
|---|---|---|---|
| `insertar_inicio` | O(1) | O(1) | Solo se reasigna la cabeza |
| `insertar_final` | O(1) | O(1) | Se mantiene referencia a la cola |
| `insertar_en` | O(n) | O(n) | Hay que recorrer hasta la posición |
| `eliminar` | O(n) | O(n) | Hay que buscar la primera coincidencia |
| `buscar` | O(n) | O(n) | Búsqueda lineal |
| `obtener` | O(n) | O(n) | Recorrido hasta la posición |
| `__len__`, `esta_vacia` | O(1) | O(1) | Contador de tamaño |
| `__str__` | O(n) | O(n) | Recorre toda la lista |
| `imprimir_reversa` | — | O(n) | Recorre con el puntero `anterior` desde la cola |

### Funciones recursivas (`util/recursion.py`)

| Función | Caso base | Caso recursivo | Tipo | Complejidad |
|---|---|---|---|---|
| `sumar_valores` | nodo es `None` → 0 | valor actual + suma del resto | Lineal | O(n) |
| `contar_urgentes` | nodo es `None` → 0 | 1 o 0 + urgentes del resto | Lineal | O(n) |
| `buscar_recursivo` | `None` → False; dato igual → True | buscar en el resto | De cola | O(n) |
| `imprimir_reversa_recursivo` | nodo es `None` → no hace nada | recursión y luego imprime | Lineal | O(n) |
| `invertir_lista` | vacía o un nodo → ese nodo | invertir el resto y re-enlazar | Lineal | O(n) |

### Límite de recursión de Python

Python limita la profundidad de recursión a unas 1 000 llamadas (`sys.getrecursionlimit()`).
Como estas funciones hacen una llamada por nodo, con historiales de más de ~1 000 pedidos
lanzan `RecursionError`. Python tampoco optimiza la recursión de cola, así que
`buscar_recursivo` tiene el mismo límite aunque sea de cola. En la práctica un cliente no
tiene tantos pedidos, pero la versión iterativa no tendría ese límite.
