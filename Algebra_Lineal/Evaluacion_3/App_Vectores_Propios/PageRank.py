import numpy as np

# ===== MATRIZ DE ENLACES H =====
# Representa los hipervínculos entre 4 páginas web
# H[i][j] = probabilidad de seguir un enlace de la página j a la página i
# Si una página no tiene enlaces salientes, se distribuye uniformemente
H = np.array([
    [0.0, 0.0, 0.5, 0.5],    # Enlaces hacia P1
    [0.5, 0.0, 0.0, 0.0],    # Enlaces hacia P2
    [0.5, 1.0, 0.0, 0.5],    # Enlaces hacia P3
    [0.0, 0.0, 0.0, 0.0]     # Enlaces hacia P4
])

# Número de páginas
n = H.shape[0]

# ===== FACTOR DE DAMPING (AMORTIGUAMIENTO) =====
# d = 0.85: Probabilidad de seguir un enlace
# 1-d = 0.15: Probabilidad de saltar a una página aleatoria (modelo de navegación web real)
d = 0.85

# ===== MATRIZ DE GOOGLE (G) =====
# Fórmula: G = d*H + (1-d)*(1/n)*e*e^T
# Esta matriz asegura convergencia y representa el navegador web aleatorio
e = np.ones((n, 1))  # Vector columna de unos
G = d * H + (1 - d) * (1/n) * np.dot(e, e.T)

print("Matriz de Google:")
print(G)
print()

# ===== VECTOR INICIAL =====
# x₀ = (1/n, 1/n, ..., 1/n) - distribución uniforme inicial
x = np.ones(n) / n

# ===== MÉTODO DE POTENCIAS (POWER METHOD) =====
# Encuentra el eigenvector dominante de G (vector de PageRank)
# x_{k+1} = G * x_k (normalizado)
# El algoritmo converge cuando ||x_{k+1} - x_k|| < tolerancia
# La normalización es esencial para evitar desbordamiento numérico

tol = 1e-10          # Tolerancia de convergencia
max_iter = 100       # Máximo número de iteraciones
convergencia = False

print("Iteraciones del método de potencias:")
for i in range(max_iter):
    x_new = np.dot(G, x)
    x_new = x_new / np.sum(x_new)  # Normalización por suma para mantener probabilidad
    
    error = np.linalg.norm(x_new - x, ord=1)  # Norma L1 del residuo
    
    if (i+1) % 10 == 0 or error < tol:
        print(f"Iteración {i+1}: Error = {error:.10e}")
    
    if error < tol:
        convergencia = True
        break
    
    x = x_new

print()
if convergencia:
    print(f"✓ Convergencia alcanzada en {i+1} iteraciones")
else:
    print(f"⚠ No convergió en {max_iter} iteraciones")
print()

# ===== RESULTADOS FINALES =====
print("=" * 50)
print("VECTOR PAGERANK FINAL (Eigenvector dominante):")
print("=" * 50)
print(x)
print()

# Validación: suma debe ser 1 (probabilidad)
print(f"Suma del vector PageRank: {np.sum(x):.10f}")
print()

# ===== RANKING DE PÁGINAS =====
print("=" * 50)
print("RANKING DE PÁGINAS WEB")
print("=" * 50)
pages = ['P1', 'P2', 'P3', 'P4']
ranking = sorted(zip(pages, x), key=lambda t: t[1], reverse=True)

for rank, (page, score) in enumerate(ranking, 1):
    print(f"{rank}. {page}: {score:.10f}")
