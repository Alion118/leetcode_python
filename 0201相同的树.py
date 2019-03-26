# -*- coding: utf-8 -*-
# @Time    : 2019/2/1 16:00
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def isSameTree(self, p, q):
		"""
		:type p: TreeNode
		:type q: TreeNode
		:rtype: bool
		"""
		if not p and not q:
			return True
		elif p is not None and q is not None:
			if p.val == q.val:
				return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
			else:
				return False
		else:
			return False

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
if __name__=='__main__':
	p=stringToTreeNode('1,2,1')
	q=stringToTreeNode('1,1,2')
	print(Solution().isSameTree(p,q))
