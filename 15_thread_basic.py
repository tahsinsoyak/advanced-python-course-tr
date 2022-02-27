#Thread Basics

#Fonksiyonu çoklu threadlere devretme
#Bütün threadlerin bitmesini bekleme
#Bütün threadler ayrı ayrı çalışıyor

#Imports

import logging #kayıt için
from threading import Thread
import time #çalışan threadi bekletmek için [sleep için]
import random #random sayılar için


#İş yapması için fonksiyon
def longtask(name):
    max = random.randrange(1,10)
    logging.info(f'Task: {name} performing {str(max)} times')
    for x in  range(max):
        logging.info(f'Task {name}: {x}')
        time.sleep(random.randrange(1,3)) #çalışan threadi durduyor [mainde çalışırsa kilitler]
    logging.info(f'Task: {name}: complete') #hangi threadin gittiğini görmek için


#Main fonksiyonu
def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s',datefmt='%H:%M:%S',level=logging.DEBUG)
    logging.info('Starting')
    #longtask('main') #tek thread ile yapar çok uzun sürer


    #Çoklu thread için
    threads = []
    for x in range(1,10):
        t = Thread(target=longtask, args=['thread' + str(x)])
        threads.append(t)
        t.start()

    #bütün threadlerin bitmesini beklemek için
    for t in threads:
        t.join()

    logging.info('Finished all threads')






if __name__ == "__main__":
    main()