# -*- coding: utf-8 -*-
# @Time    : 2019/3/14 16:42
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
class Solution:
	def searchMatrix(self, matrix: [[int]], target: int) -> bool:
		if not matrix:
			return False
		m=len(matrix)
		n=len(matrix[0])

		if n!=0:
			if target<matrix[0][0]:
				return False
			if target>matrix[m-1][n-1]:
				return False

			for i in range(m):
				for j in range(n):
					if matrix[i][j]==target:
						return True
			return False
		else:
			return False

if __name__=='__main__':
	print(Solution().searchMatrix(matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,50]],target=13))