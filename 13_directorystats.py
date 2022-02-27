#Dir Stats
#Dizini recursive [özyinelemeli] olarak tarayan basit uygulama
#Ağaç şeklinden tarayacağız

#Import'lar ve Globaller [değişkenler]

import os #işletim sisteminden veri almak için [dosya yapısı,boyutu]

stats = dict(path='',folders=0,files=0,links=0,size=0)

#Kullanıcı girdisi alacağız

def get_input():
    global stats #global kullanmassak yeni değişken yaratıyor
    ret = os.path.abspath(input('Enter a folder path'))
    #kullanıcı girdisini alıp bir yola dönüştürüyoruz

    #yol yoksa çıkış yapıyoruz
    if not os.path.exists(ret):
        print('Sorry that path does not exist!')
        exit(1) #0 herhangi bir sorun yok demek [1 hata var]
    if not os.path.isdir(ret):
        print('Sorry that path is not a directory!')
        exit(2)
    
    stats['path'] = ret #path i atıyoruz

#yolu recursive tarıyoruz
def scan(path):
    global stats
    print('Scanning: ' + path)

    #farklı yolları da var biz walk deneyeceğiz
    for root,dirs,files in os.walk(path,onerror=None, followlinks=False):
        #error erişime izin olmayanlar için
         #linkleri takip ederek olduğumuz klasörden dışarı çıkarız
        stats['folders'] += len(dirs)
        stats['files'] += len(files)
        for name in files:
            fullname = os.path.join(root,name)
            #yolu ve dosya ismini birleştiriyoruz
            size = os.path.getsize(fullname)
            stats['size'] += size


#Display
def display():
    global stats
    print('Results:')
    for k,v in stats.items():
        print(f'{k} = {v}')


#Main Fonksiyonu
def main():
    global stats
    get_input()
    scan(stats['path'])
    display()


if __name__ == "__main__":
    main()