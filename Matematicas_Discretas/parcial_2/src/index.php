<?php
echo "<h1>Entorno PHP + Apache + MySQL</h1>";
echo "<p>PHP versión: " . phpversion() . "</p>";

$host = 'db';
$db   = 'practice_db';
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
    echo "<p style='color: green;'><strong>Conexión a MySQL exitosa!</strong></p>";
} catch (\PDOException $e) {
    echo "<p style='color: orange;'>Esperando o error de conexión a base de datos: " . $e->getMessage() . "</p>";
}
?>