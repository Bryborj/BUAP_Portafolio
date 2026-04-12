Informe - Segmentación de Clientes con K-means
=============================================

1. Descripción

   Se implementó el algoritmo K-means para agrupar clientes según características numéricas.

2. Procedimiento

   - Cargar datos (CSV) o generar dataset de ejemplo.
   - Preprocesamiento: eliminar nulos y estandarizar con `StandardScaler`.
   - Aplicar `KMeans(n_clusters=k)` y obtener etiquetas y centroides.
   - Visualizar en 2D usando PCA y guardar resultados.

3. Archivos entregados

   - `main.py`: código fuente.
   - `requirements.txt`: dependencias.
   - `labels.csv`: etiqueta por registro (generado por la ejecución).
   - `centroids.csv`: coordenadas de centroides (generado por la ejecución).
   - `clusters.png`: visualización PCA de clusters.

4. Interpretación (ejemplo)

   - Revisar `centroids.csv` para conocer el perfil promedio de cada cluster.
   - Comparar edades, ingresos y frecuencia para nombrar segmentos (jóvenes/bajos ingresos, adultos/medios, etc.).

5. Elección de `k`

   - Para elegir `k` se puede usar el método del codo (no implementado aquí por simplicidad).

6. Recomendaciones

   - Escalar variables si tienen rangos muy distintos.
   - Probar varios `k` y validar con métricas externas o conocimiento del negocio.
