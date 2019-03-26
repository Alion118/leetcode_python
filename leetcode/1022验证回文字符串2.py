# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 21:03
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
class Solution:
	def validPalindrome(self,s):
		def ispalindrome(s,start,end,count):
			if count>1:
				return False
			while start<end:
				if s[start]!=s[end]:
					break
				start+=1
				end-=1
			if start==end or start==end+1:
				return True
			return ispalindrome(s,start+1,end,count+1) or ispalindrome(s,start,end-1,count+1)

		return ispalindrome(s,0,len(s)-1,0)

	def validPalindrome_my(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		start=0
		end=len(s)-1
		flag=1
		t=0 # 仅去掉一个字符

		while start<=end:
			if s[start]!=s[end]:
				if t==0:
					if s[start+1]==s[end]:
						start=start+1
					else:
						flag=0
				else:
					flag=0
				t+=1
			start+=1
			end-=1

		start = 0
		end = len(s) - 1
		t = 0  # 仅去掉一个字符
		if flag:
			return bool(flag)
		else:
			flag=1

		while start <= end:
			if s[start] != s[end]:
				if t == 0:
					if s[start] == s[end - 1]:
						end = end - 1
					else:
						flag = 0
				else:
					flag = 0
				t += 1
			start += 1
			end -= 1
		return bool(flag)


if __name__=='__main__':
	s='cupuupuupucu'
	print(Solution().validPalindrome(s))