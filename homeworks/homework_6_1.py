from datetime import datetime as dt
from time import sleep


def checktime_before_after(func):
    def wrapper(*args, **kwargs):
        start =dt.now()
        print(f'функция была вызвана в {start.strftime("%H:%M:%S %d/%m/%Y")}')
        result = func(*args,**kwargs)
        end =dt.now()
        print(f'функция была закончена в {end.strftime("%H:%M:%S %d/%m/%Y")}')
        return result
    return wrapper

@checktime_before_after
def hello_world():
   print("hello world")
   sleep(1)

hello_world()

