#Filter Fonksiyonu

#Filtre ile eşleşiyorsa true dönderir
#filter(fun, iterables)


#Sub range
import random
from unicodedata import name
v = []
for x in range(10):
    v.append(random.randrange(100))

print(v)

def lower(value):
    if value < 50:
        return True
    else:
        return False

#hemen fitreledik
f = filter(lower,v)
print(f'Less than 50: {list(f)}')


#Filtre Türleri

class Animal:
    name = ''
    def __init__(self,name):
        self.name = name

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

#Birbirinden haberi olmayan 2 sınıf


animals = []
for x in range(10):
    name = 'Animal ' + str(x)
    if(x % 2) == 0:
        #Çift Sayılar
        animals.append(Cat(name))
    else:
        #Tek Sayılar
        animals.append(Dog(name))

print(animals)
#kediler ve köpeklerden oluşan karışık bir liste yaptık

for a in animals:
    print(f'Animal: {a.name}')

#değer cat sınıfının bir örneğimi diye kontrol
def cats(value):
    return isinstance(value,Cat)

def dogs(value):
    return isinstance(value,Dog)


for c in list(filter(cats,animals)):
    print(f'Cat: {c.name}')

for c in list(filter(dogs,animals)):
    print(f'Dog: {c.name}')      

#filtreden gelen hayvanları filtreliyoruz

