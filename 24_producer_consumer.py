#Basit Üretici ve Tüketici

#Queue ve kilitlerle event


#Imports
import random
import threading
import multiprocessing
import logging
from threading import Thread
from queue import Queue
import time
from tkinter.tix import Tree
logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s',datefmt='%H:%M:%S',level=logging.DEBUG)


#Fonksiyonlar
def display(msg):
    threadname = threading.current_thread().name
    processname = multiprocessing.current_process().name
    logging.info(f'{processname}\{threadname}: {msg} ')


#Producer
def create_work(queue,finished,max):
    finished.put(False)
    for x in range(max):
        v = random.randrange(1,100)
        queue.put(v)
        display(f'Producing {x}: {v}')
    finished.put(True)
    display('finished producing')

#Consumer
def perform_work(work,finished):
    counter = 0
    while True:
        if not work.empty():
            v = work.get()
            display(f'Consuming {counter}: {v}')
            counter +=1
        else:
            q = finished.get()
            if q == True:
                break
        display('Finished Consuming')


#Main Fonksiyonu
def main():
    max = 50
    work = Queue()
    finished = Queue()

    producer = Thread(target=create_work,args=[work,finished,max],daemon=True)
    consumer = Thread(target=perform_work,args=[work,finished],daemon=True)

    #birbirlerinden habersiz 2 thread
    producer.start()
    consumer.start()

    producer.join()
    display('Producer has Finished')

    consumer.join()
    display('Consumer has Finished')

    display('Finished')



if __name__ == "__main__":
    main()