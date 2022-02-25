#Logging Temelleri

#Printten daha iyi
#Her levenin sayısı var
"""
DEBUG     -> Developer için ne olduğunu bilmesi
INFO      -> Birşeyler oldu [kullancinin gormesi gerekebilir]
WARNING   -> Düzeltilmesse yada devam ederse kötü birşey olabilir
ERROR     -> Hata
CIRITICAL -> Hatadan daha kötü
"""

from cgitb import handler
import logging

#en üst seviye logger
#from logging import root


#Basit Logging
#Standart olarak gösterilmiyor

def test():
    print('-'*20)
    level = logging.getLevelName(logging.getLogger().getEffectiveLevel())
    print(f'Log Level: {level}') #level set edilmediğinden standart olarak warning
    #debug mesajı yaratıyoruz root loggerinda
    logging.debug('debug message here')
    logging.info('info message here')
    logging.warning('warning message here')
    logging.error('error message here')
    logging.critical('critical message here')
    print('-'*20)

test()


#Logging levels
#Logging levelini get ve set etme
#Filtrelemeye yarıyor

#Get the root logger
#eğer birden fazla logger [roottan başka] varsa getLogger('name') kısmına isim yazarız.
rootLog = logging.getLogger() #daha güzel gözüksün diye atama yaptık
print('Level: ' + logging.getLevelName(rootLog.getEffectiveLevel()))

#Set it to debug
rootLog.setLevel(logging.DEBUG)
test()

#Set it to critical
rootLog.setLevel(logging.CRITICAL)
test()

#Set it to Warning
rootLog.setLevel(logging.WARNING)
test()


#Dosyaya kaydetme [log to file]
#basicConfic sadece logger daha önce ayarlanmamışsa çalışır [kodun en başında çalışır]
#logging.basicConfig(filename='app.txt',filemode='w',format='%(levelname)s:%(message)s',level=logging.DEBUG)
#logging.debug('Hello')


#Handler ve formatter gerek
handler = logging.FileHandler('file.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#handlera nasıl formatlaması gerekeceğini söylüyor
handler.setFormatter(formatter)
rootLog.addHandler(handler)
rootLog.setLevel(logging.DEBUG)
rootLog.debug('test')
test()