#include <bits/stdc++.h>
#include <vector>

using namespace std;

class RedServidores {
private:
    int V;
    vector<vector<int>> grafo;

public:
    RedServidores(int vertices) : V(vertices), grafo(vertices) {}
    void conectar(int u, int v) {
        grafo[u].push_back(v);
        grafo[v].push_back(u);
    }

    void simularBroadcast(int origen) {
        vector<bool> visitado(V, false);
        std::queue<int> q;
        visitado[origen] = true;
        q.push(origen);

        while (!q.empty()) {
            int actual = q.front();
            q.pop();
            cout << "Servidor " << actual << " recibió el mensaje." << endl;

            for (int vecino : grafo[actual]) {
                if (!visitado[vecino]) {
                    visitado[vecino] = true;
                    q.push(vecino);
                }
            }
        }
    }

    bool rastrearPaquete(int actual, int destino, vector<bool>& visitado) {
        if (actual == destino) {
            cout << "\nPaquete entregado en el servidor " << destino << "." << flush;
            return true;
        }
        visitado[actual] = true;
        cout << "\nExplorando servidor " << actual << "..." << flush;

        for (int vecino : grafo[actual]) {
            if (!visitado[vecino]) {
                if (rastrearPaquete(vecino, destino, visitado)) {
                    return true;
                }
            }
        }
        return false;
    }
};

int main() {
    cout << "Simulación de Red de Servidores utilizando Lista de Adyacencia" << flush;
    cout << "Creando red de servidores..." << flush;
    RedServidores red(6);
    red.conectar(0, 1);
    red.conectar(0, 2);
    red.conectar(1, 3);
    red.conectar(2, 4);
    red.conectar(3, 4);
    red.conectar(3, 5);
    red.conectar(4, 5);
    cout << "Simulación de Broadcast:" << flush;
    red.simularBroadcast(0);
    cout << "\nRastreo de paquete desde el servidor 0 al servidor 5: \n" << flush;
    vector<bool> visitado(6, false);
    if (red.rastrearPaquete(0, 5, visitado)) {
        cout << "El paquete fue rastreado exitosamente." << endl;
    } else {
        cout << "No se pudo rastrear el paquete." << endl;
    }
    return 0;
}
