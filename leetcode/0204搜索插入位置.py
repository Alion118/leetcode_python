# -*- coding: utf-8 -*-
# @Time    : 2019/2/4 14:22
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
class Solution:
	def searchInsert(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		if target in nums:
			return nums.index(target)
		else:
			nums.append(target)
			nums.sort()
			return nums.index(target)
if __name__=='__main__':
	print(Solution().searchInsert([1,3,5,6],5))