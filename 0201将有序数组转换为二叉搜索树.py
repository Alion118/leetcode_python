# -*- coding: utf-8 -*-
# @Time    : 2019/2/1 16:33
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def sortedArrayToBST(self, nums):
		"""
		:type nums: List[int]
		:rtype: TreeNode
		"""
		if not nums:
			return None
		else:
			mid=len(nums)//2
			tn=TreeNode(nums[mid])
			nums1=nums[0:mid]
			nums2=nums[mid+1:len(nums)]
			tn.left=self.sortedArrayToBST(nums1)
			tn.right=self.sortedArrayToBST(nums2)
		return tn


if __name__=='__main__':
	print(Solution().sortedArrayToBST([-10,-3,0,5,9]))
