
"""
Explorador de vectores y geometría 3D

Requisitos:
    pip install numpy matplotlib

Ejecución:
    python explorador_vectores.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Button

# ============================================================
# AQUI VA: PREPARAR LAS HERRAMIENTAS DEL PROGRAMA
# ============================================================
EPS = 1e-10  # Umbral para considerar un vector como cero

# ============================================================
# AQUI VA: CREAR LAS OPERACIONES MATEMÁTICAS REUTILIZABLES [OK]
# ============================================================

def magnitud(v):
    return float(np.linalg.norm(v))

def normalizar(v):
    n = magnitud(v)
    return None if n < EPS else v / n

def fmt(v):
    return "(" + ", ".join(f"{x:.3f}" for x in v) + ")"

class ExploradorVectores:

    def __init__(self):

        # ====================================================
        # AQUI VA: DEFINIR LOS VALORES INICIALES DE LOS VECTORES [OK]
        # ====================================================

        self.valores_iniciales = {
            "ax": "3.0", "ay": "2.0", "az": "1.0",
            "bx": "1.0", "by": "3.0", "bz": "2.0"
        }

        # ====================================================
        # AQUI VA: CONSTRUIR LA VENTANA Y SUS ÁREAS [OK]
        # ====================================================
        
        self.fig = plt.figure(figsize=(14, 8.5))
        self.ax = self.fig.add_axes([0.04, 0.12, 0.57, 0.8], projection="3d")
        self.ax_info = self.fig.add_axes([0.64, 0.28, 0.33, 0.62])
        self.ax_info.axis("off")

        # ====================================================
        # AQUI VA: CONSTRUIR LOS CONTROLES DE ENTRADA [OK]
        # ====================================================
        
        self.cajas = {}
        posiciones = [
            ("ax", 0.08), ("ay", 0.19), ("az", 0.30),
            ("bx", 0.43), ("by", 0.54), ("bz", 0.65)
        ]
        

        for nombre, x in posiciones:    
            caja_ax = self.fig.add_axes([x, 0.055, 0.085, 0.045])   
            self.cajas[nombre] = TextBox(
                caja_ax, 
                nombre + " ",  
                initial=self.valores_iniciales[nombre]
            )

        # ====================================================
        # AQUI VA: CONECTAR EL BOTÓN CON EL EVENTO DE ACTUALIZACIÓN [OK]
        # ====================================================

        boton_ax = self.fig.add_axes([0.77, 0.045, 0.16, 0.06])
        self.boton = Button(boton_ax, "Actualizar gráfica")
        self.boton.on_clicked(self.actualizar_desde_controles)

        self.fig.text(
            0.04, 0.015,
            "Introduce las componentes de A y B en las casillas inferiores y pulsa «Actualizar gráfica».",
            fontsize=9
        )

        self.actualizar_grafica(np.array([3., 2., 1.]), np.array([1., 3., 2.]))


    # ========================================================
    # AQUI VA: CREAR LA FUNCIÓN PARA DIBUJAR VECTORES [OK]
    # ========================================================
    
    def dibujar_vector(self, v, color, etiqueta):
        self.ax.quiver(
            0, 0, 0,
            v[0], v[1], v[2],
            color=color,
            linewidth=2.5, 
            arrow_length_ratio=0.12
        )
        
        self.ax.text(
            v[0], v[1], v[2],
            f" {etiqueta}",
            color=color,
            fontsize=10
        )
    
    def actualizar_desde_controles(self, _evento):
        try:
            # ========================================================
            # AQUI VA: LEER Y VALIDAR LAS ENTRADAS DEL USUARIO [OK]
            # ========================================================    
            
            a = np.array([float(self.cajas[k].text) for k in ["ax", "ay", "az"]])
            b = np.array([float(self.cajas[k].text) for k in ["bx", "by", "bz"]])
            if not np.all(np.isfinite(a)) or not np.all(np.isfinite(b)):
                raise ValueError("Componentes no finitas")
            self.actualizar_grafica(a, b)
            
        except ValueError:
            self.ax_info.clear()
            self.ax_info.axis("off")
            self.ax_info.text(
                0, 0.95,
                "Entrada no válida.\nEscribe números reales en las seis casillas.",
                va="top", fontsize=12, color="crimson"
            )
            self.fig.canvas.draw_idle()

    def actualizar_grafica(self, a, b):

        # ====================================================
        # AQUI VA: LIMPIAR LA REPRESENTACIÓN ANTERIOR [OK]
        # ====================================================
        
        self.ax.clear()
        self.ax_info.clear()
        self.ax_info.axis("off")

        # ====================================================
        # AQUI VA: PREPARAR LOS EJES Y LA CUADRÍCULA [OK]
        # ====================================================
        
        self.ax.set_title("Vectores en el espacio tridimencional")
        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.ax.set_zlabel("Z")
        self.ax.grid(True, alpha=0.35)
        
        self.ax.axhline(0, color="gray", linewidth=0.7)
        self.ax.plot([0, 0], [0, 0], [-1, 1], color="gray", linewidth=0.7)
        


        # ====================================================
        # AQUI VA: DIBUJAR LOS PUNTOS Y VECTORES PRINCIPALES [OK]
        # ====================================================
        
        self.ax.scatter(*a, color="royalblue", s=45)
        self.ax.scatter(*b, color="darkorange", s=45)
        self.dibujar_vector(a, "royalblue", "A")
        self.dibujar_vector(b, "darkorange", "B")


        # Segmento entre las puntas de A y B
        self.ax.plot(
            [a[0], b[0]], [a[1], b[1]], [a[2], b[2]],
            linestyle="--", color="gray", linewidth=1.6, label="Segmento A-B"
        )

        # ====================================================
        # AQUI VA: CALCULAR LAS PROPIEDADES DE LOS VECTORES [OK]
        # ====================================================
        
        mag_a, mag_b = magnitud(a), magnitud(b)
        producto_punto = float(np.dot(a, b))
        producto_cruz = np.cross(a, b)
        distancia = magnitud(a - b)
        unit_a, unit_b = normalizar(a), normalizar(b)

        perpendicular = abs(producto_punto) < 1e-7 * max(1.0, mag_a * mag_b)

        # Proyección de A sobre B y componente perpendicular restante
        proyeccion = None
        resto = None
        
        # ====================================================
        # AQUI VA: CALCULAR Y DIBUJAR LA PROYECCIÓN [OK]
        # ====================================================
        
        if mag_b >= EPS:
            proyeccion = (producto_punto / (mag_b ** 2)) * b
            resto = a - proyeccion

            self.dibujar_vector(proyeccion, "seagreen", "Proy A sobre B")
            self.ax.plot(
                [a[0], proyeccion[0]], [a[1], proyeccion[1]], [a[2], proyeccion[2]],
                linestyle=":", color="purple", linewidth=2
            )
            self.ax.plot(
                [0, proyeccion[0]], [0, proyeccion[1]], [0, proyeccion[2]],
                color="seagreen", linewidth=2
            )
            
        # Escala uniforme para que los ejes tengan proporciones comparables
        todos = [a, b, np.zeros(3)]
        if proyeccion is not None:
            todos.append(proyeccion)
        puntos = np.array(todos)
        limite = max(2.0, float(np.max(np.abs(puntos))) * 1.25)
        self.ax.set_xlim(-limite, limite)
        self.ax.set_ylim(-limite, limite)
        self.ax.set_zlim(-limite, limite)
        try:
            self.ax.set_box_aspect((1, 1, 1))
        except AttributeError:
            pass
        self.ax.legend(loc="upper left", fontsize=8)

        # Ángulo entre A y B
        if mag_a >= EPS and mag_b >= EPS:
            coseno = np.clip(producto_punto / (mag_a * mag_b), -1.0, 1.0)
            angulo = float(np.degrees(np.arccos(coseno)))
            angulo_texto = f"{angulo:.3f} grados"
        else:
            angulo_texto = "No definido si algún vector es cero"

        cruz_texto = fmt(producto_cruz)
        ua_texto = fmt(unit_a) if unit_a is not None else "No definido (vector cero)"
        ub_texto = fmt(unit_b) if unit_b is not None else "No definido (vector cero)"

        # ====================================================
        # AQUI VA: CONSTRUIR EL PANEL DE RESULTADOS [OK]
        # ====================================================
        
        lineas = [
            "RESULTADOS",
            "",
            f"Vector A = {fmt(a)}",
            f"Vector B = {fmt(b)}",
            f"|A| = {mag_a:.5f}",
            f"|B| = {mag_b:.5f}",
            f"Distancia entre puntas |A-B| = {distancia:.5f}",
            "",
            f"Unitario de A = {ua_texto}",
            f"Unitario de B = {ub_texto}",
            "",
            f"A · B = {producto_punto:.5f}",
            f"Ángulo entre A y B = {angulo_texto}",
            f"¿Perpendiculares? {'Sí' if perpendicular else 'No'}",
            "",
            f"A × B = {cruz_texto}",
            f"|A × B| = {magnitud(producto_cruz):.5f}",
        ]


        if proyeccion is not None:
            lineas.extend([
                "",
                f"Proyección de A sobre B = {fmt(proyeccion)}",
                f"Componente perpendicular = {fmt(resto)}",
                f"|Proyección| = {magnitud(proyeccion):.5f}",
            ])
        else:
            lineas.extend([
                "",
                "Proyección de A sobre B: no definida",
                "porque B es el vector cero."
            ])

        lineas.extend([
            "",
            "Lectura visual:",
            "Azul: A | Naranja: B",
            "Verde: proyección de A sobre B",
            "Morado punteado: diferencia A - proyección",
            "Gris discontinuo: segmento entre las puntas",
        ])


        # ====================================================
        # AQUI VA: MOSTRAR LOS RESULTADOS EN EL PANEL y ACTUALIZAR LA REPRESENTACIÓN VISUAL
        # ====================================================
        
        self.ax_info.text(
            0.0, 1.0,
            "\n".join(lineas),
            va="top",
            ha="left",
            fontsize=10,
            family="monospace",
            linespacing=1.25
        )
        
        self.fig.canvas.draw_idle()


def main():
    ExploradorVectores()
    plt.show()


if __name__ == "__main__":
    main()