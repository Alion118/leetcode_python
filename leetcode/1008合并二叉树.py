# -*- coding: utf-8 -*-
# @Time    : 2018/10/8 21:32
class TreeNode(object):  # 创建树节点
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):  # 递归算法
	def mergeTrees(self, t1, t2):
		if t1 and t2:
			root = TreeNode(t1.val + t2.val)
			root.left = self.mergeTrees(t1.left, t2.left)
			root.right = self.mergeTrees(t1.right, t2.right)
			return root
		else:
			return t1 or t2

#  ---leetcode自带---
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

def treeNodeToString(root):
	if not root:
		return "[]"
	output = ""
	queue = [root]
	current = 0
	while current != len(queue):
		node = queue[current]
		current = current + 1

		if not node:
			output += "null, "
			continue

		output += str(node.val) + ", "
		queue.append(node.left)
		queue.append(node.right)
	return "[" + output[:-2] + "]"

if __name__=='__main__':
	line1='1,3,2,5'
	t1=stringToTreeNode(line1)
	line2='2,1,3,null,4,null,7'
	t2=stringToTreeNode(line2)
	print(treeNodeToString(Solution().mergeTrees(t1,t2)))