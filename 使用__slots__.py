class Student():
    __slots__ = ('name','score')        # 用tuple定义允许绑定的属性名称   ###__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
    pass
s=Student()
s.name='lucy'   #给实例绑定一个属性
print(s.name)

def set_age(self,age):#定义一个函数
    self.age=age

from types import MethodType    #导入
s.set_age=MethodType(set_age,s)     #  将set_age与实例s绑定  #应为上面的定义限制,绑定age将会报错.
s.set_age(23)
print(s.age)

s2=Student()
#s2.set_age(24) #新建实例后,是无法调用之前实例绑定的方法的.

#给class绑定方法
def set_score(self,score):
    self.score=score
Student.set_score=set_score  #给Student类绑定一个get_score方法
s.set_score(100)
print(s.score)

s2.set_score(88)
print(s2.score)
