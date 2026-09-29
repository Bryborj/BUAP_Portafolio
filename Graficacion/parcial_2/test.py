import math
from multiprocessing import Process, Queue


def calcX(coorX, scaleX, transX, queue):
    x = (coorX * scaleX) + transX
    queue.put(("x", x))


def calcY(coorY, scaleY, transY, queue):
    y = (coorY * scaleY) + transY
    queue.put(("y", y))


def rotation(x, y, rot):
    newX = x * math.cos(rot) - y * math.sin(rot)
    newY = x * math.sin(rot) + y * math.cos(rot)

    return newX, newY


if __name__ == "__main__":

    processing = []
    queue = Queue()

    coorX, coorY = 2, 2

    Sx, Sy = 2, 3

    Tx, Ty = 0, 4

    r = 45 * math.pi / 180

    processX = Process(
        target=calcX,
        args=(coorX, Sx, Tx, queue)
    )

    processY = Process(
        target=calcY,
        args=(coorY, Sy, Ty, queue)
    )

    processX.start()
    processY.start()

    processing.append(processX)
    processing.append(processY)

    for process in processing:
        process.join()

    results = {}

    while not queue.empty():
        key, value = queue.get()
        results[key] = value

    x = results["x"]
    y = results["y"]

    print("Escala + traslación:")
    print("X:", x)
    print("Y:", y)

    x, y = rotation(x, y, r)

    print("Rotación:")
    print("X:", x)
    print("Y:", y)

    print("Finish")