import argparse
import os
import sys
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


def load_data(path):
	if path and os.path.exists(path):
		df = pd.read_csv(path)
		return df
	return None


def generate_sample(n=300, random_state=42):
	rng = np.random.RandomState(random_state)
	ages = rng.normal(loc=40, scale=12, size=n).clip(18, 80)
	income = rng.normal(loc=50000, scale=24000, size=n).clip(5000, 200000)
	freq = rng.poisson(lam=3, size=n)
	df = pd.DataFrame({"Age": ages.astype(int), "Income": income, "Frequency": freq})
	return df


def preprocess(df, features=None):
	df = df.copy()
	if features is None:
		features = df.select_dtypes(include=[np.number]).columns.tolist()
	df = df[features].dropna()
	scaler = StandardScaler()
	X = scaler.fit_transform(df.values)
	return X, df.index, features, scaler


def run_kmeans(X, k, random_state=0):
	kmeans = KMeans(n_clusters=k, random_state=random_state, n_init=10)
	kmeans.fit(X)
	return kmeans


def save_results(outdir, df_index, labels, centroids, features):
	os.makedirs(outdir, exist_ok=True)
	pd.DataFrame({"label": labels}, index=df_index).to_csv(os.path.join(outdir, "labels.csv"))
	pd.DataFrame(centroids, columns=features).to_csv(os.path.join(outdir, "centroids.csv"))


def plot_clusters(X, labels, centroids, outpath, title="K-means clusters"):
	pca = PCA(n_components=2)
	X2 = pca.fit_transform(X)
	c2 = pca.transform(centroids)
	plt.figure(figsize=(8,6))
	scatter = plt.scatter(X2[:,0], X2[:,1], c=labels, cmap='tab10', s=30, alpha=0.7)
	plt.scatter(c2[:,0], c2[:,1], c='black', s=150, marker='X')
	plt.title(title)
	plt.xlabel('PC1')
	plt.ylabel('PC2')
	plt.legend(*scatter.legend_elements(), title="Clusters", loc='best')
	plt.tight_layout()
	plt.savefig(outpath)
	plt.close()


def main():
	parser = argparse.ArgumentParser(description="K-means segmentation de clientes")
	parser.add_argument("--input", "-i", help="CSV de entrada (opcional)")
	parser.add_argument("--k", "-k", type=int, default=3, help="Número de clusters")
	parser.add_argument("--out", "-o", default="outputs", help="Directorio de salida")
	parser.add_argument("--sample", action='store_true', help="Generar dataset de ejemplo si no hay input")
	args = parser.parse_args()

	df = load_data(args.input)
	if df is None:
		if args.input:
			print(f"Archivo no encontrado: {args.input}")
		if args.sample or args.input is None:
			print("Generando dataset de ejemplo...")
			df = generate_sample()
		else:
			print("No hay datos de entrada. Use --sample para generar un ejemplo.")
			sys.exit(1)

	X, idx, features, scaler = preprocess(df)
	kmeans = run_kmeans(X, args.k, random_state=0)

	labels = kmeans.labels_
	centroids = scaler.inverse_transform(kmeans.cluster_centers_)

	save_results(args.out, idx, labels, centroids, features)
	plot_clusters(X, labels, kmeans.cluster_centers_, os.path.join(args.out, "clusters.png"))

	print("Resultados guardados en:", args.out)
	print("Centroides:")
	print(pd.DataFrame(centroids, columns=features))


if __name__ == '__main__':
	main()

