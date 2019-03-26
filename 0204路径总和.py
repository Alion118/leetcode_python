# -*- coding: utf-8 -*-
# @Time    : 2019/2/4 14:17
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def hasPathSum(self, root, sum):
		"""
		:type root: TreeNode
		:type sum: int
		:rtype: bool
		"""
		return sum in self.binaryTreePaths(root)

	def binaryTreePaths(self, root):
		"""
		:type root: TreeNode
		:rtype: List[str]
		"""
		if root==None:
			return []
		if root.right==None and root.left==None:
			return [root.val]
		paths=self.binaryTreePaths(root.left)+self.binaryTreePaths(root.right)
		for index in range(len(paths)):
			paths[index]=root.val+paths[index]
		return paths

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
if __name__=='__main__':
	p=listToTreeNode([5,4,8,11,'null',13,4,7,2,'null',1])
	print(Solution().binaryTreePaths(p))
	print(Solution().hasPathSum(p,22))