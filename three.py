#!/usr/bin/python
# -*- coding: UTF-8 -*-
print "+++++++++++++++++++++条件语句++++++++++++++++++"

num = 5
if num == 3:  # 判断num的值
    print 'boss'
elif num == 2:
    print 'user'
elif num == 1:
    print 'worker'
elif num < 0:  # 值小于零时输出
    print 'error'
else:
    print 'roadman'  # 条件均不成立时输出



num = 9
if num >= 0 and num <= 10:  # 判断值是否在0~10之间
    print 'hello'
# 输出结果: hello

num = 10
if num < 0 or num > 10:  # 判断值是否在小于0或大于10
    print 'hello'
else:
    print 'undefine'
# 输出结果: undefine

num = 8
# 判断值是否在0~5或者10~15之间
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
    print 'hello'
else:
    print 'undefine'
# 输出结果: undefine



#八皇后问题 （循环递归法）
print "++++++++++++++++递归循环++++++++++++++++++"
BOARD_SIZE = 8

def under_attack(col, queens):
   left = right = col
   for r, c in reversed(queens):
 #左右有冲突的位置的列号
       left, right = left - 1, right + 1

       if c in (left, col, right):
           return True
   return False

def solve(n):
   if n == 0:
       return [[]]

   smaller_solutions = solve(n - 1)

   return [solution+[(n,i+1)]
       for i in xrange(BOARD_SIZE)
           for solution in smaller_solutions
               if not under_attack(i+1, solution)]
for answer in solve(BOARD_SIZE):
   print answer


print "+++++++++++++++++++while 循环++++++++++++++++++"
count = 0
while (count < 9):
    print 'The count is:', count
    count = count + 1

print "Good bye!"

# continue 和 break 用法
print "=================continue 和 break==============="
i = 1
while i < 10:
    i += 1
    if i % 2 > 0:  # 非双数时跳过输出
        continue
    print i  # 输出双数2、4、6、8、10

i = 1
while 1:  # 循环条件为1必定成立
    print i  # 输出1~10
    i += 1
    if i > 10:  # 当i大于10时跳出循环
        break
