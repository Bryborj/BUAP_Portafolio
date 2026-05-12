/**
 * @file pista.cpp
 * @author Bryan Albino Borges
 * @brief Implementación de una lista doblemente enlazada para gestionar una playlist de canciones.
 * @version 1.0
 * @date 2026-02-02
 * @institution BUAP - Estructuras de Datos
 */

 // Compilación: g++ -std=c++17 -o pista pista.cpp
 // Ejecución: ./pista.exe


#include <iostream>
#include <string>
using namespace std;

struct Pista
{
    string tittle;
    string artist;
    int duration;

    Pista* next;
    Pista* prev;

    Pista(string t, string a, int d) : tittle(t), artist(a), duration(d), next(nullptr), prev(nullptr) {}
};

class Playlist
{
private:
    Pista* head;
    Pista* tail;
    Pista* current;
public:
    Playlist(){
        head = nullptr;
        tail = nullptr;
        current = nullptr;
    }
    void addSong(string t, string a, int d){
        Pista* newSong = new Pista(t, a, d);
        if (!head) {
            head = tail = current = newSong;
        } else {
            tail->next = newSong;
            newSong->prev = tail;
            tail = newSong;
        }
    }

    void showPlaylist(){
        Pista* temp = head;
        if (!temp) {cout << "Playlist vacia." << endl; return;}
        while (temp) {
            cout << "-. Titulo: " << temp->tittle << ", Artista: " << temp->artist << ", Duracion: " << temp->duration << "s" << endl;
            temp = temp->next;
        }
    }

    void playCurrent(){
        if (current) {
            cout << "Reproduciendo: " << current->tittle << " - " << current->artist << endl;
        } else {
            cout << "No hay canciones seleccionadas." << endl;
        }
    }

    void nextSong(){
        if (current && current->next) {
            current = current->next;
            playCurrent();
        } else {
            cout << "Fin de la playlist." << endl;
        }
    }

    void previousSong(){
        if (current && current->prev) {
            current = current->prev;
            playCurrent();
        } else {
            cout << "Inicio de la playlist." << endl;
        }
    }

    void deleteSong(){
        if (!current) return;
        Pista* toDelete = current;

        if (toDelete->prev) 
            toDelete->prev->next = toDelete->next;
        else 
            head = toDelete->next;

        if (toDelete->next) toDelete->next->prev = toDelete->prev;
        else tail = toDelete->prev;

        if (toDelete->next) current = toDelete->next;
        else if (toDelete->prev) current = toDelete->prev;
        else current = head = tail = nullptr;

        delete toDelete;
        cout << "Cancion eliminada" << endl;
    }
};

void newSongInput(Playlist &playlist) {
    string title, artist;
    int duration;
    cout << "Titulo: ";
    cin >> ws;
    getline(cin, title);
    cout << "Artista: ";
    getline(cin, artist);
    cout << "Duracion (seg): ";
    cin >> duration;
    playlist.addSong(title, artist, duration);
}

int main() {
    Playlist playlist;
    int op;
    do {
        cout << ("--- REPRODUCTOR Z_SH ---"
                "\n 1. Agregar cancion"
                "\n 2. Mostrar Playlist"
                "\n 3. Reproducir Actual"
                "\n 4. Siguiente cancion"
                "\n 5. Cancion anterior"
                "\n 6. Eliminar cancion"
                "\n 0. Salir"
                "\n Ingrese una opcion: "
        ) << endl;
        cin >> op;
        switch (op)
        {
        case 1: newSongInput(playlist); break;
        case 2: playlist.showPlaylist(); break;
        case 3: playlist.playCurrent(); break;
        case 4: playlist.nextSong(); break;
        case 5: playlist.previousSong(); break;
        case 6: playlist.deleteSong(); break;
        }
    } while (op != 0);
    return 0;
}