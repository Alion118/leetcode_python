# -*- coding: utf-8 -*-
# @Time    : 2019/2/10 14:34
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
class MinStack(object):
	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.s=[]

	def push(self, x):
		"""
		:type x: int
		:rtype: void
		"""
		if len(self.s) == 0:
			self.s.append(x)
			self.s.append(x)
		else:
			tmp=self.s[-1]
			self.s.append(x)
			d=x if x<tmp else tmp
			self.s.append(d)

	def pop(self):
		"""
		:rtype: void
		"""
		self.s.pop()
		self.s.pop()

	def top(self):
		"""
		:rtype: int
		"""
		return self.s[-2]

	def getMin(self):
		"""
		:rtype: int
		"""
		return self.s[-1]


		# Your MinStack object will be instantiated and called as such:
		# obj = MinStack()
		# obj.push(x)
		# obj.pop()
		# param_3 = obj.top()
		# param_4 = obj.getMin()
if __name__=='__main__':
	obj = MinStack()
	obj.push(2)
	obj.push(3)
	obj.push(1)
	obj.push(4)
	param_3 = obj.top()
	param_4 = obj.getMin()
	print(param_3)
	print(param_4)