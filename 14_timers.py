#Timers

#time intervallerinde [aralık] kodu çalıştıracağız
#threadleri anlamak için önemli


#Importlar ve Displya

from cProfile import run
import time #tüm hepsini kullanmak için import
from threading import Timer #tek kısım için
#python java threading kullanır

def display(msg):
    print(msg + ' ' + time.strftime('%H:%M:%S'))

#Basit Timer
def run_once():
    display('Run once: ')
    t = Timer(5,display,['Timeout:'])
    t.start() #arka planda run metodu çalışıyor [javadan aldığı için]


run_once()
#Hemen çalışıyor!
#Ama sadece 1 defa çalışıyor
print('waiting...')
#çıktıda timer çıktısı çalışmıyor,5 saniye sonra çalıştırıyor



#Interval timer [aralıklı]
#Class içine sarıyoruz
#Biz durdurana kadar çalıştırıyoruz
#Birden fazla timerımız olacak

class RepeatTimer(Timer):
    def run(self): #run otomatik çalışıyor
        while not self.finished.wait(self.interval):
            self.function(*self.args,**self.kwargs)
        print('Done')

#Thread yapıp kontrol edeceğiz

timer = RepeatTimer(1,display,['Repeating'])
timer.start() #run metodunu çağıracak ve while döngüsü çalışacak

print('Threading started.')
time.sleep(10) #çıktıyı girilen saniye kadar duraklatıyoruz
print('Threading finishing')

timer.cancel() #kapatıyoruz

#threadimizi sleep yamazsak direk çalışır ve kapanır