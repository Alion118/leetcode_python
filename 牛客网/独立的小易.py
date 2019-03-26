# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 16:26
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
lst=[i for i in map(int,input().split())]
x=lst[0]
f=lst[1]
d=lst[2]
p=lst[3]
max_day=min(f,d//x)
if d-f*x>0:
	if max_day==f:
		max_day+=(d-f*x)//(p+x)
print(max_day)