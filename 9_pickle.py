#Pickle

#Serializing Objects [Nesne Serileştirme]
#Nesneleri ve durumlarını kaydetme ve yükleme
#Python data türleri ve top seviye classlar

#The pickle module is not secure. Only unpickle data you trust.!!

""" Pickle Edilebilecek Türler
Booleans,
Integers,
Floats,
Complex numbers,
(normal and Unicode) Strings,
Tuples,
Lists,
Sets, and
Dictionaries that ontain picklable objects.
Bazi fonksiyonlar ve siniflarda pickle edilebilir.
"""

import pickle

#Her zamanki Decorator
def outline(func):
    def inner(*args, **kwargs):
        print('-'*20)
        print(f'Function: {func.__name__}')
        func(*args,**kwargs)
        print('-'*20)
    return inner


#Basit Sınıf
class Cat:
    def __init__(self,name,age,info):
        self._name =name #_ bu sınıfa ait başkası erişmesin diye
        self._age =age
        self._info =info
    @outline
    def display(self,msg=''):
        print(msg)
        print(f'{self._name} is a {self._age} years old cat')
        for k,v in self._info.items():
            print(f'{k} = {v}')

othello = Cat('Othello', 15, dict(color='Black',weight=15,loves='eating'))
othello.display('deneme')


#Serialize
sc = pickle.dumps(othello) #othello nesne örneğini bir stringe aktarıyoruz
print(sc) #pickle edildikten sonra gözüken şey
#başındaki b binary

with open('cat.txt','wb') as f: #dosyayı kaydetmek için [wb (write binnary)]
    pickle.dump(othello,f) #f dosyasına dumplıyoruz [hex olarak]
#serialize edilmiş dosyamız kaydedildi

#Deserialize
mycat = pickle.loads(sc) #dosyayı al ve kullanılabilir objeye aktar diyoruz
print('from string')
mycat.display('from string')

#Dosyadan yapmak için
with open('cat.txt','rb') as f: #rb read binary
    diskcat = pickle.load(f)
diskcat.display('from disk')
#aynı kaynaktan gelselerde farklı objeler


print(mycat)
print(diskcat)