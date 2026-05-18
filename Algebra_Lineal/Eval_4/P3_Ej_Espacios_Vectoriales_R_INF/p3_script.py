import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Actividad 1: Colores RGB
r = np.array([255, 0, 0])
g = np.array([0, 255, 0])
b = np.array([0, 0, 255])
c = np.array([120, 200, 75])

# c = a1*r + a2*g + a3*b
# [r g b] * [a1 a2 a3]^T = c
M_rgb = np.column_stack((r, g, b))
coeffs_rgb = np.linalg.solve(M_rgb, c)
print("--- Actividad 1: Colores RGB ---")
print(f"Coeficientes para (120, 200, 75) en base RGB: {coeffs_rgb}")
print(f"Comprobación: {coeffs_rgb[0]*r + coeffs_rgb[1]*g + coeffs_rgb[2]*b}\n")

# Actividad 2: Matrices 2x2
A = np.array([[120, 80], [60, 200]])
E11 = np.array([[1, 0], [0, 0]])
E12 = np.array([[0, 1], [0, 0]])
E21 = np.array([[0, 0], [1, 0]])
E22 = np.array([[0, 0], [0, 1]])

print("--- Actividad 2: Imagen como Matriz ---")
print("Matriz A:")
print(A)
print(f"A como combinación lineal: 120*E11 + 80*E12 + 60*E21 + 200*E22")
# Graficar
plt.figure()
plt.imshow(A, cmap='gray', vmin=0, vmax=255)
plt.title('Imagen 2x2 en escala de grises')
plt.axis('off')
for i in range(2):
    for j in range(2):
        plt.text(j, i, str(A[i, j]), color='red', ha='center', va='center')
plt.savefig('matriz_imagen.png')
print("Imagen guardada como matriz_imagen.png\n")

# Actividad 3: Polinomios
x = sp.Symbol('x')
p = 1 + 2*x - x**2
q = 3 - x + 4*x**2

print("--- Actividad 3: Polinomios ---")
print(f"p(x) = {p}")
print(f"q(x) = {q}")
print(f"p(x) + q(x) = {sp.simplify(p + q)}")
print(f"3 * p(x) = {sp.simplify(3 * p)}")

# Coordenadas en la base {1, x, x^2}
def get_coords(poly):
    poly = sp.expand(poly)
    return [poly.coeff(x, 0), poly.coeff(x, 1), poly.coeff(x, 2)]

print(f"Coordenadas de p(x) en base {{1, x, x^2}}: {get_coords(p)}")
print(f"Coordenadas de q(x) en base {{1, x, x^2}}: {get_coords(q)}")

# Actividad 4 y 5 (Teórico / Rango de matrices para comprobar independencia)
# Comprobar independencia de {1, x, x^2, x^3} ... {e1, e2 ...}
print("\n--- Independencia Lineal ---")
print("Para demostrar independencia lineal finita, calculamos el rango:")
# Ejemplo base P2
M_p2 = np.eye(3) # [1,0,0], [0,1,0], [0,0,1]
print(f"Rango de la matriz identidad 3x3 (Base de P2): {np.linalg.matrix_rank(M_p2)}")
