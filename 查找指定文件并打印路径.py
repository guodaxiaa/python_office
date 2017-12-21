#!/usr/bin/python
#coding:utf-8
import os
g=os.walk('C:\\') #生成的是一个三元数组,第一个是路径，第二个是路径下面的目录，第三个是路径下面的非目录
path_dic=[]
for path,d,filelist in g:
    path_dic.append(path)
a=range(1,len(path_dic))
for i in a:
    new_dir=os.listdir(path_dic[i])
    for x in range(0,len(new_dir)):
        if os.path.splitext(new_dir[x])[0]=='我的简历2':
            print(new_dir[x],'文件的路径是:',path_dic[i])