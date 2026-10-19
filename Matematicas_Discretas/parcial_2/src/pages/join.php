<?php

require "../config/conection.php";

try {
    $pdo = conect();
    $connected = true;
    $sqtm = $pdo->query("SELECT fl.*, fc.*, fa.*, fd.* , c.*, a.*
        FROM film AS fl
        JOIN film_category AS fc ON fl.film_id = fc.film_id
        JOIN film_actor AS fa ON fl.film_id = fa.film_id
        JOIN film_text AS fd ON fl.film_id = fd.film_id 
        JOIN category AS c ON fc.category_id = c.category_id
        JOIN actor AS a ON fa.actor_id = a.actor_id
        ORDER BY fl.title
    ");
    $films = $sqtm->fetchAll();
}
catch (\PDOException $e) {
    $connected = false;
    $errorMessage = $e->getMessage();
}

/** Ejemplo
 * SELECT tp.*, ti.*, tv.*
 * FROM tabla_principal AS tp
 * JOIN table_ids AS ti ON tp.id = ti.tabla_id
 * JOIN table_values AS tv ON ti.value_id = tv.id;
 */
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JUNTURAS | Mates Discretas</title>
    <style>
        body { font-family: system-ui, -apple-system, sans-serif; background: #f4f6f8; color: #333; margin: 40px; }
        .card { background: white; padding: 24px; border-radius: 8px; box-shadow: 0 2px 6px rgba(0,0,0,0.1); max-width: 800px; margin: 0 auto; }
        .badge-success { background: #e6f4ea; color: #137333; padding: 6px 12px; border-radius: 4px; font-weight: bold; display: inline-block; }
        .badge-danger { background: #fce8e6; color: #c5221f; padding: 6px 12px; border-radius: 4px; font-weight: bold; display: inline-block; }
        .stats { display: flex; gap: 20px; margin: 20px 0; }
        .stat-box { flex: 1; background: #e8f0fe; padding: 16px; border-radius: 6px; text-align: center; }
        .stat-box h3 { margin: 0; color: #1a73e8; font-size: 24px; }
        .stat-box p { margin: 4px 0 0; color: #5f6368; font-size: 14px; }
        table { width: 100%; border-collapse: collapse; margin-top: 16px; }
        th, td { border: 1px solid #dadce0; padding: 10px; text-align: left; }
        th { background: #f8f9fa; }
    </style>
</head>
<body>
    <div class="card">
        <h1>Junturas x 3</h1>
        <?php if ($connected): ?>
            <p>
                <span class="badge-success">
                    La conexion con la base de datos fue exitosa
                </span>
            </p>
            <h3>Peliculas juntura con Categorias</h3>
            <h3>Peliculas juntura con actores</h3>
            <h3>Peliculas juntura con descripcion</h3>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Titulo</th>
                        <th>Año</th>
                        <th>Actor</th>
                        <th>Duracion</th>
                        <th>Clasificación</th>
                        <th>Categoria</th>
                        <th>Descripción</th>
                    </tr>
                </thead>
                <tbody>
                    <?php foreach ($films as $film): ?>
                        <tr>
                            <td><?= htmlspecialchars($film['film_id']); ?></td>
                            <td><?= htmlspecialchars($film['title']); ?></td>
                            <td><?= htmlspecialchars($film['release_year']); ?></td>
                            <td><?= htmlspecialchars($film['first_name']); ?></td>
                            <td><?= htmlspecialchars($film['length']); ?></td>
                            <td><?= htmlspecialchars($film['rating']); ?></td>
                            <td><?= htmlspecialchars($film['name']); ?></td>
                            <td><?= htmlspecialchars($film['description']); ?></td>
                        </tr>
                        <?php endforeach; ?>
                </tbody>
            </table>
        <?php else: ?>
            <p>
                <span class="badge-danger">Error al conectar con la base de datos: <?= htmlspecialchars($errorMessage); ?>  ?> </span>
            </p>
        <?php endif; ?>
    </div>
</body>
</html>
