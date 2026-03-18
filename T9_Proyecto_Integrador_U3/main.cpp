#include <iostream>
#include <vector>
#include <unordered_map>
#include <map>
#include <queue>
#include <limits>
#include <algorithm>
#include <string>

using namespace std;

// Clase para representar el grafo
class Grafo {
private:
    unordered_map<string, vector<pair<string, int>>> adyacencia;
    
public:
    // Agregar arista bidireccional al grafo
    void agregarArista(const string& nodo1, const string& nodo2, int peso) {
        adyacencia[nodo1].push_back({nodo2, peso});
        adyacencia[nodo2].push_back({nodo1, peso});
    }
    
    // Verificar si un nodo existe
    bool existeNodo(const string& nodo) const {
        return adyacencia.find(nodo) != adyacencia.end();
    }
    
    // Agregar nodo aislado
    void agregarNodo(const string& nodo) {
        if (!existeNodo(nodo)) {
            adyacencia[nodo] = vector<pair<string, int>>();
        }
    }
    
    // Implementar Algoritmo de Dijkstra
    pair<map<string, int>, map<string, string>> dijkstra(const string& inicio) {
        map<string, int> distancias;
        map<string, string> padres;
        priority_queue<pair<int, string>, vector<pair<int, string>>, greater<pair<int, string>>> pq;
        
        // Inicializar distancias
        for (const auto& nodo : adyacencia) {
            distancias[nodo.first] = numeric_limits<int>::max();
            padres[nodo.first] = "";
        }
        
        distancias[inicio] = 0;
        pq.push({0, inicio});
        
        while (!pq.empty()) {
            auto [distActual, nodoActual] = pq.top();
            pq.pop();
            
            if (distActual > distancias[nodoActual]) continue;
            
            for (const auto& [vecino, peso] : adyacencia[nodoActual]) {
                int nuevaDist = distancias[nodoActual] + peso;
                
                if (nuevaDist < distancias[vecino]) {
                    distancias[vecino] = nuevaDist;
                    padres[vecino] = nodoActual;
                    pq.push({nuevaDist, vecino});
                }
            }
        }
        
        return {distancias, padres};
    }
    
    // Obtener la ruta más corta entre dos nodos
    void mostrarRuta(const string& inicio, const string& fin) {
        if (!existeNodo(inicio) || !existeNodo(fin)) {
            cout << "Error: Uno o ambos nodos no existen.\n";
            return;
        }
        
        auto [distancias, padres] = dijkstra(inicio);
        
        if (distancias[fin] == numeric_limits<int>::max()) {
            cout << "No hay ruta entre " << inicio << " y " << fin << ".\n";
            return;
        }
        
        // Reconstruir la ruta
        vector<string> ruta;
        string actual = fin;
        
        while (!actual.empty()) {
            ruta.push_back(actual);
            actual = padres[actual];
        }
        
        reverse(ruta.begin(), ruta.end());
        
        cout << "\n=== Ruta más rápida de " << inicio << " a " << fin << " ===\n";
        cout << "Ruta: ";
        for (size_t i = 0; i < ruta.size(); i++) {
            cout << ruta[i];
            if (i < ruta.size() - 1) cout << " -> ";
        }
        cout << "\nTiempo total: " << distancias[fin] << " minutos\n\n";
    }
    
    // Mostrar todas las distancias desde un nodo
    void mostrarDistancias(const string& nodo) {
        if (!existeNodo(nodo)) {
            cout << "Error: El nodo no existe.\n";
            return;
        }
        
        auto [distancias, _] = dijkstra(nodo);
        
        cout << "\n=== Distancias desde " << nodo << " ===\n";
        for (const auto& [destino, distancia] : distancias) {
            if (distancia == numeric_limits<int>::max()) {
                cout << destino << ": Inalcanzable\n";
            } else {
                cout << destino << ": " << distancia << " minutos\n";
            }
        }
        cout << "\n";
    }
    
    // Mostrar grafo
    void mostrarGrafo() const {
        if (adyacencia.empty()) {
            cout << "El grafo está vacío.\n";
            return;
        }
        
        cout << "\n=== Estructura del Grafo ===\n";
        for (const auto& [nodo, vecinos] : adyacencia) {
            cout << nodo << " -> ";
            for (size_t i = 0; i < vecinos.size(); i++) {
                cout << vecinos[i].first << " (" << vecinos[i].second << " min)";
                if (i < vecinos.size() - 1) cout << ", ";
            }
            cout << "\n";
        }
        cout << "\n";
    }
};

