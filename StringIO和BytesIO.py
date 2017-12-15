#!/usr/bin/python
#coding:utf-8
#我们需要先创建一个StringIO，然后，像文件一样写入即可
#getvalue()方法用于获得写入后的str。
from io import StringIO
f=StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())

#要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：
f2=StringIO('hello!\nhi!!\ngoodbye!')
while True:
    s=f2.readline()
    if s=='':
        break
    print(s.strip())

#StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
#BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：
from io import BytesIO
f3=BytesIO()
f3.write('中文'.encode('utf-8'))
print(f3.getvalue())
#和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取：
f4=BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f4.read())
print(f4.getvalue().decode('utf-8'))
