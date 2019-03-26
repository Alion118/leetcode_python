# -*- coding: utf-8 -*-
# @Time    : 2018/10/8 15:27
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @File    : 第K个排列.py
# @Software: PyCharm
import math
class Solution:
	def jiecheng(self,n):
		if n==0:
			return 1
		else:
			return n*Solution.jiecheng(self,n-1)

	def getPermutation(self, n, k):
		"""
		:type n: int
		:type k: int
		:rtype: str
		"""
		nums=[]
		k_value=[]
		ks_value=''
		for i in range(n):
			nums.append(i+1)

		while len(nums)>0:
			n1=int((k-0.1)/Solution.jiecheng(self,n-1))  # 第i位数字的index
			k_value.append(nums[n1])
			ks_value=ks_value+str(nums[n1])
			nums.pop(n1)
			k=k-Solution.jiecheng(self,n-1)*n1
			n=n-1

		return ks_value

if __name__=='__main__':
	s=Solution()
	n=3
	k=3
	# print(s.jiecheng(0))
	print(s.getPermutation(n,k))