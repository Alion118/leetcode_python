# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 15:40
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
nums=[i for i in map(int,input().split())]
nums.sort()
diff=nums[1]-nums[0]
flag='Possible'
for i in  range(1,len(nums)-1):
	if nums[i+1]-nums[i]!=diff:
		flag='Impossible'
		break

print(flag)



