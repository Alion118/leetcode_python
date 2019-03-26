# -*- coding: utf-8 -*-
# @Time    : 2019/2/9 22:16
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
class Solution:
	def findContentChildren(self, g, s):
		"""
		:type g: List[int]
		:type s: List[int]
		:rtype: int
		"""
		g.sort() #先事先排序
		s.sort()
		i=j=res=0
		while i<len(g) and j<len(s):
			if g[i]<=s[j]:
				res+=1
				i+=1
			j+=1
		return res

if __name__=='__main__':
	print(Solution().findContentChildren([1,2],[1,1,2,3]))