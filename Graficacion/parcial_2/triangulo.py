import sys
import os
# Configuramos la plataforma a X11/GLX para evitar el error de contexto en Linux (Wayland)
os.environ['PYOPENGL_PLATFORM'] = 'x11'

# Importamos las librerías principales de OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Función que se encarga de dibujar en la pantalla
def dibujar():
    # Limpiamos la pantalla (el buffer de color) antes de dibujar para que no quede basura visual
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Iniciamos el dibujo de primitivas, en este caso le indicamos que serán triángulos
    glBegin(GL_TRIANGLES)
    
    # Definimos el primer vértice del triángulo
    glColor3f(1.0, 0.0, 0.0) # Le damos un color: Rojo (R=1, G=0, B=0)
    glVertex2f(-0.5, -0.5)   # Posición en X=-0.5, Y=-0.5 (esquina inferior izquierda)
    
    # Definimos el segundo vértice del triángulo
    glColor3f(0.0, 1.0, 0.0) # Le damos un color: Verde (R=0, G=1, B=0)
    glVertex2f(0.5, -0.5)    # Posición en X=0.5, Y=-0.5 (esquina inferior derecha)
    
    # Definimos el tercer vértice del triángulo
    glColor3f(0.0, 0.0, 1.0) # Le damos un color: Azul (R=0, G=0, B=1)
    glVertex2f(0.0, 0.5)     # Posición en X=0, Y=0.5 (centro arriba)
    
    # Le indicamos a OpenGL que hemos terminado de definir los vértices del triángulo
    glEnd()
    
    # Forzamos a que se ejecuten todos los comandos de OpenGL para que se muestre en pantalla
    glFlush()

# Función principal que inicializa y configura la ventana
def main():
    # 1. Inicializamos GLUT (la librería que nos ayuda a crear la ventana y gestionar eventos)
    glutInit(sys.argv)
    
    # 2. Configuramos el modo de visualización: Usaremos un solo buffer y colores RGB
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    
    # 3. Configuramos el tamaño inicial de nuestra ventana (ancho=500, alto=500 píxeles)
    glutInitWindowSize(500, 500)
    
    # 4. Configuramos la posición inicial de la ventana en la pantalla (X=100, Y=100)
    glutInitWindowPosition(100, 100)
    
    # 5. Creamos la ventana y le asignamos un título (debe ir con 'b' de byte string para evitar errores)
    glutCreateWindow(b"Mi Primer Triangulo en OpenGL")
    
    # 6. Establecemos el color de fondo de la ventana (Negro: R=0, G=0, B=0, Alpha/Transparencia=1)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    
    # 7. Le decimos a GLUT qué función debe llamar cuando necesite dibujar la pantalla
    glutDisplayFunc(dibujar)
    
    # 8. Iniciamos el ciclo principal infinito, que mantendrá la ventana abierta esperando eventos
    glutMainLoop()

# Punto de entrada de Python: Si ejecutamos este archivo directamente, llamará a main()
if __name__ == "__main__":
    main()
