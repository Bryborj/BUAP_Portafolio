Sistema de Recomendación (SVD)

Uso rápido:

1. Crear un DataFrame de pandas con usuarios en filas y items en columnas (NaN = no visto).
2. Ajustar modelo:

```python
from recommender import SVDRecommender
model = SVDRecommender(n_components=20)
model.fit(ratings_df)
```

3. Predecir o recomendar:

```python
pred = model.predict(user_id, item_id)
recs = model.recommend(user_id, ratings_df, n=10)
```

Demo: ejecutar `python main.py`.
