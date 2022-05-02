#Communicating with process

#Gerçek zamanlı  process iletişimi
#Başka bilgisayarla bile olur
#Soketler aracaılığıyla networking yapıyoruz [Internet]
#Client bağlanıyor servere
#Server dinliyor


#Imports
import imp
import logging
import time
import multiprocessing
from multiprocessing import process
from multiprocessing.context import Process
from multiprocessing.connection import Listener, Client


logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s',datefmt='%H:%M:%S',level=logging.DEBUG)


#Worker Process
def proc(server='localhost',port=6000, password=b'password'):
    name = process.current_process().name
    logging.info(f'{name} started ')

    #Dinlemeye Başlıyoruz [bağlantı için]
    address = (server,port)
    listener = Listener(address,authkey=password)
    conn = listener.accept()
    logging.info(f'{name}: connection from {listener.last_accepted} ')

    #Girdi için döngü [bağlanılan processten]
    while True:
        msg = conn.recv()
        logging.info(f'{name} data in: {msg}')
        if msg == 'quit':
            conn.close() #bağlantıyı kapatıyoruz
            break
    Listener.close() #serveri kapatıyoruz

    logging.info(f'{name} finished ')


#Main Fonksiyonu
def main():
    name = process.current_process().name
    logging.info(f'{name} started')

    #Process'i Kuruyoruz
    address = 'localhost' #127.0.0.1 #local loopback
    port = 2823  #1024 üzerinde olmalı
    password = b'password'
    p = Process(target=proc,args=[address,port,password],daemon=True,name="Worker")
    #Daemon herşey kapandığında kapansın diye
    p.start()
    logging.info(f' {name} waiting on the working... ')
    time.sleep(1) #işimiz uzun olduğu için bağlantıda bekletiyoruz biraz

    #Process'e Bağlanıyoruz
    dest = (address,port)
    conn = Client(dest,authkey=password) #şifre process ile aynı olmalı

    #Komut Loop'u [kullanıcının göndermesi için]
    while True:
        command = input('\r\n\Enter a command or type quit:\r\n').strip()
        logging.info(f' {name} command: {command} ')
        conn.send(command)
        if command == 'quit':
            break
    
    #Temizlik ve Kapatma
    if p.is_alive:
        logging.info(f' {name} terminating worker ')
        conn.close()
        time.sleep(1)
        p.terminate() #kapanmassa diye bağlantı processi kapatıyoruz
    p.join() #maine tekrar katılsın process

    logging.info(f'{name} finished ')

if __name__ == "__main__":
    main()