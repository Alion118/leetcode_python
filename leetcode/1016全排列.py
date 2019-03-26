# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 19:13

class Solution(object):
	def permute(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		# print 'nums', nums
		if len(nums) <= 1:
			return [nums]
		ans = []
		for i, num in enumerate(nums):
			n = nums[:i] + nums[i+1:]
			for temp_list in self.permute(n):
				ans.append([num] + temp_list)
		return ans






if __name__=='__main__':
	lst=[1,2,3]
	print(Solution().permute(lst))