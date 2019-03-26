# -*- coding: utf-8 -*-
class Solution:
	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: List[str]
		:rtype: bool
		"""
		if not s:
			return True

		breakp = [0]

		for i in range(len(s) + 1):
			for j in breakp:
				if s[j:i] in wordDict:
					breakp.append(i)
					break
		return breakp[-1] == len(s)

print(Solution().wordBreak(s='catsandog',wordDict=['cats','dog','sand','and','cat']))