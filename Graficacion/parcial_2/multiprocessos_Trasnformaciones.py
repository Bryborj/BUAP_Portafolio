import math
from multiprocessing import Process
import time

x = 0
y = 0

def calcX(coorX, scaleX, transX, rot):
    global x
    x = (coorX * scaleX) + transX
    return x

def calcY(coorY, scaleY, transY, rot):
    global y 
    y = (coorY * scaleY) + transY
    return y

def rotation(rot):
    global x
    global y
    x = coorX * math.cos(rot) - coorY * math.sin(rot)
    y = coorY * math.sin(rot) + coorY * math.cos(rot)
    return x, y

if __name__ == "__main__":
    processing = []
    coorX, coorY = 2, 2
    Sx, Sy = 2, 3
    Tx, Ty = 0, 4
    r = 45 * math.pi/180
    
    processX = Process(target=calcX, args=(coorX, Sx, Tx, r))
    processY = Process(target=calcY, args=(coorY, Sy, Ty, r))
    
    processX.start()
    processY.start()
    
    processing.append(processX)
    processing.append(processY)
    
    for starting in processing: 
        starting.join()
    
    processRot = Process(target=rotation, args=(r,))
    processRot.start()
    processRot.join()
        
    print("Finish")