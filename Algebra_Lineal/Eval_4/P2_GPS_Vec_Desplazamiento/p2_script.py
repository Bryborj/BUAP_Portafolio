import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('gps.csv', delimiter=',', skip_header=1)
x = data[:, 0]
y = data[:, 1]

vx = np.diff(x)
vy = np.diff(y)

# Calcular magnitudes
magnitudes = np.sqrt(vx**2 + vy**2)
distancia_total = np.sum(magnitudes)

print(f"Desplazamientos X: {vx}")
print(f"Desplazamientos Y: {vy}")
print(f"Magnitudes: {magnitudes}")
print(f"Distancia Total GPS: {distancia_total}")

# Graficar
plt.figure()
plt.quiver(x[:-1], y[:-1], vx, vy, angles='xy', scale_units='xy', scale=1, color='blue')
plt.plot(x, y, 'ro-', alpha=0.5)
plt.axis('equal')
plt.title('Trayectoria Reconstruida')
plt.grid(True)
plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plt.savefig('plot_gps.png')

# Angulo entre tramos (ejemplo entre primer y segundo tramo distinto)
# Tramos: v1 = (0, 1), v2 = (1, 0)
v1 = np.array([vx[2], vy[2]]) # el tramo de 0,2 a 0,3 es (0,1)
v2 = np.array([vx[3], vy[3]]) # el tramo de 0,3 a 1,3 es (1,0)
dot_product = np.dot(v1, v2)
mag_v1 = np.linalg.norm(v1)
mag_v2 = np.linalg.norm(v2)
angle_rad = np.arccos(dot_product / (mag_v1 * mag_v2))
angle_deg = np.degrees(angle_rad)
print(f"Angulo entre tramo {v1} y {v2} es: {angle_deg} grados")
