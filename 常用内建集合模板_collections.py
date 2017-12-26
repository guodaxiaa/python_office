#!/usr/bin/python
#coding:utf-8
#collections是Python内建的一个集合模块，提供了许多有用的集合类。
#namedtuple
from collections import namedtuple,deque,defaultdict,OrderedDict,Counter
Point=namedtuple('Point',['x','y'])
p=Point(2,3)
print (p.x)
print (p.y)
#nmaedtuple有两个参数,第一个person是这个namedtuple的名字,后面定义了元素的类型和个数
person=namedtuple('person','name age gender')
person1=person('郭锐',20,'female')
print (person1.name,person1.age)
print (isinstance(p,Point))
print (isinstance(p,tuple))

#deque
#使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，
# 因为list是线性存储，数据量大的时候，插入和删除效率很低。
#deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
q=deque([1,2,3])
print(q[1])
q.append('x')#最后加
print (q)
q.appendleft('y')#前面加
print (q)
q.pop()#抛最后一个
print (q)
q.popleft()#抛第一个
print (q)
#defaultdict
#使用dict时，如果引用的Key不存在，就会抛出KeyError。
# 如果希望key不存在时，返回一个默认值，就可以用defaultdict
dd=defaultdict(lambda :'N/A')
dd[1]='abc'
dd[2]='efg'
print (dd[1])
print (dd[3])
print (dd)
#除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。

#OrderedDict
#使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
#如果要保持Key的顺序，可以用OrderedDict：
ee=dict([('x',1),('b',2),('g',3),('d',4),('e',5),('f',6)])
print (ee)
ff=OrderedDict([('x',1),('b',2),('g',3),('d',4),('e',5),('f',6)])
#Counter
#Counter是一个简单的计数器，例如，统计字符出现的个数：
c=Counter()
for ch in 'programming':
    c[ch]=c[ch]+1

print(c)

