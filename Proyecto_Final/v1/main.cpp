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
}

int main() {
    cout << "Generador y Resolutor Visual de Laberintos CLI" << endl;
    return 0;
}