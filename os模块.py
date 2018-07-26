"""
座右铭:近朱者赤近墨者黑
@project:7-26
@author:Mr.chi
@file:os模块.PY
@ide:PyCharm
@time:2018-07-26 09:26:42
"""
# os全称（operationSystem）操作系统
# os： 模块用于操作文件、文件夹等等
import os
# 1.cpu_count():获取cpu的个数
# 根据cpu的个数可以决定创建几个进程更合适，cpu个数=最好开启的进程数
count=os.cpu_count()
print('cpu的个数为{}'.format(count))

# 2.gencwd():返回当前文件所在的文件夹的绝对路径(重点)
cwd=os.getcwd()
print('当前路径的绝对路径是{}'.format(cwd))

# 3.name
# nt:windows系统
name=os.name
print('操作系统的名称:',name)

# 4.os.path.abspath():返回自身所在路径的绝对路径。
result=os.path.abspath('os模块.py')
print('绝对路径是{}'.format(result))

# 5.os.path.basename
result_1=os.path.basename('C:/Users/Administrator/Desktop/7-26/os模块.py')
print('取路径的最后一部分：{}'.format(result_1))

# 6. os.path.dirname():返回当前文件或文件夹所在的父级文件夹。
result_2=os.path.dirname('C:/Users/Administrator/Desktop/7-26/os模块.py')
print('当前文件所在的上一级目录是：{}'.format(result_2))

# 7.os.path.exists:判断路径下的文件/文件夹是否存在 True存在 False不存在（重点）
result_3=('C:/Users/Administrator/Desktop/7-26/os模块.py')
print('该路径对应的文件是否存在：{}'.format(result_3))

# 8. os.path.isfile():判断是否为文件
result_4=os.path.isfile('os模块.py')
print('是不是一个文件：{}'.format(result_4))

# 9. os.path.isdir():判断是否为文件夹
result_5=os.path.isdir('C:/Users/Administrator/Desktop/7-26')
print('是否为文件夹：',result_5)

# 10. os.path.join():拼接路径（小重点）
result_6=os.path.join('C:/Users/Administrator/Desktop/7-26/os模块.py')
print('拼接之后的路径是：{}'.format(result_6))

# 11. mkdir():创建文件夹（重点）
# 如果要在dir_1下面继续创建文件夹需要切换到dir_1这个文件夹中
# os.mkdir('dir_1')
# print(os.getcwd())

# 12.chdir():切换文件夹（重点）
# os.chdir('dir_1')
# os.mkdir('dir_2')
# os.chdir('dir_2')
# os.mkdir('dir_3')
# print(os.getcwd())

# 13.makedirs:递归创建文件夹,exist_ok=True存在也不会报错
# os.makedirs('a/b/c/d',exist_ok=True)

# 14.removedirs:递归删除文件夹
# os.removedirs('a/b/c/d')

# 补充：renames（更名）
# os.renames('a/b/c/d','e/f/g/h')

# 15.mknod创建文件(使用文件读写的open)，但是windows上面的python不支持创建
# os.mknod('test.txt')

# 16.rename:文件更名。（重点）
# os.rename('test.txt','test1.txt')

# 17.remove:文件删除。（重点）
# os.remove('test.txt')

# 18.os.path.pardir:返回当前文件或文件夹所在的父级目录（重点）
# ..父级目录
# .当前目录
# cudir()当前目录
print('当前文件/文件夹所在的父级目录：{}'.format(os.path.pardir))