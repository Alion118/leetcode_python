# -*- coding: utf-8 -*-
# @Time    : 2018/10/7 21:40
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @File    : 较大分组的位置.py
# @Software: PyCharm
class Solution(object):
		def largeGroupPositions(self, S):
			""" 
			:type S: str 
			rtype: List[List[int]]
			"""
			return_list=[]
			i,j,n=0,0,len(S)
			while j<n-1:
				while j<n-1 and S[j+1]==S[j]:
					j += 1
				if j-i>=2:
					return_list.append([i,j])
				j=j+1
				i=j
			return return_list

"""
1.首先构建一个保存较大分组的列表return_list,并且定义i为每个连续相同元素的初始位置，j为截止位置

2.如果连续相同元素的长度大于等于3，则为较大分组并保存到return_list中
"""
if __name__=='__main__':
	s=Solution()
	str1="abcdddeeeeaabbbcd"
	print(s.largeGroupPositions(str1))