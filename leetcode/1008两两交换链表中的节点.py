"""
本题的思路是先虚拟一个新的头节点，连接现有头节点，令p指向头节点，q指向头节点后面的节点，
然后连接方式我下图所示，按照①，②，③的顺序连接，①X，②X，③X代表①，②，③连接时断开的。
https://img-blog.csdn.net/20171229013819061?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQveGlhb2xpbmdfMDAwNjY2/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center
"""
# Definition for singly-linked list.
# -*- coding: utf-8 -*
class ListNode(object):
	def __init__(self, val, p=None):
		self.val = val
		self.next = p

class Solution():
	def swapPairs(self, head):
		if head == None or head.next == None:
			return head
		else:
			start = ListNode(0)
			start.next = head
			p = start
			q = start.next
			while q != None and q.next != None:
				p.next = q.next
				q.next = p.next.next
				p.next.next = q
				p = q
				q = q.next
			return start.next


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

if __name__=='__main__':
	l = '1,2,3,4'
	l_node=stringToListNode(l)
	p = Solution().swapPairs(l_node)
	out = listNodeToString(p)
	print(out)