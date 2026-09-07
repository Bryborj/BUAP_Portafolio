# Mapa con Tiles de 8x8

###Scripts necesarios

- tiles_Struct_Get.py
- Proyecto_Eva_1.py

### EJecución

Crear entorno virtual

```bash
python -m venv <nombre que quieras>
# Entrar al etorno virtual
# Linux
source <nombre que quieras>/bin/activate
# Windows
<nombre que quieras>/Scripts/activate
```

Instalar dependencias necesarias

```bash
pip install -r requeriments.txt
```

Ejecución del script principal

```bash
python Proyecto_Eva_1.py
```

> [!NOTE] \
> Por defecto se abriran 2 ventanas, una del mapa completo y otra con un view port de 8x8 tiles es decir 64x64 unidades. \
> El tamaño del mapa completo es de 40 x 40 tiles es decir 320 x 320 unidades.

### Controles del viewport

| Tecla         | Acción                                |
| ------------- | ------------------------------------- |
| Arriba / W    | Mover el view port hacia arriba       |
| Abajo / S     | Mover el view port hacia abajo        |
| Izquierda / A | Mover el view port hacia la izquierda |
| Derecha / D   | Mover el view port hacia la derecha   |
| Esc           | Cerrar el programa                    |
