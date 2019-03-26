# -*- coding: utf-8 -*-
# @Time    : 2019/2/10 21:55
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
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


# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def deleteDuplicates(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		tmp = ListNode(0)
		tmp.next = head
		while head:
			while head.next and head.next.val == head.val:
				head.next = head.next.next
			head = head.next
		return tmp.next


s=stringToListNode('1,1,2')
print(listNodeToString(Solution().deleteDuplicates(s)))

