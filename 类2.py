class Student(object):
    count=0
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
        Student.count+=1 #每创建一个学生类就加1


    def print_score(self):
        print('%s:%s'%(self.__name,self.__score))

    def get_name(self):
        return self.__name
    def get_score(self):
        return  self.__score
    def set_score(self,score):
        if 0 <=score<=100:
            self.__score=score
        else:
            raise ValueError('bad score')

a=Student('lili',99)
b=Student('lucy',89)
print(Student.count)





