#定制类
class Student():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name:%s)' % self.name

    __repr__ = __str__
####################################################################
#如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

#我们以斐波那契数列为例，写一个Fib类，可以作用于for循环：
class Fib():
    def __init__(self):
        self.a,self.b=0,1 #初始化两个变量
    def __iter__(self):
        return self #实例本身就是迭代对象,故返回自己
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b  #计算下一个值
        if self.a > 100000: #退出循环的条件
            raise StopIteration()
        return self.a #返回下一个值

#调试

'''for n in Fib():
    print(n)

'''

#Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素.
#要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
#调试
class Fib1():
    def __getitem__(self, n):
            a,b=1,1
            for i in range(n):
                a,b=b,a+b
            return a

f=Fib1()
print(f[100])
#但是list有个神奇的切片方法,对于Fib却报错。
# 原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：
class Fib2():
    def __getitem__(self, n):
        if isinstance(n,int): #判断是否未索引
            a,b=1,1
            for x in range(n):
                a,b=b,a+b
            return a
        if isinstance(n,slice):#判断是否为切片.
            start=n.start
            stop=n.stop
            if start is None:
                start = 0
            a,b=1,1
            L=[]
            for x in range(stop):
                if x >=start:
                    L.append(a)
                a,b=b,a+b
            return L

f=Fib2()
print(f[0:10])

#__getattr__  调用不存在的属性的时候,如果没有定义__getattr__方法,就会报AttributeError..
# 可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用。
class Student():
	def __init__(self):
		self.name='Micheal'
	def __getattr__(self,attr):
		if attr=='score':
			return 99
		else:
			return '没有该属性!!'
s=Student()
print(s.name)
print(s.score)
print(s.aaaa)

#__call__
#一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用.
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。Python中有一个有趣的语法，只要定义类型的时候，实现__call__函数，这个类型就成为可调用的。
#换句话说，我们可以把这个类型的对象当作函数来使用，相当于 重载了括号运算符。

class Student3():
    def __init__(self,name):
        self.name=name
    def __call__(self):
        print('My name is %s'% self.name)

s=Student3('lucy')
print(s())
#那么，怎么判断一个变量是对象还是函数呢？
# 其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例：
'''>>> callable(Student3())
True
>>> callable(max)
True
>>> callable([1, 2, 3])
False
>>> callable(None)
False
>>> callable('str')
False'''










