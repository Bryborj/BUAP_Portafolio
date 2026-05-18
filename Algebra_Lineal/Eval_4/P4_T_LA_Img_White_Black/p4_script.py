import numpy as np
import matplotlib.pyplot as plt
import cv2

# Crear una imagen de prueba (patrón de anillos)
x = np.linspace(-3, 3, 256)
y = np.linspace(-3, 3, 256)
X, Y = np.meshgrid(x, y)
G = np.sin(X**2 + Y**2)
G = (G - G.min()) / (G.max() - G.min()) # normalizar a [0, 1]

print(f"Tamaño: {G.shape[0]} x {G.shape[1]} (dimensión vectorial = {G.size})")

alpha = 1.5
T1 = alpha * G
T1 = np.clip(T1, 0, 1)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(G, cmap='gray', vmin=0, vmax=1)
plt.title('Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(T1, cmap='gray', vmin=0, vmax=1)
plt.title('T(G) = 1.5 * G')
plt.axis('off')

plt.savefig('plot_contraste.png')

# Filtro promedio (Blur)
K = np.ones((5, 5)) / 25.0
G_blur = cv2.filter2D(G, -1, K, borderType=cv2.BORDER_REPLICATE)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(G, cmap='gray', vmin=0, vmax=1)
plt.title('Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(G_blur, cmap='gray', vmin=0, vmax=1)
plt.title('Filtro promedio (Lineal)')
plt.axis('off')

plt.savefig('plot_blur.png')

# Filtro detección de bordes (Laplaciano)
K_edge = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
G_edge = cv2.filter2D(G, -1, K_edge)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(G, cmap='gray', vmin=0, vmax=1)
plt.title('Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(np.abs(G_edge), cmap='gray')
plt.title('Detección de Bordes')
plt.axis('off')

plt.savefig('plot_bordes.png')
