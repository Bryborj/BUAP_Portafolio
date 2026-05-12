/*
 * Archivo: main.cpp
 * Autor: Bryan Albino Borges
 * Fecha: 02/05/2026
 * Descripcion: Implementacion de un sistema de usuarios con hashing
*/

#include <iostream>
#include <string>
#include <vector>

using namespace std;


const int m = 10;
struct User {
    string username;
    long long passwordHash;
    
    User() {
        username = "";
        passwordHash = 0;
    }
};

vector<User> table(m);

int hashUsername(string user){
    int hash = 0;
    int p = 31;
    for (char c : user){
        hash = (hash * p + c) % m;
    }
    return hash;
}

long long hashPassword(string pass){
    long long hash = 0;
    int p = 31;
    for (char c : pass){
        hash = (hash * p + c);
    }
    return hash;
}

void postUser(string user, string pass){
    int index = hashUsername(user);
    long long passHash = hashPassword(pass);

    int start = index;

    while(table[index].username != "") {
        index = (index + 1) % m;

        if (index == start){
            cout << "[!Error] La tabla se encuentra llena \n";
            return;
        }
    }

    table[index].username = user;
    table[index].passwordHash = passHash;

    cout << "El usuario " << user << " fue guardado en el indice >" << index << "<\n";
}

bool login(string user, string pass){
    int index = hashUsername(user);
    int start = index;

    while(table[index].username != ""){
        if (table[index].username == user) {
            long long passHash = hashPassword(pass);
            // cout << "DEBUG -> Tabla: " << table[index].passwordHash << " | Input: " << passHash << "\n";
            return table[index].passwordHash == passHash;
        }

        index = (index + 1) % m;

        if (index == start){
            break;
        }
    }
    return false;
}

///* Uncoment to run debug table

void showTable(){
    cout << "\nTabla Hash:\n";
    for (int i = 0; i < m; i++) {
        cout << i << ": ";
        if (table[i].username == "")
            cout << "[VACIO]\n";
        else
            cout << table[i].username << "\n";
    }
}

//*/

void loginInter(string user, string pass) {
    string msgSucces = "Acceso exitoso, Bienvenido";
    string msgFail = "[!] Acceso denegado, credenciales invalidas";

    if (login(user, pass))
        cout << msgSucces << "\n";
    else
        cout << msgFail << "\n";
}

int main() {
    postUser("bry", "1234");
    postUser("root", "admin");
    postUser("juan", "cachorra");
    postUser("diego", "debug");
    postUser("sarahi", "passw");

    showTable();

    loginInter("bry", "1234");
    loginInter("root", "admin");
    loginInter("juan", "cachorra");
    loginInter("diego", "1234"); // Probando contraseña incorrecta
    loginInter("sarahi", "passw");

    return 0;
}