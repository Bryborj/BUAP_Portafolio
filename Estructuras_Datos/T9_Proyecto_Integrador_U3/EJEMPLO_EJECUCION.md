# Proyecto Integrador Unidad 3 - Ejecutable y Ejemplos

## Descripción del Proyecto

Este es un **Proyecto Integrador de Estructuras de Datos** que implementa un **Grafo Bidireccional Pesado** con el **Algoritmo de Dijkstra** para encontrar la ruta más rápida entre dos nodos.

### Características Principales

 **Grafo Bidireccional**: Las conexiones funcionan en ambas direcciones
**Pesos en Minutos**: Cada arista tiene un peso que representa el tiempo en minutos
**Algoritmo de Dijkstra**: Encuentra la ruta más corta entre dos nodos
**Anterfaz Intuitiva**: Menú amigable para navegar
 **Visualización**: Muestra la estructura completa del grafo

---

## Cómo Compilar

```bash
cd T9_Proyecto_Integrador_U3
g++ -std=c++17 -o main main.cpp
```

## Cómo Ejecutar

```bash
./main
```

---

## Ejemplo de Uso

### Caso de Uso: Red de Transporte Urbano

Supongamos una red de ciudades conectadas:

```
     5min         3min       7min
Oslo -------- Stockholm ------- Helsinki
     |              |
   2min           4min
     |              |
 Bergen --------- Malmö
        8min
```

### Pasos en la Ejecución:

1. **Crear nodos**:

   - Opción 1: Agregar nodo "Oslo"
   - Opción 1: Agregar nodo "Stockholm"
   - Opción 1: Agregar nodo "Helsinki"
   - Opción 1: Agregar nodo "Bergen"
   - Opción 1: Agregar nodo "Malmö"
2. **Agregar conexiones** (Opción 2):

   - Oslo ↔ Stockholm: 5 minutos
   - Stockholm ↔ Helsinki: 3 minutos
   - Stockholm ↔ Malmö: 4 minutos
   - Oslo ↔ Bergen: 2 minutos
   - Bergen ↔ Malmö: 8 minutos
3. **Visualizar el grafo** (Opción 3):

   ```
   === Estructura del Grafo ===
   Oslo -> Stockholm (5 min), Bergen (2 min)
   Stockholm -> Oslo (5 min), Helsinki (3 min), Malmö (4 min)
   Helsinki -> Stockholm (3 min)
   Bergen -> Oslo (2 min), Malmö (8 min)
   Malmö -> Stockholm (4 min), Bergen (8 min)
   ```
4. **Buscar ruta más rápida** (Opción 4):

   - De: "Oslo"
   - A: "Helsinki"

   **Resultado**:

   ```
   === Ruta más rápida de Oslo a Helsinki ===
   Ruta: Oslo -> Stockholm -> Helsinki
   Tiempo total: 8 minutos
   ```
5. **Mostrar todas las distancias** (Opción 5):

   - Desde: "Oslo"

   **Resultado**:

   ```
   === Distancias desde Oslo ===
   Oslo: 0 minutos
   Stockholm: 5 minutos
   Helsinki: 8 minutos
   Bergen: 2 minutos
   Malmö: 9 minutos
   ```

---

## Menú Principal

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

## Implementación Técnica

### Clase Grafo

La clase `Grafo` implementa:

1. **Destructor de Dijkstra**:

   ```cpp
   pair<map<string, int>, map<string, string>> dijkstra(const string& inicio)
   ```

   - Calcula las distancias más cortas desde un nodo de inicio
   - Retorna un mapa de distancias y un mapa de padres para reconstruir rutas
2. **Agregar Arista Bidireccional**:

   ```cpp
   void agregarArista(const string& nodo1, const string& nodo2, int peso)
   ```

   - Agrega la conexión en ambas direcciones
3. **Mostrar Ruta**:

   ```cpp
   void mostrarRuta(const string& inicio, const string& fin)
   ```

   - Muestra la ruta más corta y el tiempo total
4. **Mostrar Distancias**:

   ```cpp
   void mostrarDistancias(const string& nodo)
   ```

   - Muestra todas las distancias desde un nodo

---

## Complejidad Algorítmica

**Algoritmo de Dijkstra**:

- **Tiempo**: O((V + E) log V) usando priority_queue
- **Espacio**: O(V) para almacenar distancias y padres

Donde:

- V = número de vértices (nodos)
- E = número de aristas (conexiones)

---

## Requisitos

- C++17 o superior
- Compilador g++ o compatible

---

## Autor

**Bryan Borges**
Universidad Autónoma de Puebla (BUAP)
Periodo: 4to Semestre

---

## Notas Importantes

 El programa utiliza `priority_queue` para una ejecución eficiente
 Los pesos deben ser números positivos
 El grafo soporta nodos desconectados
 Las distancias inalcanzables se muestran como "Inalcanzable"

---

**Última actualización**: 18 de Marzo de 2026
