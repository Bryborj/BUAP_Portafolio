import glfw
import numpy as np
from OpenGL.GL import *
import ctypes


# ============================================================
# 1. INICIALIZAR GLFW
# ============================================================

if not glfw.init():
    raise Exception("No se pudo inicializar GLFW")


# ============================================================
# 2. CREAR LA VENTANA
# ============================================================

window = glfw.create_window(
    800,
    600,
    "Cuadrado en movimiento",
    None,
    None
)

if not window:
    glfw.terminate()
    raise Exception("No se pudo crear la ventana")


glfw.make_context_current(window)


# ============================================================
# 3. VERTICES
# ============================================================

vertices = np.array([
    -0.5, -0.5,   # vértice 0
     0.5, -0.5,   # vértice 1
     0.5,  0.5,   # vértice 2
    -0.5,  0.5    # vértice 3
], dtype=np.float32)


# ============================================================
# 4. INDICES
# ============================================================

indices = np.array([
    0, 1, 2,
    2, 3, 0
], dtype=np.uint32)


# ============================================================
# 5. VERTEX SHADER
# ============================================================

vertex_shader_source = """
#version 330 core

// Atributo de posición
layout(location = 0) in vec2 position;

// Variable que recibiremos desde Python
uniform float desplazamientoY;

void main()
{
    // Movemos el vértice en Y
    float y = position.y + desplazamientoY;

    // Posición final
    gl_Position = vec4(
        position.x,
        y,
        0.0,
        1.0
    );
}
"""


# ============================================================
# 6. FRAGMENT SHADER
# ============================================================

fragment_shader_source = """
#version 330 core

out vec4 color;

void main()
{
    // Color rojo
    color = vec4(
        0.0,
        0.0,
        1.0,
        1.0
    );
}
"""


# ============================================================
# 7. CREAR Y COMPILAR VERTEX SHADER
# ============================================================

vertex_shader = glCreateShader(GL_VERTEX_SHADER)

glShaderSource(
    vertex_shader,
    vertex_shader_source
)

glCompileShader(vertex_shader)


# Comprobar errores de compilación
if not glGetShaderiv(vertex_shader, GL_COMPILE_STATUS):
    error = glGetShaderInfoLog(vertex_shader).decode()
    raise Exception(
        "Error compilando Vertex Shader:\n" + error
    )


# ============================================================
# 8. CREAR Y COMPILAR FRAGMENT SHADER
# ============================================================

fragment_shader = glCreateShader(GL_FRAGMENT_SHADER)

glShaderSource(
    fragment_shader,
    fragment_shader_source
)

glCompileShader(fragment_shader)


# Comprobar errores de compilación
if not glGetShaderiv(fragment_shader, GL_COMPILE_STATUS):
    error = glGetShaderInfoLog(fragment_shader).decode()
    raise Exception(
        "Error compilando Fragment Shader:\n" + error
    )


# ============================================================
# 9. CREAR PROGRAMA DE SHADERS
# ============================================================

shader_program = glCreateProgram()


glAttachShader(
    shader_program,
    vertex_shader
)

glAttachShader(
    shader_program,
    fragment_shader
)


glLinkProgram(shader_program)


# Comprobar errores de enlace
if not glGetProgramiv(shader_program, GL_LINK_STATUS):
    error = glGetProgramInfoLog(shader_program).decode()
    raise Exception(
        "Error enlazando Shader Program:\n" + error
    )


# ============================================================
# 10. YA NO NECESITAMOS LOS SHADERS INDIVIDUALES
# ============================================================

glDeleteShader(vertex_shader)
glDeleteShader(fragment_shader)


# ============================================================
# 11. CREAR VAO
# ============================================================

VAO = glGenVertexArrays(1)

glBindVertexArray(VAO)


# ============================================================
# 12. CREAR VBO
# ============================================================

VBO = glGenBuffers(1)

glBindBuffer(
    GL_ARRAY_BUFFER,
    VBO
)


# Copiar los vértices al VBO
glBufferData(
    GL_ARRAY_BUFFER,
    vertices.nbytes,
    vertices,
    GL_STATIC_DRAW
)


# ============================================================
# 13. CONFIGURAR EL ATRIBUTO DE POSICIÓN
# ============================================================

glVertexAttribPointer(
    0,                              # location
    2,                              # cantidad de valores
    GL_FLOAT,                       # tipo
    GL_FALSE,                       # normalización
    2 * vertices.itemsize,          # stride
    ctypes.c_void_p(0)              # offset
)


# Activar atributo 0
glEnableVertexAttribArray(0)


# ============================================================
# 14. CREAR EBO
# ============================================================

EBO = glGenBuffers(1)

glBindBuffer(
    GL_ELEMENT_ARRAY_BUFFER,
    EBO
)


# Copiar índices al EBO
glBufferData(
    GL_ELEMENT_ARRAY_BUFFER,
    indices.nbytes,
    indices,
    GL_STATIC_DRAW
)


# ============================================================
# 15. OBTENER LA UBICACIÓN DEL UNIFORM
# ============================================================

location_y = glGetUniformLocation(
    shader_program,
    "desplazamientoY"
)


# ============================================================
# 16. DESVINCULAR VAO
# ============================================================

glBindVertexArray(0)


# ============================================================
# 17. LOOP PRINCIPAL
# ============================================================

while not glfw.window_should_close(window):

    # --------------------------------------------------------
    # Limpiar pantalla
    # --------------------------------------------------------

    glClearColor(
        0.1,
        0.1,
        0.1,
        1.0
    )

    glClear(GL_COLOR_BUFFER_BIT)


    # --------------------------------------------------------
    # Activar nuestro programa de shaders
    # --------------------------------------------------------

    glUseProgram(shader_program)


    # --------------------------------------------------------
    # Obtener tiempo
    # --------------------------------------------------------

    tiempo = glfw.get_time()


    # --------------------------------------------------------
    # Calcular posición X
    # --------------------------------------------------------

    desplazamientoY = np.sin(tiempo) * 0.5


    # --------------------------------------------------------
    # Enviar posición al Vertex Shader
    # --------------------------------------------------------

    glUniform1f(
        location_y,
        desplazamientoY
    )


    # --------------------------------------------------------
    # Activar VAO
    # --------------------------------------------------------

    glBindVertexArray(VAO)


    # --------------------------------------------------------
    # Dibujar cuadrado
    # --------------------------------------------------------

    glDrawElements(
        GL_TRIANGLES,
        6,
        GL_UNSIGNED_INT,
        None
    )


    # --------------------------------------------------------
    # Mostrar el frame
    # --------------------------------------------------------

    glfw.swap_buffers(window)


    # --------------------------------------------------------
    # Procesar eventos
    # --------------------------------------------------------

    glfw.poll_events()


# ============================================================
# 18. LIBERAR RECURSOS
# ============================================================

glDeleteVertexArrays(
    1,
    [VAO]
)

glDeleteBuffers(
    1,
    [VBO]
)

glDeleteBuffers(
    1,
    [EBO]
)

glDeleteProgram(
    shader_program
)

glfw.terminate()