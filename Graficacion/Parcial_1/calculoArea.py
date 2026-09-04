coors = [
    (2,1),
    (3,1),
    (4,2),
    (4,3),
    (3,4),
    (2,4),
    (1,3),
    (1,2),
    (2,1),
]

eje_x = []
eje_y = []
suma = 0

for i in coors:
    eje_x.append(i[0])
    eje_y.append(i[1])

for i in range(len(eje_x) - 1):
    suma += (eje_x[i] * eje_y[i + 1]) - (eje_y[i] * eje_x[i + 1])

area = suma / 2
print(area)
