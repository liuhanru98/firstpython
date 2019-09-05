#!/usr/bin/python
# -*- coding: UTF-8 -*-

#定义父类
class Parent:
    parentAttr = 100
    def __init__(self):
        print "调用父类构造函数"

    def parentMethod(self):
        print "调用父类方法"

    def setAtrr(self, attr):
        Parent.parentAttr = attr

    def getAtrr(self):
        print "父类属性：", Parent.parentAttr

    def myMethod(self):
        print "调用父类方法"

#定义子类
class Child(Parent):
    def __init__(self):
        print "调用子类的构造函数"

    def childMethod(self):
        print "调用子类方法"
    def myMethod(self):
        print "调用子类方法"

c = Child()        #实例化子类
c.childMethod();   #调用子类的方法
c.parentMethod()   #调用父类的方法
c.setAtrr(200)     #再次调用父类的方法 - 设置属性值
c.getAtrr()        #再次调用父类的方法 - 获取属性值
c.myMethod()       #方法重写
