#Pythonda herşey birer nesnesidir
#Fonksiyonlar object olarak kullanılabilir
#Decorator bir fonksiyon alıyor ve fonksiyonellik ekleyip geri dönderiyor


#Basit Decorator
#Execute sırasını değiştiriyoruz. [Dikkat return yok]
from operator import truediv


def test_decorator(func):
    print('before')
    func()
    print('after')

#decorate etmemiz istediğimiz fonksiynoun üstüne yazıyoruz
@test_decorator
def do_stuff():
    print('Doing stuff')

#kodu çağırmamamıza rağmen direk çalışıyor





#Real Decorator
#Bu örnekte fonksiyelliğini değiştireceğiz
def makeBold(func):
    def inner():
        print('<b>')
        func()
        print('</b>')
    return inner #inner fonksiyona işaret eden  return

#printName i paremetre olarak al inner fonksiyonuna gir
#<b> yazdır ve bizim fonksiyonumuzu çağır ardından </b> yazdır
#ve return fonksiyonunu çağırmadan dönder.


#@makeBold 
# f = makeBold(printName)
# f()
#'a eşittir ve bu şekilde çalışyor

@makeBold
def printName():
    print('Tahsin Soyak')

printName() #ancak bu şekilde çalıştırdık
#aslında "inner()" demiş olduk


#Decorator [Paremetreli]
#Paremetre sayısı tanımlı olacak

def numCheck(func):
    def checkInt(o):
        if isinstance(o,int): #int kontrolu
            if o == 0: #0 kontrolu
                print('Can not divide by zero')
                return False
            return True
        print(f'{o} is not a number')
        return False

    def inner(x,y):
        if not checkInt(x) or not checkInt(y):
            return  #sadece return olduğundan aksiyon almayacak
        return func(x,y)
    return inner

@numCheck
def divide(a,b):
    print(a / b)


divide(100,3)
divide(100,0)
divide(100,'cat')
#Decoratorsuz çalışmayan kodlar
#0'a bölünme hatası alırız, divide(100,0)
#desteklenmeyen bölme, divide(100,'cat')




#Decorators [Bilinmeyen Sayıda Argüman]
#Paremetre alan ve herşeyi halleden decorator istiyoru
#Decoratorları birbirlerine zincirlemek istiyorsak
# *args, **kwargs kurtarıcıdır
#zincir kısmında return'ün önemini anlıyoruz
def outline(func):
    def inner(*args, **kwargs):
        print('~'*20)
        func(*args,**kwargs)
        print('~'*20)
    return inner

def list_items(func):
    def inner(*args,**kwargs):
        func(*args,**kwargs)
        print(f'args = {args}')
        print(f'kargs = {kwargs}')
        for x in args:
            print(f'arg={x}')
        for k,v in kwargs.items(): #k,v key,value
            print(f'key={k}, value={v}')
    return inner

#ilk yazılan çalışır
@outline
@list_items
def display(msg):
    print(msg)


#çalıştığında list_items fonksiyonu outline fonksiyonunun içinden çalışır
#zincirin anlamı iş içe, outline en baştaki sembol
#ilk decorator ilk çalışır
display('hello world')
#kwargs yok argüman var


#2. bir fonksiyonda yine aynı decoratorları kullanabiliriz
@outline
@list_items
def birthday(name='',age=0):
    print(f'Happy birthday {name} you are {age} years old')

birthday(name="Tahsin", age=21)


#args tupple
#kwargs dictionary