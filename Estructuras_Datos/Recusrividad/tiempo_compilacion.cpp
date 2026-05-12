#include <iostream>
#include <chrono>

int main() {
    // Tomar tiempo de inicio
    auto inicio = std::chrono::high_resolution_clock::now();

    // --- Código a medir ---
    // ----------------------

    // Tomar tiempo de fin
    auto fin = std::chrono::high_resolution_clock::now();

    // Calcular la diferencia
    auto duracion = std::chrono::duration_cast<std::chrono::microseconds>(fin - inicio);

    std::cout << "Tiempo de ejecución: " << duracion.count() << " microsegundos" << std::endl;

    return 0;
}
