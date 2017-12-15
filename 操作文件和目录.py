#!/usr/bin/python
#coding:utf-8
import os
print(os.environ.get('PATH'))
print(os.path.abspath('.')) #查看当前目录的绝对路径
print(os.path.join('G:\python_office','testdir'))## 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
os.mkdir('G:\python_office\\testdir')## 然后创建一个目录:
#把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，
# 这样可以正确处理不同操作系统的路径分隔符
