from scipy.optimize import linprog

# Maximizar: z = 3x1 + 2x2

#Sujeto a:
#X_1 + X_2 <= 4
#2X_1 + X_2 <= 5
#X_1 + X_2 >= 0


# Coeficientes de la función objetivo (negativos para maximizar)
c = [-3, -2]


# Matriz de restricciones (A_ub * x <= b_ub)
A = [
     [1, 1], 
     [2, 1]
    ]
b = [4, 5]

# Limites de las variables (non-negative)
#x0_bounds = (0, None)
#x1_bounds = (0, None)
bounds = (0, None)

# Aplicar método Simplex
res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

if res.success:
    print(f"Estado: {res.message}")
    print(f"Solución Óptima: x1 = {res.x[0]}, x2 = {res.x[1]}")
    print(f"Valor Máximo de Z: {-res.fun}")
else:
    print("No se pudo encontrar una solución.")