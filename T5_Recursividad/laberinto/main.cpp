//backtracking
#include <iostream>
#include <stdio.h>
using namespace std;

#define COLS 5
#define ROWS 5
char laberinto [ROWS][COLS] = {
    {'I', ' ', '#', ' ', ' '},
    {'#', ' ', '#', ' ', '#'},
    {' ', ' ', ' ', ' ', ' '},
    {'#', '#', '#', '#', ' '},
    {' ', ' ', ' ', ' ', 'S'}
};

// 'I' = inicio
// 'S' = salida
// '#' = pared
// ' ' = camino

bool buscarSalida(int x, int y) {
    if (x < 0 || x >= ROWS || y< 0 || y >= COLS)
        return false; // fuera de los límites del laberinto
    if (laberinto[x][y] == '#' || laberinto[x][y] == '*')
        return false; // pared o ya visitado
    if (laberinto[x][y] == 'S') 
        return true; // salida encontrada
    if (laberinto[x][y] != 'I')
        laberinto[x][y] = '*'; // marcar como visitado
    if (buscarSalida(x - 1, y) || 
        buscarSalida(x + 1, y) ||
        buscarSalida(x, y - 1) ||
        buscarSalida(x, y + 1))
        return true;

    return false;
}

int main(int argc, char const *argv[])
{
    try
    {
        cout << "Ejecutando\n" << endl;
        if (buscarSalida(0,0))
            cout << "Salida encontrada!" << endl;
        else
            cout << "No hay salida." << endl;

        printf("Mapa final:\n");
        for (int i = 0; i < ROWS; i++) {
            for (int j = 0; j < COLS; j++) {
                printf("%c ", laberinto[i][j]);
            }
            printf("\n");
        }
        return 0;
    }
    catch(const std::exception& e)
    {
        std::cerr << "ha ocurrido un error inesperado: {e.what()}" << '\n';
    }
    
}
