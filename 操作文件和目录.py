import os #https://www.cnblogs.com/kaituorensheng/archive/2013/03/18/2965766.html os模块详解
print(os.name) #获取系统系统基本信息,如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
print(os.environ)#获取系统环境变量
print(os.environ.get('path'))#获取指定的环境变量
#操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：
print(os.path.abspath('.'))  #获取当前目录的绝对路径.
print(os.path.join('C:\\Users\\Administrator\\PycharmProjects\\python_office','testdir')) #把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符
#os.mkdir('C:\\Users\\Administrator\\PycharmProjects\\python_office\\testdir')
print (os.path.split('C:\\Users\\Administrator\\PycharmProjects\\python_office\\testdir\\test.txt')) #这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
print (os.path.splitext('C:\\Users\\Administrator\\PycharmProjects\\python_office\\testdir\\test.txt'))#可以直接让你得到文件扩展名
os.rename('C:\\Users\\Administrator\\PycharmProjects\\python_office\\testdir\\test.txt','C:\\Users\\Administrator\\PycharmProjects\\python_office\\testdir\\test.py') #重命名

