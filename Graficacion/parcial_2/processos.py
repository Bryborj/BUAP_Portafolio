from multiprocessing import Process
import time

def searchWorlds(name):
    if "an" in name:
        print(f"\"an\" esta en: {name}")

if __name__ == "__main__":
    processing = []
    names = ["Juan", "Miguel", "Alex", "Vicente"]
    for name in names:
        process = Process(target=searchWorlds, args=(name,))
        process.start()
        processing.append(process)
        
    for element in processing:
        element.join()
        
    print("Finish")