#!/usr/bin/python
#coding:utf-8
import re
m=re.match(r'^\d{3}\-\d{3,8}$','010-12345')
print (m.group())
print ('ab    c'.split(' '))
print (re.split(r'[\s\,\;]+','a,b ;; ;*  c'))#以一个或者多个空格为分割符
#除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）
m=re.match(r'^(\d{3})\-(\d{3,8})$','010-123456')
#如果正则表达式中定义了组，就可以在Match对象上用group()方法提取出子串来
print (m.group(2))
#如果该正则在后面需要使用n多次,则预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配
re_telephone = re.compile(r'^(\d{3,4})\-(\d{3,8})$')
print(re_telephone.match('0713-5773279').group(2))