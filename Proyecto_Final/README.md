<center>
    <h1>REPORTE TECNICO</h1>
</center>

Estudiante: Bryan Albino Borges.
Matricula: 202423701
Materia: Estructura de datos.
Proyecto: Generador y Resolutor Visual de Laberintos.
Maestro: Daniel Marcelo Gonzalez Arriaga.
Institucion: Benemerita Universidad Autonoma de Puebla.

En el desarrollo de esta aplicación grafica en C++ se ven integrados diversos temas que se vieron a lo largo del curso. En este se ven reflejados: Recursividad, Grafos, Arboles y otros mas para generar un laberinto de forma aleatora (usando Backtraking recursivo) y buscar la solucion con el algoritmo BFS, siendo visualizado todo este proceso mediante una ventana implementando la libreria SFML 2D.

Generación Procedural con Backtracking Recursivo.
Para generar el laberinto implementando una cuadricula inicial. Se utilizo el algoritmo backtraking en el cual se utilizo una Pila para llevar el rastro del del camino en exploración. Desde alguna celda inicial se el algoritmo selecciona un vecino aleatorio no visitado, elimina la pared compartida y apila la celda actual. Si en alguna parte llega a un callejón sin salida realiza un retroceso (genStack.pop();) hasta encontrar una celda con vecinos libres. Usando este concepto matematicamente esta garantizada la creación de un laberinto sin ciclos cerrados y con una sola ruta entre cualquier par de celdas.