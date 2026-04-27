/**
 * @file
 * @author Bryan A Borges
 * @brief 
 * @version 0.1
 * @date 2026-04-24
 */

#include <iostream>
#include <vector>
#include <list>
#include <string>

using namespace std;

struct RegistroDNS {
    string url;
    string ip;
};

class CacheDNS {
private:
    int m; 
    int p; 
    vector<list<RegistroDNS>> tabla;

public:
    CacheDNS(int tamano = 11, int primo = 31) {
        m = tamano;
        p = primo;
        tabla.resize(m);
    }

    // Función hash polinomial h(s) = sum(s[i] * p^i) mod m
    int hashString(string url) {
        long long hashValue = 0;
        long long p_pow = 1;
        
        for (char c : url) {
            hashValue = (hashValue + c * p_pow) % m;
            p_pow = (p_pow * p) % m;
        }
        
        return hashValue;
    }

    // Funciones del Sistema
    // Insertar o actualizar un registro
    void insertar(string url, string ip) {
        int indice = hashString(url);
        
        // Recorrer la lista para actualizar si la URL ya existe
        for (auto& registro : tabla[indice]) {
            if (registro.url == url) {
                registro.ip = ip;
                return;
            }
        }
        
        // Si no existe, insertar un nuevo registro al final de la lista correspondiente
        tabla[indice].push_back({url, ip});
    }

    // Buscar un registro y retornar la IP
    string buscar(string url) {
        int indice = hashString(url);
        
        // Buscar a lo largo de la lista ligada (Manejo de colisiones)
        for (const auto& registro : tabla[indice]) {
            if (registro.url == url) {
                return registro.ip; // Retornar IP si se encuentra
            }
        }
        
        return "No encontrado"; // Retornar este string si no se encontró
    }

    // Mostrar el estado interno de la Tabla Hash
    void mostrarTabla() {
        for (int i = 0; i < m; ++i) {
            cout << "Indice [" << i << "]: ";
            for (const auto& registro : tabla[i]) {
                cout << "[" << registro.url << " | " << registro.ip << "] -> ";
            }
            cout << "NULL" << endl;
        }
    }
};

int main() {
    // Inicializamos el CacheDNS con tabla de tamaño 11
    CacheDNS cache(11);

    // Pruebas
    // 10 dominios diferentes
    cache.insertar("google.com", "142.250.190.46");
    cache.insertar("youtube.com", "142.250.190.78");
    cache.insertar("github.com", "140.82.113.3");
    cache.insertar("unam.mx", "132.248.10.2");
    cache.insertar("buap.mx", "148.228.1.1");
    cache.insertar("wikipedia.org", "103.102.166.224");
    cache.insertar("reddit.com", "151.101.129.140");
    cache.insertar("amazon.com", "176.32.103.205");
    // Algunos más por si acaso, para asegurar colisiones
    cache.insertar("stackoverflow.com", "104.18.32.7");
    cache.insertar("bing.com", "13.107.21.200");

    cout << "---------------------------------------" << endl;
    cout << "  Contenido de la Tabla Hash (Cache)   " << endl;
    cout << "---------------------------------------" << endl;
    // Mostramos la tabla para visualizar colisiones
    cache.mostrarTabla();

    cout << "\n---------------------------------------" << endl;
    cout << "          Pruebas de Busqueda          " << endl;
    cout << "---------------------------------------" << endl;
    cout << "Buscando IP de 'github.com': " << cache.buscar("github.com") << endl;
    cout << "Buscando IP de 'unam.mx'   : " << cache.buscar("unam.mx") << endl;
    cout << "Buscando IP de 'yahoo.com' : " << cache.buscar("yahoo.com") << endl;

    cout << "\n---------------------------------------" << endl;
    cout << "        Prueba de Actualizacion        " << endl;
    cout << "---------------------------------------" << endl;
    cout << "IP actual de 'buap.mx': " << cache.buscar("buap.mx") << endl;
    cout << "Actualizando IP de 'buap.mx' a '192.168.1.1'..." << endl;
    cache.insertar("buap.mx", "192.168.1.1");
    cout << "Nueva IP de 'buap.mx' : " << cache.buscar("buap.mx") << endl;

    return 0;
}