# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 19:02
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
import numpy as np
def find_next_zero(lst1,loc1):
	zero_lst=np.argwhere(np.array(lst1[loc1:])==0)
	if zero_lst.size==1:
		index=loc1+zero_lst[0][0]
	else:
		index=loc1+zero_lst[1][0]
	return index

n=int(input())
nums=[i+1 for i in range(n)]

flag = [0]*n
print(nums[0], end=' ')
flag[0]=1

loc=0
while(flag.count(1)<n):
	i0=find_next_zero(flag,loc)
	print(nums[i0],end=' ')
	loc=i0
	flag[i0]=1
	if np.argwhere(np.array(flag)==0).size>0:
		l=np.argwhere(np.array(flag)==0)
		if l.size>1:
			if loc>l[-2][0]:
				loc=l[0][0]
		else:
			loc=l[0][0]







