import numpy as np
import pandas as pd
from scipy.sparse.linalg import svds


class SVDRecommender:
    """Recomendador basado en SVD simple.

    Requiere una matriz de calificaciones `ratings_df` con usuarios en filas
    y items en columnas. Valores faltantes deben ser NaN.
    """

    def __init__(self, n_components=20):
        self.k = n_components
        self.user_index = None
        self.item_index = None
        self.user_means = None
        self.U = None
        self.S = None
        self.Vt = None
        self.fitted = False

    def fit(self, ratings_df: pd.DataFrame):
        self.user_index = list(ratings_df.index)
        self.item_index = list(ratings_df.columns)

        self.user_means = ratings_df.mean(axis=1).fillna(0).values

        R_filled = ratings_df.copy().astype(float)
        for i, u in enumerate(self.user_index):
            R_filled.loc[u] = R_filled.loc[u].fillna(self.user_means[i])

        R_centered = R_filled.values - self.user_means.reshape(-1, 1)

        k = min(self.k, min(R_centered.shape) - 1)
        if k <= 0:
            raise ValueError("n_components demasiado grande para la matriz dada")

        U, s, Vt = svds(R_centered, k=k)
        idx = np.argsort(s)[::-1]
        s = s[idx]
        U = U[:, idx]
        Vt = Vt[idx, :]

        self.U = U
        self.S = np.diag(s)
        self.Vt = Vt
        self.fitted = True

    def _reconstructed_matrix(self):
        if not self.fitted:
            raise RuntimeError("El modelo no está ajustado. Llama a fit().")
        R_hat = self.U @ self.S @ self.Vt
        R_hat = R_hat + self.user_means.reshape(-1, 1)
        return pd.DataFrame(R_hat, index=self.user_index, columns=self.item_index)

    def predict(self, user, item):
        """Predecir calificación para un usuario e ítem.

        user: índice (etiqueta) presente en `ratings_df.index`
        item: etiqueta presente en `ratings_df.columns`
        """
        R_hat = self._reconstructed_matrix()
        try:
            return float(R_hat.loc[user, item])
        except Exception:
            raise KeyError("Usuario o ítem no encontrado en el conjunto entrenado")

    def recommend(self, user, original_ratings: pd.DataFrame, n=10):
        """Devolver top-n ítems recomendados para `user`.

        `original_ratings` debe ser la misma matriz de entrada (con NaN para no vistos).
        """
        if user not in original_ratings.index:
            raise KeyError("Usuario no encontrado en original_ratings")

        R_hat = self._reconstructed_matrix()
        user_row = original_ratings.loc[user]
        unseen = user_row[user_row.isna()].index.tolist()
        if not unseen:
            return []

        preds = R_hat.loc[user, unseen].sort_values(ascending=False)
        return list(preds.head(n).items())


def from_long_dataframe(df_long, user_col='user', item_col='item', rating_col='rating'):
    """Convertir DataFrame en formato largo a matriz usuarios x items.

    Devuelve matriz pandas con usuarios como índice y items como columnas.
    """
    pivot = df_long.pivot_table(index=user_col, columns=item_col, values=rating_col, aggfunc='mean')
    return pivot
