#全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但互不影响。
# 你可以把local_school看成全局变量，但每个属性如local_school.student都是线程的局部变量，
# 可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理。
#可以理解为全局变量local_school是一个dict，不但可以用local_school.student，还可以绑定其他变量，如local_school.teacher等等。
import threading
local_school = threading.local()

def process_student():
    std = local_school.student
    print('Hello,%s (in %s)' % (std,threading.current_thread().name))

def process_thread (name):
    local_school.student = name
    process_student()

t1 = threading.Thread(target = process_thread,args = ('lucy',),name = 'Thread_A')
t2 = threading.Thread(target=process_thread,args=('lily',),name='Thread_B')
t1.start()
t2.start()
t1.join()
t2.join()
