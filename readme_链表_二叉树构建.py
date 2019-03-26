# -*- coding: utf-8 -*-
# @Time    : 2018/10/8 22:04
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm


str1='1,2,3'
str_list=str1.split(',') #['1','2','3']
int_list=[int(x) for x in str_list]  #[1,2,3]

#1-----------从string构建二叉树、二叉树转成string输出------------
## 创建树节点
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

## str转二叉树
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

## 二叉树转str
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

## 测试
line1='1,3,2,5'
t1=stringToTreeNode(line1)
line2='2,1,3,null,4,null,7'
t2=stringToTreeNode(line2)



#2---------从string构建链表、链表转成string输出-----------------
## 创建链表节点
class ListNode(object):
	def __init__(self, val, p=None):
		self.val = val
		self.next = p

## str转链表
def stringToListNode(input):
	# Generate list from the input
	numbers = input.split(',')
	numbers = [int(x) for x in numbers]

	# Now convert that list into linked list
	dummyRoot = ListNode(0)
	ptr = dummyRoot
	for number in numbers:
		ptr.next = ListNode(number)
		ptr = ptr.next

	ptr = dummyRoot.next
	return ptr

## 链表转str
def listNodeToString(node):
	if not node:
		return "[]"

	result = ""
	while node:
		result += str(node.val) + ", "
		node = node.next
	return "[" + result[:-2] + "]"

## 测试
l = '1,2,3,4'
l_node=stringToListNode(l)
