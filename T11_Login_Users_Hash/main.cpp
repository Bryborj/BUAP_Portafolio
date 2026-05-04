/*
 * Archivo: main.cpp
 * Autor: Bryan Albino Borges
 * Fecha: 02/05/2026
 * Descripcion: Implementacion de un sistema de usuarios con hashing
*/

#include <iostream>
#include <string>
#include <math.h>
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
        hash += c * pow(p, c);
    }
    return hash;
}

void postUser(string user, string pass){
    int index = hashUsername(user);

}

int main(){
    cout << "Sistema de Autenticación Segura" << endl;
}