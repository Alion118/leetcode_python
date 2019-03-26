# -*- coding: utf-8 -*-
# @Time    : 2019/1/31 11:05
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
class Solution:
	def plusOne(self, digits):
		"""
		:type digits: List[int]
		:rtype: List[int]
		"""
		l=len(digits)
		num=0
		for i in range(l):
			num=num+int(digits[i])*10**(l-i-1)
		lst=list(str(num+1))
		out=[int(i) for i in lst]
		return out


if __name__=='__main__':
	print(Solution().plusOne([2,3,4,9]))