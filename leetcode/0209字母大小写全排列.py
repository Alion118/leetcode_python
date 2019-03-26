# -*- coding: utf-8 -*-
# @Time    : 2019/2/10 15:33
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
import itertools
class Solution(object):
	def letterCasePermutation(self, S):
		"""
		:type S: str
		:rtype: List[str]
		"""
		L=[[i.upper(),i.lower()] if i.isalpha() else i for i in S]
		return [''.join(i) for i in itertools.product(*L)]
	#product(A, B)函数，返回A、B中的元素的笛卡尔积的元组

if __name__=='__main__':
	s='a1b2'
	print(Solution().letterCasePermutation(s))