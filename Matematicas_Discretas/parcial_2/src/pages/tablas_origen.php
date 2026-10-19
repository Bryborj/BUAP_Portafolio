<?php
require "../config/conection.php";

try {
    $pdo = conect();
    $connected = true;

    // 1. Tabla Principal: film (3 filas)
    $stmtFilm = $pdo->query("SELECT film_id, title, release_year, rental_rate, length, rating FROM film LIMIT 3");
    $films = $stmtFilm->fetchAll();

    // 2. Tabla Intermedia: film_actor (3 filas)
    $stmtFilmActor = $pdo->query("SELECT actor_id, film_id, last_update FROM film_actor LIMIT 3");
    $filmActors = $stmtFilmActor->fetchAll();

    // 3. Tabla Relacionada: actor (3 filas)
    $stmtActor = $pdo->query("SELECT actor_id, first_name, last_name, last_update FROM actor LIMIT 3");
    $actors = $stmtActor->fetchAll();

    // 4. Tabla Intermedia: film_category (3 filas)
    $stmtFilmCat = $pdo->query("SELECT film_id, category_id, last_update FROM film_category LIMIT 3");
    $filmCategories = $stmtFilmCat->fetchAll();

    // 5. Tabla Relacionada: category (3 filas)
    $stmtCat = $pdo->query("SELECT category_id, name, last_update FROM category LIMIT 3");
    $categories = $stmtCat->fetchAll();
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
    <title>Tablas de Origen (Juntura) | Mates Discretas</title>
    <style>
        body { font-family: system-ui, -apple-system, sans-serif; background: #f4f6f8; color: #333; margin: 30px 20px; }
        .card { background: white; padding: 28px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.08); max-width: 1100px; margin: 0 auto; }
        .header-bar { display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; padding-bottom: 16px; border-bottom: 1px solid #e2e8f0; }
        .btn-back { background: #1a73e8; color: white; padding: 8px 16px; border-radius: 6px; text-decoration: none; font-weight: 500; font-size: 14px; display: inline-flex; align-items: center; gap: 6px; }
        .btn-back:hover { background: #1557b0; }
        .section-box { margin-bottom: 30px; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px; }
        .section-title { margin: 0 0 8px 0; color: #0f172a; font-size: 18px; display: flex; align-items: center; gap: 8px; }
        .tag-pk { background: #dbeafe; color: #1e40af; padding: 2px 8px; border-radius: 4px; font-size: 12px; font-weight: 600; }
        .tag-fk { background: #fef3c7; color: #92400e; padding: 2px 8px; border-radius: 4px; font-size: 12px; font-weight: 600; }
        .table-desc { color: #64748b; font-size: 13px; margin: 0 0 12px 0; }
        .table-container { overflow-x: auto; background: white; border: 1px solid #e2e8f0; border-radius: 6px; }
        table { width: 100%; border-collapse: collapse; min-width: 500px; }
        th, td { border-bottom: 1px solid #e2e8f0; padding: 10px 14px; text-align: left; font-size: 13px; }
        th { background: #f1f5f9; color: #334155; font-weight: 600; }
        tr:last-child td { border-bottom: none; }
        .badge-danger { background: #fce8e6; color: #c5221f; padding: 6px 12px; border-radius: 4px; font-weight: bold; display: inline-block; }
    </style>
</head>
<body>
    <div class="card">
        <div class="header-bar">
            <div>
                <h1 style="margin: 0; font-size: 24px;">Tablas de Origen de la Juntura</h1>
                <p style="margin: 4px 0 0 0; color: #64748b; font-size: 14px;">Muestra de las 5 tablas base que intervienen en la operación de relación (3 filas cada una)</p>
            </div>
            <div style="display: flex; gap: 10px; flex-wrap: wrap;">
                <a href="proyections.php" class="btn-back" style="background: #7c3aed;">📊 Proyecciones</a>
                <a href="join.php" class="btn-back">← Volver a JOIN</a>
            </div>
        </div>

        <?php if ($connected): ?>

            <!-- 1. FILM -->
            <div class="section-box">
                <h2 class="section-title">
                    <span>1. Tabla Principal: <code>film</code></span>
                    <span class="tag-pk">PK: film_id</span>
                </h2>
                <p class="table-desc">Almacena el catálogo central de películas. Cada película posee un identificador único <code>film_id</code>.</p>
                <div class="table-container">
                    <table>
                        <thead>
                            <tr>
                                <th>film_id</th>
                                <th>title</th>
                                <th>release_year</th>
                                <th>rental_rate</th>
                                <th>length</th>
                                <th>rating</th>
                            </tr>
                        </thead>
                        <tbody>
                            <?php foreach ($films as $row): ?>
                                <tr>
                                    <td><strong><?= htmlspecialchars($row['film_id']); ?></strong></td>
                                    <td><?= htmlspecialchars($row['title']); ?></td>
                                    <td><?= htmlspecialchars($row['release_year']); ?></td>
                                    <td>$<?= htmlspecialchars($row['rental_rate']); ?></td>
                                    <td><?= htmlspecialchars($row['length']); ?> min</td>
                                    <td><?= htmlspecialchars($row['rating']); ?></td>
                                </tr>
                            <?php endforeach; ?>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- 2. FILM_ACTOR -->
            <div class="section-box">
                <h2 class="section-title">
                    <span>2. Tabla Intermedia: <code>film_actor</code></span>
                    <span class="tag-fk">FK: film_id</span>
                    <span class="tag-fk">FK: actor_id</span>
                </h2>
                <p class="table-desc">Resuelve la relación muchos a muchos (M:N) entre películas y actores vinculando las claves foráneas.</p>
                <div class="table-container">
                    <table>
                        <thead>
                            <tr>
                                <th>actor_id</th>
                                <th>film_id</th>
                                <th>last_update</th>
                            </tr>
                        </thead>
                        <tbody>
                            <?php foreach ($filmActors as $row): ?>
                                <tr>
                                    <td><strong><?= htmlspecialchars($row['actor_id']); ?></strong></td>
                                    <td><strong><?= htmlspecialchars($row['film_id']); ?></strong></td>
                                    <td><?= htmlspecialchars($row['last_update']); ?></td>
                                </tr>
                            <?php endforeach; ?>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- 3. ACTOR -->
            <div class="section-box">
                <h2 class="section-title">
                    <span>3. Tabla Relacionada: <code>actor</code></span>
                    <span class="tag-pk">PK: actor_id</span>
                </h2>
                <p class="table-desc">Catálogo de actores con su identificador y nombre completo.</p>
                <div class="table-container">
                    <table>
                        <thead>
                            <tr>
                                <th>actor_id</th>
                                <th>first_name</th>
                                <th>last_name</th>
                                <th>last_update</th>
                            </tr>
                        </thead>
                        <tbody>
                            <?php foreach ($actors as $row): ?>
                                <tr>
                                    <td><strong><?= htmlspecialchars($row['actor_id']); ?></strong></td>
                                    <td><?= htmlspecialchars($row['first_name']); ?></td>
                                    <td><?= htmlspecialchars($row['last_name']); ?></td>
                                    <td><?= htmlspecialchars($row['last_update']); ?></td>
                                </tr>
                            <?php endforeach; ?>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- 4. FILM_CATEGORY -->
            <div class="section-box">
                <h2 class="section-title">
                    <span>4. Tabla Intermedia: <code>film_category</code></span>
                    <span class="tag-fk">FK: film_id</span>
                    <span class="tag-fk">FK: category_id</span>
                </h2>
                <p class="table-desc">Asocia las películas a una o varias categorías temáticas.</p>
                <div class="table-container">
                    <table>
                        <thead>
                            <tr>
                                <th>film_id</th>
                                <th>category_id</th>
                                <th>last_update</th>
                            </tr>
                        </thead>
                        <tbody>
                            <?php foreach ($filmCategories as $row): ?>
                                <tr>
                                    <td><strong><?= htmlspecialchars($row['film_id']); ?></strong></td>
                                    <td><strong><?= htmlspecialchars($row['category_id']); ?></strong></td>
                                    <td><?= htmlspecialchars($row['last_update']); ?></td>
                                </tr>
                            <?php endforeach; ?>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- 5. CATEGORY -->
            <div class="section-box">
                <h2 class="section-title">
                    <span>5. Tabla Relacionada: <code>category</code></span>
                    <span class="tag-pk">PK: category_id</span>
                </h2>
                <p class="table-desc">Catálogo de géneros cinematográficos (Action, Animation, Children, etc.).</p>
                <div class="table-container">
                    <table>
                        <thead>
                            <tr>
                                <th>category_id</th>
                                <th>name</th>
                                <th>last_update</th>
                            </tr>
                        </thead>
                        <tbody>
                            <?php foreach ($categories as $row): ?>
                                <tr>
                                    <td><strong><?= htmlspecialchars($row['category_id']); ?></strong></td>
                                    <td><?= htmlspecialchars($row['name']); ?></td>
                                    <td><?= htmlspecialchars($row['last_update']); ?></td>
                                </tr>
                            <?php endforeach; ?>
                        </tbody>
                    </table>
                </div>
            </div>

            <div style="text-align: center; margin-top: 20px;">
                <a href="join.php" class="btn-back">← Volver a la Juntura (JOIN)</a>
            </div>

        <?php else: ?>
            <p><span class="badge-danger">Error al conectar: <?= htmlspecialchars($errorMessage); ?></span></p>
        <?php endif; ?>
    </div>
</body>
</html>
