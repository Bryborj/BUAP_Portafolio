#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONTAINER_NAME="db_mate_discretas"
MYSQL_ROOT_PASS="admin"
DATASET_DIR="$SCRIPT_DIR/dataset/sakila-db"

# Validar existencia de archivos SQL
if [[ ! -f "$DATASET_DIR/sakila-schema.sql" ]] || [[ ! -f "$DATASET_DIR/sakila-data.sql" ]]; then
    echo "Error: No se encontraron los archivos sakila-schema.sql o sakila-data.sql en $DATASET_DIR" >&2
    exit 1
fi

echo "=========================================================="
echo "      Iniciando proceso de carga de Sakila DB             "
echo "=========================================================="

# 1. Asegurar que los contenedores estén levantados
echo "==> [1/5] Verificando contenedores con docker compose..."
docker compose -f "$SCRIPT_DIR/docker-compose.yml" up -d

# 2. Esperar a que MySQL esté listo para recibir conexiones
echo "==> [2/5] Esperando a que el servicio MySQL esté disponible..."
retries=30
until docker exec "$CONTAINER_NAME" mysqladmin ping -u root -p"$MYSQL_ROOT_PASS" --silent &>/dev/null; do
    retries=$((retries - 1))
    if [[ $retries -le 0 ]]; then
        echo "Error: MySQL no estuvo listo a tiempo." >&2
        exit 1
    fi
    sleep 2
done
echo "    MySQL está activo y aceptando conexiones."

# 3. Importar esquema
echo "==> [3/5] Importando esquema (sakila-schema.sql)..."
docker exec -i "$CONTAINER_NAME" mysql -u root -p"$MYSQL_ROOT_PASS" < "$DATASET_DIR/sakila-schema.sql"
echo "    Esquema importado correctamente."

# 4. Importar datos
echo "==> [4/5] Importando datos (sakila-data.sql)..."
docker exec -i "$CONTAINER_NAME" mysql -u root -p"$MYSQL_ROOT_PASS" < "$DATASET_DIR/sakila-data.sql"
echo "    Datos importados correctamente."

# 5. Asignar privilegios a devuser y verificar
echo "==> [5/5] Concediendo privilegios a devuser y validando datos..."
docker exec -i "$CONTAINER_NAME" mysql -u root -p"$MYSQL_ROOT_PASS" -e "
GRANT ALL PRIVILEGES ON sakila.* TO 'devuser'@'%';
FLUSH PRIVILEGES;

SELECT 'Tablas en sakila' AS Entidad, COUNT(*) AS Total FROM information_schema.tables WHERE table_schema='sakila';
SELECT 'Peliculas (sakila.film)' AS Entidad, COUNT(*) AS Total FROM sakila.film;
SELECT 'Actores (sakila.actor)' AS Entidad, COUNT(*) AS Total FROM sakila.actor;
SELECT 'Clientes (sakila.customer)' AS Entidad, COUNT(*) AS Total FROM sakila.customer;
"

echo "=========================================================="
echo "  ¡Carga de Sakila DB finalizada y verificada con éxito!  "
echo "=========================================================="
