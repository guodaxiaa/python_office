#!/usr/bin/python
#coding:utf-8
#方法一:直接打印变量:
def foo(s):
    n = int(s)
    print('>>>n = %d'% s)
    return 10/s

def main():
    return foo(1)

main()
#方法二:断言,凡是用print()来辅助查看的地方，都可以用断言（assert）来替代：

def foo1(s):
    n=int(s)
    assert n !=0,'n is zero'
    #assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
    return 10/s
def main1():
    return foo1(1)#如果是0,就会抛出错误
main1()

#方法三:logging
'''这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，
当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。
这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。'''
import logging
logging.basicConfig(level=logging.INFO)
s='0'
n=int(s)
logging.info('n=%d'% n)
print(10/n)

#方法四:pdb,让程序以单步方式运行，可以随时查看运行状态。

