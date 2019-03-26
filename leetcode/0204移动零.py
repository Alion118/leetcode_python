# -*- coding: utf-8 -*-
# @Time    : 2019/2/4 15:29
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
class Solution:
	def moveZeroes(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		j = 0
		numsSize=len(nums)
		for i in range(numsSize):
			if nums[i] != 0:
				nums[j] = nums[i]
				j += 1
		while j < numsSize:
			nums[j] = 0
			j +=1
		return nums
if __name__=='__main__':
	print(Solution().moveZeroes([0,1,0,3,12]))