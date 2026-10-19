<?php
require "../config/conection.php";

$limit = isset($_GET['limit']) ? intval($_GET['limit']) : 10;
if ($limit < 1) {
    $limit = 1;
} elseif ($limit > 1000) {
    $limit = 1000;
}

try {
    $pdo = conect();
    $connected = true;

    $query = "SELECT 
        fl.film_id,
        fl.title,
        fl.release_year,
        fl.length,
        fl.rating,
        fl.description,
        GROUP_CONCAT(DISTINCT c.name ORDER BY c.name SEPARATOR ', ') AS categorias,
        GROUP_CONCAT(DISTINCT CONCAT(a.first_name, ' ', a.last_name) ORDER BY a.first_name, a.last_name SEPARATOR ', ') AS actores
    FROM film AS fl
    LEFT JOIN film_category AS fc ON fl.film_id = fc.film_id
    LEFT JOIN category AS c ON fc.category_id = c.category_id
    LEFT JOIN film_actor AS fa ON fl.film_id = fa.film_id
    LEFT JOIN actor AS a ON fa.actor_id = a.actor_id
    GROUP BY fl.film_id
    ORDER BY fl.title
    LIMIT :limit";

    $sqtm = $pdo->prepare($query);
    $sqtm->bindValue(':limit', $limit, PDO::PARAM_INT);
    $sqtm->execute();
    $films = $sqtm->fetchAll();
}
catch (\PDOException $e) {
    $connected = false;
    $errorMessage = $e->getMessage();
}
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JUNTURAS | Mates Discretas</title>
    <style>
        body { font-family: system-ui, -apple-system, sans-serif; background: #f4f6f8; color: #333; margin: 30px 20px; }
        .card { background: white; padding: 28px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.08); max-width: 1200px; margin: 0 auto; }
        .badge-success { background: #e6f4ea; color: #137333; padding: 6px 12px; border-radius: 4px; font-weight: bold; display: inline-block; }
        .badge-danger { background: #fce8e6; color: #c5221f; padding: 6px 12px; border-radius: 4px; font-weight: bold; display: inline-block; }
        .header-actions { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 15px; margin: 20px 0; padding: 15px; background: #f8f9fa; border-radius: 8px; border: 1px solid #e2e8f0; }
        .selector-form { display: flex; align-items: center; gap: 10px; flex-wrap: wrap; }
        .selector-form input[type="number"] { width: 90px; padding: 7px 10px; border: 1px solid #cbd5e1; border-radius: 6px; font-size: 15px; }
        .btn-primary { background: #1a73e8; color: white; border: none; padding: 8px 16px; border-radius: 6px; cursor: pointer; font-weight: 500; font-size: 14px; text-decoration: none; display: inline-flex; align-items: center; }
        .btn-primary:hover { background: #1557b0; }
        .btn-outline { background: #0f9d58; color: white; padding: 8px 16px; border-radius: 6px; text-decoration: none; font-weight: 500; font-size: 14px; display: inline-flex; align-items: center; gap: 6px; }
        .btn-outline:hover { background: #0b8043; }
        .chip { display: inline-block; padding: 4px 10px; background: #e2e8f0; color: #334155; text-decoration: none; border-radius: 16px; font-size: 13px; font-weight: 500; }
        .chip:hover, .chip.active { background: #1a73e8; color: white; }
        .table-container { width: 100%; overflow-x: auto; margin-top: 15px; border: 1px solid #e2e8f0; border-radius: 8px; }
        table { width: 100%; border-collapse: collapse; min-width: 900px; }
        th, td { border-bottom: 1px solid #e2e8f0; padding: 12px 14px; text-align: left; vertical-align: top; font-size: 14px; }
        th { background: #f1f5f9; color: #1e293b; font-weight: 600; position: sticky; top: 0; }
        tr:hover { background: #f8fafc; }
        .actors-cell { max-width: 300px; color: #1e293b; line-height: 1.4; }
        .desc-cell { max-width: 250px; color: #64748b; font-size: 13px; line-height: 1.4; }
        .cat-tag { background: #e0f2fe; color: #0369a1; padding: 3px 8px; border-radius: 4px; font-size: 12px; font-weight: 600; display: inline-block; }
    </style>
</head>
<body>
    <div class="card">
        <h1>Junturas Relacionales (JOINs)</h1>
        <p style="color: #64748b; margin-top: -10px;">Aplicación de conjuntos y relaciones: <code>film</code> ⨝ <code>film_category</code> ⨝ <code>category</code> ⨝ <code>film_actor</code> ⨝ <code>actor</code></p>

        <?php if ($connected): ?>
            <p>
                <span class="badge-success">Conexión con la base de datos realizada con éxito</span>
            </p>

            <div class="header-actions">
                <form method="GET" class="selector-form">
                    <label for="limit"><strong>Límite de filas:</strong></label>
                    <input type="number" id="limit" name="limit" min="1" max="1000" value="<?= htmlspecialchars($limit); ?>">
                    <button type="submit" class="btn-primary">Aplicar</button>
                    <span style="color: #94a3b8;">|</span>
                    <span style="color: #64748b; font-size: 13px;">Rápido:</span>
                    <a href="?limit=5" class="chip <?= $limit == 5 ? 'active' : '' ?>">5</a>
                    <a href="?limit=10" class="chip <?= $limit == 10 ? 'active' : '' ?>">10</a>
                    <a href="?limit=25" class="chip <?= $limit == 25 ? 'active' : '' ?>">25</a>
                    <a href="?limit=50" class="chip <?= $limit == 50 ? 'active' : '' ?>">50</a>
                    <a href="?limit=100" class="chip <?= $limit == 100 ? 'active' : '' ?>">100</a>
                </form>

                <div style="display: flex; gap: 10px; flex-wrap: wrap;">
                    <a href="conditions.php" class="btn-primary" style="background: #d97706;">
                        Condiciones
                    </a>
                    <a href="proyections.php" class="btn-primary" style="background: #7c3aed;">
                        Proyecciones
                    </a>
                    <a href="tablas_origen.php" class="btn-outline">
                        Tablas de origen (3 filas c/u)
                    </a>
                </div>
            </div>

            <p style="font-size: 14px; color: #64748b;">
                Mostrando <strong><?= count($films); ?></strong> película(s). Los actores relacionados han sido agrupados en una sola celda.
            </p>

            <div class="table-container">
                <table>
                    <thead>
                        <tr>
                            <th style="width: 50px;">ID</th>
                            <th>Título</th>
                            <th style="width: 60px;">Año</th>
                            <th>Categoría(s)</th>
                            <th style="width: 320px;">Actores (agrupados en 1 celda)</th>
                            <th style="width: 80px;">Duración</th>
                            <th style="width: 90px;">Clasificación</th>
                            <th>Descripción</th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php if (empty($films)): ?>
                            <tr>
                                <td colspan="8" style="text-align: center; color: #94a3b8; padding: 20px;">No se encontraron registros.</td>
                            </tr>
                        <?php else: ?>
                            <?php foreach ($films as $film): ?>
                                <tr>
                                    <td><strong><?= htmlspecialchars($film['film_id']); ?></strong></td>
                                    <td><strong><?= htmlspecialchars($film['title']); ?></strong></td>
                                    <td><?= htmlspecialchars($film['release_year']); ?></td>
                                    <td>
                                        <span class="cat-tag"><?= htmlspecialchars($film['categorias'] ?? 'Sin categoría'); ?></span>
                                    </td>
                                    <td class="actors-cell">
                                        <?= htmlspecialchars($film['actores'] ?? 'Sin actores asignados'); ?>
                                    </td>
                                    <td><?= htmlspecialchars($film['length']); ?> min</td>
                                    <td><?= htmlspecialchars($film['rating']); ?></td>
                                    <td class="desc-cell"><?= htmlspecialchars($film['description']); ?></td>
                                </tr>
                            <?php endforeach; ?>
                        <?php endif; ?>
                    </tbody>
                </table>
            </div>
        <?php else: ?>
            <p>
                <span class="badge-danger">Error al conectar con la base de datos: <?= htmlspecialchars($errorMessage); ?></span>
            </p>
        <?php endif; ?>
    </div>
</body>
</html>
