#!/usr/bin/python
#coding:utf-8
#文档测试详细解释:http://blog.csdn.net/liuchunming033/article/details/51455663
def abs(n):
    '''
    用来获取绝对值;
    例如:
    >>>abs(1)
    1
    >>>abs(-1)
    1
    >>>abs(0)
    0
    '''
    return n if n>=0 else (-n)

if __name__=='__main__':
    import doctest
