# Práctica: Matrices de Cambio de Base en Transformaciones 3D

Este proyecto contiene la implementación de la práctica de transformaciones en 3D utilizando matrices de cambio de base en Python, con `numpy` y `matplotlib`.

## Entregables
1. **Código Python:** Se encuentra implementado en el archivo `main.py`.
2. **Capturas de Pantalla:** Al ejecutar el script se generarán las siguientes imágenes mostrando las transformaciones:
   - `01_transformacion_45_grados.png`: Rotación original a 45 grados (base ortonormal).
   - `02_transformacion_60_grados.png`: Rotación a 60 grados (base ortonormal).
   - `03_transformacion_no_ortogonal.png`: Sesgo/shear aplicado con una base no ortogonal.
3. **Explicación breve de resultados:**

### Respuestas a las Preguntas de la Práctica

1. **¿Qué representa físicamente el cambio de base en gráficos?**
   Representa un cambio en el sistema de referencia o sistema de coordenadas. Por ejemplo, es la operación matemática detrás de pasar las coordenadas de un objeto (Object Space) a las coordenadas del mundo (World Space), o del mundo a la vista de la cámara (Camera Space). Físicamente, implica reinterpretar las posiciones de los vértices relativas a unos nuevos ejes dados por los vectores de la base.

2. **¿Por qué el objeto no cambia de forma?**
   Si la matriz de cambio de base es **ortonormal** (como en el caso de la rotación inicial de 45 grados o 60 grados), la transformación es una *isometría*, lo que significa que preserva distancias y ángulos. Los vectores base siguen siendo perpendiculares entre sí y tienen una longitud de 1 (vectores unitarios). Por lo tanto, el objeto solo experimenta una rotación o traslación rígidamente, pero su forma no se deforma.

3. **¿Qué sucede si la base no es ortonormal?**
   El objeto sufre deformaciones geométricas. Dependiendo de los vectores elegidos, puede experimentar un **escalado** (si la longitud de los vectores no es 1) o un **sesgo/shear** (si los vectores base no son perpendiculares entre sí, como se demuestra en la "tarea 2" implementada en el código). Pierde sus propiedades rígidas y proporciones originales.

4. **¿Cómo se relaciona esto con la cámara en videojuegos?**
   En el desarrollo de videojuegos, la cámara posee su propio sistema de coordenadas (usualmente localizada en el origen de dicho sistema y mirando hacia un eje particular, como el eje -Z). Para renderizar en la pantalla los objetos 3D colocados en el mundo, todos los vértices deben transformarse multiplicando por una **View Matrix** (Matriz de Vista). Esta matriz no es más que una matriz de cambio de base que transforma las coordenadas del "espacio de mundo" a las coordenadas relativas a "espacio de la cámara".

5. **¿Qué ocurre si la matriz no es invertible?**
   Si la matriz no es invertible (su determinante es 0), significa que los vectores que forman las columnas de la matriz no son linealmente independientes (no forman una base válida para ℝ³). Geométricamente, esto implica una pérdida de dimensionalidad; el objeto 3D colapsaría en un plano 2D, una línea o un solo punto. Esto destruye la información y hace imposible revertir la transformación para recuperar las coordenadas originales (ya que matemáticamente no se puede calcular $P^{-1}$).
