# -*- coding: utf-8 -*-
# @Time    : 2019/3/24 18:45
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
class Solution:
	def beautifulArray(self, N: int) -> [int]:
		nums=[i+1 for i in range(N)]

		return self.part(nums)
	def part(self,nums):
		if len(nums)<=2:
			return nums
		left=[]
		right=[]
		for i in range(0,len(nums),2):
			left.append(nums[i])
			if i+1<len(nums):
				right.append(nums[i+1])
		return self.part(left)+self.part(right)

print(Solution().beautifulArray(7))