<?php
$host = 'db';
$db   = 'sakila';
$user = 'devuser';
$pass = 'root';
$charset = 'utf8mb4';

$_CONECTION_STRING = "mysql:host=$host;dbname=$db;charset=$charset";
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false,
];
function conect(){
    global $_CONECTION_STRING, $user, $pass, $options;
    return new PDO($_CONECTION_STRING, $user, $pass, $options);
}
?>