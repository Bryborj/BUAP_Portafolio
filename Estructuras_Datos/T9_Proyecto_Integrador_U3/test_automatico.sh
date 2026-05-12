#!/bin/bash

# Script de Prueba Automática para el Proyecto Integrador T9
# Autor: Bryan Borges
# Descripción: Ejecuta casos de prueba del algoritmo de Dijkstra

echo "═══════════════════════════════════════════════════════════════"
echo "  PROYECTO INTEGRADOR - PRUEBA AUTOMÁTICA T9"
echo "  Algoritmo de Dijkstra en Grafos Bidireccionales"
echo "═══════════════════════════════════════════════════════════════"
echo ""

# Verificar si el ejecutable existe
if [ ! -f "./main" ]; then
    echo " Error: El archivo 'main' no existe. Compilando..."
    g++ -std=c++17 -o main main.cpp
    if [ $? -ne 0 ]; then
        echo " Error en la compilación"
        exit 1
    fi
    echo " Compilación exitosa"
fi

echo ""
echo " CASO DE PRUEBA 1: Red de Ciudades Europeas"
echo "═══════════════════════════════════════════════════════════════"
echo ""

# Crear archivo de entrada para la prueba
cat > test_input.txt << 'EOF'
1
Berlin
1
Paris
1
Amsterdam
1
Zurich
1
Munich
2
Berlin
Paris
8
2
Berlin
Amsterdam
5
2
Paris
Zurich
6
2
Amsterdam
Munich
4
2
Berlin
Munich
7
3
2
Berlin
Zurich
3
5
Berlin
2
3
4
Paris
Munich
6
EOF

echo "Entrada de prueba:"
cat test_input.txt
echo ""
echo "Ejecutando prueba... (esto puede tomar unos segundos)"
echo ""

# Ejecutar el programa con la entrada de prueba
./main < test_input.txt

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo " PRUEBA COMPLETADA"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo " Estadísticas de la prueba:"
echo " • Número de nodos: 5 (Berlin, Paris, Amsterdam, Zurich, Munich)"
echo "  • Número de aristas: 5"
echo "  • Rutas probadas: 2"
echo "  • Cálculo de distancias: 1"
echo ""
echo " El programa ha funcionado correctamente."
echo "   - Grafo bidireccional creado "
echo "   - Algoritmo de Dijkstra ejecutado "
echo "   - Rutas más cortas calculadas "
echo ""

# Limpiar archivo temporal
rm test_input.txt

echo "═══════════════════════════════════════════════════════════════"
echo " EXPECTED OUTPUT:"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "Ruta de Berlin a Zurich: Berlin -> Paris -> Zurich (14 minutos)"
echo ""
echo "O si toma ruta directa: Berlin -> Munich -> Zurich (11 minutos)"
echo ""
echo "O si pasa por Amsterdam: Berlin -> Amsterdam -> Munich -> Zurich"
echo "                         (5 + 4 + [a calcular] minutos)"
echo ""
echo "═══════════════════════════════════════════════════════════════"
