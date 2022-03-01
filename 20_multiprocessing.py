#Multi Processing

#Aynı senaryoyu çalıştıran birden fazla proses
#Her prosesin kendi memorysi ve threadleri vardır


#Imports
import logging
import multiprocessing
from multiprocessing import process #sadece proeses yazmak için
import time

#Prosesin başlatma fonksiyonu
def run(num):
    name = process.current_process().name
    logging.info(f'Running {name} as {__name__}')
    time.sleep(num * 2)
    logging.info(f'Finished {name}')

#Basit proses kullanımı
def main():
    #logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s',datefmt='%H:%M:%S',level=logging.DEBUG)
    name = process.current_process().name
    logging.info(f'Running {name} as {__name__}')

    processes = []
    for x in range(5):
        p = multiprocessing.Process(target=run,args=[x],daemon=True)
        #maini öldürdükten sonra memory yemesinler diye daemon true
        processes.append(p)
        p.start()

    #prosesler için bekle
    for p in processes:
        p.join()

    logging.info(f'Finished {name}')


#bütün proseslerin login leveli olsun diye
logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s',datefmt='%H:%M:%S',level=logging.DEBUG)
if __name__ == "__main__":
    main()
