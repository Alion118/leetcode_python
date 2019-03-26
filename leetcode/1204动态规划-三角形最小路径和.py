# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 20:27
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm


class Solution(object):
	def minimumTotal(self, triangle):
		"""
		:type triangle: List[List[int]]
		:rtype: int
		"""
		n = len(triangle)
		dp = triangle[-1]
		for i in range(n - 2, -1, -1):
			for j in range(i + 1): # 从倒数第二层开始往上，变化数字，dp[-1]一开始就用不到了
				dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
		return dp[0]

if __name__=='__main__':
	lst0=[[2],[3,4],[6,5,7],[4,1,8,3]]
	lst=[[-1],[2,3],[1,-1,-3]]
	print(Solution().minimumTotal(lst))