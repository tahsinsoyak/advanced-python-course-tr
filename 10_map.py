#Map

#Loop kullanmadan döngü yapmak
#map fonksiyonu item koleksiyonunu çağırır
#map(func,itearables) -> fonksiyon ve yinelebilir öğeler



#Basit Kullanım - Uzunluk Sayma
from audioop import mul


people = ['Matt','Tahsin','Ali','Hasan']

#eski tarz
counts = []
for x in people:
    counts.append(len(x))
print(f'Old way: {counts}')


#modern tarz
print(f'Mapped: {list(map(len,people))}')
#map people listesini alıp len fonksiyonun içine atıyor
#list te map objesini alıyor ve listeye çeviriyor




#Complex Kullanım - Elementleri Birleştirme
#Birden fazla argüman [*args] gönderme ve farklı uzunluklarda [veri sayısı]

firstnames = ('Apple','Choclate','Fudge','Pizza')
lastnames = ('Pie','Cake','Brownies')

def merg(a,b):
    return a + ' ' + b

x = map(merg,firstnames, lastnames)
print(x) #-> map objesi diye birşey görürüz
print(list(x)) #liste cast edip görüyoruz
#Veri sayısından dolayı hata vermedi sessizce etkisizleşti
#Program çökmedi



#Çoklu Fonksiyon - Fonksiyon Birleştirme
#Tek map çağrısında birden fazla fonksiyon çağırma

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

def doall(func,num):
    return func(num[0],num[1]) # numaraları liste olarak alıyoruz

#pythonda fonksiyonlar tupple objesidir.
#fonksiyonlardan bir tupple oluşturuyoruz
f = (add,subtract,multiply,divide)
v = [[5,3]] #tek elemanlı liste [elemanı => liste]
n = list(v) * len(f)
#listemizi alıp kaç tane fonksiyonumuz varsa onun kadar çarpıyoruz

print(f'f: {f}, n:{n}')
#f çıktısında fonksiyonlarımız ve adresleri
#n çuktısında her bir fonksiyon çağrısı için listemiz var [4 tane]
# 5 ve 3 num[0] ve num[1]

m = map(doall,f,n)
#map' doall fonksiyonunu f'e[bütün fonksiyonlarımıza] n koyarak yap.
#map objesi döner

print(list(m))