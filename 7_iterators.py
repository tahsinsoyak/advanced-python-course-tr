#Iterators [yineleyici]
#Saymayı kolaylaştırmak için


#tuple üzerinde nasıl gezindiğimizi anlayacağız
t = (1,2,3,4)
for x in t:
    print(x)


#Iter (yenileme) Temelleri
#Lists, tuples, dictionaries, ve sets yenilenebilir nesnelerdir
#İçinden iterator (yenileyici) alabileceğin yenilenebilir containerlardır

people = ['Tahsin','Hasan','Ayse']
i = iter(people)
print(i) #list iterator olduğunu görürüz.
#liste değil bir yineleyici [pythona listede nasıl manevra yapacağımızı söylüyor.]

print(next(i))
print(next(i))
print(next(i))
#print(next(i)) #StopIteration [İşlemeyi bırak diyor python'a]



#Iterable Class
import random
class Lotto:
    def __init__(self): #Constructor
        self._max=5
    def __iter__(self):
        #yield => fonksiyonun çalışmasını durdurup
        #çağırana value'yu geri yolluyor ve durumun kaldığı
        #yerden devam etmesi için çıktının olmasını bekliyor
        #çıktı olduğunda kaldığı yerden devam ediyor
        for _ in range(self._max):
            yield random.randrange(0,100)
        #yield olduğu için '__next__' e gerek kalmıyor
        
    def setMax(self,value):
        self._max=value

print('-'*20)
lotto = Lotto()
lotto.setMax(5) #kaç tane sayı 

for x in lotto:
    print(x)

print('-'*20)

