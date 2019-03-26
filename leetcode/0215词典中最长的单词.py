# -*- coding: utf-8 -*-
# @Time    : 2019/2/16 00:11
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
# encoding=utf-8
import numpy as np
import functools

class Solution(object):
	def string_cmp(self, s1, s2):
		if len(s1) < len(s2):
			return 1
		elif len(s1) > len(s2):
			return -1
		else:
			if s1 > s2:
				return 1
			elif s1 < s2:
				return -1
			return 0

	def longestWord(self, words):
		"""
		:type words: List[str]
		:rtype: str
		"""

		words.sort(key=functools.cmp_to_key(self.string_cmp))
		for item in words:
			top = len(item)
			flag = True
			while top > 0:
				if item[0:top] in words:
					top -= 1
					continue
				else:
					flag = False
					break
			if flag == True:
				return item
		return ''

print(Solution().longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"]))