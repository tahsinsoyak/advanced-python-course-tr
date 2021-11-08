

#değişken tanımlamadan atama yapıyoruz
#Feline Class
class Feline:
    def __init__(self,name):
        self.name = name
        print('creating a feline')

    def meow(self):
        print(f'{self.name}: meow')

    def setName(self,name):
        print(f'{self} setting name: {name}')
        self.name = name

#Leon Class
class Lion(Feline):
    def roar(self):
        print(f'{self.name} roar')


#Tiger Class
class Tiger(Feline):
    #constuctoru override etmek sıkıntılı
    def __init__(self):
        #Super miras veren  aileye erişiyor
        #superi unutursak çok sıkıntı yaşarız
        #super().__init__('No Name')
        print('Creating a tiger')
# bütün işi yapması için pythona güveniyoruz
    def stalk(self):
        # ismin parentte tanımlandığına dikkat etmeliyiz
        # bu -LBYL (look before you leap [atlamadan önce bak])
        # dinamik olarak attribute ekliyoruz

        # eğer super kullanarak constructor oluşturmasak sıkıntı yaşarız.
        # ğer hasattr(self, 'name'): super().setName('No Name') yapmassak olmaz
        print(f'{self.name}: stalking')

    def rename(self,name):
        super().setName(name)
        """
        #setname burada ismi eklerken super miras alınan
        #classın constructorunda ekliyor.
        setName('tiger')
        """




c = Feline('Kitty')
print(c)
c.meow()

#çıktı
"""
creating a feline
<__main__.Feline object at 0x000002C32D4F3FD0>
Kitty: meow
"""



#clasta fonksiyon olmasa bile mirastan dolayı artık var
l = Lion('Leo')
print(l)
l.meow()
l.roar()

# constructor tanımlamasak bile kittynin constructorunu çağırıyor
# Çıktı
"""
creating a feline
<__main__.Lion object at 0x000002C32D4F3E80>
Leo: meow
Leo roar
"""


t = Tiger() # Feline ama başka contructor var
print(t)
t.stalk()
#düzelttikten sonra sürekli çağırabiliriz

"""
Creating a tiger
<__main__.Tiger object at 0x0000026C2B033CD0>
#kendi constructorımızı tanımlamamız sıkıntı yarattı bize
#super çağırarak düzeltebiliriz
AttributeError: 'Tiger' object has no attribute 'name'. Did you mean: 'rename'? 
"""