# -*- coding: utf-8 -*-
# @Time    : 2019/3/25 17:06
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution(object):
	def rightSideView(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		if root == None:
			return []
		stack = [root]
		res = []
		while stack != []:
			new = []
			for i in stack:
				if i.left:
					new.append(i.left)
				if i.right:
					new.append(i.right)
			res.append(stack[-1].val)
			stack = new
		return res



def stringToTreeNode(input):
	input = input.strip()
	# input = input[1:-1]
	if not input:
		return None

	inputValues = [s.strip() for s in input.split(',')]
	root = TreeNode(int(inputValues[0]))
	nodeQueue = [root]
	front = 0
	index = 1
	while index < len(inputValues):
		node = nodeQueue[front]
		front = front + 1

		item = inputValues[index]
		index = index + 1
		if item != "null":
			leftNumber = int(item)
			node.left = TreeNode(leftNumber)
			nodeQueue.append(node.left)

		if index >= len(inputValues):
			break

		item = inputValues[index]
		index = index + 1
		if item != "null":
			rightNumber = int(item)
			node.right = TreeNode(rightNumber)
			nodeQueue.append(node.right)
	return root


print(Solution().rightSideView(stringToTreeNode('6,1,null,null,3,2,5,null,null,4')))
