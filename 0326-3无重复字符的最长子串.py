# -*- coding: utf-8 -*-
# @Time    : 2019/3/26 17:15
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		if s =='':
			return 0
		out=[1]
		temp = ''
		for si in s:
			if si not in temp:
				temp+=si
			else:
				start=temp.index(si)+1
				if temp!='':
					out.append(len(temp))
				temp=temp[start:] if len(temp)-start>0 else ''
				temp+=si
		out.append(len(temp))
		return max(out)
print(Solution().lengthOfLongestSubstring('dvdf'))
