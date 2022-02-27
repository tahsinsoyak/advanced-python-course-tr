#Thread Locking

#Race condition ve Deadlocklardan kaçmak için
#Race condition: Birden fazla threadin aynı kaynağa erişmesi
#Deadlock: Birden fazla threadin aynı kaynağa yazması

#Imports and globals
import logging
import threading
from concurrent.futures import ThreadPoolExecutor #eşzamanlılıktan
import time
import random

counter = 0
#Race condition yaratacagız
#sayıyı artttırmaya çalışacağız

#Test fonksiyonu
def test(count):
    global counter
    threadname = threading.current_thread().name
    logging.info(f'Startting: {threadname}')

    for x in range (count):
        logging.info(f'Count: {threadname} += {count}')

        #GIL Global Interpreter Lock
        #counter += 1
    
    # #LOCKING
    # lock = threading.Lock() #başka thread girmemesi için kilitliyoruz
    # lock.acquire() #kilitleme
    # #lock.acquire() # Deadlock!! [2. kez yazma]
    # try:
    #     counter += 1
    # finally:
    #     lock.release() #açma

    #Basitleştirilmiş Locking 
    lock = threading.Lock()
    with lock:
        logging.info(f'Locked: {threadname}')
        counter += 1
        time.sleep(2)

    logging.info(f'Completed: {threadname}')
    
#Main fonksiyonu
def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s',datefmt='%H:%M:%S',level=logging.DEBUG)
    logging.info('App Started')

    workers = 2
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for x in range(workers*2):
            v = random.randrange(1,5)
            ex.submit(test,v) #direk fonksiyonu çağırıyoruz

    #değerine bakalım counterin
    print(f'Counter: {counter}')
    logging.info('App Finished')

if __name__ == "__main__":
    main()