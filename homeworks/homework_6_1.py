from datetime import datetime as dt
from time import sleep


def checktime_before_after(func):
    def wrapper():
        start =dt.now()
        print(f'функция была вызвана в {start.strftime("%H:%M:%S %d/%m/%Y")}')
        func()
        end =dt.now()
        print(f'функция была закончена в {end.strftime("%H:%M:%S %d/%m/%Y")}')
    return wrapper

@checktime_before_after
def hello_world():
   print("hello world")
   sleep(1)

hello_world()

