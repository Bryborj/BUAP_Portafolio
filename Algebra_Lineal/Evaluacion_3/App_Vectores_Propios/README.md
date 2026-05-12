# PageRank: Aplicación de Vectores Propios en Redes de Navegación Web

## Descripción del Problema

Este programa implementa el **algoritmo PageRank de Google**, una aplicación práctica de **eigenvectores y valores propios** del álgebra lineal. Calcula la importancia de páginas web en una red de enlaces utilizando el método de potencias.

## Conceptos de Álgebra Lineal

### 1. **Matriz de Enlaces (H)**
Representa los hipervínculos entre páginas web. El elemento H[i][j] indica la probabilidad de navegar desde la página j hacia la página i.

```
H = [
    [0.0, 0.0, 0.5, 0.5],  # P1 recibe enlaces de P3 y P4
    [0.5, 0.0, 0.0, 0.0],  # P2 recibe enlaces de P1
    [0.5, 1.0, 0.0, 0.5],  # P3 recibe enlaces de P1, P2 y P4
    [0.0, 0.0, 0.0, 0.0]   # P4 no recibe enlaces
]
```

### 2. **Factor de Damping (d = 0.85)**
- **d = 0.85**: Probabilidad de seguir un enlace aleatorio (85%)
- **1-d = 0.15**: Probabilidad de saltar a una página aleatoria (15%)

Este factor modela un navegador web realista donde los usuarios ocasionalmente se cansan y saltan a una página aleatoria.

### 3. **Matriz de Google (G)**
Combina la matriz de enlaces con el factor de damping:

$$G = d \cdot H + (1-d) \cdot \frac{1}{n} \cdot \mathbf{e}\mathbf{e}^T$$

Donde:
- **n** = número de páginas
- **e** = vector columna de unos
- Esta matriz garantiza convergencia del algoritmo

### 4. **Método de Potencias (Power Method)**
Encuentra el **eigenvector dominante** de G iterativamente:

$$\mathbf{x}_{k+1} = \frac{G \cdot \mathbf{x}_k}{\sum(G \cdot \mathbf{x}_k)}$$

Comienza con un vector inicial uniforme y converge cuando:

$$\|\mathbf{x}_{k+1} - \mathbf{x}_k\|_1 < \text{tolerancia}$$

**Nota de implementación**: La normalización después de cada iteración es esencial para:
- Mantener el vector como distribución de probabilidad (suma = 1)
- Evitar desbordamiento o desaparición numérica
- Acelerar convergencia
- Garantizar precisión numérica

El vector resultante **es el eigenvector asociado al mayor eigenvalor** (que siempre es 1 en este caso).

## Interpretación de Resultados

El **vector PageRank final** contiene las importancias relativas de cada página:

- **Suma = 1**: Es una distribución de probabilidad
- **Componentes mayores**: Páginas más importantes en la red
- **Ejemplo**: Si P3 tiene score 0.4448, significa que 44.48% del tráfico web se concentra en esa página

### En nuestro ejemplo:
- **P3 (44.48%)**: Página más importante. Recibe enlaces de P1, P2 y P4
- **P1 (30.36%)**: Segunda más importante. Recibe enlaces de P3 y P4
- **P2 (20.53%)**: Tercera. Recibe enlaces de P1
- **P4 (4.62%)**: Menos importante. Sin enlaces entrantes directos

Esta distribución refleja la estructura de la red: quien más enlaza recibe, y quien más recibe es más importante.

## Cómo Ejecutar

```bash
python PageRank.py
```

### Salida esperada
```
Matriz de Google:
[[0.0375 0.0375 0.4625 0.4625]
 [0.4625 0.0375 0.0375 0.0375]
 [0.4625 0.8875 0.0375 0.4625]
 [0.0375 0.0375 0.0375 0.0375]]

Iteraciones del método de potencias:
Iteración 10: Error = 3.7456861765e-03
Iteración 20: Error = 1.6021530681e-05
Iteración 30: Error = 1.2443831536e-07
Iteración 40: Error = 7.2353565500e-10
Iteración 45: Error = 5.2548847218e-11

✓ Convergencia alcanzada en 45 iteraciones

===================================================
VECTOR PAGERANK FINAL (Eigenvector dominante):
===================================================
[0.30359351 0.20534764 0.44481694 0.0462419 ]

Suma del vector PageRank: 1.0000000000

===================================================
RANKING DE PÁGINAS WEB
===================================================
1. P3: 0.4448169441
2. P1: 0.3035935137
3. P2: 0.2053476400
4. P4: 0.0462419022
```

## Conexión con Eigenvectores

El vector PageRank **x** satisface la ecuación de eigenvalor:

$$G \cdot \mathbf{x} = \lambda \mathbf{x}$$

Donde λ = 1 es el eigenvalor dominante. Esto significa que:
- Si el navegador web aleatoriamente distribuye su posición según **x**, mantiene esa distribución indefinidamente
- Es el único equilibrio estable del proceso

## Aplicaciones Prácticas

- **Google Search (1998)**: Algoritmo original de ranking de resultados
- **Análisis de redes sociales**: Influencia de usuarios
- **Recomendación de contenidos**: Importancia de nodos en grafos
- **Análisis de citas académicas**: PageRank de artículos científicos

---

**Curso**: Álgebra Lineal  
**Profesor**: M.C. Margarita Carmina García López  
**Alumno**: Bryan A. Borges  
**Universidad**: Benemérita Universidad Autónoma de Puebla (BUAP)  
**Licenciatura**: Ingeniería en Ciencias de la Computación  
**Tema**: Aplicación de Vectores Propios y Eigenvalores
