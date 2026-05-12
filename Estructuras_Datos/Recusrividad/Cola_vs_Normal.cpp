#include <iostream>
#include <chrono>

using namespace std;

int fac(int n, int acum=1){
    if (n == 0) return acum;

    return fac(n-1, acum*n);
}


int main() {
    // Tomar tiempo de inicio
    auto inicio = std::chrono::high_resolution_clock::now();

    // --- Código a medir ---
    fac(1000);
    // ----------------------

    // Tomar tiempo de fin
    auto fin = std::chrono::high_resolution_clock::now();

    // Calcular la diferencia
    auto duracion = std::chrono::duration_cast<std::chrono::microseconds>(fin - inicio);

    std::cout << "Tiempo de ejecución: " << duracion.count() << " microsegundos" << std::endl;

    return 0;
}