<?php
$_CONECTION_STRING = "mysql:host=db;dbname=practice_db;charset=utf8mb4";
$USER = "devuser";
$PASS = "root";
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false,
];

function conect(){
    global $_CONECTION_STRING, $USER, $PASS, $options;
    try {
        $pdo = new PDO($_CONECTION_STRING, $USER, $PASS, $options);
        $pdo->setAttribute(PDO::MYSQL_ATTR_USE_BUFFERED_QUERY, false);
        return $pdo;
    }
    catch (PDOException $e) {
        echo "<p style='color: orange;'>Esperando o error de conexión a base de datos: " . $e->getMessage() . "</p>";
        return null;
    }
}

function close($pdo){
    $pdo = null;
}
?>