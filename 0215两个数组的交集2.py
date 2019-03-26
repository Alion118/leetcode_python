# -*- coding: utf-8 -*-
# @Time    : 2019/2/15 16:33
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
class Solution:
	def intersect(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: List[int]
		"""
		inter=set(nums1)&set(nums2)
		l=[]
		for i in inter:
			l+=[i]*min(nums1.count(i),nums2.count(i))
		return l