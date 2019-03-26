# -*- coding: utf-8 -*-
# @Time    : 2019/1/23 21:24
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
from functools import lru_cache
class Solution:
	@lru_cache(10**8)
	def climbStairs(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n==1:
			return 1
		elif n==2:
			return 2
		else:
			n1=self.climbStairs(n-1)
			n2=self.climbStairs(n-2)
			return n1+n2




if __name__=='__main__':
	n=38
	print(Solution().climbStairs(n))