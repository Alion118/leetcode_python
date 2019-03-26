# -*- coding: utf-8 -*-
# @Time    : 2019/3/14 15:41
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
import numpy as np
class Solution:
	def setZeroes(self, matrix: [[int]]) -> None:
		"""
		Do not return anything, modify matrix in-place instead.
		"""
		zero_index = []
		if not matrix:
			return
		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				if matrix[i][j] == 0:
					zero_index.append([i, j])
		if zero_index:
			for index in zero_index:
				matrix[index[0]] = [0] * len(matrix[0])
				for i in range(len(matrix)):
					matrix[i][index[1]]=0
		print(matrix)


if __name__ == '__main__':
	Solution().setZeroes(matrix=[[1, 1, 1], [1, 0, 1], [1, 1, 1]])
