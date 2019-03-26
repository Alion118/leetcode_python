# -*- coding: utf-8 -*-
# @Time    : 2018/10/7 21:56
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @File    : 转换成小写字母.py
# @Software: PyCharm
class Solution:
	def toLowerCase1(self, str):
		"""
		:type str: str
		:rtype: str
		"""
		n=len(str)
		temp=list(str)
		for i in range(n):
			if temp[i]>='A' and temp[i]<='Z':
				x= ord(temp[i])+32
				temp[i]=chr(x)
		return ''.join(temp)
	def toLowerCase(self, str):
		return str.lower()
if __name__=='__main__':
	s=Solution()
	str1="abcdddEeeSFHbbbcd"
	print(s.toLowerCase(str1))