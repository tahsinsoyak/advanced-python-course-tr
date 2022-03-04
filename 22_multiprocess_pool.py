#Multiprocess poll

#Her prosesin sonucu ve toplu prosesler


#Imports
import logging
import multiprocessing
from multiprocessing.context import Process
import time
import random


#Work Processes
def work(item,count):
    name = multiprocessing.current_process().name
    logging.info(f'{name} started: {item}')
    for x in range(count):
        logging.info(f'{name}: {item} = {x}')
        time.sleep(1)
    logging.info(f'{name} finished')
    return item + ' is finished'

#Main Process

#Callback tanımlıyoruz
#work fonksiyonundan gelen return olacak
def proc_result(result):
    logging.info(f'Result: {result}')


def main():
    logging.info('Started')

    max = 5
    pool = multiprocessing.Pool(max) #proses poolu yaratıyoruz
    results = []
    for x in range(max):
        item = 'Item' + str(x)
        count = random.randrange(1,5)
        r = pool.apply_async(work,[item,count],callback=proc_result)
        #apply senkronize hepsi tek tek
        #apply_async hepsi aynı anda
        results.append(r)

    #Result için wait
    for r in results:
        r.wait()

    #pool.close yada pool.terminate
    pool.close()
    pool.join()
    logging.info('Finished')


logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s',datefmt='%H:%M:%S',level=logging.DEBUG)
if __name__ == "__main__":
    main()

