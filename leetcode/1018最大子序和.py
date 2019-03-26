# -*- coding: utf-8 -*-
# @Time    : 2018/10/18 21:43
class Solution:
	def maxSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		l=len(nums)
		i=0
		sum=0
		MaxSum=nums[0]
		while i<l:
			sum+=nums[i]
			if sum>MaxSum:
				MaxSum=sum
			if sum<0:
				sum=0
			i+=1
		return MaxSum


if __name__=='__main__':
	# nums=[-2,1,-3,4,-1,2,1,-5,4]
	nums = [-2, -3, -1,  -5]
	print(Solution().maxSubArray(nums))

#   转态转移方程：MaxSum[i] = Max{ MaxSum[i-1] + A[i], A[i]};
