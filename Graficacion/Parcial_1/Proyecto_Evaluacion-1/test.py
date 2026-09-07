import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# MAPA
# ==========================================

ALTO_MAPA = 256
ANCHO_MAPA = 256

matriz = np.arange(ALTO_MAPA * ANCHO_MAPA).reshape(
    ALTO_MAPA,
    ANCHO_MAPA
)

# ==========================================
# VIEWPORT
# ==========================================

VIEWPORT_ALTO = 64
VIEWPORT_ANCHO = 64

# Posición del viewport
x = 0
y = 0


# ==========================================
# ACTUALIZAR VIEWPORT
# ==========================================

def actualizar():
    global x, y

    viewport = matriz[
        y:y + VIEWPORT_ALTO,
        x:x + VIEWPORT_ANCHO
    ]

    imagen.set_data(viewport)

    ax.set_title(
        f"Viewport: ({x}, {y}) | "
        f"{VIEWPORT_ANCHO}x{VIEWPORT_ALTO}"
    )

    fig.canvas.draw_idle()


# ==========================================
# TECLADO
# ==========================================

def teclado(event):
    global x, y

    # --------------------------
    # Izquierda
    # --------------------------
    if event.key in ("left", "a"):
        x = max(0, x - 1)

    # --------------------------
    # Derecha
    # --------------------------
    elif event.key in ("right", "d"):
        x = min(
            ANCHO_MAPA - VIEWPORT_ANCHO,
            x + 1
        )

    # --------------------------
    # Arriba
    # --------------------------
    elif event.key in ("up", "w"):
        y = max(0, y - 1)

    # --------------------------
    # Abajo
    # --------------------------
    elif event.key in ("down", "s"):
        y = min(
            ALTO_MAPA - VIEWPORT_ALTO,
            y + 1
        )

    # --------------------------
    # Salir
    # --------------------------
    elif event.key == "escape":
        plt.close(fig)
        return

    actualizar()


# ==========================================
# MATPLOTLIB
# ==========================================

fig, ax = plt.subplots()

viewport = matriz[
    y:y + VIEWPORT_ALTO,
    x:x + VIEWPORT_ANCHO
]

imagen = ax.imshow(
    viewport,
    interpolation="nearest",
    cmap="viridis"
)

ax.set_title(
    f"Viewport: ({x}, {y}) | "
    f"{VIEWPORT_ANCHO}x{VIEWPORT_ALTO}"
)

# Conectar teclado
fig.canvas.mpl_connect(
    "key_press_event",
    teclado
)

plt.show()