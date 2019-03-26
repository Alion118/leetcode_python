# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 20:10
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
# Definition for singly-linked list.
import random
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def __init__(self, head):
		"""
		@param head The linked list's head.
		Note that the head is guaranteed to be not null, so it contains at least one node.
		:type head: ListNode
		"""
		p=head()
		self.value=[]
		while p:
			self.value.append(p.val)
			p=p.next

	def getRandom(self):
		"""
		Returns a random node's value.
		:rtype: int
		"""
		idx=random.randint(0,len(self.value)-1)
		return self.value[idx]



		# Your Solution object will be instantiated and called as such:
		# obj = Solution(head)
		# param_1 = obj.getRandom()