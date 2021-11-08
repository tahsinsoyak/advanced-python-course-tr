

#Taşıt sınıfı yapıyoruz.
class Vehical:
    speed = 0
    def drive(self,speed):
        self.speed = speed
        print('Driving')

    def stop(self):
        self.speed = 0
        print('Stopped')

    def display(self):
        print(f'Driving at {self.speed} speed')

#Dondurucu sınıfı
class Freezer:
    temp = 0
    def freeze(self,temp):
        self.temp = temp
        print('Freezing')

    def display(self):
        print(f'Freezing at {self.temp} temp')


#FreezerTruck sınıfı
# Method Resolution Order (MRO) - methodu önce tanımladığımızın displayi gözükecek
# İlk gelen ilk çözünür
class FreezerTruck(Freezer,Vehical):
    """
    #hiçbirşey yapmayan sınıf tanımlıyoruz
    #pass hiçbirşey yapmıyor demek
    pass
    """
    def display(self):
        #freezertruck freeezerın alt sınıfı diyoruz
        print(f'Is a Freezer: {issubclass(FreezerTruck,Freezer)}')
        print(f'Is a Vehical: {issubclass(FreezerTruck,Vehical)}')
        #supere her ikisininde displayini çağır dedik
        """
                super(Vehical,self).display() #çalışır ama ikisi olursa çalışmaz
        #biri önce geldiği için çalışmıyor MRO'dan dolayı
        super(Freezer,self).display()
        """
        #bağımsız olarak her birini çağırmamız lazım
        Freezer.display(self)
        Vehical.display(self)


t = FreezerTruck()
t.drive(30)
t.freeze(-25)
print('-'*20)
t.display()