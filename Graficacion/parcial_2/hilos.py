import random
import threading


def tarea(number):
    print(f"Hilo {number}: {i}")
    global result
    result = result + random.randint(0, 10)
    array.append(random.randint(0, 10))

if __name__ == "__main__":
    treads = []
    array = []
    result = 0
    
    for i in range(8):
        t = threading.Thread(
            target=tarea,
            args=(i,)
        )
        treads.append(t)
        t.start()
    
    for t in treads:
        t.join()
    print(array)
    print("Hilos terminados")