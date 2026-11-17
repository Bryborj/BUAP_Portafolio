% Hecho: a ana le gusta la pizza
le_gusta(ana, pizza).
% Hecho: a luis le gustan los tacos
le_gusta(luis, tacos).
% Hecho: a ana le gustan los tacos
le_gusta(ana, tacos).
% Hecho: X y Y comparten la comida C
% si a los dis les gusta C y son distintos.
comparten(X, Y, C) :- le_gusta(X, C), le_gusta(Y, C), X \= Y.