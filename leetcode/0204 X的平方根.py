# -*- coding: utf-8 -*-
# @Time    : 2019/2/4 14:46
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
class Solution:
	def mySqrt1(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		end=x
		mid=x//2
		while(end>=mid):
			if mid**2>x:
				end=mid-1
				mid=end//2
			else:
				if (mid+1)**2>x:
					return mid
					#break
				else:
					mid=mid+1

	def mySqrt(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		if x <= 1:
			return x
		r = x
		while r > x / r:
			r = (r + x / r) // 2
		return int(r)

if __name__=='__main__':
	print(Solution().mySqrt(8))