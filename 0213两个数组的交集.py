# -*- coding: utf-8 -*-
# @Time    : 2019/2/15 16:20
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1)&set(nums2))

print(Solution().intersection([1,2,3],[3,2,1,4]))