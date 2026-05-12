#include <iostream>
#include <vector>
#include <queue>

/**
 * Implementación del algoritmo de Prim para encontrar el árbol de expansión mínima en un grafo no dirigido.
 * El grafo se representa mediante una lista de adyacencia, donde cada nodo tiene una lista de conexiones (destino y costo).
 * El algoritmo utiliza una cola de prioridad para seleccionar la arista de menor costo en cada paso, asegurando que se construya un árbol de expansión mínima.
 * Al finalizar, se muestra la lista de aristas seleccionadas y el costo total del árbol de expansión mínima.
 * 
 * Nota: Este código asume que el grafo es conexo y no dirigido, y que los costos de las aristas son positivos.
 * 
 * Autor: Bryan Albino Borges
 * Curso: Estructura de Datos
 * Fecha: 2026-03-07
 * Versión: 1.0
 */

using namespace std;

struct Conexion
{
    int destino, costo;
};

struct AristaPQ
{
    int origen, destino, costo;
    bool operator<(const AristaPQ &otra) const
    {
        return costo > otra.costo;
    }
};

class Grafo
{
public:
    int V; 
    vector<vector<Conexion>> grafo;
    vector<bool> visitado;

    Grafo(int vertices) : V(vertices)
    {
        grafo.resize(V);
        visitado.resize(V, false);
    }

    void agregarArista(int origen, int destino, int costo)
    {
        grafo[origen].push_back({destino, costo});
        grafo[destino].push_back({origen, costo});
    }
};

std::string format_num(long long num) {
    std::string s = std::to_string(num);
    int pos = s.length() - 3;

    while (pos > 0) {
        s.insert(pos, ",");
        pos -= 3;
    }

    return s;
}

void prim(vector<vector<Conexion>> &grafo)
{
    int V = grafo.size();
    vector<bool> visitado(V, false);
    vector<AristaPQ> mst;
    int totalCosto = 0;
    priority_queue<AristaPQ> pq;

    visitado[0] = true; // Ndo 0
    for (const auto &con : grafo[0]) {
        pq.push({0, con.destino, con.costo});
    }

    while (!pq.empty() && mst.size() < V - 1) {
        AristaPQ arista = pq.top();
        pq.pop();
        if (visitado[arista.destino]) continue;
        visitado[arista.destino] = true;
        mst.push_back(arista);
        totalCosto += arista.costo;
        for (const auto &con : grafo[arista.destino]) {
            if (!visitado[con.destino]) {
                pq.push({arista.destino, con.destino, con.costo});
            }
        }
    }

    cout << "Aristas del árbol de expansión mínima (Prim):\n";
    for (const auto &arista : mst) {
        cout << arista.origen << " - " << arista.destino << " (costo: " << arista.costo << ")\n";
    }
    cout << "Costo total: $" << format_num(totalCosto * 1000) << " Dolares \n" << flush;
}

int main()
{
    int vertices = 9;
    Grafo g(vertices);

    g.agregarArista(0, 1, 10);
    g.agregarArista(0, 2, 15);
    g.agregarArista(1, 2, 5);
    g.agregarArista(1, 3, 12);
    g.agregarArista(2, 3, 8);
    g.agregarArista(2, 4, 10);
    g.agregarArista(3, 4, 2);
    g.agregarArista(3, 5, 6);
    g.agregarArista(4, 5, 7);

    prim(g.grafo);
    return 0;
}