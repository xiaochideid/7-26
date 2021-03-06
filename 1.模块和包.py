"""
座右铭:将来的你一定会感激现在拼命的自己
@project:7-25
@author:Mr.Zhang
@file:模块和保.PY
@ide:PyCharm
@time:2018-07-25 16:34:33
"""
#Python中的模块分为三类：
#1.Python标准库
#2.第三方库(模块)
#3.用户自定义模块


#1.模块的定义:本质上就是一个.py结尾的文件，文件里面包含着一些变量，函数，类等。
#.py文件名：my_module.py 对应的模块的名称：module


#导入模块的几种方式：
#第一种：
#(每个模块名之间要用逗号隔开)
# import 模块名1，模块名2，模块名3

#第二种:
#from 模块名 import 变量1，变量2，函数1，函数2

#from 模块名 import *(这种方式不建议用)

#因为假如导入的模块，也有被导入模块中的函数或者变量，则它们会产生冲突


#第三种+
#from 模块名 import xx  as 别名


#2.包：包里面放置了一堆模块，包里面必须包含__init__.py这个文件才能称之为包。
