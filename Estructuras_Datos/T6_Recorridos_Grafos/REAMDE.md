# Practica 6: Recorridos en Grafos (BFS y DFS)

- Autor: Bryan Albino Borges
- Mat: 202423701
- Ing. CS. Computación

**Descripción**: Implementación de un grafo mediante lista de adyacencia y recorridos BFS y DFS (recursivo e iterativo). El programa lee un grafo no dirigido y produce los órdenes de visita desde un vértice inicial.

**Archivo principal**: `Lista_Adyacencia_Grafos.cpp`

**Compilar**:

```bash
g++ -std=c++17 Lista_Adyacencia_Grafos.cpp -o recorridos_grafo
```

**Ejecutar**:

El binario espera la siguiente entrada por stdin:
- Primera línea: `V E` (número de vértices y número de aristas)
- Siguientes `E` líneas: pares `u v` (arista entre `u` y `v`, índices 0-based)
- Última línea: `s` (vértice de inicio para los recorridos)

Ejemplo de entrada:

```
6 7
0 1
0 2
1 3
2 3
3 4
4 5
1 2
0
```

Salida esperada (formato):

```
BFS: 0 1 2 3 4 5
DFS_recursive: 0 1 3 2 4 5
DFS_iterative: 0 2 1 3 4 5
```

Notas:
- Las salidas pueden variar en orden dentro de cada nivel dependiendo del orden de las aristas en la lista de adyacencia.
- El programa usa índices 0-based para vértices. Adapte la entrada si prefiere 1-based.

Si quieres, puedo añadir soporte para grafos dirigidos, cargar desde archivo o pruebas unitarias.
