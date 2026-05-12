# ======================================================
# Practica 6: Resolución de Problemas de Optimización con el Método Simplex
# Autor: Bryan A. Borges
# Matricula: 202423701
# Materia: Algebra Lineal
# ======================================================

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

def main():
    """
    El problema de optimización lineal es:
    Maximizar Z = 4x1 + 5x2
    Sujeto a:
    3x1 + 2x2 <= 12  (Trabajadores)
    2x1 + 3x2 <= 12  (Materiales)
    x1, x2 >= 0
    """

    # linprog minimiza por defecto, por lo que multiplicamos la función objetivo por -1
    # Z = -4x1 - 5x2
    c = [-4, -5]

    # Matriz de restricciones de desigualdad (lado izquierdo)
    A = [[3, 2],
         [2, 3]]

    # Vector de restricciones de desigualdad (lado derecho)
    b = [12, 12]

    # Límites para x1 y x2 (ambos deben ser >= 0)
    x0_bounds = (0, None)
    x1_bounds = (0, None)

    # Resolvemos el problema utilizando el método Simplex
    # scipy.optimize usa el método 'highs' por defecto que es más avanzado, 
    # pero podemos especificar 'highs' o 'simplex' (legacy). Usaremos 'highs'.
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')

    print("=== Resultados de la Optimización con Simplex ===")
    if res.success:
        print("Estado: Óptimo encontrado con éxito")
        x1_opt = res.x[0]
        x2_opt = res.x[1]
        ganancia_optima = -res.fun # Recordar multiplicar por -1 de vuelta
        
        print(f"Cantidad óptima a producir del Producto 1 (x1): {x1_opt:.2f}")
        print(f"Cantidad óptima a producir del Producto 2 (x2): {x2_opt:.2f}")
        print(f"Ganancia máxima total (Z): {ganancia_optima:.2f}")
        
        # Trabajadores y materiales usados:
        trabajadores_usados = 3 * x1_opt + 2 * x2_opt
        materiales_usados = 2 * x1_opt + 3 * x2_opt
        print(f"Trabajadores utilizados: {trabajadores_usados:.2f} de 12")
        print(f"Materiales utilizados: {materiales_usados:.2f} de 12")
    else:
        print("El problema no pudo ser resuelto:", res.message)

    # Graficar la región factible y el punto óptimo
    x = np.linspace(0, 10, 200)
    
    # 3x1 + 2x2 <= 12  =>  x2 <= (12 - 3x1) / 2
    y1 = (12 - 3*x) / 2
    
    # 2x1 + 3x2 <= 12  =>  x2 <= (12 - 2x1) / 3
    y2 = (12 - 2*x) / 3
    
    plt.figure(figsize=(8, 6))
    
    # Ejes
    plt.plot(x, y1, label=r'$3x_1 + 2x_2 \leq 12$ (Trabajadores)', color='red')
    plt.plot(x, y2, label=r'$2x_1 + 3x_2 \leq 12$ (Materiales)', color='blue')
    
    # Región factible
    y3 = np.minimum(y1, y2)
    plt.fill_between(x, 0, y3, where=(y3>=0)&(x>=0), color='gray', alpha=0.3, label='Región Factible')
    
    # Punto óptimo
    if res.success:
        plt.plot(x1_opt, x2_opt, 'go', markersize=10, label=f'Punto Óptimo ({x1_opt:.2f}, {x2_opt:.2f})')
        
    plt.xlim(0, 6)
    plt.ylim(0, 6)
    plt.xlabel('Producto 1 ($x_1$)')
    plt.ylabel('Producto 2 ($x_2$)')
    plt.title('Solución Gráfica - Optimización de Recursos')
    plt.axhline(0, color='black',linewidth=1)
    plt.axvline(0, color='black',linewidth=1)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    
    # Guardar gráfico
    plt.savefig('Resultados_Graficos_Simplex.png')
    print("\nGráfico de la región factible guardado como 'Resultados_Graficos_Simplex.png'.")

if __name__ == '__main__':
    main()
