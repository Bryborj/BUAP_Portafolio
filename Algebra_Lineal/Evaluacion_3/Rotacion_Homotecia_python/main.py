import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # Configura el backend de Matplotlib para usar TkAgg
import matplotlib.pyplot as plt
import cv2

#Carga de imagen
img  = cv2.imread('/media/brybor/M2_Ext_Bry/Academico/BUAP/Semestres/4to Semestre/Algebra_Lineal/Evaluacion_3/Rotacion_Homotecia_python/imagen.jpeg')


# /media/brybor/M2_Ext_Bry/Academico/BUAP/Semestres/4to Semestre/Algebra_Lineal/Evaluacion_3/Rotacion_Homotecia_python/imagen.jpeg
# Exepción si la imagen no se carga correctamente
if img is None:
    print("Error: No se pudo cargar la imagen.")
    exit()

#Rotación de 90°
rows, cols = img.shape[:2]
M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
rotated_img = cv2.warpAffine(img, M, (cols, rows))

# Rotación de 45°
M_45 = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
rotated_img_45 = cv2.warpAffine(img, M_45, (cols, rows))

# K = 0.5 (escala a la mitad)
scale_matrix_half = np.array([[0.5,0,0],[0,0.5,0]], dtype=np.float32)
scaled_img_half = cv2.warpAffine(img, scale_matrix_half, (cols//2, rows//2))

# Homotecia (escala)
scale_matrix = np.array([[2,0,0],[0,2,0]], dtype=np.float32)
scaled_img = cv2.warpAffine(img, scale_matrix, (cols*2, rows*2))

# Mostrar resultados
plt.subplot(2, 3, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original')
plt.axis("off")

plt.subplot(2, 3, 2)
plt.imshow(cv2.cvtColor(rotated_img, cv2.COLOR_BGR2RGB))
plt.title('Rotada 90°')
plt.axis("off")

plt.subplot(2, 3, 3)
plt.imshow(cv2.cvtColor(rotated_img_45, cv2.COLOR_BGR2RGB))
plt.title('Rotada 45°')
plt.axis("off")

plt.subplot(2, 3, 4)
plt.imshow(cv2.cvtColor(scaled_img, cv2.COLOR_BGR2RGB))
plt.title('Homotecia (Escala x2)')
plt.axis("off")

plt.subplot(2, 3, 5)
plt.imshow(cv2.cvtColor(scaled_img_half, cv2.COLOR_BGR2RGB))
plt.title('Escala 0.5')
plt.axis("off")

plt.show()