# -*- coding: utf-8 -*-
# @Time    : 2019/1/21 19:37
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
class Solution:
	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		num=[]
		if len(nums)==0:
			return 0
		else:
			i=0
			for j in range(1,len(nums)):
				if nums[j]!=nums[i]:
					i += 1
					nums[i]=nums[j]
			return i+1


if __name__=='__main__':
	nums=[1,1,2]
	print(Solution().removeDuplicates(nums))