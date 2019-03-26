# -*- coding: utf-8 -*-
# @Time    : 2019/1/31 11:58
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
class Solution:
	def shortest(self,strs):
		res = strs[0]
		for s in strs:
			if len(s)<len(res):
				res=s
		return res
	def longestCommonPrefix(self, strs):
		"""
		:type strs: List[str]
		:rtype: str
		"""
		if len(strs)==0:
			return ""
		elif len(strs)==1:
			return strs[0]
		else:
			res=self.shortest(strs)
			out=[""]*len(strs)
			for s in range(len(strs)):
				for i in range(len(res)):
					if res[i]==strs[s][i]:
						out[s]=out[s]+res[i]
					else:
						break
			return self.shortest(out)



if __name__=='__main__':
	print(Solution().longestCommonPrefix(["flower","flow","flight"]))