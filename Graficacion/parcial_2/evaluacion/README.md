# Evaluación Unidad 2: Paralelización Matricial con Procesos e Hilos

Este directorio contiene todo el material desarrollado para la **Evaluación de la Unidad 2** a partir del archivo base `example_multiprocessing.py`.

---

## 📁 Estructura de Archivos

1. **`propuesta_mejora.py`**:
   - Implementación en código Python de la propuesta de mejora lógica y del algoritmo original para comparación.
   - Contiene la función `multiplicar_propuesta_mejora(A, B)` basada en particionado por chunks y granularidad vectorial.
   - Incluye un banco de pruebas y benchmark automatizado con cálculo de métricas (aceleración *speedup*, reducción de hilos y validación de matrices).
   - Para ejecutar la demostración:
     ```bash
     python3 evaluacion/propuesta_mejora.py
     ```

2. **`ENTREGABLE_PROPUESTA.md`**:
   - **Documento formal del entregable para el profesor**.
   - Incluye el **Diagnóstico Crítico** de las fallas lógicas de `example_multiprocessing.py`.
   - Incluye el **Diagrama de Flujo (Mermaid)** y el **Pseudocódigo Estructurado**.
   - Tabla comparativa de complejidad algorítmica ($O(N^3)$ vs $O(N)$) y análisis de ahorro de memoria.

3. **`GUIA_EXPOSICION_10MIN.md`**:
   - Libreto organizado para **3 integrantes de equipo** con un límite estricto de **10 minutos**:
     - **Integrante 1 (0:00 - 3:00):** Diagnóstico del problema original y cuellos de botella (`q.get()`, GIL, overhead $N^3$).
     - **Integrante 2 (3:00 - 7:00):** Propuesta de mejora lógica, Diagrama de Flujo y Pseudocódigo.
     - **Integrante 3 (7:00 - 10:00):** Viabilidad teórica, Benchmark experimental en vivo y Conclusiones.
   - Incluye un **Banco de Preguntas Típicas del Profesor** con respuestas preparadas.

---

## 🚀 Resumen de Resultados Empíricos

Al ejecutar `propuesta_mejora.py` contra el código original:
- **Matriz 3x3:** Reducción de 27 a 3 hilos (88.9% menos). Aceleración: **2.34x**.
- **Matriz 8x8:** Reducción de 512 a 8 hilos (98.4% menos). Aceleración: **5.64x**.
- **Matriz 16x16:** Reducción de 4,096 a 16 hilos (99.6% menos). Aceleración: **13.55x**.
