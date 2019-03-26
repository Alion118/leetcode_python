# -*- coding: utf-8 -*-
# @Time    : 2019/3/13 22:08
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
class Solution:
	def minDistance(self, word1: str, word2: str) -> int:
		if word1==None and word2==None:
			return 0
		l1=len(word1)
		l2=len(word2)
		if l1==0:
			return l2
		if l2==0:
			return l1
		dp=[[0 for i in range(l2+1)] for i in range(l1+1)]
		for i in range(l1+1):
			dp[i][0]=i
		for j in range(l2+1):
			dp[0][j]=j
		for i in range(1,l1+1):
			for j in range(1,l2+1):
				if word1[i-1]==word2[j-1]:
					dp[i][j]=dp[i-1][j-1]
				else:
					dp[i][j]=min(min(dp[i-1][j],dp[i-1][j-1]),dp[i][j-1])+1
		return dp[l1][l2]

if __name__=='__main__':
	print(Solution().minDistance('horse','ros'))