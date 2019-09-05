#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
localtime = time.asctime(time.localtime(time.time()));
print "本地时间为：", localtime

#格式化日期
print "++++++++++++++格式化日期++++++++++++"
# 格式化成2016-03-20 11:45:39形式
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# 格式化成Sat Mar 28 22:24:24 2016形式
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))



#获取某月日历
print "++++++++++++++获取某月日历++++++++++++"
import calendar
cal = calendar.month(2019,9)
print "以下输出2019年9月份的日历："
print cal


print "++++++++++++++函数调用+++++++++++++"
#定义函数
def printme(str):
    "打印任何传入的字符"
    print str;
    return;
#调用函数
printme("我要调用用户自定义函数");
printme("再次调用同一个函数");


# 可写函数说明
print "===============数据列表=============="
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1,2,3,4]);
    print "函数内取值：",mylist
    return
#调用changeme函数
mylist = [10,11,12];
changeme(mylist);
print "函数外取值：",mylist

#可写函数说明
print "===============个人信息（传参）============="
def personinfo (name,age):
    print "Name:",name;
    print "Age:",age;
    return;
#调用函数
personinfo("lhr","18")


# 可写函数说明
print "===============个人信息（固定参数）============="
def printinfo(name, age=35):
    "打印任何传入的字符串"
    print "Name: ", name;
    print "Age ", age;
    return;


# 调用printinfo函数
printinfo(age=50, name="miki");
printinfo(name="miki");

print "===============不定长参数============="
#可写函数
def praminfo(arg1,*vartuple):
    "打印任何输入参数"
    print "输出："
    print arg1
    for var in vartuple:
        print var
    return ;
#调用函数
praminfo(10);
praminfo(70,60,50);


#匿名函数
print "+++++++++++++匿名函数+++++++++++"
sum = lambda agr1, agr2: agr1+agr2;

#调用sum函数
print "相加后的值为：",sum(10,20);
print "相加后的值为：",sum(20,20);


#全局变量和局部变量
print "++++++++++++全局变量和局部变量+++++++++++"
total = 0;  # 这是一个全局变量


# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2;  # total在这里是局部变量.
    print "函数内是局部变量 : ", total
    return total;

# 调用sum函数
sum(10, 20);
print "函数外是全局变量 : ", total

#使用global设置全局变量
print "++++++++++++++++global设置全局变量+++++++++++++++"
Money = 2000
def AddMoney():
    # 想改正代码就取消以下注释:
    global Money
    Money = Money + 1


print "调用方法前：",Money
AddMoney()
print "调用方法后：",Money