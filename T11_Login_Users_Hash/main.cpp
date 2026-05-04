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
        username = "":
        passwordHash = 0;
    }
};

vector<User> table (m);

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
    // long long passHash = hashPassword(pass);

    int start = index;

    while(table[index].username != "") {
        index = (index + 1) % m;

        if (index == start){
            cout << "[!Error] La tabla se encuentra llena \n";
            return;
        }
    }

    table[index].username = user;
    table[index].passwordHash = hashPassword(pass);

    cout << "El usuario " << user << " fue guardado en el indice >" << index << "<\n";
}

bool login(string user, string pass){
    int index, start = hashUsername(user);

    while(table[index].username != ""){
        if (table[index].username == user) {
            return tabla[index].passwordHash == hashPassword(pass);
        }

        index = (index + 1) % m;

        if (index == start){
            break;
        }
    }
    return false;
}

