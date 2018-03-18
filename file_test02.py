# -*- coding:utf-8 -*-

__author__ = 'Gaoyonxian666'
__date__ = '2018/3/7 19:26'

# python中对文件、文件夹（文件操作函数）的操作需要涉及到os模块和shutil模块。



# 得到当前工作目录，即当前Python脚本工作的目录路径:
# os.getcwd()
# 返回指定目录下的所有文件和目录名:
# os.listdir()
# 函数用来删除一个文件: \
# os.remove()
# 删除多个目录：
# os.removedirs(r"c：\python")
# 返回一个路径的目录名和文件名: os.path.split()
# eg
# os.path.split('/home/swaroop/byte/code/poem.txt')
# 结果：('/home/swaroop/byte/code', 'poem.txt')

# 判断
# 检验给出的路径是否是一个文件：
# os.path.isfile()
# 检验给出的路径是否是一个目录：
# os.path.isdir()
# 判断是否是绝对路径：
# os.path.isabs()
# 检验给出的路径是否真地存:
#  os.path.exists()

# 重命名：os.rename（old， new）
# 创建多级目录：os.makedirs（r“c：\python\test”）
# 创建单个目录：os.mkdir（“test”）
# 获取文件属性：os.stat（file）
# 修改文件权限与时间戳：os.chmod（file）
# 终止当前进程：os.exit（）
# 获取文件大小：os.path.getsize（filename）
# 目录操作： os.mkdir("file")
# 分离扩展名：os.path.splitext()
# 获取路径名：os.path.dirname()
# 获取文件名：os.path.basename()

# 复制文件： shutil.copyfile("oldfile", "newfile")
# oldfile和newfile都只能是文件
# shutil.copy("oldfile", "newfile")
# oldfile只能是文件夹，newfile可以是文件，也可以是目标目录
# 复制文件夹：shutil.copytree("olddir", "newdir")
# olddir和newdir都只能是目录，且newdir必须不存在
# 重命名文件（目录）os.rename("oldname", "newname")
# 文件或目录都是使用这条命令
# 移动文件（目录） shutil.move("oldpos", "newpos")
# 删除文件
# os.remove("file")
# 删除目录
# os.rmdir("dir")
# 只能删除空目录
# shutil.rmtree("dir")
# 空目录、有内容的目录都可以删
# 转换目录换路径os.chdir("path")


# 给出当前平台使用的行终止符: os.linesep
# Windows使用'\r\n'，Linux使用 '\n'而Mac使用'\r'
# 指示你正在使用的平台：os.name
# 对于Windows，它是'nt'，而对于Linux / Unix用户，它是 'posix'
# 运行shell命令: os.system()
# 读取和设置环境变量:
# os.getenv()
# os.putenv()


import re
import os
import time


# str.split(string)分割字符串
# '连接符'.join(list) 将列表组成字符串
def change_name(path):
    global i
    if not os.path.isdir(path) and not os.path.isfile(path):
        return False
    if os.path.isfile(path):
        file_path = os.path.split(path)  # 分割出目录与文件
        lists = file_path[1].split('.')  # 分割出文件与文件扩展名
        file_ext = lists[-1]  # 取出后缀名(列表切片操作)
        img_ext = ['bmp', 'jpeg', 'gif', 'psd', 'png', 'jpg']
        if file_ext in img_ext:
            os.rename(path, file_path[0] + '/' + lists[0] + '_fc.' + file_ext)
            i += 1  # 注意这里的i是一个陷阱
            # 或者
            # img_ext = 'bmp|jpeg|gif|psd|png|jpg'
            # if file_ext in img_ext:
            #    print('ok---'+file_ext)
    elif os.path.isdir(path):
        for x in os.listdir(path):
            change_name(os.path.join(path, x))  # os.path.join()在路径处理上很有用


img_dir = 'D:\\xx\\xx\\images'
img_dir = img_dir.replace('\\', '/')
start = time.time()
i = 0
change_name(img_dir)
c = time.time() - start
print('程序运行耗时:%0.2f' % (c))
print('总共处理了 %s 张图片' % (i))



# 替换old为new：str.replace('old','new')
# 替换指定次数的old为new：str.replace('old','new',maxReplaceTimes)
# 保持目录a的目录结构，在b中创建对应的文件夹, 并把a中所有的文件加上后缀_bak

import os

Root = 'a'
Dest = 'b'

for (root, dirs, files) in os.walk(Root):
    new_root = root.replace(Root, Dest, 1)
    # 切换目录
    if not os.path.exists(new_root):
        os.mkdir(new_root)

    for d in dirs:
        d = os.path.join(new_root, d)
        if not os.path.exists(d):
            os.mkdir(d)

    for f in files:
        # 把文件名分解为 文件名.扩展名
        # 在这里可以添加一个 filter，过滤掉不想复制的文件类型，或者文件名
        (shotname, extension) = os.path.splitext(f)
        # 原文件的路径
        old_path = os.path.join(root, f)
        new_name = shotname + '_bak' + extension
        # 新文件的路径
        new_path = os.path.join(new_root, new_name)
        try:
            # 复制文件
            open(new_path, 'wb').write(open(old_path, 'rb').read())
        except IOError as e:
            print(e)
