#Async Code

#Async code aynı threadte çalışıyor
#Corutine kullanarak aynı threadte çalışıyor
# "async" ve "await" kullanacağız

#Imports
import threading #threadi görüntülemek için
import multiprocessing
import logging
import asyncio #async input output
import random


#Log formatı için
logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s',datefmt='%H:%M:%S',level=logging.DEBUG)


#Fonksiyonlar
def display(msg):
    threadname = threading.current_thread().name
    processname = multiprocessing.current_process().name
    logging.info(f'{processname}\{threadname}: {msg} ')


#Async Fonksiyon
async def work(name):
    display(name + ' Starting')
    #Do Something
    #async fonksiyonun bitmesi için bekliyecek
    await asyncio.sleep(random.randint(1,10))
    display(name + ' Finished')

async def run_async(max):
    tasks = []
    for x in range(max):
        name = "Item " + str(x)
        #Wrap a coroutine or an awaitable in a future.
        #If the argument is a Future, it is returned directly.
        tasks.append(asyncio.ensure_future(work(name)))

    await asyncio.gather(*tasks) #görevleri toplama
    #future'un bitip bitmediğine bakıyor

def main():
    display('Main Started')

    #eventloop alıyoruz [arkaplanda sürekli çalışan]
    loop = asyncio.get_event_loop() 

    #Async taskler bitene kadar loop
    loop.run_until_complete(run_async(50))

    #app sonsuza kadar çalışır [zorla durdurana kadar]
    #loop.run_forever()

    #Dögüyü durduruyoruz,kaynakları bırakıyoruz
    loop.close()


    display('Main Finished')

if __name__ == "__main__":
    main()
