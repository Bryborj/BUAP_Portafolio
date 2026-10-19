<?php
$host = 'db';
$db   = 'sakila';
$user = 'devuser';
$pass = 'root';
$charset = 'utf8mb4';

$dsn = "mysql:host=$host;dbname=$db;charset=$charset";
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false,
];

try {
    $pdo = new PDO($dsn, $user, $pass, $options);
    $connected = true;

    // Métricas generales
    $filmCount = $pdo->query("SELECT COUNT(*) FROM film")->fetchColumn();
    $actorCount = $pdo->query("SELECT COUNT(*) FROM actor")->fetchColumn();
    $customerCount = $pdo->query("SELECT COUNT(*) FROM customer")->fetchColumn();

    // Muestra de películas
    $stmt = $pdo->query("SELECT film_id, title, release_year, rental_rate, length FROM film LIMIT 5");
    $sampleFilms = $stmt->fetchAll();
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
    <title>Sakila DB - Matemáticas Discretas (Parcial 2)</title>
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
        <h1>Entorno Parcial 2: Sakila DB</h1>
        <p>PHP Versión: <strong><?= phpversion(); ?></strong></p>

        <?php if ($connected): ?>
            <p><span class="badge-success">Conexión exitosa a la base de datos 'sakila' como 'devuser'</span></p>

            <div style="display: flex; gap: 10px; margin: 20px 0; flex-wrap: wrap;">
                <a href="pages/conditions.php" style="background: #d97706; color: white; padding: 10px 18px; border-radius: 6px; text-decoration: none; font-weight: bold; font-size: 14px;">Condiciones (Filtros)</a>
                <a href="pages/proyections.php" style="background: #7c3aed; color: white; padding: 10px 18px; border-radius: 6px; text-decoration: none; font-weight: bold; font-size: 14px;">Proyecciones</a>
                <a href="pages/join.php" style="background: #1a73e8; color: white; padding: 10px 18px; border-radius: 6px; text-decoration: none; font-weight: bold; font-size: 14px;">Junturas (JOINs)</a>
            </div>

            <div class="stats">
                <div class="stat-box">
                    <h3><?= htmlspecialchars($filmCount); ?></h3>
                    <p>Películas</p>
                </div>
                <div class="stat-box">
                    <h3><?= htmlspecialchars($actorCount); ?></h3>
                    <p>Actores</p>
                </div>
            </div>

            <h3>Muestra de Películas (sakila.film)</h3>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Título</th>
                        <th>Año</th>
                        <th>Precio Renta</th>
                        <th>Duración (min)</th>
                    </tr>
                </thead>
                <tbody>
                    <?php foreach ($sampleFilms as $film): ?>
                        <tr>
                            <td><?= htmlspecialchars($film['film_id']); ?></td>
                            <td><?= htmlspecialchars($film['title']); ?></td>
                            <td><?= htmlspecialchars($film['release_year']); ?></td>
                            <td>$<?= htmlspecialchars($film['rental_rate']); ?></td>
                            <td><?= htmlspecialchars($film['length']); ?></td>
                        </tr>
                    <?php endforeach; ?>
                </tbody>
            </table>
        <?php else: ?>
            <p><span class="badge-danger">✗ Error al conectar: <?= htmlspecialchars($errorMessage); ?></span></p>
        <?php endif; ?>
    </div>
</body>
</html>