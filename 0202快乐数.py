# -*- coding: utf-8 -*-
# @Time    : 2019/2/2 20:08
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
class Solution:
	def isHappy(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		if n==1:
			return True
		elif n in [4,16,37,58,89,145,42,20]:
			return False
		else:
			num=[int(i)**2 for i in list(str(n))]
			new=sum(num)
			return self.isHappy(new)
if __name__=='__main__':
	print(Solution().isHappy(19))