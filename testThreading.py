from threading import Thread
from time import sleep

def Writer(cymbol, delay):
    for i in range(10):
        print(cymbol)
        sleep(delay)

t1 = Thread(target = Writer, args= ('A', 1))    
t2 = Thread(target = Writer, args= ('B', 2))    

t1.start()
t2.start()

t1.join()
t2.join()
    