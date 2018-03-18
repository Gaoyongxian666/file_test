# -*- coding:utf-8 -*-
from sys import path

__author__ = 'Gaoyonxian666'
__date__ = '2018/3/7 19:04'

import os
import os.path

# rootdir = "D:\\360"
# 指明被遍历的文件夹
# 注意反斜杠要转义
# 如果想要是根目录"D:\\"


# 如果只需要获得单个目录节点的子节点：
# 返回的是个list不管是文件还是文件夹


# 找某个目录下的某中后缀文件
rootdir=r'C:\Users\gyx\Desktop\作业'
dirlist=os.listdir(rootdir)
print(dirlist)
for filename in dirlist:
    print(os.path.join(rootdir, filename))
(parent, dirnames, filenames) = next(os.walk(rootdir))
print(dirnames)
#list类型
for filename in dirnames:
    print(os.path.join(rootdir, filename))
print(filenames)
#list类型
for filename in filenames:
    files_path=os.path.join(rootdir, filename)
    print(files_path)
    file_path = os.path.split(files_path)  # 分割出目录与文件
    print(file_path)
    lists = file_path[1].split('.') # 分割出文件与文件扩展名,字符串变成列表
    print(lists)
    file_ext = lists[-1]  # 取出后缀名(列表切片操作)
    print(file_ext)
    img_ext = ['bmp', 'jpeg', 'gif', 'psd', 'png', 'jpg']
    if file_ext in img_ext:
        pass


# next() 返回迭代器的下一个项目。 iterator - 可迭代对象.  default - 可选，用于设置在没有下一个元素时返回该默认值，如果不设置，又没有下一个元素则会触发 StopIteration 异常。返回对象帮助信息。
# 语法：next(iterator[, default])
# 首先获得Iterator对象:
# eg:
# it = iter([1, 2, 3, 4, 5])
# # 循环:
# while True:
#     try:
#         # 获得下一个值:
#         x = next(it)
#         print(x)
#     except StopIteration:
#         # 遇到StopIteration就退出循环        break




# for parent, dirnames, filenames in os.walk(rootdir):  # 三个参数：分别返回
#     # 1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
#     # 注意这个会遍历目录其中的所有文件
#     for dirname in dirnames:  # 输出文件夹信息
#         print("parent is:" + parent)
#         print("dirname is" + dirname)
#
#     for filename in filenames:  # 输出文件信息
#         print("parent is:" + parent)
#         print("filename is:" + filename)
#         print("the full name of the file is:" + os.path.join(parent, filename) ) # 输出文件路径信息
