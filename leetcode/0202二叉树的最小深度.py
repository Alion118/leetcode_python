# -*- coding: utf-8 -*-
# @Time    : 2019/2/2 21:00
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
	def minDepth(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if root==None:
			return 0
		else:
			left=self.minDepth(root.left)
			right= self.minDepth(root.right)
			return 1+min(left,right) if left and right else 1+left+right

if __name__=='__main__':

	print(Solution().minDepth(listToTreeNode([1,2,3,'null','null',5,7])))