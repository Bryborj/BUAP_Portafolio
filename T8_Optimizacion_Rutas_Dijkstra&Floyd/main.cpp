#include <iostream>
#include <vector>
#include <queue>

using namespace std;
struct Arista
{
    int destino, peso;
};

void agregarArista(vector<vector<Arista>> &grafo, int origen, int destino, int peso)
{
    grafo[origen].push_back({destino, peso});
}

// Digrafo ponderado
// Nodos: 0 a 4. Aristas dirigidas (Origen -> Destino: Costo)

// Dijkstra (Origen Único),
// Calcular el costo mínimo para envias paquetes desde el nodo 0 hacia los demás nodos.
// grafo representado con Lista de Adtacencia: vector<vector<pair<int, int>>> grafo(vertices);
// Utilizar una cola de prioridad para seleccionar el nodo con el costo mínimo en cada iteración. (priority_queue como min-heap)
void dijkstra(vector<vector<Arista>> &grafo, int origen)
{
    int v = grafo.size();
    const int INF = 1e9;      // Representa un costo infinito
    vector<int> dist(v, INF); // Inicializar distancias con infinito

    priority_queue<
        pair<int, int>,
        vector<pair<int, int>>,
        greater<pair<int, int>>>
        pq;

    dist[origen] = 0;
    pq.push({0, origen});

    while (!pq.empty())
    {
        int costo = pq.top().first;
        int u = pq.top().second;
        pq.pop();

        if (costo > dist[u])
            continue;

        for (Arista a : grafo[u])
        {
            int v = a.destino;
            int peso = a.peso;

            if (dist[u] + peso < dist[v])
            {
                dist[v] = dist[u] + peso;
                pq.push({dist[v], v});
            }
        }
    }

    cout << "Distancias minimas desde el nodo " << origen << ":\n";
    for (int i = 0; i < v; i++)
    {
        cout << "Nodo " << origen << " -> Nodo " << i << " = " << dist[i] << "\n"
             << flush;
    }
}

// Imprimir una tabla de referencia rápida (matriz) que tenga el costo
// minimo de viaje entre cualquier par de nodos.

// Converción de grafo representado con Lista de Adyacencia a Matriz de Adyacencia
vector<vector<int>> matAdy(vector<vector<Arista>> &grafo)
{
    int V = grafo.size();
    const int INF = 1E9;
    vector<vector<int>> mat(V, vector<int>(V, INF));

    for (int i = 0; i < V; i++)
        mat[i][i] = 0;

    for (int u = 0; u < V; u++)
    {
        for (Arista a : grafo[u])
        {
            int v = a.destino;
            mat[u][v] = a.peso;
        }
    }
    return mat;
}
void FloydWarshall(vector<vector<int>> &grafoMatriz)
{
    int V = grafoMatriz.size();
    
    for (int k = 0; k < V; k++)
        for (int i = 0; i < V; i++)
            for (int j = 0; j < V; j++)
                if (grafoMatriz[i][k] + grafoMatriz[k][j] < grafoMatriz[i][j])
                    grafoMatriz[i][j] = grafoMatriz[i][k] + grafoMatriz[k][j];
}

void impMat(vector<vector<int>> &grafoMatriz)
{
    for (int i = 0; i < grafoMatriz.size(); i++)
    {
        for (int j = 0; j < grafoMatriz[i].size(); j++)
        {
            if (grafoMatriz[i][j] == 1e9)
                cout << "INF\t";
            else
                cout << grafoMatriz[i][j] << "\t";
        }
        cout << "\n"
             << flush;
    }
}

int main()
{
    int V = 5;
    vector<vector<Arista>> grafo(V);

    agregarArista(grafo, 0, 1, 10);
    agregarArista(grafo, 0, 3, 5);
    agregarArista(grafo, 1, 2, 1);
    agregarArista(grafo, 1, 3, 2);
    agregarArista(grafo, 2, 4, 4);
    agregarArista(grafo, 3, 1, 3);
    agregarArista(grafo, 3, 2, 9);
    agregarArista(grafo, 3, 4, -5);
    agregarArista(grafo, 4, 0, 7);
    agregarArista(grafo, 4, 2, 6);

    dijkstra(grafo, 0);

    vector<vector<int>> matrizAdyacencia = matAdy(grafo);
    FloydWarshall(matrizAdyacencia);
    cout << "Grafo representado con matriz de Adyacencia:\n";
    impMat(matrizAdyacencia);

    return 0;
}

/**
 * Si el vuelo de 3 -> 4 tuviera un subsidio gubernamental 
 * y su costo pasara a ser $-5k (peso negativo),¿cual de 
 * los dos algoritmos fallarıa y por que?
 * 
 * Respuesta: En el caso es Dijkstra, ya que supone que todos los pesos de las aristas son no negativos.
 *            un peso negativo puede llevar a que el algoritmo no encuentre la ruta más corta correctamente, 
 *            ya que podría seguir explorando rutas que parecen más costosas debido al peso negativo, 
 *            lo que puede resultar en un ciclo negativo y un resultado incorrecto.
 */