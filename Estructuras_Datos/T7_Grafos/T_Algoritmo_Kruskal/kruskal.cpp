#include <vector>
#include <bits/stdc++.h>

using namespace std;

struct Arista {
    int origen, destino, peso;
};

class Disjoint {
private:
    vector<int> padre, rango;
public:
    Disjoint(int n) {
        padre.resize(n);
        rango.resize(n);
        for (int i = 0; i < n; i++) {
            padre[i] = i;
            rango[i] = 1;
        }
    }

    int buscar(int i) {
        return (padre[i] == i) ? i : (padre[i] = buscar(padre[i]));
    }

    void unir(int i, int j) {
        int s1 = buscar(i), s2 = buscar(j);
        if (s1 != s2) {
            if (rango[s1] < rango[s2]) padre[s1] = s2;
            else if (rango[s1] > rango[s2]) padre[s2] = s1;
            else padre[s2] = s1, rango[s1]++;
        }
    }
};

/*bool comparar(vector<int> &a, vector<int> &b) {
    return a[2] < b[2];
}*/

bool comparar(const Arista &a, const Arista &b) {
    return a.peso < b.peso;
}

int kruskal(int n, vector<Arista> &arista) {
    std::sort(arista.begin(), arista.end(), comparar);
    Disjoint ds(n);
    int costo = 0, contador = 0;
    for (auto &e : arista) {
        int x = e.origen, y = e.destino, w = e.peso;
        if (ds.buscar(x) != ds.buscar(y)) {
            ds.unir(x, y);
            cout << " Arista " << x << "|" << y << " # Peso: " << w << endl;
            costo += w;
            if (++contador == n-1) break;
        }
    }
    return costo;
}

int main() {
    vector<Arista> arista = {
        {0, 1, 4},
        {0, 2, 2},
        {1, 2, 5},
        {1, 3, 10},
        {2, 2, 5},
        {2, 3, 8},
        {2, 4, 3},
        {3, 4, 6}
    };

    int n = 6, costo = kruskal(n, arista);
    cout << "Costo total: $" << costo << " MDP\n" << flush;
    return 0;
}