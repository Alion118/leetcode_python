# -*- coding: utf-8 -*-
# @Time    : 2019/2/10 21:11
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def less(self, a,b):
		return a if a.val<b.val else b
	def mergeTwoLists(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		l3=ListNode(0)
		rl3=l3
		while l1 or l2:
			if not l1 or not l2: #为空链表
				l3.next=l1 if l1 else l2
				break

			l3.next=self.less(l1,l2)
			if l3.next==l1:
				l1= l1.next
			else :
				l2=l2.next
			l3=l3.next
		return rl3.next

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
def listNodeToString(node):
	if not node:
		return "[]"

	result = ""
	while node:
		result += str(node.val) + ", "
		node = node.next
	return "[" + result[:-2] + "]"

input1=stringToListNode('1,2,4')
input2=stringToListNode('1,3,4')
print(listNodeToString(Solution().mergeTwoLists(input1,input2)))
