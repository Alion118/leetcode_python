# -*- coding: utf-8 -*-
# @Time    : 2019/2/10 18:57
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
class MyQueue(object):
	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.input = []
		self.output = []

	def push(self, x):
		"""
		Push element x to the back of queue.
		:type x: int
		:rtype: void
		"""
		self.input.append(x)

	def pop(self):
		"""
		Removes the element from in front of queue and returns that element.
		:rtype: int
		"""
		if not self.output:
			while self.input:
				self.output.append(self.input.pop())
		return self.output.pop()

	def peek(self):
		"""
		Get the front element.
		:rtype: int
		"""
		if not self.output:
			while self.input:
				self.output.append(self.input.pop())
		return self.output[-1]

	def empty(self):
		"""
		Returns whether the queue is empty.
		:rtype: bool
		"""
		return len(self.input) == 0 and len(self.output) == 0



		# Your MyQueue object will be instantiated and called as such:
if __name__=='__main__':
	obj = MyQueue()
	obj.push(2)
	obj.push(1)
	obj.push(3)
	param_2 = obj.pop()
	param_3 = obj.peek()
	param_4 = obj.empty()