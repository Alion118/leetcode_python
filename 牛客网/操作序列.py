# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 16:05
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
n=int(input())
nums=list(input().split())
c=nums[0:n:2]
d=nums[1:n:2]
c.reverse()
c.extend(d)
if n%2==0:
    c.reverse()
print(' '.join(c))