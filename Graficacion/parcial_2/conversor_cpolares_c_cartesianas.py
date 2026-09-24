import numpy as np
import matplotlib.pyplot as plt

# Coordenas polares
r = 5
theta = 45

# Converción a radianes 
angulo = np.radians(theta)

# Conversión polar -> Cartesiana
x = r * np.cos(angulo)
y = r * np.sin(angulo)

# Cdear figura
fig, ax = plt.subplots()

# Punto
ax.scatter(x, y, s=100)

# Linea desde el origen hasta el punto
ax.plot([0, x], [0, y])

# Etiqueta del punto
ax.text(x, y, f"    P{r}, {theta}")

# Lineas de referencia
ax.axhline(0)
ax.axvline(0)

# Limites
ax.set_xlim(-6,6)
ax.set_ylim(-6,6)

ax.set_label("X")
ax.set_ylabel("Y")

ax.set_title("Coordenadas polares")
ax.grid(True)
ax.set_aspect("equal")
plt.show()
print("Coordenadas polares: " \
f"\nr = {r}" \
f"\no = {theta}" \
"\n Coordenadas cartesianas: " \
f"\nx = {x:.2f}" \
f"\nx = {y:.2f}")