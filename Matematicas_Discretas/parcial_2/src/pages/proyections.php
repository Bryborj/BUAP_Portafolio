<?php
include '../config/conection.php';

$limit = isset($_GET['limit']) ? intval($_GET['limit']) : 3;
if ($limit < 1)
    $limit = 1;
elseif ($limit > 1000)
    $limit = 1000;

try {
    $pdo = conect();
    $connected = true;

    // Tabla Origen Base R (6 columnas)
    $query_base = "SELECT 
        fl.film_id, 
        fl.title, 
        fl.release_year, 
        fl.rental_rate, 
        fl.length, 
        fl.rating 
    FROM film AS fl 
    ORDER BY fl.film_id 
    LIMIT :limit";
    $stmtFilm = $pdo->prepare($query_base);
    $stmtFilm->bindValue(':limit', $limit, PDO::PARAM_INT);
    $stmtFilm->execute();
    $tabla_origen = $stmtFilm->fetchAll();

    // Proyección 1: P_{1, 2, 3} -> (film_id, title, release_year)
    $query = "SELECT
        fl.film_id, 
        fl.title,
        fl.release_year
    FROM film AS fl
    ORDER BY fl.film_id
    LIMIT :limit";
    $sqtm = $pdo->prepare($query);
    $sqtm->bindValue(':limit', $limit, PDO::PARAM_INT);
    $sqtm->execute();
    $p_1 = $sqtm->fetchAll();

    // Proyección 2: P_{1, 2, 4} -> (film_id, title, rental_rate)
    $query = "SELECT
        fl.film_id, 
        fl.title,
        fl.rental_rate
    FROM film AS fl
    ORDER BY fl.film_id
    LIMIT :limit";
    $sqtm = $pdo->prepare($query);
    $sqtm->bindValue(':limit', $limit, PDO::PARAM_INT);
    $sqtm->execute();
    $p_2 = $sqtm->fetchAll();

    // Proyección 3: P_{1, 4, 6} -> (film_id, rental_rate, rating)
    $query = "SELECT
        fl.film_id, 
        fl.rental_rate,
        fl.rating
    FROM film AS fl
    ORDER BY fl.film_id
    LIMIT :limit";
    $sqtm = $pdo->prepare($query);
    $sqtm->bindValue(':limit', $limit, PDO::PARAM_INT);
    $sqtm->execute();
    $p_3 = $sqtm->fetchAll();

    // Proyección 4: P_{1, 4} -> (film_id, rental_rate)
    $query = "SELECT
        fl.film_id, 
        fl.rental_rate
    FROM film AS fl
    ORDER BY fl.film_id
    LIMIT :limit";
    $sqtm = $pdo->prepare($query);
    $sqtm->bindValue(':limit', $limit, PDO::PARAM_INT);
    $sqtm->execute();
    $p_4 = $sqtm->fetchAll();

    // Proyección 5: P_{1, 5} -> (film_id, length)
    $query = "SELECT
        fl.film_id, 
        fl.length
    FROM film AS fl
    ORDER BY fl.film_id
    LIMIT :limit";
    $sqtm = $pdo->prepare($query);
    $sqtm->bindValue(':limit', $limit, PDO::PARAM_INT);
    $sqtm->execute();
    $p_5 = $sqtm->fetchAll();

    // Proyección 6: P_{1, 6} -> (film_id, rating)
    $query = "SELECT
        fl.film_id, 
        fl.rating
    FROM film AS fl
    ORDER BY fl.film_id
    LIMIT :limit";
    $sqtm = $pdo->prepare($query);
    $sqtm->bindValue(':limit', $limit, PDO::PARAM_INT);
    $sqtm->execute();
    $p_6 = $sqtm->fetchAll();

} catch (\PDOException $e) {
    $connected = false;
    $errorMessage = $e->getMessage();
}
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!--<script src="https://jsdelivr.net"></script>-->
    <title>PROYECCIONES | Mates Discretas</title>
    <style>
        body { font-family: system-ui, -apple-system, sans-serif; background: #f4f6f8; color: #333; margin: 30px 20px; }
        .card { background: white; padding: 28px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.08); max-width: 1200px; margin: 0 auto; }
        .badge-success { background: #e6f4ea; color: #137333; padding: 6px 12px; border-radius: 4px; font-weight: bold; display: inline-block; }
        .badge-danger { background: #fce8e6; color: #c5221f; padding: 6px 12px; border-radius: 4px; font-weight: bold; display: inline-block; }
        .header-actions { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 15px; margin: 20px 0; padding: 15px; background: #f8f9fa; border-radius: 8px; border: 1px solid #e2e8f0; }
        .selector-form { display: flex; align-items: center; gap: 10px; flex-wrap: wrap; }
        .selector-form input[type="number"] { width: 90px; padding: 7px 10px; border: 1px solid #cbd5e1; border-radius: 6px; font-size: 15px; }
        .btn-primary { background: #1a73e8; color: white; border: none; padding: 8px 16px; border-radius: 6px; cursor: pointer; font-weight: 500; font-size: 14px; text-decoration: none; }
        .btn-primary:hover { background: #1557b0; }
        .btn-outline { background: #0f9d58; color: white; padding: 8px 16px; border-radius: 6px; text-decoration: none; font-weight: 500; font-size: 14px; }
        .btn-outline:hover { background: #0b8043; }
        .chip { display: inline-block; padding: 4px 10px; background: #e2e8f0; color: #334155; text-decoration: none; border-radius: 16px; font-size: 13px; font-weight: 500; }
        .chip:hover, .chip.active { background: #1a73e8; color: white; }
        
        .box-base { background: #f0f7ff; border: 2px solid #bfdbfe; border-radius: 8px; padding: 18px; margin-bottom: 30px; }
        .col-index { display: inline-block; background: #1e40af; color: white; border-radius: 12px; width: 20px; height: 20px; text-align: center; font-size: 12px; line-height: 20px; margin-right: 4px; }
        
        .grid-projections { display: grid; grid-template-columns: repeat(auto-fit, minmax(360px, 1fr)); gap: 20px; margin-top: 20px; }
        .proj-card { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; }
        .proj-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; border-bottom: 1px solid #e2e8f0; padding-bottom: 8px; }
        .proj-title { font-size: 17px; font-weight: bold; color: #0f172a; margin: 0; }
        .proj-badge { background: #e0f2fe; color: #0369a1; padding: 3px 8px; border-radius: 4px; font-size: 12px; font-weight: 600; }
        
        .table-container { overflow-x: auto; background: white; border: 1px solid #e2e8f0; border-radius: 6px; margin-top: 8px; }
        table { width: 100%; border-collapse: collapse; }
        th, td { border-bottom: 1px solid #e2e8f0; padding: 9px 12px; text-align: left; font-size: 13px; }
        th { background: #f1f5f9; color: #1e293b; font-weight: 600; }
        tr:last-child td { border-bottom: none; }
        tr:hover { background: #fbfcfd; }
    </style>
</head>
<body>
    <div class="card">
        <h1>Proyecciones Relacionales</h1>
        <p style="color: #64748b; margin-top: -10px;">
            En Matemáticas Discretas, la <strong>proyección</strong> $P_{i_1, i_2, \dots, i_k}(R)$ filtra y conserva únicamente las columnas indicadas de una relación base $R$.
        </p>

        <?php if ($connected): ?>
            <p>
                <span class="badge-success">Conexión con la base de datos realizada con éxito</span>
            </p>

            <div class="header-actions">
                <form method="GET" class="selector-form">
                    <label for="limit"><strong>Filas a mostrar:</strong></label>
                    <input type="number" id="limit" name="limit" min="1" max="1000" value="<?= htmlspecialchars($limit); ?>">
                    <button type="submit" class="btn-primary">Aplicar</button>
                    <span style="color: #94a3b8;">|</span>
                    <span style="color: #64748b; font-size: 13px;">Rápido:</span>
                    <a href="?limit=3" class="chip <?= $limit == 3 ? 'active' : '' ?>">3</a>
                    <a href="?limit=5" class="chip <?= $limit == 5 ? 'active' : '' ?>">5</a>
                    <a href="?limit=10" class="chip <?= $limit == 10 ? 'active' : '' ?>">10</a>
                    <a href="?limit=20" class="chip <?= $limit == 20 ? 'active' : '' ?>">20</a>
                </form>

                <div style="display: flex; gap: 10px; flex-wrap: wrap;">
                    <a href="conditions.php" class="btn-outline" style="background: #d97706;">Condiciones</a>
                    <a href="join.php" class="btn-outline">Ir a Junturas (JOINs)</a>
                    <a href="tablas_origen.php" class="btn-outline" style="background: #475569;">Tablas de Origen</a>
                </div>
            </div>

            <!-- TABLA BASE ORIGEN R -->
            <div class="box-base">
                <h2 style="margin: 0 0 6px 0; color: #1e3a8a; font-size: 19px;">
                    Tabla Origen Base $R$: <code>film</code> (6 Atributos / Columnas)
                </h2>
                <p style="margin: 0 0 12px 0; color: #475569; font-size: 13px;">
                    Todas las proyecciones se obtienen seleccionando subconjuntos de columnas a partir de esta relación base:
                </p>
                <div class="table-container">
                    <table>
                        <thead>
                            <tr>
                                <th><span class="col-index">1</span> film_id</th>
                                <th><span class="col-index">2</span> title</th>
                                <th><span class="col-index">3</span> release_year</th>
                                <th><span class="col-index">4</span> rental_rate</th>
                                <th><span class="col-index">5</span> length</th>
                                <th><span class="col-index">6</span> rating</th>
                            </tr>
                        </thead>
                        <tbody>
                            <?php foreach ($tabla_origen as $row): ?>
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

            <!-- GRID CON LAS 6 PROYECCIONES -->
            <h2 style="color: #0f172a; margin-top: 30px;">Las 6 Proyecciones Requeridas</h2>
            
            <div class="grid-projections">

                <!-- 1. P_{1, 2, 3} -->
                <div class="proj-card">
                    <div class="proj-header">
                        <span class="proj-title">Proyección 1: $P_{1, 2, 3}$</span>
                        <span class="proj-badge">Cols: 1, 2, 3</span>
                    </div>
                    <p style="font-size: 12px; color: #64748b; margin: 4px 0 8px 0;">
                        Preserva: <strong>film_id</strong>, <strong>title</strong>, <strong>release_year</strong>
                    </p>
                    <div class="table-container">
                        <table>
                            <thead>
                                <tr>
                                    <th>film_id</th>
                                    <th>title</th>
                                    <th>release_year</th>
                                </tr>
                            </thead>
                            <tbody>
                                <?php foreach ($p_1 as $row): ?>
                                    <tr>
                                        <td><strong><?= htmlspecialchars($row['film_id']); ?></strong></td>
                                        <td><?= htmlspecialchars($row['title']); ?></td>
                                        <td><?= htmlspecialchars($row['release_year']); ?></td>
                                    </tr>
                                <?php endforeach; ?>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- 2. P_{1, 2, 4} -->
                <div class="proj-card">
                    <div class="proj-header">
                        <span class="proj-title">Proyección 2: $P_{1, 2, 4}$</span>
                        <span class="proj-badge">Cols: 1, 2, 4</span>
                    </div>
                    <p style="font-size: 12px; color: #64748b; margin: 4px 0 8px 0;">
                        Preserva: <strong>film_id</strong>, <strong>title</strong>, <strong>rental_rate</strong>
                    </p>
                    <div class="table-container">
                        <table>
                            <thead>
                                <tr>
                                    <th>film_id</th>
                                    <th>title</th>
                                    <th>rental_rate</th>
                                </tr>
                            </thead>
                            <tbody>
                                <?php foreach ($p_2 as $row): ?>
                                    <tr>
                                        <td><strong><?= htmlspecialchars($row['film_id']); ?></strong></td>
                                        <td><?= htmlspecialchars($row['title']); ?></td>
                                        <td>$<?= htmlspecialchars($row['rental_rate']); ?></td>
                                    </tr>
                                <?php endforeach; ?>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- 3. P_{1, 4, 6} -->
                <div class="proj-card">
                    <div class="proj-header">
                        <span class="proj-title">Proyección 3: $P_{1, 4, 6}$</span>
                        <span class="proj-badge">Cols: 1, 4, 6</span>
                    </div>
                    <p style="font-size: 12px; color: #64748b; margin: 4px 0 8px 0;">
                        Preserva: <strong>film_id</strong>, <strong>rental_rate</strong>, <strong>rating</strong>
                    </p>
                    <div class="table-container">
                        <table>
                            <thead>
                                <tr>
                                    <th>film_id</th>
                                    <th>rental_rate</th>
                                    <th>rating</th>
                                </tr>
                            </thead>
                            <tbody>
                                <?php foreach ($p_3 as $row): ?>
                                    <tr>
                                        <td><strong><?= htmlspecialchars($row['film_id']); ?></strong></td>
                                        <td>$<?= htmlspecialchars($row['rental_rate']); ?></td>
                                        <td><?= htmlspecialchars($row['rating']); ?></td>
                                    </tr>
                                <?php endforeach; ?>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- 4. P_{1, 4} -->
                <div class="proj-card">
                    <div class="proj-header">
                        <span class="proj-title">Proyección 4: $P_{1, 4}$</span>
                        <span class="proj-badge">Cols: 1, 4</span>
                    </div>
                    <p style="font-size: 12px; color: #64748b; margin: 4px 0 8px 0;">
                        Preserva: <strong>film_id</strong>, <strong>rental_rate</strong>
                    </p>
                    <div class="table-container">
                        <table>
                            <thead>
                                <tr>
                                    <th>film_id</th>
                                    <th>rental_rate</th>
                                </tr>
                            </thead>
                            <tbody>
                                <?php foreach ($p_4 as $row): ?>
                                    <tr>
                                        <td><strong><?= htmlspecialchars($row['film_id']); ?></strong></td>
                                        <td>$<?= htmlspecialchars($row['rental_rate']); ?></td>
                                    </tr>
                                <?php endforeach; ?>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- 5. P_{1, 5} -->
                <div class="proj-card">
                    <div class="proj-header">
                        <span class="proj-title">Proyección 5: $P_{1, 5}$</span>
                        <span class="proj-badge">Cols: 1, 5</span>
                    </div>
                    <p style="font-size: 12px; color: #64748b; margin: 4px 0 8px 0;">
                        Preserva: <strong>film_id</strong>, <strong>length</strong>
                    </p>
                    <div class="table-container">
                        <table>
                            <thead>
                                <tr>
                                    <th>film_id</th>
                                    <th>length</th>
                                </tr>
                            </thead>
                            <tbody>
                                <?php foreach ($p_5 as $row): ?>
                                    <tr>
                                        <td><strong><?= htmlspecialchars($row['film_id']); ?></strong></td>
                                        <td><?= htmlspecialchars($row['length']); ?> min</td>
                                    </tr>
                                <?php endforeach; ?>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- 6. P_{1, 6} -->
                <div class="proj-card">
                    <div class="proj-header">
                        <span class="proj-title">Proyección 6: $P_{1, 6}$</span>
                        <span class="proj-badge">Cols: 1, 6</span>
                    </div>
                    <p style="font-size: 12px; color: #64748b; margin: 4px 0 8px 0;">
                        Preserva: <strong>film_id</strong>, <strong>rating</strong>
                    </p>
                    <div class="table-container">
                        <table>
                            <thead>
                                <tr>
                                    <th>film_id</th>
                                    <th>rating</th>
                                </tr>
                            </thead>
                            <tbody>
                                <?php foreach ($p_6 as $row): ?>
                                    <tr>
                                        <td><strong><?= htmlspecialchars($row['film_id']); ?></strong></td>
                                        <td><?= htmlspecialchars($row['rating']); ?></td>
                                    </tr>
                                <?php endforeach; ?>
                            </tbody>
                        </table>
                    </div>
                </div>

            </div>

        <?php else: ?>
            <p>
                <span class="badge-danger">Error al conectar con la base de datos: <?= htmlspecialchars($errorMessage); ?></span>
            </p>
        <?php endif; ?>
    </div>
    <script>
        // Tu texto en formato Markdown
        const textoMarkdown = "$P_{i_1, i_2, \dots, i_k}(R)$";

        // Convertir Markdown a HTML y asignarlo al div
        document.getElementById("regla").innerHTML = marked.parse(textoMarkdown);
    </script>
</body>
</html>