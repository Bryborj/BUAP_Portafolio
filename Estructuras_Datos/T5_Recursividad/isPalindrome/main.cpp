#include <iostream>
#include <string.h>
using namespace std;

bool esPalindromo(string str, int n){
    if(n <= 1) return true;
    if(str[0] != str[n-1]) return false;
    return esPalindromo(str.substr(1,n-2), n-2);
}

void run(){
    string str;
    cout << "Ingrese la palabra a comprobar: ";
    cin >> str;
    if(esPalindromo(str, str.length())) cout << "Es palindromo" << endl;
    else cout << "No es palindromo" << endl;
    cout << "Desea comprobar otra palabra? (s/n): ";
    char respuesta;    cin >> respuesta;
    if(respuesta == 'n' || respuesta == 'N') exit(0);
    else system("cls");
}

int main(){
    while (true)
        run();
    return 0;
}