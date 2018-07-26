"""
座右铭:近朱者赤近墨者黑
@project:7-26
@author:Mr.chi
@file:时间模块.PY
@ide:PyCharm
@time:2018-07-26 10:52:05
"""
import  time

# 1.获取时间戳
# 1.获取时间戳，单位为秒，从1970年1月1日00:00到现在一共经历了时间是多少秒
# 时间戳一般用于验证登录否过期
timestamp=time.time()
print(timestamp)
# 2.localtime():用于返回本地时间的函数，返回值是一个元组。[不方便观看]
localtime=time.localtime()
print(localtime)
print(localtime.tm_year)
print(localtime.tm_mon)
print(localtime.tm_mday)
# 3.asctime():获取格式化的本地时间 【方便观看】
local_time=time.asctime(time.localtime())
print('000',local_time)

# 4.将本地时间元组格式化成2018-7-26 11:01：xx的形式
# strftime():将时间元组转化成格式化的时间字符串
time_1=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
print(time_1)

# 5.将格式化的字符串转化为时间元组
string='Thu Jul 26 14:04 2018'
time_2=time.strptime(string,'%a %b %d %H:%M %Y')
print(time_2)

string1='2018-07-26 14:20:55'
time_3=time.strptime(string1,'%Y-%m-%d %H:%M:%S')
print(time_3)

# 2018-7-26 14:04 Thu Jul
string2='2018-7-26  14:04 Thu Jul'
time_4=time.strptime(string2,'%Y-%m-%d %H:%M  %a %b')
# 将时间元组转化成格式化的字符串：14:05:30  7-26-18
time_5=time.strftime('%H:%M:%S %m-%d-%y',time.localtime())
print(time_5)