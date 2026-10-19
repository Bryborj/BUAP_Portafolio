# Relaciones de conjuntos

## Objetivo:

Esta practica busca ver la aplicacion de los conceptos vistos en clase sobre la realcion de los conjuntos en la programacion, mas especificamente en bases de datos.

## Instrucciones de Teams

LA PRACTICA CONSISTE EN BUSCAR UNA BASE DE DATOS DE MINIMO 20 DATOS Y HACER UN PROGRAMA EN DONDE PUEDADN OBTENER

* 6 Condiciones (Filtros/Columnas)
* 6  Proyecciones (Filtro por columna)
* 3 Join (Relacion entre tablas)

## Sobre el proyecto

Se ah utilizado una BD relacional en MySQL obtenida de https://dataedo.com/kb/databases/mariadb/sample-databases

Lenguajes de desarrollo:

- PHP
- JavaScript
- SQL

## Condiciones (Filtros de datos) x 6

En la tabla peliculas "film".

- Año (release_year)
- Duracion (length)
- Contiene "x" letra el titulo y Año (title, release_year)
- Publico dirigido / clasificacion (Formato estadounidence) (raiting)
- Categoria (category) (requiere juntura 3)
- Actor(es) (actor_id) (juntura 2)

## Proyecciones (Solo dejar columnas)  x 6

- P_{1,2, 3}
- P_{1,2,4}
- P_{1,4,6}
- P_{1, 4}
- P_{1, 5}
- P_{1, 6}

## Join x 3

- Tabla films con Tabla film_category mas tabla category
- Tabla films con Tabla film_actor mas actor
- Tabla films con Tabla film_text
- Tabla con todas las junturas anteriores
