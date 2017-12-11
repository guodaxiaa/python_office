#!/usr/bin/python
#coding:utf-8
try:
    print('try...')
    r=10/0  #r如果这一步出现错误,下面的print不会执行,会被except捕获到,并且打印错误类型except: division by zero
    print('result:',r)
except ZeroDivisionError as e:
    print('except:',e)
finally:#这一步是一定会执行的,有时候finally不是必须的
    print('finally...')
print('end')

try:
    print('try...')
    r=10/int('1')   #这里可以出现三种类型非整型数字,0,整型  会根据不通的错误类型来捕捉
    print('result:',r)
except ValueError as e:
    print ('except:',e)
except ZeroDivisionError as e:
    print('except:',e)
else:                  #可以接一个else,如果没有错误的时候会直接执行.
    print('no error!!!')
finally:
    print('finally...')
print('END')
#Python的错误其实也是class，所有的错误类型都继承自BaseException.
# 所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”
#Python所有的错误都是从BaseException类派生的，常见的错误类型和继承关系看这里：
#https://docs.python.org/3/library/exceptions.html#exception-hierarchy
#######################################################################################

#记录错误:
import logging
def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s)*2
def main():
    try:
        return  bar('3')
    except Exception as e:
        logging.exception(e)

print(main())
print('END')

#抛出错误
class FooError(ValueError): #自己定义的一个错误类,继承ValueError
    pass
def foo1(s):
    n=int(s)
    if n==0:
        raise FooError('invalid value %s'% s) #然后抛出自己定义的错误类型
    return 10/s

print(foo1(1))
#练习
'''from functools import reduce

def str2num(s):
    return int(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()'''
#修改后的代码
from functools import reduce

def str2num(s):
    return int(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    try:
        r = calc('100 + 200 + 345')
        print('100 + 200 + 345 =', r)
    except ValueError as e:
        print('数据类型错误:',e)
    try:
        r = calc('99 + 88 + 7.6')
        print('99 + 88 + 7.6 =', r)
    except ValueError as e:
        print('数据类型错误:',e)
main()

