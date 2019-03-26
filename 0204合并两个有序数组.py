# -*- coding: utf-8 -*-
# @Time    : 2019/2/4 15:11
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
class Solution:
	def merge(self, nums1, m, nums2, n):
		"""
		:type nums1: List[int]
		:type m: int
		:type nums2: List[int]
		:type n: int
		:rtype: void Do not return anything, modify nums1 in-place instead.
		"""
		nums1[m:] = nums2
		nums1.sort()
		return m
if __name__=='__main__':
	nums1=[1,2,3,0,0,0]
	m=3
	nums2=[2,5,6]
	n=3
	print(Solution().merge(nums1,m,nums2,n))