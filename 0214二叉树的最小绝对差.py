# -*- coding: utf-8 -*-
# @Time    : 2019/2/15 18:01
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm

class Solution(object):
	def getMinimumDifference(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		result = []

		def midsearch(root):
			if root == None:
				return
			if root.left:
				midsearch(root.left)
			result.append(root.val)
			if root.right:
				midsearch(root.right)

		midsearch(root)

		if len(result) < 2:
			return 0
		for i in range(1, len(result)):
			result[i - 1] = abs(result[i] - result[i - 1])
		return min(result[:-1])
