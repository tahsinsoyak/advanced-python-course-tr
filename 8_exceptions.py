#Exceptions [Try,Except and Finally]
#Hatalar meydana geldiğinde

"""
Errors mostly occur at runtime that's they belong to an unchecked type.
Exceptions are the problems which can occur at runtime and compile time.
It mainly occurs in the code written by the developers.
Exceptions are divided into two categories such as
checked exceptions and unchecked exceptions.
"""

#Basit Decorator
from typing import final


def outline(func):
    def inner(*args, **kwargs):
        print('-'*20)
        print(f'Function: {func.__name__}') #fonksiyon ismi için
        func(*args,**kwargs)
        print('-'*20)
    return inner



#Try,Except and Finally
@outline
def test_one(x,y):
    try:
        #attempt [girişim]
        z = x/y
        print(f'Result: {z}')
    except: 
        #Catch
        print(f'Something bad happened x:{x}, y:{y}')
    finally:
        #Ne olursa olsun çağrılacak [Clean up - Temizlik]
        print('Complete')

test_one(5,0)
test_one(5,'cat')
test_one(5,2)


print('*****************')
print('*****************')



#Exceptionları Belirtmek
@outline
def test_two(x,y):
    try:
        #attempt
        assert(x > 0) #ileri sürmek,idda etmek
        assert(y > 0) #geçemesse AssertionError yaratacak ve exceptiona girecek
    except AssertionError: #SPECIFIC ERROR
        print(f'Failed to assert x:{x}, y:{y}')
    except TypeError:
        print(f'Type Error x:{type(x)}, y:{type(y)}')
    except Exception as e: #Rastgele hata için.
        #catch
        print(f'Something bad happened x:{x}, y:{y}, issue: {e}')
    else:
        #trusted code [güvenilir kod]
        z = x/y
        print(f'Result: {z}')
    finally:
        #clean up
        print('Complete')


test_two(5,0)
test_two(5,'cat')
test_two(5,2)



#Kullanıcı Tanımlı Hata ve Raising
class CatError(RuntimeError): #Built-in errordan kalıtım aldık
    def __init__(self,*args):
        self.args = args

@outline
def test_cats(qty):
    try:
        if not isinstance(qty,int):
            raise TypeError('Must be an int')#Hatayı çalıştırıyoruz
        if qty < 9:
            raise CatError('Must own more than 9 cats')
        print(f'You own {qty} cats')
    except Exception as e:
        print(f'Opps: {e.args}')
    finally:
        print('Complete')

test_cats('abc')
test_cats(3)
test_cats(12.3)
test_cats(11)