# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 15:48
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
nums=[i for i in map(int,list(input()))]

max_list=[]
temp=[nums[0]]
for i in range(len(nums)-1):
	if nums[i+1]!=nums[i]:
		temp.append(nums[i+1])
	else:
		if len(temp)>1:
			max_list.append(temp)
		temp = [nums[i + 1]]
max_list.append(temp)
print(max([len(i) for i in max_list]))