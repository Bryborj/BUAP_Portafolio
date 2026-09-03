from itertools import product

# ---------------------------------------------------------
# Función que verifica si dos proposiciones son equivalentes
# ---------------------------------------------------------
def son_equivalentes(vars_, f1, f2):

    # product genera todas las combinaciones posibles de True y False.
    # repeat=len(vars_) indica cuántas variables tenemos.
    #
    # Para p y q se generan:
    # True,  True
    # True,  False
    # False, True
    # False, False
    for valores in product([True, False], repeat=len(vars_)):

        # zip relaciona cada variable con su valor.
        # dict convierte esa relación en un diccionario.
        #
        # Ejemplo:
        # vars_ = ['p', 'q']
        # valores = (True, False)
        # resultado:
        # {'p': True, 'q': False}
        a = dict(zip(vars_, valores))

        # Evaluamos las dos proposiciones con los mismos valores.
        # Si los resultados son diferentes, las proposiciones
        # NO son equivalentes.
        if f1(a) != f2(a):
            return False

    # Si terminamos de revisar todas las combinaciones
    # y nunca encontramos una diferencia, son equivalentes.
    return True


# ---------------------------------------------------------
# Primera proposición:
#
# p OR (NOT p AND q)
#
# En Python:
# or  = OR
# and = AND
# not = NOT
# ---------------------------------------------------------
f1 = lambda a: (a['p'] or True) and (a['q'] or False)


# ---------------------------------------------------------
# Segunda proposición:
#
# p OR q
# ---------------------------------------------------------
f2 = lambda a: a['q']


# ---------------------------------------------------------
# Comprobamos si f1 y f2 son lógicamente equivalentes.
# ---------------------------------------------------------
print(son_equivalentes(['p', 'q'], f1, f2))

# Resultado:
# True
#
# Esto significa que f1 y f2 producen el mismo resultado
# para TODAS las combinaciones posibles de p y q.
#False para combinaciones incorrectas o una contingencia por lo cual
#no seria una equivalencia
