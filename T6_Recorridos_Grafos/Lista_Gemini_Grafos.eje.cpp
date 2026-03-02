#include <iostream>
#include <vector>
#include <queue> // Necesario para BFS
#include <list>

using namespace std;

class RedServidores {
private:
    int numServidores;
    // Lista de adyacencia usando vector de vectores como pide el PDF [cite: 16]
    vector<vector<int>> adj;

public:
    // Constructor
    RedServidores(int n) {
        numServidores = n;
        adj.resize(n); // Redimensionamos el vector para tener n listas
    }

    // Paso 1: Función para agregar aristas bidireccionales [cite: 17]
    void conectar(int u, int v) {
        // Verificamos que los nodos sean válidos para evitar errores
        if (u >= 0 && u < numServidores && v >= 0 && v < numServidores) {
            adj[u].push_back(v);
            adj[v].push_back(u); // Bidireccional: u connecta con v y v con u
        }
    }

    // Paso 2: BFS - Protocolo Broadcast [cite: 22]
    void simularBroadcast(int origen) {
        // Arreglo de visitados para no procesar el mismo servidor dos veces 
        vector<bool> visitados(numServidores, false);
        queue<int> q; // Cola para el orden de procesamiento

        // Marcamos el origen como visitado y lo encolamos
        visitados[origen] = true;
        q.push(origen);

        cout << "--- Inicio Protocolo Broadcast (BFS) desde Servidor " << origen << " ---" << endl;

        while (!q.empty()) {
            int actual = q.front();
            q.pop();

            // Imprimimos el servidor actual (simulando recepción de alerta) [cite: 24]
            cout << "Alerta recibida en Servidor: " << actual << endl;

            // Recorremos los vecinos del servidor actual
            for (int vecino : adj[actual]) {
                if (!visitados[vecino]) {
                    visitados[vecino] = true; // Importante marcar antes de encolar
                    q.push(vecino);
                }
            }
        }
        cout << "--- Fin del Broadcast ---\n" << endl;
    }

    // Paso 3: DFS - Rastreo de Ruta (Recursivo) 
    bool rastrearPaquete(int actual, int destino, vector<bool>& visitados) {
        // Marcar nodo actual como visitado [cite: 30]
        visitados[actual] = true;
        cout << "Explorando Servidor: " << actual << endl;

        // Caso Base: Si llegamos al destino, retornamos true [cite: 31]
        if (actual == destino) {
            cout << ">> ¡Paquete entregado exitosamente en el Servidor " << destino << "!" << endl;
            return true;
        }

        // Caso Recursivo: Explorar vecinos
        for (int vecino : adj[actual]) {
            if (!visitados[vecino]) {
                // Si la llamada recursiva retorna true, propagamos el true hacia arriba
                if (rastrearPaquete(vecino, destino, visitados)) {
                    return true;
                }
            }
        }

        // Backtracking: Si exploramos todos los vecinos y no encontramos el destino
        // (En este caso simple de solo buscar, no desmarcamos visitados para evitar ciclos infinitos en grafos cíclicos)
        return false;
    }
};

int main() {
    // 1. Instanciar la red con 6 nodos (0 al 5) [cite: 18]
    RedServidores red(6);

    // Agregar las conexiones descritas en el escenario [cite: 7-13]
    // Nota: Como es bidireccional, solo necesitamos declarar la conexión una vez por par.
    
    // Conexiones del 0
    red.conectar(0, 1);
    red.conectar(0, 2);
    
    // Conexiones del 1 (0 ya está)
    red.conectar(1, 3);
    
    // Conexiones del 2 (0 ya está)
    red.conectar(2, 4);
    
    // Conexiones del 3 (1 ya está)
    red.conectar(3, 4);
    red.conectar(3, 5);
    
    // Conexiones del 4 (2 y 3 ya están)
    red.conectar(4, 5); 
    
    // Conexiones del 5 (3 y 4 ya están) -> Listo.

    // --- PRUEBA 1: BFS --- [cite: 34]
    red.simularBroadcast(0);

    // --- PRUEBA 2: DFS --- [cite: 35]
    cout << "--- Inicio Rastreo de Paquete (DFS) de 0 a 5 ---" << endl;
    
    // El PDF pide crear el vector de visitados fuera y pasarlo por referencia 
    vector<bool> visitadosDFS(6, false);
    
    bool encontrado = red.rastrearPaquete(0, 5, visitadosDFS);
    
    if (!encontrado) {
        cout << "Error: No se pudo encontrar una ruta al destino." << endl;
    }

    return 0;
}