# Práctica 5: Diagonalización de Matrices mediante Vectores Propios

**Procedimiento (Fórmulas y operaciones):**
1. **Matriz A:** $A = \begin{pmatrix} 4 & 1 & 0 \\ 1 & 4 & 0 \\ 0 & 0 & 2 \end{pmatrix}$.
   *   **Polinomio Característico:** $\lambda^3 - 10\lambda^2 + 31\lambda - 30$. Valores propios: $\lambda \in \{5, 3, 2\}$.
   *   Matriz Diagonal $D = \text{diag}(2, 3, 5)$. Se generó la matriz base de vectores propios $P$ y se comprobó algorítmicamente que $P \cdot D \cdot P^{-1} = A$. La matriz **es diagonalizable**.
2. **Matriz B:** $B = \begin{pmatrix} 2 & 1 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{pmatrix}$.
   *   Valores propios: $\lambda = 2$ (multiplicidad algebraica 2), $\lambda = 3$ (multiplicidad algebraica 1).
   *   En el código, se demostró que falla el proceso ya que el espacio propio para $\lambda=2$ es deficiente (dimensión geométrica 1, que es menor a 2).
   *   **No es diagonalizable**.
3. **Matriz E:** $E = \begin{pmatrix} 6 & 0 & 0 \\ 0 & 2 & 1 \\ 0 & 1 & 2 \end{pmatrix}$.
   *   Valores propios: $\lambda \in \{6, 3, 1\}$. Matriz **diagonalizable**, $D = \text{diag}(1, 3, 6)$.

**Evidencia Computacional:**
Se adjuntó el script `p5_script.py` en este directorio, y se resolvió empleando el motor simbólico *SymPy*, el cual validó exitosamente las diagonalizaciones.

**Conclusiones:**
La diagonalización de matrices permite expresar una matriz acoplada en su base ortogonal/propia más sencilla, donde operaciones pesadas computacionalmente como elevar a la potencia resultan elementales. La actividad simulada sirvió para comprobar el axioma matemático fundamental: no toda matriz puede ser diagonalizada; si los vectores propios no logran conformar una base completa que genere al espacio total, el proceso es inviable.
