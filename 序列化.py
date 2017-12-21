#!/usr/bin/python
#coding:utf-8
import pickle
'''d=dict(name='bobo',age=20,score=89)
print(d['name'])
print(pickle.dumps(d))
#pickle.dumps()方法把任意对象序列化成一个bytes，
# 然后，就可以把这个bytes写入文件。
# 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object
f=open('dump.txt','wb')
pickle.dump(d,f)
f.close()
print(d)
'''
#保存后的dump.txt文件,我们可以再开启一个python解释器,反序列化就可以看到内容了
f=open('dump.txt','rb')
d=pickle.load(f)
#print(d)

########################################################################
#JSON
import json
d=dict(name='bobo',age=20,score=99)
print(json.dumps(d))

#json进阶
class student():
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score

s=student('bob',20,98)
#前面的代码之所以无法把Student类实例序列化为JSON，是因为默认情况下，
# dumps()方法不知道如何将Student实例变为一个JSON的{}对象。
def student2dict(std):#为Student专门写一个转换函数，再把函数传进去即可
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score
    }
print (json.dumps(s,default=student2dict))


obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)