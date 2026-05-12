# Documentación Técnica - Proyecto Integrador T9

## Análisis de la Implementación

### 1. Estructura de Datos

#### Grafo como Lista de Adyacencia

```cpp
unordered_map<string, vector<pair<string, int>>> adyacencia;
```

**Advantages:**

-  Acceso O(1) a los vecinos de un nodo
- Eficiente en memoria para grafos dispersos
- Soporta pesos (segundo elemento del par)

**Structure:**

```
Berlin ──> [(Paris, 8), (Amsterdam, 5), (Munich, 7)]
Paris  ──> [(Berlin, 8), (Zurich, 6)]
Amsterdam ──> [(Berlin, 5), (Munich, 4)]
...
```

---

### 2. Algoritmo de Dijkstra - Implementación

#### Pseudocódigo Usado

```
DIJKSTRA(Graph, source)
    distance[source] ← 0
    distance[v] ← ∞ for all v ≠ source
  
    PriorityQueue Q
    Q.insert(source, 0)
  
    while Q not empty:
        u ← Q.extractMin()
      
        for each edge (u, v) with weight w:
            if distance[u] + w < distance[v]:
                distance[v] ← distance[u] + w
                parent[v] ← u
                Q.insert(v, distance[v])
  
    return (distance, parent)
```

#### Complejidad

| Aspecto              | Complejidad      | Detalles                                  |
| -------------------- | ---------------- | ----------------------------------------- |
| **Tiempo**     | O((V + E) log V) | V extracciones de cola, E actualizaciones |
| **Espacio**    | O(V)             | Almacenamiento de distancias y padres     |
| **Mejor Caso** | O(V log V)       | Grafo muy denso                           |
| **Peor Caso**  | O(E log V)       | Muchas actualizaciones de distancias      |

---

### 3. Funcionalidades Principales

#### A. Agregar Arista Bidireccional

```cpp
void agregarArista(const string& nodo1, const string& nodo2, int peso) {
    adyacencia[nodo1].push_back({nodo2, peso});
    adyacencia[nodo2].push_back({nodo1, peso});
}
```

**Características:**

- Agrega ambas direcciones automáticamente
- Crea nodos si no existen
- Soporta múltiples aristas entre mismos nodos (no hay validación de duplicados)

**Ejemplo:**

```
Input: agregarArista("Berlin", "Paris", 8)
Result: Berlin ↔ Paris (8 min)
```

---

#### B. Algoritmo de Dijkstra

```cpp
pair<map<string, int>, map<string, string>> dijkstra(const string& inicio)
```

**Pasos:**

1. Inicializar todas las distancias a infinito
2. Establecer distancia del nodo inicial a 0
3. Insertar (0, inicio) en priority queue
4. Mientras la cola no está vacía:
   - Extraer nodo con menor distancia
   - Para cada vecino, actualizar distancia si es mejor
5. Retornar mapas de distancias y padres

**Ejemplo de ejecución:**

```
Inicio: Berlin
Distancia inicial: {Berlin: 0, Paris: ∞, Amsterdam: ∞, Munich: ∞, Zurich: ∞}

Iteración 1 - Procesar Berlin (dist=0):
  - Berlin→Paris: 0+8=8 < ∞ ✓ Actualizar
  - Berlin→Amsterdam: 0+5=5 < ∞ ✓ Actualizar
  - Berlin→Munich: 0+7=7 < ∞ ✓ Actualizar
  Distancias: {Berlin: 0, Paris: 8, Amsterdam: 5, Munich: 7, Zurich: ∞}

Iteración 2 - Procesar Amsterdam (dist=5):
  - Amsterdam→Munich: 5+4=9 > 7 ✗ No actualizar
  Distancias sin cambios

Iteración 3 - Procesar Munich (dist=7):
  - Munich→Zurich: 7+? = ?
  ... (continuar)
```

---

#### C. Reconstrucción de Ruta

```cpp
void mostrarRuta(const string& inicio, const string& fin) {
    auto [distancias, padres] = dijkstra(inicio);
  
    // Reconstruir ruta usando padres
    vector<string> ruta;
    string actual = fin;
  
    while (!actual.empty()) {
        ruta.push_back(actual);
        actual = padres[actual];
    }
  
    reverse(ruta.begin(), ruta.end());
    // Mostrar ruta
}
```

