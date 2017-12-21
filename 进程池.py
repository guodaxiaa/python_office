#!/usr/bin/python
#coding:utf-8
from  multiprocessing import Pool
import os,time,random
def long_time_task(name):
    print('Run task %s (%s)...'% (name,os.getpid()))
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print('Task %s runs %0.2f seconds.'% (name,(end - start)))

if __name__ =='__main__':
    print ('Parent process %s.'% os.getpid())
    p=Pool(9)
    for i in range(2):
        p.apply_async(long_time_task,args=(i,))
    print ('Waiting or all subprocesses done...')
    p.close()
    p.join()
    print ('All subprocesses done.')
#子进程
#很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。
#subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
#下面的例子演示了如何在Python代码中运行命令nslookup www.python.org，这和命令行直接运行的效果是一样的：
import subprocess
print ('$  nslookup www.pythoon.org')
r=subprocess.call(['nslookup','www.python.org'])
print ('Exit code:',r)

