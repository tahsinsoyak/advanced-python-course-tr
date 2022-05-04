#DateTime
#Tarihlerle çalışmak, timedelta


#Imports
from datetime import date, datetime, timedelta
from time import strftime


def main():
    #now
    #eğer bilgisayar utc saat dilimindeyse now ile farkı olmaz
    now = datetime.now()
    utc = datetime.utcnow()

    print(f'Now: {now}')
    print(f'UTC: {utc}')
    print(f'Offset: {now.utcoffset()}')

    #time
    print(f'Hour: {now.hour}')
    print(f'Minute: {now.minute}')
    print(f'Second: {now.second}')
    print(f'Microsecond: {now.microsecond}')

    #Date
    print(f'Year: {now.year}')
    print(f'Month: {now.month}')
    print(f'Day: {now.day}')

    #Timedelta
    #Aradaki fark
    print(f'Next Month: {now + timedelta(days=30)}')
    print(f'Next Week: {now + timedelta(weeks=1)}')
    print(f'5 Hours: {now + timedelta(hours=5)}')
    print(f'45 Seconds: {now + timedelta(seconds=45)}')
    print(f'200 Milliseconds: {now + timedelta(milliseconds=200)}')
    print(f'10 Microseconds: {now + timedelta(microseconds=10)}')


    #ISO Strings
    d = datetime.fromisoformat('2020-12-16')
    print(d)
    #string ayarlama yapıyoruz [tarih almıyoruz]


    #Formatlama
    #A reference of all the legal format codes:
    #https://www.w3schools.com/python/python_datetime.asp
    print(now.strftime('%y'))
    print(now.strftime('%Y'))
    print(now.strftime('%d'))
    print(now.strftime('%D'))
    print(now.strftime('%b'))
    print(now.strftime('Today is %B %d'))




if __name__ == "__main__":
    main()