**Ejemplo:**

```
Padres: {Zurich: Munich, Munich: Berlin, Berlin: "", ...}

Reconstrucción de Zurich:
  actual = Zurich → ruta = [Zurich]
  actual = padres[Zurich] = Munich → ruta = [Zurich, Munich]
  actual = padres[Munich] = Berlin → ruta = [Zurich, Munich, Berlin]
  actual = padres[Berlin] = "" → STOP

Invertir: [Berlin, Munich, Zurich]
```

---

### 4. Validaciones e Edge Cases

#### Validaciones Implementadas

1. **Nodos válidos:**

   ```cpp
   if (!existeNodo(inicio) || !existeNodo(fin)) {
       cout << "Error: Uno o ambos nodos no existen.\n";
       return;
   }
   ```
2. **Pesos positivos:**

   ```cpp
   if (peso <= 0) {
       cout << "Error: El peso debe ser positivo.\n";
       return;
   }
   ```
3. **Rutas alcanzables:**

   ```cpp
   if (distancias[fin] == numeric_limits<int>::max()) {
       cout << "No hay ruta entre " << inicio << " y " << fin << ".\n";
   }
   ```

#### Edge Cases Considerados

| Caso                  | Manejo                 |
| --------------------- | ---------------------- |
| Nodos no existen      | Error message          |
| Grafo vacío          | Mostrar mensaje        |
| Mismo nodo inicio-fin | Distancia = 0          |
| Grafo desconectado    | Mostrar "Inalcanzable" |
| Peso inválido        | Rechazar entrada       |

---

### 5. Optimizaciones Realizadas

#### 1. Uso de `priority_queue`

```cpp
priority_queue<pair<int, string>, 
               vector<pair<int, string>>, 
               greater<pair<int, string>>> pq;
```

- Ordena automáticamente por distancia (min-heap)
- O(log n) para inserción y extracción
- Mejor que revisar linealmente todos los nodos

#### 2. `unordered_map` para acceso O(1)

- Prefierene a `map` que es O(log n)
- Ideal para búsquedas frecuentes de nodos

#### 3. Structured Bindings (C++17)

```cpp
auto [distancias, padres] = dijkstra(inicio);
```

- Código más limpio y legible
- Sin necesidad de lógica de desempaquetado adicional

#### 4. Early Exit

```cpp
if (distActual > dist ancias[nodoActual]) continue;
```

- Evita procesar un nodo dos veces
- Reduce iteraciones innecesarias

---

### 6. Análisis de Complejidad Espacial

```
Memoria Total = O(V + E)

Donde:
- Grafo (adyacencia): O(V + 2E) 
  V listas, 2E pares (bidireccional)
  
- Durante Dijkstra: O(V)
  - distancias map: O(V)
  - padres map: O(V)
  - priority queue: O(E) en peor caso
  
Total: O(V + E)
```

---

### 7. Casos de Prueba Sugeridos

#### Test 1: Grafo Simple Linear

```
A---5---B---3---C
Dijkstra(A) → B=5, C=8
```

#### Test 2: Grafo con Ciclos

```
    5
  A---B
  |   |
  8   3
  |   |
  C---D
    6
```

#### Test 3: Nodos Desconectados

```
A---5---B      C---3---D
(sin conexión entre B y C)
```

#### Test 4: Aristas de Igual Peso

```
A---1---B
|       |
1       1
|       |
C---1---D
```

---

### 8. Código Clave - Priority Queue

```cpp
// Min Priority Queue (ordena por primer elemento del pair)
priority_queue<pair<int, string>,           // tipo
               vector<pair<int, string>>,  // contenedor
               greater<pair<int, string>>> // comparador min-heap
```

**Funcionamiento:**

```cpp
pq.push({0, "Berlin"});     // (distancia, nodo)
pq.push({5, "Amsterdam"});
pq.push({8, "Paris"});

auto [dist, nodo] = pq.top();  // Obtiene (0, "Berlin")
pq.pop();                       // Remueve el mínimo

auto [dist, nodo] = pq.top();  // Ahora (5, "Amsterdam")
```

