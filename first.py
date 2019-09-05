#!/usr/bin/python
# -*- coding: UTF-8 -*-
#上面一句是设置字符编码格式的,如果在setting的encoding中设置了编码格式，这个地方就不需要在设置了
print "Hello World!"
print 'hello';print 'runoob';

if True:
    print "Answer"
    print "True"
else:
    print "Answer"
    print "False"

x="a"
y="b"

# 换行输出
print x
print y

print '---------'
# 不换行输出
print x,
print y,

# 不换行输出
print x,y


print "===============变量赋值============"
count = 100 #赋值整型变量
miles = 1000.0 #浮点型
name = "John" #字符串

print count
print miles
print name


print "++++++++++++++++字符串截取++++++++++++"
str = "Hello Python!"

print str             # 输出完整字符串
print str[0]          # 输出字符串中的第一个字符
print str[2:5]        # 输出字符串中第三个至第六个之间的字符串
print str[2:]         # 输出从第三个字符开始的字符串
print str * 2         # 输出字符串两次
print str + "TEST"    # 输出连接的字符串


print "------------------列表截取---------------"
list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print list             # 输出完整列表
print list[0]          # 输出列表的第一个元素
print list[1:3]        # 输出第二个至第三个元素
print list[2:]         # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2     # 输出列表两次
print list + tinylist  # 打印组合的列表
list[1] = 1000
print list

print "------------------元组截取---------------"
tuple = ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')

print tuple                 # 输出完整元组
print tuple[0]              # 输出元组的第一个元素
print tuple[1:3]            # 输出第二个至第四个（不包含）的元素
print tuple[2:]             # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2         # 输出元组两次
print tuple + tinytuple     # 打印组合的元组
#tuple[2] = 1000            # 会报错，不能修改


print "#################Python字典###############"
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print dict['one']          # 输出键为'one' 的值
print dict[2]              # 输出键为 2 的值
print tinydict             # 输出完整的字典
print tinydict.keys()      # 输出所有键
print tinydict.values()    # 输出所有值

#pyth内置函数
#abs() 函数返回数字的绝对值。
print "==============abs() 函数=============="
print "abs(-45) : ", abs(-45)
print "abs(100.12) : ", abs(100.12)
print "abs(119L) : ", abs(119L)

