import threading
from multiprocessing import Process, Queue


def mult(array_aux, x, y):
    result = x * y
    array_aux.append(result)

def mult_row_col(q, row, B):
    row_aux = []
    for i in range(0, 3):
        treads = []
        array_aux = []

        for j in range(0, 3):
            element = row[j]
            tread = threading.Thread(target=mult, args=(array_aux, element, B[j][i]))
            tread.start()
            treads.append(tread)

        for element in treads:
            element.join()
        row_aux.append(sum(array_aux))
    q.put(row_aux)


if __name__ == "__main__":
    C = []
    q = Queue()
    processInit = []
    A = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    B = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    for row in A:
        processingInit = Process(target=mult_row_col, args=(q, row, B))
        processingInit.start()
        processInit.append(processingInit)
        C.append(q.get())
        
    for element in processInit:
        element.join()
    
    print(C)
    print("Finished")
