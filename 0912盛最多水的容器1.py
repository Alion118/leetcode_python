# -*- coding: utf-8 -*-
# @Time    : 2018/9/12 21:59
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @File    : 盛最多水的容器1.py
# @Software: PyCharm

# class Solution:
# 	def maxArea(self, height):
# 		"""
# 		:type height: List[int]
# 		:rtype: int
# 		"""
# 		temp = height.copy()
# 		start = height.index(max(height))
# 		temp[start] = 0
# 		end = temp.index(max(temp))
# 		temp_index = start
# 		start = min(start, end)
# 		end = max(temp_index, end)
#
# 		temp_h = min(height[end], height[start])
# 		max_area = min(height[end], height[start]) * (end - start)
#
# 		if height[start]>height[end]:
# 			for i in range(start):
# 				if height[i]*(end-i) > max_area:
# 					max_area = min(height[i], temp_h) * (end - i)
# 					start = i
# 					temp_h = min(height[end], height[start])
# 		else:
# 			for j in range(end + 1, len(height)):
# 				if min(height[j], height[start])*(j-start) > max_area:
# 					max_area = min(height[j], height[start]) * (j - start)
# 		return max_area
#
#
# s = Solution()
# print(s.maxArea([8,10,14,0,13,10,9,9,11,11]))
class Solution(object):
	def maxArea(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		l = 0
		r = len(height) - 1
		if not height or len(height) == 1:
			return 0
		res = (r - l) * (height[l] if height[l] < height[r] else height[r])

		while l < r:
			if height[l] < height[r]:
				l += 1
			else:
				r -= 1
			res=max(res,min(height[r],height[l])*(r-l))
		return res
s=Solution()
print(s.maxArea([8,10,14,0,13,10,9,9,11,11]))

