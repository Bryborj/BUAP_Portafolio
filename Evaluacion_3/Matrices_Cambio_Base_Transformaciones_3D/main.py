# ======================================================
# Practica 5: Matrices de cambio de base en transformaciones 3D
# Autor: Bryan A. Borges
# Matricula: 202423701
# Materia: Algebra Lineal
# ======================================================


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def plot_cube(ax, vertices, color, alpha=0.5, label=''):
    # Define las 6 caras del cubo usando los índices de los vértices
    faces = [
        [vertices[0], vertices[1], vertices[2], vertices[3]], # Base inferior
        [vertices[4], vertices[5], vertices[6], vertices[7]], # Base superior
        [vertices[0], vertices[1], vertices[5], vertices[4]], # Cara frontal
        [vertices[2], vertices[3], vertices[7], vertices[6]], # Cara trasera
        [vertices[1], vertices[2], vertices[6], vertices[5]], # Cara lateral derecha
        [vertices[0], vertices[3], vertices[7], vertices[4]]  # Cara lateral izquierda
    ]
    # Se agrega la colección 3D al plot
    collection = Poly3DCollection(faces, facecolors=color, linewidths=1, edgecolors='black', alpha=alpha)
    ax.add_collection3d(collection)
    
    # Se plotean los vértices para forzar los límites de los ejes y tener el label en la leyenda
    x, y, z = vertices[:, 0], vertices[:, 1], vertices[:, 2]
    ax.scatter(x, y, z, color=color, label=label)

def main():
    # ==========================================
    # Paso 1: Definir vértices de un cubo
    # ==========================================
    vertices = np.array([
        [0, 0, 0],
        [1, 0, 0],
        [1, 1, 0],
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 1],
        [1, 1, 1],
        [0, 1, 1]
    ])

    # ==========================================
    # Paso 2: Definir nueva base (45 grados)
    # ==========================================
    theta = np.deg2rad(45)  # 45 grados
    v1 = np.array([np.cos(theta), np.sin(theta), 0])
    v2 = np.array([-np.sin(theta), np.cos(theta), 0])
    v3 = np.array([0, 0, 1])

    # ==========================================
    # Paso 3: Construir matriz P
    # ==========================================
    P = np.column_stack((v1, v2, v3))

    # ==========================================
    # Paso 4: Transformar puntos
    # ==========================================
    vertices_transformados = vertices @ P

    # ==========================================
    # Paso 5: Graficar (45 grados)
    # ==========================================
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    plot_cube(ax, vertices, 'blue', alpha=0.1, label='Original')
    plot_cube(ax, vertices_transformados, 'green', alpha=0.5, label='Transformado (45°)')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Transformación con Base Ortonormal (Rotación 45°)')
    ax.legend()
    
    # Ajuste dinámico de los límites
    all_v = np.vstack((vertices, vertices_transformados))
    ax.set_xlim([np.min(all_v[:,0])-0.5, np.max(all_v[:,0])+0.5])
    ax.set_ylim([np.min(all_v[:,1])-0.5, np.max(all_v[:,1])+0.5])
    ax.set_zlim([np.min(all_v[:,2])-0.5, np.max(all_v[:,2])+0.5])
    plt.savefig('Resultados/01_transformacion_45_grados.png')
    plt.close()

    # ==========================================
    # Implementación de instrucciones de la práctica
    # ==========================================

    # 1. Modificar el ángulo de rotación (ej: 60 grados)
    theta_60 = np.pi / 3 # 60 grados
    v1_60 = np.array([np.cos(theta_60), np.sin(theta_60), 0])
    v2_60 = np.array([-np.sin(theta_60), np.cos(theta_60), 0])
    v3_60 = np.array([0, 0, 1])
    P_60 = np.column_stack((v1_60, v2_60, v3_60))
    vertices_trans_60 = vertices @ P_60

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    plot_cube(ax, vertices, 'blue', alpha=0.1, label='Original')
    plot_cube(ax, vertices_trans_60, 'orange', alpha=0.5, label='Transformado (60°)')
    ax.set_title('Transformación con Base Ortonormal (Rotación 60°)')
    ax.legend()
    all_v_60 = np.vstack((vertices, vertices_trans_60))
    ax.set_xlim([np.min(all_v_60[:,0])-0.5, np.max(all_v_60[:,0])+0.5])
    ax.set_ylim([np.min(all_v_60[:,1])-0.5, np.max(all_v_60[:,1])+0.5])
    ax.set_zlim([np.min(all_v_60[:,2])-0.5, np.max(all_v_60[:,2])+0.5])
    plt.savefig('Resultados/02_transformacion_60_grados.png')
    plt.close()

    # 2. Definir otra base no ortogonal (Shear / Sesgo)
    u1 = np.array([1, 0, 0])
    u2 = np.array([0.5, 1, 0])
    u3 = np.array([0, 0, 1])
    P_no_orto = np.column_stack((u1, u2, u3))
    vertices_trans_no_orto = vertices @ P_no_orto

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    plot_cube(ax, vertices, 'blue', alpha=0.1, label='Original')
    plot_cube(ax, vertices_trans_no_orto, 'purple', alpha=0.5, label='Transformado (No Ortogonal)')
    ax.set_title('Transformación con Base No Ortogonal (Sesgo)')
    ax.legend()
    all_v_no = np.vstack((vertices, vertices_trans_no_orto))
    ax.set_xlim([np.min(all_v_no[:,0])-0.5, np.max(all_v_no[:,0])+0.5])
    ax.set_ylim([np.min(all_v_no[:,1])-0.5, np.max(all_v_no[:,1])+0.5])
    ax.set_zlim([np.min(all_v_no[:,2])-0.5, np.max(all_v_no[:,2])+0.5])
    plt.savefig('Resultados/03_transformacion_no_ortogonal.png')
    plt.close()

    # 3. Calcular la inversa de P
    P_inv = np.linalg.inv(P)
    print("--- 3. Matriz Inversa ---")
    print("Matriz P (Base Original de 45°):")
    print(P)
    print("\nInversa de P:")
    print(P_inv)

    # 4. Verificar que: np.linalg.inv(P) @ (vertices @ P).T recupera las coordenadas originales
    recuperados_pdf = (P_inv @ (vertices @ P).T).T
    print("\n--- 4. Verificación de Recuperación de Coordenadas ---")
    print("Coordenadas Originales:")
    print(vertices)
    print("\nCoordenadas Recuperadas con la fórmula del PDF [ np.linalg.inv(P) @ (vertices @ P).T ].T :")
    print(np.round(recuperados_pdf, decimals=5))
    
    son_iguales_pdf = np.allclose(vertices, recuperados_pdf)
    print(f"¿Las coordenadas coinciden con la fórmula del PDF?: {'Sí' if son_iguales_pdf else 'No'}")

    print("\nNota: La fórmula sugerida en el PDF asume una convención diferente de vectores fila/columna.")
    print("Al aplicar 'vertices @ P' estamos multiplicando vectores fila. Por lo tanto, la recuperación correcta es post-multiplicando por la inversa:")
    
    recuperados_correctos = (vertices @ P) @ P_inv
    print("\nCoordenadas Recuperadas correctamente con [ (vertices @ P) @ np.linalg.inv(P) ]:")
    print(np.round(recuperados_correctos, decimals=5))
    
    son_iguales_correctos = np.allclose(vertices, recuperados_correctos)
    print(f"¿Las coordenadas coinciden con la fórmula corregida?: {'Sí' if son_iguales_correctos else 'No'}")

if __name__ == "__main__":
    main()
