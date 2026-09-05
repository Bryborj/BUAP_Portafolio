import numpy as np
import os
import sys
import tty
import termios
import select

# Matriz 10 x 10
matriz = np.arange(100).reshape(10, 10)

# Tamaño de la ventana
ALTO = 2
ANCHO = 2

# Coordenadas iniciales
x = 0
y = 0

def imprimir_seleccion():
    os.system('clear')
    
    print(f"Posición: ({x}, {y})")
    print()
    
    seleccion = matriz[y:y + ALTO, x:x + ANCHO]
    
    print(seleccion)

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

while True: # Ciclo para "Escuchar los eventos"
    imprimir_seleccion()
    
    tecla = getch()
    
    
    # En Linux, las flechas y teclas especiales envían una secuencia
    # que empieza con Escape (\x1b). Leemos el resto de la secuencia.
    
    if tecla == '\x1b': # Solamente Escape
        break
    elif tecla == 'w': # Arriba
        y = max(0, y - 1)
    elif tecla == 's': # Abajo
        y = min(9, y + 1)
    elif tecla == 'a': # Izquierda
        x = max(0, x - 1)
    elif tecla == 'd': # Derecha
        x = min(9, x + 1)