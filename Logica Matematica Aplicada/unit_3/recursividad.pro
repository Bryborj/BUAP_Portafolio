% Caso base: al llegar a 0 se imprime "despegue"
cuenta(0) :- write(despegue), nl.
% Caso recursivo: si N > 0, imprime N
% y vuelve a contar desde N - 1.

cuenta(N) :-
    N > 0,          % Solo para N positivo
    write(N), nl,   % Imprime N y salta la línea
    N1 is N - 1,    % Calcula el siguiente
    cuenta(N1).     % Se llama a si misma