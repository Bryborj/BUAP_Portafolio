import ctypes

import glfw
import numpy as np
from OpenGL.GL import *

# -----------------------------------------
# 1. Inicializar GLFW
# -----------------------------------------

if not glfw.init():
    raise Exception("No se pudo inicializar GLFW")


# -----------------------------------------
# 2. Crear ventana
# -----------------------------------------

window = glfw.create_window(800, 600, "VAO VBO EBO + Shaders", None, None)

if not window:
    glfw.terminate()
    raise Exception("No se pudo crear la ventana")


glfw.make_context_current(window)


# -----------------------------------------
# 3. Vértices
# -----------------------------------------

vertices = np.array(
    [
         -0.5, 0.0,  # vértice 0
         -0.25, 0.5,  # vértice 1
          0.0, 0.0,  # vértice 2
          
         -0.25, 0.5,  # vértice 3
          0.0, 0.0,  # vértice 4
          0.25, 0.5,  # vértice 5
          
          0.0, 0.0,   # vértice 6
          0.25, 0.5,  # vértice 7
          0.5, 0.0,   # vértice 8
    ],
    dtype=np.float32,
)


# -----------------------------------------
# 4. Índices
# -----------------------------------------

indices = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8], dtype=np.uint32)


# -----------------------------------------
# 5. Vertex Shader
# -----------------------------------------

vertex_shader_source = """
#version 330 core

layout(location = 0) in vec2 position;

void main()
{
    gl_Position = vec4(position, 0.0, 1.0);
}
"""


# -----------------------------------------
# 6. Fragment Shader
# -----------------------------------------

fragment_shader_source = """
#version 330 core

out vec4 color;

void main()
{
    color = vec4(1.0, 0.0, 0.0, 1.0);
}
"""


# -----------------------------------------
# 7. Compilar Vertex Shader
# -----------------------------------------

vertex_shader = glCreateShader(GL_VERTEX_SHADER)

glShaderSource(vertex_shader, vertex_shader_source)

glCompileShader(vertex_shader)


# -----------------------------------------
# 8. Compilar Fragment Shader
# -----------------------------------------

fragment_shader = glCreateShader(GL_FRAGMENT_SHADER)

glShaderSource(fragment_shader, fragment_shader_source)

glCompileShader(fragment_shader)


# -----------------------------------------
# 9. Crear programa
# -----------------------------------------

shader_program = glCreateProgram()


glAttachShader(shader_program, vertex_shader)

glAttachShader(shader_program, fragment_shader)


glLinkProgram(shader_program)


# -----------------------------------------
# 10. Eliminar shaders individuales
# -----------------------------------------

glDeleteShader(vertex_shader)
glDeleteShader(fragment_shader)


# -----------------------------------------
# 11. Crear VAO
# -----------------------------------------

VAO = glGenVertexArrays(1)

glBindVertexArray(VAO)


# -----------------------------------------
# 12. Crear VBO
# -----------------------------------------

VBO = glGenBuffers(1)

glBindBuffer(GL_ARRAY_BUFFER, VBO)


glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)


# -----------------------------------------
# 13. Configurar atributo
# -----------------------------------------

glVertexAttribPointer(
    0, 2, GL_FLOAT, GL_FALSE, 2 * vertices.itemsize, ctypes.c_void_p(0)
)


glEnableVertexAttribArray(0)


# -----------------------------------------
# 14. Crear EBO
# -----------------------------------------

EBO = glGenBuffers(1)

glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)


glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)


# -----------------------------------------
# 15. Desvincular VAO
# -----------------------------------------

glBindVertexArray(0)


# -----------------------------------------
# 16. Loop principal
# -----------------------------------------

while not glfw.window_should_close(window):
    # Limpiar pantalla
    glClearColor(0.1, 0.1, 0.1, 1.0)

    glClear(GL_COLOR_BUFFER_BIT)

    # Usar shaders
    glUseProgram(shader_program)

    # Activar VAO
    glBindVertexArray(VAO)

    # Dibujar
    glDrawElements(GL_TRIANGLES, 9, GL_UNSIGNED_INT, None)

    # Mostrar resultado
    glfw.swap_buffers(window)

    # Procesar eventos
    glfw.poll_events()


# -----------------------------------------
# 17. Liberar recursos
# -----------------------------------------

glDeleteVertexArrays(1, [VAO])
glDeleteBuffers(1, [VBO])
glDeleteBuffers(1, [EBO])
glDeleteProgram(shader_program)

glfw.terminate()