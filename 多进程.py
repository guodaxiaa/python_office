#!/usr/bin/python
#coding:utf-8
from multiprocessing import Process
import os
def run_proc (name):
    print('run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print ('parent prcdess %s.' % os.getpid())
    p=Process(target=run_proc,args=('test',))
    print ('child process will start..')
    p.start()
    p.join()
    print('child process end..')
#创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，
# 用start()方法启动，这样创建进程比fork()还要简单。
#join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
