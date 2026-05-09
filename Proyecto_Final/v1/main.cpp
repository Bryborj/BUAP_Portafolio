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
#include <algorithm>
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
    bool walls[4] = {true, true, true, true};
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
    sf::RenderWindow window;
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
        int x = grid[index].x;
        int y = grid[index].y;

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
            grid[a].walls[3] = false; // Izquierda
            grid[b].walls[1] = false; // Derecha
        } else if (dx == -1) {
            grid[a].walls[1] = false;
            grid[b].walls[3] = false;
        }

        int dy = grid[a].y - grid[b].y;
        if (dy == 1) {
            grid[a].walls[0] = false; // Top
            grid[b].walls[2] = false; // Bottom
        } else if (dy == -1) {
            grid[a].walls[2] = false;
            grid[b].walls[0] = false;
        }
    }
public:
    MazeApp() : window(sf::VideoMode(WIDTH, HEIGHT), "Generador y Resutor Visual de Laberintos") {
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

//Mapeo a Grafo No Dirigido
void mapToGraph() {
    // Recorrer la cuadricula, si no hay pared entre celda A y B
    // llamar a mazeGraph-add

    for (int i = 0; i < grid.size(); ++i) {
        // Revision Derecha y Abajo
        int right = getIndex(grid[i].x + 1, grid[i].y);
        int down = getIndex(grid[i].x, grid[i].y + 1);

        if (right != -1 && !grid[i].walls[1]) mazeGraph->addEdge(i, right);
        if (down != -1 && !grid[i].walls[2]) mazeGraph->addEdge(i, down);
    }

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
        needToVisit.pop();

        // Reconstrucción del camino más corto
        if (current == goalNode) {
            int temp = goalNode;
            while (temp != -1) {
                finalPath.push_back(temp);
                temp = parent[temp];
            }
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
    for (int i = 0; i < grid.size(); i++) {
        const auto& cell = grid[i];
        int x = cell.x * CELL_SIZE;
        int y = cell.y * CELL_SIZE;

        // Logica gradica para celdas
        sf::RectangleShape cellShape(sf::Vector2f(CELL_SIZE, CELL_SIZE));
        cellShape.setPosition(x,y);
        
        // Colores distintos
        if (currentState == GENERATING) {
            if (grid[i].visited) cellShape.setFillColor(sf::Color(70, 70, 150)); // Morado (visitado)
            else cellShape.setFillColor(sf::Color(50, 50, 50)); // Gris No visitado
            if (i == currentGenCell) cellShape.setFillColor(sf::Color::Yellow); // Celda actual
        } else {
            cellShape.setFillColor(sf::Color(240, 240, 240)); // Pasillos White
            if (isAddedToQueue[i]) cellShape.setFillColor(sf::Color(180, 200, 255)); // Azul claro (Explorado BFS)
        }

        window.draw(cellShape);

        // Dibujar el camino final (Rojo)
        if (currentState == DONE && find(finalPath.begin(), finalPath.end(), i) != finalPath.end()) {
            sf::RectangleShape pathShape(sf::Vector2f(CELL_SIZE, CELL_SIZE));
            pathShape.setPosition(x,y);
            pathShape.setFillColor(sf::Color::Red);
            window.draw(pathShape);
        }

        // Dibujar paredes
        sf::RectangleShape wall;
        wall.setFillColor(sf::Color::Black);
        if (grid[i].walls[0]) { 
            wall.setSize(sf::Vector2f(CELL_SIZE, 2)); 
            wall.setPosition(x, y); window.draw(wall); 
        }
        if (grid[i].walls[1]) { 
            wall.setSize(sf::Vector2f(2, CELL_SIZE)); 
            wall.setPosition(x + CELL_SIZE - 2, y); 
            window.draw(wall); 
        }
        if (grid[i].walls[2]) { 
            wall.setSize(sf::Vector2f(CELL_SIZE, 2)); 
            wall.setPosition(x, y + CELL_SIZE - 2); 
            window.draw(wall); 
        }
        if (grid[i].walls[3]) { 
            wall.setSize(sf::Vector2f(2, CELL_SIZE)); 
            wall.setPosition(x, y); window.draw(wall); 
        }
    }
    window.display();
}

void run() {
    // Bucle de la ventana
    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed) {
                window.close();
            }
        } // end pollEvent

        // Logica de estados
        if (currentState == GENERATING) {
            // Aumento de velocidad generando varias celdas por fotograma
            for (int i = 1; i<5; i++)
                generateMazeStep();
        } else if (currentState == MAPPING) {
            mapToGraph();
        } else if (currentState == SOLVING) {
            solveMazeStep();
            sf::sleep(sf::milliseconds(20)); // Pausa para animar BFS
        }

        draw(); // Redibujar en cada frame
    }
}
}; // Fin clase MazeApp


int main() {
    cout << "Generador y Resolutor Visual de Laberintos CLI" << endl;
    MazeApp app;
    app.run();
    return 0;
}