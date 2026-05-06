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
const int COLS = 20;
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

    // BFS
    queue<int> needToVisit; // FIFO
    vector<boot> visited; // Visitados
    vector<int> parent; // Camino

    // Estados de animación
    enum State { GENERATING, MAPPING, SOLVING, DONE };
    State currentState;

    int getIndex(int x, int y) {
        if (x < 0 || y < 0 || x >= COLS || y >= ROWS) return -1;
        return x + y * COLS;
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
    }
    ~MazeApp() {
        delete mazeGraph;
    }
}

// Backtracking recursivo
void generateMazeStep() {
    // Logica de backtracking con pila (stack)
    // 1. Eligir vecino no visitado
    // 2. TIrar la parend entre la celda actual y el vecino
    // 3. Marcar como visitado y apilar
    // Al terminar, currentState = MAPPING;
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
        currentState = DONE; //NO se encontro solucion
    }
}

int main() {
    cout << "Generador y Resolutor Visual de Laberintos CLI" << endl;
    return 0;
}