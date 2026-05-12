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

###### Generación Procedural con Backtracking Recursivo.

Para generar el laberinto implementando una cuadricula inicial. Se utilizo el algoritmo backtraking en el cual se utilizo una Pila para llevar el rastro del del camino en exploración. Desde alguna celda inicial se el algoritmo selecciona un vecino aleatorio no visitado, elimina la pared compartida y apila la celda actual. Si en alguna parte llega a un callejón sin salida realiza un retroceso (genStack.pop();) hasta encontrar una celda con vecinos libres. Usando este concepto matematicamente esta garantizada la creación de un laberinto sin ciclos cerrados y con una sola ruta entre cualquier par de celdas.

###### Mapeo de grafo.

Una vez generado el laberinto se transforma en un Grafo No Dirigido. Cada celda es un vertice mientras cada pasillo representa un arista. Se utilizaron Listas de Adyacencia en lugar de matrices asiendo esta estructura ideal para ahorar memoria, ya que el laberinto es un grafo disperso donde cada nodo tiene como maximo 4 vecinos.

###### Resolucion.

La resolución del laberinto se realiza con el algoritmo de Búsqueda a lo Ancho (BFS) en la exploración del grafo se realiza expandiéndose nivel por nivel en todas las direcciones posibles, asegurando encontrar el camino más corto de forma óptima. Se ha empleado un cola basada en el principio FIFO para programar las visitas a las celdad adyacentes, así mismo, se utiliza un arreglo de visitados para evitar prosesar la misma celdad dos veces y una arreglo de predecesores que permite rastrear y pintar el recorrido final desde la meta hasta el inicio. Tambien fue añadido un limite de fotogramas a 120 y la posibilidad de reiniciar el programa presionando la tecla "R"
