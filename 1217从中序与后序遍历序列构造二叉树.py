# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 15:46
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class TreeNode:
	def __init__(self,x):
		self.val=x
		self.left=None
		self.right=None

class Solution(object):
	def buildTree(self, inorder, postorder):
		"""
		:type inorder: List[int]
		:type postorder: List[int]
		:rtype: TreeNode
		"""
		if not postorder:
			return None
		root = TreeNode(postorder[-1])
		n = inorder.index(root.val)
		root.left = self.buildTree(inorder[:n], postorder[:n])
		root.right = self.buildTree(inorder[n + 1:], postorder[n:-1])
		return root

if __name__=='__main__':
	inorder=[9,3,15,20,7]
	postorder=[9,15,7,20,3]
	print(Solution().buildTree(inorder,postorder))