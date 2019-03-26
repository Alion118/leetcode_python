# -*- coding: utf-8 -*-
# @Time    : 2019/2/10 15:03
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
class MyStack():
	def __init__(self):
		self.l=[]
	def push(self,x):
		self.l.append(x)
	def pop(self):
		return self.l.pop()
	def top(self):
		return self.l[-1]
	def empty(self):
		return self.l==[]


if __name__=='__main__':
	obj = MyStack()
	obj.push(2)
	obj.push(3)
	obj.push(2)
	param_2 = obj.pop()
	param_3 = obj.top()
	param_4 = obj.empty()