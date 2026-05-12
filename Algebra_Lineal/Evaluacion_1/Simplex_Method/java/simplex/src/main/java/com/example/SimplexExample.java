package com.example;

import org.apache.commons.math3.optim.PointValuePair;
import org.apache.commons.math3.optim.linear.*;
import org.apache.commons.math3.optim.nonlinear.scalar.GoalType;
import java.util.ArrayList;
import java.util.Collection;

public class SimplexExample {
    public static void main(String[] args) {
        // 1. Definir la función objetivo: 3x1 + 2x2
        // El tercer parámetro (0) es el valor constante
        LinearObjectiveFunction f = new LinearObjectiveFunction(new double[] { 3, 2 }, 0);

        // 2. Definir las restricciones
        Collection<LinearConstraint> constraints = new ArrayList<>();
        
        // x1 + x2 <= 4
        constraints.add(new LinearConstraint(new double[] { 1, 1 }, Relationship.LEQ, 4));
        
        // 2x1 + x2 <= 5
        constraints.add(new LinearConstraint(new double[] { 2, 1 }, Relationship.LEQ, 5));

        // 3. Configurar el optimizador (SimplexSolver)
        SimplexSolver solver = new SimplexSolver();
        
        try {
            // Resolver: Maximizando, con variables no negativas (true)
            PointValuePair solution = solver.optimize(
                f, 
                new LinearConstraintSet(constraints), 
                GoalType.MAXIMIZE, 
                new NonNegativeConstraint(true)
            );

            // 4. Mostrar resultados
            double[] vars = solution.getPoint();
            System.out.println("--- Solución Óptima ---");
            System.out.println("x1 = " + vars[0]);
            System.out.println("x2 = " + vars[1]);
            System.out.println("Valor Máximo (z) = " + solution.getValue());

        } catch (NoFeasibleSolutionException e) {
            System.out.println("No se encontró una solución factible.");
        }
    }
}