---

### 9. Diferencias con Dijkstra Original

| Característica | Nuestra Implementación | Dijkstra Original           |
| --------------- | ----------------------- | --------------------------- |
| Cola            | Priority Queue          | Original: selección manual |
| Nombres         | Strings                 | Integers (0 a V-1)          |
| Bidireccional   | Sí                     | No especificado             |
| Pesos           | Positivos               | Positivos requeridos        |

---

### 10. Posibles Mejoras Futuras

1. **Algoritmo A\***: Usar heurísticas para acelerar búsqueda
2. **Bellman-Ford**: Permitir pesos negativos
3. **Floyd-Warshall**: Todas las parejas de caminos más cortos
4. **Persistencia**: Guardar grafo en archivo
5. **Interfaz Gráfica**: Visualizar el grafo y rutas
6. **Generador de Grafos**: Crear grafos aleatorios
7. **Análisis de Escasa Conectividad**: Encontrar componentes conexos
8. **Detección de Ciclos**: Identificar bucles en el grafo

---

## Ejemplo Completo con Seguimiento

```
Entrada:
  Nodos: A, B, C, D
  Aristas: A-B(1), B-C(2), A-D(4), D-C(1)

      1      2
    A --- B --- C
    |           ^
    4           1
    |_____D_____|

Ejecutar: Dijkstra(A)

PROCESAMIENTO:
┌─────────────────────────────────────┐
│ Inicialización                      │
│ dist[A]=0, dist[B]=∞, dist[C]=∞    │
│ dist[D]=∞                           │
│ PQ: [(0,A)]                         │
└─────────────────────────────────────┘

PASO 1: Procesar A(0)
┌─────────────────────────────────────┐
│ Vecinos: B(1), D(4)                 │
│ • A→B: 0+1=1 < ∞ ✓ dist[B]=1       │
│ • A→D: 0+4=4 < ∞ ✓ dist[D]=4       │
│ dist: {A:0, B:1, C:∞, D:4}          │
│ PQ: [(1,B), (4,D)]                  │
└─────────────────────────────────────┘

PASO 2: Procesar B(1)
┌─────────────────────────────────────┐
│ Vecinos: A(1), C(2)                 │
│ • B→A: 1+1=2 > 0 ✗                  │
│ • B→C: 1+2=3 < ∞ ✓ dist[C]=3       │
│ dist: {A:0, B:1, C:3, D:4}          │
│ PQ: [(3,C), (4,D)]                  │
└─────────────────────────────────────┘

PASO 3: Procesar C(3)
┌─────────────────────────────────────┐
│ Vecinos: B(2), D(1)                 │
│ • C→B: 3+2=5 > 1 ✗                  │
│ • C→D: 3+1=4 = 4 ✗ (no mejor)       │
│ dist: {A:0, B:1, C:3, D:4}          │
│ PQ: [(4,D)]                         │
└─────────────────────────────────────┘

PASO 4: Procesar D(4)
┌─────────────────────────────────────┐
│ Vecinos: A(4), C(1)                 │
│ • D→A: 4+4=8 > 0 ✗                  │
│ • D→C: 4+1=5 > 3 ✗                  │
│ dist: {A:0, B:1, C:3, D:4}          │
│ PQ: []                              │
└─────────────────────────────────────┘

RESULTADO FINAL:
┌─────────────────────────────────────┐
│ Distancias desde A:                 │
│ • A → A: 0 minutos                  │
│ • A → B: 1 minuto  (A→B)            │
│ • A → C: 3 minutos (A→B→C)          │
│ • A → D: 4 minutos (A→D)            │
│ Padre: {A:--, B:A, C:B, D:A}        │
└─────────────────────────────────────┘
```

---

## Conclusiones

1. El algoritmo de Dijkstra está correctamente implementado
2. Maneja grafos bidireccionales con pesos
3. Tiene complejidad óptima O((V+E)log V)
4. Incluye validaciones y manejo de errores
5. Interfaz amigable y clara
