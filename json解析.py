"""
座右铭:近朱者赤近墨者黑
@project:7-26
@author:Mr.chi
@file:json解析.PY
@ide:PyCharm
@time:2018-07-26 16:06:23
"""
# pip install requests(在python中安装requests包)
# 第三方的用于发送网络请求的一个模块，经常被用于爬虫
import requests
import json
response=requests.get('http://api.map.baidu.com/telematics/v3/weather?location=郑州市&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?').text
print(type(response))
print(response)
res_result=json.loads(response)
print(type(res_result))
print(res_result)
# 取error得值
error=res_result['error']
print('error的值',error)
# 取status的值
status=res_result['status']
# 取data的值
date=res_result['date']
print(date)
# 取results的值,取出来的结果是一个列表，列表里面是包含着一个字典。
results=res_result['results']
print(results)

# 从result这个列表中取出这个字典
dict_1=results[0]
print(type(dict_1))
print(dict_1)
# 从dict_1这个字典当中，通过键取值
currentCity=dict_1['currentCity']
print(currentCity)
pm_25=dict_1['pm25']
print(pm_25)
# 从dict_1这个字典中取出键是index的值，对应的是一个列表
index=dict_1['index']

# 使用for循环遍历index这个列表
for dex in index:
    # 取出来的每一个dex都是字典。
    des=dex['des']
    tipt=dex['tipt']
    title=dex['title']
    zs=dex['zs']
    print(des,tipt,title,zs)

# 从result这个列表中取出这个字典
dict_2=results[0]
print(type(dict_2))
print(dict_2)
# 从dict_1这个字典当中，通过键取值
weather_data=dict_2['weather_data']
print(weather_data)



# 使用for循环遍历weather_data这个列表
for dex1 in weather_data:
    # 取出来的每一个dex都是字典。
    date=dex1['date']
    dayPictureUrl=dex1['dayPictureUrl']
    nightPictureUrl=dex1['nightPictureUrl']
    weather=dex1['weather']
    wind = dex1['wind']
    temperature= dex1['temperature']
    print(date,dayPictureUrl,nightPictureUrl,weather,wind,temperature)