import time,threading
blance=0
lock = threading.Lock()
def change_it(n):
    global blance
    blance=blance+n
    blance=blance-n

def run_thread(n):
    for i in range(2000000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()


t1=threading.Thread(target=run_thread,args=(5,))
t2=threading.Thread(target=run_thread,args=(4,))
t1.start()
t2.start()
t1.join()
t2.join()
print('blance:',blance)
#死循环
import  multiprocessing

def lop():
    x=0
    while True:
        x=x^1

for i in range(10):
    t=threading.Thread(target=lop)
    t.start()
