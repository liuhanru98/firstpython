#!/usr/bin/python
# -*- coding: UTF-8 -*-
print "Python 是一个非常棒的语言，不是吗？"

# print "+++++++++++raw_input函数++++++++++++"
# str = raw_input("请输入：")
# print "您输入的内容是：",str
#
# print "++++++++++++input函数++++++++++++++"
# str = input("请输入：")
# print "你输入的内容是: ", str

# 打开一个文件
print "+++++++++++++打开一个文件++++++++++++"
fo = open("foo.txt", "w")
print "文件名: ", fo.name
print "是否已关闭 : ", fo.closed
print "访问模式 : ", fo.mode
print "末尾是否强制加空格 : ", fo.softspace
#关闭文件
fo.close()
print "是否已关闭 : ", fo.closed

print "=============创建一个foo.txt文件并写入些内容=============="
fo = open("foo.txt", "w")
fo.write( "www.runoob.com!\nVery good site!\n")
# 关闭打开的文件
fo.close()
print "是否已关闭 : ", fo.closed


# 打开一个文件
print "============读取部分文件内容==========="
fo = open("foo.txt", "r+")
str = fo.read(10)
print "读取的字符串是 : ", str

#查找当前位置
position = fo.tell()
print "当前文件位置：", position
position = fo.seek(0,0)
str = fo.read(10)
print "重新读取字符串:", str
# 关闭打开的文件
fo.close()



print "===============重命名和删除文件=============="
import os
#重命名文件test1.txt到test2.txt
# os.rename("test1.txt","test2.txt")

#删除一个已经存在的文件
# os.remove("test2.txt")

# 创建目录test
# os.mkdir("test3")

# 将当前目录改为"/home/newdir"
# os.chdir("/home/newdir2")

# 给出当前的目录
print os.getcwd()

# 删除”/tmp/test”目录
# os.rmdir("/tmp/test")

print "++++++++++++++异常获取解决++++++++++++++"
try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print "Error: 没有找到文件或读取文件失败"
else:
    print "内容写入文件成功"
    fh.close()

#当在try块中抛出一个异常，立即执行finally块代码。
#finally块中的所有语句执行后，异常被再次触发，并执行except块代码。
#参数的内容不同于异常。
try:
    fh = open("testfile","w")
    try:
        fh.write("这是一个测试文件，用于测试异常！！")
    finally:
        fh.close()
        print "文件已关闭"
except IOError:
    print "Error:没有找到文件或问津读取失败"


