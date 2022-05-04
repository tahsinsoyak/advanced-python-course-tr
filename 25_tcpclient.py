#TCP Client

"""
TCP (Transmission Control Protocol) - is a standart that defines establish
and maintain a network conversation through which application programs can
exchange data. TCP works with the IP (Internet Protocol), which defines how
computer send packets of data to each other. 

Uses a 3 way hand shake
c > syn
s < syn/ack
c > ack

Server -  listens for incomming connections via TCP
Client - connects to the server via TCP
Network - A network consists of two or more computer that are linked
IP - the number of that reperesents the machine on the networks (IP4 vs IP6)
Port - A comminication end point
Protocol - Defined means of application communications
"""

#Includes
import logging
import socket

logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s',datefmt='%H:%M:%S',level=logging.DEBUG)


#TCP Client
def download(server,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #tcp soketi tasarla ipv4 (INET) kullanan. 
    #açık durması,akması,sürmesi için stream. tcp
    adress = (server,port)
    logging.info(f'Connectiong to : {server}:{port}')

    s.connect(adress)
    logging.info('Connected')

    logging.info('Send')
    s.send(b'Hello \r\n')
    #bilgi gönderiyoruz, birsürü boş veride server çoker

    logging.info('Recv')
    data = s.recv(1024) #veri aliyoruz - 1024 buffer size

    logging.info('Closing')
    s.close()

    logging.info(f'Data: {data}')

#Main Function

def main():
    download("voidrealms.com",80)
    #sisteme bağlanıp veri almaya çalışıyoruz
    #port rastgele olursa reddedildi hatası alırız.
    #adres rastgele girersek servis bulunamadı der.


if __name__ == "__main__":
    main()
