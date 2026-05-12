<div align="center">
    <h1>🕸️ ESTRUCTURAS DE DATOS: GRAFOS</h1>
    <h3>Proyecto Integrador Unidad 3</h3>
    <p><strong>Implementación del Algoritmo de Dijkstra en Grafos Bidireccionales Pesados</strong></p>
</div>

---

## Descripción del Proyecto

Este proyecto implementa un **grafo bidireccional pesado** con capacidad de encontrar la ruta más rápida entre dos nodos usando el **Algoritmo de Dijkstra**. Está diseñado para aplicaciones de optimización de rutas en sistemas de transporte, redes de comunicación, y otros problemas de camino más corto.

---

## Características Implementadas

 **Grafo Bidireccional**: Conexiones en ambas direcciones
 **Pesos en Minutos**: Cada arista representa tiempo en minutos
 **Algoritmo de Dijkstra**: Encuentra la ruta más corta eficientemente
 **Validación de Entrada**: Verifica nodos válidos y pesos positivos
 **Visualización**: Muestra la estructura completa del grafo
 **Cálculo de Distancias**: Obtiene todas las distancias desde un nodo
 **Interfaz Intuitiva**: Menú fácil de usar

---

## Requisitos

- **C++17** o superior
- Compilador **g++** o compatible
- Sistema operativo: Linux/macOS/Windows

---

## Compilación

```bash
cd T9_Proyecto_Integrador_U3
g++ -std=c++17 -o main main.cpp
```

---

## Ejecución

```bash
./main        # Linux/macOS
main.exe      # Windows
```

---

## Menú de Opciones

```
════════════════════════════════════════
          MENÚ PRINCIPAL
════════════════════════════════════════
1. Agregar nodo
2. Agregar conexión (arista) entre nodos
3. Mostrar estructura del grafo
4. Buscar ruta más rápida (Dijkstra)
5. Mostrar distancias desde un nodo
6. Salir
════════════════════════════════════════
```

---

## Ejemplo de Uso

Consulta el archivo [EJEMPLO_EJECUCION.md](./EJEMPLO_EJECUCION.md) para un ejemplo completo con una red de ciudades.

---

## Estructura del Código

### Clase Principal: `Grafo`

**Métodos principales:**

| Método                 | Descripción                                       |
| ----------------------- | -------------------------------------------------- |
| `agregarArista()`     | Agrega una conexión bidireccional entre dos nodos |
| `dijkstra()`          | Implementa el algoritmo de Dijkstra                |
| `mostrarRuta()`       | Muestra la ruta más corta entre dos nodos         |
| `mostrarDistancias()` | Muestra todas las distancias desde un nodo         |
| `mostrarGrafo()`      | Visualiza la estructura del grafo                  |

### Complejidad Algorítmica

**Tiempo**: O((V + E) log V)
**Espacio**: O(V)

Donde V = vértices, E = aristas

---

## Teoría Implementada

### Algoritmo de Dijkstra

El algoritmo de Dijkstra es un algoritmo voraz que:

1. Inicializa las distancias como infinito excepto el nodo inicial (0)
2. Usa una priority queue para procesar nodos en orden de distancia
3. Para cada nodo, actualiza las distancias de sus vecinos
4. Continúa hasta procesar todos los nodos alcanzables

**Pseudocódigo:**

```
dijkstra(grafo, inicio):
    dist[todos] = ∞
    dist[inicio] = 0
  
    mientras hay nodos no visitados:
        actual = nodo con menor distancia
        para cada vecino de actual:
            si dist[actual] + peso < dist[vecino]:
                actualizar dist[vecino]
```

---

## Aplicaciones Reales

- Sistemas de navegación (Google Maps, Waze)
- Rutas aéreas y transporte
- Redes de comunicación
- Planificación de logística médica
-  Sincronización de redes

---

## Instrucciones Originales

[Descargar PDF](./Tarea_9_Estructura.pdf)

**Requisitos:**

- Aplicar teoría de grafos
- Implementar Algoritmo Dijkstra
- Encontrar la ruta más rápida
- Soporte bidireccional
- Pesos en minutos

---

## Autor

**Bryan Borges**
[GitHub](https://github.com/Bryborj)

**Institución:** Universidad Autónoma de Puebla (BUAP)
**Semestre:** 4to Semestre
**Fecha:** 18 de Marzo de 2026

---

## Licencia

Proyecto académico - Uso educativo

---

## Recursos Adicionales

- Documentación de C++ estándar
- Algoritmo de Dijkstra: [Wikipedia](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
- Teoría de Grafos: Estructura de Datos Avanzadas

---

**Estado:**  Completado
**Última actualización:** 18 de Marzo de 2026
