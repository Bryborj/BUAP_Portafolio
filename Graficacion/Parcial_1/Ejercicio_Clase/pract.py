import numpy as np
import matplotlib.pyplot as plt

pasto = np.zeros((8,8,3), dtype = np.uint8)
# ( fila , columna, intensidad RGB )
#verde claro
pasto [:,:,:] = [134,239,172]
# Algunos píxeles verdes oscuros
pasto[0,1] = [22,101,52]
pasto[1,5] = [22,101,52]
pasto[2,3] = [22,101,52]
pasto[4,0] = [22,101,52]
pasto[5,4] = [22,101,52]
pasto[7,2] = [22,101,52]

tierra = np.zeros((8,8,3), dtype= np.uint8)
#color tierra
tierra[:,:,:] = [115, 60, 26]
# algunos pixeles mas oscuros
tierra[0,1] = [73, 18, 3]
tierra[1,5] = [73, 18, 3]
tierra[2,3] = [73, 18, 3]
tierra[4,0] = [73, 18, 3]
tierra[5,4] = [73, 18, 3]
tierra[7,2] = [73, 18, 3]

#Agua
agua = np.zeros((8,8,3), dtype=np.uint8)
agua[:,:,:] = [1, 123, 255]
agua[0,1] = [71, 44, 255]
agua[1,5] = [71, 44, 255]
agua[2,3] = [71, 44, 255]
agua[4,0] = [71, 44, 255]
agua[5,4] = [71, 44, 255]
agua[7,2] = [71, 44, 255]

#plt.imshow(pasto, interpolation='nearest')
#plt.imshow(tierra, interpolation='nearest')
#plt.imshow(agua, interpolation='nearest')
#plt.grid()
#plt.show()

fig, ax = plt.subplots(1,4)

ax[0].imshow(pasto, interpolation='nearest')
ax[1].imshow(tierra, interpolation='nearest')
ax[2].imshow(agua, interpolation='nearest')
plt.show()