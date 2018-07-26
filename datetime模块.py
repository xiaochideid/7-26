"""
座右铭:近朱者赤近墨者黑
@project:7-26
@author:Mr.chi
@file:datetime.PY
@ide:PyCharm
@time:2018-07-26 14:34:54
"""
import datetime

# 1.获取当前时间和日期
datetime_dt=datetime.datetime.today()
print('获取当前时间和日期:{}'.format(datetime_dt))

# 2.格式化时间和日期
datetime_str=datetime_dt.strftime('%Y-%m-%d %H:%M:%S')
print('获取当前时间和日期格式化之后为:{}'.format(datetime_str))

# 3.设置一个时间间隔
time_delta=datetime.timedelta(hours=3)
print('当前设置的时间间隔为：{}'.format(time_delta))
# 把当前的时间延后三个小时
datetime_pre=datetime.datetime.today()+time_delta
print('时间延后三个小时为：{}'.format(datetime_pre))

# 4.获取当前的日期
date=datetime.datetime.today().date()
print('当前日期为：{}'.format(date))
# 5.获取当前时间
time=datetime.datetime.today().time()
print('当前时间为：{}'.format(time))

# 6.将时间和日期换成时间戳
time_s=datetime.datetime.today().timestamp()
print('现在的时间戳为：{}'.format(time_s))