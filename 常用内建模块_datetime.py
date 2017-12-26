#!/usr/bin/python
#coding:utf-8
from datetime import datetime,timedelta
now_time=datetime.now()
t=datetime(2017,12,21,21,5)  # 用指定日期时间创建datetime
print (now_time)
print(t.timestamp())
print (now_time.timestamp()) # 把datetime转换为timestamp
epoch_time=1234567890
t2=datetime.fromtimestamp(epoch_time)#把timestamp转换为datetime
print(t2)
t3=datetime.utcfromtimestamp(epoch_time)#timestamp也可以直接被转换到UTC标准时区的时间：
print (t3)
time_str='year 2014-12-24 time 19:21:23'
t4=datetime.strptime(time_str,'year %Y-%m-%d time %H:%M:%S')#str转换为datetime
print (t4)
#datetime转换为str
print (now_time.strftime('%a, %b %d %H:%M'))
t5=now_time.strftime('%a, %b %d %H:%M')
print (t5)
#datetime加减,需要导入timedelta这个类
t6=now_time+timedelta(days=10,hours=10,seconds=20,minutes=10)#可加可减,时分秒,天
print(t6)
