# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 21:44
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
class Solution:
	def containsDuplicate(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		return len(set(nums))!=len(nums)


if __name__=='__main__':
	l=[1,2,4,2,5,7]
	print(set(l))
	print(Solution().containsDuplicate(l))