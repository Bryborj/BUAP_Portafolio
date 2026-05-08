/*
Bryan Albino Borges
Estructuras de Datos
Problema: Generador y Resolutor Visual de Laberintos CLI
version: 1.0.0
Starging proyect: 2026-05-05
End proyect: ----
*/

#include <SFML/Graphics.hpp>
#include <vector>
#include <stack>
#include <queue>
#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

// Configs
const int CELL_SIZE = 30;
const int COLS = 25;
const int ROWS = 20;
const int WIDTH = COLS * CELL_SIZE;
const int HEIGHT = ROWS * CELL_SIZE;

// Estructura de las celdas
struct Cell {
    int x, y;
    bool walls[3] = (true, true, true, true);
    bool visited = false;
};

// Grafo usando listas de adyacencia
class Graph {
    public:
    int vertices;
    vector<vector<int>> adj;

    Graph(int n) : vertices(n) {
        adj.resize(n);
    }

    void addEdge(int u, int v) {
        adj[u].push_back(v);
        adj[v].push_back(u); // Grafo no dirigido
    }
};

// Clase principal
class MazeApp {
private: 
    sf::RenderWIndow window;
    vector<Cell> grid;
    Graph* mazeGraph;

    // Variables generación
    stack<int> genStack;
    int currentGenCell;

    // BFS
    queue<int> needToVisit; // FIFO
    vector<bool> isAddedToQueue; // Visitados
    vector<int> parent; // Camino
    vector<int> finalPath; // Camino final

    // Estados de animación
    enum State { GENERATING, MAPPING, SOLVING, DONE };
    State currentState;

    int getIndex(int x, int y) {
        if (x < 0 || y < 0 || x >= COLS || y >= ROWS) return -1;
        return x + y * COLS;
    }

    // Retornar vecinos no visitados para el backtracking
    vector<int> getUnvisitedNeighbors(int index) {
        vector<int> neighbors;
        int x = grid(index).x;
        int y = grid(index).y;

        int top = getIndex(x, y - 1);
        int bottom = getIndex(x, y + 1);
        int left = getIndex(x - 1, y);
        int right = getIndex(x + 1, y);

        if (top != -1 && !grid[top].visited) neighbors.push_back(top);
        if (right != -1 && !grid[right].visited) neighbors.push_back(right);
        if (bottom != -1 && !grid[bottom].visited) neighbors.push_back(bottom);
        if (left != -1 && !grid[left].visited) neighbors.push_back(left);

        return neighbors;
    }

    // Eliminar pared entre dos celdas adyacentes
    void removeWalls(int a, int b) {
        int dx = grid[a].x - grid[b].x;
        if (dx == 1) {
            grid[a].walls[4] = false; // Izquierda
            grid[b].walls[5] = false; // Derecha
        } else if (dx == -1) {
            grid[a].walls[5] = false;
            grid[b].walls[4] = false;
        }

        int dy = grid[a].y - grid[b].y;
        if (dy == 1) {
            grid[a].walls = false;
            grid[b].walls[6] = false;
        } else if (dy == -1) {
            grid[a].walls[6] = false;
            grid[b].walls = false;
        }
    }
public:
    MazeApp() : window(sf::videoMode(WIDTH, HEIGHT), "Generador y Resutor Visual de Laberintos") {
        srand(time(NULL));
        // Cuadricula
        for (int y = 0; y < ROWS; y++) {
            for (int x = 0; x < COLS; x++) {
                Cell cell;
                cell.x = x;
                cell.y = y;
                grid.push_back(cell);
            }
        }
        mazeGraph = new Graph(COLS * ROWS);
        currentState = GENERATING;

        currentGenCell = 0;
        grid[currentGenCell].visited = true;
        genStack.push(currentGenCell);
    }
    ~MazeApp() {
        delete mazeGraph;
    }
}

// Backtracking recursivo Iterativo (Pila)
void generateMazeStep() {
    if (!genStack.empty()) {
        vector<int> neighbors = getUnvisitedNeighbors(currentGenCell);
        if (!neighbors.empty()) {
            int next = neighbors[rand() % neighbors.size()]; // Elección de vecino
            genStack.push(currentGenCell);
            removeWalls(currentGenCell, next);
            currentGenCell = next;
            grid[currentGenCell].visited = true;
        } else {
            currentGenCell = genStack.top(); // Retroceso (backtrack)
            genStack.pop();
        }
    } else {
        currentState = MAPPING; // Termina generacion, pasamos a mapeo
    }
}

//Mapeo a Grado
void mapToGraph() {
    // Recorrer la cuadricula, si no hay pared entre celda A y B
    // llamar a mazeGraph-add

    // Preparando BFS
    isAddedToQueue.assign(COLS * ROWS, false);
    parent.assign(COLS * ROWS, -1);

    int startNode = 0;
    needToVisit.push(startNode);
    isAddedToQueue[startNode] = true;

    currentState = SOLVING;
}

// Busqueda a lo ancho (BFS)
void solveMazeStep() {
    int goalNode = (COLS * ROWS) - 1; // Ultima celda

    if (!needToVisit.empty()) {
        int current = needToVisit.front();
        needToVisit.pop;

        // Al llegar a la meta, terminar y reconstruir el camino
        if (current == goalNode) {
            currentState = DONE;
            return;
        }

        // Explorar vecinos
        for (int neighbor : mazeGraph->adj[current]) {
            if (!isAddedToQueue[neighbor]) {
                isAddedToQueue[neighbor] = true;
                parent[neighbor] = current; // Guarda el rastro
                needToVisit.push(neighbor);
            }
        }
    } else {
        currentState = DONE; //No se encontro solucion
    }
}

// Dibujo del laberinto en SFML POO
void draw() {
    window.clear(sf::Color::Black);

    // Celdas y paredes
    for (const auto& cell : grid) {
        int x = cell.x * CELL_SIZE;
        int y = cell.y * CELL_SIZE;

        // Logica gradica para celdas
        // Lineas de pared
        // Colores distintos
        // isAddedToQueue[getIndex(cell.x, cell.y)] == true -> Animacion
    }

    window.display();
}

void run() {
    // Bucle de la ventana
    while (window.isOpen()) {
        sf::Event event,
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed) {
                window.close();
            }

            // Estados para animar el proceso
            if (currentState == GENERATING) 
                generateMazeStep();
            else if (currentState == MAPPING)
                mapToGraph();
            else if (currentState == SOLVING) {
                solveMazeStep();
                sf::sleep(sf::milliseconds(50)); // Control de velocidad de animación
            }

            draw(); // Redibujar en cada frame
        }
    }
}


int main() {
    cout << "Generador y Resolutor Visual de Laberintos CLI" << endl;
    MazeApp app;
    app.run();
    return 0;
}