# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 22:06
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
import heapq

class KthLargest:
	def __init__(self, k, nums):
		"""
		:type k: int
		:type nums: List[int]
		"""
		self.k = k
		self.heap = []
		for n in nums:
			self.add(n)

	def add(self, val):
		"""
		:type val: int
		:rtype: int
		"""
		if len(self.heap) < self.k:
			heapq.heappush(self.heap, val)
		elif self.heap[0] < val:
			heapq.heappop(self.heap)
			heapq.heappush(self.heap, val)
		return self.heap[0]



		# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(k=2, nums=[3,2,5])
print(obj.add(4))

# 堆是一种特殊的数据结构，它的通常的表示是它的根结点的值最大或者是最小。
# python中heapq的使用
# 列出一些常见的用法：
# heap = []#建立一个常见的堆
# heappush(heap,item)#往堆中插入一条新的值
# item = heappop(heap)#弹出最小的值