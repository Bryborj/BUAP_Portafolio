/*
 * Archivo: main.cpp
 * Autor: Bryan Albino Borges
 * Fecha: 02/05/2026
 * Descripcion: Implementacion de un sistema de usuarios con hashing
*/

#include <iostream>
#include <string>
#include <math.h>

using namespace std;

struct User {
    string username;
    long passwordHash;
};

int hashUsername(string user){
    int hash = 0;
    int p = 31;
    int m = 0;
    for (char c : user){
        hash += c * pow(p, c);
    }
    return hash % m;
}

long long hashPassword(string pass){
    long long hash = 0;
    int p = 31;
    int m = 0;
    for (char c : pass){
        hash += c * pow(p, c);
    }
    return hash % m;
}

void postUser(){

}