Proyecto: K-means - Segmentación de Clientes

Uso rápido:

1. Instalar dependencias:

	pip install -r requirements.txt

2. Ejecutar con dataset propio:

	python main.py --input datos.csv --k 3 --out resultados

3. O ejecutar con un dataset de ejemplo generado:

	python main.py --sample --k 3 --out resultados

Resultados guardados en el directorio `resultados` por defecto: `labels.csv`, `centroids.csv`, `clusters.png`.

Revisar `informe.md` para el informe y la interpretación de los clusters.
