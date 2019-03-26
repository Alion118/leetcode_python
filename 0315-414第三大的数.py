# -*- coding: utf-8 -*-
# @Time    : 2019/3/15 15:32
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
class Solution:
	def thirdMax(self, nums: [int]) -> int:
		s=list(set(nums))
		s.sort(reverse=True)
		if len(s)>2:
			return s[2]
		else:
			return s[0]
print(Solution().thirdMax(nums=[2,2,3,1]))