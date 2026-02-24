//backtracking
#include <iostream>
using namespace std;

// mapa
char laberinto [5][5] = {
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
    if (laberinto[x][y] == NULL)
        return false; // fuera de los límites del laberinto
    if (laberinto[x][y] == '#' || laberinto[x][y] == '*')
        return false; // pared o ya visitado
    if (laberinto[x][y] == 'S') 
        return true; // salida encontrada
    if (laberinto[x][y] == ' ')
        laberinto[x][y] = '*'; // marcar como visitado
    return buscarSalida(x - 1, y) || buscarSalida(x + 1, y) || buscarSalida(x, y - 1) || buscarSalida(x, y + 1);
}

int main(int argc, char const *argv[])
{
    cout << "Ejecutando";
    buscarSalida(0,0);
    printf("Laberinto:\n");
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            printf("%c ", laberinto[i][j]);
        }
        printf("\n");
    }
    return 0;
}
