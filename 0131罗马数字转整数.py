# -*- coding: utf-8 -*-
# @Time    : 2019/1/31 11:24
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
class Solution:
	def romanToInt(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		di={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
		lst=list(s)
		num=0
		i=0
		if len(lst)==1:
			return di[s]
		else:
			while(i<len(lst)-1):
				if di[lst[i]]>=di[lst[i+1]]:
					num=num+di[lst[i]]
					i+=1
				else:
					num=num+di[lst[i+1]]-di[lst[i]]
					i+=2
				if i == len(lst) - 1:
					num=num+di[lst[i]]
				#print()
			return num


if __name__=='__main__':
	print(Solution().romanToInt("D"))