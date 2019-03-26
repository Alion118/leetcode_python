# -*- coding: utf-8 -*-
# @Time    : 2019/2/2 20:21
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
class TreeNode():
	def __init__(self,x):
		self.value=x
		self.left=None
		self.right=None
def listToTreeNode(input):
	if not input:
		return None

	root = TreeNode(int(input[0]))
	nodeQueue = [root]
	front = 0
	index = 1
	while index < len(input):
		node = nodeQueue[front]
		front = front + 1

		item = input[index]
		index = index + 1
		if item != "null":
			leftNumber = int(item)
			node.left = TreeNode(leftNumber)
			nodeQueue.append(node.left)

		if index >= len(input):
			break

		item = input[index]
		index = index + 1
		if item != "null":
			rightNumber = int(item)
			node.right = TreeNode(rightNumber)
			nodeQueue.append(node.right)
	return root
class Solution:
	def maxDepth(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		return 0 if root==None else max(self.maxDepth(root.right),self.maxDepth(root.left))+1
if __name__=='__main__':

	print(Solution().maxDepth(listToTreeNode([3,9,20,'null','null',15,7])))