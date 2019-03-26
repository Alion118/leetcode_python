# -*- coding: utf-8 -*-
# @Time    : 2019/3/26 16:36
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
class Solution:
	def replaceWords(self, dict: [str], sentence: str) -> str:
		sen_lst=sentence.split(' ')
		i=0
		for word in sen_lst:
			temp=sen_lst[i]
			for d in dict:
				if word.startswith(d):
					temp=d
					break
			sen_lst[i] = temp
			i+=1
		return ' '.join(sen_lst)

print(Solution().replaceWords(dict=['a','b','c'],sentence="aadsfasf absbs bbab cadsfafs"))
