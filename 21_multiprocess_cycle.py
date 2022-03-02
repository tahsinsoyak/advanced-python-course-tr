#Multiprocess starting and stopping

#Full döngü


#Imports
import logging
import multiprocessing
from multiprocessing.context import Process #Scope
import time


#Worker process
def work(msg,max):
    name = multiprocessing.current_process().name
    logging.info(f'{name} Started')
    for x in range(max):
        logging.info(f'{name} {msg}')
        time.sleep(1)
    logging.info(f'{name} Finished')

#Main process
def main():
    logging.info('Started')
    max = 2
    worker = Process(target=work,args=['Working',max],daemon=True,name='Worker')
    worker.start()

    time.sleep(5)

    #5 saniteden sonra Proses çalışıyorsa, durdur
    if worker.is_alive:
        worker.terminate() #SIGTERM
    worker.join() #maine joinliyoruz

    #exit code
    # 0 ise iyi, değilse kötü
    logging.info(f'Finished {worker.exitcode}')


logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s',datefmt='%H:%M:%S',level=logging.DEBUG)
if __name__ == "__main__":
    main()