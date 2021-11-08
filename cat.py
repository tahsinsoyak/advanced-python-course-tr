class Cat:
    #blueprintleri oluşturuyoruz
    name = ''
    age = 0
    color = ''

    #constructor [boşta geçilebilir]
    # __ ile başlayanlar python tarafından yazılmış
    # self kullanılan objeye referans

    # def __init__():
    #     pass
    
    #self gerekli diğer paremetreler isteğe bağlı
    def __init__(self,name,age=0,color='white'):
        self.name = name
        self.age = age
        self.color = color
        print(f'Constructor for {self.name}')

    def meow(self):
        print(f'{self.name} meow')
    
    def sleep(self):
        print(f'{self.name} zzz')

    def hungry(self):
        for x in range(5):
            self.meow()

    def eat(self):
        print(f'{self.name} nom nom nom')
    
    def description(self):
        print(f'{self.name} is a {self.color} cat, who is {self.age} years old.')