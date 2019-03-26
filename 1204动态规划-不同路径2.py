# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 22:08
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm

class Solution(object):
	def uniquePathsWithObstacles(self, obstacleGrid):
		for i in range(len(obstacleGrid)):
			for j in range(len(obstacleGrid[0])):
				if i==0 and j==0:# 第一个数
					obstacleGrid[i][j] = 1 - obstacleGrid[i][j]
				elif i == 0:# 第一行
					obstacleGrid[i][j] = obstacleGrid[i][j-1] * (1 - obstacleGrid[i][j])
				elif j == 0:#第一列
					obstacleGrid[i][j] = obstacleGrid[i-1][j] * (1 - obstacleGrid[i][j])
				else: #其他所有情况
					obstacleGrid[i][j] = (obstacleGrid[i][j-1]+obstacleGrid[i-1][j])*(1 - obstacleGrid[i][j])
		return obstacleGrid[-1][-1]
# 给所有位置乘了个1 - obstacleGrid[i][j]。如果原来位置是1（拦住了），就乘个0，说明没有路
		return memo[n - 1][m - 1]

if __name__=='__main__':
	s=[ [0,0,0], [0,1,0], [0,0,0] ]
	s1=[[0,0]]
	print(Solution().uniquePathsWithObstacles(s))