<?php
require "../config/conection.php";

$limit = isset($_GET['limit']) ? intval($_GET['limit']) : 20;
if ($limit < 1) $limit = 1;
if ($limit > 1000) $limit = 1000;

// Filtros
$filter_year         = isset($_GET['year']) ? trim($_GET['year']) : '';
$filter_duration     = isset($_GET['duration']) ? trim($_GET['duration']) : '';
$filter_title_search = isset($_GET['title_search']) ? trim($_GET['title_search']) : '';
$filter_rating       = isset($_GET['rating']) ? trim($_GET['rating']) : '';
$filter_category_id  = isset($_GET['category_id']) ? trim($_GET['category_id']) : '';
$filter_actor_id     = isset($_GET['actor_id']) ? trim($_GET['actor_id']) : '';

try {
    $pdo = conect();
    $connected = true;

    // Obtener catálogo de categorías para el selector
    $categories = $pdo->query("SELECT category_id, name FROM category ORDER BY name")->fetchAll();

    // Obtener catálogo de actores para el selector
    $actors = $pdo->query("SELECT actor_id, first_name, last_name FROM actor ORDER BY first_name, last_name")->fetchAll();

    // Obtener años distintos existentes
    $years = $pdo->query("SELECT DISTINCT release_year FROM film ORDER BY release_year DESC")->fetchAll(PDO::FETCH_COLUMN);

    // Obtener clasificaciones existentes
    $ratings = ['G', 'PG', 'PG-13', 'R', 'NC-17'];

    // Construcción de condiciones WHERE parametrizadas
    $where_clauses = [];
    $params = [];

    // 1. Año (release_year)
    if ($filter_year !== '') {
        $where_clauses[] = "fl.release_year = :year";
        $params[':year'] = intval($filter_year);
    }

    // 2. Duración (length)
    if ($filter_duration !== '') {
        if ($filter_duration === 'short') {
            $where_clauses[] = "fl.length < 60";
        } elseif ($filter_duration === 'medium') {
            $where_clauses[] = "fl.length BETWEEN 60 AND 120";
        } elseif ($filter_duration === 'long') {
            $where_clauses[] = "fl.length > 120";
        } elseif (is_numeric($filter_duration)) {
            $where_clauses[] = "fl.length <= :duration";
            $params[':duration'] = intval($filter_duration);
        }
    }

    // 3. Contiene "x" letra/texto en título
    if ($filter_title_search !== '') {
        $where_clauses[] = "fl.title LIKE :title_search";
        $params[':title_search'] = '%' . $filter_title_search . '%';
    }

    // 4. Clasificación / Rating
    if ($filter_rating !== '') {
        $where_clauses[] = "fl.rating = :rating";
        $params[':rating'] = $filter_rating;
    }

    // 5. Categoría (juntura / subconsulta)
    if ($filter_category_id !== '') {
        $where_clauses[] = "fl.film_id IN (SELECT film_id FROM film_category WHERE category_id = :category_id)";
        $params[':category_id'] = intval($filter_category_id);
    }

    // 6. Actor (juntura / subconsulta)
    if ($filter_actor_id !== '') {
        $where_clauses[] = "fl.film_id IN (SELECT film_id FROM film_actor WHERE actor_id = :actor_id)";
        $params[':actor_id'] = intval($filter_actor_id);
    }

    // Query principal
    $sql = "SELECT 
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
    LEFT JOIN actor AS a ON fa.actor_id = a.actor_id";

    if (!empty($where_clauses)) {
        $sql .= " WHERE " . implode(" AND ", $where_clauses);
    }

    $sql .= " GROUP BY fl.film_id ORDER BY fl.title LIMIT :limit";

    $stmt = $pdo->prepare($sql);
    foreach ($params as $key => $val) {
        $stmt->bindValue($key, $val);
    }
    $stmt->bindValue(':limit', $limit, PDO::PARAM_INT);
    $stmt->execute();
    $films = $stmt->fetchAll();

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
    <title>CONDICIONES Y FILTROS | Mates Discretas</title>
    <style>
        body { font-family: system-ui, -apple-system, sans-serif; background: #f4f6f8; color: #333; margin: 30px 20px; }
        .card { background: white; padding: 28px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.08); max-width: 1250px; margin: 0 auto; }
        .badge-success { background: #e6f4ea; color: #137333; padding: 6px 12px; border-radius: 4px; font-weight: bold; display: inline-block; }
        .badge-danger { background: #fce8e6; color: #c5221f; padding: 6px 12px; border-radius: 4px; font-weight: bold; display: inline-block; }
        
        .header-nav { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 15px; margin-bottom: 24px; padding-bottom: 16px; border-bottom: 1px solid #e2e8f0; }
        .nav-links { display: flex; gap: 10px; flex-wrap: wrap; }
        .btn-nav { background: #1a73e8; color: white; padding: 8px 16px; border-radius: 6px; text-decoration: none; font-weight: 500; font-size: 14px; }
        .btn-nav:hover { background: #1557b0; }
        .btn-nav-purple { background: #7c3aed; }
        .btn-nav-purple:hover { background: #6d28d9; }
        .btn-nav-gray { background: #475569; }
        .btn-nav-gray:hover { background: #334155; }

        .filter-panel { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin-bottom: 24px; }
        .filter-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; margin-bottom: 16px; }
        .form-group { display: flex; flex-direction: column; gap: 6px; }
        .form-group label { font-size: 13px; font-weight: 600; color: #1e293b; }
        .form-group input, .form-group select { padding: 8px 10px; border: 1px solid #cbd5e1; border-radius: 6px; font-size: 14px; background: white; }
        
        .filter-actions { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; border-top: 1px solid #e2e8f0; padding-top: 16px; }
        .action-buttons { display: flex; gap: 10px; align-items: center; }
        .btn-submit { background: #0f9d58; color: white; border: none; padding: 9px 20px; border-radius: 6px; font-weight: 600; font-size: 14px; cursor: pointer; }
        .btn-submit:hover { background: #0b8043; }
        .btn-reset { background: #e2e8f0; color: #475569; border: none; padding: 9px 18px; border-radius: 6px; font-weight: 600; font-size: 14px; text-decoration: none; cursor: pointer; display: inline-block; }
        .btn-reset:hover { background: #cbd5e1; color: #1e293b; }

        .active-condition-tag { display: inline-block; background: #e0f2fe; color: #0369a1; padding: 4px 10px; border-radius: 14px; font-size: 12px; font-weight: 600; margin-right: 6px; margin-bottom: 6px; }
        
        .table-container { width: 100%; overflow-x: auto; margin-top: 15px; border: 1px solid #e2e8f0; border-radius: 8px; }
        table { width: 100%; border-collapse: collapse; min-width: 950px; }
        th, td { border-bottom: 1px solid #e2e8f0; padding: 12px 14px; text-align: left; vertical-align: top; font-size: 13px; }
        th { background: #f1f5f9; color: #1e293b; font-weight: 600; position: sticky; top: 0; }
        tr:hover { background: #f8fafc; }
        .actors-cell { max-width: 280px; color: #1e293b; line-height: 1.4; }
        .desc-cell { max-width: 240px; color: #64748b; font-size: 12px; line-height: 1.4; }
        .cat-tag { background: #e0f2fe; color: #0369a1; padding: 3px 8px; border-radius: 4px; font-size: 12px; font-weight: 600; display: inline-block; }
    </style>
</head>
<body>
    <div class="card">
        <div class="header-nav">
            <div>
                <h1 style="margin: 0; font-size: 24px;">Condiciones y Filtros (Selección Relacional)</h1>
                <p style="margin: 4px 0 0 0; color: #64748b; font-size: 14px;">
                    En Álgebra Relacional, la operación de selección $\sigma_{condición}(R)$ filtra las filas que satisfacen uno o varios predicados.
                </p>
            </div>
            <div class="nav-links">
                <a href="join.php" class="btn-nav">Ir a Junturas</a>
                <a href="proyections.php" class="btn-nav btn-nav-purple">Ir a Proyecciones</a>
                <a href="tablas_origen.php" class="btn-nav btn-nav-gray">Ver Tablas de Origen</a>
            </div>
        </div>

        <?php if ($connected): ?>
            <p>
                <span class="badge-success">Conexión con la base de datos realizada con éxito</span>
            </p>

            <!-- PANEL DE FILTROS (LAS 6 CONDICIONES) -->
            <form method="GET" class="filter-panel">
                <div class="filter-grid">
                    
                    <!-- Condición 1: Año -->
                    <div class="form-group">
                        <label for="year">1. Año (release_year)</label>
                        <select id="year" name="year">
                            <option value="">Todos los años</option>
                            <?php foreach ($years as $yr): ?>
                                <option value="<?= htmlspecialchars($yr); ?>" <?= $filter_year == $yr ? 'selected' : ''; ?>>
                                    <?= htmlspecialchars($yr); ?>
                                </option>
                            <?php endforeach; ?>
                        </select>
                    </div>

                    <!-- Condición 2: Duración -->
                    <div class="form-group">
                        <label for="duration">2. Duración (length)</label>
                        <select id="duration" name="duration">
                            <option value="">Cualquier duración</option>
                            <option value="short" <?= $filter_duration === 'short' ? 'selected' : ''; ?>>Corta (Menos de 60 min)</option>
                            <option value="medium" <?= $filter_duration === 'medium' ? 'selected' : ''; ?>>Media (60 a 120 min)</option>
                            <option value="long" <?= $filter_duration === 'long' ? 'selected' : ''; ?>>Larga (Más de 120 min)</option>
                            <option value="90" <?= $filter_duration === '90' ? 'selected' : ''; ?>>Hasta 90 minutos</option>
                        </select>
                    </div>

                    <!-- Condición 3: Título contiene letra o palabra -->
                    <div class="form-group">
                        <label for="title_search">3. Título contiene letra/palabra</label>
                        <input type="text" id="title_search" name="title_search" placeholder="Ej: A, LOVE, WAR..." value="<?= htmlspecialchars($filter_title_search); ?>">
                    </div>

                    <!-- Condición 4: Clasificación / Público dirigido -->
                    <div class="form-group">
                        <label for="rating">4. Clasificación (rating)</label>
                        <select id="rating" name="rating">
                            <option value="">Todas las clasificaciones</option>
                            <?php foreach ($ratings as $rt): ?>
                                <option value="<?= htmlspecialchars($rt); ?>" <?= $filter_rating === $rt ? 'selected' : ''; ?>>
                                    <?= htmlspecialchars($rt); ?>
                                </option>
                            <?php endforeach; ?>
                        </select>
                    </div>

                    <!-- Condición 5: Categoría (juntura) -->
                    <div class="form-group">
                        <label for="category_id">5. Categoría (category)</label>
                        <select id="category_id" name="category_id">
                            <option value="">Todas las categorías</option>
                            <?php foreach ($categories as $cat): ?>
                                <option value="<?= htmlspecialchars($cat['category_id']); ?>" <?= $filter_category_id == $cat['category_id'] ? 'selected' : ''; ?>>
                                    <?= htmlspecialchars($cat['name']); ?>
                                </option>
                            <?php endforeach; ?>
                        </select>
                    </div>

                    <!-- Condición 6: Actor (juntura) -->
                    <div class="form-group">
                        <label for="actor_id">6. Actor (actor)</label>
                        <select id="actor_id" name="actor_id">
                            <option value="">Todos los actores</option>
                            <?php foreach ($actors as $act): ?>
                                <option value="<?= htmlspecialchars($act['actor_id']); ?>" <?= $filter_actor_id == $act['actor_id'] ? 'selected' : ''; ?>>
                                    <?= htmlspecialchars($act['first_name'] . ' ' . $act['last_name']); ?>
                                </option>
                            <?php endforeach; ?>
                        </select>
                    </div>

                </div>

                <div class="filter-actions">
                    <div style="display: flex; align-items: center; gap: 10px;">
                        <label for="limit" style="font-size: 13px; font-weight: 600;">Límite de filas:</label>
                        <input type="number" id="limit" name="limit" min="1" max="1000" value="<?= htmlspecialchars($limit); ?>" style="width: 80px; padding: 6px; border: 1px solid #cbd5e1; border-radius: 4px;">
                    </div>

                    <div class="action-buttons">
                        <button type="submit" class="btn-submit">Aplicar filtros</button>
                        <a href="conditions.php" class="btn-reset">Limpiar filtros</a>
                    </div>
                </div>
            </form>

            <!-- RESUMEN DE FILTROS ACTIVOS -->
            <div style="margin: 15px 0;">
                <span style="font-size: 14px; color: #475569;">Filtros activos:</span>
                <?php
                $any_filter = false;
                if ($filter_year !== '') {
                    echo '<span class="active-condition-tag">Año: ' . htmlspecialchars($filter_year) . '</span>';
                    $any_filter = true;
                }
                if ($filter_duration !== '') {
                    echo '<span class="active-condition-tag">Duración: ' . htmlspecialchars($filter_duration) . '</span>';
                    $any_filter = true;
                }
                if ($filter_title_search !== '') {
                    echo '<span class="active-condition-tag">Título contiene: "' . htmlspecialchars($filter_title_search) . '"</span>';
                    $any_filter = true;
                }
                if ($filter_rating !== '') {
                    echo '<span class="active-condition-tag">Clasificación: ' . htmlspecialchars($filter_rating) . '</span>';
                    $any_filter = true;
                }
                if ($filter_category_id !== '') {
                    $cat_name = '';
                    foreach ($categories as $c) {
                        if ($c['category_id'] == $filter_category_id) { $cat_name = $c['name']; break; }
                    }
                    echo '<span class="active-condition-tag">Categoría: ' . htmlspecialchars($cat_name) . '</span>';
                    $any_filter = true;
                }
                if ($filter_actor_id !== '') {
                    $act_name = '';
                    foreach ($actors as $a) {
                        if ($a['actor_id'] == $filter_actor_id) { $act_name = $a['first_name'] . ' ' . $a['last_name']; break; }
                    }
                    echo '<span class="active-condition-tag">Actor: ' . htmlspecialchars($act_name) . '</span>';
                    $any_filter = true;
                }
                if (!$any_filter) {
                    echo '<span style="font-size: 13px; color: #94a3b8; font-style: italic;">Ninguno (mostrando todas las películas)</span>';
                }
                ?>
            </div>

            <p style="font-size: 14px; color: #64748b; margin-top: 8px;">
                Filas encontradas: <strong><?= count($films); ?></strong> película(s).
            </p>

            <!-- TABLA DE RESULTADOS -->
            <div class="table-container">
                <table>
                    <thead>
                        <tr>
                            <th style="width: 50px;">ID</th>
                            <th>Título</th>
                            <th style="width: 60px;">Año</th>
                            <th>Categoría(s)</th>
                            <th style="width: 300px;">Actor(es)</th>
                            <th style="width: 80px;">Duración</th>
                            <th style="width: 90px;">Clasificación</th>
                            <th>Descripción</th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php if (empty($films)): ?>
                            <tr>
                                <td colspan="8" style="text-align: center; color: #94a3b8; padding: 25px;">
                                    No se encontraron películas con las condiciones seleccionadas.
                                </td>
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
