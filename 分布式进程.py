#!/usr/bin/python
#coding:utf-8
#举个例子：如果我们已经有一个通过Queue通信的多进程程序在同一台机器上运行，
# 现在，由于处理任务的进程任务繁重，希望把发送任务的进程和处理任务的进程分布到两台机器上。
# 怎么用分布式进程实现？
import random,time,queue
from multiprocessing.managers import BaseManager
#发送任务的队列
task_queue=queue.Queue()
#接受结果的队列
result_queue=queue.Queue()
#从basemanager继承的QueueManager
class QueueManager(BaseManager):
    pass

#把两个Queue都注册到网络上,callable参数关联了Queue对象
QueueManager.register('get_task_queue',callable=lambda: task_queue)
QueueManager.register('get_result_queue',callable=lambda: result_queue)
#绑定端口5000,设置验证码为'abc'
manager=QueueManager(address=('',5000),authkey=b'abc')
#启动Queue
manager.start()
#获得通过网络获得的Queue对象
task=manager.get_task_queue()
result=manager.get_result_queue()
#放几个任务进去
for i in range(10):
    n=random.randint(0,10000)
    print('Put task %d...'% n)
    task.put(n)
 #从result队列读取结果:
print ('Try get results...')
for i in range(10):
    r=result.get(timeout=10)
    print('Result:%s'%r)
#关闭
manager.shutdown()
print('master exit')
#请注意，当我们在一台机器上写多进程程序时，创建的Queue可以直接拿来用，
# 但是，在分布式多进程环境下，添加任务到Queue不可以直接对原始的task_queue进行操作，
# 那样就绕过了QueueManager的封装，必须通过manager.get_task_queue()获得的Queue接口添加。
#上述代码只能在非windos环境下运行


