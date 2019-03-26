# -*- coding: utf-8 -*-
# @Time    : 2018/12/5 21:40
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm


#Posdp[i] = max(nums[i], max(nums[i] * Posdp[i - 1], nums[i] * Negdp[i - 1]));
#Negdp[i] = min(nums[i], min(nums[i] * Posdp[i - 1], nums[i] * Negdp[i - 1]));
# 由于乘积时会负负得正，所以需要记录一个正的最大值和一个负的最小值。
#
# 状态Posdp[i]：表示以第i个元素为结尾的子序列的最大乘积
#
# 状态Negdp[i]: 表示第i个元素为结尾的子序列的最小乘积
class Solution:
	def maxProduct(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		n =len(nums)
		Posdp=[0]*(n+1)
		Negdp=[0]*(n+1)
		ans = nums[0]
		Posdp[0] = nums[0]
		Negdp[0] = nums[0]
		for i in range(1,n):
			Posdp[i] = max( nums[i], max( nums[i] * Posdp[i-1], nums[i] * Negdp[i-1] ) )
			Negdp[i] = min( nums[i], min( nums[i] * Posdp[i-1], nums[i] * Negdp[i-1] ) )
			ans = max( ans, Posdp[i] )
		return ans

if __name__=='__main__':
	nums=[-2,0,-1]
	print(Solution().maxProduct(nums))