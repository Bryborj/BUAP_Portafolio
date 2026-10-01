from multiprocessing import Process, Queue

def mult(x, y):
    q.put(x * y)


if __name__ == "__main__":
    A = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    B = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    process = []
    C = []
    q = Queue()
    
    for row in A:
        for i in range(0, 3):
            rowAux = []
            aux = 0
            
            for j in range(0, 3):
                element = row[j]
                proce = Process(target=mult, args=(element, B[j][i], q))
                proce.start()
                result = q.get()
                aux = aux + result
                process.append(proce)
            
            rowAux.append(aux)
            
        C.append(rowAux)
