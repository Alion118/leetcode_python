# -*- coding: utf-8 -*-
# @Time    : 2019/2/1 16:39
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
class TreeNode():
	def __init__(self,x):
		self.val=x
		self.left=None
		self.right=None


class Solution(object):
	def maxDepth(self, root):
		if root == None:
			return 0
		len_left = self.maxDepth(root.left)
		len_right = self.maxDepth(root.right)
		if len_left == -1 or len_right == -1:
			return -1
		if abs(len_left - len_right) <= 1:
			return max(len_right, len_left) + 1
		else:
			return -1

	def isBalanced(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		if root == None:
			return True
		if self.maxDepth(root) == -1:
			return False
		else:
			return True

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
	root=stringToTreeNode('1,2,2,3,3,null,null,4,4')
	print(Solution().isBalanced(root))