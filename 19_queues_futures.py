#Queues and Futures

#Thread'den geri dönüş değeri alma

"""
Que mesaj bırakıyor.
Future program çıktısını senkronize etmek için eşzamanlı
programlama dillerinde kullanılıyor.
"""


#Imports
from cgi import test
import logging
import threading
from threading import Thread, Timer
import time
import random
from concurrent.futures import ThreadPoolExecutor
from queue import Queue


#Queues
#öne ve arkaya mesajlar verebilmek için
#mesajı verip alıyoruz [put,get]

#threadin çalıştırdığı fonksiyon
def test_que(name, que):
    threadname = threading.current_thread().name
    logging.info(f'Starting: {threadname}')
    time.sleep(random.randrange(1,5))
    logging.info(f'Finished: {threadname}')
    ret = 'Hello ' + name + ' your random number is: ' + str(random.randrange(1,10))
    que.put(ret) #çoklu threadde sorun olmasın diye kilitlemeliyiz

#thread yaratacak
def queued():
    que = Queue()
    t = Thread(target=test_que,args=['Tahsin',que])
    t.start()
    logging.info('Do something on the main thread')
    t.join()
    ret = que.get()
    logging.info(f'Returned: {ret}')


#Futures
#Kolay ve temiz kullanımı var
#verileri threadlerden toplayıp sonra bakabiliyoruz
def test_future(name):
    threadname = threading.current_thread().name
    logging.info(f'Starting: {threadname}')
    time.sleep(random.randrange(1,5))
    logging.info(f'Finished: {threadname}')
    ret = 'Hello ' + name + ' your random number is: ' + str(random.randrange(1,10))
    return ret

#que yerine 20 tane aynı ayna
def pooled():
    workers = 20
    ret = []
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for x in range(workers):
            v = random.randrange(1,5)
            future = ex.submit(test_future,'Tahsin' + str(x))
            ret.append(future)
    logging.info('Do something on the main thread')
    for r in ret:
        logging.info(f'Returned: {r.result()}')

#Main Fonksiyonu
def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s',datefmt='%H:%M:%S',level=logging.DEBUG)
    logging.info('App Start')
    #queued()
    pooled()



if __name__ == "__main__":
    main()