import itertools,time
y=itertools.count(5)
'''for i in y:
    print(i)
    time.sleep(1)
'''
'''
c=itertools.cycle('Abcdefg')
for i in c:
    print(i)
'''
#repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
d=itertools.repeat('A',3)
for i in d:
    print(i)

#chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
for i in itertools.chain('abc','EFG'):
    print(i)

#groupby()把迭代器中相邻的重复元素挑出来放在一起
for key,group in itertools.groupby('AAAABBBBCCCDDDFFGGG'):
    print(key,list(group))