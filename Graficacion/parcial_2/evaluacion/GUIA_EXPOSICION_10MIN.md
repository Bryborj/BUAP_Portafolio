# Guía de Exposición: Evaluación Unidad 2 (10 Minutos)

**Tema:** Propuesta de Mejora para Multiplicación Matricial Paralela (Procesos e Hilos)  
**Modalidad:** Exposición oral en equipo (3 personas)  
**Tiempo Límite:** 10 minutos (estrictos)  

---

## Estructura General del Tiempo

| Integrante | Rol | Tema Principal | Tiempo Sugerido |
| :---: | :--- | :--- | :---: |
| **Integrante 1** | *El Diagnóstico Crítico* | Planteamiento y Cuellos de Botella del Código Original | **0:00 - 3:00** (3 min) |
| **Integrante 2** | *El Arquitecto del Sistema* | Propuesta de Mejora, Diagrama de Flujo y Pseudocódigo | **3:00 - 7:00** (4 min) |
| **Integrante 3** | *El Analista de Rendimiento* | Viabilidad Teórica, Demostración/Benchmark y Cierre | **7:00 - 10:00** (3 min) |

---

## Guión Detallado por Integrante

### 🎤 Integrante 1: Diagnóstico Crítico del Programa Original (Minutos 0:00 a 3:00)

#### Objetivo:
Demostrar al profesor que el equipo comprendió a fondo el código base y detectó los problemas reales de diseño concurrente, no solo errores superficiales de sintaxis.

#### Puntos a Exponer:
1. **Introducción breve (30 seg):**
   > *"Buenos días profesor y compañeros. En esta evaluación analizamos el programa base `example_multiprocessing.py`, cuyo objetivo es paralelizar la multiplicación de matrices $A \times B$ combinando procesos e hilos. Sin embargo, al inspeccionar la lógica del programa, descubrimos que en realidad se ejecutaba de forma secuencial y con una sobrecarga masiva de recursos."*

2. **Falla 1: Falso Paralelismo / Serialización Oculta (1 min):**
   > *"El primer cuello de botella está en el bucle principal de procesos:*
   > ```python
   > for row in A:
   >     processingInit = Process(...)
   >     processingInit.start()
   >     C.append(q.get())  # <-- BLOQUEO AQUÍ
   > ```
   > *Al colocar `q.get()` dentro del mismo bucle inmediatamente después del `start()`, el proceso padre se queda congelado esperando el resultado del proceso hijo antes de poder crear el siguiente. La ejecución es 100% secuencial: no hay concurrencia real entre procesos."*

3. **Falla 2: Hiper-fragmentación de hilos a nivel escalar (1 min):**
   > *"El segundo problema radica en la granularidad de los hilos. Para cada elemento de la matriz, el programa crea un hilo para multiplicar dos números simples ($x \times y$). Esto genera $N^3$ hilos. Para una matriz de $3 \times 3$ son 27 hilos, pero para una de $16 \times 16$ son más de 4,000 hilos. En sistemas operativos y en Python bajo el GIL (Global Interpreter Lock), crear un hilo para una sola multiplicación de 64 bits cuesta miles de ciclos de CPU más que la multiplicación misma."*

4. **Transición a Integrante 2 (30 seg):**
   > *"Por ello, nuestra propuesta no fue cambiar una línea de código, sino rediseñar la arquitectura lógica del algoritmo. Mi compañero explicará la propuesta."*

---

### 🎤 Integrante 2: Arquitectura de la Propuesta de Mejora (Minutos 3:00 a 7:00)

#### Objetivo:
Explicar el modelo jerárquico híbrido, el Diagrama de Flujo y el Pseudocódigo (el entregable formal solicitado).

#### Puntos a Exponer:
1. **Presentación de la Propuesta Lógica (1 min):**
   > *"Diseñamos una Arquitectura Jerárquica Híbrida en dos niveles de granularidad:*
   > *1. **Nivel Procesos (Multi-core real):** En lugar de crear procesos por cada fila o por cada número, dividimos la matriz en bloques o **chunks** contiguos según el número de núcleos físicos del procesador ($P = \min(\text{cores}, N)$).*
   > *2. **Nivel Hilos (Granularidad Vectorial):** Elevamos el trabajo de cada hilo. Un hilo ya no multiplica dos números; cada hilo calcula una fila completa o vector del resultado.*
   > *3. **Asincronía Desacoplada:** Lanzamos todos los procesos de forma asíncrona y recolectamos los resultados mediante tuplas indexadas `(start_row, chunk_resultado)` para garantizar un ensamblado determinista y sin condiciones de carrera."*

