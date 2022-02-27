#Thread Pools

#Var olan threadleri kullanma [sıfırdan thread maliyetli]

#Imports
import logging
import threading
from concurrent.futures import ThreadPoolExecutor #eşzamanlılıktan
import time
import random


#Test fonksiyonu
def test(item):
    s = random.randrange(1,10)
    logging.info(f'Thread {item}: id = {threading.get_ident()}')
    logging.info(f'Thread {item}: name = {threading.current_thread().name}')
    logging.info(f'Thread {item}: sleeping for = {s}')
    time.sleep(s)
    logging.info(f'Thread {item}: finished')


#Main fonksiyonu [havuzda çalıştırmak için]
def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s',datefmt='%H:%M:%S',level=logging.DEBUG)
    logging.info('APP Started')
    
    workers = 5
    items = 15 #işçiden çok eşyamız var
    # bu yüzden eşzamanlı ve tekrardan kullanılabilir olmalı

    with ThreadPoolExecutor(max_workers=workers) as executor:
    #kaç tane en fazla kullanacağını belirttik
        executor.map(test,range(items))


    logging.info('APP Finished')



if __name__ == "__main__":
    main()