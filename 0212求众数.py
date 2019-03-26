# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 21:40
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt, ret = 0, 0
        for num in nums:
            if cnt == 0:
                ret = num
            if num != ret:
                cnt -= 1
            else:
                cnt += 1
        return ret
print(Solution().majorityElement())
# 题目定义元素个数大于n/2的才为众数，故[2,3,1,3,4]不符合列表，没有众数