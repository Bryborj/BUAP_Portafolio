% Escribe un programa con lo siguiente
% ===== Reglas =====
% Tres hechos "creditos(Mteria, Creditos):" logica tiene 8 credios. cálculo 10 e inglés 4
% Una regla "pesada(M)"
% Documentar cada linea.

% Hechos: cada materia tiene un número de créditos
creditos(logica, 8).
creditos(calculo, 10).
creditos(ingles, 4).

% Una materia es pesada si tiene más de 8 créditos
pesada(M) :- creditos(M, C), C >= 8.