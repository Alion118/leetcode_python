# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 16:36
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
import copy
class Solution:
	def imageSmoother(self, M):
		"""
		:type M: List[List[int]]
		:rtype: List[List[int]]
		"""
		m=len(M)
		n=len(M[0])
		smo_M=[]

		for i in range(m):
			smo_M.append([])
			for j in range(n):
				value = 0
				num = 0
				for ii in range(i-1,i+2):
					for jj in range(j-1,j+2):
						if ii>=0 and ii<m and jj>=0 and jj<n:
							value+=M[ii][jj]
							num+=1
				smo_M[i].append(int(value/num))
		return smo_M
	def fun(self,M): # 深拷贝，全部拷贝，M.copy()浅拷贝，只拷贝一层
		M1=copy.deepcopy(M)
		M1[0][0]=0
		print(M)




if __name__=='__main__':
	M=[[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
	print(Solution().imageSmoother(M))
	# Solution().fun(M)
