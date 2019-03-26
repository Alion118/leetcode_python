# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 23:08
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
# import itertools
# s=input()
# all=[]
# for i in itertools.permutations(s,len(s)):
# 	all.append(''.join(i))
# strs=list(set(all))
# color_lst=[]
# for si in strs:
# 	different_num=0
# 	for i in range(len(si)-1):
# 		if si[i]!=si[i+1]:
# 			different_num+=1
# 	color_lst.append(different_num)
#
# print(color_lst.count(1)+color_lst.count(0))
s = list(input())
print(set(s))
discnt = len(set(s))
if discnt>2:
    print(0)
elif discnt==1:
    print(1)
elif discnt==2:
    print(2)