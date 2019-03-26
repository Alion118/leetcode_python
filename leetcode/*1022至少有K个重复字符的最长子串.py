# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 15:23

# 目前处理子串的方法有：
#
# （1）双指针；
#
# （2）dp；
#
# （3）分治；
# 分治法如下：
import numpy as np


class Solution(object):
	def longestSubstring(self, s, k):
		"""
		:type s: str
		:type k: int
		:rtype: int
		"""

		def longestSubstringHelper(s, k, start, end):
			count = [0] * 26
			for i in range(start, end):
				count[ord(s[i]) - ord('a')] += 1
			max_len = 0
			i = start
			while i < end:
				while i < end and count[ord(s[i]) - ord('a')] < k:
					i += 1
				j = i
				while j < end and count[ord(s[j]) - ord('a')] >= k:
					j += 1

				if i == start and j == end:
					return end - start

				max_len = max(max_len, longestSubstringHelper(s, k, i, j))
				i = j
			return max_len

		return longestSubstringHelper(s, k, 0, len(s))
# LeetCode运行显示超时
class Solution1:
	def longestSubstring(self, s, k):
		"""
		:type s: str
		:type k: int
		:rtype: int
		"""
		return Solution().helper(s,0,len(s),k)

	def helper(self,s,beg,end,k):
		if end-beg<k:
			return 0
		cnt=np.zeros(26)
		for i in range(beg,end):
			cnt[ord(s[i])-ord('a')]+=1
		for i in range(26):
			if cnt[i] and cnt[i]<k:
				for j in range(beg,end):
					if s[j]==chr(i+ord('a')):
						return max(Solution().helper(s,beg,j,k),Solution().helper(s,j+1,end,k))
		return end-beg

if __name__=='__main__':
	s='abbcadda'
	k=2
	print(Solution().longestSubstring(s,k))
