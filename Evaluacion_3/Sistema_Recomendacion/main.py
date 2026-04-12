"""Demo rápido del sistema de recomendación SVD.
Ejecuta: python main.py
"""
import pandas as pd
from recommender import SVDRecommender, from_long_dataframe


def example():
    data = [
        (1, 'A', 5), (1, 'B', 3), (1, 'C', None),
        (2, 'A', 4), (2, 'B', None), (2, 'C', 2),
        (3, 'A', None), (3, 'B', 2), (3, 'C', 5),
        (4, 'A', 1), (4, 'B', None), (4, 'C', None),
        (5, 'A', None), (5, 'B', 4), (5, 'C', 4),
    ]
    df_long = pd.DataFrame(data, columns=['user', 'item', 'rating'])

    ratings = from_long_dataframe(df_long)
    print('Matriz de calificaciones (NaN = no visto):')
    print(ratings)

    model = SVDRecommender(n_components=2)
    model.fit(ratings)

    user = 1
    recs = model.recommend(user, ratings, n=3)
    print(f'Principales recomendaciones para el usuario {user}:')
    for item, score in recs:
        print('-', item, 'pred:', round(score, 3))


if __name__ == '__main__':
    example()
