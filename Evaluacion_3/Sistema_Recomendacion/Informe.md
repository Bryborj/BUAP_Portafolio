# Informe: Sistema de Recomendación usando SVD

## Objetivo
Implementar un sistema de recomendación sencillo basado en Descomposición en Valores Singulares (SVD) y entregar código en Python, demo y este informe.

## Metodología
- Se parte de una matriz usuarios x items con NaN donde no hay calificación.
- Se imputan los NaN con la media del usuario.
- Se centra la matriz restando la media por usuario.
- Se aplica SVD truncada (svds de scipy) y se reconstruye la matriz aproximada.
- Las predicciones son las entradas reconstructoras (se suma la media de usuario de vuelta).

## Justificación
SVD captura patrones latentes de usuarios e ítems y funciona bien para matrices densas o moderadamente escasas cuando se usa imputación y centrado.

## Limitaciones
- La imputación simple por media del usuario es una aproximación básica.
- Métodos iterativos (SVD iterativo) o modelos probabilísticos suelen dar mejores resultados.

## Uso y resultados
Ejecutar `python main.py` para ver un ejemplo de uso con datos sintéticos.

## Archivos incluidos
- `recommender.py`: implementación principal.
- `main.py`: demo.
- `requirements.txt`: dependencias.
- `README.md`: instrucciones de uso.

## Posibles mejoras
- Implementar imputación iterativa (SVD impute).
- Normalizar por ítem además de por usuario.
- Añadir evaluación (MAE, RMSE) utilizando conjuntos de entrenamiento/prueba.

