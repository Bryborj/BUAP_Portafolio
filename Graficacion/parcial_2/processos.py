from multiprocessing import Process
import time

def task(procces):
    print(f"Proceso: {procces}")
    # time.sleep(10)

if __name__ == "__main__":
    processing = []
    for i in range(0, 7):
        process = Process(target=task, args=(i,))
        process.start()
        processing.append(process)
        
    for element in processing:
        element.join()
        
    print("Finishing")