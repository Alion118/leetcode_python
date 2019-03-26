# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 19:39
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm

# 转移方程：1，如果str1(m)==str2(n)，那么L(m,n)=L(m-1,n-1)+1。2，如果str1(m)!=str2(n)，那么L(m,n)=max(L(m-1,n),L(m,n-1))
#
# 解释一下，假如m和n相等，那么这个时候最长子序列无疑是前一个L(m-1,n-1)加上1，因为这两个字符串这个地方的字符都可以加入到最长子序列里面去。如果不相等，那么要么舍弃新来的来自str1的那个字符m号，要么舍弃str2的n号字符（最长子序列每个位置上当然都是唯一确定的一个字符），舍弃之后呢，就从
#
# L(m-1,n),L(m,n-1)当中挑一个好的（能更长的）为当前状态的最长子序列。
class Solution:

	def getRemoveNumber(self,s):
		lst=list(s)
		lst2=list(s)
		lst.reverse()
		l=len(lst)
		temp=[[0 for i in range(l+1)] for i in range(l+1)]
		for i in range(l):
			for j in range(l):
				if lst[i]==lst2[j]:
					temp[i+1][j+1]=temp[i][j]+1
				else:
					temp[i + 1][j + 1] = max(temp[i][j+1],temp[i+1][j])
		return l-temp[l][l]


s=input()
#s='zgtklhfzomzjckwmluvivvcmhjrwkuvcjrxojobpdedpamdshcwwsetfbacvonecrdvugeibglvhxuymjvoryqjwullvzglqazxrdmczyvbgakjagttrezmvrlptiwoqkrtxuroeqmryzsgokopxxdpbejmtwvpnaqrgqladdszhdwxfckmewhdvihgvacueqhvwvjxoitlpfrckxkuksaqzjpwgoldyhugsacflcdqhifldoaphgdbhaciixouavqxwlghadmfortqacbffqzocinvuqpjthgekunjsstukeiffjipzzabkuiueqnjgkuiojwbjzfynafnlcaryygqjfixaoeowhkxkbsnpsvnbxuywfxbnuoemxynbtgkqtjvzqikbafjnpbeirxxrohhnjqrbqqzercqcrcswojyylunuevtdhamlkzqnjrzibwckbkiygysuaxpjrgjmurrohkhvjpmwmmtpcszpihcntyivrjplhyrqftghglkvqeidyhtmrlcljngeyaefxnywpfsualufjwnffyqnpitgkkyrbwccqggycrvoocbwsdbftkigrkcbojuwwctknzzmvhbhbfzrqwzllulbabztqnznkqdyoqnrxhwavqhzyzvmmmphzxbikpharseywpfsqyybkynwbdrgfsaxduxojcdqcjuaywzbvdjgjqtoffasiuhvxcaockebkuxpiomqmtvsqhnyxfjceqevqvnapbk '
print(Solution().getRemoveNumber(s))
