# -*- coding: utf-8 -*-
# @Time    : 2019/3/19 15:22
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
class Solution:
	def findWord(self,s,word):
		i=0
		num=0
		for w in word:
			while i<len(s):
				if s[i]==w:
					num+=1
					i += 1
					break
				i+=1
		if num==len(word):
			return True
		else:
			return False

	def findLongestWord(self, s: str, d:[str]) -> str:
		max_word=''
		for word in d:
			if self.findWord(s,word):
				if len(word)>len(max_word):
					max_word=word
				elif len(word)==len(max_word):
					max_word=word if word<max_word else max_word
		return max_word

print(Solution().findWord('bab','ba'))
print(Solution().findLongestWord('bab',d=['ba','ab','a','b']))