2. **Explicación del Diagrama de Flujo (1.5 min):**
   > *(Mostrar el Diagrama de Flujo de Mermaid proyectado)*
   > *"Como observamos en el diagrama de flujo:*
   > *- El proceso maestro valida dimensiones e inspecciona los núcleos físicos.*
   > *- Se particiona la matriz A en $P$ chunks balanceados.*
   > *- Se bifurcan los procesos trabajadores (Fork).*
   > *- En cada trabajador, se crean hilos dedicados a cada fila del chunk, calculando el producto punto.*
   > *- Los resultados se envían a la cola indexada y el maestro los ensambla directamente en sus posiciones de memoria, sin bloqueos prematuros."*

3. **Explicación del Pseudocódigo (1 min):**
   > *(Mostrar el pseudocódigo estructurado)*
   > *"El pseudocódigo formal muestra claramente la separación entre la fase de despacho asíncrono, la subrutina del trabajador de bloque y la recolección determinista.*
   > *Reducimos la creación de hilos de $O(N^3)$ a $O(N)$, eliminando por completo la sobrecarga innecesaria."*

4. **Transición a Integrante 3 (30 seg):**
   > *"Ahora mi compañero presentará la viabilidad teórica y los resultados empíricos que validan esta mejora."*

---

### 🎤 Integrante 3: Viabilidad Teórica, Benchmark y Conclusiones (Minutos 7:00 a 10:00)

#### Objetivo:
Demostrar con métricas matemáticas y experimentales que la propuesta cumple con mejorar tiempo de ejecución y ahorrar memoria.

#### Puntos a Exponer:
1. **Viabilidad Teórica y Complejidad (1 min):**
   > *"Nuestra propuesta es teóricamente viable porque respeta los principios fundamentales de la computación paralela:*
   > *- **Ley de Amdahl:** Minimizamos la fracción secuencial al eliminar el bloqueo en el bucle maestro.*
   > *- **Relación Cómputo/Comunicación:** Aumentamos la granularidad de la tarea para que el tiempo útil de cálculo supere por amplio margen al costo de instanciación del hilo.*
   > *- **Ahorro de Memoria:** Reducir los hilos de $N^3$ a $N$ reduce el tamaño de las pilas de memoria asociadas a cada hilo de $O(N^3 \times \text{StackSize})$ a solo $O(N)$."*

2. **Resultados del Benchmark Experimental (1 min):**
   > *(Mostrar la tabla o ejecutar el script en terminal: `python3 evaluacion/propuesta_mejora.py`)*
   > *"Implementamos la solución y medimos el rendimiento real en nuestro procesador:*
   > *- Para matrices $3 \times 3$: pasamos de 27 hilos a 3 hilos, acelerando **2.34x**.*
   > *- Para matrices $8 \times 8$: pasamos de 512 hilos a 8 hilos, acelerando **5.64x**.*
   > *- Para matrices $16 \times 16$: el programa original creaba **4,096 hilos** tardando casi 0.8 segundos. Con nuestra propuesta se crearon solo **16 hilos**, tardando 0.05 segundos: una aceleración de **13.55x más rápido** y una **reducción del 99.6% en sobrecarga de hilos**."*

3. **Conclusión y Cierre (1 min):**
   > *"En conclusión, demostramos que la concurrencia eficiente no consiste en lanzar la mayor cantidad posible de hilos o procesos, sino en alinear la granularidad del algoritmo con la arquitectura del hardware. Con esto cubrimos todos los requisitos solicitados por el profesor. Quedamos atentos a sus preguntas."*

---

## Banco de Preguntas Típicas del Profesor y Respuestas Preparadas

### P1: "¿Por qué no usar hilos para cada multiplicación escalar como estaba en el original?"
* **Respuesta:** *"Porque el costo de crear el contexto de un hilo en el sistema operativo y gestionarlo a través del GIL de Python es de miles de ciclos de CPU, mientras que multiplicar dos números toma 1 solo ciclo de reloj. La relación cómputo/overhead era sumamente desfavorable."*

### P2: "¿Por qué no crear un proceso por cada fila si hay matrices de 1000 filas?"
* **Respuesta:** *"Porque un procesador típico tiene entre 4 y 16 núcleos físicos. Si creamos 1,000 procesos, el sistema operativo satura la memoria con miles de tablas de páginas y gasta casi todo el tiempo en cambios de contexto de procesos (multiprocess overhead). La técnica de chunking agrupa las filas para que haya exactamente tantos procesos como núcleos útiles."*

### P3: "¿Cómo evitan que las filas de la matriz se desordenen al usar una cola de procesos?"
* **Respuesta:** *"En el código original, si se quita el bloqueo, las filas llegarían en orden aleatorio. En nuestra propuesta, cada proceso envía una tupla con su índice inicial `(start_row, submatriz)`. El proceso principal preasigna la matriz $C$ e inserta cada bloque exactamente en su posición matemática correspondiente."*
