# Alt tire 
#_Single
#__Double
#__Before
#After__
#__Both__


#Skipping /atlama
# x yerine kullanılır
# birdaha umursamayacağımız, kullanmayacağımız değişkenler için
for _ in range(6):
    print('Hello')

#Test Class  [Person]
from person import *

#Before (Single)
#Internal kullanım sadece
p = Person()
p.setName('Bryan')
#erişmemize izin versede erişmemeliyiz
print(f'Weak Private {p._name}')


#Before (Double) [sadece tanımlandığı sınıfta çalışır]
#Internal kullanım sadece, alt sınıflarla çakışmadan kurtarır
#pythona ismi yeniden yazmasını söyle (Mangling [parçalıyor bozuyor])
p = Person()
p.work()
"""
p.__think()
#hata alırız
AttributeError: 'Person' object has no attribute '__think'
"""
c = Child()
"""
c.testDouble()
AttributeError: 'Child' object has no attribute '_Child__think'
"""


#After (Any) [zaten kullanılan değişkenleri syntaxa uysun diye değiştiriyoruz.]
#Çakışmaları engelliyor
class_ = Person()
print(class_)


#Before and Afret
#Pythona özel init,main gibi
p = Person()
p.__call__()
