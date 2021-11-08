# self ilk parametre
# başka programlama dillerinde "this"
# instance = created

# yazdığımız kedi klasini import edelim


#bütün classları çağırır
import cat
# sadece belirttiğimiz classı çağırır
from cat import Cat

def test():
    #self python tarafından konuluyor
    b = Cat('Kitkat',1,'tabby')
    c = Cat('Othello',6,'black')
    print(b)
    print(c)
    b.description()
    c.description()

    c.meow()
    b.sleep()
    c.hungry()
    b.eat()

#program çalıştığında çalışacak
# 3 örnek obje oluşturuyoruz
if __name__ == "__main__":
    x = Cat('test')
    print(x)
    test()
