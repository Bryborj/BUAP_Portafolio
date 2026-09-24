import matplotlib.pyplot as plt
import numpy as np
import math

def rotacion(x,y,theta):
    resx = []
    resy = []
    rad = theta * math.pi/180
    
    for i in range(0,len(x)):
        xa = x[i]
        ya = y[i]
        x1 = xa*np.cos(rad) - ya*np.sin(rad)
        y1 = xa*np.sin(rad) + ya*np.cos(rad)
        
        resx.append(x1)
        resy.append(y1)
    return resx, resy


def escala(x,y,escalaMul):
    resx = []
    resy = []
    
    for i in range(0,len(x)):
        xi = x[i] * escalaMul
        yi = y[i] * escalaMul
        resx.append(xi)
        resy.append(yi)
    return resx, resy

def escalaNoUniforme(x,y,s1,s2):
    resx = []
    resy = []
    
    for i in range(0,len(x)):
        xi = x[i] * s1
        yi = y[i] * s2
        resx.append(xi)
        resy.append(yi)
    return resx, resy

def reflexion(x,y,isX = False):
    resx = []
    resy = []
    
    for i in range(0,len(x)):
        if isX: 
            yi = y[i] * -1
            xi = x[i]
        else:
            xi = x[i] * -1
            yi = y[i]
        resx.append(xi)
        resy.append(yi)
    return resx, resy

def corte(x,y,kx,isH = False):
    resx = []
    resy = []
    
    for i in range(0,len(x)):
        if isH: 
            yi = y[i]
            xi = x[i] + kx*y[i]
        else:
            xi = x[i]
            yi = y[i] + kx*x[i]
        resx.append(xi)
        resy.append(yi)
    return resx, resy

x = [1,4,4,1,1]
y = [1,1,4,4,1]
theta = 90
escalav = 2
s1 = 2
s2 = 3
kx = 1

x2, y2 = rotacion(x,y,theta)
x3, y3 = escala(x, y, escalav)
x4, y4 = escalaNoUniforme(x, y, s1, s2)
x5, y5 = reflexion(x, y, 0)
x6, y6 = corte(x, y, kx, 1)

plt.plot(x, y, marker='o')
#plt.plot(x2, y2, marker='o')
#plt.plot(x3, y3, marker='o')
#plt.plot(x4, y4, marker='o')
#plt.plot(x5, y5, marker='o')
plt.plot(x6, y6, marker='o')
plt.xlim(0, 5)
plt.ylim(0, 5)
plt.grid(True)

plt.axis('equal')
plt.show()