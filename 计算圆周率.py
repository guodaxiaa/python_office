#计算圆周率
# -*- coding: utf-8 -*-
#def pi(N):
    #' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...

    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.

    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...

    # step 4: 求和:
import itertools
from decimal import *

def pi(n):
    getcontext().prec = n
    a=itertools.count(1)
    d=[]
    for i in a:
        if i%2 == 1 and i <(2*n):
            d.append(i)
        if i >2*n:
            break
    d2=[]
    for i in range(n):
        if i%2==1:
            d2.append(-(d[i]))
        if i%2==0:
            d2.append(d[i])
    p=0
    for i in range(n):
        p=p+(4/(d2[i]))

    print(p)
pi(1000)

