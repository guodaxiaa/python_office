''''#定义一个学生类,变量score通过方法设置,且可以检查数据
#
class Student(object):
    def get_score(self):
        return self.__score
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be integer!!!')
        elif value < 0 or value > 100:
            raise ValueError('score must between 0~100 !!!')
        else :
            self.__score=value
'''

'''s = Student()
s.set_score(60) # ok!
s.get_score()
60
s.set_score(9999)
Traceback (most recent call last):
...
ValueError: score must between 0 ~ 100!'''
#上面的调用方法又略显复杂，没有直接用属性这么直接简单
#Python内置的@property装饰器就是负责把一个方法变成属性调用的
class Student():
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!!!')
        if value >100 or value <0:
            raise ValueError('score must between 0~100!!!')
        self.__score=value

################################################################################
class Student():
    @property
    def birth(self):
        return self.__birth

    @birth.setter
    def birth(self, value):
        self.__birth = value

    @property
    def age(self):
        return 2017 - self.__birth


class Screen():
    @property
    def wigth(self):
        return self.__wigth

    @property
    def height(self):
        return self.__height

    @wigth.setter
    def wigth(self,value):
        self.__wigth=value

    @height.setter
    def height(self,value):
        self.__height=value

    @property
    def resolution(self):
        return self.__wigth * self.__height



