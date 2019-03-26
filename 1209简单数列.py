# -*- coding: utf-8 -*-
# @Time    : 2018/12/9 19:18
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
class Solution:
	def isMonotonic(self, A):
		"""
		:type A: List[int]
		:rtype: bool
		"""
		flag=True
		if len(A)>1:
			d=[]
			for i in range(len(A)-1):
				if (A[i+1]-A[i])!=0:
					d.append((A[i+1]-A[i]))
			for i in range(len(d)-1):
				if d[i+1]*d[i]<0:
					flag=False
		return flag



if __name__=='__main__':
	A=[11,11,9,4,3,3,3,1,-1,-1,3,3,3,5,5,5]
	print(Solution().isMonotonic(A))