import sympy as sp
from sympy.matrices.exceptions import MatrixError

A = sp.Matrix([[4, 1, 0], [1, 4, 0], [0, 0, 2]])
print("--- MATRIZ A ---")
print(f"Polinomio característico: {A.charpoly().as_expr()}")
print(f"Valores propios: {A.eigenvals()}")
print(f"Vectores propios: {A.eigenvects()}")
P, D = A.diagonalize()
print(f"P:\n{P}")
print(f"D:\n{D}")
print(f"Comprobación P * D * P^-1 == A: {P * D * P.inv() == A}\n")

B = sp.Matrix([[2, 1, 0], [0, 2, 0], [0, 0, 3]])
print("--- MATRIZ B ---")
print(f"Polinomio característico: {B.charpoly().as_expr()}")
print(f"Valores propios: {B.eigenvals()}")
print(f"Vectores propios: {B.eigenvects()}")
try:
    P_B, D_B = B.diagonalize()
except Exception as e:
    print(f"No se puede diagonalizar B: {e}\n")

E = sp.Matrix([[6, 0, 0], [0, 2, 1], [0, 1, 2]])
print("--- MATRIZ E (Equipo) ---")
print(f"Polinomio característico: {E.charpoly().as_expr()}")
print(f"Valores propios: {E.eigenvals()}")
print(f"Vectores propios: {E.eigenvects()}")
P_E, D_E = E.diagonalize()
print(f"P_E:\n{P_E}")
print(f"D_E:\n{D_E}")
print(f"Comprobación P_E * D_E * P_E^-1 == E: {P_E * D_E * P_E.inv() == E}")
