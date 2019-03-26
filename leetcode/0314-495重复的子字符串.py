# -*- coding: utf-8 -*-
# @Time    : 2019/3/14 16:59
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for l in range(1,len(s)//2+1):
            if s[:l] * (len(s)//l) == s:
                return True
        return False

print(Solution().repeatedSubstringPattern(s='abac'))