// Funciones globales
Grafo grafo;

void printAboutme();
void menu();
void agregarConexion();
void agregarNodoAislado();
void mostrarGrafo();
void buscarRutaMasRapida();
void mostrarDistanciasDesdeNodo();
void clearScreen();

// Programa principal
int main() {
    printAboutme();
    
    while (true) {
        try {
            menu();
            int choice;
            cout << "Seleccione una opción: ";
            cin >> choice;
            
            switch (choice) {
                case 1:
                    agregarNodoAislado();
                    break;
                case 2:
                    agregarConexion();
                    break;
                case 3:
                    mostrarGrafo();
                    break;
                case 4:
                    buscarRutaMasRapida();
                    break;
                case 5:
                    mostrarDistanciasDesdeNodo();
                    break;
                case 6:
                    cout << "\n¡Gracias por usar el programa! Saliendo...\n";
                    return 0;
                default:
                    cout << "Opción no válida. Por favor, intente de nuevo.\n";
            }
        } catch (const std::exception& e) {
            std::cerr << "Error: " << e.what() << '\n';
        }
    }
    
    return 0;
}

// Implementación de funciones

void menu() {
    cout << "\n════════════════════════════════════════\n";
    cout << "          MENÚ PRINCIPAL\n";
    cout << "════════════════════════════════════════\n";
    cout << "1. Agregar nodo\n";
    cout << "2. Agregar conexión (arista) entre nodos\n";
    cout << "3. Mostrar estructura del grafo\n";
    cout << "4. Buscar ruta más rápida (Dijkstra)\n";
    cout << "5. Mostrar distancias desde un nodo\n";
    cout << "6. Salir\n";
    cout << "════════════════════════════════════════\n";
}

void printAboutme() {
    cout << "\n╔════════════════════════════════════════╗\n";
    cout << "║   PROYECTO INTEGRADOR UNIDAD 3         ║\n";
    cout << "║   ESTRUCTURAS DE DATOS: GRAFOS         ║\n";
    cout << "║   Algoritmo de Dijkstra                ║\n";
    cout << "╠════════════════════════════════════════╣\n";
    cout << "║ Universidad: BUAP                      ║\n";
    cout << "║ Desarrollador: Bryan Borges            ║\n";
    cout << "║ Descripción: Encuentra la ruta más     ║\n";
    cout << "║              rápida entre dos nodos    ║\n";
    cout << "║ Tipo de Grafo: Bidireccional pesado    ║\n";
    cout << "╚════════════════════════════════════════╝\n\n";
}

void agregarNodoAislado() {
    string nodo;
    cout << "Ingrese el nombre del nodo: ";
    cin >> nodo;
    
    if (grafo.existeNodo(nodo)) {
        cout << "El nodo '" << nodo << "' ya existe.\n";
    } else {
        grafo.agregarNodo(nodo);
        cout << "Nodo '" << nodo << "' agregado exitosamente.\n";
    }
}

void agregarConexion() {
    string nodo1, nodo2;
    int peso;
    
    cout << "Ingrese el primer nodo: ";
    cin >> nodo1;
    cout << "Ingrese el segundo nodo: ";
    cin >> nodo2;
    cout << "Ingrese el tiempo (peso en minutos): ";
    cin >> peso;
    
    if (peso <= 0) {
        cout << "Error: El peso debe ser positivo.\n";
        return;
    }
    
    grafo.agregarArista(nodo1, nodo2, peso);
    cout << "Conexión agregada: " << nodo1 << " <-> " << nodo2 
         << " (" << peso << " minutos).\n";
}

void mostrarGrafo() {
    grafo.mostrarGrafo();
}

void buscarRutaMasRapida() {
    string inicio, fin;
    cout << "Ingrese el nodo de inicio: ";
    cin >> inicio;
    cout << "Ingrese el nodo de destino: ";
    cin >> fin;
    
    grafo.mostrarRuta(inicio, fin);
}

void mostrarDistanciasDesdeNodo() {
    string nodo;
    cout << "Ingrese el nodo de referencia: ";
    cin >> nodo;
    
    grafo.mostrarDistancias(nodo);
}

void clearScreen() {
#ifdef _WIN32
    system("pause");
    system("cls");
#else
    cin.get();
    system("clear");
#endif
}