# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 22:21
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
class Solution:
	def fizzBuzz(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		l=[]
		i=1
		while i<=n:
			if i%5==0 and i%3==0:
				l.append("FizzBuzz")
			elif i%5==0:
				l.append("Buzz")
			elif i%3==0:
				l.append("Fizz")
			else:
				l.append(str(i))
			i+=1
		return l
if __name__=='__main__':
	n=15
	print(Solution().fizzBuzz(n))