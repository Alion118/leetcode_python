# -*- coding: utf-8 -*-
# @Time    : 2019/1/23 22:02
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
class Solution:
	def isPalindrome(self, x):
		"""
		:type x: int
		:rtype: bool
		"""
		lst_r=list(str(x))
		lst=lst_r.copy()
		lst_r.reverse()
		return(lst_r==lst)

if __name__=='__main__':
	print(Solution().isPalindrome(12321))